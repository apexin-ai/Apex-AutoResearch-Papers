# writing related work revision

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related_work_revision_20260513T180340_result.json`
- **Structured JSON:** [`4bf6e93aa1eede8c9168.json`](../../sessions/4b/4bf6e93aa1eede8c9168.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件格式正确，四项修正结果：

**修正 1：补回 4 篇论文** ✅
- HWM — 插入 THICK 之后，描述 multi-scale latent world models + fixed two-level planner 局限
- DyMoDreamer — 插入 ASI 之后，描述 inter-frame differencing masks + per-step quality（非 temporal resolution）
- DMWM — 紧随 DyMoDreamer，描述 dual-mind RSSM + logic-informed reasoning
- ELVIS — 插入 paragraph 3（Event-based），描述 uncertainty-aware λ-return gating，对比"trust weighting vs temporal resolution"

**修正 2：LS-Imagine 描述统一** ✅
- 改为 "goal-conditioned jumpy state transitions, learning jump flags via affordance-map kurtosis"
- 保留 "jump decisions are action-independent" 补充说明

**修正 3：computation claim 措辞** ✅
- `"without additional latent computation"` → `"with the same number of latent dynamics steps"`

**修正 4：ASI 描述验证** ✅
- 读了 Neitz et al. NeurIPS 2018 原文（Algorithm 1, Section 3）：temporal matching supervisor 用 `argmin_{t'} L(x_u, x_{t'})` 选择 window 内 loss 最小的 ground-truth frame。"min-pooling over losses" 是准确的简述
- 唯一修正：`"reconstruction losses"` → `"prediction losses"`（原文用 "prediction loss L_x"，不涉及 decoder reconstruction）
- "optimizing for prediction ease rather than dynamical significance" 与原文一致

---
