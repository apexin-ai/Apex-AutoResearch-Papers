# analysis m1 gemini leverage

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m1_gemini_leverage_20260522T091146_result.json`
- **Structured JSON:** [`6194d71725841b0830e4.json`](../../sessions/61/6194d71725841b0830e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**count_8 (n=50)** — 完全稳健。去掉 2 个 leverage points 后 r 从 -0.887 **增强**到 -0.913（p=1.7e-19）。两个 leverage points 都是 accuracy 异常值，不是 BCS 异常值。

**count_16 (n=10)** — 确认单点驱动。high_4 (BCS=0.97) 在 BCS 维度上是 11.2σ 离群点，h_ii=0.93 占据 93% 的 x-leverage。移除后 r 降至 -0.42 (n.s.)。其余 9 个 batch 的 BCS 范围仅 [0.50, 0.62]，不足以检测相关性。

**对论文的影响**：cross-model generalization claim 稳健。论文对 count_16 的披露（Appendix T）已经充分，count_8 作为主要 Gemini Dim2 证据无需额外 caveat。

---
