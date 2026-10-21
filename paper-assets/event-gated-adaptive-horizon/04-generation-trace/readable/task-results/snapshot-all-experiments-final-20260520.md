# snapshot all experiments final 20260520

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_snapshot_all_experiments_final_20260520_20260520T110322_result.json`
- **Structured JSON:** [`f98f21c48f4276f460eb.json`](../../sessions/f9/f98f21c48f4276f460eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总表

| exp_id | 服务器 | 步数 | eval_latest | NVE_latest | 状态 |
|--------|--------|------|-------------|------------|------|
| **exp_027_s0_sigma02** (σ=0.2 s0) | bjb1-40020 | **205K** | **558.7** | **0.100** | 运行中，距210K约5K步 |
| exp_029a_s1_sigma02 (σ=0.2 s1) | bjb1-40020 | 75K | 171.2 | 0.398 | 运行中 |
| exp_030a_cheetah_s0_sigma02 (Cheetah σ=0.2) | bjb1-45299 | ~64K (eval@55K) | 31.9 | 1.903 | **运行中⚠️ 疑似崩溃** |
| exp_027_s1 (σ=0.5 s1) | bjb1-45299 | 168K (eval@165K) | 209.5 | 0.539 | 运行中 |

---

### exp_027_s0_sigma02 (σ=0.2 s0) — 详细报告

**尚未完成 210K，当前 205K。**

**Eval 轨迹 (每 10K):**

| Step | eval_return |
|------|-------------|
| 5K | 35.6 |
| 15K | 150.6 |
| 25K | 199.4 |
| 35K | 278.2 |
| 45K | 315.6 |
| 55K | 278.6 |
| 65K | 331.0 |
| 75K | 293.1 |
| 85K | 363.9 |
| 95K | 171.4 |
| 105K | 236.4 |
| 115K | 543.8 |
| 125K | 458.4 |
| 135K | 496.7 |
| 145K | 542.7 |
| 155K | 660.5 |
| 165K | 653.3 |
| **175K** | **821.1** ← 峰值 |
| 185K | 560.5 |
| 195K | 567.9 |
| 205K | 558.7 |

**NVE 轨迹 (每 10K):**

| Step | ve_ratio | value_mean |
|------|----------|------------|
| 15K | 0.019 | 2.9 |
| 25K | 0.096 | 19.2 |
| 35K | 0.188 | 52.2 |
| 45K | 0.301 | 95.0 |
| 55K | 0.523 | 145.8 |
| 65K | 0.565 | 187.1 |
| 75K | 0.611 | 179.1 |
| 85K | 0.467 | 169.8 |
| **95K** | **0.908** ← 最大 | 155.7 |
| 105K | 0.563 | 133.0 |
| 115K | 0.211 | 114.5 |
| 125K | 0.218 | 100.0 |
| 135K | 0.176 | 87.6 |
| 145K | 0.143 | 77.6 |
| 155K | 0.106 | 70.0 |
| 165K | 0.098 | 64.0 |
| 175K | 0.073 | 59.9 |
| 185K | 0.105 | 58.7 |
| 195K | 0.103 | 58.3 |
| 205K | 0.100 | 55.6 |

**关键统计:**
- **Eval 峰值:** 821.1 @ Step 175K
- **末期均值 (175K-205K):** 627.1 (n=4)
- **NVE 全程最大值:** 0.908 @ Step 95K
- **NVE 范围:** [0.019, 0.908]
- **NVE 后半程趋势:** 95K 后持续下降并稳定在 ~0.10，value estimation 收敛良好

---

### 警告: exp_030a Cheetah

Eval 在 35K 达峰 299.5 后急剧崩溃到 55K 的 31.9，同时 VE ratio 飙升到 1.903（value explosion）。该实验可能已不可恢复。

---
