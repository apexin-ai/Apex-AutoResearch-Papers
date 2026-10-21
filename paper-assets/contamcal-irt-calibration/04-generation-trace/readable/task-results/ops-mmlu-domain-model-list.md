# ops mmlu domain model list

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mmlu_domain_model_list_20260517T061550_result.json`
- **Structured JSON:** [`cc0a122bf66b352f836c.json`](../../sessions/cc/cc0a122bf66b352f836c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 21 模型列表：

| # | Model | Scale | Dosage | Seed |
|---|-------|-------|--------|------|
| 1 | Qwen2.5-0.5B_d000_s123_aligned | 0.5B | d000 | s123 |
| 2 | Qwen2.5-0.5B_d000_s42_aligned | 0.5B | d000 | s42 |
| 3 | Qwen2.5-0.5B_d005_s123_aligned | 0.5B | d005 | s123 |
| 4 | Qwen2.5-0.5B_d005_s42_aligned | 0.5B | d005 | s42 |
| 5 | Qwen2.5-0.5B_d025_s123_aligned | 0.5B | d025 | s123 |
| 6 | Qwen2.5-0.5B_d025_s42_aligned | 0.5B | d025 | s42 |
| 7 | Qwen2.5-0.5B_d100_s123_aligned | 0.5B | d100 | s123 |
| 8 | Qwen2.5-0.5B_d100_s42_aligned | 0.5B | d100 | s42 |
| 9 | Qwen2.5-1.5B_d000_s123_aligned | 1.5B | d000 | s123 |
| 10 | Qwen2.5-1.5B_d000_s42_aligned | 1.5B | d000 | s42 |
| 11 | Qwen2.5-1.5B_d005_s123_aligned | 1.5B | d005 | s123 |
| 12 | Qwen2.5-1.5B_d005_s42_aligned | 1.5B | d005 | s42 |
| 13 | Qwen2.5-1.5B_d025_s123_aligned | 1.5B | d025 | s123 |
| 14 | Qwen2.5-1.5B_d025_s42_aligned | 1.5B | d025 | s42 |
| 15 | Qwen2.5-1.5B_d100_s123_aligned | 1.5B | d100 | s123 |
| 16 | Qwen2.5-1.5B_d100_s42_aligned | 1.5B | d100 | s42 |
| 17 | Qwen2.5-3B_d005_s123_aligned | 3B | d005 | s123 |
| 18 | Qwen2.5-3B_d025_s123_aligned | 3B | d025 | s123 |
| 19 | Qwen2.5-3B_d025_v3_s42_aligned | 3B | d025 | s42 |
| 20 | Qwen2.5-3B_d100_a32_s123_aligned | 3B | d100 | s123 |
| 21 | Qwen2.5-3B_d100_a32_s42_aligned | 3B | d100 | s42 |

**统计：**

| 维度 | 分布 |
|------|------|
| **Scale** | 0.5B: 8, 1.5B: 8, 3B: 5 |
| **Seed** | s42: 10, s123: 11 |
| **Dosage** | d000: 4, d005: 5, d025: 5, d100: 7 |
| **_aligned 后缀** | 全部 21 个都有 `_aligned`（`aligned_only=True`）|
| **alpha 变体 (a32)** | 2 个：`Qwen2.5-3B_d100_a32_s123_aligned`、`Qwen2.5-3B_d100_a32_s42_aligned` |

**注意：3B 缺失 d000 模型**（没有 `Qwen2.5-3B_d000_*_aligned` 通过 RRF 过滤），所以 3B 只有 5 个而非 8 个。

---
