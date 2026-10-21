# ops extract k03 results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_k03_results_20260518T102220_result.json`
- **Structured JSON:** [`5b4b17b06814abe8584c.json`](../../sessions/5b/5b4b17b06814abe8584c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被之前清理）。Registry 已更新为 DONE/success。

## eval_openvla_pruning_k03_restart 结果

| 指标 | 值 |
|---|---|
| **Overall SR** | **20.6% (103/500)** |
| Wilson 95% CI | [17.3%, 24.4%] |
| 耗时 | 288.6 min |

### Per-task SR

| Task | SR |
|---|---|
| salad_dressing | 64% |
| orange_juice | 42% |
| bbq_sauce | 30% |
| ketchup | 30% |
| alphabet_soup | 14% |
| chocolate_pudding | 10% |
| tomato_sauce | 8% |
| milk | 8% |
| cream_cheese | 0% |
| butter | 0% |

### Degradation curve 更新（OpenVLA random pruning, libero_object）

| k (keep ratio) | Tokens kept | SR |
|---|---|---|
| 1.0 (baseline) | 256 | ~96% |
| 0.7 | 179 | 待查 |
| 0.5 | 128 | 待查 |
| **0.3** | **76** | **20.6%** |

k=0.3 的实际 SR (20.6%) 低于之前估计的 ~26%，与 partial results 暗示的 ~19% 接近。保留仅 30% 的 vision tokens 导致性能从 baseline 的 ~96% 剧烈下降至 ~21%，确认 70% 的 token 被随机丢弃后模型几乎不可用。

---
