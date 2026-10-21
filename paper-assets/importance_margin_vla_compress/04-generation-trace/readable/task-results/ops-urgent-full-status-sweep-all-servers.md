# ops urgent full status sweep all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-full-status-sweep-all-servers_20260521T121759_result.json`
- **Structured JSON:** [`2a98c34da1c3df2693e6.json`](../../sessions/2a/2a98c34da1c3df2693e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Data collection complete. Here's the full status report:

---

## 全服务器巡查报告 (2026-05-21 20:20)

### P0: westd-41074 — π0.5 seed43 sweep

| GPU | 任务 | PID | 运行时间 | VRAM | 状态 |
|-----|------|-----|---------|------|------|
| GPU0 | π0.5 L2norm k=0.5 seed43 | 206999 | 51min | 10.4GB | **RUNNING** |
| GPU1 | π0.5 L2norm k=0.3 seed43 | 207154 | 51min | 10.4GB | **RUNNING** |
| GPU2 | M96 train | 68539 | 1d8h38m | 28.5GB | **RUNNING** |
| GPU3 | M64v6 train + π0.5 L2norm k=0.7 seed43 | 59671/209861 | 3h/49min | 27.5+10.5GB | **RUNNING** |

seed43 结果尚未产出，估计还需 ~40min。

已确认 **π0.5 L2norm k=0.7 seed42** 结果：**SR=55.0% (275/500)** ✅

---

### P1: westd-38929 — OpenVLA eval sweep

| GPU | 任务 | PID | 运行时间 | 状态 |
|-----|------|-----|---------|------|
| GPU0 | random k=0.5 seed42 | 181687 | 24min | **RUNNING** Task 1 Ep 40/50 (重启过) |
| GPU1 | random k=0.3 seed42 | 2478 | 4h52m | **RUNNING** Task 4+ |
| GPU2 | l2norm k=0.5 seed42 (rerun?) | 186986 | 15min | **RUNNING** |
| GPU3 | l2norm k=0.3 seed43 | 195280 | 3min | **RUNNING** Task 1 |

**已完成 OpenVLA 结果（seed42）：**

| Method | k | SR | N/500 |
|--------|---|----|-------|
| L2norm | 0.95 | **70.6%** | 353 |
| L2norm | 0.9 | **70.6%** | 353 |
| L2norm | 0.7 | **49.8%** | 249 |
| L2norm | 0.5 | **39.2%** | 196 |
| L2norm | 0.3 | **25.0%** | 125 |
| Random | 0.95 | **69.2%** | 346 |
| Random | 0.7 | **44.4%** | 222 |

注意：`openvla_l2norm_prune_k05_object.json`（无下划线版）的 per_task 与 k=0.7 完全一致，疑似文件名错误。实际 k=0.5 结果应为 `k0_5` 版（39.2%）。

---

### P2: cqa1-33015 — X-VLA eval

| GPU | 任务 | PID | 运行时间 | 状态 |
|-----|------|-----|---------|------|
| GPU0 | L2norm k=0.85 seed43 | 358232 | 15min | **RUNNING** |
| GPU1 | random k=0.3 seed44 | 267697 | 42min | **RUNNING** |
| GPU2 | random k=0.85 seed43 | 358390 | 15min | **RUNNING** |
| GPU3 | L2norm k=0.7 seed44 | 269294 | 42min | **RUNNING** |

**新完成 X-VLA 结果：**

| Method | k | seed | SR | N/500 |
|--------|---|------|----|-------|
| L2norm | 0.7 | 42 | **58.2%** | 291 |
| L2norm | 0.7 | 43 | **59.0%** | 295 |
| L2norm | 0.3 | 43 | **21.0%** | 105 |
| Random | 0.3 | 42 | **62.8%** | 314 |
| Random | 0.3 | 43 | **66.2%** | 331 |
| Random | 0.7 | 43 | **65.0%** | 325 |
| Random | 0.7 | 44 | **65.0%** | 325 |

---

### P3: westd-27271

| GPU | 任务 | PID | 运行时间 | VRAM | 状态 |
|-----|------|-----|---------|------|------|
| GPU0 | OpenVLA L2norm k=0.3 rerun | 193983 | 4h24m | 16.1GB | **RUNNING** |
| GPU1 | M32 train | 921279 | 1d1h31m | 42.2GB | **RUNNING** |

**M32 训练进度：step 57,550 / 100,000 (57.6%)**，loss=2.55-2.68，lr=4.05e-5，sps=0.5

已有结果：OpenVLA baseline seed43 = **74.0%** (370/500)，OpenVLA random k=0.7 seed7 = **49.0%** (245/500)

---

### GPU 占用总览

| 服务器 | GPU0 | GPU1 | GPU2 | GPU3 | 空闲 |
|--------|------|------|------|------|------|
| westd-41074 | eval | eval | train | train+eval | **0** |
| westd-38929 | eval | eval | eval | eval | **0** |
| cqa1-33015 | eval | eval | eval | eval | **0** |
| westd-27271 | eval | train | — | — | **GPU2, GPU3** |

**16 GPU 中 14 在用，2 空闲（westd-27271 GPU2/GPU3）。**

---
