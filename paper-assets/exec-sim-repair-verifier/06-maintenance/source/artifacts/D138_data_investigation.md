# D138 Data Investigation Report

## Problem 1: Qwen3-4B CLS per-test 76.92% vs Table 4's 83.63%

### Root Cause: Different checkpoint and seq_length

| | 76.92% (v2 aggregation script) | 83.63% (Table 4) |
|---|---|---|
| **Location** | seetacloud: `/root/autodl-tmp/eval_results/cls_v5/` | home: `/home/sonny/.../results/repo_cls_v5_ckpt4600_test/` |
| **Checkpoint** | `cls_v5_checkpoint-600` | `checkpoints_repo_cls_v5/checkpoint-4600` |
| **seq_length** | 2048 | 5120 |
| **Unparseable** | 132 | 0 |
| **Truncated** | yes (some) | 0 |
| **Per-test acc** | 76.92% | 83.63% |
| **Variant-level** | 68.75% (33/48) | 64.58% (31/48) |

**Conclusion**: The variant-level aggregation script v2 (`aggregate_variant_level_v2.py`) hardcodes the path to the ckpt-600 eval on seetacloud. The paper's Table 4 correctly uses ckpt-4600 (the better checkpoint after longer training) with seq5120 (no truncation). These are two completely different eval runs.

### Variant-level aggregation for 83.63% predictions

Variant-level accuracy (AND rule, n=48): **64.58% (31/48)**

This matches the paper's claim at line 166: "variant-level accuracy ranges from 64.58% (4B)".

Errors (17 variants):

| Variant | GT | Pred | #Tests | #Pass | #Fail | Error Type |
|---|---|---|---|---|---|---|
| astropy__astropy-7336__gold | 1 | 0 | 357 | 356 | 1 | FN (1 test wrong) |
| django__django-11848__mutation_off_by_one | 0 | 1 | 79 | 79 | 0 | FP (all pass) |
| django__django-11848__mutation_operator_swap | 0 | 1 | 79 | 79 | 0 | FP (all pass) |
| django__django-12325__mutation_operator_swap | 0 | 1 | 237 | 237 | 0 | FP (all pass) |
| django__django-12406__gold | 1 | 0 | 219 | 199 | 20 | FN |
| django__django-14351__gold | 1 | 0 | 76 | 75 | 1 | FN (1 test wrong) |
| django__django-14351__mutation_boundary_removal | 1 | 0 | 76 | 75 | 1 | FN (1 test wrong) |
| django__django-14434__gold | 1 | 0 | 151 | 150 | 1 | FN (1 test wrong) |
| django__django-15037__mutation_operator_swap | 0 | 1 | 32 | 32 | 0 | FP (all pass) |
| psf__requests-6028__gold | 1 | 0 | 221 | 186 | 35 | FN |
| pydata__xarray-6992__gold | 1 | 0 | 1161 | 1158 | 3 | FN (3 tests wrong) |
| pydata__xarray-6992__mutation_operator_swap | 1 | 0 | 1161 | 1158 | 3 | FN (3 tests wrong) |
| pytest-dev__pytest-6202__mutation_return_value | 0 | 1 | 90 | 90 | 0 | FP (all pass) |
| pytest-dev__pytest-7490__gold | 1 | 0 | 114 | 113 | 1 | FN (1 test wrong) |
| scikit-learn__scikit-learn-14053__mutation_operator_swap | 0 | 1 | 23 | 23 | 0 | FP (all pass) |
| sphinx-doc__sphinx-11445__gold | 1 | 0 | 44 | 25 | 19 | FN |
| sphinx-doc__sphinx-11445__mutation_off_by_one | 1 | 0 | 44 | 25 | 19 | FN |

Pattern: 6 FP (mutations predicted all-pass), 11 FN (gold patches with a few wrong tests trigger AND rule).

### Action needed

Update `aggregate_variant_level_v2.py` to use the correct 83.63% predictions. Either:
- Copy predictions from home to seetacloud
- Or add a config entry pointing to the home server path

---

## Problem 2: Fail Recall Comparison

### Per-test Fail/Pass Recall

| Model | Seed | seq | Per-test Acc | Fail Recall | Pass Recall |
|---|---|---|---|---|---|
| **DeepSeek CLS s123** | 123 | 8192 | 74.93% | **13.72%** (363/2646) | 97.62% (6968/7138) |
| DeepSeek CLS s123 | 123 | 2048 | 82.62% | 36.77% (973/2646) | 99.62% (7111/7138) |
| **Qwen3-4B CLS s42 (ckpt4600)** | 42 | 5120 | 83.63% | 48.72% (1289/2646) | 96.57% (6893/7138) |
| Qwen3-4B CLS s42 (ckpt600) | 42 | 2048 | 76.92% | 79.29% (2098/2646) | 76.04% (5428/7138) |
| **Qwen3-8B CLS s42** | 42 | 8192 | 84.48% | 56.76% (1502/2646) | 94.76% (6764/7138) |
| **Qwen3-8B CLS s123** | 123 | 8192 | 85.60% | 51.44% (1361/2646) | 98.26% (7014/7138) |

### Variant-level Comparison

| Model | Per-test Acc | Fail Recall | Variant Acc (n=48) |
|---|---|---|---|
| DeepSeek CLS s123 (seq8192) | 74.93% | 13.72% | 56.25% |
| DeepSeek CLS s123 (seq2048) | 82.62% | 36.77% | 72.92% |
| DeepSeek CLS s42 (v4, seq8192) | 71.29% | N/A | 58.33% |
| Qwen3-4B CLS s42 (ckpt4600) | 83.63% | 48.72% | 64.58% |
| Qwen3-4B CLS s42 (ckpt600) | 76.92% | 79.29% | 68.75% |
| Qwen3-8B CLS s42 | 84.48% | 56.76% | 72.92% |
| Qwen3-8B CLS s123 | 85.60% | 51.44% | 81.25% |

---

## Key Findings

### 1. DeepSeek "decision collapse" confirmed
- Fail recall 13.72% at seq8192: the model predicts pass on nearly everything
- Even at seq2048 (36.77%), fail recall is far below Qwen3 models
- Variant-level accuracy (56.25%) barely above majority baseline (54.17%)
- Paper's claim at line 166 is accurate

### 2. Qwen3-4B ckpt4600 shows moderate pass bias, not collapse
- Fail recall 48.72% is intermediate (not as extreme as DeepSeek's 13.72%)
- Per-test accuracy high (83.63%) but aggregation penalty drops variant-level to 64.58%
- Paper correctly categorizes this as "aggregation penalty" rather than "decision collapse"

### 3. Interesting: ckpt600 vs ckpt4600 trade-off
- ckpt600 (76.92% acc): balanced fail/pass recall (79.29% / 76.04%) → **higher variant-level** (68.75%)
- ckpt4600 (83.63% acc): pass-biased (48.72% / 96.57%) → **lower variant-level** (64.58%)
- Higher per-test accuracy does NOT guarantee higher variant-level accuracy
- The ckpt4600 model learned to predict pass more aggressively, which helps per-test (because 72.96% are pass) but hurts variant-level (AND rule punishes any false-pass on fail tests)

### 4. Does data support "model-contingent decision collapse"?
**Yes, with nuance.** The failure modes form a clear spectrum:

| | DeepSeek (seq8192) | Qwen3-4B (ckpt4600) | Qwen3-8B |
|---|---|---|---|
| Failure mode | Decision collapse | Aggregation penalty | Aggregation penalty |
| Fail recall | 13.72% | 48.72% | 51-57% |
| Pass recall | 97.62% | 96.57% | 95-98% |
| Variant acc | 56.25% | 64.58% | 73-81% |

The same CLS formulation exhibits qualitatively different failure modes across models: DeepSeek collapses to near-always-pass, while Qwen3 maintains meaningful fail detection but suffers from AND-rule amplification. The failure mode is indeed model-contingent.
