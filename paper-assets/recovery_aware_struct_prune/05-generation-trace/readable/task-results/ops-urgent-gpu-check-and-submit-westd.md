# ops urgent gpu check and submit westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_gpu_check_and_submit_westd_20260517T181945_result.json`
- **Structured JSON:** [`fd6911c3a8587f6eba72.json`](../../sessions/fd/fd6911c3a8587f6eba72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| GPU | 状态 | 任务 |
|-----|------|------|
| cuda:0 | **已提交** | eval_sft_cka_only_20_n1319 (PID 43815) |
| cuda:1 | 运行中 | eval_math500_grpo_standard_20 (PID 14556) |
| cuda:2 | **已提交** | eval_postprune_rasp_30 (PID 43906) |
| cuda:3 | 运行中 | eval_math500_grpo_rasp_20_v3 (PID 31706) |

30% pruning 模型状态：`pruned_rasp_30` 和 `pruned_standard_30` 均存在（~10.1GB each，生成于 01:37-01:38）。

4 张 GPU 现在全部满载。

---
