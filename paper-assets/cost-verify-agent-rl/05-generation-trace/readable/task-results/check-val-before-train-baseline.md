# check val before train baseline

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_val_before_train_baseline_20260517T075909_result.json`
- **Structured JSON:** [`edf4c6cf7e3f32c02547.json`](../../sessions/ed/edf4c6cf7e3f32c02547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整了。以下是三个实验的 val_before_train (step 0) success rate：

---

### exp029 (episode-level GRPO)

| 指标 | 值 |
|------|-----|
| **success rate** | **12.5%** (4/32) |
| val set 大小 | 32 episodes (`env_groups: 32, group_size: 1`) |
| 来源 | `/root/runs/cost-verify-agent-rl/exp029_episode_level.log` **line 14230** |
| 原始值 | `val-env/AlfworldSG/success:np.float64(0.125)` |

### exp028c (selfguide recipe)

| 指标 | 值 |
|------|-----|
| **success rate** | **6.25%** (1/16) |
| val set 大小 | 16 episodes (`env_groups: 16, group_size: 1`) |
| 来源 | `/root/runs/cost-verify-agent-rl/exp028c_selfguide_recipe.log` **line 14327** |
| 原始值 | `val-env/AlfworldSG/success:np.float64(0.0625)` |

### exp026 (step-independent GRPO)

| 指标 | 值 |
|------|-----|
| **success rate** | **6.25%** (1/16) |
| val set 大小 | 16 episodes (`env_groups: 16, group_size: 1`) |
| 来源 | `/root/runs/cost-verify-agent-rl/exp026_step_independent_grpo.log` **line 5056** |
| 原始值 | `val-env/AlfworldSG/success:np.float64(0.0625)` |

---

### Baseline 不一致的原因

12.5% vs 6.25% 来自 **val set 大小不同**：
- exp029 用了 **32 episodes**，exp028c/exp026 用了 **16 episodes**
- 三个实验共用同一个 base model（训练前），但 val set 的 task 采样不同（32 vs 16 个 game_files），随机种子选到的任务不同
- 同一模型在 32 episode 上碰巧解出 4 个（12.5%），在 16 episode 上各碰巧解出 1 个（6.25%）

注意：当前 YAML 配置文件 `_alfworld_exp028c_selfguide_recipe.yaml` 已被改为 `env_groups: 140`，但实际运行时日志中记录的是 16。配置文件在实验运行后被修改过。

---
