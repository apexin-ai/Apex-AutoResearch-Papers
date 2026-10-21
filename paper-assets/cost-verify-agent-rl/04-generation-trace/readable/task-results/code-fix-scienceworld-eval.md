# code fix scienceworld eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_scienceworld_eval_20260519T183352_result.json`
- **Structured JSON:** [`842101d6fa9d33100a7e.json`](../../sessions/84/842101d6fa9d33100a7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量 eval 已启动：1796 episodes，PID 187796。

汇总：

**代码 diff**：
```python
# 修复前 (run_episode 函数内):
        shown = valid_actions[:MAX_VALID_ACTIONS]
        action_is_valid = action in shown

# 修复后:
        action_is_valid = action in valid_actions
```

**根因**：`get_valid_action_object_combinations()` 返回 ~400+ 个有效动作（包括 `open door to kitchen` 等自然语言格式），但 `[:50]` 截取后只剩前 50 个 `connect X to Y` 格式的动作。模型输出的自然语言动作全部被误判为 invalid。

**6-episode 验证结果**：

| Episode | Task | Steps | Valid Rate | Score |
|---------|------|-------|-----------|-------|
| 1 | boil v14 | 16 | **81%** | -100 |
| 2 | boil v15 | 100 | **33%** | 72 |
| 3 | change-state v14 | 100 | **26%** | 72 |
| 4 | change-state v15 | 22 | **68%** | 100 (OK) |
| 5 | chemistry-mix v16 | 100 | **31%** | 25 |
| 6 | chemistry-mix v17 | 100 | **1%** | 8 |

修复前 valid rate 接近 0%（只匹配 `connect` 格式）。修复后反映真实模型行为：成功 episode ~70-80%，长 episode（模型退化）较低。

**全量 eval**：PID 187796，1796 episodes，预计 25-40 小时。输出 → `/root/autodl-tmp/checkpoints/scienceworld_sft/eval_results_dev_v2.json`

**补充说明**：prompt 中展示给模型的 admissible actions 仍用 `get_valid_action_object_combinations()[:50]`（全是 `connect` 格式）。ScienceWorld 没有 `get_valid_actions()` API，可用的替代只有 `get_possible_actions()`（返回模板如 `go OBJ`，不可用）。如果要改善 prompt 中的 action 展示，需要对完整列表做过滤/排序（去掉大量 `connect` 冗余），但这会改变 eval 时模型看到的 prompt，可能影响结果一致性。

---
