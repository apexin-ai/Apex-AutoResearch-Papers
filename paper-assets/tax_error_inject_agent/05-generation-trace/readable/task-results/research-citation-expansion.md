# research citation expansion

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-expansion_20260515T032405_result.json`
- **Structured JSON:** [`7115bd993d4b66ccf036.json`](../../sessions/71/7115bd993d4b66ccf036.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

写入完成。结果：

**20 篇核心引用**，全部经 WebSearch 验证，分布在 5 个 cluster：
- Error injection for agents: 6 篇（含新增 AgentHER）
- Training instability: 3 篇
- Data mixing & noise: 4 篇
- ALFWorld methods: 5 篇（含新增 CoEx、AgentPRM）
- Training dynamics: 2 篇（+ Longpre 作为备选第 21 篇）

**新增 3 篇**：AgentHER (arXiv 2603.21357)、CoEx (EMNLP 2025 Findings)、AgentPRM (arXiv 2502.10325)

**已有引用纠正**：
- Mosbach et al. 是 ICLR 2021，不是 EMNLP
- D'Amour et al. 是 JMLR 2022，不是 NeurIPS
- CoEx 作者是 Kim & Hwang，不是 writing_plan 里写的 "Zhang et al."
- AgentPRM 有两篇同名论文，我们引的是 Choudhury (2502.10325)，不是 Xiong et al. (2511.08325)

产出文件：`artifacts/citation_expansion.md`

---
