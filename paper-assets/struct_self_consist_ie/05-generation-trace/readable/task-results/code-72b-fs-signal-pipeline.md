# code 72b fs signal pipeline

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_72b-fs-signal-pipeline_20260519T224957_result.json`
- **Structured JSON:** [`a97946fcb64fbab41319.json`](../../sessions/a9/a97946fcb64fbab41319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All pipeline steps done for SciERC and CoNLL. FewNERD at 91% (~30 min remaining).

---

## 72B Few-Shot Signal Results

### Full Signal Reports

#### SciERC (FS, N=8, 529 instances)
| Signal | ρ |
|--------|------|
| LP | 0.060 |
| SJ | 0.293 |
| FK | 0.301 |
| VC | 0.258 |
| EM | 0.205 |

- Greedy F1: 0.461 [0.435, 0.487]
- LP Selection F1: 0.448
- Majority Vote F1: 0.455
- Consensus LP-wt F1: 0.461
- Oracle F1: 0.604
- Degeneracy: 16.6% (constant-F1), 6.0% (entity-set)
- Construction Δ: **-0.08pp** (p=0.54, not significant)

#### CoNLL (FS, N=8, 2756 instances)
| Signal | ρ |
|--------|------|
| LP | 0.106 |
| SJ | 0.442 |
| FK | 0.451 |
| VC | 0.426 |
| EM | 0.403 |

- Greedy F1: 0.745 [0.731, 0.759]
- LP Selection F1: 0.747
- Majority Vote F1: 0.743
- Consensus LP-wt F1: 0.745
- Oracle F1: 0.796
- Degeneracy: 70.0% (constant-F1), 61.6% (entity-set)
- Construction Δ: **+0.03pp** (p=0.42, not significant)

---

### ZS vs FS Comparison

| Dataset | Metric | ZS | FS | Δ (FS−ZS) |
|---------|--------|----|----|-----------|
| **SciERC** | LP ρ | 0.081 | 0.060 | **-0.021** |
| | Degen% | 21.0% | 16.6% | **-4.4pp** (better) |
| | Construction Δ | +1.53pp | -0.08pp | **lost** |
| **CoNLL** | LP ρ | -0.002 | 0.106 | **+0.108** |
| | Degen% | 67.7% | 70.0% | +2.3pp |
| | Construction Δ | -0.37pp | +0.03pp | +0.40pp |

**Key findings:**
- **CoNLL LP ρ jumps from ~0 to 0.106** — few-shot examples make log-prob discriminative where ZS had zero signal
- SciERC LP ρ slightly decreases (0.081→0.060), and the ZS construction gain (+1.53pp) vanishes in FS
- SJ/FK/VC are all strong in FS for both datasets (0.26–0.45), same pattern as ZS
- Degeneracy is largely unchanged between regimes

---

### DATA dict entries (copy-paste ready)

```python
    # ── Qwen3-72B FS ──
    (72, "fs", "SciERC")          : {"lp_rho": 0.06, "sj_rho": 0.293, "vc_rho": 0.258, "degen": 16.6, "construction_lp_delta": -0.08, "greedy_f1": 0.461, "oracle_f1": 0.604},
    (72, "fs", "CoNLL")           : {"lp_rho": 0.106, "sj_rho": 0.442, "vc_rho": 0.426, "degen": 70.0, "construction_lp_delta": 0.03, "greedy_f1": 0.745, "oracle_f1": 0.796},
```

---

### FewNERD Status
91% done (273256/301184 prompts), ETA ~30 min. Will need a follow-up run of the same pipeline once it completes.

---
