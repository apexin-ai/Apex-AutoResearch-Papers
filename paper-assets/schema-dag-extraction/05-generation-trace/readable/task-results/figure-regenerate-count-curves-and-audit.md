# figure regenerate count curves and audit

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_regenerate_count_curves_and_audit_20260515T225822_result.json`
- **Structured JSON:** [`e99edbaba635c9c73d7f.json`](../../sessions/e9/e99edbaba635c9c73d7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

---

## 任务 1：fig_count_curves.pdf ✓

- 在 FewRel RE panel (b) 加入 `count_40=0.588` 数据点（位于 32→64 之间）
- 其他所有数据点未变
- PDF 已重新生成：`/root/schema-dag-extraction/figures/paper/fig_count_curves.pdf` (29619 bytes, valid)
- 脚本副本：`/root/schema-dag-extraction/scripts/gen_fig_count_curves.py`

## 任务 2：图表审计

`/root/schema-dag-extraction/figures/paper/` 中共 2 个图表：

| 文件 | 状态 | 说明 |
|------|------|------|
| `fig_count_curves.pdf` | ✓ 已更新 | 加入 count_40 点 |
| `fig_error_taxonomy.pdf` | ⚠️ 可能需更新 | 当前仅含 Qwen3 数据。exp012 LLaMA 跨模型 BCS 效应 (count_8 Δ=-27.1pp, count_16 Δ=-24.0pp) 可作为补充 panel 或在文字中引用，但图表本身是 error distribution by BCS bin，不是 count curve，LLaMA 数据加入方式取决于论文叙事选择 |

**无其他图表文件。** 如果论文需要 cross-model comparison figure（如 Qwen3 vs LLaMA BCS degradation 对比图），需要新建。当前 figures/paper/ 没有这类图表。

---
