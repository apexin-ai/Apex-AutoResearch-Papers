# research verify must have papers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_must_have_papers_20260519T013320_result.json`
- **Structured JSON:** [`abbd984d4f57e6def0ea.json`](../../sessions/ab/abbd984d4f57e6def0ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 篇论文验证完毕。

---

## 论文 1: Compressor-VLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2511.18950](https://arxiv.org/abs/2511.18950)
- **真实标题**: Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation
- **作者**: Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian (北京工业大学 & LiAuto)
- **Venue/日期**: arXiv 2025-11-24 (无会议录用信息)
- **核心方法**: 提出 Semantic Task Compressor (STC) + Spatial Refinement Compressor (SRC) 双模块框架，由自然语言指令动态调制 visual token 压缩。在 LIBERO 上实现 59% FLOPs 削减、3x+ token 数量压缩，同时保持 competitive success rate。
- **与我们的关系**: 直接竞争 (instruction-guided VLA token compression on LIBERO)
- **Reviewer 描述准确性**: 部分准确。cross-attention 描述大致对应其 STC 模块机制，但 97.1% SR 在 abstract 中未明确提及（仅称 "competitive"），需查论文表格确认。

---

## 论文 2: SpecPrune-VLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2509.05614](https://arxiv.org/abs/2509.05614)
- **真实标题**: SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning
- **作者**: Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai
- **Venue/日期**: arXiv 2025-09-06 (revised 2026-02-09)；submitted to ICLR 2026 ([OpenReview](https://openreview.net/forum?id=t85Ni0LwjC))，录用状态未确认
- **核心方法**: Training-free 两级剪枝：action-level static pruning (全局历史+局部 attention) + layer-level dynamic pruning (逐层重要性)。Lightweight action-aware controller 根据末端执行器速度区分粗/细粒度动作，细粒度动作降低剪枝力度。LIBERO 上 1.57x 加速，real robot 1.70x 加速，success rate 几乎无损。
- **与我们的关系**: 直接竞争 (action-aware VLA token pruning, LIBERO + real robot)
- **Reviewer 描述准确性**: 准确

---

## 论文 3: LightVLA
- **状态**: ✅ 确认存在
- **arXiv ID**: [2509.12594](https://arxiv.org/abs/2509.12594)
- **真实标题**: The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning
- **作者**: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang (LiAuto)
- **Venue/日期**: arXiv 2025-09-16；**ICRA 2026 accepted**（[GitHub](https://github.com/LiAutoAD/LightVLA) 确认）
- **核心方法**: 可微分 token 剪枝框架，用动态 query 评估 visual token 重要性，Gumbel softmax 实现可微分 token 选择。无额外可训练参数，兼容现代推理框架。LIBERO 上 59.1% FLOPs 削减、38.2% latency 削减，success rate 提升 2.6%。
- **与我们的关系**: 直接竞争 (differentiable VLA token pruning on LIBERO)
- **Reviewer 描述准确性**: 准确（arXiv ID、ICRA 2026、differentiable pruning 均吻合）

---

## 论文 4: "See What Matters"
- **状态**: ✅ 确认存在
- **arXiv ID**: 未找到 arXiv 预印本（可能仅通过会议提交）
- **真实标题**: See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model
- **作者**: Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, Chang Xu
- **Venue/日期**: **[ICML 2026 poster](https://icml.cc/virtual/2026/poster/65010)**
- **核心方法**: 提出 Differentiable Grid Sampler (GridS)，一个即插即用模块，将 token pruning 重新定义为连续 geometry-aware resampling 问题。自适应预测少量关键坐标，通过可微分插值提取特征，仅使用 <10% 的原始 visual tokens 即可实现 76% FLOPs 削减且 success rate 无损。号称目前报告的最低可行 visual token 数量。
- **与我们的关系**: 直接竞争 (grid-based VLA token compression on LIBERO + real robot)
- **Reviewer 描述准确性**: 准确（ICML 2026、grid-based compression 均吻合）

---

## 总结

| 论文 | 存在性 | Reviewer 描述 | arXiv ID |
|------|--------|--------------|----------|
| Compressor-VLA | ✅ 真实 | 部分准确 (97.1% SR 待确认) | 2511.18950 ✅ |
| SpecPrune-VLA | ✅ 真实 | 准确 | 2509.05614 ✅ |
| LightVLA | ✅ 真实 | 准确 | 2509.12594 ✅ |
| See What Matters | ✅ 真实 | 准确 | 无 arXiv (ICML 2026 直接提交) |

**4 篇论文全部真实存在，reviewer 未出现幻觉。** 这 4 篇都是 VLA visual token compression/pruning 的直接竞争工作，均在 LIBERO 上评测。

---
