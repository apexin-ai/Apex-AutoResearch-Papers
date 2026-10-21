# ssh seed456 result and cka math500 westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed456_result_and_cka_math500_westb0_20260522T180452_result.json`
- **Structured JSON:** [`ee12e26ce0d54d1e3706.json`](../../sessions/ee/ee12e26ce0d54d1e3706.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常，12G 模型正在从磁盘加载到 CPU 内存（CPU 99%），尚未 transfer 到 GPU。这是正常行为。

## seed456 GSM8K eval 结果
- 状态: **completed**
- accuracy: **50.87%** (671/1319)
- eos_rate: 99.55%
- stderr: 0.01377

## CKA-only MATH-500 启动
- PID: **234500** (python 子进程，父进程 234495)
- 模型路径: `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20` (根目录，无 checkpoint 子目录)
- GPU:0 显存: 3 MiB (模型仍在 CPU 加载中，12G safetensors 读盘需要几分钟)

**注意**: GPU:1 上有另一个正在运行的 eval (PID 220343, `eval_gsm8k grpo_qwen_math_cka_only_20 n500_v2`)，已运行约 3 小时。

---
