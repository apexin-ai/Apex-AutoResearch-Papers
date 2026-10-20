# ssh deepseek progress update

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deepseek_progress_update_20260515T150930_result.json`
- **Structured JSON:** [`f26b7045cf4740d3c820.json`](../../sessions/f2/f26b7045cf4740d3c820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### exception_only — **已完成** ✓

| 指标 | 值 |
|------|-----|
| Accuracy | **99.3%** (95% CI: 98.8%–99.7%) |
| Majority baseline | 71.5% (always predict pass) |
| Lift over baseline | **+27.8pp** |
| pass | P=1.00, R=0.99, F1=1.00 |
| fail | P=0.98, R=1.00, F1=0.99 |

结果已保存至 `deepseek_exception_only/final/eval_results.json`。

### full_trace — **训练中**

- 当前进度：**167/444 steps (37.6%)**
- 已运行：~1h21m
- 速度：~16.6s/step
- 剩余 277 steps，预估还需 **~1h17m**

### GPU

| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 | 100% | 71.6 / 97.9 GB |
| GPU 1 | 0% | 0 / 97.9 GB |

full_trace 只用了 GPU 0，GPU 1 空闲。

---
