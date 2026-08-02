"""Reproducible build and validation for the v0.2 manuscript."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pypandoc


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BUILD = ROOT / "build"
DIST = ROOT / "dist"
STEM = "Embodied_Consciousness_Framework_v0.2"
MD = DOCS / f"{STEM}.md"
TEX = DOCS / f"{STEM}.tex"
DOCX = DOCS / f"{STEM}.docx"
PDF = DOCS / f"{STEM}.pdf"
BIB = DOCS / "references.bib"
FIG_SCRIPT = ROOT / "scripts" / "generate_figures.py"


def run(command: list[str], cwd: Path = ROOT) -> None:
    print("+", " ".join(str(part) for part in command))
    subprocess.run(command, cwd=cwd, check=True)


def validate_sources() -> None:
    for path in (MD, BIB):
        if not path.exists():
            raise FileNotFoundError(path)
    source = MD.read_text(encoding="utf-8")
    headings = re.findall(r"^(#{1,6})\s+(.+)$", source, flags=re.MULTILINE)
    last_level = 0
    for marks, title in headings:
        level = len(marks)
        if last_level and level > last_level + 1:
            raise ValueError(f"Heading level jumps before {title!r}")
        last_level = level
    cited = set(re.findall(r"(?<!\w)@([A-Za-z0-9_.:-]+)", source))
    keys = re.findall(r"^@\w+\{([^,]+),", BIB.read_text(encoding="utf-8"), flags=re.MULTILINE)
    duplicate_keys = sorted({key for key in keys if keys.count(key) > 1})
    missing = sorted(cited - set(keys))
    if duplicate_keys:
        raise ValueError(f"Duplicate bibliography keys: {duplicate_keys}")
    if missing:
        raise ValueError(f"Missing bibliography keys: {missing}")
    print(f"Validated {len(headings)} headings, {len(cited)} cited works, and {len(keys)} bibliography entries.")


def figures() -> None:
    run([sys.executable, str(FIG_SCRIPT)])


def pandoc_path() -> str:
    return pypandoc.get_pandoc_path()


def make_tex() -> None:
    validate_sources()
    figures()
    args = [
        pandoc_path(),
        MD.name,
        "--from=markdown+tex_math_dollars",
        "--to=latex",
        "--standalone",
        "--natbib",
        "--number-sections",
        "--bibliography=references.bib",
        "--resource-path=.;figures",
        "-V", "documentclass=article",
        "-V", "fontsize=11pt",
        "-V", "geometry:margin=1in",
        "-V", "colorlinks=true",
        "-V", "linkcolor=blue",
        "-V", "citecolor=blue",
        "-V", "urlcolor=blue",
        "-V", "papersize=a4",
        "-o", TEX.name,
    ]
    run(args, DOCS)
    content = TEX.read_text(encoding="utf-8")
    content = content.replace(".png}", ".pdf}")
    marker = "\\begin{document}\n\\maketitle"
    status = (
        "\\begin{center}\\small\\textbf{Status:} Conceptual foundation paper, version 0.2. "
        "Mechanistic, empirical, and ontological claims are distinguished throughout.\\end{center}\n"
    )
    if marker in content and status not in content:
        content = content.replace(marker, marker + "\n" + status, 1)
    TEX.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {TEX}")


def make_docx() -> None:
    validate_sources()
    figures()
    args = [
        pandoc_path(),
        MD.name,
        "--from=markdown+tex_math_dollars",
        "--to=docx",
        "--standalone",
        "--citeproc",
        "--number-sections",
        "--bibliography=references.bib",
        "--resource-path=.;figures",
        "-o", DOCX.name,
    ]
    run(args, DOCS)
    print(f"Wrote {DOCX}")


def latexmk_path() -> str:
    found = shutil.which("latexmk")
    if not found:
        raise RuntimeError("latexmk is required to generate the PDF")
    return found


def make_pdf() -> None:
    make_tex()
    BUILD.mkdir(parents=True, exist_ok=True)
    for artifact in BUILD.glob(f"{STEM}.*"):
        artifact.unlink()
    run([
        latexmk_path(),
        "-g",
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        f"-outdir={BUILD}",
        TEX.name,
    ], DOCS)
    built = BUILD / f"{STEM}.pdf"
    if not built.exists():
        raise FileNotFoundError(built)
    shutil.copy2(built, PDF)
    print(f"Wrote {PDF}")


def make_all() -> None:
    make_pdf()
    make_docx()


def package() -> None:
    make_all()
    DIST.mkdir(parents=True, exist_ok=True)
    members = [MD, TEX, DOCX, PDF, BIB]
    for path in members:
        shutil.copy2(path, DIST / path.name)
    archive = DIST / f"{STEM}.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in members:
            zf.write(path, arcname=path.name)
    print(f"Wrote {archive}")


def clean() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    print(f"Removed temporary build directory {BUILD}")


def main() -> None:
    target = sys.argv[1].lower() if len(sys.argv) > 1 else "all"
    actions = {
        "md": validate_sources,
        "tex": make_tex,
        "pdf": make_pdf,
        "docx": make_docx,
        "all": make_all,
        "package": package,
        "clean": clean,
    }
    if target not in actions:
        raise SystemExit(f"Unknown target {target!r}; choose from {', '.join(actions)}")
    actions[target]()


if __name__ == "__main__":
    main()
