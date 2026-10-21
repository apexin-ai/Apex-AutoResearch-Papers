# ops fix eval cuda23

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_eval_cuda23_20260525T113927_result.json`
- **Structured JSON:** [`e2ceffbfba9de1e40586.json`](../../sessions/e2/e2ceffbfba9de1e40586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 运行正常。

**总结**：

**修复的 3 个问题**：
1. **config_name**：`baseline_object_pudding` 不存在于 openpi config 注册表 → 使用 `pi05_libero`（模型架构完全匹配）
2. **LoRA state_dict 不匹配**：A1 checkpoint 含手动 LoRA keys (`.base.weight`/`.lora_A`/`.lora_B`)，`--model_type a1` 按非 LoRA 加载 → 改用 `--model_type lora_baseline`（该路径先注入 LoRA 再加载 safetensors）
3. **GPU 分配错误**：eval 脚本 line 1127 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` 覆盖 shell 的 CUDA_VISIBLE_DEVICES，`--gpu 0` 导致全部跑到 GPU 0 → 改用 `--gpu 2`/`--gpu 3` 直接指定

**当前状态**：

| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 19055 MiB | 100% | 训练 (phase2_lambda0) PID 168730 |
| 1 | 1 MiB | 0% | 空闲 |
| 2 | 9116 MiB | 37% | eval s1 (seed1_l005) PID 191263 |
| 3 | 9116 MiB | 4% | eval s2 (seed2_l005) PID 191403 |

**正确的 eval 命令**（供后续使用）：
```bash
nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/colliforce-vla && export WANDB_MODE=disabled && python scripts/eval_safelibero.py \
  --checkpoint &lt;CKPT_PATH> \
  --config_name pi05_libero \
  --suite safelibero_object \
  --model_type lora_baseline \
  --pi05 --seed 0 --gpu &lt;GPU_ID>' > logs/eval_xxx.log 2>&1 &
```

---
