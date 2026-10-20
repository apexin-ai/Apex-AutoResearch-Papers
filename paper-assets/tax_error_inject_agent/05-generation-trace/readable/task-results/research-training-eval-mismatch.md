# research training eval mismatch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_training-eval-mismatch_20260515T015251_result.json`
- **Structured JSON:** [`cc6ae105388d49aa378d.json`](../../sessions/cc/cc6ae105388d49aa378d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是与你们发现最相关的 5 篇论文：

---

### 1. A Closer Look at Memorization in Deep Networks
**Arpit et al., 2017, ICML**

- **关联点**：直接解释了你们观察到的 "injection 比例越高 → 训练 loss 越低但 eval 越差" 的现象。DNN 在含噪数据上会经历两个阶段：先学习 clean pattern（early learning phase），然后逐步 memorize noise sample。50% injection 时模型有大量 noisy sample 可以 memorize，训练 loss/accuracy 看起来更好，但学到的是 noise-specific pattern 而非可泛化的 knowledge。
- **核心结论**：DNNs tend to prioritize learning simple patterns first, then memorize noise. 训练数据本身在决定 memorization 程度上起关键作用——dataset-independent 的 capacity 概念不足以解释泛化行为。

### 2. Early-Learning Regularization Prevents Memorization of Noisy Labels
**Liu et al., 2020, NeurIPS**

- **关联点**：提出了 "early learning phenomenon" 的形式化描述。模型先用 cross-entropy 学到 true labels（即使部分 sample 有错误标注），然后在后期 memorize 错误标注。这与你们的情况高度吻合：error injection 的 sample 在训练早期被正确处理，但随着训练推进，模型开始 memorize injected errors，导致对 clean distribution 的泛化下降。
- **核心结论**：Early learning provides a window where the model predicts true labels even for mislabeled examples; without intervention, the model eventually memorizes wrong labels, degrading clean-data generalization。他们提出的 ELR 正则化通过利用 early learning 阶段的预测来防止 memorization。

### 3. LIMA: Less Is More for Alignment
**Zhou et al., 2023, NeurIPS**

- **关联点**：提出 **Superficial Alignment Hypothesis**——LLM 的 knowledge 和 capability 几乎全部来自 pretraining，SFT 只教模型 output style/format。这解释了为什么你们的 training loss 改善不等于 capability 提升：error injection 让模型更好地拟合训练分布的 surface pattern（更低 loss），但并未增强（甚至损害了）预训练获得的 downstream task capability。
- **核心结论**：Almost all knowledge in LLMs is learned during pretraining; only limited instruction tuning data is necessary to teach models to produce high-quality output. SFT loss 的优化方向与 downstream capability 本质上是不同的目标。

### 4. An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning
**Luo et al., 2023, arXiv**

- **关联点**：SFT 本质是 off-policy learning——模型模仿固定数据而非从自身尝试中学习，因此容易 overfit 到训练分布并遗忘预训练 knowledge。你们的 error injection 引入了与 clean eval 分布更大的 gap，加剧了 catastrophic forgetting。50% injection 的 taxei 模型 eval 从 61.7% 降到 51.1%，说明 injected distribution 覆写了部分预训练知识。
- **核心结论**：Catastrophic forgetting severity intensifies as the divergence between fine-tuning data and original pretraining distribution increases。模型在 1B-7B 参数范围内，forgetting 随 scale 增加反而加剧。

### 5. To Augment or Not to Augment? A Comparative Study on Text Augmentation Techniques for Low-Resource NLP
**Longpre et al., 2020, ACL (Computational Linguistics)**

- **关联点**：系统研究了 NLP data augmentation 失效的场景。核心发现：文本增强方法假设是 label-preserving 且不改变数据分布，但这些假设在实践中经常不成立，导致 noisy labels 或 distribution shift 从而降低性能。Token-level augmentation 在复杂任务上 surprisingly hurt performance。你们的 error injection 本质上就是一种 non-label-preserving augmentation，引入了 distribution shift。
- **核心结论**：Data augmentation in NLP can degrade performance when it violates label-preservation assumptions or shifts the data distribution, especially for harder tasks where baseline performance is already challenging.

---

**总结你们现象的文献解释链**：

Error injection → 训练分布偏移（Paper 5） → 模型先学 clean pattern 再 memorize noise（Paper 1, 2） → SFT loss 优化的是 surface-level 拟合而非 downstream capability（Paper 3） → 偏移的训练分布加剧 catastrophic forgetting，覆写预训练知识（Paper 4）。

injection 比例越高，这条链的每个环节都放大，所以 50% injection 出现 "训练最好、eval 最差" 的极端 pattern。

Sources:
- [Arpit et al. 2017 - A Closer Look at Memorization in Deep Networks](https://arxiv.org/abs/1706.05394)
- [Liu et al. 2020 - Early-Learning Regularization Prevents Memorization of Noisy Labels](https://par.nsf.gov/servlets/purl/10229423)
- [Zhou et al. 2023 - LIMA: Less Is More for Alignment](https://arxiv.org/pdf/2305.11206)
- [Luo et al. 2023 - An Empirical Study of Catastrophic Forgetting in LLMs](https://arxiv.org/abs/2308.08747)
- [Longpre et al. 2020 - To Augment or Not to Augment?](https://direct.mit.edu/coli/article/48/1/5/108844/To-Augment-or-Not-to-Augment-A-Comparative-Study)

---
