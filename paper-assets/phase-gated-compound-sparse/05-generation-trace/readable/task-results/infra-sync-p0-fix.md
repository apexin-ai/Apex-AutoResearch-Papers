# infra sync p0 fix

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_sync-p0-fix_20260513T202043_result.json`
- **Structured JSON:** [`1fd1e457d2bbcb8db9a2.json`](../../sessions/1f/1fd1e457d2bbcb8db9a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。汇报：

**同步状态**：8 个文件全部写入 westd-22162，同时更新了 flat 结构（`/root/autodl-tmp/pacs/profiling/`）和 package 结构（`/root/autodl-tmp/pacs/pacs/profiling/`），因为服务器存在两套目录，Python 实际加载的是 flat 结构。

**Import 验证**：3/3 通过
- `InteractionIndexCalculator` — OK
- `PhaseAnnotation` metadata 字段 — OK
- `run_profiling` — OK

**P0 KV eviction mask 修复验证**：通过
- `_select_kv_to_evict` 返回 **1D tensor `(seq_len,)`**，不再是 per-layer 2D mask
- BOS (position 0) 始终保留
- 2D importance input 正确 mean→1D

**清理**：`__pycache__` 已清除，旧 profiling_results.json 已备份为 `_m1_failed.json`。

---
