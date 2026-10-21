# analysis aime bias ratio

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aime-bias-ratio_20260520T134142_result.json`
- **Structured JSON:** [`445ad32e0bd7665f797d.json`](../../sessions/44/445ad32e0bd7665f797d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**AIME bias ratio 是结构性不可计算的**，原因是 QwQ-32B 在 22 道 AIME 题上的 answer diversity = 0%（每题只有 1 个候选答案，所有 traces 收敛到同一数值），FOLIO 风格的 bias ratio 公式退化为 1.0/0.0 = undefined。

核心发现：

| 指标 | FOLIO (Mistral-7B, N=204) | AIME (QwQ-32B, N=22) |
|------|---------------------------|----------------------|
| Bias ratio (wrong) | **4.97×** | **undefined** |
| Multi-candidate rate | 高 (3-category) | **0%** |
| SICA ≡ SC | 否 (SICA +4.9pp) | **是 (gap=0)** |
| 错误题的失败模式 | 约束偏向多数错答 | 约束提取完全失败 (6/22=27%) |

**关键交叉因子**：FOLIO 用 Mistral-7B（弱模型），AIME 用 QwQ-32B（强推理模型）。QwQ-32B 在 ProofWriter（逻辑域，同 FOLIO 答案空间）上也几乎无 diversity（effective C0=2.6%）。因此零 diversity 是**模型效应**（强推理模型→确定性输出），而非任务效应。

**结论**：AIME 跨任务泛化 **inconclusive**。需要用弱模型（如 14B/7B）跑 AIME 才能解耦模型和任务的影响。

产出已保存: `art_20260520_33967c` (JSON)。

---
