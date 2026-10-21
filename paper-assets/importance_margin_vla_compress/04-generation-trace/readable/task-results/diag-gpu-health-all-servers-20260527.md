# diag gpu health all servers 20260527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_health_all_servers_20260527_20260527T052835_result.json`
- **Structured JSON:** [`815c1c52c1e1bb0bf75c.json`](../../sessions/81/815c1c52c1e1bb0bf75c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have enough data to compile the full report. Here's the complete GPU diagnostic:

---

## westd-27271 (2× RTX PRO 6000 Blackwell, 98GB)

| GPU | Mem | Util | PID | 实验标识 | 状态 |
|-----|-----|------|-----|---------|------|
| 0 | 1 MiB | 0% | — | **IDLE** | 空闲 |
| 1 | 15980 MiB | 77% | 638225 | OpenVLA Attn k=0.95 Object seed42 | Running, task 10/10 ep ~40/50 |

---

## westd-38929 (4× RTX PRO 6000 Blackwell, 98GB)

| GPU | Mem | Util | PID | 实验标识 | 状态 |
|-----|-----|------|-----|---------|------|
| 0 | 15964 MiB | 77% | 949253 | OpenVLA Attn k=0.95 Goal seed42 | Running, task 10/10 starting |
| 1 | 15880 MiB | 65% | 949447 | OpenVLA L2norm k=0.95 LIBERO-10 seed42 | Running, task 4/10 ep 20/50 |
| 2 | 15780 MiB | 68% | 968309 | OpenVLA L2norm k=0.75 LIBERO-10 seed42 | Running, task 3/10 ep 10/50 |
| 3 | 15880 MiB | 78% | 950007 | OpenVLA Attn k=0.95 LIBERO-10 seed42 | Running, task 4/10 ep 20/50 |

**GPU 3 状态更新**: 之前的 Random k=0.75 Goal (PID 811418) 已不在，替换为新实验 Attn k=0.95 LIBERO-10。

---

## westd-41074 (4× RTX PRO 6000 Blackwell, 98GB)

| GPU | Mem | Util | PID | 实验标识 | 状态 |
|-----|-----|------|-----|---------|------|
| 0 | 16394 MiB | 67% | 32184 | OpenVLA Random k=0.95 LIBERO-10 seed42 | Running, task 5/10 ep ~30/50 |
| 1 | 10724 MiB | 52% | 155174 | π0.5 Random k=0.75 LIBERO-10 seed42 | **CRASHED** — Network unreachable |
| 2 | 10918 MiB | 47% | 94308 | π0.5 Attn k=0.9 LIBERO-10 seed42 | Running |
| 3 | 10648 MiB | 35% | 94384 | π0.5 Attn k=0.85 LIBERO-10 seed42 | Running |

**GPU 1 异常**: `eval_pi05_random_k075_long_seed42_strict.log` 启动时 tokenizer 下载失败 (`[Errno 101] Network is unreachable`)，EXIT_CODE=1。进程已死但 GPU 内存未释放。**需要 kill PID 155174 并重启**。

---

## cqa1-33015 (4× RTX 4090 D, 24GB)

| GPU | Mem | Util | PID | 实验标识 | 状态 |
|-----|-----|------|-----|---------|------|
| 0 | 15710 MiB | 40% | 896333 | OpenVLA Random k=0.95 Goal seed42 | Running, task 6 |
| 1 | 10306 MiB | 12% | 972716 | π0.5 Baseline (no prune) Goal seed42 | Running, task 3 (T2: SR=96%) |
| 2 | 10336 MiB | 18% | 938642 | π0.5 Attn k=0.95 LIBERO-10 seed42 | Running |
| 3 | 15712 MiB | 68% | 897100 | OpenVLA Attn k=0.5 Goal seed42 | Running, task 4 |

**GPU 0 & 1 状态更新**: 之前空闲，现均已部署实验。

---

## 近期已完成实验结果

| 服务器 | 实验 | Overall SR | 状态 |
|--------|------|-----------|------|
| westd-27271 | OpenVLA L2norm k=0.95 Goal seed42 | **75.2%** | ✓ 正常完成 |
| westd-41074 | OpenVLA Random k=0.75 LIBERO-10 seed42 | **43.0%** | ✓ 正常完成 |
| westd-41074 | OpenVLA Attn k=0.75 LIBERO-10 seed42 | — | ✗ 超时 (EXIT_CODE=124), 跑到 task 9/10 |
| cqa1-33015 | π0.5 Attn k=0.95 LIBERO-10 seed42 | **77.0%** | ✓ 正常完成 |
| cqa1-33015 | π0.5 Attn k=0.5 LIBERO-10 seed42 | **49.8%** | ✓ 正常完成 |
| cqa1-33015 | π0.5 Attn k=0.85 LIBERO-10 seed42 | **51.6%** | ✓ 正常完成 |
| cqa1-33015 | π0.5 Random k=0.85 LIBERO-10 seed42 | **44.4%** | ✓ 正常完成 |
| cqa1-33015 | π0.5 L2norm k=0.85 LIBERO-10 seed42 | **78.8%** | ✓ 正常完成 |
| cqa1-33015 | OpenVLA Attn k=0.95 Goal seed42 | — | ✗ 被 kill (EXIT_CODE=143), task 4 后终止 |
| cqa1-33015 | OpenVLA Attn k=0.95 Object seed42 | — | ✗ 被 kill (EXIT_CODE=143), 0% SR 后终止 |

---

## 需要关注的问题

1. **westd-27271 GPU 0 空闲** — 可以部署新实验
2. **westd-41074 GPU 1 已崩溃** — PID 155174 需要 kill 并重启（π0.5 Random k=0.75 LIBERO-10 的 tokenizer 下载因网络不可达失败）
3. **cqa1-33015 上两个 OpenVLA 实验被 kill** — Attn k=0.95 Goal 和 Attn k=0.95 Object 均被终止，可能是人工清理后重新部署了当前实验

---
