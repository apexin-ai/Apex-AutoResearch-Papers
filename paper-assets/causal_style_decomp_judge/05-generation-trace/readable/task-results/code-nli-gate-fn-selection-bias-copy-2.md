# code nli gate fn selection bias

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nli_gate_fn_selection_bias_20260521T103855_result.json`
- **Structured JSON:** [`c1f3505781886f273d9e.json`](../../sessions/c1/c1f3505781886f273d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

## NLI Gate Selection Bias 结果

### Formality (N=355, pass=323, fail=32)

| Metric | Pass (mean±std) | Fail (mean±std) | U p-val | Cohen's d | Direction |
|--------|----------------|-----------------|---------|-----------|-----------|
| Norm. Edit Distance | 0.3676±0.1826 | 0.3967±0.1882 | 0.2315 | +0.159 | fail>pass |
| Char Diff (abs) | 99.14±148.31 | 55.00±70.62 | 0.0743 | -0.308 | pass>fail |
| Char Diff (rel) | 0.1529±0.2423 | 0.2360±0.2618 | 0.1134 | +0.340 | fail>pass |
| Token Diff (abs) | 9.89±14.63 | 5.13±6.31 | 0.0748 | -0.338 | pass>fail |
| Token Diff (rel) | 0.1104±0.2187 | 0.1280±0.1304 | 0.3233 | +0.083 | fail>pass |
| **BLEU Score** | 0.3608±0.2811 | 0.2352±0.1588 | **0.0183** | -0.461 | **fail&lt;pass** * |
| **TF-IDF Cosine** | 0.6903±0.2108 | 0.5578±0.2426 | **0.0016** | -0.620 | **fail&lt;pass** * |

→ **CONSERVATIVE bias**: fail 组 BLEU 和 TF-IDF 显著更低（style 变化更大），gate 过滤了大幅改变的 pairs。

### Verbosity (N=100, pass=39, fail=61)

| Metric | Pass (mean±std) | Fail (mean±std) | U p-val | Cohen's d | Direction |
|--------|----------------|-----------------|---------|-----------|-----------|
| **Norm. Edit Distance** | 0.5284±0.1785 | 0.6901±0.2204 | **0.0002** | +0.788 | **fail>pass** * |
| Char Diff (abs) | 425.82±358.64 | 660.20±606.30 | 0.0744 | +0.447 | fail>pass |
| **Char Diff (rel)** | 1.5275±3.8904 | 8.0421±20.9924 | **0.0002** | +0.392 | **fail>pass** * |
| Token Diff (abs) | 69.10±53.74 | 104.90±91.99 | 0.1018 | +0.451 | fail>pass |
| **Token Diff (rel)** | 1.6978±4.9306 | 6.0196±13.9881 | **0.0003** | +0.380 | **fail>pass** * |
| **BLEU Score** | 0.2187±0.1655 | 0.1315±0.1589 | **0.0014** | -0.540 | **fail&lt;pass** * |
| **TF-IDF Cosine** | 0.6753±0.1812 | 0.4914±0.2498 | **0.0003** | -0.815 | **fail&lt;pass** * |

→ **CONSERVATIVE bias (强信号)**: 5/7 metrics 显著，fail 组在所有指标上都显示更大的 style 变化。TF-IDF cosine 效应量 d=−0.815 达到 large。

### Register (N=100, pass=80, fail=20)

| Metric | Pass (mean±std) | Fail (mean±std) | U p-val | Cohen's d | Direction |
|--------|----------------|-----------------|---------|-----------|-----------|
| Norm. Edit Distance | 0.4462±0.1659 | 0.4534±0.3221 | 0.2193 | +0.035 | fail>pass |
| Char Diff (abs) | 114.63±158.12 | 153.40±254.59 | 0.4377 | +0.214 | fail>pass |
| Char Diff (rel) | 0.2519±0.3360 | 2.1833±6.6139 | 0.6853 | +0.660 | fail>pass |
| Token Diff (abs) | 10.18±14.75 | 13.45±17.65 | 0.9793 | +0.213 | fail>pass |
| Token Diff (rel) | 0.1527±0.2230 | 1.8563±6.4736 | 0.6531 | +0.596 | fail>pass |
| BLEU Score | 0.2578±0.2394 | 0.3049±0.4001 | 0.1513 | +0.170 | pass<fail |
| TF-IDF Cosine | 0.6050±0.1990 | 0.5467±0.3463 | 0.4586 | -0.248 | fail<pass |

→ **无显著 selection bias** (0/7 显著)，但 fail 样本仅 20 个，统计效力有限。

## 结论

Gate **确实**系统性过滤了 style 变化较大的 pairs，尤其在 **verbosity**（5/7 显著，d 最大 0.815）和 **formality**（2/7 显著，BLEU 和 TF-IDF）上。Register 未检测到显著差异（可能受限于 n=20 的统计效力）。

这意味着我们报告的 bias 效应是 **保守估计（lower bound）**——真实的 style bias 可能比我们测到的更大。这对 Reviewer R3-W8 的担忧是一个正面回应：bias 确实存在，而且我们的方法低估了它。

脚本和 violin plots 已保存：
- 脚本: `csd_pipeline/nli_fn_selection_bias.py`
- 图表: `artifacts/nli_fn_bias/nli_fn_bias_{formality,verbosity,register}.png`

---
