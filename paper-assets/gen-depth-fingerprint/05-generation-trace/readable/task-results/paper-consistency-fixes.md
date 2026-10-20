# paper consistency fixes

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency-fixes_20260515T045751_result.json`
- **Structured JSON:** [`6b8c452d4d0fb89b4c3e.json`](../../sessions/6b/6b8c452d4d0fb89b4c3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。共修改 16 个文件，修复报告已写入 `consistency_fixes_report.md`。

**修复总结：**
- **Fix 1 (CI 区间)**: 从所有 6-gen 上下文删除 [0.786, 0.799]，仅保留在 5-gen baselines 表格中（已标注 "5-gen LOGO"）
- **Fix 2 (实验 ID)**: 删除全部 `plan-014`、`plan-015`、`plan-004-v2` 共 16 处
- **Fix 3 (Binoculars)**: 5 个文件中 `0.59--0.82` → `0.41--0.82`
- **Fix 4 (6-gen 主线)**: ablation 句中 `macro-F1=0.80` → `0.79`，held-out 范围统一为 `0.68 to 0.86`

---
