# writing related work section

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related_work_section_20260513T175837_result.json`
- **Structured JSON:** [`b1c3043d6eaf244d921c.json`](../../sessions/b1/b1c3043d6eaf244d921c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `related_work_section.md`，651 词，四个类别：

1. **Fixed-horizon MBRL** — MBPO, DreamerV3, NE-Dreamer, R2-Dreamer；指出固定步长的 credit assignment 瓶颈
2. **Variable-rate / temporal abstraction in MBRL** — TAWM, THICK, LS-Imagine, I-TAP, ASI；总结各自机制与局限（外部指定 Δt / 固定两层 / 仅探索 / 离线 / 预测易度驱动）
3. **Event-based / adaptive stepping in RL** — Options, FiGAR, TempoRL；强调这些是 model-free 的时间抽象，不扩展 imagination horizon
4. **本工作定位** — 明确三个差异：vs THICK/LS-Imagine（gate 选择 Δt∈{1,...,K} 而非 early-termination/binary jump）、vs FiGAR/TempoRL（在 imagination 中而非 execution 中）、vs TAWM（learned 而非 externally specified）；单模型架构避免 hierarchical exploitation 问题

---
