# ops check processes

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_processes_20260515T185239_result.json`
- **Structured JSON:** [`dbb55a736be6c9991937.json`](../../sessions/db/dbb55a736be6c9991937.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态报告

### 进程存活
| 实验 | PID | 状态 | 运行时长 |
|------|-----|------|---------|
| spon_2048_s42 | 109601 | **存活** | 11min 10s |
| ste_kl_s42 | 112197 | **存活** | 2min 19s |

### GPU 使用
| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| cuda:0 (spon_2048_s42) | 100% | 33,917 / 97,887 MiB (35%) |
| cuda:1 (ste_kl_s42) | 100% | 75,185 / 97,887 MiB (77%) |

### ste_kl_s42 — Step 40/1000 (4%)
```
[Step  1] loss=6.9688  sparsity=0.539  lambda=0.50
[Step 10] loss=3.3750  sparsity=0.539  lambda=0.01
[Step 20] loss=2.2344  sparsity=0.533  lambda=0.01
[Step 30] loss=1.8516  sparsity=0.527  lambda=0.01
[Step 40] loss=1.5156  sparsity=0.520  lambda=0.01  lr=4e-4
```
Loss 持续下降，sparsity 从 0.539 缓慢向 0.5 target 靠拢。

### spon_2048_s42 — Step 300/1000 (30%)
```
[Step 100] loss=0.4121  mean_bias_norm=0.015928  lr=1.00e-5
[Step 200] loss=0.3574  mean_bias_norm=0.030933  lr=9.70e-6
[Step 300] loss=0.3516  mean_bias_norm=0.040398  lr=8.83e-6
```
Loss 收敛中（0.41 → 0.36 → 0.35），bias norm 稳步增长。每 100 步打一次日志。

两个进程都在正常训练。

---
