# Dataset Survey: EC-HTE Project Real-World Data

Date: 2026-05-20

---

## 1. Ashwin et al. (2025) Dataset Accessibility

### Paper Information
- **Full title**: "Using Large Language Models for Qualitative Analysis can Introduce Serious Bias"
- **Authors**: Julian Ashwin, Aditya Chhabra, Vijayendra Rao
- **Venue**: *Sociological Methods & Research* (SAGE), 2025
- **DOI**: [10.1177/00491241251338246](https://journals.sagepub.com/doi/10.1177/00491241251338246)
- **arXiv**: [2309.17147](https://arxiv.org/abs/2309.17147)

### Dataset Description
- **Sample size**: 2,407 open-ended interviews
- **Population**: Rohingya refugees and their Bangladeshi hosts in Cox's Bazar, Bangladesh
- **Text type**: Interview transcripts about aspirations for eldest child and navigational capacity
- **Annotation type**: Qualitative coding tree with human-annotated codes; LLM annotations compared against human gold standard
- **Demographic subgroups**: Respondent characteristics (Rohingya vs. Bengali host, plus other interview-subject characteristics used to detect systematic LLM bias)
- **Code repository**: [github.com/worldbank/iQual](https://github.com/worldbank/iQual) (Python package for qualitative analysis pipeline)

### Data Availability: NOT PUBLICLY AVAILABLE
- Interview transcripts **cannot** be made publicly available due to **privacy and IRB/ethics restrictions**
- An **anonymised version is available upon request** from the authors
- No public data repository link (no Dataverse, OSF, Zenodo, or GitHub data release found)

### Author Contact
- **Julian Ashwin**, Assistant Professor, Maastricht University; Academic Consultant, World Bank
- **Email**: julian.ashwin@maastrichtuniversity.nl
- **Homepage**: [sites.google.com/view/julianashwin](https://sites.google.com/view/julianashwin/home)
- **NBER profile**: [nber.org/people/julian_ashwin](https://www.nber.org/people/julian_ashwin)

### Conclusion
The Ashwin dataset is **not publicly downloadable**. Obtaining it requires emailing the author for an anonymised version. Given the sensitive refugee population, approval may involve additional conditions. This introduces timeline risk and reproducibility constraints for our project.

---

## 2. Alternative CSS Datasets

### 2.1 UC Berkeley Measuring Hate Speech Corpus (RECOMMENDED #1)

| Field | Detail |
|-------|--------|
| **Paper** | Kennedy et al. (2022), "The Measuring Hate Speech Corpus", NLPerspectives @ ACL |
| **URL** | [huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech](https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech) |
| **Project site** | [hatespeech.berkeley.edu](https://hatespeech.berkeley.edu/) |
| **Sample size** | 50,070 social media comments (YouTube, Reddit, Twitter) |
| **Annotators** | 11,143 AMT workers |
| **Subgroup structure** | **8 target identity groups** (race/ethnicity, religion, national origin, gender, sexual orientation, age, disability, political ideology) with 42 subgroups; **6 annotator demographic dimensions** with 40 subgroups |
| **Annotation type** | 10 ordinal labels (sentiment, disrespect, insult, humiliation, dehumanization, violence, genocide, etc.) + continuous Rasch-scaled hate speech score + 3-class benchmark label |
| **Public download** | Yes, freely available on HuggingFace |
| **Limitations** | English only; social media text (not interview/survey); annotator demographics are about the annotators, not the text authors |

**Why recommended**: Richest demographic subgroup structure of any available dataset. Both target-group and annotator-group metadata enable HTE analysis along multiple axes. Large sample, validated annotation methodology (Rasch measurement theory), well-published.

---

### 2.2 Social Bias Inference Corpus / Social Bias Frames (RECOMMENDED #2)

| Field | Detail |
|-------|--------|
| **Paper** | Sap et al. (2020), "Social Bias Frames", ACL 2020 |
| **URL** | [huggingface.co/datasets/allenai/social_bias_frames](https://huggingface.co/datasets/allenai/social_bias_frames) |
| **Project site** | [maartensap.com/social-bias-frames](https://maartensap.com/social-bias-frames/) |
| **Sample size** | 150k+ structured annotations over social media posts |
| **Annotators** | Amazon Mechanical Turk workers |
| **Subgroup structure** | **Annotator demographics**: political leaning, race, age; **Target groups**: 1,000+ demographic groups mentioned in posts |
| **Annotation type** | Offensiveness, intent to offend, lewdness, target group, implied stereotype, free-text implication |
| **Public download** | Yes, freely available on HuggingFace |
| **Limitations** | Annotator demographic metadata is coarse; annotation task is somewhat complex (implied bias reasoning); may not map cleanly to standard classification |

**Why recommended**: Large scale, rich target-group taxonomy, annotator demographics available. Published at top venue. The implied-stereotype annotation adds a unique dimension for studying LLM reasoning vs. human judgment.

---

### 2.3 POPQUORN Dataset (RECOMMENDED #3)

| Field | Detail |
|-------|--------|
| **Paper** | Pei et al. (2023), "When Do Annotator Demographics Matter?", LAW @ ACL 2023 |
| **URL** | [github.com/Jiaxin-Pei/Potato-Prolific-Dataset](https://github.com/Jiaxin-Pei/Potato-Prolific-Dataset) |
| **Sample size** | 45,000 annotations from 1,484 annotators |
| **Annotators** | US-population-representative sample via Prolific |
| **Subgroup structure** | **Sex, age, race** (representative of US population) |
| **Annotation type** | 4 NLP tasks: offensiveness detection, question answering, politeness rating, text rewriting |
| **Public download** | Yes, freely available on GitHub |
| **Limitations** | Smaller sample of texts (annotations are dense per text); English only; limited to 3 demographic axes |

**Why recommended**: Explicitly designed to study how annotator demographics influence labels. US-representative sampling makes demographic subgroups well-defined and balanced. Multiple task types allow cross-task HTE analysis.

---

### 2.4 Jigsaw Unintended Bias in Toxicity Classification

| Field | Detail |
|-------|--------|
| **Paper** | Borkan et al. (2019), Kaggle competition dataset by Google/Jigsaw |
| **URL** | [huggingface.co/datasets/google/jigsaw_unintended_bias](https://huggingface.co/datasets/google/jigsaw_unintended_bias) |
| **Sample size** | ~2,000,000 comments |
| **Subgroup structure** | 9 identity mention columns: male, female, homosexual_gay_or_lesbian, Christian, Jewish, Muslim, black, white, psychiatric_or_mental_illness |
| **Annotation type** | Toxicity score (continuous), identity mention flags |
| **Public download** | Yes, on HuggingFace and Kaggle |
| **Limitations** | Identity columns indicate **mentions** in text, not author demographics; subgroups are binary flags, not metadata about the respondent |

**Why less ideal**: Very large scale but subgroup structure is based on identity mentions in text rather than author/respondent demographics. This is a different kind of subgroup than what EC-HTE typically needs (demographic metadata about the person generating the text).

---

### 2.5 Multilingual Twitter Hate Speech Corpus

| Field | Detail |
|-------|--------|
| **Paper** | Huang et al. (2020), "Multilingual Twitter Corpus and Baselines for Evaluating Demographic Bias in Hate Speech Recognition", LREC 2020 |
| **URL** | [github.com/xiaoleihuang/Multilingual_Fairness_LREC](https://github.com/xiaoleihuang/Multilingual_Fairness_LREC) |
| **Sample size** | Multi-language corpus (EN, IT, PL, PT, ES) |
| **Subgroup structure** | 4 inferred **author demographics**: age, country, gender, race/ethnicity |
| **Annotation type** | Hate speech labels |
| **Public download** | Partially; anonymized text available by email request (xiaolei.huang@memphis.edu) |
| **Limitations** | Demographics are **inferred** (not self-reported), requiring email request for full data; binarized demographic attributes |

**Why less ideal**: Interesting multilingual angle but demographics are inferred rather than ground-truth, and data requires email request.

---

### 2.6 StudentDebt Facebook Comments

| Field | Detail |
|-------|--------|
| **Paper** | Mishra & Collier (2020), "A Framework for Generating Annotated Social Media Corpora" |
| **URL** | [github.com/socialmediaie/StudentDebtFbComments](https://github.com/socialmediaie/StudentDebtFbComments) |
| **Sample size** | 3 datasets of Facebook comments on student loan discussions |
| **Subgroup structure** | Gender, military affiliation, age-group, political leaning, race |
| **Annotation type** | Stance, topicality, civility, neoliberal views |
| **Public download** | Yes, on GitHub |
| **Limitations** | Small sample size; narrow topic domain (student debt); may have limited generalizability |

**Why less ideal**: Rich demographic annotation but likely small scale. Good as a supplementary validation dataset.

---

## 3. Recommendation Ranking

| Rank | Dataset | Rationale |
|------|---------|-----------|
| **1** | **UC Berkeley Measuring Hate Speech** | Best combination of: large sample (50K comments, 11K annotators), rich subgroup structure on both target and annotator sides (8+6 demographic dimensions), validated continuous scale, fully public, well-published |
| **2** | **Social Bias Frames (SBIC)** | 150K+ annotations, 1000+ target groups, annotator demographics (politics/race/age), fully public; good for studying how annotator perspective interacts with LLM annotation |
| **3** | **POPQUORN** | Purpose-built for studying demographic influence on annotation; US-representative; 4 diverse tasks; fully public; smaller but cleanest experimental design |
| **4** | **Ashwin et al. (request)** | Most directly relevant to EC-HTE framing (interview data, qualitative coding, explicit LLM bias finding) but requires author permission; IRB constraints may limit use |
| **5** | **Jigsaw** | Massive scale but subgroups are text-mention-based, not respondent demographics |
| **6** | **Multilingual Twitter** | Inferred demographics + email-gated access |
| **7** | **StudentDebt FB** | Rich annotations but likely too small for robust HTE |

### Strategic Recommendation

Use **UC Berkeley Measuring Hate Speech** as the primary dataset for EC-HTE experiments: it has the richest subgroup structure, is fully public, and directly supports the project's core question (whether LLM annotation errors correlate with demographic characteristics). Supplement with **POPQUORN** for cross-task validation. In parallel, email Julian Ashwin to request the anonymised Rohingya interview data for a qualitative-coding replication that directly extends the original paper's findings.
