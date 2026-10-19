# ops disk cleanup m1 check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-m1-check_20260513T013350_result.json`
- **Structured JSON:** [`56d6c390f40f0678f33a.json`](../../sessions/56/56d6c390f40f0678f33a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。

---

## 1. 磁盘清理

| 指标 | 清理前 | 清理后 | 变化 |
|------|--------|--------|------|
| 已用 | 155G (92%) | 142G (84%) | **-13G** |
| 可用 | 15G | 28G | **+13G** |

清理项：`._____temp/`、`Qwen3-14B-AWQ/`、`.ms_cache/`

---

## 2. M1 提取进度

**进程 577864 仍在运行**，已运行 ~4h46m。

截至最新日志（09:34），**21 个 repo 已开始提取**，进度如下：

| Repo | 进度 | 状态 |
|------|------|------|
| seatgeek/thefuzz | 完成 | 文件已在输出目录 |
| pytest-dev/iniconfig | 50/63 | 接近完成 |
| luozhouyang/python-string-similarity | 50/59 | 接近完成 |
| jd/tenacity | 150/152 | 接近完成 |
| pudo/dataset | 100/107 | 接近完成 |
| Suor/funcy | 300/306 | 接近完成 |
| cknd/stackprinter | 100/137 | |
| agronholm/exceptiongroup | 100/139 | |
| agronholm/typeguard | 300/333 | 接近完成 |
| jaraco/inflect | 100/133 | |
| bottlepy/bottle | 350/373 | 接近完成 |
| joke2k/faker | 150/360 | |
| PyCQA/flake8 | 450/454 | 接近完成 |
| Cog-Creators/Red-DiscordBot | 450/460 | 接近完成 |
| marshmallow-code/webargs | 50/321 | |
| pyupio/safety | 300/759 | |
| mahmoud/boltons | 450/737 | |
| oauthlib/oauthlib | 700/940 | |
| pygments/pygments | 450/1430 | |
| cantools/cantools | 350/1440 | |
| keleshev/schema | 在处理中（CodeQL 日志可见） |

当前提取输出占 **2.2GB**，skip_log 有 **660 条**（主要是 pdfminer 等 clone 失败的）。

---

## 3. m1_training_data 来源分析

**位置**：`/root/autodl-tmp/structfuse/m1_training_data/`（不是 `/root/structfuse/data/`）

**文件数量确认**：
- train_dataflow.jsonl: **1086 行** (93.9MB)
- train_embedding.jsonl: **1086 行** (104.5MB)
- train_random.jsonl: **1086 行** (86.9MB)
- val.jsonl: **272 行** (22.1MB)

**生成时间**：2026-05-13 **05:12:46**（创建）→ 05:17（写完）

**生成脚本**：`/root/structfuse/scripts/build_m1_training_data.py`，参数为 `--extraction-dir`、`--repos-dir`、`--output-dir`、`--embedding-mining-mode static`

**基于 10 个 repo 的数据**（不是全量 131 个）：
1. Cog-Creators/Red-DiscordBot
2. Suor/funcy
3. agronholm/typeguard
4. cknd/stackprinter
5. jd/tenacity
6. oauthlib/oauthlib
7. pudo/dataset
8. pygments/pygments
9. pytest-dev/iniconfig
10. seatgeek/thefuzz

**时间线推断**：提取进程 ~04:48 启动，05:01-05:07 这 10 个 repo 陆续产出了第一批（50条）结果。训练数据在 **05:12** 生成，抓取的是当时已有的**早期/部分提取结果**。这就是为什么只有 10 个 repo — 它不是基于全量数据，而是提取刚开始 ~25 分钟时的快照。

---
