# research plan003 theorem1 proof

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan003-theorem1-proof_20260522T111238_result.json`
- **Structured JSON:** [`dc36935f1267845893e1.json`](../../sessions/dc/dc36935f1267845893e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存到 `artifacts/theorem1_proof.tex`，6 页，编译通过。

**证明结构总结**：

1. **Lemma 1 (K=3, 独立)**：显式计算 ASR = η₁η₂ + η₁η₃ + η₂η₃ − 2η₁η₂η₃，对 η_max 求导得 ∂ASR/∂η_max = η₁(1−η₂) + η₂(1−η₁) ≥ 0。

2. **Lemma 2 (一般 K, 独立)**：利用条件分解 ASR = P(Y≥t) + P(Y=t−1)·η_K，其中 Y 是其余 K−1 个 judge 的失败数。ASR 关于 η_K 是仿射函数，斜率 P(Y=t−1) ≥ 0（pivotal voter 概率）。

3. **Theorem 1 (一般 K, 相关+自适应对手)**：核心证明。对固定攻击 a，按 s = Σx_j 分三种情况：s≥t（两个 panel 都失败）、s=t−1（pivotal，由 pointwise dominance 保证）、s≤t−2（两个都不失败）。因此 ASR(P',a) ≥ ASR(P,a) 对所有 a 成立，取 sup 后 adaptive adversary 的结果跟着。

4. **Tightness**：等号条件是 pivotal 状态下两个 judge 的条件失败概率完全相等（非退化情况下单调性是严格的）。上下界：ASR = Θ(η_max^t)。

5. **Corollary**：robustness-first 两阶段设计——先筛 η_max ≤ τ，再最大化 K_eff。

---
