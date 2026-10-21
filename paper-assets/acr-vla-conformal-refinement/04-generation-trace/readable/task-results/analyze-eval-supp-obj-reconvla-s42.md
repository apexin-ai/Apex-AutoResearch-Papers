# analyze eval supp obj reconvla s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-obj-reconvla-s42_20260523T065844_result.json`
- **Structured JSON:** [`cdd69da925aa614041c2.json`](../../sessions/cd/cdd69da925aa614041c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。结果汇总：

**eval-supp-obj-reconvla-s42 — Overall SR: 79.0% (158/200)**

| Task | SR |
|------|----|
| bbq_sauce | 95.0% |
| ketchup | 90.0% |
| orange_juice | 90.0% |
| salad_dressing | 85.0% |
| tomato_sauce | 80.0% |
| alphabet_soup | 75.0% |
| chocolate_pudding | 75.0% |
| cream_cheese | 70.0% |
| butter | 65.0% |
| milk | 65.0% |

Object Reconvla K=10 的 79.0% 与 Spatial Reconvla K=10 的 79.0% 完全一致，验证了 CRM-based refinement 跨 suite 的泛化性。Conclusion 已从 cron 误判的 `failed` 修正为 `success`，status 设为 `DONE`。

---
