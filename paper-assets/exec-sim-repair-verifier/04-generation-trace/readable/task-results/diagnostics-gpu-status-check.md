# diagnostics gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostics_gpu-status-check_20260519T131204_result.json`
- **Structured JSON:** [`5cc4c5acb045ce8f271d.json`](../../sessions/5c/5cc4c5acb045ce8f271d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报 — seetacloud-westd-4x5090

### GPU 总览 (21:12:22)

| GPU | VRAM | Util | 温度 | PID | 状态 |
|-----|------|------|------|-----|------|
| 0 | 27714/32607 MiB | 90% | 68°C | 778334 | **运行中** — Qwen3-8B CWM eval |
| 1 | 17263/32607 MiB | 63% | 61°C | 836311 | **运行中** — 进程活跃（CLS chain 已完成） |
| 2 | 26083/32607 MiB | 84% | 60°C | 833672 | **运行中** — DeepSeek CWM s42 seq4096 eval |
| 3 | 0/32607 MiB | 0% | 31°C | — | **空闲** |

---

### GPU 0 — Qwen3-8B CWM eval (D146)

- **进度**: 6504 / 9784 = **66.5%**
- **Running acc**: 63.9%
- **速度**: ~8.4 samples/min（每 8 samples 约 57 秒）
- **剩余**: 3280 samples → **预计 ~6.5 小时** → ETA **~03:40 May 20**

---

### GPU 1 — CLS ablation chain

**全部 3 个 checkpoint eval 已完成。** Chain log 输出 `[chain] All CLS ablation evals done.` (21:02:01)

结果目录均已生成：`cls8b_s42_ckpt{2200,3600,6633}_test/`

| Checkpoint | Accuracy | F1 macro | F1 fail | F1 pass | P_fail | R_fail |
|-----------|----------|----------|---------|---------|--------|--------|
| **ckpt-2200** | **85.34%** | **79.04%** | **67.56%** | 90.53% | 84.16% | **56.42%** |
| ckpt-3600 | 84.48% | 78.17% | 66.43% | 89.91% | 80.06% | 56.76% |
| ckpt-6633 | 85.29% | 78.44% | 66.28% | 90.60% | **87.23%** | 53.44% |

**观察**: ckpt-2200 是综合最优（accuracy+F1 macro 均最高）。ckpt-6633 的 precision_fail 最高（87.2%）但 recall_fail 最低（53.4%），说明训练越久越保守。ckpt-3600 全面不如两端。

GPU 1 仍有活跃进程（PID 836311, 17GB VRAM, 63% util），chain 已结束但进程未退出，可能是 tmux 中残留的 Python 进程。

---

### GPU 2 — DeepSeek CWM s42 seq4096 eval

- **状态**: **已启动并运行中**（之前标记为 PREPARING 的实验已跑起来）
- **进度**: 420 / 9784 = **4.3%**
- **Running acc**: 59.0%
- **速度**: ~12.5 samples/min
- **剩余**: 9364 samples → **预计 ~12.5 小时** → ETA **~09:40 May 20**
- 增量结果写入 `deepseek_cwm_repo_s42_seq4096/results_incremental.jsonl`（420 行）

---

### GPU 3 — 空闲 ✓

0 MiB VRAM，0% util，无进程。已确认空闲。

---

### 磁盘状态

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/root/autodl-tmp` | 250G | 196G | 55G | **79%** |
| `/` (根) | 30G | 20G | 11G | **67%** |

### 数据文件 (`data/swebench_full/`)

总大小 ~145M，16 个文件，43491 行总计。关键文件：

| 文件 | 大小 | 行数 |
|------|------|------|
| swebench_test.jsonl | 58M | 9784 |
| swebench_pilot_data.jsonl | 32M | 7349 |
| swebench_train.jsonl | 25M | 4359 |
| swebench_val.jsonl | 22M | 3107 |
| swebench_verified_meta.jsonl | 6.3M | 500 |

`test.jsonl`/`train.jsonl`/`val.jsonl` 是符号链接指向对应的 `swebench_*.jsonl`，文件完整无异常。

---
