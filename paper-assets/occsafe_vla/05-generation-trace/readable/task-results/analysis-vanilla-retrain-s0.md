# analysis vanilla retrain s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vanilla_retrain_s0_20260523T175902_result.json`
- **Structured JSON:** [`793c42e0c9bf776bfff6.json`](../../sessions/79/793c42e0c9bf776bfff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已齐全。

## 结果摘要
- **conclusion: success**
- 总步数: 50005（跑满）
- 最终 loss: 0.0457 (action_loss)
- checkpoint 路径: `/root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- W&B run_id: 无（本次训练未启用 W&B）
- 训练时长: ~14h 8min
- EXIT_CODE: 0

**Loss 曲线（每 10k 步采样）:**

| Step | action_loss | occ_loss | depth_loss |
|------|------------|----------|------------|
| 0 | 0.6836 | 0.0000 | 0.0000 |
| 10000 | 0.1211 | 0.0000 | 0.0000 |
| 20000 | 0.1216 | 0.0000 | 0.0000 |
| 30000 | 0.0845 | 0.0000 | 0.0000 |
| 40000 | 0.0654 | 0.0000 | 0.0000 |
| 50000 | 0.0457 | 0.0000 | 0.0000 |

## 详细发现

1. **Loss 收敛正常**：action_loss 从 0.68 单调下降到 0.046，无异常波动。occ/depth loss 始终为 0（符合 vanilla baseline 无辅助头的预期）。

2. **Checkpoint 部分缺失**：日志确认 5 个 checkpoint（10k/20k/30k/40k/50k）均已保存，但磁盘上仅存 10000、40000、50000 三个。20000 和 30000 可能被清理释放磁盘空间。对 plan_023 梯度分析影响不大——最终 checkpoint (50000) 完整存在。

3. **最终 checkpoint 完整**：15GB，包含 4 个 safetensor 分片、action_head (289MB)、proprio_projector (65MB)、lora_adapter、tokenizer 等全部文件。可直接用于后续梯度分析。

4. **训练速度稳定**：~1.08 it/s，无明显 slowdown 或 OOM。

---
