# code fix reviewer 4issues

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-reviewer-4issues_20260514T083028_result.json`
- **Structured JSON:** [`910a663d7590d90e4c3c.json`](../../sessions/91/910a663d7590d90e4c3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 汇报

**问题 1** — `inject_and_generate.py` 第308行：recovery step 的 observation 从 `&lt;injection_detected>...` 改为 `record.get("current_observation", "")`，即注入点处环境返回的真实观测。

**问题 2** — dry-run 验证结果：
- Vanilla SFT: 150 条，TaxEI SFT: 152 条（150 + 2 注入 = 152）✓
- 无 `&lt;injection_detected>` 标签 ✓
- 注入样本的 recovery 步骤前的 user 内容是真实环境观测（如 "You arrive at countertop 1..." / "You arrive at fridge 1..."）✓
- 注入样本含 `&lt;think>` + `&lt;action>` 格式 ✓

**问题 3** — 服务器 formatter.py 已包含双字段名兼容 `traj.get("task_description", "") or traj.get("task_desc", "")`，无需修改。

**问题 4** — `"I'll help with this task."` boilerplate 已从服务器和本地 formatter.py 删除。task description 现在只作为第一轮 user 消息，不再附带空洞的 assistant 回复。

---
