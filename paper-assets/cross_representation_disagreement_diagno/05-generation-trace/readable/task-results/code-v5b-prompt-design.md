# code v5b prompt design

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v5b_prompt_design_20260514T130829_result.json`
- **Structured JSON:** [`71a2c44516f62acdd6e2.json`](../../sessions/71/71a2c44516f62acdd6e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告：

**1. Revert 状态：** 无 git 历史，直接从 v5 → v5b 替换（已备份 v5 到 `formalize.py.v5_backup`）

**2. v5b diff（v5 → v5b）：**
- 移除 closed-world assumption（规则 4-5），恢复 3-way 输出（True/False/Unknown）
- Unknown 加了 anti-lazy 约束：`genuinely lack sufficient information` + `attempt to derive both True and False`
- 新增规则 7：禁止 hardcode 答案，所有 print 必须在依赖计算变量的条件分支内
- Example 1/2 加了标签 `(True)`/`(False)`
- 新增 Example 3 (Unknown) 展示合法 Unknown 用法

**3. PID 29177：** 正常运行中（v4 pipeline 未受影响）

---
