# analysis grpo qwen math v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_qwen_math_v3_20260516T154508_result.json`
- **Structured JSON:** [`93bb683b394f0146f3fa.json`](../../sessions/93/93bb683b394f0146f3fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 registry 已更新为 DONE。分析完成，总结如下：

---

## 结果总结

### grpo_rasp_qwen_math_v3 → **SUCCESS**
- Permanent collapse 在 Qwen2.5-Math-7B 上复现
- reward 全程 0.04-0.08，frac_zero_std 0.55-0.70，clipped_ratio ~0.98
- 与 DeepSeek RASP collapse 定性一致（但程度较轻：frac_zero_std 0.65 vs DeepSeek 0.95）

### grpo_standard_qwen_math_v3 → **NEGATIVE**
- Standard 在 Qwen Math 上也出现 **permanent collapse**，而非预期的 transient dip + recovery
- frac_zero_std 0.75-0.90，**比 RASP 更严重**
- DeepSeek 上 Standard 的 recovery 优势不具备跨模型泛化性

### 对论文的影响
- **C1 (RASP collapse)** 获得第二个模型支持 ✓
- **C2 (Standard recovery)** 不能 claim 为通用现象，需弱化表述或探究 model-specific 原因
- 建议关键后续实验：Qwen Math **unpruned** GRPO baseline，确认是 pruning 导致的 collapse 还是 model 本身的问题

---
