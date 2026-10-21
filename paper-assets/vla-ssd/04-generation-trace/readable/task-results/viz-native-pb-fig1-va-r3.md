# viz native pb fig1 vA r3

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_native_pb_fig1_vA_r3_20260524T081823_result.json`
- **Structured JSON:** [`fb47dec3b7ec270f7251.json`](../../sessions/fb/fb47dec3b7ec270f7251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 结果 |
|------|------|
| **质量评分** | **6.5/10** |
| **迭代次数** | 1（critic 自动通过） |
| **模型** | VLM: gemini-2.5-pro / Image: gemini-3-pro-image-preview |
| **文字可读性** | 中等偏低 — 正文 ~8pt，数值标注可辨认但在印刷尺寸下偏小 |
| **内容准确性** | 三个 panel 标题、内容、数值标注全部正确 |

**主要问题：**
- 文字整体偏小，print-size 下可读性受限（figsize 被图像生成模型压缩）
- Panel (c) 分类框缺少指定的彩色左边框样式
- 配色接近但未严格匹配指定的 hex 色板
- 第一次用 gemini-2.5-pro 时 stylist 返回空响应（已 patch `response.text` None 处理），切 flash 生成的 v1 内容严重错误，回到 pro 后 v2 正确

**产出路径：** `projects/vla-ssd/artifacts/figures/paper/fig_overview_vA.png`（已注册 `art_20260524_9f7624`）

---
