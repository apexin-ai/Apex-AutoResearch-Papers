# status all servers progress

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_all_servers_progress_20260527T091423_result.json`
- **Structured JSON:** [`2ab6434ff9f6ba168c37.json`](../../sessions/2a/2ab6434ff9f6ba168c37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全服务器实验进度快照 (2026-05-27 ~17:20 UTC)

---

### westd-27271 (2× RTX PRO 6000 96GB)

| GPU | 利用率 | 显存 | 实验 | 进度 | ETA (UTC) |
|-----|--------|------|------|------|-----------|
| 0 | **0%** | 1/98 GB | eval_openvla_l2norm_k09_goal_seed43_v3 | **已完成** SR=75.2% (376/500) | ✅ Done |
| 1 | 70% | 16/98 GB | eval_openvla_l2norm_k085_object_seed42 | Task 7/10, Ep 40/50 (2.0 eps/min) | ~18:30 |

> ⚠️ GPU0 上运行的不是预期的 `attn_k095_goal_seed42_v2`，而是 `l2norm_k09_goal_seed43_v3`，已完成并空闲。

---

### westd-38929 (4× RTX PRO 6000 96GB)

| GPU | 利用率 | 显存 | 实验 | 进度 | ETA (UTC) |
|-----|--------|------|------|------|-----------|
| 0 | 45% | 16/98 GB | eval_openvla_random_k095_long_seed42_v2 | Task 4/10, Ep 10/50 (1.0 eps/min) | ~23:00 |
| 1 | 75% | 16/98 GB | eval_openvla_l2norm_k095_long_seed42 | Task 8/10, Ep 20/50 (0.8 eps/min) | ~19:50 |
| 2 | **0%** | 16/98 GB | eval_openvla_l2norm_k075_long_seed42_v2 | Task 7/10, 刚开始 (0.7 eps/min) | ~22:00 |
| 3 | 86% | 16/98 GB | eval_openvla_attn_k095_long_seed42 | Task 8/10, Ep 30/50 (0.8 eps/min) | ~19:40 |

> ⚠️ GPU2 利用率 0% 但占 16GB 显存——可能在 Task 切换间隙加载环境，非卡死（日志刚完成 Task 6）。

---

### westd-41074 (4× RTX PRO 6000 96GB)

| GPU | 利用率 | 显存 | 实验 | 进度 | ETA (UTC) |
|-----|--------|------|------|------|-----------|
| 0 | **0%** | 1/98 GB | **空闲** | — | **现在可用** |
| 1 | **0%** | 1/98 GB | **空闲** | — | **现在可用** |
| 2 | 33% | 11/98 GB | eval_pi05_random_k095_long_seed42_strict | Task 6/10, Ep 20/50 | ~18:30 |
| 3 | 45% | 10/98 GB | eval_pi05_l2norm_k095_long_seed42_strict | Task 8/10, Ep 10/50 (累计 89.8%) | ~18:15 |

---

### cqa1-33015 (4× RTX 4090 D 24GB)

| GPU | 利用率 | 显存 | 实验 | 进度 | ETA (UTC) |
|-----|--------|------|------|------|-----------|
| 0 | 21% | 10/25 GB | eval_pi05_random_k07_long_seed42_strict_v2 | Task 2/10 即将开始 (T0=96%, T1=66%) | ~20:40 |
| 1 | 35% | 10/25 GB | eval_pi05_random_k05_long_seed42_strict | Task 1/10, Ep 20/50 (T0=84%) | ~21:10 |
| 2 | 21% | 10/25 GB | eval_pi05_l2norm_k085_long_seed42_strict | Task 3/10, Ep 30/50 (累计 92.7%) | ~20:00 |
| 3 | 74% | 16/25 GB | eval_openvla_attn_k05_goal_seed42_v3 | Task 9/10, Ep 40/50 | ~18:10 |

> ❌ **eval_openvla_random_k095_goal_seed42_v2 已 CRASH** — CUDA OOM，尝试在 GPU0 上和 pi05 实验共存，显存不足。

---

### 汇总

**最早释放的 GPU：**
1. **westd-27271 GPU0** — 现在空闲
2. **westd-41074 GPU0, GPU1** — 现在空闲
3. **cqa1-33015 GPU3** — ~18:10 UTC（~50 min 后）
4. **westd-41074 GPU3** — ~18:15 UTC
5. **westd-41074 GPU2** — ~18:30 UTC
6. **westd-27271 GPU1** — ~18:30 UTC

**异常：**
1. **cqa1-33015 GPU0**: `eval_openvla_random_k095_goal_seed42_v2` OOM 崩溃，需要单独 GPU 重跑
2. **westd-27271 GPU0**: 实验名与预期不符（实际跑的是 `l2norm_k09_goal_seed43_v3`），已完成，GPU 空闲
3. **westd-38929 GPU2**: 瞬时 0% 利用率，大概率是 Task 间隙，暂不判定卡死
4. **westd-38929 GPU0** 的 Long suite 实验（random k=0.95）进度较慢（1.0 eps/min），ETA 最晚 ~23:00 UTC，仍在 deadline (5/28 08:00 UTC) 之前

**所有实验预计 5/28 00:00 UTC 前完成，无 deadline 风险。**

---
