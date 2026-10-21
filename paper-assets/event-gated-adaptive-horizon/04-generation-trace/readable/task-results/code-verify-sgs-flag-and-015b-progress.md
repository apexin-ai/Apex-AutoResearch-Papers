# code verify sgs flag and 015b progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify_sgs_flag_and_015b_progress_20260515T143126_result.json`
- **Structured JSON:** [`68184a822c508fa7b075.json`](../../sessions/68/68184a822c508fa7b075.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 任务 1: `--reward_dt_emb_detach` 实现状态

**已实现。** 出现在 3 个位置：

| 位置 | 文件:行号 | 作用 |
|------|----------|------|
| 配置 | `configs.yaml:120` | 默认值 `false` |
| 梯度减法 | `models.py:339-355` | **核心逻辑** — 在 optimizer step 前，先算 reward loss 对 `dt_embedding.weight` 的梯度 `_reward_grad`，然后注册 backward hook `grad - _reward_grad`，等效于从 dt_embedding 的总梯度中**减去 reward 分量**（selective stop-gradient）。optimizer step 后立即 remove hook。 |
| 诊断日志 | `models.py:389-409` | 每 1000 步记录 `dt_emb_reward_grad_norm` 和 decoder 梯度范数，用于监控 detach 效果 |

**逻辑总结**：不是简单的 `.detach()`，而是 **gradient surgery** — 通过 backward hook 在反传时从 dt_embedding 的梯度中精确移除 reward loss 的贡献。效果等价于"reward head 看到的 dt_emb 是 detached 的，但 decoder 和 dynamics 仍然可以正常反传梯度到 dt_embedding"。

---

### 任务 2: exp_015b 训练进度

| 指标 | 值 |
|------|----|
| **当前 step** | **40,000** / 105,000 (38.1%) |
| **最新 eval_return** | 201.6 (@ step 35K) |
| **train_return** (@ 40K) | 93.8 ~ 221.6 (4 episodes) |
| **GPU (cuda:1)** | RTX PRO 6000 Black, 2742 MiB / 97887 MiB, **21% 利用率** |
| **FPS** | ~3.8 steps/sec |

**eval_return 趋势**：
- 5K: 31.0 → 15K: 139.3 → 25K: 176.7 → 35K: 201.6 — **稳步上升**

**预计剩余时间**：剩余 65,000 steps，fps ≈ 3.8 → ~17,100 秒 ≈ **4.75 小时**（约今晚 03:15 完成）。

**注意**：cuda:1 利用率仅 21%，说明大部分时间花在 CPU 端（env step / data loading），GPU 间歇空闲，这对 Dreamer 类算法是正常的（交替 env interaction 和 model training）。

---
