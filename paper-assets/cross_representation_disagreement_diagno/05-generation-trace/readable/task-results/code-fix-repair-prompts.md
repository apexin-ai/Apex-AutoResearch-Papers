# code fix repair prompts

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_repair_prompts_20260514T180357_result.json`
- **Structured JSON:** [`c3099e0dee44cebe5e25.json`](../../sessions/c3/c3099e0dee44cebe5e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。结果：

- `BLIND_REGEN_PROMPT`：`Output ONLY a complete **{repr_type}** script` — FOL 时渲染为 "**FOL (Z3)** script"，Code 时渲染为 "**Python code** script"
- `TARGETED_REPAIR_PROMPT`：`Output ONLY the corrected **{repr_type}** script` — 同上
- 硬编码 "Python script" 已完全消除（grep 确认无残留）
- 代码块标记保持 ` ```python``` `（Z3 是 Python 库，不变）
- 原文件已备份为 `repair.py.bak_prompt_fix`
- 未触碰 pipeline.py，未重启任何进程

---
