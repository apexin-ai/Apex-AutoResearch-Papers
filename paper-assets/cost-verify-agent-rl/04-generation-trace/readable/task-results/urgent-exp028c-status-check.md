# urgent exp028c status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_exp028c_status_check_20260516T062859_result.json`
- **Structured JSON:** [`24959255445e63938ffd.json`](../../sessions/24/24959255445e63938ffd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp028c 状态报告

### 进程状态: ✅ 存活
- PID 824675，运行 8h51m
- 当前正在执行 step 11 的 rollout generation

### GPU 状态: ✅ 正常工作
| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 (RTX PRO 6000) | 61% | 48.3/97.9 GB | rollout_generate_sequences |
| 1 (RTX PRO 6000) | 57% | 48.4/97.9 GB | rollout_generate_sequences |

**GPU 0% 报警是误报** — 可能抓到了 checkpoint 保存期间的瞬时低负载（14:15 保存 global_step_10）。

### 进度
- 10/100 steps 完成，8h29m 已过，~50min/step
- Step 10 checkpoint 已保存（14:15），step 11 rollout 正在生成中

### Training Metrics (趋势向好)

| Step | success | pass@8 | action_is_valid | kl_loss | entropy | grad_norm |
|------|---------|--------|-----------------|---------|---------|-----------|
| 1 | 13.3% | 37.5% | 76.4% | 0.013 | 0.263 | 16.88 |
| 5 | 9.4% | 37.5% | 89.6% | 0.824 | 0.236 | 13.08 |
| 8 | 15.6% | 50.0% | 92.7% | 0.039 | 0.204 | 11.34 |
| 9 | 17.97% | 56.25% | 93.6% | 0.047 | 0.204 | 12.87 |

### Validation Metrics

| Step | success | pass@1 | action_is_valid | reward/mean |
|------|---------|--------|-----------------|-------------|
| 0 | **6.25%** | 6.25% | 74.5% | 0.119 |
| 5 | **6.25%** | 6.25% | 96.5% | 0.518 |
| 10 | **未出现** — metrics line 未写入日志 | | | |

### Step 10 Val 状况
Step 10 的 validation generation 已完成（401s），checkpoint 已保存，但 `step:10` 的 metrics 行尚未刷入日志。框架先保存 checkpoint 再异步/延迟写 metrics。等 step 11 rollout 完成后（预计 ~20min）应该会出现。

### 关键判断
- **val success 停滞在 6.25%**（steps 0 和 5 相同），未达到 ≥20% MVP 线
- 但 training success 明显上升（6.25% → 17.97%），action_is_valid 从 74.5% 飙升到 93.6%
- val-core/reward/mean 从 0.119 → 0.518，有改善但幅度有限
- Step 10 val 是关键判定点，需等待 metrics 刷出。如果 val success 仍为 6.25%，则训练效果未泛化到 val set

---
