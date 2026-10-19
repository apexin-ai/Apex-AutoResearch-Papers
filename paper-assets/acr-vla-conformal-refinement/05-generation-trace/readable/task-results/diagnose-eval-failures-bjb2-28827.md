# diagnose eval failures bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-failures-bjb2-28827_20260523T042920_result.json`
- **Structured JSON:** [`38f1e047435e7bb37444.json`](../../sessions/38/38f1e047435e7bb37444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论**：三个实验在04:12提交时立即死亡，无任何日志/traceback/OOM记录。原始日志已被12:12的重跑覆盖。最可能原因是**GPU资源争抢**——提交时训练任务 `train-crm-smolvla-3suite-v1` 仍在运行（07:03才结束），占用了GPU导致eval进程CUDA初始化失败后立即退出。

三个实验已在12:11-12:12重新提交，当前均正常运行中，无需额外操作。

报告已写入 `artifacts/diagnose_bjb2_failures_20260523.md`。

---
