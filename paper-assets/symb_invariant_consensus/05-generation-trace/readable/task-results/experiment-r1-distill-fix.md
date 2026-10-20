# experiment r1 distill fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1-distill-fix_20260521T142748_result.json`
- **Structured JSON:** [`f2b8b727526b149aeb38.json`](../../sessions/f2/f2b8b727526b149aeb38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**阻塞**：无法继续，两个问题：

### 1. 模型权重缺失
`/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B/` 只有 config 文件（4.3GB），缺少两个 safetensors 权重文件（共 ~16GB），vLLM 无法启动。

### 2. 数据盘 100% 满
`/root/autodl-tmp/` 250GB 已全部用完（剩 845MB），无法下载 ~12GB 的权重文件。

当前大模型占用：
| 模型 | 大小 |
|------|------|
| Qwen2.5-72B-Instruct | 100GB |
| gemma-3-27b-it | 52GB |
| Qwen2.5-14B-Instruct | 28GB |
| Qwen3-14B | 28GB |
| Mistral-7B-Instruct-v0.3 | 16GB |
| Qwen2.5-7B-Instruct | 15GB |
| deepseek-r1-0528-qwen3-8b | 8.7GB |

需要释放 ~12GB 空间。请告诉我可以删除哪些模型（或者指定其他解决方案）。

---
