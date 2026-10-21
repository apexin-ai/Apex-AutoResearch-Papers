# code prep exp010 mistral v3 script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp010-mistral-v3-script_20260517T064640_result.json`
- **Structured JSON:** [`6b3cf695d3fd4a1af026.json`](../../sessions/6b/6b3cf695d3fd4a1af026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法验证通过。v3 脚本关键参数：

| 参数 | 值 |
|------|-----|
| 模型路径 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3` |
| max-model-len | 8192 |
| max-tokens | 4096 |
| gpu-memory-utilization | 0.90 |
| vLLM 清理 | `pkill -9 -f "vllm.entrypoints"` + sleep 5 + nvidia-smi 确认 |
| 启动等待 | 180s with health check |

两个问题已修复：
1. 开头增加标准化 vLLM 清理块（`pkill -9 -f "vllm.entrypoints"`），只杀 vllm 进程不会误杀 tmux
2. max-model-len 保持 8192（原脚本已是 8192，v1 的 4096 问题已在之前修复过）

---
