# research d030 answer conditioned constraints

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d030-answer-conditioned-constraints_20260517T061408_result.json`
- **Structured JSON:** [`dadfa76e6ea3e860a54b.json`](../../sessions/da/dadfa76e6ea3e860a54b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调研报告：Answer-Conditioned Constraint Extraction

### 最相关论文

| # | 论文 | Venue | 核心思路 |
|---|------|-------|----------|
| 1 | [Math-Shepherd](https://arxiv.org/abs/2312.08935) | ACL 2024 | 从每步续写多条路径，检查能否到达正确答案——步骤标签本质是 outcome-conditioned |
| 2 | [GRACE](https://arxiv.org/abs/2305.14934) | EMNLP 2023 | 对比学习训练 step-level discriminator，区分正确/错误推理步骤，解码时引导生成 |
| 3 | [DiVeRSe](https://arxiv.org/abs/2206.02336) | ACL 2023 | 多样路径 + step-aware verifier 逐步验证 + 加权投票 |
| 4 | Multi-Agent Debate (D3) | 2024 | 实证表明 debate 增益主要来自 aggregation 而非论证交互——与 SICA 退化问题一致 |
| 5 | [Atomic-SNLI](https://arxiv.org/html/2601.06528v1) | 2025 | 将推理分解为 atomic facts，用 NLI 逐个判断蕴含/矛盾关系 |

### 可适配到 SICA 的技术方案

**推荐优先级: C → B → A**

- **C. Contrastive prompt**（改动最小）: 修改 prompt 为"列出支持答案 X / 反对答案 X 的约束"，使约束天然 answer-conditioned。零额外成本。
- **B. NLI-based filtering**（轻量后处理）: 用现成 NLI 模型判断"约束 → 答案"蕴含关系，过滤掉对所有答案都成立的 domain facts。不需训练，推理成本低。
- **A. Outcome-conditioned labeling**（Math-Shepherd 式）: 对每条约束续写检查与各候选答案兼容性。更精确但推理成本高（每条约束需多次 LLM 调用）。

### 可行性评估

- 方案 C/B 不需训练额外模型，可在现有 pipeline 上快速验证
- 方案 A 推理成本约为当前 3-5 倍（每条约束 × 候选答案数次续写）
- 训练 discriminator（方案 D/GRACE 式）需要标注数据，适合后期优化而非 pilot 阶段

报告已保存到项目 memory.md。

---
