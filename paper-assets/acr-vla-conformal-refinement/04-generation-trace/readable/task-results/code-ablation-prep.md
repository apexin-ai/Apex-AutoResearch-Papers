# code ablation prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation-prep_20260513T201522_result.json`
- **Structured JSON:** [`f65cbf5c30c0a553039c.json`](../../sessions/f6/f65cbf5c30c0a553039c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

---

## 结论

### 1. 是否已支持 ablation：**No**

`parse_args()` 中没有 `--ablation`、`--mode`、`--input_mode` 等参数。特征拼接逻辑硬编码为 full 模式（obs + conformal + mean_action）。

### 2. 当前特征流

| 组件 | 维度 | 来源 |
|------|------|------|
| `mean_action` | 30D (H_EFF×CORRECTION_DIM = 5×6) | CGS: K samples 均值 |
| `uncertainty_features` | 40D (per_dof_std 30 + conformal_radius 5 + log_volume 5) | CGS: 结构化不确定性 |
| `obs_features` | 960D | VLM frozen encoder |
| **总输入** | **1030D** | CRM 输入 |

关键代码位置：
- **CRM 模型** `crm.py:26-27` — `input_dim = action_dim + uncertainty_dim + obs_dim`，`forward()` 中 `torch.cat([mean_action, uncertainty_features, obs_features])`
- **训练循环** `train_crm.py` `train()` 函数 — CRM 实例化硬编码 `uncertainty_dim=40`, `action_dim=30`, `obs_dim=960`；forward 调用 `crm(ma, uf, obs_feat)`

### 3. 最小改动方案

**目标**：加一个 `--input_mode` 参数，支持三种模式：

| mode | 输入 | 维度 | 对应 plan |
|------|------|------|-----------|
| `full` (默认) | obs + uncertainty + mean_action | 1030D | 当前 baseline |
| `obs_only` | obs + mean_action (无 conformal) | 990D | plan_002 (A3) |
| `scalar_unc` | obs + scalar_uncertainty + mean_action | 960+S+30 | plan_003 (A4) |

#### 修改文件 1: `train_crm.py`

**A. `parse_args()` 加参数**（约 L68 附近）：
```python
p.add_argument("--input_mode", type=str, default="full",
               choices=["full", "obs_only", "scalar_unc"],
               help="full=all features, obs_only=no conformal, scalar_unc=scalar uncertainty")
```

**B. `train()` 函数中 CRM 实例化**（约 L330 附近）：
```python
# 根据 input_mode 决定 uncertainty_dim
if args.input_mode == "full":
    unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 40
elif args.input_mode == "obs_only":
    unc_dim = 0
elif args.input_mode == "scalar_unc":
    unc_dim = 3  # euclidean_dist + mean_conformal_radius + mean_log_volume
```

**C. 训练循环中 forward 调用**（约 L355, L370, L390 三处）：
```python
uf, ma = cgs.compute_features_batch(k_samp)

if args.input_mode == "obs_only":
    uf_input = None  # 不传 uncertainty
elif args.input_mode == "scalar_unc":
    uf_input = compute_scalar_uncertainty(k_samp, ma)  # 新函数
else:
    uf_input = uf
```

验证和 augmentation 两处也要同步改。

#### 修改文件 2: `crm.py`

**D. `__init__` 和 `forward` 支持 `uncertainty_dim=0`**（L15, L40）：
```python
def __init__(self, action_dim=30, uncertainty_dim=40, obs_dim=960, hidden_dim=256):
    input_dim = action_dim + uncertainty_dim + obs_dim  # 已有，不变

def forward(self, mean_action, uncertainty_features, obs_features):
    if uncertainty_features is not None:
        x = torch.cat([mean_action, uncertainty_features, obs_features], dim=-1)
    else:
        x = torch.cat([mean_action, obs_features], dim=-1)
    delta = self.net(x)
    return mean_action + delta
```

#### 修改文件 3: `cgs.py` 或 `train_crm.py` 中新增辅助函数

**E. `compute_scalar_uncertainty()`**（plan_003 需要）：
```python
def compute_scalar_uncertainty(k_samples, mean_action):
    """K samples → 3 scalar features: avg_std, avg_conformal_radius, avg_log_volume."""
    # k_samples: (B, K, H, D), mean_action: (B, 30)
    B = k_samples.shape[0]
    ma_reshaped = mean_action.reshape(B, H_EFF, CORRECTION_DIM)
    diff = k_samples - ma_reshaped.unsqueeze(1)  # (B, K, H, D)
    euclidean = diff.norm(dim=-1).mean(dim=(1, 2))  # (B,) scalar spread
    per_dof_std = k_samples.std(dim=1).mean(dim=(1, 2))  # (B,)
    max_std = k_samples.std(dim=1).max(dim=-1).values.mean(dim=1)  # (B,)
    return torch.stack([euclidean, per_dof_std, max_std], dim=-1)  # (B, 3)
```

#### 输出目录区分

`--output_dir` 加 mode 后缀：
```python
args.output_dir = os.path.join(args.output_dir, args.input_mode)
```

### 4. plan_002 / plan_003 训练命令（改完后）

```bash
# plan_002 (A3): obs only, no conformal
python train_crm.py --benchmark spatial --epochs 50 --input_mode obs_only \
  --output_dir /root/autodl-tmp/checkpoints/crm/obs_only/

# plan_003 (A4): scalar uncertainty
python train_crm.py --benchmark spatial --epochs 50 --input_mode scalar_unc \
  --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/
```

### 5. 预估训练时间和 GPU 需求

Phase 2 训练（加载缓存后）是纯 MLP 训练，参数量约 280K（full 模式），ablation 模式更少：
- **obs_only**: input_dim=990, 约 260K params
- **scalar_unc**: input_dim=993, 约 260K params

50 epochs 在单 GPU 上预计 **5-15 分钟**（取决于数据量）。GPU 显存需求极低（<1GB），任意 GPU 均可。precompute cache 已有则无需重新生成。

---
