# code v7 impl and launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v7_impl_and_launch_20260518T183815_result.json`
- **Structured JSON:** [`bf5cdf8888c8b81c2654.json`](../../sessions/bf/bf5cdf8888c8b81c2654.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. 代码修改摘要

| 文件 | 变更 |
|------|------|
| **config.py** | `GAR_LOSS_MODE` → `"mse_target"`, 新增 `LAMBDA_GATE_DIV=1.0`, `MIN_GATE_STD=0.05` |
| **gar.py** | `compute_gar_loss` 新增 `mse_target` 模式: `(mean_gar - target)^2`，双向惩罚 |
| **threadgate.py** | hook 中新增 `_gate_values_with_grad` 存储带梯度的 gate tensor; `get_gate_values(with_grad=False)` 新增参数 |
| **train_phase2.py** | 新增 `--lambda-gate-div`/`--min-gate-std` 参数; 训练循环中计算 `L_gate_div = relu(min_std - gate_std)`; loss = L_NTP + λ_gar·L_GAR + λ_div·L_DIV; 日志/config dump 同步更新 |

### 2. get_gate_values() 修改

原始实现返回 `gate.detach()`，梯度断开。已修改为同时存储带梯度版本，通过 `with_grad=True` 参数获取，确保 L_gate_div 可微分。

### 3. 同步确认

4 文件 md5 校验: config.py/gar.py/threadgate.py 完全一致，train_phase2.py 功能代码一致（空行差异）。

### 4. Dry-run 结果

| 指标 | Step 0 | Step 4 | 判定 |
|------|--------|--------|------|
| L_NTP | 2.0275 | 1.6477 | 正常 |
| L_GAR | 0.2342 | 0.2355 | 非零正值 (MSE=(~0.02-0.5)^2≈0.23) |
| L_DIV | 0.0153 | 0.0000 | 初始触发(std=0.034<0.05)，5步后std=0.088>0.05自动归零 |
| Total Loss | 2.2770 | 1.8832 | 正值 |
| Gate均值 | 0.810 | 0.801 | 非恒等 |
| Gate std | 0.034→0.088 | | 多样性增加 |
| Gate梯度 | **True** | | 确认收到 |

### 5. 全量训练

已通过 tmux session `v7_train` 在 westd-20861 启动，日志: `/root/turn_residual_gating/runs/phase2_tg_s42_v7.log`

---
