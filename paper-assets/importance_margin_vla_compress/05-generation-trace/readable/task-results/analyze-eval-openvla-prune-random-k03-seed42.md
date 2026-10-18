# analyze eval openvla prune random k03 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_prune_random_k03_seed42_20260525T123217_result.json`
- **Structured JSON:** [`20b6a885ee15337d036c.json`](../../sessions/20/20b6a885ee15337d036c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果：eval_openvla_prune_random_k03_seed42

| 指标 | 值 |
|------|-----|
| **Overall SR** | **20.6% (103/500)** |
| Mode | random_prune, k=0.3 (256→76 tokens) |
| Seed | 42 |
| 耗时 | 374.6 min |

### Per-task 成绩

| Task | SR | Successes |
|------|-----|-----------|
| alphabet soup | 26.0% | 13/50 |
| cream cheese | 2.0% | 1/50 |
| salad dressing | 48.0% | 24/50 |
| bbq sauce | 26.0% | 13/50 |
| ketchup | 32.0% | 16/50 |
| tomato sauce | 0.0% | 0/50 |
| butter | 0.0% | 0/50 |
| milk | 10.0% | 5/50 |
| chocolate pudding | 4.0% | 2/50 |
| orange juice | 58.0% | 29/50 |

### 结论

**Success** — seed42 = 20.6%，与 seed7 = 20.6% 完全一致。Random pruning 在 70% 剪枝率下跨 seed 高度稳定，MF-3 验证通过。

---
