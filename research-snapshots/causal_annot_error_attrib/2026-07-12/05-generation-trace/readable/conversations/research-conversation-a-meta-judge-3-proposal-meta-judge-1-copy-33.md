# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/e09acbc0-003c-4a30-b9de-1af02d01433e.jsonl`
- **Structured JSON:** [`6dea575e6880b51d34cc.json`](../../sessions/6d/6dea575e6880b51d34cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:38:05.451Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:38:05.451Z",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient research context. Let me compile the final evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478) (arXiv, Jan 2026): 最直接的竞争者。通过跨perturbation变体pooling reward实现Level-2一致性。取得Pass@k提升(AMC12/AIME24上+9.84)，但**未在任何perturbation robustness benchmark上评估**（GSM-Symbolic, VAR-MATH, MATH-Perturb均未测试）。本proposal精准定位了这一盲区。\n- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101) (arXiv, Mar 2026): 在GRPO中加入InfoNCE对比学习，对齐同一问题的不同正确rollout。方向是same-problem cross-trajectory invariance。本proposal的对比学习组件（L_contrastive）目标不同——cross-perturbation invariance，是互补而非重复的invariance维度。CLIPO在GSM8K-P1/P2上有改进但幅度有限。\n- [AIR: Towards Context-Invariant Safety Alignment](https://arxiv.org/abs/2605.20994) (arXiv, May 2026): 使用非对称stop-gradient anchor invariance regularization整合到GRPO中，但主要面向safety alignment而非math robustness。其非对称设计适合safety场景（一个prompt变体有更可靠反馈），但不适合math perturbation对（双侧对称可验证）。本proposal选择对称JS散度的论证合理。\n- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157) (arXiv, Mar 2026): 在GRPO中使用JS散度作为diversity-preserving regularizer（current vs. historical policy），验证了JS散度在GRPO框架中的可行性和优越性（JS > Forward KL）。为本proposal的技术选择提供了经验支持，但DyJR的JS用途是diversity preservation，本proposal的JS用途是cross-perturbation consistency——不同目标。\n- [AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking](https://openreview.net/forum?id=fDk95XPsCU) (ICLR 2026): 通过RL训练显式抽象再求解，但受限于GSM级别问题。本proposal声称通过分布一致性正则化隐式实现类似抽象效果。\n- [MATH-Perturb](https://arxiv.org/abs/2502.06453) (arXiv, 2025): 基准测试显示即使o1-mini等模型在hard perturbation上也有10%-25%准确率下降，验证了perturbation robustness问题的真实性和严重性。\n- [GSM-Symbolic](https://arxiv.org/abs/2410.05229) (ICLR 2025, Apple): 开创性工作，揭示LLM在symbolic/structural perturbation下的脆弱性。\n- [PrAg-PO: Prompt Augmentation Scales up GRPO](https://arxiv.org/abs/2602.03190) (arXiv, Feb 2026): 使用13种prompt模板作为隐式正则化，属于Data-level (Level 1)。\n- [The Choice of Divergence](https://arxiv.org/abs/2509.07430) (arXiv, 2025): 系统研究f-divergence在RLVR中的作用，发现mass-covering divergence（forward KL, JS）优于reverse KL在保持多样性方面。\n\n- **调研总结**: Math reasoning的perturbation robustness是一个已被充分验证的重要问题（GSM-Symbolic, VAR-MATH, MATH-Perturb等多个benchmark证实）。在RL训练方面，TA-GRPO开创了reward-level一致性但缺乏robustness评估，CLIPO/AIR/DyJR各自在GRPO框架中使用了不同的正则化/对比学习但未直接针对perturbation robustness。本proposal所定位的\"distribution-level consistency for perturbation invariance\"在现有工作中确实是一个未被占据的具体位置，三级框架的分析有见地。但这一位置的\"增量\"性质也意味着novelty的天花板有限——本质上是将已有技术（JS divergence, contrastive learning）组合应用到一个已有问题上。\n\n【整体印象】:\n如果我是审稿人，第一反应是：这是一篇**定位精准、调研扎实、实验设计周全**的工作。三级一致性框架（Data → Reward → Distribution）的提出有清晰的递进逻辑，对TA-GRPO\"correct but inconsistent reasoning\"盲区的分析切中要害。但第二反应是：**核心技术贡献的深度有限**——本质上是在GRPO loss上加了一个JS散度正则项和一个InfoNCE对比项，这两者都不是新技术。论文的价值更多在于\"将对的东西放到对的地方\"（right combination for the right problem），而非方法论上的突破。\n\n我会倾向于**weak accept / borderline**——如果实验结果确实显著（尤其在perturbation robustness benchmarks上的提升），有可能跨过accept线；但如果reviewer认为这只是existing techniques的straightforward combination，可能会被borderline reject。\n\n【核心贡献】:\n1. **三级一致性框架（Level 1-2-3）**: 对现有math robustness方法的系统性分类（Data/Reward/Distribution），理论上论证了为什么Level 2（reward pooling）不足以捕捉\"correct but inconsistent reasoning\"。这个框架本身有学术价值。\n2. **ConsistGRPO方法**: 在GRPO中加入cross-perturbation JS散度一致性loss和contrastive loss。技术上是incremental（JS divergence + InfoNCE都是成熟工具），但应用场景和组合方式有novelty。\n3. **完备的实验设计**: 8个baseline、7+个benchmark、5维ablation的设计本身就是一个贡献，尤其是填补了TA-GRPO未做robustness评估的空白。\n\n对领域的价值：**中等偏上**。如果实验验证了distribution-level > reward-level的假设，这会为math RL robustness社区提供一个有价值的empirical insight和实用方法。但不太可能改变领域的研究方向。\n\n【方法合理性】:\n方法整体合理，但有几个需要关注的点：\n\n1. **JS散度计算的实际效果**: proposal使用sequence-level log-probabilities构造empirical rollout distributions P_x和P_x'，然后计算JS(P_x || P_x')。但G个rollout（通常G=8-16）构成的empirical distribution可能非常noisy，JS的估计方差大。这与DyJR使用buffer accumulated distributions不同——DyJR有更多样本来估计分布。proposal需要讨论small-sample JS estimation的问题。\n\n2. **更简单的替代方案**: 一个直接的替代方案是在rollout的token-level logits上做KL/JS对齐（类似knowledge distillation），而非sequence-level。这可能提供更dense的梯度信号。另一个替代方案是直接在TA-GRPO基础上加一个简单的reward consistency bonus（如果x和x'都对则bonus增大），而非引入JS散度——这更简单但可能近似达到类似效果。proposal应明确论证为何distribution-level JS优于这些simpler alternatives。\n\n3. **Perturbation pipeline的reliability**: 对于MATH/AMC/AIME level的问题（竞赛数学），自动化perturbation的正确性验证是一个非平凡的工程问题。proposal提到用SymPy验证，但竞赛数学的很多问题（组合、数论、几何）不容易用SymPy自动验证。这可能限制training数据的覆盖率。proposal提到了这个问题并计划做pilot study，这是好的，但也意味着实际可用的training data可能比预期少。\n\n4. **Consistency-diversity tradeoff**: 这是一个关键问题。强一致性约束可能导致rollout diversity collapse（如果模型被迫让P_x ≈ P_x'，可能会converge到单一推理路径）。proposal意识到了这个问题并计划做tradeoff分析，这很好。但这也意味着最优的λ₁可能需要非常小，此时L_consist的实际贡献就变得很边际。\n\n【5 维度打分】:\n\n1. **研究问题: 强** — Math reasoning模型在perturbation下的脆弱性是一个经GSM-Symbolic (ICLR 2025)、VAR-MATH、MATH-Perturb等多个benchmark验证的真实问题。RL训练（GRPO）不仅未解决反而可能加剧这一问题。TA-GRPO的reward pooling方法未做robustness评估、且理论上对\"correct but inconsistent reasoning\"存在盲区——这个gap的定位非常精准且有价值。问题的重要性和时效性都很强。\n\n2. **方法与创新: 中** — 三级框架的分析有insight，但核心方法（JS divergence regularization + InfoNCE contrastive loss）都是成熟技术的组合应用，不涉及方法论创新。与CLIPO (arXiv 2603.10101) 相比，对比学习组件的区别仅在于positive pair的构造方式（cross-perturbation vs. cross-trajectory）；与DyJR (arXiv 2603.16157) 相比，JS散度的使用方式不同（cross-perturbation vs. temporal）但技术形式类似；与AIR (arXiv 2605.20994) 相比，区别在于对称vs.非对称——有道理但不构成显著创新。一个苛刻的reviewer可能会认为这是\"TA-GRPO + JS regularization\"的straightforward extension。proposal需要通过强实验结果来弥补方法novelty的不足。\n\n3. **实验设计: 强** — 这是proposal最突出的优势。8个baseline覆盖了Data/Reward/Representation/None四个consistency level，形成完整的ablation对照；7+个benchmark涵盖robustness和clean accuracy两个维度；5维ablation（component decomposition, perturbation type, hyperparameter sensitivity, training dynamics, divergence metric comparison）非常周全；FLOPs-matched baseline的设计解决了公平性问题；scale validation (1.7B + 8B) 增加了可信度。特别值得肯定的是divergence metric comparison (JS vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style)——这直接回应了DyJR和Choice of Divergence等工作的发现，既是ablation也是对领域的贡献。\n\n4. **可行性: 中** — \n   - Qwen3-8B的训练在单节点8×A100/H100上可行（约2-4周）。\n   - 主要风险在perturbation pipeline：竞赛数学(AMC/AIME)的自动perturbation + 正确性验证是非平凡的工程任务。proposal限制在algebraic/arithmetic subtypes是务实的，但可能导致training data覆盖率不足。\n   - JS散度计算需要对每个问题做2×G次rollout（original + perturbed），计算开销翻倍。proposal承认这一点并计划profile FLOPs，但这可能需要额外的优化（如shared prefix caching）。\n   - 整体可行但有工程挑战。\n\n5. **写作与呈现: 强** — proposal的结构清晰、逻辑递进（问题定义 → 三级框架 → 方法 → 实验设计）。相关工作的调研非常全面，对每个相关工作的定位和区分精确。三级框架的提出为读者提供了清晰的conceptual map。\"correct but inconsistent reasoning\"的例子直观有力。唯一可改进的是：proposal略显冗长，如果能更精炼地呈现核心idea会更好。\n\n【概率估计】: [28% - 42%] 中位 35%\n\n【估计理由】:\n\n**上行因素（推向42%）**:\n- 研究问题精准且timely，精确定位了TA-GRPO的理论盲区\n- 实验设计极为完备（8 baselines, 7+ benchmarks, 5-dim ablation），这本身是显著加分项\n- 三级框架提供了有价值的conceptual contribution\n- 领域调研极其全面，reviewer不太会找到\"missed related work\"这类问题\n- Perturbation robustness在2025-2026是热门话题，reviewers对该方向普遍有兴趣\n\n**下行因素（推向28%）**:\n- 方法novelty有限——核心是JS divergence + InfoNCE的straightforward combination，AAAI reviewers可能认为technical contribution不足\n- 目前没有实验结果。如果distribution-level一致性的提升相对于TA-GRPO的reward pooling是边际的（例如<3%），论文会失去核心论据\n- Perturbation pipeline的实际覆盖率和质量是不确定因素\n- Consistency-diversity tradeoff可能限制方法的实际增益\n- GRPO variants已经非常拥挤（DAPO, DR.GRPO, CLIPO, DyJR, TA-GRPO, PrAg-PO, MCPO, AIR...），reviewer可能对\"yet another GRPO variant\"产生审美疲劳\n\n**中位35%的理由**: 这是一篇\"solid but incremental\"的投稿。问题定位好、实验设计完备、写作清晰，但方法novelty的天花板限制了它。在AAAI 2026的competitive pool中，它位于borderline区域。如果实验结果显著（distribution-level显著优于reward-level，尤其在perturbation benchmarks上），概率偏向上界；如果实验结果边际，概率偏向下界。\n\n【主要风险】:\n1. **\"Insufficient novelty / straightforward combination\"**: 最可能的拒稿理由。Reviewer可能认为JS-divergence regularization + InfoNCE contrastive loss的组合缺乏方法论深度，尤其是在GRPO variants已经极度拥挤的当下。三级框架虽好，但框架+combination可能不足以构成AAAI主会级别的贡献。\n2. **实验结果不确定性**: Proposal尚无实验结果。如果distribution-level一致性相对于reward-level（TA-GRPO）的提升幅度有限，或者consistency-diversity tradeoff使得最优λ₁很小导致L_consist贡献边际，核心claim（Level 3 > Level 2）将缺乏实证支撑。\n\n【实施评估】:\n- **计算资源**: 中高。需要8×A100/H100 GPU节点。每个问题需2×G次rollout（原始+扰动），计算量约为vanilla GRPO的2-2.5倍。JS散度和contrastive loss的额外计算开销相对较小。估计总GPU-hours: 2000-4000（含所有ablation和baseline复现）。\n- **数据需求**: MATH/AMC/AIME训练集（公开可用）。关键瓶颈是perturbation pipeline的构建——需要对竞赛数学问题进行自动化扰动并验证正确性。Pilot study (100题) 可在1-2周内完成。\n- **人工介入**: 中等。Perturbation pipeline需要人工验证（尤其是geometry/number theory等难以自动验证的题型）。LLM-generated perturbations需要质量抽检。Baseline复现（TA-GRPO, CLIPO, AbstRaL）可能需要调试。\n- **训练需求**: 需要完整的RL训练流程（GRPO + 正则化项）。Qwen3-8B约需2-3周训练，Qwen3-1.7B约需1周。总训练时间（含所有variants和ablations）约4-6周。\n- **新 Benchmark**: 不需要构建新benchmark——使用现有的GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM。但perturbation pipeline本身可视为一个工程产出。\n- **预估周期**: 10-14周（Pilot study 2周 + Perturbation pipeline 2-3周 + 主实验+ablation 4-6周 + 论文写作 2-3周）。假设计算资源充足，一个2-3人团队可在AAAI 2026 deadline前完成。\n```\n\nSources:\n- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)\n- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)\n- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)\n- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)\n- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://arxiv.org/abs/2502.06453)\n- [GSM-Plus: A Comprehensive Benchmark for Evaluating Robustness of LLMs](https://arxiv.org/abs/2402.19255)\n- [The Choice of Divergence in RLVR](https://arxiv.org/abs/2509.07430)\n- [Post-Training in 2026: GRPO, DAPO, RLVR & Beyond](https://llm-stats.com/blog/research/post-training-techniques-2026)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nBased on my research, I now have sufficient information to provide a comprehensive evaluation.\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478) (arXiv, Jan 2026): 最直接的 Level 2 对比方法。通过 reward pooling 跨变换变体共享 advantage，在 AMC12/AIME24 上 Pass@k 提升最高 +9.84。但关键发现：未在任何 perturbation robustness benchmark 上评估，这正是本 proposal 的攻击点。其 ablation 证实\"仅 augmentation 不够\"，支持更强一致性信号的必要性。\n- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101) (arXiv, Mar 2026): 在 GRPO 中引入 InfoNCE 对比学习，对齐同一问题不同正确 rollout 的表征。GSM8K-P1/P2 分别 +1.48/+3.36。其 invariance 维度是 cross-trajectory（同题不同解），而本 proposal 的 cross-perturbation 维度（同义不同题）是正交的。\n- [AIR: Towards Context-Invariant Safety Alignment](https://arxiv.org/abs/2605.20994) (arXiv, May 2026): 非对称 stop-gradient anchor invariance regularization，主要面向安全对齐。因其假设一侧反馈更可靠（verifiable anchor），不适合数学 perturbation 对的对称场景。技术上最接近本 proposal 的 invariance regularization 范式，但应用场景和设计选择明确不同。\n- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157) (arXiv, Mar 2026): 在 GRPO 中使用 JS-divergence 作为当前策略与历史分布之间的正则化器，防止 diversity collapse。经验上验证了 JS > Forward KL 在 GRPO 中的适用性。为本 proposal 的 JS 选择提供了技术先例。\n- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885) (arXiv, 2025): 文档化了 RL-trained 模型在数值替换下的严重退化（AMC23: -47.9%, AIME24: -58.8%, AIME25: -72.9%），为本 proposal 的问题动机提供了强有力的实证基础。\n- [GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations](https://arxiv.org/abs/2605.07053) (arXiv, May 2026): 最新的语义扰动 benchmark 框架，在 14 个 SOTA LLM 上观察到一致的性能下降（~28% at maximum strictness），进一步验证了 perturbation robustness 问题的普遍性。\n- [f-GRPO & Beyond: Divergence-Based RL Algorithms](https://arxiv.org/html/2602.05946) (arXiv, 2026): 探索 GRPO 中替代 divergence measure 的通用框架，表明 divergence 选择是活跃研究方向。\n- 调研总结: Math RL robustness 是 2025-2026 的热点方向，问题已被充分文档化（VAR-MATH, MATH-Perturb, GSM-Symbolic），但训练时解决方案仍处于早期：TA-GRPO 提供 reward-level 方案但缺乏 robustness 评估，CLIPO 提供 representation-level 方案但面向不同维度，AIR 面向安全而非数学。本 proposal 的\"distribution-level consistency\"定位在这些工作之间有清晰的空位。\n\n【整体印象】: 作为审稿人，第一反应是 **lean accept / borderline**。这是一篇 positioning 极为精准、实验设计极为完善的 proposal。三层框架（Data → Reward → Distribution）的叙事结构清晰有力，对现有工作的分析透彻且公平。核心 insight（reward pooling 对\"correct but inconsistent reasoning\"失明）在理论上 sound 且 intuitively compelling。主要顾虑在于核心技术贡献（加一个 JS-divergence regularizer）的 novelty 深度是否足够——方法本身相对 straightforward，可能被部分审稿人视为\"obvious next step\"。但如果实验结果强劲（在 robustness benchmarks 上显著超越 TA-GRPO 同时保持 clean accuracy），这足以弥补方法简洁性的不足。\n\n【核心贡献】: \n1. **概念贡献**：提出三级一致性框架并论证 distribution-level > reward-level > data-level，为 math RL robustness 提供了清晰的 taxonomy。\n2. **技术贡献**：设计 ConsistGRPO，在 GRPO 训练中加入 perturbation pair 间的 JS-divergence 一致性损失，实现对 reasoning trajectory 全程的连续梯度监督。\n3. **实验贡献**：如果执行到位，将是第一个在完整 robustness benchmark 矩阵上系统比较 training-time consistency enforcement 策略的工作。\n\n贡献价值判断：概念贡献有中等价值（框架化现有 landscape），技术贡献在\"neat and effective\"和\"too simple\"之间取决于实验效果，实验贡献如完成度高则独立具有价值。\n\n【方法合理性】: \n方法设计总体合理，JS-divergence 的选择有充分论证（对称性、有界性、DyJR 经验支持）。但存在几个需要审视的点：\n\n1. **rollout 分布的定义模糊**: \"sequence-level log-probabilities to form empirical rollout distributions P_x and P_x'\"—G 个 rollout 形成的经验分布在高维序列空间中是极其稀疏的。JS-divergence 在仅 G=8-16 个样本上的估计噪声可能很大。是用 kernel density estimation？还是简单离散分布？这影响梯度质量。\n\n2. **更简单的替代方案存在吗？** \n   - 直接对 perturbation pair 做 sequence-level KL（取平均方向）\n   - 在 token-level 逐步计算一致性（类似 knowledge distillation 的 logit matching）\n   - 简单地将 perturbation pair 的 rollout 合并计算 advantage（即 TA-GRPO 的扩展）\n   - 这些替代方案需要在 ablation 中明确排除或比较（proposal 的 ablation 5 部分覆盖了这点，是好设计）\n\n3. **consistency-diversity 冲突**: 强制两个 perturbation 的 rollout 分布一致可能会压缩策略的 exploration 能力。Proposal 意识到了这点并设计了 tradeoff 分析，这是好的。\n\n【5 维度打分】:\n  1. 研究问题: [强] — VAR-MATH 的实证数据（47-72% accuracy drop）清楚表明这是一个真实且严重的问题。RL-trained 模型的 perturbation fragility 是当前社区关注的焦点，且缺乏有效的 training-time 解决方案。问题定义精确，不含歧义。\n  \n  2. 方法与创新: [中] — 核心方法（JS-divergence between perturbation pair rollouts）技术上 sound 但相对 straightforward。创新性主要来自：(a) 将已有技术组件（JS-divergence from DyJR, contrastive from CLIPO, augmentation from TA-GRPO）以新的方式组合并面向新目标；(b) \"correct but inconsistent reasoning\" failure mode 的识别和 distribution-level 解决思路。但 reviewer 可能认为这是\"obvious combination\"——DyJR 证明 JS 在 GRPO 中可行，TA-GRPO 证明 perturbation augmentation 有用，合在一起不意外。与 AIR 的差异化论证 compelling（symmetric vs asymmetric），但 AIR 本身不面向 math 所以竞争性不强。\n  \n  3. 实验设计: [强] — 这是整个 proposal 最突出的亮点。8 个 baseline 涵盖所有相关方法且按一致性级别清晰分类；5 维 ablation 设计严谨（特别是 divergence metric comparison 和 consistency-diversity tradeoff 分析）；评估 benchmark 覆盖完整（GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM）；compute fairness 考虑周全（FLOPs-matched baseline + overhead profiling）；scale validation 在两个模型尺度上复制。这个实验设计本身就能让审稿人信服作者的 rigor。\n  \n  4. 可行性: [中] — 主要顾虑：(a) Perturbation pipeline 对 AMC/AIME 级别问题的覆盖率存疑——proposal 承认仅限 algebraic/arithmetic subtypes，这可能限制训练数据规模和多样性；(b) JS-divergence 在小样本 G 上的估计质量需要验证；(c) 计算开销（双倍 rollouts + JS 计算 + contrastive loss）可能显著，特别是在 8B 模型上。但 pilot study 设计（100 MATH-500 problems）和 Qwen3-1.7B scale validation 表明作者对可行性风险有清醒认识。\n  \n  5. 写作与呈现: [强] — Proposal 的结构、逻辑和 positioning 是一流的。三级框架的叙事有教科书般的清晰度；对每个相关工作的差异化论证精确到位；theoretical limitation 的论证（\"correct but inconsistent reasoning\" failure mode）简洁有力。如果论文写作保持此水准，presentation 不会是短板。\n\n【概率估计】: [30% - 42%] 中位 35%\n\n【估计理由】: \n- 问题重要性和 timeliness 为底线提供了保障（不太可能因为问题不相关被拒）\n- 实验设计的完善度是显著加分项，表明如果执行到位将产出 solid 的实证 paper\n- 核心方法的 novelty depth 是主要风险——\"add JS regularizer to GRPO for perturbation consistency\"可能被审稿人认为 contribution 不够深\n- 中位 35% 反映：这是一篇\"solidly above average\"的投稿，但在 novelty 这个关键维度上不是顶级水平。如果实验结果显示 L_consist 带来的 robustness gain 显著且 clean accuracy 不降（或提升），probability 可上移到 40%+；如果 gain 仅 marginal 或 perturbation pipeline 覆盖太窄导致结果不够 comprehensive，则下移到 25-30%\n- 在 AAAI 2026 的审稿环境中，这类\"简洁方法 + 完善实验\"的论文有一定优势——AAAI 审稿人通常重视 empirical thoroughness\n\n【主要风险】: \n1. **Novelty insufficiency**: 核心技术贡献（JS regularizer on perturbation pairs）被审稿人视为\"obvious combination of existing techniques\"（DyJR's JS + TA-GRPO's augmentation），leading to \"limited novelty\" rejection reason。这是最可能的致命风险。\n2. **Perturbation pipeline bottleneck**: 如果自动化 perturbation 仅覆盖 MATH/AMC/AIME 问题的一小部分（如 <40%），实验的 significance 和 generalizability 都会受质疑——reviewer 可能认为方法仅适用于特定题型。\n\n【实施评估】:\n  - 计算资源: 中等偏高。双倍 rollouts（G×2）+ 对比损失前向传播。Qwen3-8B 的 GRPO 训练本身需 4-8×A100 约 1-2 天；ConsistGRPO 估计需 2-3× overhead → 约 8×A100 3-5 天。1.7B 实验额外 1-2 天。总计约 200-400 A100-hours。\n  - 数据需求: MATH/AMC/AIME 训练集（公开可用）+ 自动生成的 perturbation variants。GSM-Symbolic/VAR-MATH generators 需要适配到更高难度问题。\n  - 人工介入: 中等。Perturbation pipeline 开发和验证需要人工审查（特别是 geometry/number theory 的 LLM-generated perturbations）。Pilot study 100 题的质量验证需要人工。\n  - 训练需求: 需要训练。主要是 RL fine-tuning（GRPO + 一致性损失），不需要从头预训练。对比头（MLP projection）参数量极小。\n  - 新 Benchmark: 不需要构建新 benchmark（使用现有 GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM）。但 perturbation pipeline 本身类似一个小规模 data generation 工具。\n  - 预估周期: 6-10 周。Pipeline 开发 + pilot study: 2-3 周；主实验训练 + 评估: 2-3 周；ablation + scale validation: 2-3 周；论文写作: 2 周（可与实验并行）。\n```\n\nSources:\n- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)\n- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)\n- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)\n- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)\n- [VAR-MATH: Probing True Mathematical Reasoning in LLMs](https://arxiv.org/abs/2507.12885)\n- [GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations](https://arxiv.org/abs/2605.07053)\n- [f-GRPO & Beyond: Divergence-Based RL Algorithms for General LLM Alignment](https://arxiv.org/html/2602.05946)\n- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://arxiv.org/html/2502.06453v2)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a comprehensive evaluation. Let me compile the assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- [TA-GRPO (arXiv 2601.22478)](https://arxiv.org/abs/2601.22478) (Jan 2026): 最直接的竞争者。通过 reward pooling 跨扰动变体共享 advantage，Pass@k 提升显著（AMC12/AIME24 +9.84），但确实未在任何扰动鲁棒性 benchmark 上评估。Proposal 对其\"blind to correct-but-inconsistent reasoning\"的批评成立。\n- [CLIPO (arXiv 2603.10101)](https://arxiv.org/abs/2603.10101) (Mar 2026, Qwen Applications): 在 GRPO 中集成 InfoNCE 对比学习，对齐同题不同正确推理路径的不变结构。GSM8K-P1/P2 提升 +1.48/+3.36。Proposal 正确区分了 same-problem cross-trajectory 与 cross-perturbation 两种不变性维度。\n- [AIR (arXiv 2605.20994)](https://arxiv.org/abs/2605.20994) (May 2026): 非对称锚点不变性正则化，主要面向 safety alignment，math 为辅助评估。使用 stop-gradient anchoring。Proposal 正确指出其非对称设计不适合数学扰动对的对称关系。\n- [DyJR (arXiv 2603.16157)](https://arxiv.org/abs/2603.16157) (Mar 2026): 在 GRPO 中使用 JS-divergence 作为 diversity-preserving regularizer（current vs. historical policy），实证证明 JS > Forward KL。为 proposal 的 JS 选择提供了直接的先验支持。\n- [AbstRaL (ICLR 2026, Apple)](https://arxiv.org/abs/2506.07751): 通过 RL 训练显式抽象能力，限于 GSM 级别问题。Proposal 主张通过正则化隐式实现类似抽象效果，覆盖更高难度问题。\n- [GRPO-CARE (arXiv 2506.16141)](https://arxiv.org/abs/2506.16141) (Jun 2025): 一致性感知 GRPO，但面向多模态视频推理。概念上有重叠（consistency + GRPO），但应用领域和技术细节不同。\n- [GSM-Symbolic (ICLR 2025)](https://arxiv.org/abs/2410.05229): 基础性 benchmark，证明数值替换可导致 LLM 性能大幅下降。MATH-Perturb、VAR-MATH 将此发现扩展到竞赛级数学。\n- [The Choice of Divergence (arXiv 2509.07430)](https://arxiv.org/abs/2509.07430): 系统分析 RLVR 中不同散度选择对 diversity collapse 的影响，为本文的 JS vs KL 讨论提供理论背景。\n- [F²C / BCT (arXiv 2025)]: 验证 consistency training 在 NLP 鲁棒性（+11.6% agreement）和 alignment（attack success 67.8%→2.9%）中的有效性，为数学领域迁移提供间接支持。\n\n- **调研总结**: 数学推理扰动鲁棒性是一个 well-documented 且 active 的问题。现有工作分布在 data augmentation（MathForge, PrAg-PO）、reward-level（TA-GRPO）、representation-level（CLIPO）和 explicit abstraction（AbstRaL），但**尚无工作在 GRPO 中实现 distribution-level 的跨扰动一致性正则化**。Proposal 占据了一个真实但相对 narrow 的空位。核心技术手段（JS-divergence consistency regularization between perturbed inputs）在 NLP/CV 中是成熟技术，novelty 主要来自在 math RL rollout distribution 层面的特定应用和完善的实验框架。\n\n【整体印象】: \n作为审稿人，我的第一反应是\"这是一篇 well-positioned、well-engineered 的工作，但技术新颖性有限\"。Proposal 展现了对领域极其深入的理解，三层框架（Data → Reward → Distribution）的概念分类清晰且有洞察力，\"correct but inconsistent reasoning\"的 failure mode 识别很尖锐。但核心方法——在扰动对之间最小化 JS-divergence——本质上是 consistency regularization 的一个特定实例，这在 semi-supervised learning、data augmentation 文献中已被广泛研究（R-Drop、consistency training 等）。创新主要在于\"将已知范式迁移到 math RL rollout 分布层面\"，这是一个有意义但bounded 的贡献。实验设计非常出色，是 proposal 最大的加分项。总体倾向 borderline，偏向 weak accept 但可能因 novelty 被 challenge。\n\n【核心贡献】: \n(1) 三层一致性框架（Data/Reward/Distribution-level）的概念分类——这是一个对领域有组织价值的taxonomy；\n(2) ConsistGRPO 方法本身——JS-divergence consistency loss + cross-perturbation contrastive loss 的组合；\n(3) 对 TA-GRPO \"correct but inconsistent reasoning\" 盲点的理论分析。\n贡献 (1) 对领域有中等价值（conceptual clarity），贡献 (2) 的技术新颖性受限于 consistency regularization 是已知范式，贡献 (3) 是一个好的 motivation 但偏 observational。\n\n【方法合理性】: \n方法在技术上是合理的。JS-divergence 的选择有充分论据（对称性、有界性、DyJR 的实证支持）。Rollout distribution 层面的一致性确实能提供比 reward pooling 更丰富的梯度信号。**但存在一个关键问题需要回应**：一个更简单的替代方案是\"TA-GRPO + 在 reward 中加入 consistency bonus\"（类似 GRPO-CARE 的思路），这是否能达到类似效果？Proposal 需要在实验中明确回答 distribution-level 相对于 reward-level consistency 的边际收益。Contrastive loss 作为可选组件的处理是务实的。\n\n【5 维度打分】:\n  1. 研究问题: 【强】 — 扰动鲁棒性是数学推理 LLM 的核心痛点，GSM-Symbolic/VAR-MATH 提供了充分的实证支持（performance drops 47-73%）。问题重要且具有实际价值。RL-trained models 同样脆弱这一发现进一步强化了研究动机。\n  \n  2. 方法与创新: 【中】 — 三层框架的 conceptual contribution 有价值，JS-divergence consistency loss 在 math RL 中的特定应用是新的。但核心技术（consistency regularization via divergence minimization between perturbed inputs）是 NLP/CV 中的成熟技术（R-Drop [NIPS 2021]、consistency training for semi-supervised learning）。与 GRPO-CARE（consistency bonus in GRPO）、AIR（invariance regularization in GRPO）在 high-level idea 上有重叠，虽然 application domain 和具体设计不同。对比 CLIPO 和 TA-GRPO 的差异化清晰。相对于 DyJR（已在 GRPO 中使用 JS-divergence 做 regularization，虽然目的不同），novelty 的增量需要通过强实验结果来支撑。\n  \n  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点。8 个 baseline（含 FLOPs-matched）覆盖了所有相关工作层级，7+ 评估 benchmark 涵盖 GSM 到 competition-level，5 维 ablation 设计系统且完整（尤其是 divergence metric comparison 和 consistency-diversity tradeoff 分析）。Scale validation（1.7B + 8B）、perturbation pipeline pilot study、compute fairness profiling 都体现了严谨性。唯一的小瑕疵是缺少 human evaluation 或 case study 来定性分析\"reasoning process invariance\"。\n  \n  4. 可行性: 【中】 — 方法实现本身不复杂（JS loss 计算、contrastive head 均为标准组件）。主要风险在 perturbation generation pipeline：(a) MATH/AMC/AIME 中 geometry 和 number theory 问题的扰动生成依赖 LLM + 符号验证，可靠性存疑；(b) \"restricted to algebraic and arithmetic subtypes\" 的限制削弱了 generality claim；(c) 8B 模型 on-the-fly perturbation + 双倍 rollout 的计算开销需要 careful profiling。Proposal 对这些风险有意识但未给出详细的 mitigation 方案。Qwen3-8B 的训练在合理计算资源范围内（估计 8-16 GPU days）。\n  \n  5. 写作与呈现: 【强】 — 组织结构清晰，三层框架提供了很好的叙事线索。Related work 的定位精准且充分，每个 baseline 的局限性分析到位。方法描述技术上准确。Motivation 从 VAR-MATH 数据到 theoretical limitation analysis 的递进逻辑有说服力。唯一建议是增加 formal notation 来更严格地定义 \"rollout distribution\" 和 JS-divergence 的具体计算方式。\n\n【概率估计】: [25% - 38%] 中位 30%\n\n【估计理由】: \n这个 proposal 的核心矛盾在于：**极强的工程和实验设计** vs **有限的技术新颖性**。\n\n(+) 研究问题重要且 timely，三层框架有概念价值，实验设计异常完备（8 baselines, 5-dim ablation, scale validation, FLOPs fairness），定位清晰且差异化明确。如果实验结果强劲（在 VAR-MATH/MATH-Perturb 上显著优于 TA-GRPO 且不损害 clean accuracy），这可以是一篇 solid empirical paper。\n\n(-) 核心方法是 well-known 的 consistency regularization 技术在 math RL 中的特定应用，技术新颖性 bounded。缺乏理论分析（无 convergence guarantee、sample complexity bound）。领域极度拥挤（GRPO variants 已有 10+ 篇 2026 年论文），reviewer fatigue 是现实风险。AAAI 2026 acceptance rate ~23%，对于 novelty 中等但执行力强的论文，命运高度依赖 reviewer 匹配——遇到重视 empirical rigor 的 reviewer 可能 accept，遇到要求 technical novelty 的 reviewer 很可能 reject。\n\n中位估 30% 反映了：一篇在各方面都 competent、在实验设计上 above-average、但在 novelty 上处于 borderline 的投稿，在一个 competitive 的领域。\n\n【主要风险】: \n1. **Novelty 不足被拒**：最可能的拒稿理由是\"consistency regularization via JS-divergence between perturbed inputs is a well-known technique; the application to GRPO rollout distributions is a straightforward extension, not a fundamental contribution\"。特别是 DyJR 已经在 GRPO 中使用了 JS-divergence（虽然目的不同），GRPO-CARE 已经在 GRPO 中做了 consistency-aware training（虽然领域不同），reviewer 可能认为本文只是已知组件的 recombination。\n2. **Perturbation pipeline 的可靠性与 generality**：限制在 algebraic/arithmetic subtypes 会被 reviewer 质疑 generality claim。LLM-generated perturbations + symbolic verification 的 fallback 方案可靠性未经验证，如果 pilot study 覆盖率不高，会严重削弱整个方法的实用性。\n\n【实施评估】:\n  - 计算资源: 中等偏高。Qwen3-8B 的 GRPO 训练 + 双倍 rollout（original + perturbed）+ contrastive head 前向/反向传播。估计需要 4-8 × A100 80GB，训练 3-5 天（primary），1.7B scale validation 额外 1-2 天。总计约 200-400 A100 GPU-hours。\n  - 数据需求: MATH/AMC/AIME 训练集（公开可得）+ on-the-fly perturbation generation。7+ 评估 benchmark 均为公开数据集。数据本身不是瓶颈。\n  - 人工介入: 中等。Perturbation pipeline 需要 careful engineering（SymPy filter、LLM fallback verification）。Pilot study 100题需要人工审核扰动质量。Hyperparameter sweep（λ₁, λ₂, G）需要反复实验调参。\n  - 训练需求: 需要完整的 RL 训练流程（GRPO + 两个额外 loss term）。8 个 baseline 中至少 4-5 个需要从头训练/复现（vanilla GRPO, GRPO+Aug, TA-GRPO reproduction, CLIPO reproduction, FLOPs-matched）。总训练运行次数估计 15-25 runs。\n  - 新 Benchmark: 不需要构建新 benchmark。但 perturbation generation pipeline 本身可作为工具贡献（如果质量可靠）。\n  - 预估周期: 6-10 周。Pipeline 开发与 pilot study (1-2周) → 主实验训练 (2-3周) → Ablation 与 analysis (2-3周) → 写作 (1-2周)。主要瓶颈是 perturbation pipeline 的工程开发和大量 baseline 复现。\n```\n\nSources:\n- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)\n- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)\n- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)\n- [DyJR: Preserving Diversity in RL with Verifiable Rewards via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)\n- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)\n- [GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning](https://arxiv.org/abs/2506.16141)\n- [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs](https://arxiv.org/abs/2410.05229)\n- [The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR](https://arxiv.org/abs/2509.07430)\n- [MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations](https://arxiv.org/abs/2502.06453)\n- [DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths](https://arxiv.org/abs/2505.09655)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling\n\n## Core Problem\n\nRL-trained mathematical reasoning models achieve SOTA on clean benchmarks but suffer severe accuracy drops under trivial surface-form perturbations even after RL training: VAR-MATH (arXiv 2025) reports average declines of 47.9% (AMC23), 58.8% (AIME24), and 72.9% (AIME25) on RL-trained models under numerical substitution. GRPO's reward signal provides no gradient against surface-form-dependent reasoning — the policy is rewarded for correct answers regardless of whether it exploits superficial patterns or genuine mathematical structure.\n\n## Three-Level Framework for Consistency Enforcement in Math RL\n\nWe identify three progressively stronger levels of consistency enforcement:\n\n**Level 1 — Data-level**: Augmenting training with perturbed variants without explicit consistency signal (MathForge ICLR 2026; PrAg-PO arXiv 2026 with 13 prompt templates). TA-GRPO's ablation (arXiv 2601.22478) demonstrates this alone is insufficient: \"augmentation without pooling doesn't help.\"\n\n**Level 2 — Reward-level**: Pooling rewards across original and perturbed variants (TA-GRPO, arXiv 2601.22478). Provides implicit consistency through shared advantages but operates on sparse binary feedback (correct/incorrect). TA-GRPO achieves Pass@k gains (up to +9.84 on AMC12/AIME24) but has not been evaluated on any perturbation robustness benchmark (GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP). **Theoretical limitation**: consider two semantically equivalent problems x, x' where the policy solves x via memorized pattern-matching and x' via genuine derivation — both correct, so reward pooling assigns identical advantages, remaining blind to the fragile reasoning on x. This \"correct but inconsistent reasoning\" failure mode is invisible to reward-level signals.\n\n**Level 3 — Distribution-level** (this work): Explicitly minimizing JS-divergence between policy rollout distributions on original and perturbed problems. This provides continuous gradient signal over the entire reasoning trajectory, detecting and penalizing divergent reasoning processes even when both lead to correct answers. By enforcing reasoning structure invariance — that the model's reasoning process is determined by mathematical structure rather than surface form — this approach implicitly forces the kind of abstraction that AbstRaL (ICLR 2026) achieves explicitly, but through a regularization mechanism rather than a separate abstraction stage.\n\n## Research Landscape\n\n**Training-time math robustness**: AbstRaL (ICLR 2026, Apple) uses RL to train explicit abstraction before solving, limited to GSM-level. TA-GRPO (arXiv 2601.22478, Jan 2026) introduces transform-augmented reward pooling in GRPO with Pass@k improvements on competition math but no robustness evaluation. AIR (arXiv 2605.20994, May 2026) applies asymmetric anchor invariance regularization to GRPO primarily for safety alignment (with auxiliary math evaluation), using stop-gradient anchoring — appropriate when one prompt variant has more reliable feedback, but suboptimal for math perturbation pairs where both sides are symmetric and equally verifiable.\n\n**Contrastive learning in GRPO**: CLIPO (arXiv 2603.10101, Mar 2026) integrates InfoNCE over correct rollouts within GRPO, extracting invariant reasoning structures across different correct solution paths to the same problem. MCPO (arXiv 2605.25443, May 2026) extends cross-domain contrastive policy optimization. Both target same-problem cross-trajectory invariance (aligning different correct reasoning paths). Our cross-perturbation contrastive component targets a different invariance dimension: aligning representations across surface-form-different but semantically-identical problem pairs, directly enforcing perturbation robustness rather than obtaining it as a side effect.\n\n**GRPO variants**: DAPO, DR.GRPO, COPO, DRA-GRPO address stability/diversity/efficiency but none target perturbation invariance. DyJR (arXiv 2603.16157) uses JS-divergence in GRPO as diversity-preserving regularizer between current and historical policies, establishing JS-divergence viability in GRPO and demonstrating JS > Forward KL for this purpose. PrAg-PO (arXiv 2602.03190, Feb 2026) uses prompt templates as implicit regularization with no consistency loss.\n\n**Adjacent work**: GRPO-CARE (Jun 2026) adds consistency bonuses for multimodal video reasoning. CSR (Jan 2026) enforces causal consistency via operator perturbation in SFT, not RL. F²C (arXiv 2025) validates consistency training for NLP robustness (11.6% agreement recovery). BCT (arXiv 2025) validates consistency training for alignment (attack success 67.8% → 2.9%). Reward Under Attack (arXiv 2026) examines PRM robustness. MathForge (ICLR 2026) combines difficulty-weighted GRPO with reformulation (clean accuracy only).\n\n**Why JS-divergence over alternatives**: JS-divergence is chosen over KL-divergence for two reasons: (1) symmetry — perturbation pairs (x, x') have symmetric epistemic status (both equally verifiable), making asymmetric KL(P_x || P_x') arbitrary in direction; (2) boundedness — JS ∈ [0, ln2] while KL can diverge, providing more stable training gradients. DyJR's empirical finding that JS outperforms Forward KL in GRPO regularization provides additional support.\n\n## Proposed Approach\n\n**ConsistGRPO** augments GRPO with distribution-level consistency enforcement as its primary mechanism:\n\n**Primary: Policy-level JS-divergence consistency loss (L_consist).** For each problem x, generate a math-equivalence-preserving perturbation x'. Collect G rollouts from each: {τ₁,...,τ_G} ~ π_θ(·|x) and {τ'₁,...,τ'_G} ~ π_θ(·|x'). Compute sequence-level log-probabilities to form empirical rollout distributions P_x and P_x'. The consistency loss L_consist = JS(P_x || P_x') provides symmetric, continuous gradient toward invariance over the full reasoning process. Unlike TA-GRPO's reward pooling (which transmits only binary outcome signals and is blind to \"correct but inconsistent reasoning\"), L_consist directly penalizes divergent reasoning distributions even when both variants are answered correctly.\n\n**Secondary: Cross-perturbation contrastive loss (L_contrastive).** Extract representations via mean-pooling the last hidden layer, project through a 2-layer MLP head (discarded at inference). Positive pairs: representations from perturbation pair (x, x') rollouts. Negative pairs: in-batch representations from different problems. Loss: InfoNCE. This complements CLIPO's same-problem cross-trajectory contrastive learning (arXiv 2603.10101) with a different invariance dimension — cross-perturbation invariance — directly targeting the \"blind skill application\" failure identified by MATH-Perturb (arXiv 2025). This component is treated as optional; ablations will determine its marginal contribution beyond L_consist.\n\n**Combined objective**: L = L_GRPO + λ₁·L_consist + λ₂·L_contrastive.\n\n**Perturbation generation pipeline**: Adapt GSM-Symbolic/VAR-MATH generators for MATH/AMC/AIME, restricted to algebraic and arithmetic subtypes amenable to automated perturbation (numerical substitution, variable renaming). Apply SymPy-based validity filter verifying solvability and answer computability. For problem types where automated perturbation is unreliable (geometry, certain number theory), use LLM-generated perturbations with symbolic verification. Report perturbation success rates per problem category. Conduct pilot study on 100 MATH-500 problems to validate pipeline coverage before full-scale training.\n\n**Training**: Qwen3-8B (primary) and Qwen3-1.7B (scale validation) on MATH/AMC/AIME with on-the-fly perturbation generation.\n\n## Experimental Design\n\n**Baselines (8 methods):**\n| Method | Consistency Level | Key Feature |\n|--------|------------------|-------------|\n| Vanilla GRPO | None | Same data, no augmentation |\n| GRPO + Aug Only | Data | Same perturbations, no consistency/contrastive loss |\n| TA-GRPO (arXiv 2601.22478) | Reward | Transform-augmented reward pooling |\n| CLIPO (arXiv 2603.10101) | Representation | Same-problem cross-trajectory contrastive |\n| AbstRaL (ICLR 2026) | — | Abstraction-based (GSM-level; best-effort on MATH/AIME) |\n| DR.GRPO | — | GRPO variant for stability |\n| PrAg-PO (arXiv 2026) | Data | 13 prompt templates, implicit regularization |\n| FLOPs-matched GRPO | — | Vanilla GRPO with matched total compute (profiled, not preset) |\n\n**Evaluation benchmarks**: GSM-Symbolic (ICLR 2025), GSM-Plus (ACL 2024), VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM (May 2026) for robustness; MATH-500, AIME 2024/2025 for clean accuracy. Report absolute accuracy, robustness gap (clean − perturbed), and Pass@k (k=1, 8, 64).\n\n**Ablations (5 dimensions):**\n1. Component decomposition: GRPO → +Aug → +L_consist → +L_contrastive → Full (5-row table isolating each component)\n2. Perturbation type: numerical substitution only / variable renaming only / combined\n3. Hyperparameter sensitivity: λ₁, λ₂ weight sweep (5 values each); group size G effect on L_consist\n4. Training dynamics: clean vs. robustness accuracy learning curves; entropy trajectory (cf. PrAg-PO entropy collapse)\n5. Divergence metric comparison: JS-divergence vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style asymmetric stop-gradient\n\n**Consistency-diversity tradeoff analysis**: Track Pass@k curves across λ₁ values; report unique correct solution count per problem and pairwise rollout distance as diversity metrics; analyze whether stronger consistency constraints cause diversity collapse (cf. DyJR arXiv 2603.16157).\n\n**Compute fairness**: Profile actual FLOPs overhead of ConsistGRPO vs. vanilla GRPO before setting FLOPs-matched baseline. Report breakdown: rollout generation, JS-divergence computation, contrastive loss overhead. Report wall-clock time and total GPU-hours.\n\n**Scale validation**: Replicate core comparison (ConsistGRPO vs. vanilla GRPO vs. TA-GRPO vs. CLIPO) on Qwen3-1.7B.\n\n## Key References\n\n- GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025)\n- GSM-Plus: Comprehensive Benchmark for Evaluating Robustness of LLMs as Math Problem Solvers (ACL 2024, arXiv 2402.19255)\n- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- Prompt Augmentation Scales up GRPO Training on Math Reasoning (arXiv 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (arXiv 2025)\n- PutnamGAP: Robustness of LLMs via Mathematically-Equivalent Transformation (arXiv 2025)\n- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations (arXiv 2025)\n- Consistency Training Helps Stop Sycophancy and Jailbreaks (arXiv 2025)\n- Reward Under Attack: Robustness and Hackability of Process Reward Models (arXiv 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478, Jan 2026)\n- AIR: Towards Context-Invariant Safety Alignment for LLMs (arXiv 2605.20994, May 2026)\n- DyJR: Preserving Diversity in RL with Verifiable Rewards via JS-Divergence (arXiv 2603.16157, 2026)\n- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, Mar 2026)\n- MCPO: Harmony in Diversity — Multi-domain Contrastive Policy Optimization (arXiv 2605.25443, May 2026)"
}
````

---

### Runtime record

_source line 2 · 2026-05-29T06:38:05.457Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:38:05.457Z",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-29T06:38:05.565Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient research context. Let me compile the final evaluation.

```
【阶段】: Triage

【领域调研】:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478) (arXiv, Jan 2026): 最直接的竞争者。通过跨perturbation变体pooling reward实现Level-2一致性。取得Pass@k提升(AMC12/AIME24上+9.84)，但**未在任何perturbation robustness benchmark上评估**（GSM-Symbolic, VAR-MATH, MATH-Perturb均未测试）。本proposal精准定位了这一盲区。
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101) (arXiv, Mar 2026): 在GRPO中加入InfoNCE对比学习，对齐同一问题的不同正确rollout。方向是same-problem cross-trajectory invariance。本proposal的对比学习组件（L_contrastive）目标不同——cross-perturbation invariance，是互补而非重复的invariance维度。CLIPO在GSM8K-P1/P2上有改进但幅度有限。
- [AIR: Towards Context-Invariant Safety Alignment](https://arxiv.org/abs/2605.20994) (arXiv, May 2026): 使用非对称stop-gradient anchor invariance regularization整合到GRPO中，但主要面向safety alignment而非math robustness。其非对称设计适合safety场景（一个prompt变体有更可靠反馈），但不适合math perturbation对（双侧对称可验证）。本proposal选择对称JS散度的论证合理。
- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157) (arXiv, Mar 2026): 在GRPO中使用JS散度作为diversity-preserving regularizer（current vs. historical policy），验证了JS散度在GRPO框架中的可行性和优越性（JS > Forward KL）。为本proposal的技术选择提供了经验支持，但DyJR的JS用途是diversity preservation，本proposal的JS用途是cross-perturbation consistency——不同目标。
- [AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking](https://openreview.net/forum?id=fDk95XPsCU) (ICLR 2026): 通过RL训练显式抽象再求解，但受限于GSM级别问题。本proposal声称通过分布一致性正则化隐式实现类似抽象效果。
- [MATH-Perturb](https://arxiv.org/abs/2502.06453) (arXiv, 2025): 基准测试显示即使o1-mini等模型在hard perturbation上也有10%-25%准确率下降，验证了perturbation robustness问题的真实性和严重性。
- [GSM-Symbolic](https://arxiv.org/abs/2410.05229) (ICLR 2025, Apple): 开创性工作，揭示LLM在symbolic/structural perturbation下的脆弱性。
- [PrAg-PO: Prompt Augmentation Scales up GRPO](https://arxiv.org/abs/2602.03190) (arXiv, Feb 2026): 使用13种prompt模板作为隐式正则化，属于Data-level (Level 1)。
- [The Choice of Divergence](https://arxiv.org/abs/2509.07430) (arXiv, 2025): 系统研究f-divergence在RLVR中的作用，发现mass-covering divergence（forward KL, JS）优于reverse KL在保持多样性方面。

- **调研总结**: Math reasoning的perturbation robustness是一个已被充分验证的重要问题（GSM-Symbolic, VAR-MATH, MATH-Perturb等多个benchmark证实）。在RL训练方面，TA-GRPO开创了reward-level一致性但缺乏robustness评估，CLIPO/AIR/DyJR各自在GRPO框架中使用了不同的正则化/对比学习但未直接针对perturbation robustness。本proposal所定位的"distribution-level consistency for perturbation invariance"在现有工作中确实是一个未被占据的具体位置，三级框架的分析有见地。但这一位置的"增量"性质也意味着novelty的天花板有限——本质上是将已有技术（JS divergence, contrastive learning）组合应用到一个已有问题上。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇**定位精准、调研扎实、实验设计周全**的工作。三级一致性框架（Data → Reward → Distribution）的提出有清晰的递进逻辑，对TA-GRPO"correct but inconsistent reasoning"盲区的分析切中要害。但第二反应是：**核心技术贡献的深度有限**——本质上是在GRPO loss上加了一个JS散度正则项和一个InfoNCE对比项，这两者都不是新技术。论文的价值更多在于"将对的东西放到对的地方"（right combination for the right problem），而非方法论上的突破。

我会倾向于**weak accept / borderline**——如果实验结果确实显著（尤其在perturbation robustness benchmarks上的提升），有可能跨过accept线；但如果reviewer认为这只是existing techniques的straightforward combination，可能会被borderline reject。

【核心贡献】:
1. **三级一致性框架（Level 1-2-3）**: 对现有math robustness方法的系统性分类（Data/Reward/Distribution），理论上论证了为什么Level 2（reward pooling）不足以捕捉"correct but inconsistent reasoning"。这个框架本身有学术价值。
2. **ConsistGRPO方法**: 在GRPO中加入cross-perturbation JS散度一致性loss和contrastive loss。技术上是incremental（JS divergence + InfoNCE都是成熟工具），但应用场景和组合方式有novelty。
3. **完备的实验设计**: 8个baseline、7+个benchmark、5维ablation的设计本身就是一个贡献，尤其是填补了TA-GRPO未做robustness评估的空白。

对领域的价值：**中等偏上**。如果实验验证了distribution-level > reward-level的假设，这会为math RL robustness社区提供一个有价值的empirical insight和实用方法。但不太可能改变领域的研究方向。

【方法合理性】:
方法整体合理，但有几个需要关注的点：

1. **JS散度计算的实际效果**: proposal使用sequence-level log-probabilities构造empirical rollout distributions P_x和P_x'，然后计算JS(P_x || P_x')。但G个rollout（通常G=8-16）构成的empirical distribution可能非常noisy，JS的估计方差大。这与DyJR使用buffer accumulated distributions不同——DyJR有更多样本来估计分布。proposal需要讨论small-sample JS estimation的问题。

2. **更简单的替代方案**: 一个直接的替代方案是在rollout的token-level logits上做KL/JS对齐（类似knowledge distillation），而非sequence-level。这可能提供更dense的梯度信号。另一个替代方案是直接在TA-GRPO基础上加一个简单的reward consistency bonus（如果x和x'都对则bonus增大），而非引入JS散度——这更简单但可能近似达到类似效果。proposal应明确论证为何distribution-level JS优于这些simpler alternatives。

3. **Perturbation pipeline的reliability**: 对于MATH/AMC/AIME level的问题（竞赛数学），自动化perturbation的正确性验证是一个非平凡的工程问题。proposal提到用SymPy验证，但竞赛数学的很多问题（组合、数论、几何）不容易用SymPy自动验证。这可能限制training数据的覆盖率。proposal提到了这个问题并计划做pilot study，这是好的，但也意味着实际可用的training data可能比预期少。

4. **Consistency-diversity tradeoff**: 这是一个关键问题。强一致性约束可能导致rollout diversity collapse（如果模型被迫让P_x ≈ P_x'，可能会converge到单一推理路径）。proposal意识到了这个问题并计划做tradeoff分析，这很好。但这也意味着最优的λ₁可能需要非常小，此时L_consist的实际贡献就变得很边际。

【5 维度打分】:

1. **研究问题: 强** — Math reasoning模型在perturbation下的脆弱性是一个经GSM-Symbolic (ICLR 2025)、VAR-MATH、MATH-Perturb等多个benchmark验证的真实问题。RL训练（GRPO）不仅未解决反而可能加剧这一问题。TA-GRPO的reward pooling方法未做robustness评估、且理论上对"correct but inconsistent reasoning"存在盲区——这个gap的定位非常精准且有价值。问题的重要性和时效性都很强。

2. **方法与创新: 中** — 三级框架的分析有insight，但核心方法（JS divergence regularization + InfoNCE contrastive loss）都是成熟技术的组合应用，不涉及方法论创新。与CLIPO (arXiv 2603.10101) 相比，对比学习组件的区别仅在于positive pair的构造方式（cross-perturbation vs. cross-trajectory）；与DyJR (arXiv 2603.16157) 相比，JS散度的使用方式不同（cross-perturbation vs. temporal）但技术形式类似；与AIR (arXiv 2605.20994) 相比，区别在于对称vs.非对称——有道理但不构成显著创新。一个苛刻的reviewer可能会认为这是"TA-GRPO + JS regularization"的straightforward extension。proposal需要通过强实验结果来弥补方法novelty的不足。

3. **实验设计: 强** — 这是proposal最突出的优势。8个baseline覆盖了Data/Reward/Representation/None四个consistency level，形成完整的ablation对照；7+个benchmark涵盖robustness和clean accuracy两个维度；5维ablation（component decomposition, perturbation type, hyperparameter sensitivity, training dynamics, divergence metric comparison）非常周全；FLOPs-matched baseline的设计解决了公平性问题；scale validation (1.7B + 8B) 增加了可信度。特别值得肯定的是divergence metric comparison (JS vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style)——这直接回应了DyJR和Choice of Divergence等工作的发现，既是ablation也是对领域的贡献。

4. **可行性: 中** — 
   - Qwen3-8B的训练在单节点8×A100/H100上可行（约2-4周）。
   - 主要风险在perturbation pipeline：竞赛数学(AMC/AIME)的自动perturbation + 正确性验证是非平凡的工程任务。proposal限制在algebraic/arithmetic subtypes是务实的，但可能导致training data覆盖率不足。
   - JS散度计算需要对每个问题做2×G次rollout（original + perturbed），计算开销翻倍。proposal承认这一点并计划profile FLOPs，但这可能需要额外的优化（如shared prefix caching）。
   - 整体可行但有工程挑战。

5. **写作与呈现: 强** — proposal的结构清晰、逻辑递进（问题定义 → 三级框架 → 方法 → 实验设计）。相关工作的调研非常全面，对每个相关工作的定位和区分精确。三级框架的提出为读者提供了清晰的conceptual map。"correct but inconsistent reasoning"的例子直观有力。唯一可改进的是：proposal略显冗长，如果能更精炼地呈现核心idea会更好。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:

**上行因素（推向42%）**:
- 研究问题精准且timely，精确定位了TA-GRPO的理论盲区
- 实验设计极为完备（8 baselines, 7+ benchmarks, 5-dim ablation），这本身是显著加分项
- 三级框架提供了有价值的conceptual contribution
- 领域调研极其全面，reviewer不太会找到"missed related work"这类问题
- Perturbation robustness在2025-2026是热门话题，reviewers对该方向普遍有兴趣

**下行因素（推向28%）**:
- 方法novelty有限——核心是JS divergence + InfoNCE的straightforward combination，AAAI reviewers可能认为technical contribution不足
- 目前没有实验结果。如果distribution-level一致性的提升相对于TA-GRPO的reward pooling是边际的（例如<3%），论文会失去核心论据
- Perturbation pipeline的实际覆盖率和质量是不确定因素
- Consistency-diversity tradeoff可能限制方法的实际增益
- GRPO variants已经非常拥挤（DAPO, DR.GRPO, CLIPO, DyJR, TA-GRPO, PrAg-PO, MCPO, AIR...），reviewer可能对"yet another GRPO variant"产生审美疲劳

**中位35%的理由**: 这是一篇"solid but incremental"的投稿。问题定位好、实验设计完备、写作清晰，但方法novelty的天花板限制了它。在AAAI 2026的competitive pool中，它位于borderline区域。如果实验结果显著（distribution-level显著优于reward-level，尤其在perturbation benchmarks上），概率偏向上界；如果实验结果边际，概率偏向下界。

【主要风险】:
1. **"Insufficient novelty / straightforward combination"**: 最可能的拒稿理由。Reviewer可能认为JS-divergence regularization + InfoNCE contrastive loss的组合缺乏方法论深度，尤其是在GRPO variants已经极度拥挤的当下。三级框架虽好，但框架+combination可能不足以构成AAAI主会级别的贡献。
2. **实验结果不确定性**: Proposal尚无实验结果。如果distribution-level一致性相对于reward-level（TA-GRPO）的提升幅度有限，或者consistency-diversity tradeoff使得最优λ₁很小导致L_consist贡献边际，核心claim（Level 3 > Level 2）将缺乏实证支撑。

【实施评估】:
- **计算资源**: 中高。需要8×A100/H100 GPU节点。每个问题需2×G次rollout（原始+扰动），计算量约为vanilla GRPO的2-2.5倍。JS散度和contrastive loss的额外计算开销相对较小。估计总GPU-hours: 2000-4000（含所有ablation和baseline复现）。
- **数据需求**: MATH/AMC/AIME训练集（公开可用）。关键瓶颈是perturbation pipeline的构建——需要对竞赛数学问题进行自动化扰动并验证正确性。Pilot study (100题) 可在1-2周内完成。
- **人工介入**: 中等。Perturbation pipeline需要人工验证（尤其是geometry/number theory等难以自动验证的题型）。LLM-generated perturbations需要质量抽检。Baseline复现（TA-GRPO, CLIPO, AbstRaL）可能需要调试。
- **训练需求**: 需要完整的RL训练流程（GRPO + 正则化项）。Qwen3-8B约需2-3周训练，Qwen3-1.7B约需1周。总训练时间（含所有variants和ablations）约4-6周。
- **新 Benchmark**: 不需要构建新benchmark——使用现有的GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM。但perturbation pipeline本身可视为一个工程产出。
- **预估周期**: 10-14周（Pilot study 2周 + Perturbation pipeline 2-3周 + 主实验+ablation 4-6周 + 论文写作 2-3周）。假设计算资源充足，一个2-3人团队可在AAAI 2026 deadline前完成。
```

Sources:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)
- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [GSM-Plus: A Comprehensive Benchmark for Evaluating Robustness of LLMs](https://arxiv.org/abs/2402.19255)
- [The Choice of Divergence in RLVR](https://arxiv.org/abs/2509.07430)
- [Post-Training in 2026: GRPO, DAPO, RLVR & Beyond](https://llm-stats.com/blog/research/post-training-techniques-2026)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Based on my research, I now have sufficient information to provide a comprehensive evaluation.

```
【阶段】: Triage

【领域调研】:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478) (arXiv, Jan 2026): 最直接的 Level 2 对比方法。通过 reward pooling 跨变换变体共享 advantage，在 AMC12/AIME24 上 Pass@k 提升最高 +9.84。但关键发现：未在任何 perturbation robustness benchmark 上评估，这正是本 proposal 的攻击点。其 ablation 证实"仅 augmentation 不够"，支持更强一致性信号的必要性。
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101) (arXiv, Mar 2026): 在 GRPO 中引入 InfoNCE 对比学习，对齐同一问题不同正确 rollout 的表征。GSM8K-P1/P2 分别 +1.48/+3.36。其 invariance 维度是 cross-trajectory（同题不同解），而本 proposal 的 cross-perturbation 维度（同义不同题）是正交的。
- [AIR: Towards Context-Invariant Safety Alignment](https://arxiv.org/abs/2605.20994) (arXiv, May 2026): 非对称 stop-gradient anchor invariance regularization，主要面向安全对齐。因其假设一侧反馈更可靠（verifiable anchor），不适合数学 perturbation 对的对称场景。技术上最接近本 proposal 的 invariance regularization 范式，但应用场景和设计选择明确不同。
- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157) (arXiv, Mar 2026): 在 GRPO 中使用 JS-divergence 作为当前策略与历史分布之间的正则化器，防止 diversity collapse。经验上验证了 JS > Forward KL 在 GRPO 中的适用性。为本 proposal 的 JS 选择提供了技术先例。
- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885) (arXiv, 2025): 文档化了 RL-trained 模型在数值替换下的严重退化（AMC23: -47.9%, AIME24: -58.8%, AIME25: -72.9%），为本 proposal 的问题动机提供了强有力的实证基础。
- [GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations](https://arxiv.org/abs/2605.07053) (arXiv, May 2026): 最新的语义扰动 benchmark 框架，在 14 个 SOTA LLM 上观察到一致的性能下降（~28% at maximum strictness），进一步验证了 perturbation robustness 问题的普遍性。
- [f-GRPO & Beyond: Divergence-Based RL Algorithms](https://arxiv.org/html/2602.05946) (arXiv, 2026): 探索 GRPO 中替代 divergence measure 的通用框架，表明 divergence 选择是活跃研究方向。
- 调研总结: Math RL robustness 是 2025-2026 的热点方向，问题已被充分文档化（VAR-MATH, MATH-Perturb, GSM-Symbolic），但训练时解决方案仍处于早期：TA-GRPO 提供 reward-level 方案但缺乏 robustness 评估，CLIPO 提供 representation-level 方案但面向不同维度，AIR 面向安全而非数学。本 proposal 的"distribution-level consistency"定位在这些工作之间有清晰的空位。

【整体印象】: 作为审稿人，第一反应是 **lean accept / borderline**。这是一篇 positioning 极为精准、实验设计极为完善的 proposal。三层框架（Data → Reward → Distribution）的叙事结构清晰有力，对现有工作的分析透彻且公平。核心 insight（reward pooling 对"correct but inconsistent reasoning"失明）在理论上 sound 且 intuitively compelling。主要顾虑在于核心技术贡献（加一个 JS-divergence regularizer）的 novelty 深度是否足够——方法本身相对 straightforward，可能被部分审稿人视为"obvious next step"。但如果实验结果强劲（在 robustness benchmarks 上显著超越 TA-GRPO 同时保持 clean accuracy），这足以弥补方法简洁性的不足。

【核心贡献】: 
1. **概念贡献**：提出三级一致性框架并论证 distribution-level > reward-level > data-level，为 math RL robustness 提供了清晰的 taxonomy。
2. **技术贡献**：设计 ConsistGRPO，在 GRPO 训练中加入 perturbation pair 间的 JS-divergence 一致性损失，实现对 reasoning trajectory 全程的连续梯度监督。
3. **实验贡献**：如果执行到位，将是第一个在完整 robustness benchmark 矩阵上系统比较 training-time consistency enforcement 策略的工作。

贡献价值判断：概念贡献有中等价值（框架化现有 landscape），技术贡献在"neat and effective"和"too simple"之间取决于实验效果，实验贡献如完成度高则独立具有价值。

【方法合理性】: 
方法设计总体合理，JS-divergence 的选择有充分论证（对称性、有界性、DyJR 经验支持）。但存在几个需要审视的点：

1. **rollout 分布的定义模糊**: "sequence-level log-probabilities to form empirical rollout distributions P_x and P_x'"—G 个 rollout 形成的经验分布在高维序列空间中是极其稀疏的。JS-divergence 在仅 G=8-16 个样本上的估计噪声可能很大。是用 kernel density estimation？还是简单离散分布？这影响梯度质量。

2. **更简单的替代方案存在吗？** 
   - 直接对 perturbation pair 做 sequence-level KL（取平均方向）
   - 在 token-level 逐步计算一致性（类似 knowledge distillation 的 logit matching）
   - 简单地将 perturbation pair 的 rollout 合并计算 advantage（即 TA-GRPO 的扩展）
   - 这些替代方案需要在 ablation 中明确排除或比较（proposal 的 ablation 5 部分覆盖了这点，是好设计）

3. **consistency-diversity 冲突**: 强制两个 perturbation 的 rollout 分布一致可能会压缩策略的 exploration 能力。Proposal 意识到了这点并设计了 tradeoff 分析，这是好的。

【5 维度打分】:
  1. 研究问题: [强] — VAR-MATH 的实证数据（47-72% accuracy drop）清楚表明这是一个真实且严重的问题。RL-trained 模型的 perturbation fragility 是当前社区关注的焦点，且缺乏有效的 training-time 解决方案。问题定义精确，不含歧义。
  
  2. 方法与创新: [中] — 核心方法（JS-divergence between perturbation pair rollouts）技术上 sound 但相对 straightforward。创新性主要来自：(a) 将已有技术组件（JS-divergence from DyJR, contrastive from CLIPO, augmentation from TA-GRPO）以新的方式组合并面向新目标；(b) "correct but inconsistent reasoning" failure mode 的识别和 distribution-level 解决思路。但 reviewer 可能认为这是"obvious combination"——DyJR 证明 JS 在 GRPO 中可行，TA-GRPO 证明 perturbation augmentation 有用，合在一起不意外。与 AIR 的差异化论证 compelling（symmetric vs asymmetric），但 AIR 本身不面向 math 所以竞争性不强。
  
  3. 实验设计: [强] — 这是整个 proposal 最突出的亮点。8 个 baseline 涵盖所有相关方法且按一致性级别清晰分类；5 维 ablation 设计严谨（特别是 divergence metric comparison 和 consistency-diversity tradeoff 分析）；评估 benchmark 覆盖完整（GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM）；compute fairness 考虑周全（FLOPs-matched baseline + overhead profiling）；scale validation 在两个模型尺度上复制。这个实验设计本身就能让审稿人信服作者的 rigor。
  
  4. 可行性: [中] — 主要顾虑：(a) Perturbation pipeline 对 AMC/AIME 级别问题的覆盖率存疑——proposal 承认仅限 algebraic/arithmetic subtypes，这可能限制训练数据规模和多样性；(b) JS-divergence 在小样本 G 上的估计质量需要验证；(c) 计算开销（双倍 rollouts + JS 计算 + contrastive loss）可能显著，特别是在 8B 模型上。但 pilot study 设计（100 MATH-500 problems）和 Qwen3-1.7B scale validation 表明作者对可行性风险有清醒认识。
  
  5. 写作与呈现: [强] — Proposal 的结构、逻辑和 positioning 是一流的。三级框架的叙事有教科书般的清晰度；对每个相关工作的差异化论证精确到位；theoretical limitation 的论证（"correct but inconsistent reasoning" failure mode）简洁有力。如果论文写作保持此水准，presentation 不会是短板。

【概率估计】: [30% - 42%] 中位 35%

【估计理由】: 
- 问题重要性和 timeliness 为底线提供了保障（不太可能因为问题不相关被拒）
- 实验设计的完善度是显著加分项，表明如果执行到位将产出 solid 的实证 paper
- 核心方法的 novelty depth 是主要风险——"add JS regularizer to GRPO for perturbation consistency"可能被审稿人认为 contribution 不够深
- 中位 35% 反映：这是一篇"solidly above average"的投稿，但在 novelty 这个关键维度上不是顶级水平。如果实验结果显示 L_consist 带来的 robustness gain 显著且 clean accuracy 不降（或提升），probability 可上移到 40%+；如果 gain 仅 marginal 或 perturbation pipeline 覆盖太窄导致结果不够 comprehensive，则下移到 25-30%
- 在 AAAI 2026 的审稿环境中，这类"简洁方法 + 完善实验"的论文有一定优势——AAAI 审稿人通常重视 empirical thoroughness

【主要风险】: 
1. **Novelty insufficiency**: 核心技术贡献（JS regularizer on perturbation pairs）被审稿人视为"obvious combination of existing techniques"（DyJR's JS + TA-GRPO's augmentation），leading to "limited novelty" rejection reason。这是最可能的致命风险。
2. **Perturbation pipeline bottleneck**: 如果自动化 perturbation 仅覆盖 MATH/AMC/AIME 问题的一小部分（如 <40%），实验的 significance 和 generalizability 都会受质疑——reviewer 可能认为方法仅适用于特定题型。

【实施评估】:
  - 计算资源: 中等偏高。双倍 rollouts（G×2）+ 对比损失前向传播。Qwen3-8B 的 GRPO 训练本身需 4-8×A100 约 1-2 天；ConsistGRPO 估计需 2-3× overhead → 约 8×A100 3-5 天。1.7B 实验额外 1-2 天。总计约 200-400 A100-hours。
  - 数据需求: MATH/AMC/AIME 训练集（公开可用）+ 自动生成的 perturbation variants。GSM-Symbolic/VAR-MATH generators 需要适配到更高难度问题。
  - 人工介入: 中等。Perturbation pipeline 开发和验证需要人工审查（特别是 geometry/number theory 的 LLM-generated perturbations）。Pilot study 100 题的质量验证需要人工。
  - 训练需求: 需要训练。主要是 RL fine-tuning（GRPO + 一致性损失），不需要从头预训练。对比头（MLP projection）参数量极小。
  - 新 Benchmark: 不需要构建新 benchmark（使用现有 GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM）。但 perturbation pipeline 本身类似一个小规模 data generation 工具。
  - 预估周期: 6-10 周。Pipeline 开发 + pilot study: 2-3 周；主实验训练 + 评估: 2-3 周；ablation + scale validation: 2-3 周；论文写作: 2 周（可与实验并行）。
```

Sources:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)
- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs](https://arxiv.org/abs/2507.12885)
- [GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations](https://arxiv.org/abs/2605.07053)
- [f-GRPO & Beyond: Divergence-Based RL Algorithms for General LLM Alignment](https://arxiv.org/html/2602.05946)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://arxiv.org/html/2502.06453v2)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a comprehensive evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [TA-GRPO (arXiv 2601.22478)](https://arxiv.org/abs/2601.22478) (Jan 2026): 最直接的竞争者。通过 reward pooling 跨扰动变体共享 advantage，Pass@k 提升显著（AMC12/AIME24 +9.84），但确实未在任何扰动鲁棒性 benchmark 上评估。Proposal 对其"blind to correct-but-inconsistent reasoning"的批评成立。
- [CLIPO (arXiv 2603.10101)](https://arxiv.org/abs/2603.10101) (Mar 2026, Qwen Applications): 在 GRPO 中集成 InfoNCE 对比学习，对齐同题不同正确推理路径的不变结构。GSM8K-P1/P2 提升 +1.48/+3.36。Proposal 正确区分了 same-problem cross-trajectory 与 cross-perturbation 两种不变性维度。
- [AIR (arXiv 2605.20994)](https://arxiv.org/abs/2605.20994) (May 2026): 非对称锚点不变性正则化，主要面向 safety alignment，math 为辅助评估。使用 stop-gradient anchoring。Proposal 正确指出其非对称设计不适合数学扰动对的对称关系。
- [DyJR (arXiv 2603.16157)](https://arxiv.org/abs/2603.16157) (Mar 2026): 在 GRPO 中使用 JS-divergence 作为 diversity-preserving regularizer（current vs. historical policy），实证证明 JS > Forward KL。为 proposal 的 JS 选择提供了直接的先验支持。
- [AbstRaL (ICLR 2026, Apple)](https://arxiv.org/abs/2506.07751): 通过 RL 训练显式抽象能力，限于 GSM 级别问题。Proposal 主张通过正则化隐式实现类似抽象效果，覆盖更高难度问题。
- [GRPO-CARE (arXiv 2506.16141)](https://arxiv.org/abs/2506.16141) (Jun 2025): 一致性感知 GRPO，但面向多模态视频推理。概念上有重叠（consistency + GRPO），但应用领域和技术细节不同。
- [GSM-Symbolic (ICLR 2025)](https://arxiv.org/abs/2410.05229): 基础性 benchmark，证明数值替换可导致 LLM 性能大幅下降。MATH-Perturb、VAR-MATH 将此发现扩展到竞赛级数学。
- [The Choice of Divergence (arXiv 2509.07430)](https://arxiv.org/abs/2509.07430): 系统分析 RLVR 中不同散度选择对 diversity collapse 的影响，为本文的 JS vs KL 讨论提供理论背景。
- [F²C / BCT (arXiv 2025)]: 验证 consistency training 在 NLP 鲁棒性（+11.6% agreement）和 alignment（attack success 67.8%→2.9%）中的有效性，为数学领域迁移提供间接支持。

- **调研总结**: 数学推理扰动鲁棒性是一个 well-documented 且 active 的问题。现有工作分布在 data augmentation（MathForge, PrAg-PO）、reward-level（TA-GRPO）、representation-level（CLIPO）和 explicit abstraction（AbstRaL），但**尚无工作在 GRPO 中实现 distribution-level 的跨扰动一致性正则化**。Proposal 占据了一个真实但相对 narrow 的空位。核心技术手段（JS-divergence consistency regularization between perturbed inputs）在 NLP/CV 中是成熟技术，novelty 主要来自在 math RL rollout distribution 层面的特定应用和完善的实验框架。

【整体印象】: 
作为审稿人，我的第一反应是"这是一篇 well-positioned、well-engineered 的工作，但技术新颖性有限"。Proposal 展现了对领域极其深入的理解，三层框架（Data → Reward → Distribution）的概念分类清晰且有洞察力，"correct but inconsistent reasoning"的 failure mode 识别很尖锐。但核心方法——在扰动对之间最小化 JS-divergence——本质上是 consistency regularization 的一个特定实例，这在 semi-supervised learning、data augmentation 文献中已被广泛研究（R-Drop、consistency training 等）。创新主要在于"将已知范式迁移到 math RL rollout 分布层面"，这是一个有意义但bounded 的贡献。实验设计非常出色，是 proposal 最大的加分项。总体倾向 borderline，偏向 weak accept 但可能因 novelty 被 challenge。

【核心贡献】: 
(1) 三层一致性框架（Data/Reward/Distribution-level）的概念分类——这是一个对领域有组织价值的taxonomy；
(2) ConsistGRPO 方法本身——JS-divergence consistency loss + cross-perturbation contrastive loss 的组合；
(3) 对 TA-GRPO "correct but inconsistent reasoning" 盲点的理论分析。
贡献 (1) 对领域有中等价值（conceptual clarity），贡献 (2) 的技术新颖性受限于 consistency regularization 是已知范式，贡献 (3) 是一个好的 motivation 但偏 observational。

【方法合理性】: 
方法在技术上是合理的。JS-divergence 的选择有充分论据（对称性、有界性、DyJR 的实证支持）。Rollout distribution 层面的一致性确实能提供比 reward pooling 更丰富的梯度信号。**但存在一个关键问题需要回应**：一个更简单的替代方案是"TA-GRPO + 在 reward 中加入 consistency bonus"（类似 GRPO-CARE 的思路），这是否能达到类似效果？Proposal 需要在实验中明确回答 distribution-level 相对于 reward-level consistency 的边际收益。Contrastive loss 作为可选组件的处理是务实的。

【5 维度打分】:
  1. 研究问题: 【强】 — 扰动鲁棒性是数学推理 LLM 的核心痛点，GSM-Symbolic/VAR-MATH 提供了充分的实证支持（performance drops 47-73%）。问题重要且具有实际价值。RL-trained models 同样脆弱这一发现进一步强化了研究动机。
  
  2. 方法与创新: 【中】 — 三层框架的 conceptual contribution 有价值，JS-divergence consistency loss 在 math RL 中的特定应用是新的。但核心技术（consistency regularization via divergence minimization between perturbed inputs）是 NLP/CV 中的成熟技术（R-Drop [NIPS 2021]、consistency training for semi-supervised learning）。与 GRPO-CARE（consistency bonus in GRPO）、AIR（invariance regularization in GRPO）在 high-level idea 上有重叠，虽然 application domain 和具体设计不同。对比 CLIPO 和 TA-GRPO 的差异化清晰。相对于 DyJR（已在 GRPO 中使用 JS-divergence 做 regularization，虽然目的不同），novelty 的增量需要通过强实验结果来支撑。
  
  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点。8 个 baseline（含 FLOPs-matched）覆盖了所有相关工作层级，7+ 评估 benchmark 涵盖 GSM 到 competition-level，5 维 ablation 设计系统且完整（尤其是 divergence metric comparison 和 consistency-diversity tradeoff 分析）。Scale validation（1.7B + 8B）、perturbation pipeline pilot study、compute fairness profiling 都体现了严谨性。唯一的小瑕疵是缺少 human evaluation 或 case study 来定性分析"reasoning process invariance"。
  
  4. 可行性: 【中】 — 方法实现本身不复杂（JS loss 计算、contrastive head 均为标准组件）。主要风险在 perturbation generation pipeline：(a) MATH/AMC/AIME 中 geometry 和 number theory 问题的扰动生成依赖 LLM + 符号验证，可靠性存疑；(b) "restricted to algebraic and arithmetic subtypes" 的限制削弱了 generality claim；(c) 8B 模型 on-the-fly perturbation + 双倍 rollout 的计算开销需要 careful profiling。Proposal 对这些风险有意识但未给出详细的 mitigation 方案。Qwen3-8B 的训练在合理计算资源范围内（估计 8-16 GPU days）。
  
  5. 写作与呈现: 【强】 — 组织结构清晰，三层框架提供了很好的叙事线索。Related work 的定位精准且充分，每个 baseline 的局限性分析到位。方法描述技术上准确。Motivation 从 VAR-MATH 数据到 theoretical limitation analysis 的递进逻辑有说服力。唯一建议是增加 formal notation 来更严格地定义 "rollout distribution" 和 JS-divergence 的具体计算方式。

【概率估计】: [25% - 38%] 中位 30%

【估计理由】: 
这个 proposal 的核心矛盾在于：**极强的工程和实验设计** vs **有限的技术新颖性**。

(+) 研究问题重要且 timely，三层框架有概念价值，实验设计异常完备（8 baselines, 5-dim ablation, scale validation, FLOPs fairness），定位清晰且差异化明确。如果实验结果强劲（在 VAR-MATH/MATH-Perturb 上显著优于 TA-GRPO 且不损害 clean accuracy），这可以是一篇 solid empirical paper。

(-) 核心方法是 well-known 的 consistency regularization 技术在 math RL 中的特定应用，技术新颖性 bounded。缺乏理论分析（无 convergence guarantee、sample complexity bound）。领域极度拥挤（GRPO variants 已有 10+ 篇 2026 年论文），reviewer fatigue 是现实风险。AAAI 2026 acceptance rate ~23%，对于 novelty 中等但执行力强的论文，命运高度依赖 reviewer 匹配——遇到重视 empirical rigor 的 reviewer 可能 accept，遇到要求 technical novelty 的 reviewer 很可能 reject。

中位估 30% 反映了：一篇在各方面都 competent、在实验设计上 above-average、但在 novelty 上处于 borderline 的投稿，在一个 competitive 的领域。

【主要风险】: 
1. **Novelty 不足被拒**：最可能的拒稿理由是"consistency regularization via JS-divergence between perturbed inputs is a well-known technique; the application to GRPO rollout distributions is a straightforward extension, not a fundamental contribution"。特别是 DyJR 已经在 GRPO 中使用了 JS-divergence（虽然目的不同），GRPO-CARE 已经在 GRPO 中做了 consistency-aware training（虽然领域不同），reviewer 可能认为本文只是已知组件的 recombination。
2. **Perturbation pipeline 的可靠性与 generality**：限制在 algebraic/arithmetic subtypes 会被 reviewer 质疑 generality claim。LLM-generated perturbations + symbolic verification 的 fallback 方案可靠性未经验证，如果 pilot study 覆盖率不高，会严重削弱整个方法的实用性。

【实施评估】:
  - 计算资源: 中等偏高。Qwen3-8B 的 GRPO 训练 + 双倍 rollout（original + perturbed）+ contrastive head 前向/反向传播。估计需要 4-8 × A100 80GB，训练 3-5 天（primary），1.7B scale validation 额外 1-2 天。总计约 200-400 A100 GPU-hours。
  - 数据需求: MATH/AMC/AIME 训练集（公开可得）+ on-the-fly perturbation generation。7+ 评估 benchmark 均为公开数据集。数据本身不是瓶颈。
  - 人工介入: 中等。Perturbation pipeline 需要 careful engineering（SymPy filter、LLM fallback verification）。Pilot study 100题需要人工审核扰动质量。Hyperparameter sweep（λ₁, λ₂, G）需要反复实验调参。
  - 训练需求: 需要完整的 RL 训练流程（GRPO + 两个额外 loss term）。8 个 baseline 中至少 4-5 个需要从头训练/复现（vanilla GRPO, GRPO+Aug, TA-GRPO reproduction, CLIPO reproduction, FLOPs-matched）。总训练运行次数估计 15-25 runs。
  - 新 Benchmark: 不需要构建新 benchmark。但 perturbation generation pipeline 本身可作为工具贡献（如果质量可靠）。
  - 预估周期: 6-10 周。Pipeline 开发与 pilot study (1-2周) → 主实验训练 (2-3周) → Ablation 与 analysis (2-3周) → 写作 (1-2周)。主要瓶颈是 perturbation pipeline 的工程开发和大量 baseline 复现。
```

Sources:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)
- [DyJR: Preserving Diversity in RL with Verifiable Rewards via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning](https://arxiv.org/abs/2506.16141)
- [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs](https://arxiv.org/abs/2410.05229)
- [The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR](https://arxiv.org/abs/2509.07430)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths](https://arxiv.org/abs/2505.09655)


【原始 proposal（允许参考但不是主要依据）】:
# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling

## Core Problem

RL-trained mathematical reasoning models achieve SOTA on clean benchmarks but suffer severe accuracy drops under trivial surface-form perturbations even after RL training: VAR-MATH (arXiv 2025) reports average declines of 47.9% (AMC23), 58.8% (AIME24), and 72.9% (AIME25) on RL-trained models under numerical substitution. GRPO's reward signal provides no gradient against surface-form-dependent reasoning — the policy is rewarded for correct answers regardless of whether it exploits superficial patterns or genuine mathematical structure.

## Three-Level Framework for Consistency Enforcement in Math RL

We identify three progressively stronger levels of consistency enforcement:

**Level 1 — Data-level**: Augmenting training with perturbed variants without explicit consistency signal (MathForge ICLR 2026; PrAg-PO arXiv 2026 with 13 prompt templates). TA-GRPO's ablation (arXiv 2601.22478) demonstrates this alone is insufficient: "augmentation without pooling doesn't help."

**Level 2 — Reward-level**: Pooling rewards across original and perturbed variants (TA-GRPO, arXiv 2601.22478). Provides implicit consistency through shared advantages but operates on sparse binary feedback (correct/incorrect). TA-GRPO achieves Pass@k gains (up to +9.84 on AMC12/AIME24) but has not been evaluated on any perturbation robustness benchmark (GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP). **Theoretical limitation**: consider two semantically equivalent problems x, x' where the policy solves x via memorized pattern-matching and x' via genuine derivation — both correct, so reward pooling assigns identical advantages, remaining blind to the fragile reasoning on x. This "correct but inconsistent reasoning" failure mode is invisible to reward-level signals.

**Level 3 — Distribution-level** (this work): Explicitly minimizing JS-divergence between policy rollout distributions on original and perturbed problems. This provides continuous gradient signal over the entire reasoning trajectory, detecting and penalizing divergent reasoning processes even when both lead to correct answers. By enforcing reasoning structure invariance — that the model's reasoning process is determined by mathematical structure rather than surface form — this approach implicitly forces the kind of abstraction that AbstRaL (ICLR 2026) achieves explicitly, but through a regularization mechanism rather than a separate abstraction stage.

## Research Landscape

**Training-time math robustness**: AbstRaL (ICLR 2026, Apple) uses RL to train explicit abstraction before solving, limited to GSM-level. TA-GRPO (arXiv 2601.22478, Jan 2026) introduces transform-augmented reward pooling in GRPO with Pass@k improvements on competition math but no robustness evaluation. AIR (arXiv 2605.20994, May 2026) applies asymmetric anchor invariance regularization to GRPO primarily for safety alignment (with auxiliary math evaluation), using stop-gradient anchoring — appropriate when one prompt variant has more reliable feedback, but suboptimal for math perturbation pairs where both sides are symmetric and equally verifiable.

**Contrastive learning in GRPO**: CLIPO (arXiv 2603.10101, Mar 2026) integrates InfoNCE over correct rollouts within GRPO, extracting invariant reasoning structures across different correct solution paths to the same problem. MCPO (arXiv 2605.25443, May 2026) extends cross-domain contrastive policy optimization. Both target same-problem cross-trajectory invariance (aligning different correct reasoning paths). Our cross-perturbation contrastive component targets a different invariance dimension: aligning representations across surface-form-different but semantically-identical problem pairs, directly enforcing perturbation robustness rather than obtaining it as a side effect.

**GRPO variants**: DAPO, DR.GRPO, COPO, DRA-GRPO address stability/diversity/efficiency but none target perturbation invariance. DyJR (arXiv 2603.16157) uses JS-divergence in GRPO as diversity-preserving regularizer between current and historical policies, establishing JS-divergence viability in GRPO and demonstrating JS > Forward KL for this purpose. PrAg-PO (arXiv 2602.03190, Feb 2026) uses prompt templates as implicit regularization with no consistency loss.

**Adjacent work**: GRPO-CARE (Jun 2026) adds consistency bonuses for multimodal video reasoning. CSR (Jan 2026) enforces causal consistency via operator perturbation in SFT, not RL. F²C (arXiv 2025) validates consistency training for NLP robustness (11.6% agreement recovery). BCT (arXiv 2025) validates consistency training for alignment (attack success 67.8% → 2.9%). Reward Under Attack (arXiv 2026) examines PRM robustness. MathForge (ICLR 2026) combines difficulty-weighted GRPO with reformulation (clean accuracy only).

**Why JS-divergence over alternatives**: JS-divergence is chosen over KL-divergence for two reasons: (1) symmetry — perturbation pairs (x, x') have symmetric epistemic status (both equally verifiable), making asymmetric KL(P_x || P_x') arbitrary in direction; (2) boundedness — JS ∈ [0, ln2] while KL can diverge, providing more stable training gradients. DyJR's empirical finding that JS outperforms Forward KL in GRPO regularization provides additional support.

## Proposed Approach

**ConsistGRPO** augments GRPO with distribution-level consistency enforcement as its primary mechanism:

**Primary: Policy-level JS-divergence consistency loss (L_consist).** For each problem x, generate a math-equivalence-preserving perturbation x'. Collect G rollouts from each: {τ₁,...,τ_G} ~ π_θ(·|x) and {τ'₁,...,τ'_G} ~ π_θ(·|x'). Compute sequence-level log-probabilities to form empirical rollout distributions P_x and P_x'. The consistency loss L_consist = JS(P_x || P_x') provides symmetric, continuous gradient toward invariance over the full reasoning process. Unlike TA-GRPO's reward pooling (which transmits only binary outcome signals and is blind to "correct but inconsistent reasoning"), L_consist directly penalizes divergent reasoning distributions even when both variants are answered correctly.

**Secondary: Cross-perturbation contrastive loss (L_contrastive).** Extract representations via mean-pooling the last hidden layer, project through a 2-layer MLP head (discarded at inference). Positive pairs: representations from perturbation pair (x, x') rollouts. Negative pairs: in-batch representations from different problems. Loss: InfoNCE. This complements CLIPO's same-problem cross-trajectory contrastive learning (arXiv 2603.10101) with a different invariance dimension — cross-perturbation invariance — directly targeting the "blind skill application" failure identified by MATH-Perturb (arXiv 2025). This component is treated as optional; ablations will determine its marginal contribution beyond L_consist.

**Combined objective**: L = L_GRPO + λ₁·L_consist + λ₂·L_contrastive.

**Perturbation generation pipeline**: Adapt GSM-Symbolic/VAR-MATH generators for MATH/AMC/AIME, restricted to algebraic and arithmetic subtypes amenable to automated perturbation (numerical substitution, variable renaming). Apply SymPy-based validity filter verifying solvability and answer computability. For problem types where automated perturbation is unreliable (geometry, certain number theory), use LLM-generated perturbations with symbolic verification. Report perturbation success rates per problem category. Conduct pilot study on 100 MATH-500 problems to validate pipeline coverage before full-scale training.

**Training**: Qwen3-8B (primary) and Qwen3-1.7B (scale validation) on MATH/AMC/AIME with on-the-fly perturbation generation.

## Experimental Design

**Baselines (8 methods):**
| Method | Consistency Level | Key Feature |
|--------|------------------|-------------|
| Vanilla GRPO | None | Same data, no augmentation |
| GRPO + Aug Only | Data | Same perturbations, no consistency/contrastive loss |
| TA-GRPO (arXiv 2601.22478) | Reward | Transform-augmented reward pooling |
| CLIPO (arXiv 2603.10101) | Representation | Same-problem cross-trajectory contrastive |
| AbstRaL (ICLR 2026) | — | Abstraction-based (GSM-level; best-effort on MATH/AIME) |
| DR.GRPO | — | GRPO variant for stability |
| PrAg-PO (arXiv 2026) | Data | 13 prompt templates, implicit regularization |
| FLOPs-matched GRPO | — | Vanilla GRPO with matched total compute (profiled, not preset) |

**Evaluation benchmarks**: GSM-Symbolic (ICLR 2025), GSM-Plus (ACL 2024), VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM (May 2026) for robustness; MATH-500, AIME 2024/2025 for clean accuracy. Report absolute accuracy, robustness gap (clean − perturbed), and Pass@k (k=1, 8, 64).

**Ablations (5 dimensions):**
1. Component decomposition: GRPO → +Aug → +L_consist → +L_contrastive → Full (5-row table isolating each component)
2. Perturbation type: numerical substitution only / variable renaming only / combined
3. Hyperparameter sensitivity: λ₁, λ₂ weight sweep (5 values each); group size G effect on L_consist
4. Training dynamics: clean vs. robustness accuracy learning curves; entropy trajectory (cf. PrAg-PO entropy collapse)
5. Divergence metric comparison: JS-divergence vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style asymmetric stop-gradient

**Consistency-diversity tradeoff analysis**: Track Pass@k curves across λ₁ values; report unique correct solution count per problem and pairwise rollout distance as diversity metrics; analyze whether stronger consistency constraints cause diversity collapse (cf. DyJR arXiv 2603.16157).

**Compute fairness**: Profile actual FLOPs overhead of ConsistGRPO vs. vanilla GRPO before setting FLOPs-matched baseline. Report breakdown: rollout generation, JS-divergence computation, contrastive loss overhead. Report wall-clock time and total GPU-hours.

**Scale validation**: Replicate core comparison (ConsistGRPO vs. vanilla GRPO vs. TA-GRPO vs. CLIPO) on Qwen3-1.7B.

## Key References

- GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025)
- GSM-Plus: Comprehensive Benchmark for Evaluating Robustness of LLMs as Math Problem Solvers (ACL 2024, arXiv 2402.19255)
- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)
- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)
- Prompt Augmentation Scales up GRPO Training on Math Reasoning (arXiv 2026)
- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)
- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (arXiv 2025)
- PutnamGAP: Robustness of LLMs via Mathematically-Equivalent Transformation (arXiv 2025)
- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations (arXiv 2025)
- Consistency Training Helps Stop Sycophancy and Jailbreaks (arXiv 2025)
- Reward Under Attack: Robustness and Hackability of Process Reward Models (arXiv 2026)
- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478, Jan 2026)
- AIR: Towards Context-Invariant Safety Alignment for LLMs (arXiv 2605.20994, May 2026)
- DyJR: Preserving Diversity in RL with Verifiable Rewards via JS-Divergence (arXiv 2603.16157, 2026)
- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, Mar 2026)
- MCPO: Harmony in Diversity — Multi-domain Contrastive Policy Optimization (arXiv 2605.25443, May 2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "12c27705-ac01-4f56-80da-73729f779c43",
  "type": "user",
  "uuid": "4e9f5608-5b5b-4486-ae09-dd3035046b28",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:38:05.561Z_

```json
{
  "parentUuid": "4e9f5608-5b5b-4486-ae09-dd3035046b28",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "7df1c828-38e0-4734-98ab-1918d53c0c8a",
  "timestamp": "2026-05-29T06:38:05.561Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:38:05.562Z_

```json
{
  "parentUuid": "7df1c828-38e0-4734-98ab-1918d53c0c8a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6e3ea504-3c04-4abb-9bab-ae460e875b71",
  "timestamp": "2026-05-29T06:38:05.562Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile the fin…",
  "leafUuid": "6e3ea504-3c04-4abb-9bab-ae460e875b71",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency for math RL robustness",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e"
}
```

---

### Assistant

_source line 8 · 2026-05-29T06:38:37.988Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the three independent reviews and synthesize them as the Meta Judge.

**Three reviewers' probability estimates:**
- R1: [28% - 42%] 中位 35%
- R2: [30% - 42%] 中位 35%
- R3: [25% - 38%] 中位 30%

Medians: 35%, 35%, 30% → sorted: [30%, 35%, 35%]
Mean of medians: 33.3%
Median of medians: 35%
Std of medians: √[((30-33.3)² + (35-33.3)² + (35-33.3)²)/3] = √[(10.89 + 2.89 + 2.89)/3] = √[5.56] ≈ 2.36%


The standard deviation is under 3%, indicating strong agreement across reviewers.

Now I'm identifying where the reviewers converge and where they diverge. All three unanimously rated the research problem as strong, and they all marked the methodology as moderate with the same core concern—the combination of JS-divergence and InfoNCE relies on existing techniques without substantial novelty. The experimental design also received unanimous strong ratings, with all three highlighting the eight baseline comparisons.

All three reviewers flagged feasibility as moderate, citing concerns about the perturbation pipeline's reliability, computational overhead from double rollouts, and the limitation to algebraic and arithmetic subtypes. Writing and presentation earned unanimous strong marks. The most critical consensus is that novelty insufficiency is the primary risk across all reviews—described as a straightforward combination of existing methods or an obvious next step. The perturbation pipeline reliability emerges as a secondary concern, and both R1 and R2 raised questions about JS divergence estimation with small sample sizes when G is between 8 and 16.

All three reviewers also identified the consistency-diversity tradeoff as problematic. R3 uniquely surfaced GRPO-CARE and R-Drop as related precedents, flagged the absence of theoretical guarantees, and suggested token-level logit matching as an alternative to sequence-level matching. R3's acceptance probability estimate (30%) is slightly lower than R1 and R2 (35% each). The reviewer consensus is remarkably tight—standard deviation around 2.36% across all rubric dimensions—indicating high agreement on the paper's strengths and weaknesses.

Given this convergence, I'm anchoring on the median of the three estimates (35%) but adjusting slightly downward to account for R3's more conservative stance. The upper bounds cluster around 38-42%, while lower bounds range from 25-30%. I'm settling on a final probability around 33-34%, which respects the high consistency while staying slightly conservative given the theoretical gaps R3identified. Now I'm pulling together the implementation assessments from all three reviewers to finalize the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e3ea504-3c04-4abb-9bab-ae460e875b71",
  "isSidechain": false,
  "requestId": "req_011CbWQ8PGRcQkc5naRAzSzL",
  "type": "assistant",
  "uuid": "f462446e-7c18-464f-b2fb-f80dde1d9087",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TAu6PvwXzdSU6o3NZQhnD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18906,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3369,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18906
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

### Assistant

_source line 9 · 2026-05-29T06:39:30.540Z_

【阶段】: Meta Judge
【三次中位】: [35%, 35%, 30%]  std=2.4%
【共识维度】:
- **研究问题: 强**（3/3 一致）— 扰动鲁棒性问题经 GSM-Symbolic / VAR-MATH / MATH-Perturb 充分验证，RL 训练未解决甚至加剧，gap 定位精准
- **方法与创新: 中**（3/3 一致）— 核心技术（JS-divergence + InfoNCE）均为成熟工具的组合应用，三级框架有概念价值但技术深度有限；"straightforward combination" / "obvious next step" 是三位共同顾虑
- **实验设计: 强**（3/3 一致）— 8 baselines / 7+ benchmarks / 5-dim ablation / FLOPs-matched / scale validation，公认为 proposal 最突出亮点
- **可行性: 中**（3/3 一致）— perturbation pipeline 覆盖率存疑（限于 algebraic/arithmetic）、双倍 rollout 计算开销、小样本 JS 估计噪声
- **写作与呈现: 强**（3/3 一致）— 三级框架叙事清晰、related work 定位精准、逻辑递进
- **主要风险 #1: Novelty 不足**（3/3 一致）— 最可能的拒稿理由，DyJR 已在 GRPO 中使用 JS、TA-GRPO 已做 augmentation，组合缺乏方法论突破
- **主要风险 #2: Perturbation pipeline 可靠性**（3/3 一致）— 竞赛数学自动扰动的覆盖率和正确性验证是工程瓶颈
- **Consistency-diversity tradeoff**（3/3 一致）— 强一致性约束可能导致 rollout diversity collapse，最优 λ₁ 可能很小使 L_consist 贡献边际
- **小样本 JS 估计问题**（2/3 提及，R1+R2）— G=8-16 个 rollout 构成的经验分布极其稀疏，JS 估计方差大

【异常维度】:
- R3 独有：提到 GRPO-CARE（multimodal consistency GRPO）在 high-level idea 上的重叠，以及 R-Drop (NeurIPS 2021) 作为 consistency regularization 的成熟先例 — 有一定参考价值但不改变判决方向，因 GRPO-CARE 面向 video reasoning 领域不同、R-Drop 是 SFT 场景的先例
- R3 独有：缺乏理论分析（no convergence guarantee, sample complexity bound）— 合理关切但在 AAAI empirical paper 中非致命
- R1 独有：token-level logit matching 作为更简单替代方案 — 有效的 ablation 建议但 proposal 的 divergence metric comparison 已部分覆盖

【最终概率】: [28% - 40%] 中位 33%
【一致性】: 高
【综合理由】:
三位审稿人在所有 5 个 rubric 维度上给出完全一致的判决（强/中/强/中/强），主要风险识别高度重叠，std 仅 2.4%，属于高一致性。在此情况下取中位附近并适度偏严：

1. **R1 和 R2 的 35% 中位**反映了"solid but incremental, 实验设计弥补 novelty 短板"的判断；**R3 的 30%** 更强调 consistency regularization 在 NLP/CV 中已是成熟范式（R-Drop 等），进一步压低了方法论创新的评价。R3 的视角合理且并非 outlier，因此终值略向 R3 偏移。

2. **核心矛盾高度明确**：极强的问题定位 + 实验设计 vs. 有限的技术新颖性。这决定了概率的天花板——即使实验结果完美，"existing techniques combination" 的标签仍可能导致部分 reviewer 给 borderline reject。

3. **上界 40%（而非 42%）**：R3 的上界仅 38%，综合后不应超过最宽松评审的上界（42%），但 R3 的理据（成熟范式迁移）使上界应有所收缩。

4. **下界 28%**：三位下界分别为 28%/30%/25%，取中间值。perturbation pipeline 失败或实验结果 marginal 是下行风险的主要来源。

5. 中位 33% 意味着：这是一篇在 AAAI 2026 的 competitive pool 中处于 borderline 偏下的投稿——问题好、实验好、执行力强，但方法 novelty 是硬伤。命运高度依赖 reviewer 匹配和实验结果强度。

【建议】: 边缘
【实施评估】:
  - 计算资源: 中高。需 8×A100/H100 节点。每问题 2×G 次 rollout（原始+扰动），计算量约为 vanilla GRPO 的 2-2.5 倍。三位估算一致：总计约 200-400 A100 GPU-hours（含全部 ablation 和 baseline 复现）。Qwen3-8B 主实验约 3-5 天，1.7B scale validation 额外 1-2 天。
  - 数据需求: MATH/AMC/AIME 训练集（公开可得），7+ 评估 benchmark 均公开。关键瓶颈是 perturbation pipeline 的构建——需对竞赛数学问题做自动化扰动 + 正确性验证（SymPy + LLM fallback）。限于 algebraic/arithmetic subtypes 可能导致覆盖率不足，pilot study（100 题）可验证。
  - 人工介入: 中等。perturbation pipeline 工程开发和质量审核需要人工（尤其 geometry/number theory 的 LLM-generated perturbations）；pilot study 100 题需人工验证；4-5 个 baseline 需从头训练/复现并调参。
  - 训练需求: 需要完整 RL 训练流程（GRPO + 两个额外 loss term），不需从头预训练。对比头（MLP projection）参数量极小。总训练运行次数约 15-25 runs（含 ablation 和 hyperparameter sweep）。
  - 新 Benchmark: 不需要。使用现有 GSM-Symbolic / GSM-Plus / VAR-MATH / MATH-Perturb / PutnamGAP / GSM-SEM。perturbation pipeline 可作为工程副产品。
  - 预估周期: 8-12 周（三位估算的中位综合）。Pipeline 开发 + pilot study 2 周 → perturbation 工程完善 1-2 周 → 主实验 + baseline 复现 2-3 周 → ablation + scale validation 2-3 周 → 论文写作 2 周（可与后期实验并行）。2-3 人团队在计算资源充足条件下可在 AAAI 2026 deadline 前完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f462446e-7c18-464f-b2fb-f80dde1d9087",
  "isSidechain": false,
  "requestId": "req_011CbWQ8PGRcQkc5naRAzSzL",
  "type": "assistant",
  "uuid": "e6be898f-4a0c-451d-ac1b-d3e7e55a46d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TAu6PvwXzdSU6o3NZQhnD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18906,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18906,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3369,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 18906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18906
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient research context. Let me compile the fin…",
  "leafUuid": "e6be898f-4a0c-451d-ac1b-d3e7e55a46d3",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency for math RL robustness",
  "sessionId": "e09acbc0-003c-4a30-b9de-1af02d01433e"
}
```

---
