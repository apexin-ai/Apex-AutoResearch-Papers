# code lora baseline eval adapt

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lora_baseline_eval_adapt_20260522T135625_result.json`
- **Structured JSON:** [`dc4aa9f5b14d54bafc51.json`](../../sessions/dc/dc4aa9f5b14d54bafc51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已启动，正在创建模型和注入 LoRA。

**汇报：**

- **代码改动**：`eval_safelibero.py` 新增 `--model_type lora_baseline` 支持，添加 `_load_policy_lora_baseline` 函数。实现方式：用 `PI0Pytorch` 创建非 LoRA 基础模型 → `inject_lora_pi0` 注入 LoRA → `safetensors.load_model` 加载完整 state dict → 手动构建 Policy。
- **Dry-run**：3 episodes × 4 tasks 全部通过，无报错。结果保存到 `/root/autodl-tmp/eval_results/`。
- **正式 eval 已启动**：
  - `eval_lora_spatial` — GPU 1, 50 episodes, safelibero_spatial, log: `/tmp/eval_lora_baseline_spatial_v11.log`
  - `eval_lora_object` — GPU 2, 50 episodes, safelibero_object, log: `/tmp/eval_lora_baseline_object_v11.log`
- **tmux sessions**: `eval_lora_spatial`, `eval_lora_object`

---
