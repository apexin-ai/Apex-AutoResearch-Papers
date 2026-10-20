# analysis gradient aggregation audit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_aggregation_audit_20260525T080605_result.json`
- **Structured JSON:** [`0d6ca7bf205e46bc43f6.json`](../../sessions/0d/0d6ca7bf205e46bc43f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果令人意外——现在汇总全部发现。

---

## 调查报告：梯度聚合方法不一致

### 1. 原始脚本位置

| 脚本 | 服务器 | 路径 |
|------|--------|------|
| 原始 mixed-seed 梯度分析 | westd-34685 | `/root/occsafe_vla/analysis/gradient_analysis.py` |
| same-seed 梯度分析 | westd-10894 | `/root/occsafe_vla/analysis/gradient_analysis.py` |
| gradient_dose_response_s0 | westd-10894 | `/root/autodl-tmp/analysis/gradient_dose_response_s0/gradient_dose_response_s0.py` |

### 2. 聚合方法精确对比

**原始脚本 (`gradient_analysis.py`)：**
```python
# 损失函数：L1 action loss（~0.15-0.22）
pred_actions = action_head.predict_action(act_hidden)
action_loss = nn.L1Loss()(gt_actions, pred_actions)

# 梯度计算：per-batch torch.autograd.grad
action_grads = torch.autograd.grad(action_loss, all_encoder_params, ...)

# 聚合：per-layer L2 norm → mean across 201 batches → mean across 51 layers
flat_a = torch.cat([g.float().reshape(-1) for g in action_grads])
stats = {"action_grad_norm": flat_a.norm().item()}
```

**新脚本 (`gradient_dose_response_s0.py`)：**
```python
# 损失函数：CE language model loss（~24）
output = model(input_ids=..., labels=batch_labels)
loss = output.loss / num_batches
loss.backward()  # 梯度累积 4 batches

# 梯度计算：读 param.grad（累积后）
layer_grads[key].append(param.grad.detach().float().flatten())

# 聚合：per-layer L2 norm → mean across vision layers
action_grad_norm = action_grads[key].norm().item()
```

**三个关键差异：**

| 维度 | 原始脚本 | 新脚本 |
|------|---------|--------|
| 损失函数 | L1 action loss (~0.15) | CE LM loss (~24), 包含所有 token |
| 梯度路径 | action_head → hidden_states → LM → vision | LM_head → LM → vision |
| 聚合 | per-batch 独立计算 norm, 再 mean across batches | 累积 4 batches 的梯度再算 norm |

### 3. 用 retrained same-seed checkpoints 的复现结果

在 westd-10894 上跑验证脚本，同时计算两种梯度 norm（20 batches, seed 42）：

```
Metric                         Vanilla       Detach     D/V ratio
─────────────────────────────────────────────────────────────────
L1 action loss grad norm       0.138974     0.159509      114.8%
CE loss grad norm                5.0132       6.2222      124.1%
```

**原始 mixed-seed 数据回顾：**
- Detach_BN_**s2**: mean_action_grad_norm = 0.004931
- Vanilla_**s0**: mean_action_grad_norm = 0.126248
- ratio = 3.9%

### 4. 结论

**论文 §4.3 的 1-13% ratio 不可用 same-seed checkpoints 复现。**

根本原因不是聚合方法差异，而是**实验设计问题**：

1. **原始实验比较了不同 seed 的 checkpoints**：`ablation_occ_detach_s2`（seed 2）vs `vanilla_retrain_s0`（seed 0）。不同 seed 导致完全不同的训练数据顺序和收敛状态。

2. **same-seed retrained checkpoints 的 ratio 是 ~115%**（L1 loss）和 ~124%（CE loss）。Detach 的视觉编码器梯度 norm 实际上略大于 Vanilla，而非论文声称的 1-13%。

3. **gradient_dose_response_s0 的 78% ratio** 方向正确（接近 1:1），但因使用 CE loss 而非 L1 action loss，数值与原始方法不直接可比。

4. **关于论文的建议**：§4.3 的梯度分析数据依赖于 mixed-seed 比较，该结论不稳健。应使用 same-seed checkpoints 重做梯度分析。如果 Detach 的核心 claim 是"减少辅助损失对 action gradient 的干扰"，需要比较的是 **有/无 OCC loss 时的 action gradient 变化**，而非跨条件的绝对 gradient norm 大小。

---
