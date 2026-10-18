# research xvla setup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_xvla-setup_20260520T033718_result.json`
- **Structured JSON:** [`bc63f569fc00ac361cb4.json`](../../sessions/bc/bc63f569fc00ac361cb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 memory.md。总结如下：

## X-VLA 调研结论

**模型确认**: X-VLA（[2toinf/X-VLA](https://github.com/2toinf/X-VLA)），0.9B 参数，ICLR 2026，LIBERO 98.1% SR。

**架构**:
- Vision encoder: Florence-Large (DaViT)
- Connector: **Linear projection** (dim 2048→1024) + LayerNorm
- Backbone: 24-layer Transformer (hidden=1024, 16 heads)
- Action: Flow matching, 30 anchor points × 20 dims (EE6D)
- 特色: 每个 embodiment 有 32 个 learnable soft prompts

**Vision Token 数量**: DaViT total stride=32，224×224 输入下 7×7=49 tokens。但 Florence-2-Large 默认分辨率是 768×768 (24×24=576 tokens)，**需要加载模型后验证 X-VLA 实际使用的分辨率**。

**VTC 集成方案**: 插入在 Florence2 `_encode_image()` 输出和 `_merge_input_ids_with_image_features()` 之间，复用 VisionTokenCompressor（hidden_dim 改 1024）。需适配 flow matching loss。

**权重**: 使用 `2toINF/X-VLA-Libero` 作为起点（已在 LIBERO 上 fine-tune 到 98.1%）。

**预计工作量**: 8-12 小时（adapter 代码 4-6h + 环境 2-3h + 调试 2-3h）。

**与 OpenVLA 对比的关键点**: X-VLA 的 linear projection 不引入非线性变换，vision token 经过的变换远少于 OpenVLA 的 2-layer MLP。预期压缩行为与 MLP connector 存在质性差异——这正是论文需要的 "最简 connector" 数据点。

Sources:
- [X-VLA GitHub](https://github.com/2toinf/X-VLA)
- [X-VLA Paper (arXiv:2510.10274)](https://arxiv.org/abs/2510.10274)
- [X-VLA-Libero on HuggingFace](https://huggingface.co/2toINF/X-VLA-Libero)
- [X-VLA HuggingFace Collection](https://huggingface.co/collections/2toINF/x-vla)
- [Florence-2-Large Config](https://huggingface.co/microsoft/Florence-2-large)

---
