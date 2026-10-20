# analysis probe 002

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_probe-002_20260514T094949_result.json`
- **Structured JSON:** [`df430feae0f06951516b.json`](../../sessions/df/df430feae0f06951516b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。

## probe-002 分析总结

probe-002 使用全量数据（54,809 windows, min_confidence=0）训练 GRU probe，epoch 9 达到最佳 val macro-F1=0.8862，epoch 14 触发 early stopping。

**测试集指标**：macro-F1=**0.8468**，accuracy=0.8785，F1(stagnation)=0.7772，F1(progress)=0.9165。相比最强 baseline Repeat-3（macro-F1=0.6104），GRU probe 提升 +0.2365（+38.7%）。

**与 probe-001 对比**：全量数据 macro-F1（0.8468）较 conf≥2 子集（0.9055）**下降 0.0587**。数据量从 15,401 扩大到 54,809（+256%），但 F1 反而下降约 6.5%。

**结论**：低置信度样本引入了噪声，稀释了高质量标注的信号。conf≥2 子集虽然数据量仅为全量的 28%，但标注质量更高，模型表现更优。这验证了弱监督标注中置信度过滤的必要性——在数据量和标注质量之间，质量优先的策略更有效。

---
