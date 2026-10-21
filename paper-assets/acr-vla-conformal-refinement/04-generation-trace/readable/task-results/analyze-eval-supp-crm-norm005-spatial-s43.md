# analyze eval supp crm norm005 spatial s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-crm-norm005-spatial-s43_20260523T083401_result.json`
- **Structured JSON:** [`5032fcb4f24dde2fe71a.json`](../../sessions/50/5032fcb4f24dde2fe71a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 总结

**eval-supp-crm-norm005-spatial-s43** — CRM obs_only, norm=0.05, Spatial, seed=43

| Task | SR | 详情 |
|------|-----|------|
| between_plate_and_ramekin | 100% | 20/20 |
| next_to_ramekin | 95% | 19/20 |
| from_table_center | 95% | 19/20 |
| on_cookie_box | 100% | 20/20 |
| in_top_drawer_wooden_cabinet | 75% | 15/20 |
| on_ramekin | 0% | 0/20 |
| next_to_cookie_box | 95% | 19/20 |
| on_stove | 85% | 17/20 |
| next_to_plate | 70% | 14/20 |
| on_wooden_cabinet | 95% | 19/20 |
| **Overall** | **81.0%** | **162/200** |

**与 seed42 对比**：seed42 = 80.0%, seed43 = 81.0%, **+1.0pp**。两个 seed 均高于 VLA-only baseline (78.5%)，cross-seed 一致性良好。

**结论**：**success** — SR 81.0% > VLA-only baseline 78.5%，已标记 DONE。

---
