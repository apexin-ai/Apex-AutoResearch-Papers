# diagnose exp022 val config check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp022-val-config-check_20260515T032205_result.json`
- **Structured JSON:** [`d09c617066b4cb246ad2.json`](../../sessions/d0/d09c617066b4cb246ad2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Config 验证 — 全部生效 ✅

| 参数 | YAML 文件值 | Hydra override | **实际生效值** |
|------|------------|----------------|--------------|
| `es_manager.val.env_groups` | 4 | `=8` | **8** ✅ |
| `es_manager.val.env_configs.n_groups` | [4] | `=[8]` | **[8]** ✅ |
| `kl_loss_coef` | 0.5 (sed已改) | — | **0.5** ✅ |

Hydra resolved config 中确认：`'val': {'env_groups': 8, 'group_size': 1, 'env_configs': {'n_groups': [8]}}`

### 2. 训练进度

- **Step 1/30** 刚完成，速度 ~208s/step
- PID 434853 存活，运行 ~5 分钟
- GPU 0,1：100% 利用率，各 ~14GB 显存

### 3. Step 0 val_before_train 结果（已完成）

| 指标 | 值 |
|------|-----|
| **success** | **0.125** (1/8) |
| **pass@1** | 0.125 |
| **action_is_valid** | 0.4875 |
| **action_is_effective** | 1.0 |
| **num_actions** | 28.125 |
| **response_length** | 3017.5 |
| **reward/mean@8** | 1.25 |
| **reward/best@8/mean** | 6.61 |

### 4. ⚠️ C003 合规性问题

Val 实际使用 **8 episodes**（env_groups=8 × group_size=1），仍 **不满足 C003 要求的 ≥16 episodes**。12.5% success rate 基于 8 episodes 统计可靠性仍然有限。如需合规，需将 `env_groups` 提升至 16 或将 `group_size` 改为 2。

---
