# diagnose pi05 backfill failures

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-backfill-failures_20260528T113140_result.json`
- **Structured JSON:** [`d2848e46a922c5b98351.json`](../../sessions/d2/d2848e46a922c5b98351.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**根因：CRM checkpoint 与模型初始化维度不匹配。** 3 个实验完全相同的错误。

### Traceback（3 个实验一致）

```
RuntimeError: Error(s) in loading state_dict for ConformalRefinementModule:
  size mismatch for input_mean: [2118] vs [990]
  size mismatch for input_std:  [2118] vs [990]
  size mismatch for net.0.weight: [256, 2118] vs [256, 990]
```

### 维度分析

CRM `input_dim = action_dim + uncertainty_dim + obs_dim`

| | action_dim | unc_dim | obs_dim | input_dim |
|---|---|---|---|---|
| **当前模型**（crm_obs_only, 默认 obs_dim） | 30 | 0 | 960 | **990** |
| **Checkpoint**（crm_pi05_unified_3suite） | 30 | 40 | 2048 | **2118** |

Checkpoint 是用 **perdof 模式**（unc_dim=40）+ **PI05 obs_dim=2048** 训练的（30+40+2048=2118）。

但 3 个实验的命令：
- 实验 1&2：`--mode crm_obs_only` → unc_dim=0
- 实验 3：`--mode adaptive_conformal_crm` → unc_dim=0
- 全部：`--obs_dim` 取默认值 960（SmolVLA 的维度，不是 PI05 的 2048）

### 两层不匹配

1. **obs_dim 错误**：PI05 输出 2048D 特征，但命令未指定 `--obs_dim 2048`
2. **mode 与 checkpoint 不兼容**：obs_only/adaptive 模式 unc_dim=0，但 checkpoint 训练时 unc_dim=40（perdof）

### GPU 状态

cuda:2 和 cuda:3 已空闲（1 MiB），可立即重用。cuda:0/1/4/5 有其他进程。

### 修复方案

**不能直接重试**，命令本身有 bug。需要二选一：

**方案 A**（改命令适配现有 checkpoint）：
- 实验 1&2：`--mode crm_perdof --obs_dim 2048`（替换 crm_obs_only）
- 实验 3：需要一个支持 unc_dim=40 的 adaptive 模式，或改用 `--mode acr_vla --obs_dim 2048`

**方案 B**（用 obs_only 专用 checkpoint）：
- 需要一个用 `unc_dim=0, obs_dim=2048` 训练的 PI05 CRM checkpoint
- 当前服务器上不存在这样的 checkpoint（`crm_pi05_full/` 下只有 object/ 和 spatial/，没有 long/）

请确认要走哪个方案，我立即修改命令重新提交。

---
