# gpu kill 064 deploy 069 llama8b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_kill-064-deploy-069-llama8b_20260519T120406_result.json`
- **Structured JSON:** [`9519d92c7d190c00152f.json`](../../sessions/95/9519d92c7d190c00152f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

| 项目 | 状态 |
|---|---|
| exp-064 kill | 已清理（vLLM port 8002 + runner + 2个 tmux session） |
| cuda:0 孤儿 vLLM (port 8005) | 已清理 |
| exp-069-llama8b-logiqa200 | 运行中，vLLM port 8012 on cuda:2，HTTP 200 正常返回 |

**nvidia-smi 最终状态：**
- cuda:0: 7% util, 16477 MiB（有一个小进程，非 exp-064 相关）
- cuda:1: 97%, 88287 MiB
- cuda:2: 97%, 88261 MiB — exp-069 LLaMA-8B 运行中
- cuda:3: 97%, 88263 MiB

注意 cuda:0 上多了 16GB 占用，不是我们启动的。可能是其他用户进程。

---
