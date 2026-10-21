# code d146 final status and eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-final-status-and-eval_20260520T003447_result.json`
- **Structured JSON:** [`b416da2cee0ca90126ce.json`](../../sessions/b4/b416da2cee0ca90126ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D146 Pipeline Status

### 5/6 完成，isr_s44 仍在训练

| Experiment | Step | Prove Rate | ISR Mean | Reward | Status |
|---|---|---|---|---|---|
| d146_pf_exec_s42 | 500 | 1.000 | 0.000 | 1.000 | **DONE** |
| d146_pf_exec_s43 | 500 | 1.000 | 0.205 | 1.000 | **DONE** |
| d146_pf_exec_s44 | 500 | 1.000 | 0.043 | 1.000 | **DONE** |
| d146_pf_isr_s42 | 500 | **0.000** | 0.000 | 0.000 | **DONE (collapsed)** |
| d146_pf_isr_s43 | 500 | 1.000 | 0.205 | 1.020 | **DONE** |
| d146_pf_isr_s44 | 175/500 | 0.500 | 0.100 | 0.510 | **RUNNING** |

### isr_s44 详细统计
- 176 steps done, speed=0.07 step/s
- prove_rate: mean=0.322, final_50=0.395 (still learning)
- ISR: mean=0.088, final_50=0.109
- **ETA: ~72 min (约 10:10 UTC 完成)**

### 警告：isr_s42 完全崩溃
prove_rate=0.0, reward=0.0, isr=0.0 — 训练完全失败。只剩 isr_s43 和 isr_s44 两个有效 ISR seed。

### Eval/Classify: 未启动
isr_s44 还在跑（GPU 0 占用 93%, 83GB），等训练完成后再启动。预计 ~72 min 后可开始。

---
