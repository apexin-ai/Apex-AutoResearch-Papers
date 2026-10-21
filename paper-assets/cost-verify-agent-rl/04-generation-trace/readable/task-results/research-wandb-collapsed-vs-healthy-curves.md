# research wandb collapsed vs healthy curves

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wandb_collapsed_vs_healthy_curves_20260522T220334_result.json`
- **Structured JSON:** [`76a794ab27f578ad2a18.json`](../../sessions/76/76a794ab27f578ad2a18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已提取并保存至 `artifacts/exp029/data/learning_curve_data.json`。

## 汇总

### W&B Run ID 映射

| Seed | Run ID | Run Name | 训练步数 | 类别 |
|------|--------|----------|---------|------|
| seed2048 | `5j94efd5` | exp029-new-seed-2048 | 4 | Collapsed |
| seed42 | `kvdbh1sz` | exp029-seed42-episode-level | 4 | Collapsed |
| seed8 | `c0l6e7vd` | exp029-seed8-episode-level | 9 | Collapsed |
| seed4 | `fb1o765g` | exp029-seed4-episode-level | 14 | Healthy |
| seed5 | `yyoghk1f` | exp029-seed5-episode-level | 10 | Healthy |
| seed6 | `2bbyvsdr` | exp029-seed6-episode-level | 14 | Healthy |
| seed100 | `55kt9yf9` | exp029-seed100-episode-level | 4 | Healthy |

### 关键模式

**Collapsed seeds 特征**:
- **seed8** 最典型：step 1-4 success 在 0.31-0.44，step 5 开始骤降至 0.06-0.11，response_length 从 ~9000 暴涨到 ~15000
- **seed2048** 始终低位（0.01-0.10），response_length 始终 ~15000
- **seed42** 仅 4 步，step 3 到 0.25 后 step 4 回落到 0.09

**Healthy seeds 特征**:
- **seed6** 最成功：从 0.07 稳步上升到 0.89，response_length 从 14910 降至 3329
- **seed5** 前期强（peak 0.73），后期有回退（step 10 降至 0.23）
- **seed4** 在 0.12-0.38 之间振荡，未达高位但也未崩溃
- **seed100** 仅 4 步数据，趋势不明

### 注意事项
- `train/AlfworldSG/response_length` 字段在 W&B 中为 null，替代使用 `response_length/mean`
- W&B `fetch_wandb_run_history` 工具有 bug（key-filtered scan_history 只返回所有指定 key 均非 null 的行），改用 SSH 直接调 W&B API 提取

---
