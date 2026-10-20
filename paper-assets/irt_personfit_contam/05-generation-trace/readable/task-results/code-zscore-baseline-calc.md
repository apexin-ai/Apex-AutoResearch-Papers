# code zscore baseline calc

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_zscore-baseline-calc_20260521T133219_result.json`
- **Structured JSON:** [`dd316825d4211df45839.json`](../../sessions/dd/dd316825d4211df45839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了所有需要的数据。Registry 中 `exp-baseline-comparison` 有 HT d（仅 Qwen contam_15=3.21）。

汇总对比表：

| Model | Condition | n_clean | acc_clean_mean | acc_contam | z_score | lz\*_d | HT_d |
|-------|-----------|---------|---------------|------------|---------|--------|------|
| **Qwen** | contam_15 | 10 | 0.6775 | 0.7310 | **34.93** | 6.575 | 3.21 |
| **Qwen** | contam_50 | 10 | 0.6775 | 0.7644 | **56.70** | 1.897 | — |
| **Llama** | contam_15 | 7 | 0.5948 | 0.6654 | **21.79** | 2.34 | — |
| **Llama** | contam_50 | 7 | 0.5948 | 0.6983 | **31.95** | 2.56 | — |
| **Mistral** | contam_15 | 3 | 0.5326 | 0.5949 | **3.81** | 1.20 | — |
| **Mistral** | contam_50 | 3 | 0.5326 | 0.6732 | **8.61** | 1.73 | — |

关键观察：

1. **acc z-score 对 n_clean 极度敏感**：Qwen/Llama 的 z 值膨胀到 20-57，因为 clean seed 间 accuracy 方差极小（sd=0.0015~0.003）。Mistral 因仅 3 个 seed（sd=0.016）z 值相对正常。
2. **z-score vs lz\* d 量级不可比**：z-score 衡量的是 accuracy 偏离，lz\* d 衡量的是 person-fit 统计量的效应量。z 值越大说明 accuracy baseline 方差越小（检测越容易），但不代表方法更好。
3. **lz\* 的优势在 contam_50**：Qwen contam_50 的 lz\* d 仅 1.897（inverted-U 效应），而 z-score 却最大（56.70）。这说明高污染率下 accuracy 持续上升但 lz\* 信号反而减弱——accuracy z-score 无法捕捉 inverted-U 现象。

---
