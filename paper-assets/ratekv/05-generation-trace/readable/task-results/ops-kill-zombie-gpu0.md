# ops kill zombie gpu0

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_zombie_gpu0_20260514T063856_result.json`
- **Structured JSON:** [`0d9ec57da133aacd819a.json`](../../sessions/0d/0d9ec57da133aacd819a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个进程已处理：
- PID 189442: `No such process`（已自行退出）
- PID 190168, 190531: 已被 kill，无报错

GPU 0 显存从 ~46.4 GiB 占用降至 **35.6 GiB**（剩余为 PID 185608 downstream_eval_qwen 17.4G + PID 189811 l0_heuristic_corrected 18.2G，均为合法进程）。GPU 1 上 PID 188308 (bf16_reeval) 67.2G 不受影响。

---
