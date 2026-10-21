# code m3 limitations patch

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_m3-limitations-patch_20260522T024958_result.json`
- **Structured JSON:** [`7c381f6f2a0427e122c0.json`](../../sessions/7c/7c381f6f2a0427e122c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

**Diff：** 在 line 16（`discrete, pre-defined subgroups` 句）之后新增 2 句（lines 17-18）：
- Line 17: 说明实验用 text-feature subgroups，demographic subgroups 需要敏感数据，引用了 `\citep{ashwin2025bias}`
- Line 18: 强调 EC-HTE 的纠正机制对 subgroup 定义方式 agnostic

**编译结果：**
- 20 pages，0 errors，0 undefined references
- Conclusion 仍在 page 8（页数未变）

**Ashwin et al. bib 条目：** 已找到 `ashwin2025bias`，已添加 `\citep{ashwin2025bias}` 引用。

**Limitations 长度：** 18 行（约 3 段），覆盖 ~5 个点（sample budget、classifier accuracy、symmetric errors、discrete subgroups + external validity、variance approximation），符合 EMNLP 简短要求。

---
