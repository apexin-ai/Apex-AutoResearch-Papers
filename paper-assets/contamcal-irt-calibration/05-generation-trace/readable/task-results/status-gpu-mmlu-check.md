# status gpu mmlu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_gpu_mmlu_check_20260514T023208_result.json`
- **Structured JSON:** [`0004263497416db14fdb.json`](../../sessions/00/0004263497416db14fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是结构化报告。

---

## 服务器状态报告 — cqa1-21977（2026-05-14 ~10:32 UTC）

### 1. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX 4090 D | 10,055 / 24,564 MiB (41%) | 22% |
| cuda:1 | RTX 4090 D | 12,620 / 24,564 MiB (51%) | 100% |
| **cuda:2** | RTX 4090 D | **21,983 / 24,564 MiB (90%)** | **100%** |
| cuda:3 | RTX 4090 D | 8,957 / 24,564 MiB (36%) | 60% |
| cuda:4 | RTX 4090 D | 5,829 / 24,564 MiB (24%) | 49% |
| cuda:5 | RTX 4090 D | 5,829 / 24,564 MiB (24%) | 45% |

### 2. 进程状态

| PID | 任务 | 状态 | 运行时长 | 备注 |
|-----|------|------|---------|------|
| 251924 | cuda:0, 1.5B d100 SFT | **ALIVE** (Sl) | 1h23m | 训练中 |
| 249294 | cuda:1, 3B d000_s42 eval | **ALIVE** (Rl+) | 1h38m | 评估中 |
| 255322 | cuda:1, 0.5B d005_s42 eval | **ALIVE** (Rl) | 1h04m | 评估中 |
| 242581 | cuda:3, 3B d000_s123 eval | **ALIVE** (Ss+) | 2h14m | 评估中 |
| 243290 | cuda:4, 1.5B d000_s42 eval | **ALIVE** (Ss+) | 2h09m | 评估中 |
| 250600 | cuda:5, 1.5B d000_s123 eval | **ALIVE** (Ss+) | 1h33m | 评估中 |
| 263528 | cuda:2, 0.5B d000_s42 eval v2 | **ALIVE** (Ss+) | 4m | 刚启动 |
| 263784 | cuda:2, 0.5B d100 eval v2 | **ALIVE** (Ss+) | 4m | 刚启动 |

**全部 8 个进程均存活。**

### 3. 重点关注

#### cuda:1 双占情况
- 两个 eval 进程都在跑（PID 249294 和 255322），显存占 12,620 MiB (51%)，利用率 100%
- 3B 模型和 0.5B 模型共享一块卡，显存够用但 GPU 利用率打满

#### cuda:2 实际状态（PREPARING → 已确认在跑）
- PID 263528（0.5B d000_s42 v2）和 PID 263784（0.5B d100 v2）**都已真正在运行**，不再是 PREPARING
- 两个都刚启动约 4 分钟，当前都在跑 MMLU 评估
- PID 263528 (d000_s42): MMLU 进度 ~GSM8K 阶段（MMLU 已完成，acc=0.4049），正在跑 GSM8K
- PID 263784 (d100): MMLU 进度 ~GSM8K 阶段（MMLU 已完成，acc=0.2322），正在跑 GSM8K
- 显存占用 21,983 MiB (90%)，利用率 100%——**两个 0.5B eval 挤在一张卡上，显存接近满载**

> **注意**: d100 的 MMLU acc 只有 0.2322，远低于 d000 的 0.4049，下降明显。

### 4. MMLU Paraphrase
- **无 `mmlu_paraphrases*.json` 文件**
- **无 vLLM/paraphrase 相关进程**
- 状态：**未生成或已清理**

### 5. SFT 数据文件

| 文件 | 行数 |
|------|------|
| sft_dosage_000.jsonl | 50,000 |
| sft_dosage_005.jsonl | 50,826 |
| sft_dosage_025.jsonl | 54,133 |
| sft_dosage_050.jsonl | 58,266 |
| sft_dosage_100.jsonl | 66,533 |

### 6. Eval 结果产出

| 目录 | 状态 |
|------|------|
| Qwen2.5-0.5B_d000_s123 | **已完成** |
| Qwen2.5-0.5B_d000_s42 | 空（eval 正在 cuda:2 跑 v2） |
| Qwen2.5-0.5B_d000_s42_para | 空 |
| Qwen2.5-0.5B_d005_s42 | 空（eval 正在 cuda:1 跑） |
| Qwen2.5-0.5B_d100_s42 | 空（eval 正在 cuda:2 跑 v2） |
| Qwen2.5-1.5B_d000_s42 | 空（eval 正在 cuda:4 跑） |
| Qwen2.5-1.5B_d000_s123 | 空（eval 正在 cuda:5 跑） |
| Qwen2.5-3B_d000_s42 | 空（eval 正在 cuda:1 跑） |
| Qwen2.5-3B_d000_s123 | 空（eval 正在 cuda:3 跑） |

**唯一已完成的 eval 分数（0.5B d000_s123）：**
- MMLU: **0.4182** (5873/14042)
- GSM8K: **0.3404**
- ARC-Challenge: **0.3976**
- HumanEval: **0.1037** (pass@1)

### 7. SFT 训练进度（PID 251924, 1.5B d100）

- 进度: **1503/4159 (36%)**，已跑 1h23m
- 速度: ~3.9-4.1 s/it
- ETA: ~2h53m 剩余
- loss=1.31, token_accuracy=0.70, epoch=0.29

---
