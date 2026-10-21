# diag plan a spatial seed43 fail

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_plan-a-spatial-seed43-fail_20260521T000354_result.json`
- **Structured JSON:** [`a48311e72215a6cd2585.json`](../../sessions/a4/a48311e72215a6cd2585.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：seed42/43 没有失败，是监控误报。** 三个 seed 全部正常完成，结果文件完整有效：

| seed | 成功率 | 状态 |
|------|--------|------|
| 42 | 34.0% | 完成，JSON 存在 |
| 43 | 35.0% | 完成，JSON 存在 |
| 44 | 36.0% | 完成，JSON 存在 |

日志无任何 error/OOM/crash，三个 seed 的 conformal CRM 统计指标高度一致（mean_unc ~0.26, trigger_rate ~98%）。监控报 "process dead 5× with no sentinel/W&B" 是因为检测不到进程标记，不是进程真的挂了。

**行动项**：将 seed42/43 状态更正为 completed，结果可直接使用，无需重试。报告已写入 `artifacts/diag_plan_a_spatial_seed42_43.md`。

---
