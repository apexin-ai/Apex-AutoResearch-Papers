# Cross-Method EDCR Table (Plan_003)

## Script
`/root/autodl-tmp/freige/eval/cross_method_table.py`
Run: `cd /root/autodl-tmp && python -m freige.eval.cross_method_table`

## Results (exported to /root/autodl-tmp/eval_results/cross_method_table.json)

| Method | rel_f1 | Δf1 | evi_f1 | EDCR | ΔEDCR | preds | trunc |
|--------|--------|-----|--------|------|-------|-------|-------|
| SFT baseline | 0.4057 | — | 0.7979 | 0.7118 | — | 18815 | 367 |
| RSFT-CED (s42) | 0.4449 | +3.92 | 0.8187 | 0.6565 | -5.53 | 15307 | 213 |
| RSFT-CED (s43) | 0.4683 | +6.26 | 0.8156 | 0.6388 | -7.30 | 14970 | 171 |
| RSFT-CED (s44) | 0.4655 | +5.98 | 0.8087 | 0.6350 | -7.67 | 15202 | 189 |
| RSFT-CED (r2a) | 0.4494 | +4.37 | 0.8108 | 0.6641 | -4.76 | 15482 | 208 |
| RSFT-CED (r2b) | 0.4493 | +4.37 | 0.8128 | 0.6609 | -5.08 | 14829 | 179 |
| RSFT-flatNLI | 0.4539 | +4.82 | 0.8043 | 0.6431 | -6.87 | 15294 | 199 |
| CED-reranker | 0.4864 | +8.07 | 0.8188 | 0.6156 | -9.62 | 14782 | - |
| bf16 GRPO | 0.4549 | +4.93 | 0.8086 | 0.6318 | -8.00 | 10701 | 61 |

RSFT-CED 3-seed: rel_f1=0.4596±0.0128, evi_f1=0.8144±0.0051, EDCR=0.6434±0.0114
