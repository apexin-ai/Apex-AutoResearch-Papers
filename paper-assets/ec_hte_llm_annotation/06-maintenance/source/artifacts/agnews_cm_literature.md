# LLM Classification Performance on AG News & MNLI: Literature Search Results

## 1. AG News (4-class: World / Sports / Business / Sci-Tech)

### 1.1 Complete Confusion Matrices Found

**Source: Comparative Evaluation of ChatGPT and DeepSeek (arXiv:2506.18501)**

Sample size: 20 items per class (n=80 total). Small but provides proportional confusion patterns.

#### ChatGPT (GPT-4-turbo) — Overall Accuracy: 80.0%

| True \ Predicted | Business | Sci/Tech | Sport | World |
|-----------------|----------|----------|-------|-------|
| **Business**    | **11**   | 0        | 0     | 9     |
| **Sci/Tech**    | 0        | **17**   | 3     | 0     |
| **Sport**       | 0        | 0        | **18**| 2     |
| **World**       | 0        | 0        | 2     | **18**|

Per-class metrics:
| Class    | Precision | Recall | F1    |
|----------|-----------|--------|-------|
| Business | 100.0%    | 55.0%  | 71.0% |
| Sci/Tech | 100.0%    | 85.0%  | 91.9% |
| Sport    | 78.3%     | 90.0%  | 83.7% |
| World    | 62.1%     | 90.0%  | 73.5% |

**Key pattern: Business → World is dominant confusion (9/20 = 45% of Business items misclassified as World)**

#### DeepSeek — Overall Accuracy: 81.3%

| True \ Predicted | Business | Sci/Tech | Sport | World |
|-----------------|----------|----------|-------|-------|
| **Business**    | **13**   | 2        | 0     | 5     |
| **Sci/Tech**    | 3        | **14**   | 3     | 0     |
| **Sport**       | 0        | 0        | **20**| 0     |
| **World**       | 0        | 0        | 2     | **18**|

Per-class metrics:
| Class    | Precision | Recall | F1    |
|----------|-----------|--------|-------|
| Business | 81.3%     | 65.0%  | 72.2% |
| Sci/Tech | 87.5%     | 70.0%  | 77.8% |
| Sport    | 80.0%     | 100.0% | 88.9% |
| World    | 78.3%     | 90.0%  | 83.7% |

**Key patterns: Business → World (5/20), Sci/Tech → Business (3/20), Sci/Tech → Sport (3/20)**

### 1.2 Overall Accuracy / Macro-F1 (No Per-Class Breakdown)

| Source | Model | Metric | Score |
|--------|-------|--------|-------|
| arXiv:2402.07470 (RGPT) | GPT-4 | Accuracy | 84.62% |
| arXiv:2402.07470 | GPT-4 | Macro-F1 | 84.50% |
| arXiv:2402.07470 | LLaMA 2 | Accuracy | 79.40% |
| arXiv:2402.07470 | LLaMA 2 | Macro-F1 | 80.67% |
| arXiv:2402.07470 | ChatGLM 2 | Accuracy | 82.51% |
| arXiv:2602.06370 (Cost-Aware) | GPT-4o zero-shot | Macro-F1 | 87.93% |
| arXiv:2602.06370 | GPT-4o few-shot | Macro-F1 | 89.65% |
| arXiv:2602.06370 | Claude 4.5 zero-shot | Macro-F1 | 91.35% |
| arXiv:2602.06370 | Claude 4.5 few-shot | Macro-F1 | 90.56% |
| Datawizz blog | GPT-4 zero-shot | Accuracy | 87.2% |
| arXiv:2506.18501 | ChatGPT | Accuracy | 80.0% |
| arXiv:2506.18501 | DeepSeek | Accuracy | 81.3% |
| arXiv:2404.11122 | Best small LM (124M) | Accuracy | 73.4% |

**Note:** GPT-4/GPT-4o scores vary across papers (80–88%) depending on prompt design, sample size, and evaluation protocol. The 2506.18501 paper uses only 80 samples which explains the lower score.

### 1.3 Confusion Patterns (Qualitative, from Multiple Sources)

1. **Business ↔ World** is the most common confusion across all LLMs tested
   - RGPT paper (2402.07470): "RGPT tends to misclassify 'Business' to be 'World' and 'Technology'"
   - ChatGPT CM: 45% of Business items → World
   - DeepSeek CM: 25% of Business items → World
   
2. **Sci/Tech ↔ Business** is a secondary confusion
   - DeepSeek: 15% of Sci/Tech → Business; 10% of Business → Sci/Tech

3. **Sports** is the easiest class (highest recall: 90–100%)
   - Sports has distinctive vocabulary (teams, scores, games)
   
4. **Business** is the hardest class (lowest recall: 55–65%)
   - Business news often involves international/political content → confused with World

### 1.4 Reference: Fine-tuned Model Baselines

| Model | Accuracy/F1 |
|-------|-------------|
| BERT fine-tuned | 94.43% F1 |
| RoBERTa fine-tuned | 94.63% F1 |
| DeBERTa fine-tuned | 95.32% |
| XLNet fine-tuned | 95.51% |
| CARP (SOTA) | 96.40% |

---

## 2. MNLI / NLI (3-class: Entailment / Contradiction / Neutral)

### 2.1 Per-Class Data Found

**Source: arXiv:2506.18501 — FraCaS Dataset (3-way NLI, n=75)**

#### ChatGPT — Overall Accuracy: 64.0%

| Class         | Precision | Recall | F1    |
|---------------|-----------|--------|-------|
| Entailment    | 59.3%     | 64.0%  | 61.5% |
| Neutral       | 56.5%     | 52.0%  | 54.2% |
| Contradiction | 76.0%     | 76.0%  | 76.0% |

#### DeepSeek — Overall Accuracy: 69.3%

| Class         | Precision | Recall | F1    |
|---------------|-----------|--------|-------|
| Entailment    | 60.6%     | 80.0%  | 69.0% |
| Neutral       | 66.7%     | 40.0%  | 50.0% |
| Contradiction | 81.5%     | 88.0%  | 84.6% |

**Key patterns:**
- **Neutral is the hardest class** (lowest F1 for both models: 50–54%)
- **Contradiction is the easiest** (highest F1: 76–85%)
- DeepSeek over-predicts Entailment (80% recall but 60.6% precision)
- ChatGPT more balanced but overall weaker

### 2.2 Known MNLI Patterns from Literature

- GPT-4 on standard MNLI-matched is estimated at ~87–89% accuracy (GPT-4 technical report notes strong NLI performance but doesn't report exact MNLI scores)
- Neutral class is consistently the hardest for LLMs
- LLMs tend to over-predict Entailment (bias toward "yes, this follows")
- Fine-tuned DeBERTa-v3 on MNLI achieves ~91% accuracy as SOTA baseline

### 2.3 Caveat

The FraCaS dataset is a formal semantics test suite (formal logic examples), not the standard MNLI benchmark. Performance is lower because FraCaS tests formal reasoning. Standard MNLI accuracy for GPT-4 class models is higher (~85-89%).

---

## 3. Synthesis: Recommended CM for Experiments

### 3.1 AG News Confusion Matrices to Use

**Option A: Directly use the ChatGPT CM from arXiv:2506.18501**

Normalize to row-stochastic form:
```
         Bus    Sci    Sport  World
Bus    [ 0.55   0.00   0.00   0.45 ]
Sci    [ 0.00   0.85   0.15   0.00 ]
Sport  [ 0.00   0.00   0.90   0.10 ]
World  [ 0.00   0.00   0.10   0.90 ]
```

**Option B: Calibrated CM based on GPT-4 at ~85% overall accuracy**

Adjust the proportions to match the higher accuracy seen in larger-scale evaluations (84–88%), keeping the same confusion direction but lower error rates:
```
         Bus    Sci    Sport  World
Bus    [ 0.72   0.03   0.00   0.25 ]
Sci    [ 0.03   0.88   0.07   0.02 ]
Sport  [ 0.00   0.01   0.95   0.04 ]
World  [ 0.02   0.01   0.05   0.92 ]
```

Rationale: Business→World remains dominant confusion; Sports highest accuracy; overall ~87% accuracy matching GPT-4o zero-shot performance.

**Option C: Weaker LLM (GPT-3.5 / LLaMA 2 class, ~80% accuracy)**

Use the raw ChatGPT CM from the paper directly (already at 80%).

**Option D: Stronger LLM (Claude 4.5 class, ~91% macro-F1)**

```
         Bus    Sci    Sport  World
Bus    [ 0.85   0.03   0.00   0.12 ]
Sci    [ 0.02   0.92   0.04   0.02 ]
Sport  [ 0.00   0.01   0.97   0.02 ]
World  [ 0.01   0.01   0.03   0.95 ]
```

### 3.2 MNLI Confusion Matrices to Use

**Option A: From FraCaS empirical data (ChatGPT, ~64% — too low for MNLI)**

Not recommended directly since FraCaS is much harder than standard MNLI.

**Option B: Constructed CM for GPT-4 on MNLI (~87% accuracy)**

Based on known patterns (neutral hardest, contradiction easiest):
```
              Ent    Con    Neu
Entailment [ 0.90   0.02   0.08 ]
Contradict [ 0.03   0.92   0.05 ]
Neutral    [ 0.15   0.07   0.78 ]
```

**Option C: Weaker LLM (~80% accuracy) based on FraCaS proportional patterns:**
```
              Ent    Con    Neu
Entailment [ 0.83   0.03   0.14 ]
Contradict [ 0.05   0.88   0.07 ]
Neutral    [ 0.22   0.10   0.68 ]
```

### 3.3 Recommendation for Experiments

1. **AG News primary CM**: Use Option B (calibrated GPT-4 level, ~87%) as the "strong LLM" and Option A/C (raw 80%) as the "weak LLM"
2. **Subgroup heterogeneity**: Make Business articles have higher error (0.72 correct) while Sports has lower error (0.95 correct). This mirrors empirical patterns and creates natural treatment-correlated misclassification if treatment assignment correlates with topic.
3. **MNLI**: Use Option B (~87%) as baseline; vary Neutral class error rate to test sensitivity
4. **For the paper**: Cite arXiv:2506.18501 as empirical grounding for CM structure, arXiv:2402.07470 and arXiv:2602.06370 for accuracy calibration

---

## 4. Source Papers

| Paper | Key Data | URL |
|-------|----------|-----|
| arXiv:2506.18501 (2025) | Full 4×4 CM for ChatGPT & DeepSeek on AG News; 3-way NLI metrics | https://arxiv.org/abs/2506.18501 |
| arXiv:2402.07470 (2024) | GPT-4 84.6%, LLaMA2 79.4% on AG News; confusion pattern analysis | https://arxiv.org/abs/2402.07470 |
| arXiv:2602.06370 (2026) | GPT-4o 87.9%, Claude 4.5 91.4% macro-F1 on AG News | https://arxiv.org/abs/2602.06370 |
| Datawizz Blog (2024) | GPT-4 87.2% vs fine-tuned Llama 95% | https://datawizz.ai/blog/outperforming-gpt-4-on-news-classification |
| Gilardi et al. PNAS (2023) | ChatGPT outperforms crowd workers on annotation tasks | https://www.pnas.org/doi/10.1073/pnas.2305016120 |
| Törnberg (2024) | GPT-4 outperforms experts on political message classification | https://arxiv.org/abs/2304.06588 |
| arXiv:2406.08660 (2024) | Fine-tuned small LLMs outperform zero-shot GPT-4 | https://arxiv.org/abs/2406.08660 |
| arXiv:2404.11122 (2024) | Small LMs zero-shot: 73.4% on AG News | https://arxiv.org/abs/2404.11122 |
| arXiv:2412.14461 (2024) | LLM annotation measurement error framework | https://arxiv.org/abs/2412.14461 |
| arXiv:2504.15432 (2025) | LLM annotations degrade BERT fine-tuning | https://arxiv.org/abs/2504.15432 |

---

## 5. Summary

- **Full confusion matrix found**: Yes, for ChatGPT and DeepSeek on AG News (arXiv:2506.18501). Small sample (n=80) but provides validated confusion structure.
- **Per-class metrics found**: Yes, precision/recall/F1 for all 4 AG News classes for 2 models.
- **Key empirical fact**: Business→World is the dominant misclassification pattern; Sports is easiest; this creates natural heterogeneous error rates across classes.
- **MNLI**: Only found per-class data on FraCaS (formal semantics, harder than MNLI). Neutral is hardest class. Need to construct calibrated MNLI CM from known patterns.
- **Multiple accuracy levels available**: Weak LLM (~80%), Medium (~85%), Strong (~88-91%), enabling multi-level CM experiments.
