# fix reviewer crossmodel fixes

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_reviewer_crossmodel_fixes_20260514T210233_result.json`
- **Structured JSON:** [`dd7600b90b942a4023d4.json`](../../sessions/dd/dd7600b90b942a4023d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 项修复完成：

| Fix | 修改内容 |
|-----|---------|
| #1 | 表格 Llama SciERC (U) CF: 0.09→0.24；注释 CF=0.0009→0.0024；CF 段落 0.09%→0.24% |
| #2 | "reach 0%" → "are eliminated or near-eliminated ($\leq$0.03%)" |
| #3 | R-F1 段落后新增 E-F1 讨论（Qwen +0.03/+1.22pp，Llama DocRED -0.64pp + parse fail 归因） |
| #5 | caption 末尾添加 parse failure 数据（4 组 U→S1） |
| #6 | 所有 `phase2_*_llama_*` exp_id 改为 `llama_*` 格式（header + 4 条数据注释） |

---
