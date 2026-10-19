# code libero download dryrun

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_download_dryrun_20260516T015827_result.json`
- **Structured JSON:** [`26ef2334676e2b7249ff.json`](../../sessions/26/26ef2334676e2b7249ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. LIBERO 数据
- **文件数量**: 97 个 parquet 文件 (`data/chunk-000/file-000~096.parquet`)
- **总大小**: 8.7GB
- **Episodes**: 454 (对应 97 个 parquet，部分 parquet 含多 episode)
- **总 frames**: 66,984
- **Tasks**: 10 个 (e.g. "pick up the orange juice and place it in the basket")

### 2. Dry-run 结果

| perturbation_type | 数据源 | step 0 loss | step 1 loss | exit code | 状态 |
|---|---|---|---|---|---|
| visual | synthetic | 8.8095 | 1.9148 | 0 | PASSED |
| physical | synthetic | 13.5834 | 1.4699 | 0 | PASSED |
| universal | synthetic | 9.8495 | 3.2123 | 0 | PASSED |
| visual | **real data** | 0.0533 | 0.0617 | 0 | PASSED |

注：universal dry-run 有一条预期的 warning: `SpatialAugmentation is a no-op placeholder`

### 3. rank-48 支持
- `--lora_rank` 参数已内置，默认 16，alpha 自动设为 `rank * 2`
- rank-48 real data dry-run: **PASSED**
  - 11,059,200 trainable params (0.31%)，loss=0.0964→0.1014
  - 自动保存到 `checkpoints/lora_universal_r48/`

### 4. 训练启动命令

```bash
# 环境
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/meta_brain_lora_routing

# 单 GPU 各 perturbation type
python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 --lora_rank 16
python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 0 --lora_rank 16
python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 0 --lora_rank 48

# 多 GPU 并行（如有 4 张卡）
python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 &
python phase1/train_lora_expert.py --perturbation_type spatial  --gpu_id 1 &
python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 2 &
python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 3 --lora_rank 48 &

# 关键可选参数
# --no_wandb          禁用 wandb
# --lr 2e-4           学习率（默认）
# --batch_size 2      batch size（默认）
# --num_train_steps 30000  总步数（默认）
# --max_steps N       覆盖 num_train_steps
# --save_interval 1000
```

---
