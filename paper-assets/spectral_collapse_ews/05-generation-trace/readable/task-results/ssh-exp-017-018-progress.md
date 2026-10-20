# ssh exp 017 018 progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_017_018_progress_20260522T191441_result.json`
- **Structured JSON:** [`90b96c8f7680ac5c06cb.json`](../../sessions/90/90b96c8f7680ac5c06cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### exp_017 (r=0.2, seed43, cuda:1)
- **Generation**: 6/10
- **状态**: Running — Gen 6 训练已完成 (loss=1.2219)，正在评估中 (computing effective rank + perplexity)
- 评估完成后进入 Gen 7，还剩 4 个 generation

### exp_018 (r=0.5, seed43, cuda:0)
- **Generation**: 1/10
- **状态**: Running — Gen 1 样本生成阶段，12,800/25,000 samples (~51%)
- 生成完还要训练+评估才算 Gen 1 结束，整体进度很早期

日志中无时间戳，无法精确估算完成时间。exp_017 预计还需跑约 40% 的总工作量（4/10 gens），exp_018 约 90%+。

---
