# paper ablation section

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_ablation_section_20260514T081904_result.json`
- **Structured JSON:** [`9662dd9c4e5467022637.json`](../../sessions/96/9662dd9c4e5467022637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处编辑已生效。改动总结：

**§5.3 (C3 — RGDS vs Random 50%)**：
- 展开了变量控制说明：明确列出 same budget / protocol / seed / checkpoint，只有 selection mechanism 不同
- 补充了 p 值和 Cohen's d（p=.017, d=5.61），以及三个 seed 的逐一数值
- 新增最后一段，构建对照组层级：within-budget（无混淆）vs cross-budget（有混淆），指向 §5.4 的降级处理

**§5.4 (S3/D017 — Random vs Uncurated)**：
- 加入 "cross-budget comparison conflates any selection benefit with a data quantity effect" 定性
- 加入 "draw no causal inference about budget effects from this comparison alone" 明确不做因果推断
- 删除了一处冗余的 "in the iterative self-training setting"

---
