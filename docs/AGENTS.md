# AGENTS.md — ACS Consciousness Paper

## Mission

Develop the repository manuscript into a rigorous, self-contained conceptual foundation paper on embodied cognition and consciousness.

The target for the next milestone is **v0.2**: a substantially expanded and improved version of the current paper, while preserving its strongest features:

- cautious scientific tone;
- explicit relation to existing theories;
- operationalized and falsifiable predictions;
- separation between mechanistic, empirical, and ontological claims;
- ability to stand independently of unfinished simulations and companion AI work.

The paper should present a unified research programme connecting:

1. self-stabilizing embodied cognition;
2. hierarchical abstraction through invariants;
3. activation-correlation structures (ACS);
4. dynamic homeostasis;
5. metastable neural and physical organization;
6. electromagnetic field organization as a manifestation of organized electrical dynamics;
7. consciousness as the intrinsic or ontological realization of a qualifying physical organization;
8. the language-game and continuum problems surrounding qualia;
9. experimentally testable neuroscience and artificial-agent predictions.

Do not reduce the paper to predictive processing, active inference, electromagnetic-field theory, IIT, enactivism, or Russellian monism. The manuscript should explain where it overlaps with each and what the proposed synthesis adds.

## Repository inspection

Before editing:

1. Inspect the full repository tree.
2. Identify the authoritative Markdown manuscript, LaTeX manuscript, bibliography, generated DOCX/PDF outputs, build scripts, and version conventions.
3. Read the complete current manuscript before changing its structure.
4. Preserve useful citations and references from the existing version.
5. Never edit generated DOCX or PDF files as the primary source.

If no source-of-truth convention exists, use Markdown as the conceptual master and LaTeX as the publication master:

- Markdown for readable drafting and semantic review.
- LaTeX for equations, cross-references, bibliography, and final PDF.
- DOCX and PDF as generated artifacts.

Document this convention in the repository README.

## Required v0.2 deliverables

Produce and keep synchronized:

- `Embodied_Consciousness_Framework_v0.2.md`
- `Embodied_Consciousness_Framework_v0.2.tex`
- `Embodied_Consciousness_Framework_v0.2.docx`
- `Embodied_Consciousness_Framework_v0.2.pdf`
- `references.bib`, if not already present
- a ZIP containing the four manuscript formats and bibliography
- a concise `CHANGELOG.md` entry

Use existing filenames and directory conventions when established. Do not create needless duplicate trees.

The four manuscript formats must contain the same substantive sections, claims, equations, predictions, limitations, and references.

## Target scope

The v0.2 paper must be a meaningful intermediate manuscript, not an outline or placeholder.

Recommended length:

- approximately 15–25 journal-style pages;
- roughly 8,000–13,000 words, excluding references;
- long enough to develop the distinctive theory;
- short enough to remain a focused conceptual foundation paper.

Do not inflate length through repetition, generic literature review, or broad descriptions of consciousness.

## Central thesis

Develop the following chain:

> An embodied cognitive system continually stabilizes perception-action relations under internal and external perturbation. Repeated stabilization at different spatial and temporal scales produces hierarchically organized invariants. The evolving organization is best characterized through multiscale activation-correlation structures rather than isolated activity values. In biological nervous systems, these organized electrical dynamics necessarily have coherent electromagnetic manifestations. Conscious experience is hypothesized to be identical not with a separate observer, substance, computation, or electromagnetic field considered independently, but with the intrinsic existence of a qualifying self-stabilizing physical organization and its dynamically maintained internal world.

This is a hypothesis and research programme, not an established result.

Keep three epistemic levels distinct:

1. **Mechanistic proposal:** how self-stabilizing embodied cognition may operate.
2. **Empirical hypothesis:** which ACS and physical signatures correlate with conscious organization.
3. **Ontological proposal:** why the qualifying organization may be identical with subjective existence.

Do not treat evidence for one level as automatic proof of another.

## Required conceptual expansions

### 1. Self-stabilizing embodied cognition

Expand the mechanistic theory well beyond the current treatment.

Explain cognition as active stabilization of coupled organism-environment dynamics, not passive input encoding.

Include:

- closed perception-action loops;
- perturbations from environment, body, action, and internal activity;
- stabilization as a functional process rather than static equilibrium;
- multiple compatible metastable states;
- continuous adjustment rather than permanent convergence;
- relations among perception, action, prediction, control, and correction;
- determinate perceptual organization without an inner observer;
- maintenance of viable relations with the world.

Clarify that prediction-error minimization and free-energy minimization may implement stabilization but are not assumed to be its only formalization.

Avoid claiming that action is required for every momentary conscious state. The stronger claim is developmental and organizational: the relevant architecture is formed and maintained through closed embodied coupling, even when a particular episode is temporarily decoupled from overt action, as in imagery or dreaming.

### 2. Dynamic homeostasis

Add a dedicated subsection distinguishing dynamic homeostasis from static constancy.

Dynamic homeostasis should describe maintenance of neural and bodily variables within functional regimes while preserving enough variability to encode information and reorganize.

Explain why this matters:

- permanent saturation destroys representational sensitivity;
- permanent depression or silence destroys functional differentiation;
- cognition requires bounded activity, recoverability, and ongoing variation;
- local adaptation and global regulation must coexist;
- stability must preserve the capacity for future change.

Where supported, connect this to homeostatic plasticity, excitation-inhibition balance, allostasis, interoception, and viability regulation. Do not claim equivalence without evidence.

### 3. Hierarchical abstraction through invariant pickup

Develop the mechanism by which increasingly abstract representations emerge:

1. fast, local patterns stabilize over short intervals;
2. repeated regularities survive variation and perturbation;
3. higher levels become sensitive to features stable across lower-level changes;
4. deeper or slower dynamics encode increasingly invariant relations;
5. abstractions become histories of successful stabilization across transformations.

Use examples such as edges, objects, places, affordances, agents, social situations, self-models, and abstract concepts.

Do not imply that hierarchy must correspond directly to anatomical depth. It may involve spatial scale, temporal scale, recurrent depth, causal organization, or combinations of these.

### 4. Internal physical worlds

Make this a central section rather than a brief metaphor.

The nervous system does not construct a miniature picture viewed by an internal spectator. It maintains a physically instantiated, dynamically organized world of relations shaped by organism-environment interaction.

Develop the claim that this internal world is:

- physically instantiated;
- causally active;
- constrained by external reality;
- partly autonomous through recurrence, memory, and prediction;
- organized across multiple timescales;
- centered on the organism's body, actions, and viability;
- continuously maintained rather than statically stored.

State clearly:

> The conscious subject is not an additional entity observing the internal world. The proposal is that the subject and experienced world are aspects of the ongoing existence of that organized physical process.

Treat this as the paper's central identity hypothesis, not as an established conclusion.

## Activation-Correlation Structures

### Role of ACS

ACS must become the central mesoscopic dynamical object of the framework, not merely a convenient measurement.

Use ACS to bridge microscopic neural events, population dynamics, large-scale coordination, metastable cognitive states, behavior, phenomenological transitions, and measurable EM manifestations.

Define ACS as a time-evolving, multiscale relational structure that may include:

- pairwise and lagged correlations;
- phase synchrony;
- directed or causal dependencies;
- recurrence;
- higher-order interactions;
- community structure;
- integration and segregation;
- cross-frequency relationships;
- temporal persistence and transition structure.

Do not imply that simple Pearson correlation matrices are sufficient. They are an initial operationalization.

### Minimal formalism

Let neural or physical population state be:

```math
x(t) \in \mathbb{R}^{n}.
```

Define a family of windowed relational operators:

```math
C_{\tau}^{(m)}(t)
=
\mathcal{R}^{(m)}
\left(
x(t') : t' \in [t-\tau,t]
\right),
```

where `tau` is the observation timescale, `m` identifies the relational measure, and `R^(m)` may represent correlation, lagged mutual information, phase coupling, transfer entropy, recurrence, or a higher-order estimator.

Define the multiscale ACS as:

```math
\mathcal{A}(t)
=
\left\{
C_{\tau}^{(m)}(t)
\right\}_{\tau \in T,\,m \in M}.
```

A metastable episode may be described by relatively slow deformation:

```math
D\!\left(\mathcal{A}(t+\Delta t),\mathcal{A}(t)\right) < \varepsilon
```

for a finite dwell interval, where `D` is a suitable distance over relational structures. Transitions involve a transient increase in structural change.

The formalism must remain provisional:

- several choices of relational operator and distance are possible;
- different modalities require different estimators;
- ACS is a research construct, not yet a uniquely defined invariant;
- the computational companion paper must compare operationalizations.

### ACS as state space

Explain carefully that saying cognition evolves in ACS space is a modelling claim: some cognitive regularities may be more naturally captured by trajectories through relational organization than by trajectories of isolated activation values.

Do not say neurons are unimportant. ACS supervenes on and is implemented by physical neural activity.

### ACS quality dimensions

Introduce candidate dimensions without collapsing them into a single scalar:

- coherence;
- differentiation;
- integration;
- modularity;
- recurrence;
- hierarchical depth;
- multiscale persistence;
- transition richness;
- controllability;
- embodiment or sensorimotor closure;
- robustness under perturbation;
- adaptability after perturbation.

Do not invent a consciousness score in v0.2. Use a multidimensional profile.

## Electromagnetic organization

Preserve the distinction between this framework and CEMI-style theories.

Core position:

- neural activity consists of ionic and electrical currents;
- organized currents necessarily generate electromagnetic fields;
- coherent neural organization therefore has coherent EM manifestations;
- EEG, MEG, local field potentials, and related measures capture partial projections;
- the EM field is not currently posited as an independently consciousness-producing substance;
- the ontologically relevant entity is the complete organized physical process, not a field abstracted from its generators.

Preferred wording:

> Coherent electromagnetic organization is the most directly measurable macroscopic manifestation of coordinated electrical dynamics, not necessarily an independently causal or sufficient substrate of consciousness.

Avoid overstating background thermal noise unless directly supported.

Do not claim that EM perturbation can leave generating ACS completely unchanged. Reformulate the empirical contrast in terms of mediation and residual effects:

- Does the effect of EM perturbation on conscious content disappear once changes in neural ACS are accounted for?
- Or do field-level variables predict additional effects not mediated by measurable changes in the generating neural organization?

## Ontology and the hard problem

Expand the ontology section while remaining explicit about what is and is not solved.

Develop this reasoning:

1. Physicalist neuroscience usually asks why neural processes generate experience.
2. The framework proposes identity rather than production.
3. A qualifying organized physical world does not create a second thing called experience.
4. Its intrinsic existence is hypothesized to be the subjective aspect.
5. The residual question becomes why organized existence has an intrinsic aspect at all.
6. This maps the hard problem onto the broader ontological question of existence.

Use the central idea:

> Asking why qualia exist may ultimately be comparable to asking why spacetime, fields, matter, or existence itself exist.

Add the cautions:

- this relocates rather than deductively solves the hard problem;
- it belongs near Russellian-monist and identity-theoretic families;
- the distinctive contribution is the restricted mechanistic route from embodied stabilization to qualifying organization;
- the restriction to certain organizations still needs principled justification.

Do not claim novelty for the ontological move itself. Potential novelty lies in the combination of embodied self-stabilization, dynamic homeostasis, hierarchical invariants, multiscale ACS, EM manifestation without EM-substrate identity, internal physical worlds, a restricted identity claim, and operational predictions.

Do not claim the combination problem is solved by construction. The restriction creates a qualification problem: why do some organizations qualify and others not?

## Qualia, language games, and the long spectrum

Expand this section substantially.

### Language-game thesis

Language uses categories such as conscious/unconscious, experience/no experience, red/not red, pain/no pain, and self/non-self. These distinctions are pragmatically useful but need not map to sharp natural boundaries.

Explain that language can force binary predicates onto continuous, multidimensional, or family-resemblance phenomena.

Do not claim linguistic analysis proves consciousness is continuous. The continuity argument must come independently from the graded organization of the proposed mechanisms.

### Long-spectrum view

Develop consciousness as a potentially long, multidimensional spectrum extending across:

- ordinary waking states;
- attention and inattention;
- dreaming;
- sedation and anesthesia;
- disorders of consciousness;
- infants and developing organisms;
- non-human animals;
- simple nervous systems;
- neural cultures and organoids;
- future embodied artificial systems;
- hypothetical minimal qualifying physical organizations.

Avoid asserting that all these systems are conscious.

The framework replaces a premature yes/no judgment with empirical questions concerning the kind, degree, organization, and temporal stability of internal physical worlds.

Distinguish:

- level or presence;
- richness of content;
- selfhood;
- temporal continuity;
- reportability;
- access;
- valence;
- moral relevance.

Do not collapse these dimensions.

### Qualia transitions

Use color experience as an example:

- red → orange → yellow may correspond to continuous but structured ACS transformations;
- cross-individual commonalities may be detectable at a relational level despite anatomical and autobiographical variation;
- such patterns would be signatures or correlates, not proof that an artificial system has identical experience.

Do not claim matching one neural pattern is sufficient for identical qualia.

## Comparisons with existing theories

Retain and improve the comparison table.

At minimum compare with:

- Global Neuronal Workspace;
- Integrated Information Theory;
- Recurrent Processing Theory;
- Predictive Processing;
- Active Inference;
- Enactivism;
- coordination dynamics and metastability;
- CEMI and other EM-field theories;
- Biological Naturalism and Anil Seth's beast-machine view;
- Russellian monism;
- identity theory;
- process philosophy, only if used carefully and with references.

For every comparison specify:

1. shared ground;
2. precise divergence;
3. evidence that could separate the views;
4. whether the difference is mechanistic, empirical, conceptual, or ontological.

Do not caricature neighboring theories.

## Experimental programme

Expand the experimental section into coherent research lines.

### Programme A — Stable percepts and transitions

Test whether multiscale ACS features predict perceptual stabilization, bistable transitions, masking, near-threshold detection, binocular rivalry, temporal integration, and confidence.

Compare ACS models with firing rate or amplitude, anatomy, spectral power, standard connectivity, and behavioral variables. Use held-out, cross-subject, and cross-dataset validation.

### Programme B — Qualia-related relational signatures

Study structured transitions such as red → orange → yellow, pitch or timbre gradients, tactile intensity, pain quality, and body-state transformations.

Test within-subject reproducibility, cross-subject relational alignment, invariance across context, and differences between sensory similarity and linguistic labeling.

Call these candidate organizational correlates or physical signatures, not the qualia itself.

### Programme C — Consciousness level

Compare ACS profiles across wakefulness, REM and non-REM sleep, anesthesia, sedation, seizures, coma, disorders of consciousness, meditation, and psychedelic states where appropriate.

Relate ACS measures to independent indices such as perturbational complexity, behavioral responsiveness, and clinical outcome.

### Programme D — Lesions and reversible perturbations

Study how damage or transient inhibition changes multiscale organization, stability, transition structure, content, global level, recovery, and compensation.

Avoid simplistic one-region/one-qualia assumptions.

### Programme E — Neural culture and organoid systems

Propose progressively structured systems:

1. spontaneous cultures;
2. patterned input;
3. closed-loop stimulation;
4. differentiated sensory-like input layers;
5. embodied robotic coupling;
6. adaptive homeostatic control.

Ask when systems show robust metastability, perturbation recovery, hierarchical invariants, action-dependent stabilization, and multiscale ACS organization.

Do not claim organoid consciousness.

### Programme F — Minimal physical organization

Compare excitable chemical media, coupled oscillators, neuromorphic circuits, recurrent analog networks, active matter, and biological collectives.

The purpose is to clarify distinctive properties, not prematurely label systems conscious.

### Programme G — Artificial embodied agents

Compare agents with and without closed loops, persistent state, homeostatic variables, multi-timescale recurrence, hierarchical invariant learning, and local/global stabilization.

Use matched parameter counts and controlled environments. Assess object permanence, transfer, robustness, adaptation, self-maintenance, representation geometry, and ACS-like organization.

Behavioral performance alone is insufficient to infer consciousness.

## Predictions

Every prediction must specify dataset or paradigm, independent variable, dependent measure, baseline, statistical comparison, expected direction, disconfirming outcome, and theory-specificity.

Recommended v0.2 predictions:

### P1 — ACS adds predictive value

Multiscale ACS features should predict trial-level conscious perception beyond amplitude, rate, spectral power, and anatomical features.

Disconfirmation: no reproducible out-of-sample incremental value across suitable datasets.

### P2 — Cross-subject relational convergence

Matched perceptual organization should exhibit greater cross-subject alignment in relational ACS space than in raw activation space after reasonable anatomical alignment.

Disconfirmation: relational features do not improve reproducibility or generalization.

### P3 — Hierarchical depth tracks invariant cognition

Tasks requiring generalization across transformations should recruit ACS structures stable across longer timescales and perturbations.

Disconfirmation: invariant performance is consistently explained without such multiscale persistence.

### P4 — Dynamic homeostasis is necessary for sustained flexible encoding

Models lacking adaptive regulation should more often collapse into saturation, silence, or unstable activity and generalize less robustly than matched regulated models.

Disconfirmation: homeostatic mechanisms provide no robust benefit or predicted signatures do not arise.

### P5 — Consciousness level relates to a multidimensional ACS profile

Independent measures of consciousness level should covary with an ACS profile involving persistence, differentiation, recurrence, and multiscale coordination, not necessarily a single scalar.

Disconfirmation: the profile fails to generalize across sleep, anesthesia, and clinical datasets.

### P6 — Field effects are mediated by organized neural dynamics

Effects of external EM perturbation on conscious content should be statistically mediated by measurable changes in neural ACS under the manifestation view.

Evidence favoring independent causal-field theories: reproducible residual conscious effects predicted by field-level variables after sufficiently sensitive ACS measurement and mediation analysis.

### P7 — Embodied stabilization precedes broad task optimization

Closed-loop self-stabilizing agents should acquire transferable invariant organization before maximal benchmark performance, unlike matched feed-forward or open-loop controls.

Disconfirmation: no reproducible ordering or advantage.

Do not imply that confirmation proves the ontological identity thesis. The predictions primarily test mechanistic and empirical layers.

## Artificial intelligence and PRAttention

Keep the AI section subordinate to the paper's main purpose.

### Current AI

State cautiously:

- current language models exhibit complex internal dynamics and learned representations;
- most deployed systems lack persistent embodied loops, organism-like viability regulation, and continuously self-maintained internal worlds;
- behavioral sophistication alone is insufficient under this framework to infer consciousness;
- the framework does not prove current AI is unconscious.

### Future AI

Identify relevant design principles:

- persistent recurrent state;
- environmental coupling;
- sensorimotor closure;
- self-maintenance variables;
- dynamic homeostasis;
- multi-timescale memory;
- hierarchical invariant pickup;
- endogenous goals constrained by viability;
- ACS monitoring and perturbation analysis.

### PRAttention

Present PRAttention only as a possible engineering bridge:

- standard attention performs context-dependent binding;
- PRAttention introduces explicit references and progressive retrieval;
- this can extend effective context and support persistent referential structure;
- it may approximate one component of hierarchical world maintenance;
- it is not by itself a theory or implementation of consciousness;
- it remains closer to deep-learning engineering than full self-stabilizing embodied cognition.

Detailed architecture belongs in a companion paper.

## Structure for v0.2

Use a structure close to:

1. Abstract
2. Introduction
3. Scope, claims, and epistemic levels
4. Cognition as self-stabilizing embodied dynamics
   1. perception as stabilization
   2. action and sensorimotor closure
   3. perturbation and metastability
   4. dynamic homeostasis
   5. hierarchical invariant formation
   6. internal physical worlds
5. Activation-Correlation Structures
   1. motivation
   2. formal definition
   3. multiscale ACS space
   4. metastable trajectories
   5. candidate measures and limitations
6. Electromagnetic manifestation of organized dynamics
7. Consciousness as ontological realization
8. Qualia, language games, and the long spectrum
9. Mapping the hard problem onto ontology
10. Particle and field analogies: scope and limits
11. Relation to existing theories
12. Experimental programme
13. Operationalized predictions
14. Artificial intelligence and PRAttention
15. Objections, alternatives, and limitations
16. Research programme and companion papers
17. Conclusion
18. References

Adapt to the existing manuscript where beneficial.

## Objections that must be addressed

Include a serious objections section covering at least:

1. redescription objection;
2. boundary or qualification objection;
3. sufficiency versus correlation;
4. observer-relative scale and variable selection;
5. multiple realizability and biological specificity;
6. dreaming and paralysis;
7. feed-forward consciousness;
8. EM epiphenomenon;
9. combination, decomposition, and subject unity;
10. causal closure and scientific usefulness of identity claims;
11. language-game continuity versus phenomenal continuity;
12. AI behavioral imitation without experience.

Do not pretend all objections are resolved. Mark responses, open problems, and companion-paper tasks separately.

## Scientific and philosophical style

Write in clear academic English.

Preferred tone:

- ambitious but restrained;
- explicit about hypotheses;
- precise about novelty;
- constructive toward related theories;
- readable across neuroscience, cognitive science, AI, and philosophy.

Avoid:

- `obviously`;
- `definitively`;
- `proves consciousness`;
- `solves the hard problem`;
- `qualia are just...`;
- categorical claims that all current AI is unconscious;
- rhetorical attacks on mainstream theories;
- inflated claims of revolution or paradigm change.

Use terminology consistently:

- **consciousness**, not `conscience`, in English;
- **activation-correlation structure (ACS)** on first use;
- **self-stabilizing**;
- **multiscale**;
- **metastable**;
- **perception-action loop**;
- **dynamic homeostasis**;
- **internal physical world**;
- **ontological realization** and **intrinsic existence**, with definitions.

Do not use `conscious experience` when discussing mere report or access unless the distinction is explicit.

## Citation and research rules

Never invent citations, DOIs, page numbers, datasets, quotations, or results.

Before adding a factual claim:

1. locate a suitable source;
2. verify the source supports the claim;
3. add it to the bibliography;
4. cite it in the relevant paragraph.

Prefer peer-reviewed papers, primary research, major scholarly books, and authoritative reviews.

Expand references selectively in enactivism, sensorimotor theory, coordination dynamics, metastability, homeostatic plasticity, allostasis, recurrent processing, synchrony, dynamic connectivity, representational similarity, inter-subject alignment, perturbational complexity, disorders of consciousness, anesthesia, EM-field theories, active inference, interoception, Russellian monism, identity theories, graded consciousness, organoid ethics, closed-loop cultures, and embodied robotics.

Add a bibliography validation step:

- compile LaTeX with warnings visible;
- check unresolved citations;
- check duplicate bibliography keys;
- ensure Markdown and LaTeX citations match;
- avoid long direct quotations.

## Figures

For v0.2, include figure placeholders or simple vector diagrams when feasible:

1. mechanistic chain;
2. ACS hierarchy and metastable transitions;
3. multidimensional long spectrum;
4. theory-comparison matrix;
5. experimental programme.

Figures must remain scientifically neutral and must not present speculative entities as established facts.

Prefer SVG, PDF, or TikZ source under version control.

## Build and synchronization

Create or improve reproducible build tooling.

Preferred commands:

```bash
make md
make tex
make pdf
make docx
make all
make package
```

Equivalent scripts are acceptable.

Requirements:

- clean build from a fresh checkout;
- generated artifacts in `dist/` or `build/`;
- no machine-specific absolute paths;
- avoid proprietary dependencies;
- PDF from LaTeX where possible;
- DOCX through Pandoc or a documented equivalent;
- consistent metadata across formats.

Update `.gitignore` for temporary LaTeX artifacts.

## Conversion checks

Verify the same title, version, abstract, section order, equations, predictions, references, tables, and figures in all formats.

### Markdown

- valid heading hierarchy;
- readable equations;
- no unnecessary renderer-breaking raw LaTeX.

### LaTeX

- compiles without fatal errors;
- no materially damaging overfull boxes;
- equations and references resolve;
- bibliography renders;
- Unicode is handled.

### DOCX

- headings use styles;
- equations are readable;
- tables fit;
- references are intact;
- no duplicated title or abstract.

### PDF

Inspect every page visually for clipping, missing glyphs, unexpected blanks, page numbering, and figure legibility.

## Version discipline

Use manuscript milestones:

- v0.1: current Claude revision or imported baseline;
- v0.2: expanded conceptual and mechanistic manuscript;
- v0.3: literature and formalism strengthening;
- v0.4: figures and empirical-design refinement;
- v0.5: external-review revision;
- v1.0: submission candidate.

Do not silently overwrite a milestone.

For each milestone preserve source history, create a release ZIP, update `CHANGELOG.md`, and record unresolved issues.

## Work sequence for Codex

### Phase 1 — Repository audit

- inspect files and build system;
- identify the baseline manuscript;
- note inconsistencies among formats;
- create `docs/v0.2-audit.md`.

### Phase 2 — Structural revision

- create the v0.2 Markdown source;
- restructure sections;
- preserve strong baseline material;
- add evidence placeholders rather than inventing support.

### Phase 3 — Mechanistic expansion

- expand embodied stabilization;
- add dynamic homeostasis;
- deepen hierarchical invariants;
- expand internal physical worlds.

### Phase 4 — ACS formalism

- add multiscale definitions;
- distinguish construct from estimators;
- clarify metastability and state-space language;
- revise measurable predictions.

### Phase 5 — Philosophy and ontology

- expand ontological identity;
- expand language-game analysis;
- develop the long-spectrum view;
- add objections and limitations.

### Phase 6 — Empirical programme and AI

- expand experiments;
- revise the EM perturbation prediction;
- add cultures, organoids, minimal systems, and embodied AI;
- include restrained PRAttention discussion.

### Phase 7 — Citation audit

- verify every new scientific claim;
- update bibliography;
- remove unsupported or overstated claims.

### Phase 8 — Format generation

- synchronize LaTeX;
- generate DOCX and PDF;
- inspect outputs;
- package the release ZIP.

### Phase 9 — Final report

Create `docs/v0.2-completion-report.md` listing changed files, conceptual changes, references, build commands, limitations, and proposed v0.3 tasks.

## Definition of done for v0.2

v0.2 is complete only when:

- the manuscript is a substantial paper, not a plan;
- cognition theory is clearly more developed than v0.1;
- dynamic homeostasis is integrated;
- ACS is the central relational dynamical construct;
- ontology and mechanism remain distinguished;
- qualia/language-game and spectrum arguments are expanded;
- the EM claim is accurately separated from CEMI;
- predictions are operationalized and disconfirmable;
- AI discussion is cautious and PRAttention is only a bridge;
- objections and limitations are serious;
- all citations are real and verified;
- MD, TEX, DOCX, and PDF are synchronized;
- PDF and DOCX are visually checked;
- a downloadable release ZIP exists.

## Non-goals for v0.2

Do not:

- claim experimental validation;
- present simulation results that have not been run;
- claim a unique mathematical definition of consciousness;
- produce a universal consciousness scalar;
- claim identical ACS implies identical qualia;
- claim EM fields are independently sufficient;
- claim Russellian monism has been proven;
- classify current AI, organoids, insects, or simple physical systems definitively;
- bury limitations;
- expand the manuscript into an unfocused book chapter.

Move detailed computational models, simulation results, PRAttention architecture, and full protocols into companion-paper plans.

## Research programme beyond v0.2

Maintain a backlog for:

1. **Self-Stabilizing Embodied Cognition** — local learning rules, homeostasis, hierarchy formation.
2. **Activation-Correlation Structures** — estimator comparison, graph and information measures, neural-data pipelines.
3. **Computational Experiments** — embodied agents, perturbations, controls, invariant structure.
4. **Experimental Neuroscience** — preregisterable protocols, public datasets, alignment, anesthesia, clinical states.
5. **Artificial Intelligence** — PRAttention, persistent referential state, self-stabilizing agents, ethical inference.
6. **Ontology and Philosophy** — qualification criteria, unity, intrinsic existence, identity theory, Russellian monism.

The v0.2 foundation paper should point toward these projects without depending on their completion.
