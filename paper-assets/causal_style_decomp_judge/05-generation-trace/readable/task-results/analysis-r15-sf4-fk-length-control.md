# analysis r15 sf4 fk length control

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15-sf4-fk-length-control_20260523T061120_result.json`
- **Structured JSON:** [`39ee94e97eb00ad70cf0.json`](../../sessions/39/39ee94e97eb00ad70cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存并注册。核心发现：

**描述性统计**：
- Verbosity rewrites: ΔFK = +2.26 (d=0.50), Δsentence_length = +3.40 words/sent (d=0.35)
- Formality rewrites: ΔFK = −0.30 (d=−0.08), Δsentence_length = −0.11 (d=−0.04) — 几乎无变化

**回归分析**：
- Model 1 (无控制): `style_axis` β=2.56, p<0.001, R²=0.09
- Model 2 (控制句长): `style_axis` β=1.04, p=0.013; `delta_sentlen` β=0.43, p<0.001; R²=0.59
- 系数缩减 **59.3%**，R² 从 0.09 跳到 0.59

**Mediation 分析**：
- Sobel z=3.36, p<0.001，59.3% 的 FK 效应通过句长中介
- 相关系数: verbosity 轴内 Δsentlen↔ΔFK r=0.88

**结论**：FK cross-axis contamination 的主要成因是句长变化（59% mediated），但仍有残余直接效应显著 (p=0.013)——可能来自 verbose 改写引入的多音节填充词。这支持论文中"FK 依赖句子长度"的归因，同时也应承认存在约 41% 的非句长因素。

---
