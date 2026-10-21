# code check multiseed logs

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_multiseed_logs_20260517T074810_result.json`
- **Structured JSON:** [`8dd23b5863449be2a8b8.json`](../../sessions/8d/8dd23b5863449be2a8b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：partial — 实验设计与预期不符**

实验成功完成（EXIT_CODE=0），但实际跑的是 **2 methods × 2 seeds**，不是预期的 4 seeds × Standard：

| # | 配置 | Accuracy |
|---|------|----------|
| 1/4 | RASP seed=123 | 0.6050 (121/200) |
| 2/4 | Standard seed=123 | 0.6450 (129/200) |
| 3/4 | RASP seed=456 | 0.6000 (120/200) |
| 4/4 | Standard seed=456 | 0.6100 (122/200) |

**缺失：** seed 42 和 seed 789 的结果文件不存在。实际脚本只跑了 seed 123 和 456，且同时跑了 RASP 和 Standard 两种方法。

**判断：partial** — 进程本身无错误退出，但覆盖范围与任务描述（4 seeds × Standard only）不一致。

---
