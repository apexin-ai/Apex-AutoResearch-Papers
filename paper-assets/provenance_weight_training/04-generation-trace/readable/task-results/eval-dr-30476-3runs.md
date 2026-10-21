# eval dr 30476 3runs

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dr_30476_3runs_20260518T134907_result.json`
- **Structured JSON:** [`5e68d95409d222efb001.json`](../../sessions/5e/5e68d95409d222efb001.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 全部完成。汇总结果：

| Checkpoint | Loss | Perplexity | Tokens |
|---|---|---|---|
| `detect_remove_q05_seed123/final` | 2.8491 | **17.27** | 4,077,068 |
| `detect_remove_q05_seed456/final` | 2.8493 | **17.28** | 4,077,068 |
| `detect_remove_q09_seed42/final` | 2.8577 | **17.42** | 4,077,068 |

q05 两个 seed 的 PPL 非常接近（17.27 vs 17.28），q09 略高（17.42）。JSON 结果已分别保存到 `/root/autodl-tmp/output/eval_q05_seed123.json`、`eval_q05_seed456.json`、`eval_q09_seed42.json`。

---
