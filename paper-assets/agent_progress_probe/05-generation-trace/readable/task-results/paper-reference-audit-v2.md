# paper reference audit v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference-audit-v2_20260515T052646_result.json`
- **Structured JSON:** [`a6b4f9a36db3f2190f03.json`](../../sessions/a6/a6b4f9a36db3f2190f03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。

## 关键发现

**清洁度**：46 条 `\cite` key 全部在 `references.bib` 中找到，46 条 bib 条目全部被引用——**0 missing / 0 orphan**。

**OpenAlex 在线核查**：39 verified / 4 mismatch（解释见报告）/ 10 not_found（已用 WebSearch 全部手工确认为真实论文）。

**未发现幻觉引用。** 包括 8 篇 2026 年的 arXiv 预印本均可在 arXiv/OpenAlex/WebSearch 中找到对应论文。

## 修复

`references.bib` 中 `sala2019multiresolution` 作者顺序错误（原写 Sala 为第一作者）。NeurIPS 2019 proceedings 中实际第一作者为 Paroma Varma。已修正为完整作者列表，Varma 在前。

## 其他说明

- `_acl_template/custom.bib` 中有 7 条 ACL 模板自带条目（APA:83、Aho:72 等），paper 用 `\bibliography{references}` 不会加载它们，不影响编译，可在投稿前删除 `_acl_template/` 目录。
- `ratner2017snorkel` OpenAlex 报 2019，bib 写 2017——这是 VLDB Vol.11 的标准引用约定，保留。
- `jimenez2024swebench`、`george2025cycledetection` 的 first_author mismatch 是 OpenAlex 解析问题（不是 bib 错误）。

## 产出

- 审计报告：`artifacts/reference-audit/audit_report.md`
- 修复：`docs/paper/references.bib`（1 处条目）

Sources:
- [Multi-Resolution Weak Supervision for Sequential Data (NeurIPS 2019 PDF)](https://proceedings.neurips.cc/paper_files/paper/2019/file/93db85ed909c13838ff95ccfa94cebd9-Paper.pdf)
- [Monitoring LLM Agents for Sequentially Contextual Harm (OpenReview)](https://openreview.net/forum?id=LC0XQ6ufbr)
- [Kaufman et al. Leakage in Data Mining (ACM TKDD)](https://dl.acm.org/doi/10.1145/2382577.2382579)
- [Categorizing Variants of Goodhart's Law (arXiv 1803.04585)](https://arxiv.org/abs/1803.04585)
- [Why Do Multi-Agent LLM Systems Fail? (arXiv 2503.13657)](https://arxiv.org/abs/2503.13657)
- [Where LLM Agents Fail and How They Can Learn From Failures (arXiv 2509.25370)](https://arxiv.org/abs/2509.25370)
- [Reliable Weak-to-Strong Monitoring of LLM Agents (arXiv 2508.19461)](https://arxiv.org/abs/2508.19461)
- [Exploring Reasoning Reward Model for Agents (arXiv 2601.22154)](https://arxiv.org/abs/2601.22154)

---
