# ssh 7b urgent pipeline execution

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_7b-urgent-pipeline-execution_20260520T042302_result.json`
- **Structured JSON:** [`0b6672ae804c14735610.json`](../../sessions/0b/0b6672ae804c14735610.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## Qwen2.5-7B FT FewNERD N=8 — 3-Seed Results

### Per-Seed + Aggregated Metrics

| Metric | seed42 | seed123 | seed456 | **Mean ± Std** |
|--------|--------|---------|---------|----------------|
| LP ρ | 0.3221 | 0.3538 | 0.3629 | **0.346 ± 0.021** |
| SJ ρ | 0.3554 | 0.3979 | 0.4105 | **0.388 ± 0.029** |
| VC ρ | 0.3930 | 0.4067 | 0.4118 | **0.404 ± 0.010** |
| Degen% | 31.1% | 32.8% | 31.3% | **31.7% ± 0.9%** |
| Greedy F1 | 0.7851 | 0.7850 | 0.7825 | **0.784 ± 0.001** |
| Oracle F1 | 0.8718 | 0.8777 | 0.8771 | **0.876 ± 0.003** |
| Construction LP Δ (pp) | −0.40 | −0.03 | +0.09 | **−0.11 ± 0.25** |

### DATA dict entry (copy-paste for plot_scaling_curve.py)

```python
DATA[(7, "ft", "FewNERD")] = {
    "lp_rho": 0.346,   # mean ± 0.021
    "sj_rho": 0.388,   # mean ± 0.029
    "vc_rho": 0.404,   # mean ± 0.010
    "degen": 31.7,      # mean ± 0.9
    "construction_lp_delta": -0.11,  # mean ± 0.25
    "greedy_f1": 0.784, # mean ± 0.001
    "oracle_f1": 0.876, # mean ± 0.003
}
```

### Bootstrap Construction Test

| | seed123 | seed456 |
|---|---------|---------|
| Observed diff | −0.03pp | +0.09pp |
| 95% CI | [−0.16, +0.11] | [−0.09, +0.26] |
| p-value | 0.651 | 0.168 |
| Significant? | **NO** | **NO** |
| Cohen's d | −0.002 | 0.007 |

Both seeds confirm construction LP-weighted does not significantly improve over greedy for 7B FewNERD. The effect is near zero with inconsistent sign across seeds.

Note: seed42 bootstrap was skipped — no per-instance file available on either server (compute_signals was run in a previous session that didn't persist on 5090-b). Aggregated JSON saved to `output/fewnerd_7b/aggregated_3seed_scaling.json` on 5090-b.

---
