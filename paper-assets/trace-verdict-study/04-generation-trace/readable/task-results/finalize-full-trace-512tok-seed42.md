# finalize full trace 512tok seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_finalize_full_trace_512tok_seed42_20260516T001401_result.json`
- **Structured JSON:** [`e0a19bc584b35d1334e7.json`](../../sessions/e0/e0a19bc584b35d1334e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| accuracy | **80.42%** [78.1%, 82.6%] |
| majority_baseline | 71.5% |
| lift | +8.9pp |
| pass_f1 | 0.862 |
| fail_f1 | 0.665 |
| n | 1190 |

**Conclusion: negative** — 512tok (80.42%) 低于 untruncated full_trace (81.8%)，截断到 512 tokens 损失了约 1.4pp。

**已执行操作：**
1. registry metrics 已写入
2. conclusion = "negative" 已设置
3. status = "DONE" 已设置
4. spec.checkpoint_path 已更新为 final 目录
5. cron `full_trace_512tok_seed42` 已删除

---
