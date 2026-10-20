# research r13 taskB gollie f1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r13_taskB_gollie_f1_20260520T190855_result.json`
- **Structured JSON:** [`a1fe70211afbce274338.json`](../../sessions/a1/a1fe70211afbce274338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。核心发现：

1. **GoLLIE 没有 SciERC RE 的 zero-shot 结果** — SciERC 是 GoLLIE 的 supervised 训练集之一，不是 zero-shot 评测目标。GoLLIE 只在 ACE05 上报了 supervised RE（34B: 70.1 F1）。

2. **SciERC RE 的 baseline 地图**：
   - Supervised SOTA: Rel+ F1 = 42.3 (FSN), Rel F1 = 54.2
   - LLM zero-shot 最好: 23.14 (AgentRE)
   - LLM few-shot 最好: 33.70 (AgentRE)

3. **对 rebuttal 的意义**：我们的 R-F1 40-46% 大幅超越 LLM zero-shot（~23）和 few-shot（~34）baselines，接近 supervised SOTA（42.3 Rel+）。GoLLIE 不能作为 SciERC RE 的 zero-shot 锚点，但 AgentRE 和 GPT-RE 可以。

---
