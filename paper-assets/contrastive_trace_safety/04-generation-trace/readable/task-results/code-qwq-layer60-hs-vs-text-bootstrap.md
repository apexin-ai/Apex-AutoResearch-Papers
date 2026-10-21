# code qwq layer60 hs vs text bootstrap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwq_layer60_hs_vs_text_bootstrap_20260517T133345_result.json`
- **Structured JSON:** [`70215eced77c7c62c89c.json`](../../sessions/70/70215eced77c7c62c89c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the complete summary:

## QwQ-32B Layer 60 HS vs Text Bootstrap Results

### HS Probe Metrics (Layer 60)

| W | HS bal_acc | HS prec | HS FPR | Coverage | Lead |
|---|-----------|---------|--------|----------|------|
| 1 | **0.739** | 0.658 | 0.123 | 0.737 | -1.4 |
| 3 | 0.726 | 0.622 | 0.142 | 0.789 | 1.1 |
| 5 | 0.731 | 0.638 | 0.133 | 0.789 | -0.1 |
| 10 | 0.726 | **0.671** | **0.108** | 0.789 | -1.0 |
| 15 | 0.733 | **0.688** | **0.102** | 0.632 | 1.0 |

### Paired Bootstrap (HS - Text, Bonferroni 0.0167)

| W | ba delta | ba p | prec delta | prec p | FPR delta | FPR p | sig |
|---|---------|------|-----------|--------|----------|-------|-----|
| 1 | +0.218 | <0.001 | +0.302 | <0.001 | -0.171 | <0.001 | **3/3** |
| 3 | +0.148 | <0.001 | +0.235 | <0.001 | -0.095 | 0.005 | **3/3** |
| 5 | +0.138 | <0.001 | +0.135 | 0.003 | -0.065 | 0.019 | 2/3 |
| 10 | +0.122 | <0.001 | +0.232 | 0.006 | -0.081 | 0.007 | **3/3** |
| 15 | +0.132 | <0.001 | +0.279 | <0.001 | -0.089 | 0.011 | **3/3** |

### Position Baseline
- Layer 60 position: bal_acc=0.746 > Best HS (W=1)=0.739 (delta=-0.007)
- Layer 2 position: 0.706 > HS=0.678

### Key Findings

1. **Layer 60 HS significantly outperforms text** across all 5 window sizes (14/15 metrics pass Bonferroni). This is a stark contrast to Layer 2 where 0/3 passed.

2. **Layer-selection dependent**: The QwQ-32B HS vs text comparison is definitively layer-dependent:
   - Layer 2 (3.2% depth): HS ≈ Text (delta=+0.9pp, p=0.828)
   - Layer 60 (95.2% depth): HS >> Text (delta=+12-22pp, all p<0.001)

3. **Position baseline still competitive**: Position (0.746) slightly exceeds best HS (0.739), consistent with the Layer 2 pattern (0.706 > 0.678). The position baseline's advantage is small and likely reflects the fixed commitment-point structure of the dataset.

4. **Precision gains are largest**: HS precision (0.66-0.69) vs text (0.39-0.46) shows the biggest deltas (+13-30pp), meaning the HS probe makes far fewer false positive predictions when it does predict "committed."

Results JSON saved to: `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_qwq_layer60_bootstrap/results.json`

---
