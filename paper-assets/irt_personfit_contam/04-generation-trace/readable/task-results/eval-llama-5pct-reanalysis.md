# eval llama 5pct reanalysis

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama-5pct-reanalysis_20260524T041247_result.json`
- **Structured JSON:** [`3bb0987ef9c764828c77.json`](../../sessions/3b/3bb0987ef9c764828c77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总结果：

### Llama 5% 完整指标表

| 指标 | Overall | Seen (702) | Unseen (13340) |
|------|---------|------------|----------------|
| **Accuracy** | 0.6379 | 0.8006 | 0.6294 |
| **lz\* (free-θ, MLE=-0.407)** | -4.6954 | -0.6101 | -4.3984 |
| **lz\* (fixed-θ=-0.102)** | -16.5919 | 2.7407 | -17.6451 |

### Cohen's d（vs clean baseline）

| 对比 | Clean baseline | Contam_5 值 | Cohen's d |
|------|---------------|-------------|-----------|
| **free-θ lz\*** | mean=8.684, sd=0.735 | -4.695 | **-18.20** |
| **fixed-θ lz\*** | mean=8.681, sd=0.685 | -16.592 | **-36.89** |

### 要点

- seen items 准确率 80.1% vs unseen 62.9%，差值 17.1pp，确认污染信号
- fixed-θ 的 lz\* 在 seen 子集上仍为正值 (2.74)，但 unseen 极端负值 (-17.65)，说明模型整体能力下降（θ_MLE=-0.41 远低于 clean 的 -0.10）
- fixed-θ Cohen's d 远大于 free-θ，因为 free-θ 的 MLE 会部分吸收能力偏移
- `theta_fixed_all_seeds.json` 已更新包含 contam_5
- 结果保存在 `results/llama/contam_5_full_analysis.json`

---
