# research citation verification

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification_20260520T104340_result.json`
- **Structured JSON:** [`1ae0e263ebe493667403.json`](../../sessions/1a/1ae0e263ebe493667403.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 篇搜索完毕，结果如下：

---

## 论文 1: Cross-Model Disagreement as a Label-Free Correctness Signal
- 存在性: ✅ 真实存在
- 实际标题: Cross-Model Disagreement as a Label-Free Correctness Signal
- 作者: Matt Gorbett, Suman Jana
- Venue: arXiv preprint, March 2026
- arXiv ID: 2603.25450
- URL: https://arxiv.org/abs/2603.25450
- BibTeX:
```bibtex
@article{gorbett2026crossmodel,
  title={Cross-Model Disagreement as a Label-Free Correctness Signal},
  author={Gorbett, Matt and Jana, Suman},
  journal={arXiv preprint arXiv:2603.25450},
  year={2026}
}
```
- 与本文相关性: 提出 Cross-Model Perplexity/Entropy 作为无标签正确性信号，与 §4.3 per-example divergence 的思路有交叉但角度不同——他们聚焦 deployment monitoring/selective prediction，本文聚焦 fine-tuning gating。可以在 Related Work 中讨论。

---

## 论文 2: The Hidden Attention of Mamba Models
- 存在性: ✅ 真实存在
- 实际标题: The Hidden Attention of Mamba Models
- 作者: Ameen Ali, Itamar Zimerman, Lior Wolf
- Venue: ACL 2025 (Long Paper)
- arXiv ID: 2403.01590
- URL: https://aclanthology.org/2025.acl-long.76/
- BibTeX:
```bibtex
@inproceedings{ali2025hidden,
  title={The Hidden Attention of Mamba Models},
  author={Ali, Ameen and Zimerman, Itamar and Wolf, Lior},
  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2025}
}
```
- 与本文相关性: 揭示 Mamba SSM 可等价为隐式 attention，与 Appendix D attention pattern analysis 方法论相关。如果 Appendix D 分析了 SSM-based 模型的 attention patterns，应当引用。

---

## 论文 3: Reconciling Model Multiplicity for Downstream Decision Making
- 存在性: ✅ 真实存在
- 实际标题: Reconciling Model Multiplicity for Downstream Decision Making
- 作者: Ally Yalei Du, Dung Daniel Ngo, Zhiwei Steven Wu
- Venue: ICLR 2025
- arXiv ID: 2405.19667
- URL: https://openreview.net/forum?id=uy4EavBEwl
- BibTeX:
```bibtex
@inproceedings{du2025reconciling,
  title={Reconciling Model Multiplicity for Downstream Decision Making},
  author={Du, Ally Yalei and Ngo, Dung Daniel and Wu, Zhiwei Steven},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2025}
}
```
- 与本文相关性: 直接处理 predictive multiplicity 下的 model reconciliation，与本文 entrainment gating 框架在 multiplicity 层面有理论联系。建议引用。

---

## 论文 4: Resolving Predictive Multiplicity for the Rashomon Set
- 存在性: ✅ 真实存在
- 实际标题: Resolving Predictive Multiplicity for the Rashomon Set
- 作者: Parian Haghighat, Hadis Anahideh, Cynthia Rudin
- Venue: arXiv preprint, January 2026
- arXiv ID: 2601.09071
- URL: https://arxiv.org/abs/2601.09071
- BibTeX:
```bibtex
@article{haghighat2026resolving,
  title={Resolving Predictive Multiplicity for the Rashomon Set},
  author={Haghighat, Parian and Anahideh, Hadis and Rudin, Cynthia},
  journal={arXiv preprint arXiv:2601.09071},
  year={2026}
}
```
- 与本文相关性: Rashomon set 上通过 outlier correction + local patching 降低 multiplicity，是 predictive multiplicity 理论的最新进展。如果本文涉及 Rashomon set 或 multiplicity resolution，应引用。

---

## 论文 5: Mamba-3
- 存在性: ✅ 真实存在
- 实际标题: Mamba-3: Improved Sequence Modeling using State Space Principles
- 作者: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- Venue: ICLR 2026
- arXiv ID: 2603.15569
- URL: https://openreview.net/forum?id=HwCvaJOiCj
- BibTeX:
```bibtex
@inproceedings{lahoti2026mamba3,
  title={Mamba-3: Improved Sequence Modeling using State Space Principles},
  author={Lahoti, Aakash and Li, Kevin Y. and Chen, Berlin and Wang, Caitlin and Bick, Aviv and Kolter, J. Zico and Dao, Tri and Gu, Albert},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2026}
}
```
- 与本文相关性: 最新 hybrid SSM architecture，如果本文实验涉及 Mamba 系列模型或讨论 hybrid architectures，可在 Related Work 中提及作为最新进展。

---

## 论文 6: D'Amour et al. Underspecification 年份验证
- 存在性: ⚠️ 存在，审稿人年份质疑不成立
- 实际情况:
  - arXiv 预印本: 2020 年 11 月 6 日 (arXiv:2011.03395)
  - JMLR 正式发表: 2022 年, Volume 23, Issue 226, pp. 1–61
- **结论: 当前 bib 引用 JMLR 2022 是正确的。** 审稿人说"应为 2020"是混淆了 arXiv 预印本日期和正式发表日期。学术引用应以正式发表版本为准。
- URL: https://www.jmlr.org/papers/v23/20-1335.html
- 当前 BibTeX 无需修改。

---

## 总结

| # | 论文 | 存在性 | 审稿人信息准确度 |
|---|------|--------|-----------------|
| 1 | Cross-Model Disagreement | ✅ 真实 | arXiv ID、年份均正确 |
| 2 | Hidden Attention of Mamba | ✅ 真实 | Venue、年份均正确 |
| 3 | Reconciling Model Multiplicity | ✅ 真实 | Venue、年份均正确 |
| 4 | Resolving Predictive Multiplicity | ✅ 真实 | arXiv ID、年份均正确 |
| 5 | Mamba-3 | ✅ 真实 | Venue、年份均正确 |
| 6 | D'Amour underspecification | ⚠️ 审稿人有误 | JMLR 2022 正确，非 2020 |

**5 篇遗漏引用全部真实存在**，非 AI 幻觉。论文 6 的年份质疑不成立，当前 bib 无需修改。

---
