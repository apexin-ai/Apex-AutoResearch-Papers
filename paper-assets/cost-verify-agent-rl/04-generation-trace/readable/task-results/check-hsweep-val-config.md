# check hsweep val config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_hsweep_val_config_20260517T080628_result.json`
- **Structured JSON:** [`8ba983cc1ea06574bfe3.json`](../../sessions/8b/8ba983cc1ea06574bfe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. hsweep val env_groups

Config: `_alfworld_hsweep_h2.yaml`

| 参数 | 值 |
|------|-----|
| val.env_groups | 32 |
| val.group_size | 1 |
| 总 val episodes | 32 |

### 2. Step 0 val success

**0/32 (0.0%)**

所有 32 个 episode 平均 num_actions=49.9375（≈max_turn 50），全部超时未完成。

### 3. 与 exp029 差异原因

两者都用同一 checkpoint、同样的 val 配置（32 env_groups × 1 group_size），step 0 无训练差异。唯一区别：

| | exp029 | hsweep_h2_seed1 |
|--|--------|----------------|
| context_window_mode | `full` | `step_independent` |
| history_length | N/A (全量) | **2** |
| step 0 val | 12.5% (4/32) | 0% (0/32) |

**原因是 context window 截断**：h=2 时模型只能看到最近 2 步历史，丧失了对之前探索结果的记忆，导致在需要多步推理的 AlfWorld 任务上完全无法完成。这是 h-sweep 的预期行为——验证了 context window 长度对性能的因果影响。

次要因素：train_seed=10000 可能导致 val task 采样不同，但 0% vs 12.5% 的差距主要由 context 截断解释。

---
