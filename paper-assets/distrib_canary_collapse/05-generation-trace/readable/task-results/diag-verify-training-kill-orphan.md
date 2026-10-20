# diag verify training kill orphan

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_verify_training_kill_orphan_20260518T222058_result.json`
- **Structured JSON:** [`39e53b94d36baddee1c6.json`](../../sessions/39/39e53b94d36baddee1c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 四个新实验状态

| Session | 状态 | 当前进度 |
|---------|------|----------|
| `qwen35_08b_fp32` | 运行中 | 生成阶段（输出 padding_side 警告，GPU 0 利用率 99%） |
| `a060_s42_fp32` | 运行中 | Featurizing q: 37% (p 已完成) |
| `a005_s42_fp32` | 运行中 | Featurizing q: 5% (p 已完成) |
| `interv_pred_fp32` | 运行中 | Featurizing p: 65% |

四个实验均在正常运行，未出现启动后退出的情况。

### 2. 孤儿进程

PID 44889 (OPT-1.3B, seed 43) 已 kill。GPU 5 显存从 28480 MiB 降至 9719 MiB，释放约 **18.7 GiB**。现在 GPU 5 上只剩 alpha_sweep_a010_s43 (PID 45289)。

### 3. GPU 全局状态

| GPU | 显存占用 | 总显存 | 利用率 | 备注 |
|-----|---------|--------|--------|------|
| 0 | 70761 MiB | 97887 MiB | 99% | qwen35_08b_fp32 |
| 1 | 2885 MiB | 97887 MiB | 40% | 新实验（featurizing 阶段） |
| 2 | 7083 MiB | 97887 MiB | 0% | 新实验（featurizing，CPU 密集） |
| 3 | 7083 MiB | 97887 MiB | 0% | 新实验（featurizing，CPU 密集） |
| 4 | 7083 MiB | 97887 MiB | 91% | 新实验 |
| 5 | 9719 MiB | 97887 MiB | 39% | alpha_sweep_a010_s43（孤儿已清除） |

6 张 GPU 均有进程。GPU 2/3 利用率暂时 0% 是因为 featurizing 阶段主要吃 CPU，进入训练后会上去。

---
