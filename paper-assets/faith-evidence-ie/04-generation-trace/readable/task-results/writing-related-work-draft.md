# writing related work draft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-draft_20260516T003933_result.json`
- **Structured JSON:** [`690807efdd45de58781f.json`](../../sessions/69/690807efdd45de58781f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Related Work 初稿已写入 `artifacts/paper/sections/related_work.md`（961 词，在 800-1200 目标范围内）。

结构如下：

1. **Document-Level Relation Extraction** — 从 encoder 方法（DREEAM, EIDER, CDER, EAAGRE）到 LLM 方法（AutoRE, RelPrior, LMRC, DocKS-RAG, GLiDRE），指出无方法同时输出证据
2. **Evidence-Based Information Extraction** — DocRE 中的 evidence grounding（DREEAM, Evidence-aware DocRE, GEGA, COREX, KnowRA），以及 faithfulness-performance trade-off 的广泛文献支撑（Mind Your Step, Performance-Explanation Trade-off, Correctness≠Faithfulness），引出 "evidence generation tax" 概念
3. **Rejection Sampling and Reward-Based Fine-Tuning** — RAFT 框架、RSFT=PPO 理论联系、AdaSTaR/TrajFusion/RIFT 扩展、BoN 推理时选择及其 reward hacking 问题，连接到 FREIGE 的 CED-based RSFT + reranker 方案
4. **RL for Structured Generation** — GRPO 及其变体（DAPO, Dr. GRPO, REINFORCE++）、IE 领域应用（R1-RE, R2GRPO, E-GRPO, ReasoningNER）、QLoRA artifacts 文献（QeRL, LoRA vs FFT, Q-BLoRA），支撑 decoupling 发现和 QLoRA-as-amplifier 论点

所有引用均来自 `literature_map.yaml`，覆盖 32 个 category 中的 ~50 篇关键论文。

---
