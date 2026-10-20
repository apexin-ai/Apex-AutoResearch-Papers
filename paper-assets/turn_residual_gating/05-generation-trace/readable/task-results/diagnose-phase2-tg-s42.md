# diagnose phase2 tg s42

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase2_tg_s42_20260518T112048_result.json`
- **Structured JSON:** [`1a1ac3aa2b510173408a.json`](../../sessions/1a/1a1ac3aa2b510173408a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总关键数据：

- L_GAR 共 282 个记录点，其中 247 次为 0.0000（87.6%），非零时最大仅 ~0.04
- Gate 值始终锁定在 ~0.99，从未学习到有效调制
- NTP loss 正常收敛（1.9 → 0.8-0.9）
- 无任何 ERROR/WARNING/NaN
- 日志最后一行为 "Terminated"，EXIT_CODE=143
- Checkpoints 存在（epoch_0, epoch_1）

```json
{"root_cause":"GAR loss几乎恒为0（87.6%的step为0.0000），gate值锁死在~0.99无法学习调制。训练本身正常运行，被diagnose_gar_loss_and_fix Worker发现此bug后通过SIGTERM主动kill，以便启动修复后的v2实验（cumulative GAR loss with ε=0.001）","error_type":"intentional_kill","training_progress":{"steps_completed":"~6050 (Epoch 0全部3000+ steps + Epoch 1至step 6050)","ntp_loss_trend":"正常收敛，从1.92降至0.8-0.9区间","gar_loss_trend":"几乎全程为0.0000（282次中247次为零），偶尔出现极小值(max~0.04)，gate值从0.9923缓慢降至0.9876，gating机制完全失效"},"checkpoint_exists":true,"fix_steps":["v2实验已在PREPARING，使用修复后的cumulative GAR loss (ε=0.001)替代原始GAR loss计算，防止梯度消失导致loss归零"],"can_auto_fix":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GAR loss几乎恒为0（87.6%的step为0.0000），gate值锁死在~0.99无法学习调制。训练本身正常运行，被diagnose_gar_loss_and_fix Worker发现此bug后通过SIGTERM主动kill，以便启动修复后的v2实验（cumulative GAR loss with ε=0.001）",
    "error_type": "intentional_kill",
    "training_progress": {
      "steps_completed": "~6050 (Epoch 0全部3000+ steps + Epoch 1至step 6050)",
      "ntp_loss_trend": "正常收敛，从1.92降至0.8-0.9区间",
      "gar_loss_trend": "几乎全程为0.0000（282次中247次为零），偶尔出现极小值(max~0.04)，gate值从0.9923缓慢降至0.9876，gating机制完全失效"
    },
    "checkpoint_exists": true,
    "fix_steps": [
      "v2实验已在PREPARING，使用修复后的cumulative GAR loss (ε=0.001)替代原始GAR loss计算，防止梯度消失导致loss归零"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
