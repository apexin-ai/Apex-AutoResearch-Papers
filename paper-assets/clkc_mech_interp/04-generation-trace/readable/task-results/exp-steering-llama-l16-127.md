# exp steering llama L16 127

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_steering-llama-L16-127_20260524T004213_result.json`
- **Structured JSON:** [`829bc1d38f04bdaeca49.json`](../../sessions/82/829bc1d38f04bdaeca49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## L16 Steering 实验结果

### Probe
- **Probe accuracy at L16: 0.915**（与 L12/L13/L14 同条件训练的 probe）

### Baseline
- contextual: 131, neither: 56, both: 10, parametric: 4（N=201）

### 各 alpha 结果

| alpha | steering flips / N | control flips / N | Fisher exact p |
|-------|-------------------|-------------------|----------------|
| -20 | 49/201 (24.4%) | 47/201 (23.4%) | 0.907 |
| -10 | 29/201 (14.4%) | 23/201 (11.4%) | 0.458 |
| -5 | 15/201 (7.5%) | 12/201 (6.0%) | 0.691 |
| +5 | 10/201 (5.0%) | 9/201 (4.5%) | 1.000 |
| **+10** | **37/201 (18.4%)** | **17/201 (8.5%)** | **0.005** |
| +20 | 56/201 (27.9%) | 57/201 (28.4%) | 1.000 |

### Bonferroni 校正
- 阈值：p < 0.0083（k=6）
- **alpha=+10 的 p=0.005 通过 Bonferroni 校正**（0.005 < 0.0083）

### 结论：**SUCCESS**

与预期的 negative 不同，L16 在同条件复现下出现了显著的 steering 效应。alpha=+10 的 Fisher exact p=0.005，通过 Bonferroni 校正。这表明 L16 的 probe direction 确实能显著影响模型输出（steering flips 是 control 的 2.2 倍）。原始实验 p=0.12 可能是因为 probe quality 较低（77% vs 91%）导致的 power 不足。

---
