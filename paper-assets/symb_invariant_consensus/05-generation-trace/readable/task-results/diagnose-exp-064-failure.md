# diagnose exp 064 failure

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-064-failure_20260519T181304_result.json`
- **Structured JSON:** [`1bc39401bc15924366dd.json`](../../sessions/1b/1bc39401bc15924366dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：exp-064 是 Cron 误报，实验已正常完成 204/204。**

关键发现：
- 日志末尾 `FULL_MVP_DONE`，results.json 包含全部 204 条结果
- **SICA = 83.8%, SC = 83.8%**（完全一致，约束聚合无额外增益）
- Cron 误报原因：脚本没写 sentinel 文件，也没集成 W&B，进程正常退出后 Cron 探测不到进程，累计 5 次误判为 failed
- 结果文件完整，无需重跑

报告已写入 `artifacts/exp-064-diagnosis.md` 并注册。

---
