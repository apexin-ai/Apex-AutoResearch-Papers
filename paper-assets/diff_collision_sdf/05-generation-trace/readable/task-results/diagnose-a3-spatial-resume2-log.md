# diagnose a3 spatial resume2 log

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a3_spatial_resume2_log_20260521T081320_result.json`
- **Structured JSON:** [`30a9664a4e019abd7b6b.json`](../../sessions/30/30a9664a4e019abd7b6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 系统状态
- **GPU**: 2× NVIDIA RTX PRO 6000 (96GB each), 空闲，无进程运行
- **磁盘**: `/root/autodl-tmp` 250GB，已用 71GB (29%)，正常
- **结论**: 不是硬件/资源问题

---

### 4 个日志文件，2 种不同错误

两个实验 (a3_spa_s0, a3_obj_s0) 各有 `train_resume.log` 和 `train_resume2.log`，错误模式完全一致：

---

#### 错误 1: train_resume.log（第 3 次失败）— LoRA 注入路径错误

```
File "/root/colliforce-vla/scripts/train_a3_hook.py", line 118, in inject_lora
    pali_layers = model.paligemma_with_expert.paligemma.language_model.model.layers
AttributeError: 'GemmaModel' object has no attribute 'model'
```

`GemmaModel` 没有 `.model` 子属性。正确路径应该是 `.language_model.layers` 而不是 `.language_model.model.layers`（多了一层 `.model`）。**训练未开始就崩溃。**

---

#### 错误 2: train_resume2.log（第 4 次失败，当前）— LoRALinear 缺少 .weight

```
Training:  67%|██████▋   | 20000/30000  (spa)
Training:  73%|███████▎  | 22000/30000  (obj)

File "/root/colliforce-vla/scripts/../openpi/src/openpi/models_pytorch/pi0_pytorch.py", line 334, in forward
    self.paligemma_with_expert.paligemma.language_model.layers[0].self_attn.q_proj.weight.dtype
AttributeError: 'LoRALinear' object has no attribute 'weight'
```

resume2 修复了路径问题，LoRA 注入成功了，训练也跑到了 20k/22k 步。但 `pi0_pytorch.py:334` 的 forward 方法里有一行 **dtype 检查代码**直接访问 `q_proj.weight.dtype`——LoRA 注入后 `q_proj` 已经从 `nn.Linear` 变成了 `LoRALinear`，后者不直接暴露 `.weight` 属性。

---

### 根因分析

**根本原因是 LoRA 注入与模型 forward 方法的兼容性问题，有两层：**

1. **`train_a3_hook.py:118`** — LoRA 注入时 GemmaModel 的层级路径写错（已在 resume2 修复）
2. **`pi0_pytorch.py:334`** — forward 方法里硬编码访问 `.weight.dtype`，假设 `q_proj` 是原生 `nn.Linear`。LoRA 注入替换了这些模块后，这个假设不再成立

**修复方案**：`pi0_pytorch.py:334` 那行 dtype 检查需要兼容 LoRALinear。改法：

```python
# 原代码
q_proj = self.paligemma_with_expert.paligemma.language_model.layers[0].self_attn.q_proj
dtype = q_proj.weight.dtype

# 修复：兼容 LoRALinear
q_proj = self.paligemma_with_expert.paligemma.language_model.layers[0].self_attn.q_proj
dtype = q_proj.base_layer.weight.dtype if hasattr(q_proj, 'base_layer') else q_proj.weight.dtype
```

或者根据你的 `LoRALinear` 实现，可能是 `q_proj.original.weight` / `q_proj.linear.weight` 等——取决于 LoRALinear 如何包装原始 Linear。需要检查 `LoRALinear` 类的实现来确认属性名。

---
