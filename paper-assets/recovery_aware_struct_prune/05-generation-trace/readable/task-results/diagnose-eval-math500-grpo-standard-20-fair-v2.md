# diagnose eval math500 grpo standard 20 fair v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_grpo_standard_20_fair_v2_20260519T013818_result.json`
- **Structured JSON:** [`04501be862ad2bbf09cb.json`](../../sessions/04/04501be862ad2bbf09cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

**进程消失原因：正常结束，sentinel 未写入。**

日志最后一行明确显示评估于 `2026-05-19 09:35:46` 正常完成全部 500 题，结果已保存。tmux session 在脚本结束后自动退出，但脚本没有写 `_fair_v2` 对应的 sentinel 文件（`/tmp/agent-ml-exit/` 下只有旧的 `grpo_standard_20_fair.exit`，无 `v2` 版本）。

**结果：**
- **MATH-500 Accuracy: 26.40% (132/500)**, 置信区间 ±1.97%
- 总耗时约 7 小时 6 分钟
- 无 OOM、无 crash、无异常错误

问题仅是启动脚本缺少写 v2 sentinel 的逻辑，Cron 因找不到 sentinel 而误报。

---
