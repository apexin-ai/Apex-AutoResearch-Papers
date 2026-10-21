# analysis case study extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_case-study-extraction_20260518T092754_result.json`
- **Structured JSON:** [`4c444e4b0d0e48b74e2b.json`](../../sessions/4c/4c444e4b0d0e48b74e2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。总结：

**3个Case已选定，素材保存到 `artifacts/case_study_materials.md`**

| Case | 问题 | 结果 | 亮点 |
|------|------|------|------|
| SICA win | folio_134 (短，直觉清晰) | 6:6 tie, 7 constraints, 1 excluded → SICA 选对 | 罕见的 constraint 起作用 |
| SC win | PW-1066_Q6 (属性链推理) | 6:6 tie, 17 constraints, 2 excluded → SICA 选错 | Constraint 排除惩罚了正确答案 |
| Non-discriminative | PW-903_Q6 (关系链推理) | 6:6 tie, 44 constraints, 仅1 excluded → SICA=SC | 44个 constraint 几乎全是 domain fact |

**关键数据缺失**：实际提取的 constraint 字符串（存在已回收服务器 westd-32608 的 `sica_expanded_14b.json` 中）。文件中用 DSL 推导的代表性 constraint 标注了 [DERIVED]。如需真实 constraint 文本，需在 westd-25068 上对这3题重跑 SICA pipeline。

---
