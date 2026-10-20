# 文献调研：SFT Contamination 的跨 Benchmark 泛化效应

> 背景：MMLU contamination SFT 在 GSM8K 上产生 +11.07pp 提升（Qwen-7B s42），GSM8K 不在训练集中。

---

## 1. SFT Cross-Benchmark Transfer

- **[Yao et al., 2026]** *The Impact of Post-training on Data Contamination* (arXiv:2601.06103) — 在预训练中注入 GSM8K/MBPP 测试集，对比 SFT 和 GRPO 的影响。关键发现：**SFT 仅在被污染任务上膨胀分数，而 GRPO 同时在未污染任务（GSMPlus, HumanEval）上也产生提升。** 与我们的发现形成对比：我们的 SFT 在 MMLU 数据上训练却提升了 GSM8K，说明 contamination source（知识型 QA）向 math reasoning 的跨域 transfer 可能有不同机制。

- **[Ren et al., 2026]** *Rethinking Generalization in Reasoning SFT* (arXiv:2604.06628) — 反驳"SFT memorizes, RL generalizes"。发现跨域泛化是 **conditional** 的：(1) 存在 dip-and-recovery 模式（短训练低估泛化）；(2) 高质量 long-CoT 数据能产生跨域增益；(3) 更强的基座模型能从训练数据中提取可迁移的程序化模式。直接支持我们的发现——强基座（Qwen-7B）+ 高质量 MMLU SFT 数据可能激活了潜在数学能力。

- **[Huan et al., 2025]** *Does Math Reasoning Improve General LLM Capabilities?* (arXiv:2507.00432) — 评估 20+ reasoning-tuned 模型，发现 math SFT 模型通常**无法**迁移到其他领域（coding、agent planning），而 RL 可以。SFT 导致 representation drift。但注意方向相反：他们是 math→general，我们是 knowledge QA→math。

- **[Krishna et al., 2025]** *Latent Traits and Cross-Task Transfer: Deconstructing Dataset Interactions in LLM Fine-tuning* (arXiv:2509.13624) — 用 IRT-inspired 框架分析跨任务 transfer。发现性能改善往往**不能用表面数据集相似度解释**，隐藏的统计因子（类分布、生成长度倾向）和语言特征更有影响力。LoRA fine-tuning 可产生"反直觉的 transfer behavior"。

- **[Yang et al., 2024]** *Data Contamination Can Cross Language Barriers* (EMNLP 2024, arXiv:2406.13236) — 在翻译版 MMLU/ARC/MathQA 上做 continual pretraining，原始英文 benchmark 分数大幅提升。证明 **contamination effect 可以跨越语言边界**，暗示 contamination 学到的不仅是 surface form。

- **[Ott et al., 2024]** *Training on the Test Task Confounds Evaluation and Emergence* (arXiv:2407.07890) — 在 MMLU 和 GSM8K 上系统分析 "training on the test task" 效应。Fine-tuning on task-relevant data 后，新旧模型的 scaling trend 趋同，表面的模型间差异可能仅源于 test-task training 程度不同。

## 2. SFT as General Capability Enhancer

- **[Zhou et al., 2023]** *LIMA: Less Is More for Alignment* (NeurIPS 2023, arXiv:2305.11206) — 仅 1000 条精选数据的 SFT 即可产生强 generalization。提出 **Superficial Alignment Hypothesis (SAH)**：几乎所有知识在预训练中习得，SFT 仅教模型正确的输出格式和风格。对我们的发现有两面性：SAH 预测 MMLU SFT 教的是"答题格式"而非知识，但格式学习本身可能释放预训练中已有的数学推理能力。

- **[Gudibande et al., 2024]** *Revisiting the Superficial Alignment Hypothesis* (arXiv:2410.03717) — 部分挑战 SAH：对 math 和 multihop reasoning，少量样本仅做 stylistic alignment 不够，SFT 的真正价值在于让模型学会用新知识进行推理。暗示 MMLU SFT 可能不仅教格式，还增强了推理过程的 elicitation。

- **[Lu et al., 2024]** *Disperse-Then-Merge: Pushing the Limits of Instruction Tuning via Alignment Tax Reduction* (arXiv:2405.13432) — SFT 初期主要习得可泛化能力，后期开始过拟合数据偏差损害参数知识（alignment tax）。这解释了为什么适度 MMLU SFT（我们的 dosage 实验）可能在甜蜜点提升通用能力，而过量则退化。

- **[Ouyang et al., 2022; Bai et al., 2022]** Alignment tax 首次记录：RLHF 后 in-context learning 能力退化。后续研究表明 SFT 数据量增大时，知识和推理 benchmark 分数下降。但少量、高质量 SFT 可能处于 alignment tax 的正区间。

- **[Lin et al., 2025]** *Debunk the Myth of SFT Generalization* (arXiv:2510.00237) — 证明 SFT generalization 失败主要源于 frozen-prompt artifacts（固定 prompt 模板导致模型依附训练时语义）。引入 prompt diversity 后 SFT 可匹敌 RL 的泛化。我们的 MMLU SFT 包含多 subject、多格式数据，天然具备 prompt diversity。

## 3. Format vs Content Effect

- **[Spiesberger et al., 2026]** *Soft Contamination Means Benchmarks Test Shallow Generalization* (ICML 2026 submission, arXiv:2602.12413) — **核心论文**。发现：(1) semantic duplicates 与 exact duplicates 效果相同（均 ~20% 提升）；(2) contamination 提升不仅限于见过的题目，**同 benchmark 的未见题目也提升**（within-distribution generalization）；(3) 但**跨 benchmark 泛化未被证实**——作者称之为 "shallow generalization"。我们的 +11.07pp GSM8K 发现与此矛盾，因为 MMLU→GSM8K 是跨 benchmark、跨格式（MC→generation）、跨能力域（knowledge→math）。

- **[Dong et al., 2024]** *Generalization or Memorization: Data Contamination and Trustworthy Evaluation* (ACL 2024 Findings, arXiv:2402.15938) — 提出 CDD（通过 output distribution peakedness 检测 contamination）和 TED（修正 contamination 效果）。区分了 content memorization（记住答案）和 evaluation memorization（记住评分协议）。TED 可消除 66.9% 的 contamination-attributed 性能提升。

- **[Schaeffer et al., 2026]** *Quantifying the Effect of Test Set Contamination on Generative Evaluations* (arXiv:2601.04301) — 首次系统研究 contamination 对 **generative** evaluation（非 MC）的影响。在 MATH benchmark 上发现：contamination 效果与 model size 正相关，存在三种 memorization regime（受 solution length 和 sampling temperature 调节）。与我们的场景相关：GSM8K 是 generative task，MMLU 是 MC，格式完全不同。

- **[Song et al., 2026]** *Silicon Bureaucracy and AI Test-Oriented Education* (arXiv:2603.21636) — 提出 contamination sensitivity 审计框架。核心思想：如果 benchmark 被污染，在 problems 被删除/改写/扰动后性能应下降；否则说明能力是 genuine。可用于验证我们的 GSM8K 提升是否来自 genuine capability vs shallow transfer。

---

## Summary for Framing

基于文献，我们的 MMLU→GSM8K +11.07pp 发现是 **非平凡且文献中尚未充分记录的现象**。现有研究（Spiesberger et al., 2026）仅证实了 within-benchmark shallow generalization，而明确缺乏 cross-benchmark transfer 证据；Yao et al. (2026) 甚至发现 SFT 的 contamination effect 仅限于被污染任务本身。我们的发现超越了这两个结论。

最可能的解释框架是 **"SFT as capability elicitor" + Superficial Alignment Hypothesis 的扩展**：MMLU contamination SFT 不是让模型"记住 MMLU 答案"（content effect），而是通过多学科 QA 训练教会模型一种结构化推理和回答的模式（format/process effect），这种模式释放了预训练中已有但未被充分 elicit 的数学推理能力。支撑证据：(1) MMLU 和 GSM8K 格式完全不同（MC vs generation），排除 format memorization；(2) Ren et al. (2026) 证明强基座模型能从 SFT 中提取可迁移的程序化模式；(3) LIMA 的 SAH 表明 SFT 的核心作用是 capability elicitation 而非 knowledge injection。

这一发现对 contamination 检测和 benchmark integrity 有重要启示：即使模型未接触某 benchmark 的任何数据，contamination SFT 仍可能通过 capability elicitation 间接膨胀该 benchmark 的分数，使传统的基于数据重叠的检测方法失效。
