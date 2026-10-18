# check submission format

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_submission-format_20260522T034259_result.json`
- **Structured JSON:** [`ade8a96a2e9aca20c414.json`](../../sessions/ad/ade8a96a2e9aca20c414.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Check 1: 字体
- 所有字体嵌入: **✓**（26 个字体全部 emb=yes）
- Type 3 字体: **无** ✓
- CID TrueType 字体: 有（DejaVuSans 系列 × 4，来自 matplotlib 图表），ACL 不禁止但少数旧系统兼容性略差——**低风险**

## Check 2: ACL 模板 & 匿名性
- review 模式: **✓**（`\usepackage[review]{acl}`）
- 匿名 author: **✓**（`\author{Anonymous}`）
- Self-citation 泄露: **无** ✓
- 暴露 URL: **无** ✓
- `\aclfinalcopy`: **未出现** ✓

## Check 3: Figure 分辨率
- 矢量图/高分辨率: **✓**（2 个 figure 均为 PDF 矢量格式）
  - `fig1_decoupling_hero.pdf` — 41KB, 矢量
  - `fig2_task_specificity.pdf` — 77KB, 矢量
- 低分辨率文件: **无**
- PDF 内嵌光栅图: **无**（pdfimages 输出为空）

## Check 4: 交叉引用完整性
- 悬空引用: **无** ✓
- 孤儿 label（定义但未引用）: **17 个**
  - sections: `sec:experiments`, `sec:method`, `ssec:convergence_metrics`, `ssec:model_zoo`, `ssec:per_example_decomposition`, `ssec:robustness`, `ssec:statistical_methods`
  - appendix: `app:arceasy`, `app:benchmark_details`, `app:cross_scale`, `app:per_example_counts`, `app:transformer_entrainment`
  - tables: `tab:attn_entropy`, `tab:cross_scale_jaccard`, `tab:scale_comparison`, `tab:subsample`, `tab:winogrande_multiplicity`
- 编译 warning: **无** ✓

## Check 5: 页数
- 总页数: **17**
- 主文（Introduction → Conclusion）: **~7 页** ✓（限制 8）
- Limitations + Ethics + References: 第 7–8 页（不计入页数限制）
- Appendix: 第 9–17 页（不计入页数限制）

---

**总结: 格式合规，无阻断问题。** 唯一值得注意的是 17 个孤儿 label——不影响提交，但若需要引用这些 section/table/appendix，可以补上 `\ref{}`；若确认不需要，可清理掉多余的 `\label{}`。

---
