# research libero goal feasibility

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_libero-goal-feasibility_20260515T160020_result.json`
- **Structured JSON:** [`899fa0a0c7d738163062.json`](../../sessions/89/899fa0a0c7d738163062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已更新并注册。核心发现总结：

**Grant et al. 2026 精读结果**:
- LIBERO-Goal 10 tasks 共享同一 kitchen scene，仅 goal 不同
- OFT/X-VLA/GR00T 在 wrong prompt 下 collapse 到 0-10%（LIBERO-Object 不受影响）
- **关键 paradox**: π0.5 Layer 17 上 99.3% prompt classification accuracy，但行为不受 prompt 影响 → "encoded but not used"

**Novelty gap 明确**:
- Grant: behavioral intervention (6 models)，**没有 trained vs untrained 对比**
- Swann/Buurmeijer: SAE interpretability，**没有 language features 分析**
- LIBERO-CF: counterfactual behavioral benchmark，**没有 representation analysis**
- 我们的空间: **trained vs untrained × layer × timestep granularity 的 instruction probing** — 无人做过

**建议 Conditional GO**:
1. 先过 t=0 visual similarity gate（DINO cosine sim ≥ 0.95）
2. 方案 B（8 关键层）~6h 端到端
3. 与 temporal distance + action probe 组成 "when does VLA training matter?" 的三段式 story

---
