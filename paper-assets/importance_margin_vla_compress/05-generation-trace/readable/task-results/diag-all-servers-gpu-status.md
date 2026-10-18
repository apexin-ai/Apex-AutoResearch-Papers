# diag all servers gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_all-servers-gpu-status_20260523T165044_result.json`
- **Structured JSON:** [`8989bf98c1e234d371c5.json`](../../sessions/89/8989bf98c1e234d371c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

---

## westd-38929 (4× H800 98GB)

| GPU | Util% | Mem Used/Total | Experiment | Status |
|-----|-------|----------------|------------|--------|
| 0 | 1% | 4.9/98 GB | e5_xvla_attn_last_goal_k05_v2 | ✅ Running, T1/10 |
| 1 | 1% | 4.9/98 GB | e5_xvla_attn_mean_goal_k05_v2 | ✅ Running, T1/10 |
| 2 | 20% | 4.9/98 GB | e5_xvla_attn_rollout_goal_k05_v2 | ✅ Running, T1/10 |
| 3 | 0% | 4.6/98 GB | xvla_random_k05_goal_seed42_v2 | ✅ Running, T1/10 |

- **4 个 E5 Goal k=0.5 v2 实验全部正常启动**，刚开始 ~4 分钟，Task 1/10 进行中
- **eval_e5_xvla_attn_mean_goal_k03: 非崩溃，已正常完成** (EXIT_CODE=0, 29.7min)，结果已保存到 `xvla_attn_attention_mean_k0.3_libero_goal.json`

## westd-27271 (2× H800 98GB)

| GPU | Util% | Mem Used/Total | Experiment | Status |
|-----|-------|----------------|------------|--------|
| 0 | 71% | 16.0/98 GB | openvla_baseline_goal_seed42_v3 | ✅ T6/10, Ep 30/50 |
| 1 | 78% | 16.2/98 GB | openvla_baseline_long_seed42 | ✅ T2/10, Ep 20/50 |

## westd-41074 (4× H800 98GB)

| GPU | Util% | Mem Used/Total | Experiment | Status |
|-----|-------|----------------|------------|--------|
| 0 | — | 0/98 GB | — | 🟢 **空闲** |
| 1 | 3% | 10.5/98 GB | pi05_random_k07 (PID 224308) | ⚠️ 已完成 SR=78.2%, 进程残留 |
| 2 | 33% | 9.9/98 GB | pi05_random_k03 (PID 224557) | ⚠️ 已完成 SR=50.6%, 进程残留 |
| 3 | 43% | 10.5/98 GB | pi05_random_k09 (PID 225108) | ⚠️ 已完成 SR=62.2%, 进程残留 |

- 3 个 random 实验均已完成并保存结果，但 EXIT_CODE=129 (SIGHUP)，python 进程成为孤儿进程仍占 GPU
- 只有 3 个 random 实验 (k03/k07/k09)，不是 4 个

## cqa1-33015 (4× 4090 24.5GB)

| GPU | Util% | Mem Used/Total | Experiment | Status |
|-----|-------|----------------|------------|--------|
| 0 | 14% | 10.3/24.5 GB | pi05_l2norm_k095_goal_v2 | ✅ T6/10, Ep 20/50 (SR≈93%) |
| 1 | 1% | 10.3/24.5 GB | pi05_l2norm_k09_goal_v2 | ✅ T6/10, Ep 20/50 (SR≈95%) |
| 2 | 48% | 10.3/24.5 GB | pi05_l2norm_k07_goal_v2 | ✅ T5/10, Ep 20/50 (SR≈76%) |
| 3 | 50% | 10.1/24.5 GB | pi05_l2norm_k03_goal_v2 | ✅ T4/10, Ep 10/50 (SR≈49%) |

- **GPU 3 不空闲**，l2norm_k03 实验正常运行中

## 汇总

**空闲可用 GPU：**
- westd-41074 GPU 0: 已空闲
- westd-41074 GPU 1-3: kill 残留进程后可用（共 3 个 GPU）

**需要行动：**
- westd-41074 有 3 个孤儿 python 进程 (PID 224308, 224557, 225108) 需要 kill 以释放 GPU 1-3

**无崩溃：**
- eval_e5_xvla_attn_mean_goal_k03 → 正常完成 EXIT_CODE=0
- cqa1-33015 GPU 3 → l2norm_k03 正常运行中

---
