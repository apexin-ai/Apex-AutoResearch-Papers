# ops harvest scan bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-scan-bjb2-28827_20260518T182743_result.json`
- **Structured JSON:** [`0c5bf442598ac0c53e84.json`](../../sessions/0c/0c5bf442598ac0c53e84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture acquired. Here's the report:

---

## bjb2-28827 实验扫描报告

### 已完成但未 harvest（需要标记 DONE）

| exp_id | SR% | JSON 文件 | Registry 状态 |
|--------|-----|-----------|--------------|
| eval-random-selection-object-seed44 | **13%** | `logs/eval_object_random_selection_seed44.json` (May 19 02:00) | RUNNING |
| eval-obs-only-object-norm01-seed42 | **19%** | `logs/eval_object_obs_only_norm01_seed42.json` (May 18 23:16) | DEPLOYED |
| eval-perdof-object-norm01-seed42 | **11%** | `logs/eval_object_perdof_norm01_seed42.json` (May 18 23:12) | DEPLOYED |

`eval-random-selection-object-seed44` 的 exit code 已确认为 0（`/tmp/agent-ml-exit/`）。

### 仍在运行的实验（11 个，全部由 ps 确认存活）

**旧批次（output 重定向到 ~/runs/ log，tmux pane 显示空白）：**

| exp_id | GPU | 进度 | 当前 task |
|--------|-----|------|-----------|
| eval-obs-only-object-norm02-k5-seed44 | cuda:2 | **7/10** | milk |
| eval-obs-only-object-norm01-seed45-r2 | cuda:1 | 3/10 | bbq_sauce |
| eval-obs-only-object-default-seed45-r2 | cuda:3 | 3/10 | bbq_sauce |
| eval-perdof-object-norm03-seed43 | cuda:5 | 2/10 | cream_cheese |
| eval-perdof-object-norm005-seed45 | cuda:0 | 1/10 | cream_cheese |

**新批次（00:31 启动，双跑部署）：**

| exp_id | GPU | 进度 | 当前 task |
|--------|-----|------|-----------|
| eval-random-selection-object-seed45 | cuda:0 | 1/10 | cream_cheese |
| eval-perdof-object-norm003-seed46 | cuda:1 | 1/10 | cream_cheese |
| eval-obs-only-object-norm02-k5-seed45 | cuda:2 | 2/10 | salad_dressing |
| eval-obs-only-object-default-seed48 | cuda:3 | 1/10 | cream_cheese |
| eval-perdof-object-default-seed47 | cuda:4 | 1/10 | cream_cheese |
| eval-perdof-object-norm03-seed47 | cuda:5 | 1/10 | cream_cheese |

### GPU 状态

| GPU | Util | VRAM | 进程数 | 备注 |
|-----|------|------|--------|------|
| 0 | 99% | 10361/24564 MiB | 2 | perdof-norm005-seed45 + random-selection-seed45 |
| 1 | 99% | 9465/24564 MiB | 2 | obs-only-norm01-seed45-r2 + perdof-norm003-seed46 |
| 2 | 99% | 7142/24564 MiB | 2 | obs-only-norm02-k5-seed44 + obs-only-norm02-k5-seed45 |
| 3 | 99% | 9465/24564 MiB | 2 | obs-only-default-seed45-r2 + obs-only-default-seed48 |
| 4 | 18% | 5201/24564 MiB | 1 | perdof-default-seed47（仅单进程） |
| 5 | 99% | 9932/24564 MiB | 2 | perdof-norm03-seed43 + perdof-norm03-seed47 |

**空闲 GPU：无。** 所有 6 块 GPU 均被占用。GPU 4 利用率低是因为只有 1 个进程（其余都是双跑）。

### 关键发现

- **3 个实验已完成但未 harvest**（1 个 RUNNING + 2 个 DEPLOYED）
- 旧批次 5 个实验的 tmux pane 显示空白是因为 output 被重定向到 `~/runs/` log 文件，进程实际在跑，不是 crash
- `eval-obs-only-object-norm02-k5-seed44` 进度最快（7/10），预计最先完成
- GPU 4 可以再加一个实验（目前只跑了 perdof-default-seed47）

---
