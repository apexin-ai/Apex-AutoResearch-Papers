# ops seed43 harvest gpu audit v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed43_harvest_gpu_audit_v1_20260522T085151_result.json`
- **Structured JSON:** [`36abb3ff04d0079496bd.json`](../../sessions/36/36abb3ff04d0079496bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-27271

| GPU | PID | 实验 | 状态 | SR / 进度 | 运行时间 |
|-----|-----|------|------|-----------|---------|
| 0 | — | — | **空闲** | — | — |
| 1 | 212585 | l2norm_k095_object_seed43 | 运行中 | T6 ep10, 累计 97.3% (292/300) | 45min |
| 1 | 213482 | l2norm_k095_object_seed43 (**重复**) | 运行中 | 同上 | 44min |
| — | ~~119111~~ | random_k07_spatial_seed43 | **已完成** | **SR=73.8%** (369/500) | — |
| — | ~~119449~~ | l2norm_k07_spatial_seed43 | **已完成** | **SR=68.4%** (342/500) | — |

空闲 GPU: **GPU 0**

> ⚠️ PID 213482 是 212585 的重复进程（同参数），两个都跑在 GPU 1 上，各占 ~10.5GB。建议 kill 一个。

---

## westd-38929

| GPU | PID | 实验 | 状态 | SR / 进度 | 运行时间 |
|-----|-----|------|------|-----------|---------|
| 0 | 708992 | l2norm_k05_spatial_seed43 | 运行中 | T5 ep50完, 累计 59.7% (179/300) | 1h10m |
| 1 | 709233 | random_k03_spatial_seed43 | 运行中 | T5 ep30, 累计 ~52% (131/250) | 1h10m |
| 2 | 709369 | l2norm_k03_spatial_seed43 | 运行中 | T5 ep30, 累计 ~49% (123/250) | 1h10m |
| 3 | 808099 | random_k03_object_seed43 | 运行中 | T1 ep10, 刚启动 | 12min |

空闲 GPU: 无

---

## cqa1-33015

可达。4x RTX 4090D (24GB)

| GPU | PID | 实验 | 状态 | 进度 | 运行时间 |
|-----|-----|------|------|------|---------|
| 0 | 249598 | l2norm_k095_object_seed43 | 运行中 | T0 ep40, 98% | 12min |
| 1 | 249668 | l2norm_k09_object_seed43 | 运行中 | T0 ep40, 100% | 12min |
| 2 | 249746 | l2norm_k0925_spatial_seed43 | 运行中 | T1 ep10, T0=100% | 12min |
| 3 | 249887 | random_k05_spatial_seed43 | 运行中 | T1 starting, T0=94% | 12min |

空闲 GPU: 无

---

## 已完成需收割的实验

| 实验 | SR | 服务器 | 结果文件 |
|------|-----|--------|---------|
| random_k07_spatial_seed43 | **73.8%** | westd-27271 | `eval_results/pi05_random_k0.70_libero_spatial_seed43.json` |
| l2norm_k07_spatial_seed43 | **68.4%** | westd-27271 | `eval_results/pi05_l2norm_k0.70_libero_spatial_seed43.json` |

另外 westd-27271 上还有两个 **OpenVLA** seed43 已完成（非 pi05）：
- openvla_l2norm_k07_object_seed43: SR=74.0%
- openvla_l2norm_k05_object_seed43: SR=39.2%

---

**需关注**:
1. westd-27271 GPU 1 上有重复进程 (PID 213482)，浪费显存
2. westd-27271 GPU 0 完全空闲，可部署新实验
3. westd-38929 的 `eval_pi05_l2norm_k085_spatial_seed42.log` 尾部显示网络错误崩溃（tokenizer 下载 `[Errno 101] Network is unreachable`），这是 seed42 实验非当前 seed43 批次

---
