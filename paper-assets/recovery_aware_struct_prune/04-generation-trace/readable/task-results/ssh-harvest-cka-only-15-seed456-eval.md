# ssh harvest cka only 15 seed456 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_cka_only_15_seed456_eval_20260520T230232_result.json`
- **Structured JSON:** [`23ea8510986a68d66020.json`](../../sessions/23/23ea8510986a68d66020.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程**仍在运行**，未退出。PID 285821 状态 `Rl+`，CPU 108%。

当前进度：761/1319（58%），最近一次 checkpoint 报告（750/1319）acc=0.7253，eos_rate=99.07%。

第 761 条的 109.98s/it 是 GPU 争用导致的短暂慢速（当前 4 个 eval 同时跑在 cuda:0-3 上），不是崩溃。

按 ~2.5s/it 平均速度估算，剩余 558 条约需 ~23 分钟完成。暂不更新 registry 和删除 cron。

---
