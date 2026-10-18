# audit gpu full status 0527 loop15

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_full_status_0527_loop15_20260527T021836_result.json`
- **Structured JSON:** [`848001f14c4fd12bacf7.json`](../../sessions/84/848001f14c4fd12bacf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## GPU 实况审计报告 — 2026-05-27 ~10:30 UTC

### westd-38929 — 4× RTX PRO 6000 Blackwell

| GPU | Mem Used | Util% | PID | Experiment | Progress | ETA (est.) |
|-----|----------|-------|-----|-----------|----------|------------|
| 0 | 15964 MiB | 71% | 949253 | openvla attn k=0.95 **goal** | Task 4/10, 2.3 eps/min | ~2.5h |
| 1 | 16188 MiB | 69% | 949447 | openvla l2norm k=0.95 **libero_10** | Task 2/10, 0.9 eps/min | ~8h |
| 2 | 15470 MiB | 90% | 965423 | openvla attn k=0.75 **goal** (v2) | Task 1/10 Ep40, 1.0 eps/min | ~8h |
| 2 | 16169 MiB | (shared) | 968309 | openvla l2norm k=0.75 **libero_10** (v2) | Task 1/10 Ep10, **0.4 eps/min** | **~20h** |
| 3 | 16188 MiB | 83% | 950007 | openvla attn k=0.95 **libero_10** | Task 2/10, 0.8 eps/min | ~9h |

> **GPU 2 双进程共享，l2norm k=0.75 long v2 极慢(0.4 eps/min)，可能超 deadline。**

### westd-41074 — 4× RTX PRO 6000 Blackwell

| GPU | Mem Used | Util% | PID | Experiment | Progress | ETA (est.) |
|-----|----------|-------|-----|-----------|----------|------------|
| 0 | 16188 MiB | 57% | 32184 | openvla random k=0.95 **libero_10** | Task 2/10 Ep30, 0.7-1.0 eps/min | ~7-10h |
| 1 | 16118 MiB | 47% | 856656 | openvla random k=0.75 **libero_10** | Task 8/10 Ep10, 0.9 eps/min | ~2.5h |
| **2** | **1 MiB** | **0%** | — | **空闲** | — | — |
| 3 | 15780 MiB | 67% | 824210 | openvla attn k=0.75 **libero_10** | Task 9/10 Ep30, 1.0 eps/min | ~1h |

> **GPU 2 确认空闲——eval_openvla_random_k095_object_seed42 已完成(SR=67.4%)，进程已退出。**

### westd-27271 — 2× RTX PRO 6000 Blackwell

| GPU | Mem Used | Util% | PID | Experiment | Progress | ETA (est.) |
|-----|----------|-------|-----|-----------|----------|------------|
| 0 | 15964 MiB | 70% | 609731 | openvla l2norm k=0.95 **goal** | Task 6/10 Ep10, 2.3 eps/min | ~1.7h |
| 1 | 15980 MiB | 84% | 638225 | openvla attn k=0.95 **object** | Task 2/10 Ep40, 2.0 eps/min | ~3.4h |

> 另有 3 个 tmux 残留：`pi05_attn_k075_long` 和 `pi05_attn_k07_long_rerun` 启动即失败（`--prune_mode attention` 不在 choices 中），`pi05_l2norm_k07_long_rerun` 已完成。均无 GPU 占用。

### cqa1-33015 — 4× RTX 4090 D

| GPU | Mem Used | Util% | PID | Experiment | Progress |
|-----|----------|-------|-----|-----------|----------|
| 0 | 0 MiB | 0% | — | **空闲** | — |
| 1 | 0 MiB | 0% | — | **空闲** | — |
| 2 | 0 MiB | 0% | — | **空闲** | — |
| 3 | 0 MiB | 0% | — | **空闲** | — |

> 所有 pi05 实验已完成，无进程残留，无 tmux。

---

## 汇总

### 实际在跑：10 个实验
全部是 OpenVLA 评估，分布在 westd-38929(5)、westd-41074(3)、westd-27271(2)。

### 实际空闲 GPU：5 个
- **westd-41074 GPU 2** — 1× RTX PRO 6000 Blackwell
- **cqa1-33015 GPU 0/1/2/3** — 4× RTX 4090 D

### Registry RUNNING 列表 vs 实际 — **全部 5 个已完成，registry 需更新**

| Registry RUNNING 项 | 实际状态 | 服务器 | 最终 SR |
|---------------------|---------|--------|---------|
| eval_pi05_l2norm_k085_long_seed42 | **已完成** | cqa1-33015 | 77.8% |
| eval_openvla_random_k095_object_seed42 | **已完成** | westd-41074 | 67.4% |
| eval_pi05_random_k07_long_seed42 | **已完成** | cqa1-33015 | 62.4% |
| eval_openvla_random_k075_goal_seed42 | **已完成** | westd-38929 | 72.0% |
| eval_openvla_attn_k075_goal_seed42 | **已完成** | westd-27271 | 67.4% |

### 有进程但不在 Registry 的实验：全部 10 个运行中的

### 已完成但未清理的 tmux/进程
- westd-27271: `pi05_attn_k075_long`(失败)、`pi05_attn_k07_long_rerun`(失败)、`pi05_l2norm_k07_long_rerun`(完成)
- westd-41074: `eval_pi05_attention_k0925_long_seed42`(完成)、`profiling_pi05_latency_westd41074`(闲置)

---

## 建议立即行动

1. **紧急：拆分 westd-38929 GPU 2 的双进程。** l2norm k=0.75 long v2 仅 0.4 eps/min，按当前速度需 ~20h，**将超 deadline**。建议将其中一个迁移到 westd-41074 GPU 2 或 cqa1-33015（如果 OpenVLA 模型可在 4090D 24GB 上运行）。

2. **更新 registry。** 5 个标记为 RUNNING 的实验实际已全部完成，需标记 COMPLETED 并注册结果。

3. **利用 5 个空闲 GPU。** cqa1-33015 的 4 GPU 和 westd-41074 GPU 2 完全空闲。如果还有待跑实验，应立即调度。

4. **清理残留 tmux sessions。** westd-27271 和 westd-41074 各有 2-3 个已完成/失败的 tmux session 占着终端。

5. **修复 pi05 attention prune 参数。** westd-27271 上 `pi05_attn_k075_long` 和 `pi05_attn_k07_long_rerun` 因 `--prune_mode attention` 不在 choices 中而失败——如果还需要这些 pi05 attention 实验，需先修复 `eval_pi05_pruning_libero.py` 的 argparse。

---
