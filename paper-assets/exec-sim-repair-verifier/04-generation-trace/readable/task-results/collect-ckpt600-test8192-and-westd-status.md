# collect ckpt600 test8192 and westd status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_ckpt600-test8192-and-westd-status_20260514T220023_result.json`
- **Structured JSON:** [`ff8cb2053deac0d3e3aa.json`](../../sessions/ff/ff8cb2053deac0d3e3aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. ckpt-600 test@8192 eval — 仍在运行（95.7% 完成）

| 指标 | 当前值 |
|------|--------|
| 进度 | 9370 / 9784 (95.8%) |
| running_acc | **78.9%** |
| 预计剩余 | ~5-7 分钟 |

**对比 ckpt-400 test@8192 = 84.79%，ckpt-600 下降约 5.9 个百分点。** 这确认了真实的泛化退化，不是截断假象。最终结果会非常接近 78.9%（仅剩 414 个样本）。

### 2. 全 GPU 状态

| GPU | 显存 | 利用率 | 任务 | PID |
|-----|------|--------|------|-----|
| 0 | 17.6/32.6 GB | 99% | ckpt-600 test@8192 eval（即将完成） | 294732 |
| 1 | 27.3/32.6 GB | 86% | s42 8B CLS resume training | 295794 |
| 2 | 30.7/32.6 GB | 96% | 8B CWM training (from ckpt-1600) | 266816 |
| 3 | 30.9/32.6 GB | 98% | 8B CLS seed123 training (from ckpt-3000) | 266449 |

4 块 GPU 全部满载。cuda:0 在 eval 完成后将空闲。

### 3. s42 resume 训练进度

- **Step 656 / 6633** (9.9%)
- 从 checkpoint-600 resume，3 epochs 总计 6633 steps
- Loss@650 = 0.9643, lr = 4.75e-5
- 速度 ~8.1s/step → 剩余约 **13.5 小时**

### 关键结论

ckpt-600 test@8192 ≈ **78.9%** accuracy，比 ckpt-400 的 84.79% 低约 6 个百分点。这是真实的过拟合/泛化退化信号。F1_macro 和 unparseable_rate 需要等 eval 跑完最后 ~400 样本后从最终输出获取。要我几分钟后再查一次最终结果吗？

---
