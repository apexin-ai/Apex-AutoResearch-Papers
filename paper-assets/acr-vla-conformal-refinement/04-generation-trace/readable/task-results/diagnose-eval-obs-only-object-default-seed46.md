# diagnose eval obs only object default seed46

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-default-seed46_20260518T002341_result.json`
- **Structured JSON:** [`078e9480031c5644cfc6.json`](../../sessions/07/078e9480031c5644cfc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**`eval-obs-only-object-default-seed46` 实际已成功完成**，监控误报。

核心发现：
- JSON 结果文件存在且完整：overall_success_rate = **15.0%** (15/100)
- Log 正常结束，无任何错误
- GPU 3 当前空闲（实验已跑完释放）
- 监控报失败是因为：实验通过 nohup 启动绕过了任务管理系统，无 sentinel、无 W&B、无 runs/ log，进程正常退出后被误判为 crash

**`eval-obs-only-object-norm01-seed46`** 则确实从未运行过（无任何痕迹），需要重新提交。GPU 3 空闲可用。

报告已写入 `artifacts/diagnose_default_seed46.md`。

---
