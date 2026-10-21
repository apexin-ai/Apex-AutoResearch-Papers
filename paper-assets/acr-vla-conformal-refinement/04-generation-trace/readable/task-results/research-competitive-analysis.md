# research competitive analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_competitive-analysis_20260515T014521_result.json`
- **Structured JSON:** [`85a879b44aedf7f3b024.json`](../../sessions/85/85a879b44aedf7f3b024.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心发现：

**竞品覆盖**：8 篇竞品已分析（ACoT-VLA、ReconVLA、SC-VLA、VLA-Pilot、AsyncVLA、A2C2、PLD、SRPO）。paper_framing.md 和 literature_map.yaml 的覆盖率很好，主要缺失 **AsyncVLA** (arXiv:2511.14148)。

**关键数据点**：
- ACoT-VLA: LIBERO 98.5%, LIBERO-Plus 84.1% — CVPR 2026，confirmed SOTA
- ReconVLA: AAAI 2026 Outstanding Paper — 需在 paper_framing.md 中标注
- SC-VLA: ManiSkill +9% SR，但未在 LIBERO 评估
- 无竞品使用 per-DOF conformal statistics 作为 learned correction 输入

**建议行动**：
1. `literature_map.yaml` 新增 AsyncVLA 条目
2. paper_framing.md Gap 段补充 AsyncVLA 的 confidence-guided refinement 作为对比
3. ReconVLA 条目补充 AAAI 2026 Outstanding Paper 信息
4. 论文叙事策略：强调 relative improvement (+22.5pp) 和 stacking potential，而非与 7B+ backbone 方法做绝对数值竞争

Sources:
- [ACoT-VLA (CVPR 2026)](https://arxiv.org/abs/2601.11404)
- [SC-VLA](https://arxiv.org/abs/2602.21633)
- [VLA-Pilot](https://arxiv.org/abs/2511.14178)
- [AsyncVLA](https://arxiv.org/abs/2511.14148)
- [ReconVLA](https://arxiv.org/html/2604.16677v1)
- [A2C2](https://arxiv.org/abs/2509.23224)
- [PLD (ICLR 2026)](https://arxiv.org/abs/2511.00091)
- [SRPO](https://arxiv.org/abs/2511.15605)
- [Conformal Risk Control for HRI](https://arxiv.org/abs/2603.10392)
- [ICLR 2026 VLA landscape](https://mbreuss.github.io/blog_post_iclr_26_vla.html)

---
