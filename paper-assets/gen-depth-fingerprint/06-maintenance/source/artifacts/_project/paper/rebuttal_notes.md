# Rebuttal Notes — Method Novelty (D1)

## ARR Policy Reference
- **H7**: "Do not penalize a method for being simple. If an approach is simple but well-motivated and effective, simplicity is a strength."

## Core Defense Points

### 1. Contribution is task formulation + empirical characterization, not feature engineering
- We introduce **ordinal depth estimation** as a new task (gen-0/gen-1/gen-2+)
- No prior work addresses depth estimation in non-paraphrastic continuation chains
- The features are intentionally simple; the contribution is showing they exhibit differential depth response

### 2. Differential depth response is a novel empirical finding
- Three-gradient decomposition (drifting / moderate / stationary) has no prior documentation in inference-chain literature
- Lower-tail compression + upper-tail preservation pattern is new
- This is not a method paper — it is a measurement and characterization paper

### 3. Simplicity is a feature, not a bug
- 7-feature ensemble achieves binary F1=0.694 across 8 generators / 5 families
- Our approach: single lightweight reference model (Pythia-410M, 410M params)
- Their approach: four independent detection pipelines (each requiring separate inference)
- Interpretability: seven named statistics vs opaque ensemble

### 4. Scientific value independent of method complexity
- Establishes 3-class granularity ceiling (5-class fails, Appendix F)
- Documents prompt-type dependence bounds
- Negative downstream finding prevents wasted engineering effort
- Connection to model collapse literature (inference-chain drift as early indicator)

## Anticipated Objections and Responses

**"Just standard features"**: Features individually are standard; the contribution is (a) showing they decompose into depth-sensitive and depth-invariant groups, (b) that this decomposition generalizes across 8 generators / 5 families, (c) the ordinal task formulation.

**"Limited to base models"**: Deliberate design choice to isolate mechanism. Instruct results (F1 near chance) confirm this was the right call — instruction tuning confounds require separate study.

**"No deep learning method"**: QLoRA ceiling (F1=0.905) shows deep methods work better but don't change the scientific conclusions about DDR. Paper's value is the characterization, not maximizing F1.
