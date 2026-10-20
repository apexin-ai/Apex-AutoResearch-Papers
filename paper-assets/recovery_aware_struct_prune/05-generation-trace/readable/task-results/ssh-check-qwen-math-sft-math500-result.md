# ssh check qwen math sft math500 result

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_qwen_math_sft_math500_result_20260523T104307_result.json`
- **Structured JSON:** [`05aca492717f5ff5a5dc.json`](../../sessions/05/05aca492717f5ff5a5dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，cron 已不存在（可能已被之前的 session 删除）。

**结果**: accuracy = **21.6%** (108/500), stderr ± 1.84%

**关键信号**: 82% 的样本被截断（410/500 truncated, avg_response_length=1745），说明 max_new_tokens=2048 对数学推理偏短，大量回答未生成完整答案就被截断。

**GPU 状态**: cuda:0 和 cuda:1 均空闲（0% util, 0 MiB）。

---
