# ops register westb crons

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_register_westb_crons_20260518T182313_result.json`
- **Structured JSON:** [`28516ccd590340ebcdc5.json`](../../sessions/28/28516ccd590340ebcdc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| 实验 | GPU | PID | 运行时间 | 状态 | Cron ID |
|---|---|---|---|---|---|
| eval_gsm8k_grpo_standard_20_1p5b | cuda:0 | 823050 | ~112 min | 运行中 (99% GPU) | `991bf561` |
| eval_gsm8k_grpo_cka_only_20_1p5b | cuda:1 | 822503 | ~112 min | 运行中 (98% GPU) | `4ee7cea1` |

两个 cron 已注册，每 5 分钟检查一次。进程结束后会自动读取结果文件并汇报。

---
