# diagnose exp 001 and 004 ssh recovery

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_and_004_ssh_recovery_20260513T152619_result.json`
- **Structured JSON:** [`e3a5704d0d54577f000d.json`](../../sessions/e3/e3a5704d0d54577f000d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. 进程状态：两个进程均健康运行

| 实验 | PID | GPU | 显存占用 | GPU Util |
|------|-----|-----|---------|----------|
| exp_001_baseline | 9409 | GPU 0 (RTX PRO 6000 Black) | 4156MiB / 97887MiB | 19% |
| exp_004_event_gated_v3 | 36645 | GPU 1 (RTX PRO 6000 Black) | 4340MiB / 97887MiB | 0%* |

*GPU 1 的 0% 是瞬时采样，进程仍在运行（metrics.jsonl 最后写入 23:26，与 nvidia-smi 时间一致）。

---

### 2. exp_001_baseline 最新指标（step 365K）

| 指标 | 值 |
|------|-----|
| **step** | 365,000 |
| **eval_return** | 935.76 |
| **train_return** (step 364K, 4 envs) | 925.5 ~ 963.0 |
| **fps** | 7.66 |
| **model_loss** | 3.157 |
| **reward_loss** | 0.302 |
| **kl** | 4.028 |
| **actor_entropy** | -0.990 |
| **update_count** | 90,099 |

趋势：eval_return 从 345K 的 969.8 → 355K 的 941.1 → 365K 的 935.8，略有下降但仍在高位。训练稳定。

---

### 3. exp_004_event_gated_v3 最新指标（step 135K）

| 指标 | 值 |
|------|-----|
| **step** | 135,000 |
| **eval_return** | 342.27 |
| **train_return** (step 136K, 4 envs) | 269 ~ 424 |
| **fps** | 6.81 |
| **gate_scale** | 0.800 |
| **gate_dt_mean** | 2.724 |
| **gate_dt_std** | 1.311 |
| **gate_empirical_entropy** | 1.596 |
| **gate_entropy_ratio** | 0.767 |
| **gate_dt distribution** | dt=1: 18%, dt=2: 33%, dt=3: 23%, dt=4: 16%, dt=5: 8%, dt=6: 3% |
| **actor_entropy** | 3.221 |

gate 分布合理，dt=2 和 dt=3 为主，无退化到全 dt=1 的情况。

---

### 4. 异常警告

**exp_004 的 gate_loss / model_loss 异常大：**
- step 125K: gate_loss = **278,850,976**，model_loss = 278,850,976
- step 135K: gate_loss = **226,705,584**，model_loss = 226,705,584

gate_loss 完全主导了 model_loss（其他 loss 分量在 0.001~5 量级）。虽然 gate_loss 在下降（2.79e8 → 2.27e8），但这个量级是否符合预期需要确认。eval_return 从 352 → 342 略降，训练 return 波动大（10~481），学习不稳定。

---

### 5. Checkpoint 与磁盘

| 实验 | 文件 | 大小 | 最后修改 |
|------|------|------|---------|
| baseline_s1 | latest.pt | 219MB | 23:17 |
| event_gated_v4_s1 | latest.pt | 225MB | 23:19 |

**磁盘：250GB 总量，已用 2.8GB (2%)，剩余 248GB** — 完全充足。

---
