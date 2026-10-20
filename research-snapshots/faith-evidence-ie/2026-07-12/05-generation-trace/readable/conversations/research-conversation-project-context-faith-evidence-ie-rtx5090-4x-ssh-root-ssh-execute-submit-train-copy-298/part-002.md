# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-faith-evidence-ie-rtx5090-4x-ssh-root-ssh-execute-submit-train-copy-298.md) · [Structured JSON](../../../sessions/9b/9becda9ae83386c56594.json)

## Round 1

### Tool result

_source line 130 · 2026-05-15T23:17:15.233Z_

<details><summary>↩ Tool result · `toolu_01EhTEM9Cmu8LcMSTpADdt7H`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feba2d5e-db5f-4b8e-92b3-15c81bda511d",
  "isSidechain": false,
  "promptId": "fcca1661-c354-402e-b3d8-f5d1df3d64fd",
  "type": "user",
  "uuid": "f7634df0-40ad-4de8-ab86-743af4a826e2",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "oldString": "      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理\n      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，\n      但方向相反：不是让推理隐式化，而是让验证外部化。",
    "newString": "      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理\n      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，\n      但方向相反：不是让推理隐式化，而是让验证外部化。\n\n  # =========================================================================\n  # Related Work Survey (2026-05-15): 5 directions for FREIGE paper\n  # =========================================================================\n\n  # === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===\n\n  - title: \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\"\n    authors: Youmi Ma, An Wang, Naoaki Okazaki\n    year: 2023\n    venue: EACL 2023\n    url: https://arxiv.org/abs/2302.08675\n    category: evidence_based_docre\n    role: direct-competitor\n    key_finding: >\n      用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences。\n      提出 evidence retrieval (ER) self-training 策略，在无 evidence 标注的大规模数据上自动生成\n      silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。\n      解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。\n    relevance_to_freige: >\n      最重要的 evidence-based DocRE 先驱工作。DREEAM 用 evidence 引导 attention（encoder-based），\n      我们用 evidence 引导 RL reward（generative LLM）。关键代际差异：\n      (1) DREEAM 是 encoder-based（BERT/RoBERTa），我们是 LLM generative；\n      (2) DREEAM 的 evidence 用于注意力监督，我们的 evidence 用于 reward 设计和 CED reranking；\n      (3) DREEAM 未量化 evidence 对 RE 的 performance cost。\n      Related Work 必引：evidence-based DocRE 的代表性工作。\n\n  - title: \"DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models\"\n    authors: Junpeng Li, Zixia Jia, Zilong Zheng\n    year: 2023\n    venue: EMNLP 2023\n    url: https://arxiv.org/abs/2311.07314\n    category: evidence_based_docre\n    role: method-component\n    key_finding: >\n      用 LLM（ChatGPT）+ NLI 模块半自动生成 relation triples，增强 DocRE 数据集。\n      特别擅长 re-annotating long-tail relation types。提供四个增强训练数据集。\n      解决了 vanilla in-context learning 无法处理 DocRE 大量细粒度 relation types 的问题。\n    relevance_to_freige: >\n      DocGNRE 的 NLI 验证模块与我们 CED reranker 的 NLI scoring 思路类似——\n      都用 NLI 检查生成内容是否被文档支持。差异：DocGNRE 用 NLI 过滤数据增强，\n      我们用 NLI 做 inference-time reranking。DocGNRE 关注数据质量，我们关注训练范式。\n\n  - title: \"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction\"\n    authors: Khai Phan Tran, Xue Li\n    year: 2025\n    venue: arXiv 2504.06529\n    url: https://arxiv.org/abs/2504.06529\n    category: evidence_based_docre\n    role: direct-competitor\n    key_finding: >\n      用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式。\n      文档转化为 bipartite graph（entity pair nodes + sentence nodes），\n      三子图：Entity Pair 子图建模协作、Entity Pair-Sentence 子图捕捉语义关系、\n      Sentence 子图辅助共指推理。在 DocRED 上 evidence retrieval 和 RE 均有提升。\n    relevance_to_freige: >\n      CDER 是最新的 encoder-based evidence retrieval 方法，验证了 evidence 对 DocRE 的价值。\n      与我们的关键差异：(1) CDER 是 encoder-based pipeline，我们是 LLM generative；\n      (2) CDER 用 evidence 作为输入特征，我们用 evidence quality 作为 reward/reranking 信号；\n      (3) CDER 未探索 evidence generation 的 performance cost。\n\n  - title: \"Evidence-aware Document-level Relation Extraction\"\n    authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al.\n    year: 2022\n    venue: CIKM 2022\n    url: https://dl.acm.org/doi/10.1145/3511808.3557313\n    category: evidence_based_docre\n    role: background\n    key_finding: >\n      将 evidence sentence selection 建模为序列决策问题，\n      用 RL 机制选择支撑关系的 evidence sentences。\n      在 DocRED 上验证 evidence-aware 方法的有效性。\n    relevance_to_freige: >\n      早期将 RL 用于 DocRE evidence 的工作。其 RL 用于 evidence selection 策略，\n      我们的 RL 用于整体模型微调（GRPO/RSFT）。证实 RL+evidence+DocRE 的组合有研究价值。\n\n  # === Category 22: Faithfulness Cost in NLP (Direction 2) ===\n\n  - title: \"Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks\"\n    authors: Xiaolei Lu, Jianghong Ma\n    year: 2024\n    venue: arXiv 2404.00140\n    url: https://arxiv.org/abs/2404.00140\n    category: faithfulness_cost\n    role: evaluation\n    key_finding: >\n      在 sentiment analysis、intent detection、topic labeling 三个 NLP 任务上\n      系统比较 faithfulness 和 plausibility 的关系。传统 perturbation-based 方法\n      （Shapley value、LIME）可同时达到较高 faithfulness 和 plausibility。\n      关键发现：faithfulness 和 plausibility 并非必然冲突，\n      可通过双目标优化同时提升。\n    relevance_to_freige: >\n      提供了 faithfulness-plausibility 关系的实证基础。我们的 evidence generation\n      可视为 plausibility（evidence 看起来合理）vs faithfulness（evidence 真正驱动 RE）的张力。\n      CED reranker 的 NLI verification 本质上是在检查 faithfulness 而非仅 plausibility。\n\n  - title: \"Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models\"\n    authors: Anonymous\n    year: 2024\n    venue: arXiv 2402.04614\n    url: https://arxiv.org/abs/2402.04614\n    category: faithfulness_cost\n    role: key_evidence\n    key_finding: >\n      LLM 擅长生成 plausible 的解释，但这些解释不一定 faithful——\n      不与 LLM 的实际推理过程对齐。Self-explanations 的 reliability 存疑。\n      LLM 的解释行为更像 post-hoc rationalization 而非真实推理报告。\n    relevance_to_freige: >\n      直接支持我们的核心论点：要求 LLM 在 DocRE 中同时生成 evidence 可能\n      只是让模型学会 post-hoc rationalize，而非真正基于 evidence 做 RE。\n      CED reranker 的外部 NLI verification 正是为了对抗这种 unreliable self-explanation。\n\n  - title: \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"\n    authors: Anonymous\n    year: 2025\n    venue: EMNLP 2025\n    url: https://aclanthology.org/2025.emnlp-main.504.pdf\n    category: faithfulness_cost\n    role: evaluation\n    key_finding: >\n      通过 unlearning 推理步骤来衡量 CoT 的 faithfulness。\n      如果 unlearn 某个推理步骤后模型行为不变，说明该步骤不 faithful。\n      揭示了 CoT 推理步骤的 faithfulness 在不同任务和模型间差异巨大。\n    relevance_to_freige: >\n      提供了量化 faithfulness 的方法论。可用类似思路评估我们模型生成的 evidence\n      是否真正影响 RE 决策。CED reranker 的 evidence corruption test\n      本质上是这种 faithfulness 检验的 inference-time 版本。\n\n  # === Category 23: LoRA/QLoRA Training Artifacts (Direction 3) ===\n\n  - title: \"LoRA vs Full Fine-tuning: An Illusion of Equivalence\"\n    authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma\n    year: 2024\n    venue: arXiv 2410.21228\n    url: https://arxiv.org/abs/2410.21228\n    category: lora_qlora_artifacts\n    role: key_evidence\n    key_finding: >\n      LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵。LoRA 引入 intruder dimensions——\n      奇异值分解中出现新的高秩奇异向量（与预训练权重高度不相似）。Full fine-tuning 不会。\n      LoRA 的 forgetting 几乎全部集中在 intruder dimensions。\n      缩小 intruder dimensions 的奇异值可显著恢复预训练分布建模能力，\n      同时仅微小影响下游任务性能。\n    relevance_to_freige: >\n      直接解释我们的 QLoRA GRPO decoupling 现象。LoRA/QLoRA 的 intruder dimensions\n      可能是 extraction-evidence decoupling 的结构性原因：\n      4-bit 量化 + LoRA 低秩约束导致 extraction 和 evidence 任务被迫共享\n      有限的 intruder dimensions，当 RL 优化 amplify 这些维度时，\n      两个任务的 gradient 在 intruder space 中产生干扰导致 decoupling。\n      bf16 full fine-tuning 无 intruder dimensions 问题，因此不复现。\n\n  - title: \"The Impact of LoRA on the Emergence of Clusters in Transformers\"\n    authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard\n    year: 2024\n    venue: arXiv 2402.15415\n    url: https://arxiv.org/abs/2402.15415\n    category: lora_qlora_artifacts\n    role: theoretical_support\n    key_finding: >\n      用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。\n      LoRA 作为低秩扰动作用于交互粒子系统（tokens）。\n      发现关于扰动范数和 Transformer 深度的 phase transition：\n      超过某个阈值后从 non-forgetting 转变为 forgetting behavior。\n      理论上界 time-to-deviation 与扰动大小和谱特性相关。\n    relevance_to_freige: >\n      提供了 LoRA forgetting 的理论框架。我们的 QLoRA GRPO decoupling 可能\n      对应 phase transition 的临界区域——4-bit 量化使扰动有效范数增大，\n      加上 GRPO 的 online 更新持续增大扰动，更容易触发 forgetting/decoupling phase transition。\n      bf16 下扰动范数更可控，因此保持在 non-forgetting phase。\n\n  - title: \"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs\"\n    authors: NVIDIA, MIT, HKU, THU\n    year: 2025\n    venue: arXiv 2510.11696\n    url: https://arxiv.org/abs/2510.11696\n    category: lora_qlora_artifacts\n    role: direct-competitor\n    key_finding: >\n      标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声\n      可通过增加 policy entropy 促进探索。Adaptive Quantization Noise (AQN) 机制\n      动态调整噪声。结合 NVFP4 + LoRA 实现 1.5x rollout 加速。\n      首次在单张 H100 上实现 32B LLM 的 RL 训练。\n    relevance_to_freige: >\n      QeRL 证明量化噪声可以被利用而非消除。与我们的发现互补：\n      我们发现 QLoRA 的量化在多目标 RL 中导致 task decoupling（负面影响），\n      QeRL 发现适当控制的量化噪声可促进单目标 exploration（正面利用）。\n      差异在于：单目标场景下噪声促进探索有益，\n      多目标场景下噪声加剧不同子任务间的 gradient 干扰。\n\n  - title: \"The Impact of Quantization on Large Reasoning Model Reinforcement Learning\"\n    authors: Anonymous\n    year: 2025\n    venue: NeurIPS 2025 Workshop (Efficient Reasoning)\n    url: https://arxiv.org/abs/2511.15694\n    category: lora_qlora_artifacts\n    role: key_evidence\n    key_finding: >\n      系统评估量化对 LRM RL 训练的影响。发现 quantization-aware RL training\n      反而损害学习过程，PTQ 和 QLoRA 表现更好。\n      post-RL 量化模型和 quantization-aware RL 模型在推理性能上存在显著差距。\n    relevance_to_freige: >\n      直接支持我们的观察：QLoRA GRPO 训练不稳定可能源于\n      quantization 和 RL 优化的复杂交互。该论文在数学推理任务上的发现\n      与我们在 DocRE 上的 task decoupling 观察一致——\n      量化在 RL 训练过程中引入系统性干扰。\n\n  # === Category 24: GRPO / Online RL for NLP Beyond RLHF (Direction 4) ===\n\n  - title: \"ReasoningNER: A Reasoning Paradigm for Named Entity Recognition\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2511.11978\n    url: https://arxiv.org/abs/2511.11978\n    category: grpo_nlp_applications\n    role: direct-competitor\n    key_finding: >\n      三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。\n      用 composite reward（entity F1 + format compliance）训练 GRPO policy。\n      ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1，\n      1.7B 版本超 DeepSeek-R1-8B 10.5 F1。\n    relevance_to_freige: >\n      GRPO 成功应用于 IE（NER）的案例。NER reward 结构相对简单（entity-level F1），\n      reward variance 天然较高（不同 span 组合产生多样 F1 分数）。\n      再次支持：结构简单的 IE 任务 GRPO 成功，\n      文档级多 triple + evidence 的复杂任务需要额外设计（CED/RSFT）。\n\n  - title: \"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2508.05170\n    url: https://arxiv.org/abs/2508.05170\n    category: grpo_nlp_applications\n    role: method-component\n    key_finding: >\n      在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward），\n      有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。\n      通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。\n    relevance_to_freige: >\n      P-GRPO 的\"仅对成功输出奖励推理过程\"与我们 RSFT 的 rejection sampling 理念一致——\n      都是只从高质量输出中学习。P-GRPO 的 conditional reward 思路可启发 CED 改进：\n      只在 RE 正确时奖励 evidence quality，避免\"evidence 好但 RE 错\"的情况。\n\n  # === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===\n\n  - title: \"OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning\"\n    authors: Anonymous\n    year: 2024\n    venue: arXiv 2412.16145\n    url: https://arxiv.org/abs/2412.16145\n    category: rsft_offline_rl\n    role: direct-competitor\n    key_finding: >\n      基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function，\n      优化 soft Bellman Equation。无需 paired preference data，\n      实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。\n      在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。\n    relevance_to_freige: >\n      OREO 提供了比简单 RSFT 更理论化的 offline RL 框架。\n      我们的 RSFT 可视为 OREO 的特例（无 value function，简单 threshold filtering）。\n      Future work 方向：用 OREO 替代简单 RSFT 可能进一步提升 DocRE 性能。\n\n  - title: \"PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning\"\n    authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian\n    year: 2026\n    venue: arXiv 2601.14716\n    url: https://arxiv.org/abs/2601.14716\n    category: rsft_offline_rl\n    role: key_evidence\n    key_finding: >\n      基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法，\n      在训练稳定性和效率上优于 GRPO 等 online RL。\n      AIME 2024 平均 90.9%，AIME 2025 平均 85.6%，\n      在 Qwen2.5-32B post-training 中达 SOTA。\n    relevance_to_freige: >\n      强有力证据支持 offline RL > online RL 的论点。\n      PCL-Reasoner 在数学推理上用 offline RL 超越 GRPO，\n      与我们在 DocRE 上 RSFT 超越 GRPO 的发现一致。\n      两个独立领域的 converging evidence 增强了\n      \"structured output 任务中 offline 方法优于 online GRPO\"的普遍性论述。\n\n  - title: \"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models\"\n    authors: Anonymous\n    year: 2024\n    venue: NAACL 2024 Findings\n    url: https://arxiv.org/abs/2402.10038\n    category: rsft_offline_rl\n    role: method-component\n    key_finding: >\n      系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt，\n      根据 reward 分布识别 contrastive pairs，用 DPO 对齐。\n      在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。\n    relevance_to_freige: >\n      RS-DPO 提供了 rejection sampling 和 preference optimization 的桥梁方法。\n      我们的 RSFT 只用正样本训练（SFT loss），RS-DPO 进一步利用负样本构造 preference pair。\n      Future work 方向：可考虑用 RS-DPO 方式利用 RSFT rejected 样本做 DPO。\n\n  - title: \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\"\n    authors: Anonymous\n    year: 2024\n    venue: TMLR 2024\n    url: https://arxiv.org/abs/2304.06767\n    category: rsft_offline_rl\n    role: background\n    key_finding: >\n      RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。\n      每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。\n      在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。\n    relevance_to_freige: >\n      我们的 RSFT pipeline 直接基于 RAFT 框架。差异在于：\n      (1) 我们用 verifiable reward（F1 score）替代 learned reward model；\n      (2) 我们的 filtering 基于 extraction F1 threshold 而非 top-k ranking；\n      (3) 我们额外引入 CED reward 维度用于 inference-time reranking。",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 916,
        "oldLines": 3,
        "newStart": 916,
        "newLines": 315,
        "lines": [
          "       我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理",
          "       转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，",
          "       但方向相反：不是让推理隐式化，而是让验证外部化。",
          "+",
          "+  # =========================================================================",
          "+  # Related Work Survey (2026-05-15): 5 directions for FREIGE paper",
          "+  # =========================================================================",
          "+",
          "+  # === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===",
          "+",
          "+  - title: \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\"",
          "+    authors: Youmi Ma, An Wang, Naoaki Okazaki",
          "+    year: 2023",
          "+    venue: EACL 2023",
          "+    url: https://arxiv.org/abs/2302.08675",
          "+    category: evidence_based_docre",
          "+    role: direct-competitor",
          "+    key_finding: >",
          "+      用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences。",
          "+      提出 evidence retrieval (ER) self-training 策略，在无 evidence 标注的大规模数据上自动生成",
          "+      silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。",
          "+      解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。",
          "+    relevance_to_freige: >",
          "+      最重要的 evidence-based DocRE 先驱工作。DREEAM 用 evidence 引导 attention（encoder-based），",
          "+      我们用 evidence 引导 RL reward（generative LLM）。关键代际差异：",
          "+      (1) DREEAM 是 encoder-based（BERT/RoBERTa），我们是 LLM generative；",
          "+      (2) DREEAM 的 evidence 用于注意力监督，我们的 evidence 用于 reward 设计和 CED reranking；",
          "+      (3) DREEAM 未量化 evidence 对 RE 的 performance cost。",
          "+      Related Work 必引：evidence-based DocRE 的代表性工作。",
          "+",
          "+  - title: \"DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models\"",
          "+    authors: Junpeng Li, Zixia Jia, Zilong Zheng",
          "+    year: 2023",
          "+    venue: EMNLP 2023",
          "+    url: https://arxiv.org/abs/2311.07314",
          "+    category: evidence_based_docre",
          "+    role: method-component",
          "+    key_finding: >",
          "+      用 LLM（ChatGPT）+ NLI 模块半自动生成 relation triples，增强 DocRE 数据集。",
          "+      特别擅长 re-annotating long-tail relation types。提供四个增强训练数据集。",
          "+      解决了 vanilla in-context learning 无法处理 DocRE 大量细粒度 relation types 的问题。",
          "+    relevance_to_freige: >",
          "+      DocGNRE 的 NLI 验证模块与我们 CED reranker 的 NLI scoring 思路类似——",
          "+      都用 NLI 检查生成内容是否被文档支持。差异：DocGNRE 用 NLI 过滤数据增强，",
          "+      我们用 NLI 做 inference-time reranking。DocGNRE 关注数据质量，我们关注训练范式。",
          "+",
          "+  - title: \"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction\"",
          "+    authors: Khai Phan Tran, Xue Li",
          "+    year: 2025",
          "+    venue: arXiv 2504.06529",
          "+    url: https://arxiv.org/abs/2504.06529",
          "+    category: evidence_based_docre",
          "+    role: direct-competitor",
          "+    key_finding: >",
          "+      用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式。",
          "+      文档转化为 bipartite graph（entity pair nodes + sentence nodes），",
          "+      三子图：Entity Pair 子图建模协作、Entity Pair-Sentence 子图捕捉语义关系、",
          "+      Sentence 子图辅助共指推理。在 DocRED 上 evidence retrieval 和 RE 均有提升。",
          "+    relevance_to_freige: >",
          "+      CDER 是最新的 encoder-based evidence retrieval 方法，验证了 evidence 对 DocRE 的价值。",
          "+      与我们的关键差异：(1) CDER 是 encoder-based pipeline，我们是 LLM generative；",
          "+      (2) CDER 用 evidence 作为输入特征，我们用 evidence quality 作为 reward/reranking 信号；",
          "+      (3) CDER 未探索 evidence generation 的 performance cost。",
          "+",
          "+  - title: \"Evidence-aware Document-level Relation Extraction\"",
          "+    authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al.",
          "+    year: 2022",
          "+    venue: CIKM 2022",
          "+    url: https://dl.acm.org/doi/10.1145/3511808.3557313",
          "+    category: evidence_based_docre",
          "+    role: background",
          "+    key_finding: >",
          "+      将 evidence sentence selection 建模为序列决策问题，",
          "+      用 RL 机制选择支撑关系的 evidence sentences。",
          "+      在 DocRED 上验证 evidence-aware 方法的有效性。",
          "+    relevance_to_freige: >",
          "+      早期将 RL 用于 DocRE evidence 的工作。其 RL 用于 evidence selection 策略，",
          "+      我们的 RL 用于整体模型微调（GRPO/RSFT）。证实 RL+evidence+DocRE 的组合有研究价值。",
          "+",
          "+  # === Category 22: Faithfulness Cost in NLP (Direction 2) ===",
          "+",
          "+  - title: \"Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks\"",
          "+    authors: Xiaolei Lu, Jianghong Ma",
          "+    year: 2024",
          "+    venue: arXiv 2404.00140",
          "+    url: https://arxiv.org/abs/2404.00140",
          "+    category: faithfulness_cost",
          "+    role: evaluation",
          "+    key_finding: >",
          "+      在 sentiment analysis、intent detection、topic labeling 三个 NLP 任务上",
          "+      系统比较 faithfulness 和 plausibility 的关系。传统 perturbation-based 方法",
          "+      （Shapley value、LIME）可同时达到较高 faithfulness 和 plausibility。",
          "+      关键发现：faithfulness 和 plausibility 并非必然冲突，",
          "+      可通过双目标优化同时提升。",
          "+    relevance_to_freige: >",
          "+      提供了 faithfulness-plausibility 关系的实证基础。我们的 evidence generation",
          "+      可视为 plausibility（evidence 看起来合理）vs faithfulness（evidence 真正驱动 RE）的张力。",
          "+      CED reranker 的 NLI verification 本质上是在检查 faithfulness 而非仅 plausibility。",
          "+",
          "+  - title: \"Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models\"",
          "+    authors: Anonymous",
          "+    year: 2024",
          "+    venue: arXiv 2402.04614",
          "+    url: https://arxiv.org/abs/2402.04614",
          "+    category: faithfulness_cost",
          "+    role: key_evidence",
          "+    key_finding: >",
          "+      LLM 擅长生成 plausible 的解释，但这些解释不一定 faithful——",
          "+      不与 LLM 的实际推理过程对齐。Self-explanations 的 reliability 存疑。",
          "+      LLM 的解释行为更像 post-hoc rationalization 而非真实推理报告。",
          "+    relevance_to_freige: >",
          "+      直接支持我们的核心论点：要求 LLM 在 DocRE 中同时生成 evidence 可能",
          "+      只是让模型学会 post-hoc rationalize，而非真正基于 evidence 做 RE。",
          "+      CED reranker 的外部 NLI verification 正是为了对抗这种 unreliable self-explanation。",
          "+",
          "+  - title: \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"",
          "+    authors: Anonymous",
          "+    year: 2025",
          "+    venue: EMNLP 2025",
          "+    url: https://aclanthology.org/2025.emnlp-main.504.pdf",
          "+    category: faithfulness_cost",
          "+    role: evaluation",
          "+    key_finding: >",
          "+      通过 unlearning 推理步骤来衡量 CoT 的 faithfulness。",
          "+      如果 unlearn 某个推理步骤后模型行为不变，说明该步骤不 faithful。",
          "+      揭示了 CoT 推理步骤的 faithfulness 在不同任务和模型间差异巨大。",
          "+    relevance_to_freige: >",
          "+      提供了量化 faithfulness 的方法论。可用类似思路评估我们模型生成的 evidence",
          "+      是否真正影响 RE 决策。CED reranker 的 evidence corruption test",
          "+      本质上是这种 faithfulness 检验的 inference-time 版本。",
          "+",
          "+  # === Category 23: LoRA/QLoRA Training Artifacts (Direction 3) ===",
          "+",
          "+  - title: \"LoRA vs Full Fine-tuning: An Illusion of Equivalence\"",
          "+    authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma",
          "+    year: 2024",
          "+    venue: arXiv 2410.21228",
          "+    url: https://arxiv.org/abs/2410.21228",
          "+    category: lora_qlora_artifacts",
          "+    role: key_evidence",
          "+    key_finding: >",
          "+      LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵。LoRA 引入 intruder dimensions——",
          "+      奇异值分解中出现新的高秩奇异向量（与预训练权重高度不相似）。Full fine-tuning 不会。",
          "+      LoRA 的 forgetting 几乎全部集中在 intruder dimensions。",
          "+      缩小 intruder dimensions 的奇异值可显著恢复预训练分布建模能力，",
          "+      同时仅微小影响下游任务性能。",
          "+    relevance_to_freige: >",
          "+      直接解释我们的 QLoRA GRPO decoupling 现象。LoRA/QLoRA 的 intruder dimensions",
          "+      可能是 extraction-evidence decoupling 的结构性原因：",
          "+      4-bit 量化 + LoRA 低秩约束导致 extraction 和 evidence 任务被迫共享",
          "+      有限的 intruder dimensions，当 RL 优化 amplify 这些维度时，",
          "+      两个任务的 gradient 在 intruder space 中产生干扰导致 decoupling。",
          "+      bf16 full fine-tuning 无 intruder dimensions 问题，因此不复现。",
          "+",
          "+  - title: \"The Impact of LoRA on the Emergence of Clusters in Transformers\"",
          "+    authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard",
          "+    year: 2024",
          "+    venue: arXiv 2402.15415",
          "+    url: https://arxiv.org/abs/2402.15415",
          "+    category: lora_qlora_artifacts",
          "+    role: theoretical_support",
          "+    key_finding: >",
          "+      用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。",
          "+      LoRA 作为低秩扰动作用于交互粒子系统（tokens）。",
          "+      发现关于扰动范数和 Transformer 深度的 phase transition：",
          "+      超过某个阈值后从 non-forgetting 转变为 forgetting behavior。",
          "+      理论上界 time-to-deviation 与扰动大小和谱特性相关。",
          "+    relevance_to_freige: >",
          "+      提供了 LoRA forgetting 的理论框架。我们的 QLoRA GRPO decoupling 可能",
          "+      对应 phase transition 的临界区域——4-bit 量化使扰动有效范数增大，",
          "+      加上 GRPO 的 online 更新持续增大扰动，更容易触发 forgetting/decoupling phase transition。",
          "+      bf16 下扰动范数更可控，因此保持在 non-forgetting phase。",
          "+",
          "+  - title: \"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs\"",
          "+    authors: NVIDIA, MIT, HKU, THU",
          "+    year: 2025",
          "+    venue: arXiv 2510.11696",
          "+    url: https://arxiv.org/abs/2510.11696",
          "+    category: lora_qlora_artifacts",
          "+    role: direct-competitor",
          "+    key_finding: >",
          "+      标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声",
          "+      可通过增加 policy entropy 促进探索。Adaptive Quantization Noise (AQN) 机制",
          "+      动态调整噪声。结合 NVFP4 + LoRA 实现 1.5x rollout 加速。",
          "+      首次在单张 H100 上实现 32B LLM 的 RL 训练。",
          "+    relevance_to_freige: >",
          "+      QeRL 证明量化噪声可以被利用而非消除。与我们的发现互补：",
          "+      我们发现 QLoRA 的量化在多目标 RL 中导致 task decoupling（负面影响），",
          "+      QeRL 发现适当控制的量化噪声可促进单目标 exploration（正面利用）。",
          "+      差异在于：单目标场景下噪声促进探索有益，",
          "+      多目标场景下噪声加剧不同子任务间的 gradient 干扰。",
          "+",
          "+  - title: \"The Impact of Quantization on Large Reasoning Model Reinforcement Learning\"",
          "+    authors: Anonymous",
          "+    year: 2025",
          "+    venue: NeurIPS 2025 Workshop (Efficient Reasoning)",
          "+    url: https://arxiv.org/abs/2511.15694",
          "+    category: lora_qlora_artifacts",
          "+    role: key_evidence",
          "+    key_finding: >",
          "+      系统评估量化对 LRM RL 训练的影响。发现 quantization-aware RL training",
          "+      反而损害学习过程，PTQ 和 QLoRA 表现更好。",
          "+      post-RL 量化模型和 quantization-aware RL 模型在推理性能上存在显著差距。",
          "+    relevance_to_freige: >",
          "+      直接支持我们的观察：QLoRA GRPO 训练不稳定可能源于",
          "+      quantization 和 RL 优化的复杂交互。该论文在数学推理任务上的发现",
          "+      与我们在 DocRE 上的 task decoupling 观察一致——",
          "+      量化在 RL 训练过程中引入系统性干扰。",
          "+",
          "+  # === Category 24: GRPO / Online RL for NLP Beyond RLHF (Direction 4) ===",
          "+",
          "+  - title: \"ReasoningNER: A Reasoning Paradigm for Named Entity Recognition\"",
          "+    authors: Anonymous",
          "+    year: 2025",
          "+    venue: arXiv 2511.11978",
          "+    url: https://arxiv.org/abs/2511.11978",
          "+    category: grpo_nlp_applications",
          "+    role: direct-competitor",
          "+    key_finding: >",
          "+      三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。",
          "+      用 composite reward（entity F1 + format compliance）训练 GRPO policy。",
          "+      ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1，",
          "+      1.7B 版本超 DeepSeek-R1-8B 10.5 F1。",
          "+    relevance_to_freige: >",
          "+      GRPO 成功应用于 IE（NER）的案例。NER reward 结构相对简单（entity-level F1），",
          "+      reward variance 天然较高（不同 span 组合产生多样 F1 分数）。",
          "+      再次支持：结构简单的 IE 任务 GRPO 成功，",
          "+      文档级多 triple + evidence 的复杂任务需要额外设计（CED/RSFT）。",
          "+",
          "+  - title: \"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation\"",
          "+    authors: Anonymous",
          "+    year: 2025",
          "+    venue: arXiv 2508.05170",
          "+    url: https://arxiv.org/abs/2508.05170",
          "+    category: grpo_nlp_applications",
          "+    role: method-component",
          "+    key_finding: >",
          "+      在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward），",
          "+      有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。",
          "+      通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。",
          "+    relevance_to_freige: >",
          "+      P-GRPO 的\"仅对成功输出奖励推理过程\"与我们 RSFT 的 rejection sampling 理念一致——",
          "+      都是只从高质量输出中学习。P-GRPO 的 conditional reward 思路可启发 CED 改进：",
          "+      只在 RE 正确时奖励 evidence quality，避免\"evidence 好但 RE 错\"的情况。",
          "+",
          "+  # === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===",
          "+",
          "+  - title: \"OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning\"",
          "+    authors: Anonymous",
          "+    year: 2024",
          "+    venue: arXiv 2412.16145",
          "+    url: https://arxiv.org/abs/2412.16145",
          "+    category: rsft_offline_rl",
          "+    role: direct-competitor",
          "+    key_finding: >",
          "+      基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function，",
          "+      优化 soft Bellman Equation。无需 paired preference data，",
          "+      实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。",
          "+      在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。",
          "+    relevance_to_freige: >",
          "+      OREO 提供了比简单 RSFT 更理论化的 offline RL 框架。",
          "+      我们的 RSFT 可视为 OREO 的特例（无 value function，简单 threshold filtering）。",
          "+      Future work 方向：用 OREO 替代简单 RSFT 可能进一步提升 DocRE 性能。",
          "+",
          "+  - title: \"PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning\"",
          "+    authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian",
          "+    year: 2026",
          "+    venue: arXiv 2601.14716",
          "+    url: https://arxiv.org/abs/2601.14716",
          "+    category: rsft_offline_rl",
          "+    role: key_evidence",
          "+    key_finding: >",
          "+      基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法，",
          "+      在训练稳定性和效率上优于 GRPO 等 online RL。",
          "+      AIME 2024 平均 90.9%，AIME 2025 平均 85.6%，",
          "+      在 Qwen2.5-32B post-training 中达 SOTA。",
          "+    relevance_to_freige: >",
          "+      强有力证据支持 offline RL > online RL 的论点。",
          "+      PCL-Reasoner 在数学推理上用 offline RL 超越 GRPO，",
          "+      与我们在 DocRE 上 RSFT 超越 GRPO 的发现一致。",
          "+      两个独立领域的 converging evidence 增强了",
          "+      \"structured output 任务中 offline 方法优于 online GRPO\"的普遍性论述。",
          "+",
          "+  - title: \"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models\"",
          "+    authors: Anonymous",
          "+    year: 2024",
          "+    venue: NAACL 2024 Findings",
          "+    url: https://arxiv.org/abs/2402.10038",
          "+    category: rsft_offline_rl",
          "+    role: method-component",
          "+    key_finding: >",
          "+      系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt，",
          "+      根据 reward 分布识别 contrastive pairs，用 DPO 对齐。",
          "+      在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。",
          "+    relevance_to_freige: >",
          "+      RS-DPO 提供了 rejection sampling 和 preference optimization 的桥梁方法。",
          "+      我们的 RSFT 只用正样本训练（SFT loss），RS-DPO 进一步利用负样本构造 preference pair。",
          "+      Future work 方向：可考虑用 RS-DPO 方式利用 RSFT rejected 样本做 DPO。",
          "+",
          "+  - title: \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\"",
          "+    authors: Anonymous",
          "+    year: 2024",
          "+    venue: TMLR 2024",
          "+    url: https://arxiv.org/abs/2304.06767",
          "+    category: rsft_offline_rl",
          "+    role: background",
          "+    key_finding: >",
          "+      RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。",
          "+      每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。",
          "+      在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。",
          "+    relevance_to_freige: >",
          "+      我们的 RSFT pipeline 直接基于 RAFT 框架。差异在于：",
          "+      (1) 我们用 verifiable reward（F1 score）替代 learned reward model；",
          "+      (2) 我们的 filtering 基于 extraction F1 threshold 而非 top-k ranking；",
          "+      (3) 我们额外引入 CED reward 维度用于 inference-time reranking。"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "feba2d5e-db5f-4b8e-92b3-15c81bda511d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "381322a6-8e0b-4a79-be76-b18c9ab69f81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 131_

```json
{
  "type": "last-prompt",
  "leafUuid": "f7634df0-40ad-4de8-ab86-743af4a826e2",
  "sessionId": "381322a6-8e0b-4a79-be76-b18c9ab69f81"
}
```

---


### Runtime record

_source line 132_

```json
{
  "type": "ai-title",
  "aiTitle": "Research literature related work for FREIGE paper",
  "sessionId": "381322a6-8e0b-4a79-be76-b18c9ab69f81"
}
```

---


### Assistant

_source line 133 · 2026-05-15T23:17:29.902Z_

已完成。`literature_map.yaml` 更新为 25 个类别共 53 篇论文，新增 15 篇覆盖 5 个调研方向：

| 方向 | 新增论文 | 关键文献 |
|------|---------|---------|
| **1. Evidence-based DocRE** | 4 篇 | DREEAM (EACL'23), DocGNRE (EMNLP'23), CDER (2025), Evidence-aware DocRE (CIKM'22) |
| **2. Faithfulness cost** | 3 篇 | "Faithfulness vs Plausibility" (2024), "Does Faithfulness Conflict..." (2024), "Measuring CoT Faithfulness" (EMNLP'25) |
| **3. LoRA/QLoRA artifacts** | 4 篇 | "Illusion of Equivalence" (2024), LoRA phase transition (2024), QeRL (NVIDIA'25), Quantization impact on RL (NeurIPS'25 WS) |
| **4. GRPO beyond RLHF** | 2 篇 | ReasoningNER (2025), Posterior-GRPO (2025) |
| **5. RSFT / Offline RL** | 4 篇 (新增2已有3) | OREO (2024), PCL-Reasoner (2026), RS-DPO (NAACL'24), RAFT (TMLR'24) |

核心发现对论文 positioning 的影响：
- **C2 (QLoRA decoupling)** 现在有"Illusion of Equivalence"的 intruder dimensions 和 LoRA phase transition 理论支撑
- **C1 (evidence tax)** 有 DREEAM/EIDER 作为 DocRE evidence 先驱 + faithfulness cost 量化文献
- **RSFT 优于 GRPO** 有 PCL-Reasoner (math) 和 OREO 作为跨领域 converging evidence

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7634df0-40ad-4de8-ab86-743af4a826e2",
  "isSidechain": false,
  "requestId": "req_011Cb5CziHpG2wyygwKvuqGa",
  "type": "assistant",
  "uuid": "0d710c09-ed45-461c-8370-bbbe04813356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "381322a6-8e0b-4a79-be76-b18c9ab69f81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FmPAb6zbL4cBBXDXH9kJF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6505,
      "cache_read_input_tokens": 121509,
      "output_tokens": 550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 550,
          "cache_read_input_tokens": 121509,
          "cache_creation_input_tokens": 6505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6505
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 134_

```json
{
  "type": "last-prompt",
  "leafUuid": "0d710c09-ed45-461c-8370-bbbe04813356",
  "sessionId": "381322a6-8e0b-4a79-be76-b18c9ab69f81"
}
```

---


### Runtime record

_source line 135_

```json
{
  "type": "ai-title",
  "aiTitle": "Research literature related work for FREIGE paper",
  "sessionId": "381322a6-8e0b-4a79-be76-b18c9ab69f81"
}
```

---
