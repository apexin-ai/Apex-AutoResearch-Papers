# viz hybrid fig1 vA dense

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_hybrid_fig1_vA_dense_20260524T075338_result.json`
- **Structured JSON:** [`e571b10d5420f1bb9c73.json`](../../sessions/e5/e571b10d5420f1bb9c73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**流程变更**：`poll_secret_request` 返回 request not found，无法获取 Gemini API key。改为直接手写 matplotlib 代码（跳过 VLM 生成+迭代循环）。

**迭代记录**（共 4 轮渲染）：
1. 初版：基本布局正确，Panel (a) "attends to all context" 被裁切，Method 3 heatmap 与结果行重叠
2. 调整 Panel (a) 弧形箭头位置、heatmap 上移
3. 微调 heatmap 与结果行间距
4. 最终版：heatmap 底部 "ro" 标签可见性修复

**最终视觉质量**：7.5/10 — 布局清晰、色彩协调、文字可读，三个面板信息密度适中。数值标注（ΔR²、Cohen's d、head counts）完整。

**VLM critique**：未执行（无 API key）。

**残留问题**：
- Panel (a) "attends to all context" 竖排文字偏小（受面板宽度限制）
- Heatmap 是示意数据，非真实数据
- 如需 PDF 矢量输出，改 `savefig` 后缀即可

**Artifact**：`art_20260524_eea8e7`，代码保存在 `artifacts/figures/paper/fig_overview_hybrid_vA.py`

---
