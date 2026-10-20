# diagnosis qwen8b watcher bug check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_qwen8b_watcher_bug_check_20260521T135406_result.json`
- **Structured JSON:** [`47397015c689737b06a0.json`](../../sessions/47/47397015c689737b06a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都**没有** pgrep 自匹配 bug：

- **start_qwen8b_on_free_gpu.sh** (PID 356867, 存活中，已运行 1h46m)：用 `nvidia-smi --query-compute-apps` 查 GPU 占用，bash watcher 不会出现在 nvidia-smi 的 compute app 列表中，无自匹配风险。当前 GPU 0/1/2 全忙，watcher 每 60s 轮询，行为正常。
- **start_cuda3_chain_v2.sh**：用 `kill -0 $PID` 等待特定 PID，纯 PID 检测，无进程名匹配。

报告已写入 `artifacts/_project/analysis/watcher_bug_check.txt`。

---
