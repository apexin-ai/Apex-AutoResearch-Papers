# diag westd experiments

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd_experiments_20260517T231718_result.json`
- **Structured JSON:** [`a60907e1c55e7ddec2d6.json`](../../sessions/a6/a60907e1c55e7ddec2d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 任务 1: eval_math500_grpo_unpruned (PID 64467)

| 项目 | 状态 |
|------|------|
| 进程 | **存活**，运行 8 分 23 秒 |
| GPU | cuda:2，PID 64472 占用 17658 MiB |
| 进度 | 模型加载完成，正在评估 MATH500。日志显示 55/500 样本，~85s/sample |
| 结果文件 | 尚未生成（正常，评估未完成） |
| tmux | `eval_math500_grpo_unpruned` session 存在 |

**结论**：正常运行中，PREPARING 状态是 cron 系统尚未检测到进度更新。预计总耗时 ~12 小时。

---

### 任务 2: eval_postprune_cka_only_30 (PID 59403)

| 项目 | 状态 |
|------|------|
| 进程 | **存活**，运行 1 小时 18 分 |
| GPU | cuda:2，PID 59408 占用 11538 MiB |
| 进度 | 50/200 样本完成，**acc=0.0000**，eos_rate=4%，avg_len=4024 |
| 结果文件 | 尚未生成 |

**结论**：进程正常运行中，report 标 failed 可能是误判。但 **acc=0.0000 且 eos_rate 仅 4%** 说明模型生成几乎全是 max_length 截断、无法正确作答。这是 pruned_cka_only_30 模型本身质量问题，不是脚本 bug。

---

### 任务 3: westd-11672 GPU 全览

| GPU | 显存占用 | 利用率 | 进程 |
|-----|----------|--------|------|
| cuda:0 | 41198/97887 MiB | 97% | PID 47672 (eval_postprune_standard_30) + PID 49480 (eval_sft_cka_only_20_n1319) |
| cuda:1 | 34569/97887 MiB | 98% | PID 14556 (eval_math500_grpo_standard_20) |
| cuda:2 | 29210/97887 MiB | 94% | PID 59408 (eval_postprune_cka_only_30) + PID 64472 (eval_math500_grpo_unpruned) |
| cuda:3 | 32517/97887 MiB | 99% | PID 31706 (eval_math500_grpo_rasp_20_v3) |

**4 张 GPU 全部满载运行中**，共 6 个评估实验并发。注意 cuda:2 上跑了两个任务，可能互相影响速度。

---
