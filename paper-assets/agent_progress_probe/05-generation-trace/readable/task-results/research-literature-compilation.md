# research literature compilation

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-compilation_20260514T183143_result.json`
- **Structured JSON:** [`02b163f869c80b38c329.json`](../../sessions/02/02b163f869c80b38c329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已就绪。完成总结：

**literature_map.yaml 已创建**，包含 **30 篇论文**，覆盖 5 个类别：

| 类别 | 数量 | 关键论文 |
|------|------|----------|
| direct-competitor | 6 | AgentPRM, PRM framework, ToolPRMBench, Plan-RewardBench, monitoring harm, weak-to-strong |
| method-component | 9 | Data Programming, Snorkel, FlyingSquid, WRENCH, Dawid-Skene, HMM-Crowd, Linked HMM, Multi-resolution WS |
| evaluation | 4 | SlopCodeBench, SWE-bench, SWE-agent, OpenHands |
| background | 8 | Reflexion, LATS, ToT, 3 篇 failure taxonomy, 2 篇 cycle detection |
| technique | 4 | GRU, Attention, SupCon, Qwen3-Embedding |

**Novelty 检查结论**：Temporal Label Model 作为 general-purpose data programming extension for sequential data **是 novel 的**。最近前驱：
- Safranchik AAAI 2020：linked HMM，但限于 NER/BIO tagging
- Sala NeurIPS 2019：multi-resolution WS，不建模 label transitions
- Nguyen ACL 2017：HMM-Crowd，crowdsourcing 而非 programmatic LFs

没有人将 data programming + HMM-style temporal transitions 用于通用序列分类或 agent monitoring。

**需注意**：AgentPRM 第一作者是 **Xi**（席）不是 Xie（谢）。Monitoring harm 论文无 arxiv ID（workshop-only, OpenReview: LC0XQ6ufbr）。

---
