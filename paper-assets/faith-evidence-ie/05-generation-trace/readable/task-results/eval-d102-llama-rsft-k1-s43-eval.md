# eval d102 llama rsft k1 s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d102_llama_rsft_k1_s43_eval_20260518T130559_result.json`
- **Structured JSON:** [`29fb188c9e8a3cbeb9a0.json`](../../sessions/29/29fb188c9e8a3cbeb9a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**C001 约束触发**：cuda:3 当前被 PID 541954 占用 18412MiB，不满足 < 2GB 的要求。四张卡全部被占用：

| GPU | PID | 显存占用 |
|-----|-----|---------|
| 0 | 540786 | 22034MiB |
| 1 | 540991 | 27794MiB |
| 2 | 542126 | 16608MiB |
| 3 | 541954 | 18412MiB |

Checkpoint 验证通过：checkpoint-1107、SFT adapter、base model 均存在。

需要等 cuda:3 上的任务结束后再提交 eval。要我查一下 cuda:3 上跑的是什么任务，还是等它跑完后再提交？

---
