# ssh check cka only rerun math500 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_cka_only_rerun_math500_result_20260523T085503_result.json`
- **Structured JSON:** [`f2c5f693d805f49f2c19.json`](../../sessions/f2/f2c5f693d805f49f2c19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。Cron 不存在（可能已被删除或未在本 session 创建）。

**结果汇报：**

| 指标 | 值 |
|------|-----|
| Accuracy | **27.4%** (137/500) |
| Stderr | ±1.995% |
| Natural EOS | 390, Truncated 110 |
| Avg response length | 654.7 tokens |

**GPU 3 已空闲**（0% utilization, 0 MiB memory）。

对比：旧 eval 脚本报 29.2%，新 eval 脚本 rerun 得 27.4%，下降 1.8pp。SFT CKA-only 新脚本为 26.8%，GRPO 仍高 0.6pp。

---
