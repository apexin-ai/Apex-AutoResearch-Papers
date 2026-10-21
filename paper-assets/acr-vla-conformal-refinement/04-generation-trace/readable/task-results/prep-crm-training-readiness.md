# prep crm training readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_crm-training-readiness_20260521T154152_result.json`
- **Structured JSON:** [`28599720645d41bb8be0.json`](../../sessions/28/28599720645d41bb8be0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，以下是汇总报告。

---

## CRM Training Pipeline Readiness 报告

### 1. Training mode: `--model pi05` ✅ 支持

- `train_crm.py` 的 `--model` 参数仅作用于 **precompute 阶段**（加载 Pi05Wrapper 提取 2048D features）
- **Training 阶段是 model-agnostic**：从 cache 读取 `obs_features.pt` / `k_samples.pt` / `expert_actions.pt`
- CRM 的 `obs_dim` 从 `manifest.json` 自动读取（`manifest["obs_dim"]`），pi05 cache 会记录为 2048 → CRM 自动配置 `obs_dim=2048`
- 不需要额外传 `--obs_dim` 给 training

### 2. Cache 合并: ⚠️ 需要手动干预

**现状**：
- 只有 `object/` 目录，**`spatial/` 还没开始**
- **没有 `manifest.json`** — precompute 仍在运行
- 总大小 235M，~150 个 partial 文件

**问题**：Shard s5 有**重叠的 partial 文件**（两种粒度共存）：
- 100-sample 粒度：`partial_s5_0_100.pt`, `partial_s5_100_200.pt`, ...
- 500-sample 粒度：`partial_s5_400_900.pt`, `partial_s5_900_1400.pt`, ...

`_try_merge()` 会 glob 所有 partial 文件并 concat → **重叠范围会产生重复数据**。

**合并触发机制**：`_try_merge()` 在每个 shard precompute 结束时自动调用，检查所有 shard 是否完成后才合并。需要 `num_shards` 参数匹配。

**修复方案**：precompute 完成后，清除 s5 的 500-sample 粒度文件（`partial_s5_400_900.pt` 等），保留 100-sample 粒度文件，再手动触发合并。

### 3. Eval mode: ⚠️ 有 Gap

evaluate.py **支持 `--model pi05`**，但：

- **没有 `plan_a` mode**。可用 modes：`vla_only`, `crm_scalar`, `crm_perdof`, `acr_vla`, `crm_obs_only`, `reconvla`, `adaptive_k`, `adaptive_unc_head`, `adaptive_conformal_crm`
- `acr_vla` 是 `crm_perdof` 的 alias，即完整 ACR-VLA pipeline

**关键 Bug（line 576-578）**：
```python
if args.model == "pi05" and crm is not None:
    obs_proj = torch.nn.Linear(2048, OBS_DIM).to(device)  # 随机初始化！
```
当 CRM 已用 2048D features 训练时，这个 **未训练的随机投影** 会破坏 eval 结果。需要修复为：
- 如果 CRM 的 `obs_dim == 2048`，不应用投影
- 如果 CRM 的 `obs_dim == 960`，需要用训练好的投影（但这不是我们的方案）

**另外**：eval 用 `args.obs_dim`（默认 960）构建 CRM，pi05 需要传 `--obs_dim 2048`。

### 4. 建议的 Training 命令

**Object CRM**：
```bash
cd /root/acr-vla-conformal-refinement
python src/train_crm.py \
  --benchmark object \
  --cache_dir /root/autodl-tmp/crm_cache_pi05/ \
  --output_dir /root/autodl-tmp/checkpoints/crm_pi05/object_perdof/ \
  --input_mode full \
  --epochs 50 --batch_size 32 --lr 1e-3 --seed 42
```

**Spatial CRM**（spatial cache 完成后）：
```bash
python src/train_crm.py \
  --benchmark spatial \
  --cache_dir /root/autodl-tmp/crm_cache_pi05/ \
  --output_dir /root/autodl-tmp/checkpoints/crm_pi05/spatial_perdof/ \
  --input_mode full \
  --epochs 50 --batch_size 32 --lr 1e-3 --seed 42
```

### 5. 建议的 Eval 命令

```bash
# Object — 3 seeds
for SEED in 42 123 456; do
  python src/evaluate.py \
    --benchmark object --model pi05 --obs_dim 2048 \
    --mode acr_vla \
    --checkpoint /root/autodl-tmp/checkpoints/crm_pi05/object_perdof/crm_best.pt \
    --n_rollouts 20 --seed $SEED
done

# Spatial — 3 seeds
for SEED in 42 123 456; do
  python src/evaluate.py \
    --benchmark spatial --model pi05 --obs_dim 2048 \
    --mode acr_vla \
    --checkpoint /root/autodl-tmp/checkpoints/crm_pi05/spatial_perdof/crm_best.pt \
    --n_rollouts 20 --seed $SEED
done
```

### 6. 需要修复的 Gap

| # | 问题 | 严重性 | 修复 |
|---|------|--------|------|
| 1 | `evaluate.py` L576: pi05 时用未训练的 `nn.Linear(2048, 960)` 投影 | **Critical** | 当 CRM obs_dim=2048 时跳过投影，直接传 2048D features |
| 2 | Object cache s5 有重叠 partial 文件 | **High** | 清除 500-sample 粒度的 s5 文件后重新 merge |
| 3 | Spatial precompute 还没开始 | Medium | Object 完成后启动 spatial precompute |
| 4 | `--obs_dim` 默认值 960 对 pi05 不合适 | Low | eval 时记得传 `--obs_dim 2048`，或在 evaluate.py 中 auto-detect |

---
