# inference qwen scierc seed456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inference_qwen_scierc_seed456_20260515T050627_result.json`
- **Structured JSON:** [`f0768801cbe853545dba.json`](../../sessions/f0/f0768801cbe853545dba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_018_qwen_scierc_seed456 完成，结果如下：

**输出验证**: `samples.jsonl` = 551 行 × 8 samples ✓

**NER 结果**:
- Greedy F1: 0.6627, Oracle F1: 0.7766 (headroom +11.4pp)
- ρ(SJ, F1) full: +0.3445, conditional: +0.3062
- Structural > Surface: **YES** (advantage +0.113)

**RE 结果**:
- Greedy F1: 0.4195, Oracle F1: 0.5858 (headroom +16.6pp)
- ρ(SJ, F1) full: +0.2466, conditional: +0.2862
- Structural > Surface: **NO** (delta -0.058)
- 44.5% samples F1=0

**Verdict: FAIL** — RE 的 ρ_sj (0.2466) 未达到 0.40 阈值，且 structural 未胜过 surface。日志建议降温到 T=0.7 重跑（>30% RE samples F1=0 表明 T=1.0 下 RE 输出质量不稳定）。

---
