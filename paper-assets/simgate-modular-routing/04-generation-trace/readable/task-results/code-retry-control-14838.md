# code retry control 14838

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_retry-control-14838_20260517T145413_result.json`
- **Structured JSON:** [`727231c0370e0a1a6998.json`](../../sessions/72/727231c0370e0a1a6998.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，实验正常运行中。

## 报告

| 项目 | 状态 |
|------|------|
| **vLLM (port 8002, cuda:0)** | 运行中，session `vllm-retry` |
| **retry-part1** | PID 49468，7 tasks × 20 episodes = 140 episodes，已开始 `chemistry-mix` Episode 1 |
| **retry-part2** | PID 49575，4 tasks × 20 episodes = 80 episodes，已开始 `inclined-plane-determine-angle` Episode 1 |

**修复记录**：原始命令中 `--tasks 0 1 2 3...` 使用了数字索引，但脚本需要实际任务名（如 `chemistry-mix`）。已改用正确的任务名格式。

日志路径：`/tmp/retry-part1.log`、`/tmp/retry-part2.log`。

---
