# Research conversation: 【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。 【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/69038657-ab9a-4d76-b530-7cafdadb1db6.jsonl`
- **Structured JSON:** [`c4417ce0e4ee653ec5e6.json`](../../sessions/c4/c4417ce0e4ee653ec5e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T07:19:16.569Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T07:19:16.569Z",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6",
  "content": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。\n\n【三位审稿人评估】:\n━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━\nNow I have sufficient information to produce a thorough evaluation. Let me compile my analysis.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055): 12 LLMs × 41,871 items 的 IRT 分析，发现 benchmark 饱和与难度天花板问题。假设零污染——正是本 proposal 要突破的局限。\n- JECS (arXiv 2605.21543, 2026): 首个提供 conformal per-item 污染 p-value 并实现 GCR 控制的方法。本 proposal 将其 pre-aggregation p-value 作为 IRT 先验，属下游应用而非竞争关系。\n- MATH-Perturb (ICML 2025): o1-mini 在 hard perturbation 上下降 16.49%。仅 answer-level，无 step-level 分析。\n- VAR-MATH (arXiv 2507.12885): RL 模型在符号变体上下降 47–73%。提供 SymPy-backed 变体生成方法论，本 proposal 直接复用。仅 answer-level。\n- RIDE (arXiv 2511.04120): IRT→perturbation 方向（用 IRT 难度估计指导对抗性扰动生成），与本 proposal perturbation→IRT 方向互补而非竞争。\n- DCR Factor (EMNLP 2025): 通过模糊推理系统对 9 个模型进行 ad-hoc 污染校正，平均误差 ~4%。无 IRT 基础，无 step-level 分析。\n- GenPRM (AAAI 2026): 生成式过程奖励模型，GenPRM-1.5B 超越 GPT-4o。本 proposal 用其做 step-level verification。\n- Illusion of Reasoning (arXiv 2603.22816, 2026): 13 个前沿模型的 step-level faithfulness 评估，发现三种 CoT 模式（genuine/scaffolding/decoration），step necessity 4–93%。仅单问题分析，无扰动交互。\n- Robust Answers Fragile Logic (arXiv 2505.17406): 提出 Decoupling Hypothesis 和 MATCHA 框架，发现模型在对抗扰动下维持正确答案但推理崩溃。本 proposal 的 SPA 是对此假说的首个心理计量操作化。\n- CoDeC (ICLR 2026): 99.9% AUC 的污染检测，但检测而不校正。\n- Growing Pains (arXiv 2604.12843, 2026): 400+ 模型的多维 IRT，明确指出污染威胁 anchor 稳定性但未建模。\n- Reasoning or Memorization (arXiv 2507.10532, 2025): 证明 Qwen2.5 的 RL 提升是污染伪影，需构建全新 synthetic dataset (RandomCalculation) 才能证明——正是本 proposal CAS-IRT 声称能更低成本解决的场景。\n\n- 调研总结: LLM 评估的 IRT 方向（PSN-IRT, Growing Pains, ATLAS）、污染检测方向（JECS, CoDeC, DVD）、扰动鲁棒性方向（MATH-Perturb, VAR-MATH, RIDE）三条线在 2025-2026 快速发展但彼此独立。**目前没有任何已发表或预印工作将 IRT 估计、污染校正和 step-level 扰动分析统一在一个框架内。** 本 proposal 的定位是这三个方向的交叉点，novelty claim 成立。\n\n【整体印象】:\n作为审稿人，我的第一反应是\"这是一篇精心设计、定位精准的 systems paper\"。Proposal 展现了对领域格局的深刻理解，准确识别了一个真实且重要的 gap（IRT 评估假设零污染，污染检测不校正能力估计，扰动分析仅 answer-level），并提出了一个技术上合理的统一框架。实验设计的完备性（6 个 baseline、系统性 ablation、多层验证）是显著的加分项。\n\n倾向 **weak accept**，但以下几点让我犹豫：(1) 框架复杂度高，有 over-engineering 之嫌；(2) 3PL mixture 在 N=50-100 的 identifiability 是真实风险；(3) 论文需要极好的写作才能让审稿人在有限时间内理解全部贡献。\n\n【核心贡献】:\n1. **CAS-IRT 框架本身**：首个在 IRT 框架内联合建模 genuine ability、contamination susceptibility 和 robustness deficit 的方法。相比 DCR Factor 的 ad-hoc 校正和 detect-then-discard 的信息浪费，这是概念上的显著进步。\n2. **SPA 指标**：首次将 step-level 推理与 perturbation 的结构依赖关系结合，提供了超越 answer-level 的污染/记忆化诊断信号。这是 Decoupling Hypothesis 的首个可计算操作化。\n3. **三社区统一**：bridging 污染检测、对抗鲁棒性和心理计量评估三个原本独立的研究方向，这种 unification 本身就是对领域的贡献。\n\n这些贡献对领域有较高价值：如果 CAS-IRT 的 identifiability 问题能被解决，它将改变社区评估 LLM 能力的方式——从\"不断构建新 benchmark 来逃避污染\"转向\"在现有 benchmark 上做诊断性分解\"。\n\n【方法合理性】:\n方法整体合理，各组件有理论或实证基础：\n- 3PL IRT 的 contamination mixture 扩展在概念上自然，JECS p-value 作为 informative prior 是巧妙的解决方案。\n- SPA 的核心思想——检查推理步骤的变化是否与 SymPy dependency graph 的结构依赖一致——逻辑严密。\n- EM 估计有 human psychometrics 中 rapid-guessing detection 的先例。\n\n**更简单的替代方案**：一个合理的 reviewer concern 是\"为什么不直接用 detect-then-filter（JECS 过滤污染项 → 标准 IRT）？\"——proposal 将此作为 Baseline 2 并声称 CAS-IRT 通过 continuous modeling 和 cross-item information borrowing 更优。这是可以实验验证的 claim，但如果 detect-then-filter 表现接近，CAS-IRT 的额外复杂度就难以证明。这是方法论上最大的风险。\n\n另一个 concern：additive decomposition（Observed = Genuine + Contamination − Robustness）是否过度简化？交互项扩展是好的补救措施，但如果 BIC/AIC 选择了交互模型，additive 叙事就需要调整。\n\n【5 维度打分】:\n  1. 研究问题: 【强】— LLM benchmark 评估被污染混淆是一个真实、紧迫且影响广泛的问题。PSN-IRT (AAAI 2026 Oral) 和 Growing Pains (arXiv 2604.12843) 都明确指出 IRT 评估中污染的未解决问题。\"Reasoning or Memorization\" (arXiv 2507.10532) 展示了 RL 训练中污染的严重后果。这个 decomposition 问题对整个 LLM 评估社区有直接实用价值。\n\n  2. 方法与创新: 【强】— 核心 novelty claim 经调研确认成立：(a) 无已有工作将 IRT 与污染校正联合建模（PSN-IRT 假设零污染，DCR Factor 无 IRT）；(b) SPA 的 step×perturbation 交互是新的（MATH-Perturb/VAR-MATH 仅 answer-level，Illusion of Reasoning 仅单问题）；(c) 与 RIDE 的互补关系（方向相反）定位清晰。唯一扣分点：框架组件过多，novelty 分散在多个 contribution 中，需要清晰的叙事来统一。\n\n  3. 实验设计: 【强】— 这是本 proposal 最突出的优势之一。6 个 baseline 覆盖了所有合理的替代方案（标准 IRT、detect-then-filter、DCR Factor、raw accuracy、answer-level CAS-IRT、non-IRT pipeline）。Ablation 设计系统性极强（5 种配置 + 多个维度的变体）。三层验证（synthetic recovery、known-contamination、predictive on held-out）是金标准。AIME 2026/AMC 2026 作为 contamination-free held-out 的选择有说服力。Human gold standard 的标注预算（250+ pairs, 2+ annotators, Cohen's κ）也显示了严谨性。按照 MATH-Perturb 和 VAR-MATH 的实验标准，这个设计已经超标。\n\n  4. 可行性: 【中】— 计算资源需求（700-800 GPU-hours, $5k-10k API）对有一定资源的研究组可行。但以下依赖链条令人担忧：(a) SymPy 变体生成的品类覆盖率（geometry, combinatorics 可能低覆盖），(b) GenPRM 在 variant 上的表现是未验证假设，(c) JECS pre-aggregation p-value 的提取需要重现 JECS pipeline，(d) 150-200 person-hours 的人工标注是显著投入，(e) 10-14 周时间线紧凑。任何一个环节出问题都可能影响全局。Proposal 包含了 fallback 策略（per-model c, algebra-only subset），这是好的，但复杂度仍然高。\n\n  5. 写作与呈现: 【中】— 作为 proposal，信息密度极高，展示了深入的领域知识。但这也是双刃剑：AAAI 论文通常 8 页（含 references），要在有限篇幅内清晰传达 CAS-IRT 框架、SPA 指标、三社区统一、完整实验设计，写作难度很高。如果处理不好，审稿人可能觉得\"贪多嚼不烂\"。建议在正文中聚焦 CAS-IRT + SPA 的核心故事，将部分 ablation 和 tiered evaluation 细节移至 appendix。此外，proposal 中对 related work 的 differentiation 虽然精确，但需要更简洁的叙事——一个清晰的 figure 或 table 比 20 条文字对比更有效。\n\n【概率估计】: [33% - 48%] 中位 40%\n\n【估计理由】:\n上界 48%——如果实验结果清晰验证了 CAS-IRT 相对 detect-then-filter 和 DCR Factor 的优势、SPA 指标展示了直观的 memorization signature、写作清晰到位，这篇论文具备 solid accept 的潜力。PSN-IRT 拿到了 AAAI 2026 Oral 说明 IRT-for-LLM 方向受认可，CAS-IRT 作为其 contamination-aware 后继有天然的叙事。\n\n下界 33%——如果 (a) identifiability 实验显示 N=50 regime 下参数恢复不理想需要 fallback 到简化模型，(b) CAS-IRT 相比 detect-then-filter 的改进幅度有限（\"这么复杂值得吗？\"），(c) 论文篇幅限制导致方法和实验阐述不充分，(d) 某位审稿人对 additive decomposition 的理论基础提出根本质疑，都可能导致 borderline reject。\n\n中位 40%——这是一篇 above-average 的投稿。研究问题和创新性都过线，实验设计远超平均水平，但框架复杂度和 identifiability 风险使其不是\"稳中\"的水平。AAAI 的接收率约 23-25%，这篇位于中稿线附近偏上。\n\n【主要风险】:\n1. **Identifiability + \"何必这么复杂\"的双重质疑**：3PL contamination mixture 在有限模型数（N~50-100）下的 identifiability 是最大技术风险。如果 synthetic recovery 显示需要 fallback 到简化模型（per-model c），框架的核心叙事（per-item contamination modeling）就被削弱。同时，如果 CAS-IRT 相对 Baseline 2（detect-then-filter）的改进有限，审稿人会质疑整个框架的必要性——Occam's razor 是强有力的反对理由。\n2. **论文组织与范围控制**：Proposal 包含 4 个核心贡献 + 6 个 baseline + 10+ ablation 维度 + 三层验证。在 8 页正文中清晰呈现这一切的写作难度极高。如果叙事不够凝练，审稿人可能感到 overwhelmed 并质疑 focus。\n\n【实施评估】:\n  - 计算资源: 700-800 A100-80G GPU-hours (open-weight models) + $5k-10k API (closed-source)。对有 GPU 集群的研究组可行，但 671B MoE 的多 GPU 推理和 100+ 模型的 batch inference 有工程复杂度。\n  - 数据需求: MATH-500, AMC, AIME, GSM8K (公开)；AIME 2026/AMC 2026 作为 held-out (公开)；FrontierMath (Epoch AI, 需要申请访问权限，且质量审核进行中)。核心数据均可获取。\n  - 人工介入: ~200 person-hours (250+ pairs × 2 annotators)。这是显著投入，需要具备数学背景的标注者。半自动 pipeline 可降低但不消除此成本。\n  - 训练需求: 无模型训练（evaluation-time framework）。需运行 GenPRM-1.5B inference 和 JECS pipeline，但均有开源实现。\n  - 新 Benchmark: 不需要构建新 benchmark，但需要生成数千个 SymPy-backed algebraic variants。这是本质上的 benchmark 扩展工作。\n  - 预估周期: 10-14 周（含 pilot study）。紧凑但可行，前提是团队 2-3 人全职投入且无重大技术障碍。\n```\n\nSources:\n- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)\n- [JECS: Provable Joint Decontamination](https://arxiv.org/abs/2605.21543)\n- [MATH-Perturb (ICML 2025)](https://openreview.net/forum?id=OZy70UggXr)\n- [VAR-MATH: Symbolic Multi-Instance Benchmarks](https://arxiv.org/abs/2507.12885)\n- [RIDE: IRT-Guided Difficulty Perturbation](https://arxiv.org/abs/2511.04120)\n- [DCR Factor (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)\n- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)\n- [The Illusion of Reasoning](https://arxiv.org/abs/2603.22816)\n- [Robust Answers, Fragile Logic: Decoupling Hypothesis](https://arxiv.org/abs/2505.17406)\n- [CoDeC: Contamination Detection via ICL (ICLR 2026)](https://openreview.net/forum?id=YlpaaYxx4t)\n- [Growing Pains: IRT Anchor Calibration](https://arxiv.org/abs/2604.12843)\n- [Reasoning or Memorization? RL Data Contamination](https://arxiv.org/abs/2507.10532)\n\n━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━\nNow I have sufficient information to provide a thorough evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055): 将IRT应用于LLM评估的里程碑工作，分析12个LLM × 41,871 items，发现现有benchmark的测量质量缺陷。假设零contamination——CAS-IRT直接填补这一空白。PSN-IRT拿到Oral说明AAAI对IRT-for-LLM方向高度认可。\n- Growing Pains (arXiv 2604.12843, 2026): 多维IRT框架，400+ models，使用anchor items实现跨时间可比性。明确提到contamination威胁anchor稳定性但未建模——进一步确认contamination-aware IRT是公认的open problem。\n- JECS (arXiv 2605.21543, 2026): 首个提供conformal per-item contamination信号的方法，GCR控制有理论保证。CAS-IRT将其作为IRT prior的关键输入，时间线吻合（2026年5月）。\n- CoDeC (ICLR 2026): 基于in-context learning的contamination检测，99.9% AUC。仅检测不纠正——与CAS-IRT的\"检测+校正\"定位互补。\n- DCR Factor (EMNLP 2025): 通过fuzzy inference system调整分数，9个模型，~4% error。缺乏IRT理论支撑，ad-hoc性质明显——CAS-IRT的对比优势清晰。\n- RIDE (arXiv 2511.04120): IRT→perturbation方向（用IRT难度指导扰动生成），35 LLMs，21.73% drop。CAS-IRT是perturbation→IRT方向（用扰动响应改善能力估计）。两者互补非竞争，差异化清晰且重要。\n- MATH-Perturb (ICML 2025): answer-level perturbation robustness benchmark，o1-mini -16.49%。仅answer-level，不做step-level分析——SPA的step×perturbation交互是真正的新增维度。\n- VAR-MATH (arXiv 2507.12885, 2025): SymPy-backed符号变体生成，RL模型drop 47-73%。提供了可复用的variant generation基础设施，CAS-IRT可直接利用。\n- Illusion of Reasoning (arXiv 2603.22816, 2026): 发现三种CoT模式（genuine/scaffolding/decoration），step necessity 4-93%。提供step-level faithfulness理论基础，但无perturbation交互——SPA结合两者。\n- Robust Answers Fragile Logic (arXiv 2505.17406, 2025): 提出Decoupling Hypothesis并通过MATCHA验证。CAS-IRT的SPA声称提供该假说的首个psychometric operationalization。\n- Scalable IRT for 2211 Models (arXiv 2605.07046, 2026): 大规模IRT应用，同样假设零contamination。\n- 调研总结: IRT-for-LLM在2025-2026经历爆发式增长（PSN-IRT获AAAI Oral、Growing Pains 400+模型、2211模型大规模应用），但所有现有工作均假设零contamination。同时contamination检测（JECS/CoDeC）和perturbation robustness（MATH-Perturb/VAR-MATH）各自成熟但未与IRT整合。CAS-IRT的\"三社区统一\"在时间窗口上确实是2025-2026才变得可行的方向，proposal对这一gap的定位是准确的。\n\n【整体印象】: \n作为审稿人，第一反应是\"这是一篇 ambitious 且 well-crafted 的 proposal\"。研究问题重要且 timely（所有现有IRT工作都假设零contamination），方法论路径有psychometric传统支撑（EM-IRT rapid-guessing detection的类比恰当），文献综述极为全面，差异化论证清晰有力。实验设计的完备程度（6个baselines、13+ablation configurations、三级validation、tiered evaluation）在proposal阶段罕见。我的倾向是 **weak accept**，但有两个需要关注的风险：(1) 框架复杂度是否会让reviewer感到\"too many moving parts\"；(2) SPA的实际operationalization能否达到proposal中描述的精度。如果实验结果能证明CAS-IRT在held-out benchmark预测上显著优于standard IRT和detect-then-filter，这将是一篇有影响力的工作。\n\n【核心贡献】: \n核心贡献是将LLM的benchmark表现分解为genuine ability、contamination susceptibility和robustness deficit三个可解释的组分，并通过IRT框架提供了有理论支撑的联合估计方法。具体而言：\n(a) CAS-IRT框架本身——contamination-aware的IRT扩展，相比DCR Factor的ad-hoc调整和detect-then-filter的信息丢失，提供了principled的替代方案；\n(b) SPA metric——首个在step×perturbation交互层面区分memorization和genuine reasoning的指标；\n(c) 三社区统一——将原本独立发展的contamination detection、perturbation robustness和IRT-based evaluation整合为统一框架。\n对领域的价值中等偏高：如果框架可行，它改变了LLM evaluation的paradigm——从\"defense by obsolescence\"（不断造新benchmark）到\"diagnostic decomposition on existing benchmarks\"。但实际影响取决于框架的adoption barrier（复杂度较高）。\n\n【方法合理性】: \n方法的整体思路是合理的——用contamination信号作为IRT的mixture prior，用perturbation response pattern提供robustness信号，用step-level alignment作为fine-grained memorization探针。每一步都有psychometric或统计学传统支撑。\n\n但需要关注的是\"更简单替代方案\"的问题：\n(1) **Detect-then-filter**（baseline 2）是最直接的替代——JECS检测contaminated items后直接剔除，对剩余items做standard IRT。CAS-IRT需要证明联合估计显著优于这种简单方法。如果优势微小，reviewer会质疑复杂框架的必要性。\n(2) **Non-IRT pipeline decomposition**（baseline 6）是另一个关键对比——直接在clean/contaminated/variant子集上分别计算accuracy，加权组合。如果这种简单pipeline效果接近CAS-IRT，IRT joint estimation的价值就会被质疑。\n(3) **Additive分解假设**（Observed = Genuine + Contamination − Robustness）的first-order approximation性质需要实验验证。Proposal提到了interaction term extension和BIC/AIC model selection，这是好的safeguard。\n\n总体而言，方法论路径合理但复杂，\"必要性证明\"将是reviewers重点关注的。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】— 所有现有IRT-for-LLM工作（PSN-IRT、Growing Pains、metabench、2211-model scaling）均假设零contamination，而contamination已被多个独立工作（CoDeC 99.9% AUC、JECS、Reasoning or Memorization的Qwen2.5案例）证实为严重问题。在IRT-for-LLM进入大规模应用的关键时期（2025-2026），contamination-aware IRT是一个clearly important且timely的research question。PSN-IRT获AAAI 2026 Oral进一步验证了AAAI对此方向的兴趣。\n\n2. 方法与创新: 【中偏强】— SPA（step×perturbation alignment）是genuinely novel的贡献，无先前工作在此层面操作（MATH-Perturb/VAR-MATH仅answer-level，Illusion of Reasoning无perturbation交互，EvalQReason无perturbation，PEARL用bit-flip而非structural variant）。CAS-IRT框架将JECS prior集成到3PL IRT中是principled但相对incremental的扩展。与RIDE的方向对比（IRT→perturbation vs. perturbation→IRT）是清晰的差异化。主要风险在于\"组合式创新\"——每个组件（JECS、SymPy variants、GenPRM、3PL IRT）均为已有工作，novelty来自整合。部分reviewers可能认为这是\"engineering contribution\"而非\"research contribution\"。\n\n3. 实验设计: 【强】— 这是proposal最突出的优势之一。6个精心选择的baselines覆盖了所有合理的替代方案（standard IRT、detect-then-filter、DCR ad-hoc、raw accuracy、answer-level CAS-IRT、non-IRT pipeline）。Ablation design系统性极强，13+配置涵盖每个组件的贡献。三级validation（synthetic recovery、known-contamination、predictive on held-out benchmarks）层层递进。Tiered evaluation（15 flagship + 80-100 open-weight）在规模和可行性之间取得了好的平衡。Identifiability safeguards（N=50 recovery作为primary报告、per-model c fallback）体现了对psychometric方法论的deep understanding。AIME 2026/AMC 2026作为contamination-free validation是clever的设计。\n\n4. 可行性: 【中】— 计算资源需求合理（700-800 GPU-hours + $5K-10K API），在标准学术实验室可承受范围内。10-14周时间线偏紧但可行。主要风险：(a) SPA的SymPy dependency graph对geometry/combinatorics的覆盖不足，LLM-assisted perturbation引入方法异质性；(b) GenPRM在variant上的step-level验证准确性未知（proposal有pilot study计划但结果不确定）；(c) 3PL mixture model在N=50 models时的identifiability——如果recovery差，需要fallback到per-model c，削弱了per-item contamination建模的核心贡献；(d) 人工标注250+ pairs需要~150-200 person-hours，对标注质量一致性有要求。\n\n5. 写作与呈现: 【强】— Proposal的结构清晰，逻辑链条完整。文献综述几乎涵盖了所有relevant工作（2025-2026的最新成果），差异化论证精准（特别是vs. RIDE、vs. DCR Factor、vs. DeconIEP的对比）。\"Three-Community Unification\"的framing有效传达了贡献的scope。技术细节（EM estimation、identifiability safeguards、variant generation protocol）的呈现既专业又可读。时间窗口论证（为何2025-2026才可行）增强了说服力。\n\n【概率估计】: [32% - 42%] 中位 37%\n\n【估计理由】: \n正面因素：(1) 研究问题重要且timely，精准对应IRT-for-LLM领域的核心盲点（contamination assumption）；(2) PSN-IRT获AAAI 2026 Oral证明AAAI对IRT-for-LLM方向友好；(3) SPA是genuinely novel的技术贡献；(4) 实验设计在proposal阶段罕见地完备，baselines和ablation覆盖全面；(5) 文献综述和差异化论证的质量极高。\n\n负面因素：(1) 框架复杂度高——组合了JECS + SymPy variants + GenPRM/step-ablation + 3PL IRT + EM，reviewer可能质疑是否over-engineered；(2) \"组合式创新\"的novelty perception风险——每个组件均非原创，reviewer可能认为主要贡献是\"engineering integration\"；(3) identifiability在小N regime下的不确定性——如果N=50 recovery不佳，核心主张弱化；(4) SPA的operationalization高度依赖SymPy和GenPRM的可靠性，存在execution risk；(5) additive decomposition是simplifying assumption，可能被challenge。\n\n综合判断：这是一篇整体扎实、方向正确、设计完备的proposal，但复杂度和\"组合式创新\"的定位使其处于borderline区间。如果实验能证明CAS-IRT显著优于detect-then-filter（最简单的替代方案），且SPA确实提供了answer-level分析无法获得的洞察，中稿概率会偏向上界。如果实验结果marginal improvement，则偏向下界。\n\n【主要风险】: \n1. **\"组合式创新\" vs. \"原创研究\"的perception问题**：3位reviewer中如果有1位认为\"只是把现有工具拼在一起\"（JECS + SymPy + GenPRM + IRT），给出weak reject，这将是最常见的reject理由。Proposal需要通过ablation证明joint estimation不可被简单pipeline替代——但这取决于实验结果。\n2. **CAS-IRT vs. detect-then-filter的marginal improvement风险**：如果JECS已经能高效检测contaminated items，简单剔除后做standard IRT就可能达到接近CAS-IRT的效果。如果held-out benchmark预测上CAS-IRT的优势不够显著（例如Spearman ρ提升 < 0.05），reviewer会认为复杂框架不值得。\n\n【实施评估】:\n  - 计算资源: 700-800 A100 GPU-hours + $5K-10K API cost，中等规模，标准学术实验室可承受。Tier 2的vLLM batch inference设计合理地降低了成本。\n  - 数据需求: MATH-500、AMC、AIME、GSM8K均为公开benchmark。SymPy-backed variants需要自行生成（有VAR-MATH基础设施可借鉴）。AIME 2026/AMC 2026作为held-out validation需等待竞赛数据公开。\n  - 人工介入: ~200 person-hours（250+ pairs标注 + pilot studies），需要2+名具有数学专业背景的标注人员。Semi-automated pipeline降低了成本但对pipeline质量有要求。\n  - 训练需求: 不需要训练新模型。GenPRM-1.5B为现有模型。EM estimation是统计优化，非深度学习训练。\n  - 新 Benchmark: 不构建新benchmark，但需要生成SymPy-backed variants（实质上是variant dataset construction）。\n  - 预估周期: 10-14周（Proposal自估），偏紧但对于evaluation-focused工作基本可行。关键路径：variant generation + human annotation可能成为瓶颈。\n```\n\nSources:\n- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)\n- [Growing Pains: Extensible LLM Benchmarking via Fixed Parameter Calibration](https://arxiv.org/abs/2604.12843)\n- [JECS: Provable Joint Decontamination](https://arxiv.org/html/2605.21543)\n- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/abs/2510.27055)\n- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)\n- [RIDE: Difficulty Evolving Perturbation with IRT](https://arxiv.org/abs/2511.04120)\n- [MATH-Perturb: Benchmarking LLMs' Math Reasoning (ICML 2025)](https://arxiv.org/abs/2502.06453)\n- [VAR-MATH: Symbolic Multi-Instance Benchmarks](https://arxiv.org/abs/2507.12885)\n- [The Illusion of Reasoning: Step-Level Evaluation](https://arxiv.org/abs/2603.22816)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)\n- [Scalable IRT for 2211 Models](https://arxiv.org/abs/2605.07046)\n\n━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━\nNow I have sufficient research to provide a comprehensive evaluation. Let me compile my assessment.\n\n---\n\n```\n【阶段】: Triage\n\n【领域调研】:\n- PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055): 最直接的IRT-for-LLM前作。分析12 LLMs × 41,871 items，发现benchmark饱和与难度天花板。关键局限：完全不建模contamination，假设所有response pattern来自genuine ability。CAS-IRT直接继承并扩展其框架。\n- JECS (arXiv 2605.21543, May 2026): 提供conformal per-item contamination p-values，实现GCR控制。CAS-IRT将JECS的pre-aggregation p-values作为IRT contamination prior——这是一个创造性的跨框架复用，但JECS极为新近（2026年5月），尚未经过同行评审。\n- MATH-Perturb (ICML 2025): 279道level-5扰动题，o1-mini下降16.49%。仅答案级分析，不涉及step-level perturbation interaction——这正是CAS-IRT的SPA所填补的空白。\n- VAR-MATH (arXiv 2507.12885): SymPy支持的symbolic变体，RL模型下降47-73%。同样仅答案级，且其SymPy variant generation pipeline可被CAS-IRT直接复用。\n- RIDE (arXiv 2511.04120): 使用IRT指导perturbation生成（IRT→perturbation方向），与CAS-IRT的perturbation→IRT方向互补而非竞争。proposal对此区分准确。\n- GenPRM (AAAI 2026): 1.5B模型在ProcessBench上超越GPT-4o。CAS-IRT拟用其做step-level verification。\n- Illusion of Reasoning (arXiv 2603.22816): 识别三种CoT模式（genuine/scaffolding/decoration），step necessity 4-93%。不涉及perturbation interaction。\n- DCR Factor (EMNLP 2025): 模糊推理contamination校正，9个模型~4% error。无IRT基础，ad-hoc。\n- Growing Pains (arXiv 2604.12843): 400+ models的多维IRT，明确指出contamination威胁anchor稳定性但未建模。\n- CoDeC (ICLR 2026): 99.9% AUC contamination检测，但只做detect不做correct。\n- 调研总结: IRT-for-LLM (PSN-IRT, Growing Pains, ATLAS)、contamination detection (JECS, CoDeC)、perturbation robustness (MATH-Perturb, VAR-MATH) 三个社区各自快速发展但确实尚无交叉。CAS-IRT的\"三社区统一\"定位准确，填补了一个真实且有价值的空白。这个交叉点在2025-2026年才变得可行（JECS提供contamination prior、GenPRM提供step verification），proposal的时机判断是正确的。\n\n【整体印象】:\n如果我是审稿人，第一反应是\"这是一个ambitious且有洞察力的proposal\"。核心idea——将contamination从noise source转变为IRT可建模的structured confounder——是genuinely novel的。研究landscape分析异常详尽，每个相关工作的定位和差异化都非常精准（尤其是RIDE的方向性对比）。实验设计在proposal阶段就已经非常完备，包含synthetic validation、known-contamination validation、predictive validation三层验证，ablation覆盖全面。\n\n但我会有两个主要顾虑：(1) 系统复杂度极高——IRT + contamination mixture + perturbation + step-level verification + SPA，每个组件都可能出问题，整合后的failure modes更多；(2) additive decomposition (Observed = Genuine + Contamination − Robustness) 作为一阶近似是否足够——即使proposal提出了interaction term扩展和BIC/AIC model selection，但如果additive模型被reject，fallback方案的convincingness存疑。\n\n整体倾向：borderline accept-leaning。方向正确、gap真实、设计严谨，但执行风险和复杂度是实际障碍。\n\n【核心贡献】:\n1. SPA (Step×Perturbation Alignment) 作为结构化依赖探测器：这是最独特的贡献。现有工作要么做answer-level perturbation (MATH-Perturb, VAR-MATH)，要么做step-level faithfulness without perturbation (Illusion of Reasoning)。将两者交叉——测量reasoning steps是否在perturbation的数学依赖结构中正确位置发生变化——是genuinely new的idea，且有清晰的理论动机（Decoupling Hypothesis的psychometric操作化）。\n2. CAS-IRT框架本身：将contamination从binary detect-and-discard提升为continuous psychometric estimation，利用JECS p-values作为informative prior。三个技术优势（item difficulty calibration、continuous contamination、cross-item information borrowing）相对于non-IRT pipeline均有清晰的理论基础。\n3. 实用价值：替代\"defense by obsolescence\"（不断造新benchmark）的contamination诊断范式，降低边际成本。Qwen2.5 RL contamination的retroactive case study是有说服力的motivation。\n\n这些贡献对LLM evaluation领域有较大价值，特别是在contamination问题日益严重、现有IRT工作明确回避contamination的背景下。\n\n【方法合理性】:\n方法的核心架构（3PL IRT + contamination mixture）有坚实的psychometric先例（EM-IRT rapid-guessing detection），扩展到LLM contamination场景是合理的类比。JECS p-values作为Bayesian prior初始化contamination parameter是巧妙的设计——既避免了flat prior导致的identifiability问题，又保留了IRT框架的joint estimation优势。\n\n潜在的更简单替代方案：\n- **Pipeline approach (Baseline 6)**: JECS标记 → clean/contaminated分组 → 分别计算accuracy → 加权组合。这比CAS-IRT简单得多。Proposal明确将其设为baseline并承诺比较，这是正确的。但如果pipeline approach效果接近CAS-IRT，joint estimation的额外复杂度就难以justify。\n- **Detect-then-filter (Baseline 2)**: 移除contaminated items后做标准IRT。更简单，但会丢失信息（contaminated items上的performance仍含genuine ability signal）。CAS-IRT的理论优势在于不丢弃数据。\n\n关键methodological风险：\n1. 3PL mixture的identifiability：即使有JECS prior，N=50模型下per-model×item contamination parameter的recovery质量存疑。Proposal有fallback（per-model shared c），但这大幅简化了contamination model。\n2. SPA依赖step-level verification的准确性：GenPRM-1.5B在AIME难度问题上的step verification质量未经验证。Dual-source design (GenPRM + step ablation) 缓解了风险，但inter-source disagreement的处理方案（\"agreement subset\"）可能大幅缩小可用数据。\n3. SymPy variant generation的覆盖度：geometry/combinatorics的低覆盖需要LLM-assisted perturbation，引入质量不确定性。\n\n整体而言，方法设计是合理的，风险被正确识别且有mitigation策略，但成功执行需要多个组件同时work。\n\n【5 维度打分】:\n\n1. 研究问题: 【强】\n   — 问题真实且重要：现有IRT-for-LLM工作（PSN-IRT, Growing Pains, metabench）全部假设zero contamination，而Growing Pains (arXiv 2604.12843) 明确指出contamination威胁anchor stability但未提出解决方案。Contamination detection社区（JECS, CoDeC）只做检测不做能力校正。这是一个documented but unaddressed gap。随着LLM evaluation stakes上升（benchmark-driven development, RL training feedback），decompose genuine ability vs. contamination artifact有真实的学术和实用需求。\n\n2. 方法与创新: 【强】\n   — SPA的novelty经调研确认成立：MATH-Perturb (ICML 2025) 和 VAR-MATH (arXiv 2507.12885) 均为answer-level，Illusion of Reasoning (arXiv 2603.22816) 做step-level但无perturbation interaction，PEARL (arXiv 2505.03019) 用bit-flip perturbation（表面级），EvalQReason (arXiv 2602.02295) 用step-level probability但无perturbation。SPA的step×perturbation交叉确实是unexplored的。CAS-IRT框架与DCR Factor (EMNLP 2025) 相比有明确的理论优势（IRT grounding vs. ad-hoc fuzzy inference）。与RIDE (arXiv 2511.04120) 的方向性互补关系论证清晰。唯一的concern是contribution密度——可能需要在8页内justify过多component。\n\n3. 实验设计: 【强】\n   — 这是proposal最突出的方面之一。Baselines覆盖了所有合理的替代方案（standard 3PL、detect-then-filter、DCR Factor、raw accuracy+perturbation、answer-level CAS-IRT、non-IRT pipeline），每个baseline都target一个specific question。Ablation table系统性地隔离每个component的贡献。三层validation (synthetic → known-contamination → predictive) 是psychometric研究的gold standard。Predictive validation使用time-stamped contamination-free benchmarks (AIME 2026/AMC 2026) 是clever的设计。Tiered evaluation (15 flagship + 80-100 open-weight) 在资源约束下是务实的。Human gold standard (250+ pairs, 2+ annotators, Cohen's κ) 体现了rigor。\n\n4. 可行性: 【中】\n   — 计算预算（~700-800 GPU-hours, ~$5K-10K API, ~200 person-hours, 10-14 weeks）对一个有GPU access的academic lab是可行的，但偏紧。主要可行性风险：(a) 闭源模型API成本波动和rate limiting可能影响Tier 1 full SPA；(b) SymPy variant generation的per-category coverage可能显著低于预期（geometry/combinatorics），导致algebra-only subset成为primary result；(c) GenPRM在variant上的calibration drift需要Platt scaling，但如果drift严重则scaling不够；(d) JECS是2026年5月的preprint，如果其pre-aggregation p-value extraction API/代码不公开或有bug，contamination prior的获取将受阻。14周timeline紧凑，留给troubleshooting的空间有限。\n\n5. 写作与呈现: 【强】\n   — Proposal本身的写作质量很高：research landscape分析详尽且准确（经调研验证），每个相关工作的差异化都有precise的论证。Core contributions的表述清晰，避免了overclaiming。Methodological risks被主动识别并附带mitigation策略，显示出成熟的研究态度。唯一的concern是信息密度极高——如果完整论文要在8+1页内呈现所有component（SPA定义、CAS-IRT formulation、variant generation、step verification、三层validation、6 baselines、全面ablation），writing和space management将是重大挑战。\n\n【概率估计】: [30% - 42%] 中位 36%\n\n【估计理由】:\n上调因素：(1) 研究gap真实且经调研确认，PSN-IRT (AAAI 2026 Oral) 和Growing Pains均明确回避contamination建模；(2) SPA的novelty claim成立，在answer-level perturbation和step-level faithfulness之间开辟了新维度；(3) 实验设计在proposal阶段已达到unusually high completeness，baselines/ablations/validation均超过平均proposal水平；(4) 三社区统一的narrative有学术appeal，且timing argument (2025-2026才变得可行) 是convincing的；(5) AAAI接受LLM evaluation方向的工作（PSN-IRT获Oral）。\n\n下调因素：(1) 系统复杂度极高，reviewer可能质疑\"是一篇完整的论文还是三篇论文的拼接\"；(2) additive decomposition的理论基础偏弱——如果interaction term在BIC/AIC中显著优于additive model，核心claim需要重新表述；(3) N=50 models下per-model×item contamination parameter的identifiability是genuine concern，fallback到per-model shared c实质上简化了contamination model的表达力；(4) 数学领域限定降低了generalizability，reviewer可能期望至少一个cross-domain extension；(5) 多个关键依赖组件（JECS p-values、GenPRM variant calibration、SymPy coverage）同时需要work，单一failure point可能cascade；(6) 8页内fitting all content将极其困难。\n\n中位36%反映：这是一个方向正确、novelty genuine、设计严谨的solid proposal，但复杂度和执行风险使其处于\"strong borderline\"区域。如果实验结果clean（CAS-IRT显著优于所有baselines、SPA提供interpretable insights、synthetic recovery质量好），有机会进入accept区域；如果某个组件失败导致ablation不完整，则可能跌入reject区域。\n\n【主要风险】:\n1. **\"Too many moving parts\" 质疑**：审稿人可能认为IRT+contamination+perturbation+step-level四个组件中任意两个的组合就足以构成一篇论文，四合一导致每个component的depth不够。特别是如果某个ablation显示step-level SPA的marginal gain较小，该component的justify将困难。\n2. **Identifiability failure at realistic N**：如果N=50模型下synthetic recovery的bias/RMSE不够好，即使fallback到per-model shared c也可能无法convincingly demonstrate CAS-IRT的估计质量优于simpler baselines (detect-then-filter)。这将直接削弱核心contribution。\n\n【实施评估】:\n  - 计算资源: ~700-800 A100-80G GPU-hours（开源模型inference + GenPRM step verification），$5K-10K API费用（闭源模型），对有GPU集群的学术团队可行但不轻松\n  - 数据需求: MATH-500, AMC, AIME, GSM8K（均公开），需自行生成SymPy variants（geometry/combinatorics覆盖是瓶颈），AIME 2026/AMC 2026作为time-stamped held-out（公开可获取）\n  - 人工介入: ~200 person-hours（250+ pairs human annotation, 2+ annotators），semi-automated pipeline降低单位成本，但仍需expertise in math problem verification\n  - 训练需求: 无模型训练，仅inference + EM parameter estimation（计算开销可忽略）\n  - 新 Benchmark: 不需要构建新benchmark，但需要生成SymPy variants（中等工程量）和human gold standard annotations（significant effort）\n  - 预估周期: 10-14周（从pilot到submission-ready），紧凑但可行，前提是JECS代码和GenPRM模型按预期可用\n```\n\nSources:\n- [PSN-IRT - AAAI 2026 Oral](https://ojs.aaai.org/index.php/AAAI/article/view/40814)\n- [PSN-IRT - arXiv](https://arxiv.org/abs/2505.15055)\n- [JECS - Provable Joint Decontamination](https://arxiv.org/abs/2605.21543)\n- [MATH-Perturb - ICML 2025](https://openreview.net/forum?id=OZy70UggXr)\n- [VAR-MATH - arXiv](https://arxiv.org/abs/2507.12885)\n- [RIDE - IRT-Guided Difficulty Perturbation](https://arxiv.org/abs/2511.04120)\n- [DCR Factor - EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1173/)\n- [GenPRM - AAAI 2026](https://arxiv.org/abs/2504.00891)\n- [The Illusion of Reasoning](https://arxiv.org/abs/2603.22816)\n- [Growing Pains - IRT Anchor Calibration](https://arxiv.org/abs/2604.12843)\n- [Reasoning or Memorization - RL Data Contamination](https://arxiv.org/abs/2507.10532)\n\n\n【原始 proposal（允许参考但不是主要依据）】:\n# Decomposing LLM Ability via Contamination-Aware Step-Level IRT\n\n## Core Problem\n\nCurrent LLM evaluation conflates genuine reasoning, contamination-driven memorization, and robustness deficits into a single accuracy score. We disentangle these via calibrated decomposition (Observed = Genuine + Contamination − Robustness) with psychometric and statistical rigor.\n\n## Core Contributions\n\n1. **Step×Perturbation Alignment (SPA) as a structural dependency probe**: SPA measures whether a model's reasoning steps adapt in correspondence with the mathematical dependency structure when problem constraints change across original-variant pairs. If a model encodes genuine structural understanding, its reasoning trace changes at precisely the steps downstream of the perturbed constraint; memorizers either reproduce frozen templates or collapse at unpredictable points. No prior work measures this step×perturbation interaction: MATH-Perturb (ICML 2025) and VAR-MATH (arXiv 2507.12885) examine only answer-level drops; Illusion of Reasoning (arXiv 2603.22816) examines step faithfulness on single problems; EvalQReason (arXiv 2602.02295) measures step-level probability distributions without perturbation interaction. SPA provides the first psychometric operationalization of the Decoupling Hypothesis (Robust Answers Fragile Logic, arXiv 2505.17406)—decomposing decoupling into contamination-driven (memorization masking as reasoning) and robustness-driven (genuine ability insufficient for variant) components, going beyond MATCHA's binary adversarial verification.\n\n2. **CAS-IRT Framework**: A contamination-aware extension of 3PL IRT that jointly estimates genuine ability θ, contamination susceptibility, and robustness deficit via EM. The additive decomposition is a first-order approximation; we additionally fit an interaction-term extension and use BIC/AIC model selection to validate whether additivity is sufficient. Three advantages over non-IRT pipeline approaches: (a) item difficulty calibration—contamination of easy vs. hard items has different impact on ability estimation; (b) continuous contamination modeling—JECS p-values as continuous prior, vs. binary detect-and-discard; (c) cross-item information borrowing—a model's performance on clean items informs its genuine ability estimate on contaminated items via shared θ.\n\n3. **Three-Community Unification**: First framework bridging contamination detection (JECS, CoDeC), adversarial robustness (MATH-Perturb, VAR-MATH), and IRT-based evaluation (PSN-IRT, ATLAS, metabench). This combination was infeasible until 2025–2026: JECS (May 2026) provided the first conformal per-item contamination signal usable as IRT prior; VAR-MATH (2025) demonstrated scalable SymPy-backed variant generation; GenPRM (AAAI 2026) and Illusion of Reasoning (Mar 2026) simultaneously delivered step-level verification tools and faithfulness theory. Crucially, this is perturbation-informed IRT (perturbation response patterns improve IRT estimation), the inverse direction of RIDE (arXiv 2511.04120), which uses IRT-guided perturbation (IRT difficulty estimates guide perturbation generation). Both use IRT + perturbation, but for fundamentally different purposes.\n\n4. **Training Diagnostic Application**: CAS-IRT enables decomposing benchmark improvement into genuine ability gain vs. contamination exploit vs. robustness deficit without constructing ad-hoc clean datasets. Retroactive case study: Reasoning or Memorization (arXiv 2507.10532, 2025) required building a fully synthetic dataset (RandomCalculation) to prove Qwen2.5's RL gains were contamination artifacts—a costly methodology. CAS-IRT could detect this directly from benchmark response patterns. More broadly, the community's current contamination defense relies on continually building new benchmarks (\"defense by obsolescence\"); CAS-IRT offers a complementary paradigm—diagnostic decomposition on existing benchmarks—with far lower marginal cost.\n\n## Research Landscape\n\n**IRT-for-LLM (assumes zero contamination):** PSN-IRT (AAAI 2026 Oral) analyzes 12 LLMs × 41,871 items, finding benchmark saturation and difficulty ceilings. ATLAS achieves 90% item reduction via adaptive testing. metabench captures 79.3% variance with sparse items. arXiv 2605.07046 scales IRT to 2211 models. Growing Pains (arXiv 2604.12843) uses multidimensional IRT across 400+ models, explicitly noting contamination threatens anchor stability but not modeling it. All assume zero contamination.\n\n**IRT + perturbation (opposite direction):** RIDE (arXiv 2511.04120) uses IRT difficulty estimation to guide adversarial perturbation generation across 35 LLMs, achieving 21.73% average performance drop. RIDE's direction is IRT→perturbation (better benchmark construction); CAS-IRT's direction is perturbation→IRT (better ability estimation). The two are complementary, not competing.\n\n**Contamination detection (detects without correcting):** CoDeC (ICLR 2026) achieves 99.9% AUC. JECS (arXiv 2605.21543) provides conformal guarantees with GCR control. DVD (arXiv 2601.04895) models memory-adherence vs. perturbation-drift dual states. RADAR achieves 93%. DeconIEP (arXiv 2601.19334) corrects contamination at inference time via embedding perturbation but requires model weight access and does not produce decomposed ability scores. None correct ability estimates within a psychometric framework.\n\n**Score correction (ad-hoc):** DCR Factor (EMNLP 2025) adjusts scores via fuzzy inference on 9 models with ~4% average error, without IRT grounding.\n\n**Perturbation robustness (answer-level only):** MATH-Perturb (ICML 2025): o1-mini drops 16.49% on hard perturbations. VAR-MATH (arXiv 2507.12885): RL-trained models drop 47–73%. Both answer-level only.\n\n**Step-level reasoning (no perturbation interaction):** Illusion of Reasoning (arXiv 2603.22816) identifies three CoT patterns with step necessity 4–93%. ProcessBench (ACL 2025) finds 51.8% process errors. Fragile Thoughts (arXiv 2603.03332) documents snowball effects. Robust Answers Fragile Logic (arXiv 2505.17406) validates the Decoupling Hypothesis via MATCHA. PEARL (arXiv 2505.03019) validates PSH using bit-flip perturbation—surface-level, distinct from structural algebraic variants. EvalQReason (arXiv 2602.02295) uses step-level probability distributions (CSD/SFC) for reasoning evaluation without perturbation.\n\n**Key differentiations:**\n- vs. RIDE: Same building blocks (IRT + perturbation), opposite directions. RIDE: IRT→perturbation (benchmark construction). CAS-IRT: perturbation→IRT (ability estimation + contamination decomposition).\n- vs. DVD: Binary detection vs. continuous psychometric quantification.\n- vs. PEARL: Bit-flip input perturbation vs. structural algebraic variants enabling step-level analysis.\n- vs. DCR Factor: Ad-hoc adjustment vs. joint IRT estimation with calibrated parameters.\n- vs. DeconIEP: Inference-time model correction (requires weight access) vs. evaluation-time score decomposition (model-agnostic, works on closed-source).\n- vs. Agent Psychometrics (arXiv 2604.00594, ICLR 2026 Workshop): Decomposes observable architectural components (LLM vs. scaffold); CAS-IRT decomposes latent confounders requiring identification via JECS priors + perturbation design.\n\n## Proposed Approach\n\n**Model specification.** Extend 3PL IRT with contamination mixture: P(correct|θ,d,c) = c·p_mem + (1−c)·σ(a(θ−d)), where c is the contamination indicator per model×item, initialized from JECS pre-aggregation per-model×item conformal p-values (extracted before JECS's max-p aggregation; see JECS arXiv 2605.21543). p_mem is constant in the base specification; item-dependent p_mem(d) tested as extension. Interaction term c·(1−r)·p_interaction fitted alongside the additive model, compared via BIC/AIC.\n\n**Identifiability safeguards.** The 3PL mixture faces known identifiability challenges (Bayesian EMM for 3PLM, PMC6555200). Mitigations: (a) informative Bayesian prior on c centered at JECS p-values; (b) synthetic parameter recovery across regimes (N=50,100,200 models × contamination rates 5%,15%,30%); (c) multi-start EM with convergence diagnostics; (d) if N=50 recovery proves insufficient, fallback to per-model contamination susceptibility (shared c across items per model), substantially reducing parameter count. N=50 recovery quality is reported as primary since it matches the experimental regime.\n\n**Variant generation.** SymPy-backed algebraic variants for MATH-500, AMC, AIME, GSM8K. Pilot: per-category coverage estimation across MATH-500's 7 categories. For low-coverage categories (expected: geometry, combinatorics), LLM-assisted perturbation + human verification following MATH-Perturb (ICML 2025). Variant quality protocol: each variant verified on (a) structural preservation (same solution steps), (b) difficulty preservation (answer magnitude/solution length proxy), (c) targeted parameter change only. Report per-category coverage and per-method quality metrics (human verification pass rate). Algebra-only subset ablation to check variant method bias.\n\n**SPA metric.** For each original-variant pair:\n- Impact point definition (model-independent): SymPy dependency graph identifies which solution steps are downstream of the perturbed variable. Impact point = first dependent step.\n- Step-level correctness transition: each step → (correct_orig, correct_variant) in four states.\n- Reasoning divergence point: first substantive divergence between traces, compared against SymPy-derived impact point. Tolerance window ±1 step. Memorization signature: divergence too early or too late relative to impact point.\n- Normalized by perturbation scope. Report both strict SPA and relaxed SPA (±1 tolerance).\n- Human gold standard includes impact point annotation (2+ annotators, Cohen's κ); SymPy-derived vs. human-annotated impact points compared in ablation.\n\n**Step-level verification (dual-source, equal status).** Source 1: GenPRM (AAAI 2026), using GenPRM-1.5B for compute efficiency. Source 2: Illusion of Reasoning step ablation (remove-one-step, observe answer change)—PRM-independent, equally applicable to originals and variants. ThinkPRM (arXiv 2504.16828) as additional cross-check. Pilot (50–100 items × 3 models): measure GenPRM original vs. variant step-level accuracy against human gold standard; report inter-source agreement (Cohen's κ). If GenPRM shows systematic variant degradation, apply Platt scaling calibration. Core SPA uses agreement subset; full-set as sensitivity analysis. Human gold standard: 250+ stratified pairs (benchmarks × perturbation types × difficulty), 2+ annotators, semi-automated pipeline (auto-annotate → human correct). Budget by difficulty: GSM8K ~5 min/pair, MATH-500 ~15 min/pair, AIME ~30 min/pair; total ~150–200 person-hours.\n\n**Tiered evaluation.** Tier 1 (~15 flagship models: DeepSeek-R1, Qwen3, GLM-4.7, Kimi-K2.5, Llama-4, GPT-4o, Claude, Gemini): full SPA on all items. Tier 2 (~80–100 open-weight models via vLLM batch inference): answer-level on originals+variants + JECS pipeline, sampled step-level on 15% of items. Total ~100–115 models for IRT calibration.\n\n**Estimation.** Joint EM yields per-model genuine ability θ, contamination susceptibility, robustness deficit. Grounded in EM-IRT rapid-guessing detection precedent from human psychometrics.\n\n## Validation Protocol\n\n**Synthetic validation:** Simulated response matrices with known θ, c, robustness. EM recovery (bias, RMSE) across regime variations. N=50 regime reported as primary. Identifiability boundary mapping.\n\n**Known-contamination validation:** Open-source models with partially known training data (e.g., Llama series): CAS-IRT contamination estimates vs. known overlap.\n\n**Predictive validation (multi-benchmark tiered):**\n- Primary: AIME 2026 / AMC 2026 (competition date past training cutoffs, time-stamped contamination-free). Bootstrap CIs reported given small item count (~25–30 per competition).\n- Secondary: FrontierMath Tier 1–3 (arXiv 2411.04872, Epoch AI; same-domain difficult math; note: Epoch AI quality review ongoing as of May 2026—report scores with caveat). Tier 4 reported separately (research-level, tests transfer beyond training difficulty range).\n- Exploratory: LiveCodeBench (cross-domain transfer).\n- All: compare Spearman/Kendall of θ_genuine vs. raw accuracy vs. standard IRT θ.\n\n## Baselines\n\n1. **Standard 3PL IRT** (PSN-IRT approach): no contamination modeling.\n2. **Detect-then-filter**: JECS removes contaminated items → standard 3PL on clean subset.\n3. **DCR Factor post-hoc** (EMNLP 2025): ad-hoc contamination correction.\n4. **Raw accuracy + perturbation drop**: no IRT.\n5. **Answer-level CAS-IRT**: full model without step-level SPA.\n6. **Non-IRT pipeline decomposition**: JECS labels + separate accuracy computation on clean/contaminated/variant sets → post-hoc weighted combination without IRT. Tests whether IRT joint estimation adds value over simple pipeline.\n\nEvaluation: (a) ranking correlation with held-out benchmarks; (b) contamination detection precision/recall; (c) synthetic parameter recovery; (d) robustness prediction accuracy.\n\n## Ablation Design\n\n| Configuration | Contamination | Perturbation | Step-level |\n|---|---|---|---|\n| Standard 3PL IRT | ✗ | ✗ | ✗ |\n| + Contamination only | ✓ (JECS init) | ✗ | ✗ |\n| + Perturbation only | ✗ | ✓ | ✗ |\n| + Contamination + Perturbation (answer-level) | ✓ | ✓ | ✗ |\n| Full CAS-IRT | ✓ | ✓ | ✓ |\n\nAdditional: JECS init vs. uniform init; variants per item (1, 3, 5); GenPRM vs. step-ablation vs. ensemble SPA; EM convergence; additive vs. interaction (BIC/AIC); algebra-only vs. full-coverage; SymPy-only vs. mixed-method variants; per-model c vs. per-model×item c; SymPy-derived vs. human-annotated impact points.\n\n## Compute Budget\n\nTier 1 (~15 models, full SPA): 400–500 A100-80G GPU-hours for open-weight models (including 671B MoE via multi-GPU); $3,000–8,000 API for closed-source. Tier 2 (~80–100 models, answer-level + 15% step-level): ~150–200 GPU-hours via vLLM batch. Step verification (GenPRM-1.5B): ~50 GPU-hours. Human annotation (250+ pairs, semi-automated, 2 annotators): ~150–200 person-hours. Pilot studies: ~50 GPU-hours + 30 person-hours. Total: ~700–800 GPU-hours, ~$5,000–10,000 API, ~200 person-hours. Timeline: 10–14 weeks from pilot to submission-ready.\n\n## Key References\n\n- Lost in Benchmarks? PSN-IRT (AAAI 2026 Oral)\n- metabench: A Sparse Benchmark (ICLR 2025)\n- ATLAS: Adaptive Testing for LLM Evaluation (arXiv 2025)\n- DCR: Quantifying Data Contamination (EMNLP 2025)\n- JECS: Provable Joint Decontamination (arXiv 2605.21543, 2026)\n- CoDeC: Detecting Contamination via In-Context Learning (ICLR 2026)\n- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026)\n- ThinkPRM: Process Reward Models That Think (arXiv 2504.16828)\n- The Illusion of Reasoning (arXiv 2603.22816, 2026)\n- Reasoning or Memorization? RL Data Contamination (arXiv 2507.10532, 2025)\n- MATH-Perturb (ICML 2025)\n- FrontierMath: Advanced Math Reasoning (arXiv 2411.04872, Epoch AI)\n- Growing Pains: IRT Anchor Calibration (arXiv 2604.12843, 2026)\n- Scalable IRT for 2211 Models (arXiv 2605.07046, 2026)\n- RIDE: IRT-Guided Difficulty Perturbation (arXiv 2511.04120)\n- DVD: Detection via Variance of Distribution (arXiv 2601.04895, 2026)\n- DeconIEP: Inference-Time Decontamination (arXiv 2601.19334, 2026)\n- PEARL: Perturbation Sensitivity Hypothesis (arXiv 2505.03019, 2025)\n- EvalQReason: Step-Level Reasoning Evaluation (arXiv 2602.02295, 2026)\n- VAR-MATH: Symbolic Variant Benchmark (arXiv 2507.12885, 2025)\n- ProcessBench: Process Error Identification (ACL 2025)\n- Robust Answers Fragile Logic: Decoupling Hypothesis (arXiv 2505.17406, 2025)\n- Fragile Thoughts: Snowball Effects in CoT (arXiv 2603.03332, 2026)\n- Agent Psychometrics: IRT for Agentic Coding (arXiv 2604.00594, ICLR 2026 Workshop)\n- Bayesian EMM for 3PLM (PMC6555200)"
}
````

---

### Runtime record

_source line 2 · 2026-05-29T07:19:16.573Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T07:19:16.573Z",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-29T07:19:16.629Z_

【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。

【三位审稿人评估】:
━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━
Now I have sufficient information to produce a thorough evaluation. Let me compile my analysis.

---

```
【阶段】: Triage

【领域调研】:
- PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055): 12 LLMs × 41,871 items 的 IRT 分析，发现 benchmark 饱和与难度天花板问题。假设零污染——正是本 proposal 要突破的局限。
- JECS (arXiv 2605.21543, 2026): 首个提供 conformal per-item 污染 p-value 并实现 GCR 控制的方法。本 proposal 将其 pre-aggregation p-value 作为 IRT 先验，属下游应用而非竞争关系。
- MATH-Perturb (ICML 2025): o1-mini 在 hard perturbation 上下降 16.49%。仅 answer-level，无 step-level 分析。
- VAR-MATH (arXiv 2507.12885): RL 模型在符号变体上下降 47–73%。提供 SymPy-backed 变体生成方法论，本 proposal 直接复用。仅 answer-level。
- RIDE (arXiv 2511.04120): IRT→perturbation 方向（用 IRT 难度估计指导对抗性扰动生成），与本 proposal perturbation→IRT 方向互补而非竞争。
- DCR Factor (EMNLP 2025): 通过模糊推理系统对 9 个模型进行 ad-hoc 污染校正，平均误差 ~4%。无 IRT 基础，无 step-level 分析。
- GenPRM (AAAI 2026): 生成式过程奖励模型，GenPRM-1.5B 超越 GPT-4o。本 proposal 用其做 step-level verification。
- Illusion of Reasoning (arXiv 2603.22816, 2026): 13 个前沿模型的 step-level faithfulness 评估，发现三种 CoT 模式（genuine/scaffolding/decoration），step necessity 4–93%。仅单问题分析，无扰动交互。
- Robust Answers Fragile Logic (arXiv 2505.17406): 提出 Decoupling Hypothesis 和 MATCHA 框架，发现模型在对抗扰动下维持正确答案但推理崩溃。本 proposal 的 SPA 是对此假说的首个心理计量操作化。
- CoDeC (ICLR 2026): 99.9% AUC 的污染检测，但检测而不校正。
- Growing Pains (arXiv 2604.12843, 2026): 400+ 模型的多维 IRT，明确指出污染威胁 anchor 稳定性但未建模。
- Reasoning or Memorization (arXiv 2507.10532, 2025): 证明 Qwen2.5 的 RL 提升是污染伪影，需构建全新 synthetic dataset (RandomCalculation) 才能证明——正是本 proposal CAS-IRT 声称能更低成本解决的场景。

- 调研总结: LLM 评估的 IRT 方向（PSN-IRT, Growing Pains, ATLAS）、污染检测方向（JECS, CoDeC, DVD）、扰动鲁棒性方向（MATH-Perturb, VAR-MATH, RIDE）三条线在 2025-2026 快速发展但彼此独立。**目前没有任何已发表或预印工作将 IRT 估计、污染校正和 step-level 扰动分析统一在一个框架内。** 本 proposal 的定位是这三个方向的交叉点，novelty claim 成立。

【整体印象】:
作为审稿人，我的第一反应是"这是一篇精心设计、定位精准的 systems paper"。Proposal 展现了对领域格局的深刻理解，准确识别了一个真实且重要的 gap（IRT 评估假设零污染，污染检测不校正能力估计，扰动分析仅 answer-level），并提出了一个技术上合理的统一框架。实验设计的完备性（6 个 baseline、系统性 ablation、多层验证）是显著的加分项。

倾向 **weak accept**，但以下几点让我犹豫：(1) 框架复杂度高，有 over-engineering 之嫌；(2) 3PL mixture 在 N=50-100 的 identifiability 是真实风险；(3) 论文需要极好的写作才能让审稿人在有限时间内理解全部贡献。

【核心贡献】:
1. **CAS-IRT 框架本身**：首个在 IRT 框架内联合建模 genuine ability、contamination susceptibility 和 robustness deficit 的方法。相比 DCR Factor 的 ad-hoc 校正和 detect-then-discard 的信息浪费，这是概念上的显著进步。
2. **SPA 指标**：首次将 step-level 推理与 perturbation 的结构依赖关系结合，提供了超越 answer-level 的污染/记忆化诊断信号。这是 Decoupling Hypothesis 的首个可计算操作化。
3. **三社区统一**：bridging 污染检测、对抗鲁棒性和心理计量评估三个原本独立的研究方向，这种 unification 本身就是对领域的贡献。

这些贡献对领域有较高价值：如果 CAS-IRT 的 identifiability 问题能被解决，它将改变社区评估 LLM 能力的方式——从"不断构建新 benchmark 来逃避污染"转向"在现有 benchmark 上做诊断性分解"。

【方法合理性】:
方法整体合理，各组件有理论或实证基础：
- 3PL IRT 的 contamination mixture 扩展在概念上自然，JECS p-value 作为 informative prior 是巧妙的解决方案。
- SPA 的核心思想——检查推理步骤的变化是否与 SymPy dependency graph 的结构依赖一致——逻辑严密。
- EM 估计有 human psychometrics 中 rapid-guessing detection 的先例。

**更简单的替代方案**：一个合理的 reviewer concern 是"为什么不直接用 detect-then-filter（JECS 过滤污染项 → 标准 IRT）？"——proposal 将此作为 Baseline 2 并声称 CAS-IRT 通过 continuous modeling 和 cross-item information borrowing 更优。这是可以实验验证的 claim，但如果 detect-then-filter 表现接近，CAS-IRT 的额外复杂度就难以证明。这是方法论上最大的风险。

另一个 concern：additive decomposition（Observed = Genuine + Contamination − Robustness）是否过度简化？交互项扩展是好的补救措施，但如果 BIC/AIC 选择了交互模型，additive 叙事就需要调整。

【5 维度打分】:
  1. 研究问题: 【强】— LLM benchmark 评估被污染混淆是一个真实、紧迫且影响广泛的问题。PSN-IRT (AAAI 2026 Oral) 和 Growing Pains (arXiv 2604.12843) 都明确指出 IRT 评估中污染的未解决问题。"Reasoning or Memorization" (arXiv 2507.10532) 展示了 RL 训练中污染的严重后果。这个 decomposition 问题对整个 LLM 评估社区有直接实用价值。

  2. 方法与创新: 【强】— 核心 novelty claim 经调研确认成立：(a) 无已有工作将 IRT 与污染校正联合建模（PSN-IRT 假设零污染，DCR Factor 无 IRT）；(b) SPA 的 step×perturbation 交互是新的（MATH-Perturb/VAR-MATH 仅 answer-level，Illusion of Reasoning 仅单问题）；(c) 与 RIDE 的互补关系（方向相反）定位清晰。唯一扣分点：框架组件过多，novelty 分散在多个 contribution 中，需要清晰的叙事来统一。

  3. 实验设计: 【强】— 这是本 proposal 最突出的优势之一。6 个 baseline 覆盖了所有合理的替代方案（标准 IRT、detect-then-filter、DCR Factor、raw accuracy、answer-level CAS-IRT、non-IRT pipeline）。Ablation 设计系统性极强（5 种配置 + 多个维度的变体）。三层验证（synthetic recovery、known-contamination、predictive on held-out）是金标准。AIME 2026/AMC 2026 作为 contamination-free held-out 的选择有说服力。Human gold standard 的标注预算（250+ pairs, 2+ annotators, Cohen's κ）也显示了严谨性。按照 MATH-Perturb 和 VAR-MATH 的实验标准，这个设计已经超标。

  4. 可行性: 【中】— 计算资源需求（700-800 GPU-hours, $5k-10k API）对有一定资源的研究组可行。但以下依赖链条令人担忧：(a) SymPy 变体生成的品类覆盖率（geometry, combinatorics 可能低覆盖），(b) GenPRM 在 variant 上的表现是未验证假设，(c) JECS pre-aggregation p-value 的提取需要重现 JECS pipeline，(d) 150-200 person-hours 的人工标注是显著投入，(e) 10-14 周时间线紧凑。任何一个环节出问题都可能影响全局。Proposal 包含了 fallback 策略（per-model c, algebra-only subset），这是好的，但复杂度仍然高。

  5. 写作与呈现: 【中】— 作为 proposal，信息密度极高，展示了深入的领域知识。但这也是双刃剑：AAAI 论文通常 8 页（含 references），要在有限篇幅内清晰传达 CAS-IRT 框架、SPA 指标、三社区统一、完整实验设计，写作难度很高。如果处理不好，审稿人可能觉得"贪多嚼不烂"。建议在正文中聚焦 CAS-IRT + SPA 的核心故事，将部分 ablation 和 tiered evaluation 细节移至 appendix。此外，proposal 中对 related work 的 differentiation 虽然精确，但需要更简洁的叙事——一个清晰的 figure 或 table 比 20 条文字对比更有效。

【概率估计】: [33% - 48%] 中位 40%

【估计理由】:
上界 48%——如果实验结果清晰验证了 CAS-IRT 相对 detect-then-filter 和 DCR Factor 的优势、SPA 指标展示了直观的 memorization signature、写作清晰到位，这篇论文具备 solid accept 的潜力。PSN-IRT 拿到了 AAAI 2026 Oral 说明 IRT-for-LLM 方向受认可，CAS-IRT 作为其 contamination-aware 后继有天然的叙事。

下界 33%——如果 (a) identifiability 实验显示 N=50 regime 下参数恢复不理想需要 fallback 到简化模型，(b) CAS-IRT 相比 detect-then-filter 的改进幅度有限（"这么复杂值得吗？"），(c) 论文篇幅限制导致方法和实验阐述不充分，(d) 某位审稿人对 additive decomposition 的理论基础提出根本质疑，都可能导致 borderline reject。

中位 40%——这是一篇 above-average 的投稿。研究问题和创新性都过线，实验设计远超平均水平，但框架复杂度和 identifiability 风险使其不是"稳中"的水平。AAAI 的接收率约 23-25%，这篇位于中稿线附近偏上。

【主要风险】:
1. **Identifiability + "何必这么复杂"的双重质疑**：3PL contamination mixture 在有限模型数（N~50-100）下的 identifiability 是最大技术风险。如果 synthetic recovery 显示需要 fallback 到简化模型（per-model c），框架的核心叙事（per-item contamination modeling）就被削弱。同时，如果 CAS-IRT 相对 Baseline 2（detect-then-filter）的改进有限，审稿人会质疑整个框架的必要性——Occam's razor 是强有力的反对理由。
2. **论文组织与范围控制**：Proposal 包含 4 个核心贡献 + 6 个 baseline + 10+ ablation 维度 + 三层验证。在 8 页正文中清晰呈现这一切的写作难度极高。如果叙事不够凝练，审稿人可能感到 overwhelmed 并质疑 focus。

【实施评估】:
  - 计算资源: 700-800 A100-80G GPU-hours (open-weight models) + $5k-10k API (closed-source)。对有 GPU 集群的研究组可行，但 671B MoE 的多 GPU 推理和 100+ 模型的 batch inference 有工程复杂度。
  - 数据需求: MATH-500, AMC, AIME, GSM8K (公开)；AIME 2026/AMC 2026 作为 held-out (公开)；FrontierMath (Epoch AI, 需要申请访问权限，且质量审核进行中)。核心数据均可获取。
  - 人工介入: ~200 person-hours (250+ pairs × 2 annotators)。这是显著投入，需要具备数学背景的标注者。半自动 pipeline 可降低但不消除此成本。
  - 训练需求: 无模型训练（evaluation-time framework）。需运行 GenPRM-1.5B inference 和 JECS pipeline，但均有开源实现。
  - 新 Benchmark: 不需要构建新 benchmark，但需要生成数千个 SymPy-backed algebraic variants。这是本质上的 benchmark 扩展工作。
  - 预估周期: 10-14 周（含 pilot study）。紧凑但可行，前提是团队 2-3 人全职投入且无重大技术障碍。
```

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)
- [JECS: Provable Joint Decontamination](https://arxiv.org/abs/2605.21543)
- [MATH-Perturb (ICML 2025)](https://openreview.net/forum?id=OZy70UggXr)
- [VAR-MATH: Symbolic Multi-Instance Benchmarks](https://arxiv.org/abs/2507.12885)
- [RIDE: IRT-Guided Difficulty Perturbation](https://arxiv.org/abs/2511.04120)
- [DCR Factor (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)
- [GenPRM (AAAI 2026)](https://arxiv.org/abs/2504.00891)
- [The Illusion of Reasoning](https://arxiv.org/abs/2603.22816)
- [Robust Answers, Fragile Logic: Decoupling Hypothesis](https://arxiv.org/abs/2505.17406)
- [CoDeC: Contamination Detection via ICL (ICLR 2026)](https://openreview.net/forum?id=YlpaaYxx4t)
- [Growing Pains: IRT Anchor Calibration](https://arxiv.org/abs/2604.12843)
- [Reasoning or Memorization? RL Data Contamination](https://arxiv.org/abs/2507.10532)

━━━━━━━━━━ 审稿人 2（独立评审）━━━━━━━━━━
Now I have sufficient information to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055): 将IRT应用于LLM评估的里程碑工作，分析12个LLM × 41,871 items，发现现有benchmark的测量质量缺陷。假设零contamination——CAS-IRT直接填补这一空白。PSN-IRT拿到Oral说明AAAI对IRT-for-LLM方向高度认可。
- Growing Pains (arXiv 2604.12843, 2026): 多维IRT框架，400+ models，使用anchor items实现跨时间可比性。明确提到contamination威胁anchor稳定性但未建模——进一步确认contamination-aware IRT是公认的open problem。
- JECS (arXiv 2605.21543, 2026): 首个提供conformal per-item contamination信号的方法，GCR控制有理论保证。CAS-IRT将其作为IRT prior的关键输入，时间线吻合（2026年5月）。
- CoDeC (ICLR 2026): 基于in-context learning的contamination检测，99.9% AUC。仅检测不纠正——与CAS-IRT的"检测+校正"定位互补。
- DCR Factor (EMNLP 2025): 通过fuzzy inference system调整分数，9个模型，~4% error。缺乏IRT理论支撑，ad-hoc性质明显——CAS-IRT的对比优势清晰。
- RIDE (arXiv 2511.04120): IRT→perturbation方向（用IRT难度指导扰动生成），35 LLMs，21.73% drop。CAS-IRT是perturbation→IRT方向（用扰动响应改善能力估计）。两者互补非竞争，差异化清晰且重要。
- MATH-Perturb (ICML 2025): answer-level perturbation robustness benchmark，o1-mini -16.49%。仅answer-level，不做step-level分析——SPA的step×perturbation交互是真正的新增维度。
- VAR-MATH (arXiv 2507.12885, 2025): SymPy-backed符号变体生成，RL模型drop 47-73%。提供了可复用的variant generation基础设施，CAS-IRT可直接利用。
- Illusion of Reasoning (arXiv 2603.22816, 2026): 发现三种CoT模式（genuine/scaffolding/decoration），step necessity 4-93%。提供step-level faithfulness理论基础，但无perturbation交互——SPA结合两者。
- Robust Answers Fragile Logic (arXiv 2505.17406, 2025): 提出Decoupling Hypothesis并通过MATCHA验证。CAS-IRT的SPA声称提供该假说的首个psychometric operationalization。
- Scalable IRT for 2211 Models (arXiv 2605.07046, 2026): 大规模IRT应用，同样假设零contamination。
- 调研总结: IRT-for-LLM在2025-2026经历爆发式增长（PSN-IRT获AAAI Oral、Growing Pains 400+模型、2211模型大规模应用），但所有现有工作均假设零contamination。同时contamination检测（JECS/CoDeC）和perturbation robustness（MATH-Perturb/VAR-MATH）各自成熟但未与IRT整合。CAS-IRT的"三社区统一"在时间窗口上确实是2025-2026才变得可行的方向，proposal对这一gap的定位是准确的。

【整体印象】: 
作为审稿人，第一反应是"这是一篇 ambitious 且 well-crafted 的 proposal"。研究问题重要且 timely（所有现有IRT工作都假设零contamination），方法论路径有psychometric传统支撑（EM-IRT rapid-guessing detection的类比恰当），文献综述极为全面，差异化论证清晰有力。实验设计的完备程度（6个baselines、13+ablation configurations、三级validation、tiered evaluation）在proposal阶段罕见。我的倾向是 **weak accept**，但有两个需要关注的风险：(1) 框架复杂度是否会让reviewer感到"too many moving parts"；(2) SPA的实际operationalization能否达到proposal中描述的精度。如果实验结果能证明CAS-IRT在held-out benchmark预测上显著优于standard IRT和detect-then-filter，这将是一篇有影响力的工作。

【核心贡献】: 
核心贡献是将LLM的benchmark表现分解为genuine ability、contamination susceptibility和robustness deficit三个可解释的组分，并通过IRT框架提供了有理论支撑的联合估计方法。具体而言：
(a) CAS-IRT框架本身——contamination-aware的IRT扩展，相比DCR Factor的ad-hoc调整和detect-then-filter的信息丢失，提供了principled的替代方案；
(b) SPA metric——首个在step×perturbation交互层面区分memorization和genuine reasoning的指标；
(c) 三社区统一——将原本独立发展的contamination detection、perturbation robustness和IRT-based evaluation整合为统一框架。
对领域的价值中等偏高：如果框架可行，它改变了LLM evaluation的paradigm——从"defense by obsolescence"（不断造新benchmark）到"diagnostic decomposition on existing benchmarks"。但实际影响取决于框架的adoption barrier（复杂度较高）。

【方法合理性】: 
方法的整体思路是合理的——用contamination信号作为IRT的mixture prior，用perturbation response pattern提供robustness信号，用step-level alignment作为fine-grained memorization探针。每一步都有psychometric或统计学传统支撑。

但需要关注的是"更简单替代方案"的问题：
(1) **Detect-then-filter**（baseline 2）是最直接的替代——JECS检测contaminated items后直接剔除，对剩余items做standard IRT。CAS-IRT需要证明联合估计显著优于这种简单方法。如果优势微小，reviewer会质疑复杂框架的必要性。
(2) **Non-IRT pipeline decomposition**（baseline 6）是另一个关键对比——直接在clean/contaminated/variant子集上分别计算accuracy，加权组合。如果这种简单pipeline效果接近CAS-IRT，IRT joint estimation的价值就会被质疑。
(3) **Additive分解假设**（Observed = Genuine + Contamination − Robustness）的first-order approximation性质需要实验验证。Proposal提到了interaction term extension和BIC/AIC model selection，这是好的safeguard。

总体而言，方法论路径合理但复杂，"必要性证明"将是reviewers重点关注的。

【5 维度打分】:

1. 研究问题: 【强】— 所有现有IRT-for-LLM工作（PSN-IRT、Growing Pains、metabench、2211-model scaling）均假设零contamination，而contamination已被多个独立工作（CoDeC 99.9% AUC、JECS、Reasoning or Memorization的Qwen2.5案例）证实为严重问题。在IRT-for-LLM进入大规模应用的关键时期（2025-2026），contamination-aware IRT是一个clearly important且timely的research question。PSN-IRT获AAAI 2026 Oral进一步验证了AAAI对此方向的兴趣。

2. 方法与创新: 【中偏强】— SPA（step×perturbation alignment）是genuinely novel的贡献，无先前工作在此层面操作（MATH-Perturb/VAR-MATH仅answer-level，Illusion of Reasoning无perturbation交互，EvalQReason无perturbation，PEARL用bit-flip而非structural variant）。CAS-IRT框架将JECS prior集成到3PL IRT中是principled但相对incremental的扩展。与RIDE的方向对比（IRT→perturbation vs. perturbation→IRT）是清晰的差异化。主要风险在于"组合式创新"——每个组件（JECS、SymPy variants、GenPRM、3PL IRT）均为已有工作，novelty来自整合。部分reviewers可能认为这是"engineering contribution"而非"research contribution"。

3. 实验设计: 【强】— 这是proposal最突出的优势之一。6个精心选择的baselines覆盖了所有合理的替代方案（standard IRT、detect-then-filter、DCR ad-hoc、raw accuracy、answer-level CAS-IRT、non-IRT pipeline）。Ablation design系统性极强，13+配置涵盖每个组件的贡献。三级validation（synthetic recovery、known-contamination、predictive on held-out benchmarks）层层递进。Tiered evaluation（15 flagship + 80-100 open-weight）在规模和可行性之间取得了好的平衡。Identifiability safeguards（N=50 recovery作为primary报告、per-model c fallback）体现了对psychometric方法论的deep understanding。AIME 2026/AMC 2026作为contamination-free validation是clever的设计。

4. 可行性: 【中】— 计算资源需求合理（700-800 GPU-hours + $5K-10K API），在标准学术实验室可承受范围内。10-14周时间线偏紧但可行。主要风险：(a) SPA的SymPy dependency graph对geometry/combinatorics的覆盖不足，LLM-assisted perturbation引入方法异质性；(b) GenPRM在variant上的step-level验证准确性未知（proposal有pilot study计划但结果不确定）；(c) 3PL mixture model在N=50 models时的identifiability——如果recovery差，需要fallback到per-model c，削弱了per-item contamination建模的核心贡献；(d) 人工标注250+ pairs需要~150-200 person-hours，对标注质量一致性有要求。

5. 写作与呈现: 【强】— Proposal的结构清晰，逻辑链条完整。文献综述几乎涵盖了所有relevant工作（2025-2026的最新成果），差异化论证精准（特别是vs. RIDE、vs. DCR Factor、vs. DeconIEP的对比）。"Three-Community Unification"的framing有效传达了贡献的scope。技术细节（EM estimation、identifiability safeguards、variant generation protocol）的呈现既专业又可读。时间窗口论证（为何2025-2026才可行）增强了说服力。

【概率估计】: [32% - 42%] 中位 37%

【估计理由】: 
正面因素：(1) 研究问题重要且timely，精准对应IRT-for-LLM领域的核心盲点（contamination assumption）；(2) PSN-IRT获AAAI 2026 Oral证明AAAI对IRT-for-LLM方向友好；(3) SPA是genuinely novel的技术贡献；(4) 实验设计在proposal阶段罕见地完备，baselines和ablation覆盖全面；(5) 文献综述和差异化论证的质量极高。

负面因素：(1) 框架复杂度高——组合了JECS + SymPy variants + GenPRM/step-ablation + 3PL IRT + EM，reviewer可能质疑是否over-engineered；(2) "组合式创新"的novelty perception风险——每个组件均非原创，reviewer可能认为主要贡献是"engineering integration"；(3) identifiability在小N regime下的不确定性——如果N=50 recovery不佳，核心主张弱化；(4) SPA的operationalization高度依赖SymPy和GenPRM的可靠性，存在execution risk；(5) additive decomposition是simplifying assumption，可能被challenge。

综合判断：这是一篇整体扎实、方向正确、设计完备的proposal，但复杂度和"组合式创新"的定位使其处于borderline区间。如果实验能证明CAS-IRT显著优于detect-then-filter（最简单的替代方案），且SPA确实提供了answer-level分析无法获得的洞察，中稿概率会偏向上界。如果实验结果marginal improvement，则偏向下界。

【主要风险】: 
1. **"组合式创新" vs. "原创研究"的perception问题**：3位reviewer中如果有1位认为"只是把现有工具拼在一起"（JECS + SymPy + GenPRM + IRT），给出weak reject，这将是最常见的reject理由。Proposal需要通过ablation证明joint estimation不可被简单pipeline替代——但这取决于实验结果。
2. **CAS-IRT vs. detect-then-filter的marginal improvement风险**：如果JECS已经能高效检测contaminated items，简单剔除后做standard IRT就可能达到接近CAS-IRT的效果。如果held-out benchmark预测上CAS-IRT的优势不够显著（例如Spearman ρ提升 < 0.05），reviewer会认为复杂框架不值得。

【实施评估】:
  - 计算资源: 700-800 A100 GPU-hours + $5K-10K API cost，中等规模，标准学术实验室可承受。Tier 2的vLLM batch inference设计合理地降低了成本。
  - 数据需求: MATH-500、AMC、AIME、GSM8K均为公开benchmark。SymPy-backed variants需要自行生成（有VAR-MATH基础设施可借鉴）。AIME 2026/AMC 2026作为held-out validation需等待竞赛数据公开。
  - 人工介入: ~200 person-hours（250+ pairs标注 + pilot studies），需要2+名具有数学专业背景的标注人员。Semi-automated pipeline降低了成本但对pipeline质量有要求。
  - 训练需求: 不需要训练新模型。GenPRM-1.5B为现有模型。EM estimation是统计优化，非深度学习训练。
  - 新 Benchmark: 不构建新benchmark，但需要生成SymPy-backed variants（实质上是variant dataset construction）。
  - 预估周期: 10-14周（Proposal自估），偏紧但对于evaluation-focused工作基本可行。关键路径：variant generation + human annotation可能成为瓶颈。
```

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)
- [Growing Pains: Extensible LLM Benchmarking via Fixed Parameter Calibration](https://arxiv.org/abs/2604.12843)
- [JECS: Provable Joint Decontamination](https://arxiv.org/html/2605.21543)
- [CoDeC: Detecting Data Contamination via In-Context Learning (ICLR 2026)](https://arxiv.org/abs/2510.27055)
- [DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)
- [RIDE: Difficulty Evolving Perturbation with IRT](https://arxiv.org/abs/2511.04120)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning (ICML 2025)](https://arxiv.org/abs/2502.06453)
- [VAR-MATH: Symbolic Multi-Instance Benchmarks](https://arxiv.org/abs/2507.12885)
- [The Illusion of Reasoning: Step-Level Evaluation](https://arxiv.org/abs/2603.22816)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)
- [Scalable IRT for 2211 Models](https://arxiv.org/abs/2605.07046)

━━━━━━━━━━ 审稿人 3（独立评审）━━━━━━━━━━
Now I have sufficient research to provide a comprehensive evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055): 最直接的IRT-for-LLM前作。分析12 LLMs × 41,871 items，发现benchmark饱和与难度天花板。关键局限：完全不建模contamination，假设所有response pattern来自genuine ability。CAS-IRT直接继承并扩展其框架。
- JECS (arXiv 2605.21543, May 2026): 提供conformal per-item contamination p-values，实现GCR控制。CAS-IRT将JECS的pre-aggregation p-values作为IRT contamination prior——这是一个创造性的跨框架复用，但JECS极为新近（2026年5月），尚未经过同行评审。
- MATH-Perturb (ICML 2025): 279道level-5扰动题，o1-mini下降16.49%。仅答案级分析，不涉及step-level perturbation interaction——这正是CAS-IRT的SPA所填补的空白。
- VAR-MATH (arXiv 2507.12885): SymPy支持的symbolic变体，RL模型下降47-73%。同样仅答案级，且其SymPy variant generation pipeline可被CAS-IRT直接复用。
- RIDE (arXiv 2511.04120): 使用IRT指导perturbation生成（IRT→perturbation方向），与CAS-IRT的perturbation→IRT方向互补而非竞争。proposal对此区分准确。
- GenPRM (AAAI 2026): 1.5B模型在ProcessBench上超越GPT-4o。CAS-IRT拟用其做step-level verification。
- Illusion of Reasoning (arXiv 2603.22816): 识别三种CoT模式（genuine/scaffolding/decoration），step necessity 4-93%。不涉及perturbation interaction。
- DCR Factor (EMNLP 2025): 模糊推理contamination校正，9个模型~4% error。无IRT基础，ad-hoc。
- Growing Pains (arXiv 2604.12843): 400+ models的多维IRT，明确指出contamination威胁anchor稳定性但未建模。
- CoDeC (ICLR 2026): 99.9% AUC contamination检测，但只做detect不做correct。
- 调研总结: IRT-for-LLM (PSN-IRT, Growing Pains, ATLAS)、contamination detection (JECS, CoDeC)、perturbation robustness (MATH-Perturb, VAR-MATH) 三个社区各自快速发展但确实尚无交叉。CAS-IRT的"三社区统一"定位准确，填补了一个真实且有价值的空白。这个交叉点在2025-2026年才变得可行（JECS提供contamination prior、GenPRM提供step verification），proposal的时机判断是正确的。

【整体印象】:
如果我是审稿人，第一反应是"这是一个ambitious且有洞察力的proposal"。核心idea——将contamination从noise source转变为IRT可建模的structured confounder——是genuinely novel的。研究landscape分析异常详尽，每个相关工作的定位和差异化都非常精准（尤其是RIDE的方向性对比）。实验设计在proposal阶段就已经非常完备，包含synthetic validation、known-contamination validation、predictive validation三层验证，ablation覆盖全面。

但我会有两个主要顾虑：(1) 系统复杂度极高——IRT + contamination mixture + perturbation + step-level verification + SPA，每个组件都可能出问题，整合后的failure modes更多；(2) additive decomposition (Observed = Genuine + Contamination − Robustness) 作为一阶近似是否足够——即使proposal提出了interaction term扩展和BIC/AIC model selection，但如果additive模型被reject，fallback方案的convincingness存疑。

整体倾向：borderline accept-leaning。方向正确、gap真实、设计严谨，但执行风险和复杂度是实际障碍。

【核心贡献】:
1. SPA (Step×Perturbation Alignment) 作为结构化依赖探测器：这是最独特的贡献。现有工作要么做answer-level perturbation (MATH-Perturb, VAR-MATH)，要么做step-level faithfulness without perturbation (Illusion of Reasoning)。将两者交叉——测量reasoning steps是否在perturbation的数学依赖结构中正确位置发生变化——是genuinely new的idea，且有清晰的理论动机（Decoupling Hypothesis的psychometric操作化）。
2. CAS-IRT框架本身：将contamination从binary detect-and-discard提升为continuous psychometric estimation，利用JECS p-values作为informative prior。三个技术优势（item difficulty calibration、continuous contamination、cross-item information borrowing）相对于non-IRT pipeline均有清晰的理论基础。
3. 实用价值：替代"defense by obsolescence"（不断造新benchmark）的contamination诊断范式，降低边际成本。Qwen2.5 RL contamination的retroactive case study是有说服力的motivation。

这些贡献对LLM evaluation领域有较大价值，特别是在contamination问题日益严重、现有IRT工作明确回避contamination的背景下。

【方法合理性】:
方法的核心架构（3PL IRT + contamination mixture）有坚实的psychometric先例（EM-IRT rapid-guessing detection），扩展到LLM contamination场景是合理的类比。JECS p-values作为Bayesian prior初始化contamination parameter是巧妙的设计——既避免了flat prior导致的identifiability问题，又保留了IRT框架的joint estimation优势。

潜在的更简单替代方案：
- **Pipeline approach (Baseline 6)**: JECS标记 → clean/contaminated分组 → 分别计算accuracy → 加权组合。这比CAS-IRT简单得多。Proposal明确将其设为baseline并承诺比较，这是正确的。但如果pipeline approach效果接近CAS-IRT，joint estimation的额外复杂度就难以justify。
- **Detect-then-filter (Baseline 2)**: 移除contaminated items后做标准IRT。更简单，但会丢失信息（contaminated items上的performance仍含genuine ability signal）。CAS-IRT的理论优势在于不丢弃数据。

关键methodological风险：
1. 3PL mixture的identifiability：即使有JECS prior，N=50模型下per-model×item contamination parameter的recovery质量存疑。Proposal有fallback（per-model shared c），但这大幅简化了contamination model。
2. SPA依赖step-level verification的准确性：GenPRM-1.5B在AIME难度问题上的step verification质量未经验证。Dual-source design (GenPRM + step ablation) 缓解了风险，但inter-source disagreement的处理方案（"agreement subset"）可能大幅缩小可用数据。
3. SymPy variant generation的覆盖度：geometry/combinatorics的低覆盖需要LLM-assisted perturbation，引入质量不确定性。

整体而言，方法设计是合理的，风险被正确识别且有mitigation策略，但成功执行需要多个组件同时work。

【5 维度打分】:

1. 研究问题: 【强】
   — 问题真实且重要：现有IRT-for-LLM工作（PSN-IRT, Growing Pains, metabench）全部假设zero contamination，而Growing Pains (arXiv 2604.12843) 明确指出contamination威胁anchor stability但未提出解决方案。Contamination detection社区（JECS, CoDeC）只做检测不做能力校正。这是一个documented but unaddressed gap。随着LLM evaluation stakes上升（benchmark-driven development, RL training feedback），decompose genuine ability vs. contamination artifact有真实的学术和实用需求。

2. 方法与创新: 【强】
   — SPA的novelty经调研确认成立：MATH-Perturb (ICML 2025) 和 VAR-MATH (arXiv 2507.12885) 均为answer-level，Illusion of Reasoning (arXiv 2603.22816) 做step-level但无perturbation interaction，PEARL (arXiv 2505.03019) 用bit-flip perturbation（表面级），EvalQReason (arXiv 2602.02295) 用step-level probability但无perturbation。SPA的step×perturbation交叉确实是unexplored的。CAS-IRT框架与DCR Factor (EMNLP 2025) 相比有明确的理论优势（IRT grounding vs. ad-hoc fuzzy inference）。与RIDE (arXiv 2511.04120) 的方向性互补关系论证清晰。唯一的concern是contribution密度——可能需要在8页内justify过多component。

3. 实验设计: 【强】
   — 这是proposal最突出的方面之一。Baselines覆盖了所有合理的替代方案（standard 3PL、detect-then-filter、DCR Factor、raw accuracy+perturbation、answer-level CAS-IRT、non-IRT pipeline），每个baseline都target一个specific question。Ablation table系统性地隔离每个component的贡献。三层validation (synthetic → known-contamination → predictive) 是psychometric研究的gold standard。Predictive validation使用time-stamped contamination-free benchmarks (AIME 2026/AMC 2026) 是clever的设计。Tiered evaluation (15 flagship + 80-100 open-weight) 在资源约束下是务实的。Human gold standard (250+ pairs, 2+ annotators, Cohen's κ) 体现了rigor。

4. 可行性: 【中】
   — 计算预算（~700-800 GPU-hours, ~$5K-10K API, ~200 person-hours, 10-14 weeks）对一个有GPU access的academic lab是可行的，但偏紧。主要可行性风险：(a) 闭源模型API成本波动和rate limiting可能影响Tier 1 full SPA；(b) SymPy variant generation的per-category coverage可能显著低于预期（geometry/combinatorics），导致algebra-only subset成为primary result；(c) GenPRM在variant上的calibration drift需要Platt scaling，但如果drift严重则scaling不够；(d) JECS是2026年5月的preprint，如果其pre-aggregation p-value extraction API/代码不公开或有bug，contamination prior的获取将受阻。14周timeline紧凑，留给troubleshooting的空间有限。

5. 写作与呈现: 【强】
   — Proposal本身的写作质量很高：research landscape分析详尽且准确（经调研验证），每个相关工作的差异化都有precise的论证。Core contributions的表述清晰，避免了overclaiming。Methodological risks被主动识别并附带mitigation策略，显示出成熟的研究态度。唯一的concern是信息密度极高——如果完整论文要在8+1页内呈现所有component（SPA定义、CAS-IRT formulation、variant generation、step verification、三层validation、6 baselines、全面ablation），writing和space management将是重大挑战。

【概率估计】: [30% - 42%] 中位 36%

【估计理由】:
上调因素：(1) 研究gap真实且经调研确认，PSN-IRT (AAAI 2026 Oral) 和Growing Pains均明确回避contamination建模；(2) SPA的novelty claim成立，在answer-level perturbation和step-level faithfulness之间开辟了新维度；(3) 实验设计在proposal阶段已达到unusually high completeness，baselines/ablations/validation均超过平均proposal水平；(4) 三社区统一的narrative有学术appeal，且timing argument (2025-2026才变得可行) 是convincing的；(5) AAAI接受LLM evaluation方向的工作（PSN-IRT获Oral）。

下调因素：(1) 系统复杂度极高，reviewer可能质疑"是一篇完整的论文还是三篇论文的拼接"；(2) additive decomposition的理论基础偏弱——如果interaction term在BIC/AIC中显著优于additive model，核心claim需要重新表述；(3) N=50 models下per-model×item contamination parameter的identifiability是genuine concern，fallback到per-model shared c实质上简化了contamination model的表达力；(4) 数学领域限定降低了generalizability，reviewer可能期望至少一个cross-domain extension；(5) 多个关键依赖组件（JECS p-values、GenPRM variant calibration、SymPy coverage）同时需要work，单一failure point可能cascade；(6) 8页内fitting all content将极其困难。

中位36%反映：这是一个方向正确、novelty genuine、设计严谨的solid proposal，但复杂度和执行风险使其处于"strong borderline"区域。如果实验结果clean（CAS-IRT显著优于所有baselines、SPA提供interpretable insights、synthetic recovery质量好），有机会进入accept区域；如果某个组件失败导致ablation不完整，则可能跌入reject区域。

【主要风险】:
1. **"Too many moving parts" 质疑**：审稿人可能认为IRT+contamination+perturbation+step-level四个组件中任意两个的组合就足以构成一篇论文，四合一导致每个component的depth不够。特别是如果某个ablation显示step-level SPA的marginal gain较小，该component的justify将困难。
2. **Identifiability failure at realistic N**：如果N=50模型下synthetic recovery的bias/RMSE不够好，即使fallback到per-model shared c也可能无法convincingly demonstrate CAS-IRT的估计质量优于simpler baselines (detect-then-filter)。这将直接削弱核心contribution。

【实施评估】:
  - 计算资源: ~700-800 A100-80G GPU-hours（开源模型inference + GenPRM step verification），$5K-10K API费用（闭源模型），对有GPU集群的学术团队可行但不轻松
  - 数据需求: MATH-500, AMC, AIME, GSM8K（均公开），需自行生成SymPy variants（geometry/combinatorics覆盖是瓶颈），AIME 2026/AMC 2026作为time-stamped held-out（公开可获取）
  - 人工介入: ~200 person-hours（250+ pairs human annotation, 2+ annotators），semi-automated pipeline降低单位成本，但仍需expertise in math problem verification
  - 训练需求: 无模型训练，仅inference + EM parameter estimation（计算开销可忽略）
  - 新 Benchmark: 不需要构建新benchmark，但需要生成SymPy variants（中等工程量）和human gold standard annotations（significant effort）
  - 预估周期: 10-14周（从pilot到submission-ready），紧凑但可行，前提是JECS代码和GenPRM模型按预期可用
```

Sources:
- [PSN-IRT - AAAI 2026 Oral](https://ojs.aaai.org/index.php/AAAI/article/view/40814)
- [PSN-IRT - arXiv](https://arxiv.org/abs/2505.15055)
- [JECS - Provable Joint Decontamination](https://arxiv.org/abs/2605.21543)
- [MATH-Perturb - ICML 2025](https://openreview.net/forum?id=OZy70UggXr)
- [VAR-MATH - arXiv](https://arxiv.org/abs/2507.12885)
- [RIDE - IRT-Guided Difficulty Perturbation](https://arxiv.org/abs/2511.04120)
- [DCR Factor - EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1173/)
- [GenPRM - AAAI 2026](https://arxiv.org/abs/2504.00891)
- [The Illusion of Reasoning](https://arxiv.org/abs/2603.22816)
- [Growing Pains - IRT Anchor Calibration](https://arxiv.org/abs/2604.12843)
- [Reasoning or Memorization - RL Data Contamination](https://arxiv.org/abs/2507.10532)


【原始 proposal（允许参考但不是主要依据）】:
# Decomposing LLM Ability via Contamination-Aware Step-Level IRT

## Core Problem

Current LLM evaluation conflates genuine reasoning, contamination-driven memorization, and robustness deficits into a single accuracy score. We disentangle these via calibrated decomposition (Observed = Genuine + Contamination − Robustness) with psychometric and statistical rigor.

## Core Contributions

1. **Step×Perturbation Alignment (SPA) as a structural dependency probe**: SPA measures whether a model's reasoning steps adapt in correspondence with the mathematical dependency structure when problem constraints change across original-variant pairs. If a model encodes genuine structural understanding, its reasoning trace changes at precisely the steps downstream of the perturbed constraint; memorizers either reproduce frozen templates or collapse at unpredictable points. No prior work measures this step×perturbation interaction: MATH-Perturb (ICML 2025) and VAR-MATH (arXiv 2507.12885) examine only answer-level drops; Illusion of Reasoning (arXiv 2603.22816) examines step faithfulness on single problems; EvalQReason (arXiv 2602.02295) measures step-level probability distributions without perturbation interaction. SPA provides the first psychometric operationalization of the Decoupling Hypothesis (Robust Answers Fragile Logic, arXiv 2505.17406)—decomposing decoupling into contamination-driven (memorization masking as reasoning) and robustness-driven (genuine ability insufficient for variant) components, going beyond MATCHA's binary adversarial verification.

2. **CAS-IRT Framework**: A contamination-aware extension of 3PL IRT that jointly estimates genuine ability θ, contamination susceptibility, and robustness deficit via EM. The additive decomposition is a first-order approximation; we additionally fit an interaction-term extension and use BIC/AIC model selection to validate whether additivity is sufficient. Three advantages over non-IRT pipeline approaches: (a) item difficulty calibration—contamination of easy vs. hard items has different impact on ability estimation; (b) continuous contamination modeling—JECS p-values as continuous prior, vs. binary detect-and-discard; (c) cross-item information borrowing—a model's performance on clean items informs its genuine ability estimate on contaminated items via shared θ.

3. **Three-Community Unification**: First framework bridging contamination detection (JECS, CoDeC), adversarial robustness (MATH-Perturb, VAR-MATH), and IRT-based evaluation (PSN-IRT, ATLAS, metabench). This combination was infeasible until 2025–2026: JECS (May 2026) provided the first conformal per-item contamination signal usable as IRT prior; VAR-MATH (2025) demonstrated scalable SymPy-backed variant generation; GenPRM (AAAI 2026) and Illusion of Reasoning (Mar 2026) simultaneously delivered step-level verification tools and faithfulness theory. Crucially, this is perturbation-informed IRT (perturbation response patterns improve IRT estimation), the inverse direction of RIDE (arXiv 2511.04120), which uses IRT-guided perturbation (IRT difficulty estimates guide perturbation generation). Both use IRT + perturbation, but for fundamentally different purposes.

4. **Training Diagnostic Application**: CAS-IRT enables decomposing benchmark improvement into genuine ability gain vs. contamination exploit vs. robustness deficit without constructing ad-hoc clean datasets. Retroactive case study: Reasoning or Memorization (arXiv 2507.10532, 2025) required building a fully synthetic dataset (RandomCalculation) to prove Qwen2.5's RL gains were contamination artifacts—a costly methodology. CAS-IRT could detect this directly from benchmark response patterns. More broadly, the community's current contamination defense relies on continually building new benchmarks ("defense by obsolescence"); CAS-IRT offers a complementary paradigm—diagnostic decomposition on existing benchmarks—with far lower marginal cost.

## Research Landscape

**IRT-for-LLM (assumes zero contamination):** PSN-IRT (AAAI 2026 Oral) analyzes 12 LLMs × 41,871 items, finding benchmark saturation and difficulty ceilings. ATLAS achieves 90% item reduction via adaptive testing. metabench captures 79.3% variance with sparse items. arXiv 2605.07046 scales IRT to 2211 models. Growing Pains (arXiv 2604.12843) uses multidimensional IRT across 400+ models, explicitly noting contamination threatens anchor stability but not modeling it. All assume zero contamination.

**IRT + perturbation (opposite direction):** RIDE (arXiv 2511.04120) uses IRT difficulty estimation to guide adversarial perturbation generation across 35 LLMs, achieving 21.73% average performance drop. RIDE's direction is IRT→perturbation (better benchmark construction); CAS-IRT's direction is perturbation→IRT (better ability estimation). The two are complementary, not competing.

**Contamination detection (detects without correcting):** CoDeC (ICLR 2026) achieves 99.9% AUC. JECS (arXiv 2605.21543) provides conformal guarantees with GCR control. DVD (arXiv 2601.04895) models memory-adherence vs. perturbation-drift dual states. RADAR achieves 93%. DeconIEP (arXiv 2601.19334) corrects contamination at inference time via embedding perturbation but requires model weight access and does not produce decomposed ability scores. None correct ability estimates within a psychometric framework.

**Score correction (ad-hoc):** DCR Factor (EMNLP 2025) adjusts scores via fuzzy inference on 9 models with ~4% average error, without IRT grounding.

**Perturbation robustness (answer-level only):** MATH-Perturb (ICML 2025): o1-mini drops 16.49% on hard perturbations. VAR-MATH (arXiv 2507.12885): RL-trained models drop 47–73%. Both answer-level only.

**Step-level reasoning (no perturbation interaction):** Illusion of Reasoning (arXiv 2603.22816) identifies three CoT patterns with step necessity 4–93%. ProcessBench (ACL 2025) finds 51.8% process errors. Fragile Thoughts (arXiv 2603.03332) documents snowball effects. Robust Answers Fragile Logic (arXiv 2505.17406) validates the Decoupling Hypothesis via MATCHA. PEARL (arXiv 2505.03019) validates PSH using bit-flip perturbation—surface-level, distinct from structural algebraic variants. EvalQReason (arXiv 2602.02295) uses step-level probability distributions (CSD/SFC) for reasoning evaluation without perturbation.

**Key differentiations:**
- vs. RIDE: Same building blocks (IRT + perturbation), opposite directions. RIDE: IRT→perturbation (benchmark construction). CAS-IRT: perturbation→IRT (ability estimation + contamination decomposition).
- vs. DVD: Binary detection vs. continuous psychometric quantification.
- vs. PEARL: Bit-flip input perturbation vs. structural algebraic variants enabling step-level analysis.
- vs. DCR Factor: Ad-hoc adjustment vs. joint IRT estimation with calibrated parameters.
- vs. DeconIEP: Inference-time model correction (requires weight access) vs. evaluation-time score decomposition (model-agnostic, works on closed-source).
- vs. Agent Psychometrics (arXiv 2604.00594, ICLR 2026 Workshop): Decomposes observable architectural components (LLM vs. scaffold); CAS-IRT decomposes latent confounders requiring identification via JECS priors + perturbation design.

## Proposed Approach

**Model specification.** Extend 3PL IRT with contamination mixture: P(correct|θ,d,c) = c·p_mem + (1−c)·σ(a(θ−d)), where c is the contamination indicator per model×item, initialized from JECS pre-aggregation per-model×item conformal p-values (extracted before JECS's max-p aggregation; see JECS arXiv 2605.21543). p_mem is constant in the base specification; item-dependent p_mem(d) tested as extension. Interaction term c·(1−r)·p_interaction fitted alongside the additive model, compared via BIC/AIC.

**Identifiability safeguards.** The 3PL mixture faces known identifiability challenges (Bayesian EMM for 3PLM, PMC6555200). Mitigations: (a) informative Bayesian prior on c centered at JECS p-values; (b) synthetic parameter recovery across regimes (N=50,100,200 models × contamination rates 5%,15%,30%); (c) multi-start EM with convergence diagnostics; (d) if N=50 recovery proves insufficient, fallback to per-model contamination susceptibility (shared c across items per model), substantially reducing parameter count. N=50 recovery quality is reported as primary since it matches the experimental regime.

**Variant generation.** SymPy-backed algebraic variants for MATH-500, AMC, AIME, GSM8K. Pilot: per-category coverage estimation across MATH-500's 7 categories. For low-coverage categories (expected: geometry, combinatorics), LLM-assisted perturbation + human verification following MATH-Perturb (ICML 2025). Variant quality protocol: each variant verified on (a) structural preservation (same solution steps), (b) difficulty preservation (answer magnitude/solution length proxy), (c) targeted parameter change only. Report per-category coverage and per-method quality metrics (human verification pass rate). Algebra-only subset ablation to check variant method bias.

**SPA metric.** For each original-variant pair:
- Impact point definition (model-independent): SymPy dependency graph identifies which solution steps are downstream of the perturbed variable. Impact point = first dependent step.
- Step-level correctness transition: each step → (correct_orig, correct_variant) in four states.
- Reasoning divergence point: first substantive divergence between traces, compared against SymPy-derived impact point. Tolerance window ±1 step. Memorization signature: divergence too early or too late relative to impact point.
- Normalized by perturbation scope. Report both strict SPA and relaxed SPA (±1 tolerance).
- Human gold standard includes impact point annotation (2+ annotators, Cohen's κ); SymPy-derived vs. human-annotated impact points compared in ablation.

**Step-level verification (dual-source, equal status).** Source 1: GenPRM (AAAI 2026), using GenPRM-1.5B for compute efficiency. Source 2: Illusion of Reasoning step ablation (remove-one-step, observe answer change)—PRM-independent, equally applicable to originals and variants. ThinkPRM (arXiv 2504.16828) as additional cross-check. Pilot (50–100 items × 3 models): measure GenPRM original vs. variant step-level accuracy against human gold standard; report inter-source agreement (Cohen's κ). If GenPRM shows systematic variant degradation, apply Platt scaling calibration. Core SPA uses agreement subset; full-set as sensitivity analysis. Human gold standard: 250+ stratified pairs (benchmarks × perturbation types × difficulty), 2+ annotators, semi-automated pipeline (auto-annotate → human correct). Budget by difficulty: GSM8K ~5 min/pair, MATH-500 ~15 min/pair, AIME ~30 min/pair; total ~150–200 person-hours.

**Tiered evaluation.** Tier 1 (~15 flagship models: DeepSeek-R1, Qwen3, GLM-4.7, Kimi-K2.5, Llama-4, GPT-4o, Claude, Gemini): full SPA on all items. Tier 2 (~80–100 open-weight models via vLLM batch inference): answer-level on originals+variants + JECS pipeline, sampled step-level on 15% of items. Total ~100–115 models for IRT calibration.

**Estimation.** Joint EM yields per-model genuine ability θ, contamination susceptibility, robustness deficit. Grounded in EM-IRT rapid-guessing detection precedent from human psychometrics.

## Validation Protocol

**Synthetic validation:** Simulated response matrices with known θ, c, robustness. EM recovery (bias, RMSE) across regime variations. N=50 regime reported as primary. Identifiability boundary mapping.

**Known-contamination validation:** Open-source models with partially known training data (e.g., Llama series): CAS-IRT contamination estimates vs. known overlap.

**Predictive validation (multi-benchmark tiered):**
- Primary: AIME 2026 / AMC 2026 (competition date past training cutoffs, time-stamped contamination-free). Bootstrap CIs reported given small item count (~25–30 per competition).
- Secondary: FrontierMath Tier 1–3 (arXiv 2411.04872, Epoch AI; same-domain difficult math; note: Epoch AI quality review ongoing as of May 2026—report scores with caveat). Tier 4 reported separately (research-level, tests transfer beyond training difficulty range).
- Exploratory: LiveCodeBench (cross-domain transfer).
- All: compare Spearman/Kendall of θ_genuine vs. raw accuracy vs. standard IRT θ.

## Baselines

1. **Standard 3PL IRT** (PSN-IRT approach): no contamination modeling.
2. **Detect-then-filter**: JECS removes contaminated items → standard 3PL on clean subset.
3. **DCR Factor post-hoc** (EMNLP 2025): ad-hoc contamination correction.
4. **Raw accuracy + perturbation drop**: no IRT.
5. **Answer-level CAS-IRT**: full model without step-level SPA.
6. **Non-IRT pipeline decomposition**: JECS labels + separate accuracy computation on clean/contaminated/variant sets → post-hoc weighted combination without IRT. Tests whether IRT joint estimation adds value over simple pipeline.

Evaluation: (a) ranking correlation with held-out benchmarks; (b) contamination detection precision/recall; (c) synthetic parameter recovery; (d) robustness prediction accuracy.

## Ablation Design

| Configuration | Contamination | Perturbation | Step-level |
|---|---|---|---|
| Standard 3PL IRT | ✗ | ✗ | ✗ |
| + Contamination only | ✓ (JECS init) | ✗ | ✗ |
| + Perturbation only | ✗ | ✓ | ✗ |
| + Contamination + Perturbation (answer-level) | ✓ | ✓ | ✗ |
| Full CAS-IRT | ✓ | ✓ | ✓ |

Additional: JECS init vs. uniform init; variants per item (1, 3, 5); GenPRM vs. step-ablation vs. ensemble SPA; EM convergence; additive vs. interaction (BIC/AIC); algebra-only vs. full-coverage; SymPy-only vs. mixed-method variants; per-model c vs. per-model×item c; SymPy-derived vs. human-annotated impact points.

## Compute Budget

Tier 1 (~15 models, full SPA): 400–500 A100-80G GPU-hours for open-weight models (including 671B MoE via multi-GPU); $3,000–8,000 API for closed-source. Tier 2 (~80–100 models, answer-level + 15% step-level): ~150–200 GPU-hours via vLLM batch. Step verification (GenPRM-1.5B): ~50 GPU-hours. Human annotation (250+ pairs, semi-automated, 2 annotators): ~150–200 person-hours. Pilot studies: ~50 GPU-hours + 30 person-hours. Total: ~700–800 GPU-hours, ~$5,000–10,000 API, ~200 person-hours. Timeline: 10–14 weeks from pilot to submission-ready.

## Key References

- Lost in Benchmarks? PSN-IRT (AAAI 2026 Oral)
- metabench: A Sparse Benchmark (ICLR 2025)
- ATLAS: Adaptive Testing for LLM Evaluation (arXiv 2025)
- DCR: Quantifying Data Contamination (EMNLP 2025)
- JECS: Provable Joint Decontamination (arXiv 2605.21543, 2026)
- CoDeC: Detecting Contamination via In-Context Learning (ICLR 2026)
- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026)
- ThinkPRM: Process Reward Models That Think (arXiv 2504.16828)
- The Illusion of Reasoning (arXiv 2603.22816, 2026)
- Reasoning or Memorization? RL Data Contamination (arXiv 2507.10532, 2025)
- MATH-Perturb (ICML 2025)
- FrontierMath: Advanced Math Reasoning (arXiv 2411.04872, Epoch AI)
- Growing Pains: IRT Anchor Calibration (arXiv 2604.12843, 2026)
- Scalable IRT for 2211 Models (arXiv 2605.07046, 2026)
- RIDE: IRT-Guided Difficulty Perturbation (arXiv 2511.04120)
- DVD: Detection via Variance of Distribution (arXiv 2601.04895, 2026)
- DeconIEP: Inference-Time Decontamination (arXiv 2601.19334, 2026)
- PEARL: Perturbation Sensitivity Hypothesis (arXiv 2505.03019, 2025)
- EvalQReason: Step-Level Reasoning Evaluation (arXiv 2602.02295, 2026)
- VAR-MATH: Symbolic Variant Benchmark (arXiv 2507.12885, 2025)
- ProcessBench: Process Error Identification (ACL 2025)
- Robust Answers Fragile Logic: Decoupling Hypothesis (arXiv 2505.17406, 2025)
- Fragile Thoughts: Snowball Effects in CoT (arXiv 2603.03332, 2026)
- Agent Psychometrics: IRT for Agentic Coding (arXiv 2604.00594, ICLR 2026 Workshop)
- Bayesian EMM for 3PLM (PMC6555200)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "20d0771e-b54d-4f1a-82b8-f14ba5c5af21",
  "type": "user",
  "uuid": "0a802727-21f8-480a-b4f3-a857bcf468c9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T07:19:16.626Z_

```json
{
  "parentUuid": "0a802727-21f8-480a-b4f3-a857bcf468c9",
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
  "uuid": "0fa0321a-93d4-4cff-ae30-932b1660588a",
  "timestamp": "2026-05-29T07:19:16.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T07:19:16.626Z_

```json
{
  "parentUuid": "0fa0321a-93d4-4cff-ae30-932b1660588a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d28bc685-f9c1-40e4-939f-91d88fb200fa",
  "timestamp": "2026-05-29T07:19:16.626Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6",
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to produce a thorough evalua…",
  "leafUuid": "d28bc685-f9c1-40e4-939f-91d88fb200fa",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Decomposing LLM ability via contamination-aware IRT",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6"
}
```

---

### Assistant

_source line 8 · 2026-05-29T07:19:49.529Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the three independent reviews and produce a Meta Judge synthesis.

First, let me extract the key numbers and assessments:

**Reviewer 1:**
- Probability: [33% - 48%] 中位 40%
- Rubric scores: 研究问题【强】, 方法与创新【强】, 实验设计【强】, 可行性【中】, 写作与呈现【中】
- Tendency: weak accept
- Main risks: Identifiability + "why so complex", paper organization

**Reviewer 2:**
- Probability: [32% - 42%] 中位 37%


- Rubric scores: 研究问题【强】, 方法与创新【中偏强】, 实验设计【强】, 可行性【中】, 写作与呈现【强】
- Tendency: weak accept
- Main risks: "组合式创新" perception, CAS-IRT vs detect-then-filter marginal improvement

**Reviewer 3:**
- Probability: [30% - 42%] 中位 36%
- Rubric scores: 研究问题【强】, 方法与创新【强】, 实验设计【强】

, 可行性【中】, 写作与呈现【强】
- Tendency: borderline accept-leaning
- Main risks: "Too many moving parts", Identifiability failure at realistic N

Now I'm calculating the consensus across reviewers. The three midpoints average to about 37.67%, with a median of 37% and very tight standard deviation around 1.70%, indicating strong agreement. All three reviewers rated the research question as strong, which is a clear consensus point.

Looking at where the reviewers align, experimental design and feasibility both show unanimous agreement, while methodology and innovation lean toward strong with one reviewer slightly lower. Writing quality has two reviewers rating it strong. The critical risks that emerged across all three reviews are identifiability problems at small sample sizes, the complexity of the model with too many interacting components, and questions about whether the CAS-IRT approach offers meaningful improvement over a simpler detect-then-filter strategy.

Beyond those universal concerns, all three flagged page constraints, and there's a tension between treating this as engineering optimization versus genuine research innovation. The one outlier is the first reviewer's lower writing assessment compared to the other two. Given how tightly the reviewers clustered—only about 1.7% standard deviation—I should anchor to the median scores and tighten my confidence intervals. The three ranges converge around 30-48%, so I'm looking at where they overlap most.

Taking the median of their lower bounds gives me 32%, and the median of their upper bounds is 42%. The first reviewer's 48% ceiling is generous compared to the others, so I'll respect that constraint without pushing beyond it. For the final estimate, I'm settling on roughly 32-43%, with the midpoint around 37-38%—this reflects strong consensus that this sits at the borderline between weak accept and accept, without being more lenient than the most generous reviewer or harsher than the most critical.

Now I'm consolidating the implementation assessments, where all three reviewers align on the core requirements: 700-800 GPU-hours plus $5K-10K in API costs, around 200 person-hours for annotation work, no model training involved, a 10-14 week timeline, with SymPy variant generation as the main engineering challenge and JECS code availability as a potential dependency risk. I'll write up the synthesis now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d28bc685-f9c1-40e4-939f-91d88fb200fa",
  "isSidechain": false,
  "requestId": "req_011CbWTGY7K4xNKTVZJuyH5B",
  "type": "assistant",
  "uuid": "d0363ef1-95fa-42ee-8edf-86f5fce5b79f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cDhTevj23wrPTkr3cXAj9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20510,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3322,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20510
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

_source line 9 · 2026-05-29T07:20:33.204Z_

【阶段】: Meta Judge
【三次中位】: [40%, 37%, 36%]  std=1.7%
【共识维度】: 
- 研究问题【强】（3/3 一致）：所有现有 IRT-for-LLM 工作假设零 contamination 是 documented but unaddressed gap，PSN-IRT 获 AAAI 2026 Oral 验证方向认可
- 实验设计【强】（3/3 一致）：6 个 baseline 覆盖所有合理替代方案，三层 validation（synthetic → known-contamination → predictive）是 psychometric gold standard，ablation 系统性极强
- 可行性【中】（3/3 一致）：700-800 GPU-hours 可行但偏紧，多组件依赖链（JECS + SymPy + GenPRM）的 cascade failure 风险，14 周 timeline 紧凑
- 方法与创新【强/中偏强】（2/3 强，1/3 中偏强）：SPA 的 step×perturbation 交互经三人独立调研确认 novelty 成立；"组合式创新"的 perception 风险是共识 concern
- 写作与呈现【强/中】（2/3 强，1/3 中）：文献综述和差异化论证质量极高，但 8 页空间限制下的内容压缩是共识风险
- **共识风险**（3/3 均提到）：(a) N=50 regime 下 identifiability；(b) "too many moving parts" / over-engineering 质疑；(c) CAS-IRT vs detect-then-filter 的 marginal improvement 不确定性；(d) 8 页篇幅约束

【异常维度】: 
- 审稿人 1 写作与呈现【中】为 outlier（其余两人【强】）——R1 的 concern 更侧重"能否在 8 页内讲清楚"这一执行层面风险，而非 proposal 本身的写作质量。降权处理：proposal 写作质量本身无问题，但篇幅管理风险作为共识风险保留
- 审稿人 2 方法与创新【中偏强】为 slight outlier（其余两人【强】）——R2 对"组合式创新 = engineering contribution"的 concern 更强。此 concern 有合理性但属主观 perception，不降低 rubric 判决，作为风险因素保留
- 审稿人 1 上界 48% 为 outlier（其余两人上界均 42%）——R1 的乐观情景假设"所有实验结果清晰 + 写作到位"，但这需要多个乐观条件同时满足。按宁缺毋滥原则，上界取 R2/R3 的 42% 而非 R1 的 48%

【最终概率】: [32% - 42%] 中位 37%
【一致性】: 高（std=1.7%，三人 rubric 判决高度一致，倾向均为 weak accept / borderline accept-leaning）
【综合理由】: 
三位审稿人在几乎所有维度上高度收敛：研究问题重要且 timely（3/3 强）、实验设计在 proposal 阶段罕见地完备（3/3 强）、SPA 的 novelty 经独立调研确认成立（3/3）、可行性有风险但可控（3/3 中）。核心分歧极小——仅 R2 对方法创新性略保守（中偏强 vs 强），R1 对写作呈现略悲观（中 vs 强）。

概率判定逻辑：
- **Idea 天花板**：研究问题【强】+ 方法创新【强/中偏强】→ idea 质量允许的天花板约 42-45%。SPA 是 genuinely novel 的贡献，但"组合式创新"的 perception 风险限制了上界
- **实验地板**：实验设计【强】确保了下限不会因设计缺陷被击穿。三层 validation + 系统 ablation 是强有力的 defense。但可行性【中】意味着执行风险可能拖低实际结果
- **中位 37%** 反映：这是一篇方向正确、gap 真实、novelty genuine、设计严谨的 solid 投稿，位于 AAAI 接收线（~23-25%）上方但非"稳中"区间。核心不确定性在于 (a) CAS-IRT 是否能 convincingly 优于 simpler baselines，(b) 8 页内能否清晰呈现全部贡献——这两者只有实验和写作完成后才能确定
- 上界 42% 取 R2/R3 共识而非 R1 的 48%（宁缺毋滥）；下界 32% 取三人下界中位

【建议】: 边缘（偏积极侧——如果实验结果 clean 且写作凝练，有实质中稿机会；但需要多个条件同时满足）

【实施评估】:
  - 计算资源: ~700-800 A100-80G GPU-hours（开源模型推理 + GenPRM step verification）+ $5K-10K API（闭源模型）。671B MoE 需多 GPU 推理，有工程复杂度。对有 GPU 集群的学术团队可行
  - 数据需求: MATH-500、AMC、AIME、GSM8K（均公开）；SymPy variants 需自行生成（geometry/combinatorics 低覆盖是瓶颈）；AIME 2026/AMC 2026 作为 held-out（公开）；FrontierMath 需申请（Epoch AI 质量审核进行中）
  - 人工介入: ~150-200 person-hours（250+ pairs × 2+ annotators），需具备数学背景的标注者。Semi-automated pipeline 降低单位成本但不消除。标注质量一致性有要求
  - 训练需求: 无模型训练。GenPRM-1.5B 和 JECS pipeline 均有开源实现，仅需 inference + EM 参数估计
  - 新 Benchmark: 不构建新 benchmark，但需生成数千 SymPy-backed algebraic variants（中等工程量）+ human gold standard annotations（significant effort）
  - 预估周期: 10-14 周（从 pilot 到 submission-ready）。紧凑但可行，前提是 2-3 人全职投入、JECS 代码可用、无重大技术障碍。关键路径：variant generation + human annotation 可能成为瓶颈

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0363ef1-95fa-42ee-8edf-86f5fce5b79f",
  "isSidechain": false,
  "requestId": "req_011CbWTGY7K4xNKTVZJuyH5B",
  "type": "assistant",
  "uuid": "875bfc77-5910-41c0-9ed2-32f292ad49e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011cDhTevj23wrPTkr3cXAj9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20510,
      "cache_read_input_tokens": 16543,
      "output_tokens": 3322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3322,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 20510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20510
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
  "lastPrompt": "【任务】: 请以「角色 A'：Meta Judge」综合以下 3 位审稿人对同一 proposal 的独立评估，给出稳健的最终客观概率估计。严格按 Meta Judge 输出格式输出。  【三位审稿人评估】: ━━━━━━━━━━ 审稿人 1（独立评审）━━━━━━━━━━ Now I have sufficient information to produce a thorough evalua…",
  "leafUuid": "875bfc77-5910-41c0-9ed2-32f292ad49e0",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Decomposing LLM ability via contamination-aware IRT",
  "sessionId": "69038657-ab9a-4d76-b530-7cafdadb1db6"
}
```

---
