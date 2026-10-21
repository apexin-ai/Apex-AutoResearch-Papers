# code llama fewnerd inference status v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_fewnerd_inference_status_v3_20260519T024716_result.json`
- **Structured JSON:** [`6c4130e35d10f8f1d991.json`](../../sessions/6c/6c4130e35d10f8f1d991.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the full report:

---

## LLaMA 3.1-8B FewNERD 3-Seed Results

**Tmux session**: `llama_fewnerd_infer` — DONE
**Test instances**: 37,648 total, 32,565 gold-filtered (per seed)
**Config**: N=8 stochastic (temp=1.0) + greedy (temp=0), 3 seeds

### Per-Seed Core Metrics

| Metric | Seed 42 | Seed 123 | Seed 456 | **3-seed Mean** | **Std** |
|--------|---------|----------|----------|-----------------|---------|
| Greedy F1 | 0.7841 | 0.7840 | 0.7844 | **0.7842** | 0.0002 |
| Oracle F1 | 0.8854 | 0.8839 | 0.8835 | **0.8843** | 0.0008 |
| Headroom (pp) | 10.13 | 9.99 | 9.91 | **10.01** | 0.09 |
| Degeneracy (%) | 27.32 | 24.63 | 18.13 | **23.36** | 3.86 |

### 5-Signal Selection F1 (delta vs greedy, pp)

| Signal | Seed 42 | Seed 123 | Seed 456 | **Mean delta** | **Mean F1** |
|--------|---------|----------|----------|----------------|-------------|
| LP | +0.34 | +0.37 | +0.36 | **+0.36** | 0.7877 |
| SJ | -0.06 | -0.41 | -1.08 | **-0.52** | 0.7790 |
| FK | -0.09 | -0.39 | -1.10 | **-0.53** | 0.7789 |
| EM | -0.46 | -0.99 | -1.62 | **-1.02** | 0.7739 |
| VC | -2.54 | -2.61 | -2.02 | **-2.39** | 0.7603 |

### Correlations (Spearman rho with sample quality)

| Signal | Seed 42 | Seed 123 | Seed 456 | **Mean rho** | **Std** |
|--------|---------|----------|----------|--------------|---------|
| EM | 0.4240 | 0.4136 | 0.4061 | **0.4146** | 0.0073 |
| FK | 0.4380 | 0.4083 | 0.3812 | **0.4092** | 0.0232 |
| SJ | 0.4234 | 0.3992 | 0.3508 | **0.3911** | 0.0302 |
| LP | 0.3639 | 0.3232 | 0.2611 | **0.3161** | 0.0423 |
| VC | 0.3543 | 0.3196 | 0.2743 | **0.3161** | 0.0328 |

### DGS (tau=0.05)

| Metric | Seed 42 | Seed 123 | Seed 456 | **Mean** |
|--------|---------|----------|----------|----------|
| DGS F1 | 0.7842 | 0.7809 | 0.7769 | **0.7807** |
| DGS gain (pp) | +0.01 | -0.31 | -0.75 | **-0.35** |

### Within-instance LP-F1 correlation

| Metric | Seed 42 | Seed 123 | Seed 456 |
|--------|---------|----------|----------|
| n (non-degenerate) | 23,668 | 24,544 | 26,662 |
| Median rho | 0.5879 | 0.5843 | 0.6070 |
| Mean rho | 0.3881 | 0.4081 | 0.4671 |
| LP range mean | 0.0573 | 0.0733 | 0.1070 |

---

### Comparison with Qwen FewNERD (4-seed mean)

| Metric | **LLaMA 3.1-8B** | **Qwen** | **Delta** |
|--------|-------------------|----------|-----------|
| Greedy F1 | 0.7842 | 0.7481 | **+3.61 pp** |
| Oracle F1 | 0.8843 | 0.8739 | **+1.04 pp** |
| Headroom | 10.01 pp | 12.58 pp | **-2.57 pp** |
| Degeneracy | 23.36% | 12.69% | **+10.67 pp** |
| LP delta | +0.36 pp | — | — |
| DGS delta | -0.35 pp | — | — |

### Key observations

1. **LLaMA greedy baseline significantly stronger** (+3.61 pp), leaving less headroom for self-consistency
2. **Degeneracy nearly doubled** (23.36% vs 12.69%) — LLaMA produces far more degenerate sample sets at temp=1.0
3. **LP is the only positive selection signal** (+0.36 pp); all structural/surface signals (SJ, FK, EM, VC) hurt performance
4. **DGS fails** (-0.35 pp) — the degeneracy gate doesn't help because even non-degenerate instances see structural signal failures
5. **LP correlation is the weakest across-instance signal** (rho=0.3161) but the **only one that translates to positive selection gain** — structural signals (EM rho=0.4146, FK rho=0.4092) have higher correlation but negative selection delta, suggesting they pick consistently wrong "high-agreement" samples over the greedy baseline

---
