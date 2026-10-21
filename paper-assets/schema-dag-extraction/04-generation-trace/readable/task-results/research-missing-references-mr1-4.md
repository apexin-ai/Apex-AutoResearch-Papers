# research missing references mr1 4

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing_references_mr1_4_20260517T145447_result.json`
- **Structured JSON:** [`0e0355725b8c68d66979.json`](../../sessions/0e/0e0355725b8c68d66979.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已确认。MR4 有一个重要发现：COLING 2025 关于 universal entity taxonomy 的论文实际上是 Yang et al.（B2NER），而非 Fetahu/Li。Review report 可能记错了作者。

---

## MR1: Constrained Decoding — §Related Work / §Methodology (routing failure analysis)

```bibtex
@article{willard2023efficient,
  title     = {Efficient Guided Generation for Large Language Models},
  author    = {Willard, Brandon T. and Louf, R{\'e}mi},
  journal   = {arXiv preprint arXiv:2307.09702},
  year      = {2023},
  url       = {https://arxiv.org/abs/2307.09702}
}
```

Venue 说明：仅有 arXiv 预印本，未正式发表于会议/期刊。Outlines 库的基础论文。

---

## MR2: Batch Prompting — §Methodology (count-curve / efficiency)

```bibtex
@inproceedings{cheng2023batch,
  title     = {Batch Prompting: Efficient Inference with Large Language Model {API}s},
  author    = {Cheng, Zhoujun and Kasai, Jungo and Yu, Tao},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: Industry Track},
  pages     = {792--810},
  year      = {2023},
  address   = {Singapore},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2023.emnlp-industry.74/},
  doi       = {10.18653/v1/2023.emnlp-industry.74}
}
```

---

## MR3: Prompt Order Sensitivity — §Related Work (label ordering)

```bibtex
@inproceedings{lu2022fantastically,
  title     = {Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity},
  author    = {Lu, Yao and Bartolo, Max and Moore, Alastair and Riedel, Sebastian and Stenetorp, Pontus},
  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {8086--8098},
  year      = {2022},
  address   = {Dublin, Ireland},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2022.acl-long.556/},
  doi       = {10.18653/v1/2022.acl-long.556}
}
```

---

## MR4: Universal Entity Taxonomy — §Related Work (type hierarchy)

**注意**：Review round 12 标注为 "Fetahu/Li et al. (COLING 2025)"，但 COLING 2025 唯一关于 universal entity taxonomy 的论文是 Yang et al. (B2NER)。Fetahu 的相关工作是 MultiCoNER（SemEval-2023），并非 COLING 2025。请确认是否引用此篇：

```bibtex
@inproceedings{yang2025beyond,
  title     = {Beyond Boundaries: Learning a Universal Entity Taxonomy across Datasets and Languages for Open Named Entity Recognition},
  author    = {Yang, Yuming and Zhao, Wantong and Huang, Caishuang and Ye, Junjie and Wang, Xiao and Zheng, Huiyuan and Nan, Yang and Wang, Yuran and Xu, Xueying and Huang, Kaixin and Zhang, Yunke and Gui, Tao and Zhang, Qi and Huang, Xuanjing},
  booktitle = {Proceedings of the 31st International Conference on Computational Linguistics},
  pages     = {10902--10923},
  year      = {2025},
  address   = {Abu Dhabi, UAE},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2025.coling-main.725/}
}
```

如果 review 指的确实是 Fetahu 的工作，则应引的是 MultiCoNER 2（SemEval-2023）：

```bibtex
@inproceedings{fetahu2023semeval,
  title     = {{SemEval}-2023 Task 2: Fine-grained Multilingual Named Entity Recognition ({MultiCoNER} 2)},
  author    = {Fetahu, Besnik and Kar, Sudipta and Chen, Zhiyu and Rokhlenko, Oleg and Malmasi, Shervin},
  booktitle = {Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023)},
  year      = {2023},
  address   = {Toronto, Canada},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2023.semeval-1.310/}
}
```

MR1-MR3 信息已通过 ACL Anthology / arXiv 交叉验证。MR4 需要你确认 Yang et al. (COLING 2025) vs Fetahu et al. (SemEval 2023) 哪个是目标引用。

---
