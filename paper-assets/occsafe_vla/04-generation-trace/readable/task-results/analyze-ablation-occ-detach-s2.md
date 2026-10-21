# analyze ablation occ detach s2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_ablation_occ_detach_s2_20260522T215935_result.json`
- **Structured JSON:** [`3633f585977425c12528.json`](../../sessions/36/3633f585977425c12528.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`ablation_occ_detach_s2` 已推进到 DONE。

**训练结果摘要：**
- 50005 steps 正常完成，EXIT_CODE=0，无异常错误
- 训练时长：14.76 小时（~1.08 it/s）
- Checkpoint：`/root/autodl-tmp/checkpoints/ablation_occ_detach_s2/openvla-7b+...--50000_chkpt`（15GB，含 action_head/occ_head/proprio_projector + 4 shard merged model）
- 训练 loss 未记录到日志（仅 tqdm 进度条），与 detach_s0/s1 一致

**注意：** final_action_loss / final_occ_loss 无法从日志提取（losses 仅写入 wandb，本地无 wandb 目录）。需要 eval 才能得到 CAR/TSR 指标，与 s0 (CAR=0.746) / s1 (CAR=0.744) 对比。

---
