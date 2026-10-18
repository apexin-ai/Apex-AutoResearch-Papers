# ops check m64 and xvla progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_m64_and_xvla_progress_20260523T035138_result.json`
- **Structured JSON:** [`5514b931baf434bfd800.json`](../../sessions/55/5514b931baf434bfd800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M64
**未运行。** cqa1-33015 上不存在 `train_openvla_sc_m64_v6_seed42.log`。最近的 M64 日志是 5/19 的 `train_smart_compress_m64_seed43.log`（已完成）。4 块 GPU 全部空闲。

## X-VLA Long Random k=0.95 seed42 (westd-27271:0)
PID 126840 存活，已运行 1h03m
- Task 7 ep 11/50 进行中，总进度 **361/500 (72.2%)**
- Task 6 SR: 18.0%
- ETA ≈ **24 min**（~12:16 完成）

## Goal seed43 (westd-41074:1)
PID 368157 存活，已运行 24m
- Task 3 ep 10/50 进行中，总进度 **160/500 (32.0%)**
- T0: 80%, T1: 90%, T2: 76% | 累计 82.0%
- ETA ≈ **51 min**（~12:40 完成）

## GPU 扫描

| 服务器 | GPU 0 | GPU 1 | GPU 2 | GPU 3 |
|--------|-------|-------|-------|-------|
| westd-27271 | **68% / 5.0GB** | 0% / idle | — | — |
| westd-38929 | 0% / idle | 0% / idle | 0% / idle | 0% / idle |
| westd-41074 | 0% / idle | **44% / 10.5GB** | 0% / idle | 0% / 27.5GB (loaded) |
| cqa1-33015 | 0% / idle | 0% / idle | 0% / idle | 0% / idle |

**可用资源**: westd-27271 GPU1, westd-38929 全部 4 卡, westd-41074 GPU0/2, cqa1-33015 全部 4 卡 — 共 **10 卡空闲**。westd-41074 GPU3 有 27.5GB 显存占用但 0% 利用率，可能有残留进程。

---
