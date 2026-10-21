# code crm training prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_crm-training-prep_20260513T200232_result.json`
- **Structured JSON:** [`2c7236826ac689251ad2.json`](../../sessions/2c/2c7236826ac689251ad2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总如下：

---

## 产出

### 1. train_crm.py 头部 80 行
已确认，Two-phase 架构：Phase 1 precompute (GPU) → Phase 2 train (CPU/GPU)。入口 `main()` → `train(args)`。

### 2. argparse 参数列表

| 参数 | 类型 | 默认值 |
|------|------|--------|
| `--benchmark` | str nargs='+' | `["spatial"]` |
| `--epochs` | int | 50 |
| `--batch_size` | int | 32 |
| `--lr` | float | 1e-3 |
| `--seed` | int | 42 |
| `--output_dir` | str | `/root/autodl-tmp/checkpoints/crm/` |
| `--cache_dir` | str | `/root/autodl-tmp/crm_cache/` |
| `--K` | int | 10 |
| `--obs_dim` | int | 960 |
| `--hidden_dim` | int | 256 |
| `--aug_noise_min` | float | 0.02 |
| `--aug_noise_max` | float | 0.1 |
| `--aug_ratio` | float | 0.5 |
| `--precompute` | flag | - |
| `--auto` | flag | - |
| `--val_split` | float | 0.1 |
| `--log_every` | int | 50 |

### 3. manifest.json (spatial)
```json
{
  "benchmark": "spatial",
  "n_samples": 2402,
  "K": 10,
  "obs_dim": 960,
  "action_dim": 6,
  "h_eff": 5
}
```

Cache 文件：`obs_features.pt` (8.8MB), `k_samples.pt` (2.7MB), `expert_actions.pt` (276KB) + 5 个 partial shards。

### 4. CRM 模型结构

**CRM** (`src/crm.py`): `ConformalRefinementModule(nn.Module)`
- Input: 1030D = 30 (mean_action) + 40 (uncertainty_features) + 960 (obs_features)
- Net: Linear(1030→256) → ReLU → Linear(256→256) → ReLU → Linear(256→30)
- Residual: output = mean_action + delta（最后一层初始化为 zero）
- **337,438 params**

**CGS** (`src/cgs.py`): `ConformilizedGaussianScoring`
- Input: (B, K=10, H_eff=5, D=6)
- Output: uncertainty_features (B, 40) = per_dof_std(30) + conformal_radius(5) + log_volume(5)，mean_action (B, 30)

### 5. 草拟启动命令

**仅 spatial（object cache 还没好）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement && \
python src/train_crm.py \
  --benchmark spatial \
  --epochs 50 \
  --batch_size 32 \
  --lr 1e-3 \
  --K 10 \
  --seed 42
```

**spatial + object（object precompute 完成后）：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement && \
python src/train_crm.py \
  --benchmark spatial object \
  --epochs 50 \
  --batch_size 32 \
  --lr 1e-3 \
  --K 10 \
  --seed 42
```

所有默认值和任务要求的参数一致，无需额外指定 `--cache_dir` 和 `--output_dir`（默认值已正确）。不需要指定 GPU——训练会自动检测 CUDA，2402 samples + 337K params 在 CPU 上也能跑完（约几分钟）。

### 6. dry-run 结果

| 检查项 | 结果 |
|--------|------|
| `--help` 解析 | ✅ |
| CRM 实例化 | ✅ 337,438 params |
| CGS forward | ✅ uf=(4,40), ma=(4,30) |
| CRM forward | ✅ output=(4,30) |
| spatial cache 加载 | ✅ 2402 samples, shapes 全部匹配 |
| object cache | ❌ 空目录，precompute 还在进行中 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "benchmark": "spatial",
    "n_samples": 2402,
    "K": 10,
    "obs_dim": 960,
    "action_dim": 6,
    "h_eff": 5
  }
}
```

</details>

---
