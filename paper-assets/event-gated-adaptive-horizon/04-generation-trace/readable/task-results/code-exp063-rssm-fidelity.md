# code exp063 rssm fidelity

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp063-rssm-fidelity_20260524T185452_result.json`
- **Structured JSON:** [`b4b8fb88515ae3f74366.json`](../../sessions/b4/b4b8fb88515ae3f74366.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_063_rssm_fidelity 完成。结果摘要：

**CROSS-MODEL COMPARISON**

| Model | Test | Obs MSE | Reward MAE |
|-------|------|---------|------------|
| baseline_s1 | dt1_single | 13.70 | 0.042 |
| baseline_s1 | dt2_chained | 20.62 | 0.063 |
| exp_008d (collapsed) | dt1_single | 26.93 | 0.054 |
| exp_008d (collapsed) | dt2_chained | 36.93 | 0.076 |
| exp_008d (collapsed) | dt2_single | 42.02 | **0.146** |

**KEY FINDINGS**

- Baseline dt2/dt1 (chained): obs_mse **1.505x**, reward **1.483x**
- Collapsed dt2/dt1 (single, via dt_embedding): obs_mse **1.560x**, reward **2.695x**
- Collapsed single/chained dt2: obs_mse **1.138x**, reward **1.926x**

**Fidelity gap confirmed**: 即使 exp_008d 模型在 dt=2 转移上训练过，其 dt=2 单步预测的 reward MAE 仍然是 dt=1 的 2.7 倍。dt_embedding 的单步预测甚至比 2x chained dt=1 更差（obs_mse 高 13.8%，reward_mae 高 92.6%），说明 dt_embedding 并未学到忠实的多步动力学，支持 "delusional critic" 假说。

结果已保存至 `logdir/exp_063_rssm_fidelity/results.json`，artifact 已注册 (`art_20260524_58cc25`)。

---
