# exp exp 060 analysis

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp_060_analysis_20260520T144620_result.json`
- **Structured JSON:** [`66b21d283bd549d4b97f.json`](../../sessions/66/66b21d283bd549d4b97f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_060 结果汇报

**Feature Extraction**: 2229 samples, 498 seeds, depth 分布 {0: 498, 1: 488, 2: 466, 3: 414, 4: 363}

**DDR Analysis — Qwen3-14B-Base (14.7B params)**:

| Feature | Spearman ρ | p-value | Cohen's d (gen0 vs gen≥2) | Group |
|---------|-----------|---------|---------------------------|-------|
| entropy_mean | −0.3877 | 7.06e-81 | +0.7765 | **drifting** |
| entropy_std | −0.0557 | 0.00851 | −0.0223 | stationary |
| entropy_max | +0.0791 | 0.000186 | −0.1717 | stationary |
| entropy_min | −0.2471 | 2.27e-32 | −0.1365 | stationary |
| ttr | −0.4916 | 5.48e-136 | +1.0913 | **drifting** |
| hapax_ratio | −0.5065 | 1.52e-145 | +1.1245 | **drifting** |
| tail_decay | −0.0637 | 0.00262 | +0.1356 | stationary |

**DDR pattern match: True** — entropy_mean/ttr/hapax_ratio 漂移，entropy_max/entropy_min/tail_decay 稳定，与预期一致。DDR pattern 在 14.7B 规模下 **CONFIRMED**。

结果已保存至 `results/exp_060_14b_ddr.json`。

---
