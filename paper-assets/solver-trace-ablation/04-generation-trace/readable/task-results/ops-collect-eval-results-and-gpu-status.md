# ops collect eval results and gpu status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-eval-results-and-gpu-status_20260515T022622_result.json`
- **Structured JSON:** [`48359e06802743bdf6e6.json`](../../sessions/48/48359e06802743bdf6e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## 任务 1: eval + classify_h7 已完成
- PID 108514 已结束，eval 在 10:24:23 完成
- Checkpoint: `/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3/checkpoint-500`

**exp1-isr-b03-s43-r3 评估结果（eval_sta.py on proofwriter_fol_100）：**
| 指标 | 值 |
|---|---|
| n_proved | 86/100 |
| PR | 0.86 |
| ISR* (proved_only_mean_isr) | 0.2948 |
| mean_isr (全部) | 0.2535 |
| median_isr | 0.3333 |

**classify_h7 分类结果：**
| 类别 | 计数 | 占 proved 比例 |
|---|---|---|
| H7 strict (single premise == conclusion) | 4/86 | 4.7% |
| H1 strict (multi-prem, concl in premises) | 59/86 | 68.6% |
| H7+H1 合计 | 63/86 | 73.3% |
| N-H (其他) | 23/86 | 26.7% |
| Single premise | 5/86 | 5.8% |
| ISR=1.0 | 0/86 | 0.0% |

## 任务 2: GPU 与训练状态
- **GPU 0**: 0 MiB / 97887 MiB，空闲
- **GPU 1**: 0 MiB / 97887 MiB，空闲
- **PID 51297**: 已结束。`exp1_random_b03_s44_r2` 训练已完成，checkpoint-500 写盘时间 10:25（reward_log 134KB，模型权重齐全），可进入 eval 阶段
- 两张 GPU 现都空闲，可启动新任务

## 任务 3: Checkpoint 路径
- `/root/autodl-tmp/outputs/exp1_isr_b03_s43_r3/checkpoint-500`（已用于本次 eval）

---
