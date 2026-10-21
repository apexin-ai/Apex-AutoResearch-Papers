# ssh verify gpus westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_gpus_westb_20260523T222412_result.json`
- **Structured JSON:** [`00584252fc2bc8de5e4f.json`](../../sessions/00/00584252fc2bc8de5e4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### 当前 GPU 占用

| GPU | 进程 | PID | 显存占用 | GPU 利用率 | 温度 | 运行时间 |
|-----|------|-----|---------|-----------|------|---------|
| 0 | eval_math500 **grpo_cka_only_20_fixed** | 321428 | 17,044 MiB / 97,887 MiB | **95%** | 71°C | 2h48m |
| 1 | eval_math500 **grpo_random_20_fixed** | 330254 | 15,354 MiB / 97,887 MiB | **99%** | 81°C | 37m |

- 每张 GPU **只有一个进程**，无竞争
- 注意：GPU 0 实际 PID 是 **321428**（不是预期的 321423），可能是子进程 fork 导致的偏移

### 正在运行的 eval 详情

- **GPU 0**: `eval_math500_grpo_cka_only_20_fixed.json` ← 模型路径 `grpo_cka_only_20/checkpoint-100`
- **GPU 1**: `eval_math500_grpo_random_20_fixed.json` ← 模型路径 `grpo_random_20_retrain`

### 已完成的 eval 结果

| 文件 | 完成时间 | Accuracy | n_correct / n_total |
|------|---------|----------|---------------------|
| eval_math500_**sft_cka_only_20_fixed** | May 24 03:33 | **27.4%** | 137/500 |
| eval_math500_**grpo_rasp_alpha0p5_20** | May 23 18:05 | **24.8%** | 124/500 |
| eval_math500_**sft_qwen_math_cka_only_20** | May 23 18:37 | **21.6%** | 108/500 |
| eval_math500_**sft_standard_25** | May 21 19:16 | **13.0%** | 65/500 |

---
