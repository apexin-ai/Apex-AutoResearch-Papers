# BibTeX Fix Report

Date: 2026-05-26

## 1. `schulman2015trpo` — Author order fix

**Source**: arXiv abs/1502.05477

**Before**:
```
author = {Schulman, John and Levine, Sergey and Abbeel, Pieter and Jordan, Michael and Moritz, Philipp}
```

**After**:
```
author = {Schulman, John and Levine, Sergey and Moritz, Philipp and Jordan, Michael and Abbeel, Pieter}
```

## 2. `lightman2024lets` — Author name spelling fix

**Source**: arXiv abs/2305.20050

**Before**:
```
Burda, Yuri ... Edwards, Harrison
```

**After**:
```
Burda, Yura ... Edwards, Harri
```

## 3. `kazemnejad2024vineppo` — Title and venue update

**Source**: arXiv abs/2410.01679 (v2, accepted at ICML 2025)

**Before**:
```
title     = {VinePPO: Unlocking RL Potential For LLM Reasoning Through Refined Credit Assignment}
booktitle = {Advances in Neural Information Processing Systems}
year      = {2024}
```

**After**:
```
title     = {VinePPO: Refining Credit Assignment in RL Training of LLMs}
booktitle = {Proceedings of the International Conference on Machine Learning}
year      = {2025}
```

## 4. `gradientcoupling2025` — Title update (v1 → v4)

**Source**: arXiv abs/2509.23870 (v4)

**Before**:
```
title = {Rethinking Reward Miscalibration of GRPO in Agentic RL}
```

**After**:
```
title = {Gradient Coupling: The Hidden Barrier to Generalization in Agentic Reinforcement Learning}
```

## 5. `istar2025` — Venue update (arXiv → ICLR 2026)

**Source**: OpenReview forum id=ooROvpmxMV (ICLR 2026 Poster)

**Before**:
```
@article{istar2025,
  journal = {arXiv preprint arXiv:2509.19199},
  year    = {2025},
}
```

**After**:
```
@inproceedings{istar2025,
  booktitle = {International Conference on Learning Representations},
  year      = {2026},
}
```

## 6. `wang2024mathshepherd` — Venue name completion

**Source**: ACL Anthology 2024.acl-long.510

**Before**:
```
booktitle = {Proceedings of the Association for Computational Linguistics}
```

**After**:
```
booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}
```

## Compilation Result

```
pdflatex + bibtex + pdflatex + pdflatex: PASS
- 0 errors
- 0 undefined citations
- bibtex: 0 warnings
```
