# research framing 30pct proposal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_framing_30pct_proposal_20260516T025534_result.json`
- **Structured JSON:** [`5be469e05b701432a820.json`](../../sessions/5b/5be469e05b701432a820.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提案已写入 `artifacts/framing_proposal_30pct_downstream.md` 并注册 (`art_20260516_b1c4cd`)。

核心结论：

1. **原 Claim 3 ("30% 为推荐配置") 被数据否定** — MMLU 在 30% 就崩到随机水平，PPL +47% 完全无法预测这一灾难。

2. **根因是 per-layer sparsity 不均匀** — 30% global top-k 把后层（L26-31）推到 50-70% 实际 sparsity，后层直连 LM head，downstream 依赖后层精确输出。

3. **三种 narrative 备选**：
   - **A (推荐主线)**: PPL-downstream disconnect 作为论文核心贡献之一，填补文献空白
   - **B (需新实验)**: Uniform per-layer allocation 修复 collapse — 依赖 P0 实验结果
   - **C (子节)**: Task-sensitive sparsity spectrum，揭示 WinoGrande(robust) → ARC-c(cliff) → MMLU/GSM8K(ultra-fragile) 三层敏感度

4. **关键决策点**: uniform_30% downstream 实验结果决定最终走 A 还是 B。决策树已在提案 §7 给出。

5. **所有已做实验在新 framing 下仍然有效**，部分实验（50% collapse、GSM8K 生成对比）反而升值。

---
