# code exp028 penalty mechanism

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp028_penalty_mechanism_20260515T202841_result.json`
- **Structured JSON:** [`03935f9991989f7eb512.json`](../../sessions/03/03935f9991989f7eb512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

导入正常。

---

## 总结

### 数据流追踪结果

**`invalid_action_penalty_coef=0.1` 已在 exp027 中生效。** 路径：

```
env.action_is_valid → es_manager.history.info → ctx_manager.non_tensor_batch["is_action_valid"]
→ assign_step_rewards(-0.1/invalid) → discounted_returns → compute_grpo_step_advantage
→ 覆写 GRPO outcome advantage → 最终 advantages
```

exp027 config 中没有显式设置 `invalid_action_penalty_coef`，但代码默认值为 0.1（`agent_trainer.py:1467`），所以 penalty 实际上一直在工作。

### 代码修改

新增 `reward_include_step_penalties` 功能（`agent_trainer.py`）：
- 将累积 step penalty 注入 `token_level_rewards`（episode-level reward）
- 使 GRPO outcome advantage 和 GiGPO episode advantage 也能区分不同失败 trajectory
- 只修改 `token_level_rewards`，不修改 `non_tensor_batch["reward"]`，避免与 `assign_step_rewards` 双重计算
- 默认关闭，完全向后兼容
- 8/8 新增测试通过，17/17 GiGPO 现有测试通过

### exp028a 配置

```yaml
algorithm:
  invalid_action_penalty_coef: 0.1        # 显式声明
  reward_include_step_penalties: true      # 新功能
```

### 残余问题

对于"valid but useless"动作（动作在 admissible_actions 中但无法推进任务），penalty 不生效，失败 episode 仍可能零方差。这需要额外的 reward shaping（如 progress reward）来解决，不在本次修改范围内。

报告已写入 `artifacts/exp027_penalty_dataflow_report.md`。

---
