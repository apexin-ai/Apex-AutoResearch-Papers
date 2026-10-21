# analysis d112 q5 hybrid strategy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d112_q5_hybrid_strategy_20260516T092356_result.json`
- **Structured JSON:** [`083f5e81734ef2a51b95.json`](../../sessions/08/083f5e81734ef2a51b95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存于 `/root/autodl-tmp/struct_self_consist_ie/output/d112_hybrid_strategy/`。

**核心结论：**

| Dataset | %Degen | Greedy | MBR-SJ | **Hybrid** | Hybrid Δ(greedy) |
|---------|--------|--------|--------|------------|------------------|
| SciERC NER (N=8) | 21.1% | 0.6182 | 0.6188 | **0.6200** | **+0.0018** |
| CoNLL NER (N=16) | 58.0% | 0.7239 | 0.7215 | 0.7215 | -0.0024 |
| SciERC RE (N=16) | 45.7% | 0.2904 | 0.2847 | 0.2847 | -0.0057 |

Hybrid 策略（degenerate 用 greedy，non-degenerate 用 MBR-SJ）仅在 SciERC NER 上微弱优于 greedy (+0.18pp)。CoNLL/RE 的 degenerate 比例高（58%/46%），且在 non-degenerate instances 上 MBR 选择并未超过 greedy，导致 hybrid 反而略低于 greedy。

---
