# ssh check crm input dim

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-crm-input-dim_20260516T234450_result.json`
- **Structured JSON:** [`abb4ecadc650a24b026d.json`](../../sessions/ab/abb4ecadc650a24b026d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## 维度确认

**文件**: `/root/acr-vla-conformal-refinement/src/crm.py`

| 组件 | 维度 | 来源 |
|------|------|------|
| obs_dim | **960** | VLM hidden_size (`utils.py:20`) |
| action_dim | **30** | 5 steps × 6 DOF (`H_EFF=5, CORRECTION_DIM=6`) |

## 各 variant 的 input_dim

定义于 `train_crm.py:347-349`：

| input_mode | uncertainty_dim | **总 input_dim** | 计算 |
|---|---|---|---|
| `full` | 40 (30 per_dof_std + 5 conformal_radius + 5 log_volume) | **1030** | 30 + 40 + 960 |
| `obs_only` | 0 (uncertainty_features=None) | **990** | 30 + 0 + 960 |
| `scalar_unc` | 3 (norm_std, mean_radius, mean_logvol) | **993** | 30 + 3 + 960 |

注意：代码中没有名为 `perdof` 的 variant。现有的 `full` mode 已包含 per-DOF std（30维），这可能就是你指的 "perdof"。

## 协方差计算方式

**文件**: `/root/acr-vla-conformal-refinement/src/cgs.py`

协方差是 **per-step (6×6)** 计算的，不是 full 30×30：

```python
for h in range(self.horizon):          # 逐 step 循环
    step_samples = samples[:, h, :]    # (K, 6) — 单步的 K 个样本
    cov_matrix = self._ledoit_wolf_cov(step_samples)  # (6, 6)
```

每个 step 独立用 Ledoit-Wolf 估计一个 6×6 协方差矩阵，产出该 step 的 per_dof_std(6)、conformal_radius(1)、log_volume(1)。5 个 step 拼接得到 40D uncertainty features。

---
