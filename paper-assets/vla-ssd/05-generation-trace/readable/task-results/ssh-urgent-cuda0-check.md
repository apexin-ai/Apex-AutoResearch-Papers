# ssh urgent cuda0 check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_cuda0_check_20260522T031739_result.json`
- **Structured JSON:** [`b45b9a693b4aa307fb64.json`](../../sessions/b4/b45b9a693b4aa307fb64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

---

### 1. openvla_spatial — 仍在下载，pipeline 未启动

| 项目 | 状态 |
|------|------|
| 目标路径 | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-spatial/` |
| 模型总大小 | **15.1 GB** (4 shards) |
| 当前已下载 | **~9.6 GB** (shard 3 完整 4.7G, shard 4 完整 251M, shard 1+2 下载中) |
| 日志最新 | `[11:17:40] Still waiting... (7.6G downloaded)` |
| 下载耗时 | 09:37 开始，已 1h40m，速度波动大 |
| 预估进度 | ~50-60%，剩余 ~5.5 GB，按当前速度还需 1-2h |
| GPU 0 | **空闲**，等待下载完成后启动 pipeline |

下载速度非常不稳定（8.5G → 5.1G → 7.6G 反复波动），可能是 HF 下载器在轮替写入 shard 1 和 shard 2 的临时文件。

---

### 2. openvla_goal — Phase 1 运行中，~70% 完成

| 阶段 | 条件 | 状态 |
|------|------|------|
| **TRAINED** (08:33-10:22) | wrong, empty, shuffled, paraphrased | 全部完成 |
| **UNTRAINED** (10:22-) | wrong | 完成 (11:05) |
| | **empty** | **进行中 2800/5000** |
| | shuffled | 待运行 |
| | paraphrased | 待运行 |

每个 condition ~20min，empty 还剩 ~10min，shuffled + paraphrased ~40min。**预计 ~12:10 左右完成 Phase 1**。

---

### 3. GPU 占用

| GPU | 型号 | 利用率 | 显存 | 进程 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell (96GB) | **0%** | 0 MiB | 无（等 spatial 下载） |
| 1 | RTX PRO 6000 Blackwell (96GB) | **90%** | 15.3 / 97.9 GB | PID 591235 (goal 实验) |

---
