# FK Excess Agreement — All Configurations

Fleiss' Kappa decomposition: FK = (P_o - P_e) / (1 - P_e), where excess agreement = P_o - P_e.

| Config | Subtask | N | n_instances | mean P_o | mean P_e | mean excess (P_o−P_e) | mean FK | FK range (5th–95th pctl) |
|--------|---------|---|-------------|----------|----------|-----------------------|---------|--------------------------|
| Qwen SciERC NER | NER | 8 | 551 | 0.747 | 0.508 | 0.240 | 0.393 | −0.114 – 1.000 |
| Qwen SciERC RE | RE | 8 | 551 | 0.726 | 0.488 | 0.238 | 0.293 | −0.143 – 1.000 |
| Qwen CoNLL NER | NER | 8 | 3453 | 0.895 | 0.238 | 0.657 | 0.721 | −0.143 – 1.000 |
| Qwen CoNLL NER N=16 | NER | 16 | 3453 | 0.910 | 0.309 | 0.601 | 0.716 | −0.067 – 1.000 |
| LLaMA SciERC NER | NER | 8 | 551 | 0.774 | 0.472 | 0.302 | 0.451 | −0.126 – 1.000 |
| LLaMA SciERC RE | RE | 8 | 551 | 0.755 | 0.447 | 0.308 | 0.368 | −0.143 – 1.000 |
| LLaMA CoNLL NER | NER | 8 | 3453 | 0.973 | 0.068 | 0.906 | 0.928 | 0.357 – 1.000 |
| LLaMA CoNLL NER N=16 | NER | 16 | 3453 | 0.976 | 0.085 | 0.891 | 0.929 | 0.426 – 1.000 |

## Key Findings

**P_e (chance agreement) varies dramatically by dataset, not model.** SciERC configs have high P_e (0.45–0.51) reflecting few distinct items per instance and skewed category distributions. CoNLL P_e is much lower (0.07–0.31), meaning more diverse item spaces where chance agreement is rare.

**Excess agreement (P_o − P_e) is the more informative metric.** LLaMA CoNLL shows the highest excess (~0.90), meaning nearly all observed agreement is genuine. SciERC configs have modest excess (0.24–0.31) despite reasonable P_o, because P_e inflates the baseline. This means a substantial fraction of SciERC's raw agreement is attributable to chance.

**RE consistently has lower FK than NER on the same data**, despite similar P_o levels. Qwen SciERC RE (FK=0.293) vs NER (FK=0.393); LLaMA SciERC RE (FK=0.368) vs NER (FK=0.451). RE's slightly lower P_e doesn't compensate for its lower P_o, resulting in less excess agreement.

**N=8 vs N=16 shows minimal FK change.** Qwen CoNLL: 0.721→0.716; LLaMA CoNLL: 0.928→0.929. However, P_e increases with N (0.238→0.309 for Qwen CoNLL) because more samples surface more unique items, slightly reducing excess despite higher P_o.

**LLaMA vs Qwen:** LLaMA consistently achieves higher excess agreement across all configs, particularly on CoNLL (+0.25 excess over Qwen). On SciERC the gap is smaller (~0.06). This suggests LLaMA's outputs are more internally consistent.
