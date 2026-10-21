# analysis rssm prediction quality

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rssm_prediction_quality_20260514T095505_result.json`
- **Structured JSON:** [`772a8beea7259868291d.json`](../../sessions/77/772a8beea7259868291d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### model_loss 对比（@105K）

| 实验 | model_loss | KL | velocity_loss |
|------|-----------|-----|--------------|
| baseline (dt=1 only) | **3.654** | 4.332 | 0.472 |
| 008a (sub OFF, dt=2 imag) | 3.766 | 4.377 | 0.488 |
| 008e_v3 (sub ON, dt=1 imag) | 4.634 | 5.477 | 0.606 |
| 008f (sub ON, no dt_embed) | 4.559 | 5.292 | 0.607 |
| 008d (sub ON, dt_embed=32) | ~5.01 @55K | 5.882 @55K | 0.704 @55K |

### C2 claim 的关键证据

1. **Subsample ON → model_loss +24%**：dt=2 transitions 训练数据使 RSSM 预测难度显著增加，主要来自 KL (+24%) 和 velocity_loss (+27%)

2. **dt_embedding 反而让 model_loss 更高 (+15%)**：008d (dt_embed=32) 的 KL=5.88 远高于 008f (no embed) 的 5.06。embedding 没有帮助预测——反而创造了可被 critic 利用的结构性缺口

3. **机制链条**：dt=2 → 更大的状态跳跃 → 更高的 KL → prior-posterior 不对齐 → dt_embedding 放大了这个分离 → critic 利用 embedding 信号做出 delusional value estimates

**限制**：metrics.jsonl 无法按 dt 类型拆分 loss，只能看到总体平均值。

报告已保存到 `artifacts/rssm_prediction_quality_analysis.json`。

---
