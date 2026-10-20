# ESS-only Baseline Implementation

## 修改文件

### 1. `artifacts/weighting/alpha_eff.py`
- **新增函数 `find_ess_only_b`**（第 82–103 行区域）
- 在 `compute_sample_weights` 前插入

### 2. `artifacts/training/pretrain_weighted.py`
- **import**：新增 `find_ess_only_b`
- **docstring**：更新为 4 种方法
- **argparse choices**：`["uniform", "grid", "adaptive", "ess_only"]`
- **compute_loss**：新增 `ess_only` 分支，调用 `find_ess_only_b`

### 3. `training/run_ess_only_seed42.sh`（新建）
- 运行脚本，`--weighting_method ess_only`，seed=42，200M tokens

## b* 计算算法

**ESS-only**: `b* = max{b ≥ 0 : ESS(b) ≥ n_min}`

ESS(b) 对 b 单调非递增（b 越大，权重越不均匀，ESS 越小），因此用二分搜索：
- 搜索范围 `[0, b_max]`，`b_max=20.0`
- 精度 `tol=0.01`
- 若 `ESS(0) < n_min`，返回 0（数据本身 ESS 不足）
- 若 `ESS(b_max) ≥ n_min`，返回 `b_max`
- 否则二分找 `lo` 使得 `ESS(lo) ≥ n_min` 且 `ESS(hi) < n_min`

## 与 adaptive 的关键差异

| | adaptive (ours) | ess_only (baseline) |
|---|---|---|
| 目标 | `inf{b : α_eff(b) ≥ τ}` s.t. `ESS ≥ n_min` | `max{b : ESS(b) ≥ n_min}` |
| 准则 | 最小干预（minimum intervention） | 最大干预（maximum intervention） |
| b* 大小 | 较小（刚好满足 α_eff 阈值） | 较大（推到 ESS 边界） |
| α_eff 约束 | 有（≥ τ） | 无 |
| 预期效果 | 保留更多数据信号 | 过度下权导致信息损失 |

adaptive 找到最小的 b 使 α_eff 达标（保守），ess_only 找最大的 b 直到 ESS 刚好够（激进）。ess_only 的 b* ≥ adaptive 的 b*。
