# code related work revision

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_related-work-revision_20260514T010609_result.json`
- **Structured JSON:** [`9077920a1e9e457a058e.json`](../../sessions/90/9077920a1e9e457a058e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修订完成。变更摘要：

**1. MTRouter** — Tool-Use Learning 段末尾新增 1 句，区分"选模型 vs 选推理模态"，强调我们分析 signal composition 而非优化 cost。同时精简了原 "Our work differs" 句，去掉三轴罗列改为更紧凑的表述。

**2. EnvSimBench** — World Model Routing 段（已更名为 "World Model Routing and Environment Simulation"）新增 1 句，引入 state-change cliff，形成因果链：EnvSimBench 诊断 WHERE LLMs fail → 我们的 deterministic modality sidesteps this cliff → counterfactual 揭示这只 matters for death avoidance。

**3. LLM Agentic Failures** — 新增 Agent Failure Analysis 段，1 句话：他们定性分类 4 种 failure archetypes，我们定量隔离 dominant failure mechanism (death = 99%)。

**空间管理** — 移除 Agent Frameworks 段（ReAct 引用标注移至 Introduction），全文约 340 words，控制在 400 以内。

---
