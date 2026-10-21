# diagnosis eval perdof object norm005 seed45 r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_eval-perdof-object-norm005-seed45-r2_20260519T152913_result.json`
- **Structured JSON:** [`5926c86995d93084e8f6.json`](../../sessions/59/5926c86995d93084e8f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：实验已正常完成，非异常退出。**

- 进程消失原因：评估运行完毕后进程自然退出，cron 在 sentinel 文件写入前检测到进程消失，产生误报
- 结果文件 `eval_object_perdof_norm005_seed45.json` 于 23:20 写入，内容完整
- **overall_success_rate = 0.10**（10 tasks × 10 rollouts，共 10/100 成功）
- Registry 已更新为 DONE (conclusion=success)

---
