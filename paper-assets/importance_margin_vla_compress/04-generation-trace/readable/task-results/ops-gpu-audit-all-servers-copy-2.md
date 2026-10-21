# ops gpu audit all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-all-servers_20260524T001558_result.json`
- **Structured JSON:** [`58796e1aed1a9e211baa.json`](../../sessions/58/58796e1aed1a9e211baa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. westd-38929 — 4× RTX PRO 6000 Blackwell (96GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 4938/97887 MiB | 1% | 运行中 (eval_xvla l2norm goal seed43) |
| 1 | 5250/97887 MiB | 78% | 运行中 (eval_xvla l2norm spatial seed43) |
| 2 | 1/97887 MiB | 0% | **空闲** |
| 3 | 4856/97887 MiB | 1% | 运行中 (eval_xvla random goal seed43) |

**TMUX Sessions (4):**
- `eval_xvla_l2norm_k05_spatial_seed43` — X-VLA l2_norm k=0.5, libero_spatial
- `eval_xvla_l2norm_k05_long_seed43` — X-VLA l2_norm k=0.5, libero_10
- `xvla_random_goal_s43_v4` — X-VLA random k=0.5, libero_goal
- `eval_xvla_random_k05_spatial_seed43` — (tmux 存在但未见活跃 python 进程，可能已完成)

**磁盘:** 52G 可用 / 250G (80%)

---

## 2. westd-27271 — 2× RTX PRO 6000 Blackwell (96GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 15964/97887 MiB | 71% | 运行中 (eval_openvla l2norm goal seed42) |
| 1 | 1/97887 MiB | 0% | **空闲** |

**TMUX Sessions (1):**
- `eval_openvla_l2norm_k05_goal_seed42_v2` — OpenVLA l2norm_prune k=0.5, libero_goal

**磁盘:** 77G 可用 / 250G (70%)

---

## 3. westd-41074 — 4× RTX PRO 6000 Blackwell (96GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 1/97887 MiB | 0% | **空闲** |
| 1 | 1/97887 MiB | 0% | **空闲** |
| 2 | 10614/97887 MiB | 36% | 运行中 (eval_pi05 random k=0.85 spatial) |
| 3 | 10472/97887 MiB | 45% | 运行中 (eval_pi05 attention k=0.5 long) |

**TMUX Sessions (5):**
- `eval_pi05_attention_k05_long_seed42` — π0.5 attention k=0.5, libero_10
- `eval_pi05_random_k085_spatial_seed42_postfix` — π0.5 random k=0.85, libero_spatial
- `smolvla_spatial` / `xvla_long` / `diag_read_goal_results` — 旧 session (May 22-23)，可能已完成

**磁盘:** 38G 可用 / 250G (86%) ⚠️ 偏高

---

## 4. cqa1-33015 — 4× RTX 4090 D (24GB)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 10313/24564 MiB | 11% | 运行中 (eval_pi05 random k=0.9 object) |
| 1 | 10324/24564 MiB | 5% | 运行中 (eval_pi05 random k=0.95 object) |
| 2 | 10264/24564 MiB | 19% | 运行中 (eval_pi05 l2norm k=0.3 goal) |
| 3 | 1/24564 MiB | 0% | **空闲** |

**TMUX Sessions (2):**
- `eval_pi05_random_k09_object_seed42_v2` — π0.5 random k=0.9, libero_object
- `eval_pi05_random_k095_object_seed42_v2` — π0.5 random k=0.95, libero_object

**磁盘:** 115G 可用 / 250G (55%)

---

## 汇总表

| 服务器 | GPU 0 | GPU 1 | GPU 2 | GPU 3 | 磁盘可用 |
|--------|-------|-------|-------|-------|---------|
| westd-38929 | 🔴 eval xvla | 🔴 eval xvla | 🟢 **空闲** | 🔴 eval xvla | 52G (20%) |
| westd-27271 | 🔴 eval openvla | 🟢 **空闲** | — | — | 77G (30%) |
| westd-41074 | 🟢 **空闲** | 🟢 **空闲** | 🔴 eval π0.5 | 🔴 eval π0.5 | 38G (14%) ⚠️ |
| cqa1-33015 | 🔴 eval π0.5 | 🔴 eval π0.5 | 🔴 eval π0.5 | 🟢 **空闲** | 115G (45%) |

**可立即使用的 GPU (共 5 块):**
- westd-38929 GPU 2 (96GB Blackwell)
- westd-27271 GPU 1 (96GB Blackwell)
- westd-41074 GPU 0, GPU 1 (2× 96GB Blackwell)
- cqa1-33015 GPU 3 (24GB 4090D)

---
