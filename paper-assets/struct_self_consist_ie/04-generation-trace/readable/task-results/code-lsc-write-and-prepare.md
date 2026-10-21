# code lsc write and prepare

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lsc_write_and_prepare_20260520T162619_result.json`
- **Structured JSON:** [`580e8c7bd5b54a8690ae.json`](../../sessions/58/580e8c7bd5b54a8690ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。

`run_lsc.py` 已写入 `artifacts/experiments/lsc/run_lsc.py`。

**核心设计**:
- **Forward pass**: 对每个 sample 的 `[chat_template(prompt) + reconstructed_JSON_output]` 做 forward pass，提取指定层 hidden states
- **Entity span 定位**: 双策略 — 优先用 `offset_mapping` 做 char→token 映射，fallback 用 token subsequence matching（含 leading space 变体）
- **输出重建**: 因 JSONL 不存 raw_output，从 parsed entities/relations/events 重建 JSON 字符串
- **Prompt 复用**: 内置 `_TRAIN_ALIGNED_TEMPLATE` 和 `_NER_TEMPLATE`，通过 `--use_train_format` / `--no_train_format` + `--schema_hint` 匹配推理时的 prompt

**三种聚合方法**:
- **A) Centroid Selection** — sample 级 entity centroid → 选 cosine 距离最近 grand centroid 的 sample
- **B) Latent Confidence** — 收集同一 entity 跨 sample 的 hidden vectors，计算 mean pairwise cosine similarity 作为 latent agreement，乘以 frequency 后 threshold 做 weighted construction
- **C) Clustering** — k-means(k=2) 在 instance 级 entity vectors 上，检测 cluster-correctness separation

**显存管理**: 逐 instance 处理，batch 内即时释放 `model_outputs` 和 `hidden_states`，右侧 padding 简化位置计算。

---
