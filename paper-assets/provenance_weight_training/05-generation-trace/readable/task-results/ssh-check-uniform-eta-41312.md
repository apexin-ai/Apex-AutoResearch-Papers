# ssh check uniform eta 41312

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_uniform_eta_41312_20260517T174948_result.json`
- **Structured JSON:** [`ee7c74d8127142be4ad4.json`](../../sessions/ee/ee7c74d8127142be4ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成，汇报结果：

---

## 任务 A：uniform_seed42 训练进度

| 项目 | 数值 |
|------|------|
| **当前 optimizer step** | **799 / 6103** (13.1%) |
| **每步耗时** | ~2.1 s/step (从进度条稳定值) |
| **已运行时长** | ~2h54m (22:59 → 01:53 CST) |
| **纯训练时间** | ~28 min (799 steps × 2.1s) |
| **Eval 开销** | ~146 min (每次 eval 67823 样本 / 8 per batch = 8477 iterations，耗时约 44 min) |

**Loss 趋势**：per-batch loss 从 step 0 的 ~2.8 降至 step 799 的 ~1.6-2.5，有下降但幅度有限（尚未完成 1 个 epoch，epoch=0.03）。训练正常。

**ETA 估算**：
- 纯训练剩余：5304 steps × 2.1s ≈ **3.1h**
- Eval 剩余：eval_steps=200，剩余约 26 次 eval × 44 min ≈ **19h**
- **总 ETA ≈ 22-23 小时**

**严重问题**：eval 占比 84% 的运行时间（每 200 步 eval 一次，每次 44 min vs 训练 200 步仅 7 min）。如果需要加速，可以增大 eval_steps（如改为 1000）或减少 eval 数据量。

---

## 任务 B：random_reweight_seed456

已提交成功：
- 脚本：`/root/provenance_weight_training/scripts/run_random_reweight_seed456.sh`
- GPU：**cuda:2**（cuda:3 被 grid_b0_3_seed456 占用）
- 日志：`~/runs/provenance_weight_training/random_reweight_seed456.log`
- 与 seed42 脚本的差异：seed 42→456，output_dir 改为 random_reweight_seed456，WANDB_MODE=disabled

---
