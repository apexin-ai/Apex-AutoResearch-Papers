# monitor bjb1 progress check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-progress-check_20260514T212441_result.json`
- **Structured JSON:** [`76161e81d7305cf1d940.json`](../../sessions/76/76161e81d7305cf1d940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总所有数据。

## 实验进度汇总

### 进程状态：6/6 全部存活

### Eval 实验

| # | 实验 | PID | GPU | 运行时间 | 已完成 tasks | 当前进度 | 中间 metrics |
|---|------|-----|-----|---------|-------------|---------|-------------|
| 1 | **eval-acr-spatial-v4-default** (crm_v3_norm, 默认correction) | 252489 | cuda:0 | ~55min | **未知** | **日志丢失** | 见下方说明 |
| 2 | eval-argmin-only-spatial (reconvla baseline) | 231426 | cuda:1 | 3h37m | 3/10 | Task 4 rollout 5/10 (1/5) | T1=60%, T2=100%, T3=0% |
| 3 | eval-tiny-correction-spatial (crm_v2, max_norm=0.05) | — | cuda:2 | 3h37m | 3/10 | Task 4 rollout 5/10 (1/5) | T1=70%, T2=90%, T3=0% |
| 4 | eval-acr-spatial-v4-small (crm_v3_norm, max_norm=0.1) | 253085 | cuda:3 | ~55min | 1/10 | Task 2 未开始 | T1=60% |

**v4-default 日志问题**：tee 进程 (PID 252490) 未成功创建输出文件（fd 只有 pipe→/dev/pts/0，无 file fd）。`/root/autodl-tmp/logs/` 目录在 tee 启动时可能不存在。输出仅进入 tmux terminal buffer。旧的 `eval-acr-spatial-v3.log` 里存的是 crm_v2 旧实验数据（5 tasks: 10%, 0%, 0%, 0%, 0%），不是 v4-default 的。

**需要用 ssh_execute 执行 `tmux capture-pane -t eval-acr-spatial-v3 -p -S -100` 来读取 v4-default 的中间输出。** 是否执行？

### CRM 训练实验

| # | 实验 | PID | 运行时间 | 进度 | best val_loss | 趋势 |
|---|------|-----|---------|------|---------------|------|
| 5 | crm-train-v3-norm-obs-only | 256776 | 35min | **23/50 epochs** | **0.016689** (epoch 23) | 稳步下降，每个 epoch 都在刷新 best |
| 6 | crm-train-v3-norm-scalar-unc | 257091 | 35min | **23/50 epochs** | **0.040811** (epoch 23) | 持续下降，每个 epoch 都在刷新 best |

obs_only 的 val_loss（0.0167）比 scalar_unc（0.0408）低 2.4x，说明 obs_only 输入模式在这个 normalized CRM 上拟合更好。两个训练都还在 loss 下降期，没有过拟合迹象。

### 早期 eval 对比（前 3 tasks 平均 success rate）

| 方法 | T1 | T2 | T3 | 平均 |
|------|----|----|----|----|
| argmin-only (无 CRM) | 60% | 100% | 0% | 53.3% |
| tiny-correction (crm_v2, 0.05) | 70% | 90% | 0% | 53.3% |
| v4-small (crm_v3_norm, 0.1) | 60% | — | — | 60%* |
| **v4-default (crm_v3_norm, default)** | **?** | **?** | **?** | **?** |

T3 (table_center) 对所有方法都是 0%——这可能是一个本质困难的 task。tiny-correction 在 T1/T2 上略优于 argmin-only baseline，但 correction 幅度太小差异不显著。

---
