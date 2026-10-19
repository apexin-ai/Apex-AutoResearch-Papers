# prep phase2 commands

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_phase2-commands_20260514T074706_result.json`
- **Structured JSON:** [`bcdbdda17b41f379e2d4.json`](../../sessions/bc/bcdbdda17b41f379e2d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是 Phase 2 完整命令清单。

---

## Phase 2 完整命令清单

### 环境信息
- 服务器: bjb1-18228，4× RTX 4090 (24GB)
- 旧 cache: `/root/autodl-tmp/crm_cache/` (max_demos=10, 6D state buggy, action_dim=6)
- 新 cache: `/root/autodl-tmp/crm_cache_v2/` (max_demos=50, 8D state C1 fix)
- 旧 cache 样本: spatial=12,167, object=14,570 (100 traj each, max_demos=10)
- 新 cache 预估: spatial≈60k, object≈73k (500 traj each, max_demos=50)

---

### Step 1: Precompute（3 shard 并行，GPU 0/1/2）

**Shard 0 (GPU 0):**
```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python src/train_crm.py \
  --precompute \
  --benchmark spatial object \
  --cache_dir /root/autodl-tmp/crm_cache_v2/ \
  --K 10 \
  --shard_id 0 --num_shards 3 \
  --max_demos_per_task 50 \
  --precompute_batch_size 4 \
  --save_every 500
```

**Shard 1 (GPU 1):**
```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=1 python src/train_crm.py \
  --precompute \
  --benchmark spatial object \
  --cache_dir /root/autodl-tmp/crm_cache_v2/ \
  --K 10 \
  --shard_id 1 --num_shards 3 \
  --max_demos_per_task 50 \
  --precompute_batch_size 4 \
  --save_every 500
```

**Shard 2 (GPU 2):**
```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=2 python src/train_crm.py \
  --precompute \
  --benchmark spatial object \
  --cache_dir /root/autodl-tmp/crm_cache_v2/ \
  --K 10 \
  --shard_id 2 --num_shards 3 \
  --max_demos_per_task 50 \
  --precompute_batch_size 4 \
  --save_every 500
```

- **GPU**: 各用 1 块，共 3 块
- **预计时间**: 每 shard ~5-6h（两个 benchmark 串行，每个 benchmark ~44k samples / 3 shards ≈ 14-16k × 0.45s/sample）
- **自动合并**: 最后完成的 shard 自动触发 `_try_merge`，生成 `obs_features.pt` / `k_samples.pt` / `expert_actions.pt` / `manifest.json`
- **支持断点续传**: 每 500 samples 存 partial 文件，中断后重启自动恢复

---

### Step 2: CRM Retrain（1 GPU，等 Step 1 全部完成）

```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python src/train_crm.py \
  --benchmark spatial object \
  --cache_dir /root/autodl-tmp/crm_cache_v2/ \
  --output_dir /root/autodl-tmp/checkpoints/crm_v2/ \
  --K 10 \
  --epochs 50 \
  --batch_size 32 \
  --lr 1e-3 \
  --input_mode full
```

- **GPU**: 1 块
- **预计时间**: ~10-15 min（CRM 仅 337K 参数，训练很快）
- **产出**: `crm_best.pt` + epoch checkpoints 在 `/root/autodl-tmp/checkpoints/crm_v2/`
- **已内置 fix**: `_argmin_base_action` (W2 argmin fix)，`load_libero_demos` 中 8D state (C1 fix)

---

### Step 3: Re-eval（1 GPU，等 Step 2 完成）

```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
TARGET_GPU=0 python run_eval_gpu.py \
  --benchmark spatial \
  --mode acr_vla \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/crm_best.pt \
  --K 10 \
  --n_rollouts 20 \
  --output_file /root/autodl-tmp/eval_results/acr_spatial_v3_postfix/results.json
```

- **GPU**: 1 块（`run_eval_gpu.py` 封装 EGL 设备映射）
- **预计时间**: ~2-3h（10 tasks × 20 rollouts × ≤300 steps）
- **产出**: JSON 结果文件

---

### 依赖关系

```
Step 1 (Shard 0) ─┐
Step 1 (Shard 1) ──┼──▶ Step 2 (Train) ──▶ Step 3 (Eval)
Step 1 (Shard 2) ─┘
        并行                   串行            串行
```

### 注意事项

1. **旧 cache 保留**: 新 cache 写入 `crm_cache_v2/`，旧 `crm_cache/` 不受影响
2. **旧 checkpoint 保留**: 新 checkpoint 写入 `checkpoints/crm_v2/`，旧 `checkpoints/crm/` 不变
3. **max_demos_per_task=50 vs 旧版 10**: 数据量增加 5x，precompute 时间相应增加。如需加速可改回 `--max_demos_per_task 10`（与旧版相同数据量，precompute 降至 ~1h/shard）
4. **GPU 3 空闲**: precompute 用 GPU 0-2，GPU 3 可同时跑其他任务
5. **merge 注意**: 3 个 shard 必须全部完成才能 merge。如某 shard 挂了，重启同参数即可（自动续传），最后完成的 shard 触发 merge
6. **eval 只跑 spatial**: 如需 object benchmark eval，换 `--benchmark object` 并调整 output_file 路径

---
