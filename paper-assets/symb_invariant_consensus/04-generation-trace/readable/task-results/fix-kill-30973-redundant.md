# fix kill 30973 redundant

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-30973-redundant_20260523T182216_result.json`
- **Structured JSON:** [`7721f2cdf64c9c83fc2d.json`](../../sessions/77/7721f2cdf64c9c83fc2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 结果

| GPU | 状态 | 说明 |
|-----|------|------|
| cuda:0 | 已空闲 (0MiB) | qwen25-pw-seed789-v3 在连接前已结束 |
| cuda:1 | 已空闲 (0MiB) | killed llama-pw-seed789-v2 残留进程 (PIDs 48261, 48260, 48252) |
| cuda:2 | 正常运行 (88275MiB) | vLLM (LLaMA, port 8002) 未受影响 |

**被 kill 的进程**：
- PID 48261 — `run_cross_dataset_replication.py` (llama-pw-seed789-v2 主进程)
- PID 48260 — timeout wrapper
- PID 48252 — bash wrapper

**注意**：qwen25-pw-seed789-v3 的实验进程和对应的 vLLM 在连接时已经不存在，无需操作。cuda:2 的 vLLM 和 seed456 实验完全未受影响。

---
