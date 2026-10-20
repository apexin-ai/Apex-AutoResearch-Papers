# research related work literature

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-literature_20260513T021053_result.json`
- **Structured JSON:** [`fa69605e07d384f287ac.json`](../../sessions/fa/fa69605e07d384f287ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不可用。文件已直接保存到 artifacts 目录。

产出总结：

**文件位置：** `artifacts/literature_survey_related_work.md`

**覆盖 20 篇论文，按 4 个方向组织：**

**Direction 1 — Cross-method Consensus (4篇)**
- **CIRCUS (Parekh, 2026)** — 直接竞争对手。在单一归因方法上变化剪枝阈值取共识。CSS 的差异化：跨方法多样性 > 阈值多样性
- Certified Circuits (Anani et al., 2026) — 数据扰动稳定性，互补
- Open Problems in MI (Sharkey et al., 2025) — 明确呼吁报告 explanation ensembles，直接支持 CSS
- Circuit Tracing (Anthropic, 2025) — feature-level 平行方向

**Direction 2 — Faithfulness Evaluation (4篇)**
- **Miller et al. (COLM 2024)** — faithfulness metrics 对消融方法极其敏感，强支持 CSS
- Hanna et al. (COLM 2024) — EAP-IG 原论文，overlap ≠ faithfulness
- MIB Benchmark (2025–2026) — 标准化评估框架
- DiscoGP (Yu et al., 2024) — weight+edge 联合剪枝

**Direction 3 — Binary vs Continuous Scoring (5篇)**
- Edge Pruning (Bhaskar et al., NeurIPS 2024) — CSS 基础方法，binary masks
- Syed et al. (BlackboxNLP 2024) — EAP vs ACDC 方法间差异
- HAP (NeurIPS 2025) — EAP→EP 串行组合，与 CSS 的并行共识互补
- Sparse Feature Circuits (ICLR 2025 Oral) — feature-level circuits
- Transcoders (NeurIPS 2024) — 替代 circuit 表征

**Direction 4 — Single-method Instability (6篇)**
- **Méloux et al. (2025–2026)** — 定量证明 EAP/EAP-IG 电路高方差，强支持 CSS
- Sun (ACL 2025) — 形式化 circuit stability 概念
- Franco et al. (2026) — IOI 无单一电路，prompt-specific
- Formal MI (ICLR 2026) — 可证明保证方向
- CD-T (ICLR 2025) — 潜在可纳入 CSS 的新方法
- ACDC (NeurIPS 2023) — CSS 基础方法

**关键定位建议：**
1. CIRCUS 是最大竞争对手——核心区分点是 method diversity vs threshold diversity
2. 分布偏移下的鲁棒性评估是 CSS 独有的贡献
3. Binary consensus 避免了跨方法分数校准问题
4. 文献充分支持"单方法不稳定"的前提

---
