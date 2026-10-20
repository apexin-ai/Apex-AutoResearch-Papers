# diag westb grpo v8 verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westb-grpo-v8-verify_20260515T161818_result.json`
- **Structured JSON:** [`6b92d902166152b38b5a.json`](../../sessions/6b/6b92d902166152b38b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个进程都在正常运行，双卡满载。** Director 报告的"只有1张卡"是误报。

| 项目 | 状态 |
|------|------|
| **RASP v8** (PID 532861) | cuda:0, 运行 1h44m, GPU 100%, 显存 71674/97887 MiB |
| **Standard v8** (PID 534667) | cuda:1, 运行 1h35m, GPU 100%, 显存 71692/97887 MiB |
| GPU 温度 | 两卡均 83°C, 功耗 ~600W/600W |

两个 GRPO v8 训练进程均健康运行，无异常。

---
