# research phase b prereq

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_phase-b-prereq_20260515T232930_result.json`
- **Structured JSON:** [`c372d9d12e875d6d18df.json`](../../sessions/c3/c372d9d12e875d6d18df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已保存到 `artifacts/phase_b_prereq_analysis.md`。

核心结论：

**前置 1（`&lt;VERIFY>` token）**：Qwen3-1.7B 的 embedding 层有 151936 slot，tokenizer 只用了 151669，添加 `&lt;VERIFY>` 后为 151670 — **不需要 resize_token_embeddings**。只需一个离线脚本扩展 tokenizer 并保存到新目录，改 config 的 model_path 即可，所有组件（FSDP actor/ref、vLLM rollout）自动对齐。工作量 1-2h。

**前置 2（a_pre 开销量化）**：核心度量用 token 数而非 latency。在 `BIAVRTracker` 中增加 a_pre token 统计，配合一个基线量化脚本从 Phase A rollout 数据计算 always-on 开销。工作量 2-3h，依赖 Phase A 产出 rollout 数据。

**总预估 4-6 Worker-hours，两个前置条件可与 Phase A 并行推进。**

---
