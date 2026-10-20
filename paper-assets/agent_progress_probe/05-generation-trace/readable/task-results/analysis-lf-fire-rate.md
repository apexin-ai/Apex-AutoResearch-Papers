# analysis lf fire rate

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lf-fire-rate_20260514T213654_result.json`
- **Structured JSON:** [`5ca8565db1858a3444cb.json`](../../sessions/5c/5ca8565db1858a3444cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| LF | SWE-Agent fire% | OpenHands fire% |
|---|---|---|
| cmd_rep | 65.5% | 92.2% |
| file_diff | 57.3% | 42.1% |
| outcome_bp | 23.9% | 19.8% |

- **file_diff**: SWE-Agent 57.3%（33,941/59,268），OpenHands 42.1%（65,096/154,743）。OH 较低是因为 OpenHands 的 edit 命令格式不同，更多窗口落入 `edit_count ≤ 1` 的 ABSTAIN 路径。
- **outcome_bp**: SWE-Agent 23.9%（14,142/59,268），OpenHands 19.8%（30,612/154,743）。只对最后 2 个窗口 + timeout/stuck 全局投票，所以 fire rate 最低。

数据已保存到服务器 `results_lf_fire_rates.json` 并注册为 artifact `art_20260514_51cf0d`。

---
