# analysis grpo qwen math v3 pair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_qwen_math_v3_pair_20260516T154824_result.json`
- **Structured JSON:** [`6543fa9b21a07321480a.json`](../../sessions/65/6543fa9b21a07321480a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是核心结论：

---

## Qwen2.5-Math-7B GRPO v3 分析总结

### 跨模型验证结果：**部分失败**

**Standard 20% (negative)**:
- frac_zero_std 全程 0.75-0.90，reward 0.03-0.07，无 clear recovery
- 与 Llama 的 "transient dip→recovery" 不一致，表现为 **persistent reward-signal starvation**
- Entropy 健康 (~0.18)，模型生成多样但全错

**RASP 20% (partial)**:
- **没有** Llama-like 的 reward crash (reward 0.05-0.10，反而比 Standard 高)
- **没有** frac_zero_std 飙升 (0.55-0.70，比 Standard 还低)
- **但有** entropy collapse (0.07 vs Standard 0.18) + length pathology (clipped_ratio ~0.98)
- RASP 损伤在强模型上表现为 **mode collapse**（输出多样性崩塌），而非 reward collapse

### 关键发现

| | Llama-3.2-3B | Qwen2.5-Math-7B |
|---|---|---|
| Standard | Transient dip→recovery | Persistent high frac_zero_std |
| RASP | Reward collapse (→0.04) | Entropy collapse (→0.07) |
| 机制差异 | 能力不足 → 做不出题 | 多样性丧失 → 重复做题 |

Collapse 的**存在性**跨模型一致，但**机制**取决于模型容量。论文应 frame 为 "pruning-method-dependent GRPO fragility" 而非 "universal collapse signature"。

报告和 registry 已更新。

---
