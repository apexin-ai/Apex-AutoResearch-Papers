# code check humaneval standard

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_humaneval_standard_20260517T083038_result.json`
- **Structured JSON:** [`a95248780aa2ba917545.json`](../../sessions/a9/a95248780aa2ba917545.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_humaneval_sft_standard_20 状态：已完成**

| 项目 | 结果 |
|------|------|
| PID 9605 | 已退出 |
| tmux session | 已销毁 |
| 退出码 | 0 (正常) |
| **pass@1** | **0.0305 ± 0.0134 (5/164)** |
| 耗时 | ~17 分钟 |

模型几乎全部生成了 chain-of-thought 式的自然语言文本而非代码，所有 response 都截断在 max_tokens=512，导致 pass@1 极低（3.05%）。

**cuda:3 当前状态：空闲**（0MiB / 0% utilization）。cuda:0/1/2 被其他 python 进程占用。

---
