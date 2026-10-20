# diagnose exp 042b premise formal

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-042b-premise-formal_20260518T192035_result.json`
- **Structured JSON:** [`e7fc5f673d810b31f4fe.json`](../../sessions/e7/e7fc5f673d810b31f4fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根本原因：脚本参数顺序传反

脚本 `run_premise_formalization.sh` 定义的参数顺序是：

```bash
PORT=${1:-8000}
GPU=${2:-0}
```

但启动命令传的是 `bash scripts/run_premise_formalization.sh 2 8002`，导致：
- **PORT=2**（应为 8002）
- **GPU=8002**（应为 2）

vLLM 启动时 `CUDA_VISIBLE_DEVICES=8002`，调用 `pynvml.nvmlDeviceGetHandleByIndex()` 找不到 device 8002，抛出 `NVMLError_InvalidArgument` 崩溃。等待 120s 超时后脚本 exit 1。

### 是否有部分输出

无。vLLM 根本没启动成功，Python 推理脚本从未执行。输出目录不存在。

### 修复

参数顺序调换即可。正确命令：

```bash
bash scripts/run_premise_formalization.sh 8002 2
```

或者修改脚本，将参数顺序改为更符合直觉的 `GPU PORT`（与调用方的心智模型一致）：

```bash
GPU=${1:-0}
PORT=${2:-8000}
```

---
