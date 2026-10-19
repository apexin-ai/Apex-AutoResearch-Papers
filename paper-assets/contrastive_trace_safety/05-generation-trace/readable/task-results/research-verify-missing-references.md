# research verify missing references

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_missing_references_20260522T231144_result.json`
- **Structured JSON:** [`02258f8aedd649f10b86.json`](../../sessions/02/02258f8aedd649f10b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部搜索完成，以下是逐篇验证结果。

---

**论文 1: Berk, Brown, Buja, Zhang, & Zhao (2013)**
- **(a) 存在性:** 是
- **(b) 正确引用格式:** Berk, R., Brown, L., Buja, A., Zhang, K., & Zhao, L. (2013). Valid post-selection inference. *Annals of Statistics*, 41(2), 802–837. DOI: 10.1214/12-AOS1077
- **(c) 与 CoT safety probing 的相关性:** 中 — 提供 post-selection inference 的理论基础，我们的 CR-composite 做了 metric-driven layer selection 后再报告性能，存在 selection bias 的统计隐患，此文提供 PoSI 框架的理论锚点
- **(d) 建议引用方式:** 简短提及 — 在讨论 layer selection 引入的 post-selection bias 时作为经典统计参考，无需详细展开方法
- **注意:** 末位作者是 Zhao, **L.**(Linda Zhao)，非 "Zhao, I."，引用时需修正

---

**论文 2: Lee, Sun, Sun, & Taylor (2016)**
- **(a) 存在性:** 是
- **(b) 正确引用格式:** Lee, J. D., Sun, D. L., Sun, Y., & Taylor, J. E. (2016). Exact post-selection inference, with application to the lasso. *Annals of Statistics*, 44(3), 907–927. DOI: 10.1214/15-AOS1371
- **(c) 与 CoT safety probing 的相关性:** 中 — 与论文 1 互补，给出 exact (conditional) post-selection inference，比 Berk 的 universal PoSI 更紧；若我们在 discussion 中讨论 layer selection 后的推断有效性，两篇一起引用可构成完整的统计背景
- **(d) 建议引用方式:** 简短提及 — 与 Berk 2013 并列引用即可，一句话带过
- **注意:** 声称标题缺少副标题 "with application to the lasso"，引用时需补全

---

**论文 3: CLAP (Cross-Layer Attention Probing) — arXiv 2509.09700**
- **(a) 存在性:** 是
- **(b) 正确引用格式:** Suresh, M., Aljundi, R., Nkisi-Orji, I., & Wiratunga, N. (2025). Cross-layer attention probing for fine-grained hallucination detection. *arXiv preprint arXiv:2509.09700*.
- **(c) 与 CoT safety probing 的相关性:** 高 — CLAP 将全部层的 activations 作为 joint sequence 做 cross-layer attention aggregation，直接解决了 "选哪一层" 的问题。但它面向的是 **response-level** hallucination detection（区分同一 prompt 下不同 sampled response 的幻觉/非幻觉），不是 step-level reasoning trace。对 variable-length CoT traces，CLAP 的 token×layer joint sequence 长度会随 CoT 步数线性增长，直接迁移需要解决 scalability 问题。
- **(d) 建议引用方式:** 详细讨论 — 在 Related Work 的 layer aggregation 部分作为关键对比方法，指出它的 cross-layer aggregation 思路与我们 metric-driven layer selection 的 divergence 问题直接相关，但不处理 variable-length CoT 的 step-level 结构，这正是我们工作的差异化定位

---

**论文 4: BERTology Aggregator — arXiv 2601.13288**
- **(a) 存在性:** 是
- **(b) 正确引用格式:** Meyoyan, G. A. & Del Corro, L. (2026). A BERTology view of LLM orchestrations: Token- and layer-selective probes for efficient single-pass classification. *arXiv preprint arXiv:2601.13288*.
- **(c) 与 CoT safety probing 的相关性:** 高 — 直接处理 production LLM 中 safety classification 的 layer/token selection 问题，提出 two-stage aggregator（先 within-layer token pooling，再 cross-layer aggregation），发现 safety-relevant features 分布在多层而非集中在某一深度——这和我们观察到的 metric 选择不同层的现象高度吻合
- **(d) 建议引用方式:** 详细讨论 — 作为 Related Work 中最直接的对比工作。他们用 learned aggregation 绕过 layer selection，我们则从 metric divergence 角度揭示为什么 fixed single-layer readout 有系统性偏差

---

**论文 5: "Detecting LLM Hallucination Through Layer-wise Information Deficiency"**
- **(a) 存在性:** 是
- **(b) 正确引用格式:** Kim, H., Lamb, T. A., Bibi, A., Torr, P., & Gal, Y. (2025). Detecting LLM hallucination through layer-wise information deficiency: Analysis of ambiguous prompts and unanswerable questions. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, pages 1644. ACL. (arXiv:2412.10246)
- **(c) 与 CoT safety probing 的相关性:** 中 — 研究 layer-wise information flow 与 hallucination 的关系，发现幻觉表现为 inter-layer information deficiency。与我们工作的交集在于都分析了不同层的行为差异，但它关注的是 hallucination detection 而非 safety refusal，且不涉及 metric selection bias
- **(d) 建议引用方式:** 简短提及 — 在 Related Work 中作为 "layer-wise analysis for LLM reliability" 的代表工作之一，一句话说明它从 information flow 角度验证了层间行为差异的存在

---

**汇总:**

| # | 存在 | 引用需修正 | 相关性 | 建议 |
|---|------|-----------|--------|------|
| 1 | ✓ | 末位作者 Zhao,L (非I) | 中 | 简短提及 |
| 2 | ✓ | 补副标题 "with application to the lasso" | 中 | 简短提及 |
| 3 | ✓ | 标题是 hallucination detection, 非 safety | 高 | 详细讨论 |
| 4 | ✓ | 无误 | 高 | 详细讨论 |
| 5 | ✓ | 无误 | 中 | 简短提及 |

5 篇全部真实存在，无虚构引用。论文 3 (CLAP) 和论文 4 (BERTology aggregator) 与我们的 layer selection bias 工作最直接相关，建议在 Related Work 中重点讨论。

Sources:
- [Berk et al. 2013 - Project Euclid](https://projecteuclid.org/journals/annals-of-statistics/volume-41/issue-2/Valid-post-selection-inference/10.1214/12-AOS1077.full)
- [Lee et al. 2016 - Project Euclid](https://projecteuclid.org/journals/annals-of-statistics/volume-44/issue-3/Exact-post-selection-inference-with-application-to-the-lasso/10.1214/15-AOS1371.full)
- [CLAP - arXiv 2509.09700](https://arxiv.org/abs/2509.09700)
- [BERTology Aggregator - arXiv 2601.13288](https://arxiv.org/abs/2601.13288)
- [Kim et al. 2025 - ACL Anthology](https://aclanthology.org/2025.emnlp-main.1644/)

---
