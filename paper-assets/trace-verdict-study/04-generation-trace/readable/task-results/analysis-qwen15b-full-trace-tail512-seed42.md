# analysis qwen15b full trace tail512 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_full_trace_tail512_seed42_20260517T211954_result.json`
- **Structured JSON:** [`30cb6fdb7af0b55fda73.json`](../../sessions/30/30cb6fdb7af0b55fda73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### 核心指标

| 指标 | 值 |
|------|-----|
| **Accuracy** | **95.6%** (CI: 94.5%–96.8%) |
| Majority baseline | 71.5% |
| Lift | +24.1pp |
| pass F1 / fail F1 | 0.97 / 0.92 |

### 与基准对比

| 条件 | Accuracy |
|------|----------|
| **Qwen-1.5B tail-512 (本实验)** | **95.6%** |
| Qwen-7B tail-512 | 93.61% |
| Qwen-7B tail-256 | 78.9% |
| Qwen-1.5B tail-256 | 72.6% |

### Conclusion: **SUCCESS — scale-invariant phase transition confirmed**

1. **95.6% 超出假设范围上限**，1.5B 比 7B（93.61%）还高 +1.99pp，CI 下界 94.5% 都高于 7B 点估计
2. **Phase transition 是 scale-invariant 的**：两个模型都在 256→512 出现跳变（1.5B: +23pp, 7B: +14.7pp），临界阈值由 trace 信息含量决定，与模型规模无关
3. **1.5B 反超 7B 是意外发现**，可能原因：4720 样本下 1.5B 过拟合更少，或 512 tokens 信号已饱和使额外容量无收益

---
