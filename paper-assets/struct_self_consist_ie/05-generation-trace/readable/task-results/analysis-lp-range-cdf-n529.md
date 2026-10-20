# analysis lp range cdf n529

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lp_range_cdf_n529_20260515T131311_result.json`
- **Structured JSON:** [`d5cc4485c37f47841095.json`](../../sessions/d5/d5cc4485c37f47841095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件均已更新完成。数值变化汇总：

### `analysis_lp_range_cdf.json`（N=8）

| 指标 | n=551（旧） | n=529（新） |
|------|------------|------------|
| n_instances | 551 | 529 |
| eps_0.05 tied fraction | **59.7%** | **60.3%** |
| eps_0.01 | 2.0% | 1.1% |
| eps_0.10 | 83.7% | 83.9% |
| median LP range | 0.0413 | 0.0401 |
| mean LP range | 0.0623 | 0.0622 |
| min LP range | 0.0 | 9.57e-05 |

### `analysis_lp_range_cdf_n16_3seed.json`（N=16×3seed）

| 指标 | n=1653（旧） | n=1587（新） |
|------|-------------|-------------|
| n_instances | 1653 (551×3) | 1587 (529×3) |
| pooled eps_0.05 | 42.6% | 43.6% |
| pooled median | 0.0586 | 0.0563 |

关键变化：过滤掉 22 个空 gold 标注样本后，eps=0.05 的 tied fraction 从 59.7% 升至 60.3%，符合预期。min LP range 从 0.0 变为 9.57e-05（之前的 0.0 来自空 gold 实例）。

---
