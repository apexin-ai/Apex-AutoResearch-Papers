# analysis tost sensitivity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tost-sensitivity_20260521T072359_result.json`
- **Structured JSON:** [`06ac297bd6412f8901c4.json`](../../sessions/06/06ac297bd6412f8901c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。结果写入 `tost_sensitivity.json`，摘要：

| Margin | Equivalent | Genuinely Different | Underpowered |
|--------|-----------|-------------------|-------------|
| ±1pp | 0 | 2 | 14 |
| ±2pp | 4 | 2 | 10 |
| ±3pp | 10 | 0 | 6 |

关键发现：
- **±1pp**：过严，无条件通过等价检验；Mistral/Qwen2.5 的 PW-D5 两条被判为"genuinely different"
- **±2pp**：4/16 通过（Qwen3 系列 + Mistral FOLIO s456），2 条 PW-D5 仍为 different，10 条 underpowered
- **±3pp**：10/16 通过，0 条 different（因 |Δ|>3 的条件均未达 McNemar 显著），6 条 underpowered（主要是 SE 较大的 LLaMA/Mistral 条件）

SE 估计方法：6 条 `raw_p < 1.0` 的从 McNemar z 统计量反推；10 条 `raw_p = 1.0` 的用 paired proportion model（假设方法间相关系数 r=0.95）估计。

---
