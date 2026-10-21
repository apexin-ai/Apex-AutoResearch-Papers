# fix cross model w5 table

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cross-model-w5-table_20260523T165502_result.json`
- **Structured JSON:** [`1a448b137c44452e4877.json`](../../sessions/1a/1a448b137c44452e4877.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已更新。变更：

1. **添加 $w$ 列**，tabular 从 6 列扩展到 7 列
2. **每个 cross-model voter 组合添加 w=5 行**（multirow 包裹 voter 名称），NLI 行保持 w=3
3. **Caption 更新**：`$w{=}3$` → `$w \in \{3,5\}$`，补充说明 NLI 使用 w=3，增加"worsening at higher $w$"的观察
4. **关键数据确认**：Qwen3-14B → Qwen2.5-14B w=5 = 83.33%, −2.50pp, p=.006，与 solutions.tex 引用一致

solutions.tex 无需修改（选项 A 成功）。

---
