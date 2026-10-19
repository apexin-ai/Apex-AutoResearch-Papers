# paper fig1 teaser design

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig1_teaser_design_20260527T015636_result.json`
- **Structured JSON:** [`bc57a8a1fbeef949acd1.json`](../../sessions/bc/bc57a8a1fbeef949acd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已产出并注册：`artifacts/fig1_teaser_design.md`

核心设计决策：

1. **Panel A/C 从 bar chart → robot arm schematic**：frozen arm（虚线/灰色/静止）vs active arm（实线/蓝色/弧形轨迹），底部保留 displacement bar 作为定量锚点
2. **Panel B 从 lollipop → filtering flow diagram**：垂直 flow 展示 τ_d 如何将 Pi0+A1 的 91.5% 筛到 ≈0%，Pi0.5 不受影响
3. **A/C 对称设计**：虚线 vs 实线、灰色 vs 蓝色、静止 vs 运动、空 bar vs 满 bar，每个维度都在强化 frozen vs genuine 的对比
4. **Caption 改进**：末尾加入论文核心口号 *"The robot is frozen, not safe."* 作为 punch line

实现建议 matplotlib schematic（与现有 pipeline 一致），降级方案也已包含。等 Director 审核后再执行渲染。

---
