# eval mistral contam5 read results

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral-contam5-read-results_20260524T060246_result.json`
- **Structured JSON:** [`ccfa4a2958567314592e.json`](../../sessions/cc/ccfa4a2958567314592e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Mistral contam_5 评估结果

文件 `/root/autodl-tmp/ctrl_contam_mistral/results/contam_5_results.json` 存在（2026-05-24 13:29）。

### 核心指标

| 指标 | Overall | Seen | Unseen |
|------|---------|------|--------|
| **Accuracy** | 55.90% | 76.64% | 54.81% |
| **lz\* (free θ)** | -5.729 | -3.346 | -4.730 |

- **θ_MLE (free)**: -0.848
- **n_seen**: 702, **n_unseen**: 13,340 (total: 14,042)
- **Contamination rate**: 5% (702/14042)

### 缺失项

`theta_fixed_n10_recompute.json` 中**没有 contam_5 条目**——只有 contam_15 和 contam_50 的 fixed-θ 结果。因此以下指标缺失：

- lz\* (fixed θ) — overall/seen/unseen
- Cohen's d

需要用 θ_fixed = -1.0876（来自 10 个 clean seed 的均值）对 contam_5 重新计算 fixed-θ lz\* 和 Cohen's d，才能补全完整指标。

---
