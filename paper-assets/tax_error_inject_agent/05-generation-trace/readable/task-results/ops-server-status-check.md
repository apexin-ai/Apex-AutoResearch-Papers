# ops server status check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-status-check_20260516T134839_result.json`
- **Structured JSON:** [`caba8913a987b6bfea1d.json`](../../sessions/ca/caba8913a987b6bfea1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### 1. GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 状态 |
|-----|------|---------|--------|------|
| 0 | RTX 5090 | 0/32GB | 0% | **空闲** |
| 1 | RTX 5090 | 26.7/32GB | 99% | vanilla-s123 训练中 |
| 2 | RTX 5090 | 30.9/32GB | 99% | taxei-s123 训练中 |
| 3 | RTX 5090 | 30.9/32GB | 99% | random-s123 训练中 |

### 2. s123 训练状态

| 模型 | GPU | 进度 | Epoch | 已耗时 | 剩余 | Checkpoint |
|------|-----|------|-------|--------|------|------------|
| vanilla-s123 | 1 | 1310/1635 (80%) | 2.40 | 56m | ~14m | ckpt-545, ckpt-1090 |
| taxei-s123 | 2 | 1500/3387 (44%) | 1.33 | 56m | ~1h11m | ckpt-1129 |
| random-s123 | 3 | 1500/3387 (44%) | 1.33 | 56m | ~1h11m | ckpt-1129 |

vanilla-s123 约14分钟完成；taxei-s123 和 random-s123 还需约1h11m。

### 3. TaxEI s0 Eval 结果

**Clean（无注入）** — `llama31_taxei_s0_clean.json`:
- success_rate: **0.766**

**Injected** — `llama31_taxei_s0_eval.json`:
- recovery_rate: **0.745**, detection_rate: **0.277**
- C1_context_truncation: recovery 0.75, detection 0.167
- C4_observation_masking: recovery 0.727, detection 0.273
- P1_step_order_swap: recovery 0.75, detection 0.25
- P2_sub_goal_deletion: recovery 0.75, detection 0.417

### 4. TaxEI s42 Clean 结果

`llama31_taxei_s42_clean.json`: success_rate: **0.766**

### 5. 新 llama31 系列完整结果汇总

| 模型 | Seed | Clean SR | Recovery Rate | Detection Rate |
|------|------|----------|--------------|----------------|
| **vanilla** s0 | 0 | 0.723 | 0.723 | 0.234 |
| **vanilla** s42 | 42 | 0.723 | — | — |
| **taxei** s0 | 0 | 0.766 | 0.745 | 0.277 |
| **taxei** s42 | 42 | 0.766 | — | — |
| **random** s0 | 0 | 0.745 | 0.745 | 0.255 |
| **random** s42 | 42 | 0.766 | — | — |

旧 v4 checkpoint 的 random recovery 结果：

| 文件 | Recovery Rate | Detection Rate |
|------|--------------|----------------|
| v4_random_recovery_eval_s0 | 0.553 | 0.0 |
| v4_random_recovery_eval_s123 | 0.66 | 0.0 |

### 6. tmux 会话

无活跃 tmux 会话。

### 7. 活跃进程

3 个 `swift sft` 训练进程（PID 277575/277781/277973）正在运行，对应 s123 三组训练。另有 jupyter-lab 和 tensorboard 系统服务。

---
