# eval full trace v5

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_full-trace-v5_20260515T040151_result.json`
- **Structured JSON:** [`90ab8693a3ffbbf60ade.json`](../../sessions/90/90ab8693a3ffbbf60ade.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## full_trace_v5 评估结果

| 指标 | 值 |
|------|-----|
| **accuracy** | **81.8%** (95% CI: [79.7%, 83.9%]) |
| majority_baseline | 71.5% |
| **lift** | **+10.3pp** (95% CI: [+7.4pp, +13.2pp]) |
| pass P/R/F1 | 0.88 / 0.87 / 0.87 |
| fail P/R/F1 | 0.67 / 0.70 / 0.69 |
| **collapse 确认** | **否** — collapse 消除 |
| eval 来源 | eval_results.json（刚由 PID 951029 生成） |

**关键发现**：v5 没有 collapse。accuracy 从 v2 的 28.4% 跃升至 81.8%，chat template overhead 修复彻底解决了 collapse 问题。模型不再全部预测 majority class，fail recall 达到 70%。

---
