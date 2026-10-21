# audit westd41074 westd38929 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd41074-westd38929-gpu-status_20260524T021409_result.json`
- **Structured JSON:** [`8b927e13c800c878ca11.json`](../../sessions/8b/8b927e13c800c878ca11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 审计报告

### westd-41074 — 4× RTX PRO 6000 Blackwell (96GB)

**所有 4 个 GPU 满载，无空闲 GPU。**

| GPU | VRAM | Util | PID | 实验 | 进度 |
|-----|------|------|-----|------|------|
| 0 | 10530/97887 MiB | 54% | 363766 | π0.5 Random k=0.95 Goal s43 | Task 3 ep20, 累计 84.7% |
| 1 | 10455/97887 MiB | 54% | 345089 | π0.5 L2Norm k=0.7 Goal s43 | Task 4 ep40, 累计 67.5% |
| 2 | 10651/97887 MiB | 0%* | 363842 | π0.5 L2Norm k=0.5 Long s43 | Task 1 ep20, 累计 ~66% |
| 3 | 10514/97887 MiB | 55% | 318964 | π0.5 Random k=0.85 Goal s43 | **Task 9 ep10, 即将完成** (累计 56.9%) |

*GPU 2 util 0% 是采样瞬态，进程活跃。

Tmux sessions: `eval_pi05_random_k085_goal_seed43`, `eval_pi05_l2norm_k07_goal_seed43_v2`, `eval_pi05_random_k095_goal_seed43`, `eval_pi05_l2norm_k05_long_seed43` + 历史残留 `smolvla_spatial`, `xvla_long`, `diag_read_goal_results`, `eval_random_k09_s42`

**GPU 3 上的 Random k=0.85 Goal s43 预计 ~15-20 分钟内完成。**

---

### westd-38929 — 4× RTX PRO 6000 Blackwell (96GB)

**GPU 0、1 空闲，GPU 2、3 运行中。**

| GPU | VRAM | Util | PID | 实验 | 进度 |
|-----|------|------|-----|------|------|
| 0 | 1 MiB | 0% | — | **空闲** | — |
| 1 | 1 MiB | 0% | — | **空闲** | — |
| 2 | 4838 MiB | 24% | 674830 | X-VLA Random k=0.85 Goal s42 | 某 task ep46/50 |
| 3 | 4362 MiB | 16% | 674970 | X-VLA Random k=0.85 Spatial s42 | 某 task ep46/50 |

注意：这两个实验没有日志文件输出到 logs/ 目录，只在 tmux 内输出。

---

### westd-38929 已完成实验（今日，未收割）

**X-VLA Random k=0.50 seed43 — 4 suite 全部完成：**

| Suite | SR | 95% CI |
|-------|-----|--------|
| Object | **71.6%** | [67.5%, 75.4%] |
| Goal (v4) | **68.6%** | [64.4%, 72.5%] |
| Spatial | **72.6%** | [68.5%, 76.3%] |
| Long (libero_10) | **58.2%** | [53.8%, 62.4%] |

**X-VLA L2Norm k=0.50 seed43 — 2 suite 完成：**

| Suite | SR | 95% CI |
|-------|-----|--------|
| Object | **43.0%** | [38.7%, 47.4%] |
| Goal | **60.2%** | [55.8%, 64.4%] |

---

### 小结

- **westd-41074**：4 GPU 全满，GPU 3 实验即将完成（~15min），之后可释放
- **westd-38929**：**GPU 0、1 空闲可用**，GPU 2/3 运行 X-VLA k=0.85 s42 评测（这两个实验无 log 文件，需从 tmux 收割结果）
- westd-38929 上 X-VLA Random k=0.50 s43 全 4 suite 结果已完成待收割，L2Norm k=0.50 s43 有 object/goal 两个结果

---
