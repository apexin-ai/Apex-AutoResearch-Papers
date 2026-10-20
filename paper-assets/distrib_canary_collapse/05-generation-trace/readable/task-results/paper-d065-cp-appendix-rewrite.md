# paper d065 cp appendix rewrite

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d065_cp_appendix_rewrite_20260518T142654_result.json`
- **Structured JSON:** [`08412532acbe6367b097.json`](../../sessions/08/08412532acbe6367b097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

替换完成。验证结果：

- `grep -c "FPR|66.7|ordering|reversal|complementary"` = **4** (≥3 ✅)
- `grep -c "independent evidence"` = **0** (= 0 ✅)
- em-dash (—) = **0** ✅

Change-Point 段落已按 D065 要求重写：
1. 第一段：null control FPR 66.7% (12/18) 先讲，说明单调漂移即可触发断点
2. 第二段：ordering reversal 作为核心论点（null: downstream gen 2 先变 → canary gen 4-8 后变；treatment: canary gen 1 先变 → downstream gen 2-4 后变），用 "complementary evidence from a distinct statistical framework"
3. 第三段：caveats（无多重比较校正、token_entropy gen-1 split 仅 1 点导致 1/3 seeds 显著、T=11 power 限制）
4. 新增 α=0.00 null control 表格（`tab:cp_null`），保留原 α=0.75 表格（`tab:cp_results`）

---
