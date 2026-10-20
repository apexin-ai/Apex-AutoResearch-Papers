# ops nomarker seed123 completion

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_nomarker-seed123-completion_20260516T190600_result.json`
- **Structured JSON:** [`329134b9eb100604e30a.json`](../../sessions/32/329134b9eb100604e30a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已完成，结果如下：

## 汇报

**1. 训练状态：成功**
- 3 epochs, 444 steps, 训练时间 ~75 分钟
- train_loss: 0.1074, eval_loss: 0.4814
- Checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only_nomarker/final`

**2. Eval 结果（n=1190）：**

| 指标 | 值 | 95% CI |
|------|-----|--------|
| **Accuracy** | **97.82%** | [96.97%, 98.57%] |
| Majority baseline | 71.51% | |
| **Lift** | **+26.3%** | |
| Pass precision | 0.970 | |
| Pass recall | 1.000 | |
| Pass F1 | 0.985 | |
| Fail precision | 1.000 | |
| Fail recall | 0.923 | |
| Fail F1 | 0.960 | |

**3. GPU 状态：**
- GPU 0: 0% 利用率，但 49GB 显存占用（训练进程残留，需 kill 释放）
- GPU 1: 100% 利用率，46GB 占用（有其他任务在跑）

GPU 0 利用率为 0 但显存未释放，可能是训练进程退出后 PyTorch 未清理。如需复用 GPU 0，需要找到并 kill 残留进程。

---
