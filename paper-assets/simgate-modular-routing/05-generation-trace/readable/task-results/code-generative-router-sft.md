# code generative router sft

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_generative-router-sft_20260514T071905_result.json`
- **Structured JSON:** [`617811cb0bdaa5b14413.json`](../../sessions/61/617811cb0bdaa5b14413.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出总结：**

1. **代码** — `src/training/generative_router_sft.py` 已部署到 westb-13313
   - 基于 ablation-b 的 `implicit_router_sft.py`，移除了 class_weights 路径，只保留 upsample
   - 默认 batch_size=4, grad_accum=8（有效 batch=32）
   - 数据 upsample internal 从 180→1560（1:1 平衡）+ WeightedRandomSampler
   - 支持 `--max_steps` dry-run、`--upsample_ratio` 控制平衡比例
   - 显式设置 `model.config.pad_token_id`

2. **Dry-run** — 5 步训练 + eval 全部通过，adapter 正常保存

3. **实验注册** — `plan-002-generative-v1` (status=PREPARING)，启动命令：
   ```
   CUDA_VISIBLE_DEVICES=1 WANDB_MODE=offline HF_HUB_OFFLINE=1 python src/training/generative_router_sft.py train \
     --data_dir data/plan-004-implicit \
     --model_name /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
     --epochs 3 --batch_size 4 --gradient_accumulation_steps 8 \
     --output_dir checkpoints/plan-002-generative-v1 --seed 42 --gpu_id 0
   ```

---
