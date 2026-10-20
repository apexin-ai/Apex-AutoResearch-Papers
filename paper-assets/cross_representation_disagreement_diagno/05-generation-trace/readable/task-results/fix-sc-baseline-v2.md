# fix sc baseline v2

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sc_baseline_v2_20260515T072917_result.json`
- **Structured JSON:** [`dca589939e3ce720b609.json`](../../sessions/dc/dca589939e3ce720b609.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，验证通过。

---

### 改动总结

**问题 1 — `--mode` 参数（标准 SC vs 温度扫描）**

- 新增 `--mode {standard,sweep}` 参数，默认 `standard`
- `standard`：固定 temp=0.7，k 次 i.i.d. 采样（符合 Wang et al. 2022）
- `sweep`：原逻辑，温度扫描 [0.6, 0.7, 0.8, 0.9, 1.0]（保留作 appendix）

**问题 2 — `_crd_is_correct()` 单一答案判定**

旧逻辑对 disagree 样本用 `fol_v == gt or code_v == gt`（oracle upper bound），改为：

| 情况 | 最终答案 |
|------|----------|
| agree / both_error | 共识答案（fol_verdict） |
| disagree + 有 repair + 有效 verdict | 最后一轮 repair 的 `exec_result.verdict` |
| disagree + 无有效 repair, predicted_error_side=code | fol_verdict（FOL 更可靠） |
| disagree + 无有效 repair, predicted_error_side=fol | code_verdict（Code 更可靠） |
| disagree + 无 stability 信息 | fol_verdict（默认，FOL 准确率更高） |

---
