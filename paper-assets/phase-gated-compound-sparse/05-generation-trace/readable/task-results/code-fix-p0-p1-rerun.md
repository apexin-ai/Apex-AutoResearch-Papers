# code fix p0 p1 rerun

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-p0-p1-rerun_20260513T195930_result.json`
- **Structured JSON:** [`7489fec13146dfcf3824.json`](../../sessions/74/7489fec13146dfcf3824.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 产出汇报

**P0 修复（KV eviction bug）**：
1. `_select_kv_to_evict` 签名从 `(num_layers, seq_len, ratio)` → `(seq_len, ratio)`，返回 `(seq_len,)` 单一 mask 而非 `(num_layers, seq_len)` 独立 mask。所有层共享同一 mask，BOS 永不 evict。
2. `forward_with_sparse_config` 增加 `kv_mask.dim()` 判断，兼容 1D 新格式和 2D 旧格式。
3. `compute_interaction_index` 和 `run_profiling.py` 的调用点都移除了 `num_layers` 参数。
4. `_build_kv_attention_mask` 同步更新为接受 1D/2D mask。

**效果**：ratio=0.3 时，现在稳定保留 70% token（之前只有 0.06%）。

**P1 诊断（sparsity dump）**：
1. `PhaseAnnotation` 新增 `metadata: dict` 字段。
2. `find_phase_boundaries` 和 `_retry_with_narrow_bandwidth` 通过 `_meta` dict 记录 `n_minima_found`、`fallback`、`fallback_reason`、`boundary_order`、`bandwidth`。
3. `run_profiling.py` 在 phase segmentation 后收集 per-problem diagnostics（sparsity 统计 + phase 分布 + KDE metadata），输出 JSON 新增 `diagnostics` 字段含 per-problem 数据和 50-bin 全局 sparsity histogram。

**需注意**：
- `_select_heads_to_mask` 仍是 per-layer 独立 mask，这是正确行为（不同层可以 mask 不同 head）。只有 KV eviction 需要跨层共享。
- importance-based KV eviction 现在对 2D importance tensor 取 layer 均值后选择，语义从 "每层 evict 自己最不重要的" 变为 "全局平均最不重要的"。

---
