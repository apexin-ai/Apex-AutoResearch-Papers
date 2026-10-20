# ssh urgent westb full check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_westb_full_check_20260523T192322_result.json`
- **Structured JSON:** [`a5839147ab95974fed80.json`](../../sessions/a5/a5839147ab95974fed80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072

| 项目 | 状态 |
|------|------|
| **空闲 GPU** | `cuda:0` (97887 MiB 全空闲) |
| **占用 GPU** | `cuda:1` — PID 306968 (python), 17030 MiB, 99% util |
| **grpo_random_20_retrain_v2** | **已完成** ✓ EXIT_CODE=0, 100/100 steps, 耗时 2h56m。checkpoint: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain/model.safetensors` + `checkpoint-100/model.safetensors`。wandb: `grpo_sft_random_20` (9c16hnf7) |
| **eval_math500_sft_cka_only_20_fixed_v2** | **运行中** 484/500 (97%), 已跑 3h38m, 预计还需 ~15min。结果 JSON 尚未写入 |
| **sft_rasp_alpha3p0_20 checkpoint** | `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935/model.safetensors` |
| **磁盘** | `/root/autodl-tmp/` **99%** (246G/250G, 仅剩 4.3G) — 危险 |

**注意**: 数据盘只剩 4.3G，后续实验（如 grpo retrain for sft_rasp_alpha3p0_20）需要先清理空间。

---
