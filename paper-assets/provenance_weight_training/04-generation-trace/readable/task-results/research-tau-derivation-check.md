# research tau derivation check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tau_derivation_check_20260515T153144_result.json`
- **Structured JSON:** [`08d4f3f1be35fa053fbd.json`](../../sessions/08/08d4f3f1be35fa053fbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心结论：

1. **2602.16065 中不存在 τ**。论文的 α 是已知设计参数，无 α_eff/importance weighting 概念。
2. **D025 判断基本正确**，但叙述需修正：不是"τ 来源于该论文"，而是"Wang 的收敛理论 motivates 需要质量阈值，τ 是我们自己的实践构造"。
3. **代码中 `τ = 1.0 - contamination_ratio * 0.5` 是真正的问题**——直接使用已知比例，与 Claim 3 矛盾。应改为固定默认值（如 τ=0.8），τ sweep 已证明具体值不敏感。

---
