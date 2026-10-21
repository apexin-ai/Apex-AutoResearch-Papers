# analysis negative results systematic

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_negative_results_systematic_20260524T220731_result.json`
- **Structured JSON:** [`452fc3a4d85be06f4396.json`](../../sessions/45/452fc3a4d85be06f4396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册：`art_20260524_5ecde0`

**核心结论**：16 个阴性实验统一指向一个根本问题——**flow-matching VLA 的 action space 不接受 gradient-based correction**。无论 A1（训练时 SDF loss）还是 A3（推理时 gradient refinement），所有 SDF-gradient-to-action 路径都导致 action collapse（96.7-99.6% fake safety）。即使 GT oracle 最优条件，real safety improvement = 0。

**归因分布**：
- 结构性限制（7个）：action collapse + EE-only 限制
- 实现 bug（5个）：M024/M026/M027，但修复后仍不 work
- 基座特性（4个）：Pi0 collapse 倾向 + capability-safety tradeoff

**建议 pivot**：从 post-hoc action correction 转向 pre-generation conditioning 或 safe rejection sampling。

---
