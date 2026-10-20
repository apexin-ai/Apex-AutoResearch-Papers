# diag scoring progress

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_scoring_progress_20260515T023008_result.json`
- **Structured JSON:** [`3656f1450ba3709e85b5.json`](../../sessions/36/3656f1450ba3709e85b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### Structural scoring (PID 85841)
- **状态**: 已完成退出
- **结果**: 38/38 实例全部完成，耗时 1024.6s（~17 分钟）
- **Segments**: 491 个总计，351 scored，**140 failed**（fallback 23 次，其余为 API 返回 None content 导致的重试失败）
- **输出**: `/root/trace_distill_repair/pipeline_output/phase2_structural_scores.json`

### Line scoring v2 (PID 86816)
- **状态**: 运行中（已跑 ~32 分钟）
- **进度**: **10/38 实例完成**，正在处理第 11 个 `httpie_2`（130 segments）
- **PARSE_FAILURE**: 0
- **已完成实例**: black_14, black_1, black_2, black_5, cookiecutter_1, cookiecutter_2, cookiecutter_3, fastapi_1, fastapi_2, httpie_1
- **已用时间**: ~1652s（~28 分钟）到第 10 个实例
- **预估剩余**: 还剩 28 个实例。前 10 个平均 165s/实例，但 fastapi 实例（143-144 segments）各用了 ~10 分钟。保守估计还需 **40-60 分钟**。

---
