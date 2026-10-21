# diagnose gpu status all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-status-all-servers_20260521T161713_result.json`
- **Structured JSON:** [`206d554a52543ec17ea5.json`](../../sessions/20/206d554a52543ec17ea5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器 GPU 实际状态汇总（2026-05-21 ~23:40）

### 总结
- **17 个物理 GPU 中 14 个在跑 precompute**，**bjb1-18228 上 3 个 GPU 空闲**（ROADMAP "17/17 GPU 满载" 的说法不准确）
- 所有运行进程都是 `python -u src/train_crm.py --model pi05 --precompute`，与 ROADMAP 描述一致
- Registry 显示 0 RUNNING 是**追踪漏记**，不是实际未运行——进程是直接 python 启动的，未通过 `submit_training_job`（无 tmux session）
- 整体已跑 1.5–3.4 小时，多数 shard 已到 3500–4000 之间，object 几乎收尾

### 各服务器状态表

| 服务器 | GPU 数 | 在用 GPU | 状态 | 任务 |
|---|---|---|---|---|
| **bjb1-32546** | 6 | 6/6（3 张双载） | 99% / 25% util | pi05 **object** shards 1–9（共 10 shards，9 个进程） |
| **bjb2-28827** | 6 | 6/6 | 20–66% util | pi05 **spatial** shards 0–5（共 7 shards） |
| **bjb1-18228** | 4 | **1/4** ⚠️ | GPU3 24%, GPU0/1/2 **空闲** | pi05 **spatial** shard 6 |
| **bjb2-40593** | 1 | 1/1 | 14% util | pi05 **object+spatial** shard 0/10 |

### 进程映射详情

**bjb1-32546** (9 进程 / 6 GPU，部分 GPU 双开):
| PID | shard | 进程显存 |
|---|---|---|
| 175531 | object s5 | 9874 MiB |
| 178365 | object s1 | 9874 MiB |
| 178514 | object s2 | 9874 MiB |
| 175827 | object s6 | 9874 MiB |
| 178661 | object s7 | 9874 MiB |
| 176106 | object s3 | 9874 MiB |
| 178940 | object s8 | 9874 MiB |
| 176451 | object s4 | 9874 MiB |
| 182292 | object s9 | 9874 MiB |

**bjb2-28827** (PID → shard): 100400=s0, 100547=s1, 100889=s2, 101236=s3, 101575=s4, 101854=s5
**bjb1-18228**: PID 781280 → spatial s6（其他 3 GPU 完全闲置，0 MiB 显存）
**bjb2-40593**: PID 872656 → `--benchmark object spatial --shard_id 0 --num_shards 10`（注意 num_shards 与其他不一致，只有该机用 10）

### 进度估算（按 cache 文件时间戳）

| 数据集 | 各 shard 当前进度 | cache 大小 |
|---|---|---|
| object (10 shards 总) | s1–s4 到 3000–3500，s5–s9 到 3900–4000，s0 到 4100–4200 | bjb1-32546: 299M / bjb2-40593: 48M |
| spatial (7 shards 总) | s0–s5 到 3500–4000，s6 到 4000–4500 | bjb2-28827: 209M / bjb1-18228: 41M |

### 启动时间（运行时长，2026-05-21 当前 ~23:40）
- bjb2-40593: 20:16（最早，~3.4h）
- bjb2-28827: 21:45（~1.9h）
- bjb1-18228: 21:46（~1.9h）
- bjb1-32546: 22:05–23:04（~0.6–1.6h，进程时间不一，可能中途重启过几个 shard）

### 关键结论
1. **precompute 在跑，没完成**。Object 各 shard 已接近 4000，spatial 已到 3500–4500，估计再 1–2 小时可全部跑完
2. **bjb1-18228 的 3 张 GPU 是浪费的**。可以加 3 个进程处理剩余的 object shard 0 或加速其它工作
3. **registry 与实际状态完全脱节**——进程是手动 python 启动而非 submit_training_job，所以 registry 没记录。需要重新对账
4. logs 目录里没有 precompute 日志文件，输出可能直接到 stdout/tmux 或丢失了

---
