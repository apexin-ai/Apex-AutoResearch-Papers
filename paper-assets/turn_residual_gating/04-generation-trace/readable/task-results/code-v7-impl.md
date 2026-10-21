# code v7 impl

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v7_impl_20260518T183903_result.json`
- **Structured JSON:** [`faa1c75c879aca5e6522.json`](../../sessions/fa/faa1c75c879aca5e6522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个文件语法验证全部通过。变更汇总：

### gar.py — 无变更
`mse_target` 模式已存在（行 196-204）。

### config.py — 无变更
`LAMBDA_GATE_DIV = 1.0` 和 `MIN_GATE_STD = 0.05` 已存在（行 17-18）。

### train_phase2.py — 3 处变更

**1. 新增 `import torch.nn.functional as F`**（行 9）

**2. Label masking 修复**（`__getitem__` 方法）：
- 将 `boundaries` 获取移到 `turn_feats` 之前
- `labels[:] = -100` 先 mask 全部
- 遍历 `boundaries["turns"]`，只对 `role == "assistant"` 的 turn 恢复原始 token

**3. `torch.relu` → `F.relu`**（gate diversity loss 计算处）

### gate_values 梯度处理
`threadgate.py` 的 `get_gate_values(with_grad=True)` 返回 `_gate_values_with_grad`（行 131 存储未 detach 的 gate tensor），训练循环已正确使用 `model.get_gate_values(with_grad=True)` 获取有梯度的 gate 值。梯度链路完整。

其余变更（CLI 参数、gate diversity loss 计算、总 loss 公式、日志输出、config dump）已在外部完成。

---
