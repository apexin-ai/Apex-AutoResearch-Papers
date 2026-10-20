# Paper Table 1: Complete Metrics Summary

Generated: 2026-05-16

## Main Table (Paper-ready methods)

| Method | Rel-F1 | Ign-F1 | Evi-F1 | EDCR | Evi-F1-Joint | Note |
|--------|--------|--------|--------|------|--------------|------|
| SFT baseline | 0.4106 | 0.4036 | 0.8013 | 0.7039 | 0.3216 | noquant, v2 |
| SFT no-evidence | 0.4893 | 0.4736 | — | — | — | noquant, v2 |
| RSFT-CED s43 | 0.4601 | 0.4512 | 0.8063 | 0.6542 | 0.3605 | D076, bs=4 |
| RSFT-CED s45 | 0.4514 | 0.4416 | 0.8174 | 0.6550 | 0.3558 | D076, bs=4 |
| **RSFT-CED (2-seed mean)** | **0.4557** | **0.4464** | **0.8118** | **0.6546** | **0.3581** | s42/s44 pending |
| RSFT-flatNLI s44 | 0.4615 | 0.4521 | 0.8131 | 0.6458 | 0.3597 | D076, bs=4 |
| RSFT-flatNLI s45 | 0.4551 | 0.4462 | 0.8154 | 0.6521 | 0.3556 | D076, bs=4 |
| **RSFT-flatNLI (2-seed mean)** | **0.4583** | **0.4491** | **0.8143** | **0.6490** | **0.3577** | s42/s43 pending |
| RSFT top-k=3 | 0.4454 | 0.4364 | 0.8088 | 0.6635 | 0.3478 | v2, bs=16 |
| CED-reranker (N=8) | 0.4864 | 0.4736 | — | — | — | rel metrics only |
| DPO-CED | 0.4034 | 0.3888 | 0.8088 | 0.7139 | 0.3069 | v2, 1ep |
| GRPO bf16 (ckpt100) | 0.4549 | 0.4559 | 0.8086 | 0.6318 | 0.3571 | G=8, v2 |
| GRPO QLoRA (ckpt100) | 0.2167 | 0.2153 | 0.5746 | 0.8539 | 0.1301 | **collapsed** |

## GRPO bf16 Trajectory

| Checkpoint | Rel-F1 | Ign-F1 | Evi-F1 | EDCR | Evi-F1-Joint |
|------------|--------|--------|--------|------|--------------|
| step 30 | 0.4340 | 0.4310 | 0.8063 | 0.6807 | 0.3396 |
| step 50 | 0.4276 | 0.4277 | 0.8024 | 0.6855 | 0.3300 |
| step 70 | 0.4341 | 0.4359 | 0.8099 | 0.6685 | 0.3396 |
| step 100 | 0.4549 | 0.4559 | 0.8086 | 0.6318 | 0.3571 |

## Pending Reevals (D076 Unified Protocol)

| Eval Dir | Method | Status |
|----------|--------|--------|
| rsft_ced_s42_reeval | RSFT-CED s42 | running |
| rsft_ced_s44_reeval | RSFT-CED s44 | running |
| rsft_flat_nli_s42_reeval | RSFT-flatNLI s42 | running |
| rsft_flat_nli_s43_reeval_r2 | RSFT-flatNLI s43 (bs=4 redo) | running |

## Key Observations

1. **RSFT-CED vs RSFT-flatNLI**: Very close on available seeds. CED slightly lower Rel-F1 but slightly better EDCR. Need all 4 seeds for definitive comparison.

2. **CED-reranker**: Best Rel-F1 (0.4864) but lacks evidence metrics in current eval format.

3. **GRPO bf16**: Rel-F1 peaks at ckpt100 (0.4549) but EDCR degrades steadily (0.6807→0.6318) — classic Rel-F1/EDCR tradeoff.

4. **DPO-CED**: Worst Rel-F1 among trained methods (0.4034, below SFT baseline) but best EDCR (0.7139). Severely under-recalled.

5. **GRPO QLoRA**: Completely collapsed. Not viable.

6. **SFT no-evidence**: Highest Rel-F1 (0.4893) but no evidence capability — confirms evidence generation is costly.

## Protocol Notes

- **D076 unified protocol**: bs=4, max_tokens=1024, no-quant, sft_adapter merged, dev split
- **v2 metrics**: Fixed Ign-F1 with doc_id-free train_facts
- Methods not re-evaluated under D076 (SFT baseline, DPO, GRPO bf16, RSFT top-k=3) used bs=16 but same metrics v2 computation

## Data Location

- Server JSON: `/root/autodl-tmp/eval_results/paper_table_data.json`
- All metrics from: `/root/autodl-tmp/eval_results/<method>/metrics_v2.json` (or metrics.json)
