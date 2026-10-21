# deploy westd38929 cuda1 and check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_cuda1_and_check_20260522T174344_result.json`
- **Structured JSON:** [`0ece62b36642890bd825.json`](../../sessions/0e/0ece62b36642890bd825.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 进程已启动，正在加载模型。

## 汇报

### 任务 A — cuda:1 部署 ✅
- **exp_id**: `eval_pi05_l2norm_k07_long_seed42`
- **PID**: 892021，已启动，正在加载 π0.5 模型
- **Registry**: RUNNING，hypothesis 已录入

### 任务 B — cuda:2 进程身份 ❌ 不部署
- **cuda:2 (2848 MiB, 28% util)**: **SmolVLA Random k=0.95 Long seed42** 正在运行
  - PID 802614: `python -u eval_official_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42`
  - 这是 PID 233183 链式任务的第 3 段（baseline → l2_norm → random_prune Long），说明 SmolVLA baseline Long 和 l2_norm k=0.95 Long 已完成
- **不部署** attention k=0.85 Object，等 SmolVLA Long 链跑完后再安排

### 任务 C — cuda:0 身份确认 ✅
- **cuda:0 (10510 MiB, 48% util)**: **π0.5 L2norm k=0.85 Long seed42**
  - PID 781071: `python eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0`
  - 已运行约 5 小时（00:35 启动）

### 四卡 GPU 状态

| GPU | 显存 | Util | 实验 |
|-----|------|------|------|
| cuda:0 | 10510 MiB | 48% | π0.5 L2norm k=0.85 Long seed42 (PID 781071) |
| cuda:1 | 4 MiB (加载中) | 0% | π0.5 L2norm k=0.7 Long seed42 (PID 892021) ← 刚部署 |
| cuda:2 | 2848 MiB | 28% | SmolVLA Random k=0.95 Long seed42 (PID 802614) |
| cuda:3 | 10942 MiB | 57% | π0.5 Random k=0.95 Long seed42 (PID 781138) |

---
