# check westd 41718 full status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_41718_full_status_20260520T124443_result.json`
- **Structured JSON:** [`889dbff2ddf4b434ea7a.json`](../../sessions/88/889dbff2ddf4b434ea7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 状态总结

### 1. GPU 状态
| GPU | 显存使用 | 显存总量 | GPU 利用率 |
|-----|---------|---------|-----------|
| 0 | 66,101 MiB | 97,887 MiB (67.5%) | 100% |
| 1 | 46,199 MiB | 97,887 MiB (47.2%) | 100% |

两张卡都满载运行。

### 2. Python 进程
- **PID 249688** — `benchmark_eval.py --exp_id bce_ste_s42_eval` (GPU 0)，运行 52 分钟，CPU 100%
- **PID 254228** — `benchmark_eval.py --exp_id c4_ood_downstream_kl30` (GPU 0，但实际占用了 GPU 1 显存)，运行 3 分钟，CPU 113%

### 3. tmux sessions
`tmux ls` 被 read_only 拦截，无法检查。（两个任务都是 nohup 启动的，符合 C002 约束。）

### 4. BCE+STE downstream eval (PID 249688)
- **状态：RUNNING**
- 日志路径：`/tmp/bce_ste_s42_eval.log`
- 当前进度：MMLU loglikelihood 请求 **12,457 / 40,168 (31%)**，速度 ~21.2 it/s
- 已完成任务：wikitext2 PPL、arc_challenge、winogrande、gsm8k、hellaswag、piqa（均已跑完）
- 正在跑：**MMLU**（57 个子任务，总量大）
- 结果文件：**尚未生成**（`results/benchmark/bce_ste_s42_eval/` 目录存在但为空）
- 预估剩余：(40168-12457) / 21.2 / 60 ≈ **21.8 分钟**跑完 MMLU，之后写结果

### 5. C4 OOD downstream (PID 254228)
- **状态：RUNNING**
- 当前进度：loglikelihood 请求 **2,640 / 4,687 (56.3%)**，速度 ~21.8 it/s（正在跑 6 个 downstream task）
- Sparsity：KL30 predictor，uniform allocation，model-level 0.295
- 结果文件：**尚未生成**
- 预估剩余：取决于还有哪些 task 未跑，但当前 batch 约 **1.6 分钟**

### 6. BCE+STE checkpoint
```
predictor_bce.pt  151,965,283 bytes (145 MB)  2026-05-20 19:52
```

### 7. 磁盘
| 分区 | 大小 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / | 30G | 7.8G | 23G | 26% |
| /root/autodl-tmp | 250G | 47G | 204G | 19% |

磁盘充裕，无风险。

**总结：两个 eval 任务都在正常运行中。BCE+STE eval 的 MMLU 还需约 22 分钟；C4 OOD downstream 进度过半，预计较快完成。**

---
