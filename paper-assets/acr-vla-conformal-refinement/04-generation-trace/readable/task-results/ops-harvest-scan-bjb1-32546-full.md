# ops harvest scan bjb1 32546 full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-scan-bjb1-32546-full_20260519T013025_result.json`
- **Structured JSON:** [`55763b90883b99078de2.json`](../../sessions/55/55763b90883b99078de2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 扫描报告

### GPU 状态

| GPU | Util% | VRAM Used/Total | 实验 1 | 实验 2 | 空闲 slot |
|-----|-------|-----------------|--------|--------|-----------|
| 0 | 83% | 7608/24564 MiB | perdof-norm005-seed46 (9h) | obs-only-norm003-seed44 (6h) | - |
| 1 | 99% | 4814/24564 MiB | perdof-norm005-seed43 (12h) | obs-only-default-seed47 (9h) | - |
| 2 | 99% | 4814/24564 MiB | perdof-norm003-seed43 (12h) | perdof-norm03-seed46 (9h) | - |
| 3 | 99% | 8537/24564 MiB | perdof-norm01-seed48 (6h) | perdof-norm003-seed48 (6h) | - |
| 4 | 21% | 2876/24564 MiB | scalar-seed46 (9h) | — | **~21 GiB 空闲** |
| 5 | 99% | 7608/24564 MiB | obs-only-norm01-seed47 (9h) | obs-only-norm003-seed46 (6h) | - |

**6 GPU 全部在用，11 个实验并行运行。GPU 4 只跑了 1 个实验，有空闲 slot。**

### 最近完成但可能未收割的实验

| 文件 | 完成时间 | SR |
|------|----------|-----|
| eval_object_obs_only_norm005_seed45.json | May 18 22:11 | **14%** |
| eval_object_perdof_norm01_seed43.json | May 18 22:32 | **12%** |
| eval_object_perdof_default_seed45.json | May 19 08:56 | **0%** |

### 超时实验 (exit code 124)

| 实验 | 超时时间 | 是否已重试 |
|------|----------|-----------|
| eval-obs-only-object-norm003-seed44 | May 18 21:16 | 已重试 → eval-obs-only-norm003-seed44-t16 |
| eval-obs-only-object-norm003-seed45 | May 18 21:16 | **未重试** |
| eval-perdof-object-norm003-seed45 | May 18 21:16 | **未重试** |

### 已死 tmux session

**无。** 所有 11 个 tmux session 均有存活进程。其中 `eval-perdof-object-norm003-seed43` 和 `eval-perdof-object-norm005-seed43` 的 tmux pane 显示空白（输出重定向到日志文件），但对应 python 进程仍以 137%+ CPU 运行。

### Orphan 进程

无。所有 evaluate.py 进程都关联到 tmux session。

### 建议动作

1. 收割 3 个已完成实验结果（obs-only-norm005-seed45 SR=14%, perdof-norm01-seed43 SR=12%, perdof-default-seed45 SR=0%）
2. GPU 4 有大量空闲 VRAM，可加塞实验
3. 2 个超时实验（norm003-seed45 的 obs-only 和 perdof）未重试，需决定是否补跑

---
