# Bootstrap CI & Permutation Test Results: arXiv Cross-Scorer Experiments

**Scorer**: Pythia-1.4B (cross-scorer)  
**Method**: GroupKFold(5) OOF predictions + doc-level bootstrap (10,000 resamples) + label permutation (10,000 permutations)  
**Threshold**: theta = 0.60  
**Date**: 2026-05-18

---

## Summary Table: 2v3 Pair (Critical Boundary)

| Generator | AUC (OOF) | 95% CI | CI lower > 0.60? | CI upper > 0.60? | K* (CI) | Perm p-value |
|-----------|-----------|--------|-------------------|-------------------|---------|--------------|
| Qwen-7B | 0.5986 | [0.5835, 0.6133] | No | **Yes** | 2 | < 0.0001 |
| Qwen-1.5B | 0.6316 | [0.6165, 0.6464] | **Yes** | Yes | 3 | < 0.0001 |
| LLaMA-8B | 0.6202 | [0.6054, 0.6355] | **Yes** | Yes | 3 | < 0.0001 |
| Mistral-7B | 0.6075 | [0.5930, 0.6220] | No | **Yes** | 2 | < 0.0001 |

---

## Key Findings

1. **Qwen-7B 2v3** (AUC=0.5986): CI upper = 0.6133 > theta, but CI lower = 0.5835 < theta. The 95% CI straddles the threshold. Bootstrap p(AUC <= 0.60) = 0.571, meaning ~57% of bootstrap samples fall below theta. K* conservatively remains at 2.

2. **Qwen-1.5B 2v3** (AUC=0.6316): CI lower = 0.6165 > theta. Statistically significant above threshold. K* = 3.

3. **LLaMA-8B 2v3** (AUC=0.6202): CI lower = 0.6054 > theta. Marginally significant above threshold (only 0.54 percentage points above). Bootstrap p(AUC <= 0.60) = 0.0041. K* = 3.

4. **Mistral-7B 2v3** (AUC=0.6075): CI lower = 0.5930 < theta. The CI straddles the threshold. Bootstrap p(AUC <= 0.60) = 0.1556. K* conservatively remains at 2.

---

## Full Pairwise Results

### Qwen-7B (K* = 2)

| Pair | AUC | 95% CI | Perm p | CI lower > theta |
|------|-----|--------|--------|-----------------|
| 0v1 | 0.9573 | [0.9518, 0.9626] | 0.0001 | PASS |
| 1v2 | 0.8163 | [0.8049, 0.8277] | 0.0001 | PASS |
| 2v3 | 0.5986 | [0.5835, 0.6133] | 0.0001 | FAIL |
| 3v4 | 0.5413 | [0.5255, 0.5570] | 0.0001 | FAIL |
| 4v5 | 0.5191 | [0.5029, 0.5353] | 0.0166 | FAIL |

### Qwen-1.5B (K* = 3)

| Pair | AUC | 95% CI | Perm p | CI lower > theta |
|------|-----|--------|--------|-----------------|
| 0v1 | 0.9746 | [0.9703, 0.9785] | 0.0001 | PASS |
| 1v2 | 0.8101 | [0.7983, 0.8218] | 0.0001 | PASS |
| 2v3 | 0.6316 | [0.6165, 0.6464] | 0.0001 | PASS |
| 3v4 | 0.5437 | [0.5276, 0.5598] | 0.0001 | FAIL |
| 4v5 | 0.5287 | [0.5127, 0.5448] | 0.0020 | FAIL |

### LLaMA-8B (K* = 3)

| Pair | AUC | 95% CI | Perm p | CI lower > theta |
|------|-----|--------|--------|-----------------|
| 0v1 | 0.9627 | [0.9577, 0.9675] | 0.0001 | PASS |
| 1v2 | 0.8427 | [0.8318, 0.8533] | 0.0001 | PASS |
| 2v3 | 0.6202 | [0.6054, 0.6355] | 0.0001 | PASS |
| 3v4 | 0.5228 | [0.5064, 0.5391] | 0.0060 | FAIL |
| 4v5 | 0.5247 | [0.5085, 0.5408] | 0.0034 | FAIL |

### Mistral-7B (K* = 2)

| Pair | AUC | 95% CI | Perm p | CI lower > theta |
|------|-----|--------|--------|-----------------|
| 0v1 | 0.9798 | [0.9761, 0.9832] | 0.0001 | PASS |
| 1v2 | 0.8138 | [0.8018, 0.8252] | 0.0001 | PASS |
| 2v3 | 0.6075 | [0.5930, 0.6220] | 0.0001 | FAIL |
| 3v4 | 0.5489 | [0.5334, 0.5642] | 0.0001 | FAIL |
| 4v5 | 0.5389 | [0.5233, 0.5547] | 0.0001 | FAIL |

---

## Interpretation for Paper

- All 2v3 pairwise AUCs are significantly > 0.5 (permutation p < 0.001), confirming real separability exists.
- For K* determination using conservative CI criterion:
  - **2 models get K*=3** (Qwen-1.5B, LLaMA-8B): their 2v3 CI lower bound exceeds theta=0.60
  - **2 models get K*=2** (Qwen-7B, Mistral-7B): their 2v3 CI lower bound does NOT exceed theta=0.60
- Qwen-7B is a borderline case: point estimate 0.5986 is just 0.14pp below theta, and 43% of bootstrap samples exceed theta. A more liberal criterion (point estimate) would give K*=2 (below theta) while the CI upper bound suggests the true AUC may exceed 0.60.
- LLaMA-8B is the tightest pass: CI lower = 0.6054, only 0.54pp above theta.

---

## Raw JSON

Full results saved on server at:  
`/root/autodl-tmp/gen-depth-contamination/artifacts/crossscorer_bootstrap_ci.json`

Script:  
`/root/autodl-tmp/gen-depth-contamination/scripts/crossscorer_bootstrap_ci.py`
