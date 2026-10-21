# diagnose cqa1 gpu2 process gone

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_gpu2_process_gone_20260527T114520_result.json`
- **Structured JSON:** [`fcdeef470740581b016c.json`](../../sessions/fc/fcdeef470740581b016c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：cqa1-33015

### GPU2 实验 `eval_pi05_l2norm_k085_long_seed42_strict`

**状态：已完成** — 实验正常结束，进程退出，无崩溃。

**结果：`overall_sr = 77.6%`**（388/500, 224.8 min）

Per-task breakdown:
| Task | SR |
|------|-----|
| T0 alphabet soup + tomato sauce → basket | 98% |
| T1 cream cheese + butter → basket | 94% |
| T2 stove + moka pot | 86% |
| T3 black bowl → drawer | 96% |
| T4 white mug + yellow mug → plates | 68% |
| T5 book → caddy | 96% |
| T6 white mug → plate + pudding | 8% |
| T7 alphabet soup + cream cheese → basket | 80% |
| T8 moka pots → stove | 56% |
| T9 yellow mug → microwave | 94% |

结果已保存到 `eval_results/pi05_l2norm_k0.85_libero_10_seed42.json`。无 sentinel 文件（脚本未写 .done/.failed），但日志和 JSON 输出均完整，进程正常退出。

### 其他实验状态

| GPU | PID | 实验 | 状态 |
|-----|-----|------|------|
| GPU0 | 109156 | `random k=0.7 libero_10 seed42` (v2) | **运行中** (28% util, 10GB VRAM) |
| GPU1 | 118731 | `random k=0.5 libero_10 seed42` | **运行中** (30% util, 10GB VRAM) |
| GPU2 | — | `l2norm k=0.85 libero_10 seed42` | **已完成**, GPU 空闲 (1MiB) |
| GPU3 | 200112 | `l2norm k=0.9 libero_10 seed42` | **运行中** (31% util, 10GB VRAM) |

### GPU 可用性

**GPU2 空闲，可立即部署新实验。** 其余 3 个 GPU 均在跑实验。

---
