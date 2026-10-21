# Reference Verification Report

Date: 2025-05-17

## 1. Hammoudeh & Lowd 2024

- **Status**: VERIFIED (real paper)
- **Title**: Training Data Influence Analysis and Estimation: A Survey
- **Authors**: Zayd Hammoudeh, Daniel Lowd
- **Year**: 2024
- **Venue**: Machine Learning (Springer), Volume 113, pp. 2351--2403
- **arXiv**: 2212.04612
- **DOI**: 10.1007/s10994-023-06495-7

**Summary**: First comprehensive survey of training data influence analysis and estimation. Formalizes definitions of training data influence, organizes methods into a taxonomy (retraining-based vs. gradient-based), and compares assumptions, complexities, and trade-offs.

**Relevance to depth fingerprinting**: Moderate. Training data attribution quantifies how individual training instances affect model behavior, which is conceptually related to identifying generative model fingerprints. However, this is a survey of influence estimation methods (influence functions, data Shapley, etc.), not directly about text generation detection. Appropriate as background reference if the paper discusses how training data shapes generator-specific artifacts, but not a core related work for stylometric detection.

**Current citation status**: Not yet cited in the paper bib files.

---

## 2. Kumarage et al. 2023

- **Status**: VERIFIED (real paper)
- **Title**: Stylometric Detection of AI-Generated Text in Twitter Timelines
- **Authors**: Tharindu Kumarage, Joshua Garland, Amrita Bhattacharjee, Kirill Trapeznikov, Scott Ruston, Huan Liu
- **Year**: 2023
- **arXiv**: 2303.03697
- **Venue**: arXiv preprint (cited in multiple survey papers; no formal journal/conference publication identified)

**Summary**: Proposes a stylometric approach to detect AI-generated tweets, using a fusion of fine-tuned RoBERTa with lexical, syntactic, and structural stylometric features (lexical richness, readability, punctuation counts). Addresses two tasks: discriminating human vs. AI tweets, and detecting the point in a timeline when AI generation begins.

**Relevance to depth fingerprinting**: High. Directly relevant as related work on LLM-generated text detection using stylometric signals. The use of linguistic features to distinguish human from AI text is closely aligned with depth fingerprinting's goal of identifying generator-specific stylistic patterns. Good candidate for the Related Work section under "detection methods" or "stylometric approaches."

**Current citation status**: Not yet cited in the paper bib files.

---

## Suggested BibTeX Entries

```bibtex
@article{hammoudeh2024training,
  title={Training Data Influence Analysis and Estimation: A Survey},
  author={Hammoudeh, Zayd and Lowd, Daniel},
  journal={Machine Learning},
  volume={113},
  pages={2351--2403},
  year={2024},
  publisher={Springer},
  doi={10.1007/s10994-023-06495-7}
}

@article{kumarage2023stylometric,
  title={Stylometric Detection of {AI}-Generated Text in Twitter Timelines},
  author={Kumarage, Tharindu and Garland, Joshua and Bhattacharjee, Amrita and Trapeznikov, Kirill and Ruston, Scott and Liu, Huan},
  journal={arXiv preprint arXiv:2303.03697},
  year={2023}
}
```
