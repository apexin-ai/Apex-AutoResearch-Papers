# analysis bootstrap ci tg vs lora

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_tg_vs_lora_20260519T144212_result.json`
- **Structured JSON:** [`862df8a20f3a090ebfdf.json`](../../sessions/86/862df8a20f3a090ebfdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整了。

## Paired Bootstrap CI 结果

```
======================================================================
PAIRED BOOTSTRAP CONFIDENCE INTERVALS (n_boot=10000, seed=42)
======================================================================

## TG vs LoRA-only
GAR-ours:   mean_diff=+0.000644, 95% CI=[-0.001793, +0.003583], contains_0=True
GAR-Dongre: mean_diff=+0.002055, 95% CI=[+0.001788, +0.002279], contains_0=False
PPL:        mean_diff=-0.000349, 95% CI=[-0.005498, +0.004728], contains_0=True

## UG vs LoRA-only
GAR-ours:   mean_diff=+0.001931, 95% CI=[-0.000599, +0.004487], contains_0=True
GAR-Dongre: mean_diff=-0.000678, 95% CI=[-0.000819, -0.000564], contains_0=False
PPL:        mean_diff=-0.002988, 95% CI=[-0.009753, +0.003710], contains_0=True

## TG vs UG (bonus)
GAR-ours:   mean_diff=-0.001288, 95% CI=[-0.002986, +0.000634], contains_0=True
GAR-Dongre: mean_diff=+0.002733, 95% CI=[+0.002478, +0.002936], contains_0=False
PPL:        mean_diff=+0.002639, 95% CI=[-0.004074, +0.008228], contains_0=True
```

## 解读

**GAR-ours 和 PPL**：所有 CI 均包含 0，三种模型（TG/UG/LO）无统计显著差异 → 支持 "zero benefit" 结论。

**GAR-Dongre 的 "显著性" 需要谨慎对待**：
- 绝对差异极小（0.002 / 0.0007），在 mean≈0.015 的量级上
- paired diff 的 std 仅 0.0009（配对后方差极低），导致 CI 极窄
- TG > LO 但 UG < LO，方向不一致 → 不支持任何 "gating 有帮助" 的连贯叙事
- Cohen's d = 2.27 看起来大，但这是因为 Dongre 定义下 per-conversation GAR 本身量级很小、paired variance 几乎为零

**结论**：在主指标（GAR-ours, PPL）上，TG ≈ UG ≈ LO，三路等价，统计确认 gating 无额外收益。GAR-Dongre 的微小显著差异无实际意义且方向矛盾。

---
