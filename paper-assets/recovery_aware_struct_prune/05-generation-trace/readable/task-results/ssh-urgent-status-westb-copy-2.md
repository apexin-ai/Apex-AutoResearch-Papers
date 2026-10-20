# ssh urgent status westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_westb_20260523T183609_result.json`
- **Structured JSON:** [`14c9c805ff9074977543.json`](../../sessions/14/14c9c805ff9074977543.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 状态

**空闲 GPU**: 无（两张均被占用）

**运行中**:
| PID | GPU | 实验名 | 运行时间 | 进度 | 显存 |
|-----|-----|--------|---------|------|------|
| 309964 (子进程 309969) | cuda:0 | grpo_random_20_retrain_v2 | 2h18m | 76/100 steps (76%) | 55,530 MiB / 97,887 MiB |
| 306963 (子进程 306968) | cuda:1 | eval_math500_sft_cka_only_20_fixed_v2 | 2h51m | 381/500 (76%) | 17,030 MiB / 97,887 MiB |

**已完成 eval**: 无（结果文件尚未生成，eval 仍在运行中）

**grpo_random_20_retrain_v2**: 运行中，76/100 steps，输出目录 `grpo_random_20_retrain/` 已创建（含 `completions/` 子目录），预计约 40 分钟内完成

**eval_math500_sft_cka_only_20_fixed_v2**: 运行中，381/500 (76%)，平均 ~27s/it，预计约 50 分钟内完成

**Checkpoint 确认**:
- grpo_cka_only_20/checkpoint-100: **存在** (11.5GB)
- sft_rasp_alpha3p0_20/checkpoint-935: **存在** (11.5GB)
- sft_random_20: **存在** (11.3GB)

**磁盘**: /root/autodl-tmp 209G/250G (84%), 剩余 42G

---
