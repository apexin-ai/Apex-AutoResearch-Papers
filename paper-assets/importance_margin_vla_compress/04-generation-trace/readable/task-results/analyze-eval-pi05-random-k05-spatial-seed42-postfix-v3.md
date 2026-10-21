# analyze eval pi05 random k05 spatial seed42 postfix v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_spatial_seed42_postfix_v3_20260524T044353_result.json`
- **Structured JSON:** [`17f0310d3ab4d430244f.json`](../../sessions/17/17f0310d3ab4d430244f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已推进到 DONE。

**实验结果：π0.5 Random k=0.5 Spatial seed42 (post-fix v3)**

| 指标 | 值 |
|---|---|
| Overall SR | **71.8%** (359/500) |
| 耗时 | 139.2 min |

**Per-task SR:** 88%, 88%, 88%, 48%, 40%, 32%, 92%, 86%, 84%, 72%

**关键发现：** Random pruning 50% 在 π0.5 Spatial 上表现与 Attention pruning 几乎无差异（71.8% vs 72.6%, -0.8pp），远超 L2norm（58.2%, +13.6pp）。这与 X-VLA 上的 Random k=0.5 Spatial (71.4%) 高度一致，说明 Spatial suite 对 random token removal 有较强鲁棒性，L2norm 作为 importance metric 在此场景下反而有害。

---
