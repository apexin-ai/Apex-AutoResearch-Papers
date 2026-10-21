# analysis mvp baseline v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_baseline_v2_20260515T145527_result.json`
- **Structured JSON:** [`f9b1e59696e7ad4b7043.json`](../../sessions/f9/f9b1e59696e7ad4b7043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

## mvp_baseline_v2 结果：**FAILED**

**核心问题：**
1. **训练提前终止** — 仅跑到 step 600/30000（2%），进程静默退出，无任何错误或完成信息
2. **Loss 坍塌** — step 150 起 loss 降至 0.0000，gradient 也为 0.00，典型的 degenerate solution
3. **无 checkpoint** — checkpoints 目录为空
4. **W&B offline** — 无云端指标，eval 也未执行（首次 eval 在 2K steps）

**Loss 轨迹摘要：** 0.2332 → 4.08（spike）→ 0.0096 → 0.0000（collapse at step 150+）

**需要排查：**
- Action 数据分布是否 normalize 后集中在零附近（模型输出零即可获得零 loss）
- 进程退出原因（OOM kill 或 tmux 异常？）
- 下次运行需设 `WANDB_MODE=online`

---
