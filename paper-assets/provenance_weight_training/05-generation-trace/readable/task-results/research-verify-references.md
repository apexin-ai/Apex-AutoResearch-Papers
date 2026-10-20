# research verify references

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_references_20260523T033006_result.json`
- **Structured JSON:** [`31e3ef6951b94463246c.json`](../../sessions/31/31e3ef6951b94463246c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| # | 引用 | 存在? | 真实标题 | 作者 | Venue | 相关性 |
|---|------|-------|---------|------|-------|--------|
| 1 | Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733) | **存在** | Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining | Daouda Sow, Herbert Woisetschläger, Saikiran Bulusu, Shiqiang Wang, Hans-Arno Jacobsen, Yingbin Liang | arXiv 2025 (也在 OpenReview) | **高度相关** — 直接研究 instance-level loss-based reweighting 用于 LLM pretraining |
| 2 | Self-Influence Guided Data Reweighting (ICLR 2025) | **存在，但 venue 错误** | Self-Influence Guided Data Reweighting for Language Model Pre-training | Megh Thakkar, Tolga Bolukbasi, Sriram Ganapathy, Shikhar Vashishth, Sarath Chandar, Partha Talukdar | **EMNLP 2023**（非 ICLR 2025） | **高度相关** — 提出 PRESENCE，用 self-influence score 做 pretraining data reweighting |
| 3 | ToReMi (arXiv:2504.00695) | **存在** | ToReMi: Topic-Aware Data Reweighting for Dynamic Pre-Training Data Selection | Xiaoxuan Zhu, Zhouhong Gu, Baiqian Wu, Suhang Zheng, Tao Wang, Tianyu Li, Hongwei Feng, Yanghua Xiao | arXiv 2025 (Fudan/Alibaba) | **高度相关** — topic-level reweighting 用于 pretraining data selection |
| 4 | LLM-Generated Text Detection Survey (Wu et al. 2025) | **存在** | A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions | Junchao Wu, Shu Yang, Runzhe Zhan, Yulin Yuan, Lidia Sam Chao, Derek Fai Wong | Computational Linguistics 2025 (Vol 51, Issue 1) | **间接相关** — 关于 AI 生成文本检测（data provenance 中的来源归属），不涉及 instance-level reweighting |

**需要修正的问题：**
- **论文 2 的 venue 必须更正**：从 "ICLR 2025" 改为 "EMNLP 2023"（arXiv:2311.00913）。搜索结果中出现的 ICLR 2025 PDF 链接属于同一作者 Shiqiang Wang 的另一篇论文，不是这篇。
- **论文 4 的相关性存疑**：如果引用目的是支持 data provenance（数据来源判别），则合理；如果是支持 instance-level reweighting，则不太对口。

Sources:
- [arXiv:2502.06733](https://arxiv.org/abs/2502.06733)
- [Self-Influence Guided Data Reweighting - ACL Anthology](https://aclanthology.org/2023.emnlp-main.125/)
- [arXiv:2504.00695 ToReMi](https://arxiv.org/abs/2504.00695)
- [LLM-Generated Text Detection Survey - ACL Anthology](https://aclanthology.org/2025.cl-1.8/)

---
