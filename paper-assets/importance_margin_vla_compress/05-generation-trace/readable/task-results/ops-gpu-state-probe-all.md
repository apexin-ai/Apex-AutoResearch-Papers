# ops gpu state probe all

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-state-probe-all_20260521T210304_result.json`
- **Structured JSON:** [`1daef1b503156022cd1f.json`](../../sessions/1d/1daef1b503156022cd1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`tmux ls` 不在 read_only 白名单内。nvidia-smi 数据已足够判断。

## GPU 使用状态汇总

### 1. westd-41074 — 4× RTX PRO 6000 Blackwell (98GB)

| GPU | 显存使用 | 利用率 | PID | 备注 |
|-----|---------|--------|-----|------|
| 0 | 10054 / 97887 MiB | 1% | 627797 | python |
| 1 | 10535 / 97887 MiB | 17% | 629631 | python |
| 2 | 28546 / 97887 MiB | 0% | 68539 | python |
| 3 | 27526 / 97887 MiB | 0% | 59671 | `/root/miniconda3/bin/python` — **train_openvla_sc_m64_seed42_v6 仍在运行** |

**空闲 GPU: 无** (4卡全被占用)

GPU 0/1 各占 ~10GB 但利用率低，GPU 2/3 各占 ~28GB 利用率 0%——可能在做 checkpoint 或 eval 间歇。

---

### 2. westd-38929 — 4× RTX PRO 6000 Blackwell (98GB)

| GPU | 显存使用 | 利用率 | PID | 备注 |
|-----|---------|--------|-----|------|
| 0 | 10456 / 97887 MiB | 41% | 788122 | python |
| 1 | 1 / 97887 MiB | 0% | — | **空闲** |
| 2 | 10554 / 97887 MiB | 32% | 788362 | python |
| 3 | 1 / 97887 MiB | 0% | — | **空闲** |

**空闲 GPU: 1, 3** (2卡可用，各98GB)

---

### 3. westd-27271 — 2× RTX PRO 6000 Blackwell (98GB)

| GPU | 显存使用 | 利用率 | PID | 备注 |
|-----|---------|--------|-----|------|
| 0 | 15961 / 97887 MiB | 73% | 306599 | **eval_openvla_l2norm_k09_object_seed42** — 仍在跑 (PID 306599，你记录的 306593 可能是父进程) |
| 1 | 42180 / 97887 MiB | 0% | 921279 | **train_openvla_sc_m32_vtconly_seed42** — PID 匹配，42GB 占用，利用率 0%（可能在 eval/save 阶段） |

**空闲 GPU: 无**

---

### 4. cqa1-33015 — 4× RTX 4090 D (24GB)

| GPU | 显存使用 | 利用率 | PID | 备注 |
|-----|---------|--------|-----|------|
| 0 | 1 / 24564 MiB | 0% | — | **空闲** (eval_smolvla_official_l2norm_k090 已结束) |
| 1 | 2159 / 24564 MiB | 1% | 579179 | python — 可能是 SmolVLA sweep 残留的一个 |
| 2 | 1 / 24564 MiB | 0% | — | **空闲** |
| 3 | 1 / 24564 MiB | 0% | — | **空闲** (eval_smart_compress_m32_official 已结束) |

**空闲 GPU: 0, 2, 3** (3卡可用，各24GB)

---

## 关键发现

**可部署新实验的空闲 GPU:**

| 服务器 | 空闲 GPU | 单卡显存 | 适合部署 |
|--------|---------|---------|---------|
| westd-38929 | GPU 1, 3 | 98GB | 大模型训练/eval |
| cqa1-33015 | GPU 0, 2, 3 | 24GB | SmolVLA 级别 eval |

**共 5 张空闲卡** (2×98GB + 3×24GB)

**你关注的实验状态:**
- cqa1-33015 上的 eval_smolvla_official_l2norm_k090 和 eval_smart_compress_m32_official **已完成**
- SmolVLA sweep 4 个实验大部分已结束，GPU1 上可能还有 1 个残留
- westd-27271 上两个实验 **仍在运行**
- westd-41074 上 train_openvla_sc_m64_seed42_v6 (PID 59671) **仍在运行**

---
