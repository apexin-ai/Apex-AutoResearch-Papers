# ops check rrf output contamination

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-rrf-output-contamination_20260516T034351_result.json`
- **Structured JSON:** [`7f08ca6d9b4f240dcf7c.json`](../../sessions/7f/7f08ca6d9b4f240dcf7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### RRF 输出文件

| 文件 | 时间戳 | 污染状态 |
|------|--------|----------|
| `/root/autodl-tmp/exp003/exposure_aggregated.json` | May 14 22:17 | **无污染** — 不含任何 alpha=16 3B 模型名 |
| `/root/autodl-tmp/exp003/exposure_scores.json` | May 14 22:17 | **无污染** — 不含任何 alpha=16 3B 模型名 |

### 详情

两个文件均不包含 blocklist 中的 5 个 alpha=16 目录名（`Qwen2.5-3B_d000_s42`, `Qwen2.5-3B_d000_v2_s42`, `Qwen2.5-3B_d005_s42`, `Qwen2.5-3B_d025_s42`, `Qwen2.5-3B_d100_s42`）。

`exposure_scores.json` 中出现的 `Qwen2.5-0.5B_d005_s42` 和 `Qwen2.5-0.5B_d100_s42` 是 **0.5B 模型**，不在 alpha=16 blocklist 范围内，属正常数据。

**结论：无污染，不需要重新生成。**

---
