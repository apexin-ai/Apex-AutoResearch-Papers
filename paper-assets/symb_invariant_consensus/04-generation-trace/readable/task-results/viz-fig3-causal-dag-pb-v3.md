# viz fig3 causal dag pb v3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig3-causal-dag-pb-v3_20260524T101440_result.json`
- **Structured JSON:** [`91f6c851690c4ef562c2.json`](../../sessions/91/91f6c851690c4ef562c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**输出文件**：
- PNG: `docs/paper/figures/fig3_causal_dag_pb_v3.png`
- PDF: `docs/paper/figures/fig3_causal_dag_pb_v3.pdf`

**迭代过程**（3 轮外部迭代）：
1. PaperBanana 首次生成 → 3D 效果强，但背景有灰色渐变
2. PaperBanana 重试 × 2 → Gemini critic 返回 None 崩溃（API 不稳定）
3. 对 round 1 结果做精细化后处理：仅修白低饱和度高亮度的背景像素，保留节点阴影和渐变

**立体感评估**：所有 6 项检查通过——阴影清晰、渐变明显、卡片浮起感、Y 节点最突出、A→C 红箭头是视觉焦点、注释框有深度。

---
