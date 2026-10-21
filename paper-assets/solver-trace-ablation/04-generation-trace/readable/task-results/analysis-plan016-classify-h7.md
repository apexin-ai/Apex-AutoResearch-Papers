# analysis plan016 classify h7

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan016-classify-h7_20260514T173339_result.json`
- **Structured JSON:** [`fbeb8868e2a591d0edf2.json`](../../sessions/fb/fbeb8868e2a591d0edf2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

结果：

```
n_proved: 96
h7_count: 0    / h7_rate: 0%
h1_count: 96   / h1_rate: 100%
genuine_count: 0 / genuine_rate: 0%
```

96/96 proved 样本全部为 H1（多前提 + 结论嵌入前提），零 genuine。模式清晰：1000 步 exec-only 训练学会了在大量冗余前提中嵌入结论（avg 18.55 components），而非单前提 tautology（H7=0）。因为删除任何一个冗余前提不影响结果，ISR≈0。

---
