Script location: rtx5090-4x:/root/autodl-tmp/scripts/edcr_diagnostic.py

Current table preview (18 methods):
| Method | Rel-F1 | Evi-F1 | EDCR | ΔF1pp |
|--------|--------|--------|------|-------|
| CED-reranker (N=8) | 0.4864 | 0.8188 | 0.6156 | +7.58 |
| SFT no-evidence | 0.4893 | 0.0000 | 0.0000 | +7.86 |
| RSFT-CED s43 (best) | 0.4683 | 0.8156 | 0.6388 | +5.77 |
| RSFT-CED 3-seed mean | 0.4596±0.0128 | 0.8143±0.0051 | 0.6434±0.0115 | -- |
| GRPO bf16 ckpt100 | 0.4549 | 0.8086 | 0.6318 | +4.43 |
| RSFT-flatNLI s42 | 0.4539 | 0.8043 | 0.6431 | +4.33 |
| SFT baseline (noquant) | 0.4106 | 0.8013 | 0.7039 | 0.00 |
| DPO 3ep | 0.3429 | 0.8403 | 0.7294 | -6.77 |
| GRPO QLoRA kl001 | 0.2108 | 0.5666 | 0.8584 | -19.98 |

Pending: RSFT-flatNLI s43 reeval, DPO 1ep reeval, flatNLI s44/s45 evals, RSFT topk3 reeval