# code plan015 k5 crm prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan015-k5-crm-prep_20260513T235543_result.json`
- **Structured JSON:** [`0c6f3729c03f48ac3c9f.json`](../../sessions/0c/0c6f3729c03f48ac3c9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=5 CRM 训练就绪状态报告

### 1. K=5 Cache: **完整可用**

| Benchmark | 样本数 | K | obs_dim | manifest |
|-----------|--------|---|---------|----------|
| spatial | 12,167 | 5 | 960 | OK |
| object | 14,570 | 5 | 960 | OK |

总大小 233MB，两个子目录均有 `obs_features.pt` / `k_samples.pt` / `expert_actions.pt` + `manifest.json`。

### 2. 训练命令格式确认

`--cache_dir` 和 `--output_dir` 均支持。`--K` 参数仅在 precompute 阶段和 manifest 记录中使用，训练阶段直接从 cache 加载，传 `--K 5` 用于元数据一致性。

### 3. 输出目录

K=10 结果在默认目录 `/root/autodl-tmp/checkpoints/crm/`（已完成 50 epochs）。`scalar_unc/` 下有另一个训练进行中（3 epochs）。K=5 应用独立目录避免冲突。

### 4. GPU 状态

GPU 0 占用 15.7GB（有任务运行中），GPU 1-3 基本空闲。

### 5. 推荐提交命令

```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 nohup python src/train_crm.py \
  --benchmark spatial object \
  --epochs 50 \
  --batch_size 32 \
  --lr 1e-3 \
  --K 5 \
  --seed 42 \
  --cache_dir /root/autodl-tmp/crm_cache_k5/ \
  --output_dir /root/autodl-tmp/checkpoints/crm/k5/ \
  > /root/autodl-tmp/checkpoints/crm/k5/train.log 2>&1 &
```

### 6. 潜在问题

- **GPU 0 被占用**（15.7GB），需等当前任务结束或改用空闲 GPU（`CUDA_VISIBLE_DEVICES=1`）
- **输出目录 `/root/autodl-tmp/checkpoints/crm/k5/` 尚不存在**，需提交前 `mkdir -p` 或依赖脚本的 `mkdir(parents=True)`（代码中 output_dir 未见自动创建，需确认）
- scalar_unc 训练正在 GPU 0 上跑，如果要等它跑完再提交 K=5，用 `CUDA_VISIBLE_DEVICES=0` 即可；如果想并行，用 `CUDA_VISIBLE_DEVICES=1`

---
