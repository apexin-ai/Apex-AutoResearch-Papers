# writing paper atlas results method

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-atlas-results-method_20260515T145251_result.json`
- **Structured JSON:** [`e0a6ea2683faf93d389b.json`](../../sessions/e0/e0a6ea2683faf93d389b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有改动已确认正确。

## 修改汇总

### atlas.tex (Task 1 — D024/D027 EDD 连续衰减叙事)
- **Cross-model EDD 段落** (L77-81): 扩展了三处
  1. d3v4 添加 "only Pythia achieves conventional significance, yet all three exhibit the same directional pattern"——避免过强的 "all significant" 措辞
  2. d4v5 从 "range 0.681--0.694" 改为逐模型报告 (Pythia 0.683, OLMo 0.694, GPT-2 XL 0.681)
  3. 新增跨模型 EDD threshold sensitivity 句：三模型在 T=0.65/0.70/0.75/0.80 下 EDD 完全一致 (5/4/4/3)
- EDD sensitivity table、d0-d5 AUC 衰减曲线、Pythia CI 等已有内容确认准确无误

### method.tex (Task 2 — 基准构建确认)
- **无需修改**。unconditional generation (L33)、reference model spec (L37-40，GPT-2 base 124M)、cross-model LOO circularity discussion (L39-40) 均已到位且准确

### generalization.tex (Task 3 — Per-class recall + Baseline 重构 + RoBERTa overlap)
- **Cross-strategy per-class recall** (L94, 新增): "d0 recall ≥89.5% inflating headline; d2 recall 3.7–19%"——补齐 W6 对 cross-strategy LOO 的 per-class disclosure
- **RoBERTa feature overlap** (L106-107, 替换原 DeBERTa-only 句): 双架构报告 DeBERTa ρ=-0.484 + RoBERTa ρ=-0.456, top-5 overlap=0, "architecture-independent finding" 结论
- **Baseline 叙事** (L9-12, L35): 确认已反映 D022/D023（RF≈CORAL≈DivEye 统计不可区分, all >> CE-MLP, 贡献在特征非分类器）——无需改动
- **Cross-model LOO per-class recall table** (L50-67): 确认已包含 d0/d1/d2/d3 recall 列，数值与 registry 一致

---
