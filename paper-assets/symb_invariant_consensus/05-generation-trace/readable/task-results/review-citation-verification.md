# review citation verification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_citation-verification_20260519T054740_result.json`
- **Structured JSON:** [`1d9796d84dbd99185ea6.json`](../../sessions/1d/1d9796d84dbd99185ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇总结果：

---

## 验证结果

### 1. `diverseaware2026` — ⚠️ 存在但会议接收状态存疑

- **标题**: "Diversity-Aware Training for Test-Time Scaling" ✅ 匹配
- **作者**: Lyu, Bohan 等 10 人 ✅ 匹配
- **Bib 声称**: `booktitle={ICLR}, year={2026}`
- **实际状态**: 论文在 [OpenReview](https://openreview.net/forum?id=UVL10ozjtl) 提交，PDF 头部仍为 **"Under review as a conference paper at ICLR 2026"**。无法在 iclr.cc 虚拟会议页面找到对应 poster。**无法确认已被 ICLR 2026 接收。**
- **建议**: 将 bib 条目改为 arXiv preprint 格式（需查找对应 arXiv ID），或改为 `@inproceedings{..., note={Under review}}`，避免误标为已发表。

### 2. `kim2026reasc` — ✅ 确认存在且信息准确

- **标题**: "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning" ✅ 匹配
- **作者**: Kim, Junseok; Yang, Nakyeong; Min, Kyungmin; Jung, Kyomin ✅ 匹配
- **arXiv ID**: [2601.02970](https://arxiv.org/abs/2601.02970) ✅ 匹配
- **发表日期**: 2026年1月6日 ✅
- **结论**: 信息完全准确，无需修改。

### 3. `xu2026dylos` — ✅ 确认存在且信息准确

- **标题**: "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (DyLoS)" ✅ 匹配
- **作者**: Xu, Lei; Beckmann, Pierre; Valentino, Marco; Freitas, Andre ✅ 匹配
- **会议**: EACL 2026 ✅ — 已在 [ACL Anthology](https://aclanthology.org/2026.eacl-long.54/) 收录
- **结论**: 信息完全准确，无需修改。

---

**总结**: 3 篇中 2 篇完全确认，1 篇（`diverseaware2026`）论文真实存在但 ICLR 2026 接收状态不明确，bib 中 `booktitle={ICLR}` 可能不准确，建议核实或改为 preprint 引用。

---
