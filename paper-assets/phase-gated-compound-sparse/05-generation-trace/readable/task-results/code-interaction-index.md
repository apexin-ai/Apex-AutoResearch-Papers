# code interaction index

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_interaction_index_20260513T174549_result.json`
- **Structured JSON:** [`96bb3a98e00d8428de65.json`](../../sessions/96/96bb3a98e00d8428de65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建并注册：

**`pacs/profiling/interaction_index.py`**
- `InteractionResult` 数据类，包含 4 种配置的 ppl 和 II 值
- `InteractionIndexCalculator`：通过 forward hook 实现 head masking（兼容 GQA），通过 attention mask 实现 KV eviction
- `compute_interaction_index()` — 单次 II 计算（4 次 forward pass）
- `compute_per_phase_ii()` — 按 phase 分别计算 II
- Head/KV 选择支持 importance-based 和 random 两种策略，BOS token 不会被 evict

**`pacs/utils/metrics.py`**
- `compute_perplexity()` — 支持 token_indices 过滤和 -100 label 忽略
- `compute_accuracy()` — exact match

包结构：`pacs/__init__.py`, `pacs/profiling/__init__.py`, `pacs/utils/__init__.py` 均已创建。`phase_segmentation.Phase` 用 try-import 延迟依赖，等该模块就绪后自动接入。

---
