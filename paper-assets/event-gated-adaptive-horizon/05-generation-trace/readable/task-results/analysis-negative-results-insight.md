# analysis negative results insight

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_negative-results-insight_20260524T183247_result.json`
- **Structured JSON:** [`3cb3cfe3454baa9cb8fe.json`](../../sessions/3c/3cb3cfe3454baa9cb8fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/negative_results_insights.md` 并注册。核心结论：

**7 个高 insight negative results** 构成论文两大 positive contribution：

1. **Intervention Hierarchy**（SGS/RAVE/TCN/dual-critic 系统性失败）— 证明 CIVO 在所有三个干预层级（gradient/output/representation）都难以可靠缓解，揭示根因是 forward-pass representational entanglement 而非 gradient 或 value magnitude 问题

2. **Multi-Pathway Vulnerability**（exp_008e_v3_s2 + exp_038）— trained dt_emb 通过至少两条路径创造脆弱性（CIVO = value-driven + IRD = eval-driven），消除一条不能保障安全

最有力的单点发现：
- **exp_016e**: 梯度量级 ≠ 因果重要性（reward head 49% 梯度但因果无关）
- **exp_030c**: Cheetah "impossible dose"（CIVO prevention threshold > noise tolerance threshold）
- **exp_034**: v1≈v2（pure-imagination MBRL 中 pessimism 机制失效，ρ>0.999）
- **exp_026**: 补偿放大（阻断一条通路导致 2.6-3.6× 恶化）

这些 negative results 不是 limitation，而是 diagnostic paper 的 primary contribution——系统性证明问题有多难解决。

---
