# research missing bib entries

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing_bib_entries_20260519T033709_result.json`
- **Structured JSON:** [`50fb3c45259cf0e346b5.json`](../../sessions/50/50fb3c45259cf0e346b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部找到。以下是 4 个完整 BibTeX 条目：

---

### 1. physicalintelligence2025pi05

arXiv 2504.16054, 2025 年 4 月发布。

```bibtex
@article{physicalintelligence2025pi05,
  title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
  author={{Physical Intelligence} and Black, Kevin and Brown, Noah and Darpinian, James and Dhabalia, Karan and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Galliker, Manuel Y. and Ghosh, Dibya and Groom, Lachy and Hausman, Karol and Ichter, Brian and Jakubczak, Szymon and Jones, Tim and Ke, Liyiming and LeBlanc, Devin and Levine, Sergey and Li-Bell, Adrian and Mothukuri, Mohith and Nair, Suraj and Pertsch, Karl and Ren, Allen Z. and Shi, Lucy Xiaoyang and Smith, Laura and Springenberg, Jost Tobias and Stachowicz, Kyle and Tanner, James and Vuong, Quan and Walke, Homer and Walling, Anna and Wang, Haohuan and Yu, Lili and Zhilinsky, Ury},
  journal={arXiv preprint arXiv:2504.16054},
  year={2025},
  eprint={2504.16054},
  archivePrefix={arXiv}
}
```

---

### 2. zhang2023h2o

NeurIPS 2023 conference paper。

```bibtex
@inproceedings{zhang2023h2o,
  title={H$_2${O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
  author={Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  year={2023}
}
```

---

### 3. bouthillier2024negative

**注意：cite key 与实际第一作者不匹配。** 论文 "Position: Embracing Negative Results in Machine Learning" 的实际作者是 Karl, Kemeter, Dax, Sierak，并非 Bouthillier。建议将 cite key 改为 `karl2024negative`，但按你的要求保留原 key：

```bibtex
@inproceedings{bouthillier2024negative,
  title={Position: Embracing Negative Results in Machine Learning},
  author={Karl, Florian and Kemeter, Lukas Malte and Dax, Gabriel and Sierak, Paulina},
  booktitle={Proceedings of the 41st International Conference on Machine Learning},
  series={Proceedings of Machine Learning Research},
  volume={235},
  year={2024},
  publisher={PMLR}
}
```

---

### 4. zeng2023transformers_tsf

AAAI 2023 Oral paper。

```bibtex
@inproceedings{zeng2023transformers_tsf,
  title={Are Transformers Effective for Time Series Forecasting?},
  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={37},
  number={9},
  pages={11121--11128},
  year={2023}
}
```

---

**关于 #3 的建议：** `literature_map.yaml` 中将该论文标注为 `authors: "Bouthillier, Xavier and others"` 是错误的。实际第一作者是 Florian Karl。如果论文中用 `\cite{bouthillier2024negative}` 生成的引用格式是 `(Bouthillier et al., 2024)`，读者和审稿人会发现与实际论文不符。建议改为 `karl2024negative` 并更新 tex 文件中的引用。

---
