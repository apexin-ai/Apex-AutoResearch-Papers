# viz paperbanana fig1 overview

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_paperbanana_fig1_overview_20260524T061310_result.json`
- **Structured JSON:** [`defc14f39778cf82c843.json`](../../sessions/de/defc14f39778cf82c843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**最终图片路径：**
- PNG: `artifacts/figures/paper/fig_overview_pb.png` (4128×2304, 300 DPI)
- PDF: `artifacts/figures/paper/fig_overview_pb.pdf`

**迭代记录（3 轮）：**
- 第 1 轮：基础生成 → 三列布局正确，结构完整，配色和谐。"Δaction" 被渲染为 "Aaction"。分辨率 1376×768（偏低）
- 第 2 轮：强调分辨率和细节 → 布局退化为 2+1，分辨率未改善。退步
- 第 3 轮：极力强调水平三列 → 三列恢复但太扁（1936×544），文字过小。Critic API 崩溃

**最终选择 V1**（最佳平衡），LANCZOS 上采样 3× 到 4128×2304。

**质量评估：**
- 结构/信息完整度：8/10——三面板内容齐全，逻辑正确
- 配色：8/10——pastel 调性和谐
- 文字清晰度：5/10——AI 生图固有模糊，上采样无法恢复细节
- 印刷适配：5/10——缩小到 column width 后小字可能不够清晰

**未达到顶会级别。** 根本原因：PaperBanana 对 methodology 图使用 AI 图像生成（非 matplotlib 代码生成），文字渲染精度受限于生成模型能力。Critic 模块 JSON 解析持续失败，内部迭代优化未生效。建议回退到 matplotlib 手写实现以获得矢量级精度。

---
