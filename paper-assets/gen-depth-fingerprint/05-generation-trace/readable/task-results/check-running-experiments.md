# check running experiments

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running-experiments_20260515T183313_result.json`
- **Structured JSON:** [`e0284007b17716fb34e2.json`](../../sessions/e0/e0284007b17716fb34e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. plan-010-human-edit (cuda:1)

| 进程 | 状态 | 运行时间 |
|------|------|---------|
| PID 223500 (`human_edit_robustness.py --device cuda:1`) | **RUNNING** (State: R, 258 threads) | 2h30m |
| PID 228872 (`wait_and_rerun.sh`) | RUNNING，当前子进程 `sleep 30` | 1h23m |

**进度**: Phase 4 LOGO evaluation，正在跑 `random_20pct` 条件。已完成的部分结果：

| 条件 | 3-class LOGO F1 | Binary LOGO F1 |
|------|----------------|----------------|
| baseline | **0.7889** [0.7867, 0.7979] | **0.7241** [0.7187, 0.7343] |
| random_5pct | 0.7538 [0.7496, 0.7641] | 0.7182 [0.7125, 0.7285] |
| random_10pct | 0.7425 [0.7349, 0.7517] | 0.7168 [0.7114, 0.7286] |
| random_20pct | 进行中... | — |
| llm_rephrase | 待评估 | — |

结果文件尚未写出。Log 在 `/tmp/human_edit_robustness.log`（306 行）。GPU 1 显示 0% 利用率，可能在 LOGO 交叉验证的 CPU 阶段。

### 2. review-sampling-ablation

| 进程 | 状态 | 运行时间 | 进度 |
|------|------|---------|------|
| PID 222783 (`sampling_ablation.py --device cuda:3 --phase all`) | **RUNNING** | 2h32m | 无 log 文件，无法判断进度 |
| PID 226113 (`run_high_only.py`, cuda:2) | **RUNNING** | 1h45m | **52% (516/996)** `high_t10_p095` |

cuda:2 实验速度 ~0.08 seeds/s（~12-14s/it），偶有 empty output 警告。预计还需 **~1h50m**。tmux session `high_temp` 存活。

### 3. GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 89% | 18.6 / 32.6 GB |
| 1 | 0% | 0.6 / 32.6 GB |
| 2 | 38% | 3.9 / 32.6 GB |
| 3 | 40% | 3.9 / 32.6 GB |

GPU 0 被其他任务占用。GPU 1 利用率为 0 但 human_edit 进程活着（可能在 CPU-bound 的分类器训练阶段）。

---
