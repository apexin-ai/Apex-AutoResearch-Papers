# paper introduction draft

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_introduction-draft_20260516T200221_result.json`
- **Structured JSON:** [`82fc31ede95f27317320.json`](../../sessions/82/82fc31ede95f27317320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿已写入 `artifacts/paper_drafts/introduction_draft.md`。

结构概要：

- **Para 1**: 从temporal abstraction在MBRL中的吸引力切入，引TAWM在MPC中的成功作为正面预期
- **Para 2**: 转折——同样的dt-conditioning在imagination-based actor-critic中变成pathological feedback loop，引入CIVO术语
- **Para 3**: 贡献概述——factorial design、NVE诊断指标（>1.5x perfect separation）、梯度分解（obs decoder 93%）、Full-SGS proof-of-concept
- **Contributions 1-4**: (1) phenomenon identification + paradigm asymmetry, (2) causal diagnosis via ablations, (3) mechanistic explanation via gradient decomposition, (4) Full-SGS + Pathway B residual risk
- **Closing**: practical implication（field must address CIVO before building variable-dt agents）+ paper outline

几个写作决策：
- TAWM对比放在第一段而非contribution list，建立"MPC成功 vs imagination失败"的paradigm asymmetry作为核心tension
- Contribution 4明确标注Full-SGS为"proof-of-concept"而非mature solution，预防R2
- 末段指向hierarchical approaches作为更promising的方向，避免over-claiming
- 未使用"significantly"或"consistently"，所有数值claims可追溯到具体实验

---
