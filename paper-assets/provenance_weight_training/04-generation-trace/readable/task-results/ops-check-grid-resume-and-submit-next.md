# ops check grid resume and submit next

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_grid_resume_and_submit_next_20260515T082948_result.json`
- **Structured JSON:** [`61a87964fafb114c56c1.json`](../../sessions/61/61a87964fafb114c56c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | Memory | Util | 进程 PID | 实验 | 运行时间 | 进度 | 状态 |
|-----|--------|------|----------|------|----------|------|------|
| cuda:0 | 46523 MiB | 98% | 183166 | grid_b2_0_seed456 | 49m | 4888/6103 (80%) | 训练中 |
| cuda:1 | 75007 MiB | 77% | 163662 | grid_b_low_seed42 | 7h09m | 7879/8477 (93%) | 训练中 |
| cuda:2 | 46523 MiB | 98% | 183245 | grid_b5_0_seed456 | 49m | 4388/6103 (72%) | 训练中 |
| cuda:3 | 46523 MiB | 98% | 183451 | grid_b3_0_seed456 | 49m | 4385/6103 (72%) | 训练中 |

## 实验进度

| 实验 | 进度 | ETA | final/ |
|------|------|-----|--------|
| grid_b2_0_seed456 | 80% (4888/6103) | ~43min | 无 |
| grid_b3_0_seed456 | 72% (4385/6103) | ~61min | 无 |
| grid_b5_0_seed456 | 72% (4388/6103) | ~61min | 无 |
| grid_b_low_seed42 | 93% (7879/8477) | ~3min | 无 |

所有 4 个实验都还在跑，grid_b_low_seed42 最先完成（~3min），三个 grid resume 实验预计 43-61min 后完成。

## 下一步就绪检查

| GPU | 下一实验 | 脚本 | 状态 |
|-----|----------|------|------|
| cuda:0 | ess_only_seed42 | run_ess_only_seed42.sh | **存在** |
| cuda:1 | (b_low 即将完成，可复用) | — | — |
| cuda:2 | golden_ratio_seed42 | run_golden_ratio_seed42.sh | **存在** |
| cuda:3 | nmin1_seed42 | run_nmin1_seed42.sh | **已创建** |

三个下一批脚本均已就绪。grid_b_low_seed42 约 3 分钟内完成，cuda:1 将最先空出。三个 grid seed456 实验约 1 小时后完成，届时 cuda:0/2/3 可提交 ess_only / golden_ratio / nmin1。

---
