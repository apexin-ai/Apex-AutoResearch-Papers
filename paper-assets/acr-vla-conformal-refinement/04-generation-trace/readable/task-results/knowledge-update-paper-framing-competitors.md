# knowledge update paper framing competitors

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_update-paper-framing-competitors_20260514T074639_result.json`
- **Structured JSON:** [`964b8b135059a69fffb3.json`](../../sessions/96/964b8b135059a69fffb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

更新完成。主要变更：

1. **Story Spine → Gap**：从原来仅提 ReconVLA/CP-in-the-Loop/UPS/A2C2 扩展为包含四个主要竞品（ReconVLA scalar CQR + selection only、SC-VLA residual RL 无统计保证、VLA-Pilot 2.41s 延迟启发式评分、ACoT-VLA 84.1% 但 training-time 静态模型），以"所有方法均未将 per-DOF conformal statistics 作为 learned correction 输入"收束。

2. **新增 Competitive Landscape section**：四个竞品逐一分析关键差异，末尾明确 ACR-VLA 差异化定位——唯一同时具备 per-DOF statistical guarantees + learned dimension-selective correction + online coverage adaptation 的方法。

Core Claims、Kill Criteria、Target Venue、Framing 备选策略均未修改。

---
