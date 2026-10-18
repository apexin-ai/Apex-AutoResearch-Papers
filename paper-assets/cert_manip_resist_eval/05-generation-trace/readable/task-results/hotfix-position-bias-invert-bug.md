# hotfix position bias invert bug

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_hotfix_position-bias-invert-bug_20260525T203938_result.json`
- **Structured JSON:** [`c096874e86fa105ffec6.json`](../../sessions/c0/c096874e86fa105ffec6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整对比报告：

---

## Bug 修复

删除了 3 个文件共 5 处错误的 `_invert_winners()`/`_invert()` 调用：
- `src/unified_data_loader.py` — 2 处（checkpoint + individual scores）
- `scripts/run_fractional_logit_v2.py` — 1 处（checkpoint）
- `scripts/gen_p3_figures.py` — 2 处（checkpoint + individual）

---

## 1. Position Bias ASR 对比（per model）

### MMLU × position_bias
| Model | 修正前 | 修正后 | Δ |
|---|---|---|---|
| qwen2.5-72b | 0.663 | 0.370 | -0.293 |
| llama3.1-70b | 0.600 | 0.407 | -0.193 |
| mistral-large | 0.540 | 0.443 | -0.097 |
| qwen2.5-32b | 0.660 | 0.390 | -0.270 |
| qwen2.5-14b | 0.793 | 0.330 | -0.463 |
| llama3.1-8b | 0.660 | 0.343 | -0.317 |
| claude-opus-4 | 0.547 | 0.460 | -0.087 |
| gpt-5.5 | 0.520 | 0.543 | +0.023 |
| gemini-2.5-pro | 0.553 | 0.523 | -0.030 |
| gpt-4.1 | 0.473 | 0.477 | +0.004 |
| claude-sonnet-4 | 0.480 | 0.473 | -0.007 |
| gpt-4o | 0.617 | 0.393 | -0.224 |
| gemini-2.5-flash | 0.627 | 0.463 | -0.164 |
| gpt-4o-mini | 0.543 | 0.430 | -0.113 |
| claude-3-haiku | 0.693 | 0.363 | -0.330 |

### ARC × position_bias
| Model | 修正前 | 修正后 | Δ |
|---|---|---|---|
| qwen2.5-72b | 0.597 | 0.440 | -0.157 |
| llama3.1-70b | 0.497 | 0.503 | +0.007 |
| qwen2.5-14b | 0.777 | 0.363 | -0.413 |
| llama3.1-8b | 0.727 | 0.273 | -0.453 |
| claude-3-haiku | 0.830 | 0.190 | -0.640 |

---

## 2. η_max pooled β_std trajectory

|  | K=3 | K=5 | K=7 |
|---|---|---|---|
| **旧** | 0.264 | 0.102 | 0.084 |
| **新** | **0.243** | **0.091** | **0.086** |
| CI 旧 | [0.158, 0.369] | [-0.055, 0.259] | [-0.083, 0.251] |
| CI 新 | **[0.163, 0.323]** | **[-0.031, 0.212]** | **[-0.039, 0.211]** |

## 3. K_eff pooled β_std trajectory

|  | K=3 | K=5 | K=7 |
|---|---|---|---|
| **旧** | 0.356 | 0.435 | 0.401 |
| **新** | **0.286** | **0.353** | **0.309** |

## 4. WCB significance counts (B=999, FDR<0.05)

|  | K=3 | K=5 | K=7 |
|---|---|---|---|
| K_eff 新 | **8/12** | **8/12** | **7/12** |
| η_max 新 | **5/12** | **0/12** | **1/12** |

## 5. Fractional logit significance (FDR<0.05)

|  | K=3 | K=5 | K=7 |
|---|---|---|---|
| K_eff 旧 | 9/12 | 9/12 | 9/12 |
| K_eff 新 | **10/12** | **11/12** | **11/12** |
| η_max 旧 | 6/12 | 3/12 | 4/12 |
| η_max 新 | **8/12** | **8/12** | **6/12** |
| all_pos 旧 | False | False | False |
| all_pos 新 | **False** | **False** | **False** |

## 6. R² summary

| K | mean R² |
|---|---|
| 3 | 0.3469 |
| 5 | 0.2806 |
| 7 | 0.2335 |

---

## 核心 Claim 检验

| Claim | 结果 |
|---|---|
| **"CI crosses zero at K≥5"** | **YES** — K=5 CI=[-0.031, 0.212], K=7 CI=[-0.039, 0.211] |
| **"diversity uniformly positive (12/12)"** | **NO** — position_bias 两个条件的 β_keff 变为负值（-0.33~-0.37），只有 10/12 为正 |
| **"η_max diminishes monotonically"** | **YES** — 0.243 → 0.091 → 0.086 |

---

**关键发现**: 修复后 position_bias 的 β_keff 变为负值，说明对于 position_bias 攻击，panel diversity (K_eff) 反而**降低**了 ASR。"diversity uniformly positive (12/12)" 这一 claim 不再成立（改为 10/12）。其余核心 claim 不受影响。

产出文件：
- 对比报告: `artifacts/results/plan001/position_bias_fix_comparison.json`
- Per-condition 详细数据: `artifacts/results/plan001/per_condition_full_reanalysis.json`
- 分析脚本: `scripts/rerun_full_analysis_after_fix.py`

---
