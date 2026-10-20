# analysis alpha sweep a025 s44

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a025_s44_20260516T022550_result.json`
- **Structured JSON:** [`a807d74844ed9fa8b677.json`](../../sessions/a8/a807d74844ed9fa8b677.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下为分析摘要。

---

## α=0.25 s44 实验结果

| 指标 | gen0 | gen10 | drift% |
|------|------|-------|--------|
| token_entropy | 3.234 | 3.072 | **-5.01%** |
| ece | 0.0108 | 0.0180 | +67.0% |
| perplexity | 26.95 | 21.98 | **-18.4%** |
| distinct_1 | 0.0981 | 0.0588 | **-40.0%** |
| distinct_2 | 0.5132 | 0.2270 | **-55.8%** |
| distinct_3 | 0.8058 | 0.3364 | **-58.2%** |
| effective_rank | 46.61 | 44.35 | -4.85% |
| mauve | 0.0295 | 0.0175 | -40.7% |

## α=0.25 三 seed 汇总 (s42/s43/s44)

| 指标 drift% | s42 | s43 | s44 | **mean ± std** | dev<7%? |
|-------------|-----|-----|-----|---------------|---------|
| entropy | -4.10 | -5.00 | -5.01 | **-4.70 ± 0.52** | ✓ |
| ece | +79.7 | +98.6 | +67.0 | **+81.8 ± 15.9** | ✗ (ECE 本身噪声大) |
| perplexity | -17.2 | -18.7 | -18.4 | **-18.1 ± 0.80** | ✓ |
| distinct_1 | -40.3 | -40.5 | -40.0 | **-40.3 ± 0.25** | ✓ |
| distinct_2 | -57.1 | -56.4 | -55.8 | **-56.4 ± 0.67** | ✓ |
| distinct_3 | -59.9 | -58.7 | -58.2 | **-58.9 ± 0.86** | ✓ |

除 ECE 外所有指标 cross-seed std < 1%，远低于 7% 阈值，复现性极好。ECE 的高方差 (std=15.9%) 与已知的 ECE 在小样本下的噪声特性一致。

## α=0.25 collapse 模式概括

**Diversity collapse 显著但 entropy/ppl 变化温和**——与 α=0.50 和 α=1.00 形成清晰的剂量-效应梯度：

| 指标 | α=0.25 | α=0.50 (参考) | α=1.00 (参考) |
|------|--------|--------------|--------------|
| entropy drift | -4.7% | ~-8% | ~-15% |
| ppl drift | -18.1% | ~-25% | ~-40% |
| d1 drift | -40.3% | ~-55% | ~-75% |
| d3 drift | -58.9% | ~-72% | ~-88% |

α=0.25 呈现**选择性 collapse**：diversity 指标（d1/d2/d3）大幅下降 40-59%，但 token entropy 仅微降 ~5%、perplexity 下降 ~18%。这说明低污染条件下模型的生成多样性先于分布质量崩塌——n-gram 多样性是更敏感的 canary 指标。

---
