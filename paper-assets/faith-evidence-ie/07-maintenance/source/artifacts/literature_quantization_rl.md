# Quantization-RL Interaction Literature Survey

调研日期：2026-05-15
背景：GRPO 在 structured IE 任务上，QLoRA 4-bit 导致 catastrophic forgetting（rel_f1 0.4057→0.2167），bf16 LoRA 完全正常（rel_f1=0.4549）

---

## 1. Quantization + RL Training

### 1.1 The Impact of Quantization on Large Reasoning Model Reinforcement Learning
- Kumar, Xu, Wang & Webb (2025) — **NeurIPS 2025**
- Key finding: 系统性实验发现 quantization-aware RL training (QAFT) 负面影响学习过程——quantized models produce worse policies。相比之下，先 RL 训练再 PTQ/QLoRA 量化的效果更好。量化引入的 "sudden shock" 在 RL 过程中尤其有害。
- Relevance: **直接支撑我们的发现**——4-bit quantization 在 RL training 阶段（而非推理阶段）引入的噪声破坏 policy learning。我们的 QLoRA+GRPO 正是在训练阶段量化。
- URL: https://arxiv.org/abs/2511.15694

### 1.2 QuRL: Efficient Reinforcement Learning with Quantized Rollout
- (2026) — **ICLR 2026**
- Key finding: INT8 quantization during RL rollout 导致 4% accuracy degradation vs bf16 baseline。关键发现：RL steps 之间的 weight update 极小（"extremely small"），quantization noise 淹没了这些微小更新。提出 Adaptive Clipping Range (ACR) 将 INT8 gap 缩至 2%，FP8 缩至 ~1%。
- Relevance: **核心机制解释**——RL 训练的 weight update 幅度远小于 SFT，而 4-bit quantization noise 远大于 INT8。这解释了为什么 QLoRA 在 SFT 阶段表现正常但在 GRPO 阶段 catastrophic——RL 的微小梯度信号被 4-bit 噪声完全淹没。
- URL: https://arxiv.org/abs/2602.13953

### 1.3 QeRL: Beyond Efficiency — Quantization-enhanced Reinforcement Learning for LLMs
- Huang et al. (2025) — arXiv
- Key finding: Quantization noise 增加 policy entropy，增强 exploration。通过 Adaptive Quantization Noise (AQN) 机制动态调整噪声，NVFP4+LoRA 实现比 16-bit LoRA 和 QLoRA 更快的 reward growth。7B 模型在 GSM8K 达 90.8%。
- Relevance: 表明 quantization noise 如果被适当控制可以有益（类似 exploration noise），但 **未控制的噪声导致不稳定**。标准 QLoRA 没有 AQN 机制，噪声是 uncontrolled 的。
- URL: https://arxiv.org/abs/2510.11696

### 1.4 FP4 All the Way: Fully Quantized Training of LLMs
- (2025) — arXiv
- Key finding: 提出理论临界点——**当 gradient standard deviation < √3 × quantization noise 时，quantized training 停滞**。Stochastic rounding 对低精度训练稳定性至关重要。
- Relevance: **理论基础**——4-bit NF4 的 quantization noise 量级远大于 8-bit 或 bf16。RL training 产生的 gradient signal 本身就比 SFT 弱（因为 reward-based 而非 direct supervision），更容易跌破 √3 阈值。
- URL: https://arxiv.org/abs/2505.19115

### 1.5 Training Dynamics Impact Post-Training Quantization Robustness
- (2025) — **ICLR 2026**
- Key finding: 量化误差由 learning rate 和训练超参数的复杂交互驱动。LR decay 后，validation loss 和 quantization error 出现 divergence。
- Relevance: RL training 的 learning dynamics（reward signal 变化、policy ratio clipping）与 SFT 显著不同，这种不同的 training dynamics 可能导致模型进入 quantization-sensitive 区域。
- URL: https://arxiv.org/abs/2510.06213

---

## 2. GRPO Stability / Failure Modes

### 2.1 GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control
- (2025) — arXiv
- Key finding: 识别 GRPO 两个核心失败模式：(i) **token-level penalization**——不同 response 中共享的 valuable tokens 收到矛盾梯度信号；(ii) **policy collapse**——负 reward 的 completions 惩罚 confident responses，将决策推向 unlikely tokens。GTPO 通过跳过负更新、放大正更新解决，在 OOD benchmark 上比 GRPO 高 75pp (Pass@64)。
- Relevance: **高度相关**——structured IE 中 relation tokens 和 evidence tokens 可能共享底层 representation。GRPO 的 token-level penalization 机制可能导致这些共享 tokens 收到矛盾信号，造成 relation 和 evidence extraction 的 decoupling。4-bit 噪声会放大这种矛盾。
- URL: https://arxiv.org/abs/2508.03772

### 2.2 DAPO: An Open-Source LLM Reinforcement Learning System at Scale
- ByteDance Seed (2025) — arXiv
- Key finding: Naive GRPO 训练中观察到 **entropy collapse**——policy entropy 快速下降。提出 Clip-Higher（解耦上下 clip range 给低概率 token 更多空间）+ Dynamic Sampling（过滤 uniform reward 样本确保每个 batch 有有效梯度）。Qwen2.5-32B 在 AIME 2024 达 50 分，超 DeepSeek-R1-Zero。
- Relevance: Entropy collapse 在 structured output 任务上可能更严重——IE 任务的 valid output space 高度受限（JSON schema），GRPO 容易在这种约束空间中快速 collapse。QLoRA 的噪声可能加速或异常化这个 collapse 过程。
- URL: https://arxiv.org/abs/2503.14476

### 2.3 Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training
- (2025) — arXiv
- Key finding: On-policy GRPO 不带 masking 收敛到 Pass@1=45% 但 **不稳定**。Zero-variance masking（过滤所有 response 同 reward 的 group）可稳定训练并提升至 50%。Off-policy GRPO 通过 clipped surrogate objective 匹配或超越 on-policy。
- Relevance: Zero-variance groups 在 structured IE 中很常见——当所有 sampled response 都提取到相同的 relation set 时（正确或错误），group 内 variance=0，GRPO 完全无法学习。QLoRA 的噪声可能同时影响 sampling diversity。
- URL: https://arxiv.org/abs/2505.22257

### 2.4 MO-GRPO: Mitigating Reward Hacking of GRPO on Multi-Objective Problems
- (2025) — arXiv
- Key finding: GRPO 在 multi-objective 问题上容易 reward hacking——agent overfits misspecified reward。
- Relevance: 我们的 IE 任务本质是 multi-objective（relation extraction + evidence extraction），GRPO 可能优化一个目标而牺牲另一个，这与我们观察到的 "evidence 与 relation decouple" 现象一致。
- URL: https://arxiv.org/abs/2509.22047

---

## 3. LoRA Precision Effects

### 3.1 Balancing Fidelity and Plasticity: Aligning Mixed-Precision Fine-Tuning with Linguistic Hierarchies
- (2025) — arXiv
- Key finding: 提出 **Fidelity-Plasticity Trade-off**——一个 layer 的适应能力（Plasticity）受限于其 frozen weights 的信息容量（Fidelity）。**对语义关键层的激进量化产生不可恢复的信息瓶颈**，无论 adapter rank 多高都无法补偿。提出 QR-Adaptor 联合优化 per-layer bit-width 和 LoRA rank。
- Relevance: **直接解释性**——4-bit 量化可能在 structured reasoning 最关键的中间层造成信息瓶颈。Evidence extraction 需要的细粒度语义理解（哪些 span 支持哪些 relation）需要高 Fidelity 的表示，4-bit 无法提供。
- URL: https://arxiv.org/abs/2505.03802

### 3.2 A Deep Dive into the Trade-Offs of Parameter-Efficient Preference Alignment Techniques
- IBM Research (2024) — **ACL 2024**
- Key finding: 300+ 实验横跨 SFT 和 DPO、LoRA 和 QLoRA、多个模型。发现 QLoRA 的 learning pattern 与 full fine-tuning **本质不同**（不仅是量上接近，模式也不同）。Alignment 对 data quality、method 和 adapter rank 高度敏感。
- Relevance: 如果 QLoRA 在 DPO 上就已经表现出不同的 learning pattern，那在更复杂的 GRPO 上这种差异可能更大。
- URL: https://arxiv.org/abs/2406.04879

### 3.3 Revealing Modular Gradient Noise Imbalance in LLMs
- (2026) — arXiv
- Key finding: LLM 不同模块存在 gradient scale mismatch，Adam 的 adaptivity 无法完全修正，导致收敛慢或训练不稳定。提出 MoLS（Module-wise Learning-rate Scaling）。
- Relevance: 4-bit quantization noise 会放大模块间的 gradient 不平衡——quantization noise 在不同层的影响不均匀，进一步加剧 gradient scale mismatch。
- URL: https://arxiv.org/abs/2605.05794 [UNVERIFIED - 2026年5月，可能尚未公开]

### 3.4 CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization
- (2025) — arXiv
- Key finding: QLoRA 的性能差距部分源于 suboptimal initialization——quantized weights 的误差影响 LoRA 的起始点。Calibrated initialization 使 INT2 CLoQ 在 Llama2-13B 上超越 INT4 QLoRA 在 arithmetic reasoning 上的表现。
- Relevance: QLoRA 的 initialization 问题在 RL 训练中可能被放大——RL 对 policy 的初始状态比 SFT 更敏感。
- URL: https://arxiv.org/abs/2501.18475

---

## 4. Catastrophic Forgetting in RLHF

### 4.1 Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)
- Sabbaghi, Pappas, Javanmard & Hassani (2026) — arXiv
- Key finding: Standard RLHF 找到的 high-reward policies 位于 **loss landscape 的 sharp regions**——小扰动就导致 reward 急剧下降。FRPO 在 KL-bounded 邻域内优化 reward flatness，找到对 downstream fine-tuning robust 的 policy。
- Relevance: **关键洞察**——QLoRA 的 4-bit 量化噪声本质上就是对 weights 的持续小扰动。如果 GRPO 将 policy 推向 sharp region，这些持续的量化扰动就会不断将 policy 推离高 reward 区域，导致 catastrophic forgetting。bf16 没有这种噪声所以稳定。
- URL: https://arxiv.org/abs/2602.08813

### 4.2 Mitigating the Alignment Tax of RLHF
- Lin, Tan et al. (2023/2024) — **EMNLP 2024**
- Key finding: RLHF alignment 导致 pre-training 能力退化（"alignment tax"）——包括 translation、reasoning、reading comprehension。Model averaging（插值 pre/post RLHF 权重）达到最优 alignment-forgetting Pareto front。**不同层对 alignment tax 的敏感度不同**。
- Relevance: Layer-wise sensitivity + quantization = 问题叠加。某些层既对 alignment forgetting 敏感，又被 4-bit 量化严重影响，double hit。
- URL: https://arxiv.org/abs/2309.06256

### 4.3 Mechanistic Analysis of Catastrophic Forgetting in LLMs During Continual Fine-tuning
- (2026) — arXiv
- Key finding: 识别三个遗忘机制：(i) 低层 attention weights 的 **gradient interference**（15-23% attention heads 严重受损）；(ii) 中间层的 **representational drift**（CKA 相似度下降 0.32-0.47）；(iii) **loss landscape flattening**。梯度对齐程度可预测遗忘严重性。
- Relevance: 4-bit quantization noise 在低层引入额外的 gradient interference，在中间层加速 representational drift。这两个机制可能是 QLoRA+GRPO forgetting 的直接驱动力。
- URL: https://arxiv.org/abs/2601.18699

### 4.4 RL Minimizes Catastrophic Forgetting vs SFT
- MIT (2025)
- Key finding: On-policy RL 天然比 SFT 更少遗忘，KL divergence 是遗忘严重性的预测指标。
- Relevance: **反面证据/重要限定**——这个结论基于 full-precision RL。QLoRA 的 4-bit 噪声可能破坏了 RL 的这种天然优势，使得 quantized RL 反而比 SFT 遗忘更严重。这正是我们观察到的现象。
- URL: https://www.marktechpost.com/2025/09/08/a-new-mit-study-shows-reinforcement-learning-minimizes-catastrophic-forgetting-compared-to-supervised-fine-tuning/ [UNVERIFIED - 来源为科技新闻报道]

### 4.5 Policy Gradient with Adaptive Entropy Annealing for Continual Fine-Tuning
- Zhang et al. (2026) — arXiv
- Key finding: 低 entropy 增强适应能力但增加遗忘风险。Adaptive entropy annealing 从 exploration（高 entropy）渐进到 exploitation（低 entropy），平衡 plasticity 和 stability。
- Relevance: QLoRA 的量化噪声干扰了 entropy 的自然演化——可能导致 entropy 异常波动而非平稳下降，打破 plasticity-stability 平衡。
- URL: https://arxiv.org/abs/2602.14078

---

## Summary

### 我们的发现在文献中是否有先例？

**部分有先例，但具体组合是新的。**

- **Quantization 损害 RL training 已有报告**：Kumar et al. (NeurIPS 2025) 发现 quantization-aware RL 产生更差的 policy；QuRL (ICLR 2026) 发现 INT8 就有 4% degradation；FP4 论文给出理论阈值（gradient < √3 × noise → 停滞）
- **GRPO 的稳定性问题已被广泛研究**：GTPO、DAPO、Revisiting GRPO 等多篇论文识别了 entropy collapse、token-level gradient conflict、zero-variance stalling
- **LoRA 精度影响学习模式已有发现**：Fidelity-Plasticity trade-off、IBM 300+ 实验、CLoQ 都表明 QLoRA 的 learning pattern 与 full fine-tuning 本质不同
- **RL 中的 catastrophic forgetting 已有研究**：FRPO 发现 sharp reward regions、alignment tax 论文发现 layer-wise sensitivity

**但：QLoRA 4-bit 在 GRPO 训练中导致 structured output 的 subtask decoupling（relation 与 evidence extraction 分离）这个具体现象，文献中没有直接先例。**

### 最接近的相关工作

1. **QuRL (ICLR 2026)**——最接近，但研究的是 INT8 rollout quantization 而非 4-bit training quantization，且任务是 math reasoning 而非 structured IE
2. **Kumar et al. (NeurIPS 2025)**——直接研究 quantization + RL，但未涉及 structured output 或 subtask decoupling
3. **GTPO (2025)**——识别了 GRPO 的 token-level gradient conflict，这是 decoupling 的潜在机制，但未与 quantization 关联
4. **Fidelity-Plasticity (2025)**——理论上解释了为什么 4-bit 在某些层造成不可恢复的瓶颈，但未在 RL 场景验证

### 我们的 Unique Contribution

1. **首次报告 QLoRA 4-bit + GRPO 在 structured IE 上的 catastrophic decoupling**——不仅是整体性能下降，而是 subtasks 之间的 coupling 被破坏（evidence extraction 与 relation extraction 分离）
2. **提供 quantization-precision 消融**——同一任务、同一 GRPO 配置下，4-bit vs bf16 的直接对比，干净地隔离了 quantization 的影响
3. **Structured output 场景的独特视角**——现有 quantization+RL 研究全部集中在 math reasoning（单一正确答案），structured IE 的 multi-component output（relation + evidence + faithfulness）更脆弱
4. **机制假说**——结合 QuRL 的 "微小 weight update 被噪声淹没" + GTPO 的 "token-level gradient conflict" + Fidelity-Plasticity 的 "信息瓶颈"，提出连贯解释框架：4-bit 噪声放大 GRPO 的 gradient conflict，在需要 multi-component coordination 的 structured IE 中首先破坏最脆弱的 coupling（evidence↔relation）

### Claim 2 Reframing 建议

原始 Claim 2 可 reframe 为：
> "Quantization precision is a critical but overlooked factor in RL-based IE training: 4-bit QLoRA introduces quantization noise that overwhelms GRPO's fine-grained gradient signals, causing catastrophic decoupling of structured subtasks — a failure mode absent in bf16 training and not predicted by QLoRA's strong SFT performance."

支撑论据链：
- QLoRA 在 SFT 阶段表现正常（consistent with Dettmers et al. 2023）
- RL weight updates 远小于 SFT（QuRL, ICLR 2026）
- 4-bit noise > √3 × RL gradient signal → training stagnation（FP4 theory）
- GRPO 的 token-level gradient conflict 被噪声放大（GTPO analysis）
- 结果是 subtask decoupling 而非整体退化（our unique finding）
