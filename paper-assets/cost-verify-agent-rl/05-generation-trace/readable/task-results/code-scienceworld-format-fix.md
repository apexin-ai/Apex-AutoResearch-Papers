# code scienceworld format fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld-format-fix_20260519T121606_result.json`
- **Structured JSON:** [`837a9b3ea0c1b8feee7f.json`](../../sessions/83/837a9b3ea0c1b8feee7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

经过详细对比 RAGEN ctx_manager 和提取脚本，情况和预期不同：

**RAGEN 框架 `_build_turn_state_content` (ctx_manager.py:669-674) 在 RL 训练时会生成这些标记：**
```
\nTurn {n}:\n
State:\n{state}\n
You have {actions_left} actions left. Always output: &lt;think>...&lt;/think> &lt;answer>...&lt;/answer> ...
```

且 Reward 作为单独 user message: `Reward:\n{reward}\n`

**如果从 SFT 中去掉 "Turn X:", "Reward:", "You have X actions left"，反而会增大 distribution shift。**

真正的格式差异是：

1. **第一轮 Task 位置**：
   - RAGEN: `State:\nTask: {desc}\n{obs}\n\nAdmissible actions: [...]` （Task 在 State 内，因为它是 `_format_observation` 的输出）
   - 提取脚本: `Task: {desc}\n\nState:\n{obs}\n\nAdmissible actions: [...]` （Task 在 State 外面）

2. **Reward 值**：
   - RAGEN: 中间步为 `0.0`（sparse reward），终局为 `(score/100) * config.score`
   - 提取脚本: 累积的 ScienceWorld 原始分数（5, 10, 25... 逐步增长）

需要修复的是这两个差异，而不是删除标记。要继续按这个方向修吗？

---
