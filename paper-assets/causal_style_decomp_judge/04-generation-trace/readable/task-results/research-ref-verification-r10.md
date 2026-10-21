# research ref verification r10

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-verification-r10_20260522T094209_result.json`
- **Structured JSON:** [`214e1c5671e4bd0074aa.json`](../../sessions/21/214e1c5671e4bd0074aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有搜索完成，以下是验证结果。

---

## Reference 1: Simms, Zelazny, Williams & Bernstein (2019)
- **状态**: 存在 ✓
- **完整标题**: Does the Number of Response Options Matter? Psychometric Perspectives Using Personality Questionnaire Data
- **作者**: Leonard J. Simms, Kerry Zelazny, Thomas F. Williams, Lauren Bernstein
- **Venue/Journal**: *Psychological Assessment*, Vol. 31, No. 4, pp. 557–566
- **DOI**: 10.1037/pas0000648
- **PMID**: 30869956
- **BibTeX**:
```bibtex
@article{simms2019response,
  title={Does the Number of Response Options Matter? {Psychometric} Perspectives Using Personality Questionnaire Data},
  author={Simms, Leonard J. and Zelazny, Kerry and Williams, Thomas F. and Bernstein, Lauren},
  journal={Psychological Assessment},
  volume={31},
  number={4},
  pages={557--566},
  year={2019},
  doi={10.1037/pas0000648}
}
```
- **与本文关联**: 该论文发现 2–5 个选项的量表 psychometric precision 下降，偶数选项优于奇数选项。直接支持 C2 (Likert Blindspot)——5-point Likert 的 tie rate 高可能与 scale granularity 不足有关，偶数量表消除中间选项可能改善 discriminability。
- **建议引用位置**: Discussion 或 Limitations，讨论 Likert scale design 对 judge 评分行为的影响。

---

## Reference 2: Polo et al. (2024) — tinyBenchmarks
- **状态**: 存在 ✓
- **完整标题**: tinyBenchmarks: Evaluating LLMs with Fewer Examples
- **作者**: Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- **Venue/Journal**: ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)
- **链接**: [PMLR](https://proceedings.mlr.press/v235/maia-polo24a.html), [arXiv:2402.14992](https://arxiv.org/abs/2402.14992)
- **BibTeX**:
```bibtex
@inproceedings{polo2024tinybenchmarks,
  title={tinyBenchmarks: Evaluating {LLMs} with Fewer Examples},
  author={Maia Polo, Felipe and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
  year={2024},
  url={https://arxiv.org/abs/2402.14992}
}
```
- **与本文关联**: 使用 IRT (Item Response Theory) 来评估 LLM 能力，与本文使用 BT model 类似的 psychometric approach。展示了 psychometric modeling 在 LLM evaluation 中的可行性。
- **建议引用位置**: Related Work — evaluation methodology 部分，与 BT model 的 psychometric 方法并列讨论。

---

## Reference 3: Kocmi & Federmann (2023)
- **状态**: 存在，但需注意适用性 ⚠️
- **完整标题**: Large Language Models Are State-of-the-Art Evaluators of Translation Quality
- **作者**: Tom Kocmi, Christian Federmann
- **Venue/Journal**: EAMT 2023 (Proceedings of the 24th Annual Conference of the European Association for Machine Translation)
- **链接**: [ACL Anthology](https://aclanthology.org/2023.eamt-1.19/), [arXiv:2302.14520](https://arxiv.org/abs/2302.14520)
- **BibTeX**:
```bibtex
@inproceedings{kocmi2023large,
  title={Large Language Models Are State-of-the-Art Evaluators of Translation Quality},
  author={Kocmi, Tom and Federmann, Christian},
  booktitle={Proceedings of the 24th Annual Conference of the European Association for Machine Translation (EAMT)},
  pages={193--203},
  year={2023},
  url={https://aclanthology.org/2023.eamt-1.19/}
}
```
- **与本文关联**: 该论文的核心贡献是 GEMBA（用 GPT 做 MT 评估），涉及 pairwise 和 pointwise 两种 prompt 模式。但其关注点是**机器翻译质量评估**，而非通用 LLM judge bias across evaluation formats。论文中确实比较了不同 prompt 格式，但 bias 分析不是主要内容。
- **风险提示**: 如果引用意图是 "LLM judge 在不同评估 format 下表现出不同 bias"，这篇的支撑力偏弱。bib 中已有的 `tripathi2025pairwise`（Pairwise or Pointwise? COLM 2025）和 `jeong2025comparative`（The Comparative Trap, BlackboxNLP 2025）更直接相关。建议**降低优先级或替换**。
- **建议引用位置**: 如果保留，放 Related Work 中 LLM-as-evaluator 的早期工作综述位置。

---

## Reference 4: Stureborg et al. (2024)
- **状态**: bib 中已存在 ✓（`references.bib:403-409`）
- **完整标题**: Large Language Models are Inconsistent and Biased Evaluators
- **作者**: Rickard Stureborg, Dimitris Alikaniotis, Yoshi Suhara
- **Venue**: arXiv preprint arXiv:2405.01724
- **条目完整性**: author ✓, title ✓, year ✓, url ✓。缺 venue（仅为 arXiv preprint，未发表于正式会议）——当前写法 `journal={arXiv preprint arXiv:2405.01724}` 是标准做法，无需修改。

---

**总结**: Ref 1、2、4 均确认真实且相关。Ref 3 (Kocmi & Federmann) 真实存在但其内容偏 MT 评估，对 "LLM judge bias across evaluation formats" 的直接支撑有限——bib 中已有的 Tripathi et al. (2025) 和 Jeong et al. (2025) 更切题，建议考虑替换或仅作为早期 LLM-as-evaluator 工作引用。

Sources:
- [Simms et al. 2019 - PubMed](https://pubmed.ncbi.nlm.nih.gov/30869956/)
- [Simms et al. 2019 - ResearchGate](https://www.researchgate.net/publication/331765650_Does_the_Number_of_Response_Options_Matter_Psychometric_Perspectives_Using_Personality_Questionnaire_Data)
- [Polo et al. 2024 - ICML Proceedings](https://proceedings.mlr.press/v235/maia-polo24a.html)
- [Polo et al. 2024 - arXiv](https://arxiv.org/abs/2402.14992)
- [Kocmi & Federmann 2023 - ACL Anthology](https://aclanthology.org/2023.eamt-1.19/)
- [Kocmi & Federmann 2023 - arXiv](https://arxiv.org/abs/2302.14520)
- [Stureborg et al. 2024 - arXiv](https://arxiv.org/abs/2405.01724)

---
