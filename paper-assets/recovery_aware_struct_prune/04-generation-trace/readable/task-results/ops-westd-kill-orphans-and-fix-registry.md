# ops westd kill orphans and fix registry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-kill-orphans-and-fix-registry_20260515T195537_result.json`
- **Structured JSON:** [`4a97d490eef7e71c5e76.json`](../../sessions/4a/4a97d490eef7e71c5e76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

1. **Kill 孤儿进程** — PID 59601, 59675 已 kill，westd-11672 双 GPU 已释放 (0 MiB, 0%)
2. **Registry 修复** — 两个 eval 实验已更新至 DONE + success：
   - `eval_sft_rasp_20_westd_n100`: accuracy=0.67, n=100, eos_rate=0.99
   - `eval_sft_standard_20_westd_n100`: accuracy=0.63, n=100, eos_rate=0.97
   - 两者 notes 均记录了 v2 失败历史 (EXIT_CODE=127, python path 错误)

---
