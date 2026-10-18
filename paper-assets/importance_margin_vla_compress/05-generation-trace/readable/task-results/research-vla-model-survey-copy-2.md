# research vla model survey

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vla_model_survey_20260519T161749_result.json`
- **Structured JSON:** [`9205259be563cc6c00f4.json`](../../sessions/92/9205259be563cc6c00f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在可用 MCP 工具列表中。报告已写入 `artifacts/vla_model_survey.md`。

## 调研结论

**第三种 connector 架构首选：RoboFlamingo（Perceiver Resampler + Gated Cross-Attention）**

三种 connector 形成清晰的分类体系：

| Connector 类型 | 代表模型 | 压缩哲学 | Pruning 行为 |
|---|---|---|---|
| Pixel-shuffle + MLP | SmolVLA | 空间→通道折叠 | Cliff-edge |
| MLP Projection | OpenVLA | 线性映射，保留冗余 | Graded degradation |
| **Perceiver Resampler** | **RoboFlamingo** | **注意力选择性压缩** | **待验证（新发现）** |

RoboFlamingo 的核心优势：
- Perceiver Resampler 本身就是 learned token compression（N → K via cross-attention），与 MLP 和 pixel-shuffle 本质不同
- 开源代码 + 3B/9B 两种尺寸，GPU 需求合理
- 适配 LIBERO 需要写 dataloader + eval wrapper，但难度可控（2.5/5）
- 科学问题明确：已经过注意力压缩的 tokens 再做 pruning 会出现什么 degradation pattern？

**CogACT 状况**：有公开权重（MIT License），但 connector 和 OpenVLA 完全相同（Prismatic backbone），且无原生 LIBERO 支持。对 connector 研究无增量价值。

**π0/OpenPi** 可作为补充验证（同类 connector + 不同 backbone），且 LIBERO 开箱即用。

---
