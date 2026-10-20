# fix d003 device mismatch v3

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d003_device_mismatch_v3_20260512T142213_result.json`
- **Structured JSON:** [`2365562ae8b8be0e72d8.json`](../../sessions/23/2365562ae8b8be0e72d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 smoke test 通过。

**修复汇总：**

1. **`carc_kv_eviction.py`** — `update_scores` 方法 line 80: 在 `torch.cat` 前加 device 对齐，将 `self._cumulative_scores` 移到与新 `scores` 相同的 device
2. **`d003_reasoning_traces.py`** — 6 处修复：3 个 `torch.zeros` + 1 个 `torch.rand` + 1 个 `torch.arange` + 1 个 `torch.tensor` 均添加 `device=device`
3. **`d003_wikitext_32k.py`** — 同上 6 处修复

Smoke test 结果：
- Exp1 (cuda:0): PASS — update_scores device alignment + compute_eviction_mask 均正常
- Exp2 (cuda:1 mapped): PASS — 多轮 eviction cycle 也正常

---
