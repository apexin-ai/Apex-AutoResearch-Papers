# paper fix all tex issues

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-all-tex-issues_20260514T102420_result.json`
- **Structured JSON:** [`ddfe05e29094a9cc3919.json`](../../sessions/dd/ddfe05e29094a9cc3919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation complete. Here's the summary:

## 修复结果

**已修复的 3 个剩余问题：**

1. **WARNING 6** — `discussion.tex:29`：Qwen s020 Δ 从 3dp `0.235` 统一为 2dp `0.24`（正确四舍五入）；`results.tex` 的 cross-model 表也从 `0.23` → `0.24`

2. **WARNING 7** — `discussion.tex:11`：s=0.35 数据确认存在于远程服务器 (`profiling_output_bf16_ds_imp_s035/`)，已加注"in a supplementary experiment outside the main four-level range"

3. **MODERATE 10** — `paper_framing.md`：已经使用 paired d_z 值（DeepSeek: 0.44→0.80, Qwen: 0.28→1.02），无需修改

**审计报告中其余 8 个问题（CRITICAL 1-5, MODERATE 8-9, Cleanup 11）在当前文件中已全部修复。**

**编译结果：**
- main.pdf 成功生成（22 页，334KB）
- 无 `sec:experiments` 等已修复问题产生的 undefined ref
- 仅 2 个 appendix 引用 warning（`app:multiplicative-null`, `app:bootstrap-details`）——appendix 尚未写入，属预期残留

---
