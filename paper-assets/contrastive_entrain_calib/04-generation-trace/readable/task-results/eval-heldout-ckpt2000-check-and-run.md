# eval heldout ckpt2000 check and run

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_heldout-ckpt2000-check-and-run_20260523T105048_result.json`
- **Structured JSON:** [`afa65099606fc4c98f79.json`](../../sessions/af/afa65099606fc4c98f79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**训练状态**：exp-004-heldout 正在运行中，当前 step **1910/8000**（截至日志最后条目 18:50:38 UTC）。

**已有 checkpoints**：500, 1000, 1500（在 `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp004_heldout/`）

**checkpoint-2000 尚未生成。**

**ETA 估算**：
- 每 10 步约 91-93 秒（~9.2 秒/步）
- 距 step 2000 还需 90 步 → 约 **14 分钟**
- 预计 checkpoint-2000 生成时间：**~19:05 UTC**（May 23）

训练 loss 稳定在 sft=0.0000, l2≈0.002, total≈0.0002，与之前 plateau 一致。

需要等 checkpoint-2000 生成后再跑 eval。要我过 15 分钟后再检查并自动跑 eval 吗？

---
