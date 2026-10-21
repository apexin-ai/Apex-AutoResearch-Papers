# FT (LoRA) Composability Bootstrap Significance Test

## Method
- Paired bootstrap test (n_bootstrap=10000, seed=42)
- Resample unit: sentence (SciERC, n=551) / document (DocRED, n=998)
- 95% percentile confidence interval
- Two-tailed p-value
- Comparison: constrained (full_s1) − unconstrained

## R-F1 Results (Primary Metric)

| Setting | Unconstrained R-F1 | Constrained R-F1 | ΔR-F1 (pp) | 95% CI | p-value | Sig |
|---------|-------------------|-----------------|-----------|--------|---------|-----|
| Qwen-LoRA-SciERC | 43.86% | 43.77% | −0.10 | [−0.30, +0.00] | 0.7260 | n.s. |
| Qwen-LoRA-DocRED | 40.97% | 40.60% | ���0.37 | [−0.76, ���0.05] | 0.0140 | * |
| Llama-LoRA-SciERC | 45.45% | 45.47% | +0.02 | [+0.00, +0.07] | 0.7364 | n.s. |
| Llama-LoRA-DocRED | 43.81% | 43.83% | +0.02 | [−0.15, +0.22] | 0.8506 | n.s. |

## E-F1 Results (Supplementary)

| Setting | Unconstrained E-F1 | Constrained E-F1 | ΔE-F1 (pp) | 95% CI | p-value | Sig |
|---------|-------------------|-----------------|-----------|--------|---------|-----|
| Qwen-LoRA-SciERC | 67.05% | 67.05% | +0.00 | [+0.00, +0.00] | 1.0000 | n.s. |
| Qwen-LoRA-DocRED | 82.22% | 81.50% | −0.73 | [−1.21, −0.30] | 0.0004 | *** |
| Llama-LoRA-SciERC | 67.76% | 67.76% | +0.00 | [+0.00, +0.00] | 1.0000 | n.s. |
| Llama-LoRA-DocRED | 84.01% | 84.01% | +0.00 | [−0.15, +0.18] | 0.9844 | n.s. |

## Key Findings

1. **3/4 settings show no significant R-F1 difference** (p > 0.05): constrained decoding neither helps nor hurts fine-tuned models on SciERC (both models) and Llama-DocRED.

2. **Qwen-DocRED shows a small but significant negative effect**: constrained decoding slightly reduces both R-F1 (−0.37pp, p=0.014) and E-F1 (−0.73pp, p<0.001). The constraint enforcement may over-normalize correct predictions that don't exactly match the ontology string format.

3. **Composability interpretation**: After LoRA fine-tuning, models already internalize schema compliance. Constrained decoding provides negligible additional benefit (and in one case slight harm), confirming that FT effectively subsumes the role of inference-time constraints.

## Suggested Paper Text (§5.2 Composability)

For the FT composability paragraph:

> In the fine-tuning regime, the effect of constrained decoding is negligible: across four LoRA settings, three show no significant R-F1 difference ($p{>}0.70$), while one (Qwen-DocRED) exhibits a small negative effect ($-0.37$\,pp, $p{=}0.014$, 95\% CI [$-0.76$, $-0.05$]). This confirms that fine-tuning effectively internalizes schema compliance, rendering inference-time constraints unnecessary for well-trained models.

## Files
- Script: `/root/schema_semantic_constrained_ie/compute_bootstrap_ci_ft.py`
- JSON output: `/root/schema_semantic_constrained_ie/outputs/bootstrap_ci_ft_composability.json`
- Input files: `outputs/w5_lora_scierc_*.jsonl`, `outputs/w5_*_docred_lora_*.jsonl`
