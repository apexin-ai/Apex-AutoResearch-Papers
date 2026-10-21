# code d146 isr s44 final and eval launch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-isr-s44-final-and-eval-launch_20260520T023003_result.json`
- **Structured JSON:** [`eee1406b59ae2634e7bb.json`](../../sessions/ee/eee1406b59ae2634e7bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval/classify 已启动并运行中。

## 汇总

### 1. isr-s44 训练：已完成 ✓
- **500/500 步**，结束于 2026-05-20T01:52:14 UTC（已空闲 ~8.5 小时）
- Final model 存在（4 shards）

### 2. 轨迹（每 50 步）

| Step | prove_rate | ISR | reward |
|------|-----------|-----|--------|
| 1 | 0.375 | 0.068 | 0.382 |
| 51 | 0.500 | 0.143 | 0.514 |
| 101 | 0.500 | 0.115 | 0.512 |
| 151 | 0.500 | 0.219 | 0.522 |
| 201 | 0.000 | 0.000 | 0.000 |
| 251 | 1.000 | 0.351 | 1.035 |
| 301 | 0.500 | 0.156 | 0.516 |
| 351 | 0.500 | 0.200 | 0.520 |
| 401 | 1.000 | 0.290 | 1.029 |
| 451 | 0.000 | 0.000 | 0.000 |
| 500 | 0.000 | 0.000 | 0.000 |

**统计**：
- prove_rate: mean=0.454, final_50=0.487
- ISR: mean=0.131, final_50=0.145
- 366/500 步有非零 prove_rate（nz mean: pr=0.620, ISR=0.178）

### 3. eval/classify：已启动 ✓
- tmux session `d146-eval` 运行中
- 当前：Step 0（base model Qwen3-4B），已完成 4/100 样本
- eval_sta.py PID=689352，GPU 0 占用 8501 MiB / 50%
- 脚本将依次评估：base → 6 个实验模型 → batch summary

### 4. GPU 状态
- GPU 0：8501 MiB used，50% 利用率（eval 运行中）

---
