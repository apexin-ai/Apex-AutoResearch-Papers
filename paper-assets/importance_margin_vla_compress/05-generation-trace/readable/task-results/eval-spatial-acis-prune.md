# eval spatial acis prune

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_spatial_acis_prune_20260517T103759_result.json`
- **Structured JSON:** [`469621ee57bdb1705f85.json`](../../sessions/46/469621ee57bdb1705f85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已成功启动，正在运行中。

**报告：**

| 项目 | 值 |
|------|------|
| Checkpoint | `checkpoints/libero_acis_stage1only_k03/stage1_done/checkpoint.pt` |
| Config | `configs/libero_acis_stage1only_k03.yaml` |
| PID | 431116 |
| GPU | 1 (`CUDA_VISIBLE_DEVICES=1`) |
| Suite | `libero_spatial`，10 tasks |
| 每 task episodes | 50 |
| 总 episodes | 500 |
| 预计运行时间 | ~6s/episode × 500 = ~50 min |

前 6 个 episode 全部 FAIL（达到 max_steps=280），与预期一致——k=0.5 true_removal 在 spatial 下应该也是 ~0% SR，cliff-edge 效应成立。

---
