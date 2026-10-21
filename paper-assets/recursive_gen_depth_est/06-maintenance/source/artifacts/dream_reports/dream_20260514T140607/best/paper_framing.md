# Paper Framing — recursive_gen_depth_est

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25, 2026)
- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)
- EMNLP 2026 special theme "New Missions for NLP Research" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit

## Core Claims (3 条)

1. **Ordinal depth estimation is feasible and accurate**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features and contrastive ordinal learning. On our benchmark, DCOL achieves significantly higher accuracy than binary detection baselines and standard classification approaches. (MVP signal: 78.2% 4-class accuracy with simple RF on Pythia chain)

2. **Depth Degradation Atlas — systematic characterization of recursive collapse**: We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) surprisal variance as the strongest depth signal, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), and (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. This atlas spans 3 model families × 3 decoding strategies.

3. **Depth-graduated curation outperforms binary filtering**: Using predicted depth as a continuous quality proxy enables more nuanced data curation — graduated weighting by depth retains high-quality shallow-generation content while down-weighting deeply recursive text, outperforming binary real/synthetic filtering on downstream task quality. (Proof-of-concept scope, ~1 page)

## Story Spine

- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer "is this synthetic?" but not "how many recursive cycles has this undergone?" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.

- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.

- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark (3 models × 3 strategies × 5+ depths), and propose DCOL — a contrastive ordinal learning method with learnable non-uniform margins that captures the actual geometry of recursive degradation. Crucially, we don't just build a classifier — we provide a Depth Degradation Atlas mapping how features evolve across depths, models, and strategies, including the EDD boundary where discrimination saturates.

- **Headline result template**: "On our multi-generational benchmark spanning 3 model families and 3 decoding strategies, DCOL achieves X% ordinal depth estimation accuracy (chance=16.7% for 6-class), with cross-model generalization accuracy of Y%, while the best binary detection baseline repurposed for depth estimation achieves only Z%."

## Venue Fit Risks

- **Novelty concern**: DCOL is adapted from CLOC (CVPR 2025). Mitigation: novelty emphasis on problem formalization + Atlas + EDD metric; DCOL is framed as a strong method within the framework, not the sole contribution. Three text-specific modifications (strategy-aware margins, surprisal-augmented anchors, non-uniform learned margins) differentiate from direct CLOC transfer.
- **"Just an empirical study" risk**: Mitigation: method (DCOL) + Atlas (scientific contribution) + curation (practical application) = three-line contribution with clear primary/secondary hierarchy.
- **Controlled vs wild gap**: Mitigation: honest scoping — controlled setting is primary, wild-data calibration is probed, ecological transfer is future work.

## Anticipated Reviewer Concerns

1. "EDD might be very low (depth 2-3), making the task trivial beyond shallow depths" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation)
2. "Why ordinal and not just binary?" → MVP already shows: d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs
3. "Generalization to unseen models/strategies?" → Leave-one-out experiments are core evaluation
4. "Non-monotonic degradation (Drayson et al.)?" → Learnable margins as soft inductive bias; ablation comparing DCOL vs fixed-margin CORAL vs CE loss
