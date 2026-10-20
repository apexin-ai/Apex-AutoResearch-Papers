# train detector 10pct

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_detector-10pct_20260513T224308_result.json`
- **Structured JSON:** [`1706af026eeb0c5755fe.json`](../../sessions/17/1706af026eeb0c5755fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

两个检测器均完全极化，减少数据量无法解决 q-score 二值化问题：

| 指标 | 10% 数据 (6796+8524) | 5% 数据 (3398+4262) |
|------|---------------------|---------------------|
| **AUC** | 0.9999 | 1.0000 |
| **ECE** | 0.0076 | 0.0036 |
| **Temperature** | 1.5228 | 1.5328 |
| **中间区域 (0.1-0.9)** | 0.7% (9/1360) | 0.4% (3/681) |
| **[0-0.1) 占比** | 48.5% | 49.3% |
| **[0.9-1.0] 占比** | 50.8% | 50.2% |

**结论**：即使只用 5% 数据，ModernBERT 仍然能完美区分 human 和 synthetic 文本。问题不在数据量——分类任务本身对该模型太简单。

**需要 Director 决策**：单纯减少数据无法产生有意义的不确定性。可能需要考虑替代方案，例如：
1. 用更弱的模型（如小型 CNN/浅层模型）
2. 人为截断训练（极早停止，如只训练几十步）
3. 对 logits 注入噪声
4. 使用 label smoothing 或高温度参数
5. 改变检测目标（不是检测 human vs synthetic，而是检测更细粒度的特征）

---
