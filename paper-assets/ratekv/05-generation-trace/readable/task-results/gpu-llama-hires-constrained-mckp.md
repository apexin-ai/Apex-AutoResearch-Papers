# gpu llama hires constrained mckp

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_llama_hires_constrained_mckp_20260514T214744_result.json`
- **Structured JSON:** [`fceea6c29911bb8dfedf.json`](../../sessions/fc/fceea6c29911bb8dfedf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已 RUNNING。

**摘要**:
- 脚本: `/root/ratekv/run_llama_hires_constrained.py` (基于 yi15 版本改造，处理 llama 标准 profile 的 `profiles` 包装层)
- 配置: cuda:0, bf16, budget=0.25, max_2bit=2, l0_exclude_2bit=True
- PID 266155，tmux session: `llama_hires_constrained_mckp`，log: `~/runs/ratekv/llama_hires_constrained_mckp.log`
- 模型已加载到 cuda:0 (17.1GB)，cuda:1 上的 Mistral v4 未受影响 (18.0GB)
- MCKP allocation 已完成: `{4: 253, 8: 1, 2: 2}`；2-bit heads: `[26,0, 31,7]`；8-bit head: `[12,3]`；distortion=0.7015
- 当前正在 WikiText-2 评估三个 PPL (baseline / MCKP / uniform 4-bit)

Done.

---
