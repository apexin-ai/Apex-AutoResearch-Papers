# Reference Verification Report

Date: 2026-05-23

---

## 1. Seddik et al. 2024

**Status: CONFIRMED**

- **Title:** How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse
- **Authors:** Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah
- **Venue:** COLM 2024 (First Conference on Language Modeling)
- **arXiv:** 2404.05090
- **OpenReview:** https://openreview.net/forum?id=t3z6UlV09o

**Summary:** Provides statistical/theoretical analysis of model collapse when training on synthetic data. Shows collapse is unavoidable with pure synthetic data (tails vanish), but identifies a mixing threshold below which collapse can be avoided.

**Relevance:** Highly relevant. Directly studies model collapse in recursive training from a distributional/statistical angle, complementing our spectral perspective.

```bibtex
@inproceedings{seddik2024how,
  title={How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse},
  author={Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
  booktitle={First Conference on Language Modeling (COLM)},
  year={2024},
  url={https://openreview.net/forum?id=t3z6UlV09o}
}
```

---

## 2. Self-Verification (Weng et al. 2023)

**Status: CONFIRMED**

- **Title:** Large Language Models are Better Reasoners with Self-Verification
- **Authors:** Yixuan Weng, Minjun Zhu, Fei Xia, Bin Li, Shizhu He, Shengping Liu, Bin Sun, Kang Liu, Jun Zhao
- **Venue:** Findings of EMNLP 2023, pages 2550-2575
- **arXiv:** 2212.09561
- **ACL Anthology:** https://aclanthology.org/2023.findings-emnlp.167/

**Summary:** Proposes backward verification for LLM reasoning — uses the conclusion to reconstruct the original problem, computing a verification score to select the best answer.

**Relevance:** NOT directly relevant to model collapse or spectral collapse. This is about inference-time reasoning verification, not training-time collapse detection. Unless the paper is being cited for a different purpose (e.g., general self-assessment of model outputs), the connection to our work is tangential.

```bibtex
@inproceedings{weng-etal-2023-self-verification,
  title={Large Language Models are Better Reasoners with Self-Verification},
  author={Weng, Yixuan and Zhu, Minjun and Xia, Fei and Li, Bin and He, Shizhu and Liu, Shengping and Sun, Bin and Liu, Kang and Zhao, Jun},
  booktitle={Findings of the Association for Computational Linguistics: EMNLP 2023},
  year={2023},
  publisher={Association for Computational Linguistics},
  pages={2550--2575},
  url={https://aclanthology.org/2023.findings-emnlp.167/}
}
```

---

## 3. Escaping Collapse

**Status: CONFIRMED — Two candidate papers found**

### 3a. Yi et al. (ICLR 2026)

- **Title:** Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence
- **Authors:** Bingji Yi, Qiyuan Liu, Yuwei Cheng, Haifeng Xu
- **Venue:** ICLR 2026 (Poster)
- **arXiv:** 2510.16657

**Summary:** Shows that an external synthetic data verifier prevents model collapse in iterative retraining. Performance converges to the verifier's knowledge boundary. Experiments on linear regression, VAEs (MNIST), and SmolLM2-135M (XSUM).

```bibtex
@inproceedings{yi2026escaping,
  title={Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence},
  author={Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2026},
  url={https://arxiv.org/abs/2510.16657}
}
```

### 3b. Amin et al. (NeurIPS 2025)

- **Title:** Escaping Collapse: The Strength of Weak Data for Large Language Model Training
- **Authors:** Kareem Amin, Sara Babakniya, Alex Bie, Weiwei Kong, Umar Syed, Sergei Vassilvitskii
- **Venue:** NeurIPS 2025 (Poster)
- **arXiv:** 2502.08924

**Summary:** Shows that minimal curation of synthetic data suffices for continual improvement across iterative training. Subsumes methods like STaR, ReST. Inspired by boosting theory.

```bibtex
@inproceedings{amin2025escaping,
  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
  year={2025},
  url={https://arxiv.org/abs/2502.08924}
}
```

**Relevance (both):** Moderately relevant. Both study collapse avoidance/mitigation in recursive training. Neither uses spectral analysis. Useful as related work on "collapse prevention strategies" that motivate the need for early warning signals.

**Note:** Director should clarify which of these two is intended, or whether both should be cited.

---

## 4. Golden Ratio

**Status: CONFIRMED**

- **Title:** Golden Ratio Weighting Prevents Model Collapse
- **Authors:** Hengzhi He, Shirong Xu, Guang Cheng (UCLA)
- **Venue:** arXiv preprint (no conference acceptance as of Oct 2025)
- **arXiv:** 2502.18049

**Summary:** Studies optimal weighting of real vs. synthetic data in iterative training across Gaussian estimation, GLMs, and nonparametric settings. Finds the optimal real-data weight converges to 1/phi (~0.618, the golden ratio reciprocal).

**Relevance:** Directly relevant to model collapse prevention via data mixing. Provides theoretical grounding for mixing ratios that our spectral EWS could complement (detect when mixing is insufficient). Note: preprint only, not peer-reviewed.

```bibtex
@article{he2025golden,
  title={Golden Ratio Weighting Prevents Model Collapse},
  author={He, Hengzhi and Xu, Shirong and Cheng, Guang},
  journal={arXiv preprint arXiv:2502.18049},
  year={2025}
}
```

---

## Summary

| # | Query | Found | Venue | Relevant |
|---|-------|-------|-------|----------|
| 1 | Seddik et al. 2024 | Yes | COLM 2024 | High |
| 2 | Self-Verification | Yes | Findings EMNLP 2023 | Low (tangential) |
| 3 | Escaping Collapse | Yes (2 papers) | ICLR 2026 / NeurIPS 2025 | Moderate |
| 4 | Golden Ratio | Yes | arXiv preprint | High |
