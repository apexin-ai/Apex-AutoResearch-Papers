# research jax to pytorch conversion

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_jax_to_pytorch_conversion_20260516T161259_result.json`
- **Structured JSON:** [`0b452e81aec27ce24b4f.json`](../../sessions/0b/0b452e81aec27ce24b4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

加载成功：3.50B params, strict=True 无报错。

---

## 总结

### 1. JAX→PyTorch 转换逻辑

**转换脚本**: `/root/openpi/examples/convert_jax_model_to_pytorch.py`

**转换链**:
1. `slice_initial_orbax_checkpoint()` — 用 Orbax 恢复 JAX param tree 为 numpy
2. `slice_paligemma_state_dict()` — Vision (SigLIP 27层) + LLM (Gemma2B 18层)
3. `slice_gemma_state_dict()` — Action Expert (Gemma 300M)
4. Projection params — state_proj, action_in/out_proj, action_time_mlp_in/out

**关键转换规则**:
- Linear kernel: `.transpose()` (JAX [in,out] → PyTorch [out,in])
- Conv: `transpose(3,2,0,1)` (HWIO → OIHW)
- Attention: einsum `[layers, heads, head_dim, hidden]` → 拆分为独立 q/k/v/o proj
- Weight tying: `safetensors.torch.save_model` 自动处理，加载时只存 `lm_head.weight`

### 2. norm_stats

位置: `/root/.cache/openpi/openpi-assets/checkpoints/pi0_libero/assets/physical-intelligence/libero/norm_stats.json`

```
state:   mean[:7] = [-0.0465, 0.0344, 0.7646, 2.9723, -0.2205, -0.1256, 0.0269]
actions: mean[:7] = [0.0667, 0.064, -0.805, -2.9717, 0.2274, 0.1192, -0.0349]
```

**与 base model 的 norm_stats 完全一致**（因为都是从同一 LIBERO 数据集计算）。

### 3. 已转换的 checkpoint

`/root/autodl-tmp/checkpoints/pi0_libero_openpi/` — 已就绪:
- `model.safetensors`: 7GB, 777 keys, bfloat16
- `assets/physical-intelligence/libero/norm_stats.json`: ✓
- 验证通过: `load_pi0_model()` strict=True 成功，3.50B params

### 4. 转换脚本

已写入 `/root/meta_brain_lora_routing/scripts/convert_jax_to_pytorch.py`（包装 openpi 的转换逻辑）。

### 5. v3 训练命令（4卡并行）

```bash
cd /root/meta_brain_lora_routing && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 从 fine-tuned checkpoint 出发训练 4 个 LoRA experts
python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 --checkpoint /root/autodl-tmp/checkpoints/pi0_libero_openpi --run_prefix v3 &
python phase1/train_lora_expert.py --perturbation_type spatial  --gpu_id 1 --checkpoint /root/autodl-tmp/checkpoints/pi0_libero_openpi --run_prefix v3 &
python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 2 --checkpoint /root/autodl-tmp/checkpoints/pi0_libero_openpi --run_prefix v3 &
python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 3 --checkpoint /root/autodl-tmp/checkpoints/pi0_libero_openpi --run_prefix v3 &
wait
```

关键变化 vs v2: `--checkpoint` 从 `pi0_base` → `pi0_libero_openpi`（fine-tuned 权重作为起点）。

---
