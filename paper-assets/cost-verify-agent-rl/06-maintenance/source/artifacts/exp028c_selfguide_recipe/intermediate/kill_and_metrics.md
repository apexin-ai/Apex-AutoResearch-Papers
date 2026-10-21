# exp028c Kill & Metrics Report

**Date**: 2026-05-16
**W&B Run**: `4yu6qz1m` (exp028c-alfworld-selfguide-recipe)
**Reason**: Val step 10 = 0% success, catastrophic collapse

---

## 1. 进程终止确认

| PID | Role | Status |
|-----|------|--------|
| 824675 | Main (TaskRunner) | KILLED (SIGTERM) |
| 828110 | WorkerDict GPU0 | KILLED (zombie → SIGKILL) |
| 828111 | WorkerDict GPU1 | KILLED (zombie → SIGKILL) |

**结果**: ALL_DEAD_CONFIRMED

## 2. GPU 释放确认

| GPU | Memory Used | Memory Total | Utilization |
|-----|-------------|--------------|-------------|
| 0 | 0 MiB | 97887 MiB | 0% |
| 1 | 0 MiB | 97887 MiB | 0% |

## 3. Checkpoint 状态

| Checkpoint | Size | Status |
|------------|------|--------|
| global_step_5 | 21 GB | ✓ 完整 (actor/) |
| global_step_10 | 21 GB | ✓ 完整 |

## 4. Validation Metrics (16 episodes, test_freq=5)

| Step | success | pass@1 | action_valid | action_effective | reward/mean |
|------|---------|--------|--------------|------------------|-------------|
| 0 (pre-train) | **6.25%** (1/16) | 6.25% | 74.49% | 95.0% | 0.1186 |
| 5 | **6.25%** (1/16) | 6.25% | 96.5% | 100% | 0.5183 |
| 10 | **0%** (0/16) | 0% | 93.6% | 99.6% | 0.0 |

**Val best@N at step 10**: 全部为 0.0（best@8, best@16, ... best@512 均为 0），确认完全崩溃。

## 5. Train Metrics (Steps 7-12)

| Step | success | pass@8 | action_valid | action_effective | kl_loss | ppo_kl | entropy | pg_loss | grad_norm |
|------|---------|--------|--------------|------------------|---------|--------|---------|---------|-----------|
| 7 | 21.9% | 56.3% | 91.8% | 98.3% | 0.046 | 0.0154 | 0.223 | 0.0058 | 12.05 |
| 8 | 15.6% | 50.0% | 92.7% | 98.7% | 0.039 | 0.0149 | 0.204 | 0.0051 | 11.34 |
| 9 | 18.0% | 56.3% | 93.6% | 98.9% | 0.047 | 0.0151 | 0.204 | 0.0065 | 12.87 |
| 10 | 18.8% | 50.0% | 90.7% | 98.4% | 0.197 | 0.0188 | 0.215 | 0.0059 | 9.89 |
| 11 | 7.0% | 18.8% | 89.7% | 96.3% | 0.098 | 0.0020 | 0.224 | 0.0095 | 10.35 |
| 12 | 6.3% | 25.0% | 89.5% | 94.7% | 0.272 | 0.0183 | 0.198 | 0.0049 | 10.55 |

## 6. 崩溃分析

- **Val 崩溃确认**: Step 10 val = 0/16 (0%)，所有 best@N 均为 0，模型已丧失解题能力
- **Train 下降趋势**: success 从 step 7 的 21.9% 急跌到 step 11-12 的 6-7%
- **kl_loss 异常**: step 5 出现 kl_loss=0.824 spike，step 10 出现 0.197，step 12 出现 0.272
- **entropy 持续下降**: 从 step 7 的 0.223 降到 step 12 的 0.198，策略趋于确定性
- **action_is_effective 下降**: 从 step 9 的 98.9% 降到 step 12 的 94.7%
- **ppo_kl 异常**: step 11 出现 ppo_kl=0.002 异常低值（前序 steps 约 0.015），疑似策略突变

**终止时状态**: 进程在 step 12 完成后被 kill（Training Progress: 12/100）。
