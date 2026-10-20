# check westd training and gpu

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-training-and-gpu_20260515T093843_result.json`
- **Structured JSON:** [`641e39eb4b15548b16d6.json`](../../sessions/64/641e39eb4b15548b16d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇报

### CWM 8B (PID 266816, GPU 2)
- **进度**: 4013 / 6633 (**60.5%**)，已运行 15h54m
- **最新 eval_loss**: 日志尾部未显示（eval 刚跑完但 loss 行未落入 tail 范围）
- **速度**: checkpoint 间隔 ~40min/100steps（含 eval ~19min）
- **预估完成**: 剩余 2620 steps ≈ **17h** → **5月16日 ~11:00**

### S42 Resume (PID 295794, GPU 1)
- **进度**: 4041 / 6633 (**60.9%**)，刚完成 step 4000 eval
- **最新 eval_loss**: **0.3694** (epoch 1.81)
- **速度**: ~8 s/it 训练 + ~14min eval/100steps
- **预估完成**: 剩余 2592 steps ≈ **12h** → **5月16日 ~06:00**

### GPU 状态
| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| cuda:0 | 0% | 0 / 32GB | **空闲** |
| cuda:1 | 96% | 27.3 / 32GB | S42 Resume (PID 295794) |
| cuda:2 | 97% | 30.7 / 32GB | CWM 8B (PID 266816) |
| cuda:3 | 0% | 0 / 32GB | **空闲** |

两张卡空闲（cuda:0, cuda:3），可用于新任务。

---
