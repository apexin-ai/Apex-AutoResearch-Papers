# ssh urgent gpu diagnosis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_gpu_diagnosis_20260522T045933_result.json`
- **Structured JSON:** [`38997679738b0d54b6a2.json`](../../sessions/38/38997679738b0d54b6a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全面诊断完成，汇总如下：

---

## 1. nvidia-smi 完整状态

| GPU | 型号 | 显存 | 占用 | 利用率 | 温度 |
|-----|------|------|------|--------|------|
| 0 | NVIDIA RTX PRO 6000 Blackwell | 97887 MiB | **0 MiB** | 0% | 30°C |
| 1 | NVIDIA RTX PRO 6000 Blackwell | 97887 MiB | **0 MiB** | 0% | 30°C |

**两张 GPU 完全空闲，无任何 GPU 进程。**

---

## 2. openvla_spatial pipeline 状态

**存活：是** — PID 594575 及其子进程链仍在运行（`run_spatial_pipeline.sh` → sleep 30 循环等待）。

**当前卡在：等待 checkpoint 下载完成。** pipeline 脚本在等两个条件满足：
- `model-00004-of-00004.safetensors` ✅ 已存在（263MB）
- `modeling_prismatic.py` ❌ **不存在**

**checkpoint 下载状态：**

| 文件 | 大小 | 状态 |
|------|------|------|
| model-00002-of-00004.safetensors | 4.9GB | ✅ 完成 |
| model-00003-of-00004.safetensors | 4.9GB | ✅ 完成 |
| model-00004-of-00004.safetensors | 263MB | ✅ 完成 |
| **model-00001-of-00004.safetensors** | **3.5GB / ~4.9GB** | ⏳ **下载中**（.incomplete 文件） |
| **modeling_prismatic.py** | — | ❌ **未下载** |

下载进程 PID 594477 (`python /tmp/dl_spatial.py`) 运行中，从 09:36 开始，已跑 ~3.5 小时。当前 model-00001 下载了 3.5GB，速度极慢（~200-300 KB/s，典型 AutoDL HF 代理限速）。

**预计还需**：model-00001 剩余 ~1.4GB + modeling_prismatic.py（小文件），按当前速度还需 ~1-2 小时。

---

## 3. cuda:1 状态

完全空闲，0 MiB 占用，0% 利用率。无进程占用。

---

## 4. 所有活跃进程

| 进程 | PID | 状态 | 说明 |
|------|-----|------|------|
| `python /tmp/dl_spatial.py` | 594477 | 运行中 | HF snapshot_download 下载 spatial checkpoint |
| `run_spatial_pipeline.sh` | 594580 | 运行中 | 每 30s 轮询等待 checkpoint 完成 |
| openvla_spatial tmux wrapper | 594575 | 运行中 | tmux session 主进程 |
| openvla_long_cf_trained | — | **已完成** | EXIT_CODE=0，耗时 90min，昨天 22:39 结束 |
| http.server :8765 | 759476 | 运行中 | attention results 文件服务 |
| tensorboard :6007 | 820 | 运行中 | — |

---

## 核心问题

**下载太慢**。AutoDL 通过 HF 代理下 openvla-7b（~15GB 总量），速度只有几百 KB/s。pipeline 脚本在死循环等 `model-00001` 和 `modeling_prismatic.py` 出现。

**可选加速方案**：用 ModelScope 替代 HF 下载（如果 ModelScope 有这个模型的话），或者检查是否已 `source /etc/network_turbo`。需要处理吗？

---
