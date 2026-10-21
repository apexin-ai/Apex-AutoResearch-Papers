# diag all servers comprehensive 20260523b

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_all-servers-comprehensive-20260523b_20260523T185549_result.json`
- **Structured JSON:** [`9578519a7606f02b16fa.json`](../../sessions/95/9578519a7606f02b16fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是 4 台服务器的全面诊断报告。

---

## 1. westd-38929 — 4× RTX PRO 6000 (96GB)

| GPU | 显存占用 | 利用率 | PID(s) | 实验 | 状态 |
|-----|---------|--------|--------|------|------|
| 0 | 4938/97887 MiB | 26% | 179279 | eval_xvla_l2norm_k05_spatial_seed42_v3 | 运行中, Ep 12/50 |
| 1 | 4840/97887 MiB | 10% | 179514 | eval_xvla_l2norm_k05_goal_seed42_v3 | 运行中, Ep 30/50 (近期全 FAIL) |
| 2 | 9791/97887 MiB | 3% | 179850 + 224430 | **2个实验重叠**: xvla_l2norm_k03_goal + xvla_l2norm_k03_spatial | 运行中 |
| 3 | 14055/97887 MiB | 64% | 153091 + 225371 + 261569 | **3个实验重叠**: random_k05_long + l2norm_k03_goal + l2norm_k05_long | 运行中 |

**关键发现:**
- GPU 2 有 2 个进程堆叠（PID 179850: k03_goal, PID 224430: k03_spatial）
- **GPU 3 有 3 个进程堆叠** — random_k05_long (PID 153091) 没有被清理，加上 k03_goal (PID 225371) 和 k05_long (PID 261569)
- k03_goal 似乎重复部署在 GPU 2 和 GPU 3 上
- k05_goal_v3 (GPU 1) Ep 26-30 全部 FAIL，表现堪忧
- k03_goal_v3 日志: Task 0 SR=42.0%, 当前 Task 1 Ep 13/50
- **空闲 GPU: 无**

---

## 2. westd-27271 — 2× RTX PRO 6000 (96GB)

| GPU | 显存占用 | 利用率 | PID | 实验 | 状态 |
|-----|---------|--------|-----|------|------|
| 0 | 4371/97887 MiB | 0% | 366055 | eval_xvla_l2norm_k03_long_seed42 | 运行中, Task 0 Ep 41/50 |
| 1 | 16394/97887 MiB | 86% | 291098 | eval_openvla_baseline_long_seed42 | 运行中, Task 5/10 |

**已完成:**
- eval_openvla_baseline_goal_seed42_v3: **SR=74.8% (374/500)**, EXIT_CODE=0

**异常:**
- **eval_xvla_l2norm_k03_long_seed42 被错误部署到此服务器** (GPU 0, PID 366055)，通过 `tee` 写日志到 `/root/autodl-tmp/importance_margin_vla_compress/logs/`
- cqa1-33015 上未找到该实验的 tmux session，所以不是从那边部署的
- auto_deploy_openvla_baselines.sh (PID 295287) 仍在后台运行
- **空闲 GPU: 无**

---

## 3. westd-41074 — 4× RTX PRO 6000 (96GB)

| GPU | 显存占用 | 利用率 | PID | 实验 | 状态 |
|-----|---------|--------|-----|------|------|
| 0 | 10059/97887 MiB | 0% | 728249 | eval_pi05_l2norm_k0925_goal_seed43 | 运行中, Task 6/10, 累计 SR=96.7% |
| 1 | 10670/97887 MiB | 52% | 763841 | eval_pi05_l2norm_k05_long_seed42_v3 | 刚启动, Task 0 Ep 10: 30% |
| 2 | 1/97887 MiB | 0% | — | — | **空闲** |
| 3 | 10670/97887 MiB | 35% | 764088 | eval_pi05_random_k05_long_seed42_v2 | 刚启动, Task 0 Ep 10: 60% |

**已完成:**
- eval_pi05_random_k085_spatial_seed42_v2: **SR=56.6%**, EXIT_CODE=0

**空闲 GPU: GPU 2**

---

## 4. cqa1-33015 — 4× RTX 4090 D (24GB)

| GPU | 显存占用 | 利用率 | PID | 实验 | 状态 |
|-----|---------|--------|-----|------|------|
| 0 | 10196/24564 MiB | 23% | 88440 | eval_pi05_random_k05_goal_seed42_v2 | Task 3 Ep 20/50, 累计 69.3% |
| 1 | 10292/24564 MiB | 50% | 88538 | eval_pi05_random_k085_goal_seed42_v4 | Task 2 Ep 20/50 |
| 2 | 10294/24564 MiB | 33% | 88688 | eval_pi05_l2norm_k085_goal_seed42 | Task 4 Ep 10, 累计 90.5% |
| 3 | 10140/24564 MiB | 13% | 97992 | eval_pi05_random_k03_goal_seed43_v2 | Task 2 Ep 20/50, 累计 46% |

**已完成 (本服务器之前完成的):**
- eval_pi05_l2norm_k095_goal_seed42: **SR=89.4%**
- eval_pi05_l2norm_k07_goal_seed42: **SR=73.6%**
- eval_pi05_l2norm_k03_goal_seed42: **SR=50.6%**

**异常:**
- **未发现** eval_xvla_l2norm_k03_long_seed42 tmux session（该实验在 westd-27271 上）
- **空闲 GPU: 无**

---

## 总结

| 项目 | 状态 |
|------|------|
| **空闲 GPU** | westd-41074 GPU 2（唯一） |
| **严重问题** | westd-38929 GPU 3 堆了 3 个实验互相抢资源 |
| **错误部署** | eval_xvla_l2norm_k03_long_seed42 在 westd-27271 而非预期位置 |
| **GPU 2 重叠** | westd-38929 GPU 2 有 2 个实验（k03_goal + k03_spatial） |
| **k05_goal_v3 堪忧** | westd-38929 GPU 1, Ep 26-30 全 FAIL |
| **已完成** | openvla_baseline_goal_v3 (SR=74.8%), pi05_random_k085_spatial (SR=56.6%), pi05_l2norm_k095_goal (89.4%), pi05_l2norm_k07_goal (73.6%), pi05_l2norm_k03_goal (50.6%) |

---
