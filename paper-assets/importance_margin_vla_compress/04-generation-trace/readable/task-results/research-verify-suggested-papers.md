# research verify suggested papers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_suggested_papers_20260519T013326_result.json`
- **Structured JSON:** [`a626dcb28b8314efa671.json`](../../sessions/a6/a626dcb28b8314efa671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 论文 5: "Don't Run with Scissors"
- **状态**: ✅ 确认存在
- **arXiv ID**: 2510.08464
- **真实标题**: Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered
- **作者**: Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar et al.
- **Venue/日期**: arXiv 2025-10-09
- **核心方法**: 发现剪枝会导致 VLA 模型性能剧烈退化并增加安全违规。提出 GLUESTICK，一种无需额外训练的后剪枝恢复方法，通过在 dense 和 pruned 模型权重空间做一次性插值计算校正项，推理时恢复丢失能力。
- **与我们的关系**: 直接相关。他们研究 VLA 的 weight pruning fragility，我们研究 token compression；两者都是 VLA 效率化但切入角度不同（权重 vs token）。
- **Reviewer 描述准确性**: 准确

## 论文 6: SparseVLM
- **状态**: ✅ 确认存在
- **arXiv ID**: 2410.04417
- **真实标题**: SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference
- **作者**: Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng et al.
- **Venue/日期**: **ICML 2025**（已确认接收），arXiv 2024-10-06
- **核心方法**: Training-free 的视觉 token 稀疏化方法。利用 text token 的 self-attention 矩阵评估视觉 token 重要性，逐层自适应确定稀疏比例，并通过 token recycling 压缩被剪枝的 token。LLaVA 上实现 54% FLOPs 减少。
- **与我们的关系**: 直接竞争/高度相关。同为 visual token sparsification，但他们针对 VLM（理解任务），我们针对 VLA（动作生成任务），场景需求不同。
- **Reviewer 描述准确性**: 准确（包括 ICML 2025 venue）

## 论文 7: SparseVILA
- **状态**: ✅ 确认存在
- **arXiv ID**: 2510.17777
- **真实标题**: SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference
- **作者**: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Song Han, Zhijian Liu et al.
- **Venue/日期**: **ICCV 2025**（已确认接收，Poster on Oct 23, 2025），arXiv 2025-10-20
- **核心方法**: 解耦 prefilling 和 decoding 阶段的视觉稀疏策略。Prefill 阶段剪枝冗余视觉 token（query-agnostic），decoding 阶段仅检索 query-relevant token（query-aware）。实现 4.0x prefill 加速、2.5x decoding 加速。
- **与我们的关系**: 直接相关。同为 visual token 效率化，他们的 prefill/decode 解耦思路与我们的 importance margin 方法互补或可对比。Song Han 组出品。
- **Reviewer 描述准确性**: 准确（包括 ICCV 2025 venue 和 decoupled visual sparsity 描述）

## 论文 8: RoboFlamingo
- **状态**: ✅ 确认存在
- **arXiv ID**: 2311.01378
- **真实标题**: Vision-Language Foundation Models as Effective Robot Imitators
- **作者**: Xinghang Li, Minghuan Liu, Hanbo Zhang et al. (ByteDance Research)
- **Venue/日期**: **ICLR 2024**，arXiv 2023-11-02
- **核心方法**: 基于 OpenFlamingo 构建机器人操作框架。继承 Flamingo 的 gated cross-attention 架构（frozen CLIP ViT 编码视觉 token，语言模型通过 cross-attention 层 attend 视觉特征），加上轻量 MLP action head，仅在操作数据集上 imitation learning 微调。CALVIN benchmark SOTA（4.2/5 tasks）。
- **与我们的关系**: 间接相关。它是 cross-attention connector 的 VLA 代表（vs 主流 projection-based VLA 如 OpenVLA），可作为不同 vision connector 架构下 token compression 效果对比的参考。
- **Reviewer 描述准确性**: 准确。cross-attention vision connector 是从 Flamingo 继承的架构特征，VLA 定位准确。

---

**总结**: 4 篇论文全部真实存在，Reviewer 的描述（包括 arXiv ID、venue、核心方法）均准确，无幻觉。

Sources:
- [Don't Run with Scissors](https://arxiv.org/abs/2510.08464)
- [SparseVLM](https://arxiv.org/abs/2410.04417)
- [SparseVILA](https://arxiv.org/abs/2510.17777)
- [SparseVILA ICCV 2025 Poster](https://iccv.thecvf.com/virtual/2025/poster/1739)
- [RoboFlamingo](https://arxiv.org/abs/2311.01378)
- [RoboFlamingo OpenReview (ICLR 2024)](https://openreview.net/forum?id=lFYj0oibGR)

---
