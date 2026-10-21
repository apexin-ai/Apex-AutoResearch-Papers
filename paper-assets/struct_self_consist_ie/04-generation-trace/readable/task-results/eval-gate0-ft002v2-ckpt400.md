# eval gate0 ft002v2 ckpt400

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gate0_ft002v2_ckpt400_20260514T084649_result.json`
- **Structured JSON:** [`df9ab45841c987cbc881.json`](../../sessions/df/df9ab45841c987cbc881.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ft_002_v2 checkpoint-400 Gate 0 结果

| 指标 | ckpt-400 | final (585) | 对比 |
|------|----------|-------------|------|
| NER greedy F1 | **0.6475** | 0.6615 | -1.4pp |
| RE greedy F1 | **0.3793** | 0.4177 | -3.8pp |
| Parse failures | 0 | 0 | — |
| Verdict | **FAIL** | PASS | — |

checkpoint-400 在 NER 和 RE 上均低于 final checkpoint。尤其 RE F1 只有 37.9%（低于 40% 阈线），且 58.8% 的 RE 样本 F1=0。

结论：**final checkpoint (585) 优于 checkpoint-400**，过拟合担忧不成立——后续训练实际上继续改善了性能。Registry 已更新。

---
