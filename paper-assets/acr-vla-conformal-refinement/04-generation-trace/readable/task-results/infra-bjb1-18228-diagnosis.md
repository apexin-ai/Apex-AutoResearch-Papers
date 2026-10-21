# infra bjb1 18228 diagnosis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bjb1-18228-diagnosis_20260517T225803_result.json`
- **Structured JSON:** [`1bc9551fafe18ace47ea.json`](../../sessions/1b/1bc9551fafe18ace47ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：bjb1-18228

### GPU 状态
| GPU | 状态 | 显存使用 | GPU-Util |
|-----|------|---------|----------|
| 0 | **占用** | 3342/24564 MiB | 23% |
| 1 | 空闲 | 4 MiB | 0% |
| 2 | 空闲 | 4 MiB | 0% |
| 3 | **占用** | 5200/24564 MiB | 23% |

### 活跃进程
服务器**没有因 SIGHUP 停止**，当前有两个评估进程正在运行：

1. **GPU 0** — `eval_object_obs_only_norm02_k5_seed42`（K=5, obs_only, seed42）
   - 已完成 5/10 tasks，正在跑第 8 个 task（`pick_up_the_tomato_sauce`）
   - 运行时间约 4 小时（02:54 启动）
   
2. **GPU 3** — `eval_object_perdof_norm02_seed45_r3`（K=10, perdof, seed45）
   - 已完成 1/10 tasks，正在跑第 2 个 task（`pick_up_the_cream_cheese`）
   - 运行时间约 2 小时（05:03 启动）

其他后台进程：tensorboard, jupyter-lab, flash-attn 编译（openvla 环境）, 一个 `eval-k1-seed43` tmux session（已完成产出 json）。

### 磁盘空间
| 分区 | 容量 | 已用 | 可用 |
|------|------|------|------|
| / (系统) | 30G | 17G (56%) | 14G |
| /root/autodl-tmp | 250G | 151G (61%) | 100G |

空间充足。

### 环境健康度
- Python/conda 环境正常（进程在正常跑）
- Checkpoints 完好：`crm_v3_norm/obs_only/crm_best.pt` (1.3MB), `crm_v3_norm/perdof/crm_best.pt` (1.4MB)
- LIBERO 环境加载正常（10 tasks loaded）

### K=5 Eval 进度
- **尚未产出 json 文件**（正在运行中）
- Log 显示已完成 5/10 tasks，预计还需约 3-4 小时完成剩余 5 个 tasks

### 结论
**不需要重启实验。** 服务器状态正常，K=5 eval 和 perdof eval 都在正常运行中。GPU 1 和 GPU 2 空闲，可以立即用来启动其他评估任务。

---
