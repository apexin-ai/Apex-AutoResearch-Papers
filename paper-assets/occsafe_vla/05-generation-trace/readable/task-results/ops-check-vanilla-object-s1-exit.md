# ops check vanilla object s1 exit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-vanilla-object-s1-exit_20260528T072615_result.json`
- **Structured JSON:** [`95fb101154c7a707c42a.json`](../../sessions/95/95fb101154c7a707c42a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：训练成功完成。**

| 项目 | 状态 |
|------|------|
| 训练 | **成功** — 50005/50005 steps 完成，日志显示 "Max step 50005 reached! Stopping training..." |
| 50000_chkpt | **存在** — 包含 merged model (4 safetensors shards)、lora_adapter/、action_head、dataset_statistics.json 等完整文件 |
| 其他 checkpoints | 40000_chkpt, 45000_chkpt 也存在 |
| 训练 PID 798980 | 已退出（正常结束） |
| Eval 轮询 PID 969726 | **仍在运行**（已运行 1h02m），eval 已触发且正在执行中，当前进度 T0: 80% (40/50 episodes) |
| 最终 loss | action_loss=0.0996, occ_loss=0.0, depth_loss=0.0（vanilla 无 aux loss 正常） |

注意：任务中给的 checkpoint 路径用了 `libero_spatial`，实际路径是 `libero_object`（因为这是 object task suite）。

---
