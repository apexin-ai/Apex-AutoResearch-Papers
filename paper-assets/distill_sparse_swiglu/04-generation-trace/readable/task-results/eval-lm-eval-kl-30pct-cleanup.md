# eval lm eval kl 30pct cleanup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_lm_eval_kl_30pct_cleanup_20260516T003626_result.json`
- **Structured JSON:** [`9902b75af54903f95cea.json`](../../sessions/99/9902b75af54903f95cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 被 PID 181121 占用（`eval_benchmark.py --condition mistral_dense`，运行 32 分钟）。无法直接在 cuda:0 上提交 30% eval。

当前 GPU 占用：
| GPU | PID | 进程 | 显存 | 运行时间 |
|-----|-----|------|------|---------|
| 0 | 181121 | eval_benchmark.py (mistral_dense) | 21GB | 32min |
| 1 | 174850 | 未知 python 进程 | 21GB | - |
| 1 | 179918 | lm_eval_sparse.py (50% rerun) | 16GB | 44min |

清理结果：
- PID 182573, 182747, 184120 — 已 kill
- PID 179918 — **仍在运行**（50% eval，状态 Rl，已跑 44 分钟）

30% checkpoint 已确认：`/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt` (145MB)

**需要决定**：cuda:0 上的 PID 181121 (mistral eval) 要 kill 掉给 30% eval 让路吗？还是等它跑完？

---
