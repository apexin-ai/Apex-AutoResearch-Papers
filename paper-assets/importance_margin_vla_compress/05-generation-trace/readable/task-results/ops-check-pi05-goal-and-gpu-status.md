# ops check pi05 goal and gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_pi05_goal_and_gpu_status_20260523T081019_result.json`
- **Structured JSON:** [`fa9097b9a30f88882c3a.json`](../../sessions/fa/fa9097b9a30f88882c3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

---

## westd-41074（4× RTX PRO 6000 Blackwell 96GB）

| GPU | 显存使用 | 利用率 | 进程 | 实验 ID | 备注 |
|-----|---------|--------|------|---------|------|
| 0 | 0/96GB | 0% | — | — | **空闲** |
| 1 | 0/96GB | 0% | — | — | **空闲** |
| 2 | 0/96GB | 0% | — | — | **空闲** |
| 3 | 0/96GB | 0% | — | — | **空闲** |

**π0.5 Goal 实验已完成（非死亡）：**
- `eval_pi05_random_k09_goal_seed42` → **SR=58.0%**，15:49 完成
- `eval_pi05_l2norm_k07_goal_seed42` → **SR=71.2%**，15:36 完成

tmux 会话残留：`smolvla_spatial`（已完成 spatial baseline）、`xvla_long`（已完成 xvla_long_l2norm_k09）。另有 http.server 占 port 18765。

---

## westd-38929（4× RTX PRO 6000 Blackwell 96GB）

| GPU | 显存使用 | 利用率 | 进程 | 实验 ID | 备注 |
|-----|---------|--------|------|---------|------|
| 0 | 5.1/96GB | 1% | eval_xvla_pruning_libero.py | xvla_l2norm_k07_long_v2 (libero_10, domain_id=3) | 刚启动，Ep 24/50，大部分 FAIL |
| 1 | 0/96GB | 0% | — | — | **空闲** |
| 2 | 0/96GB | 0% | — | — | **空闲** |
| 3 | 0/96GB | 0% | — | — | **空闲** |

---

## westd-27271（显示 2 GPU，非预期的 4 GPU）

| GPU | 显存使用 | 利用率 | 进程 | 实验 ID | 备注 |
|-----|---------|--------|------|---------|------|
| 0 | 20.9/96GB | 94% | 2 个进程 | ① xvla_random_k05_goal_seed42 (Ep 24/50) ② openvla_baseline_spatial_correct_seed42 (Task 6/10, ~78-90% SR) | 两个实验共享 GPU 0 |
| 1 | 4.4/96GB | 0% | eval_xvla_attention_pruning | xvla_attn_attention_last_k0.9_object | **已完成**，0/20=0% SR（dry run 2eps） |

⚠️ nvidia-smi 只显示 2 张 GPU，你预期 4 张。

---

## cqa1-33015（4× RTX 4090 D 24GB）

| GPU | 显存使用 | 利用率 | 进程 | 实验 ID | 备注 |
|-----|---------|--------|------|---------|------|
| 0 | 10.2/24GB | 1% | eval_pi05_pruning_libero.py | pi05_l2norm_k050_object_seed43 | Task 1 done, 22% cumulative |
| 1 | 10.2/24GB | 58% | eval_pi05_pruning_libero.py | pi05_random_k050_object_seed43 | Task 2, Ep 30/50 |
| 2 | 10.3/24GB | 24% | eval_pi05_pruning_libero.py | pi05_l2norm_k070_object_seed43 | Task 2, Ep 30/50, ~93% |
| 3 | 10.3/24GB | 7% | eval_pi05_pruning_libero.py | pi05_random_k070_object_seed43 | Task 2, Ep 30/50, ~87% |

---

## 汇总

**空闲 GPU（可用）：**
- westd-41074: GPU 0, 1, 2, 3（全部空闲，共 4 张）
- westd-38929: GPU 1, 2, 3（3 张空闲）
- westd-27271: GPU 1（attention dry run 已完成，可复用）

**需要重跑的实验：无。** π0.5 Goal 两个实验均已正常完成，不是进程死亡。

**正在运行的实验：**
- westd-38929 GPU 0: xvla_l2norm_k07_long_v2（刚开始）
- westd-27271 GPU 0: xvla_random_k05_goal + openvla_baseline_spatial（进行中）
- cqa1-33015 GPU 0-3: 4 个 pi05 object pruning 实验（均在 Task 1-2/10，预计还需数小时）

---
