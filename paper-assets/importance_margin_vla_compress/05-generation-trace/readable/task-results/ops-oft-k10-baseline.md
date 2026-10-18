# ops oft k10 baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oft-k10-baseline_20260520T125047_result.json`
- **Structured JSON:** [`042f79e407605b1da294.json`](../../sessions/04/042f79e407605b1da294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OFT k=1.0 baseline eval 已提交并运行中。

**总结：**
- **westd-41074 GPU 0**, PID 434280
- **exp_id**: `eval_oft_baseline_k10`
- 10 tasks × 50 episodes = 500 total, seed=7
- Dry-run 确认：模型加载正常，`[Pruning] 512 -> 512 vision tokens (k=1.0)` 无 dtype 错误
- 清理了 2 个残留 dry-run 进程（430085, 431310）
- 输出：`eval_results/eval_oft_prune_k10_baseline.json`
- 日志：`/tmp/oft_k10_full.log`

---
