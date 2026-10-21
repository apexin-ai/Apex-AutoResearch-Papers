# ops gpu status check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260523T004735_result.json`
- **Structured JSON:** [`56b083eb52ef3f99e38c.json`](../../sessions/56/56b083eb52ef3f99e38c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报 (westd-20861, 2026-05-23 ~09:04 UTC)

### 1. GPU 状态
```
利用率: 66%  |  显存: 28831 / 97887 MiB (29%)
```
GPU 在活跃工作中，显存占用不高。

### 2. 活跃进程
| 进程 | PID | 状态 |
|------|-----|------|
| `eval_attention_steering.py` (TG s42 AR N=50) | 58315 | **运行中** (113% CPU) |
| `d048_auto_transition.sh` | 56575 | 运行中 |
| `d048_final_ar_eval.sh` | 57309 | 运行中 |
| `queue_runner` tmux session | 50719 | 活跃 |

### 3. d048_final_ar_eval 进度
- **[1/6] Base s42 AR N=50** — **已完成** ✓
  - Beta=0: Mid-GAR=0.0186, PPL=1.45
  - Beta=3: Mid-GAR=0.5315, PPL=1.50
  - Beta=5: Mid-GAR=0.7042, PPL=1.95
  - 结果已保存: `results/d048_final_ar/base_s42_ar_n50.json`
- **[2/6] TG s42** — **正在加载模型权重**，刚开始

### 4. d048_ss_s123 训练进度
- queue_runner 已启动第 [3/8] 步：SS s123 训练
- 模型加载完成，训练参数已输出
- Step 0: L_NTP=1.3700, L_GAR=0.2337, Loss=1.6255, Gate=0.8118, Mem=53.0GB
- 训练目录 `runs/d048_ss_s123/` **尚未创建**（刚开始训练）

### 5. 日志位置
```
/root/queue_runner.log → 不存在（实际位置: runs/queue_runner.log）
/root/auto_transition.log → 不存在（实际位置: runs/d048_auto_transition.log）
/root/remaining_queue.log → 不存在
/root/d048_ss_s123.log → 不存在
```

### 6. results 目录（按时间排序）
```
d048_final_ar/         May 23 09:01  (1个文件: base_s42_ar_n50.json)
d048_ar_n50_existing/  May 23 08:43
d048_ss_s42/           May 23 07:02
instruction_retention  May 21
base_ultrachat_*       May 19
```

### 7. runs 目录（近期）
```
d048_auto_transition.log  May 23 09:01
d048_final_ar_eval.log    May 23 09:01
queue_runner.log          May 23 08:43
d048_ss_s42/              May 23 06:52
```

### 总结
- **eval 流水线正在跑**：6 个 AR eval 任务完成了 1/6 (base_s42)，正在执行 2/6 (TG s42)
- **SS s123 训练刚启动**：step 0 刚输出，总共 3000 steps
- GPU 利用率 66%，显存充裕（29%）
- 所有进程正常运行，无报错

---
