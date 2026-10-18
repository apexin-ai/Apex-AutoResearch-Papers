# research theory t1 sdpi

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_theory-t1-sdpi_20260521T194207_result.json`
- **Structured JSON:** [`df7f5a6bc748f0be545f.json`](../../sessions/df/df7f5a6bc748f0be545f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入。核心内容：

- **Serial vs Parallel 区分**：串联 $\eta^K$ 指数衰减 vs 并联 $K_{\text{eff}} \cdot \eta_{\max}$ 线性增长
- **Lemma 1**：并联通道联合 KL 散度上界 $D_{KL}(W^{(K)}Q \| W^{(K)}P) \leq K_{\text{eff}} \cdot \eta_{\max} \cdot \Delta$
- **Proof Sketch**：通过 KL 链式法则分解 → 条件增量递减 → Gaussian compound symmetric 模型精确推导 → Sherman-Morrison 求逆 → 证明 $K_{\text{eff}} = 1+(K-1)e^{-2I_{\max}}$ 是精确值的上界（$(K-1)^2 a(1-a) \geq 0$）
- **K_eff 推导**：Gaussian 精确值为 $K/(1+(K-1)(1-e^{-2I_{\max}}))$，提出公式是其上界，在边界 $I_{\max}=0$ 和 $I_{\max}\to\infty$ 处 tight
- **操纵抗性连接**：Pinsker 不等式 + Hoeffding 集中度 → 攻击者每 judge 的精度偏移固定（$\sqrt{\eta_{\max}\Delta/2}$），但翻转多数票的概率随 $K_{\text{eff}}$ 指数衰减 → defense gap

---
