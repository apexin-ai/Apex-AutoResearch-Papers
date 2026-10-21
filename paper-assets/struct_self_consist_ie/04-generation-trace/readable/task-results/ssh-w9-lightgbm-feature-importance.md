# ssh w9 lightgbm feature importance

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w9_lightgbm_feature_importance_20260522T145330_result.json`
- **Structured JSON:** [`a5326cd1ea81371e7465.json`](../../sessions/a5/a5326cd1ea81371e7465.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No explicit cross-domain transfer files. The `distill_verifier` experiment already contains the cross-dataset evaluation data (train on 2 datasets, test on the 3rd). Here's the full summary:

---

## Found: Verifier Feature Importance Data

### Source 1: `exp_019_trained_verifier/feature_importance.json` — LR coefficients (SciERC, N=8)

| Feature | Mean Coef | Interpretation |
|---------|-----------|----------------|
| **VC** (voting_confidence) | **0.7474 ± 0.15** | Dominant feature |
| SJ (soft_jaccard) | -0.1193 ± 0.05 | Negative weight (hurts) |
| LP (logprob) | 0.1049 ± 0.01 | Small positive |
| EM (exact_match) | 0.1021 ± 0.13 | Unstable (high variance) |
| FK (fleiss_kappa) | 0.0894 ± 0.04 | Small positive |

LR AUROC: 0.6973, but **fails to beat best single signal VC** (0.7064). Gap closure: only **0.8%**.

### Source 2: `supervised_verifier_upgrade/results.json` — Per-dataset feature importance (3 methods)

**RF Gini importance (most relevant for "what features matter"):**

| Feature | SciERC | CoNLL | FewNERD |
|---------|--------|-------|---------|
| logprob | **0.321** | **0.362** | **0.292** |
| fleiss_kappa | 0.222 | 0.159 | 0.198 |
| soft_jaccard | 0.218 | 0.187 | 0.203 |
| exact_match | 0.136 | 0.195 | 0.209 |
| voting_confidence | 0.103 | 0.097 | 0.098 |

**LR absolute coefficients:**

| Feature | SciERC | CoNLL | FewNERD |
|---------|--------|-------|---------|
| exact_match | **0.435** | **1.471** | **1.350** |
| soft_jaccard | 0.340 | 0.173 | 0.145 |
| logprob | 0.060 | 0.597 | 0.165 |
| fleiss_kappa | 0.090 | 0.079 | 0.406 |
| voting_confidence | 0.057 | 0.490 | 0.158 |

### Source 3: `distill_verifier/distill_verifier_results.json` — Cross-domain (leave-one-dataset-out)

Train on 2 datasets, test on the 3rd:

| Test Dataset | LR AUROC | RF AUROC | MLP AUROC |
|-------------|----------|----------|-----------|
| SciERC | 0.8009 | 0.7988 | 0.7980 |
| CoNLL | 0.9376 | 0.9419 | 0.9379 |
| FewNERD | 0.8855 | 0.8850 | 0.8872 |

**Key: features are `lp_score, agreement_ratio, degeneracy_flag, span_length, type_consistency, n_samples`** (6 entity-level features, not the 5 instance-level signals).

RF feature importances for cross-domain:
- **agreement_ratio** dominates: 0.686 (SciERC), 0.634 (FewNERD)
- **lp_score**: 0.165 (SciERC), 0.079 (FewNERD)
- **type_consistency**: 0.114 (SciERC), 0.120 (FewNERD)
- **degeneracy_flag**: 0.019 (SciERC), 0.127 (FewNERD)

### Source 4: `r17_analyses/mlp_verifier_comparison.json` — Supervised model comparison

Verdict: **"feature_bottleneck"** — MLP/RF don't beat LR; adding interaction features makes things worse. The 5 confidence signals lack discriminative power for sample selection.

### CoNLL→SciERC Transfer Failure Analysis

No explicit CoNLL→SciERC transfer experiment exists. The closest is the `distill_verifier` leave-one-out setup which trains on {CoNLL + FewNERD} and tests on SciERC — AUROC ~0.80, which is actually **decent**. The transfer "failure" is more about the **instance-level selection bottleneck**: even with good entity-level AUROC, supervised verifiers can't beat greedy selection F1.

Top-3 features driving the gap between domains (from LR coefficient shifts):
1. **exact_match**: coefficient jumps from 0.435 (SciERC) to 1.471 (CoNLL) — CoNLL entities are simpler, EM is much more predictive there
2. **voting_confidence**: 0.057 (SciERC) vs 0.490 (CoNLL) — high agreement is more informative for CoNLL's cleaner entity types
3. **logprob**: 0.060 (SciERC) vs 0.597 (CoNLL) — LM confidence correlates better with correctness on well-known entity types

---
