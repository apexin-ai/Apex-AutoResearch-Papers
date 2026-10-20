# paper compile check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_check_20260523T105538_result.json`
- **Structured JSON:** [`fe594688ba741d040f87.json`](../../sessions/fe/fe594688ba741d040f87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 编译结果汇报

### 编译状态
- **Errors: 0** — 编译成功
- **总页数: 17 页**
- **Warnings: 10** — 全部是 `'h' float specifier changed to 'ht'`（无害，LaTeX 自动调整浮动位置）
- **Undefined references: 0**

### B1: 训练动力学图
- `fig_training_dynamics.pdf` 在 `sections/experiments.tex:41` 中被引用 ✅
- 文件存在于 `../figures/paper/fig_training_dynamics.pdf` ✅

### D: 附录 H-K 扩展
- **不存在 Appendix H、I、J、K 章节** ❌
- 当前附录有 10 个 section（A–J 按字母顺序）：Training Configuration, Loss Formulation Search, Instruction Retention Details, Long-Conversation AR Evaluation, Statistical Test Details, Llama-3.1-8B Complete Results, Additional Visualizations, Per-Layer Gate Profile, Scheduled Sampling Implementation, Computational Cost Analysis, Qualitative Steering Examples

### 图表文件检查 — 全部 11 个 `\includegraphics` 引用的文件均存在 ✅

| 图表 | 位置 | 状态 |
|------|------|------|
| fig1_overview.pdf | 正文 (intro) | ✅ |
| fig2_training_pcgrad.pdf | 正文 (analysis) | ✅ |
| fig3_gate_shift.pdf | 正文 (analysis) | ✅ |
| fig_training_dynamics.pdf | 正文 (experiments) | ✅ |
| fig4_attention_heatmap.pdf | 正文 (experiments) | ✅ |
| fig5_attention_steering.pdf | 正文 (experiments) | ✅ |
| fig_gate_profile_heatmap.pdf | 附录 (viz) | ✅ |
| fig_gate_profile_crossmodel.pdf | 附录 (viz) | ✅ |
| fig_ar_gar_perturn.pdf | 附录 (viz) | ✅ |
| fig_gate_distribution.pdf | 附录 (viz) | ✅ |
| fig_training_loss_curves.pdf | 附录 (viz) | ✅ |

---
