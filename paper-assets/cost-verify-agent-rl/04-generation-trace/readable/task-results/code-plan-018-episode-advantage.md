# code plan 018 episode advantage

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_018_episode_advantage_20260517T190830_result.json`
- **Structured JSON:** [`9cbe71a7ab9cca809ebc.json`](../../sessions/9c/9cbe71a7ab9cca809ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 结论：代码已完整实现，无需额外改动

**已有实现覆盖了全部需求：**

| 组件 | 文件 | 行号 | 状态 |
|------|------|------|------|
| `compute_episode_returns()` | `step_rewards.py:88` | 计算 episode 级 return，同 episode 所有 window 共享 | ✅ |
| `advantage_mode` 分支 | `agent_trainer.py:288-292` | 当 `advantage_mode == "episode_level"` 时用 episode return 替代 per-window return | ✅ |
| Config 传参 | `agent_trainer.py:984,1569` | `getattr(self.config.algorithm, 'advantage_mode', None)` | ✅ |
| 实验 config | `_alfworld_factorial_h2_episode_adv.yaml:74` | `advantage_mode: "episode_level"` | ✅ |

**验证结果：**
- 模块导入成功
- episode-level mode 下同一 episode 的两个 window advantage 完全相同（0.8660, 0.8660）
- step-level mode 下同一 episode 的两个 window advantage 不同（0.8211 vs 0.9098，差 0.089）
- Hydra config 解析正确：`advantage_mode=episode_level`, `context_window_mode=step_independent`, `h=2`

**向后兼容**：`advantage_mode` 默认为 `None`，走原有 `compute_step_discounted_returns` 路径，不影响已有实验。

实验 `factorial_h2_episodeadv_seed1` 的代码已就绪，可以提交训练。

---
