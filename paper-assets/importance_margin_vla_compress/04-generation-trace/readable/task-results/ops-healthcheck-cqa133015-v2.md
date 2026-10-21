# ops healthcheck cqa133015 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_healthcheck-cqa133015-v2_20260524T093544_result.json`
- **Structured JSON:** [`bd0800912b0c7ef28bf7.json`](../../sessions/bd/bd0800912b0c7ef28bf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 GPU 健康检查报告

### GPU 状态总览

| GPU | 利用率 | 显存 | PID | 实验ID | Status | SR | Episodes |
|-----|--------|------|-----|--------|--------|----|----------|
| **0** | 38% | 10196/24564 MiB | 86738 | `eval_pi05_random_k05_goal_seed42_postfix` | **RUNNING** | 71.0% (T0-3) | 200/500 进行中 |
| **1** | 0% | 1 MiB | — | `eval_pi05_random_k03_spatial_seed42_postfix` | **COMPLETED** | **41.8%** | 500/500 |
| **2** | 0% | 1 MiB | — | `eval_pi05_random_k095_spatial_seed42_postfix_v2` | **COMPLETED** | **79.6%** | 500/500 |
| **3** | 41% | 10273/24564 MiB | 979186 | `eval_pi05_l2norm_k05_spatial_seed42_postfix` | **RUNNING** | ~58.9% (T0-8) | 450/500 进行中 |

### 详情

**GPU 0** — Random k=0.5 Goal (PID 86738, started 16:48)
- 当前进度: Task 4/10, ep 10/50, 累计 142/200=71.0%
- T0=78%, T1=44%, T2=86%, T3=76%, T4 进行中(9/10=90%)
- 预计剩余 ~1.5hr

**GPU 1** — Random k=0.3 Spatial — **已完成，可收割**
- 结果文件: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.30_libero_spatial_seed42.json`
- **SR = 41.8%** (209/500), 耗时 167min
- Per-task: T0=58%, T1=60%, T2=52%, T3=8%, T4=34%, T5=22%, T6=24%, T7=62%, T8=74%, T9=24%

**GPU 2** — Random k=0.95 Spatial — **已完成，可收割**
- 结果文件: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.95_libero_spatial_seed42.json`
- **SR = 79.6%** (398/500), 耗时 119min
- Per-task: T0=100%, T1=94%, T2=94%, T3=76%, T4=56%, T5=76%, T6=96%, T7=72%, T8=100%, T9=32%

**GPU 3** — L2norm k=0.5 Spatial (PID 979186, started 15:13 via nohup)
- 当前进度: Task 9/10, ep 20/50, 累计 265/450=58.9%
- T0=80%, T1=90%, T2=90%, T3=26%, T4=32%, T5=34%, T6=28%, T7=76%, T8=74%, T9 进行中(7/20=35%)
- **预计 ~10-15min 完成**
- 这就是 Director 报告的"未注册任务"——进程是通过 nohup 而非标准 job submission 启动的，所以 registry 可能没跟踪到

### 未注册/异常项
- tmux session `eval_pi05_random_k095_object_seed42_v2` 处于空闲状态（只有 shell prompt），无 GPU 进程，可安全清理
- GPU 1、GPU 2 空闲，可立即部署新实验

### 额外发现 — eval_results 目录中还有这些已完成的 Spatial 结果

| 配置 | SR |
|------|----|
| random k=0.50 spatial | 71.8% |
| random k=0.70 spatial | 73.8% |
| random k=0.85 spatial | 60.8% |
| random k=0.90 spatial | 53.4% |
| random k=0.95 spatial | 79.6% |
| random k=0.30 spatial | 41.8% |
| l2norm k=0.85 spatial | **88.4%** |

---
