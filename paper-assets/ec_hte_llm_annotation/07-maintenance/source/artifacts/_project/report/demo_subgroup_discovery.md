# Demographic Subgroup Discovery Report

Generated: 2026-05-24

---

## 1. Available LLM Annotation Data

### 1.1 UC Berkeley Hate Speech (exp004)

| File | Path | Size | Rows × Cols |
|------|------|------|------------|
| Raw parquet | `data/exp004_raw.parquet` | 13.4 MB | 135,556 × 143 |
| Processed (annotation-level) | `data/exp004_processed.parquet` | 10.3 MB | 135,556 × 9 |
| Processed (comment-level) | `data/exp004_comments_processed.parquet` | 4.4 MB | 39,495 × 13 |
| LLM annotations | `results/exp004_llm_annotations.csv` | 419 KB | ~2,500 comments |
| Confusion matrices | `results/exp004_confusion_matrices.csv` | 506 B | 5 subgroups |

- **LLM**: GPT-4.1 (via OpenRouter)
- **Current subgroups**: `plat0_long`, `plat0_short`, `plat23_long`, `plat23_short` (platform × text_length)
- **Causal variables**: T = target_race majority, Y = hate_speech_score, Z_human = dehumanize ≥ 2

### 1.2 CivilComments (exp023)

| File | Path | Size | Rows × Cols |
|------|------|------|------------|
| LLM annotations | `results/exp023_llm_annotations.csv` | 419 KB | 6,443 × 15 |
| Pooled parquet | `results/exp023_civil_comments_pool.parquet` | 667 KB | ~3,000 |
| Confusion matrices | `results/exp023_confusion_matrices.json` | — | 4 subgroups × 3 LLMs |

- **LLMs**: GPT-4o, GPT-4o-mini, GPT-3.5-Turbo
- **Current subgroups**: S0-S3 (text_length_bin × has_question)
- **Causal variables**: y_true = toxicity ≥ 0.5, pred_* = LLM predictions
- **Available toxicity sub-scores**: toxicity, insult, identity_attack, obscene

### 1.3 TweetEval Stance Detection (exp_stance)

| File | Path | Size |
|------|------|------|
| LLM annotations | `results/stance_llm_annotations.json` | 13.7 KB |
| Confusion matrices | `results/stance_confusion_matrices.json` | 5.2 KB |

- **LLMs**: GPT-4o (real), GPT-4o-mini, GPT-3.5-Turbo (simulated from GPT-4o)
- **Subgroups**: 5 stance targets (Atheism, Climate, Feminist, Hillary, Abortion)
- **Labels**: 3-class (none/against/favor), binarized to favor vs not-favor for CMs

### 1.4 Other LLM Annotations

| File | Description |
|------|-------------|
| `results/pilot_llm_annotations.csv` | 7 KB, GPT-4.1 pilot on UCB hate speech |
| `results/pilot_gemini_annotations.csv` | 60 KB, Gemini 2.5 Flash on hate speech |
| `artifacts/c1_multi_llm/` | Multi-LLM sweep: Mistral-7B, Gemma, Qwen2.5-7B, LLaMA |

---

## 2. Demographic Columns in Existing Data

### 2.1 UC Berkeley Hate Speech Raw (143 columns)

**Annotator demographics (in `data/exp004_raw.parquet`):**

| Category | Columns |
|----------|---------|
| Gender | `annotator_gender`, `annotator_gender_men`, `annotator_gender_women`, `annotator_gender_non_binary`, `annotator_gender_prefer_not_to_say`, `annotator_gender_self_describe` |
| Race | `annotator_race_asian`, `annotator_race_black`, `annotator_race_latinx`, `annotator_race_middle_eastern`, `annotator_race_native_american`, `annotator_race_pacific_islander`, `annotator_race_white`, `annotator_race_other` |
| Age | `annotator_age` (continuous, e.g. 30.0) |
| Education | `annotator_educ`, `annotator_education_some_high_school`, `annotator_education_high_school_grad`, `annotator_education_some_college`, `annotator_education_college_grad_aa`, `annotator_education_college_grad_ba`, `annotator_education_professional_degree`, `annotator_education_masters`, `annotator_education_phd` |
| Income | `annotator_income`, `annotator_income_<10k`, `annotator_income_10k-50k`, `annotator_income_50k-100k`, `annotator_income_100k-200k`, `annotator_income_>200k` |
| Ideology | `annotator_ideology`, `annotator_ideology_extremeley_conservative` ... `annotator_ideology_extremeley_liberal`, `annotator_ideology_no_opinion` |
| Religion | `annotator_religion_atheist`, `annotator_religion_buddhist`, `annotator_religion_christian`, `annotator_religion_hindu`, `annotator_religion_jewish`, `annotator_religion_mormon`, `annotator_religion_muslim`, `annotator_religion_nothing`, `annotator_religion_other` |
| Sexuality | `annotator_sexuality_bisexual`, `annotator_sexuality_gay`, `annotator_sexuality_straight`, `annotator_sexuality_other` |
| Transgender | `annotator_trans`, `annotator_transgender`, `annotator_cisgender` |

**Target demographics (in `data/exp004_raw.parquet`):**

| Category | Columns |
|----------|---------|
| Race | `target_race_asian`, `target_race_black`, `target_race_latinx`, `target_race_middle_eastern`, `target_race_native_american`, `target_race_pacific_islander`, `target_race_white`, `target_race_other` |
| Gender | `target_gender_men`, `target_gender_women`, `target_gender_non_binary`, `target_gender_transgender_men`, `target_gender_transgender_women` |
| Religion | `target_religion_atheist`, `target_religion_buddhist`, `target_religion_christian`, `target_religion_hindu`, `target_religion_jewish`, `target_religion_mormon`, `target_religion_muslim`, `target_religion_other` |
| Sexuality | `target_sexuality_bisexual`, `target_sexuality_gay`, `target_sexuality_lesbian`, `target_sexuality_straight`, `target_sexuality_other` |
| Age | `target_age_children`, `target_age_teenagers`, `target_age_young_adults`, `target_age_middle_aged`, `target_age_seniors` |
| Origin | `target_origin_immigrant`, `target_origin_migrant_worker`, `target_origin_specific_country`, `target_origin_undocumented` |
| Disability | `target_disability_physical`, `target_disability_cognitive`, `target_disability_neurological`, `target_disability_visually_impaired`, `target_disability_hearing_impaired` |
| Politics | `target_politics_conservative`, `target_politics_liberal`, `target_politics_republican`, `target_politics_democrat`, etc. |

### 2.2 CivilComments

**In current data (`exp023_llm_annotations.csv`):** Only `identity_attack` (continuous sub-score). No explicit demographic columns.

**In original CivilComments dataset (not yet extracted):** `male`, `female`, `transgender`, `other_gender`, `heterosexual`, `homosexual_gay_or_lesbian`, `bisexual`, `other_sexual_orientation`, `christian`, `jewish`, `muslim`, `hindu`, `buddhist`, `atheist`, `other_religion`, `black`, `white`, `asian`, `latino`, `other_race_or_ethnicity`, `physical_disability`, `intellectual_or_learning_disability`, `psychiatric_or_mental_illness`, `other_disability`.

### 2.3 TweetEval Stance

No demographic columns. Subgroups are stance targets (topic-based).

---

## 3. Key Reusable Code

### 3.1 EC-HTE Pipeline Components

| Function | File | Purpose |
|----------|------|---------|
| `diff_in_means(Y, T, mask)` | All exp files | Standard DiM CATE estimator with Welch SE |
| `get_counts(z_true, z_hat, subgroups, labels)` | exp001/exp023/exp015 | Build (K, 2, 2) confusion count arrays |
| `build_mixing_matrix(C, p_z, p_z_hat)` | exp023/exp015 | Proper Bayes rule mixing matrix (recommended) |
| `build_mixing_matrix(C)` | exp001/exp_stance | Simple version assuming P(Z)=0.5 |
| `invert_mixing_safe(M, tau_obs, se_obs)` | exp001/exp023/exp015 | Condition-guarded matrix inversion |
| `estimate_cm_mle(counts, labels)` | exp001 | Per-subgroup MLE with Laplace |
| `compute_global_cm(counts)` | exp001 | Pooled global CM |
| `estimate_cm_hb_eb(counts, labels, global_cm)` | exp001 | Empirical Bayes (fast, no MCMC) |
| `estimate_cm_hb_gibbs(...)` | exp001 (centered), exp023/exp015 (non-centered) | Full Gibbs MCMC |

### 3.2 Semi-Synthetic CATE Injection

| Pattern | Files | Details |
|---------|-------|---------|
| Simple binary CATE | exp001, exp023, exp_civilcomments_demo | `tau = tau_z1 if Z==1 else tau_z0` |
| Subgroup-varying CATE | exp015 | `tau(z, s) = f(z) + g(s)`, varies by both Z and subgroup |
| Topic-varying CATE | exp_stance | `tau_favor=0.20`, `tau_against=0.05`, `tau_none=0.10` |

### 3.3 Demographic Subgroup Code

| File | Approach |
|------|----------|
| `exp_civilcomments_demographic.py` | Keyword regex on text content → 4 groups: `race_lgbtq`, `religion`, `gender`, `no_identity` |
| `exp004_hate_speech.py` | `platform_group × text_length_bin` (ignores demographic columns) |
| `exp023_civil_comments_prepare.py` | `text_length_bin × has_question` (ignores identity columns) |

### 3.4 Per-Subgroup CM from Real Annotations

| File | Key Function |
|------|-------------|
| `exp_civilcomments_demographic.py` | `compute_subgroup_cm(df, pred_col, subgroup_col)` — produces FPR/FNR/kappa/pi per subgroup from real LLM annotations vs ground truth |
| `exp_real_cm_validation.py` | Real CM validation with R² and diagnostic AUC |
| `analyze_hatespeech.py` | CivilComments per-subgroup bias amplification and Theorem 1 R² |

---

## 4. Recommended Demographic Subgroup Strategy

### Best Option: UC Berkeley Hate Speech with Annotator Demographics

**Why:** `data/exp004_raw.parquet` has 135K annotations with rich annotator demographics. This is the only dataset where we have both:
- Real annotator demographic attributes (age, gender, race, education, ideology)
- LLM annotations (GPT-4.1) on the same comments

**Proposed subgroups for EC-HTE analysis:**
1. **Annotator race**: White vs non-White (binary), or White/Black/Asian/Latinx (4-way)
2. **Annotator gender**: Men vs Women (binary)
3. **Annotator age**: Young (<30) vs Old (≥30), or 3 bins
4. **Annotator education**: College grad vs not
5. **Annotator ideology**: Liberal vs Conservative (using binary ideology field)

**Caveat:** Current exp004 processed data collapses to comment-level and loses annotator demographics. Need to re-process at annotation level or create annotator-subgroup × comment-level cross-tabulation.

### Second Option: CivilComments with Original Identity Columns

**Why:** Original CivilComments has 24 identity columns (male/female/black/white/muslim/etc.) but they're not in the current `exp023_llm_annotations.csv`. Need to:
1. Re-download CivilComments from HuggingFace (`google/civil_comments`)
2. Join identity columns to existing LLM annotations via `idx` column
3. Define subgroups by identity mentions (e.g., gender-mentioning vs race-mentioning comments)

**Proposed subgroups:**
- `mentions_race` (black/white/asian/latino > threshold)
- `mentions_gender` (male/female > threshold)
- `mentions_religion` (muslim/christian/jewish > threshold)
- `no_identity` (all identity columns near 0)

### Third Option: Stance Detection with Topic Subgroups (Already Done)

Already implemented in `exp_stance_analysis.py` with 5 stance targets as subgroups. Can be extended but no demographic dimension.

---

## 5. Missing Pieces

1. **CivilComments identity columns** not yet joined to LLM annotations — need ~10 lines of code to add
2. **UCB annotator demographics** not yet used for subgrouping in any experiment — need to re-process exp004_raw.parquet
3. **No per-annotator-demographic confusion matrices** computed yet — key gap for the demographic HTE story
4. **exp_civilcomments_demographic.py** uses keyword regex (crude proxy), not actual CivilComments identity columns
