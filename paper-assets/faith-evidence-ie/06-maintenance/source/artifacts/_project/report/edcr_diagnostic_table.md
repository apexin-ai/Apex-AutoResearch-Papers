# EDCR Cross-Method Diagnostic Table

All metrics sourced from project registry. Sorted by rel_f1 descending.

| Method | exp_id | rel_f1 | evi_f1 | EDCR | n_pred | P | R | Δrel_f1 | Δevi_f1 |
|--------|--------|--------|--------|------|--------|------|------|---------|---------|
| CED reranker | mvp2_ced_reranker_poc | 0.4864 | 0.8188 | 0.6156 | 14782 | 0.4913 | 0.4815 | +0.0807 | +0.0209 |
| RSFT-CED s43 | mvp2_eval_rsft_s43_r2 | 0.4683 | 0.8156 | 0.6388 | 14970 | 0.4817 | 0.4556 | +0.0626 | +0.0177 |
| RSFT-CED s44 | mvp2_rsft_train_r1_s44 | 0.4655 | 0.8087 | 0.6350 | — | — | — | +0.0598 | +0.0108 |
| bf16 GRPO ckpt-100 | plan_011_grpo_g8_bf16_eval | 0.4549 | 0.8086 | 0.6318 | 10701 | — | — | +0.0492 | +0.0107 |
| flat-NLI RSFT | eval_plan_001_flat_nli | 0.4539 | 0.8043 | 0.6431 | 15294 | 0.4671 | 0.4414 | +0.0482 | +0.0064 |
| RSFT-CED r1 s42 | mvp2_eval_rsft_r1 | 0.4449 | 0.8187 | 0.6565 | 15307 | — | — | +0.0392 | +0.0208 |
| SFT baseline | mvp2_eval_sft_baseline | 0.4057 | 0.7979 | 0.7118 | 12234 | — | — | — | — |
| QLoRA GRPO step-100 | mvp2_eval_ced_kl001_r4_step100 | 0.2167 | 0.5746 | 0.8539 | 7460 | 0.2849 | 0.1749 | −0.1890 | −0.2233 |
| DPO | plan_012_dpo_ced | — | — | — | — | — | — | — | — |
| SFT-no-evidence | eval_plan_014_sft_no_evidence | — | — | — | — | — | — | — | — |

**Notes:**
- Δrel_f1 and Δevi_f1 are relative to SFT baseline (mvp2_eval_sft_baseline).
- DPO: status ANALYZING, no eval metrics yet.
- SFT-no-evidence: eval status RUNNING, pending.
- RSFT-CED s44 metrics recorded under training exp_id (eval was killed); n_pred/P/R not available.
- RSFT-CED r1 s42 and bf16 GRPO: precision/recall not recorded as separate fields in registry.
- QLoRA GRPO: catastrophic collapse (rel_f1=0.2167), included for diagnostic contrast.

## RSFT-CED 3-seed summary (s42/s43/s44)

| Seed | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| 42 | 0.4449 | 0.8187 | 0.6565 |
| 43 | 0.4683 | 0.8156 | 0.6388 |
| 44 | 0.4655 | 0.8087 | 0.6350 |
| **Mean** | **0.4596** | **0.8143** | **0.6434** |
| **Std** | **0.0127** | **0.0052** | **0.0111** |

## bf16 GRPO checkpoint trajectory (from eval_grpo_g8_bf16)

| Checkpoint | rel_f1 | evi_f1 | EDCR |
|------------|--------|--------|------|
| ckpt-80 | 0.4456 | 0.8034 | 0.6409 |
| ckpt-90 | 0.4523 | 0.8052 | 0.6414 |
| ckpt-100 | 0.4549 | 0.8086 | 0.6318 |
