# diagnose server gpu status 20260524

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_server_gpu_status_20260524_20260524T061941_result.json`
- **Structured JSON:** [`32583b4a30e16a584a49.json`](../../sessions/32/32583b4a30e16a584a49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器资源盘点

### westd-38929 — 4× RTX PRO 6000 (96GB)

| GPU | 显存占用 | 利用率 | 状态 | 占用进程 |
|-----|---------|--------|------|---------|
| 0 | 1/97887 MiB | 0% | **空闲** | — |
| 1 | 1/97887 MiB | 0% | **空闲** | — |
| 2 | 4672/97887 MiB | 6% | 占用 | `eval_xvla_pruning_libero.py` libero_10 keep=0.5 l2_norm |
| 3 | 4856/97887 MiB | 25% | 占用 | `eval_xvla_pruning_libero.py` libero_goal keep=0.3 l2_norm |

磁盘：根 29% (22G free) · 数据盘 80% (52G free)

---

### westd-27271 — 2× RTX PRO 6000 (96GB)

| GPU | 显存占用 | 利用率 | 状态 | 占用进程 |
|-----|---------|--------|------|---------|
| 0 | 0/97887 MiB | 0% | **空闲** | — |
| 1 | 0/97887 MiB | 0% | **空闲** | — |

磁盘：根 41% (18G free) · 数据盘 70% (77G free)

---

### westd-41074 — 4× RTX PRO 6000 (96GB)

| GPU | 显存占用 | 利用率 | 状态 | 占用进程 |
|-----|---------|--------|------|---------|
| 0 | 1/97887 MiB | 0% | **空闲** | — |
| 1 | 1/97887 MiB | 0% | **空闲** | — |
| 2 | 10614/97887 MiB | 36% | 占用 | `eval_pi05_pruning_libero.py` random keep=0.85 libero_spatial |
| 3 | 1/97887 MiB | 0% | **空闲** | — |

磁盘：根 17% (26G free) · 数据盘 86% (38G free)

---

### cqa1-33015 — 4× RTX 4090 D (24GB)

| GPU | 显存占用 | 利用率 | 状态 | 占用进程 |
|-----|---------|--------|------|---------|
| 0 | 10325/24564 MiB | 22% | 占用 | `eval_pi05_pruning_libero.py` random keep=0.7 libero_spatial |
| 1 | 10217/24564 MiB | 24% | 占用 | `eval_pi05_pruning_libero.py` random keep=0.3 libero_spatial |
| 2 | 1/24564 MiB | 0% | **空闲** | — |
| 3 | 1/24564 MiB | 0% | **空闲** | — |

磁盘：根 29% (22G free) · 数据盘 55% (115G free)

---

### 可立即部署的空闲 GPU 汇总

| 服务器 | 空闲 GPU | 单卡显存 | 数据盘剩余 |
|--------|---------|---------|-----------|
| **westd-38929** | GPU 0, 1 | 96GB | 52G |
| **westd-27271** | GPU 0, 1 (全空) | 96GB | 77G |
| **westd-41074** | GPU 0, 1, 3 | 96GB | 38G |
| **cqa1-33015** | GPU 2, 3 | 24GB | 115G |

共 **9 张空闲 GPU**（7× 96GB RTX PRO 6000 + 2× 24GB 4090D）。westd-41074 数据盘偏满 (86%)，部署前注意清理。

---
