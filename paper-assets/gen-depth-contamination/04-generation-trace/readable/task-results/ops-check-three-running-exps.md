# ops check three running exps

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-three-running-exps_20260519T091702_result.json`
- **Structured JSON:** [`bac5178396b18104268d.json`](../../sessions/ba/bac5178396b18104268d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. exp_code_mistral7b (cqa1-22115, cuda:3, PID 107037)

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE, 14514 MiB GPU |
| **已完成** | depth_0~4 (各 5500 行) |
| **当前** | 正在生成 depth_5 |
| **进度** | 5/6 depths 完成 = 83%, depth_5 文件尚未落盘 |

各 depth 完成时间：
- depth_0: 07:06 UTC
- depth_1: 09:59 UTC (+2h53m, 含模型加载)
- depth_2: 12:09 UTC (+2h10m)
- depth_3: 14:19 UTC (+2h10m)
- depth_4: 16:30 UTC (+2h11m)

每 depth 生成约 2h10m, depth_5 于 ~16:30 开始 → **生成完成 ETA ~18:40 UTC**, 加上分析步骤 → **全流程 ETA ~19:00-19:30 UTC**

---

### 2. exp_code_qwen7b (cqa1-22115, cuda:1, PID 114228)

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE, 15088 MiB GPU |
| **已完成** | depth_0~3 (各 5500 行) |
| **当前** | depth_4: **1050/1375 (76.4%)** |
| **速率** | ~5.51 s/it |

剩余时间估算：
- depth_4 剩余: 325 batches × 5.51s ≈ **30 min**
- depth_5 全量: 1375 batches × 5.51s ≈ **2h06m**
- 分析步骤: ~30-60 min

**全流程 ETA ~20:00-20:30 UTC** (比预计的 18:00 晚约 2h)

---

### 3. exp_32b_c4 (westd-42896, cuda:1, PID 44720)

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE, 64766 MiB GPU (PID 变为 44720, 非原 44715) |
| **已完成** | depth_0~3 (各 5000 行) + seed_docs.jsonl |
| **当前** | depth_4: **1874/2500 (75.0%)** |
| **速率** | ~14 s/it |

剩余时间估算：
- depth_4 剩余: 626 batches × 14s ≈ **2.4h**
- depth_5 全量: 2500 batches × 14s ≈ **9.7h**
- 分析步骤: ~1h

**全流程 ETA ~May 20 05:00-06:00 UTC**

---

### 总结

| 实验 | 进程 | 当前位置 | 预计完成 |
|------|------|---------|---------|
| exp_code_mistral7b | ALIVE | depth_5 生成中 | ~19:00 UTC 今天 |
| exp_code_qwen7b | ALIVE | depth_4 76% | ~20:00-20:30 UTC 今天 |
| exp_32b_c4 | ALIVE | depth_4 75% | ~May 20 05:00 UTC |

注意：exp_32b_c4 的 PID 从 44715 变为 44720，可能是进程重启过。mistral 实验没有 log 文件，但进程在跑且数据文件在正常产出。

---
