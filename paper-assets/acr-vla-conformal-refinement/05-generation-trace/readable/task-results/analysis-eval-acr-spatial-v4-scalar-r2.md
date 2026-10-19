# analysis eval acr spatial v4 scalar r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-acr-spatial-v4-scalar-r2_20260515T131713_result.json`
- **Structured JSON:** [`fdc74177d071dde7c8b9.json`](../../sessions/fd/fdc74177d071dde7c8b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志尾部输出了完整的 JSON summary，评估正常结束（EXIT_CODE=0），无错误。

## eval-acr-spatial-v4-scalar-r2 结果（scalar_unc CRM, LIBERO spatial, T3-T9）

| Task | 描述 | 成功率 | 成功/总数 |
|------|------|--------|-----------|
| T3 | pick_up ... on the cookie box ... | **40%** | 4/10 |
| T4 | pick_up ... in the top drawer ... | **0%** | 0/10 |
| T5 | pick_up ... on the ramekin ... | **0%** | 0/10 |
| T6 | pick_up ... next to the cookie box ... | **90%** | 9/10 |
| T7 | pick_up ... on the stove ... | **0%** | 0/10 |
| T8 | pick_up ... next to the plate ... | **10%** | 1/10 |
| T9 | pick_up ... on the wooden cabinet ... | **10%** | 1/10 |

**Overall: 21.4% (15/70)**

与已知部分结果对比：T3/T4/T5/T6/T8 一致，T7 确认最终为 0%（非 running 中间值），T9 = 10%（之前缺失，现已补全）。

---
