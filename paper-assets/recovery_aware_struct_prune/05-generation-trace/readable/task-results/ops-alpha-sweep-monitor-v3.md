# ops alpha sweep monitor v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_alpha-sweep-monitor-v3_20260515T213943_result.json`
- **Structured JSON:** [`6b1c0b4a0587bdfbcc5c.json`](../../sessions/6b/6b1c0b4a0587bdfbcc5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。最终摘要：

## α Ablation Sweep (westb, cal=512, post-prune GSM8K N=100)

| α | Accuracy | EOS Rate | Avg Len |
|---|----------|----------|---------|
| 0.0 | 27% | 80% | 1192 |
| 0.25 | 23% | 63% | 1834 |
| 0.5 | 22% | 81% | 1141 |
| **1.0** | **31%** | **92%** | **733** |
| **2.0** | **36%** | 59% | 2130 |

### vs westd (cal=256)

| α | westb (cal=512) | westd (cal=256) |
|---|----------------|----------------|
| 0.0 | 27% | 30% |
| 0.5 | 22% | 25% |
| 1.0 | 31% | 27% |
| 2.0 | 36% | — |
| 4.0 | — | 40% |

### 分析

1. **非单调关系在两个 calibration 设定下均确认**：小 α (0.25-0.5) 反而比 α=0.0 更差，大 α (≥1.0) 才有增益。Recovery 信号在低权重时引入噪声，需要足够强的权重才能有效引导剪枝决策。

2. **α=2.0 精度最高 (36%) 但生成质量差**：EOS 率仅 59%（41% 截断），平均长度 2130。α=1.0 是精度-生成质量的最佳平衡点（31%, EOS 92%, avg_len 733）。

3. **Calibration 影响**：westb (cal=512) 在 α=1.0 时优于 westd (cal=256) (31% vs 27%)，说明更多 calibration 样本在中等 α 时帮助更大。两者都呈 U 形曲线。

4. **α=2.0 的高精度可能是假象**：低 EOS 率+长响应意味着模型倾向用更多 token "暴力搜索"答案，而非高效推理。α=1.0 的短响应+高精度更有说服力。

---
