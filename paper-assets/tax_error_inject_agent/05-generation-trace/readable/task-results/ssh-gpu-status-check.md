# ssh gpu status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-status-check_20260514T103719_result.json`
- **Structured JSON:** [`4fdcd42ca3a869a057bc.json`](../../sessions/4f/4fdcd42ca3a869a057bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态（nvidia-smi）

| GPU | 状态 | 详情 |
|-----|------|------|
| cuda:0 | 空闲 | 0MiB / 32607MiB, 29°C, 0% util |
| cuda:1 | **占用** | PID=37424 `python3 eval/recovery.py`, 17082MiB / 32607MiB, 56°C, 81% util |
| cuda:2 | 空闲 | 0MiB / 32607MiB, 29°C, 0% util |
| cuda:3 | 空闲 | 0MiB / 32607MiB, 28°C, 0% util |

## 训练进程

| PID | 启动时间 | 命令 | 状态 |
|-----|---------|------|------|
| 11050 | 14:43 | `python3 -u data/collect_trajectories.py --num_trajectories 500 --output_dir data/trajectories/ --workers 4` | 运行中，已完成 411/500，成功率 303/411 |
| 37424 | 18:33 | `python3 eval/recovery.py --model_path checkpoints/mini_taxei_sft/v0-20260514-181630/checkpoint-195 --base_model Qwen3-8B --no_inject --output eval_results/mini_taxei_clean.json` | 运行中 (cuda:1)，正在评估第 21/47 个任务 |

## Checkpoint 目录（共 3.5GB）

| 实验 | 路径 | Checkpoints |
|------|------|-------------|
| dryrun_sft | `checkpoints/dryrun_sft/v0-20260514-161248/` | 无保存的 checkpoint |
| dryrun_sft_v2 | `checkpoints/dryrun_sft_v2/v0-20260514-161410/` | checkpoint-8 |
| **mini_taxei_sft** | `checkpoints/mini_taxei_sft/v0-20260514-181630/` | checkpoint-65, checkpoint-130, **checkpoint-195**（正在评估） |
| **mini_vanilla_sft** | `checkpoints/mini_vanilla_sft/v0-20260514-181708/` | checkpoint-18, checkpoint-36, checkpoint-54 |

---
