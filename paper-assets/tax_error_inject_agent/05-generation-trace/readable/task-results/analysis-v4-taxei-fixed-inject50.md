# analysis v4 taxei fixed inject50

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v4-taxei-fixed-inject50_20260515T012353_result.json`
- **Structured JSON:** [`dfbac22dc2d3d1e11c5e.json`](../../sessions/df/dfbac22dc2d3d1e11c5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验 v4-taxei-fixed-inject50 训练报告

### 状态：训练成功完成

| 指标 | 值 |
|------|-----|
| **EXIT_CODE** | 0（正常退出） |
| **Total steps** | 1635/1635 |
| **Epochs** | 3.0 |
| **Average train_loss** | 0.4335 |
| **Final step loss** | 0.2586 (step 1635) |
| **Final token_acc** | 91.05% |
| **训练时长** | 53m 8s (3188s) |
| **GPU 显存峰值** | 17.99 GiB |
| **训练速度** | ~1.95 s/it |

### Loss 收敛趋势

| 阶段 | Step | Loss | Token Acc |
|------|------|------|-----------|
| 初始 | 5 | 2.948 | 60.3% |
| Epoch 1 中期 | 125 | 0.591 | 82.0% |
| Epoch 1 末 | 545 | ~0.35 | ~88% |
| Epoch 2 末 | 1090 | ~0.28 | ~90% |
| Epoch 3 末 | 1635 | 0.259 | 91.1% |

收敛正常，loss 从 2.95 稳定下降到 ~0.26，无发散或异常波动。

### Checkpoint 信息

- **输出目录**: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/`
- **保存的 checkpoints**:
  - `checkpoint-545` (epoch 1)
  - `checkpoint-1090` (epoch 2)
  - `checkpoint-1635` (epoch 3, final)
- **最终 checkpoint**: `/root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject50/v0-20260515-082759/checkpoint-1635`

### W&B

未使用 W&B（日志中无 wandb 记录）。

### 异常/警告

- bitsandbytes 加载警告（`libnvJitLink.so.13` 缺失），不影响训练（未使用量化）。
- 无其他 error 或 warning。

---
