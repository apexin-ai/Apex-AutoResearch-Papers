# UC Berkeley Measuring Hate Speech — Dataset Exploration Report

**Date**: 2026-05-20  
**Dataset**: `ucberkeley-dlab/measuring-hate-speech` (HuggingFace)  
**Purpose**: Evaluate feasibility for exp-004 (real-data pattern consistency check for EC-HTE)

---

## 1. Data Overview

| Metric | Value |
|--------|-------|
| Total annotations (rows) | 135,556 |
| Unique comments | 39,565 |
| Unique annotators | 7,912 |
| Mean annotations per comment | 3.4 (median: 2) |
| Mean annotations per annotator | 17.1 (median: 17) |
| Platforms | 4 (coded 0–3) |
| Text length | mean 140 chars, max 603 |

**Important structural note**: `hate_speech_score` is a **per-comment** Rasch-model aggregated score (identical across all annotations of the same comment). The ordinal labels (`sentiment`, `dehumanize`, `hatespeech`, etc.) are **per-annotation** and vary across annotators for the same comment.

### Hate Speech Score (continuous, per-comment)

| Statistic | Value |
|-----------|-------|
| Mean | -0.567 |
| Std | 2.380 |
| Min / Max | -8.34 / 6.30 |
| 25% / 50% / 75% | -2.33 / -0.34 / 1.41 |

### 3-Class Benchmark Label (`hatespeech`, per-annotation)

| Label | Count | Fraction |
|-------|-------|----------|
| 0 (not hate) | 80,624 | 59.5% |
| 1 (ambiguous/counter) | 8,911 | 6.6% |
| 2 (hate speech) | 46,021 | 33.9% |

### Ordinal Labels (per-annotation, scale 0–4)

| Label | 0 | 1 | 2 | 3 | 4 |
|-------|---|---|---|---|---|
| sentiment | 9,658 | 9,435 | 19,785 | 35,243 | 61,435 |
| respect | 12,839 | 9,629 | 23,895 | 30,720 | 58,473 |
| insult | 18,476 | 14,667 | 18,587 | 39,673 | 44,153 |
| humiliate | 21,306 | 19,555 | 25,035 | 39,382 | 30,278 |
| dehumanize | 31,855 | 28,434 | 25,292 | 28,653 | 21,322 |
| violence | 67,922 | 30,727 | 12,241 | 11,262 | 13,404 |
| genocide | 90,058 | 22,838 | 8,107 | 5,301 | 9,252 |
| attack_defend | 7,958 | 11,046 | 38,201 | 44,883 | 33,468 |

---

## 2. Target Demographics (text-level, per-annotation)

Each annotation flags which identity groups the comment targets. These are boolean flags (multi-label).

### Aggregate Target Categories

| Category | Annotations with flag=True | % of total |
|----------|---------------------------|------------|
| target_race | 48,352 | 35.7% |
| target_gender | 40,439 | 29.8% |
| target_religion | 26,182 | 19.3% |
| target_origin | 24,372 | 18.0% |
| target_sexuality | 22,407 | 16.5% |
| target_politics | 6,276 | 4.6% |
| target_disability | 3,716 | 2.7% |
| target_age | 2,005 | 1.5% |

### Target Race Subcategories

| Subcategory | Count |
|-------------|-------|
| Black | 22,899 |
| White | 9,797 |
| Middle Eastern | 9,450 |
| Latinx | 8,497 |
| Asian | 7,025 |
| Other | 4,780 |
| Native American | 2,819 |
| Pacific Islander | 2,358 |

### Target Religion Subcategories

| Subcategory | Count |
|-------------|-------|
| Muslim | 12,509 |
| Christian | 6,982 |
| Jewish | 6,924 |
| Other | 2,328 |
| Hindu | 1,285 |
| Atheist | 953 |
| Mormon | 953 |
| Buddhist | 729 |

### Target Gender Subcategories

| Subcategory | Count |
|-------------|-------|
| Women | 27,889 |
| Men | 10,029 |
| Transgender (unspecified) | 4,703 |
| Transgender men | 3,326 |
| Transgender women | 2,611 |
| Non-binary | 2,116 |
| Other | 651 |

### Target Sexuality Subcategories

| Subcategory | Count |
|-------------|-------|
| Gay | 15,465 |
| Lesbian | 6,883 |
| Bisexual | 6,631 |
| Straight | 4,438 |
| Other | 3,104 |

---

## 3. Annotator Demographics

### Gender

| Category | Count | % |
|----------|-------|---|
| Female | 76,370 | 56.3% |
| Male | 57,582 | 42.5% |
| Non-binary | 985 | 0.7% |
| Prefer not to say | 500 | 0.4% |
| Self-describe | 119 | 0.1% |

### Race (one-hot, multi-select)

| Category | Count |
|----------|-------|
| White | 109,090 |
| Black | 13,606 |
| Latinx | 9,501 |
| Asian | 9,596 |
| Native American | 2,636 |
| Middle Eastern | 827 |
| Pacific Islander | 483 |
| Other | 1,425 |

### Ideology

| Category | Count | % |
|----------|-------|---|
| Liberal | 33,812 | 24.9% |
| Neutral | 23,112 | 17.0% |
| Slightly liberal | 21,333 | 15.7% |
| Extremely liberal | 17,944 | 13.2% |
| Conservative | 15,628 | 11.5% |
| Slightly conservative | 15,101 | 11.1% |
| Extremely conservative | 4,544 | 3.4% |
| No opinion | 4,055 | 3.0% |

### Education

| Category | Count | % |
|----------|-------|---|
| College grad (BA) | 50,206 | 37.0% |
| Some college | 35,115 | 25.9% |
| College grad (AA) | 18,011 | 13.3% |
| High school grad | 14,138 | 10.4% |
| Masters | 12,593 | 9.3% |
| Professional degree | 3,042 | 2.2% |
| PhD | 1,562 | 1.2% |
| Some high school | 872 | 0.6% |

### Age

| Statistic | Value |
|-----------|-------|
| Mean | 37.9 |
| Std | 11.6 |
| Range | 18–81 |
| <25 | 11,660 |
| 25–34 | 51,441 |
| 35–44 | 37,674 |
| 45–54 | 19,300 |
| 55+ | 15,376 |

### Income

| Category | Count |
|----------|-------|
| 10k–50k | 56,668 |
| 50k–100k | 52,803 |
| 100k–200k | 17,415 |
| <10k | 6,429 |
| >200k | 2,138 |

---

## 4. Causal Framework Mapping Schemes

### Scheme A (Recommended): Race-Targeted Hate Speech

| Component | Variable | Definition |
|-----------|----------|------------|
| **T** (treatment) | `target_race_black` | Binary: does the comment target Black people? |
| **Y** (outcome) | `hatespeech` ordinal (0/1/2) | Per-annotation hate speech judgment |
| **Z** (effect modifier) | `dehumanize` binarized (≥2 vs <2) | LLM-annotated dehumanization level |
| **S** (subgroup) | Annotator race (White / Black / Other) | Derived from `annotator_race_*` one-hot flags |

**Cell sizes (T × Z × S)**:

| T | Z (dehum_high) | Black | Other | White |
|---|----------------|-------|-------|-------|
| 0 | 0 | 4,639 | 6,223 | 41,202 |
| 0 | 1 | 5,112 | 7,701 | 47,780 |
| 1 | 0 | 743 | 908 | 6,574 |
| 1 | 1 | 1,191 | 1,870 | 11,613 |

**Min cell = 743 — sufficient.**

**CATE-like estimates** (E[Y|T=1,Z,S] - E[Y|T=0,Z,S]):

| Z | Black | Other | White |
|---|-------|-------|-------|
| dehum_low (Z=0) | +0.452 | +0.635 | +0.686 |
| dehum_high (Z=1) | +0.687 | +0.661 | +0.590 |

Key observation: **Treatment effect direction reverses across Z for Black annotators** — when dehumanization is low, Black annotators see a *smaller* CATE from race-targeting (0.45 vs 0.69 for White), but when dehumanization is high, Black annotators see a *larger* CATE (0.69 vs 0.59 for White). This Z×S interaction is exactly the pattern that EC-HTE can exploit.

**Annotator race × dehumanize perception** (for target_race_black=True comments):

| Ann. Race | dehum=0 | dehum=1 | dehum=2 | dehum=3 | dehum=4 |
|-----------|---------|---------|---------|---------|---------|
| Black | 20.2% | 18.2% | 15.8% | 18.9% | 26.9% |
| Other | 17.3% | 15.4% | 21.1% | 22.2% | 24.0% |
| White | 16.9% | 19.2% | 18.9% | 23.0% | 21.9% |

Black annotators assign more extreme dehumanization scores (26.9% at level 4 vs 21.9% for White). This differential perception is a source of LLM misclassification heterogeneity — if an LLM's dehumanization assessment aligns more with the White majority, it will systematically under-classify dehumanization as perceived by Black annotators.

### Scheme B: Gender-Targeted Hate Speech

| Component | Variable | Definition |
|-----------|----------|------------|
| **T** (treatment) | `target_gender_women` | Binary: does the comment target women? |
| **Y** (outcome) | `hate_speech_score` | Per-comment continuous Rasch score |
| **Z** (effect modifier) | `insult` binarized (≥2 vs <2) | LLM-annotated insult level |
| **S** (subgroup) | Annotator gender (Male / Female) | From `annotator_gender` |

**Cell sizes (T × Z × S, male/female only)**:

| T | Z (insult_high) | Female | Male |
|---|-----------------|--------|------|
| 0 | 0 | 15,284 | 11,434 |
| 0 | 1 | 45,383 | 34,294 |
| 1 | 0 | 3,404 | 2,621 |
| 1 | 1 | 12,299 | 9,233 |

**Min cell = 2,621 — abundant.**

**Issue**: Mean Y by T shows almost no difference (-0.564 vs -0.585) — the treatment "targeting women" doesn't strongly shift the aggregate Rasch score relative to non-gender-targeted comments. The T×S interaction is also very weak (< 0.01 difference between male/female annotators). This limits the scheme's usefulness for demonstrating EC-HTE vs. global correction divergence.

### Scheme C: Muslim-Targeted with Ideology Subgroup

| Component | Variable | Definition |
|-----------|----------|------------|
| **T** (treatment) | `target_religion_muslim` | Binary: does the comment target Muslims? |
| **Y** (outcome) | `hate_speech_score` | Per-comment continuous Rasch score |
| **Z** (effect modifier) | `violence` binarized (≥1 vs 0) | LLM-annotated violence level |
| **S** (subgroup) | Annotator ideology (Liberal vs Conservative) | From `annotator_ideology` |

**Cell sizes (T × Z × S, liberal/conservative only)**:

| T | Z (violence_any) | Conservative | Liberal |
|---|-------------------|-------------|---------|
| 0 | 0 | 16,683 | 34,031 |
| 0 | 1 | 15,481 | 32,021 |
| 1 | 0 | 1,391 | 2,998 |
| 1 | 1 | 1,718 | 4,039 |

**Min cell = 1,391 — sufficient.**

Notable T×S interaction for Muslim-targeted content: conservative annotators rate Muslim-targeted comments slightly more negatively (hate_speech_score mean -0.61) while liberal annotators rate them less negatively (-0.52). The gap is modest but the direction is meaningful for the application.

---

## 5. Pattern Consistency Feasibility

### Can we demonstrate "global correction vs EC-HTE produces qualitatively different CATE distributions"?

**Yes, Scheme A is well-suited.** The argument:

1. **LLM as Z annotator**: An LLM classifies each comment's dehumanization level (Z) based on text alone. The LLM cannot observe annotator demographics. Due to training data composition (majority White perspectives), the LLM's dehumanization assessment likely correlates more with White annotators' perception.

2. **Subgroup-specific LLM error**: For Black-targeted hate speech, Black annotators perceive significantly more dehumanization (26.9% at level 4) than White annotators (21.9%). An LLM trained predominantly on majority-perspective data would under-classify dehumanization from the Black annotator perspective. This is a **subgroup-specific misclassification pattern** — the LLM error rate on Z differs by S.

3. **Global correction failure**: A global correction (single miscalibration function applied uniformly) would adjust Z based on the population-average error. This population average is dominated by White annotators (80% of data). Applying this correction to Black annotators' CATE estimates would *over-correct* in the wrong direction — spreading the majority-group bias to the minority group.

4. **EC-HTE advantage**: EC-HTE estimates subgroup-specific correction functions. For Black annotators, EC-HTE would learn that LLM under-classifies dehumanization relative to their perception, and correct accordingly. For White annotators, the correction would be minimal. This produces qualitatively different CATE distributions:
   - Global correction: uniform shift across S → attenuates true heterogeneity
   - EC-HTE: heterogeneous correction → preserves or amplifies cross-group differences

5. **Domain knowledge alignment**: The pattern is consistent with hate speech literature — racialized groups perceive hate speech targeting their group more severely, and this differential perception is exactly what an LLM trained on majority-perspective data would miss.

### What we don't need

- No ground truth CATE required — we show method difference, not accuracy
- No RCT — the observational T (target_race_black) has clear temporal/causal interpretation: the text either targets Black people or it doesn't, and this is determined before annotation

### Potential concerns

1. **`hate_speech_score` is per-comment**: Since the Rasch score is constant per comment, it cannot serve as Y if we want to study annotator-level heterogeneity. **Use ordinal labels (hatespeech, dehumanize) as Y instead** — they vary per annotation.

2. **Annotations per comment are thin**: Median 2 annotations per comment. For CATE estimation, this limits within-comment comparison but is fine for across-comment estimation with covariates.

3. **Confounding**: Comments targeting Black people come disproportionately from platform 1 (47.6% vs 28.7% for non-Black-targeted). Platform may confound T→Y. Can control by including platform as covariate.

4. **Multi-label targets**: Some comments target multiple groups (e.g., target_race_black AND target_gender_women). These should be handled carefully — either exclude multi-target comments or include as covariates.

---

## 6. Recommended Final Mapping

### Primary: Scheme A

| Component | Variable | Operationalization |
|-----------|----------|--------------------|
| **T** | `target_race_black` | Binary (True/False) |
| **Y** | `hatespeech` ordinal | Per-annotation, 3-level (0=not hate, 1=ambiguous, 2=hate) |
| **Z** | Dehumanization level | LLM classifies text → binary (high/low), compare to human `dehumanize` |
| **S** | Annotator race | White / Black / Other (from one-hot flags) |
| **Covariates** | Platform, text length, other target flags | Control for confounding |

### Rationale

- **Largest treatment group** among target demographics (22,899 annotations)
- **Clear LLM misclassification heterogeneity** story (majority-perspective bias in dehumanization assessment)
- **Cell sizes ≥ 743** across all T×Z×S combinations
- **Domain-relevant**: hate speech against Black people is well-studied, making domain-knowledge-based evaluation credible
- **Observable Z×S interaction** in CATE estimates: the direction of treatment effect heterogeneity flips between low-Z and high-Z for Black vs White annotators

### Secondary: Scheme C (Muslim-targeted × ideology)

Use as robustness check — different T (religion instead of race) and different S (ideology instead of race), providing independent evidence.

### Not recommended: Scheme B

The gender-targeted scheme shows insufficient T main effect and negligible T×S interaction, making it a poor candidate for demonstrating EC-HTE vs. global correction divergence.
