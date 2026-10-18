# code llama eval bf16 fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_eval_bf16_fix_20260514T021119_result.json`
- **Structured JSON:** [`2397373761f481a1575d.json`](../../sessions/23/2397373761f481a1575d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已修复：**
- `run_llama_eval_fix.py:93` — `torch.float16` → `torch.bfloat16`，标签 `FP16` → `BF16`
- `run_exp_e_eval_fix.py:118` — `torch.float16` → `torch.bfloat16`

**无需修复：**
- `eval_ppl.py` — 已经是 `bfloat16`
- `run_llama_eval_recovery.py` — 已经是 `bfloat16`
- 其他文件的 `fp16` 均为变量名/字符串，不影响实际 dtype

**进程状态：**
- `llama_eval_bf16` tmux session — GPU 1 上运行中（14.9GB 已加载），PID 170958
- `mistral_pipeline` tmux session — GPU 0 上正常运行，未受影响

**注意：** 原任务指定 `CUDA_VISIBLE_DEVICES=0`，但实际 GPU 0 被 Mistral 占用（17.2GB），改用 GPU 1 启动 Llama eval。

---
