# launch seed123 eval westd2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_seed123_eval_westd2_20260522T130546_result.json`
- **Structured JSON:** [`b2d811abdac00022e4a5.json`](../../sessions/b2/b2d811abdac00022e4a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实际情况和预期不同：

| GPU | PID | 进程 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 43755 | eval_gsm8k rasp_alpha3p0_20 | 29590MiB | 91% |
| 1 | 5241 | eval_math500 sft_random_20 | 17642MiB | 98% |
| **2** | **46229** | **eval_gsm8k seed123** | 26210MiB | 99% |
| **3** | **40073** | **eval_gsm8k depth_first_20** | 16474MiB | 91% |

seed123 (PID 46229) 已经在 GPU 2 上，depth_first (PID 40073) 在 GPU 3 上 — 它们各占一张卡，并没有双 eval 共享同一 GPU 的情况。四张卡都在跑任务，没有空闲 GPU。

要怎么处理？继续 kill seed123 重启（但没有空闲卡），还是维持现状让它跑完？

---
