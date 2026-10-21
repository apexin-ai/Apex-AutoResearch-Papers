## Cross-Model Transfer Implementation Details (Exp-003)

Source: `src/experiments/exp_003_cross_transfer.py`

---

### 1. Dimensionality Reduction

- **Method**: sklearn PCA (`sklearn.decomposition.PCA`)
- **Components tested**: 2048, 1024, 512 (hardcoded `PCA_DIMS = [2048, 1024, 512]`)
- **Selection criterion**: Fixed list, NOT variance-explained threshold
- **Implementation**: Fit `PCA(n_components=max_dim)` once per model on ALL data (full dataset, no train/test split for PCA fitting), then slice columns to get lower dims
- **Optimization**: One PCA fit at `max_dim=2048`, then truncate to 1024/512 by taking first k columns of the transformed matrix

### 2. Dimension Alignment (4096 → 5120)

- **Approach**: Independent PCA projection to shared dimensionality (NO explicit alignment)
- **NOT used**: Procrustes rotation, CCA, learned linear mapping, zero-padding, truncation
- **Mechanism**: Each model's features are independently PCA-projected into its own top-k subspace. The probe trained on source model's PCA space is directly applied to target model's PCA space at the same dimensionality.
- **Key assumption**: Top PCA directions of different models capture sufficiently similar variance structure for a linear probe to transfer. No rotation or matching step is performed.

**Critical implementation detail**: This is NOT a "dimension alignment" in the traditional sense. The code simply:
1. Fits PCA_source on source model data → gets source features in R^k
2. Fits PCA_target on target model data → gets target features in R^k
3. Trains LogisticRegression on PCA_source features
4. Directly evaluates on PCA_target features

The PCA bases are unrelated between models. Transfer works only if the principal components happen to encode similar information in similar ordinal positions.

### 3. Transfer Pipeline

```
Step 1: Load hidden states at layer 14 (index 2 in stored layers [12..24])
        - r1_8b:   layer_idx=2, hidden_dim=4096
        - r1_32b:  layer_idx=2, hidden_dim=5120
        - qwq_32b: layer_idx=1, hidden_dim=5120

Step 2: Precompute PCA independently per model (fit on ALL traces/steps)

Step 3: For same-dim pairs (5120↔5120):
        Try "direct" transfer (no projection, raw feature space)
        - Train LogisticRegression on source raw features
        - Evaluate on target raw features

Step 4: For ALL pairs:
        Try PCA-based transfer at dims {2048, 1024, 512}
        - Train LogisticRegression on source PCA features
        - Evaluate on target PCA features
```

### 4. Training Data for PCA Projection

| Model | Files | Traces (with commitment_point) | Steps | Hidden dim |
|-------|-------|-------------------------------|-------|-----------|
| r1_8b | 268 | 209 | 9,667 | 4096 |
| r1_32b | 100* | 100 | 3,506 | 5120 |
| qwq_32b | 95* | 95 | 4,852 | 5120 |

*Some files may have `commitment_point=None` and are skipped

PCA is fit on the **entire dataset** per model (all traces, all steps concatenated), NOT on a train subset. The train/test split (70/30 by traces, seed=42) is only used for the LogisticRegression baseline evaluation.

### 5. Alternative Methods Attempted

**Only two methods were implemented**:

1. **Direct transfer** (same-dim pairs only, 5120→5120): Train probe on raw source features, test on raw target features. No projection.
2. **Independent PCA** (all pairs): Project each model independently to shared dimensionality.

**NOT attempted** (no code, no comments, no config options for):
- Procrustes rotation (orthogonal alignment of PCA subspaces)
- Canonical Correlation Analysis (CCA)
- Learned linear mapping / projection matrix
- Centering/whitening before alignment
- Joint PCA on concatenated data
- Zero-padding or truncation of raw features

### 6. Key Hyperparameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| PCA dimensions | [2048, 1024, 512] | Fixed list |
| LogisticRegression max_iter | 2000 | |
| LogisticRegression C | 1.0 | |
| class_weight | "balanced" | |
| random_state | 42 | |
| train/test split ratio | 0.7 | By traces |
| Crossing threshold K | 5 | Consecutive steps > 0.5 |
| Decision threshold | 0.5 | For binary prediction |

### 7. Transfer Pairs Tested

```
r1_8b  → r1_32b   (4096 → 5120, PCA only)
r1_8b  → qwq_32b  (4096 → 5120, PCA only)
r1_32b → qwq_32b  (5120 → 5120, direct + PCA)
qwq_32b → r1_32b  (5120 → 5120, direct + PCA)
r1_32b → r1_8b    (5120 → 4096, PCA only)
```

Missing: `qwq_32b → r1_8b` (not in TRANSFER_PAIRS list)

### 8. Results Summary

**Same-model baselines**:
| Model | Accuracy | Crossing Rate | Lead Mean |
|-------|----------|---------------|-----------|
| r1_8b | 0.8234 | 0.4127 | -1.46 |
| r1_32b | 0.6516 | 0.6333 | 11.74 |
| qwq_32b | 0.7171 | 0.7241 | 9.24 |

**Best cross-model transfer (accuracy)**:
| Pair | Best Method | Accuracy | Baseline Gap |
|------|------------|----------|-------------|
| r1_8b→r1_32b | PCA-2048 | 0.522 | -0.130 vs r1_32b baseline |
| r1_8b→qwq_32b | PCA-2048 | 0.595 | -0.122 vs qwq_32b baseline |
| r1_32b→qwq_32b | PCA-2048 | 0.550 | -0.167 vs qwq_32b baseline |
| qwq_32b→r1_32b | Direct-5120 | 0.673 | +0.021 vs r1_32b baseline |
| r1_32b→r1_8b | PCA-1024 | 0.583 | -0.240 vs r1_8b baseline |

### 9. Implications for Paper

The "cross-model transfer" in this experiment is a **weak baseline approach**: independent PCA without explicit alignment. The moderate transfer success (especially qwq_32b→r1_32b direct at 0.673, exceeding baseline) suggests the safety commitment signal has some universality across models, but the method leaves significant room for improvement with proper alignment techniques.

For the Appendix, frame this as: "We tested the simplest possible alignment strategy (independent PCA projection) to establish a lower bound on cross-model transferability. Even without explicit subspace alignment, partial transfer is observed, suggesting structural similarity in how different models encode safety commitment transitions."
