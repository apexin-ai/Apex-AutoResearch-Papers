# ops westd parallel ood eval gpu123

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_parallel_ood_eval_gpu123_20260522T053758_result.json`
- **Structured JSON:** [`9ff948cfd829d6d0e352.json`](../../sessions/9f/9ff948cfd829d6d0e352.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部在跑，全部初始化成功。

| GPU | 显存占用 | 利用率 | Checkpoint | PID |
|-----|---------|--------|------------|-----|
| cuda:0 | 83347/97887 MiB | 37% | SFT baseline (batch_ood_eval.sh) | 原有 |
| cuda:1 | 83347/97887 MiB | 44% | seed4 step15 | 487752 |
| cuda:2 | 83347/97887 MiB | 29% | seed5 step10 | 489063 |
| cuda:3 | 83347/97887 MiB | 43% | seed6 step15 | 489064 |

3 个新 eval 均已加载模型、初始化 134 games 环境，正在运行。

**修复要点**：
1. `--gpu` 参数要传物理 GPU 编号（1/2/3），不能用外层 `CUDA_VISIBLE_DEVICES` + `--gpu 0`（脚本第 362 行会覆盖）
2. `nohup bash -c` 子 shell 需要在内部 `cd` 或用绝对路径
3. 用 `/root/miniconda3/bin/python` 全路径避免 conda 未激活问题

**第二轮分配**（当前 3 个完成后）：cuda:1→seed8_step5, cuda:2→intervention_c_step5, cuda:3→intervention_c_step7。

---
