# ops gpu probe all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-probe-all-servers_20260521T205305_result.json`
- **Structured JSON:** [`08b4240de2ba287614da.json`](../../sessions/08/08b4240de2ba287614da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### 1. westd-41074 (4× RTX PRO 6000 Black 96GB)

| GPU | 显存 | Util | PID | 状态 |
|-----|------|------|-----|------|
| 0 | 10564 / 97887 MiB | 22% | 627797 (python) | 运行中 |
| 1 | 10554 / 97887 MiB | 33% | 629631 (python) | 运行中 |
| 2 | 28555 / 97887 MiB | 0% | 68539 (python) | 运行中但 util=0 |
| 3 | 27535 / 97887 MiB | 0% | 59671 (python) | 运行中但 util=0 |

**vs 预期**：
- GPU0: PID 627788→627797（偏移+9，可能 wrapper 进程，同一实验 k=0.95 v2 仍在跑）
- GPU1: PID 629619→629631（同上，fixed-mask k=0.9 v2 仍在跑）
- GPU2: PID 68539 **完全匹配**，VTC M96 仍在跑，但 util 从 ~71% 降到 0%——可能在 eval/checkpoint 阶段
- GPU3: PID 59671 **完全匹配**，VTC M64v6 仍在跑，但 util 从 ~22% 降到 0%——同上

**空闲 GPU**：无（全部占用）
**磁盘**：185G / 250G (74%)

---

### 2. westd-38929 (4× RTX PRO 6000 Black 96GB)

| GPU | 显存 | Util | PID | 状态 |
|-----|------|------|-----|------|
| 0 | 1 MiB | 0% | — | **空闲** |
| 1 | 10528 / 97887 MiB | 32% | 590432 (python) | 运行中 |
| 2 | 1 MiB | 0% | — | **空闲** |
| 3 | 10474 / 97887 MiB | 46% | 590825 (python) | 运行中 |

**vs 预期**（原 GPU0-3 跑 π0.5 Spatial cross-suite）：
- **GPU0、GPU2 已释放**——对应的 2 个实验（baseline + 另一个 sweep config）已完成
- GPU1、GPU3 仍在跑（新 PID 590432/590825，是剩余的 sweep 配置）

**空闲 GPU**：GPU0、GPU2
**磁盘**：199G / 250G (80%)——偏高

---

### 3. westd-27271 (2× RTX PRO 6000 Black 96GB)

| GPU | 显存 | Util | PID | 状态 |
|-----|------|------|-----|------|
| 0 | 15984 / 97887 MiB | 74% | 306599 (python) | 运行中 |
| 1 | 42189 / 97887 MiB | 0% | 921279 (python) | 运行中但 util=0 |

**vs 预期**：
- GPU0: PID 306599 **完全匹配**，OpenVLA L2norm k=0.9 仍在跑，74% util
- GPU1: PID 921279 **完全匹配**，VTC M32 仍在跑，但 util=0（eval/checkpoint 阶段）

**空闲 GPU**：无
**磁盘**：155G / 250G (62%)

---

### 4. cqa1-33015 (4× RTX 4090 D 24GB)

| GPU | 显存 | Util | PID | 状态 |
|-----|------|------|-----|------|
| 0 | 1 MiB | 0% | — | **空闲** |
| 1 | 2180 / 24564 MiB | 24% | 579179 (python) | 运行中 |
| 2 | 1 MiB | 0% | — | **空闲** |
| 3 | 1 MiB | 0% | — | **空闲** |

**vs 预期**（原 GPU0-2 跑 SmolVLA official sweep，GPU3 idle）：
- **GPU0、GPU2 已释放**——sweep 中 2 个配置已完成
- GPU1 仍在跑（PID 579179，2180 MiB，剩余的 sweep 配置）
- GPU3 仍然空闲

**空闲 GPU**：GPU0、GPU2、GPU3
**磁盘**：176G / 250G (71%)

---

### 可用 GPU 汇总

| 服务器 | 空闲 GPU | 备注 |
|--------|----------|------|
| westd-41074 | 无 | 4 卡全占 |
| westd-38929 | GPU0, GPU2 | 2× 96GB 可用 |
| westd-27271 | 无 | 2 卡全占 |
| cqa1-33015 | GPU0, GPU2, GPU3 | 3× 24GB 可用 |

---
