# research r17 citation verify

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r17-citation-verify_20260523T145853_result.json`
- **Structured JSON:** [`6cb9212f651ba167587a.json`](../../sessions/6c/6cb9212f651ba167587a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 篇论文全部验证完毕，均真实存在。以下是完整报告：

---

## 论文 1: arXiv:2602.01763 ✅ 真实存在

| 项目 | 详情 |
|------|------|
| **标题** | A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention |
| **作者** | Xiaowei Ye, Xiaoyu He, Chao Liao, Chen Wu, Pinyan Lu |
| **提交日期** | 2026-02-02 |
| **类别** | cs.LG |
| **信息匹配度** | 审稿人声称 "Ye et al. (2026)" — **完全匹配**（第一作者 Ye，2026年） |
| **时间线** | ✅ 2026-02-02 早于 ARR 2026-05-25 deadline |
| **相关性** | 建立了 hybrid linear-full attention 的表达能力层级分离，证明线性注意力层无法替代全注意力层的组合能力。与本项目 hybrid recurrent architecture 中不同注意力机制的交互直接相关 |

**BibTeX:**
```bibtex
@article{ye2026provable,
  title={A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention},
  author={Ye, Xiaowei and He, Xiaoyu and Liao, Chao and Wu, Chen and Lu, Pinyan},
  journal={arXiv preprint arXiv:2602.01763},
  year={2026}
}
```

---

## 论文 2: arXiv:2601.09071 ✅ 真实存在

| 项目 | 详情 |
|------|------|
| **标题** | Resolving Predictive Multiplicity for the Rashomon Set |
| **作者** | Parian Haghighat, Hadis Anahideh, Cynthia Rudin |
| **提交日期** | 2026-01-14 |
| **类别** | cs.LG |
| **发表情况** | 同时出现在 AAAI 会议 proceedings 中 |
| **信息匹配度** | 审稿人声称标题 — **完全匹配** |
| **时间线** | ✅ 2026-01-14 早于 ARR 2026-05-25 deadline |
| **相关性** | 提出 3 种方法减少 Rashomon set 中模型预测不一致性（outlier correction, local patching, pairwise reconciliation）。与本项目 per-example predictive multiplicity 主题直接相关 |

**BibTeX:**
```bibtex
@inproceedings{haghighat2026resolving,
  title={Resolving Predictive Multiplicity for the Rashomon Set},
  author={Haghighat, Parian and Anahideh, Hadis and Rudin, Cynthia},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  year={2026}
}
```

---

## 论文 3: arXiv:2602.09520 ✅ 真实存在

| 项目 | 详情 |
|------|------|
| **标题** | Rashomon Sets and Model Multiplicity in Federated Learning |
| **作者** | Xenia Heilmann, Luca Corbucci, Mattia Cerrato |
| **提交日期** | 2026-02-10 |
| **类别** | cs.LG |
| **信息匹配度** | 审稿人声称标题 — **完全匹配** |
| **时间线** | ✅ 2026-02-10 早于 ARR 2026-05-25 deadline |
| **相关性** | 将 Rashomon set / predictive multiplicity 概念扩展到 federated learning，提出全局/局部/client-specific 三种 Rashomon set 定义。与本项目 multiplicity 分析框架有概念关联，但 federated learning 场景与本项目 hybrid recurrent architecture 场景有一定距离 |

**BibTeX:**
```bibtex
@article{heilmann2026rashomon,
  title={Rashomon Sets and Model Multiplicity in Federated Learning},
  author={Heilmann, Xenia and Corbucci, Luca and Cerrato, Mattia},
  journal={arXiv preprint arXiv:2602.09520},
  year={2026}
}
```

---

## 总结

| 论文 | 存在 | 信息匹配 | 时间线合规 | 引用价值 |
|------|------|----------|-----------|----------|
| Ye et al. (2602.01763) | ✅ | ✅ 完全匹配 | ✅ | **高** — hybrid attention 表达能力理论，直接支撑本文架构选择 |
| Haghighat et al. (2601.09071) | ✅ | ✅ 完全匹配 | ✅ | **高** — predictive multiplicity 解决方案，与本文核心主题对齐 |
| Heilmann et al. (2602.09520) | ✅ | ✅ 完全匹配 | ✅ | **中** — multiplicity 在 FL 的扩展，概念相关但场景不同 |

与之前 Watson-Daniels 引用不同，R17 建议的 3 篇论文全部真实存在，标题/作者/arXiv ID 均准确无误。论文 2 还被 AAAI 2026 正式收录。

Sources:
- [arXiv:2602.01763 - A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention](https://arxiv.org/abs/2602.01763)
- [arXiv:2601.09071 - Resolving Predictive Multiplicity for the Rashomon Set](https://arxiv.org/abs/2601.09071)
- [arXiv:2602.09520 - Rashomon Sets and Model Multiplicity in Federated Learning](https://arxiv.org/abs/2602.09520)

---
