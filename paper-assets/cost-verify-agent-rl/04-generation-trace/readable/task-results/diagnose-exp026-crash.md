# diagnose exp026 crash

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp026_crash_20260515T110209_result.json`
- **Structured JSON:** [`f7723049b03fa38e7276.json`](../../sessions/f7/f7723049b03fa38e7276.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp026 诊断结论：假警报，进程正常运行。**

- PID 778562 存活，运行 24 分钟，状态 `Sl+`
- 2 个 Ray worker 占用 GPU，利用率 96-97%
- 日志无任何 error/traceback/OOM
- 初始验证已完成（reward mean 0.3226），当前在 step 0/150 的 rollout 阶段
- Cron 误报原因可能是 FSDP 编译/模型加载期间进程短暂不响应

报告已写入 `artifacts/exp026/crash_diagnosis.md`。建议 30 分钟后再检查 step 1 是否完成。

---
