# analyze eval supp reconvla spatial s43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-reconvla-spatial-s43_20260523T111954_result.json`
- **Structured JSON:** [`4bbb315a81cd01052037.json`](../../sessions/4b/4bbb315a81cd01052037.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## eval-supp-reconvla-spatial-s43 诊断结果

**状态**: 成功完成，registry 已更新为 DONE，cron 已删除。

**Overall SR: 81.5%** (10 tasks × 20 rollouts)

| Task | SR |
|------|-----|
| table_center | 100% |
| on_cookie_box | 100% |
| next_to_cookie_box | 100% |
| between_plate_ramekin | 95% |
| next_to_ramekin | 95% |
| on_stove | 90% |
| on_wooden_cabinet | 85% |
| next_to_plate | 80% |
| top_drawer_cabinet | 70% |
| on_ramekin | 0% |

**与 s42 对比**:
- Reconvla s43: **81.5%** vs Reconvla s42: **80.0%** → 跨 seed 一致，s43 略高
- vs VLA-only baseline (s42): **78.5%** → Reconvla 持续优于 VLA-only (+3.0pp)

**Conclusion: success** — Reconvla 在 Spatial 上跨 seed 稳定优于 VLA-only baseline。on_ramekin 任务仍是硬 case（两个 seed 都为 0%）。

---
