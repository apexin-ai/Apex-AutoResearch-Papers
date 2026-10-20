## PW NLI Combo — BART + RoBERTa Results (2026-05-23)

Server: westd-16639, cuda:1
NLI models: /root/autodl-tmp/models/bart-large-mnli, roberta-large-mnli

### Standalone NLI Accuracy
- DeBERTa-large-mnli: 55.00% (330/600)
- BART-large-mnli: 46.17% (277/600)
- RoBERTa-large-mnli: 37.67% (226/600)

### BART Combo (w=3 main comparison)
- Mistral: SC=39.33% → 44.50% (+5.17pp, BH adj_p=0.003*)
- LLaMA: SC=72.50% → 72.50% (+0.00pp)
- Qwen2.5: SC=74.00% → 75.50% (+1.50pp, adj_p=0.153)
- Qwen3: SC=85.83% → 86.50% (+0.67pp, adj_p=0.438)

### RoBERTa Combo (w=3 main comparison)
- Mistral: SC=39.33% → 43.50% (+4.17pp, BH adj_p=0.016*)
- LLaMA: SC=72.50% → 71.33% (-1.17pp, adj_p=0.961)
- Qwen2.5: SC=74.00% → 74.17% (+0.17pp)
- Qwen3: SC=85.83% → 86.50% (+0.67pp, adj_p=0.656)

WARNING: RoBERTa w=5 significantly hurts LLaMA (-7.83pp, BH adj_p=0.001*)

### Result files (westd-16639)
- /root/symb_invariant_consensus/results/pw_nli_combo_bart.json
- /root/symb_invariant_consensus/results/pw_nli_combo_roberta.json