# analysis n13 investigation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n13_investigation_20260516T164000_result.json`
- **Structured JSON:** [`5ceee36c21104112dc7e.json`](../../sessions/5c/5ceee36c21104112dc7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Root cause identified. Here's the summary:

## 结果

**N=13 = 8×1.5B + 5×3B**（排除了 0.5B 后，3B 应有 8 个但只匹配了 5 个）

### 被排除的 3 个 respondent

| # | Eval dirname (strip后) | RRF key | 原因 |
|---|---|---|---|
| 1 | `Qwen2.5-3B_d000_s42_a32` | `Qwen2.5-3B_d000_a32_s42` | `a32`/`s42` 顺序反了 |
| 2 | `Qwen2.5-3B_d000_s123` | `Qwen2.5-3B_d000_s123_a32` | eval 名缺 `_a32` 后缀 |
| 3 | `Qwen2.5-3B_d005_s42_a32` | `Qwen2.5-3B_d005_a32_s42` | `a32`/`s42` 顺序反了 |

### 排除机制

`run_pooled_rrf_irt.py` 的 `filter_models_for_benchmark()` 函数（第 57 行）用 `strip_aligned(dirname)` 做 exact match 查找 RRF key：

```python
key = strip_aligned(m["dirname"])
if key not in rrf_data:
    continue  # 静默排除
```

eval_results 目录用 `_sXX_a32` 命名（如 `d000_s42_a32_aligned`），而 RRF exposure_scores.json 用 `_a32_sXX` 命名（如 `d000_a32_s42`）。d100 没问题是因为两边碰巧一致（`d100_a32_s42`）。

### 修复方案

在 `strip_aligned()` 或 `filter_models_for_benchmark()` 中加一个 name normalization 步骤，将 `_sXX_a32` 和 `_a32_sXX` 统一成同一 canonical form。或直接在 RRF exposure_scores.json 中把 3 个 key 重命名为与 eval 一致。

两者都是低风险单点修改，不影响其他流程。

---
