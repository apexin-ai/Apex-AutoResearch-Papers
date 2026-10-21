# research experiment coverage

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_experiment-coverage_20260517T124233_result.json`
- **Structured JSON:** [`3c8c76527af482a97760.json`](../../sessions/3c/3c8c76527af482a97760.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。

**总结**: 实验覆盖度 **8/10**。13 个维度中 7 个✅充分覆盖，5 个⚠️部分覆盖，1 个❌未覆盖（多语言）。

三个主要 gap:
1. **Instruction-tuned models** (质疑概率 4/5) — 但 Limitations 已有 preliminary negative data
2. **Generator 规模 13B+** (质疑概率 4/5) — 8.2B 已是 reasonable scope，论文已报告 scale gap
3. **Sampling ablation 仅 1 generator** (质疑概率 3/5) — 论文已有理论解释

**所有 gap 已在 Limitations 中透明报告。8 天 DDL 内不建议补充新实验，重点放在论文打磨和提交准备。** Rebuttal 阶段可优先准备温度 ablation 扩展 (~2h) 和 instruct systematic 实验 (~4h)。

---
