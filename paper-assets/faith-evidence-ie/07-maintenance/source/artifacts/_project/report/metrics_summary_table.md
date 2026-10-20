# FREIGE Experiment Metrics Summary

Generated: 2026-05-16

## Main Comparison Table (Full Dev Set, 985 docs)

| Method | Rel-F1 | Ign-F1 | Evi-F1 | EDCR | Source exp_id |
|--------|--------|--------|--------|------|---------------|
| **Baselines** | | | | | |
| DREEAM (RoBERTa-large, supervised) | 0.6357 | 0.6172 | 0.5401 | — | plan_004_dreeam_baseline |
| SFT baseline (no-quant) | 0.4106 | — | 0.8013 | 0.7039 | eval_sft_baseline_noquant |
| SFT baseline (mvp2 protocol) | 0.4057 | 0.4057 | 0.7979 | 0.7118 | mvp2_eval_sft_baseline |
| **Ablations** | | | | | |
| SFT no-evidence (rel-only) | 0.4893 | 0.4893 | — | — | eval_plan_014_sft_no_evidence |
| **CED RSFT (top_k=1)** | | | | | |
| — seed 42 | 0.4449 | 0.4449 | 0.8187 | 0.6565 | mvp2_eval_rsft_r1 |
| — seed 43 | 0.4683 | 0.4683 | 0.8156 | 0.6388 | mvp2_eval_rsft_s43_r2 |
| — seed 44 | 0.4655 | 0.4655 | 0.8087 | 0.6350 | mvp2_rsft_train_r1_s44 |
| — **mean +/- std** | **0.4596 +/- 0.0128** | **0.4596 +/- 0.0128** | **0.8143 +/- 0.0051** | **0.6434 +/- 0.0115** | 3 seeds |
| **CED RSFT ablations** | | | | | |
| RSFT top_k=3 | 0.4454 | 0.4364 | 0.8088 | 0.6635 | reeval_rsft_topk3 |
| RSFT r2a (1ep, alpha=128) | 0.4494 | 0.4494 | 0.8108 | 0.6641 | mvp2_eval_rsft_r2a |
| RSFT r2b (1ep, alpha=32) | 0.4493 | 0.4493 | 0.8128 | 0.6609 | mvp2_eval_rsft_r2b |
| **flat-NLI RSFT** | | | | | |
| — seed 42 | 0.4539 | 0.4539 | 0.8043 | 0.6431 | eval_plan_001_flat_nli |
| — seed 43 | 0.4523 | 0.4523 | 0.8158 | 0.6505 | reeval_flat_nli_s43 |
| — **mean +/- std** | **0.4531 +/- 0.0011** | **0.4531 +/- 0.0011** | **0.8101 +/- 0.0081** | **0.6468 +/- 0.0052** | 2 seeds |
| **CED Reranker (N=8, no fine-tuning)** | 0.4864 | — | 0.8188 | 0.6156 | mvp2_ced_reranker_poc |
| **GRPO bf16 LoRA** | | | | | |
| — ckpt-100 (pre-training SFT baseline) | 0.4549 | 0.4549 | 0.8086 | 0.6318 | eval_grpo_g8_bf16 |
| — ckpt-90 | 0.4523 | 0.4523 | 0.8052 | 0.6414 | eval_grpo_g8_bf16 |
| — ckpt-80 | 0.4456 | 0.4456 | 0.8034 | 0.6409 | eval_grpo_g8_bf16 |
| — step-30 | 0.4340 | — | 0.8063 | 0.6807 | plan_011_bf16_g8_step_eval |
| — step-50 | 0.4276 | — | 0.8024 | 0.6855 | plan_011_bf16_g8_step_eval |
| — step-70 (best after training) | 0.4341 | — | 0.8099 | 0.6685 | plan_011_bf16_g8_step_eval |
| **GRPO QLoRA 4-bit** | | | | | |
| — step-100 (last) | 0.2167 | 0.2167 | 0.5746 | 0.8539 | mvp2_eval_ced_kl001_r4_step100 |
| — step-90 (best reward) | 0.2108 | 0.2108 | 0.5666 | 0.8584 | mvp2_eval_ced_kl001_r4_step90 |
| — step-50 | 0.1563 | 0.1563 | 0.5643 | 0.8858 | mvp2_eval_ced_kl001_r4_early |
| **DPO + CED** | | | | | |
| — 1 epoch | 0.4034 | 0.4034 | 0.8088 | 0.7139 | eval_plan_012_dpo_1ep_fixed_r2 |
| — 3 epochs (overfitted) | 0.3429 | — | 0.8403 | 0.7294 | plan_012_dpo_ced |

## Notes

1. **DREEAM** uses RoBERTa-large (355M params) with supervised training on DocRED; not directly comparable to generative LLM approach (Qwen3-4B). Evi-F1 definition differs (token-level vs sentence-level).
2. **SFT no-evidence** outputs only relation triples without evidence; Evi-F1 and EDCR are N/A by design. Higher Rel-F1 (0.4893) quantifies the cost of joint evidence generation.
3. **CED Reranker** uses N=8 SFT generations at T=0.7 + CED scoring to select best candidate; no fine-tuning required. Oracle upper bound: Rel-F1=0.6237.
4. **GRPO bf16**: ckpt-100 (0.4549) is the pre-training SFT checkpoint, NOT a GRPO training result. Best after training is step-70 (0.4341, Δ=-2.08pp from baseline). No catastrophic forgetting but mild degradation throughout training (Rel-F1 range 0.4276–0.4341).
5. **GRPO QLoRA** exhibits catastrophic forgetting: Rel-F1 drops from SFT baseline 0.4057 to 0.2167 while Evi-F1 collapses from 0.7979 to 0.5746.
6. **DPO 3ep** shows overfitting (rewards_accuracy=1.0, margins=9.01); 1ep result matches SFT baseline (delta=-0.0023).
7. **EDCR** (Evidence-Document Confusion Ratio): lower is better. Strongly anti-correlated with Rel-F1 (Spearman r=-0.96, p<0.001).
8. **Ign-F1**: F1 ignoring relational facts shared between train and dev sets. For most experiments Ign-F1 = Rel-F1 (no overlap filtering applied); reeval_rsft_topk3 has corrected Ign-F1=0.4364.
