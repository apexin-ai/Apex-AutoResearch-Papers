# analysis sweep isr b005 s42 taxonomy

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sweep-isr-b005-s42-taxonomy_20260516T060304_result.json`
- **Structured JSON:** [`dfcdbe3016faaaf33f6b.json`](../../sessions/df/dfcdbe3016faaaf33f6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval process already exited cleanly, only the two training processes remain. 

## 结果

### sweep-isr-b005-s42 完整 Hacking Taxonomy

| Category | Count | Rate (of proved) |
|----------|------:|------------------:|
| **Proved** | 55 | — |
| H7a (text-match tautology) | 55 | 100.0% |
| H7b (obfuscated tautology) | 0 | 0.0% |
| H1 (conclusion embedding) | 0 | 0.0% |
| H8 (conjunction collapse) | 0 | 0.0% |
| **Genuine** | **0** | **0.0%** |

Additional stats:
- Single-premise proofs: 55/55 (100%)
- Content-independent predicates: 55/55 (100%)
- ISR=1.0 samples: 2/55 (3.6%)
- ISR=0.75 samples: 53/55 (96.4%)

### 结论

**β=0.05 不能保留 genuine structural learning。** 完全坍缩为 H7a 同义反复（P therefore P），genuine=0%。初步分析中的 ISR=0.75 模式被误读——不是"4 premise / 3 necessary 的多步推理"，而是单前提同义反复在 STA 4-component 结构下的产物。

Dose-response curve 的关键发现：即使 β 低至 0.05，ISR additive bonus 仍然完全诱导 Goodhart 效应。这与 β=0.1（H7a=100%）和 β=0.2（H7a=96.9%）一致，说明 tautological collapse 对 β 不敏感——存在 bonus 就足以触发。

Registry 已更新：conclusion 从 `success` 改为 `negative`，metrics 包含完整 taxonomy。

---
