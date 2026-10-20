# ops disk emergency 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_emergency_17855_20260521T192620_result.json`
- **Structured JSON:** [`06321012a429e3010929.json`](../../sessions/06/06321012a429e3010929.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. 磁盘状态

| | 容量 | 已用 | 可用 | 使用率 |
|---|---|---|---|---|
| **清理前** | 350G | 350G | 1.2M | 100% |
| **清理后** | 350G | 212G | **139G** | 61% |

**释放 ~138G**，分三步：
- phase_diagram 已完成实验 checkpoint: ~21G
- alpha_sweep 全部 checkpoint: ~103G
- phase_diagram 崩溃/运行实验旧 checkpoint: ~14G

所有 JSON 文件（all_metrics.json 等）完好未动。

### 2. GPU 进程状态

| GPU | 状态 | VRAM | 利用率 | PID |
|---|---|---|---|---|
| 0 | 空闲 | 0 MiB | 0% | — |
| 1 | **运行中** | 14,535 MiB | 77% | 546624 |
| 2 | **运行中** | 7,453 MiB | 71% | 550489 |
| **3** | **空闲** | 0 MiB | 0% | — |
| 4 | 空闲 | 0 MiB | 0% | — |
| 5 | **运行中** | 14,237 MiB | 95% | 519277 |

### 3. 实验存活状态

**仍在运行（磁盘清理后恢复写入）：**
- **t25_a045_s42_fp32** — gen_12/13 在 03:28 更新，正在推进（~gen_14/25）
- **t15_a060_s43_fp32** — gen_1 在 03:28 更新，正在推进（~gen_2/15）
- 第三个 GPU 5 进程（PID 519277）— 活跃（95% 利用率）

**因磁盘满崩溃（EXIT_CODE = "No space left on device"）：**
- **t25_a060_s42_fp32★** — 崩溃于 gen_15/24（03:24），**GPU 3 已空闲，需要重启**
- **t25_a050_s42_fp32** — 崩溃于 gen_14（03:21）
- **t20_a060_s43_fp32** — 崩溃于 gen_3（03:23）

**未开始：**
- **t15_a045_s43_fp32** — 只有 config.json，无 gen 目录

### 4. 关键发现

**t25_a060★ 已因磁盘满崩溃**，停在 gen_15（需要跑到 gen_24）。GPU 3 现已空闲，磁盘空间已充足（139G），需要决定是否重启。另有 2 个实验同样崩溃。3 个仍在运行的实验在磁盘清理后已恢复正常写入。

---
