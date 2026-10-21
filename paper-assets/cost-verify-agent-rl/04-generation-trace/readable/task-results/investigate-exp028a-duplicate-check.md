# investigate exp028a duplicate check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_exp028a_duplicate_check_20260515T211724_result.json`
- **Structured JSON:** [`dc22228158ab63b276f9.json`](../../sessions/dc/dc22228158ab63b276f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部证据到齐。`.bak` 文件（exp027 运行时的代码版本）已经导入了 `step_rewards` 并包含 penalty 逻辑。

## exp028a 重复性核实

### Q1: exp027 config 中 invalid_action_penalty_coef = ?
**未显式设置。** exp027 YAML 中 `algorithm` 段没有 `invalid_action_penalty_coef`。但代码中 `getattr(self.config.algorithm, "invalid_action_penalty_coef", 0.1)` **默认值为 0.1**，与 exp028a 显式设置的值相同。

### Q2: blocking_fixes Worker 改了代码吗？
**改了，但是在 exp027 运行之前。**
- `step_rewards.py` 创建于 05-15 16:39（未提交 git，untracked 文件）
- `agent_trainer.py.bak`（05-16 04:43 备份的 exp027 运行时版本）**已经包含** `from ragen.trainer.step_rewards import assign_step_rewards` 和 penalty 调用逻辑
- exp027 于 05-15 22:33 启动 — 在 step_rewards.py 创建之后，使用的代码已包含 penalty 路径

### Q3: exp027 日志中 penalty 是否生效？
**已生效。** 代码路径分析：
- exp027 使用 `context_window_mode: "step_independent"` + `adv_estimator: grpo`
- 这触发 `compute_advantage` 中的 step-independent overlay 分支，直接调用 `assign_step_rewards(invalid_action_penalty_coef=0.1)`
- 该路径**不受** `reward_include_step_penalties` 门控
- 日志中 `critic/advantages/min` 出现负值（如 step1: -0.711, step4: -3.879），与 penalty 影响 advantage 计算一致
- `critic/rewards/min:0.0` 不矛盾——penalty 作用于 step_rewards → discounted_returns → advantages，不修改 token_level_rewards

### 结论
**重复。** exp028a 与 exp027 在功能上等价：
- 唯一 config 差异是 exp028a 显式写了 `invalid_action_penalty_coef: 0.1`，而 exp027 通过代码 `getattr` 默认值拿到同一个 0.1
- 两者运行在相同的修改后代码上，penalty 通过 `step_independent + GRPO` 路径在 exp027 中已经生效
- 其余参数完全一致（同一 SFT checkpoint、同一超参）

Reviewer 判断正确。exp028a 不应启动。

---
