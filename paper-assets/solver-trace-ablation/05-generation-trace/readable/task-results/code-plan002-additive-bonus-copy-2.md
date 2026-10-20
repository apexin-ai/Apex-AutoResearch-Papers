# code plan002 additive bonus

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-additive-bonus_20260514T022240_result.json`
- **Structured JSON:** [`c6582fc2d3d9f1f2b7e8.json`](../../sessions/c6/c6582fc2d3d9f1f2b7e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练在正常推进（step 12/500）。Reward 值符合预期：

- 有证明成功时（step 11）：`reward_mean=0.459`，`prove_rate=0.375`，`isr_mean=0.281` — 说明 additive bonus 在给结构性 reward
- 无证明时（step 10/12）：`reward_mean=0.0` — exec_reward=0 时 additive bonus 也为 0，正确

---

## 总结

**所有工作已在之前的 session 中完成，训练已启动：**

1. **代码修改** — `scripts/train_grpo.py` 已添加 `additive_bonus` 模式（第187-195行）：
   - `reward_val = execution_reward * (1 + beta * isr_val)`
   - 通过 `--beta` 参数控制，`--reward_mode additive_bonus` 选择
   - 不影响现有 `execution_only` / `execution_sta` / `random_reward` 模式

2. **配置文件** — `configs/grpo_additive_bonus.yaml`：
   - `reward_mode: additive_bonus`, `beta: 0.3`, `seed: 42`, `num_steps: 500`
   - 数据: `data/train_500_seed42.jsonl` (符合 C001)

3. **Reward 逻辑验证** — 独立测试确认：
   - 证明成功 + ISR=0.667 → reward=1.2 (exec 的 1.2x bonus)
   - 解析失败 → reward=0.0
   - reward ≥ exec_reward 恒成立

4. **训练状态** — PID 161819 在 GPU 0 上运行，step 12/500，registry 状态 RUNNING

5. **配置路径**: `/root/solver-trace-ablation/configs/grpo_additive_bonus.yaml`

**无需额外修改，训练正在正常进行。**

---
