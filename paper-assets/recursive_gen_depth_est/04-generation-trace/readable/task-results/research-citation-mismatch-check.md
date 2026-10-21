# research citation mismatch check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation_mismatch_check_20260519T032126_result.json`
- **Structured JSON:** [`aa81d98872c6a61f3407.json`](../../sessions/aa/aa81d98872c6a61f3407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有搜索完成，汇总结果如下。

---

## 1. alemohammad2024\_mad

- **当前 bib**: authors = Alemohammad, Casco-Rodriguez, Luzi, Humayun, Babaei, LeJeune, Siahkoohi, Baraniuk; venue = ICLR; year = 2024
- **WebSearch 结果**: 完全一致。ICLR 2024, Vienna. 作者列表完整且正确。
- **差异**: **无**。该条目无需修改。

---

## 2. garces\_arias2025\_decoding\_decoded

- **当前 bib**: `author = {{Garces Arias}, Esteban and ...}`, booktitle = COLING, year = 2025
- **WebSearch 结果**: COLING 2025 (Abu Dhabi) 确认。作者: Esteban **Garcés** Arias, Meimingwei Li, Christian Heumann, Matthias Assenmacher。
- **差异**: 作者姓氏缺重音符号 `Garces` → `Garc{\'e}s`
- **修正建议**:

```bibtex
@inproceedings{garces_arias2025_decoding_decoded,
  author    = {{Garc{\'e}s Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
  booktitle = {Proceedings of COLING},
  year      = {2025},
  note      = {arXiv:2410.06097},
  url       = {https://arxiv.org/abs/2410.06097},
}
```

---

## 3. he2021\_deberta\_v3

- **当前 bib**: key = `he2021_deberta_v3`, year = **2023**, booktitle = ICLR
- **WebSearch 结果**: arXiv 首次提交 2021-11-18, 正式发表 **ICLR 2023**。
- **差异**: bib **key 名** 含 "2021" 但 year 字段正确写 2023。审稿人可能因 key 名产生误解，或因正文某处写了 "(He et al., 2021)" 而非 "(He et al., 2023)"。
- **修正建议**: 将 key 改为 `he2023_deberta_v3` 以消除歧义，并确保正文 `\cite` 同步更新。bib 内容本身（year=2023, ICLR）已正确。

```bibtex
@inproceedings{he2023_deberta_v3,
  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},
  booktitle = {Proceedings of ICLR},
  year      = {2023},
  note      = {arXiv:2111.09543},
  url       = {https://arxiv.org/abs/2111.09543},
}
```

---

## 4. llama3

- **当前 bib**: `@misc`, author = `Grattafiori, Aaron and Dubey, Abhimanyu and ... and others`, year = 2024
- **WebSearch 结果**: arXiv:2407.21783, 2024。第一作者 Aaron Grattafiori, 共 559 位作者。该论文为 arXiv 技术报告，未正式发表于会议。
- **差异**: 当前条目基本正确。可考虑的改进：
  - 截断作者列表时用 `and others` 是合理做法（BibTeX 标准）
  - 可补充 `doi = {10.48550/arXiv.2407.21783}`
- **修正建议**: 实质内容无错误，可选补充 DOI：

```bibtex
@misc{llama3,
  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},
  title     = {{The Llama 3 Herd of Models}},
  year      = {2024},
  howpublished = {arXiv:2407.21783},
  url       = {https://arxiv.org/abs/2407.21783},
}
```

---

## 5. guo2024\_biscope

- **当前 bib**: **该 key 不存在于 references.bib 中**。
- **WebSearch 结果**: "BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens", **NeurIPS 2024** 确认。Authors: Hanxi Guo, Siyuan Cheng, Xiaolong Jin, Zhuo Zhang, Kaiyuan Zhang, Guanhong Tao, Guangyu Shen, Xiangyu Zhang。
- **差异**: 条目缺失，需新增。
- **修正建议**:

```bibtex
@inproceedings{guo2024_biscope,
  author    = {Guo, Hanxi and Cheng, Siyuan and Jin, Xiaolong and Zhang, Zhuo and Zhang, Kaiyuan and Tao, Guanhong and Shen, Guangyu and Zhang, Xiangyu},
  title     = {{BiScope: AI-generated Text Detection by Checking Memorization of Preceding Tokens}},
  booktitle = {Proceedings of NeurIPS},
  year      = {2024},
  url       = {https://proceedings.neurips.cc/paper_files/paper/2024/hash/bc808cf2d2444b0abcceca366b771389-Abstract-Conference.html},
}
```

---

## 6. Muennighoff et al. — Scaling Data-Constrained Language Models (新引用)

- **WebSearch 结果**: **NeurIPS 2023**（非 2024）。Outstanding Main Track Paper Runner-Up。
- Authors: Niklas Muennighoff, Alexander M. Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus, Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, Colin Raffel
- **完整 BibTeX**:

```bibtex
@inproceedings{muennighoff2023_scaling,
  author    = {Muennighoff, Niklas and Rush, Alexander M. and Barak, Boaz and Le Scao, Teven and Piktus, Aleksandra and Tazi, Nouamane and Pyysalo, Sampo and Wolf, Thomas and Raffel, Colin},
  title     = {{Scaling Data-Constrained Language Models}},
  booktitle = {Proceedings of NeurIPS},
  year      = {2023},
  note      = {arXiv:2305.16264},
  url       = {https://arxiv.org/abs/2305.16264},
}
```

---

## 7. Ilyas et al. — Datamodels (新引用)

- **WebSearch 结果**: **ICML 2022** 确认 (PMLR vol. 162)。
- Authors: Andrew Ilyas, Sung Min Park, Logan Engstrom, Guillaume Leclerc, Aleksander Madry
- **完整 BibTeX**:

```bibtex
@inproceedings{ilyas2022_datamodels,
  author    = {Ilyas, Andrew and Park, Sung Min and Engstrom, Logan and Leclerc, Guillaume and Madry, Aleksander},
  title     = {{Datamodels: Understanding Predictions with Data and Data with Predictions}},
  booktitle = {Proceedings of ICML},
  year      = {2022},
  note      = {arXiv:2202.00622},
  url       = {https://arxiv.org/abs/2202.00622},
}
```

注意 ICML 正式标题为 "Datamodels: **Understanding** Predictions with Data and Data with Predictions"（与 arXiv 标题 "Predicting Predictions from Training Data" 略有不同）。

---

**汇总需要行动的项**:

| # | Key | 问题 | 操作 |
|---|-----|------|------|
| 2 | `garces_arias2025_decoding_decoded` | Garcés 缺重音 | 修改 author |
| 3 | `he2021_deberta_v3` | key 名含 2021 但实际 2023 | 改 key + 更新所有 `\cite` |
| 5 | `guo2024_biscope` | 条目缺失 | 新增 |
| 6 | `muennighoff2023_scaling` | 新引用，NeurIPS **2023** | 新增 |
| 7 | `ilyas2022_datamodels` | 新引用，ICML 2022 | 新增 |

条目 1 和 4 无实质错误。

---
