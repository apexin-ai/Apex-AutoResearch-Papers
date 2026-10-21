# ops lora baseline eval prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_lora_baseline_eval_prep_20260526T002712_result.json`
- **Structured JSON:** [`b1b5046e52e1a0aa76f5.json`](../../sessions/b1/b1b5046e52e1a0aa76f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。汇报如下：

---

### 1. eval_safelibero.py 版本
**是修复版**。1357 行，包含 `Using external CUDA_VISIBLE_DEVICES` 检查逻辑（第 1143 行）。**无需同步**。

### 2. Checkpoint 目录
路径不是任务预设的 `/root/colliforce-vla/checkpoints/`，实际在：
- seed0: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/`
- seed1: `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/`

当前进度：两个 seed 都到了 step 28000（有 26000 和 28000 子目录 + best 目录）。目标 step 30000 目录尚未生成，训练仍在进行。

每个 step 目录含 `model.safetensors`，格式正确。

### 3. 修正后的 eval 命令

Seed 0 (GPU 0):
```bash
CUDA_VISIBLE_DEVICES=0 python scripts/eval_safelibero.py \
  --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/30000 \
  --config_name pi05_libero \
  --model_type lora_baseline \
  --suite safelibero_object \
  --pi05 \
  --gpu 0 \
  --output_path /root/autodl-tmp/eval_results/eval_lora_baseline_s0.json
```

Seed 1 (GPU 1):
```bash
CUDA_VISIBLE_DEVICES=1 python scripts/eval_safelibero.py \
  --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed1/30000 \
  --config_name pi05_libero \
  --model_type lora_baseline \
  --suite safelibero_object \
  --pi05 \
  --gpu 1 \
  --output_path /root/autodl-tmp/eval_results/eval_lora_baseline_s1.json
```

### 4. 阻塞项
- **训练未完成**：step 30000 目录尚不存在（当前 28000），需等训练完成后再执行 eval。
- **输出目录**：`/root/autodl-tmp/eval_results/` 可能不存在，执行前需 `mkdir -p /root/autodl-tmp/eval_results/`。
- 如果训练最终 step 不是 30000（例如提前停止或改了总步数），需用 `best/` 子目录替代 `30000`。

---
