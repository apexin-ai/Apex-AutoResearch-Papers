# research missing citations bibtex

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing-citations-bibtex_20260518T074239_result.json`
- **Structured JSON:** [`68917b1e8a9b9a1e2b9b.json`](../../sessions/68/68917b1e8a9b9a1e2b9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 1. Shi et al.

### BibTeX
```bibtex
@inproceedings{shi2025collapse,
  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
  booktitle={Advances in Neural Information Processing Systems},
  year={2025}
}
```

### 摘要
揭示了 diffusion model 在合成数据迭代训练中存在从 generalization 到 memorization 的转变，并提出基于 entropy 的数据选择策略来缓解 model collapse。**注意：研究对象是 diffusion model 而非 LLM**，与本文关联点在于共享"递归合成数据训练导致退化"的核心问题框架。

### Venue 确认
NeurIPS 2025 Spotlight。arXiv ID: 2509.16499。

---

## 2. Gambetta et al.

### BibTeX
```bibtex
@article{gambetta2024surplexity,
  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI},
  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
  journal={arXiv preprint arXiv:2410.12341},
  year={2024}
}
```

### 摘要
提出 surplexity（模型对文档的"惊讶度"）作为筛选训练数据的指标，通过选择高 surplexity 的文档来缓解 model collapse，无需区分人工与 AI 生成数据。与本文关联点在于提供了一种基于 next-token 概率分布特征的 data curation 策略来对抗递归训练退化。

### Venue 确认
⚠️ 目前仅确认为 arXiv preprint（2410.12341，v3 更新于 2025-09）。OpenReview 上有提交记录（ID: zzk6DUQggQ），但未能确认具体会议录用情况。**论文正式标题含前缀 "Learning by Surprise:"，引用时注意使用完整标题。**

---

## 3. Amin et al.

### BibTeX
```bibtex
@inproceedings{amin2025escaping,
  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
  booktitle={Advances in Neural Information Processing Systems},
  year={2025}
}
```

### 摘要
从 boosting 理论出发，证明即使非合成训练数据质量很差（weak data），通过适度 curation 仍可避免 model collapse 并收敛到最优 LLM。与本文关联点在于为"合成数据迭代训练下如何维持模型质量"提供了理论保证和 data curation 的最小要求分析。

### Venue 确认
NeurIPS 2025 Poster。arXiv ID: 2502.08924。

Sources:
- [Shi et al. - NeurIPS 2025](https://neurips.cc/virtual/2025/poster/119754)
- [Shi et al. - arXiv](https://arxiv.org/abs/2509.16499)
- [Gambetta et al. - arXiv](https://arxiv.org/abs/2410.12341)
- [Gambetta et al. - OpenReview](https://openreview.net/pdf?id=zzk6DUQggQ)
- [Amin et al. - NeurIPS 2025](https://neurips.cc/virtual/2025/loc/san-diego/poster/115205)
- [Amin et al. - arXiv](https://arxiv.org/abs/2502.08924)

---
