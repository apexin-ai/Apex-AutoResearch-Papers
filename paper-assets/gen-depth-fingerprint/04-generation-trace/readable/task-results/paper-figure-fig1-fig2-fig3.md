# paper figure fig1 fig2 fig3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_fig2_fig3_20260515T045043_result.json`
- **Structured JSON:** [`1b5dad7b623e200539a6.json`](../../sessions/1b/1b5dad7b623e200539a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用，跳过注册。

## 结果汇总

### Figure 1: Differential Depth Response
- **路径**: `/root/gen-depth-fingerprint/figures/paper/fig1_differential_response.{png,pdf}`
- **脚本**: `/root/gen-depth-fingerprint/scripts/plot_fig1.py`
- **内容**: 2×2 multi-panel, 6 generators, depths 0–4, bootstrap 95% CI bands
- **关键发现**:
  - (a)(b) entropy_mean 和 hapax_ratio 随 depth 单调下降，所有 generator 一致
  - Qwen3-8B 衰减最小（entropy delta = −1.09 vs 其他 −1.40~−1.65）
  - (c)(d) entropy_std 和 tail_decay 近似平稳，drift 量级比 (a)(b) 小 10–15×

### Figure 2: LOGO Classification Performance
- **路径**: `/root/gen-depth-fingerprint/figures/paper/fig2_logo_performance.{png,pdf}`
- **脚本**: `/root/gen-depth-fingerprint/scripts/plot_fig2.py`
- **内容**: grouped bar chart, 6 held-out generators, 4 类别 (macro/gen-0/gen-1/gen-2+), bootstrap CI error bars
- **关键发现**:
  - LOGO 总均值 = 0.789
  - Pythia-1B 泛化最佳 (0.856), Qwen3-8B 最难 (0.683)
  - Gen-0 (human) 检测一致高 (>0.86), Gen-1 是瓶颈 (0.54–0.71)

### Figure 3: Baseline Comparison (Forest Plot)
- **路径**: `/root/gen-depth-fingerprint/figures/paper/fig3_baseline_comparison.{png,pdf}`
- **脚本**: `/root/gen-depth-fingerprint/scripts/plot_fig3.py`
- **内容**: 4 methods, dot + bootstrap 95% CI (粗线) + per-generator range (细线)
- **关键发现**:
  - 7-Feature Ensemble: **0.798** [0.793, 0.803]
  - Avg Log-Prob: 0.759 [0.753, 0.764]
  - FastDetectGPT: 0.731 [0.725, 0.737]
  - Entropy Mean: 0.593 [0.587, 0.599]
  - 所有 bootstrap CI 不重叠，差异显著
- **缺失**: LD-Score（无公开实现）和 Binoculars（GPU 内存限制）未实验，数据不可用

---
