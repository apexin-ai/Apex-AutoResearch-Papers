# ops verify all gpu status urgent

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_all_gpu_status_urgent_20260517T150112_result.json`
- **Structured JSON:** [`45234e9485f9d8c7f417.json`](../../sessions/45/45234e9485f9d8c7f417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 张卡全部在跑，进程全部存活。

| 服务器 | GPU | 期望实验 | 期望PID | 实际PID | 状态 | 显存 | Util |
|--------|-----|----------|---------|---------|------|------|------|
| westb-23072 | cuda:0 | grpo_cka_only_20 | 725232 | 725232 | **存活** | 57265MiB / 97887MiB | 100% |
| westb-23072 | cuda:1 | grpo_random_20 | 719684 | 719684 | **存活** | 73165MiB / 97887MiB | 100% |
| westd-11672 | cuda:0 | eval_humaneval_grpo_rasp_20_2048 | 28131 | 28136¹ | **存活** | 17019MiB / 97887MiB | 92% |
| westd-11672 | cuda:1 | eval_math500_grpo_standard_20 | 14556 | 14556 | **存活** | 31527MiB / 97887MiB | 98% |
| westd-11672 | cuda:2 | eval_humaneval_grpo_standard_20_2048 | 27194 | 27199¹ | **存活** | 17277MiB / 97887MiB | 97% |
| westd-11672 | cuda:3 | eval_math500_grpo_rasp_20_v3 | 31706 | 31706 | **存活** | 29619MiB / 97887MiB | 99% |

¹ 期望 PID 是 wrapper shell，实际 GPU 上的 python 进程 PID 略有偏移（28131→28136, 27194→27199），属正常行为。

---
