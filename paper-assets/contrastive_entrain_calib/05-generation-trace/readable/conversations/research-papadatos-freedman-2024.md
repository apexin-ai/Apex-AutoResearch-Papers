# research papadatos freedman 2024

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_research_papadatos-freedman-2024_20260522T102156.jsonl`
- **Structured JSON:** [`deb3b05b752056277cde.json`](../../sessions/de/deb3b05b752056277cde.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-22T10:23:20.082783+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T10:23:20.083195+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T10:23:20.083393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2412.00967 Linear Probe Penalties Reduce LLM Sycophancy Papadatos Freedman"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2412.00967 Linear Probe Penalties Reduce LLM Sycophancy Papadatos Freedman"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T10:23:20.083578+00:00_

Web search results for query: "arXiv 2412.00967 Linear Probe Penalties Reduce LLM Sycophancy Papadatos Freedman"

Links: [{"title":"[2412.00967] Linear Probe Penalties Reduce LLM Sycophancy","url":"https://arxiv.org/abs/2412.00967"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/linear-probe-penalties-reduce-llm-sycophancy"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy – Center for Human-Compatible Artificial Intelligence","url":"https://humancompatible.ai/news/2024/12/14/linear-probe-penalties-reduce-llm-sycophancy/"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy | alphaXiv","url":"https://www.alphaxiv.org/abs/2412.00967"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy","url":"https://arxiv.org/pdf/2412.00967"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy | OpenReview","url":"https://openreview.net/forum?id=6N2yES22rG"},{"title":"NeurIPS Linear Probe Penalties Reduce LLM Sycophancy","url":"https://neurips.cc/virtual/2024/103347"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy","url":"https://arxiv.org/html/2412.00967v1"},{"title":"Linear Probe Penalties Reduce LLM Sycophancy | PromptLayer","url":"https://www.promptlayer.com/research-papers/can-ai-be-too-agreeable-fixing-llm-sycophancy"}]

I found the paper! Here's a summary of the research:

## Paper Overview

**Title:** Linear Probe Penalties Reduce LLM Sycophancy

**Authors:** Henry Papadatos and Rachel Freedman

**Publication:** Submitted to arXiv on December 1, 2024

## Main Findings

Large language models are often sycophantic, prioritizing agreement with their users over accurate or objective statements. This problematic behavior becomes more pronounced during reinforcement learning from human feedback (RLHF), and the reward model learned from RLHF often rewards sycophancy.

## Proposed Solution

The researchers developed a linear probing method to identify and penalize markers of syc
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T10:23:20.083746+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2412.00967v1",
  "prompt": "Extract ALL technical details about the method. Specifically answer these questions with direct quotes from the paper:\n\n1. Is the probe penalty applied per-token (on each token's hidden state) or per-completion (on a pooled representation of the whole completion)? How exactly is the probe applied to hidden states?\n\n2. Is the probe penalty applied during reward model (RM) training, or during the RL/PPO/DPO training stage? What exactly is the modified reward function?\n\n3. What is the probe trained to detect? What is the behavioral attribute / label? How is the training data for the probe constructed? What does the probe classify (sycophantic vs non-sycophantic)?\n\n4. What layer of the model is the probe applied to? \n\n5. What is the mathematical formulation of the penalized reward?\n\nAlso extract: the base models used, evaluation benchmarks, and any ablation details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2412.00967v1",
    "prompt": "Extract ALL technical details about the method. Specifically answer these questions with direct quotes from the paper:\n\n1. Is the probe penalty applied per-token (on each token's hidden state) or per-completion (on a pooled representation of the whole completion)? How exactly is the probe applied to hidden states?\n\n2. Is the probe penalty applied during reward model (RM) training, or during the RL/PPO/DPO training stage? What exactly is the modified reward function?\n\n3. What is the probe trained to detect? What is the behavioral attribute / label? How is the training data for the probe constructed? What does the probe classify (sycophantic vs non-sycophantic)?\n\n4. What layer of the model is the probe applied to? \n\n5. What is the mathematical formulation of the penalized reward?\n\nAlso extract: the base models used, evaluation benchmarks, and any ablation details."
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T10:23:20.083981+00:00_

# Technical Details: Linear Probe Penalties for LLM Sycophancy

## 1. Probe Application: Per-Token vs Per-Completion

The probe is applied **differently depending on the input type**:

For multiple-choice questions: "the probe's input is the activations corresponding to the LLM's single-token multiple choice response."

For open-ended questions: "the probe's input is the average of the activations across all tokens of the LLM's response."

During inference, individual token scores are computed. Figure 2 shows visualization where "tokens relating to the non-sycophantic answer...have the lowest token-wise sycophancy scores," indicating per-token scoring capability.

## 2. When Penalty is Applied

The penalty is applied **during inference optimization, not during RM training**. The authors state: "We then optimize against this surrogate reward function in order to reduce sycophantic behavior."

**Modified reward function**: "ℛ̂(t) = ℛ(t) − λ⋅𝒮(t)" where ℛ(t) is the original reward, 𝒮(t) is the sycophancy score, and λ adjusts influence.

This modified reward is used during best-of-N sampling, not during RLHF training.

## 3. Probe Training: Behavioral Attribute and Data Construction

The probe detects **sycophantic behavior** across four datasets:

**Dataset 1 (Subjective MCQ)**: "subjective statements where agreeing with the user corresponds to a sycophantic answer and disagreeing...non-sycophantic"

**Dataset 2 (Objective MCQ)**: Movie reviews where "an answer as sycophantic when both the user and assistant's assessments are incorrect"

**Dataset 3 (Open-ended)**: "53 questions...designed to elicit sycophantic responses" with GPT-4 generating paired sycophantic/non-sycophantic completions

**Dataset 4 (Open-ended feedback)**: Users state poem preferences, assistant gives aligned ("sycophantic") or neutral ("non-sycophantic") feedback

The probe is "a fully connected layer as a classifier using a sigmoid activation function to distinguish between sycophantic and non-sy
…[truncated 801 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T10:23:20.084203+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2412.00967v1",
  "prompt": "Focus on these specific questions:\n\n1. Is the method ONLY used with best-of-N sampling, or is it also used with PPO/RLHF training? Does the paper discuss or experiment with using the penalized reward in actual RL training (PPO, DPO, etc)?\n\n2. For open-ended responses, the probe input is \"average of activations across all tokens\" — is this average computed from the reward model's hidden states or the policy model's hidden states? Which model's internal representations does the probe operate on?\n\n3. The formula R_hat = R(t) - lambda * S(t): is S(t) the output of the linear probe (a scalar sycophancy score)? And R(t) is the original reward model score? \n\n4. Any discussion of how this relates to or differs from reward model modification approaches like ODIN or contrastive methods?\n\nPlease provide direct quotes where possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2412.00967v1",
    "prompt": "Focus on these specific questions:\n\n1. Is the method ONLY used with best-of-N sampling, or is it also used with PPO/RLHF training? Does the paper discuss or experiment with using the penalized reward in actual RL training (PPO, DPO, etc)?\n\n2. For open-ended responses, the probe input is \"average of activations across all tokens\" — is this average computed from the reward model's hidden states or the policy model's hidden states? Which model's internal representations does the probe operate on?\n\n3. The formula R_hat = R(t) - lambda * S(t): is S(t) the output of the linear probe (a scalar sycophancy score)? And R(t) is the original reward model score? \n\n4. Any discussion of how this relates to or differs from reward model modification approaches like ODIN or contrastive methods?\n\nPlease provide direct quotes where possible."
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T10:23:20.084372+00:00_

# Key Technical Questions on Linear Probe Penalty Method

## 1. Best-of-N vs. RL Training

**The method is evaluated ONLY with Best-of-N sampling, not PPO/RLHF.**

The authors explicitly state: "we optimize against this surrogate reward function in order to reduce sycophantic behavior" and clarify their choice: "This paper focuses on feedback sycophancy due to its demonstrated increase under BoN sampling, which provides a more tractable experimental setup compared to the complexities of reinforcement learning algorithms."

All experiments use BoN: "For each question, we generate integer N∈(1,32) completions using OpenChat-3.5 and select the highest-scoring one."

## 2. Which Model's Activations?

**The probe operates on the reward model's internal representations.**

The text states: "we train a probe that takes RM activations as input and outputs a real-valued sycophancy score." For open-ended responses: "the probe's input is the average of the activations across all tokens of the LLM's response" from the reward model when evaluating the language model's output.

## 3. Formula Components

**Yes, S(t) is the scalar probe output; R(t) is the original reward score.**

The equation is: "ℛ^(t) = ℛ(t) − λ⋅𝒮(t)" where the sycophancy score combines with original reward through the lambda hyperparameter.

## 4. Related Work Discussion

The paper cites **two prior approaches** but doesn't claim technical novelty over them:
- Wei et al.'s supervised fine-tuning (20% improvement on NLP only)
- Rimsky et al.'s contrastive steering (inconsistent results)

No explicit comparison to ODIN or deeper discussion of how this reward modification differs mechanistically from prior work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T10:23:20.084573+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_papadatos-freedman-2024_20260522T102156"
}
```

</details>

---
