# code mvp2 prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp2-prep_20260514T060832_result.json`
- **Structured JSON:** [`544ff340d5cc9b1423cd.json`](../../sessions/54/544ff340d5cc9b1423cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改完成。汇总如下：

---

## 修改汇总

### 1. `training/sft_trainer.py`
- `DEFAULT_MODEL` → `"/root/autodl-tmp/models/Qwen3-4B"`（本地模型路径）
- `attn_implementation` → `"sdpa"`（替代 flash_attention_2）
- 头部注释已经引用 `deepspeed_zero2.json`，无需改动

### 2. `training/grpo_trainer.py`
- `--model_name` default → `"/root/autodl-tmp/models/Qwen3-4B"`
- `attn_implementation` → `"sdpa"`
- 头部注释 `deepspeed_zero3.json` → `deepspeed_zero2.json`
- 新增 `--tau_start`（default=0.3）和 `--tau_end`（default=0.5），替换原 `--tau`
- `CEDRewardWrapper` 新增 tau 线性调度：接受 `tau_start`/`tau_end`/`total_steps`，通过内部计数器 `_call_count` 实现 `tau = tau_start + (tau_end - tau_start) * (step / total_steps)`
- `main()` 中根据 dataset 大小和训练参数计算 `total_steps` 传入 wrapper

### 3. `rewards/ced_reward.py`
- **无需修改**。确认 `compute_ced_reward()` 第236-237行：`hard_negative_sents` 为空时 `p_neg = 0.0`，奖励退化为 `p_pos * I(p_pos > tau)` = flat NLI，行为正确

### 4. `training/smoke_test.py`
- `MODEL_NAME` → `"/root/autodl-tmp/models/Qwen3-4B"`
- `attn_implementation` → `"sdpa"`
- `DS_CONFIG.zero_optimization.stage` → 2，移除 `offload_param`，移除 stage3 专属参数，添加 ZeRO-2 参数（`allgather_bucket_size`、`allgather_partitions`）
- `NUM_GENERATIONS` 已为 4，无需改动

---

## MVP-2 训练计划

### Phase 1: SFT warmup（~3h）
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.sft_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --output_dir /root/autodl-tmp/freige/sft_output \
    --num_epochs 3 --per_device_batch_size 1 --gradient_accumulation_steps 16 \
    --learning_rate 2e-4 --wandb_run_name sft-warmup-v1
```

### Phase 2: GRPO 三路对比（每路 ~2-3h）

**Stage 1: extraction-only**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 1 --output_dir /root/autodl-tmp/freige/grpo_s1 \
    --reward_device cpu --wandb_run_name grpo-s1-extract
```

**Stage 2: flat-NLI**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 2 --output_dir /root/autodl-tmp/freige/grpo_s2 \
    --tau_start 0.3 --tau_end 0.5 \
    --reward_device cpu --wandb_run_name grpo-s2-flatnli
```

**Stage 3: CED**
```bash
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.grpo_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --sft_adapter /root/autodl-tmp/freige/sft_output \
    --stage 3 --output_dir /root/autodl-tmp/freige/grpo_s3 \
    --tau_start 0.3 --tau_end 0.5 \
    --reward_device cpu --wandb_run_name grpo-s3-ced
```

### 预计 GPU 时间

| 阶段 | 4x RTX 5090 预估 | 说明 |
|------|-------------------|------|
| SFT warmup | ~3h | 3 epochs, ~3k docs, QLoRA |
| GRPO Stage 1 | ~2h | 1 epoch, 无 NLI 模型开销 |
| GRPO Stage 2 | ~3h | 1 epoch, CPU 上跑 DeBERTa |
| GRPO Stage 3 | ~3h | 1 epoch, CPU 上跑 DeBERTa + hard neg |
| **总计** | **~11h** | 三路 GRPO 可并行则 ~6h |

---
