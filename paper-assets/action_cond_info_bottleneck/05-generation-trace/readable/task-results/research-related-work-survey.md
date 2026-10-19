# research related work survey

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related-work-survey_20260517T150220_result.json`
- **Structured JSON:** [`1b022bef8faf14982046.json`](../../sessions/1b/1b022bef8faf14982046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

YAML 验证通过。新增 4 个 section，共 16 篇论文：

| Section | 新增论文数 | 关键论文 |
|---------|-----------|---------|
| **ViT Token Pruning (Classic)** | 4 | ToMe, DynamicViT, EViT, A-ViT |
| **IB Theory (Foundational)** | 4 | Tishby 1999, Deep VIB 2017, Tishby & Zaslavsky 2015, Kawaguchi 2023 |
| **VLA Token Selection** | 5 | Compressor-VLA, VLA-ADP, VLA-Pruner, DeepVision-VLA, Task-Cond Adapt |
| **VLM Interpretability** | 3 | Grad-CAM, Attention Rollout, LVLM-Interpret |

重点发现：
- **VLA-ADP** (action-aware dynamic pruning) 和 **Compressor-VLA** (instruction-guided compression) 是新发现的直接竞争者，必须在 Related Work 中明确区分
- **DeepVision-VLA** (2026) 用 action-to-visual attention 做 pruning，思路最接近 ACIB，但它是 post-hoc 注意力 heuristic 而非 learned scorer + IB constraint
- IB 理论基础（Tishby 1999 + Deep VIB 2017）是 must-cite，为 ACIB 的 aggregate-rate KL 提供理论根基

---
