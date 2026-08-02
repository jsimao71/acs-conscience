# ACS Consciousness Framework

This repository develops *From Self-Stabilizing Dynamics to Conscious Experience: A Physical and Ontological Framework for Embodied Consciousness*.

## Source convention

- `docs/Embodied_Consciousness_Framework_v0.2.md` is the conceptual master.
- `docs/Embodied_Consciousness_Framework_v0.2.tex` is the generated publication master.
- DOCX and PDF files are generated artifacts and are never edited as primary sources.
- `docs/embodied_conscience.md` and `docs/embodied_conscience.tex` are preserved v0.1 baselines.

## Reproducible build

From the repository root on Windows:

```powershell
.\build.ps1 all
.\build.ps1 package
```

Individual targets are `md`, `tex`, `pdf`, `docx`, `all`, `package`, and `clean`. The build uses the Pandoc binary bundled with the Python `pypandoc` package and MiKTeX/TeX Live for PDF generation. Temporary files go to `build/`; release packages go to `dist/`.

See `docs/v0.2-audit.md` and `docs/v0.2-completion-report.md` for provenance, validation, and open work.
