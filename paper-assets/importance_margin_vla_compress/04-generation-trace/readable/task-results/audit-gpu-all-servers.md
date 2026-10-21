# audit gpu all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_all_servers_20260526T072630_result.json`
- **Structured JSON:** [`86e76a8346f44f8493f3.json`](../../sessions/86/86e76a8346f44f8493f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整审计报告：

---

## westd-27271（2× H100 96GB）

| GPU | 利用率 | 显存占用 | PID | 实验 | 状态 |
|-----|--------|----------|-----|------|------|
| 0 | 81% | 32043/97887 MiB | 11195 | OpenVLA L2norm k=0.9 goal seed43 | 🏃 已注册 |
| 0 | — | — | 112404 | OpenVLA baseline spatial seed42 | 🏃 已注册 |
| 1 | 58% | 15964/97887 MiB | 112477 | OpenVLA attention k=0.9 goal seed43 | 🏃 已注册 |

全部已注册，无空闲卡。GPU0 跑了两个实验共占 32GB。

---

## cqa1-33015（4× RTX 4090 24GB）

| GPU | 利用率 | 显存占用 | PID | 实验 | 状态 |
|-----|--------|----------|-----|------|------|
| 0 | 2% | 10077/24564 MiB | 3728 | π0.5 random keep=0.75 libero_10 seed42 | ❓ 未注册 |
| 1 | 1% | 10243/24564 MiB | 3874 | π0.5 attention keep=0.75 libero_10 seed42 | ❓ 未注册 |
| 2 | 6% | 10110/24564 MiB | 77661 | π0.5 l2norm keep=0.5 libero_10 seed42 | ❓ 未注册 |
| 3 | 23% | 10110/24564 MiB | 77832 | π0.5 random keep=0.5 libero_10 seed42 | ❓ 未注册 |

**4卡全满，全部未注册。** 利用率低（1-23%）是 LIBERO 仿真瓶颈导致的正常现象，非空闲。之前报告的 cuda:0/cuda:3 "可能空闲" 判断有误。

---

## westd-41074（4× H100 96GB）

| GPU | 利用率 | 显存占用 | PID | 实验 | 状态 |
|-----|--------|----------|-----|------|------|
| 0 | 69% | 15880/97887 MiB | 415537 | OpenVLA random k=0.85 libero_10 seed42 | ❓ 未注册 |
| 1 | 0% | 1/97887 MiB | — | — | ⚠️ 空闲 |
| 2 | 69% | 15984/97887 MiB | 415737 | OpenVLA attention k=0.7 object seed42 | 🏃 已注册 |
| 3 | 0% | 1/97887 MiB | — | — | ⚠️ 空闲 |

**GPU1、GPU3 完全空闲（0%利用率，1MiB显存）。**

---

## westd-38929（4× H100 96GB）

| GPU | 利用率 | 显存占用 | PID | 实验 | 状态 |
|-----|--------|----------|-----|------|------|
| 0 | 70% | 15980/97887 MiB | 285940 | OpenVLA random k=0.85 object seed42 | ❓ 未注册 |
| 1 | 64% | 15780/97887 MiB | 279274 | OpenVLA random k=0.5 libero_10 seed42 | ❓ 未注册 |
| 2 | 69% | 15980/97887 MiB | 252246 | OpenVLA l2norm k=0.7 object seed42 | ❓ 未注册 |
| 3 | 0% | 15479/97887 MiB | 288325 | OpenVLA attention k=0.85 object seed42 | ❓ 未注册+⚠️ 0%利用率 |

GPU3 有进程和显存占用但利用率 0%，可能卡住或处于 episode 间隙，需关注。

---

## 汇总

### 空闲卡清单
| 服务器 | GPU | 显存 | 可跑模型 |
|--------|-----|------|----------|
| westd-41074 | cuda:1 | 96GB 空闲 | OpenVLA / X-VLA / π0.5 |
| westd-41074 | cuda:3 | 96GB 空闲 | OpenVLA / X-VLA / π0.5 |

### 可疑进程
| 服务器 | GPU | PID | 问题 |
|--------|-----|-----|------|
| westd-38929 | cuda:3 | 288325 | 利用率 0% 但占 15GB，可能卡住 |

### 未注册进程清单（共 9 个）
- **cqa1-33015**: 4个 π0.5 pruning eval（random/attention/l2norm × libero_10）
- **westd-41074**: 1个 OpenVLA random k=0.85 libero_10
- **westd-38929**: 4个 OpenVLA eval（random/l2norm/attention × object/libero_10）

### 注册表异常
- **eval_openvla_random_k07_goal_seed42_v2** 状态为 RUNNING，但在 4 台服务器上均未找到对应进程，可能已崩溃未更新状态。

### 建议部署方案
- **westd-41074 cuda:1 + cuda:3**：立即可用，各 96GB，可部署 2 个 OpenVLA/X-VLA eval 或 1 个多卡训练
- **westd-38929 cuda:3**：先确认 PID 288325 是否卡住，如已死则释放后可用
- 9 个未注册进程建议补注册，便于追踪

---
