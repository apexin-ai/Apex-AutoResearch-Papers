# code exp013b fix bonus validate

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013b-fix-bonus-validate_20260514T081321_result.json`
- **Structured JSON:** [`0b1a16a63dcd2a1888ed.json`](../../sessions/0b/0b1a16a63dcd2a1888ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 产出汇总

| 项目 | 结果 |
|------|------|
| valid_action_bonus 修改 | `0.5` → `0.15` (envs.yaml:422) ✓ |
| config.py 默认值 | `0.0` 不变 ✓ |
| 有效动作 reward | `0.15` ✓ |
| 无效动作 reward | `0.0` ✓ |
| reward 方差 > 0 | `{0.15, 0.0}` ✓ |
| kl_loss_coef | `0.01` ✓ |

---
