# research rsft literature check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_rsft-literature-check_20260515T102836_result.json`
- **Structured JSON:** [`478c75b57e8142a6f3b4.json`](../../sessions/47/478c75b57e8142a6f3b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 文献对标报告

**直接竞争者：无。** 在 DocRED 文档级关系抽取上，没有找到使用 rejection sampling / self-training + NLI-based reward 的已发表工作。RSFT 在 math reasoning 领域成熟（ReST, RFT），但迁移到 IE 任务属于本项目的新贡献。

**结果定位：**
- LLM-based DocRE 近期最佳改进幅度：[RelPrior](https://arxiv.org/html/2511.08143v1)（2025）在 LLaMA3-8B 上比 AutoRE 提升 +2.06–2.38pp F1；[LMRC](https://arxiv.org/html/2408.13889v2)（2024）缩小了 LLM 与 BERT-based 方法的差距但未给出绝对提升数字
- 我们的 **+5.98pp rel_f1** 显著超过同类 LLM-based DocRE 方法的改进幅度（约 2-3x）
- Self-distillation for DocRE（[Progressive Self-distillation](https://dl.acm.org/doi/10.1145/3656168), 2024）是最接近的 self-training 思路，但用 knowledge distillation 而非 rejection sampling，且无 evidence-based reward

**CED/NLI reward 的独特性：** 文献中 NLI 用于 RE 的方式是间接监督（[NLI as Indirect Supervision](https://github.com/luka-group/NLI_as_Indirect_Supervision), ACL 2023）或事后过滤，无人将其作为 rejection sampling 的打分函数。CED 作为 reward signal 驱动数据筛选是本项目的方法论贡献点。

**结论：无直接竞争者，+5.98pp 提升在 LLM-based DocRE 改进中处于领先水平，CED-as-reward 是新颖的。**

---
