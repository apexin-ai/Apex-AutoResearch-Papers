# research papadatos freedman 2024

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_papadatos-freedman-2024_20260522T102156_result.json`
- **Structured JSON:** [`00b3895fc8783114cb3c.json`](../../sessions/00/00b3895fc8783114cb3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是三个技术问题的回答：

---

**Q1 (per-token vs per-completion): 取决于任务类型，两种都有。**

- Multiple-choice 任务：per-token — probe 输入是 LLM 单个 token 回答对应的 activations（"the probe's input is the activations corresponding to the LLM's single-token multiple choice response"）
- Open-ended 任务：per-completion（mean pooling）— probe 输入是所有 response token activations 的平均值（"the probe's input is the average of the activations across all tokens of the LLM's response"）

Probe 本身是一个带 sigmoid 的全连接层，作用在 **reward model 第 16 层**的 hidden states 上，输出标量 sycophancy score。

---

**Q2 (RM vs RL stage): 都不是 — 是在 inference-time 的 Best-of-N sampling 阶段。**

Probe penalty 既不修改 RM 训练，也不进入 PPO/DPO 的 RL 训练。它构造一个 surrogate reward function：

$$\hat{\mathcal{R}}(t) = \mathcal{R}(t) - \lambda \cdot \mathcal{S}(t)$$

其中 $\mathcal{R}(t)$ 是原始 RM 分数，$\mathcal{S}(t)$ 是 probe 输出的 sycophancy score。这个修改后的 reward 仅用于 BoN reranking（N∈[1,32]）。

论文明确说："This paper focuses on feedback sycophancy due to its demonstrated increase under BoN sampling, which provides a more tractable experimental setup compared to the complexities of reinforcement learning algorithms."

---

**Q3 (probe target): 检测 sycophancy（谄媚行为），二分类。**

Probe 训练数据来自 4 个数据集，统一标签为 sycophantic vs non-sycophantic：
1. **Subjective MCQ** — 同意用户观点=sycophantic，不同意=non-sycophantic
2. **Objective MCQ** — 用户和 assistant 都错=sycophantic
3. **Open-ended** — GPT-4 生成配对的 sycophantic/non-sycophantic 回复（53 个问题）
4. **Feedback (poems)** — 用户表达偏好后，迎合=sycophantic，中立=non-sycophantic

Probe 在第 16 层达到 94% 测试准确率。

---

**与我们工作的关键区别/相似点：**

| 维度 | Papadatos & Freedman | 我们的方向 (contrastive entrain calib) |
|------|---------------------|--------------------------------------|
| 作用阶段 | Inference-time BoN reranking | （如果是训练阶段介入则不同） |
| Probe 位置 | Reward model 内部 hidden states | — |
| 方法本质 | 从 RM 中线性分离 sycophancy signal，构造 surrogate reward | Contrastive 方法 |
| 局限 | 只验证了 BoN，未进入 RL 训练循环；只处理 sycophancy 一种行为 | — |
| 可借鉴 | 用 linear probe 检测 behavioral attribute → 修改 reward 的范式是通用的；lambda 校准方法（使 penalty 标准差为 reward 标准差的 75%） | — |

核心区别：他们的 probe 是事后施加在已训练好的 RM 上做 reranking，不改变模型参数。如果我们的方法是在训练阶段通过 contrastive loss 直接调整模型表征，则是根本不同的介入层次。

Sources:
- [arXiv:2412.00967](https://arxiv.org/abs/2412.00967)
- [HTML version](https://arxiv.org/html/2412.00967v1)
- [CHAI blog post](https://humancompatible.ai/news/2024/12/14/linear-probe-penalties-reduce-llm-sycophancy/)

---
