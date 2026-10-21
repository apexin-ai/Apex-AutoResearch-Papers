# code exp028a blocking fixes

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp028a_blocking_fixes_20260515T210106_result.json`
- **Structured JSON:** [`b9f91f856291cc0dd7d4.json`](../../sessions/b9/b9f91f856291cc0dd7d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 修复总结

### Fix 1: model_path 修正 ✅

**文件**: 
- `RAGEN/config/_alfworld_exp028a_recipe_fix.yaml`
- `RAGEN/config/_alfworld_exp028b_full_recipe.yaml`

**改动**: `model_path: .../Qwen3-1.7B` → `model_path: .../Qwen3-1.7B-Instruct`

### Fix 2: penalty mechanism — 无需代码修改（已正确工作）

**结论**: Director 的分析不完整。penalty 通过两条独立路径注入：

| 路径 | 修改的对象 | step_independent 下是否生效 |
|------|-----------|--------------------------|
| `_adjust_token_rewards_with_step_penalties` | `token_level_rewards` | **否**（被 step_returns 覆盖） |
| `assign_step_rewards` | `step_rewards` → `step_returns` | **是** ✅ |

`assign_step_rewards`（step_rewards.py:41）已正确将 `invalid_action_penalty_coef` 注入到 step_rewards 中，在 `compute_step_discounted_returns` 之前执行。完整调用链：

```
config.algorithm.invalid_action_penalty_coef=0.1
  → agent_trainer.py:921 getattr → :935 传入 compute_advantage
  → agent_trainer.py:285 传入 assign_step_rewards
  → step_rewards.py:41 if not is_action_valid[i]: step_rewards[i] -= penalty
  → compute_step_discounted_returns → step_returns
  → compute_grpo_step_advantage → advantages (有方差，有梯度)
```

### 测试结果

| 测试 | 结果 |
|------|------|
| invalid actions 获得 -0.1 penalty | ✅ |
| 不同 invalid count → 不同 step_returns (ep0=-0.095 vs ep1=-0.285) | ✅ |
| penalty=0 等同于 all-valid | ✅ |
| 全失败 group 中 GRPO advantage 方差 = 0.924 (非零梯度) | ✅ |
| 成功 episode + penalty 仍为正 return (8.83) | ✅ |

### 产出文件
1. config diff: 两个 yaml 的 model_path
2. 测试: `RAGEN/tests/test_step_independent_penalty.py`
3. 无代码修改需要——penalty 机制已通过 `assign_step_rewards` 正确工作

---
