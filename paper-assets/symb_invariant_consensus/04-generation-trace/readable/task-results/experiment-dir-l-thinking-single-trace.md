# experiment dir l thinking single trace

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-l-thinking-single-trace_20260520T181344_result.json`
- **Structured JSON:** [`0bf50be530d8a479e5b4.json`](../../sessions/0b/0bf50be530d8a479e5b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已写入 `results.json`。

| Model | N | Single Trace Mean ± Std | SC@12 | Agg Gain |
|---|---|---|---|---|
| **Mistral-7B** | 204 | 46.41% ± 2.80% | 54.41% | +8.00 pp |
| **Qwen3-14B nonthinking** | 204 | 79.37% ± 1.98% | 83.82% | +4.45 pp |
| **Qwen3-14B thinking** | 166 | 83.28% ± 0.99% | 83.73% | +0.45 pp |

要点：
- Mistral SC@12=54.41% 与 baseline 一致
- Mistral 的 aggregation gain 最大（+8pp），thinking 模型几乎无 gain（+0.45pp）——thinking 模型 traces 间一致性极高（std 仅 0.99%），SC 没什么可聚合的
- Per-problem agreement 中位数：Mistral 0.42, nonthinking 1.0, thinking 1.0
- Qwen3-thinking 只有 166 题（exp028b 未跑完 folio_166-203）

---
