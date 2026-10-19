# monitor bce sparsity drift

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bce_sparsity_drift_20260515T193848_result.json`
- **Structured JSON:** [`b36cb2ab6e6a7ef19f33.json`](../../sessions/b3/b36cb2ab6e6a7ef19f33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Sparsity Drift 报告：bce_isocompute_s42

### 状态：训练已停止，未到达 step 1000

训练进程不在运行。日志停在 step 500/2700，最后修改时间 03:37:45。无 exit file，无 traceback。

GPU 0 当前被 `eval_spon_supplementary.py`（PID 122406，03:38 启动）占用，很可能是 bce_isocompute_s42 被挤掉或 OOM。

### Sparsity 趋势

| Step | Loss | BCE | Reg | Sparsity | LR |
|------|------|-----|-----|----------|----|
| 100 | 0.6711 | 0.6628 | 0.0082 | **0.582** | 1.00e-3 |
| 200 | 0.6570 | 0.6504 | 0.0066 | **0.566** | 9.96e-4 |
| 300 | 0.6494 | 0.6437 | 0.0057 | **0.557** | 9.85e-4 |
| 400 | 0.6457 | 0.6402 | 0.0054 | **0.554** | 9.68e-4 |
| 500 | 0.6461 | 0.6406 | 0.0055 | **0.555** | 9.43e-4 |

### 分析

1. **Sparsity 趋势**：从 0.582 下降到 0.555，有收敛趋势但在 step 400-500 已停滞在 0.554-0.555，仍高于目标 0.50 约 +0.055。
2. **漂移模式确认**：与 bce_comp_staged_s42 一致——BCE 训练的 sparsity 容易偏高且难以拉回目标值。Reg loss 从 0.0082 降到 0.0055 但 sparsity 下降速度已放缓。
3. **step 1000 预判**：按 step 300-500 的趋势（每 100 步仅下降 ~0.001），外推到 step 1000 sparsity 约 **0.550**，**大概率 > 0.55**。

### 需要关注

- **训练已死**：bce_isocompute_s42 不在运行，需要重启。
- **GPU 冲突**：GPU 0 当前被 eval_spon_supplementary.py 占用，需等其完成或杀掉后再重启训练。
- 即使重启，sparsity 漂移问题大概率持续——可能需要调大 reg 权重或换 sparsity 约束策略。

---
