# paper d045 final compile

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d045_final_compile_20260516T110239_result.json`
- **Structured JSON:** [`5a05b949adb78d8e3699.json`](../../sessions/5a/5a05b949adb78d8e3699.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译结果：

- **Errors**: 0
- **Undefined references**: 0
- **总页数**: 16 页
- **Overfull hbox > 5pt**: 主体正文 1 处（line 209-218, 45pt），其余全在 checklist/appendix 的 `\resizebox` 表格中（预期行为）

## 验证清单

- [x] abstract.tex: `r² = 1.3--1.7%` ✓
- [x] introduction.tex: `r = 0.112--0.129`（两处均已修正）✓
- [x] Table 2: 仅 Few-NERD 和 MAVEN 两行 ✓
- [x] Table 2 caption 末尾有 FewRel omission 说明（含 `$r=0.187$` 和 `\S\ref{sec:scs-validation}`）✓
- [x] 编译无 error ✓
- [x] 无 undefined references ✓

额外一致性修改：results.tex 正文中 `r² ≈ 1.3--3.5%` → `1.3--1.7%`，"All three datasets" → "Both datasets"，`~97--99%` → `~98--99%`。experimental_setup.tex 添加了 `\label{sec:scs-validation}`。

---
