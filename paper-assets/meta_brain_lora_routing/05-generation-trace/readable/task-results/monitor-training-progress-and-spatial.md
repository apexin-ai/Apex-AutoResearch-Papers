# monitor training progress and spatial

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-and-spatial_20260516T055757_result.json`
- **Structured JSON:** [`5eae96465fab3052c966.json`](../../sessions/5e/5eae96465fab3052c966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

### GPU 利用率

| GPU | 利用率 | 显存 | 温度 |
|-----|--------|------|------|
| cuda:0 | 99% | 12705/97887 MiB | 75°C |
| cuda:1 | 99% | 12819/97887 MiB | 70°C |
| cuda:2 | 95% | 12707/97887 MiB | 72°C |
| cuda:3 | 99% | 12965/97887 MiB | 73°C |

### 训练进度（全部运行中，目标 10000 steps）

| 训练 | GPU | 当前 Step | Loss | 速度 | 预计完成 |
|------|-----|-----------|------|------|----------|
| visual r16 | cuda:0 | **7250**/10000 (72.5%) | 0.0112 | ~51.2s/50步 | ~14:45 |
| physical r16 | cuda:1 | **7250**/10000 (72.5%) | 0.0112 | ~51.1s/50步 | ~14:45 |
| universal r16 | cuda:2 | **7250**/10000 (72.5%) | 0.0113 | ~51.0s/50步 | ~14:45 |
| universal r48 | cuda:3 | **7200**/10000 (72.0%) | 0.0105 | ~51.4s/50步 | ~14:46 |

### 结论

- **universal_r16 尚未完成**（7250/10000），还需约 47 分钟 → **不启动 spatial 训练**
- 4 路训练进度基本同步，loss 都收敛到 0.010-0.012 区间，grad_norm 稳定在 0.02-0.05
- `checkpoints/lora_*/final/` 目录下已有上一轮训练的 final checkpoint（时间戳 11:48-11:52，早于当前进程启动时间 11:54），当前轮训练完成后会覆盖
- 预计全部完成时间：**~14:45-14:46**（约 47 分钟后）

---
