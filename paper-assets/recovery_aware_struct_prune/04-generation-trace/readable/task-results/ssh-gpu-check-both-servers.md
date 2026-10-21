# ssh gpu check both servers

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_check_both_servers_20260522T230647_result.json`
- **Structured JSON:** [`7f52914003e0d1f73c38.json`](../../sessions/7f/7f52914003e0d1f73c38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## westd-32935 GPU 状态

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| 0 | 16.7/97.9 GB | 98% | **占用** | `eval_math500_grpo_rasp_alpha2p0_20` (PID 83718) |
| 1 | 17.0/97.9 GB | 98% | **占用** | `eval_math500_sft_cka_only_20` (PID 75284) |
| 2 | 30.4/97.9 GB | 96% | **占用** | `eval_math500_grpo_random_20_v2` (PID 83161) + 另一进程 (PID 83554) |
| 3 | 12.7/97.9 GB | 94% | **占用** | `eval_math500_grpo_rasp_alpha1p0_20` (PID 86243) — 新任务，评估 `grpo_stage2_rasp_20_fair` |

**GPU 3 不空闲**——之前的 `eval_math500_sft_rasp_alpha1p0_20_v2` 已完成，但新任务 `eval_math500_grpo_rasp_alpha1p0_20` 已在其上启动。

**eval_math500_sft_rasp_alpha1p0_20_v2 结果**：`accuracy = 0.212` (MATH-500, α=1.0 SFT RASP)

## westb-23072 GPU 状态

| GPU | 显存占用 | 利用率 | 状态 | 进程 |
|-----|---------|--------|------|------|
| 0 | 0/97.9 GB | 0% | **空闲** | 无进程 |
| 1 | 16.5/97.9 GB | 99% | **占用** | `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2` (PID 220343) |

**E_MATH500_SFT_QWEN_CKA 失败分析**：结果文件不存在，且模型目录 `sft_qwen_math_cka_only_20` 也不存在。存在的是 `sft_qwen_math_cka_only_20_final`——可能是路径名不匹配导致失败。

## 空闲 GPU 汇总

仅 **westb-23072 cuda:0** 空闲，可调度新任务。

---
