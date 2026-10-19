# code eval script adapt

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval_script_adapt_20260520T013841_result.json`
- **Structured JSON:** [`36ee0d376f1405b00af9.json`](../../sessions/36/36ee0d376f1405b00af9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证全部通过。

**总结：三种 model_type 的加载逻辑和 A3 推理时 refinement**

| model_type | 模型加载 | 推理行为 |
|---|---|---|
| **baseline** | `create_trained_policy()` 加载 openpi native LoRA checkpoint，原始流程不变 | 标准 `policy.infer()` |
| **a1** | 同 baseline（native LoRA），额外加载 `sdf_decoder.pt` + `ee_extractor.pt` 用于分析 | 标准推理 + SuffixOutCapture hook 捕获特征 → SDF decoder 计算碰撞距离 → 仅记录日志，不修改动作 |
| **a3** | 加载 `gemma_2b` / `gemma_300m` base（非 LoRA config），手动 `inject_lora()` 注入 LoRALinear wrappers，从 `lora_params.pt` 加载 LoRA 权重，再加载 SDF modules | 标准推理后执行 `_refine_action_a3`：用 EE extractor 预测下一步末端位置 → SDF decoder 计算该点 SDF 值 → 若 SDF < margin，沿 ∂SDF/∂position 梯度方向偏移 action[:3]，步长 = `refine_alpha` |

**A3 推理时 refinement 细节**（`_refine_action_a3`）：
1. `torch.enable_grad()` 上下文中，将 EE 预测位置设为 `requires_grad=True`
2. SDF decoder 前向传播得到 `sdf_val`
3. 若 `sdf_val < refine_margin`，`torch.autograd.grad` 计算 ∂SDF/∂position
4. 梯度 L2 归一化（`+ 1e-8` 数值稳定性），乘以 `refine_alpha`
5. 加到 `action[:3]` 上，将动作推离碰撞边界

---
