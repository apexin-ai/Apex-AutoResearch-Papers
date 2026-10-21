# diagnosis server health 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_server-health-28034_20260520T033334_result.json`
- **Structured JSON:** [`05831c3505416faadd94.json`](../../sessions/05/05831c3505416faadd94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 58% | 31376/32607 MiB |
| 1 | 65% | 31400/32607 MiB |
| 2 | 58% | 30638/32607 MiB |
| 3 | 60% | 30614/32607 MiB |

4 块 RTX 5090 全部满载，正常。

### exp-009 (Continuous Probe Probability GRPO) — **ALIVE**
- **进程**: PID 200283 存活（运行 27 分钟），实际训练 worker PID 200881/200882（DeepSpeed, GPU 1,2）
- **进度**: step 70/8000 (1%), epoch 3.18, ~22s/step
- **指标**: reward=0.494, loss=-0.0001, grad_norm=0.046, entropy=0.456, clipped_ratio=77%
- **注意**: clipped_ratio 偏高（77%），说明大部分生成被 max_length 截断。r2_mean 一直为 0。

### exp-002v3 (DC-GRPO scaled cosine) — **ALIVE**
- **进程**: PID 153957/154537 存活（运行 9h02m），DeepSpeed, GPU 0,3
- **进度**: step 2440/8000 (30%), epoch 110.91, ~10.7s/step
- **指标**: reward=0.641, loss≈0, grad_norm=0.00016, entropy=0.009, frac_reward_zero_std=61%
- **注意**: entropy 极低（0.009）且 grad_norm 接近 0，模型可能已 collapse 到近乎确定性输出。frac_reward_zero_std=61% 说明多数 batch 内 reward 方差为 0（所有 completion 得到相同 reward），GRPO 梯度失效。

两个实验进程均存活，训练正常推进。但 exp-002v3 的 entropy/grad_norm 指标值得关注。

---
