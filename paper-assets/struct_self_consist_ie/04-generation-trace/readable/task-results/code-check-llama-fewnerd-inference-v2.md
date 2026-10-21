# code check llama fewnerd inference v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_llama_fewnerd_inference_v2_20260519T023200_result.json`
- **Structured JSON:** [`ac89db61989d18fa7659.json`](../../sessions/ac/ac89db61989d18fa7659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**tmux 状态**: `llama_fewnerd_infer` session **仍在运行**

**进度**: ~82-83%（已处理 ~245k-249k / 301184 prompts），运行约 1h21m，预计剩余 ~15-25 分钟

**运行进程**: 4 个并行 `run_mvp_pilot.py` 进程
- seed=42 → `output/llama_fewnerd_s42`
- seed=123 → `output/llama_fewnerd_s123`
- seed=456 → `output/llama_fewnerd_s456`（2 个进程）

**输出文件**: 尚未生成（推理完成后才会写入）

**错误日志**: 无错误/失败文件，日志写入 `logs/llama_fewnerd_inference.log`

**模型**: `checkpoints/llama3.1-8b-fewnerd-merged`，参数 `n_samples=8, temperature=1.0, collect_logprobs`

---
