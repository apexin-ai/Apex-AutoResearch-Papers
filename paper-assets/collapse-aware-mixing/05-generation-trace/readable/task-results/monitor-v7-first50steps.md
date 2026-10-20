# monitor v7 first50steps

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_first50steps_20260513T030811_result.json`
- **Structured JSON:** [`7fbcb288cb5dc8c6b566.json`](../../sessions/7f/7fbcb288cb5dc8c6b566.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取完整数据。G0 训练已完成全部 305 步，当前正在评估 checkpoint。

---

## mvp_pilot_v7 G0 训练监控 Summary

### 状态
- **进程 60104**: 存活
- **G0 训练**: 已完成（305/305 步，770.87s）
- **当前阶段**: 评估 checkpoint 2/6（step 152），正在生成 500K tokens

### Loss 趋势（logging_steps=50）

| Step | Loss | grad_norm | lr |
|------|------|-----------|------|
| 50 | 2.6315 | 1.633 | 1.77e-06 |
| 100 | 2.6011 | 1.430 | 1.43e-06 |
| 150 | 2.5849 | 1.352 | 1.08e-06 |
| 200 | 2.5825 | 1.336 | 7.34e-07 |
| 250 | 2.5873 | 1.219 | 3.88e-07 |
| 300 | 2.5756 | 1.289 | 4.15e-08 |

**平均 train_loss**: 2.5934

### 检查结果

- ✅ **loss < 5** — 全程 2.58~2.63，正常收敛，缓慢下降
- ✅ **无 NaN/Inf**
- ✅ **grad_norm 稳定** — 全程 1.2~1.6，无异常
- ❌ **right-padding 警告仍在出现**（68 次）— `padding_side='left'` 修复未生效，在 eval 阶段生成文本时仍触发

### Eval 中间结果（checkpoint 1/6, step 76）
- eff_rank=679.7, ppl=13.53, entropy_var=2.8285, unigram_H=6.906, coverage=0.4686

### 关注项
1. **padding 警告**: 修复未覆盖评估阶段的 tokenizer 加载——生成文本时模型加载了默认 padding_side='right' 的 tokenizer。这会影响 perplexity 计算的准确性。
2. Loss 从 2.63 降到 2.58，降幅仅 ~2%，符合 20M tokens 单 epoch 的预期（数据量小，模型大）。

---
