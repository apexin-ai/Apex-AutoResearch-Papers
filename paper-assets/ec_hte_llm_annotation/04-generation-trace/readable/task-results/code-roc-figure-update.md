# code roc figure update

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_roc-figure-update_20260521T161348_result.json`
- **Structured JSON:** [`d51f10533566dd119f4d.json`](../../sessions/d5/d51f10533566dd119f4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three tasks complete. Here's the summary:

**1. 新 ROC 图** — 已生成 2-panel 布局 (161 KB) 并覆盖旧图 `fig4_roc.png`。Panel A 展示 setting-level，Panel B 展示 subgroup-level，均含 Δπ-only（实线）和 Δπ×Δτ（虚线）对比。

**2. appendix.tex caption** — 已更新为 Δτ-free 诊断描述，AUC 数字与图一致。

**3. 一致性检查**:

| 位置 | 指标 | 写的值 | 数据值 | 状态 |
|------|------|--------|--------|------|
| experiments.tex:86 | Setting-level AUC | 0.89 | 0.889 | ✓ 一致 |
| experiments.tex:85 | Subgroup-level AUC | **0.83** | **0.865** | ⚠️ 不一致 |
| appendix.tex:245 | Setting-level AUC | 0.89 | 0.889 | ✓ 一致 |
| appendix.tex:245 | Subgroup-level AUC | 0.86 | 0.865 | ✓ 一致 |

**需要 Director 确认**: `experiments.tex:85` 写的 subgroup-level AUC = 0.83，但 diagnostic_revision 数据显示 0.865（appendix 图上显示 0.86）。可能原因：主文用了 LOO-CV AUC 而 appendix 数据用直接 AUC，或数据池不同。未修改，等确认。

---
