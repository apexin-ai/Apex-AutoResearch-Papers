# ssh verify action probe start

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-action-probe-start_20260515T141945_result.json`
- **Structured JSON:** [`9b4806fedccfbde4fca4.json`](../../sessions/9b/9b4806fedccfbde4fca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行。

| 实验 | 状态 | 进度 | GPU | 显存 | 利用率 |
|------|------|------|-----|------|--------|
| `mvp2_action_trained` | **Running** | Layer 3 (4/33) 训练中 | cuda:0 | 2936MiB / 97887MiB | 50% |
| `mvp2_action_untrained` | **Running** | Layer 4 (5/33) 训练中 | cuda:1 | 2936MiB / 97887MiB | 0% (采样间隙) |

指标初步观察：
- **Trained** 模型：Layer 0 R²≈0.01（随机），Layer 2 已升至 R²=0.55，grip_acc=0.86，逐层提升趋势正常
- **Untrained** 模型：Layer 0 同样 R²≈0.01，Layer 1 即达 R²=0.57 / grip_acc=0.88，后续层保持 ~0.53-0.57

注意 untrained 日志显示 `device=cuda:0` 而非预期的 `cuda:1`，但 nvidia-smi 确认 PID 613482 实际跑在 GPU 1 上（可能是 `CUDA_VISIBLE_DEVICES=1` 使得进程内部看到的是 `cuda:0`）。两个实验互不冲突，正常推进中。

---
