# Neural Probe OLMo K*_neural Fix: 2 → 1

**Date**: 2026-05-21
**Trigger**: OLMo-1B neural probe rerun yielded K*_neural=1 (0v1 AUC=0.9773, 1v2 AUC=0.5054), but paper still referenced K*_neural=2.

## Changes

### 1. experiments_c1.tex:96 (Neural Probe subsection body)
- **Before**: "while Pythia and OLMo remain at $K^*_{\text{neural}} = 2$ ($\text{AUC}_{2v3}$: 0.5963, 0.5892)"
- **After**: "while Pythia remains at $K^*_{\text{neural}} = 2$ ($\text{AUC}_{2v3} = 0.5963$); OLMo yields $K^*_{\text{neural}} = 1$ (1v2 $\text{AUC} = 0.5054$, consistent with its 15D boundary)"

### 2. experiments_c1.tex:110 (Table `tab:neural_probe_crossmodel`, OLMo row)
- **Before**: K* = 2
- **After**: K* = 1, with footnote: "$^\dagger$OLMo 1v2 AUC = 0.5054 (below θ); K*_neural = 1."

### 3. discussion.tex:20 (Representation dependence paragraph)
- **Before**: "while Pythia and OLMo yield $K^*_{\text{neural}} = 2$"
- **After**: "while Pythia yields $K^*_{\text{neural}} = 2$ and OLMo yields $K^*_{\text{neural}} = 1$, consistent with its 15D boundary"

### 4. appendix_extended.tex:52 (Scale and Neural Probe subsection)
- **Before**: "but $2$ for Pythia and OLMo."
- **After**: "but $2$ for Pythia; OLMo yields $K^*_{\text{neural}} = 1$ (1v2 AUC = 0.5054), consistent with the 15D LightGBM boundary."

### 5. main.tex:72 (Limitations, Feature set item)
- **Before**: "$2$ for Pythia/OLMo"
- **After**: "$2$ for Pythia, $1$ for OLMo"

## Compilation
- `latexmk -pdf main.tex` passed, 20 pages, no errors.
