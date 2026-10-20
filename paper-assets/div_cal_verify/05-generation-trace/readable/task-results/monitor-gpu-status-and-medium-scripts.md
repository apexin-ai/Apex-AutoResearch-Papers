# monitor gpu status and medium scripts

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu_status_and_medium_scripts_20260513T192554_result.json`
- **Structured JSON:** [`dcc1cb2ab93bc7dd49b8.json`](../../sessions/dc/dcc1cb2ab93bc7dd49b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. 进程状态

| GPU | 进程 | 模型 | 方法 | 当前进度 | 启动时间 | 预估剩余 |
|-----|------|------|------|----------|----------|----------|
| **GPU 0** (22.4GB/97.9GB) | medium_uncurated seed42 | gpt2-medium | uncurated | **Gen 0/7, step 3/5 (training)** | 03:01 | ~3-4h（medium 每代约 25-30min） |
| **GPU 1** (21.7GB/97.9GB) | ext_seed456 | gpt2 (small) | external_only | **Gen 0/7, step 3/5 (training)** | 03:06 | ~1-1.5h（small 每代约 8-10min） |

GPU 1 上 ext_seed456 结束后会自动链式启动 `rgds_seed456`（同一 tmux session）。

### 2. 已完成实验

**uncurated_seed456** (gpt2, seed=456) — 已完成:

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|-----|--------|-----|------|------|
| 0 | 36.64 | 279.17 | 0.9880 | 0.0284 | -0.0205 |
| 7 | **44.69** | **287.93** | **0.9880** | **0.0086** | **-0.0696** |

**random50_seed123** (gpt2, seed=123) — 已完成:

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|-----|--------|-----|------|------|
| 0 | 36.46 | 272.72 | 0.9880 | 0.0293 | -0.0114 |
| 7 | **41.75** | **291.70** | **0.9880** | **0.0098** | **-0.0423** |

### 3. 创建的脚本

- `/root/div_cal_verify/run_medium_external.sh` — **新建**（external_only, gpt2-medium, seed=42, 50% Contriever selection）
- `run_medium_rgds.sh` / `run_medium_random50.sh` — **已存在**，无需创建

---
