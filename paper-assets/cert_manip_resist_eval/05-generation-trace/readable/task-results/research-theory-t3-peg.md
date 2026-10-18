# research theory t3 peg

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_theory-t3-peg_20260521T194226_result.json`
- **Structured JSON:** [`783a775bc9f886442bee.json`](../../sessions/78/783a775bc9f886442bee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

T3 理论推导已完成，写入 `artifacts/theory/t3_peg_degradation.md`。

核心结果：

**Theorem 1 (激励锐度退化)**：
$$\varepsilon_{\text{inc}}(\rho) = 1 - \sqrt{1 - \rho^2}$$

**Theorem 2 (操作性退化)**：
$$\varepsilon_{\text{op}}(\rho, K) = 1 - \left(\frac{K_{\text{eff}}}{K}\right)^{\beta}$$

两者通过 $K_{\text{eff}} = 1 + (K-1)(1-\varepsilon_{\text{inc}})^2$ 连接。

关键发现：
- 退化以 $\rho^2/2$ 二次起步，小相关性仅造成轻微退化
- Cross-family panel ($\rho \approx 0.45$) 保留 ~93% 操纵抗性，within-family ($\rho \approx 0.75$) 仅保留 ~79%
- PEG 保持 ≥90% 激励锐度的充分条件：$\rho < 0.44$，恰好对应 cross-family 选择的经验范围

技术注意：DMI 的代数性质（$\det(\Pi M) = \det(\Pi)\det(M)$）使 truthful reporting 在面对 truthful 对手时始终弱占优，不依赖于 $\rho$。退化体现在激励优势的 *幅度* 缩减（使均衡对有限理性脆弱），以及评估质量因信息冗余而下降。文档中已明确标注 proof sketch 级别的假设和 caveat。

---
