# ops rrf dry run verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rrf-dry-run-verify_20260516T032257_result.json`
- **Structured JSON:** [`b75d1a91ce975b8bce86.json`](../../sessions/b7/b75d1a91ce975b8bce86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## RRF 聚合 Dry-Run 结果

过滤逻辑确认（L233）：`SKIP_PATTERNS` 用子串匹配，`ALPHA16_BLOCKLIST` 用精确匹配（set membership）。

### INCLUDE — 13 个目录（全部 alpha=32 有效）

| 目录 | 模型 | dosage | seed |
|------|------|--------|------|
| Qwen2.5-0.5B_d000_s42 | 0.5B | d000 | s42 |
| Qwen2.5-0.5B_d000_s123 | 0.5B | d000 | s123 |
| Qwen2.5-0.5B_d005_s42 | 0.5B | d005 | s42 |
| Qwen2.5-0.5B_d025_s42 | 0.5B | d025 | s42 |
| Qwen2.5-0.5B_d100_s42 | 0.5B | d100 | s42 |
| Qwen2.5-1.5B_d000_s42 | 1.5B | d000 | s42 |
| Qwen2.5-1.5B_d005_s42 | 1.5B | d005 | s42 |
| Qwen2.5-1.5B_d025_s42 | 1.5B | d025 | s42 |
| Qwen2.5-1.5B_d100_s42 | 1.5B | d100 | s42 |
| Qwen2.5-3B_d005_s123 | 3B | d005 | s123 |
| Qwen2.5-3B_d025_s123 | 3B | d025 | s123 |
| Qwen2.5-3B_d025_v3_s42 | 3B | d025 | s42 |
| Qwen2.5-3B_d100_a32_s123 | 3B | d100 | s123 |

### SKIP — 5 个目录

| 目录 | 原因 |
|------|------|
| Qwen2.5-3B_d000_v2_s42 | ALPHA16_BLOCKLIST |
| Qwen2.5-3B_d005_s42 | ALPHA16_BLOCKLIST |
| Qwen2.5-3B_d025_s42 | ALPHA16_BLOCKLIST |
| Qwen2.5-3B_d100_s42 | ALPHA16_BLOCKLIST |
| Qwen2.5-3B_d025_s42_DEPRECATED_alpha16 | DEPRECATED 子串匹配 |

注：blocklist 中的 `Qwen2.5-3B_d000_s42` 在 signals 目录中不存在（该目录可能已被删除），属于无害冗余条目。

### 误判检查

**无误判。** 所有 alpha=16 的 3B 目录均被正确 SKIP；0.5B/1.5B 全量 INCLUDE；3B 有效目录（v3、a32、s123）均 INCLUDE。精确匹配逻辑工作正常，不会误伤含 `_v3`/`_a32` 后缀的有效目录。

---
