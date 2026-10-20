# verify rope bugfix

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_rope_bugfix_20260512T120327_result.json`
- **Structured JSON:** [`4a354c1a561e2a4945b0.json`](../../sessions/4a/4a354c1a561e2a4945b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证报告

### Bugfix 状态：已到位

**`carc_generate.py` — 修复确认：**
- L148: `position_counter = input_ids.shape[1]` — prefill 后初始化独立 position 计数器
- L168: `pos_ids = torch.tensor([[position_counter]], device=...)` — 每步构造 explicit position_ids
- L173: `position_ids=pos_ids` — forward call 传入 explicit position_ids
- L177: `position_counter += 1` — 自增计数器，不依赖 `cache.get_seq_length()`

关键：eviction 发生后 `position_counter` 不受影响，因为它是独立变量，与 cache 长度完全解耦。

**`sanity_check_eviction.py` — 修复确认：**
- L155-159: `compute_ppl()` 中使用 `position_ids = torch.arange(prefill_len, prefill_len + len(eval_tokens), ...)` + `position_ids=position_ids` 传入 forward call
- 即使 eviction 缩短了 cache，position_ids 仍从 `prefill_len` 开始，RoPE encoding 正确

**`carc_kv_eviction.py` — 无问题：**
- `apply_eviction()` (L165) 仅做 tensor 索引操作（`k[:, :, seq_mask, :]`），不修改 `_seen_tokens` 或任何 position 相关状态

### 文件清单

| 文件 | 大小 | 最后修改 |
|------|------|----------|
| `carc_calibrate.py` | 7010 | May 12 17:02 |
| `carc_generate.py` | 11339 | May 12 19:54 |
| `carc_kv_eviction.py` | 9165 | May 12 19:54 |
| `carc_mvp.py` | 28682 | May 12 17:04 |
| `carc_utils.py` | 15704 | May 12 19:37 |
| `eval_kv_eviction.py` | 20509 | May 12 19:54 |
| `merge_results.py` | 12903 | May 12 18:59 |
| `sanity_check_eviction.py` | 11133 | May 12 19:44 |

### 问题

无。修复干净且一致，三个相关文件都已正确使用 explicit position tracking。

---
