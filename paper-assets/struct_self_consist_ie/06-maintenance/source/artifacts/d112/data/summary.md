# Hybrid Strategy: Expected F1 Gain

Strategy: Use greedy for degenerate instances (constant F1 across all samples), MBR selection (highest SJ utility) for non-degenerate instances.

| Dataset | N | #Inst | %Degen | Greedy | Random | MBR-SJ | Hybrid | Oracle | Hybrid-Greedy |
|---------|---|-------|--------|--------|--------|--------|--------|--------|---------------|
| SciERC NER | 8 | 551 | 21.1% | 0.6182 | 0.5835 | 0.6188 | 0.6200 | 0.7448 | +0.0018 |
| CoNLL NER | 16 | 3453 | 58.0% | 0.7239 | 0.6919 | 0.7215 | 0.7215 | 0.7639 | -0.0024 |
| SciERC RE | 16 | 551 | 45.7% | 0.2904 | 0.2612 | 0.2847 | 0.2847 | 0.4544 | -0.0057 |

Key: Hybrid marginally helps SciERC NER (+0.18pp) but does not beat greedy on CoNLL/RE where degenerate proportion is high. On non-degenerate instances, MBR selection underperforms greedy for CoNLL/RE tasks.

Output: /root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/