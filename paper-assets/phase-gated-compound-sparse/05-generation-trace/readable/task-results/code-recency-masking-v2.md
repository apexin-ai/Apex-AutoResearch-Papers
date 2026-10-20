# code recency masking v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recency_masking_v2_20260516T183330_result.json`
- **Structured JSON:** [`05cd32064d49de737192.json`](../../sessions/05/05cd32064d49de737192.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

---

## 报告

### 1. 现有架构
- **argparse**: `run_profiling.py:649-650` — `--masking_method` choices 原为 `["importance", "random"]`
- **flag 解析**: `run_profiling.py:194-195` — `use_importance` / `use_recency_kv` 已存在（但 recency 未接入）
- **dense forward 分流**: `run_profiling.py:391` — importance 走 `compute_dense_forward_with_importance`，否则只算 CE loss
- **KV mask 构建**: `run_profiling.py:422` — 调 `InteractionIndexCalculator._select_kv_to_evict(seq_len, ratio, importance=...)`
- **recency 方法体**: `interaction_index.py:294` — `_select_kv_to_evict_recency` 已实现，evict position 1~n_evict（oldest），保留 BOS + recent

### 2. 修改内容（3 处）

| 行号 | 修改 |
|------|------|
| 650 | choices 增加 `"recency"` |
| 391 | dense forward 条件改为 `if use_importance or use_recency_kv:`（recency 仍需 head_importance） |
| 422-428 | KV mask 构建增加 `if use_recency_kv:` 分支，调用 `_select_kv_to_evict_recency` |

Head pruning 逻辑不变（recency 仍用 importance-based head mask）。

### 3. Dry-run 结果
- Argument parsing: `masking_method=recency` ✓
- Recency mask (seq_len=100, s=0.25): evict 25 oldest positions (1-25), keep 75 recent positions (26-99), BOS preserved ✓
- 全部 assertion 通过

### 4. Recency masking 细节
- 纯 position-based：按 index 升序 evict，**不使用任何 attention score**
- BOS (position 0) 永远保留
- Evict 的是 positions 1 ~ `int(seq_len * ratio)`（最早的 token）
- Keep 的是 positions `int(seq_len * ratio)+1` ~ `seq_len-1`（最近的 token）
- Head pruning 仍走 importance-based（需要 dense forward with attention）

---
