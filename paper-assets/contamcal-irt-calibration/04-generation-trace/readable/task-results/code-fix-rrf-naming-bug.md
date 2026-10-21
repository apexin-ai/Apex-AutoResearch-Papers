# code fix rrf naming bug

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-rrf-naming-bug_20260516T012622_result.json`
- **Structured JSON:** [`4365e3d3bc6b8b24ee47.json`](../../sessions/43/4365e3d3bc6b8b24ee47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。`rrf_aggregation.py` 做了两处改动：

1. **文件名匹配**（行 57-60）：优先尝试新格式 `signal_{sig_key}_{benchmark}.json`（如 `signal_s1_embedding_mmlu.json`），fallback 到旧格式 `signal_{sig_name}_{benchmark}.json`（如 `signal_embedding_mmlu.json`）

2. **merged 文件 + 个体文件的 schema 兼容**：
   - merged 路径：`item_id` 字段自动映射为 `index`
   - 个体文件路径：同时兼容旧格式（`index` + 信号值在 item 顶层）和新格式（`item_id` + `signal`/`score` 结构）

验证结果：所有 16 个 model×benchmark 组合（包含两种命名格式）均成功聚合。备份在 `rrf_aggregation.py.bak`。

---
