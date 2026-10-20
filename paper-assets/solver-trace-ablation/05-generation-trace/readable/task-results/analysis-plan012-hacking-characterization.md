# analysis plan012 hacking characterization

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan012-hacking-characterization_20260514T050649_result.json`
- **Structured JSON:** [`3dacb26f753cb20ef326.json`](../../sessions/3d/3dacb26f753cb20ef326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册为 `art_20260514_faed3a`。

核心发现：

1. **Exec-only (s42)**: 87% proved samples 含 conclusion-in-premises hack，48% ISR=0。模型把结论塞进前提里确保 Prover9 通过，再用上下文前提填充。PR=93% 看似优秀，ISR=0.13 暴露了问题。

2. **Random reward**: 100% 纯 tautology（P ⊢ P），96% 恰好 2 个 components。ISR=0.5 是因为唯一前提确实"必要"——但语义上完全空洞。

3. **Additive β=0.3**: 79/82 失败样本连 `Conclusion` 标记都没生成（format collapse）。直接优化 ISR 摧毁了格式能力。

4. **ISR 单独用不够**：random reward 的 ISR (0.54) 接近 GT (0.56)，需要联合 component count 才能区分 lean tautology 和 genuine proof。这支持论文用 (ISR, n_components) 联合诊断的设计。

---
