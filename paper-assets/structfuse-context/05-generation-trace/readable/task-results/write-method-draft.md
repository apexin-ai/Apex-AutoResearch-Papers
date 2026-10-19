# write method draft

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_method-draft_20260514T224613_result.json`
- **Structured JSON:** [`627939004545f49cf381.json`](../../sessions/62/627939004545f49cf381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_drafts/method_v1.md` 并注册。

四个 subsection 覆盖内容：

- **§3.1 Problem Formulation** — repo-level retrieval 形式化定义，contrastive learning 框架
- **§3.2 StructFuse Pipeline** — CodeQL inter-procedural data-flow extraction → file-level structural graph → drift-immune 设计
- **§3.3 Training Objective** — InfoNCE 公式（τ=0.07 learnable），LoRA 配置（r=16, α=32, q_proj/v_proj），AdamW lr=2e-5，dual checkpoint 策略
- **§3.4 Negative Mining Strategies** — random / embedding-distance / dataflow-aware 三策略定义与公式，含 difficulty gradient 讨论和 34% fallback 说明

引用与 `literature_map.yaml` 对齐（SimCLR、DPR、ANCE、FAISS、CodeQL、Qwen2.5-Coder、StarCoder 等）。约 1200 词。

---
