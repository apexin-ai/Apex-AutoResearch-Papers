# diag exp 005 status check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-005-status-check_20260522T141953_result.json`
- **Structured JSON:** [`4e0b684b543dbc01cb25.json`](../../sessions/4e/4e0b684b543dbc01cb25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### GPU 状态
- **RTX PRO 6000** (cuda:0)，97GB 显存，**空闲**（0% 利用率，0MiB 占用，无进程）

### 评估进程
- **无评估进程在运行**（GPU 也确认无进程）

### 产出文件 (`exp005_zoo_expansion/`)
- 目录存在，包含 3 个版本的运行脚本和日志
- `priority1_v3.log`（218KB，最新 22:20）— 日志显示**正在下载模型**，不是在跑评估

### 模型下载状态

| 模型 | 状态 |
|------|------|
| **GLA-hybrid-3-1** | ✅ 已完成（1.3GB，含 model.safetensors 1.33GB） |
| **DeltaNet-hybrid-3-1** | ❌ 空目录，未下载 |
| **HGRN-hybrid-3-1** | ❌ 空目录，未下载 |

### 正在进行的下载
- `priority1_v3.log` 显示有一个下载在进行：**model.safetensors 52% (655M/1.24G)**，速度约 345-408 kB/s
- 但 GPU 上无进程 → 这个下载进程可能已经**断开或挂起**（日志是最后写入状态）
- HF cache: 478MB

### 结论
1. GLA 模型已下载完成；DeltaNet 和 HGRN 目录为空，下载未启动或失败
2. 日志显示有下载在 52% 处，但当前无活跃进程 → **下载可能已中断**
3. GPU 完全空闲，没有评估在跑

---
