# code acib h prep

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib_h_prep_20260516T195215_result.json`
- **Structured JSON:** [`d0e1ae683396ed5b6cfc.json`](../../sessions/d0/d0e1ae683396ed5b6cfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**代码审查**: ACIB-H 实现完整，无需修改。关键路径：
- `scorer.py:_hard_topk` — 正确的 STE（`mask - soft.detach() + soft`）
- `config.py` — `mode="hard"`, `top_k_ratio=0.8` 默认值就位
- `train_acib.py` — `--mode`/`--top_k_ratio` 参数正确传入 ACIBConfig
- Contrastive/IB/diversity loss 全部兼容 hard mode

**Dry-run**: 10 步完成，checkpoint 正常保存。

**正式训练命令 (ACIB-H@k=0.8, 20000步)**:

```bash
cd /root/acib && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
nohup python3 -u scripts/train_acib.py \
  --model_id lerobot/smolvla_libero \
  --dataset_id lerobot/libero \
  --data_root /root/autodl-tmp/libero_dataset \
  --hidden_dim 64 --alpha 0.01 --beta 0.01 --beta_warmup_steps 1000 \
  --mode hard --top_k_ratio 0.8 \
  --condition_source language --conditioning_mode concat \
  --lambda_contrastive 0.1 --diversity_lambda 0.1 --lambda_ent 0.0 \
  --steps 20000 --batch_size 64 --lr 1e-4 --warmup_steps 1000 \
  --grad_clip 1.0 --save_freq 5000 --dtype bfloat16 \
  --gpu 0 --seed 42 \
  --output_dir /root/acib/outputs/acib_h_k08_s42 \
  --wandb_project acib --wandb_run_name acib_h_k08_s42 \
  > /root/acib/outputs/acib_h_k08_s42/train.log 2>&1 &
```

等 eval 跑完 GPU 空闲后提交即可。

---
