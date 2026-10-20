# GroupKFold Probe AUROC — Instance Leakage Fix

## Problem
Entity probe used entity-level StratifiedKFold, allowing entities from the same instance to appear in both train and test folds. This caused instance-level information leakage, inflating AUROC.

## Method
- Replaced StratifiedKFold with GroupKFold (groups=instance_idx)
- Reconstructed instance_idx by replaying extraction loop with tokenizer (CPU-only)
- All reconstruction counts matched original metadata exactly

## Results

| Dataset | StratifiedKFold | GroupKFold | Delta   | Probe > MV? |
|---------|----------------|------------|---------|-------------|
| CoNLL   | 0.9796         | 0.8849     | -0.0947 | YES         |
| FewNERD | 0.9872         | 0.6513     | -0.3359 | NO          |
| SciERC  | 0.9766         | 0.6344     | -0.3422 | NO          |

Baselines: MV = 0.87, ESJ = 0.51

## Per-fold GroupKFold detail

### CoNLL (418 unique instances)
Folds: 0.862, 0.907, 0.893, 0.950, 0.813

### FewNERD (433 unique instances)  
Folds: 0.668, 0.692, 0.644, 0.673, 0.579

### SciERC (525 unique instances)
Folds: 0.629, 0.652, 0.638, 0.622, 0.631

## Interpretation
- CoNLL: Probe still > MV — hidden states encode entity quality above what MV captures
- FewNERD/SciERC: Probe drops to 0.63-0.65 — only moderate info in representation, below MV
- The original "probe >> MV" conclusion was largely artifact of instance leakage for 2/3 datasets
- LODO result (0.559) is consistent with weak cross-instance generalization
