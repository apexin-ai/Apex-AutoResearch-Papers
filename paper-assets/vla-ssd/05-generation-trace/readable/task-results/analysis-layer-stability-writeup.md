# analysis layer stability writeup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_layer-stability-writeup_20260515T160040_result.json`
- **Structured JSON:** [`21b2b14c1985a6df1f9a.json`](../../sessions/21/21b2b14c1985a6df1f9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出已注册为 `art_20260515_72a874`。

核心结论：

**Story 强度**：Layer stability 发现不足以支撑独立论文——单模型+单 benchmark，且缺乏因果证据。最佳定位是"What does VLA training learn?"分析型论文的核心 section，或 LIBERO-Goal 论文的辅助证据。

**最大风险**：当前对比是 random-init LLM vs trained VLA，审稿人会认为 trivially expected。**Priority 1 是加 Prismatic-7B（pre-trained VLM，未做 action FT）作为 baseline**——这能区分"VLM 预训练效果" vs "VLA fine-tuning 效果"。

**文献定位**：
- Layer-wise probing 方法论成熟（Tenney 2019 → Ling 2025），但无人以 probe *stability*（跨层方差）作为指标——这是我们的 gap
- Arefin et al. (ICLR 2025) Seq-VCR 最相关：中间层 representation collapse 限制推理能力，与我们的 untrained collapse 现象直接对应
- Kachaev et al. (2025) 报告 VLA fine-tuning *导致* representation collapse（与我们相反），他们的 collapse 是视觉 grounding 丢失，我们的是随机初始化层的非功能性

**可视化方案**：3 个图——(1) 三面板 layer-wise R²/ρ 曲线对比，(2) CoV 柱状图量化 stability，(3) Layer health heatmap 一览全局。数据 spec 和 matplotlib 参数已写入文档。

**Timeline**：14 天到 CoRL deadline。Priority 1 实验需 2 天，若 5/17 前完成可留 7 天写作。紧但可行。

---
