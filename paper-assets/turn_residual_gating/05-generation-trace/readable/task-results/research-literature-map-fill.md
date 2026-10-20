# research literature map fill

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_map_fill_20260522T045024_result.json`
- **Structured JSON:** [`a2b942296e2d497b0ec2.json`](../../sessions/a2/a2b942296e2d497b0ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 papers added successfully. Here's the summary:

---

**添加了 5 篇论文，覆盖 4 个方向：**

| # | 论文 | 方向 | Role | 关联 |
|---|------|------|------|------|
| 1 | Wiseman & Rush 2016, "Sequence-to-Sequence Learning as Beam-Search Optimization" (EMNLP) | a. Exposure bias | foundation | paper_framing SP1 明确引用为 exposure bias 量化先例 |
| 2 | Zhang et al. 2019, "Bridging the Gap between Training and Inference for NMT" (ACL) | d. Scheduled sampling | method-component | 训练时混合 model-generated tokens，对应 W8 讨论的 mitigation 方向 |
| 3 | Arora et al. 2022, "Why Exposure Bias Matters" (ACL Findings) | a. Exposure bias | theoretical-foundation | 用 imitation learning 证明 exposure bias → compounding errors 且 PPL 无法捕捉——直接支撑 30x gap 论证 |
| 4 | Mihaylova & Martins 2019, "Scheduled Sampling for Transformers" (ACL SRW) | d. Scheduled sampling | method-component | 将 scheduled sampling 扩展到 transformer，相关于 Discussion 中的 mitigation 未来方向 |
| 5 | Li et al. 2024, "Measuring and Controlling Instruction (In)Stability in Language Model Dialogs" (COLM) | b/c. GAR + Multi-turn attention | direct-competitor | 同一问题（attention 到 system prompt 随轮次衰减），识别 attention decay 机制，提出 split-softmax 推理时修复 |

同时已将 5 篇的 bib entries 添加到 `paper/references.bib`。

---
