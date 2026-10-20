# infra 25068 gpu cleanup status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_25068-gpu-cleanup-status_20260519T084512_result.json`
- **Structured JSON:** [`fdf4962fbd8854c89dcc.json`](../../sessions/fd/fdf4962fbd8854c89dcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

```
GPU 状态:
  cuda:0: 空闲 ✓ (killed PID 171421, exp-059 Qwen3-14B vLLM)
  cuda:1: 空闲 ✓ (原本就空闲)
  cuda:2: 空闲 ✓ (killed PID 175167, exp-061 Qwen2.5-7B vLLM)
  cuda:3: exp-062 Gemma-3-27B vLLM 运行中 (PID 187802, 88146MiB)
          vLLM 服务正常，已响应 /v1/models 请求
          exp062_run 尚未启动（无此 tmux session）

可用模型:
  - Qwen2.5-72B-Instruct     (100G)
  - gemma-3-27b-it            (51G)
  - Qwen2.5-14B-Instruct      (28G)
  - Qwen3-14B                 (28G)
  - Mistral-7B-Instruct-v0.3  (16G)
  - Qwen2.5-7B-Instruct       (15G)
  - deepseek-r1-0528-qwen3-8b (8.7G)
  - DeepSeek-R1-Distill-Llama-8B (4.3G)
  - llama-4-scout             (60K, 可能下载不完整)

磁盘: /root/autodl-tmp 250G 已用 247G，仅剩 3.3G (99%)
```

**注意**: 磁盘几乎满了（仅 3.3G 可用）。如果需要跑新实验或下载新模型，可能需要清理不再使用的模型（如 llama-4-scout 残留目录、或已完成实验的模型）。

---
