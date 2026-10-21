# monitor v9d resume step10 verify

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v9d_resume_step10_verify_20260520T075715_result.json`
- **Structured JSON:** [`1e95945562da17416381.json`](../../sessions/1e/1e95945562da17416381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v9d 恢复验证完全成功。**

### 关键结果

| 验证项 | 状态 | 详情 |
|--------|------|------|
| **Resume from step 10** | ✓ | 加载 `global_step_10/actor/` checkpoint（model + rng + lr_scheduler），Training Progress 显示 `10/30` |
| **val_before_train** | ✓ | **96.875% success**（32 episodes，满足 C003 ≥16 要求） |
| **vLLM 初始化** | ✓ | 无 OOM/KV cache 错误，generation 耗时 80.5s |
| **symlink/model_path** | ✓ | 无相关错误 |
| **save_contents** | ✓ | actor: `['model', 'extra']`，critic: `['model', 'optimizer', 'extra']` |

### val_before_train 指标
- **success**: 96.875%
- **pass@1**: 96.875%
- **action_is_valid**: 99.6%
- **action_is_effective**: 100%
- **num_actions**: 14.8（平均步数）
- **reward/mean@32**: 9.6875

训练已从 step 10 继续，当前进度 10/30。wandb run: `aeml21w9`。

---
