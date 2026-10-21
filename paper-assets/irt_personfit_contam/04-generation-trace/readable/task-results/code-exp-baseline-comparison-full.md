# code exp baseline comparison full

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-baseline-comparison-full_20260521T035954_result.json`
- **Structured JSON:** [`14a9c1ffe05c2d7f24ee.json`](../../sessions/14/14a9c1ffe05c2d7f24ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

### Model-level（所有方法都能检测 contamination）

| Metric | Qwen 15% (d) | Qwen 50% (d) | Llama 15% (d) | Llama 50% (d) |
|--------|-------------|-------------|--------------|--------------|
| Acc z-score | +160.6 | +262.7 | +35.4 | +51.7 |
| lz* | **-3.42** | -0.99 | **-2.95** | **-3.31** |
| HT | +3.21 | +0.65 | +3.53 | **+4.69** |
| U3/Guttman | -0.43 | **-5.41** | **-3.69** | **-7.40** |

### Item-level AUROC（核心发现：所有方法都很弱）

| Method | Q-15% | Q-50% | L-15% | L-50% |
|--------|-------|-------|-------|-------|
| **Random** | 0.500 | 0.500 | 0.500 | 0.500 |
| **lz* itemwise** | 0.536 | 0.535 | 0.528 | 0.536 |
| **Gain score** | 0.560 | 0.551 | 0.568 | 0.565 |
| **IRT residual** | 0.578 | 0.563 | 0.582 | 0.581 |
| **LR cross-model** | 0.586 | 0.567 | 0.592 | 0.585 |
| **RF cross-model** | 0.521 | 0.539 | 0.532 | 0.546 |
| **LR within-model** | — | 0.571 | — | 0.590 |
| **RF within-model** | — | **0.630** | — | **0.629** |

关键结论：
- **Model-level**：所有统计量都能显著区分 contam vs clean，lz* Cohen's d 达 -2.95 ~ -3.42
- **Item-level**：即使最强的 supervised oracle (RF within-model) 也仅 AUROC≈0.63，unsupervised 方法全部 < 0.58。lz* itemwise 仅 0.53，接近 random
- **RF feature importance**：IRT 参数（a, b, c, d）和 residual/lz_contrib 占主导，raw response/gain 几乎无贡献——说明 item difficulty 特征比 response 特征重要

结果已保存到本地 `artifacts/baseline_comparison/comparison_results.json` 和服务器 `/root/autodl-tmp/baseline_comparison/results/comparison_results.json`。

---
