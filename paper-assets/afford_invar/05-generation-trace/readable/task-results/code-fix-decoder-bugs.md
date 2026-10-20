# code fix decoder bugs

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-decoder-bugs_20260519T204639_result.json`
- **Structured JSON:** [`9fae8d35753856c735c5.json`](../../sessions/9f/9fae8d35753856c735c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Line 353: `text_hs = last_hs[:, NUM_PATCHES:-1]` — 这行已经正确。image tokens 在 `0:NUM_PATCHES`，text tokens 从 `NUM_PATCHES` 开始，与修复后的 affordance feature 提取一致。

## 修复总结

**文件**: `/root/afford_invar/openvla-oft/vla-scripts/finetune_afford.py`（bug 实际在这里，不在 `affordance_decoder.py`）

**Bug 1 — hidden_states off-by-one** (lines 363, 384):
```diff
- output.hidden_states[cfg.layer_idx][:, ...]
+ output.hidden_states[cfg.layer_idx + 1][:, ...]

- p_out.hidden_states[cfg.layer_idx][:, ...]
+ p_out.hidden_states[cfg.layer_idx + 1][:, ...]
```
`hidden_states[0]` = embedding output，所以 `layer_idx=18` 对应 `hidden_states[19]`。

**Bug 2 — token 布局** (lines 363, 384):
```diff
- [:, 1:1 + NUM_PATCHES, :]   # 错误：跳过 pos 0，混入 BOS
+ [:, 0:NUM_PATCHES, :]        # 正确：image tokens 从 pos 0 开始
```
实际布局是 `[image(256)] [BOS + text...]`，不是 `[BOS] [image(256)] [text...]`。

**Unit test**: 3 项全部通过（hidden_states 索引、token 布局、decoder forward）。

---
