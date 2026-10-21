# analysis body paren spotcheck b03 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_body-paren-spotcheck-b03-s44_20260516T073851_result.json`
- **Structured JSON:** [`16604c041fec3e0985cb.json`](../../sessions/16/16604c041fec3e0985cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**exp1-isr-b03-s44-r2 的 genuine = 0，不是 19。**

所有 95 个 proved 样本都是 H7a（单 premise 文本完全等于 conclusion），甚至不需要任何归一化（纯 whitespace normalization 就能匹配）。Body-paren 修复对这个实验 **无影响**。

这是 ISR β=0.3 s44 的极端 mode collapse：模型学会了对每道题只输出一个 premise = conclusion 的恒真式。

### 对比 s43

你可能把 s44 和 s43 搞混了。s43_r3 有实际的 genuine 样本：

| 指标 | s43_r3 (旧audit) | s43_r3 (新script) | s44_r2 |
|------|---------|---------|--------|
| Proved | 86 | 86 | 95 |
| H7a | 4 | 5 (+1 body-paren) | 95 |
| H1 | 59 | 60 | 0 |
| H8 | 0 | 1 | 0 |
| Genuine | 23 | 20 | **0** |

s43 的 body-paren 修复多抓了 1 个 H7a，新 script 总共减少 3 个 genuine (23→20)。

### 结论

- **s44 spot check 不需要做** — 没有 genuine 可查
- 如果要 spot-check body-paren 效果，目标应该是 **s43_r3** (genuine 从 23 降到 20)

---
