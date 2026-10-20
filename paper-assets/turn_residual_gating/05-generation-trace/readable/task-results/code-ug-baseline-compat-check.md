# code ug baseline compat check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ug_baseline_compat_check_20260518T192003_result.json`
- **Structured JSON:** [`2fd9e61bf677377a5dfd.json`](../../sessions/2f/2fd9e61bf677377a5dfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. Uniform gate 兼容 v7 新 loss？**是，完全兼容。**

三个关键点全部通过：

**`get_gate_values(with_grad=True)`** — 兼容。这个方法定义在 `ThreadGatedModel` 上（threadgate.py:157-160），返回 `self._gate_values_with_grad`。该字典在 `_make_hook`（line 130-131）中对**两种 gate type 都会填充**：hook 通过 `self.gate_type` 分支调用对应 gate network（line 123-126），但无论走哪个分支，都执行 `self._gate_values_with_grad[layer_idx] = gate`。

**Gate diversity loss** — 兼容。train_phase2.py:259-266 只遍历 `gate_values_grad` 字典算 `per_layer_means` 的 std，不区分 gate type。UniformGateNetwork 的 gate 值同样有层间差异（每层独立的 `constant_vector` + `fc1/fc2`），diversity loss 正常工作。

**`mse_target` GAR loss** — 兼容。gar.py:196-204 只依赖 `gar_per_turn` 的 tensor 值，与 gate type 完全无关。

### 2. 无需修改

代码路径完整，没有遗漏的条件分支。

### 3. UG baseline 训练命令

config.py 的默认值已经是 v7 参数（`mse_target`, `lambda_gate_div=1.0`, `min_gate_std=0.05`），所以只需改 `--gate-type` 和 `--output-dir`：

```bash
cd /root/turn_residual_gating && python src/train_phase2.py \
  --gate-type uniform \
  --output-dir /root/turn_residual_gating/checkpoints/phase2_ug_s42 \
  --gar-loss-mode mse_target \
  --gar-target 0.5 \
  --lambda-gar 2.0 \
  --lambda-gate-div 1.0 \
  --min-gate-std 0.05 \
  --init-bias 2.0 \
  --lr 2e-4 \
  --grad-accum 8 \
  --epochs 3 \
  --seed 42
```

（显式写出所有参数确保与 v7 TG 实验完全对齐，虽然这些都是 config.py 默认值。）

---
