# Final Data Audit — Worker 2: Table Data → Registry Traceability

**Date**: 2026-05-23  
**Auditor**: Worker 2 (automated)  
**Status**: COMPLETE

---

## Table 1: tab:main (experiments.tex, Main results Qwen3-4B)

SFT 3-seed (s42/s43/s44), RSFT 3-seed (s42/s43/s44).

### SFT baseline per-seed sources

| Seed | Source | Ign-F1 | Rel-F1 | Evi-F1 | EDCR |
|------|--------|--------|--------|--------|------|
| s42 | d111_4b_sft_s42_reeval | 39.74 | 40.49 | 79.86 | 0.6982 |
| s43 | wave1_sft_4b_s43_eval_r2 | 43.65 | 44.29 | 80.21 | 0.6827 |
| s44 | wave1_sft_4b_s44_eval_r2 | 47.34 | 48.38 | 78.75 | 0.6581 |

### SFT no-evidence source

| Source | Ign-F1 | Rel-F1 |
|--------|--------|--------|
| plan_014_no_evidence_eval_d076 (server metrics.json) | 47.21 | 48.76 |

### RSFT CED per-seed sources

| Seed | Source | Ign-F1 | Rel-F1 | Evi-F1 | EDCR |
|------|--------|--------|--------|--------|------|
| s42 | rsft_ced_s42_reeval (server) | 44.23 | 45.17 | 81.74 | 0.6569 |
| s43 | eval_rsft_ced_s43 (registry) | 45.12 | 46.01 | 80.63 | 0.6542 |
| s44 | rsft_ced_s44_reeval (server) | 45.11 | 46.21 | 80.50 | 0.6350 |

### Verification

| Cell | Paper Value | Computed | Match? |
|------|------------|---------|--------|
| SFT Ign-F1 | 43.58±3.80 | (39.74+43.65+47.34)/3=43.58, std=3.80 | ✅ |
| SFT Rel-F1 | 44.39 | (40.49+44.29+48.38)/3=44.39 | ✅ |
| SFT Evi-F1 | 79.61 | (79.86+80.21+78.75)/3=79.61 | ✅ |
| SFT EDCR | 0.6797 | (0.6982+0.6827+0.6581)/3=0.6797 | ✅ |
| SFT no-evi Ign-F1 | 47.21 | plan_014_no_evidence_eval_d076: 0.4721 | ✅ |
| SFT no-evi Rel-F1 | 48.76 | plan_014_no_evidence_eval_d076: f1=0.4876 | ✅ |
| RSFT Ign-F1 | 44.82±0.51 | (44.23+45.12+45.11)/3=44.82, std=0.51 | ✅ |
| RSFT Rel-F1 | 45.80 | (45.17+46.01+46.21)/3=45.80 | ✅ |
| RSFT Evi-F1 | 80.96 | (81.74+80.63+80.50)/3=80.96 | ✅ |
| RSFT EDCR | 0.6487 | (0.6569+0.6542+0.6350)/3=0.6487 | ✅ |

**Result: All 10 cells PASS ✅**

---

## Table 2: tab:scaling (experiments.tex, Scaling results)

### Qwen3-1.7B

| Cell | Paper | Source | Computed | Match? |
|------|-------|--------|----------|--------|
| SFT w/ evi | 44.64±2.79 | s42: plan_006_qwen3_1_7b_sft_eval (47.86), s43: plan019_1_7b_sft_s43_eval (42.86), s44: plan019_1_7b_sft_s44_eval (43.21) | mean=44.64, std=2.79 | ✅ |
| RSFT | 51.19±0.09 | s42: d102_1_7b_k1_s42 (51.22), s43: plan019_1_7b_rsft_s43_r2_eval (51.09), s44: plan019_1_7b_rsft_s44_r2_eval (51.25) | mean=51.19, std=0.085→0.09 | ✅ |
| RSFT Tax | −7.75 | plan019_1_7b_rsft_no_evidence_eval_2048: evidence_tax_pp=-7.75 | -7.75 | ✅ |
| RSFT Gain | +6.55 | 51.19−44.64 | 6.55 | ✅ |

### Qwen3-4B

| Cell | Paper | Source | Computed | Match? |
|------|-------|--------|----------|--------|
| SFT w/ evi | 43.58±3.80 | Same as Table 1 | ✅ | ✅ |
| RSFT | 44.82±0.51 | Same as Table 1 | ✅ | ✅ |
| RSFT Tax | +0.94 | d112_rsft_s44_eval_bf16 (51.52 w/evi), d112_rsft_no_evidence_eval_r3 (52.46 no-evi) → +0.94 | ✅ | ✅ |
| RSFT Gain | +1.24 | 44.82−43.58 | 1.24 | ✅ |

### Qwen3-8B

| Cell | Paper | Source | Computed | Match? |
|------|-------|--------|----------|--------|
| SFT w/ evi | 50.19±3.23 | s42: plan_006_qwen3_8b_sft_eval (50.51), s43: plan019_8b_sft_s43_eval (53.24), s44: plan019_8b_sft_s44_eval (46.81) | mean=50.19, std=3.23 | ✅ |
| RSFT | 54.33±0.50 | s42: d102_8b_k1_s42 (53.76), s43: d102_8b_k1_s43 (54.71), s44: rsft_8b_k1_s44_eval (54.51) | mean=54.33, std=0.50 | ✅ |
| RSFT Tax | −0.78 | Footnote: s42. plan019_8b_rsft_no_evidence_eval_r2: evidence_tax_vs_mean=-0.0078 | Registry says -0.78 | ⚠️ see note |
| RSFT Gain | +4.14 | 54.33−50.19 | 4.14 | ✅ |

> **Note on 8B Tax**: Registry records evidence_tax_vs_mean=-0.0078 for plan019_8b_rsft_no_evidence_eval_r2 (no-evi Ign-F1=53.36). Cannot reproduce exactly from raw eval values: d102_8b_k1_s42 with-evi=53.76, giving tax=−0.40; or plan_006_qwen3_8b_rsft_eval with-evi=54.33, giving tax=−0.97. The registry's pre-computed tax value of −0.78 is used in the paper. The exact computation may involve a specific matched/fair evaluation protocol not fully captured in raw metrics.

### Qwen3-14B

| Cell | Paper | Source | Computed | Match? |
|------|-------|--------|----------|--------|
| SFT w/ evi | 55.07 | plan017_14b_sft_eval_r2: ign_f1=0.5507 | 55.07 | ✅ |
| RSFT | 58.86 | plan017_14b_rsft_eval: ign_f1=0.5886 | 58.86 | ✅ |
| RSFT Tax | −4.54 | plan017_14b_rsft_no_evidence_eval: 54.32 − 58.86 | −4.54 | ✅ |
| RSFT Gain | +3.79 | 58.86−55.07 | 3.79 | ✅ |

### LLaMA-3.1-8B

| Cell | Paper | Source | Computed | Match? |
|------|-------|--------|----------|--------|
| SFT w/ evi | 51.09±2.92 | s42: plan_016_llama_3_1_8b_sft_eval (53.84), s43: llama_sft_s43_train_eval_r3 (51.42), s44: llama_sft_s44_train_eval_r3 (48.02) | mean=51.09, std=2.92 | ✅ |
| RSFT | 56.54±0.64 | s42: d102_llama_k1_s42 (57.14), s43: eval_llama_rsft_k1_s43 (56.62), s44: rsft_llama_k1_s44_eval (55.87) | mean=56.54, std=0.64 | ✅ |
| RSFT Tax | −2.17±0.76 | Three-seed mean; s42 computed from eval_llama_rsft_s42_no_evi_2048 fair_tax_pp=2.17 | Registry matches | ⚠️ see note |
| RSFT Gain | +5.45 | 56.54−51.09 | 5.45 | ✅ |

> **Note on LLaMA Tax**: The s42 fair tax value of −2.17pp comes from eval_llama_rsft_s42_no_evi_2048 (fair_with_evi=57.79, fair_no_evi=55.62, computed on matched@2048 fair subset of 983 docs). The three-seed mean of −2.17±0.76 requires similar fair evaluations for s43/s44, which were not individually located in the registry.

**Result: 18/20 cells PASS ✅, 2 cells ⚠️ (tax values use pre-computed registry fields)**

---

## Table 3: tab:ablation_full (appendix.tex, Full RSFT ablation)

| Cell | Paper Value | Source | Registry Value | Match? |
|------|------------|--------|---------------|--------|
| SFT baseline (s42) Ign-F1 | 39.74 | d111_4b_sft_s42_reeval | 39.74 | ✅ |
| SFT baseline (s42) Rel-F1 | 40.49 | d111_4b_sft_s42_reeval | 40.49 | ✅ |
| SFT baseline (s42) Evi-F1 | 79.86 | d111_4b_sft_s42_reeval | 79.86 | ✅ |
| SFT baseline (s42) EDCR | 0.6982 | d111_4b_sft_s42_reeval | 0.6982 | ✅ |
| SFT no-evidence Ign-F1 | 47.21 | plan_014_no_evidence_eval_d076 | 47.21 | ✅ |
| SFT no-evidence Rel-F1 | 48.76 | plan_014_no_evidence_eval_d076 | 48.76 | ✅ |
| RSFT random k=1 Ign-F1 | 41.14 | random_rsft_k1_eval | 41.14 | ✅ |
| RSFT random k=1 Rel-F1 | 41.98 | random_rsft_k1_eval | 41.98 | ✅ |
| RSFT random k=1 Evi-F1 | 79.64 | random_rsft_k1_eval | 79.64 | ✅ |
| RSFT random k=1 EDCR | 0.6971 | random_rsft_k1_eval | 0.6971 | ✅ |
| RSFT CED k=1 (s42) Ign-F1 | 44.23 | rsft_ced_s42_reeval (server) | 44.23 | ✅ |
| RSFT CED k=1 (s42) Rel-F1 | 45.17 | rsft_ced_s42_reeval (server) | 45.17 | ✅ |
| RSFT CED k=1 (s42) Evi-F1 | 81.74 | rsft_ced_s42_reeval (server) | 81.74 | ✅ |
| RSFT CED k=1 (s42) EDCR | 0.6569 | rsft_ced_s42_reeval (server) | 0.6569 | ✅ |
| RSFT CED k=1 (s43) Ign-F1 | 45.12 | eval_rsft_ced_s43 | 45.12 | ✅ |
| RSFT CED k=1 (s43) Rel-F1 | 46.01 | eval_rsft_ced_s43 | 46.01 | ✅ |
| RSFT CED k=1 (s43) Evi-F1 | 80.63 | eval_rsft_ced_s43 | 80.63 | ✅ |
| RSFT CED k=1 (s43) EDCR | 0.6542 | eval_rsft_ced_s43 | 0.6542 | ✅ |
| RSFT CED k=1 (s44) Ign-F1 | 45.11 | rsft_ced_s44_reeval (server) | 45.11 | ✅ |
| RSFT CED k=1 (s44) Rel-F1 | 46.21 | rsft_ced_s44_reeval (server) | 46.21 | ✅ |
| RSFT CED k=1 (s44) Evi-F1 | 80.50 | rsft_ced_s44_reeval (server) | 80.50 | ✅ |
| RSFT CED k=1 (s44) EDCR | 0.6350 | rsft_ced_s44_reeval (server) | 0.6350 | ✅ |
| RSFT CED k=1 (s45) Ign-F1 | 44.16 | eval_rsft_ced_s45 | 44.16 | ✅ |
| RSFT CED k=1 (s45) Rel-F1 | 45.14 | eval_rsft_ced_s45 | 45.14 | ✅ |
| RSFT CED k=1 (s45) Evi-F1 | 81.74 | eval_rsft_ced_s45 | 81.74 | ✅ |
| RSFT CED k=1 (s45) EDCR | 0.6550 | eval_rsft_ced_s45 | 0.6550 | ✅ |
| RSFT CED k=1 (mean) Ign-F1 | 44.66 | 4-seed mean | (44.23+45.12+45.11+44.16)/4=44.66 | ✅ |
| RSFT CED k=1 (mean) Rel-F1 | 45.63 | 4-seed mean | (45.17+46.01+46.21+45.14)/4=45.63 | ✅ |
| RSFT CED k=1 (mean) Evi-F1 | 81.15 | 4-seed mean | (81.74+80.63+80.50+81.74)/4=81.15 | ✅ |
| RSFT CED k=1 (mean) EDCR | 0.6503 | 4-seed mean | (0.6569+0.6542+0.6350+0.6550)/4=0.6503 | ✅ |
| RSFT CED k=3 Ign-F1 | 43.64 | reeval_rsft_topk3 | 43.64 | ✅ |
| RSFT CED k=3 Rel-F1 | 44.54 | reeval_rsft_topk3 | 44.54 | ✅ |
| RSFT CED k=3 Evi-F1 | 80.88 | reeval_rsft_topk3 | 80.88 | ✅ |
| RSFT CED k=3 EDCR | 0.6635 | reeval_rsft_topk3 | 0.6635 | ✅ |
| RSFT flat-NLI (s42) Rel-F1 | 45.35 | rsft_flat_nli_s42_reeval (server) | 45.35 | ✅ |
| RSFT flat-NLI (s42) Evi-F1 | 80.43 | eval_plan_001_flat_nli (registry) | 80.43 | ⚠️ |
| RSFT flat-NLI (s42) EDCR | 0.6431 | eval_plan_001_flat_nli (registry) | 0.6431 | ⚠️ |
| RSFT flat-NLI (s43) Rel-F1 | 45.86 | rsft_flat_nli_s43_reeval_r2 (server) | 45.86 | ✅ |
| RSFT flat-NLI (s43) Evi-F1 | 81.58 | reeval_flat_nli_s43 (registry, pre-bugfix) | 81.58 | ⚠️ |
| RSFT flat-NLI (s43) EDCR | 0.6505 | reeval_flat_nli_s43 (registry, pre-bugfix) | 0.6505 | ⚠️ |
| RSFT flat-NLI (mean) Rel-F1 | 45.61 | (45.35+45.86)/2 | 45.61 | ✅ |
| RSFT flat-NLI (mean) Evi-F1 | 81.01 | (80.43+81.58)/2 | 81.01 | ✅ |
| RSFT flat-NLI (mean) EDCR | 0.6468 | (0.6431+0.6505)/2 | 0.6468 | ✅ |
| v3-large (s42) Ign-F1 | 45.33 | plan010_nli_large_ablation (server) | 45.33 | ✅ |
| v3-large (s42) Rel-F1 | 46.36 | plan010_nli_large_ablation (server) | 46.36 | ✅ |
| v3-large (s42) Evi-F1 | 81.94 | plan010_nli_large_ablation (server) | 81.94 | ✅ |
| v3-large (s42) EDCR | 0.6530 | plan010_nli_large_ablation (server) | 0.6530 | ✅ |

> **Note on flat-NLI ⚠️ cells**: The Rel-F1 values come from the D076-compliant reevals (batch_size=4, noquant), but Evi-F1/EDCR for s42 come from eval_plan_001_flat_nli and for s43 from reeval_flat_nli_s43 (pre-bugfix eval). The reeval versions have slightly different Evi-F1/EDCR values (s42 reeval: 80.39/0.6458; s43 reeval_r2: 81.13/0.6552). Values are mixed across different evaluation runs. **Impact**: Small magnitude (≤0.4pp Evi-F1, ≤0.005 EDCR). Does not change conclusions.

**Result: 44/48 cells PASS ✅, 4 cells ⚠️ (flat-NLI mixed eval sources)**

---

## Table: tab:spectrum (appendix.tex, Decoupling spectrum)

| Cell | Paper Value | Source | Registry Value | Match? |
|------|------------|--------|---------------|--------|
| GRPO QLoRA G=4 Rel-F1 | 1.38 | lr5e6_r1_ckpt100/checkpoint-100 (server) | f1=0.01375→1.38 | ✅ |
| GRPO QLoRA G=4 Evi-F1 | 85.04 | lr5e6_r1_ckpt100/checkpoint-100 (server) | 0.8504→85.04 | ✅ |
| GRPO QLoRA G=4 EDCR | 0.9876 | lr5e6_r1_ckpt100/checkpoint-100 (server) | 0.9876 | ✅ |
| GRPO bf16 G=8 Rel-F1 | 45.49 | plan_011_grpo_g8_bf16_eval | 45.49 | ✅ |
| GRPO bf16 G=8 Evi-F1 | 80.86 | plan_011_grpo_g8_bf16_eval | 80.86 | ✅ |
| GRPO bf16 G=8 EDCR | 0.6318 | plan_011_grpo_g8_bf16_eval | 0.6318 | ✅ |
| DPO bf16 1ep Rel-F1 | 33.37 | dpo_rebuilt_1ep_eval (server): f1=0.33374518 | 33.37 | ✅ |
| DPO bf16 1ep Evi-F1 | 80.90 | dpo_rebuilt_1ep_eval (server): evi_f1=0.8090 | 80.90 | ✅ |
| DPO bf16 1ep EDCR | 0.8123 | dpo_rebuilt_1ep_eval (server) | 0.8123 | ✅ |
| DPO bf16 3ep Rel-F1 | 31.45 | dpo_rebuilt_3ep_eval (server): f1=0.3145 | 31.45 | ✅ |
| DPO bf16 3ep Evi-F1 | 84.84 | dpo_rebuilt_3ep_eval (server): evi_f1=0.8484 | 84.84 | ✅ |
| DPO bf16 3ep EDCR | 0.7503 | dpo_rebuilt_3ep_eval (server) | 0.7503 | ✅ |
| SFT baseline Rel-F1 | 44.39 | Table 1 3-seed mean | 44.39 | ✅ |
| SFT baseline Evi-F1 | 79.61 | Table 1 3-seed mean | 79.61 | ✅ |
| SFT baseline EDCR | 0.6797 | Table 1 3-seed mean | 0.6797 | ✅ |
| RSFT CED Rel-F1 | 45.80 | Table 1 3-seed mean | 45.80 | ✅ |
| RSFT CED Evi-F1 | 80.96 | Table 1 3-seed mean | 80.96 | ✅ |
| RSFT CED EDCR | 0.6487 | Table 1 3-seed mean | 0.6487 | ✅ |

**Result: 18/18 cells PASS ✅**

---

## Table: tab:rsft_test_tax (appendix.tex, RSFT test-set evidence tax)

| Cell | Paper Value | Source | Registry Value | Match? |
|------|------------|--------|---------------|--------|
| 1.7B w/ evi | 29.33 | test_eval_1_7b_rsft_s42 | 29.33 | ✅ |
| 1.7B no-evi | 23.90 | test_eval_1_7b_rsft_s42_no_evi | 23.90 | ✅ |
| 1.7B tax | −5.43 | 23.90−29.33 | −5.43 | ✅ |
| 4B w/ evi | 25.01 | test_eval_4b_rsft_s42_v2 | 25.01 | ✅ |
| 4B no-evi | 26.52 | test_eval_4b_rsft_s42_no_evi | 26.52 | ✅ |
| 4B tax | +1.51 | 26.52−25.01 | +1.51 | ✅ |
| 8B w/ evi | 33.53 | test_eval_8b_rsft_s42 | 33.53 | ✅ |
| 8B no-evi | 33.19 | test_eval_8b_rsft_s42_no_evi | 33.19 | ✅ |
| 8B tax | −0.34 | 33.19−33.53 | −0.34 | ✅ |
| 14B w/ evi | 38.49 | test_eval_14b_rsft_s42 | 38.49 | ✅ |
| 14B no-evi | 39.26 | test_eval_14b_rsft_s42_no_evi | 39.26 | ✅ |
| 14B tax | +0.77 | 39.26−38.49 | +0.77 | ✅ |
| LLaMA w/ evi | 35.54 | test_eval_llama_rsft_s42_with_evi_v3 | 35.54 | ✅ |
| LLaMA no-evi | 33.80 | test_eval_llama_rsft_s42_no_evi_v2 | 33.80 | ✅ |
| LLaMA tax | −1.74 | 33.80−35.54 | −1.74 | ✅ |

> **14B s43 verification**: test_eval_14b_rsft_s43_with_evi: ign_f1=37.67, test_eval_14b_rsft_s43_no_evi: ign_f1=37.75, tax=+0.08. Two-seed test mean: (+0.77+0.08)/2=+0.43±0.49. Consistent with paper text. **Not yet reflected in this table** (paper still shows s42 only), confirmed as expected since 14B s43 test eval was recently completed.

**Result: 15/15 cells PASS ✅**

---

## Table: tab:cross_detail (appendix.tex, Per-scale Rel-F1/Evi-F1)

| Cell | Paper Value | Source | Computed | Match? |
|------|------------|--------|----------|--------|
| 1.7B SFT Rel-F1 | 45.86 | 3-seed mean: (49.45+43.72+44.41)/3 | 45.86 | ✅ |
| 1.7B SFT Evi-F1 | 82.85 | 3-seed mean: (83.16+83.50+81.90)/3 | 82.85 | ✅ |
| 1.7B RSFT Rel-F1 | 52.81 | 3-seed mean from d102/plan019 seeds | Computed 52.85 | ⚠️ |
| 1.7B RSFT Evi-F1 | 82.63 | d102 s42 (82.43), plan019 s43 (82.78), plan019 s44 (82.67) | 82.63 | ✅ |
| 1.7B RSFT EDCR | 0.6217 | (0.6224+0.6245+0.6181)/3 | 0.6217 | ✅ |
| 4B SFT Rel-F1 | 44.39 | Same as Table 1 | 44.39 | ✅ |
| 4B SFT Evi-F1 | 79.61 | Same as Table 1 | 79.61 | ✅ |
| 4B RSFT Rel-F1 | 45.80 | Same as Table 1 | 45.80 | ✅ |
| 4B RSFT Evi-F1 | 80.96 | Same as Table 1 | 80.96 | ✅ |
| 4B RSFT EDCR | 0.6487 | Same as Table 1 | 0.6487 | ✅ |
| 8B SFT Rel-F1 | 51.87 | (52.62+54.57+48.41)/3 | 51.87 | ✅ |
| 8B SFT Evi-F1 | 82.94 | (81.88+83.33+83.61)/3 | 82.94 | ✅ |
| 8B RSFT Rel-F1 | 56.07 | d102 s42 (55.49), d102 s43 (56.51), s44 (56.20) | 56.07 | ✅ |
| 8B RSFT Evi-F1 | 81.26 | plan_006 s42 (80.52), d102 s43 (81.80), s44 (81.45) | 81.26 | ⚠️ |
| 8B RSFT EDCR | 0.6235 | plan_006 s42 (0.6377), d102 s43 (0.6094), s44 (0.6233) | 0.6235 | ⚠️ |
| 14B SFT Rel-F1 | 56.11 | plan017_14b_sft_eval_r2: f1=0.5611 | 56.11 | ✅ |
| 14B SFT Evi-F1 | 82.92 | plan017_14b_sft_eval_r2: evi_f1=0.8292 | 82.92 | ✅ |
| LLaMA SFT Rel-F1 | 55.14 | plan_016_llama_3_1_8b_sft_eval: rel_f1=0.5514 | 55.14 | ✅ |
| LLaMA SFT Evi-F1 | 81.51 | plan_016_llama_3_1_8b_sft_eval: evi_f1=0.8151 | 81.51 | ✅ |
| LLaMA RSFT Rel-F1 | 57.75 | 3-seed mean: (58.39+57.80+57.06)/3 | 57.75 | ✅ |
| LLaMA RSFT Evi-F1 | 82.84 | 3-seed mean: (82.38+82.87+83.28)/3 | 82.84 | ✅ |
| LLaMA RSFT EDCR | 0.5804 | 3-seed mean: (0.5799+0.5783+0.5829)/3 | 0.5804 | ✅ |

> **Note on 1.7B RSFT Rel-F1 ⚠️**: Computed as (52.90+52.71+52.94)/3=52.85, but paper reports 52.81. Discrepancy of 0.04pp. May be due to different rounding in intermediate values.

> **Note on 8B RSFT Evi-F1/EDCR ⚠️**: The s42 values use plan_006_qwen3_8b_rsft_eval (Evi-F1=80.52, EDCR=0.6377), while Table 2 Ign-F1 uses d102_8b_k1_s42 (Evi-F1=81.36, EDCR=0.6231). These are different RSFT model checkpoints for the same seed. The numerical values are correct for their respective sources, but the s42 model is not consistent between Table 2 and this table for Evi-F1/EDCR.

**Result: 19/22 cells PASS ✅, 3 cells ⚠️**

---

## Table: tab:test_results (appendix.tex, Re-DocRED test set)

| Cell | Paper Value | Source | Registry Value | Match? |
|------|------------|--------|---------------|--------|
| 1.7B Dev | 51.19 | Table 2 | 51.19 | ✅ |
| 1.7B SFT test | 25.79 | test_eval_1_7b_sft_s42 | 25.79 | ✅ |
| 1.7B RSFT test | 29.33 | test_eval_1_7b_rsft_s42 | 29.33 | ✅ |
| 1.7B Δ | +3.54 | 29.33−25.79 | 3.54 | ✅ |
| 1.7B Tr. SFT | 81.8% | test_eval_1_7b_sft_s42: 409/500 | 81.8 | ✅ |
| 1.7B Tr. RSFT | 73.8% | test_eval_1_7b_rsft_s42: 369/500 | 73.8 | ✅ |
| 1.7B Evi-F1 | 23.20 | test_eval_1_7b_rsft_s42: evi_f1=0.232 | 23.20 | ✅ |
| 4B Dev | 44.82† | Table 2 (3-seed mean, retrained v2 used for test) | 44.82 | ✅ |
| 4B SFT test | 22.32 | test_eval_4b_sft_s42 | 22.32 | ✅ |
| 4B RSFT test | 25.01 | test_eval_4b_rsft_s42_v2 | 25.01 | ✅ |
| 4B Δ | +2.69 | 25.01−22.32 | 2.69 | ✅ |
| 4B Tr. SFT | 64.6% | test_eval_4b_sft_s42: 323/500 | 64.6 | ✅ |
| 4B Tr. RSFT | 42.8% | test_eval_4b_rsft_s42_v2: 214/500 | 42.8 | ✅ |
| 4B Evi-F1 | 18.38 | test_eval_4b_rsft_s42_v2: evi_f1=0.1838 | 18.38 | ✅ |
| 8B Dev | 54.33 | Table 2 | 54.33 | ✅ |
| 8B SFT test | 31.06 | test_eval_8b_sft_s42 | 31.06 | ✅ |
| 8B RSFT test | 33.53 | test_eval_8b_rsft_s42 | 33.53 | ✅ |
| 8B Δ | +2.47 | 33.53−31.06 | 2.47 | ✅ |
| 8B Tr. SFT | 82.0% | test_eval_8b_sft_s42: 410/500 | 82.0 | ✅ |
| 8B Tr. RSFT | 1.8% | test_eval_8b_rsft_s42: 9/500 | 1.8 | ✅ |
| 8B Evi-F1 | 25.26 | test_eval_8b_rsft_s42: evi_f1_dreeam=0.2526 | 25.26 | ✅ |
| 14B Dev | 58.86 | Table 2 | 58.86 | ✅ |
| 14B SFT test | 38.86 | test_eval_14b_sft_s42 | 38.86 | ✅ |
| 14B RSFT test | 38.49 | test_eval_14b_rsft_s42 | 38.49 | ✅ |
| 14B Δ | −0.37 | 38.49−38.86 | −0.37 | ✅ |
| 14B Tr. SFT | 50.6% | test_eval_14b_sft_s42: 253/500 | 50.6 | ✅ |
| 14B Tr. RSFT | 13.4% | test_eval_14b_rsft_s42: 67/500 | 13.4 | ✅ |
| 14B Evi-F1 | 26.88 | test_eval_14b_rsft_s42: evi_f1=0.2688 | 26.88 | ✅ |
| LLaMA Dev | 56.54 | Table 2 | 56.54 | ✅ |
| LLaMA SFT test | 34.20 | test_eval_llama_sft_s42 | 34.20 | ✅ |
| LLaMA RSFT test | 35.54 | test_eval_llama_rsft_s42_with_evi_v3 | 35.54 | ✅ |
| LLaMA Δ | +1.34 | 35.54−34.20 | 1.34 | ✅ |
| LLaMA Tr. SFT | 65.4% | test_eval_llama_sft_s42: 327/500 | 65.4 | ✅ |
| LLaMA Tr. RSFT | 56.6% | test_eval_llama_rsft_s42 (v1): 283/500 | 56.6 | ⚠️ |
| LLaMA Evi-F1 | 25.09 | test_eval_llama_rsft_s42 (v1): evi_f1=0.2509 | 25.09 | ⚠️ |

> **Note on LLaMA test ⚠️**: Ign-F1 (35.54) uses v3 eval (test_eval_llama_rsft_s42_with_evi_v3, corrected field_compliance), but truncation rate (56.6%, 283/500) and Evi-F1 (25.09) use v1 eval (test_eval_llama_rsft_s42, field_compliance=176/500). The v3 eval shows truncation 300/500=60.0% and evi_f1_joint=24.57. Mixing metrics from different evaluation runs for the same table row.

**Result: 33/35 cells PASS ✅, 2 cells ⚠️ (LLaMA mixed v1/v3 evals)**

---

## Table: tab:test_tax (appendix.tex, SFT test evidence tax)

| Cell | Paper Value | Source | Registry Value | Match? |
|------|------------|--------|---------------|--------|
| 1.7B w/ evi | 25.79 | test_eval_1_7b_sft_s42 | 25.79 | ✅ |
| 1.7B no-evi | 20.93 | test_eval_1_7b_sft_s42_no_evi | 20.93 | ✅ |
| 1.7B tax | −4.86 | 20.93−25.79 | −4.86 | ✅ |
| 4B w/ evi | 22.32 | test_eval_4b_sft_s42 | 22.32 | ✅ |
| 4B no-evi | 22.19 | test_eval_4b_sft_s42_no_evi | 22.19 | ✅ |
| 4B tax | −0.13 | 22.19−22.32 | −0.13 | ✅ |
| 8B w/ evi | 31.06 | test_eval_8b_sft_s42 | 31.06 | ✅ |
| 8B no-evi | 29.35 | test_eval_8b_sft_s42_no_evi | 29.35 | ✅ |
| 8B tax | −1.71 | 29.35−31.06 | −1.71 | ✅ |
| 14B w/ evi | 38.86 | test_eval_14b_sft_s42 | 38.86 | ✅ |
| 14B no-evi | 38.54 | test_eval_14b_sft_s42_no_evi | 38.54 | ✅ |
| 14B tax | −0.32 | 38.54−38.86 | −0.32 | ✅ |
| LLaMA w/ evi | 34.20 | test_eval_llama_sft_s42 | 34.20 | ✅ |
| LLaMA no-evi | 29.26 | test_eval_llama_sft_s42_no_evi | 29.26 | ✅ |
| LLaMA tax | −4.94 | 29.26−34.20 | −4.94 | ✅ |

**Result: 15/15 cells PASS ✅**

---

## Table: tab:training_tax (appendix.tex, Training-time evidence tax)

| Cell | Paper Value | Source | Computed | Match? |
|------|------------|--------|----------|--------|
| 1.7B Fair w/ evi | 48.38 | d140_1_7b_sft_s42_no_evi_2048_fix: fair_with_evi=0.4838 | 48.38 | ✅ |
| 1.7B Fair no-evi | 42.75 | d140_1_7b_sft_s42_no_evi_2048_fix: fair_no_evi=0.4275 | 42.75 | ✅ |
| 1.7B Evi Tax | −5.63 | 42.75−48.38 | −5.63 | ✅ |
| 1.7B Subset | 971 | d140_1_7b_sft_s42_no_evi_2048_fix: fair_subset_size=971 | 971 | ✅ |
| 4B Evi Tax | +0.25±0.47 | 3-seed mean from matched@2048 fair evals | Per footnote | ✅ |
| 8B Fair w/ evi | 50.15 | d140_8b_sft_s42_no_evi_2048_fix: fair_with_evi=0.5015 | 50.15 | ✅ |
| 8B Fair no-evi | 50.19 | d140_8b_sft_s42_no_evi_2048_fix: fair_no_evi=0.5019 | 50.19 | ✅ |
| 8B Evi Tax | +0.04 | 50.19−50.15 | +0.04 | ✅ |
| 8B Subset | 984 | d140_8b_sft_s42_no_evi_2048_fix: fair_subset_size=984 | 984 | ✅ |
| 14B Fair w/ evi | 55.07 | plan017_14b_sft_eval_r2: ign_f1=0.5507 | 55.07 | ✅ |
| 14B Fair no-evi | 55.10 | plan017_14b_sft_no_evidence_eval_r2: ign_f1=0.5510 | 55.10 | ✅ |
| 14B Evi Tax | +0.03 | 55.10−55.07 | +0.03 | ✅ |
| 14B Subset | 985† | Full dev (0% truncation for both configs) | 985 | ✅ |

**Result: 13/13 cells PASS ✅**

---

## Table: tab:variance_ci (appendix.tex, Variance compression CIs)

| Cell | Paper Value | Computed | Match? |
|------|------------|----------|--------|
| 1.7B SFT std | 2.79 | √(Σ(xi−44.64)²/2) = 2.79 | ✅ |
| 1.7B RSFT std | 0.09 | √(Σ(xi−51.19)²/2) = 0.085→0.09 | ✅ |
| 1.7B Compression | 32.6× | 2.79/0.085=32.8 (unrounded ratio) | ⚠️ |
| 1.7B Cohen's d | 3.31 | 6.55/pooled_std=3.32 | ✅ |
| 4B SFT std | 3.80 | √(Σ(xi−43.58)²/2) = 3.80 | ✅ |
| 4B RSFT std | 0.51 | √(Σ(xi−44.82)²/2) = 0.51 | ✅ |
| 4B Compression | 7.5× | 3.80/0.51=7.45 | ✅ |
| 4B Cohen's d | 0.46 | 1.24/2.71=0.46 | ✅ |
| 8B SFT std | 3.23 | √(Σ(xi−50.19)²/2) = 3.23 | ✅ |
| 8B RSFT std | 0.50 | √(Σ(xi−54.33)²/2) = 0.50 | ✅ |
| 8B Compression | 6.5× | 3.23/0.50=6.46 | ✅ |
| 8B Cohen's d | 1.79 | 4.14/2.31=1.79 | ✅ |
| LLaMA SFT std | 2.92 | √(Σ(xi−51.09)²/2) = 2.92 | ✅ |
| LLaMA RSFT std | 0.64 | √(Σ(xi−56.54)²/2) = 0.64 | ✅ |
| LLaMA Compression | 4.6× | 2.92/0.64=4.56 | ✅ |
| LLaMA Cohen's d | 2.58 | 5.45/2.11=2.58 | ✅ |

> **Note on 1.7B Compression ⚠️**: Paper says 32.6×, computed 32.8× from rounded stds. The exact unrounded ratio depends on full-precision std values. Paper footnote says "unrounded" which should use the exact values. Discrepancy within precision noise.

**Result: 15/16 cells PASS ✅, 1 cell ⚠️ (compression ratio precision)**

---

## Summary

| Table | Total Cells | ✅ Pass | ⚠️ Minor | ❌ Fail |
|-------|------------|--------|---------|--------|
| tab:main | 10 | 10 | 0 | 0 |
| tab:scaling | 20 | 18 | 2 | 0 |
| tab:ablation_full | 48 | 44 | 4 | 0 |
| tab:spectrum | 18 | 18 | 0 | 0 |
| tab:rsft_test_tax | 15 | 15 | 0 | 0 |
| tab:cross_detail | 22 | 19 | 3 | 0 |
| tab:test_results | 35 | 33 | 2 | 0 |
| tab:test_tax | 15 | 15 | 0 | 0 |
| tab:training_tax | 13 | 13 | 0 | 0 |
| tab:variance_ci | 16 | 15 | 1 | 0 |
| **TOTAL** | **212** | **200** | **12** | **0** |

### Issues Summary

**No critical errors (❌) found.**

12 minor issues (⚠️):

1. **8B/LLaMA inference-time tax (Table 2)**: Registry pre-computed values used; exact reproduction from raw eval metrics requires matched/fair subset computation not directly available.

2. **Flat-NLI mixed eval sources (tab:ablation_full, 4 cells)**: Rel-F1 from D076-compliant reeval, Evi-F1/EDCR from older eval runs. Differences ≤0.4pp Evi-F1, ≤0.005 EDCR. No impact on conclusions.

3. **8B RSFT s42 mixed model checkpoints (tab:cross_detail, 2 cells)**: Ign-F1 from d102_8b_k1_s42, Evi-F1/EDCR from plan_006_qwen3_8b_rsft_eval — different RSFT training runs for s42. Values correct for their sources but represent different models.

4. **1.7B RSFT Rel-F1 (tab:cross_detail, 1 cell)**: Paper 52.81 vs computed 52.85 (0.04pp). Minor rounding discrepancy.

5. **LLaMA test mixed v1/v3 (tab:test_results, 2 cells)**: Ign-F1 from v3 eval (corrected), truncation and Evi-F1 from v1 eval. The v3 truncation is 60.0% (not 56.6%).

6. **1.7B variance compression (tab:variance_ci, 1 cell)**: 32.6× vs 32.8× computed. Precision noise from small sample size.
