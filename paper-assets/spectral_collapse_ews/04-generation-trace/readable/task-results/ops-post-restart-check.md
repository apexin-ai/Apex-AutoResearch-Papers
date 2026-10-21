# ops post restart check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-check_20260518T125838_result.json`
- **Structured JSON:** [`9046b952eb4de84294b2.json`](../../sessions/90/9046b952eb4de84294b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp_007 (r=0.2, 5 gens, GPU 0)
- **进程**: ALIVE (PID 188503)
- **进度**: Gen 1 已完成，Gen 2 正在训练中 (step 1900/~2000+)，即将完成 Gen 2 的 fine-tuning
- **已保存结果**: gen 0 + gen 1
  - gen 0: eff_rank=417.5, log_det=2366.7, ppl=9.55
  - gen 1: eff_rank=476.7, log_det=2367.5, ppl=10.28, loss=1.77
- **错误**: 无（padding_side 警告可忽略）

### exp_008 (r=0.3, 10 gens, GPU 1)
- **进程**: ALIVE (PID 194372)
- **进度**: Gen 1 已完成，Gen 2 正在生成样本 (11840/35000)
- **已保存结果**: gen 0 + gen 1
  - gen 0: eff_rank=417.5, log_det=2366.7, ppl=9.55 (同一 base model)
  - gen 1: eff_rank=476.9, log_det=2366.1, ppl=10.19, loss=1.84
- **错误**: 无

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0   | 25017 MiB | 97% |
| 1   | 25017 MiB | 94% |

### 结论
两个实验均在服务器重启后存活，正常运行中，无需任何操作。exp_007 略领先于 exp_008（exp_007 已在 Gen 2 训练阶段，exp_008 还在 Gen 2 生成阶段）。

---
