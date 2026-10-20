# research temp diversity

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_temp-diversity_20260515T111724_result.json`
- **Structured JSON:** [`755da67da323e9172d1e.json`](../../sessions/75/755da67da323e9172d1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行 35 分钟，趋势已非常明确。让我给你一个中间报告，脚本会继续在后台运行至完成。

---

## 中间诊断结果（3/5 题完成 + 第4题部分）

### 数据汇总

| Problem | Level | T=0.7 | T=0.9 | T=1.0 |
|---------|-------|-------|-------|-------|
| test/algebra/2277 | 5 | 1u, 0(10/12) | 1u, 0(9/12) | 1u, 0(9/12) |
| test/intermediate_algebra/582 | 5 | 0u (无boxed) | 0u (无boxed) | 0u (无boxed) |
| test/number_theory/427 | 5 | 1u, 25(12/12) | 1u, 25(12/12) | 1u, 25(12/12) |
| test/precalculus/1199 | 4 | 1u, π(2/12) | 进行中... | — |

### 核心发现

1. **在所有温度下(0.7/0.9/1.0)，QwQ-32B 都产生完全一致的答案 — 零分歧**
2. Problem 2 (x^10方程) 4096 tokens 完全不够，所有 trace 都截断无答案
3. Problem 4 (图形题) 大多数 trace 截断（没有图片输入只能猜）
4. 对能完成的题(Problem 1和3)，12/12 或 9-10/12 给出完全相同的答案

### 分析

**QwQ-32B 是 reasoning model，其内部推理链条非常确定性**。即使 temperature=1.0，只要推理步骤有明确的逻辑路径，模型都会收敛到相同答案。这不是温度不够高的问题，而是模型本身的特性。

### 建议

要产生 trace 分歧（让 MVP C2 PASS），需要：

1. **使用更难的题（AIME/竞赛题）** — 推理路径不唯一的题目
2. **增大 max_tokens 到 8192-12288** — 让更多题能完成推理（当前4096太短，很多题截断）
3. **换用非-reasoning model**（如 Qwen2.5-72B-Instruct 非 QwQ）— 普通模型在高温度下分歧会更大
4. **或：改变 MVP C2 的预期** — 接受"强模型在简单题上零矛盾"的现实，用更难的题集做评测

脚本还在跑（剩余 Problem 4 的 T=0.9/1.0 和 Problem 5），完整结果会保存到 `results/diversity_diagnosis.json`。需要我等它跑完再报告最终数据吗？

---
