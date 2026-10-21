# code exp008v3 binary probe grpo

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008v3-binary-probe-grpo_20260518T215451_result.json`
- **Structured JSON:** [`645ad6be93c4fb9e3254.json`](../../sessions/64/645ad6be93c4fb9e3254.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并注册。语法验证通过。

**与 exp-014 的关键差异：**

| | exp-014 (Continuous) | exp-008 v3 (Binary) |
|---|---|---|
| `compute_r1` | `1.0 - p_syc` | `1.0 if p_syc <= 0.5 else 0.0` |
| Probe 更新 | 冻结不变 | 每 500 步用当前模型 activations retrain |
| 输出目录 | `exp014_probe_baseline` | `exp008v3_binary_probe_grpo` |

**Retrain 实现要点：**
- 通过 `training_step` 覆写触发，`_last_retrain_step` 防重复
- `accelerator.unwrap_model` 获取原始模型，`output_hidden_states=True` 提取各 reward layer 最后 token 位置的 hidden states
- 随机采样 50 条训练数据，200 epoch 训练新 `LinearProbe`，训练后替换 `self._probe` 并保存快照
- LoRA / DeepSpeed / 超参全部与 exp-014 一致，保证公平对比

---
