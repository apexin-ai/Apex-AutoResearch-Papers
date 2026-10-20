# EDCR Cross-Method Diagnostic (2026-05-16)

## Summary Table

| Method | rel_f1 | evi_f1 | EDCR | median | std | n_doc |
|---|---|---|---|---|---|---|
| SFT baseline (quant) | 0.4057 | 0.7979 | 0.7118 | 0.6838 | 0.2879 | 982 |
| SFT baseline (noquant) | 0.4106 | 0.8013 | 0.7039 | 0.6667 | 0.2927 | 983 |
| RSFT-CED s42 | 0.4449 | 0.8187 | 0.6565 | 0.6000 | 0.2936 | 985 |
| RSFT-CED s43 | 0.4683 | 0.8156 | 0.6388 | 0.5818 | 0.2902 | 985 |
| RSFT-CED s44 | 0.4655 | 0.8087 | 0.6350 | 0.5714 | 0.2894 | 985 |
| RSFT-CED r2a | 0.4494 | 0.8108 | 0.6641 | 0.6190 | 0.2844 | 985 |
| RSFT-CED r2b | 0.4493 | 0.8128 | 0.6609 | 0.6111 | 0.2866 | 983 |
| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 | 0.6000 | 0.2935 | 985 |
| SFT no-evidence | 0.4893 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0 |
| GRPO bf16 ckpt100 | 0.4549 | 0.8086 | 0.6318 | 0.5909 | 0.2743 | 985 |
| GRPO QLoRA kl001 ckpt100 | 0.2167 | 0.5746 | 0.8539 | 0.9231 | 0.1787 | 985 |
| GRPO QLoRA lr5e6 ckpt100 | 0.0147 | 0.8502 | 0.9869 | 1.0000 | 0.0562 | 984 |
| DPO-CED 1ep | 0.0022 | 0.7500 | 0.9982 | 1.0000 | 0.0137 | 981 |
| RSFT-flatNLI s43 | 0.0022 | 0.8533 | 0.9982 | 1.0000 | 0.0125 | 981 |

## Key Observations
- **Best EDCR (viable methods, rel_f1>0.4):** GRPO bf16 ckpt100 (0.6318), RSFT-CED s44 (0.6350)
- **SFT no-evidence:** EDCR=0 (no evidence produced, as expected)
- **Degenerate models** (DPO-CED 1ep, RSFT-flatNLI s43, GRPO QLoRA lr5e6): EDCR≈1.0 but rel_f1<0.02 — nearly all citations are distractors because the model barely extracts correct triples
- **GRPO bf16 has lowest EDCR AND lowest std (0.2743)** among viable methods — most consistent evidence quality

## Files
- JSON: `/root/autodl-tmp/eval_results/edcr_diagnostic.json`
- LaTeX: `/root/autodl-tmp/eval_results/edcr_diagnostic.tex`
