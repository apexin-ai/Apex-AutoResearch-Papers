# diagnose bjb1 18228 batch failure

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-18228-batch-failure_20260521T012027_result.json`
- **Structured JSON:** [`89062e0e22c168208976.json`](../../sessions/89/89062e0e22c168208976.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**核心结论：这是误报，不是实验失败。** 三个实验（norm005-seed58、norm01-seed57、norm003-seed59）全部正常完成，JSON 结果文件已存在。日志各 52 行，末尾有完整的 success rate 汇总，无任何错误。

失败的表象原因：`evaluate.py` 没有 W&B logging 和 sentinel 文件写入逻辑，所以监控系统检测不到完成信号。

结果摘要：
- norm003-seed59: **13.0%**
- norm005-seed58: **16.0%**
- norm01-seed57: **19.0%**

seed65 (PID 622479) 正在正常运行，约完成 40%。系统健康，不需要重跑。

报告已写入 `artifacts/diagnose_bjb1_18228_failure.md`。

---
