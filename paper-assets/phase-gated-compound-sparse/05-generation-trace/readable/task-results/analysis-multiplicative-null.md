# analysis multiplicative null

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiplicative-null_20260514T053548_result.json`
- **Structured JSON:** [`c9d14715ff6145dccbec.json`](../../sessions/c9/c9d14715ff6145dccbec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核心结论：

**Claim 完全 robust。** 所有 12 个 (sparsity × phase) 组合在两种 null model 下都为正，4 个 sparsity level 的 gradient 方向全部一致（low > high）。

关键数据：
- **Sign**: 全部 12/12 Both Positive
- **Gradient direction**: 4/4 match（additive gradient 24.75–401.98×, multiplicative 20.46–376.27×）
- **差异来源**: multiplicative residual = additive II − (R_h−1)(R_k−1)，correction 项在 high phase 很小（~0.03–0.37），low phase 较大（~2.2–193），但不改变定性结论
- **数学关系**: multiplicative null 更严格（要求更高），residual 系统性偏小，但 monotonic phase gradient 完全保持

---
