# research bibliography expansion

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_bibliography_expansion_20260520T193235_result.json`
- **Structured JSON:** [`aa7fa8e8b4160730c2c6.json`](../../sessions/aa/aa7fa8e8b4160730c2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个方向搜索完成，共找到 15 篇已验证论文。以下是完整结果：

---

## 方向 1: Self-consuming / Model Collapse

### 论文 1

**标题**: A Tale of Tails: Model Collapse as a Change of Scaling Laws
**作者**: Elvis Dohmatob, Yunzhen Feng, Pu Yang, François Charton, Julia Kempe
**发表**: ICML 2024 (PMLR 235)
**arXiv ID**: 2402.07043

**BibTeX**:
```bibtex
@inproceedings{dohmatob2024tale,
  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Fran\c{c}ois and Kempe, Julia},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {235},
  pages     = {11389--11413},
  year      = {2024},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v235/dohmatob24b.html}
}
```

**与本文关联**: 证明微量合成数据即可改变 scaling law 指数并引发 collapse，为 generation depth fingerprint 信号随迭代增强提供理论支撑
**建议引用位置**: Related Work (Model Collapse) / Discussion

> 注意：与已引 strong_model_collapse 同为 Dohmatob 组 ICML 2024 论文，但为不同工作（scaling law 视角 vs. 收敛证明）。

---

### 论文 2

**标题**: Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data
**作者**: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, et al.
**发表**: COLM 2024 (First Conference on Language Modeling)
**arXiv ID**: 2404.01413

**BibTeX**:
```bibtex
@inproceedings{gerstgrasser2024model,
  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},
  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
  booktitle = {First Conference on Language Modeling},
  year      = {2024},
  url       = {https://openreview.net/forum?id=5B2K4LRgmz}
}
```

**与本文关联**: 证明积累原始数据可避免 collapse，暗示 generation depth 信号源于真实的分布漂移而非采样 artifact
**建议引用位置**: Related Work / Introduction

---

### 论文 3

**标题**: How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse
**作者**: Mohamed El Amine Seddik, Suei-Wen Chen, Soufiane Hayou, Pierre Youssef, Merouane Debbah
**发表**: arXiv preprint, 2024
**arXiv ID**: 2404.05090

**BibTeX**:
```bibtex
@article{seddik2024bad,
  title   = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},
  author  = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
  journal = {arXiv preprint arXiv:2404.05090},
  year    = {2024},
  url     = {https://arxiv.org/abs/2404.05090}
}
```

**与本文关联**: 推导出触发 collapse 的合成数据比例阈值，量化了 depth-dependent 分布侵蚀
**建议引用位置**: Related Work / Discussion

---

## 方向 2: Watermarking 与 Recursive Generation

### 论文 1

**标题**: Revisiting the Robustness of Watermarking to Paraphrasing Attacks
**作者**: Saksham Rastogi, Danish Pruthi
**发表**: EMNLP 2024 (Main)
**arXiv ID**: 2411.05277

**BibTeX**:
```bibtex
@inproceedings{rastogi-pruthi-2024-revisiting,
    title     = {Revisiting the Robustness of Watermarking to Paraphrasing Attacks},
    author    = {Rastogi, Saksham and Pruthi, Danish},
    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
    year      = {2024},
    address   = {Miami, Florida, USA},
    publisher = {Association for Computational Linguistics},
    url       = {https://aclanthology.org/2024.emnlp-main.1005}
}
```

**与本文关联**: 量化 green-list watermark 在 paraphrase attack 下的信号衰减，说明 token 分布扰动在再生成步骤中的脆弱性
**建议引用位置**: Related Work (watermarking)

---

### 论文 2

**标题**: Watermark under Fire: A Robustness Evaluation of LLM Watermarking
**作者**: Jiacheng Liang, Zian Wang, Spencer Hong, Shouling Ji, Ting Wang
**发表**: Findings of EMNLP 2025
**arXiv ID**: 2411.13425

**BibTeX**:
```bibtex
@inproceedings{liang-etal-2025-watermark,
    title     = {Watermark under Fire: A Robustness Evaluation of {LLM} Watermarking},
    author    = {Liang, Jiacheng and Wang, Zian and Hong, Spencer and Ji, Shouling and Wang, Ting},
    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
    year      = {2025},
    publisher = {Association for Computational Linguistics},
    url       = {https://aclanthology.org/2025.findings-emnlp.1148}
}
```

**与本文关联**: 统一评估 10 种 watermarker 在 12 类攻击下的表现，为讨论 watermark 信号在迭代生成中的存活率提供方法论参考
**建议引用位置**: Related Work

---

### 论文 3

**标题**: Downstream Trade-offs of a Family of Text Watermarks
**作者**: Anirudh Ajith, Sameer Singh, Danish Pruthi
**发表**: EMNLP 2023
**arXiv ID**: 2311.09816

**BibTeX**:
```bibtex
@inproceedings{ajith-etal-2023-downstream,
    title     = {Downstream Trade-offs of a Family of Text Watermarks},
    author    = {Ajith, Anirudh and Singh, Sameer and Pruthi, Danish},
    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    year      = {2023},
    publisher = {Association for Computational Linguistics},
    url       = {https://arxiv.org/abs/2311.09816}
}
```

**与本文关联**: 证明 KGW 类 watermark 会使 output token 分布产生可测量的统计偏移（下游任务下降 10–20%），支持 watermark-induced 分布偏移随 depth 累积的论点
**建议引用位置**: Related Work / Discussion

---

## 方向 3: Membership Inference 与 LLM 文本检测

### 论文 1

**标题**: ReCaLL: Membership Inference via Relative Conditional Log-Likelihoods
**作者**: Roy Xie, Junlin Wang, Ruomin Huang, Minxing Zhang, Rong Ge, Jian Pei, Neil Zhenqiang Gong, Bhuwan Dhingra
**发表**: EMNLP 2024 (Main), pp. 8671–8689
**arXiv ID**: 2406.15968

**BibTeX**:
```bibtex
@inproceedings{xie-etal-2024-recall,
  title     = {{R}e{C}a{LL}: Membership Inference via Relative Conditional Log-Likelihoods},
  author    = {Xie, Roy and Wang, Junlin and Huang, Ruomin and Zhang, Minxing and
               Ge, Rong and Pei, Jian and Gong, Neil Zhenqiang and Dhingra, Bhuwan},
  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
  year      = {2024},
  pages     = {8671--8689},
  address   = {Miami, Florida, USA},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2024.emnlp-main.493}
}
```

**与本文关联**: 将 LLM 生成文本检测形式化为 membership inference（比较 conditional log-likelihood ratio），为用模型内部信号做 depth attribution 提供统计检验框架
**建议引用位置**: Related Work (detection methods)

---

### 论文 2

**标题**: Do Membership Inference Attacks Work on Large Language Models?
**作者**: Michael Duan, Anshuman Suri, Niloofar Mireshghallah, Sewon Min, Weijia Shi, et al.
**发表**: arXiv preprint, 2024 (COLM 2024 under review)
**arXiv ID**: 2402.07841

**BibTeX**:
```bibtex
@article{duan2024membership,
  title   = {Do Membership Inference Attacks Work on Large Language Models?},
  author  = {Duan, Michael and Suri, Anshuman and Mireshghallah, Niloofar and
             Min, Sewon and Shi, Weijia and Zettlemoyer, Luke and Tsvetkov, Yulia
             and Choi, Yejin and Evans, David and Hajishirzi, Hannaneh},
  journal = {arXiv preprint arXiv:2402.07841},
  year    = {2024},
  url     = {https://arxiv.org/abs/2402.07841}
}
```

**与本文关联**: 大规模实证表明 likelihood-ratio MIA 在大数据少 epoch 训练下信号微弱，解释了为什么需要 depth-specific fingerprint 而非简单 MIA 分数
**建议引用位置**: Related Work（动机论证）

---

### 论文 3

**标题**: Machine Text Detectors are Membership Inference Attacks
**作者**: Ryuto Koike, Liam Dugan, Masahiro Kaneko, Chris Callison-Burch, Naoaki Okazaki
**发表**: arXiv preprint, 2025
**arXiv ID**: 2510.19492

**BibTeX**:
```bibtex
@article{koike2025machine,
  title   = {Machine Text Detectors are Membership Inference Attacks},
  author  = {Koike, Ryuto and Dugan, Liam and Kaneko, Masahiro and
             Callison-Burch, Chris and Okazaki, Naoaki},
  journal = {arXiv preprint arXiv:2510.19492},
  year    = {2025},
  url     = {https://arxiv.org/abs/2510.19492}
}
```

**与本文关联**: 从理论上证明 machine text detector 和 MIA 等价（利用相同分布信号），为 detection-as-inference 视角提供统一框架
**建议引用位置**: Related Work（与 DetectGPT 并列引用）

---

## 方向 4: AI Text Detection Survey（2025–2026）

### 论文 1

**标题**: A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions
**作者**: Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Derek F. Wong, Lidia S. Chao
**发表**: Computational Linguistics, 51(1):275–338, 2025 (MIT Press / ACL)
**arXiv ID**: 2310.14724

**BibTeX**:
```bibtex
@article{wu-etal-2025-survey,
  title     = {A Survey on {LLM}-Generated Text Detection:
               Necessity, Methods, and Future Directions},
  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and
               Yuan, Yulin and Wong, Derek F. and Chao, Lidia S.},
  journal   = {Computational Linguistics},
  volume    = {51},
  number    = {1},
  pages     = {275--338},
  year      = {2025},
  publisher = {MIT Press},
  doi       = {10.1162/coli\_a\_00549},
  url       = {https://aclanthology.org/2025.cl-1.8}
}
```

**与本文关联**: ACL 旗舰期刊最权威的检测综述，系统覆盖 watermarking/zero-shot/fine-tuning/adversarial 四类范式，可用于定位 generation depth 在现有 taxonomy 中的空白
**建议引用位置**: Introduction / Related Work

---

### 论文 2

**标题**: The Imitation Game Revisited: A Comprehensive Survey on Recent Advances in AI-Generated Text Detection
**作者**: Zhiwei Yang, Zhengjie Feng, Rongxin Huo, Huiru Lin, et al.
**发表**: Expert Systems with Applications, Vol. 272, 2025
**DOI**: 10.1016/j.eswa.2025.126694

**BibTeX**:
```bibtex
@article{yang2025imitation,
  title   = {The Imitation Game Revisited: A Comprehensive Survey on
             Recent Advances in {AI}-Generated Text Detection},
  author  = {Yang, Zhiwei and Feng, Zhengjie and Huo, Rongxin and
             Lin, Huiru and Zheng, Hanghan and Nie, Ruichi and Chen, Hongrui},
  journal = {Expert Systems with Applications},
  volume  = {272},
  pages   = {126694},
  year    = {2025},
  publisher = {Elsevier},
  doi     = {10.1016/j.eswa.2025.126694}
}
```

**与本文关联**: 维护活跃 paper list 的全面综述，可用于支撑 "现有综述未涉及 generation depth 维度" 的论点
**建议引用位置**: Introduction

---

### 论文 3

**标题**: Human or Machine? A Survey on Machine-Generated Text Detection
**作者**: Zeeshan Ahmad, Marco Torres-Ruiz, Adeel Mahmood, Rolando Quintero, Iqra Ameer, Nilufar Bölücü
**发表**: IEEE Access, Vol. 14, pp. 34113–34136, 2026
**DOI**: 10.1109/ACCESS.2026.3666781

**BibTeX**:
```bibtex
@article{ahmad2026human,
  title   = {Human or Machine? {A} Survey on Machine-Generated Text Detection},
  author  = {Ahmad, Zeeshan and Torres-Ruiz, Marco and Mahmood, Adeel and
             Quintero, Rolando and Ameer, Iqra and B{\"{o}}l{\"{u}}c{\"{u}}, Nilufar},
  journal = {IEEE Access},
  volume  = {14},
  pages   = {34113--34136},
  year    = {2026},
  doi     = {10.1109/ACCESS.2026.3666781}
}
```

**与本文关联**: 2026 年最新综述，评估 30 个 benchmark 语料（>4M 样本）和 44 项实证研究，其 MGT 语言特征分析（低 perplexity、简单形态）直接支撑 deeper structural signals 的必要性
**建议引用位置**: Introduction / Related Work

---

## 方向 5: Ordinal Regression in NLP

### 论文 1

**标题**: Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation
**作者**: Wenzhi Cao, Vahid Mirjalili, Sebastian Raschka
**发表**: Pattern Recognition Letters, 140:325–331, 2020
**arXiv ID**: 1901.07884

**BibTeX**:
```bibtex
@article{cao2020coral,
  title     = {Rank Consistent Ordinal Regression for Neural Networks with
               Application to Age Estimation},
  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
  journal   = {Pattern Recognition Letters},
  volume    = {140},
  pages     = {325--331},
  year      = {2020},
  publisher = {Elsevier},
  doi       = {10.1016/j.patrec.2020.11.008},
  archivePrefix = {arXiv},
  eprint    = {1901.07884}
}
```

**与本文关联**: 提出 CORAL 框架——将 ordinal target 转化为带权重共享约束的 binary subtask，保证 rank-monotonic 概率估计，是 depth classifier ordinal output head 的核心技术基础
**建议引用位置**: Method（引入 ordinal loss 时）

---

### 论文 2

**标题**: Cumulative Link Models for Deep Ordinal Classification
**作者**: Víctor Manuel Vargas, Pedro Antonio Gutiérrez, César Hervás-Martínez
**发表**: Neurocomputing, 401:48–58, 2020
**arXiv ID**: 1905.13392

**BibTeX**:
```bibtex
@article{vargas2020clm,
  title     = {Cumulative Link Models for Deep Ordinal Classification},
  author    = {Vargas, V{\'i}ctor Manuel and Guti{\'e}rrez, Pedro Antonio and
               Herv{\'a}s-Mart{\'i}nez, C{\'e}sar},
  journal   = {Neurocomputing},
  volume    = {401},
  pages     = {48--58},
  year      = {2020},
  publisher = {Elsevier},
  doi       = {10.1016/j.neucom.2020.03.034},
  archivePrefix = {arXiv},
  eprint    = {1905.13392}
}
```

**与本文关联**: 提出 cumulative link model (proportional-odds) 输出层用于深度网络 ordinal classification，是 CORAL 的理论替代方案
**建议引用位置**: Method / Related Work

---

### 论文 3

**标题**: Exploring Ordinality in Text Classification: A Comparative Study of Explicit and Implicit Techniques
**作者**: Siva Rajesh Kasa, Aniket Goel, Karan Gupta, et al.
**发表**: Findings of ACL 2024
**arXiv ID**: 2405.11775

**BibTeX**:
```bibtex
@inproceedings{kasa2024ordinality,
  title     = {Exploring Ordinality in Text Classification: A Comparative Study
               of Explicit and Implicit Techniques},
  author    = {Kasa, Siva Rajesh and Goel, Aniket and Gupta, Karan and
               Roychowdhury, Sumegh and Priyatam, Pattisapu and
               Bhanushali, Anish and {Srinivasa Murthy}, Prasanna},
  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
  pages     = {5390--5404},
  year      = {2024},
  address   = {Bangkok, Thailand},
  publisher = {Association for Computational Linguistics},
  doi       = {10.18653/v1/2024.findings-acl.320},
  url       = {https://aclanthology.org/2024.findings-acl.320/}
}
```

**与本文关联**: 在 NLP 任务（情感/评分）上对比 explicit ordinal loss vs. implicit PLM label semantics，是将 ordinal regression 应用于文本分类的最直接 NLP 先例
**建议引用位置**: Related Work / Method

---

## 汇总

| 方向 | 论文数 | 发表级别 | 备注 |
|------|--------|---------|------|
| 1. Model Collapse | 3 | ICML×1, COLM×1, preprint×1 | Dohmatob 2024b 与已引 strong_model_collapse 是不同论文 |
| 2. Watermarking | 3 | EMNLP×2, Findings EMNLP×1 | 全部 peer-reviewed |
| 3. Membership Inference | 3 | EMNLP×1, preprint×2 | Koike 2025 最切合但尚未正式发表 |
| 4. Detection Survey | 3 | CL×1, ESWA×1, IEEE Access×1 | Wu 2025 (CL) 权威性最高 |
| 5. Ordinal Regression | 3 | PRL×1, Neurocomputing×1, Findings ACL×1 | Kasa 2024 是唯一 NLP-specific |

所有 arXiv ID / DOI 均已通过搜索验证。建议引入 bib 前用 `reference-audit` skill 做最终校验。

---
