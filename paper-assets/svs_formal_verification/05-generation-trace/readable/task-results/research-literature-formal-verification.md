# research literature formal verification

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_formal_verification_20260514T103412_result.json`
- **Structured JSON:** [`f43e159cd997a1e7c409.json`](../../sessions/f4/f43e159cd997a1e7c409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入 `artifacts/literature_survey_formal_verification.md`。

**核心发现：**

**两个高风险竞品：**
- **VeriCoT** (2025.11) — 与我们几乎同样的 pipeline：CoT→FOL(SMT-LIB)→Z3 验证，但做 binary 验证，无 MCS/IC scoring，无 PCV
- **VERGE** (2026.01) — 更接近：FOL+Z3+**MCS**，但 MCS 用于 error localization + iterative refinement，不做 graded scoring 或 chain selection

**我们的差异化空间（novelty 中等偏上）：**
1. IC = MCS_size/total_claims 作为连续 graded verifier — 现有工作均为 binary 或定性
2. Premise-Conditioned Verification (PCV) — 现有工作未区分题目约束 vs 推理生成的 claims
3. IC 替代 self-consistency 做 chain selection — 现有 formal verification 工作无人做 Best-of-N selection

**定位建议：** 不宜说 "首次用形式验证检查 CoT"，应说 "首次将形式一致性检查转化为 graded chain selection 机制 + PCV 框架"。论文中需清晰区分与 VERGE 的 MCS 用法差异。

---
