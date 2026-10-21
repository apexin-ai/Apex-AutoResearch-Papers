# analysis d34 cascade ordering theory

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d34_cascade_ordering_theory_20260520T184858_result.json`
- **Structured JSON:** [`c02c4f04e7ae1bd785ee.json`](../../sessions/c0/c02c4f04e7ae1bd785ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出写入 `artifacts/theory/cascade_ordering_derivation.md`。

核心结果：

1. **Part 1 (Entropy → Diversity)**: 在 mode amplification 假设下严格证明——entropy 对分布扰动是一阶敏感的（任何概率质量重分配都改变 entropy），diversity 是阈值型指标（需要 token 概率跌破生成阈值 $\epsilon$）。Theorem 1 证明 $|\Delta H| > 0$ 时 $\Delta S_\epsilon = 0$ 可行，反之不可行。

2. **Part 2 (ECE ↔ Entropy)**: 通过 Rényi 熵不等式 $\max q_i \geq e^{-H(q)}$ 和 Jensen 不等式建立 confidence-entropy 的函数耦合。在 accuracy stationarity 假设下，$\Delta\text{ECE} \geq e^{-H_t} \cdot |\Delta H_t|$——两者同时响应，零 lag。

3. **Part 3 (Timing bounds)**: 当单代扰动幅度 $\alpha \|\mathcal{T}(p)-p\|_\infty$ 小于 margin $\gamma(p, \epsilon)$ 时，diversity onset 滞后 entropy onset $\geq 1$ 代。MAUVE 进一步滞后是 heuristic argument（标注为 conjecture）。

与实测数据完全一致：4 个 $\alpha \geq 0.50$ 实验中，entropy/ECE 均在 gen 1 onset，distinct-n 均在 gen 2，lag = 1。

---
