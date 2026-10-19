# infra check bjb1 18228 gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-bjb1-18228-gpus_20260516T045312_result.json`
- **Structured JSON:** [`a8e12b80655c8f079853.json`](../../sessions/a8/a8e12b80655c8f079853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

## GPU 状态总览

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| cuda:0 | 19% | 2410/24564 MiB | **占用** |
| cuda:1 | 0% | 1/24564 MiB | **空闲** |
| cuda:2 | 79% | 9467/24564 MiB | **占用** |
| cuda:3 | 99% | 9395/24564 MiB | **占用** |

## 各 GPU 进程详情

### cuda:0 — PID 390936
```
python -u src/evaluate.py --mode crm_perdof --benchmark object --n_rollouts 10 --seed 42 --K 10
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt
  --output_file logs/eval_object_perdof_default_norm_r2.json
```
即 **eval-acr-object-v4-default-r2**，正常运行中。

### cuda:1 — 空闲
无进程。

### cuda:2 — 两个进程共享
| PID | 任务 | 显存 |
|-----|------|------|
| **428411** | eval-obs-only-object-norm02-seed44-**r2** | 4717 MiB |
| **431194** | eval-obs-only-object-norm02-seed44-**r3** | 4717 MiB |

两个进程的完整命令相同：
```
--mode crm_obs_only --benchmark object --n_rollouts 10 --seed 44 --K 10
  --crm_checkpoint .../obs_only/crm_best.pt --max_correction_norm 0.2
  --output_file logs/eval_object_obs_only_norm02_seed44.json
```

### cuda:3 — 两个进程共享
| PID | 任务 | 显存 |
|-----|------|------|
| **428122** | eval-argmin-object-seed44-**r2** | 4681 MiB |
| **430990** | eval-argmin-object-seed44-**r3** | 4681 MiB |

两个进程的完整命令相同：
```
--mode reconvla --benchmark object --n_rollouts 10 --seed 44 --K 10
  --output_file logs/eval_object_reconvla_seed44.json
```

## 关键发现

1. **cuda:1 空闲**，确认可用。
2. **r2 的 PID 428117 和 428406 仍然存活**（与 registry 的 killed 状态不符）。它们的 python 子进程 428122 和 428411 在活跃运行。
3. **r3 的进程也在运行**（PID 430990 和 431194），与 registry 显示 killed 不符。
4. **cuda:2 和 cuda:3 各有两个重复实验在跑**（r2 和 r3 写同一个 output_file），会互相覆盖结果。这是个问题——两组完全相同参数的实验写同一个输出文件。

---
