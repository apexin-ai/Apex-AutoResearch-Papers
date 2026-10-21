# analysis eval mag obsonly norm03 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-obsonly-norm03-r2_20260515T172216_result.json`
- **Structured JSON:** [`9f9a18bc21956143ce90.json`](../../sessions/9f/9f9a18bc21956143ce90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

**eval-mag-obsonly-norm03-r2** — obs_only CRM v3-norm, norm=0.3, spatial benchmark

| Task | SR |
|---|---|
| bowl_between | 90% |
| next_to_ramekin | 100% |
| table_center | 0% |
| cookie_box | 30% |
| top_drawer | 10% |
| on_ramekin | 0% |
| next_to_cookie_box | 100% |
| stove | 0% |
| next_to_plate | 30% |
| wooden_cabinet | 0% |
| **Overall** | **36%** |

**Conclusion: SUCCESS**

obs_only 在 norm=0.3 下得到 36%，与 norm=0.05/0.1/0.2 的 35% 基本一致，没有崩塌。而 perdof 在同一 norm=0.3 下崩塌到 26%。这证实了 obs_only 对高 correction norm 的鲁棒性——perdof 依赖的 per-DoF 分量在大 norm 下产生不稳定修正，obs_only 的标量修正则保持稳定。

Registry 已更新为 DONE/success。

---
