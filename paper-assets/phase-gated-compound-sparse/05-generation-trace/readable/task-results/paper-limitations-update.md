# paper limitations update

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_limitations_update_20260516T232234_result.json`
- **Structured JSON:** [`071fa8f8d82b5117701e.json`](../../sessions/07/071fa8f8d82b5117701e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

**discussion.tex:**
1. "Reasoning depth scaling" → "Reasoning depth scaling and architecture dependence"，增加了 LLaMA 架构下 strategy specificity 较弱的讨论（imp/rand 2.0-2.6× vs 15-17×），归因于 random eviction 在 LLaMA 上也有显著 phase gradient
2. 新增 "Recency control as methodological contribution" 段落：claim 用 recency eviction 作 scoring-independent control 在文献中无先例（vs StreamingLLM/H2O 仅作 performance baseline），null result 确认 phase gradient 是 attention-score-specific

**limitations.tex:**
1. "Eviction strategy scope and H2O confound" 段落重写：从"recency 作为未来工作"改为"recency control 已部分验证此 confound（单 sparsity level pilot），全面验证仍为 next step"
2. 修复了 "Task coverage" 段落中两处 em-dash

---
