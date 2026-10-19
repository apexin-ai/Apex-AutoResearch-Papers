# code crm v3 normalization prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_crm-v3-normalization-prep_20260514T181524_result.json`
- **Structured JSON:** [`705e3cda975d2809eb0b.json`](../../sessions/70/705e3cda975d2809eb0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。以下是完整报告。

---

## CRM v3 Normalization 代码检查报告

### 1. Normalization 实现状态：**未实现**

所有相关文件均无 input normalization 代码：

| 文件 | 状态 |
|------|------|
| `src/crm.py` | `forward()` 直接 `torch.cat([base_action, uf, obs_features])` 输入 MLP，无任何标准化 |
| `src/train_crm.py` | 训练循环传入原始特征，无 mean/std 计算 |
| `src/evaluate.py` | `select_action_crm()` 传入原始特征，无标准化 |
| `src/utils.py` | 无 normalization 相关工具函数 |
| `src/cgs.py` | CGS 输出原始 per_dof_std/conformal_radius/log_volume，无 rescaling |

### 2. 需要修改的文件和具体修改点

**文件 A: `src/crm.py`**（核心修改）
1. `__init__()` 中添加两个 `register_buffer`：
   - `self.register_buffer('input_mean', torch.zeros(input_dim))`
   - `self.register_buffer('input_std', torch.ones(input_dim))`
2. `forward()` 中，concatenation 之后、进入 `self.net` 之前，加一行：
   - `x = (x - self.input_mean) / (self.input_std + 1e-8)`
3. 新增方法 `set_normalization_stats(mean, std)` 用于设置 buffer 值

用 `register_buffer` 的好处：stats 自动随 `state_dict()` 保存/加载，evaluate.py 无需额外改动。

**文件 B: `src/train_crm.py`**（训练集成）
1. `train()` 函数中，加载 cache 数据后、构建 DataLoader 前：
   - 对所有 `k_samples` 批量跑 `cgs.compute_features_batch()` → 得到全量 uncertainty_features
   - 对全量 k_samples 计算 argmin base_action
   - 拼接 `[base_action, uf, obs_features]`（或根据 input_mode 选子集）
   - `mean = concatenated.mean(dim=0)`, `std = concatenated.std(dim=0)`
   - `crm.set_normalization_stats(mean, std)`
2. 注意 `scalar_unc` 模式需对 uf 做 `_to_scalar_uf` 后再拼接
3. `obs_only` 模式拼接时不含 uf

**文件 C: `src/evaluate.py`**（无修改）
- `register_buffer` 的 stats 随 `crm.load_state_dict()` 自动加载
- CRM forward 内部自动 standardize，推理路径透明

### 3. Precompute 数据

可用缓存在 `/root/autodl-tmp/crm_cache_v5/`：
- `spatial/`: 12,167 samples（obs_features.pt, k_samples.pt, expert_actions.pt）
- `object/`: 14,570 samples

从缓存计算 per-feature mean/std 完全可行，预计耗时 < 1 分钟（主要是 CGS batch 计算）。

### 4. 训练时间评估

- CRM v2 训练 50 epochs 耗时 ~5-15 分钟（模型参数量 ~330K）
- CRM v3 架构不变，仅增加 forward 中一行 standardization，开销可忽略
- 额外开销：训练前一次性计算 normalization stats（< 1 分钟）
- **预计每个 variant ~5-15 分钟，3 个 variant 共 ~15-45 分钟**

### 5. 启动训练命令（代码实现后）

```bash
cd /root/acr-vla-conformal-refinement

# 激活 conda
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Variant 1: perdof (full 40D uncertainty)
python src/train_crm.py --benchmark spatial object --epochs 50 --input_mode full \
  --cache_dir /root/autodl-tmp/crm_cache_v5 \
  --output_dir /root/autodl-tmp/checkpoints/crm_v3/perdof

# Variant 2: scalar_unc (3D scalar uncertainty)
python src/train_crm.py --benchmark spatial object --epochs 50 --input_mode scalar_unc \
  --cache_dir /root/autodl-tmp/crm_cache_v5 \
  --output_dir /root/autodl-tmp/checkpoints/crm_v3/scalar_unc

# Variant 3: obs_only (no uncertainty, input_dim=990)
python src/train_crm.py --benchmark spatial object --epochs 50 --input_mode obs_only \
  --cache_dir /root/autodl-tmp/crm_cache_v5 \
  --output_dir /root/autodl-tmp/checkpoints/crm_v3/obs_only
```

### 6. 关键注意事项

- CRM v2 checkpoints 在 `/root/autodl-tmp/checkpoints/crm_v2/{perdof,scalar_unc,obs_only}/`，各含 `crm_best.pt`，保留不动
- `--cache_dir` 默认值是 `/root/autodl-tmp/crm_cache/`（空目录），必须显式指定 v5 路径
- normalization stats 的计算必须只用训练集（val_split 之后的 train 子集），避免信息泄漏

---
