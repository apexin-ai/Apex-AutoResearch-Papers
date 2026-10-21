# ops urgent dual gpu check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-dual-gpu-check_20260516T203550_result.json`
- **Structured JSON:** [`6a33ae2cc2f1ede8b53b.json`](../../sessions/6a/6a33ae2cc2f1ede8b53b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## 状态报告

### 1. GPU 状态
| GPU | 状态 | 进程 | 显存 | 利用率 |
|-----|------|------|------|--------|
| 0 | **忙** | d_b=64 sweep 训练 (PID 262949) | 65.7/97.9 GB | 99% |
| 1 | **空闲** | 无 | 0/97.9 GB | 0% |

### 2. BCE+Gumbel+Lagrangian 3-LR 结果

全部 3 个 LR 训练已完成（今天 03:16–04:11 CST），checkpoint 存在，**尚未跑 eval**：

| LR | Final BCE Loss | Final Sparsity | λ_final | Checkpoint |
|----|---------------|----------------|---------|-----------|
| 1e-4 | 0.7158 | 0.514 | 4.00 | ✅ `bce_framework_lr1e4/predictor_bce_gumbel.pt` |
| 1e-3 | 0.6781 | 0.506 | 2.00 | ✅ `bce_framework_lr1e3/predictor_bce_gumbel.pt` |
| 3e-3 | **0.6632** | 0.504 | 0.50 | ✅ `bce_framework_lr3e3/predictor_bce_gumbel.pt` |

观察：lr=3e-3 BCE loss 最低；lr=1e-4 收敛慢且 loss 显著高。

### 3. d_b Sweep 状态

| d_b | 状态 | 进度 |
|-----|------|------|
| 64 | **训练中** | Step 870/1000（~87%，预计几分钟内完成） |
| 256 | 未开始 | 等 64 完成后自动启动 |
| 512 | 未开始 | 等 256 完成后自动启动 |

脚本 `run_db_sweep.sh` 顺序执行 train→eval，每个 d_b 结束后自动 eval。

### 4. λ 曲线数据

4 个 run，完整度良好：
- `kl_30pct_s42`: target=0.3, 1000 steps, λ_max=5000
- `kl_40pct_s42`: target=0.4, 1000 steps, λ_max=5000
- `kl_50pct_s42`: target=0.5, 200 steps, λ_max=1000
- `kl_70pct_s42`: target=0.7, 1000 steps, λ_max=1000

每个 run 约 109 数据点（前 10 步逐步 + 之后每 10 步）。

### 5. 建议立即执行

**GPU 1 空闲 → 启动 BCE framework 3-LR eval**（不影响 GPU 0 的 d_b sweep）。

是否在 GPU 1 上跑 3 个 BCE framework checkpoint 的 WikiText-2 eval？

---
