# check review exp a status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_review-exp-a-status_20260515T124250_result.json`
- **Structured JSON:** [`82f8950c3f34133ccf6c.json`](../../sessions/82/82f8950c3f34133ccf6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Exp A 完成。结果汇总：

## Exp A: 4-Baseline Ensemble LOGO 对比（6-gen, n=27529）

| Group | Features | Avg F1 | 95% CI |
|-------|----------|--------|--------|
| **(a) 4-baseline** | avg_logprob, ld_score, fastdetectgpt, binoculars | **0.7964** | [0.7921, 0.8007] |
| **(b) 4-baseline+surface** | above + ttr, hapax_ratio | **0.8049** | [0.8003, 0.8092] |
| **(c) 7-feature unified** | entropy_{mean,std,min,max}, tail_decay, ttr, hapax | **0.7887** | [0.7839, 0.7930] |
| **(d) 7-feature original** | same as (c), same hyperparams | **0.7887** | [0.7839, 0.7930] |

Per-generator F1（最难的 qwen3-8b 和最易的 pythia-1b）：

| Generator | (a) 4-baseline | (b) +surface | (c) 7-feature |
|-----------|---------------|-------------|--------------|
| pythia-1b | 0.837 | 0.848 | **0.853** |
| qwen3-0.6b | 0.825 | **0.838** | 0.823 |
| qwen3-1.7b | 0.822 | **0.838** | 0.806 |
| pythia-2.8b | 0.802 | 0.805 | 0.804 |
| olmo-2-1b | **0.779** | 0.778 | 0.765 |
| qwen3-8b | 0.713 | **0.722** | 0.682 |

关键发现：
- **(c)=(d)**：unified 和 original 超参完全相同，结果一致（sanity check pass）
- **(b) > (a) > (c)**：加 surface features（ttr+hapax）能显著提升 baseline ensemble，但 7-feature depth-only 的表现略低于 4-baseline detector ensemble
- **4-baseline+surface (0.805)** 和 **7-feature (0.789)** 的 CI 不重叠，差异显著
- qwen3-8b 始终是最难的 generator，7-feature 对它的 F1 仅 0.682

---
