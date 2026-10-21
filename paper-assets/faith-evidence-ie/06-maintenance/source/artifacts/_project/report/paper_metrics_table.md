# FREIGE Paper Main Table — Eval Metrics Summary

Generated: 2026-05-16

All metrics in %, from `metrics_v2.json` unless noted. Eval on DocRED dev set.

## Baselines

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| SFT baseline (no-quant) | 42 | 41.06 | 41.98 | 40.19 | 80.13 | 40.36 | `sft_baseline_noquant` |
| SFT no-evidence | 42 | 48.93 | 48.84 | 49.02 | — | 47.36 | `sft_no_evidence` |

## CED RSFT (multi-seed)

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| CED RSFT r1 | 42 | 44.49 | 46.07 | 43.02 | 81.87 | 43.63 | `rsft_r1` |
| CED RSFT r2a | 42 | 44.94 | 45.12 | 44.75 | 81.08 | 44.01 | `rsft_r2a` |
| CED RSFT r2b | 42 | 44.93 | 45.66 | 44.24 | 81.28 | 44.10 | `rsft_r2b` |
| CED RSFT r2b (max1536) | 42 | 45.04 | 44.88 | 45.19 | 81.02 | 44.20 | `rsft_r2b_maxtok1536` |
| CED RSFT | 43 | 46.83 | 48.17 | 45.56 | 81.56 | 45.85 | `rsft_s43` |
| CED RSFT | 44 | 46.55 | 47.98 | 45.21 | 80.87 | 45.51 | `rsft_s44` |
| CED RSFT | 45 | — | — | — | — | — | `rsft_ced_s45` ⏳ PENDING |

## flat-NLI RSFT (multi-seed)

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| flat-NLI RSFT | 42 | 45.39 | 46.71 | 44.14 | 80.43 | 44.49 | `rsft_flat_nli` |
| flat-NLI RSFT | 43 | 45.23 | 46.73 | 43.83 | 81.58 | 44.35 | `rsft_flat_nli_s43_reeval` |
| flat-NLI RSFT ⚠️ | 44 | 46.15 | 47.79 | 44.62 | 81.31 | 46.15† | `rsft_flat_nli_s44` |
| flat-NLI RSFT | 45 | — | — | — | — | — | `rsft_flat_nli_s45` ⏳ PENDING |

> † `rsft_flat_nli_s44` only has `metrics.json` (no v2). Ign-F1 = F1 exactly, indicating the known ign_f1 bug. **Needs re-eval with v2 scorer.**

## RSFT Ablation

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| RSFT top_k=3 | 42 | 44.54 | 45.12 | 43.98 | 80.88 | 43.64 | `rsft_topk3_reeval` |

## DPO

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| DPO 1ep | 42 | 40.34 | 38.09 | 42.87 | 80.88 | 38.88 | `dpo_ced_1ep_fixed` |
| DPO 3ep | 42 | — | — | — | — | — | `dpo_ced_ckpt400` ⏳ PENDING |

## GRPO bf16 G=8 (checkpoint sweep)

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| GRPO bf16 G=8 step30 | 42 | 43.40 | 43.57 | 43.22 | 80.63 | 43.10 | `plan_011_bf16_g8_step30` |
| GRPO bf16 G=8 step50 | 42 | 42.76 | 46.23 | 39.77 | 80.24 | 42.77 | `plan_011_bf16_g8_step50` |
| GRPO bf16 G=8 step70 | 42 | 43.41 | 46.03 | 41.07 | 80.99 | 43.59 | `plan_011_bf16_g8_step70` |
| GRPO bf16 G=8 step80 | 42 | 44.56 | 49.39 | 40.59 | 80.34 | 44.67 | `grpo_g8_bf16/checkpoint-80` |
| GRPO bf16 G=8 step90 | 42 | 45.23 | 49.97 | 41.31 | 80.52 | 45.20 | `grpo_g8_bf16/checkpoint-90` |
| GRPO bf16 G=8 step100 | 42 | 45.49 | 50.42 | 41.45 | 80.86 | 45.59 | `grpo_g8_bf16/checkpoint-100` |

## QLoRA GRPO (kl=0.01, failed runs)

| Method | seed | F1 | P | R | Evi-F1 | Ign-F1 | Source Dir |
|--------|------|----|---|---|--------|--------|------------|
| QLoRA GRPO step10 | 42 | 0.30 | 0.31 | 0.28 | 72.00 | 0.30 | `grpo_ced_kl001/checkpoint-10` |
| QLoRA GRPO step50 | 42 | 15.63 | 23.56 | 11.69 | 56.43 | 15.46 | `grpo_ced_kl001/checkpoint-50` |
| QLoRA GRPO step100 | 42 | 21.67 | 28.49 | 17.49 | 57.46 | 21.53 | `grpo_ced_kl001_step100/checkpoint-100` |

---

## Status Summary

| Eval | Status |
|------|--------|
| CED RSFT s45 | ⏳ PENDING (dir empty) |
| flat-NLI RSFT s44 | ⚠️ metrics.json only, ign_f1 buggy — needs v2 re-eval |
| flat-NLI RSFT s45 | ⏳ PENDING (dir empty) |
| DPO 3ep | ⏳ PENDING (dir empty) |
| SFT (quantized baseline) | ⏳ No eval results (`sft/` dir empty) |
| SFT no-evidence no-quant | ⏳ No eval results (`sft_no_evidence_noquant/` dir empty) |

## Key Observations

1. **SFT no-evidence** achieves highest relation F1 (48.93) but produces no evidence — upper bound for relation-only extraction
2. **CED RSFT** best single-seed: s43 = 46.83 F1, s44 = 46.55 F1 (both outperform s42 rounds)
3. **flat-NLI RSFT** best: s44 = 46.15 F1 (pending v2 re-eval), s42 = 45.39 F1
4. **GRPO bf16 G=8** peaks at step100: 45.49 F1, with notably high precision (50.42) but lower recall (41.45)
5. **DPO 1ep**: underperforms SFT baseline (40.34 vs 41.06)
6. **QLoRA GRPO**: failed — max 21.67 F1 even at step100
7. **Evi-F1** consistent across methods at ~80-82%, except QLoRA GRPO and no-evidence
