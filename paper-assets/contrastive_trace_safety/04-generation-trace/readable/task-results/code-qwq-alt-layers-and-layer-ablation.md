# code qwq alt layers and layer ablation

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwq_alt_layers_and_layer_ablation_20260517T131625_result.json`
- **Structured JSON:** [`659b7893fdcf00d7bea0.json`](../../sessions/65/659b7893fdcf00d7bea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments completed successfully. Here are the results:

---

## Task A: QwQ-32B Alternative Layer Probes

**95 traces, split 57/19/19 (train/val/test)**

| Layer | Depth% | Static bal_acc | Static precision | Temporal bal_acc | Temporal precision | Static pre_cp_fpr | Coverage |
|-------|--------|---------------|-----------------|-----------------|-------------------|------------------|----------|
| **2** (current) | 3.2 | 0.7298 | 0.5435 | 0.7135 | 0.5143 | 0.1850 | **0.4737** |
| 10 | 15.9 | 0.7101 | 0.5915 | 0.6669 | 0.5343 | 0.1338 | 0.3158 |
| 16 | 25.4 | 0.7000 | 0.6038 | 0.6913 | 0.6048 | 0.1386 | 0.2632 |
| 24 | 38.1 | 0.6969 | 0.6063 | 0.6878 | 0.5579 | 0.1086 | 0.1579 |
| 28 | 44.4 | 0.7150 | 0.5770 | 0.7001 | 0.5876 | 0.1398 | 0.3684 |
| 32 | 50.8 | 0.6923 | 0.5606 | 0.6987 | 0.5911 | 0.1556 | 0.2105 |
| 40 | 63.5 | 0.7094 | 0.5895 | 0.6997 | 0.5904 | 0.1418 | 0.3158 |
| 48 | 76.2 | 0.7232 | **0.6496** | 0.6844 | 0.6174 | 0.0915 | 0.2105 |
| 55 | 87.3 | 0.7270 | 0.6587 | 0.6957 | 0.6364 | 0.0935 | 0.2105 |
| **60** | 95.2 | **0.7473** | 0.6582 | **0.7211** | **0.6520** | 0.1023 | 0.3684 |

**Key findings:**
- Layer 60 has the **highest bal_acc** (static 0.7473, temporal 0.7211), surpassing L2 by +1.75pp/+0.76pp
- Layer 2's advantage is **coverage** (47.4% vs 36.8% for L60) due to earlier threshold crossing
- Later layers (L48-L60) have consistently better **precision** (0.65-0.66 vs 0.54 for L2) and lower **pre_cp_fpr** (0.09-0.10 vs 0.185)
- L2 selection reflects an **early-warning bias** from the old crossing-rate metric, not a classification error

---

## Task B: Layer Selection Metric Ablation

| Model | Metric | Selected Layer | bal_acc | precision | pre_cp_fpr |
|-------|--------|---------------|---------|-----------|-----------|
| **QwQ-32B** | bal_acc | L60 | 0.7473 | 0.6582 | 0.1023 |
| | bal_acc × crossing | **L2** | 0.7298 | 0.5435 | 0.1850 |
| | precision | L59 | 0.7435 | 0.6593 | 0.1012 |
| | pre_cp_fpr | L47 | 0.7218 | 0.6546 | 0.0895 |
| | composite | L60 | 0.7473 | 0.6582 | 0.1023 |
| **R1-32B** | bal_acc | L63 | 0.7552 | 0.5904 | 0.2335 |
| | bal_acc × crossing | **L10** | 0.7182 | 0.5490 | 0.2764 |
| | precision | L63 | 0.7552 | 0.5904 | 0.2335 |
| | pre_cp_fpr | L61 | 0.7312 | 0.5844 | 0.2102 |
| | composite | L63 | 0.7552 | 0.5904 | 0.2335 |
| **OT-7B** | bal_acc | L9 | 0.6825 | 0.4363 | 0.1186 |
| | bal_acc × crossing | L0 | 0.6677 | 0.3372 | 0.2197 |
| | precision | L19 | 0.6721 | 0.4418 | 0.1158 |
| | pre_cp_fpr | L18 | 0.6609 | 0.4255 | 0.1096 |
| | composite | L9 | 0.6825 | 0.4363 | 0.1186 |
| **R1-8B** | bal_acc | L12 | **0.7878** | 0.7039 | 0.0927 |
| | bal_acc × crossing | L0 | 0.7147 | 0.4816 | 0.1976 |
| | precision | L16 | 0.7776 | **0.7222** | **0.0809** |
| | pre_cp_fpr | L16 | 0.7776 | 0.7222 | 0.0809 |
| | composite | L16 | 0.7776 | 0.7222 | 0.0809 |

**Cross-metric consistency:**
- `qwq-32b`: L2 only selected by old metric; others select L47-L60 (VARIED)
- `r1-32b`: L10 only selected by old metric; others select L61-L63 (VARIED)
- `ot-7b`: 4 different layers selected; L16 (current) not top for any metric (VARIED)
- `r1-8b`: L12/L16 cluster; current L14 is close to the converging range (CONSISTENT)

---

**Conclusion for rebuttal:** QwQ's L2 selection is explained by the early-warning-optimized metric (bal_acc × crossing_rate). When this bias is removed, QwQ's optimal layer moves to L47-L60 (74-95% depth), consistent with other models' preference for mid-to-late layers. The L2 anomaly reflects a valid design choice (prioritizing early detection) rather than a methodological error.

Results saved to:
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_layer_ablation/qwq_alt_layers.json`
- `/root/autodl-tmp/contrastive_trace_safety/artifacts/exp_r3_layer_ablation/layer_metric_ablation.json`

---
