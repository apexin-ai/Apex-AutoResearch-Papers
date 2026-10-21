# monitor exp027 wandb check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp027_wandb_check_20260515T174257_result.json`
- **Structured JSON:** [`5c6bca34ddc52b8403e8.json`](../../sessions/5c/5c6bca34ddc52b8403e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**exp027 状态：运行正常，数据太早无法判定。**

W&B 当前仅有 step 1 的 actor 梯度指标（summary），无 step-level history：

| 指标 | 值 | 判定 |
|------|-----|------|
| actor/grad_norm | 19.44 | 正常 |
| actor/entropy | 0.275 | 单点，无法判趋势 |
| actor/kl_loss | 0.0576 | 第一步，需后续对比 |

train/success、val/success、reward 等核心指标均未上报——这是正常的：runtime ~3h 对应 step 0 (val_before_train) + step 1 rollout/训练，verl 在整步完成后才写 step-level metrics。

**无早期预警信号触发。** 下次有意义的检查点：step 2-3 完成后（~19:30-20:30 UTC）。

报告已写入 `artifacts/exp027_wandb_interim.md`。

---
