# eval seed456 completed metrics and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed456_completed_metrics_and_eval_20260515T005437_result.json`
- **Structured JSON:** [`aa3ee8bdac3bc045f098.json`](../../sessions/aa/aa3ee8bdac3bc045f098.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 实验 | train_loss | train_runtime | eval_ppl_holdout | eval_loss_holdout | status |
|------|-----------|---------------|------------------|-------------------|--------|
| grid_b1_0_seed456 | 10.178 | 12964s (3.6h) | **17.70** | 2.8734 | DONE |
| grid_b1_5_seed456 | 10.435 | 12950s (3.6h) | **17.73** | 2.8750 | DONE |

对比 adaptive 方法的 seed456: eval_ppl=17.66。三种方法在 seed456 上的 holdout perplexity 非常接近（17.66-17.73），与其他 seed 的结果一致。

Registry 已更新完毕，包含 train metrics + eval metrics，status=DONE，conclusion=success。

---
