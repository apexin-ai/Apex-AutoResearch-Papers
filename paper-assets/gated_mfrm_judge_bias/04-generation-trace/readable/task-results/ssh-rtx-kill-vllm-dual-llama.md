# ssh rtx kill vllm dual llama

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx_kill_vllm_dual_llama_20260522T233117_result.json`
- **Structured JSON:** [`d31e4d0d05d1a55bebf9.json`](../../sessions/d3/d31e4d0d05d1a55bebf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪，汇报：

---

### 执行结果

| 步骤 | 状态 |
|------|------|
| Kill Qwen vLLM (PID 420981) | 成功，cuda:1 显存已释放 |
| 第二个 Llama vLLM (cuda:1, port 8004) | 运行中，tmux `vllm-llama-2` |
| 第二个 collect.py | 运行中，tmux `judge-llama-b` |

### 分工方式

由于 collect.py 没有分片参数，两个 instance 如果跑相同 models 会 100% 重复。因此 kill 了原 collect.py，拆分 target_models：

| Shard | Port | Models | 剩余 tasks | ETA |
|-------|------|--------|-----------|-----|
| A (`judge-llama-a`) | 8001 (cuda:2) | gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613, gpt-4o, gpt-4o-mini | 2664 | ~700 min (11.7h) |
| B (`judge-llama-b`) | 8004 (cuda:1) | llama-3.3-70b, qwen2.5-72b, gemma-2-9b, qwen3-8b | 2135 | ~593 min (9.9h) |

Shard B 写入独立目录 `results/llama-3.3-70b-shard2/`（已复制现有 JSONL 做 resume），后续需合并。

### 加速效果

- 原 ETA: **~21h** (单 instance, 4816 remaining)
- 新 ETA: **~11.7h** (受限于 shard A 的 5 models)
- 加速: **~1.8x**

### GPU 状态

| GPU | 用途 |
|-----|------|
| 0 | 空闲 |
| 1 | Llama vLLM #2 (91GB) |
| 2 | Llama vLLM #1 (91GB) |
| 3 | Mistral vLLM (90GB) |

### 注意事项

- Shard B 的日志显示 "Remaining: -199" 是显示 bug（`done = len(completed)` 包含全部 model 的条目），实际 task list 构建正确 (2135 items)
- 完成后需合并 `results/llama-3.3-70b/` 和 `results/llama-3.3-70b-shard2/` 两个 JSONL
- GPU 0 仍空闲，如需进一步加速可再部署一个 vLLM instance

---
