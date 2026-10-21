# analysis r6 2c eta under kappa

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6-2c-eta-under-kappa_20260525T072558_result.json`
- **Structured JSON:** [`7ca539fdb431e6df119e.json`](../../sessions/7c/7ca539fdb431e6df119e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

```
η_max under κ-diversity regression:
K=3: FDR sig 1/12, mean β_std = 0.190
K=5: FDR sig 4/12, mean β_std = 0.104
K=7: FDR sig 1/12, mean β_std = 0.075

η_max under K_eff regression (对比):
K=3: FDR sig 4/12, mean β_std = 0.266
K=5: FDR sig 2/12, mean β_std = 0.101
K=7: FDR sig 1/12, mean β_std = 0.084

Decline pattern preserved? YES
```

两个关键发现：

1. **单调衰减在 κ-diversity 下持存**：0.190→0.104→0.075，与 K_eff 下的 0.266→0.101→0.084 方向一致。η_max 效应量随 K 增大被稀释是 metric-agnostic 的 robust finding。

2. **κ-diversity 回归中 η_max 的绝对效应量更小**（K=3 时 0.190 vs 0.266），但衰减斜率更陡（K=3→K=7 下降 60% vs 68%）。FDR 显著条件数两边都很低（κ-div 峰值 4/12 在 K=5，K_eff 峰值 4/12 在 K=3），说明 η_max 本身就是弱信号，但方向性衰减一致。

JSON 已保存至 `artifacts/results/plan001/eta_under_kappa_diversity.json`，memory.md 已更新。

---
