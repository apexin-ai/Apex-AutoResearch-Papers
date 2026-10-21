# diagnose exp 011 llama8b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-011-llama8b_20260517T025952_result.json`
- **Structured JSON:** [`902331901cf2aca054d8.json`](../../sessions/90/902331901cf2aca054d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败根因**: PID 174585 的旧 vLLM 进程占用了 83.5GB 显存，exp-011 启动时只剩 12.83 GiB，远不够所需的 85.47 GiB，触发 `ValueError`。

**模型文件完好**，4 个 safetensors shard 齐全（~14.9GB），路径正确。纯粹是显存被抢占。

**修复**: kill 掉 PID 174585 后重跑即可。建议在启动脚本前加 `pkill -f "vllm.entrypoints"` 防止复发。

报告已写入 `artifacts/exp-011-llama8b/diagnosis.md`。

---
