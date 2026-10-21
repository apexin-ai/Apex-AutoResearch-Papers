# research cogact connector

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cogact_connector_20260518T115150_result.json`
- **Structured JSON:** [`38e6e28d6a3d021c660c.json`](../../sessions/38/38e6e28d6a3d021c660c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是结论：

---

## 1. CogACT Vision Connector 类型

**2-layer MLP projector**（非 pixel-shuffle）。

架构细节：
- 基于 **Prismatic-7B VLM**
- 双 vision encoder：**DINOv2 + SigLIP**，输入分辨率 224×224
- 两个 encoder 的 feature map 在 channel 维度 concatenate，然后通过 2-layer MLP 投影到 LLM embedding space
- 产生 **256 visual tokens**
- Language backbone：LLaMA-2

## 2. EfficientVLA 在 CogACT 上的 Pruning 结果

**Pruning 对 CogACT 几乎无影响**：

| 配置 | 平均成功率 | FLOPs | 加速比 |
|---|---|---|---|
| Baseline（256 tokens） | 74.8% | 100% | 1.0× |
| Pruned（56 tokens, 22层） | 74.2% | 28.9% | 1.93× |

78% 的 token 被剪掉，成功率仅下降 0.6%。各任务明细：
- Pick Coke Can: 91.3% → 93.3%（反升）
- Move Near: 85.0% → 81.3%
- Open/Close Drawer: 71.8% → 68.2%
- Place Apple: 50.9% → 53.8%（反升）

注意：EfficientVLA **只测了 CogACT**，没有测 OpenVLA 等其他 VLA。

## 3. 对论文 Related Work 的影响

这个结果**不利于**简单的 "pruning 对 VLA 都失败" 的 claim，但**有力支持**一个更精准的叙事：

- **CogACT（MLP projector, 256 tokens）**→ pruning 几乎无损，graded degradation
- **OpenVLA（pixel-shuffle, 256 tokens 从 ~1024 压缩而来）**→ pruning 预期更有害

这恰好说明 **connector 类型决定了 token 的冗余结构**：
- MLP projector 产生的 token 之间信息高度冗余，pruning 容易找到低重要性 token
- Pixel-shuffle 保留了空间局部性，每个 token 承载不可替代的局部信息，pruning 更容易破坏关键信息

**建议论文 framing**：不要说 "VLA 的 vision tokens 不可压缩"，而是说 "pixel-shuffle connector 产生的 tokens 具有更高的 importance margin（每个 token 都重要），这使得 naive pruning 失效，但也意味着如果能识别 task-relevant spatial regions，compression 潜力更大。"

Sources:
- [CogACT Paper (arXiv HTML)](https://arxiv.org/html/2411.19650v1)
- [CogACT arXiv](https://arxiv.org/abs/2411.19650)
- [EfficientVLA Paper (arXiv HTML)](https://arxiv.org/html/2506.10100v1)
- [EfficientVLA OpenReview PDF](https://openreview.net/pdf?id=SELYlDHZk2)
- [CogACT GitHub Config](https://github.com/microsoft/CogACT/blob/main/conf/vla.py)
- [Prismatic VLMs GitHub](https://github.com/TRI-ML/prismatic-vlms)

---
