# check gpu cross validate

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_cross_validate_20260520T123955_result.json`
- **Structured JSON:** [`231853359c21b78b53d1.json`](../../sessions/23/231853359c21b78b53d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：westd-29022 GPU 状态

### GPU 概览

| GPU | Utilization | 显存占用 | 进程 |
|-----|------------|---------|------|
| **cuda:0** | **0%** | **0 MiB** / 97887 MiB | **无** |
| **cuda:1** | **0%** | **0 MiB** / 97887 MiB | **无** |
| cuda:2 | 97% | 29157 MiB / 97887 MiB | PID 226966 |
| cuda:3 | 100% | 29157 MiB / 97887 MiB | PID 227043 |

### cuda:2/3 上实际运行的进程

两个都是 **eval_gsm8k**（评估，非训练），18:26 启动，未设置 CUDA_VISIBLE_DEVICES：

- **PID 226966** → cuda:2：`eval_gsm8k.py --model_path grpo_standard_20_seed123 --max_samples 1319`
- **PID 227043** → cuda:3：`eval_gsm8k.py --model_path grpo_standard_20_seed456 --max_samples 1319`

### Director 提到的目标进程

**PID 245522 (grpo_cka_only_20_seed456) 和 PID 246464 (grpo_cka_only_15_v2) 均不存在。**

- `ps aux` 中无这两个 PID
- 日志文件 `grpo_cka_only_20_seed456.log` 和 `grpo_cka_only_15_v2.log` 也不存在于 `~/runs/recovery_aware_struct_prune/`
- 日志目录中无任何 `cka_only_20_seed456` 或 `cka_only_15_v2` 相关文件

### 结论

**cuda:0/1 确实完全空闲，不是 CUDA_VISIBLE_DEVICES 错位问题。** Director 提到的两个训练进程在 westd-29022 上从未启动过（无进程、无日志）。可能是进程名/服务器搞混了，或者这两个训练任务根本没有被下发到这台机器。

---
