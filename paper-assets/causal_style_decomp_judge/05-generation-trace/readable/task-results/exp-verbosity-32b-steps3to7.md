# exp verbosity 32b steps3to7

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_verbosity_32b_steps3to7_20260520T205331_result.json`
- **Structured JSON:** [`354a0e17b5a1825d3f06.json`](../../sessions/35/354a0e17b5a1825d3f06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**NLI pass rate = 65.0%，低于 80% 阈值。按指令停止 pipeline，不继续后续步骤。**

```
=== H1: Content Preservation ===
NLI pass rate (≥0.90): 65/100 (65.0%)  ← 低于 80% 阈值
NLI mean: 0.6544
BERTScore pass rate (≥0.85): 27/100 (27.0%)
BERTScore mean: 0.7522
Both pass: 22/100 (22.0%)

=== Double-Rewrite ===
NLI mean: 0.4847
BERTScore mean: 0.7199
Passed: 4/100 (4.0%)
```

**诊断**：verbosity 轴的 counterfactual generation 改变了过多语义内容，不仅仅是改写风格。BERTScore 尤其低（均值 0.75，27% 通过 0.85 阈值），表明原文和反事实文本的词汇/语义差异过大。Double-rewrite 质量更差（NLI 均值 0.48），说明两次改写累积了更多语义偏移。

vLLM (Qwen3-32B) 仍在 GPU 0 运行，是否需要现在 kill？

---
