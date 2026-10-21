# ops exp020 metrics archive

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp020-metrics-archive_20260523T220704_result.json`
- **Structured JSON:** [`eadb572dc36d5ad5ad9b.json`](../../sessions/ea/eadb572dc36d5ad5ad9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON saved. Summary of exp_020 (GPT-2-medium, r=0, seed42) Gen 0-4:

| Gen | r_eff | log_det | PPL | D-4 | σ₁ | train_loss |
|-----|-------|---------|-----|-----|-----|------------|
| 0 | 23.09 | 689.4 | 15.45 | 0.913 | 6598 | — |
| 1 | 155.2 | 885.3 | 16.42 | 0.891 | 1463 | 2.358 |
| 2 | **185.4** | **924.4** | 18.94 | 0.868 | 1191 | 2.119 |
| 3 | 184.9 | 889.7 | 23.33 | 0.837 | 1172 | 2.052 |
| 4 | 169.6 | 817.6 | 32.11 | 0.764 | 1224 | 1.993 |

**Key pattern**: r_eff peaks at Gen 2 (185.4), begins reversal at Gen 3 — decompression peak consistent with Pythia-410M. σ₁ drops sharply from Gen 0 (6598→1463) then stabilizes. PPL and D-4 monotonically degrade.

**Missing data**: HellaSwag and alternative EWS (SLV/RankMe/isotropy) were not computed for this experiment — only available for exp_001 (Pythia-410M).

---
