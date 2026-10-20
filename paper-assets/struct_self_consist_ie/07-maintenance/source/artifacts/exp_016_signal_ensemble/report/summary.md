# exp-016: Signal Ensemble Analysis


## NER

### Part 1: Signal Correlation (SJ vs logprob)
- Pearson r = 0.5672, Spearman ρ = 0.5379

### Part 2: Linear Combo Grid (best α)
- alpha*soft_jaccard + (1-alpha)*logprob: best α=1.0, ρ=0.3565 (single: 0.3565, 0.1396)
- alpha*voting_confidence + (1-alpha)*logprob: best α=0.8, ρ=0.4458 (single: 0.4303, 0.1396)
- alpha*soft_jaccard + (1-alpha)*voting_confidence: best α=0.3, ρ=0.4893 (single: 0.3565, 0.4303)

### Part 3: Logistic Ensemble
- Ensemble AUROC: 0.735 ± 0.0296
  - soft_jaccard: 0.6892 ± 0.0353
  - fleiss_kappa: 0.6317 ± 0.0195
  - logprob: 0.5873 ± 0.0533
  - exact_match: 0.6615 ± 0.0553
  - voting_confidence: 0.6996 ± 0.0339
- Coefficients: {'soft_jaccard': 0.1211, 'fleiss_kappa': -0.338, 'logprob': 0.0383, 'exact_match': 0.6452, 'voting_confidence': 0.8648}

### Part 4: Best-of-N Selection F1
| Method | Mean F1 |
|--------|---------|
| greedy | 0.6094 |
| random_avg | 0.5796 |
| sj_best | 0.6042 |
| voting_conf_best | 0.5959 |
| logprob_best | 0.6087 |
| ensemble_best | 0.6043 |
| oracle | 0.7692 |


## RE

### Part 1: Signal Correlation (SJ vs logprob)
- Pearson r = 0.4173, Spearman ρ = 0.4892

### Part 2: Linear Combo Grid (best α)
- alpha*soft_jaccard + (1-alpha)*logprob: best α=0.3, ρ=0.2871 (single: 0.2112, 0.2467)
- alpha*voting_confidence + (1-alpha)*logprob: best α=0.6, ρ=0.4292 (single: 0.4265, 0.2467)
- alpha*soft_jaccard + (1-alpha)*voting_confidence: best α=0.0, ρ=0.4265 (single: 0.2112, 0.4265)

### Part 3: Logistic Ensemble
- Ensemble AUROC: 0.7191 ± 0.0273
  - soft_jaccard: 0.5909 ± 0.0176
  - fleiss_kappa: 0.6284 ± 0.0327
  - logprob: 0.6207 ± 0.0508
  - exact_match: 0.4959 ± 0.0335
  - voting_confidence: 0.721 ± 0.0232
- Coefficients: {'soft_jaccard': 0.1304, 'fleiss_kappa': -0.3303, 'logprob': 0.0774, 'exact_match': -0.0669, 'voting_confidence': 1.0331}

### Part 4: Best-of-N Selection F1
| Method | Mean F1 |
|--------|---------|
| greedy | 0.3735 |
| random_avg | 0.3380 |
| sj_best | 0.3680 |
| voting_conf_best | 0.3379 |
| logprob_best | 0.3971 |
| ensemble_best | 0.3673 |
| oracle | 0.5608 |
