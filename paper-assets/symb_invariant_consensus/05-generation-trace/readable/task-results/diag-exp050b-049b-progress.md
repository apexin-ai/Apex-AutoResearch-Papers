# diag exp050b 049b progress

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp050b-049b-progress_20260518T225905_result.json`
- **Structured JSON:** [`1e039c1ae96922168e45.json`](../../sessions/1e/1e039c1ae96922168e45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### exp-050b (Mistral ICL Oracle, cuda:2)
- **进度**: 168/199 (84.4%)
- **状态**: 正常运行，HTTP 请求持续返回 200
- **最新 ETA**: ~15 min (32 remaining, avg 28.3s/prob)
- **预估完成时间**: ~07:15 UTC (约 15 分钟后)

### exp-049b (Mistral LogiQA, cuda:3)
- **进度**: 162/200 (81.0%)
- **状态**: 正常运行，最新一条处理的是 logiqa_161
- **最新 ETA**: ~15 min (38 remaining, avg 23.9s/prob)
- **预估完成时间**: ~07:15 UTC (约 15 分钟后)

### GPU 使用
| GPU | 用途 | 显存 | 利用率 | 温度 |
|-----|------|------|--------|------|
| 0 | VLLM (其他任务) | 88.4/97.9 GB | 100% | 58°C |
| 1 | VLLM (其他任务) | 88.4/97.9 GB | 100% | 56°C |
| 2 | VLLM (exp-050b) | 88.4/97.9 GB | 96% | 53°C |
| 3 | VLLM (exp-049b) | 88.1/97.9 GB | 96% | 54°C |

两个实验均正常，预计约 15 分钟后先后完成。

---
