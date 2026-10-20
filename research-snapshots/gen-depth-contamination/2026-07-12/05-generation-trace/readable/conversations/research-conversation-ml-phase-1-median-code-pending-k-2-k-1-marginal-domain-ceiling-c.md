# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 c

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/bb9f5c87-e174-4459-9a60-98cfb2795a48.jsonl`
- **Structured JSON:** [`378f46576735effad465.json`](../../sessions/37/378f46576735effad465.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T09:19:05.144Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T09:19:05.144Z",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑\n核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domain competence 不足）', 'Qwen-7B Code K*=2 但 marginal（1v2 AUC CI lower 接近 0.60）', \"Code ceiling=2 仅 3/5 模型达到，需从 'ceiling=2' 软化为 'ceiling=2 for models with sufficient code training'\", 'arXiv Qwen-7B cross-scorer K*=3→2 的下降被一位审稿人视为 scorer confound 未完全控制的证据', '一位审稿人认为 C3 negative results（Pythia, arXiv）削弱 practical relevance', 'θ-sensitivity 被要求做更详细分析（θ=0.55-0.70 全谱呈现）']\n关键指标范围：{'code_models_at_ceiling2_of_5': [3, 3], 'code_mistral7b_1v2_auc': [0.56, 0.62], 'code_qwen7b_1v2_auc': [0.6, 0.66], 'domain_ceiling_clean_fit_pct': [85, 92], 'cross_scorer_kstar_preservation_rate': [0.75, 0.85], 'c3_binary_vs_nofilter_hellaswag_delta_pp': [3.8, 6.1], 'estimated_reviewer_excitement': [3.3, 3.7], 'emnlp_main_accept_prob': [0.25, 0.5]}\n叙事方向：C1' 核心成立但 claims 需降级。Domain ceiling 从 \"predictive framework\" 调整为 \"empirical tendency with domain×competence interaction\"：中间复杂度域（C4, Code） 的 K* 受 model domain-specific competence 调制，极端域（Wiki, arXiv）稳健。Code 域叙事从 \"ceiling=2 cross-family confirmed\" 改为 \"ceiling=2 observed in models with adequate code pretraining (Qwen, LLaMA); insufficient code competence yields K*=1 (Pythia, Mistral), consistent with C4 Mistral pattern\"。C3 的 scope 在 Limitations 中更显著呈现，承认 filtering advantage 限于 homogeneous web text + 单一 base model (Qwen-1.5B)，不泛化到 arXiv 或其他 base models。补充实验：可能需要 arXiv cross-scorer bootstrap CI 的完整呈现、 θ-sensitivity full sweep figure。目标 EMNLP Findings 或 borderline Main。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\nfocus: Code domain cross-model results now include LLaMA-8B K*=2 (cross-family confirmed) + cross-scorer validation K*=2 (D079). Mistral-7B and Qwen-7B Code still RUNNING. Domain hierarchy: Wiki=1, C4=Code=2, arXiv=3. Retrain K*=7 (two families). Focus on: (1) whether 4-domain + 6-architecture-family coverage is sufficient for EMNLP accept; (2) C3 filtering weakness (negative results on arXiv/Pythia); (3) Excitement score — is domain ceiling framework + one-wash laundering concept enough to push from 3.5 to 4.0?\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）\n- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。**Cross-family validation (D079, D080)**: LLaMA-3.1-8B K*=2 (1v2 AUC=0.7394, CI [0.729, 0.750], JSD cliff 13.5x, scored by Qwen) confirmed Code ceiling=2 不是 Qwen 家族特有。Pythia-1.4B scorer 重评 Qwen Code generations K*=2 confirmed (Δ=-1.9pp)。与 Wiki 域的 scorer confound（same-family scorer inflates K* 1→2）形成对比，说明 scorer confound 是域相关（domain-specific）而非系统性的。当前状态：Qwen-1.5B K*=2, LLaMA-8B K*=2, Pythia-1.4B K*=1; Mistral-7B/Qwen-7B pending\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (8/9 configurations)**\n> **8/9 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？\"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 \"异常\"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n11. **\"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?\"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 5K docs, depth\n    0-5, scorer=Qwen2.5-1.5B. 测试 K* 是否随模型规模变化。（实际参数已从原计划 1K/depth 0-3 扩展以匹配其他实验配置）'\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  registry_id: exp_004_7b_crossscale\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: exp_006_graduated_filtering\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: exp_008_retrain_chain_v2\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: '>=4'\n    pairwise_auc:\n      0v1: 0.9847\n      1v2: 0.9484\n      2v3: 0.8888\n      3v4: 0.7982\n    pairwise_jsd:\n      0v1: 0.17\n      1v2: 0.12\n      2v3: 0.064\n      3v4: 0.04\n    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts\n      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic\n      boundary.\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: exp_009_dose_50pct\n  status: DONE\n  conclusion: failed\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: exp_011_llm_zeroshot\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_012_binary_confidence\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features。如果 neural probe 也给 K*=2 → C1'' claim 从 \"our features\n    find K*=2\" 升级为 \"K*=2 is data-intrinsic boundary\"。[D014 升级 P0：Reviewer 评估为最高边际价值实验]'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_015_neural_probe\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_016_base_vs_instruct\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- id: exp-018\n  claim: 1\n  description: 'Cross-family universality: LLaMA-3.1-8B, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 跨模型家族验证 K*。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_018_llama8b_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9225\n      1v2: 0.6123\n      2v3: 0.5274\n      3v4: 0.5138\n      4v5: 0.5097\n    jsd:\n      0v1: 0.077\n      1v2: 0.012\n      2v3: 0.005\n    bootstrap_ci:\n      0v1:\n        auc: 0.9224\n        ci_lower: 0.9174\n        ci_upper: 0.9272\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6123\n        ci_lower: 0.6028\n        ci_upper: 0.6216\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5273\n        ci_lower: 0.5169\n        ci_upper: 0.5378\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5168\n        ci_lower: 0.5062\n        ci_upper: 0.5275\n        perm_p: 0.0037\n      4v5:\n        auc: 0.5159\n        ci_lower: 0.5052\n        ci_upper: 0.5268\n        perm_p: 0.0035\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n- id: exp-019\n  claim: 1\n  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_019_mistral7b_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9843\n      1v2: 0.5935\n      2v3: 0.5402\n      3v4: 0.5232\n      4v5: 0.5181\n    bootstrap_ci_1v2:\n      ci_lower: 0.5835\n      ci_upper: 0.6032\n      p_auc_leq_060: 0.9017\n    jsd:\n      0v1: 0.124194\n      1v2: 0.008051\n      2v3: 0.005047\n      3v4: 0.004516\n      4v5: 0.004109\n    ordinal_mae: 1.2275\n    ordinal_accuracy: 0.3567\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n- id: exp-020\n  claim:\n  - 1\n  - 3\n  description: 'Pythia-1.4B decoding ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2,\n    C4 5K docs, depth 0-5. 跨模型验证解码策略对 K* 的不变性。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: exp_020_pythia_decoding\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy:\n      K_star: 2\n      auc:\n        0v1: 0.9992\n        1v2: 0.8838\n        2v3: 0.5342\n        3v4: 0.5228\n        4v5: 0.5162\n    nuc09:\n      K_star: 2\n      auc:\n        0v1: 0.9948\n        1v2: 0.677\n        2v3: 0.5549\n        3v4: 0.5299\n        4v5: 0.5013\n    t07:\n      K_star: 2\n      auc:\n        0v1: 0.9965\n        1v2: 0.7265\n        2v3: 0.5941\n        3v4: 0.5698\n        4v5: 0.5284\n    t12:\n      K_star: 2\n      auc:\n        0v1: 0.9933\n        1v2: 0.6172\n        2v3: 0.5226\n        3v4: 0.517\n        4v5: 0.5051\n- id: exp-021\n  claim: 1\n  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512\n    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_021_length_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    128tok:\n      K_star: 2\n      1v2_auc: 0.6219\n    256tok:\n      K_star: 2\n      1v2_auc: 0.6282\n    512tok:\n      K_star: 2\n      1v2_auc: 0.6073\n    all_K_star_2: true\n    bootstrap_ci:\n      512tok_1v2:\n        auc: 0.6073\n        ci_lower: 0.5979\n        ci_upper: 0.6166\n        perm_p: 0.0001\n        verdict: BORDERLINE\n- id: exp-022\n  claim:\n  - 1\n  - 2\n  description: '4x4 cross-scorer matrix: 4 generators × 4 scorers, 验证 scorer independence\n    完整性。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-021\n  registry_id: exp_022_cross_scorer_matrix\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 12\n    completed: 12\n    K_star_distribution:\n      K2: 11\n      K1: 1\n    matrix:\n      pythia_greedy×olmo:\n        K_star: 2\n        1v2: 0.8811\n      pythia_greedy×pythia:\n        K_star: 2\n        1v2: 0.8838\n      pythia_greedy×qwen_base:\n        K_star: 2\n        1v2: 0.8814\n      pythia_greedy×qwen_instruct:\n        K_star: 2\n        1v2: 0.8818\n      qwen_base×olmo:\n        K_star: 2\n        1v2: 0.6047\n      qwen_base×pythia:\n        K_star: 2\n        1v2: 0.617\n      qwen_base×qwen_base:\n        K_star: 2\n        1v2: 0.6262\n      qwen_base×qwen_instruct:\n        K_star: 2\n        1v2: 0.6273\n      qwen_cont256×olmo:\n        K_star: 2\n        1v2: 0.6028\n      qwen_cont256×pythia:\n        K_star: 1\n        1v2: 0.5979\n      qwen_cont256×qwen_base:\n        K_star: 2\n        1v2: 0.6282\n      qwen_cont256×qwen_instruct:\n        K_star: 2\n        1v2: 0.6072\n    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:\n      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to\n      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'\n- id: exp-023\n  claim:\n  - 1\n  description: 'Domain ablation: Wikipedia seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 验证 K*=2 是否跨数据域一致（C4\n    vs Wikipedia）。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_023_domain_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    1v2_auc: 0.6193\n    2v3_auc: 0.5498\n    all_folds_above_060: true\n    top_feature: freq_entropy\n    ordinal_accuracy: 0.377\n- id: exp-024\n  claim:\n  - 1\n  description: 'Domain ablation: arXiv abstracts seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 第三域验证—— 技术文本与\n    web text (C4) / 百科 (Wikipedia) 分布差异大，三域一致则 domain 维度从 Limitation 升级为 evidence。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_024_arxiv_domain\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    pairwise_auc:\n      0v1: 0.9946\n      1v2: 0.858\n      2v3: 0.6427\n      3v4: 0.5437\n      4v5: 0.5294\n    bootstrap_ci:\n      0v1:\n        auc: 0.9946\n        ci_lower: 0.9929\n        ci_upper: 0.9961\n        perm_p: 0.0001\n      1v2:\n        auc: 0.858\n        ci_lower: 0.848\n        ci_upper: 0.8679\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6427\n        ci_lower: 0.6275\n        ci_upper: 0.6575\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5437\n        ci_lower: 0.5276\n        ci_upper: 0.5598\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5294\n        ci_lower: 0.5133\n        ci_upper: 0.5455\n        perm_p: 0.0006\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First\n      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\n- id: exp-025\n  claim: 3\n  description: 'Pythia-1.4B filtering replication: LoRA rank=8 continued pretraining\n    on C4 depth chain, 3 strategies (binary/graduated/no-filter) × 3 seeds, MMLU+HellaSwag.\n    验证 filtering strategy ordering 跨模型一致性。'\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - exp-006\n  - exp-001\n  registry_id: exp_025_pythia_filtering\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 9/9\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    mmlu:\n      no_filter: 0.2568±0.0012\n      binary_ours: 0.2585±0.0004\n      graduated_a09: 0.2561±0.0009\n    hellaswag:\n      no_filter: 0.5250±0.0008\n      binary_ours: 0.5251±0.0001\n      graduated_a09: 0.5253±0.0007\n    delta_vs_no_filter:\n      binary_ours_mmlu: '+0.0017'\n      binary_ours_hellaswag: '+0.0000'\n      graduated_a09_mmlu: '-0.0007'\n      graduated_a09_hellaswag: '+0.0003'\n    key_finding: All three filtering strategies produce nearly identical results on\n      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering\n      binary>graduated>no_filter NOT confirmed.\n- id: exp-026\n  claim: 3\n  description: 'arXiv graduated vs binary filtering: Qwen2.5-1.5B base + LoRA rank=4,\n    arXiv depth chain (K*=3), 3 strategies (no_filter/binary/graduated α=0.9^d) ×\n    5 seeds, MMLU+HellaSwag. 关键实验：K*=3 域上 graduated 应超越 binary，展示 K*-aware filtering\n    增量价值。'\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - exp-006\n  - exp-024\n  registry_id: exp_026_arxiv_filtering\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 15/15\n    strategies:\n    - no_filter\n    - binary\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    mmlu:\n      no_filter: 0.5899±0.0008\n      binary: 0.5876±0.0004\n      graduated_a09: 0.5900±0.0011\n    hellaswag:\n      no_filter: 0.6600±0.0002\n      binary: 0.6642±0.0004\n      graduated_a09: 0.6599±0.0003\n    delta_vs_no_filter:\n      binary_mmlu: '-0.0023'\n      binary_hellaswag: '+0.0042'\n      graduated_mmlu: '+0.0001'\n      graduated_hellaswag: '-0.0001'\n    key_finding: All three strategies produce nearly identical results. Graduated\n      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU\n      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\n- id: exp-027\n  claim: 1\n  description: 'LaTeX markup removal ablation: 去除 arXiv 文本中的 LaTeX 格式标记后重新提取 15D features，验证\n    K*=3 是否依赖格式特征而非内容层 depth signal。排除替代假说。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-024\n  registry_id: exp_027_latex_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    k_star_preserved: true\n    pairwise_auc_original:\n      0v1: 0.9948\n      1v2: 0.8581\n      2v3: 0.6436\n      3v4: 0.544\n      4v5: 0.5299\n    pairwise_auc_stripped:\n      0v1: 0.9948\n      1v2: 0.8297\n      2v3: 0.6229\n      3v4: 0.5468\n      4v5: 0.5476\n    auc_delta:\n      0v1: 0\n      1v2: -0.028\n      2v3: -0.021\n      3v4: 0.003\n      4v5: 0.018\n    latex_reduction_by_depth:\n      depth_0: 0.6%\n      depth_5: 4.4%\n    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still\n      >θ=0.60). LaTeX format is NOT a confound.\n- id: exp-028\n  claim: 1\n  description: 'Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples,\n    确定 K*=2 判定所需最低样本量。回应 m4 reviewer concern。'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-007\n  registry_id: exp_028_power_curve\n  status: DONE\n  conclusion: success\n  metrics:\n    min_n_100pct: 2000\n    n500_auc: 0.5808\n    n500_rate: 0.2\n    n1000_auc: 0.5911\n    n1000_rate: 0.3\n    n2000_auc: 0.6101\n    n2000_rate: 1\n    n3000_auc: 0.6166\n    n3000_rate: 1\n    n4000_auc: 0.622\n    n4000_rate: 1\n    n5000_auc: 0.6288\n    n5000_rate: 1\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- exp_id: exp_011_llm_zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- exp_id: exp_015_neural_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- exp_id: exp_006_graduated_filtering\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- exp_id: exp_004_7b_crossscale\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- exp_id: exp_A_alt_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9923\n      auc_1v2: 0.7012\n      auc_2v3: 0.587\n      mae: 1.006\n      accuracy: 0.417\n      spearman_rho_vs_baseline: 0.906\n    pythia_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.99\n      auc_1v2: 0.5923\n      auc_2v3: null\n      mae: 1.216\n      accuracy: 0.371\n      spearman_rho_vs_baseline: 0.942\n    olmo_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9918\n      auc_1v2: 0.6947\n      auc_2v3: null\n      mae: 1.016\n      accuracy: 0.413\n      spearman_rho_vs_baseline: 0.92\n    olmo_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.989\n      auc_1v2: 0.5858\n      auc_2v3: null\n      mae: 1.229\n      accuracy: 0.368\n      spearman_rho_vs_baseline: 0.902\n    key_finding: 'K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1\n      (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer\n      independence of feature ranking.'\n- exp_id: exp_B_14d_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    result: K*=2 stable across all 4 models after removing self_BLEU (14D)\n    key_finding: self_BLEU removal does not change K* boundary. FR-3 resolved.\n- exp_id: exp_C_permutation_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    resamples: 10000\n    all_boundary_pairs_p: <0.0001\n    key_finding: 10K permutation confirms all boundary p-values well below 0.01. FR-11\n      resolved.\n- exp_id: exp_D_obd_n500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    obd_accuracy_final: 0.38\n    obd_ci:\n    - 0.34\n    - 0.422\n    mcnemar_vs_gpt55_p: 0.0809\n    mcnemar_vs_claude_p: 0.0693\n    mcnemar_significant: false\n    multi_seed_std: 0\n    per_depth:\n      d0: 0.96\n      d1: 0.39\n      d2: 0.14\n      d3: 0.19\n      d4: 0.22\n    prob_merge_accuracy: 0.444\n    prob_merge_d4_bias: 0.8\n    note: v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant\n      — supports discussion.tex narrative\n- exp_id: exp_E_paired_stats\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_significant_pairs: 8/15\n    hellaswag_significant_pairs: 9/15\n    binary_ours_vs_all_mmlu: all significant\n    max_cohen_d_mmlu: 10.8\n    max_cohen_d_hellaswag: 8.98\n    graduated_a09_vs_dsir_corrected_p: 0.0523\n    cohen_d_method: d_av (Lakens 2013)\n    key_finding: 'binary-ours significantly outperforms all alternatives on MMLU.\n      On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni\n      cummax bug fixed: MMLU 10/15→8/15. Cohen''s d changed to d_av.'\n    bugfix_note: Holm-Bonferroni cummax variable was never updated, causing 2 MMLU\n      pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal\n      vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\n- exp_id: exp_012_binary_confidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- exp_id: exp_kstar_theta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    output_files:\n    - kstar_theta_curve.pdf (32KB)\n    - kstar_theta_curve.png (335KB)\n    models:\n    - Qwen-rewrite\n    - Pythia\n    - OLMo\n    - Qwen-cont\n    depth_pairs: 5\n    key_finding: All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5.\n      θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical\n      resolved.\n- exp_id: exp_016_base_vs_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- exp_id: exp_018_llama8b_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9225\n      1v2: 0.6123\n      2v3: 0.5274\n      3v4: 0.5138\n      4v5: 0.5097\n    jsd:\n      0v1: 0.077\n      1v2: 0.012\n      2v3: 0.005\n    bootstrap_ci:\n      0v1:\n        auc: 0.9224\n        ci_lower: 0.9174\n        ci_upper: 0.9272\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6123\n        ci_lower: 0.6028\n        ci_upper: 0.6216\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5273\n        ci_lower: 0.5169\n        ci_upper: 0.5378\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5168\n        ci_lower: 0.5062\n        ci_upper: 0.5275\n        perm_p: 0.0037\n      4v5:\n        auc: 0.5159\n        ci_lower: 0.5052\n        ci_upper: 0.5268\n        perm_p: 0.0035\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n- exp_id: exp_019_mistral7b_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9843\n      1v2: 0.5935\n      2v3: 0.5402\n      3v4: 0.5232\n      4v5: 0.5181\n    bootstrap_ci_1v2:\n      ci_lower: 0.5835\n      ci_upper: 0.6032\n      p_auc_leq_060: 0.9017\n    jsd:\n      0v1: 0.124194\n      1v2: 0.008051\n      2v3: 0.005047\n      3v4: 0.004516\n      4v5: 0.004109\n    ordinal_mae: 1.2275\n    ordinal_accuracy: 0.3567\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n- exp_id: exp_020_pythia_decoding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy:\n      K_star: 2\n      auc:\n        0v1: 0.9992\n        1v2: 0.8838\n        2v3: 0.5342\n        3v4: 0.5228\n        4v5: 0.5162\n    nuc09:\n      K_star: 2\n      auc:\n        0v1: 0.9948\n        1v2: 0.677\n        2v3: 0.5549\n        3v4: 0.5299\n        4v5: 0.5013\n    t07:\n      K_star: 2\n      auc:\n        0v1: 0.9965\n        1v2: 0.7265\n        2v3: 0.5941\n        3v4: 0.5698\n        4v5: 0.5284\n    t12:\n      K_star: 2\n      auc:\n        0v1: 0.9933\n        1v2: 0.6172\n        2v3: 0.5226\n        3v4: 0.517\n        4v5: 0.5051\n- exp_id: exp_021_length_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    128tok:\n      K_star: 2\n      1v2_auc: 0.6219\n    256tok:\n      K_star: 2\n      1v2_auc: 0.6282\n    512tok:\n      K_star: 2\n      1v2_auc: 0.6073\n    all_K_star_2: true\n    bootstrap_ci:\n      512tok_1v2:\n        auc: 0.6073\n        ci_lower: 0.5979\n        ci_upper: 0.6166\n        perm_p: 0.0001\n        verdict: BORDERLINE\n- exp_id: exp_022_cross_scorer_matrix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 12\n    completed: 12\n    K_star_distribution:\n      K2: 11\n      K1: 1\n    matrix:\n      pythia_greedy×olmo:\n        K_star: 2\n        1v2: 0.8811\n      pythia_greedy×pythia:\n        K_star: 2\n        1v2: 0.8838\n      pythia_greedy×qwen_base:\n        K_star: 2\n        1v2: 0.8814\n      pythia_greedy×qwen_instruct:\n        K_star: 2\n        1v2: 0.8818\n      qwen_base×olmo:\n        K_star: 2\n        1v2: 0.6047\n      qwen_base×pythia:\n        K_star: 2\n        1v2: 0.617\n      qwen_base×qwen_base:\n        K_star: 2\n        1v2: 0.6262\n      qwen_base×qwen_instruct:\n        K_star: 2\n        1v2: 0.6273\n      qwen_cont256×olmo:\n        K_star: 2\n        1v2: 0.6028\n      qwen_cont256×pythia:\n        K_star: 1\n        1v2: 0.5979\n      qwen_cont256×qwen_base:\n        K_star: 2\n        1v2: 0.6282\n      qwen_cont256×qwen_instruct:\n        K_star: 2\n        1v2: 0.6072\n    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:\n      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to\n      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'\n- exp_id: exp_019b_mistral_cross_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9209\n      1v2: 0.5695\n      2v3: 0.5335\n      3v4: 0.514\n      4v5: 0.5184\n    bootstrap_ci:\n      0v1:\n        mean: 0.9209\n        ci_lower: 0.9189\n        ci_upper: 0.9229\n        pass_060: true\n      1v2:\n        mean: 0.5696\n        ci_lower: 0.5645\n        ci_upper: 0.5746\n        pass_060: false\n      2v3:\n        mean: 0.5335\n        ci_lower: 0.5283\n        ci_upper: 0.5382\n        pass_060: false\n      3v4:\n        mean: 0.514\n        ci_lower: 0.5063\n        ci_upper: 0.5213\n        pass_060: false\n      4v5:\n        mean: 0.5183\n        ci_lower: 0.5128\n        ci_upper: 0.5244\n        pass_060: false\n    jsd:\n      0v1: 0.08355\n      1v2: 0.007642\n      2v3: 0.004752\n      3v4: 0.004255\n      4v5: 0.003758\n    ordinal_mae: 1.3737\n    ordinal_accuracy: 0.3179\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n    key_finding: Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2\n      AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral\n      K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\n- exp_id: exp_023_domain_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    1v2_auc: 0.6193\n    2v3_auc: 0.5498\n    all_folds_above_060: true\n    top_feature: freq_entropy\n    ordinal_accuracy: 0.377\n- exp_id: exp_024_arxiv_domain\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    pairwise_auc:\n      0v1: 0.9946\n      1v2: 0.858\n      2v3: 0.6427\n      3v4: 0.5437\n      4v5: 0.5294\n    bootstrap_ci:\n      0v1:\n        auc: 0.9946\n        ci_lower: 0.9929\n        ci_upper: 0.9961\n        perm_p: 0.0001\n      1v2:\n        auc: 0.858\n        ci_lower: 0.848\n        ci_upper: 0.8679\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6427\n        ci_lower: 0.6275\n        ci_upper: 0.6575\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5437\n        ci_lower: 0.5276\n        ci_upper: 0.5598\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5294\n        ci_lower: 0.5133\n        ci_upper: 0.5455\n        perm_p: 0.0006\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First\n      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\n- exp_id: exp_025_pythia_arxiv\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.9877\n      1v2: 0.8047\n      2v3: 0.6545\n      3v4: 0.5507\n      4v5: 0.5287\n    pairwise_jsd:\n      0v1: 0.171338\n      1v2: 0.057344\n      2v3: 0.019524\n      3v4: 0.009917\n      4v5: 0.008846\n    bootstrap_ci:\n      0v1:\n        auc: 0.9876\n        ci_lower: 0.9851\n        ci_upper: 0.99\n        perm_p: 0.0001\n      1v2:\n        auc: 0.8047\n        ci_lower: 0.7934\n        ci_upper: 0.8162\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6544\n        ci_lower: 0.6401\n        ci_upper: 0.6688\n        perm_p: 0.0001\n      3v4:\n        auc: 0.55\n        ci_lower: 0.534\n        ci_upper: 0.5657\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5284\n        ci_lower: 0.5122\n        ci_upper: 0.5443\n        perm_p: 0.001\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    n_samples: 2200\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_mean\n    - surp_d1_skew\n    - surp_d1_mean\n    ordinal:\n      MAE: 0.8518\n      Accuracy: 0.4545\n    key_finding: Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv).\n      2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for\n      arXiv.\n- exp_id: exp_008_retrain_chain\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-008-retrain-chain\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_retrain_chain_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: '>=4'\n    pairwise_auc:\n      0v1: 0.9847\n      1v2: 0.9484\n      2v3: 0.8888\n      3v4: 0.7982\n    pairwise_jsd:\n      0v1: 0.17\n      1v2: 0.12\n      2v3: 0.064\n      3v4: 0.04\n    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts\n      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic\n      boundary.\n- exp_id: exp_009_dose_response\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 45\n    seeds: 5\n    ratios:\n    - 0.1\n    - 0.3\n    - 0.5\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated\n    cross_ratio_finding: 'Binary filtering consistently best across all ratios. Graduated\n      filtering = no_filter at every ratio. Effect size of binary advantage increases\n      with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp).\n      Original C3 hypothesis (graduated > binary) rejected.'\n    gpu_hours_total: 9.9\n- exp_id: exp_009_dose_10pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_30pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_50pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_10pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_30pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_50pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_10pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6058±0.0002\n        hellaswag: 0.6689±0.0007\n      binary_ours:\n        mmlu: 0.6079±0.0005\n        hellaswag: 0.6727±0.0008\n      graduated:\n        mmlu: 0.6066±0.0011\n        hellaswag: 0.6700±0.0015\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0021\n        p_mmlu: 0.001\n        delta_hellaswag: 0.0038\n        p_hellaswag: 0.0017\n      graduated_vs_binary:\n        delta_mmlu: -0.0014\n        p_mmlu: 0.0917\n        delta_hellaswag: -0.0027\n        p_hellaswag: 0.0399\n      graduated_vs_nofilter:\n        delta_mmlu: 0.0008\n        p_mmlu: 0.2706\n        delta_hellaswag: 0.0011\n        p_hellaswag: 0.0611\n    key_finding: Binary best. Graduated ≈ no_filter.\n- exp_id: exp_009_dose_30pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6069±0.0007\n        hellaswag: 0.6664±0.0020\n      binary_ours:\n        mmlu: 0.6082±0.0012\n        hellaswag: 0.6725±0.0007\n      graduated:\n        mmlu: 0.6072±0.0008\n        hellaswag: 0.6665±0.0014\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0013\n        p_mmlu: 0.0739\n        delta_hellaswag: 0.0061\n        p_hellaswag: 0.0036\n      graduated_vs_binary:\n        delta_mmlu: -0.001\n        p_mmlu: 0.3018\n        delta_hellaswag: -0.006\n        p_hellaswag: 0.0009\n      graduated_vs_nofilter:\n        delta_mmlu: 0.0003\n        p_mmlu: 0.6638\n        delta_hellaswag: 0.0002\n        p_hellaswag: 0.6646\n    key_finding: Binary best on HellaSwag (p=0.004). Graduated = no_filter.\n- exp_id: exp_009_dose_50pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6063±0.0013\n        hellaswag: 0.6680±0.0005\n      binary_ours:\n        mmlu: 0.6088±0.0011\n        hellaswag: 0.6731±0.0004\n      graduated:\n        mmlu: 0.6062±0.0009\n        hellaswag: 0.6679±0.0002\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0025\n        p_mmlu: 0.0377\n        delta_hellaswag: 0.0051\n        p_hellaswag: 2.0e-05\n      graduated_vs_binary:\n        delta_mmlu: -0.0026\n        p_mmlu: 0.0257\n        delta_hellaswag: -0.0052\n        p_hellaswag: 3.0e-05\n      graduated_vs_nofilter:\n        delta_mmlu: -0.0001\n        p_mmlu: 0.89\n        delta_hellaswag: -0.0001\n        p_hellaswag: 0.706\n    key_finding: Binary significantly best (HellaSwag p<0.001). Graduated = no_filter\n      exactly.\n- exp_id: exp_026_feature_stability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_016_qwen_base (prompt-chain, K*=2)\n    results:\n      15D:\n        num_tested: 1\n        num_kstar_2: 1\n        min_1v2_auc: 0.6262\n        mean_1v2_auc: 0.6262\n      10D:\n        num_tested: 5\n        num_kstar_2: 5\n        min_1v2_auc: 0.6153\n        mean_1v2_auc: 0.6191\n      8D:\n        num_tested: 5\n        num_kstar_2: 5\n        min_1v2_auc: 0.6056\n        mean_1v2_auc: 0.6159\n      5D:\n        num_tested: 5\n        num_kstar_2: 2\n        min_1v2_auc: 0.5856\n        mean_1v2_auc: 0.5998\n      3D_top3:\n        num_tested: 1\n        num_kstar_2: 0\n        min_1v2_auc: 0.5871\n        mean_1v2_auc: 0.5871\n    all_above_theta: false\n    key_finding: 'Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust\n      (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856).\n      Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where\n      all subsets trivially passed (min=0.8314).'\n    previous_run_note: v1 used retrain-chain data (K*=4), where all subsets trivially\n      passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary\n      robustness.\n- exp_id: exp_027_retrain_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_iterations: 10000\n    pairs:\n      0v1:\n        auc_point: 0.9847\n        ci_lower: 0.9828\n        ci_upper: 0.9864\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      1v2:\n        auc_point: 0.9482\n        ci_lower: 0.9443\n        ci_upper: 0.952\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      2v3:\n        auc_point: 0.8885\n        ci_lower: 0.8829\n        ci_upper: 0.894\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      3v4:\n        auc_point: 0.7977\n        ci_lower: 0.7903\n        ci_upper: 0.8051\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n    key_finding: All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min\n      CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\n- exp_id: exp_027\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kstar_ci: 4\n    0v1_auc: 0.9847\n    0v1_ci:\n    - 0.9828\n    - 0.9864\n    0v1_perm_p: 0.0001\n    1v2_auc: 0.9482\n    1v2_ci:\n    - 0.9443\n    - 0.952\n    1v2_perm_p: 0.0001\n    2v3_auc: 0.8885\n    2v3_ci:\n    - 0.8829\n    - 0.894\n    2v3_perm_p: 0.0001\n    3v4_auc: 0.7977\n    3v4_ci:\n    - 0.7903\n    - 0.8051\n    3v4_perm_p: 0.0001\n    all_ci_lower_above_theta: true\n- exp_id: exp_026_feature_stability_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_001_pythia prompt-chain (K*=2)\n    results:\n      15D:\n        num_tested: 1\n        num_pass: 1\n        min_1v2_auc: 0.6262\n        mean_1v2_auc: 0.6262\n      10D:\n        num_tested: 5\n        num_pass: 5\n        min_1v2_auc: 0.6153\n        mean_1v2_auc: 0.6191\n      8D:\n        num_tested: 5\n        num_pass: 5\n        min_1v2_auc: 0.6056\n        mean_1v2_auc: 0.6159\n      5D:\n        num_tested: 5\n        num_pass: 2\n        min_1v2_auc: 0.5856\n        mean_1v2_auc: 0.5998\n      3D_top3:\n        num_tested: 1\n        num_pass: 0\n        min_1v2_auc: 0.5871\n        mean_1v2_auc: 0.5871\n    key_finding: 8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile\n      (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\n- exp_id: exp_arXiv_olmo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.9958\n    auc_1v2: 0.5034\n    auc_2v3: 0.5069\n    auc_3v4: 0.5021\n    auc_4v5: 0.5037\n    jsd_0v1: 0.329\n    ordinal_acc: 0.33\n- exp_id: exp_arXiv_llama8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    auc_0v1: 0.9754\n    auc_1v2: 0.8447\n    auc_2v3: 0.6215\n    auc_3v4: 0.5362\n    auc_4v5: 0.5331\n    jsd_0v1: 0.1296\n    jsd_1v2: 0.0785\n    jsd_2v3: 0.0177\n    ordinal_acc: 0.4549\n    ordinal_mae: 0.8806\n- exp_id: exp_wiki_pythia\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_wiki_olmo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_wiki_pythia_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.975\n    auc_1v2: 0.5846\n    auc_2v3: 0.5445\n    auc_3v4: 0.5205\n    auc_4v5: 0.5168\n    jsd_0v1: 0.080065\n    jsd_1v2: 0.007773\n    ordinal_acc: 0.3503\n- exp_id: exp_wiki_olmo_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.9932\n    auc_1v2: 0.4986\n    auc_2v3: 0.5012\n    auc_3v4: 0.5057\n    auc_4v5: 0.5009\n    jsd_0v1: 0.1688\n    ordinal_acc: 0.3227\n- exp_id: exp_arXiv_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.983\n      1v2: 0.835\n      2v3: 0.626\n      3v4: 0.544\n      4v5: 0.513\n    pairwise_jsd:\n      0v1: 0.1656\n      1v2: 0.0668\n      2v3: 0.0156\n      3v4: 0.0089\n      4v5: 0.0061\n    ordinal_mae: 0.9\n    ordinal_accuracy: 0.446\n- exp_id: exp_wiki_llama8b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    ordinal_mae: 1.2954\n    ordinal_accuracy: 0.3313\n    auc_0v1: 0.9316\n    auc_1v2: 0.5954\n    auc_2v3: 0.5392\n    auc_3v4: 0.5221\n    auc_4v5: 0.5212\n    jsd_0v1: 0.06169\n    jsd_1v2: 0.00931\n- exp_id: exp_arXiv_mistral7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.9848\n      1v2: 0.8201\n      2v3: 0.6275\n      3v4: 0.5295\n      4v5: 0.5295\n    jsd:\n      0v1: 0.14249\n      1v2: 0.076232\n      2v3: 0.018972\n      3v4: 0.009908\n      4v5: 0.008877\n    ordinal_mae: 0.8958\n    ordinal_accuracy: 0.4474\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_mean\n    - surp_d2_mean\n- exp_id: exp_wiki_mistral7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 1\n    ordinal_mae: 1.3445\n    ordinal_accuracy: 0.3273\n    auc_0v1: 0.9607\n    auc_1v2: 0.5552\n    auc_2v3: 0.5236\n    auc_3v4: 0.5181\n    auc_4v5: 0.5012\n    jsd_0v1: 0.054134\n    jsd_1v2: 0.005678\n    jsd_2v3: 0.003698\n    jsd_3v4: 0.003459\n    jsd_4v5: 0.003274\n- exp_id: exp_14b_c4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9598\n      1v2: 0.621\n      2v3: 0.5494\n      3v4: 0.5243\n      4v5: 0.5154\n    pairwise_jsd:\n      0v1: 0.1097\n      1v2: 0.0112\n      2v3: 0.0062\n      3v4: 0.0044\n      4v5: 0.0036\n    bootstrap_ci:\n      0v1:\n      - 0.9564\n      - 0.963\n      1v2:\n      - 0.6119\n      - 0.6304\n      2v3:\n      - 0.5392\n      - 0.5594\n      3v4:\n      - 0.514\n      - 0.5346\n      4v5:\n      - 0.5045\n      - 0.5265\n    permutation_p:\n      0v1: <0.001\n      1v2: <0.001\n      2v3: <0.001\n      3v4: <0.001\n      4v5: <0.001\n    k_star_statistically_confirmed: true\n    ordinal_mae: 1.2266\n    ordinal_accuracy: 0.3497\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_d2_mean\n    key_finding: K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119)\n      > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\n- exp_id: exp_32b_c4\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_wiki_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    auc_0v1: 0.9673\n    auc_1v2: 0.6108\n    auc_2v3: 0.5562\n    auc_3v4: 0.5297\n    auc_4v5: 0.529\n    jsd_0v1: 0.083514\n    jsd_1v2: 0.010991\n    jsd_2v3: 0.00555\n    jsd_3v4: 0.004611\n    jsd_4v5: 0.003894\n    ordinal_mae: 1.2501\n    ordinal_accuracy: 0.3532\n- exp_id: exp_wiki_scorer_confound\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    confound_verdict: confirmed\n    auc_0v1: 0.9404\n    auc_1v2: 0.587\n    auc_2v3: 0.5456\n    auc_3v4: 0.525\n    auc_4v5: 0.5172\n    critical_delta_1v2: -0.0238\n- exp_id: exp_wiki_scorer_confound_1b5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    confound_verdict: confirmed\n    auc_0v1: 0.9729\n    auc_1v2: 0.5994\n    auc_2v3: 0.533\n    auc_3v4: 0.5214\n    auc_4v5: 0.5068\n    jsd_0v1: 0.0886\n    ordinal_mae: 1.2995\n    ordinal_accuracy: 0.3466\n- exp_id: exp_arXiv_qwen7b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 2\n    auc_0v1: 0.9575\n    auc_1v2: 0.8171\n    auc_2v3: 0.5989\n    auc_3v4: 0.5417\n    auc_4v5: 0.5192\n    jsd_0v1: 0.137085\n    jsd_1v2: 0.059688\n    jsd_2v3: 0.013508\n    jsd_3v4: 0.009125\n    jsd_4v5: 0.006738\n    ordinal_mae: 0.9617\n    ordinal_accuracy: 0.4255\n- exp_id: exp_arXiv_qwen1b5_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    auc_0v1: 0.9748\n    auc_1v2: 0.8105\n    auc_2v3: 0.6317\n    auc_3v4: 0.5437\n    auc_4v5: 0.5294\n    jsd_0v1: 0.154297\n    jsd_1v2: 0.066782\n    jsd_2v3: 0.019268\n    jsd_3v4: 0.008867\n    jsd_4v5: 0.006991\n    ordinal_mae: 0.9017\n    ordinal_accuracy: 0.4402\n- exp_id: exp_arXiv_llama8b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    auc_0v1: 0.9629\n    auc_1v2: 0.8433\n    auc_2v3: 0.6201\n    auc_3v4: 0.523\n    auc_4v5: 0.5245\n    jsd_0v1: 0.1214\n    jsd_1v2: 0.0815\n    jsd_2v3: 0.0195\n    jsd_3v4: 0.0083\n    jsd_4v5: 0.0082\n    ordinal_mae: 0.9025\n    ordinal_accuracy: 0.4407\n    scorer: pythia-1.4b\n- exp_id: exp_arXiv_mistral7b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    scorer: pythia-1.4b\n    auc_0v1: 0.9798\n    auc_1v2: 0.8141\n    auc_2v3: 0.6075\n    auc_3v4: 0.5489\n    auc_4v5: 0.5391\n    jsd_0v1: 0.135575\n    jsd_1v2: 0.078\n    jsd_2v3: 0.020452\n    jsd_3v4: 0.010992\n    jsd_4v5: 0.008831\n    ordinal_mae: 0.9061\n    ordinal_accuracy: 0.4412\n- exp_id: exp_025_pythia_filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 9/9\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    mmlu:\n      no_filter: 0.2568±0.0012\n      binary_ours: 0.2585±0.0004\n      graduated_a09: 0.2561±0.0009\n    hellaswag:\n      no_filter: 0.5250±0.0008\n      binary_ours: 0.5251±0.0001\n      graduated_a09: 0.5253±0.0007\n    delta_vs_no_filter:\n      binary_ours_mmlu: '+0.0017'\n      binary_ours_hellaswag: '+0.0000'\n      graduated_a09_mmlu: '-0.0007'\n      graduated_a09_hellaswag: '+0.0003'\n    key_finding: All three filtering strategies produce nearly identical results on\n      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering\n      binary>graduated>no_filter NOT confirmed.\n- exp_id: exp_026_arxiv_filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 15/15\n    strategies:\n    - no_filter\n    - binary\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    mmlu:\n      no_filter: 0.5899±0.0008\n      binary: 0.5876±0.0004\n      graduated_a09: 0.5900±0.0011\n    hellaswag:\n      no_filter: 0.6600±0.0002\n      binary: 0.6642±0.0004\n      graduated_a09: 0.6599±0.0003\n    delta_vs_no_filter:\n      binary_mmlu: '-0.0023'\n      binary_hellaswag: '+0.0042'\n      graduated_mmlu: '+0.0001'\n      graduated_hellaswag: '-0.0001'\n    key_finding: All three strategies produce nearly identical results. Graduated\n      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU\n      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\n- exp_id: exp_027_latex_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    k_star_preserved: true\n    pairwise_auc_original:\n      0v1: 0.9948\n      1v2: 0.8581\n      2v3: 0.6436\n      3v4: 0.544\n      4v5: 0.5299\n    pairwise_auc_stripped:\n      0v1: 0.9948\n      1v2: 0.8297\n      2v3: 0.6229\n      3v4: 0.5468\n      4v5: 0.5476\n    auc_delta:\n      0v1: 0\n      1v2: -0.028\n      2v3: -0.021\n      3v4: 0.003\n      4v5: 0.018\n    latex_reduction_by_depth:\n      depth_0: 0.6%\n      depth_5: 4.4%\n    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still\n      >θ=0.60). LaTeX format is NOT a confound.\n- exp_id: exp_028_subsampling_power\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_1000:\n      mean_auc: 0.608\n      std: 0.012\n      detection_prob: 0.9\n    n_2500:\n      mean_auc: 0.618\n      std: 0.006\n      detection_prob: 1\n    n_5000:\n      mean_auc: 0.629\n      std: 0\n      detection_prob: 1\n    key_finding: n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal\n      is robust, not large-sample artifact.\n- exp_id: exp_olmo_retrain_chain\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_olmo_retrain_v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_code_qwen1b5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    theta: 0.6\n    auc_0v1: 0.9388\n    auc_1v2: 0.7382\n    auc_2v3: 0.53\n    auc_3v4: 0.5022\n    auc_4v5: 0.5219\n    ci_0v1:\n    - 0.929\n    - 0.949\n    ci_1v2:\n    - 0.709\n    - 0.767\n    ci_2v3:\n    - 0.514\n    - 0.546\n    jsd_0v1: 0.0814\n    jsd_1v2: 0.0443\n    jsd_2v3: 0.0038\n    ordinal_accuracy: 0.359\n    ordinal_mae: 1.204\n- exp_id: exp_code_llama8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    pairwise_auc:\n      0v1: 0.9161\n      1v2: 0.7394\n      2v3: 0.5112\n      3v4: 0.52\n      4v5: 0.4996\n    pairwise_auc_std:\n      0v1: 0.004\n      1v2: 0.0101\n      2v3: 0.0095\n      3v4: 0.0137\n      4v5: 0.0069\n    pairwise_jsd:\n      0v1: 0.060406\n      1v2: 0.047034\n      2v3: 0.003473\n      3v4: 0.003026\n      4v5: 0.002892\n    ordinal_mae: 1.2542\n    ordinal_accuracy: 0.3485\n    top_features:\n    - freq_entropy\n    - surp_d1_mean\n    - surp_d2_mean\n- exp_id: exp_qwen_retrain_chain\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star_lower_bound: 4\n    theta: 0.6\n    auc_0v1: 0.9838\n    auc_1v2: 0.8969\n    auc_2v3: 0.81\n    auc_3v4: 0.7624\n    ci_0v1:\n    - 0.982\n    - 0.9855\n    ci_1v2:\n    - 0.8937\n    - 0.9001\n    ci_2v3:\n    - 0.8052\n    - 0.8147\n    ci_3v4:\n    - 0.7543\n    - 0.7706\n    ci_method: 5-fold CV\n    jsd_0v1: 0.2263\n    jsd_1v2: 0.1046\n    jsd_2v3: 0.0752\n    jsd_3v4: 0.0654\n- exp_id: exp_code_pythia1b4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    theta: 0.6\n    pairwise_auc:\n      0v1:\n        mean: 0.9592\n        std: 0.0036\n        folds:\n        - 0.9576\n        - 0.9576\n        - 0.9657\n        - 0.96\n        - 0.9552\n      1v2:\n        mean: 0.5983\n        std: 0.005\n        folds:\n        - 0.601\n        - 0.5884\n        - 0.6\n        - 0.5997\n        - 0.6024\n      2v3:\n        mean: 0.5215\n        std: 0.0128\n        folds:\n        - 0.5236\n        - 0.5124\n        - 0.5311\n        - 0.5024\n        - 0.5381\n      3v4:\n        mean: 0.5152\n        std: 0.012\n        folds:\n        - 0.4981\n        - 0.5327\n        - 0.5092\n        - 0.5123\n        - 0.5238\n      4v5:\n        mean: 0.5046\n        std: 0.0137\n        folds:\n        - 0.4983\n        - 0.4822\n        - 0.5074\n        - 0.5224\n        - 0.5128\n    jsd:\n      0v1: 0.070173\n      1v2: 0.008211\n      2v3: 0.003674\n      3v4: 0.002902\n      4v5: 0.002685\n    ordinal:\n      mae: 1.3268\n      accuracy: 0.3357\n    top_features:\n    - freq_entropy\n    - surp_d1_mean\n    - surp_d2_mean\n    - surp_mean\n    - surp_d1_skew\n    features_csv: /root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv\n- exp_id: exp_028_power_curve\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    min_n_100pct: 2000\n    n500_auc: 0.5808\n    n500_rate: 0.2\n    n1000_auc: 0.5911\n    n1000_rate: 0.3\n    n2000_auc: 0.6101\n    n2000_rate: 1\n    n3000_auc: 0.6166\n    n3000_rate: 1\n    n4000_auc: 0.622\n    n4000_rate: 1\n    n5000_auc: 0.6288\n    n5000_rate: 1\n- exp_id: exp_code_mistral7b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_code_qwen7b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_qwen_retrain_depth7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 7\n    theta: 0.6\n    max_depth: 7\n    analysis_method: 5-fold GroupKFold CV\n    pairwise_auc:\n      0v1:\n        mean: 0.9837\n        std: 0.0019\n        ci_95:\n        - 0.9821\n        - 0.9854\n        folds:\n        - 0.9832\n        - 0.9821\n        - 0.9837\n        - 0.9823\n        - 0.9873\n      1v2:\n        mean: 0.8971\n        std: 0.0025\n        ci_95:\n        - 0.8949\n        - 0.8993\n        folds:\n        - 0.8923\n        - 0.8988\n        - 0.8986\n        - 0.8991\n        - 0.8967\n      2v3:\n        mean: 0.8098\n        std: 0.0052\n        ci_95:\n        - 0.8052\n        - 0.8144\n        folds:\n        - 0.8086\n        - 0.8074\n        - 0.818\n        - 0.8024\n        - 0.8128\n      3v4:\n        mean: 0.76\n        std: 0.0082\n        ci_95:\n        - 0.7528\n        - 0.7672\n        folds:\n        - 0.7534\n        - 0.7617\n        - 0.7753\n        - 0.7566\n        - 0.7531\n      4v5:\n        mean: 0.7459\n        std: 0.0091\n        ci_95:\n        - 0.7379\n        - 0.7538\n        folds:\n        - 0.7429\n        - 0.7562\n        - 0.7521\n        - 0.73\n        - 0.7482\n      5v6:\n        mean: 0.7017\n        std: 0.0068\n        ci_95:\n        - 0.6958\n        - 0.7076\n        folds:\n        - 0.7006\n        - 0.7077\n        - 0.7104\n        - 0.6915\n        - 0.6984\n      6v7:\n        mean: 0.641\n        std: 0.0039\n        ci_95:\n        - 0.6376\n        - 0.6445\n        folds:\n        - 0.6419\n        - 0.6349\n        - 0.6464\n        - 0.639\n        - 0.643\n    jsd:\n      0v1: 0.23005\n      1v2: 0.103924\n      2v3: 0.075049\n      3v4: 0.065398\n      4v5: 0.060509\n      5v6: 0.034998\n      6v7: 0.017652\n- exp_id: exp_pythia_retrain_depth7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kstar: 7\n    pairwise_auc:\n      0v1: 0.9844\n      1v2: 0.947\n      2v3: 0.8891\n      3v4: 0.7999\n      4v5: 0.6907\n      5v6: 0.6497\n      6v7: 0.634\n    pairwise_auc_ci:\n      0v1:\n      - 0.9829\n      - 0.9858\n      1v2:\n      - 0.9418\n      - 0.9522\n      2v3:\n      - 0.8822\n      - 0.896\n      3v4:\n      - 0.7951\n      - 0.8047\n      4v5:\n      - 0.688\n      - 0.6934\n      5v6:\n      - 0.6429\n      - 0.6565\n      6v7:\n      - 0.6275\n      - 0.6406\n    pairwise_jsd:\n      0v1: 0.1775\n      1v2: 0.1286\n      2v3: 0.1069\n      3v4: 0.0643\n      4v5: 0.0331\n      5v6: 0.0271\n      6v7: 0.0138\n- exp_id: exp_code_qwen1b5_pythia_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    theta: 0.6\n    auc_0v1: 0.9076\n    auc_1v2: 0.7197\n    auc_2v3: 0.5308\n    auc_3v4: 0.5236\n    auc_4v5: 0.5084\n    jsd_0v1: 0.065423\n    jsd_1v2: 0.035809\n    jsd_2v3: 0.004315\n    jsd_3v4: 0.003182\n    jsd_4v5: 0.003047\n    ordinal_mae: 1.2578\n    ordinal_accuracy: 0.3433\n    scorer: pythia-1.4b\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T09:19:05.149Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T09:19:05.149Z",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-19T09:19:05.189Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑
核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domain competence 不足）', 'Qwen-7B Code K*=2 但 marginal（1v2 AUC CI lower 接近 0.60）', "Code ceiling=2 仅 3/5 模型达到，需从 'ceiling=2' 软化为 'ceiling=2 for models with sufficient code training'", 'arXiv Qwen-7B cross-scorer K*=3→2 的下降被一位审稿人视为 scorer confound 未完全控制的证据', '一位审稿人认为 C3 negative results（Pythia, arXiv）削弱 practical relevance', 'θ-sensitivity 被要求做更详细分析（θ=0.55-0.70 全谱呈现）']
关键指标范围：{'code_models_at_ceiling2_of_5': [3, 3], 'code_mistral7b_1v2_auc': [0.56, 0.62], 'code_qwen7b_1v2_auc': [0.6, 0.66], 'domain_ceiling_clean_fit_pct': [85, 92], 'cross_scorer_kstar_preservation_rate': [0.75, 0.85], 'c3_binary_vs_nofilter_hellaswag_delta_pp': [3.8, 6.1], 'estimated_reviewer_excitement': [3.3, 3.7], 'emnlp_main_accept_prob': [0.25, 0.5]}
叙事方向：C1' 核心成立但 claims 需降级。Domain ceiling 从 "predictive framework" 调整为 "empirical tendency with domain×competence interaction"：中间复杂度域（C4, Code） 的 K* 受 model domain-specific competence 调制，极端域（Wiki, arXiv）稳健。Code 域叙事从 "ceiling=2 cross-family confirmed" 改为 "ceiling=2 observed in models with adequate code pretraining (Qwen, LLaMA); insufficient code competence yields K*=1 (Pythia, Mistral), consistent with C4 Mistral pattern"。C3 的 scope 在 Limitations 中更显著呈现，承认 filtering advantage 限于 homogeneous web text + 单一 base model (Qwen-1.5B)，不泛化到 arXiv 或其他 base models。补充实验：可能需要 arXiv cross-scorer bootstrap CI 的完整呈现、 θ-sensitivity full sweep figure。目标 EMNLP Findings 或 borderline Main。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-contamination
focus: Code domain cross-model results now include LLaMA-8B K*=2 (cross-family confirmed) + cross-scorer validation K*=2 (D079). Mistral-7B and Qwen-7B Code still RUNNING. Domain hierarchy: Wiki=1, C4=Code=2, arXiv=3. Retrain K*=7 (two families). Focus on: (1) whether 4-domain + 6-architecture-family coverage is sufficient for EMNLP accept; (2) C3 filtering weakness (negative results on arXiv/Pythia); (3) Excitement score — is domain ceiling framework + one-wash laundering concept enough to push from 3.5 to 4.0?

## paper_framing.md

# Paper Framing — gen-depth-contamination

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)
- Fallback: EMNLP 2026 Findings
- Backup: AAAI 2027 (abstract July 25, paper August 1)

## Canonical Experimental Condition

**Continuation mode 是 cross-model 结论的基础。**

> "We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons."

| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |
|-----------|-------------|-------------|---------|
| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |
| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |

**原则**：
- C1' 的跨模型 claim 必须基于 continuation mode 数据
- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据
- mvp-001 (Qwen-rewrite) 定位为 "pilot study demonstrating feasibility"，后续用 continuation mode rigorously validate
- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集

## Core Claims (2+1 结构, updated D049/D050)

### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)
首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。

DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：

- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现 domain ceiling 阶梯：Wikipedia ceiling=1, C4/Code ceiling=2, arXiv ceiling=3。Domain structure 设定 K* 上界（ceiling），model 的 domain-specific generation competence 决定是否达到 ceiling（D076）
- **Web text K*=2 是 dominant mode**（C4 8/9 configurations），Code domain ceiling=2（Qwen-1.5B K*=2, AUC 1v2=0.7382; Pythia-1.4B K*=1, AUC 1v2=0.5983——code generation competence 不足未达 ceiling，与 Mistral C4 K*=1 模式一致）。Code 与 C4 共享 ceiling=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse，C4 在 0v1→1v2），说明 domain structure 不仅决定 K* ceiling 还影响信号衰减模式。**Cross-family validation (D079, D080)**: LLaMA-3.1-8B K*=2 (1v2 AUC=0.7394, CI [0.729, 0.750], JSD cliff 13.5x, scored by Qwen) confirmed Code ceiling=2 不是 Qwen 家族特有。Pythia-1.4B scorer 重评 Qwen Code generations K*=2 confirmed (Δ=-1.9pp)。与 Wiki 域的 scorer confound（same-family scorer inflates K* 1→2）形成对比，说明 scorer confound 是域相关（domain-specific）而非系统性的。当前状态：Qwen-1.5B K*=2, LLaMA-8B K*=2, Pythia-1.4B K*=1; Mistral-7B/Qwen-7B pending
- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）
- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节
- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据
- **Domain 是 K* 的主要决定因素（primary determinant with domain ceiling）**：domain structure 设定 K* ceiling，scorer control 后 model scale/architecture/decoding strategy 不改变域 ceiling。Model domain-specific competence 调制实际 K*，但从不超过 ceiling（可证伪预测）。此 model×domain interaction 在中间复杂度域（C4, Code）最显著，在极端域（Wiki K*=1 全票、arXiv K*=3 全票）消失
- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分

**子组件：**

**(a) K*=2 as dominant mode for web text (8/9 configurations)**
> **8/9 model configurations yield K*=2 on C4 web text：**
>
> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |
> |-------|-----------|---------|--------|-----------------|
> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |
> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |
> | Qwen2.5-14B cont | exp_14b_c4 | 0.6210 | [0.6119, 0.6304] | ✅ (+1.19pp) |
> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |
> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |
> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |
> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |
>
> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*
>
> *Decoding strategy invariance (exp-003):*
> | Decoding | AUC 1v2 | K* |
> |----------|---------|-----|
> | greedy | 0.6893 | 2 |
> | nucleus p=0.9 | 0.6866 | 2 |
> | temp=0.7 | 0.6887 | 2 |
> | temp=1.2 | 0.7039 | 2 |
>
> - 8/9 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60
> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变
> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1
> - ⚠️ θ-sensitivity: θ=0.60 下 8/9 K*=2; θ=0.70 下多数降至 K*=1
> - Paper 措辞："K*=2 emerges as the dominant mode for general web text (8/9 model configurations), demonstrating consistency across diverse architectures and decoding strategies."

**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**
> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)
> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)
> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)
> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)
> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)
> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）
> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 "domain competence prerequisite" 分析放 Appendix
> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity
> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代
> - Sample size: n=2,200 per model
> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 "K*=3 with boundary pair AUC of 0.62" 而非 "robustly K*=3"
> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链

**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**
> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1
> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）
> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**
> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash
> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素

**(d) Cross-model transfer (scorer invariance)**
> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact
> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移
> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model
> - Feature ordering: scorer-invariant Spearman ρ > 0.90
> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus

**(e) Representation dependence of K* (Neural Probe)**
> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:
>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅
>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌
>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌
> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2
> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*
> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显
> - 论文定位：validates choice of model-free 15D features for headline characterization

**(f) Generation mode analysis (§4.x Analysis subsection)**
> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）
> - Transferability: continuation 80-92% retention vs rewrite 61-63%
> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集
> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性
> - 论文定位：Analysis subsection，不是独立 claim

### Secondary: C3 (K*-Aware Data Curation Validation)
Domain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.

> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim "universally beneficial"。维持 "consistent advantage" 措辞，以 HellaSwag 显著性为主要证据。

### Supporting Analysis: Canonical Condition Selection
Generation mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。

## Story Spine

- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**
- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过 9 model configurations（5 architecture families, 1B-14B）、4 source domains（C4, Wikipedia, arXiv, Code/Python）、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（8/9 configurations）= Code/Python K*=2（Qwen-1.5B confirmed, AUC 1v2=0.7382），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Code 域与 C4 共享 K*=2 但 JSD cliff 位置不同（Code 在 1v2→2v3 collapse 11.7x，C4 在 0v1→1v2 9.8x），说明 domain structure 不仅决定 K* 值还影响信号衰减模式。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（"one-wash laundering" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。
- **Headline result template**: "Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a domain hierarchy across 4 source domains: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text and code at K*=2 (C4 8/9 configurations; Code/Python confirmed with distinct JSD cliff dynamics), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*, while JSD cliff position reveals domain-specific signal decay patterns even at identical K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity."

## Anticipated Reviewer Concerns & Responses

1. **"K*∈{1,2,3} 范围太小，结论是否 trivial？"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。
2. **"只基于小模型（≤8B），能推广到更大模型吗？"** → 5 architecture families (1B-14B) 覆盖了当前开源生态的主要架构，且跨 4 个 source domains（C4, Wikipedia, arXiv, Code/Python）验证了 domain dependence 的一致性。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。
3. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。
4. **"arXiv K*=3 样本量够吗？"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。
5. **"Mistral K*=1 / Pythia Code K*=1 是 outlier 还是 systematic？"** → 两者都是 domain ceiling 框架下的 systematic 现象（D076）。Cross-scorer validation 确认 Mistral C4 K*=1 是 text-intrinsic。Pythia Code K*=1 反映 code generation competence 不足（The Pile 训练，code 占比低）。Domain ceiling 框架统一解释所有 "异常"：domain structure 设定 ceiling，model domain-specific competence 决定是否达到 ceiling。此 model×domain interaction 在中间复杂度域最显著，在极端域消失（Wiki 全票 K*=1，arXiv 全票 K*=3）。
6. **"Prompt-chain 不代表真实世界递归污染"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**两家族实证验证**：retrain-chain K*=7 跨模型一致——Qwen-1.5B（6v7 AUC=0.6410, CI [0.6376, 0.6445]）和 Pythia-1.4B（6v7 AUC=0.6340, CI [0.6275, 0.6406]）均达 K*=7（D077/D078），尽管 LoRA effective capacity 差异约 3x（fused vs independent QKV），K* ceiling 完全一致。Retrain-chain 将可检测深度扩展到 7 代（prompt-chain 仅 2 代），差距源于 LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss）。
7. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。
8. **"为什么不用 learned representations"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。
9. **"θ=0.60 选择是否 arbitrary？"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。
10. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。
11. **"If K* determines filtering granularity, why doesn't graduated outperform binary on arXiv (K*=3)?"** → exp-026 (arXiv, Qwen-7B) 和 exp-025 (arXiv, Pythia-1.4B) 均为 negative：三种 filtering 策略（binary, graduated, no_filter）结果几乎相同，graduated 未优于 binary。C3 的 validated scope 限于 C4 web text（binary filtering, 30% contamination ratio），Limitations 中已承认。可能原因：(1) LoRA rank=4 capacity 不足以在短训练中捕获 arXiv 细粒度 depth signal；(2) arXiv 在 pretraining mix 中占比极低，downstream metric（MMLU/HellaSwag）对 arXiv 域 contamination 不敏感；(3) graduated weighting 的 α 选择空间未充分探索（仅测试 α=0.9）。这说明 filtering advantage 受限于 downstream eval sensitivity 和训练规模，K* 的表征价值（C1'）与 curation 的实际收益（C3）之间存在 gap，需要更大规模实验验证。

## Venue Fit

- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度
- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} across 4 domains 的 bounded range + domain dependence 是 nuanced scientific finding，比 "K*=2 everywhere" 更可信且更 interesting（审稿人不必怀疑过度外推）。Code domain 的加入进一步拓展 modality 覆盖（natural language + code），增强泛化性论证
- One-wash laundering effect 是 memorable concept 便于传播
- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,
    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_001_pythia_depth
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9932
      1v2: 0.6539
      2v3: 0.5515
      3v4: 0.5153
      4v5: 0.5135
    pairwise_auc_std:
      0v1: 0.0007
      1v2: 0.0069
      2v3: 0.0137
      3v4: 0.0084
      4v5: 0.0078
    pairwise_jsd:
      0v1: 0.2142
      1v2: 0.014
      2v3: 0.0051
      3v4: 0.0033
      4v5: 0.0031
    k_star: 2
    ordinal_mae: 1.14
    ordinal_accuracy: 0.383
- id: exp-002
  claim: 1
  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,
    C4 5K docs, depth 0-5.'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_002_olmo_depth
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.997
      1v2: 0.6146
      2v3: 0.5497
      3v4: 0.509
      4v5: 0.5044
    pairwise_auc_std:
      0v1: 0.0004
      1v2: 0.0029
      2v3: 0.004
      3v4: 0.0084
      4v5: 0.0136
    pairwise_jsd:
      0v1: 0.23941
      1v2: 0.012972
      2v3: 0.00735
      3v4: 0.003968
      4v5: 0.003851
    ordinal_mae: 1.1813
    ordinal_accuracy: 0.3685
    top_features:
    - surp_d1_mean
    - surp_d1_skew
    - freq_kurtosis
    - surp_d2_mean
    - surp_mean
- id: exp-003
  claim:
  - 1
  - 3
  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9
    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'
  priority: P0
  gpu_budget_hours: 20
  deps: []
  registry_id: exp_003_decoding_ablation
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    K_star_robust: true
    bootstrap_ci:
      config1_greedy:
        0v1:
          auc: 0.9796
          ci:
          - 0.9772
          - 0.982
          perm_p: 0
        1v2:
          auc: 0.6892
          ci:
          - 0.6802
          - 0.6982
          perm_p: 0
        2v3:
          auc: 0.5612
          ci:
          - 0.5517
          - 0.5705
          perm_p: 0
        3v4:
          auc: 0.5405
          ci:
          - 0.5308
          - 0.5502
          perm_p: 0
        4v5:
          auc: 0.5137
          ci:
          - 0.5033
          - 0.5238
          perm_p: 0.0082
      config2_nuc09:
        0v1:
          auc: 0.9945
          ci:
          - 0.9934
          - 0.9956
          perm_p: 0
        1v2:
          auc: 0.6862
          ci:
          - 0.6774
          - 0.6951
          perm_p: 0
        2v3:
          auc: 0.5917
          ci:
          - 0.5824
          - 0.601
          perm_p: 0
          note: CI upper crosses theta=0.60
        3v4:
          auc: 0.5468
          ci:
          - 0.5369
          - 0.5568
          perm_p: 0
        4v5:
          auc: 0.5066
          ci:
          - 0.4959
          - 0.5173
          perm_p: 0.1199
      config3_t07:
        0v1:
          auc: 0.9877
          ci:
          - 0.9857
          - 0.9896
          perm_p: 0
        1v2:
          auc: 0.6885
          ci:
          - 0.6797
          - 0.697
          perm_p: 0
        2v3:
          auc: 0.5901
          ci:
          - 0.5806
          - 0.5996
          perm_p: 0
        3v4:
          auc: 0.539
          ci:
          - 0.5288
          - 0.5493
          perm_p: 0
        4v5:
          auc: 0.5348
          ci:
          - 0.5243
          - 0.5454
          perm_p: 0
      config4_t12:
        0v1:
          auc: 0.9982
          ci:
          - 0.9975
          - 0.9987
          perm_p: 0
        1v2:
          auc: 0.7037
          ci:
          - 0.6945
          - 0.7126
          perm_p: 0
        2v3:
          auc: 0.582
          ci:
          - 0.5722
          - 0.5917
          perm_p: 0
        3v4:
          auc: 0.5293
          ci:
          - 0.5185
          - 0.5399
          perm_p: 0
        4v5:
          auc: 0.5237
          ci:
          - 0.5132
          - 0.5347
          perm_p: 0.0001
      resamples: 10000
      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation
- id: exp-004
  claim: 1
  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 5K docs, depth
    0-5, scorer=Qwen2.5-1.5B. 测试 K* 是否随模型规模变化。（实际参数已从原计划 1K/depth 0-3 扩展以匹配其他实验配置）'
  priority: P0
  gpu_budget_hours: 18
  deps: []
  registry_id: exp_004_7b_crossscale
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9644
      1v2: 0.6178
      2v3: 0.546
      3v4: 0.5225
      4v5: 0.5091
    pairwise_auc_std:
      0v1: 0.0034
      1v2: 0.0081
      2v3: 0.0028
      3v4: 0.0113
      4v5: 0.0052
    bootstrap_ci:
      0v1:
        auc: 0.9638
        ci_lower: 0.9607
        ci_upper: 0.9665
        perm_p: 0.0001
      1v2:
        auc: 0.6168
        ci_lower: 0.6079
        ci_upper: 0.6261
        perm_p: 0.0001
      2v3:
        auc: 0.5492
        ci_lower: 0.5388
        ci_upper: 0.5594
        perm_p: 0.0001
      3v4:
        auc: 0.5276
        ci_lower: 0.517
        ci_upper: 0.5375
        perm_p: 0.0001
      4v5:
        auc: 0.5085
        ci_lower: 0.4988
        ci_upper: 0.5191
        perm_p: 0.0676
    bootstrap_resamples: 1000
    permutation_resamples: 10000
    pairwise_jsd:
      0v1: 0.127422
      1v2: 0.010114
      2v3: 0.004798
      3v4: 0.004821
      4v5: 0.003335
    ordinal_mae: 1.2156
    ordinal_accuracy: 0.3523
    top_features:
    - freq_entropy
    - surp_d1_skew
    - surp_std
    - surp_d1_mean
    - surp_mean
    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60
      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).
      FR-4 Warning resolved.
- id: exp-005
  claim: 2
  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth
    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制
    degradation ordering heatmap。'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  registry_id: exp_005_degradation
  status: DONE
  conclusion: success
  metrics:
    cross_model_kendall_tau_by_first_auc:
      Pythia_vs_OLMo: 0.733
      Pythia_vs_Qwen_rewrite: 0.467
      Pythia_vs_Qwen_cont: 0.695
      OLMo_vs_Qwen_rewrite: 0.429
      OLMo_vs_Qwen_cont: 0.543
      Qwen_rewrite_vs_Qwen_cont: 0.733
    cross_model_kendall_tau_by_avg_auc:
      Pythia_vs_OLMo: 0.8476
      Pythia_vs_Qwen_cont: 0.7524
      OLMo_vs_Qwen_cont: 0.6762
    cross_model_spearman_rho_single_feature_auc:
      Pythia_vs_OLMo: 0.95
      Pythia_vs_Qwen_cont: 0.9143
      OLMo_vs_Qwen_cont: 0.85
      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently
        classifies depth pairs)
    4model_tau_mean_continuation_by_first_auc: 0.657
    4model_tau_mean_all_by_first_auc: 0.6
    generation_mode_delta:
      Pythia_vs_Qwen: '+0.228'
      OLMo_vs_Qwen: '+0.114'
    top3_features_ranking_by_first_auc:
      Pythia:
      - surp_d1_std
      - surp_d2_std
      - surp_std
      OLMo:
      - surp_std
      - surp_d1_std
      - surp_d2_std
      Qwen_rewrite:
      - freq_entropy
      - surp_std
      - surp_d1_std
      Qwen_cont:
      - surp_d1_std
      - surp_std
      - surp_d2_std
    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all
      architectures (single-feature AUC ranking)
    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature
      AUC ranking under controlled generation mode.
    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower
      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture
    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),
      near-generational feature importance ordering varies more across models
- id: exp-006
  claim: 3
  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter
    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)
    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness
    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α
    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated
    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'
  priority: P0
  gpu_budget_hours: 72
  deps: []
  registry_id: exp_006_graduated_filtering
  status: DONE
  conclusion: success
  metrics:
    total_runs: 51
    binary_ours:
      mmlu: 0.5941±0.0008
      hellaswag: 0.6701±0.0006
    binary_drayson:
      mmlu: 0.5913±0.0009
      hellaswag: 0.6691±0.0004
    surprisal:
      mmlu: 0.5894±0.0009
      hellaswag: 0.6641±0.0006
    graduated_a09:
      mmlu: 0.5892±0.0008
      hellaswag: 0.6701±0.0007
    graduated_a07:
      mmlu: 0.5892±0.0014
      hellaswag: 0.6695±0.0004
    graduated_a05:
      mmlu: 0.5880±0.0013
      hellaswag: 0.6687±0.0008
    graduated_a03:
      mmlu: 0.5877±0.0013
      hellaswag: 0.6669±0.0005
    graduated_a01:
      mmlu: 0.5873±0.0019
      hellaswag: 0.6640±0.0009
    dsir:
      mmlu: 0.5869±0.0003
      hellaswag: 0.6631±0.0007
    no_filter:
      mmlu: 0.5865±0.0010
      hellaswag: 0.6638±0.0008
    base_model:
      mmlu: '0.6018'
      hellaswag: '0.6821'
    best_strategy: binary-ours
    key_finding: binary-ours is best filtering strategy. All strategies degrade vs
      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR
      below all other strategies except no-filter.
- id: exp-007
  claim:
  - 1
  - 2
  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算
    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为
    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation
    test + 3-class metrics]'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  - exp-003
  registry_id: exp_007_bootstrap_ci
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      0v1:
        auc: 0.9956
        ci_lower: 0.9946
        ci_upper: 0.9965
        perm_p: 0.002
      1v2:
        auc: 0.6955
        ci_lower: 0.6859
        ci_upper: 0.7041
        perm_p: 0.002
      2v3:
        auc: 0.5893
        ci_lower: 0.5795
        ci_upper: 0.5991
        perm_p: 0.002
      3v4:
        auc: 0.5435
        ci_lower: 0.5333
        ci_upper: 0.5551
        perm_p: 0.002
      4v5:
        auc: 0.534
        ci_lower: 0.5238
        ci_upper: 0.5448
        perm_p: 0.002
    pythia_cont:
      0v1:
        auc: 0.9932
        ci_lower: 0.9921
        ci_upper: 0.9943
        perm_p: 0.002
      1v2:
        auc: 0.6539
        ci_lower: 0.6454
        ci_upper: 0.663
        perm_p: 0.002
      2v3:
        auc: 0.5514
        ci_lower: 0.5417
        ci_upper: 0.5628
        perm_p: 0.002
      3v4:
        auc: 0.5152
        ci_lower: 0.5041
        ci_upper: 0.526
        perm_p: 0.006
      4v5:
        auc: 0.5136
        ci_lower: 0.5021
        ci_upper: 0.5249
        perm_p: 0.008
    olmo_cont:
      0v1:
        auc: 0.997
        ci_lower: 0.9964
        ci_upper: 0.9975
        perm_p: 0.002
      1v2:
        auc: 0.6145
        ci_lower: 0.6045
        ci_upper: 0.6247
        perm_p: 0.002
      2v3:
        auc: 0.5496
        ci_lower: 0.5399
        ci_upper: 0.5596
        perm_p: 0.002
      3v4:
        auc: 0.5091
        ci_lower: 0.4973
        ci_upper: 0.52
        perm_p: 0.064
      4v5:
        auc: 0.5045
        ci_lower: 0.4932
        ci_upper: 0.515
        perm_p: 0.232
    qwen_cont:
      0v1:
        auc: 0.9971
        ci_lower: 0.9963
        ci_upper: 0.9978
        perm_p: 0.002
      1v2:
        auc: 0.6112
        ci_lower: 0.6015
        ci_upper: 0.6213
        perm_p: 0.002
      2v3:
        auc: 0.5609
        ci_lower: 0.5511
        ci_upper: 0.5712
        perm_p: 0.002
      3v4:
        auc: 0.5409
        ci_lower: 0.5308
        ci_upper: 0.5508
        perm_p: 0.002
      4v5:
        auc: 0.5141
        ci_lower: 0.5035
        ci_upper: 0.5255
        perm_p: 0.006
    k_star_robust: true
    all_1v2_ci_lower_above_060: true
    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold
- id: exp-008
  claim: 1
  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),
    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'
  priority: P1
  gpu_budget_hours: 8
  deps:
  - exp-001
  registry_id: exp_008_retrain_chain_v2
  status: DONE
  conclusion: success
  metrics:
    k_star: '>=4'
    pairwise_auc:
      0v1: 0.9847
      1v2: 0.9484
      2v3: 0.8888
      3v4: 0.7982
    pairwise_jsd:
      0v1: 0.17
      1v2: 0.12
      2v3: 0.064
      3v4: 0.04
    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts
      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic
      boundary.
- id: exp-009
  claim: 3
  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试
    graduated vs binary filtering 的收益差异。'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - exp-006
  registry_id: exp_009_dose_50pct
  status: DONE
  conclusion: failed
- id: exp-010
  claim:
  - 1
  - 2
  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs
    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-005
  registry_id: exp_010_ordinal_baseline
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      obd_lgbm:
        accuracy: 0.4229
        mae: 0.9836
        tau_b: 0.5518
        mean_pw_auc: 0.6214
      multiclass_lgbm:
        accuracy: 0.4182
        mae: 1.0163
        tau_b: 0.5367
        mean_pw_auc: 0.6246
      ordinal_logreg:
        accuracy: 0.3636
        mae: 0.9105
        tau_b: 0.563
        mean_pw_auc: 0.5022
    pythia:
      obd_lgbm:
        accuracy: 0.3856
        mae: 1.1072
        tau_b: 0.4745
        mean_pw_auc: 0.6055
      multiclass_lgbm:
        accuracy: 0.3832
        mae: 1.1399
        tau_b: 0.4622
        mean_pw_auc: 0.6062
      ordinal_logreg:
        accuracy: 0.3179
        mae: 1.022
        tau_b: 0.49
        mean_pw_auc: 0.4767
    olmo:
      obd_lgbm:
        accuracy: 0.3822
        mae: 1.1469
        tau_b: 0.4683
        mean_pw_auc: 0.6015
      multiclass_lgbm:
        accuracy: 0.3685
        mae: 1.1813
        tau_b: 0.4497
        mean_pw_auc: 0.5974
      ordinal_logreg:
        accuracy: 0.3265
        mae: 1.0352
        tau_b: 0.4656
        mean_pw_auc: 0.4859
- id: exp-011
  claim: 1
  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth
    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'
  priority: P1
  gpu_budget_hours: 0
  deps: []
  registry_id: exp_011_llm_zeroshot
  status: DONE
  conclusion: success
  metrics:
    gpt55_5class_acc: 0.332
    gpt55_mae: 1.102
    gpt55_spearman: 0.383
    gpt55_binary_acc: 0.878
    claude_5class_acc: 0.331
    claude_mae: 1.15
    claude_spearman: 0.416
    claude_binary_acc: 0.882
    odb_baseline_5class_acc: 0.386
    odb_baseline_mae: 1.107
    gpt55_per_depth_acc:
      depth_0: 0.77
      depth_1: 0.19
      depth_2: 0.38
      depth_3: 0.24
      depth_4: 0.08
    claude_per_depth_acc:
      depth_0: 0.69
      depth_1: 0.21
      depth_2: 0.28
      depth_3: 0.101
      depth_4: 0.37
    n_samples_per_model: 500
    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than
      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI
      detection is high (~88%) but fine-grained depth discrimination fails.
- id: exp-012
  claim: 1
  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score
    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - exp-001
  - exp-002
  registry_id: exp_012_binary_confidence
  status: DONE
  conclusion: success
  metrics:
    n_samples: 500
    generators:
    - qwen-rewrite
    - pythia-1.4b
    - olmo-1b
    - qwen-cont
    6class_accuracy:
      qwen-rewrite: 0.1987
      pythia-1.4b: 0.1303
      olmo-1b: 0.127
      qwen-cont: 0.1833
      random_baseline: 0.1667
    spearman_rho:
      qwen-rewrite:
        log_ppl_ref: -0.1233
        log_ppl_obs: 0.0815
        ppl_ratio: 0.1185
      pythia-1.4b:
        log_ppl_ref: -0.2972
        log_ppl_obs: -0.4529
        ppl_ratio: -0.392
      olmo-1b:
        log_ppl_ref: -0.378
        log_ppl_obs: -0.4614
        ppl_ratio: -0.4068
      qwen-cont:
        log_ppl_ref: -0.3887
        log_ppl_obs: -0.162
        ppl_ratio: -0.058
    binary_detector_kstar: 1
    obd_kstar: 2
    auc_non_monotonic: true
    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy
      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but
      practically weak). AUC non-monotonic — binary detectors cannot maintain depth
      ordering. Confirms binary confidence ≠ depth estimation.
- id: exp-013
  claim:
  - 1
  - 2
  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001
    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier
    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是
    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  - exp-002
  - exp-017
  registry_id: exp_013_cross_transfer
  status: DONE
  conclusion: success
  metrics:
    accuracy_matrix:
      Qwen_rw→Qwen_rw: 0.4229
      Qwen_rw→Pythia: 0.259
      Qwen_rw→OLMo: 0.2653
      Qwen_rw→Qwen_cont: 0.3466
      Pythia→Qwen_rw: 0.2718
      Pythia→Pythia: 0.3856
      Pythia→OLMo: 0.3531
      Pythia→Qwen_cont: 0.3287
      OLMo→Qwen_rw: 0.2768
      OLMo→Pythia: 0.345
      OLMo→OLMo: 0.3822
      OLMo→Qwen_cont: 0.3244
      Qwen_cont→Qwen_rw: 0.344
      Qwen_cont→Pythia: 0.3284
      Qwen_cont→OLMo: 0.3112
      Qwen_cont→Qwen_cont: 0.3875
    transfer_retention_accuracy:
      Pythia↔OLMo: 91-92%
      Qwen_rw→Pythia/OLMo: 61-63%
      Qwen_cont↔Pythia: 83-85%
      Qwen_cont↔OLMo: 80-85%
    transfer_retention_tau:
      Pythia↔OLMo: 85-86%
      Qwen_rw→Pythia/OLMo: 45-50%
      Qwen_cont↔others: 68-83%
    mean_pw_auc_matrix:
      within_avg: 0.6099
      cross_avg: 0.5905
      0v1_cross_all_above: 0.96
    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.
      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained
      depth transfer depends on model family similarity. Qwen-rewrite overfits style
      features; Qwen-cont transfers much better.
- id: exp-014
  claim: 1
  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth
    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'
  priority: P2
  gpu_budget_hours: 8
  deps:
  - exp-005
  registry_id: null
  status: planned
- id: exp-015
  claim: 1
  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +
    MLP vs hand-crafted 15D features。如果 neural probe 也给 K*=2 → C1'' claim 从 "our features
    find K*=2" 升级为 "K*=2 is data-intrinsic boundary"。[D014 升级 P0：Reviewer 评估为最高边际价值实验]'
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: exp_015_neural_probe
  status: DONE
  conclusion: success
  metrics:
    pythia:
      k_star_neural: 2
      k_star_lgbm: 2
      accuracy: 0.3892
      pairwise_auc:
        0v1: 0.966
        1v2: 0.676
        2v3: 0.596
        3v4: 0.555
        4v5: 0.532
    olmo:
      k_star_neural: 2
      k_star_lgbm: 2
      accuracy: 0.3729
      pairwise_auc:
        0v1: 0.95
        1v2: 0.657
        2v3: 0.589
        3v4: 0.547
        4v5: 0.53
    qwen_cont:
      k_star_neural: 3
      k_star_lgbm: 2
      accuracy: 0.4368
      pairwise_auc:
        0v1: 0.988
        1v2: 0.702
        2v3: 0.616
        3v4: 0.59
        4v5: 0.566
    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3
      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM
      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.
- id: exp-016
  claim: 1
  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的
    K* 和特征分布差异。'
  priority: P1
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_016_base_vs_instruct
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.987
      1v2: 0.6262
      2v3: 0.5496
      3v4: 0.5294
      4v5: 0.5182
    pairwise_auc_std:
      0v1: 0.0015
      1v2: 0.0152
      2v3: 0.0067
      3v4: 0.0132
      4v5: 0.0139
    pairwise_jsd:
      0v1: 0.163726
      1v2: 0.01081
      2v3: 0.005311
      3v4: 0.003942
      4v5: 0.003522
    ordinal_mae: 1.1691
    ordinal_accuracy: 0.3719
    top_features:
    - freq_entropy
    - surp_std
    - surp_d1_skew
    - surp_d1_mean
    - surp_mean
    n_samples: 30000
    bootstrap_ci:
      0v1:
        auc: 0.987
        ci_lower: 0.9853
        ci_upper: 0.9885
        perm_p: 0.0001
      1v2:
        auc: 0.626
        ci_lower: 0.6168
        ci_upper: 0.6353
        perm_p: 0.0001
      2v3:
        auc: 0.5496
        ci_lower: 0.5397
        ci_upper: 0.56
        perm_p: 0.0001
      3v4:
        auc: 0.5293
        ci_lower: 0.5188
        ci_upper: 0.5399
        perm_p: 0.0001
      4v5:
        auc: 0.5181
        ci_lower: 0.5075
        ci_upper: 0.5288
        perm_p: 0.0016
    bootstrap_resamples: 10000
    permutation_resamples: 10000
    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%
      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant
      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above
      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,
      0.6213] — no significant base-vs-instruct difference.
- id: exp-017
  claim:
  - 1
  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,
    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model
    对 K* 的影响。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_017_qwen_continuation
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9972
      1v2: 0.6114
      2v3: 0.5609
      3v4: 0.5408
      4v5: 0.5139
    pairwise_jsd:
      0v1: 0.28627
      1v2: 0.005107
      2v3: 0.003603
      3v4: 0.003395
      4v5: 0.003085
    ordinal_mae: 1.1547
    ordinal_accuracy: 0.3819
    top3_features:
    - freq_entropy
    - surp_mean
    - surp_std
- id: mvp-001
  claim:
  - 1
  - 2
  - 3
  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,
    nucleus p=0.95 T=1.0, depth 0-5.'
  priority: P0
  gpu_budget_hours: 12
  deps: []
  registry_id: mvp_pilot_sat_v1
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9956
      1v2: 0.6957
      2v3: 0.5893
      3v4: 0.5434
      4v5: 0.5343
    pairwise_auc_std:
      0v1: 0.0005
      1v2: 0.0072
      2v3: 0.012
      3v4: 0.0053
      4v5: 0.0091
    pairwise_jsd:
      0v1: 0.2669
      1v2: 0.0163
      2v3: 0.0069
      3v4: 0.0047
      4v5: 0.0041
    k_star: 2
    ordinal_mae: 1.0163
    ordinal_accuracy: 0.4182
- id: exp-018
  claim: 1
  description: 'Cross-family universality: LLaMA-3.1-8B, continuation mode, nucleus
    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 跨模型家族验证 K*。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_018_llama8b_depth
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9225
      1v2: 0.6123
      2v3: 0.5274
      3v4: 0.5138
      4v5: 0.5097
    jsd:
      0v1: 0.077
      1v2: 0.012
      2v3: 0.005
    bootstrap_ci:
      0v1:
        auc: 0.9224
        ci_lower: 0.9174
        ci_upper: 0.9272
        perm_p: 0.0001
      1v2:
        auc: 0.6123
        ci_lower: 0.6028
        ci_upper: 0.6216
        perm_p: 0.0001
      2v3:
        auc: 0.5273
        ci_lower: 0.5169
        ci_upper: 0.5378
        perm_p: 0.0001
      3v4:
        auc: 0.5168
        ci_lower: 0.5062
        ci_upper: 0.5275
        perm_p: 0.0037
      4v5:
        auc: 0.5159
        ci_lower: 0.5052
        ci_upper: 0.5268
        perm_p: 0.0035
    bootstrap_resamples: 10000
    permutation_resamples: 10000
- id: exp-019
  claim: 1
  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus
    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_019_mistral7b_depth
  status: DONE
  conclusion: success
  metrics:
    k_star: 1
    pairwise_auc:
      0v1: 0.9843
      1v2: 0.5935
      2v3: 0.5402
      3v4: 0.5232
      4v5: 0.5181
    bootstrap_ci_1v2:
      ci_lower: 0.5835
      ci_upper: 0.6032
      p_auc_leq_060: 0.9017
    jsd:
      0v1: 0.124194
      1v2: 0.008051
      2v3: 0.005047
      3v4: 0.004516
      4v5: 0.004109
    ordinal_mae: 1.2275
    ordinal_accuracy: 0.3567
    top3_features:
    - freq_entropy
    - surp_d1_skew
    - surp_d1_mean
- id: exp-020
  claim:
  - 1
  - 3
  description: 'Pythia-1.4B decoding ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2,
    C4 5K docs, depth 0-5. 跨模型验证解码策略对 K* 的不变性。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  registry_id: exp_020_pythia_decoding
  status: DONE
  conclusion: success
  metrics:
    greedy:
      K_star: 2
      auc:
        0v1: 0.9992
        1v2: 0.8838
        2v3: 0.5342
        3v4: 0.5228
        4v5: 0.5162
    nuc09:
      K_star: 2
      auc:
        0v1: 0.9948
        1v2: 0.677
        2v3: 0.5549
        3v4: 0.5299
        4v5: 0.5013
    t07:
      K_star: 2
      auc:
        0v1: 0.9965
        1v2: 0.7265
        2v3: 0.5941
        3v4: 0.5698
        4v5: 0.5284
    t12:
      K_star: 2
      auc:
        0v1: 0.9933
        1v2: 0.6172
        2v3: 0.5226
        3v4: 0.517
        4v5: 0.5051
- id: exp-021
  claim: 1
  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512
    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_021_length_ablation
  status: DONE
  conclusion: success
  metrics:
    128tok:
      K_star: 2
      1v2_auc: 0.6219
    256tok:
      K_star: 2
      1v2_auc: 0.6282
    512tok:
      K_star: 2
      1v2_auc: 0.6073
    all_K_star_2: true
    bootstrap_ci:
      512tok_1v2:
        auc: 0.6073
        ci_lower: 0.5979
        ci_upper: 0.6166
        perm_p: 0.0001
        verdict: BORDERLINE
- id: exp-022
  claim:
  - 1
  - 2
  description: '4x4 cross-scorer matrix: 4 generators × 4 scorers, 验证 scorer independence
    完整性。'
  priority: P0
  gpu_budget_hours: 3
  deps:
  - exp-021
  registry_id: exp_022_cross_scorer_matrix
  status: DONE
  conclusion: success
  metrics:
    total_combos: 12
    completed: 12
    K_star_distribution:
      K2: 11
      K1: 1
    matrix:
      pythia_greedy×olmo:
        K_star: 2
        1v2: 0.8811
      pythia_greedy×pythia:
        K_star: 2
        1v2: 0.8838
      pythia_greedy×qwen_base:
        K_star: 2
        1v2: 0.8814
      pythia_greedy×qwen_instruct:
        K_star: 2
        1v2: 0.8818
      qwen_base×olmo:
        K_star: 2
        1v2: 0.6047
      qwen_base×pythia:
        K_star: 2
        1v2: 0.617
      qwen_base×qwen_base:
        K_star: 2
        1v2: 0.6262
      qwen_base×qwen_instruct:
        K_star: 2
        1v2: 0.6273
      qwen_cont256×olmo:
        K_star: 2
        1v2: 0.6028
      qwen_cont256×pythia:
        K_star: 1
        1v2: 0.5979
      qwen_cont256×qwen_base:
        K_star: 2
        1v2: 0.6282
      qwen_cont256×qwen_instruct:
        K_star: 2
        1v2: 0.6072
    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:
      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to
      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'
- id: exp-023
  claim:
  - 1
  description: 'Domain ablation: Wikipedia seed data, Qwen2.5-1.5B (base) continuation
    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 验证 K*=2 是否跨数据域一致（C4
    vs Wikipedia）。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_023_domain_ablation
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    1v2_auc: 0.6193
    2v3_auc: 0.5498
    all_folds_above_060: true
    top_feature: freq_entropy
    ordinal_accuracy: 0.377
- id: exp-024
  claim:
  - 1
  description: 'Domain ablation: arXiv abstracts seed data, Qwen2.5-1.5B (base) continuation
    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 第三域验证—— 技术文本与
    web text (C4) / 百科 (Wikipedia) 分布差异大，三域一致则 domain 维度从 Limitation 升级为 evidence。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_024_arxiv_domain
  status: DONE
  conclusion: success
  metrics:
    K_star: 3
    pairwise_auc:
      0v1: 0.9946
      1v2: 0.858
      2v3: 0.6427
      3v4: 0.5437
      4v5: 0.5294
    bootstrap_ci:
      0v1:
        auc: 0.9946
        ci_lower: 0.9929
        ci_upper: 0.9961
        perm_p: 0.0001
      1v2:
        auc: 0.858
        ci_lower: 0.848
        ci_upper: 0.8679
        perm_p: 0.0001
      2v3:
        auc: 0.6427
        ci_lower: 0.6275
        ci_upper: 0.6575
        perm_p: 0.0001
      3v4:
        auc: 0.5437
        ci_lower: 0.5276
        ci_upper: 0.5598
        perm_p: 0.0001
      4v5:
        auc: 0.5294
        ci_lower: 0.5133
        ci_upper: 0.5455
        perm_p: 0.0006
    bootstrap_resamples: 10000
    permutation_resamples: 10000
    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First
      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).
- id: exp-025
  claim: 3
  description: 'Pythia-1.4B filtering replication: LoRA rank=8 continued pretraining
    on C4 depth chain, 3 strategies (binary/graduated/no-filter) × 3 seeds, MMLU+HellaSwag.
    验证 filtering strategy ordering 跨模型一致性。'
  priority: P1
  gpu_budget_hours: 16
  deps:
  - exp-006
  - exp-001
  registry_id: exp_025_pythia_filtering
  status: DONE
  conclusion: negative
  metrics:
    runs_completed: 9/9
    strategies:
    - no_filter
    - binary_ours
    - graduated_a09
    seeds:
    - 42
    - 123
    - 456
    mmlu:
      no_filter: 0.2568±0.0012
      binary_ours: 0.2585±0.0004
      graduated_a09: 0.2561±0.0009
    hellaswag:
      no_filter: 0.5250±0.0008
      binary_ours: 0.5251±0.0001
      graduated_a09: 0.5253±0.0007
    delta_vs_no_filter:
      binary_ours_mmlu: '+0.0017'
      binary_ours_hellaswag: '+0.0000'
      graduated_a09_mmlu: '-0.0007'
      graduated_a09_hellaswag: '+0.0003'
    key_finding: All three filtering strategies produce nearly identical results on
      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering
      binary>graduated>no_filter NOT confirmed.
- id: exp-026
  claim: 3
  description: 'arXiv graduated vs binary filtering: Qwen2.5-1.5B base + LoRA rank=4,
    arXiv depth chain (K*=3), 3 strategies (no_filter/binary/graduated α=0.9^d) ×
    5 seeds, MMLU+HellaSwag. 关键实验：K*=3 域上 graduated 应超越 binary，展示 K*-aware filtering
    增量价值。'
  priority: P0
  gpu_budget_hours: 24
  deps:
  - exp-006
  - exp-024
  registry_id: exp_026_arxiv_filtering
  status: DONE
  conclusion: negative
  metrics:
    runs_completed: 15/15
    strategies:
    - no_filter
    - binary
    - graduated_a09
    seeds:
    - 42
    - 123
    - 456
    - 789
    - 1024
    mmlu:
      no_filter: 0.5899±0.0008
      binary: 0.5876±0.0004
      graduated_a09: 0.5900±0.0011
    hellaswag:
      no_filter: 0.6600±0.0002
      binary: 0.6642±0.0004
      graduated_a09: 0.6599±0.0003
    delta_vs_no_filter:
      binary_mmlu: '-0.0023'
      binary_hellaswag: '+0.0042'
      graduated_mmlu: '+0.0001'
      graduated_hellaswag: '-0.0001'
    key_finding: All three strategies produce nearly identical results. Graduated
      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU
      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.
- id: exp-027
  claim: 1
  description: 'LaTeX markup removal ablation: 去除 arXiv 文本中的 LaTeX 格式标记后重新提取 15D features，验证
    K*=3 是否依赖格式特征而非内容层 depth signal。排除替代假说。'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-024
  registry_id: exp_027_latex_ablation
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    k_star_preserved: true
    pairwise_auc_original:
      0v1: 0.9948
      1v2: 0.8581
      2v3: 0.6436
      3v4: 0.544
      4v5: 0.5299
    pairwise_auc_stripped:
      0v1: 0.9948
      1v2: 0.8297
      2v3: 0.6229
      3v4: 0.5468
      4v5: 0.5476
    auc_delta:
      0v1: 0
      1v2: -0.028
      2v3: -0.021
      3v4: 0.003
      4v5: 0.018
    latex_reduction_by_depth:
      depth_0: 0.6%
      depth_5: 4.4%
    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still
      >θ=0.60). LaTeX format is NOT a confound.
- id: exp-028
  claim: 1
  description: 'Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples,
    确定 K*=2 判定所需最低样本量。回应 m4 reviewer concern。'
  priority: P1
  gpu_budget_hours: 1
  deps:
  - exp-007
  registry_id: exp_028_power_curve
  status: DONE
  conclusion: success
  metrics:
    min_n_100pct: 2000
    n500_auc: 0.5808
    n500_rate: 0.2
    n1000_auc: 0.5911
    n1000_rate: 0.3
    n2000_auc: 0.6101
    n2000_rate: 1
    n3000_auc: 0.6166
    n3000_rate: 1
    n4000_auc: 0.622
    n4000_rate: 1
    n5000_auc: 0.6288
    n5000_rate: 1


## registry (completed experiments)

- exp_id: mvp_pilot_sat_v1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9956
      1v2: 0.6957
      2v3: 0.5893
      3v4: 0.5434
      4v5: 0.5343
    pairwise_auc_std:
      0v1: 0.0005
      1v2: 0.0072
      2v3: 0.012
      3v4: 0.0053
      4v5: 0.0091
    pairwise_jsd:
      0v1: 0.2669
      1v2: 0.0163
      2v3: 0.0069
      3v4: 0.0047
      4v5: 0.0041
    k_star: 2
    ordinal_mae: 1.0163
    ordinal_accuracy: 0.4182
- exp_id: exp_001_pythia_depth
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pairwise_auc:
      0v1: 0.9932
      1v2: 0.6539
      2v3: 0.5515
      3v4: 0.5153
      4v5: 0.5135
    pairwise_auc_std:
      0v1: 0.0007
      1v2: 0.0069
      2v3: 0.0137
      3v4: 0.0084
      4v5: 0.0078
    pairwise_jsd:
      0v1: 0.2142
      1v2: 0.014
      2v3: 0.0051
      3v4: 0.0033
      4v5: 0.0031
    k_star: 2
    ordinal_mae: 1.14
    ordinal_accuracy: 0.383
- exp_id: exp_002_olmo_depth
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.997
      1v2: 0.6146
      2v3: 0.5497
      3v4: 0.509
      4v5: 0.5044
    pairwise_auc_std:
      0v1: 0.0004
      1v2: 0.0029
      2v3: 0.004
      3v4: 0.0084
      4v5: 0.0136
    pairwise_jsd:
      0v1: 0.23941
      1v2: 0.012972
      2v3: 0.00735
      3v4: 0.003968
      4v5: 0.003851
    ordinal_mae: 1.1813
    ordinal_accuracy: 0.3685
    top_features:
    - surp_d1_mean
    - surp_d1_skew
    - freq_kurtosis
    - surp_d2_mean
    - surp_mean
- exp_id: exp_003_decoding_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    K_star_robust: true
    bootstrap_ci:
      config1_greedy:
        0v1:
          auc: 0.9796
          ci:
          - 0.9772
          - 0.982
          perm_p: 0
        1v2:
          auc: 0.6892
          ci:
          - 0.6802
          - 0.6982
          perm_p: 0
        2v3:
          auc: 0.5612
          ci:
          - 0.5517
          - 0.5705
          perm_p: 0
        3v4:
          auc: 0.5405
          ci:
          - 0.5308
          - 0.5502
          perm_p: 0
        4v5:
          auc: 0.5137
          ci:
          - 0.5033
          - 0.5238
          perm_p: 0.0082
      config2_nuc09:
        0v1:
          auc: 0.9945
          ci:
          - 0.9934
          - 0.9956
          perm_p: 0
        1v2:
          auc: 0.6862
          ci:
          - 0.6774
          - 0.6951
          perm_p: 0
        2v3:
          auc: 0.5917
          ci:
          - 0.5824
          - 0.601
          perm_p: 0
          note: CI upper crosses theta=0.60
        3v4:
          auc: 0.5468
          ci:
          - 0.5369
          - 0.5568
          perm_p: 0
        4v5:
          auc: 0.5066
          ci:
          - 0.4959
          - 0.5173
          perm_p: 0.1199
      config3_t07:
        0v1:
          auc: 0.9877
          ci:
          - 0.9857
          - 0.9896
          perm_p: 0
        1v2:
          auc: 0.6885
          ci:
          - 0.6797
          - 0.697
          perm_p: 0
        2v3:
          auc: 0.5901
          ci:
          - 0.5806
          - 0.5996
          perm_p: 0
        3v4:
          auc: 0.539
          ci:
          - 0.5288
          - 0.5493
          perm_p: 0
        4v5:
          auc: 0.5348
          ci:
          - 0.5243
          - 0.5454
          perm_p: 0
      config4_t12:
        0v1:
          auc: 0.9982
          ci:
          - 0.9975
          - 0.9987
          perm_p: 0
        1v2:
          auc: 0.7037
          ci:
          - 0.6945
          - 0.7126
          perm_p: 0
        2v3:
          auc: 0.582
          ci:
          - 0.5722
          - 0.5917
          perm_p: 0
        3v4:
          auc: 0.5293
          ci:
          - 0.5185
          - 0.5399
          perm_p: 0
        4v5:
          auc: 0.5237
          ci:
          - 0.5132
          - 0.5347
          perm_p: 0.0001
      resamples: 10000
      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation
- exp_id: exp_017_qwen_continuation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9972
      1v2: 0.6114
      2v3: 0.5609
      3v4: 0.5408
      4v5: 0.5139
    pairwise_jsd:
      0v1: 0.28627
      1v2: 0.005107
      2v3: 0.003603
      3v4: 0.003395
      4v5: 0.003085
    ordinal_mae: 1.1547
    ordinal_accuracy: 0.3819
    top3_features:
    - freq_entropy
    - surp_mean
    - surp_std
- exp_id: exp_013_cross_transfer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy_matrix:
      Qwen_rw→Qwen_rw: 0.4229
      Qwen_rw→Pythia: 0.259
      Qwen_rw→OLMo: 0.2653
      Qwen_rw→Qwen_cont: 0.3466
      Pythia→Qwen_rw: 0.2718
      Pythia→Pythia: 0.3856
      Pythia→OLMo: 0.3531
      Pythia→Qwen_cont: 0.3287
      OLMo→Qwen_rw: 0.2768
      OLMo→Pythia: 0.345
      OLMo→OLMo: 0.3822
      OLMo→Qwen_cont: 0.3244
      Qwen_cont→Qwen_rw: 0.344
      Qwen_cont→Pythia: 0.3284
      Qwen_cont→OLMo: 0.3112
      Qwen_cont→Qwen_cont: 0.3875
    transfer_retention_accuracy:
      Pythia↔OLMo: 91-92%
      Qwen_rw→Pythia/OLMo: 61-63%
      Qwen_cont↔Pythia: 83-85%
      Qwen_cont↔OLMo: 80-85%
    transfer_retention_tau:
      Pythia↔OLMo: 85-86%
      Qwen_rw→Pythia/OLMo: 45-50%
      Qwen_cont↔others: 68-83%
    mean_pw_auc_matrix:
      within_avg: 0.6099
      cross_avg: 0.5905
      0v1_cross_all_above: 0.96
    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.
      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained
      depth transfer depends on model family similarity. Qwen-rewrite overfits style
      features; Qwen-cont transfers much better.
- exp_id: exp_005_degradation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cross_model_kendall_tau_by_first_auc:
      Pythia_vs_OLMo: 0.733
      Pythia_vs_Qwen_rewrite: 0.467
      Pythia_vs_Qwen_cont: 0.695
      OLMo_vs_Qwen_rewrite: 0.429
      OLMo_vs_Qwen_cont: 0.543
      Qwen_rewrite_vs_Qwen_cont: 0.733
    cross_model_kendall_tau_by_avg_auc:
      Pythia_vs_OLMo: 0.8476
      Pythia_vs_Qwen_cont: 0.7524
      OLMo_vs_Qwen_cont: 0.6762
    cross_model_spearman_rho_single_feature_auc:
      Pythia_vs_OLMo: 0.95
      Pythia_vs_Qwen_cont: 0.9143
      OLMo_vs_Qwen_cont: 0.85
      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently
        classifies depth pairs)
    4model_tau_mean_continuation_by_first_auc: 0.657
    4model_tau_mean_all_by_first_auc: 0.6
    generation_mode_delta:
      Pythia_vs_Qwen: '+0.228'
      OLMo_vs_Qwen: '+0.114'
    top3_features_ranking_by_first_auc:
      Pythia:
      - surp_d1_std
      - surp_d2_std
      - surp_std
      OLMo:
      - surp_std
      - surp_d1_std
      - surp_d2_std
      Qwen_rewrite:
      - freq_entropy
      - surp_std
      - surp_d1_std
      Qwen_cont:
      - surp_d1_std
      - surp_std
      - surp_d2_std
    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all
      architectures (single-feature AUC ranking)
    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature
      AUC ranking under controlled generation mode.
    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower
      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture
    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),
      near-generational feature importance ordering varies more across models
- exp_id: exp_007_bootstrap_ci
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      0v1:
        auc: 0.9956
        ci_lower: 0.9946
        ci_upper: 0.9965
        perm_p: 0.002
      1v2:
        auc: 0.6955
        ci_lower: 0.6859
        ci_upper: 0.7041
        perm_p: 0.002
      2v3:
        auc: 0.5893
        ci_lower: 0.5795
        ci_upper: 0.5991
        perm_p: 0.002
      3v4:
        auc: 0.5435
        ci_lower: 0.5333
        ci_upper: 0.5551
        perm_p: 0.002
      4v5:
        auc: 0.534
        ci_lower: 0.5238
        ci_upper: 0.5448
        perm_p: 0.002
    pythia_cont:
      0v1:
        auc: 0.9932
        ci_lower: 0.9921
        ci_upper: 0.9943
        perm_p: 0.002
      1v2:
        auc: 0.6539
        ci_lower: 0.6454
        ci_upper: 0.663
        perm_p: 0.002
      2v3:
        auc: 0.5514
        ci_lower: 0.5417
        ci_upper: 0.5628
        perm_p: 0.002
      3v4:
        auc: 0.5152
        ci_lower: 0.5041
        ci_upper: 0.526
        perm_p: 0.006
      4v5:
        auc: 0.5136
        ci_lower: 0.5021
        ci_upper: 0.5249
        perm_p: 0.008
    olmo_cont:
      0v1:
        auc: 0.997
        ci_lower: 0.9964
        ci_upper: 0.9975
        perm_p: 0.002
      1v2:
        auc: 0.6145
        ci_lower: 0.6045
        ci_upper: 0.6247
        perm_p: 0.002
      2v3:
        auc: 0.5496
        ci_lower: 0.5399
        ci_upper: 0.5596
        perm_p: 0.002
      3v4:
        auc: 0.5091
        ci_lower: 0.4973
        ci_upper: 0.52
        perm_p: 0.064
      4v5:
        auc: 0.5045
        ci_lower: 0.4932
        ci_upper: 0.515
        perm_p: 0.232
    qwen_cont:
      0v1:
        auc: 0.9971
        ci_lower: 0.9963
        ci_upper: 0.9978
        perm_p: 0.002
      1v2:
        auc: 0.6112
        ci_lower: 0.6015
        ci_upper: 0.6213
        perm_p: 0.002
      2v3:
        auc: 0.5609
        ci_lower: 0.5511
        ci_upper: 0.5712
        perm_p: 0.002
      3v4:
        auc: 0.5409
        ci_lower: 0.5308
        ci_upper: 0.5508
        perm_p: 0.002
      4v5:
        auc: 0.5141
        ci_lower: 0.5035
        ci_upper: 0.5255
        perm_p: 0.006
    k_star_robust: true
    all_1v2_ci_lower_above_060: true
    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold
- exp_id: exp_010_ordinal_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_rewrite:
      obd_lgbm:
        accuracy: 0.4229
        mae: 0.9836
        tau_b: 0.5518
        mean_pw_auc: 0.6214
      multiclass_lgbm:
        accuracy: 0.4182
        mae: 1.0163
        tau_b: 0.5367
        mean_pw_auc: 0.6246
      ordinal_logreg:
        accuracy: 0.3636
        mae: 0.9105
        tau_b: 0.563
        mean_pw_auc: 0.5022
    pythia:
      obd_lgbm:
        accuracy: 0.3856
        mae: 1.1072
        tau_b: 0.4745
        mean_pw_auc: 0.6055
      multiclass_lgbm:
        accuracy: 0.3832
        mae: 1.1399
        tau_b: 0.4622
        mean_pw_auc: 0.6062
      ordinal_logreg:
        accuracy: 0.3179
        mae: 1.022
        tau_b: 0.49
        mean_pw_auc: 0.4767
    olmo:
      obd_lgbm:
        accuracy: 0.3822
        mae: 1.1469
        tau_b: 0.4683
        mean_pw_auc: 0.6015
      multiclass_lgbm:
        accuracy: 0.3685
        mae: 1.1813
        tau_b: 0.4497
        mean_pw_auc: 0.5974
      ordinal_logreg:
        accuracy: 0.3265
        mae: 1.0352
        tau_b: 0.4656
        mean_pw_auc: 0.4859
- exp_id: exp_011_llm_zeroshot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gpt55_5class_acc: 0.332
    gpt55_mae: 1.102
    gpt55_spearman: 0.383
    gpt55_binary_acc: 0.878
    claude_5class_acc: 0.331
    claude_mae: 1.15
    claude_spearman: 0.416
    claude_binary_acc: 0.882
    odb_baseline_5class_acc: 0.386
    odb_baseline_mae: 1.107
    gpt55_per_depth_acc:
      depth_0: 0.77
      depth_1: 0.19
      depth_2: 0.38
      depth_3: 0.24
      depth_4: 0.08
    claude_per_depth_acc:
      depth_0: 0.69
      depth_1: 0.21
      depth_2: 0.28
      depth_3: 0.101
      depth_4: 0.37
    n_samples_per_model: 500
    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than
      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI
      detection is high (~88%) but fine-grained depth discrimination fails.
- exp_id: exp_015_neural_probe
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pythia:
      k_star_neural: 2
      k_star_lgbm: 2
      accuracy: 0.3892
      pairwise_auc:
        0v1: 0.966
        1v2: 0.676
        2v3: 0.596
        3v4: 0.555
        4v5: 0.532
    olmo:
      k_star_neural: 2
      k_star_lgbm: 2
      accuracy: 0.3729
      pairwise_auc:
        0v1: 0.95
        1v2: 0.657
        2v3: 0.589
        3v4: 0.547
        4v5: 0.53
    qwen_cont:
      k_star_neural: 3
      k_star_lgbm: 2
      accuracy: 0.4368
      pairwise_auc:
        0v1: 0.988
        1v2: 0.702
        2v3: 0.616
        3v4: 0.59
        4v5: 0.566
    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3
      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM
      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.
- exp_id: exp_006_graduated_filtering
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_runs: 51
    binary_ours:
      mmlu: 0.5941±0.0008
      hellaswag: 0.6701±0.0006
    binary_drayson:
      mmlu: 0.5913±0.0009
      hellaswag: 0.6691±0.0004
    surprisal:
      mmlu: 0.5894±0.0009
      hellaswag: 0.6641±0.0006
    graduated_a09:
      mmlu: 0.5892±0.0008
      hellaswag: 0.6701±0.0007
    graduated_a07:
      mmlu: 0.5892±0.0014
      hellaswag: 0.6695±0.0004
    graduated_a05:
      mmlu: 0.5880±0.0013
      hellaswag: 0.6687±0.0008
    graduated_a03:
      mmlu: 0.5877±0.0013
      hellaswag: 0.6669±0.0005
    graduated_a01:
      mmlu: 0.5873±0.0019
      hellaswag: 0.6640±0.0009
    dsir:
      mmlu: 0.5869±0.0003
      hellaswag: 0.6631±0.0007
    no_filter:
      mmlu: 0.5865±0.0010
      hellaswag: 0.6638±0.0008
    base_model:
      mmlu: '0.6018'
      hellaswag: '0.6821'
    best_strategy: binary-ours
    key_finding: binary-ours is best filtering strategy. All strategies degrade vs
      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR
      below all other strategies except no-filter.
- exp_id: exp_004_7b_crossscale
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9644
      1v2: 0.6178
      2v3: 0.546
      3v4: 0.5225
      4v5: 0.5091
    pairwise_auc_std:
      0v1: 0.0034
      1v2: 0.0081
      2v3: 0.0028
      3v4: 0.0113
      4v5: 0.0052
    bootstrap_ci:
      0v1:
        auc: 0.9638
        ci_lower: 0.9607
        ci_upper: 0.9665
        perm_p: 0.0001
      1v2:
        auc: 0.6168
        ci_lower: 0.6079
        ci_upper: 0.6261
        perm_p: 0.0001
      2v3:
        auc: 0.5492
        ci_lower: 0.5388
        ci_upper: 0.5594
        perm_p: 0.0001
      3v4:
        auc: 0.5276
        ci_lower: 0.517
        ci_upper: 0.5375
        perm_p: 0.0001
      4v5:
        auc: 0.5085
        ci_lower: 0.4988
        ci_upper: 0.5191
        perm_p: 0.0676
    bootstrap_resamples: 1000
    permutation_resamples: 10000
    pairwise_jsd:
      0v1: 0.127422
      1v2: 0.010114
      2v3: 0.004798
      3v4: 0.004821
      4v5: 0.003335
    ordinal_mae: 1.2156
    ordinal_accuracy: 0.3523
    top_features:
    - freq_entropy
    - surp_d1_skew
    - surp_std
    - surp_d1_mean
    - surp_mean
    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60
      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).
      FR-4 Warning resolved.
- exp_id: exp_A_alt_scorer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pythia_qwen_rw:
      k_star: 2
      auc_0v1: 0.9923
      auc_1v2: 0.7012
      auc_2v3: 0.587
      mae: 1.006
      accuracy: 0.417
      spearman_rho_vs_baseline: 0.906
    pythia_qwen_cont:
      k_star: 1
      auc_0v1: 0.99
      auc_1v2: 0.5923
      auc_2v3: null
      mae: 1.216
      accuracy: 0.371
      spearman_rho_vs_baseline: 0.942
    olmo_qwen_rw:
      k_star: 2
      auc_0v1: 0.9918
      auc_1v2: 0.6947
      auc_2v3: null
      mae: 1.016
      accuracy: 0.413
      spearman_rho_vs_baseline: 0.92
    olmo_qwen_cont:
      k_star: 1
      auc_0v1: 0.989
      auc_1v2: 0.5858
      auc_2v3: null
      mae: 1.229
      accuracy: 0.368
      spearman_rho_vs_baseline: 0.902
    key_finding: 'K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1
      (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer
      independence of feature ranking.'
- exp_id: exp_B_14d_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    result: K*=2 stable across all 4 models after removing self_BLEU (14D)
    key_finding: self_BLEU removal does not change K* boundary. FR-3 resolved.
- exp_id: exp_C_permutation_10k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    resamples: 10000
    all_boundary_pairs_p: <0.0001
    key_finding: 10K permutation confirms all boundary p-values well below 0.01. FR-11
      resolved.
- exp_id: exp_D_obd_n500
  name: ''
  status: DONE
  conclusion: success
  metrics:
    obd_accuracy_final: 0.38
    obd_ci:
    - 0.34
    - 0.422
    mcnemar_vs_gpt55_p: 0.0809
    mcnemar_vs_claude_p: 0.0693
    mcnemar_significant: false
    multi_seed_std: 0
    per_depth:
      d0: 0.96
      d1: 0.39
      d2: 0.14
      d3: 0.19
      d4: 0.22
    prob_merge_accuracy: 0.444
    prob_merge_d4_bias: 0.8
    note: v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant
      — supports discussion.tex narrative
- exp_id: exp_E_paired_stats
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu_significant_pairs: 8/15
    hellaswag_significant_pairs: 9/15
    binary_ours_vs_all_mmlu: all significant
    max_cohen_d_mmlu: 10.8
    max_cohen_d_hellaswag: 8.98
    graduated_a09_vs_dsir_corrected_p: 0.0523
    cohen_d_method: d_av (Lakens 2013)
    key_finding: 'binary-ours significantly outperforms all alternatives on MMLU.
      On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni
      cummax bug fixed: MMLU 10/15→8/15. Cohen''s d changed to d_av.'
    bugfix_note: Holm-Bonferroni cummax variable was never updated, causing 2 MMLU
      pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal
      vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).
- exp_id: exp_012_binary_confidence
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_samples: 500
    generators:
    - qwen-rewrite
    - pythia-1.4b
    - olmo-1b
    - qwen-cont
    6class_accuracy:
      qwen-rewrite: 0.1987
      pythia-1.4b: 0.1303
      olmo-1b: 0.127
      qwen-cont: 0.1833
      random_baseline: 0.1667
    spearman_rho:
      qwen-rewrite:
        log_ppl_ref: -0.1233
        log_ppl_obs: 0.0815
        ppl_ratio: 0.1185
      pythia-1.4b:
        log_ppl_ref: -0.2972
        log_ppl_obs: -0.4529
        ppl_ratio: -0.392
      olmo-1b:
        log_ppl_ref: -0.378
        log_ppl_obs: -0.4614
        ppl_ratio: -0.4068
      qwen-cont:
        log_ppl_ref: -0.3887
        log_ppl_obs: -0.162
        ppl_ratio: -0.058
    binary_detector_kstar: 1
    obd_kstar: 2
    auc_non_monotonic: true
    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy
      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but
      practically weak). AUC non-monotonic — binary detectors cannot maintain depth
      ordering. Confirms binary confidence ≠ depth estimation.
- exp_id: exp_kstar_theta
  name: ''
  status: DONE
  conclusion: success
  metrics:
    output_files:
    - kstar_theta_curve.pdf (32KB)
    - kstar_theta_curve.png (335KB)
    models:
    - Qwen-rewrite
    - Pythia
    - OLMo
    - Qwen-cont
    depth_pairs: 5
    key_finding: All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5.
      θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical
      resolved.
- exp_id: exp_016_base_vs_instruct
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.987
      1v2: 0.6262
      2v3: 0.5496
      3v4: 0.5294
      4v5: 0.5182
    pairwise_auc_std:
      0v1: 0.0015
      1v2: 0.0152
      2v3: 0.0067
      3v4: 0.0132
      4v5: 0.0139
    pairwise_jsd:
      0v1: 0.163726
      1v2: 0.01081
      2v3: 0.005311
      3v4: 0.003942
      4v5: 0.003522
    ordinal_mae: 1.1691
    ordinal_accuracy: 0.3719
    top_features:
    - freq_entropy
    - surp_std
    - surp_d1_skew
    - surp_d1_mean
    - surp_mean
    n_samples: 30000
    bootstrap_ci:
      0v1:
        auc: 0.987
        ci_lower: 0.9853
        ci_upper: 0.9885
        perm_p: 0.0001
      1v2:
        auc: 0.626
        ci_lower: 0.6168
        ci_upper: 0.6353
        perm_p: 0.0001
      2v3:
        auc: 0.5496
        ci_lower: 0.5397
        ci_upper: 0.56
        perm_p: 0.0001
      3v4:
        auc: 0.5293
        ci_lower: 0.5188
        ci_upper: 0.5399
        perm_p: 0.0001
      4v5:
        auc: 0.5181
        ci_lower: 0.5075
        ci_upper: 0.5288
        perm_p: 0.0016
    bootstrap_resamples: 10000
    permutation_resamples: 10000
    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%
      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant
      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above
      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,
      0.6213] — no significant base-vs-instruct difference.
- exp_id: exp_018_llama8b_depth
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9225
      1v2: 0.6123
      2v3: 0.5274
      3v4: 0.5138
      4v5: 0.5097
    jsd:
      0v1: 0.077
      1v2: 0.012
      2v3: 0.005
    bootstrap_ci:
      0v1:
        auc: 0.9224
        ci_lower: 0.9174
        ci_upper: 0.9272
        perm_p: 0.0001
      1v2:
        auc: 0.6123
        ci_lower: 0.6028
        ci_upper: 0.6216
        perm_p: 0.0001
      2v3:
        auc: 0.5273
        ci_lower: 0.5169
        ci_upper: 0.5378
        perm_p: 0.0001
      3v4:
        auc: 0.5168
        ci_lower: 0.5062
        ci_upper: 0.5275
        perm_p: 0.0037
      4v5:
        auc: 0.5159
        ci_lower: 0.5052
        ci_upper: 0.5268
        perm_p: 0.0035
    bootstrap_resamples: 10000
    permutation_resamples: 10000
- exp_id: exp_019_mistral7b_depth
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 1
    pairwise_auc:
      0v1: 0.9843
      1v2: 0.5935
      2v3: 0.5402
      3v4: 0.5232
      4v5: 0.5181
    bootstrap_ci_1v2:
      ci_lower: 0.5835
      ci_upper: 0.6032
      p_auc_leq_060: 0.9017
    jsd:
      0v1: 0.124194
      1v2: 0.008051
      2v3: 0.005047
      3v4: 0.004516
      4v5: 0.004109
    ordinal_mae: 1.2275
    ordinal_accuracy: 0.3567
    top3_features:
    - freq_entropy
    - surp_d1_skew
    - surp_d1_mean
- exp_id: exp_020_pythia_decoding
  name: ''
  status: DONE
  conclusion: success
  metrics:
    greedy:
      K_star: 2
      auc:
        0v1: 0.9992
        1v2: 0.8838
        2v3: 0.5342
        3v4: 0.5228
        4v5: 0.5162
    nuc09:
      K_star: 2
      auc:
        0v1: 0.9948
        1v2: 0.677
        2v3: 0.5549
        3v4: 0.5299
        4v5: 0.5013
    t07:
      K_star: 2
      auc:
        0v1: 0.9965
        1v2: 0.7265
        2v3: 0.5941
        3v4: 0.5698
        4v5: 0.5284
    t12:
      K_star: 2
      auc:
        0v1: 0.9933
        1v2: 0.6172
        2v3: 0.5226
        3v4: 0.517
        4v5: 0.5051
- exp_id: exp_021_length_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    128tok:
      K_star: 2
      1v2_auc: 0.6219
    256tok:
      K_star: 2
      1v2_auc: 0.6282
    512tok:
      K_star: 2
      1v2_auc: 0.6073
    all_K_star_2: true
    bootstrap_ci:
      512tok_1v2:
        auc: 0.6073
        ci_lower: 0.5979
        ci_upper: 0.6166
        perm_p: 0.0001
        verdict: BORDERLINE
- exp_id: exp_022_cross_scorer_matrix
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_combos: 12
    completed: 12
    K_star_distribution:
      K2: 11
      K1: 1
    matrix:
      pythia_greedy×olmo:
        K_star: 2
        1v2: 0.8811
      pythia_greedy×pythia:
        K_star: 2
        1v2: 0.8838
      pythia_greedy×qwen_base:
        K_star: 2
        1v2: 0.8814
      pythia_greedy×qwen_instruct:
        K_star: 2
        1v2: 0.8818
      qwen_base×olmo:
        K_star: 2
        1v2: 0.6047
      qwen_base×pythia:
        K_star: 2
        1v2: 0.617
      qwen_base×qwen_base:
        K_star: 2
        1v2: 0.6262
      qwen_base×qwen_instruct:
        K_star: 2
        1v2: 0.6273
      qwen_cont256×olmo:
        K_star: 2
        1v2: 0.6028
      qwen_cont256×pythia:
        K_star: 1
        1v2: 0.5979
      qwen_cont256×qwen_base:
        K_star: 2
        1v2: 0.6282
      qwen_cont256×qwen_instruct:
        K_star: 2
        1v2: 0.6072
    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:
      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to
      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'
- exp_id: exp_019b_mistral_cross_scorer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 1
    pairwise_auc:
      0v1: 0.9209
      1v2: 0.5695
      2v3: 0.5335
      3v4: 0.514
      4v5: 0.5184
    bootstrap_ci:
      0v1:
        mean: 0.9209
        ci_lower: 0.9189
        ci_upper: 0.9229
        pass_060: true
      1v2:
        mean: 0.5696
        ci_lower: 0.5645
        ci_upper: 0.5746
        pass_060: false
      2v3:
        mean: 0.5335
        ci_lower: 0.5283
        ci_upper: 0.5382
        pass_060: false
      3v4:
        mean: 0.514
        ci_lower: 0.5063
        ci_upper: 0.5213
        pass_060: false
      4v5:
        mean: 0.5183
        ci_lower: 0.5128
        ci_upper: 0.5244
        pass_060: false
    jsd:
      0v1: 0.08355
      1v2: 0.007642
      2v3: 0.004752
      3v4: 0.004255
      4v5: 0.003758
    ordinal_mae: 1.3737
    ordinal_accuracy: 0.3179
    top3_features:
    - freq_entropy
    - surp_d1_skew
    - surp_d1_mean
    key_finding: Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2
      AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral
      K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.
- exp_id: exp_023_domain_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    1v2_auc: 0.6193
    2v3_auc: 0.5498
    all_folds_above_060: true
    top_feature: freq_entropy
    ordinal_accuracy: 0.377
- exp_id: exp_024_arxiv_domain
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 3
    pairwise_auc:
      0v1: 0.9946
      1v2: 0.858
      2v3: 0.6427
      3v4: 0.5437
      4v5: 0.5294
    bootstrap_ci:
      0v1:
        auc: 0.9946
        ci_lower: 0.9929
        ci_upper: 0.9961
        perm_p: 0.0001
      1v2:
        auc: 0.858
        ci_lower: 0.848
        ci_upper: 0.8679
        perm_p: 0.0001
      2v3:
        auc: 0.6427
        ci_lower: 0.6275
        ci_upper: 0.6575
        perm_p: 0.0001
      3v4:
        auc: 0.5437
        ci_lower: 0.5276
        ci_upper: 0.5598
        perm_p: 0.0001
      4v5:
        auc: 0.5294
        ci_lower: 0.5133
        ci_upper: 0.5455
        perm_p: 0.0006
    bootstrap_resamples: 10000
    permutation_resamples: 10000
    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First
      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).
- exp_id: exp_025_pythia_arxiv
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    pairwise_auc:
      0v1: 0.9877
      1v2: 0.8047
      2v3: 0.6545
      3v4: 0.5507
      4v5: 0.5287
    pairwise_jsd:
      0v1: 0.171338
      1v2: 0.057344
      2v3: 0.019524
      3v4: 0.009917
      4v5: 0.008846
    bootstrap_ci:
      0v1:
        auc: 0.9876
        ci_lower: 0.9851
        ci_upper: 0.99
        perm_p: 0.0001
      1v2:
        auc: 0.8047
        ci_lower: 0.7934
        ci_upper: 0.8162
        perm_p: 0.0001
      2v3:
        auc: 0.6544
        ci_lower: 0.6401
        ci_upper: 0.6688
        perm_p: 0.0001
      3v4:
        auc: 0.55
        ci_lower: 0.534
        ci_upper: 0.5657
        perm_p: 0.0001
      4v5:
        auc: 0.5284
        ci_lower: 0.5122
        ci_upper: 0.5443
        perm_p: 0.001
    bootstrap_resamples: 10000
    permutation_resamples: 10000
    n_samples: 2200
    top_features:
    - freq_entropy
    - surp_std
    - surp_mean
    - surp_d1_skew
    - surp_d1_mean
    ordinal:
      MAE: 0.8518
      Accuracy: 0.4545
    key_finding: Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv).
      2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for
      arXiv.
- exp_id: exp_008_retrain_chain
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp-008-retrain-chain
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_008_retrain_chain_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: '>=4'
    pairwise_auc:
      0v1: 0.9847
      1v2: 0.9484
      2v3: 0.8888
      3v4: 0.7982
    pairwise_jsd:
      0v1: 0.17
      1v2: 0.12
      2v3: 0.064
      3v4: 0.04
    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts
      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic
      boundary.
- exp_id: exp_009_dose_response
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_runs: 45
    seeds: 5
    ratios:
    - 0.1
    - 0.3
    - 0.5
    strategies:
    - no_filter
    - binary_ours
    - graduated
    cross_ratio_finding: 'Binary filtering consistently best across all ratios. Graduated
      filtering = no_filter at every ratio. Effect size of binary advantage increases
      with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp).
      Original C3 hypothesis (graduated > binary) rejected.'
    gpu_hours_total: 9.9
- exp_id: exp_009_dose_10pct
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_009_dose_30pct
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_009_dose_50pct
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_009_dose_10pct_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_009_dose_30pct_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_009_dose_50pct_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_009_dose_10pct_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seeds: 5
    strategies: 3
    total_runs: 15
    mean_std:
      no_filter:
        mmlu: 0.6058±0.0002
        hellaswag: 0.6689±0.0007
      binary_ours:
        mmlu: 0.6079±0.0005
        hellaswag: 0.6727±0.0008
      graduated:
        mmlu: 0.6066±0.0011
        hellaswag: 0.6700±0.0015
    paired_ttest:
      binary_vs_nofilter:
        delta_mmlu: 0.0021
        p_mmlu: 0.001
        delta_hellaswag: 0.0038
        p_hellaswag: 0.0017
      graduated_vs_binary:
        delta_mmlu: -0.0014
        p_mmlu: 0.0917
        delta_hellaswag: -0.0027
        p_hellaswag: 0.0399
      graduated_vs_nofilter:
        delta_mmlu: 0.0008
        p_mmlu: 0.2706
        delta_hellaswag: 0.0011
        p_hellaswag: 0.0611
    key_finding: Binary best. Graduated ≈ no_filter.
- exp_id: exp_009_dose_30pct_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seeds: 5
    strategies: 3
    total_runs: 15
    mean_std:
      no_filter:
        mmlu: 0.6069±0.0007
        hellaswag: 0.6664±0.0020
      binary_ours:
        mmlu: 0.6082±0.0012
        hellaswag: 0.6725±0.0007
      graduated:
        mmlu: 0.6072±0.0008
        hellaswag: 0.6665±0.0014
    paired_ttest:
      binary_vs_nofilter:
        delta_mmlu: 0.0013
        p_mmlu: 0.0739
        delta_hellaswag: 0.0061
        p_hellaswag: 0.0036
      graduated_vs_binary:
        delta_mmlu: -0.001
        p_mmlu: 0.3018
        delta_hellaswag: -0.006
        p_hellaswag: 0.0009
      graduated_vs_nofilter:
        delta_mmlu: 0.0003
        p_mmlu: 0.6638
        delta_hellaswag: 0.0002
        p_hellaswag: 0.6646
    key_finding: Binary best on HellaSwag (p=0.004). Graduated = no_filter.
- exp_id: exp_009_dose_50pct_v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seeds: 5
    strategies: 3
    total_runs: 15
    mean_std:
      no_filter:
        mmlu: 0.6063±0.0013
        hellaswag: 0.6680±0.0005
      binary_ours:
        mmlu: 0.6088±0.0011
        hellaswag: 0.6731±0.0004
      graduated:
        mmlu: 0.6062±0.0009
        hellaswag: 0.6679±0.0002
    paired_ttest:
      binary_vs_nofilter:
        delta_mmlu: 0.0025
        p_mmlu: 0.0377
        delta_hellaswag: 0.0051
        p_hellaswag: 2.0e-05
      graduated_vs_binary:
        delta_mmlu: -0.0026
        p_mmlu: 0.0257
        delta_hellaswag: -0.0052
        p_hellaswag: 3.0e-05
      graduated_vs_nofilter:
        delta_mmlu: -0.0001
        p_mmlu: 0.89
        delta_hellaswag: -0.0001
        p_hellaswag: 0.706
    key_finding: Binary significantly best (HellaSwag p<0.001). Graduated = no_filter
      exactly.
- exp_id: exp_026_feature_stability
  name: ''
  status: DONE
  conclusion: success
  metrics:
    data_source: exp_016_qwen_base (prompt-chain, K*=2)
    results:
      15D:
        num_tested: 1
        num_kstar_2: 1
        min_1v2_auc: 0.6262
        mean_1v2_auc: 0.6262
      10D:
        num_tested: 5
        num_kstar_2: 5
        min_1v2_auc: 0.6153
        mean_1v2_auc: 0.6191
      8D:
        num_tested: 5
        num_kstar_2: 5
        min_1v2_auc: 0.6056
        mean_1v2_auc: 0.6159
      5D:
        num_tested: 5
        num_kstar_2: 2
        min_1v2_auc: 0.5856
        mean_1v2_auc: 0.5998
      3D_top3:
        num_tested: 1
        num_kstar_2: 0
        min_1v2_auc: 0.5871
        mean_1v2_auc: 0.5871
    all_above_theta: false
    key_finding: 'Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust
      (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856).
      Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where
      all subsets trivially passed (min=0.8314).'
    previous_run_note: v1 used retrain-chain data (K*=4), where all subsets trivially
      passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary
      robustness.
- exp_id: exp_027_retrain_bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    bootstrap_iterations: 10000
    pairs:
      0v1:
        auc_point: 0.9847
        ci_lower: 0.9828
        ci_upper: 0.9864
        perm_p: 0.0001
        ci_lower_gt_theta: true
      1v2:
        auc_point: 0.9482
        ci_lower: 0.9443
        ci_upper: 0.952
        perm_p: 0.0001
        ci_lower_gt_theta: true
      2v3:
        auc_point: 0.8885
        ci_lower: 0.8829
        ci_upper: 0.894
        perm_p: 0.0001
        ci_lower_gt_theta: true
      3v4:
        auc_point: 0.7977
        ci_lower: 0.7903
        ci_upper: 0.8051
        perm_p: 0.0001
        ci_lower_gt_theta: true
    key_finding: All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min
      CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.
- exp_id: exp_027
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kstar_ci: 4
    0v1_auc: 0.9847
    0v1_ci:
    - 0.9828
    - 0.9864
    0v1_perm_p: 0.0001
    1v2_auc: 0.9482
    1v2_ci:
    - 0.9443
    - 0.952
    1v2_perm_p: 0.0001
    2v3_auc: 0.8885
    2v3_ci:
    - 0.8829
    - 0.894
    2v3_perm_p: 0.0001
    3v4_auc: 0.7977
    3v4_ci:
    - 0.7903
    - 0.8051
    3v4_perm_p: 0.0001
    all_ci_lower_above_theta: true
- exp_id: exp_026_feature_stability_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    data_source: exp_001_pythia prompt-chain (K*=2)
    results:
      15D:
        num_tested: 1
        num_pass: 1
        min_1v2_auc: 0.6262
        mean_1v2_auc: 0.6262
      10D:
        num_tested: 5
        num_pass: 5
        min_1v2_auc: 0.6153
        mean_1v2_auc: 0.6191
      8D:
        num_tested: 5
        num_pass: 5
        min_1v2_auc: 0.6056
        mean_1v2_auc: 0.6159
      5D:
        num_tested: 5
        num_pass: 2
        min_1v2_auc: 0.5856
        mean_1v2_auc: 0.5998
      3D_top3:
        num_tested: 1
        num_pass: 0
        min_1v2_auc: 0.5871
        mean_1v2_auc: 0.5871
    key_finding: 8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile
      (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.
- exp_id: exp_arXiv_olmo
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    K_star: 1
    auc_0v1: 0.9958
    auc_1v2: 0.5034
    auc_2v3: 0.5069
    auc_3v4: 0.5021
    auc_4v5: 0.5037
    jsd_0v1: 0.329
    ordinal_acc: 0.33
- exp_id: exp_arXiv_llama8b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 3
    auc_0v1: 0.9754
    auc_1v2: 0.8447
    auc_2v3: 0.6215
    auc_3v4: 0.5362
    auc_4v5: 0.5331
    jsd_0v1: 0.1296
    jsd_1v2: 0.0785
    jsd_2v3: 0.0177
    ordinal_acc: 0.4549
    ordinal_mae: 0.8806
- exp_id: exp_wiki_pythia
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_wiki_olmo
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_wiki_pythia_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    K_star: 1
    auc_0v1: 0.975
    auc_1v2: 0.5846
    auc_2v3: 0.5445
    auc_3v4: 0.5205
    auc_4v5: 0.5168
    jsd_0v1: 0.080065
    jsd_1v2: 0.007773
    ordinal_acc: 0.3503
- exp_id: exp_wiki_olmo_v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    K_star: 1
    auc_0v1: 0.9932
    auc_1v2: 0.4986
    auc_2v3: 0.5012
    auc_3v4: 0.5057
    auc_4v5: 0.5009
    jsd_0v1: 0.1688
    ordinal_acc: 0.3227
- exp_id: exp_arXiv_qwen7b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    pairwise_auc:
      0v1: 0.983
      1v2: 0.835
      2v3: 0.626
      3v4: 0.544
      4v5: 0.513
    pairwise_jsd:
      0v1: 0.1656
      1v2: 0.0668
      2v3: 0.0156
      3v4: 0.0089
      4v5: 0.0061
    ordinal_mae: 0.9
    ordinal_accuracy: 0.446
- exp_id: exp_wiki_llama8b
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    K_star: 1
    ordinal_mae: 1.2954
    ordinal_accuracy: 0.3313
    auc_0v1: 0.9316
    auc_1v2: 0.5954
    auc_2v3: 0.5392
    auc_3v4: 0.5221
    auc_4v5: 0.5212
    jsd_0v1: 0.06169
    jsd_1v2: 0.00931
- exp_id: exp_arXiv_mistral7b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    pairwise_auc:
      0v1: 0.9848
      1v2: 0.8201
      2v3: 0.6275
      3v4: 0.5295
      4v5: 0.5295
    jsd:
      0v1: 0.14249
      1v2: 0.076232
      2v3: 0.018972
      3v4: 0.009908
      4v5: 0.008877
    ordinal_mae: 0.8958
    ordinal_accuracy: 0.4474
    top_features:
    - freq_entropy
    - surp_std
    - surp_d1_skew
    - surp_mean
    - surp_d2_mean
- exp_id: exp_wiki_mistral7b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 1
    ordinal_mae: 1.3445
    ordinal_accuracy: 0.3273
    auc_0v1: 0.9607
    auc_1v2: 0.5552
    auc_2v3: 0.5236
    auc_3v4: 0.5181
    auc_4v5: 0.5012
    jsd_0v1: 0.054134
    jsd_1v2: 0.005678
    jsd_2v3: 0.003698
    jsd_3v4: 0.003459
    jsd_4v5: 0.003274
- exp_id: exp_14b_c4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    pairwise_auc:
      0v1: 0.9598
      1v2: 0.621
      2v3: 0.5494
      3v4: 0.5243
      4v5: 0.5154
    pairwise_jsd:
      0v1: 0.1097
      1v2: 0.0112
      2v3: 0.0062
      3v4: 0.0044
      4v5: 0.0036
    bootstrap_ci:
      0v1:
      - 0.9564
      - 0.963
      1v2:
      - 0.6119
      - 0.6304
      2v3:
      - 0.5392
      - 0.5594
      3v4:
      - 0.514
      - 0.5346
      4v5:
      - 0.5045
      - 0.5265
    permutation_p:
      0v1: <0.001
      1v2: <0.001
      2v3: <0.001
      3v4: <0.001
      4v5: <0.001
    k_star_statistically_confirmed: true
    ordinal_mae: 1.2266
    ordinal_accuracy: 0.3497
    top_features:
    - freq_entropy
    - surp_d1_skew
    - surp_std
    - surp_d1_mean
    - surp_d2_mean
    key_finding: K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119)
      > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.
- exp_id: exp_32b_c4
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_wiki_qwen7b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    auc_0v1: 0.9673
    auc_1v2: 0.6108
    auc_2v3: 0.5562
    auc_3v4: 0.5297
    auc_4v5: 0.529
    jsd_0v1: 0.083514
    jsd_1v2: 0.010991
    jsd_2v3: 0.00555
    jsd_3v4: 0.004611
    jsd_4v5: 0.003894
    ordinal_mae: 1.2501
    ordinal_accuracy: 0.3532
- exp_id: exp_wiki_scorer_confound
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    k_star: 1
    confound_verdict: confirmed
    auc_0v1: 0.9404
    auc_1v2: 0.587
    auc_2v3: 0.5456
    auc_3v4: 0.525
    auc_4v5: 0.5172
    critical_delta_1v2: -0.0238
- exp_id: exp_wiki_scorer_confound_1b5
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    k_star: 1
    confound_verdict: confirmed
    auc_0v1: 0.9729
    auc_1v2: 0.5994
    auc_2v3: 0.533
    auc_3v4: 0.5214
    auc_4v5: 0.5068
    jsd_0v1: 0.0886
    ordinal_mae: 1.2995
    ordinal_accuracy: 0.3466
- exp_id: exp_arXiv_qwen7b_crossscorer
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    k_star: 2
    auc_0v1: 0.9575
    auc_1v2: 0.8171
    auc_2v3: 0.5989
    auc_3v4: 0.5417
    auc_4v5: 0.5192
    jsd_0v1: 0.137085
    jsd_1v2: 0.059688
    jsd_2v3: 0.013508
    jsd_3v4: 0.009125
    jsd_4v5: 0.006738
    ordinal_mae: 0.9617
    ordinal_accuracy: 0.4255
- exp_id: exp_arXiv_qwen1b5_crossscorer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    auc_0v1: 0.9748
    auc_1v2: 0.8105
    auc_2v3: 0.6317
    auc_3v4: 0.5437
    auc_4v5: 0.5294
    jsd_0v1: 0.154297
    jsd_1v2: 0.066782
    jsd_2v3: 0.019268
    jsd_3v4: 0.008867
    jsd_4v5: 0.006991
    ordinal_mae: 0.9017
    ordinal_accuracy: 0.4402
- exp_id: exp_arXiv_llama8b_crossscorer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    auc_0v1: 0.9629
    auc_1v2: 0.8433
    auc_2v3: 0.6201
    auc_3v4: 0.523
    auc_4v5: 0.5245
    jsd_0v1: 0.1214
    jsd_1v2: 0.0815
    jsd_2v3: 0.0195
    jsd_3v4: 0.0083
    jsd_4v5: 0.0082
    ordinal_mae: 0.9025
    ordinal_accuracy: 0.4407
    scorer: pythia-1.4b
- exp_id: exp_arXiv_mistral7b_crossscorer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    scorer: pythia-1.4b
    auc_0v1: 0.9798
    auc_1v2: 0.8141
    auc_2v3: 0.6075
    auc_3v4: 0.5489
    auc_4v5: 0.5391
    jsd_0v1: 0.135575
    jsd_1v2: 0.078
    jsd_2v3: 0.020452
    jsd_3v4: 0.010992
    jsd_4v5: 0.008831
    ordinal_mae: 0.9061
    ordinal_accuracy: 0.4412
- exp_id: exp_025_pythia_filtering
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    runs_completed: 9/9
    strategies:
    - no_filter
    - binary_ours
    - graduated_a09
    seeds:
    - 42
    - 123
    - 456
    mmlu:
      no_filter: 0.2568±0.0012
      binary_ours: 0.2585±0.0004
      graduated_a09: 0.2561±0.0009
    hellaswag:
      no_filter: 0.5250±0.0008
      binary_ours: 0.5251±0.0001
      graduated_a09: 0.5253±0.0007
    delta_vs_no_filter:
      binary_ours_mmlu: '+0.0017'
      binary_ours_hellaswag: '+0.0000'
      graduated_a09_mmlu: '-0.0007'
      graduated_a09_hellaswag: '+0.0003'
    key_finding: All three filtering strategies produce nearly identical results on
      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering
      binary>graduated>no_filter NOT confirmed.
- exp_id: exp_026_arxiv_filtering
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    runs_completed: 15/15
    strategies:
    - no_filter
    - binary
    - graduated_a09
    seeds:
    - 42
    - 123
    - 456
    - 789
    - 1024
    mmlu:
      no_filter: 0.5899±0.0008
      binary: 0.5876±0.0004
      graduated_a09: 0.5900±0.0011
    hellaswag:
      no_filter: 0.6600±0.0002
      binary: 0.6642±0.0004
      graduated_a09: 0.6599±0.0003
    delta_vs_no_filter:
      binary_mmlu: '-0.0023'
      binary_hellaswag: '+0.0042'
      graduated_mmlu: '+0.0001'
      graduated_hellaswag: '-0.0001'
    key_finding: All three strategies produce nearly identical results. Graduated
      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU
      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.
- exp_id: exp_027_latex_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 3
    k_star_preserved: true
    pairwise_auc_original:
      0v1: 0.9948
      1v2: 0.8581
      2v3: 0.6436
      3v4: 0.544
      4v5: 0.5299
    pairwise_auc_stripped:
      0v1: 0.9948
      1v2: 0.8297
      2v3: 0.6229
      3v4: 0.5468
      4v5: 0.5476
    auc_delta:
      0v1: 0
      1v2: -0.028
      2v3: -0.021
      3v4: 0.003
      4v5: 0.018
    latex_reduction_by_depth:
      depth_0: 0.6%
      depth_5: 4.4%
    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still
      >θ=0.60). LaTeX format is NOT a confound.
- exp_id: exp_028_subsampling_power
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_1000:
      mean_auc: 0.608
      std: 0.012
      detection_prob: 0.9
    n_2500:
      mean_auc: 0.618
      std: 0.006
      detection_prob: 1
    n_5000:
      mean_auc: 0.629
      std: 0
      detection_prob: 1
    key_finding: n>=2500 gives 100% reliable K*=2 detection. n=1000 already 90%. Signal
      is robust, not large-sample artifact.
- exp_id: exp_olmo_retrain_chain
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_olmo_retrain_v2
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: exp_code_qwen1b5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    theta: 0.6
    auc_0v1: 0.9388
    auc_1v2: 0.7382
    auc_2v3: 0.53
    auc_3v4: 0.5022
    auc_4v5: 0.5219
    ci_0v1:
    - 0.929
    - 0.949
    ci_1v2:
    - 0.709
    - 0.767
    ci_2v3:
    - 0.514
    - 0.546
    jsd_0v1: 0.0814
    jsd_1v2: 0.0443
    jsd_2v3: 0.0038
    ordinal_accuracy: 0.359
    ordinal_mae: 1.204
- exp_id: exp_code_llama8b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star: 2
    pairwise_auc:
      0v1: 0.9161
      1v2: 0.7394
      2v3: 0.5112
      3v4: 0.52
      4v5: 0.4996
    pairwise_auc_std:
      0v1: 0.004
      1v2: 0.0101
      2v3: 0.0095
      3v4: 0.0137
      4v5: 0.0069
    pairwise_jsd:
      0v1: 0.060406
      1v2: 0.047034
      2v3: 0.003473
      3v4: 0.003026
      4v5: 0.002892
    ordinal_mae: 1.2542
    ordinal_accuracy: 0.3485
    top_features:
    - freq_entropy
    - surp_d1_mean
    - surp_d2_mean
- exp_id: exp_qwen_retrain_chain
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K_star_lower_bound: 4
    theta: 0.6
    auc_0v1: 0.9838
    auc_1v2: 0.8969
    auc_2v3: 0.81
    auc_3v4: 0.7624
    ci_0v1:
    - 0.982
    - 0.9855
    ci_1v2:
    - 0.8937
    - 0.9001
    ci_2v3:
    - 0.8052
    - 0.8147
    ci_3v4:
    - 0.7543
    - 0.7706
    ci_method: 5-fold CV
    jsd_0v1: 0.2263
    jsd_1v2: 0.1046
    jsd_2v3: 0.0752
    jsd_3v4: 0.0654
- exp_id: exp_code_pythia1b4
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    k_star: 1
    theta: 0.6
    pairwise_auc:
      0v1:
        mean: 0.9592
        std: 0.0036
        folds:
        - 0.9576
        - 0.9576
        - 0.9657
        - 0.96
        - 0.9552
      1v2:
        mean: 0.5983
        std: 0.005
        folds:
        - 0.601
        - 0.5884
        - 0.6
        - 0.5997
        - 0.6024
      2v3:
        mean: 0.5215
        std: 0.0128
        folds:
        - 0.5236
        - 0.5124
        - 0.5311
        - 0.5024
        - 0.5381
      3v4:
        mean: 0.5152
        std: 0.012
        folds:
        - 0.4981
        - 0.5327
        - 0.5092
        - 0.5123
        - 0.5238
      4v5:
        mean: 0.5046
        std: 0.0137
        folds:
        - 0.4983
        - 0.4822
        - 0.5074
        - 0.5224
        - 0.5128
    jsd:
      0v1: 0.070173
      1v2: 0.008211
      2v3: 0.003674
      3v4: 0.002902
      4v5: 0.002685
    ordinal:
      mae: 1.3268
      accuracy: 0.3357
    top_features:
    - freq_entropy
    - surp_d1_mean
    - surp_d2_mean
    - surp_mean
    - surp_d1_skew
    features_csv: /root/autodl-tmp/gen-depth-contamination/data/exp_code_pythia1b4/features.csv
- exp_id: exp_028_power_curve
  name: ''
  status: DONE
  conclusion: success
  metrics:
    min_n_100pct: 2000
    n500_auc: 0.5808
    n500_rate: 0.2
    n1000_auc: 0.5911
    n1000_rate: 0.3
    n2000_auc: 0.6101
    n2000_rate: 1
    n3000_auc: 0.6166
    n3000_rate: 1
    n4000_auc: 0.622
    n4000_rate: 1
    n5000_auc: 0.6288
    n5000_rate: 1
- exp_id: exp_code_mistral7b
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_code_qwen7b
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_qwen_retrain_depth7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 7
    theta: 0.6
    max_depth: 7
    analysis_method: 5-fold GroupKFold CV
    pairwise_auc:
      0v1:
        mean: 0.9837
        std: 0.0019
        ci_95:
        - 0.9821
        - 0.9854
        folds:
        - 0.9832
        - 0.9821
        - 0.9837
        - 0.9823
        - 0.9873
      1v2:
        mean: 0.8971
        std: 0.0025
        ci_95:
        - 0.8949
        - 0.8993
        folds:
        - 0.8923
        - 0.8988
        - 0.8986
        - 0.8991
        - 0.8967
      2v3:
        mean: 0.8098
        std: 0.0052
        ci_95:
        - 0.8052
        - 0.8144
        folds:
        - 0.8086
        - 0.8074
        - 0.818
        - 0.8024
        - 0.8128
      3v4:
        mean: 0.76
        std: 0.0082
        ci_95:
        - 0.7528
        - 0.7672
        folds:
        - 0.7534
        - 0.7617
        - 0.7753
        - 0.7566
        - 0.7531
      4v5:
        mean: 0.7459
        std: 0.0091
        ci_95:
        - 0.7379
        - 0.7538
        folds:
        - 0.7429
        - 0.7562
        - 0.7521
        - 0.73
        - 0.7482
      5v6:
        mean: 0.7017
        std: 0.0068
        ci_95:
        - 0.6958
        - 0.7076
        folds:
        - 0.7006
        - 0.7077
        - 0.7104
        - 0.6915
        - 0.6984
      6v7:
        mean: 0.641
        std: 0.0039
        ci_95:
        - 0.6376
        - 0.6445
        folds:
        - 0.6419
        - 0.6349
        - 0.6464
        - 0.639
        - 0.643
    jsd:
      0v1: 0.23005
      1v2: 0.103924
      2v3: 0.075049
      3v4: 0.065398
      4v5: 0.060509
      5v6: 0.034998
      6v7: 0.017652
- exp_id: exp_pythia_retrain_depth7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    kstar: 7
    pairwise_auc:
      0v1: 0.9844
      1v2: 0.947
      2v3: 0.8891
      3v4: 0.7999
      4v5: 0.6907
      5v6: 0.6497
      6v7: 0.634
    pairwise_auc_ci:
      0v1:
      - 0.9829
      - 0.9858
      1v2:
      - 0.9418
      - 0.9522
      2v3:
      - 0.8822
      - 0.896
      3v4:
      - 0.7951
      - 0.8047
      4v5:
      - 0.688
      - 0.6934
      5v6:
      - 0.6429
      - 0.6565
      6v7:
      - 0.6275
      - 0.6406
    pairwise_jsd:
      0v1: 0.1775
      1v2: 0.1286
      2v3: 0.1069
      3v4: 0.0643
      4v5: 0.0331
      5v6: 0.0271
      6v7: 0.0138
- exp_id: exp_code_qwen1b5_pythia_scorer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    k_star: 2
    theta: 0.6
    auc_0v1: 0.9076
    auc_1v2: 0.7197
    auc_2v3: 0.5308
    auc_3v4: 0.5236
    auc_4v5: 0.5084
    jsd_0v1: 0.065423
    jsd_1v2: 0.035809
    jsd_2v3: 0.004315
    jsd_3v4: 0.003182
    jsd_4v5: 0.003047
    ordinal_mae: 1.2578
    ordinal_accuracy: 0.3433
    scorer: pythia-1.4b

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: median
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "59587622-660c-4957-a549-a3c2036a769c",
  "type": "user",
  "uuid": "3f1bb923-6bda-439a-bcb5-c6ecab482202",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T09:19:05.186Z_

```json
{
  "parentUuid": "3f1bb923-6bda-439a-bcb5-c6ecab482202",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "bd8d7af8-88f2-46df-a0f1-758c5345466b",
  "timestamp": "2026-05-19T09:19:05.186Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T09:19:05.186Z_

```json
{
  "parentUuid": "bd8d7af8-88f2-46df-a0f1-758c5345466b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fab1ae6f-a4b5-450b-a686-2e8c808bab85",
  "timestamp": "2026-05-19T09:19:05.186Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑 核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domai…",
  "leafUuid": "fab1ae6f-a4b5-450b-a686-2e8c808bab85",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-dependent K* saturation with cross-model validation",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Assistant

_source line 8 · 2026-05-19T09:19:24.755Z_

我先检查项目目录下的相关文件，确认 experiment_plan 的完整定义和当前状态。

Let me review the existing files to get the full picture of all experiments, especially the RUNNING ones (Mistral-7B Code, Qwen-7B Code) and any supplementary experiments that might be needed under the median tier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fab1ae6f-a4b5-450b-a686-2e8c808bab85",
  "isSidechain": false,
  "requestId": "req_011CbBgKHK6LzMXMvJAKGQG3",
  "type": "assistant",
  "uuid": "ab4723ef-8fa2-45ae-b729-ecbe46d58049",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XqJmBBgqCViwewynj6AxE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54347,
      "cache_read_input_tokens": 11841,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 308,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54347
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

### Tool call

_source line 9 · 2026-05-19T09:19:29.645Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015wtATiGMPMxLnEZgHLdogm`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan and status files",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_7, find all files related to experiment plans, registry, or phase definitions. I need to understand:\n1. What experiments are in status RUNNING or planned\n2. Any files defining the median tier scenario\n3. Any files with supplementary experiment definitions beyond what's in experiment_plan\n\nSearch for files like experiment_plan*, registry*, phase*, tier*, scenario*, median* in the project directory. Also look for any YAML or markdown files that contain \"median\" or \"RUNNING\" or \"supplementary\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab4723ef-8fa2-45ae-b729-ecbe46d58049",
  "isSidechain": false,
  "requestId": "req_011CbBgKHK6LzMXMvJAKGQG3",
  "type": "assistant",
  "uuid": "2e20a1a6-75a5-4915-bd64-57a61b2c21aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019XqJmBBgqCViwewynj6AxE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 54347,
      "cache_read_input_tokens": 11841,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 54347,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 308,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 54347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 54347
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

### Tool result

_source line 10 · 2026-05-19T09:20:35.715Z_

<details><summary>↩ Tool result · `toolu_015wtATiGMPMxLnEZgHLdogm`</summary>

```text
Perfect! Now I have gathered comprehensive information. Let me compile my findings.

## Summary Report: Experiment Plans, Registry, and Phase Definitions

### 1. RUNNING EXPERIMENTS (3 Active)

Three experiments are currently in **RUNNING** status in the registry:

1. **exp_32b_c4** (started 2026-05-17, updated 2026-05-19T02:50)
   - Qwen2.5-32B scale verification on C4 domain
   - Hypothesis: Verify K*=2 stability at 32B scale (confirmed for 1.5B/7B/8B/14B)
   - Config: C4 5K docs, depth 0-5, nucleus p=0.95 T=1.0
   - Server: westd-42896, GPU: cuda:1
   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (lines 3545-3569)

2. **exp_code_mistral7b** (started 2026-05-18, updated 2026-05-19T02:54)
   - Mistral-7B code domain K* measurement on CodeSearchNet Python
   - Hypothesis: Test if Mistral K*=1 (C4) differs from Qwen/LLaMA K*=2 on code domain
   - Config: CodeSearchNet Python 5K docs, depth 0-5, nucleus p=0.95 T=1.0
   - Server: cqa1-22115, GPU: cuda:3, PID: 107037
   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (lines 4547-4579)

3. **exp_code_qwen7b** (started 2026-05-19, updated 2026-05-19T01:48)
   - Qwen2.5-7B code domain K* measurement
   - Hypothesis: Test Qwen family scale invariance on code domain; verify cross-model consistency
   - Config: CodeSearchNet Python 5K docs, depth 0-5, nucleus p=0.95 T=1.0
   - Server: cqa1-22115, GPU: cuda:1, PID: 114228
   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (lines 4581-4615)

### 2. MEDIAN TIER SCENARIO FILES (Supplementary Experiment Definitions)

Dream reports define three reviewer tiers: **best**, **median**, **worst**. The **median** tier is the central "expected" case and contains supplementary experiment definitions beyond the main experiment_plan.yaml.

Median tier files are located in:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/` (latest symlink)

Key median scenario files:
- **imagined_experiments.yaml** - Supplementary experiment definitions with expected results
- **review_context.yaml** - Reviewer perspective and key assumptions for median tier
- **experiment_data.json** - Structured experiment metadata

The median tier defines reviewer expectations including:
- K* characterization acceptance level
- Effect sizes for filtering experiments (exp-006: MMLU Δ=0.76pp)
- Sensitivity analysis requirements (θ=0.60 boundary robustness)
- Scale limitations (≤8B considered weakness)
- Evidence requirements for C1' and C3 claims

### 3. PLAN FILES - Main Experiment Definitions

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.yaml` - Primary experiment plan with 28+ experiments (exp-001 through exp-028)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.lock` - Lock file (1 line)

The main plan includes P0 and P1 priority experiments covering:
- Cross-model universality (Pythia, OLMo, LLaMA, Mistral, Qwen)
- Decoding strategy ablations
- Scale testing (1.5B to 32B)
- Domain variations (C4, Wikipedia, arXiv)
- Cross-scorer validation
- Filtering strategy evaluation

### 4. REGISTRY FILES

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (184 KB) - Comprehensive experiment registry with execution details, metrics, and status
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/dream_registry.yaml` (8.3 KB) - Dream report registry tracking all imagined/simulated reviews

### 5. SUPPLEMENTARY PHASE/TIER DEFINITIONS

**Dream Report Tiers** (best/median/worst) organized by date:

- **dream_20260512T200328** - Route B framing (Route B = K* as first-measured saturation boundary)
- **dream_20260513T080728** - Full review mode
- **dream_20260516T073047** - Universality scoping (boundary conditions at 128-token, T=0.7, cross-scorer)
- **dream_20260518T113009** - Evaluation without arXiv negative results (exp_026 excluded)
- **dream_20260518T122223** - Failed: With arXiv honest negative (status: failed, pid: null)
- **dream_20260518T123349** - Failed: With arXiv honest negative (status: failed, pid: null)
- **dream_20260518T125757** - Current best: With arXiv negative + one-wash laundering concept (status: done, latest symlink)
- **dream_20260519T090934** - Current: RUNNING/imagining - Code domain cross-model results, focus on 4-domain + 6-architecture coverage

### 6. KEY FINDINGS FOR RUNNING DREAM (dream_20260519T090934)

**Status:** `imagining` (in progress)
**Focus areas:**
1. Code domain results: LLaMA-8B K*=2 confirmed (cross-family), Mistral-7B and Qwen-7B Code still RUNNING
2. Domain hierarchy established: Wiki(K*=1) < C4/Code(K*=2) < arXiv(K*=3)
3. Retrain chain K*=7 (two families tested)
4. Key uncertainty: Is 4-domain + 6-architecture coverage sufficient for EMNLP accept?
5. Concern: C3 filtering weakness (negative results on arXiv/Pythia)

**Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/dream_registry.yaml` (lines 181-205)
- No dream_20260519T090934/median folder yet (still in imagine stage)

### 7. SUPPLEMENTARY EXPERIMENT DEFINITIONS EXAMPLE

The median tier imagined_experiments.yaml files contain detailed supplementary definitions not in the base experiment_plan, including:

- **exp-014 (Naturalistic Common Crawl Validation)** - 10K CC 2025/2026 docs with AlignScore correlation validation
- **exp-018 (LLaMA-3.1-8B cross-family)** - Expected K*=2, pairwise AUC predictions
- Expected statistical metrics (bootstrap CI, permutation p-values)
- Reviewer-specific rationales explaining why each result matters at different tiers

**Example location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T113009/median/imagined_experiments.yaml` (1,000+ lines with full experiment specifications)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e20a1a6-75a5-4915-bd64-57a61b2c21aa",
  "isSidechain": false,
  "promptId": "59587622-660c-4957-a549-a3c2036a769c",
  "type": "user",
  "uuid": "7b00c4ae-ca83-46d8-a033-2a0551fc144b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_7, find all files related to experiment plans, registry, or phase definitions. I need to understand:\n1. What experiments are in status RUNNING or planned\n2. Any files defining the median tier scenario\n3. Any files with supplementary experiment definitions beyond what's in experiment_plan\n\nSearch for files like experiment_plan*, registry*, phase*, tier*, scenario*, median* in the project directory. Also look for any YAML or markdown files that contain \"median\" or \"RUNNING\" or \"supplementary\".",
    "agentId": "af4d04ffba38b8d5e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have gathered comprehensive information. Let me compile my findings.\n\n## Summary Report: Experiment Plans, Registry, and Phase Definitions\n\n### 1. RUNNING EXPERIMENTS (3 Active)\n\nThree experiments are currently in **RUNNING** status in the registry:\n\n1. **exp_32b_c4** (started 2026-05-17, updated 2026-05-19T02:50)\n   - Qwen2.5-32B scale verification on C4 domain\n   - Hypothesis: Verify K*=2 stability at 32B scale (confirmed for 1.5B/7B/8B/14B)\n   - Config: C4 5K docs, depth 0-5, nucleus p=0.95 T=1.0\n   - Server: westd-42896, GPU: cuda:1\n   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (lines 3545-3569)\n\n2. **exp_code_mistral7b** (started 2026-05-18, updated 2026-05-19T02:54)\n   - Mistral-7B code domain K* measurement on CodeSearchNet Python\n   - Hypothesis: Test if Mistral K*=1 (C4) differs from Qwen/LLaMA K*=2 on code domain\n   - Config: CodeSearchNet Python 5K docs, depth 0-5, nucleus p=0.95 T=1.0\n   - Server: cqa1-22115, GPU: cuda:3, PID: 107037\n   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (lines 4547-4579)\n\n3. **exp_code_qwen7b** (started 2026-05-19, updated 2026-05-19T01:48)\n   - Qwen2.5-7B code domain K* measurement\n   - Hypothesis: Test Qwen family scale invariance on code domain; verify cross-model consistency\n   - Config: CodeSearchNet Python 5K docs, depth 0-5, nucleus p=0.95 T=1.0\n   - Server: cqa1-22115, GPU: cuda:1, PID: 114228\n   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (lines 4581-4615)\n\n### 2. MEDIAN TIER SCENARIO FILES (Supplementary Experiment Definitions)\n\nDream reports define three reviewer tiers: **best**, **median**, **worst**. The **median** tier is the central \"expected\" case and contains supplementary experiment definitions beyond the main experiment_plan.yaml.\n\nMedian tier files are located in:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/` (latest symlink)\n\nKey median scenario files:\n- **imagined_experiments.yaml** - Supplementary experiment definitions with expected results\n- **review_context.yaml** - Reviewer perspective and key assumptions for median tier\n- **experiment_data.json** - Structured experiment metadata\n\nThe median tier defines reviewer expectations including:\n- K* characterization acceptance level\n- Effect sizes for filtering experiments (exp-006: MMLU Δ=0.76pp)\n- Sensitivity analysis requirements (θ=0.60 boundary robustness)\n- Scale limitations (≤8B considered weakness)\n- Evidence requirements for C1' and C3 claims\n\n### 3. PLAN FILES - Main Experiment Definitions\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.yaml` - Primary experiment plan with 28+ experiments (exp-001 through exp-028)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/experiment_plan.lock` - Lock file (1 line)\n\nThe main plan includes P0 and P1 priority experiments covering:\n- Cross-model universality (Pythia, OLMo, LLaMA, Mistral, Qwen)\n- Decoding strategy ablations\n- Scale testing (1.5B to 32B)\n- Domain variations (C4, Wikipedia, arXiv)\n- Cross-scorer validation\n- Filtering strategy evaluation\n\n### 4. REGISTRY FILES\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/registry.yaml` (184 KB) - Comprehensive experiment registry with execution details, metrics, and status\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/dream_registry.yaml` (8.3 KB) - Dream report registry tracking all imagined/simulated reviews\n\n### 5. SUPPLEMENTARY PHASE/TIER DEFINITIONS\n\n**Dream Report Tiers** (best/median/worst) organized by date:\n\n- **dream_20260512T200328** - Route B framing (Route B = K* as first-measured saturation boundary)\n- **dream_20260513T080728** - Full review mode\n- **dream_20260516T073047** - Universality scoping (boundary conditions at 128-token, T=0.7, cross-scorer)\n- **dream_20260518T113009** - Evaluation without arXiv negative results (exp_026 excluded)\n- **dream_20260518T122223** - Failed: With arXiv honest negative (status: failed, pid: null)\n- **dream_20260518T123349** - Failed: With arXiv honest negative (status: failed, pid: null)\n- **dream_20260518T125757** - Current best: With arXiv negative + one-wash laundering concept (status: done, latest symlink)\n- **dream_20260519T090934** - Current: RUNNING/imagining - Code domain cross-model results, focus on 4-domain + 6-architecture coverage\n\n### 6. KEY FINDINGS FOR RUNNING DREAM (dream_20260519T090934)\n\n**Status:** `imagining` (in progress)\n**Focus areas:**\n1. Code domain results: LLaMA-8B K*=2 confirmed (cross-family), Mistral-7B and Qwen-7B Code still RUNNING\n2. Domain hierarchy established: Wiki(K*=1) < C4/Code(K*=2) < arXiv(K*=3)\n3. Retrain chain K*=7 (two families tested)\n4. Key uncertainty: Is 4-domain + 6-architecture coverage sufficient for EMNLP accept?\n5. Concern: C3 filtering weakness (negative results on arXiv/Pythia)\n\n**Files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/dream_registry.yaml` (lines 181-205)\n- No dream_20260519T090934/median folder yet (still in imagine stage)\n\n### 7. SUPPLEMENTARY EXPERIMENT DEFINITIONS EXAMPLE\n\nThe median tier imagined_experiments.yaml files contain detailed supplementary definitions not in the base experiment_plan, including:\n\n- **exp-014 (Naturalistic Common Crawl Validation)** - 10K CC 2025/2026 docs with AlignScore correlation validation\n- **exp-018 (LLaMA-3.1-8B cross-family)** - Expected K*=2, pairwise AUC predictions\n- Expected statistical metrics (bootstrap CI, permutation p-values)\n- Reviewer-specific rationales explaining why each result matters at different tiers\n\n**Example location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T113009/median/imagined_experiments.yaml` (1,000+ lines with full experiment specifications)"
      }
    ],
    "totalDurationMs": 66062,
    "totalTokens": 63681,
    "totalToolUseCount": 41,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1694,
      "cache_read_input_tokens": 60008,
      "output_tokens": 1972,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1972,
          "cache_read_input_tokens": 60008,
          "cache_creation_input_tokens": 1694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1694,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 15,
      "searchCount": 12,
      "bashCount": 14,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "2e20a1a6-75a5-4915-bd64-57a61b2c21aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T09:20:43.723Z_

<details open><summary>🔧 Tool call — Read · `toolu_0134r4rBkfodzGaaCDaqL9Ky`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b00c4ae-ca83-46d8-a033-2a0551fc144b",
  "isSidechain": false,
  "requestId": "req_011CbBgRx9cjZvvyfE6Dy7bF",
  "type": "assistant",
  "uuid": "0a73c26f-8c60-4f03-bdff-d75905526f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WNnCxwrSJZfwbv41Mx8smQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2289,
      "cache_read_input_tokens": 66188,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 121,
          "cache_read_input_tokens": 66188,
          "cache_creation_input_tokens": 2289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2289
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

### Tool result

_source line 12 · 2026-05-19T09:20:43.742Z_

<details><summary>↩ Tool result · `toolu_0134r4rBkfodzGaaCDaqL9Ky`</summary>

```text
1	tier: median
2	narrative_guidance: 'C1'' characterization 被多数 reviewer 接受为 solid empirical work，但
3	  "sole determinant" 措辞遭挑战—— Mistral C4 K*=1 被 1-2 个 reviewer 解读为 model×domain interaction
4	  而非纯 domain effect。 C3 curation validation 证据链被认为太弱：exp-006 effect size 小（MMLU Δ=0.76pp），exp-025/026
5	  是 null results。 θ=0.60 边界选择的 robustness 被质疑（θ=0.70 下 K* 大面积降至 1）。 Qwen-cont CI lower=0.6015
6	  被单独点名要求 sensitivity analysis。 DPI 理论框架被认为 "nice motivation" 但不够深入构成独立贡献。 ≤8B scale
7	  被至少一个 reviewer 标记为 significant weakness。 整体定位：EMNLP Findings 或 conditional accept
8	  after strong rebuttal with 14B/32B evidence。 建议：C1'' 降级为 "primary factor"，C3 降级为
9	  "case study"，θ-sensitivity 升为主文 figure， rebuttal 补充 14B/32B 结果回应 scale concern。
10	
11	  '
12	imagined_experiments:
13	- name: mvp-001
14	  plan_id: mvp_pilot_sat_v1
15	  description: Qwen2.5-1.5B-Instruct rewrite mode pilot, C4 5K docs, depth 0-5
16	  expected_results:
17	    k_star: 2
18	    pairwise_auc_0v1: 0.9956
19	    pairwise_auc_1v2: 0.6957
20	    pairwise_auc_2v3: 0.5893
21	    pairwise_auc_3v4: 0.5434
22	    pairwise_auc_4v5: 0.5343
23	    ordinal_accuracy: 0.4182
24	    ordinal_mae: 1.0163
25	  result_rationale: 'Rewrite mode 因 instruction-following 引入 mode-specific style artifacts，放大
26	    depth signal 至 1v2 AUC=0.6957。 在 median 档下，1-2 个 reviewer 注意到 rewrite mode 的高
27	    AUC 不能代表 canonical condition， 要求论文明确将此实验定位为 "pilot study demonstrating feasibility"。2v3=0.5893
28	    < θ=0.60  确认 K*=2，但 reviewer 指出 rewrite mode 的 signal amplification 使 K*=2 判定比
29	    continuation  更容易，质疑是否该用 rewrite 的高 AUC 作为 headline number。 Median 档 reviewer
30	    接受此实验作为 motivation，但要求所有 cross-model claims 基于 continuation mode。
31	
32	    '
33	  tables:
34	  - name: 'Table 1 (partial): Pairwise AUC — MVP pilot'
35	    content: '| Pair | AUC    | 95% CI           | > θ=0.60? |
36	
37	      |------|--------|------------------|-----------|
38	
39	      | 0v1  | 0.9956 | [0.9946, 0.9965] | ✅ (+39.5pp) |
40	
41	      | 1v2  | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp)  |
42	
43	      | 2v3  | 0.5893 | [0.5795, 0.5991] | ❌           |
44	
45	      | 3v4  | 0.5434 | [0.5333, 0.5551] | ❌           |
46	
47	      | 4v5  | 0.5343 | [0.5238, 0.5448] | ❌           |
48	
49	      '
50	  figures_description:
51	  - AUC decay curve (rewrite mode) — 用于 Introduction 或 §3 motivation figure，展示 sharp
52	    K*=2 boundary
53	  analysis: 'Reviewer A 接受 rewrite mode 作为 pilot 合理。Reviewer B 质疑为何论文早期版本以 rewrite
54	    AUC  (0.6957) 为 headline 而非 continuation (0.6114)——存在 cherry-picking 嫌疑。 Median
55	    档下需在论文中明确标注 mvp-001 为 pilot，所有 figure 和 headline number 基于 continuation mode。
56	
57	    '
58	- name: exp-001
59	  plan_id: exp_001_pythia_depth
60	  description: Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5
61	  expected_results:
62	    k_star: 2
63	    pairwise_auc_0v1: 0.9932
64	    pairwise_auc_1v2: 0.6539
65	    pairwise_auc_2v3: 0.5515
66	    pairwise_auc_3v4: 0.5153
67	    pairwise_auc_4v5: 0.5135
68	    ci_1v2_lower: 0.6454
69	    ci_1v2_upper: 0.663
70	    ordinal_accuracy: 0.383
71	    ordinal_mae: 1.14
72	  result_rationale: 'Pythia-1.4B 作为第一个 continuation mode 跨模型验证，1v2 AUC=0.6539 距 θ=0.60
73	    有 +4.5pp 余量， 是 C4 web text 上 K*=2 的稳健证据。2v3 AUC=0.5515 远低于 θ，sharp boundary 明确。
74	    在 median 档下，reviewer 接受 Pythia 的 K*=2 判定没有争议（CI lower=0.6454 >> 0.60）， 但指出 Pythia-1.4B
75	    作为较老架构，代表性受限——单独一个模型不足以 claim universality。 Reviewer 认为此结果 "expected given information-theoretic
76	    intuition"（A1 假设）， 递归生成必然快速退化是直觉上合理的，K*=2 不算 surprising。
77	
78	    '
79	  tables:
80	  - name: 'Table 2 (row): Pythia-1.4B C4 continuation'
81	    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
82	
83	      |-------|------|------|------|------|------|----|
84	
85	      | Pythia-1.4B | 0.993 | 0.654 | 0.552 | 0.515 | 0.514 | 2 |
86	
87	      '
88	  figures_description:
89	  - Pairwise AUC heatmap 中的一行，展示 sharp 0v1→1v2 drop 和 2v3+ plateau
90	  analysis: '稳健但不 exciting。Median 档 reviewer 视为 "solid but incremental evidence for
91	    a somewhat  expected finding"。Pythia 的较高 1v2 AUC (vs Qwen-cont 0.6112) 减少了 borderline
92	    concern， 但也没有超出 reviewer 的信息论直觉预期。
93	
94	    '
95	- name: exp-002
96	  plan_id: exp_002_olmo_depth
97	  description: OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5
98	  expected_results:
99	    k_star: 2
100	    pairwise_auc_0v1: 0.997
101	    pairwise_auc_1v2: 0.6146
102	    pairwise_auc_2v3: 0.5497
103	    pairwise_auc_3v4: 0.509
104	    pairwise_auc_4v5: 0.5044
105	    ci_1v2_lower: 0.6045
106	    ci_1v2_upper: 0.6247
107	    ordinal_accuracy: 0.3685
108	    ordinal_mae: 1.1813
109	  result_rationale: 'OLMo-1B 1v2 AUC=0.6146，CI lower=0.6045，余量 +0.45pp。比 Pythia 更边缘但仍
110	    pass。 Median 档下 reviewer 注意到 OLMo 的 CI lower 只比 θ 高 0.45pp，但未被单独点名 （Qwen-cont
111	    的 0.6015 更 marginal 所以吸引了注意力）。 OLMo 1v2=0.6146 和 Pythia 1v2=0.6539 的差异暗示 model
112	    确实对 signal strength 有影响， 但两者 K* 一致=2，支持 "domain is primary determinant" 的 claim。
113	    Reviewer 接受 Pythia↔OLMo 的一致性但指出只有两个 continuation mode 模型在此阶段不够。
114	
115	    '
116	  tables:
117	  - name: 'Table 2 (row): OLMo-1B C4 continuation'
118	    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
119	
120	      |-------|------|------|------|------|------|----|
121	
122	      | OLMo-1B | 0.997 | 0.615 | 0.550 | 0.509 | 0.504 | 2 |
123	
124	      '
125	  figures_description:
126	  - Pairwise AUC heatmap 中的一行
127	  analysis: '与 Pythia 一致，增强跨模型证据。OLMo 3v4/4v5 接近 0.50 (chance)， 进一步确认 depth ≥3 后信号完全消失。Reviewer
128	    不质疑此具体结果。
129	
130	    '
131	- name: exp-003
132	  plan_id: exp_003_decoding_ablation
133	  description: 'Qwen2.5-1.5B decoding strategy ablation: greedy / nucleus p=0.9 /
134	    T=0.7 / T=1.2'
135	  expected_results:
136	    k_star: 2
137	    k_star_robust: true
138	    greedy_1v2_auc: 0.6892
139	    nuc09_1v2_auc: 0.6862
140	    t07_1v2_auc: 0.6885
141	    t12_1v2_auc: 0.7037
142	    auc_1v2_range: '[0.6862, 0.7037]'
143	    all_k_star_2: true
144	    nuc09_2v3_ci_upper: 0.601
145	  result_rationale: '四种解码策略下 K* 完全一致=2，AUC range < 2pp。这是 median 档下 reviewer 较认可的证据——
146	    解码策略不变性消除了 "K*=2 是特定 sampling 参数的 artifact" 的质疑。 但 nuc09 2v3 CI upper=0.601 接触
147	    θ=0.60 边界，被注意但未被重点攻击（因为是 CI upper 而非 lower）。 Reviewer 注意到此实验仅在 Qwen rewrite mode
148	    上做（后 exp-020 在 Pythia 上复制）， rewrite mode 的 higher baseline signal 使 K*=2 更容易 robust，
149	    需要 continuation mode 上同样的 ablation 来增强说服力。
150	
151	    '
152	  tables:
153	  - name: 'Table 3: Decoding strategy ablation'
154	    content: '| Decoding | 0v1 AUC | 1v2 AUC | 2v3 AUC | K* |
155	
156	      |----------|---------|---------|---------|-----|
157	
158	      | greedy   | 0.9796  | 0.6892  | 0.5612  | 2   |
159	
160	      | nucleus p=0.9 | 0.9945 | 0.6862 | 0.5917 | 2 |
161	
162	      | T=0.7    | 0.9877  | 0.6885  | 0.5901  | 2   |
163	
164	      | T=1.2    | 0.9982  | 0.7037  | 0.5820  | 2   |
165	
166	      '
167	  figures_description:
168	  - Bar chart showing K* invariance across decoding strategies, 用于 §4 主文
169	  analysis: 'Decoding invariance 是 C1'' 的重要支柱。Median 档 reviewer 接受此结论但权重较低 （"somewhat
170	    expected — decoding shouldn''t change fundamental information loss"）。 exp-020
171	    在 Pythia continuation 上的 replication 增强了此证据。
172	
173	    '
174	- name: exp-004
175	  plan_id: exp_004_7b_crossscale
176	  description: Qwen2.5-7B, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B
177	  expected_results:
178	    k_star: 2
179	    pairwise_auc_1v2: 0.6178
180	    ci_1v2_lower: 0.6079
181	    ci_1v2_upper: 0.6261
182	    pairwise_auc_2v3: 0.546
183	    ci_2v3_upper: 0.5594
184	    pairwise_auc_4v5_perm_p: 0.0676
185	  result_rationale: '7B scale 下 K*=2 与 1.5B 一致，CI lower=0.6079 > θ（余量 +0.79pp）。 在
186	    median 档下，reviewer 接受 1.5B→7B 的 scale invariance 但力度不足： (a) 只从 1.5B 到 7B 不算大幅
187	    scale-up；(b) A3 假设被触发——至少一个 reviewer  标记 "≤8B is a significant limitation, need
188	    13B+ evidence"。 4v5 pair p=0.0676 non-significant，被 reviewer 视为 "depth ≥4 信号消失的进一步证据"，
189	    有利于 K*=2 的 claim。但 reviewer 质疑：如果更大模型（70B）生成更高质量文本， K* 可能增加——作者需要 theoretically
190	    argue 或 empirically show 这一点。
191	
192	    '
193	  tables:
194	  - name: 'Table 2 (row): Qwen2.5-7B C4 continuation'
195	    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
196	
197	      |-------|------|------|------|------|------|----|
198	
199	      | Qwen2.5-7B | 0.964 | 0.618 | 0.546 | 0.523 | 0.509 | 2 |
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a73c26f-8c60-4f03-bdff-d75905526f72",
  "isSidechain": false,
  "promptId": "59587622-660c-4957-a549-a3c2036a769c",
  "type": "user",
  "uuid": "23ad6189-0e79-4df8-9dcf-8e110d540a3f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
      "content": "tier: median\nnarrative_guidance: 'C1'' characterization 被多数 reviewer 接受为 solid empirical work，但\n  \"sole determinant\" 措辞遭挑战—— Mistral C4 K*=1 被 1-2 个 reviewer 解读为 model×domain interaction\n  而非纯 domain effect。 C3 curation validation 证据链被认为太弱：exp-006 effect size 小（MMLU Δ=0.76pp），exp-025/026\n  是 null results。 θ=0.60 边界选择的 robustness 被质疑（θ=0.70 下 K* 大面积降至 1）。 Qwen-cont CI lower=0.6015\n  被单独点名要求 sensitivity analysis。 DPI 理论框架被认为 \"nice motivation\" 但不够深入构成独立贡献。 ≤8B scale\n  被至少一个 reviewer 标记为 significant weakness。 整体定位：EMNLP Findings 或 conditional accept\n  after strong rebuttal with 14B/32B evidence。 建议：C1'' 降级为 \"primary factor\"，C3 降级为\n  \"case study\"，θ-sensitivity 升为主文 figure， rebuttal 补充 14B/32B 结果回应 scale concern。\n\n  '\nimagined_experiments:\n- name: mvp-001\n  plan_id: mvp_pilot_sat_v1\n  description: Qwen2.5-1.5B-Instruct rewrite mode pilot, C4 5K docs, depth 0-5\n  expected_results:\n    k_star: 2\n    pairwise_auc_0v1: 0.9956\n    pairwise_auc_1v2: 0.6957\n    pairwise_auc_2v3: 0.5893\n    pairwise_auc_3v4: 0.5434\n    pairwise_auc_4v5: 0.5343\n    ordinal_accuracy: 0.4182\n    ordinal_mae: 1.0163\n  result_rationale: 'Rewrite mode 因 instruction-following 引入 mode-specific style artifacts，放大\n    depth signal 至 1v2 AUC=0.6957。 在 median 档下，1-2 个 reviewer 注意到 rewrite mode 的高\n    AUC 不能代表 canonical condition， 要求论文明确将此实验定位为 \"pilot study demonstrating feasibility\"。2v3=0.5893\n    < θ=0.60  确认 K*=2，但 reviewer 指出 rewrite mode 的 signal amplification 使 K*=2 判定比\n    continuation  更容易，质疑是否该用 rewrite 的高 AUC 作为 headline number。 Median 档 reviewer\n    接受此实验作为 motivation，但要求所有 cross-model claims 基于 continuation mode。\n\n    '\n  tables:\n  - name: 'Table 1 (partial): Pairwise AUC — MVP pilot'\n    content: '| Pair | AUC    | 95% CI           | > θ=0.60? |\n\n      |------|--------|------------------|-----------|\n\n      | 0v1  | 0.9956 | [0.9946, 0.9965] | ✅ (+39.5pp) |\n\n      | 1v2  | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp)  |\n\n      | 2v3  | 0.5893 | [0.5795, 0.5991] | ❌           |\n\n      | 3v4  | 0.5434 | [0.5333, 0.5551] | ❌           |\n\n      | 4v5  | 0.5343 | [0.5238, 0.5448] | ❌           |\n\n      '\n  figures_description:\n  - AUC decay curve (rewrite mode) — 用于 Introduction 或 §3 motivation figure，展示 sharp\n    K*=2 boundary\n  analysis: 'Reviewer A 接受 rewrite mode 作为 pilot 合理。Reviewer B 质疑为何论文早期版本以 rewrite\n    AUC  (0.6957) 为 headline 而非 continuation (0.6114)——存在 cherry-picking 嫌疑。 Median\n    档下需在论文中明确标注 mvp-001 为 pilot，所有 figure 和 headline number 基于 continuation mode。\n\n    '\n- name: exp-001\n  plan_id: exp_001_pythia_depth\n  description: Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\n  expected_results:\n    k_star: 2\n    pairwise_auc_0v1: 0.9932\n    pairwise_auc_1v2: 0.6539\n    pairwise_auc_2v3: 0.5515\n    pairwise_auc_3v4: 0.5153\n    pairwise_auc_4v5: 0.5135\n    ci_1v2_lower: 0.6454\n    ci_1v2_upper: 0.663\n    ordinal_accuracy: 0.383\n    ordinal_mae: 1.14\n  result_rationale: 'Pythia-1.4B 作为第一个 continuation mode 跨模型验证，1v2 AUC=0.6539 距 θ=0.60\n    有 +4.5pp 余量， 是 C4 web text 上 K*=2 的稳健证据。2v3 AUC=0.5515 远低于 θ，sharp boundary 明确。\n    在 median 档下，reviewer 接受 Pythia 的 K*=2 判定没有争议（CI lower=0.6454 >> 0.60）， 但指出 Pythia-1.4B\n    作为较老架构，代表性受限——单独一个模型不足以 claim universality。 Reviewer 认为此结果 \"expected given information-theoretic\n    intuition\"（A1 假设）， 递归生成必然快速退化是直觉上合理的，K*=2 不算 surprising。\n\n    '\n  tables:\n  - name: 'Table 2 (row): Pythia-1.4B C4 continuation'\n    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |\n\n      |-------|------|------|------|------|------|----|\n\n      | Pythia-1.4B | 0.993 | 0.654 | 0.552 | 0.515 | 0.514 | 2 |\n\n      '\n  figures_description:\n  - Pairwise AUC heatmap 中的一行，展示 sharp 0v1→1v2 drop 和 2v3+ plateau\n  analysis: '稳健但不 exciting。Median 档 reviewer 视为 \"solid but incremental evidence for\n    a somewhat  expected finding\"。Pythia 的较高 1v2 AUC (vs Qwen-cont 0.6112) 减少了 borderline\n    concern， 但也没有超出 reviewer 的信息论直觉预期。\n\n    '\n- name: exp-002\n  plan_id: exp_002_olmo_depth\n  description: OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5\n  expected_results:\n    k_star: 2\n    pairwise_auc_0v1: 0.997\n    pairwise_auc_1v2: 0.6146\n    pairwise_auc_2v3: 0.5497\n    pairwise_auc_3v4: 0.509\n    pairwise_auc_4v5: 0.5044\n    ci_1v2_lower: 0.6045\n    ci_1v2_upper: 0.6247\n    ordinal_accuracy: 0.3685\n    ordinal_mae: 1.1813\n  result_rationale: 'OLMo-1B 1v2 AUC=0.6146，CI lower=0.6045，余量 +0.45pp。比 Pythia 更边缘但仍\n    pass。 Median 档下 reviewer 注意到 OLMo 的 CI lower 只比 θ 高 0.45pp，但未被单独点名 （Qwen-cont\n    的 0.6015 更 marginal 所以吸引了注意力）。 OLMo 1v2=0.6146 和 Pythia 1v2=0.6539 的差异暗示 model\n    确实对 signal strength 有影响， 但两者 K* 一致=2，支持 \"domain is primary determinant\" 的 claim。\n    Reviewer 接受 Pythia↔OLMo 的一致性但指出只有两个 continuation mode 模型在此阶段不够。\n\n    '\n  tables:\n  - name: 'Table 2 (row): OLMo-1B C4 continuation'\n    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |\n\n      |-------|------|------|------|------|------|----|\n\n      | OLMo-1B | 0.997 | 0.615 | 0.550 | 0.509 | 0.504 | 2 |\n\n      '\n  figures_description:\n  - Pairwise AUC heatmap 中的一行\n  analysis: '与 Pythia 一致，增强跨模型证据。OLMo 3v4/4v5 接近 0.50 (chance)， 进一步确认 depth ≥3 后信号完全消失。Reviewer\n    不质疑此具体结果。\n\n    '\n- name: exp-003\n  plan_id: exp_003_decoding_ablation\n  description: 'Qwen2.5-1.5B decoding strategy ablation: greedy / nucleus p=0.9 /\n    T=0.7 / T=1.2'\n  expected_results:\n    k_star: 2\n    k_star_robust: true\n    greedy_1v2_auc: 0.6892\n    nuc09_1v2_auc: 0.6862\n    t07_1v2_auc: 0.6885\n    t12_1v2_auc: 0.7037\n    auc_1v2_range: '[0.6862, 0.7037]'\n    all_k_star_2: true\n    nuc09_2v3_ci_upper: 0.601\n  result_rationale: '四种解码策略下 K* 完全一致=2，AUC range < 2pp。这是 median 档下 reviewer 较认可的证据——\n    解码策略不变性消除了 \"K*=2 是特定 sampling 参数的 artifact\" 的质疑。 但 nuc09 2v3 CI upper=0.601 接触\n    θ=0.60 边界，被注意但未被重点攻击（因为是 CI upper 而非 lower）。 Reviewer 注意到此实验仅在 Qwen rewrite mode\n    上做（后 exp-020 在 Pythia 上复制）， rewrite mode 的 higher baseline signal 使 K*=2 更容易 robust，\n    需要 continuation mode 上同样的 ablation 来增强说服力。\n\n    '\n  tables:\n  - name: 'Table 3: Decoding strategy ablation'\n    content: '| Decoding | 0v1 AUC | 1v2 AUC | 2v3 AUC | K* |\n\n      |----------|---------|---------|---------|-----|\n\n      | greedy   | 0.9796  | 0.6892  | 0.5612  | 2   |\n\n      | nucleus p=0.9 | 0.9945 | 0.6862 | 0.5917 | 2 |\n\n      | T=0.7    | 0.9877  | 0.6885  | 0.5901  | 2   |\n\n      | T=1.2    | 0.9982  | 0.7037  | 0.5820  | 2   |\n\n      '\n  figures_description:\n  - Bar chart showing K* invariance across decoding strategies, 用于 §4 主文\n  analysis: 'Decoding invariance 是 C1'' 的重要支柱。Median 档 reviewer 接受此结论但权重较低 （\"somewhat\n    expected — decoding shouldn''t change fundamental information loss\"）。 exp-020\n    在 Pythia continuation 上的 replication 增强了此证据。\n\n    '\n- name: exp-004\n  plan_id: exp_004_7b_crossscale\n  description: Qwen2.5-7B, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B\n  expected_results:\n    k_star: 2\n    pairwise_auc_1v2: 0.6178\n    ci_1v2_lower: 0.6079\n    ci_1v2_upper: 0.6261\n    pairwise_auc_2v3: 0.546\n    ci_2v3_upper: 0.5594\n    pairwise_auc_4v5_perm_p: 0.0676\n  result_rationale: '7B scale 下 K*=2 与 1.5B 一致，CI lower=0.6079 > θ（余量 +0.79pp）。 在\n    median 档下，reviewer 接受 1.5B→7B 的 scale invariance 但力度不足： (a) 只从 1.5B 到 7B 不算大幅\n    scale-up；(b) A3 假设被触发——至少一个 reviewer  标记 \"≤8B is a significant limitation, need\n    13B+ evidence\"。 4v5 pair p=0.0676 non-significant，被 reviewer 视为 \"depth ≥4 信号消失的进一步证据\"，\n    有利于 K*=2 的 claim。但 reviewer 质疑：如果更大模型（70B）生成更高质量文本， K* 可能增加——作者需要 theoretically\n    argue 或 empirically show 这一点。\n\n    '\n  tables:\n  - name: 'Table 2 (row): Qwen2.5-7B C4 continuation'\n    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |\n\n      |-------|------|------|------|------|------|----|\n\n      | Qwen2.5-7B | 0.964 | 0.618 | 0.546 | 0.523 | 0.509 | 2 |\n",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 1260
    }
  },
  "sourceToolAssistantUUID": "0a73c26f-8c60-4f03-bdff-d75905526f72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-19T09:20:43.779Z_

````json
{
  "parentUuid": "23ad6189-0e79-4df8-9dcf-8e110d540a3f",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**gen-depth-contamination**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"gen-depth-contamination\")` 或 `load_project_config(\"gen-depth-contamination\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n\n### 写作规则\n\n- **[项目]** 正文写作中，除了一些专有名词（比如说一些模型的名称）之外，在正常行文中不要出现破折号。\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/gen-depth-contamination/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "74b90e0e-8710-4a57-83db-92d1e4884b9b",
  "timestamp": "2026-05-19T09:20:43.779Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑 核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domai…",
  "leafUuid": "74b90e0e-8710-4a57-83db-92d1e4884b9b",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-dependent K* saturation with cross-model validation",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Tool call

_source line 16 · 2026-05-19T09:20:52.322Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F98L3WVpxvc57GKQcwVgds`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
  "offset": 200,
  "limit": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74b90e0e-8710-4a57-83db-92d1e4884b9b",
  "isSidechain": false,
  "requestId": "req_011CbBgSYg1ny67NEvyaF6nZ",
  "type": "assistant",
  "uuid": "d5c70234-b9ce-4e87-9329-4d8d65c427c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFuq4LhhVifMzKgHaJuyXX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11229,
      "cache_read_input_tokens": 68477,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 68477,
          "cache_creation_input_tokens": 11229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11229
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

### Tool result

_source line 17 · 2026-05-19T09:20:52.825Z_

<details><summary>↩ Tool result · `toolu_01F98L3WVpxvc57GKQcwVgds`</summary>

```text
200	
201	      '
202	  figures_description:
203	  - 'Scale comparison subplot: 1.5B vs 7B pairwise AUC curves overlapping'
204	  analysis: 'Scale invariance (1.5B→7B) 被 1 个 reviewer 认为是 "weak evidence for scale
205	    generalization"。 Rebuttal 需要 14B/32B 数据。exp_14b_c4 (K*=2) 已可用但 exp_32b_c4 仍在跑。
206	    如果 32B 也给 K*=2，可在 rebuttal 中有效回应 A3。
207	
208	    '
209	- name: exp-005
210	  plan_id: exp_005_degradation
211	  description: Feature group ablation + degradation ordering analysis
212	  expected_results:
213	    cross_model_spearman_rho_pythia_olmo: 0.95
214	    cross_model_spearman_rho_pythia_qwen_cont: 0.9143
215	    cross_model_spearman_rho_olmo_qwen_cont: 0.85
216	    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std
217	    1v2_tau_weakness: ~0.37
218	  result_rationale: 'Feature ordering 跨模型高度一致（ρ≥0.85），支持 depth signal 是 text-intrinsic
219	    而非 model-specific。 Median 档下 reviewer 接受 feature ranking consistency 但不视为独立贡献——
220	    "Feature analysis is supportive but expected if the underlying signal is text-intrinsic."
221	    1v2 pair 的 feature importance 一致性最弱（τ~0.37），被 reviewer 注意但不重点攻击 （因为这恰好是 boundary
222	    pair，信号最微弱处 variance 大是合理的）。 Surprisal-based features 主导的发现与 DPI 理论一致，被 reviewer
223	    视为 "expected alignment"。
224	
225	    '
226	  tables:
227	  - name: 'Table A2: Cross-model feature ranking Spearman ρ'
228	    content: '| Model Pair | Spearman ρ |
229	
230	      |------------|-----------|
231	
232	      | Pythia ↔ OLMo | 0.950 |
233	
234	      | Pythia ↔ Qwen-cont | 0.914 |
235	
236	      | OLMo ↔ Qwen-cont | 0.850 |
237	
238	      '
239	  figures_description:
240	  - Feature importance heatmap across models — 放 Appendix
241	  analysis: 'Supporting evidence for text-intrinsic signal。不构成独立卖点但消除 "model self-familiarity"
242	    质疑。 Median 档下这个实验的贡献被 reviewer 归入 "thorough analysis" 而非 novel finding。
243	
244	    '
245	- name: exp-006
246	  plan_id: exp_006_graduated_filtering
247	  description: 'Downstream filtering evaluation: 6 strategies × 5 seeds, MMLU + HellaSwag'
248	  expected_results:
249	    binary_ours_mmlu: 0.5941±0.0008
250	    binary_ours_hellaswag: 0.6701±0.0006
251	    no_filter_mmlu: 0.5865±0.0010
252	    no_filter_hellaswag: 0.6638±0.0008
253	    delta_mmlu_binary_vs_nofilter: '+0.0076'
254	    delta_hellaswag_binary_vs_nofilter: '+0.0063'
255	    base_model_mmlu: 0.6018
256	    graduated_a09_mmlu: 0.5892±0.0008
257	    dsir_mmlu: 0.5869±0.0003
258	  result_rationale: 'Binary-ours 在所有策略中最优，但 MMLU 增益仅 +0.76pp vs no-filter。 在 median
259	    档下，这是 C3 的核心弱点（A5_fail）： (a) MMLU Δ=0.76pp 被 reviewer 质疑 practical significance——"Is
260	    <1pp improvement  worth the curation complexity?" (b) 所有策略都 degrade vs base_model（0.6018→0.5941），说明
261	    contaminated data 的  fundamental harm 无法被 filtering 完全消除 (c) Graduated α 单调递增确认
262	    K*=2 boundary，但 reviewer 指出这是 circular reasoning—— 用 K* 设计 filtering 然后用 filtering
263	    验证 K* (d) DSIR 表现差（接近 no-filter）是一个正面结果，但 reviewer 质疑 DSIR baseline  的公平性（DSIR
264	    不是为 depth-aware filtering 设计的）
265	
266	    '
267	  tables:
268	  - name: 'Table 5: Filtering strategy comparison (Qwen2.5-1.5B, 30% contamination)'
269	    content: '| Strategy | MMLU | HellaSwag | Δ MMLU vs no-filter |
270	
271	      |----------|------|-----------|-------------------|
272	
273	      | binary-ours | 0.5941±0.0008 | 0.6701±0.0006 | +0.0076* |
274	
275	      | binary-Drayson | 0.5913±0.0009 | 0.6691±0.0004 | +0.0048* |
276	
277	      | surprisal | 0.5894±0.0009 | 0.6641±0.0006 | +0.0029 |
278	
279	      | graduated α=0.9 | 0.5892±0.0008 | 0.6701±0.0007 | +0.0027 |
280	
281	      | DSIR | 0.5869±0.0003 | 0.6631±0.0007 | +0.0004 |
282	
283	      | no-filter | 0.5865±0.0010 | 0.6638±0.0008 | — |
284	
285	      | base (no contam.) | 0.6018 | 0.6821 | — |
286	
287	      '
288	  figures_description:
289	  - 'Bar chart: filtering strategies ranked by MMLU, with base_model reference line'
290	  - 'α sensitivity curve: graduated filtering MMLU as function of α'
291	  analysis: 'Median 档 reviewer 给 C3 的 substance score ~2.5-3.0。核心攻击点： 1. Effect size
292	    太小（<1pp MMLU）不够 actionable 2. Binary > graduated 说明 K* boundary 信息对 curation 有用，但增益微小
293	    3. 所有策略 degrade vs base_model 暗示 filtering 的 ceiling 低 C3 需要从 "validation" 降级为
294	    "case study / demonstration"。
295	
296	    '
297	- name: exp-007
298	  plan_id: exp_007_bootstrap_ci
299	  description: K* sensitivity at θ=0.55/0.60/0.65/0.70 + bootstrap CI + permutation
300	    test
301	  expected_results:
302	    all_1v2_ci_lower_above_060: true
303	    most_marginal: Qwen-cont CI lower=0.6015
304	    theta_055_k_star_distribution: all models K*=2 or K*=3
305	    theta_060_k_star_distribution: 7/8 K*=2, 1/8 K*=1 (Mistral)
306	    theta_065_k_star_distribution: 4-5/8 K*=2, rest K*=1
307	    theta_070_k_star_distribution: most K*=1
308	  result_rationale: 'θ-sensitivity 是 median 档的关键攻击面（A6_partial）。 θ=0.60 下 7/8 configurations
309	    K*=2 被接受，但 θ=0.70 下多数降至 K*=1 被 reviewer 放大—— "The finding is highly sensitive
310	    to threshold choice. At θ=0.70, the headline result  (K*=2 as dominant mode) collapses."
311	    Qwen-cont CI lower=0.6015 被 A8_attacked 假设触发——reviewer 要求 sensitivity analysis  或额外
312	    seeds 来确认这不是 noise。 论文需要在主文（非 appendix）展示 θ-sensitivity figure，正面呈现 K* 在 [0.55,
313	    0.65]  范围内的稳定性，并以 Cohen''s h=0.20 和 AUC gap discontinuity 为 θ=0.60 选择辩护。 Permutation
314	    test p<0.001 对所有 boundary pairs 提供统计支持，但 reviewer 指出  "statistical significance
315	    ≠ practical significance at these effect sizes"。
316	
317	    '
318	  tables:
319	  - name: 'Table 4: K* sensitivity to threshold θ'
320	    content: '| θ | K*=1 | K*=2 | K*=3 |
321	
322	      |------|------|------|------|
323	
324	      | 0.55 | 0/8  | 7/8  | 1/8  |
325	
326	      | 0.60 | 1/8  | 7/8  | 0/8  |
327	
328	      | 0.65 | 3-4/8 | 4-5/8 | 0/8 |
329	
330	      | 0.70 | 6-7/8 | 1-2/8 | 0/8 |
331	
332	      '
333	  figures_description:
334	  - '主文 Figure: θ-sensitivity heatmap，showing K* stability in [0.55, 0.65]'
335	  - AUC gap discontinuity plot at K* boundary pair
336	  analysis: 'θ-sensitivity 被 median 档 reviewer 视为 "fair analysis" 但 robustness concern
337	    未完全消除。 关键辩护：θ=0.60 对应 Cohen''s h≈0.20（small effect size threshold）， 且 1v2 vs 2v3
338	    的 AUC gap 远大于 θ 选择的 sensitivity range。 Reviewer 接受 [0.55, 0.65] 稳定性但仍认为 "the result
339	    is more about where you draw the line  than about the underlying phenomenon"。
340	
341	    '
342	- name: exp-008
343	  plan_id: exp_008_retrain_chain_v2
344	  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA, C4 5K docs, depth
345	    0-4'
346	  expected_results:
347	    k_star: '>=4'
348	    pairwise_auc_0v1: 0.9847
349	    pairwise_auc_1v2: 0.9484
350	    pairwise_auc_2v3: 0.8888
351	    pairwise_auc_3v4: 0.7982
352	  result_rationale: 'Retrain-chain K*≥4 与 prompt-chain K*=2 的对比是重要的 ecological validity
353	    argument。 LoRA fine-tune 每代引入 cumulative model artifacts（vocabulary narrowing,
354	    repetition bias）， 使各代高度可区分。Median 档下 reviewer 接受 "prompt-chain isolates text-intrinsic
355	    degradation"  的论点，但 1 个 reviewer 认为这说明 "in practice, retrain-chain contamination
356	    is more  detectable, so K*=2 underestimates real-world detectability"——这实际上对论文有利
357	    （prompt-chain K*=2 是 conservative estimate），但 reviewer 的 framing 是  "the paper
358	    should discuss this more prominently"。 3v4 AUC=0.7982 远超 θ=0.60，所有 pairs 在 retrain-chain
359	    下都高度可区分， 证明 K* 的低有界性是 prompt-chain (text-intrinsic) 特有的。
360	
361	    '
362	  tables:
363	  - name: 'Table 6: Prompt-chain vs Retrain-chain comparison'
364	    content: '| Pair | Prompt-chain AUC | Retrain-chain AUC |
365	
366	      |------|-----------------|-------------------|
367	
368	      | 0v1  | 0.993 | 0.985 |
369	
370	      | 1v2  | 0.654 | 0.948 |
371	
372	      | 2v3  | 0.552 | 0.889 |
373	
374	      | 3v4  | 0.515 | 0.798 |
375	
376	      '
377	  figures_description:
378	  - 'Dual-panel AUC decay: prompt-chain (sharp drop) vs retrain-chain (gradual decay)'
379	  analysis: '强有力的 supporting evidence。Median 档 reviewer 肯定此实验的 ecological validity
380	    贡献， 但建议正文讨论 "real-world contamination likely falls between prompt-chain and retrain-chain"。
381	
382	    '
383	- name: exp-009
384	  plan_id: exp_009_dose_50pct
385	  description: 'Contamination dose-response: 10%/30%/50% ratio × 3 strategies × 5
386	    seeds'
387	  expected_results:
388	    binary_consistently_best: true
389	    graduated_equals_no_filter: true
390	    hellaswag_binary_significant_all_ratios: true
391	    mmlu_binary_30pct_p: 0.074
392	    effect_size_increases_with_contamination: true
393	  result_rationale: 'Dose-response 确认 binary filtering 在所有 contamination ratio 下一致最优，
394	    graduated filtering 在每个 ratio 下都崩溃至 no-filter 水平。 在 median 档下： (a) HellaSwag 显著性是正面证据（p≤0.004
395	    at all ratios） (b) MMLU 在 30% ratio 下 p=0.074 不显著——reviewer 注意到 "inconsistent
396	    significance  across benchmarks weakens the claim"（A5_fail 部分触发） (c) Effect size
397	    随 contamination ratio 增加（10%: +0.38pp, 30%: +0.61pp, 50%: +0.51pp HellaSwag），
398	    但绝对值仍然小 (d) 一个 reviewer 肯定 dose-response 设计的 thoroughness，但另一个认为  "50% synthetic
399	    injection is unrealistic for current web data"
400	
401	    '
402	  tables:
403	  - name: 'Table 7: Dose-response analysis'
404	    content: '| Ratio | Strategy | MMLU | HellaSwag |
405	
406	      |-------|----------|------|-----------|
407	
408	      | 10% | binary | 0.6079 | 0.6727** |
409	
410	      | 10% | graduated | 0.6066 | 0.6700 |
411	
412	      | 10% | no-filter | 0.6058 | 0.6689 |
413	
414	      | 30% | binary | 0.6082 | 0.6725** |
415	
416	      | 30% | graduated | 0.6072 | 0.6665 |
417	
418	      | 30% | no-filter | 0.6069 | 0.6664 |
419	
420	      | 50% | binary | 0.6088 | 0.6731** |
421	
422	      | 50% | graduated | 0.6062 | 0.6679 |
423	
424	      | 50% | no-filter | 0.6063 | 0.6680 |
425	
426	      '
427	  figures_description:
428	  - 'Line plot: HellaSwag as function of contamination ratio, 3 strategies, with significance
429	    markers'
430	  analysis: 'Binary filtering 的 dose-response consistency 是 C3 的最强证据。 但 graduated=no-filter
431	    的一致性同时说明 K*-aware graduated curation 无增量价值—— 这直接削弱了 "K* informs curation granularity"
432	    的 narrative。 Median 档下 C3 的 reviewer 评分因此在 2.5-3.0 区间。
433	
434	    '
435	- name: exp-010
436	  plan_id: exp_010_ordinal_baseline
437	  description: CORAL vs multiclass LightGBM vs ordinal logistic regression
438	  expected_results:
439	    obd_lgbm_best_accuracy: 0.4229
440	    multiclass_lgbm_accuracy: 0.4182
441	    ordinal_logreg_best_tau: 0.563
442	    obd_lgbm_best_mae: 0.9836
443	  result_rationale: 'OBD-LightGBM 在 accuracy 和 mean_pw_auc 上略优于 multiclass LightGBM，
444	    但差异小（Δacc < 0.5pp）。Ordinal logistic regression MAE 最低但 accuracy 最差。 Median 档下
445	    reviewer 不特别关注此实验——它是 methodology 的 supporting evidence， 不构成独立卖点。Reviewer 认为 "the
446	    choice between ordinal and multiclass classifiers  is an implementation detail,
447	    not a contribution"。 但 ordinal structure 的存在（CORAL MAE < multiclass MAE across
448	    all models） 为论文的 "depth is ordinal, not categorical" framing 提供小幅支持。
449	
450	    '
451	  tables:
452	  - name: 'Table A3: Classifier comparison'
453	    content: '| Method | Acc | MAE | τ_b | Mean PW-AUC |
454	
455	      |--------|-----|-----|-----|-------------|
456	
457	      | OBD-LightGBM | 0.423 | 0.984 | 0.552 | 0.621 |
458	
459	      | Multiclass-LightGBM | 0.418 | 1.016 | 0.537 | 0.625 |
460	
461	      | Ordinal LogReg | 0.364 | 0.911 | 0.563 | 0.502 |
462	
463	      '
464	  figures_description: []
465	  analysis: 'Appendix material。Median 档 reviewer 不质疑也不 highlight。
466	
467	    '
468	- name: exp-011
469	  plan_id: exp_011_llm_zeroshot
470	  description: GPT-5.5 / Claude Opus 4.6 zero-shot depth estimation baseline
471	  expected_results:
472	    gpt55_5class_acc: 0.332
473	    claude_5class_acc: 0.331
474	    gpt55_binary_acc: 0.878
475	    claude_binary_acc: 0.882
476	    odb_baseline_5class_acc: 0.386
477	  result_rationale: 'Frontier LLMs 在 5-class depth estimation 上表现不如 OBD-LightGBM（33%
478	    vs 39%）， 但 binary detection 高达 88%。这是一个 strong baseline comparison： (a) 证明 depth
479	    estimation 需要 specialized features，不能 "throw LLM at it" (b) Binary detection 高但
480	    fine-grained depth 失败，支持 "binary ≠ depth" 的 claim Median 档下 reviewer 对此实验评价较正面——"Good
481	    to include, demonstrates the problem  is not trivially solvable."但 1 个 reviewer
482	    指出 OBD 也只有 39% accuracy， "both methods are poor at fine-grained depth estimation,
483	    which raises the question  of whether depth estimation beyond K* is even meaningful"。
484	    这实际上对 K* characterization 有利（K* 之后的深度确实无法区分）， 但被 reviewer 解读为对整体 contribution
485	    的 dampener。
486	
487	    '
488	  tables:
489	  - name: 'Table 8: LLM zero-shot vs OBD baseline'
490	    content: '| Method | 5-class Acc | MAE | Binary Acc |
491	
492	      |--------|------------|-----|-----------|
493	
494	      | GPT-5.5 | 0.332 | 1.102 | 0.878 |
495	
496	      | Claude Opus 4.6 | 0.331 | 1.150 | 0.882 |
497	
498	      | OBD-LightGBM | 0.386 | 1.107 | — |
499	
500	      '
501	  figures_description:
502	  - 'Per-depth accuracy heatmap: LLMs vs OBD, showing LLM failure at depth 1-4'
503	  analysis: 'Median 档 reviewer 正面评价此 baseline，但 McNemar test non-significant (p~0.07-0.08)  被注意——"The
504	    advantage of OBD over frontier LLMs is not statistically significant."
505	
506	    '
507	- name: exp-012
508	  plan_id: exp_012_binary_confidence
509	  description: DivEye/Binoculars binary detector confidence as depth proxy
510	  expected_results:
511	    binary_detector_kstar: 1
512	    obd_kstar: 2
513	    spearman_rho_range: 0.06-0.46
514	    auc_non_monotonic: true
515	    six_class_accuracy_max: 0.199
516	  result_rationale: 'Binary detectors K*≈1 vs OBD K*=2，6-class accuracy 接近 random（≤0.199
517	    vs 0.167 random）。 Spearman correlation 弱且非单调。直接支持 "binary confidence ≠ depth"
518	    的 claim。 Median 档下 reviewer 接受此结论——"Well-designed experiment that justifies the
519	    need for  depth-aware features beyond binary detection." 不被特别攻击。 但 reviewer 注意到
520	    DivEye/Binoculars 都是 perplexity-based， 建议加入 watermark-based 或 learned detectors
521	    作为 baseline。论文无此 baseline  被视为 minor weakness 而非 major concern。
522	
523	    '
524	  tables:
525	  - name: 'Table A4: Binary detector depth estimation'
526	    content: '| Generator | 6-class Acc | ρ (ppl_ratio) | AUC monotonic? |
527	
528	      |-----------|------------|--------------|---------------|
529	
530	      | Qwen-rw | 0.199 | 0.119 | ❌ |
531	
532	      | Pythia | 0.130 | -0.392 | ❌ |
533	
534	      | OLMo | 0.127 | -0.407 | ❌ |
535	
536	      | Qwen-cont | 0.183 | -0.058 | ❌ |
537	
538	      '
539	  figures_description:
540	  - 'Scatter plot: binary detector confidence vs true depth, showing non-monotonicity'
541	  analysis: 'Strong justification for the paper''s approach。Median 档下被 reviewer 正面引用。
542	
543	    '
544	- name: exp-013
545	  plan_id: exp_013_cross_transfer
546	  description: 4×4 cross-model transfer matrix
547	  expected_results:
548	    pythia_olmo_retention: 91-92%
549	    qwen_cont_cross_retention: 80-85%
550	    qwen_rw_cross_retention: 61-63%
551	    binary_0v1_cross_all_above_096: true
552	  result_rationale: 'Cross-model transfer 是 C1'' "text-intrinsic signal" 的核心证据。 Pythia↔OLMo
553	    91-92% retention 和 0v1 cross-AUC > 0.96 强力支持 depth signal 跨模型可迁移。 Median 档下 reviewer
554	    正面评价： (a) "The high transfer retention confirms K* is not a self-familiarity artifact"
555	    (b) Qwen-rewrite 低 transfer (61-63%) 进一步区分 generation mode effect vs depth signal
556	    (c) 但 reviewer 指出 "all models are ≤8B from similar training distributions,  transfer
557	    to fundamentally different models (e.g., 70B, multilingual) remains unknown" 这与
558	    A3 (scale limitation) 呼应。
559	
560	    '
561	  tables:
562	  - name: 'Table 9: Cross-model transfer retention'
563	    content: '| Transfer Direction | Accuracy Retention |
564	
565	      |-------------------|-------------------|
566	
567	      | Pythia → OLMo | 92% |
568	
569	      | OLMo → Pythia | 91% |
570	
571	      | Qwen-cont → Pythia | 85% |
572	
573	      | Qwen-cont → OLMo | 80% |
574	
575	      | Qwen-rw → Pythia | 63% |
576	
577	      | Qwen-rw → OLMo | 61% |
578	
579	      '
580	  figures_description:
581	  - 4×4 transfer heatmap in main text
582	  analysis: 'Median 档 reviewer 评价：C1'' 的 strongest supporting evidence 之一。 Transfer
583	    > 80% 在 continuation mode 下消除 scorer bias 质疑。
584	
585	    '
586	- name: exp-014
587	  plan_id: ''
588	  description: 'Naturalistic validation: Common Crawl 2025/2026 snapshot depth prediction'
589	  expected_results:
590	    predicted_depth_distribution:
591	      depth_0: 60-75%
592	      depth_1: 15-25%
593	      depth_2_plus: 5-15%
594	    correlation_with_alignscore: Spearman ρ=0.15-0.30
595	    correlation_with_vocab_richness: Spearman ρ=0.20-0.35
596	    predicted_contamination_rate: 25-40%
597	  result_rationale: 'Naturalistic validation 在 median 档下是 P2 优先级，未执行。 如果执行，预期结果：Common
598	    Crawl 2025/2026 中约 25-40% 文本被预测为 depth ≥1（合成文本）， 与外部估计一致。但 ground truth 缺失使此实验无法做定量验证——
599	    只能做 correlation with proxy metrics。AlignScore correlation 弱（ρ~0.15-0.30） 因为 AlignScore
600	    度量的是事实一致性而非 generational depth。 Vocab richness correlation 略强（ρ~0.20-0.35）因为递归生成确实导致
601	    vocabulary narrowing。 Median 档 reviewer 对此实验缺失不会严重扣分（P2 priority）， 但 1 个 reviewer
602	    可能建议 "a naturalistic study would strengthen the paper''s practical relevance"。
603	
604	    '
605	  tables: []
606	  figures_description: []
607	  analysis: '未执行。Median 档下不影响核心评分但作为 future work 建议出现在 reviewer comments 中。
608	
609	    '
610	- name: exp-015
611	  plan_id: exp_015_neural_probe
612	  description: Frozen Qwen2.5-1.5B embeddings + MLP probe vs 15D features
613	  expected_results:
614	    pythia_k_star_neural: 2
615	    olmo_k_star_neural: 2
616	    qwen_cont_k_star_neural: 3
617	    qwen_cont_2v3_neural_auc: 0.616
618	    qwen_cont_2v3_neural_ci_lower: 0.6099
619	  result_rationale: 'Neural probe 结果分裂：Pythia/OLMo K*_neural=2（与 15D 一致），Qwen-cont
620	    K*_neural=3（高于 15D）。 Qwen-cont 的差异来自 self-scorer advantage——Qwen 的 embeddings
621	    对自己生成的文本有额外 depth signal。 Median 档下 reviewer 解读： (a) Pythia/OLMo K*_neural=2 confirms
622	    "K*=2 is data-intrinsic, not feature-engineering artifact" (b) Qwen K*_neural=3
623	    被 reviewer 解读为 "model-dependent K* exists in learned representations,  which contradicts
624	    the ''K* is purely text-intrinsic'' narrative" (c) 论文需要 careful framing：model-free
625	    15D features 给出 universal K*， neural probe 给出 model-dependent K*——两者都是 valid 但
626	    serve different purposes (d) 这实际上是 A8_attacked 的延伸——Qwen self-scorer 的 +1 bias
627	    在 neural probe 中更明显
628	
629	    '
630	  tables:
631	  - name: 'Table A5: Neural probe vs 15D features'
632	    content: '| Model | K*(15D) | K*(neural) | 2v3 AUC (neural) |
633	
634	      |-------|---------|-----------|-----------------|
635	
636	      | Pythia-1.4B | 2 | 2 | 0.596 |
637	
638	      | OLMo-1B | 2 | 2 | 0.589 |
639	
640	      | Qwen-cont | 2 | 3 | 0.616 |
641	
642	      '
643	  figures_description:
644	  - 'Comparison bar chart: 15D vs neural probe pairwise AUC, per model'
645	  analysis: 'Median 档下 reviewer 接受 "model-free features for headline K*" 的选择， 但 Qwen
646	    K*_neural=3 被部分 reviewer 用来质疑 K*=2 universality。 需要 framing: "K*(neural) is representation-dependent;
647	    K*(model-free) is the conservative,  universal measure we recommend for cross-model
648	    comparisons."
649	
650	    '
651	- name: exp-016
652	  plan_id: exp_016_base_vs_instruct
653	  description: Qwen2.5-1.5B base vs Instruct continuation mode comparison
654	  expected_results:
655	    k_star: 2
656	    base_1v2_auc: 0.6262
657	    base_ci_lower: 0.6168
658	    instruct_1v2_auc: 0.6112
659	    instruct_ci_lower: 0.6015
660	    ci_overlap: true
661	  result_rationale: 'Base 和 Instruct K* 一致=2，CI 重叠说明 instruction tuning 不改变 K*。 但
662	    base 1v2 AUC (0.6262) > instruct (0.6112)，即 instruction tuning 轻微降低  depth discrimination
663	    signal（可能因为 RLHF 增加了生成多样性）。 Median 档下 reviewer 不特别关注此实验——"Expected result, instruction
664	    tuning should  not fundamentally change text-intrinsic depth properties." 但 base
665	    CI lower=0.6168 vs instruct CI lower=0.6015 的差距被注意—— 如果 instruction tuning 进一步降低
666	    signal（如更强的 RLHF），K* 可能降至 1。
667	
668	    '
669	  tables:
670	  - name: 'Table A6: Base vs Instruct'
671	    content: '| Variant | 1v2 AUC | 95% CI | K* |
672	
673	      |---------|---------|--------|-----|
674	
675	      | Base | 0.626 | [0.617, 0.635] | 2 |
676	
677	      | Instruct | 0.611 | [0.602, 0.621] | 2 |
678	
679	      '
680	  figures_description: []
681	  analysis: 'Supporting evidence for K* robustness across base/instruct variants。不是
682	    highlight。
683	
684	    '
685	- name: exp-017
686	  plan_id: exp_017_qwen_continuation
687	  description: Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5
688	  expected_results:
689	    k_star: 2
690	    pairwise_auc_1v2: 0.6112
691	    ci_1v2_lower: 0.6015
692	    pairwise_auc_2v3: 0.5609
693	  result_rationale: 'Qwen-cont 1v2 AUC=0.6112，CI lower=0.6015——仅高于 θ 0.15pp。 在 median
694	    档下这是 A8_attacked 的核心：reviewer 单独点名 "CI lower=0.6015 is dangerously  close to the
695	    threshold. A few different random seeds could flip this to K*=1." 要求 sensitivity
696	    analysis：(a) 额外 seeds/bootstrap resamples，(b) θ 微调下的稳定性， (c) cross-scorer validation
697	    下的变化。 exp-022 中 qwen_cont256×pythia K*=1 (1v2=0.5979) 进一步加剧了这个 concern—— 当 scorer
698	    从 Qwen 换成 Pythia 时，Qwen-cont 确实可以翻转为 K*=1。 论文需要承认 Qwen-cont 处于 K*=1 和 K*=2 的边界，并以此作为
699	    θ-sensitivity 讨论的案例。
700	
701	    '
702	  tables:
703	  - name: 'Table 2 (row): Qwen2.5-1.5B-Instruct continuation'
704	    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
705	
706	      |-------|------|------|------|------|------|----|
707	
708	      | Qwen-1.5B-Inst cont | 0.997 | 0.611 | 0.561 | 0.541 | 0.514 | 2 |
709	
710	      | 95% CI (1v2) | — | [0.602, 0.621] | — | — | — | — |
711	
712	      '
713	  figures_description: []
714	  analysis: 'Median 档核心攻击目标。需要在论文中显式承认 borderline nature 并提供多层辩护。 Cross-scorer 和 θ-sensitivity
715	    数据在正文中呈现而非藏在 appendix。
716	
717	    '
718	- name: exp-018
719	  plan_id: exp_018_llama8b_depth
720	  description: LLaMA-3.1-8B, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B
721	  expected_results:
722	    k_star: 2
723	    pairwise_auc_1v2: 0.6123
724	    ci_1v2_lower: 0.6028
725	    ci_1v2_upper: 0.6216
726	  result_rationale: 'LLaMA-8B K*=2，CI lower=0.6028 (余量 +0.28pp)。 第三个模型家族确认 C4 K*=2，增强跨架构证据。
727	    Median 档下 reviewer 接受 LLaMA 结果但注意到： (a) CI lower=0.6028 也较边缘（虽不如 Qwen-cont 的 0.6015
728	    极端） (b) 0v1 AUC=0.9225 是所有模型中最低的——暗示 LLaMA 的 continuation  生成与原文更相似（model quality
729	    更高），导致整体 signal 更弱 (c) 但 K* 仍=2，支持 "K* is domain-determined regardless of absolute
730	    signal strength"
731	
732	    '
733	  tables:
734	  - name: 'Table 2 (row): LLaMA-3.1-8B C4 continuation'
735	    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
736	
737	      |-------|------|------|------|------|------|----|
738	
739	      | LLaMA-3.1-8B | 0.923 | 0.612 | 0.527 | 0.514 | 0.510 | 2 |
740	
741	      '
742	  figures_description: []
743	  analysis: 'LLaMA 的低 0v1 AUC (0.9225 vs others >0.96) 被 median 档 reviewer 解读为  "larger
744	    models produce more human-like text"——这与 A3 (scale limitation) 呼应： 更大模型可能导致 0v1
745	    也接近 threshold。
746	
747	    '
748	- name: exp-019
749	  plan_id: exp_019_mistral7b_depth
750	  description: Mistral-7B-v0.3, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B
751	  expected_results:
752	    k_star: 1
753	    pairwise_auc_1v2: 0.5935
754	    ci_1v2_lower: 0.5835
755	    ci_1v2_upper: 0.6032
756	    p_auc_leq_060: 0.9017
757	  result_rationale: 'Mistral K*=1 是唯一的 C4 outlier（7/8 K*=2 中的例外）。 1v2 AUC=0.5935 <
758	    θ=0.60，CI upper=0.6032 仅微超 θ，说明 Mistral 一代后即 one-wash。 Median 档下的 reviewer 反应分裂：
759	    (a) Reviewer A 接受 "7/8 dominant mode K*=2, with Mistral as interpretable outlier"
760	    (b) Reviewer B 攻击 "If 1/8 models gives K*=1, how can you claim K*=2 is universal?  This
761	    is evidence of model×domain interaction, not pure domain dependence." Cross-scorer
762	    validation (exp-019b) 确认 K*=1 是 text-intrinsic（non-scorer artifact）， 但这并不能回应 "model
763	    matters" 的质疑。 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 是关键回应——同一模型在不同域给出不同 K*，
764	    证明 domain 仍是 primary factor。但 reviewer 认为这只是 "primary, not sole"。 论文需要从 "sole
765	    determinant" 降级为 "primary factor, with residual model effects"。
766	
767	    '
768	  tables:
769	  - name: 'Table 2 (row): Mistral-7B C4 continuation (K*=1 outlier)'
770	    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
771	
772	      |-------|------|------|------|------|------|----|
773	
774	      | Mistral-7B | 0.984 | 0.594 | 0.540 | 0.523 | 0.518 | 1 |
775	
776	      | 95% CI (1v2) | — | [0.584, 0.603] | — | — | — | — |
777	
778	      '
779	  figures_description:
780	  - Highlighted outlier point in K* summary figure, with cross-scorer validation annotation
781	  analysis: 'Median 档核心攻击点之一。论文需要正面讨论 Mistral K*=1 而非 downplay， 并用 Mistral arXiv K*=3
782	    证明 domain 仍是 primary driver。 "Sole determinant" → "primary factor" 的降级措辞是 median
783	    档的必要调整。
784	
785	    '
786	- name: exp-020
787	  plan_id: exp_020_pythia_decoding
788	  description: 'Pythia-1.4B decoding ablation: 4 strategies, C4 5K docs, depth 0-5'
789	  expected_results:
790	    all_k_star_2: true
791	    greedy_1v2: 0.8838
792	    nuc09_1v2: 0.677
793	    t07_1v2: 0.7265
794	    t12_1v2: 0.6172
795	  result_rationale: 'Pythia 上 4 种解码策略 K* 全部=2，跨模型复制 exp-003 的解码不变性。 Greedy 1v2=0.8838
796	    极高——因为 greedy decoding 引入 repetition collapse， 使 depth 1 和 depth 2 文本差异大。T=1.2
797	    的 1v2=0.6172 最低（高温增加随机性，模糊差异）。 Median 档下 reviewer 正面评价跨模型 decoding invariance：
798	    "K*=2 holds across 2 models × 4 decoding strategies = 8 conditions, which is convincing."
799	    但 greedy 的异常高 AUC 被注意——"greedy is a degenerate condition that amplifies artifacts,  it
800	    shouldn''t be treated as equally valid."
801	
802	    '
803	  tables:
804	  - name: 'Table A7: Pythia decoding ablation'
805	    content: '| Decoding | 1v2 AUC | 2v3 AUC | K* |
806	
807	      |----------|---------|---------|-----|
808	
809	      | greedy | 0.884 | 0.534 | 2 |
810	
811	      | nucleus p=0.9 | 0.677 | 0.555 | 2 |
812	
813	      | T=0.7 | 0.727 | 0.594 | 2 |
814	
815	      | T=1.2 | 0.617 | 0.523 | 2 |
816	
817	      '
818	  figures_description: []
819	  analysis: 'Supporting evidence，放 Appendix。Greedy 的 repetition collapse 作为 caveat
820	    在正文中提及。
821	
822	    '
823	- name: exp-021
824	  plan_id: exp_021_length_ablation
825	  description: 'Text length ablation: 128/256/512 tokens, Qwen continuation'
826	  expected_results:
827	    128tok_k_star: 2
828	    256tok_k_star: 2
829	    512tok_k_star: 2
830	    512tok_1v2_ci_lower: 0.5979
831	    512tok_verdict: BORDERLINE
832	  result_rationale: 'K*=2 在三种长度下一致。但 512tok 的 CI lower=0.5979 < θ 是 borderline failure——
833	    在 median 档下 reviewer 注意到 "longer texts paradoxically reduce discriminability,  which
834	    is counter-intuitive and requires explanation." 解释：512 tokens 的 continuation 更有空间
835	    converge to the generator''s style， 使 depth 1 和 depth 2 更相似。这与 "one-wash laundering"
836	    概念一致。 但 reviewer 认为 "if the result flips at 512 tokens, the 256-token headline
837	    results  may be cherry-picking the optimal length." 论文需要承认 length sensitivity
838	    并在主文讨论。
839	
840	    '
841	  tables:
842	  - name: 'Table A8: Length ablation'
843	    content: '| Length | 1v2 AUC | CI lower | K* |
844	
845	      |--------|---------|---------|-----|
846	
847	      | 128 tok | 0.622 | >0.60 | 2 |
848	
849	      | 256 tok | 0.628 | >0.60 | 2 |
850	
851	      | 512 tok | 0.607 | 0.598 | 2* |
852	
853	      '
854	  figures_description: []
855	  analysis: '512-token borderline 被 median 档 reviewer 视为 minor concern。 与 Qwen-cont
856	    CI lower=0.6015 的边缘性一起被归入 "robustness limitations" 段。
857	
858	    '
859	- name: exp-022
860	  plan_id: exp_022_cross_scorer_matrix
861	  description: '4×4 cross-scorer matrix: 4 generators × 4 scorers'
862	  expected_results:
863	    k_star_2_count: 11
864	    k_star_1_count: 1
865	    exception: qwen_cont256×pythia (1v2=0.5979)
866	    scorer_delta_within_generator: <0.025
867	  result_rationale: '11/12 combos K*=2 是 scorer independence 的强证据。 唯一例外 qwen_cont256×pythia
868	    (K*=1) 被 reviewer 注意但不被严重攻击—— 因为 Qwen-cont 本身就是最 marginal 的 generator（CI lower=0.6015），
869	    换 scorer 后 flip 到 K*=1 是 consistent with its borderline nature。 Median 档下 reviewer
870	    正面评价："Scorer independence is well-established.  The paper correctly identifies
871	    and discusses the single exception." 但 A8_attacked 的 reviewer 用这个数据加强攻击："Even
872	    with different scorers,  Qwen-cont is unstable."
873	
874	    '
875	  tables:
876	  - name: 'Table 10: Cross-scorer matrix (selected)'
877	    content: '| Generator × Scorer | 1v2 AUC | K* |
878	
879	      |-------------------|---------|-----|
880	
881	      | Qwen-base × OLMo | 0.605 | 2 |
882	
883	      | Qwen-base × Pythia | 0.617 | 2 |
884	
885	      | Qwen-cont × Pythia | 0.598 | 1 |
886	
887	      | Qwen-cont × Qwen-base | 0.628 | 2 |
888	
889	      '
890	  figures_description:
891	  - 4×4 heatmap of K* values in cross-scorer matrix
892	  analysis: 'Scorer independence confirmed。论文在正文中展示完整矩阵以预防 "self-scorer bias" 攻击。
893	
894	    '
895	- name: exp-023
896	  plan_id: exp_023_domain_ablation
897	  description: Wikipedia domain, Qwen2.5-1.5B base continuation, 5K docs, depth 0-5
898	  expected_results:
899	    k_star: 2
900	    one_v_two_auc: 0.6193
901	    all_folds_above_060: true
902	  result_rationale: 'Wikipedia K*=2 (same-family scorer) 但经 D060 cross-scorer confound
903	    分析后降为 K*=1。 这是 median 档中 scorer confound 的 key demonstration： Qwen same-family
904	    scorer 在 Wikipedia 上给出 +1 bias（K*=2）， 换 Pythia cross-family scorer 后 K*=1。 论文正文报告
905	    scorer-controlled K*=1 for Wikipedia, Appendix 披露 confound 细节。 Reviewer 接受 confound
906	    控制但质疑："If the simplest domain already saturates at K*=1,  and web text at K*=2,
907	    the range {1,2,3} is very narrow.  Is the finding essentially that recursive generation
908	    quickly loses information?" 这触发 A1 ("somewhat expected")。
909	
910	    '
911	  tables:
912	  - name: 'Table 11 (row): Wikipedia domain K*'
913	    content: '| Domain | Scorer | 1v2 AUC | K* |
914	
915	      |--------|--------|---------|-----|
916	
917	      | Wikipedia | Qwen (same-family) | 0.619 | 2 |
918	
919	      | Wikipedia | Pythia (cross-family) | 0.585 | 1 |
920	
921	      | Wikipedia | scorer-controlled | — | 1 |
922	
923	      '
924	  figures_description:
925	  - 'Domain ladder figure: Wikipedia(1) < C4(2) < arXiv(3)'
926	  analysis: 'Scorer confound on Wikipedia 是 honest reporting，增加论文可信度。 但 K*=1 for Wikipedia
927	    被 reviewer 解读为 "trivial — one generation washes everything."
928	
929	    '
930	- name: exp-024
931	  plan_id: exp_024_arxiv_domain
932	  description: arXiv domain, Qwen2.5-1.5B base continuation, 5K docs, depth 0-5
933	  expected_results:
934	    k_star: 3
935	    pairwise_auc_1v2: 0.858
936	    pairwise_auc_2v3: 0.6427
937	    ci_2v3_lower: 0.6275
938	  result_rationale: 'arXiv K*=3 是 domain dependence 的最强证据——首个 K*>2 的条件。 2v3 AUC=0.6427,
939	    CI lower=0.6275 >> θ=0.60（余量 +2.75pp）。 1v2 AUC=0.858 远超 C4/Wiki (~0.61-0.69)，arXiv
940	    的 LaTeX/citation/math  结构特征提供额外 depth-distinguishing signal。 Median 档下 reviewer
941	    反应： (a) 正面：K*=3 on arXiv is a genuinely interesting finding, domain dependence
942	    is well-demonstrated (b) 攻击：A2 假设触发——"3 domains is too few to claim ''domain is
943	    the sole determinant''.  What about code, legal text, news, social media?" (c)
944	    建议：需要更多域来充分支持 domain hierarchy claim 论文需要降级措辞从 "sole determinant" 到 "primary factor"，
945	    承认 3 domains 是 initial evidence 而非 exhaustive characterization。
946	
947	    '
948	  tables:
949	  - name: 'Table 11 (row): arXiv domain K*'
950	    content: '| Domain | 1v2 AUC | 2v3 AUC | 3v4 AUC | K* |
951	
952	      |--------|---------|---------|---------|-----|
953	
954	      | arXiv | 0.858 | 0.643 | 0.544 | 3 |
955	
956	      '
957	  figures_description:
958	  - 'AUC decay curves: 3 domains overlaid, showing domain-dependent saturation points'
959	  analysis: 'K*=3 on arXiv 是论文的 strongest individual finding，但 3-domain limitation
960	    被 reviewer 攻击。 exp_027 LaTeX ablation (K*=3 preserved after stripping) 有效消除格式
961	    confound。
962	
963	    '
964	- name: exp-025
965	  plan_id: exp_025_pythia_filtering
966	  description: 'Pythia-1.4B filtering replication: 3 strategies × 3 seeds'
967	  expected_results:
968	    all_strategies_nearly_identical: true
969	    max_delta_mmlu: 0.0017
970	    binary_hellaswag_delta: '+0.0000'
971	    key_finding: null result
972	  result_rationale: 'Pythia-1.4B 上三种策略产生几乎相同结果（max Δ=0.0017 MMLU），filtering ordering
973	    未确认。 Median 档下这是 C3 的严重打击（A5_fail 部分）： (a) Pythia 太小（1.4B, MMLU~0.26）对 filtering
974	    signal 不敏感——模型 capacity 不足 (b) 但 reviewer 质疑 "if filtering doesn''t help even
975	    small models, why should we trust  it helps larger ones?" (c) 论文需要 framing：Pythia
976	    的 base capability 太低（MMLU=0.26 接近 random）， filtering 的 marginal benefit 在 low-capability
977	    regime 被淹没 (d) 这个 null result 被 1 个 reviewer 肯定（"honest reporting of negative
978	    results"）， 被另一个 reviewer 用来质疑 C3 整体证据链
979	
980	    '
981	  tables:
982	  - name: 'Table A9: Pythia filtering (null result)'
983	    content: '| Strategy | MMLU | HellaSwag |
984	
985	      |----------|------|-----------|
986	
987	      | binary-ours | 0.259±0.000 | 0.525±0.000 |
988	
989	      | graduated α=0.9 | 0.256±0.001 | 0.525±0.001 |
990	
991	      | no-filter | 0.257±0.001 | 0.525±0.001 |
992	
993	      '
994	  figures_description: []
995	  analysis: 'Null result。放 Appendix 作为 honest reporting。 C3 的证据链因此完全依赖 exp-006 (Qwen)
996	    和 exp-009 (dose-response)。 Median 档 reviewer 评价 C3 substance ~2.5。
997	
998	    '
999	- name: exp-026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5c70234-b9ce-4e87-9329-4d8d65c427c8",
  "isSidechain": false,
  "promptId": "59587622-660c-4957-a549-a3c2036a769c",
  "type": "user",
  "uuid": "9ab724ef-9c6e-4cfa-872f-78f8cf0de49d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
      "content": "\n      '\n  figures_description:\n  - 'Scale comparison subplot: 1.5B vs 7B pairwise AUC curves overlapping'\n  analysis: 'Scale invariance (1.5B→7B) 被 1 个 reviewer 认为是 \"weak evidence for scale\n    generalization\"。 Rebuttal 需要 14B/32B 数据。exp_14b_c4 (K*=2) 已可用但 exp_32b_c4 仍在跑。\n    如果 32B 也给 K*=2，可在 rebuttal 中有效回应 A3。\n\n    '\n- name: exp-005\n  plan_id: exp_005_degradation\n  description: Feature group ablation + degradation ordering analysis\n  expected_results:\n    cross_model_spearman_rho_pythia_olmo: 0.95\n    cross_model_spearman_rho_pythia_qwen_cont: 0.9143\n    cross_model_spearman_rho_olmo_qwen_cont: 0.85\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std\n    1v2_tau_weakness: ~0.37\n  result_rationale: 'Feature ordering 跨模型高度一致（ρ≥0.85），支持 depth signal 是 text-intrinsic\n    而非 model-specific。 Median 档下 reviewer 接受 feature ranking consistency 但不视为独立贡献——\n    \"Feature analysis is supportive but expected if the underlying signal is text-intrinsic.\"\n    1v2 pair 的 feature importance 一致性最弱（τ~0.37），被 reviewer 注意但不重点攻击 （因为这恰好是 boundary\n    pair，信号最微弱处 variance 大是合理的）。 Surprisal-based features 主导的发现与 DPI 理论一致，被 reviewer\n    视为 \"expected alignment\"。\n\n    '\n  tables:\n  - name: 'Table A2: Cross-model feature ranking Spearman ρ'\n    content: '| Model Pair | Spearman ρ |\n\n      |------------|-----------|\n\n      | Pythia ↔ OLMo | 0.950 |\n\n      | Pythia ↔ Qwen-cont | 0.914 |\n\n      | OLMo ↔ Qwen-cont | 0.850 |\n\n      '\n  figures_description:\n  - Feature importance heatmap across models — 放 Appendix\n  analysis: 'Supporting evidence for text-intrinsic signal。不构成独立卖点但消除 \"model self-familiarity\"\n    质疑。 Median 档下这个实验的贡献被 reviewer 归入 \"thorough analysis\" 而非 novel finding。\n\n    '\n- name: exp-006\n  plan_id: exp_006_graduated_filtering\n  description: 'Downstream filtering evaluation: 6 strategies × 5 seeds, MMLU + HellaSwag'\n  expected_results:\n    binary_ours_mmlu: 0.5941±0.0008\n    binary_ours_hellaswag: 0.6701±0.0006\n    no_filter_mmlu: 0.5865±0.0010\n    no_filter_hellaswag: 0.6638±0.0008\n    delta_mmlu_binary_vs_nofilter: '+0.0076'\n    delta_hellaswag_binary_vs_nofilter: '+0.0063'\n    base_model_mmlu: 0.6018\n    graduated_a09_mmlu: 0.5892±0.0008\n    dsir_mmlu: 0.5869±0.0003\n  result_rationale: 'Binary-ours 在所有策略中最优，但 MMLU 增益仅 +0.76pp vs no-filter。 在 median\n    档下，这是 C3 的核心弱点（A5_fail）： (a) MMLU Δ=0.76pp 被 reviewer 质疑 practical significance——\"Is\n    <1pp improvement  worth the curation complexity?\" (b) 所有策略都 degrade vs base_model（0.6018→0.5941），说明\n    contaminated data 的  fundamental harm 无法被 filtering 完全消除 (c) Graduated α 单调递增确认\n    K*=2 boundary，但 reviewer 指出这是 circular reasoning—— 用 K* 设计 filtering 然后用 filtering\n    验证 K* (d) DSIR 表现差（接近 no-filter）是一个正面结果，但 reviewer 质疑 DSIR baseline  的公平性（DSIR\n    不是为 depth-aware filtering 设计的）\n\n    '\n  tables:\n  - name: 'Table 5: Filtering strategy comparison (Qwen2.5-1.5B, 30% contamination)'\n    content: '| Strategy | MMLU | HellaSwag | Δ MMLU vs no-filter |\n\n      |----------|------|-----------|-------------------|\n\n      | binary-ours | 0.5941±0.0008 | 0.6701±0.0006 | +0.0076* |\n\n      | binary-Drayson | 0.5913±0.0009 | 0.6691±0.0004 | +0.0048* |\n\n      | surprisal | 0.5894±0.0009 | 0.6641±0.0006 | +0.0029 |\n\n      | graduated α=0.9 | 0.5892±0.0008 | 0.6701±0.0007 | +0.0027 |\n\n      | DSIR | 0.5869±0.0003 | 0.6631±0.0007 | +0.0004 |\n\n      | no-filter | 0.5865±0.0010 | 0.6638±0.0008 | — |\n\n      | base (no contam.) | 0.6018 | 0.6821 | — |\n\n      '\n  figures_description:\n  - 'Bar chart: filtering strategies ranked by MMLU, with base_model reference line'\n  - 'α sensitivity curve: graduated filtering MMLU as function of α'\n  analysis: 'Median 档 reviewer 给 C3 的 substance score ~2.5-3.0。核心攻击点： 1. Effect size\n    太小（<1pp MMLU）不够 actionable 2. Binary > graduated 说明 K* boundary 信息对 curation 有用，但增益微小\n    3. 所有策略 degrade vs base_model 暗示 filtering 的 ceiling 低 C3 需要从 \"validation\" 降级为\n    \"case study / demonstration\"。\n\n    '\n- name: exp-007\n  plan_id: exp_007_bootstrap_ci\n  description: K* sensitivity at θ=0.55/0.60/0.65/0.70 + bootstrap CI + permutation\n    test\n  expected_results:\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015\n    theta_055_k_star_distribution: all models K*=2 or K*=3\n    theta_060_k_star_distribution: 7/8 K*=2, 1/8 K*=1 (Mistral)\n    theta_065_k_star_distribution: 4-5/8 K*=2, rest K*=1\n    theta_070_k_star_distribution: most K*=1\n  result_rationale: 'θ-sensitivity 是 median 档的关键攻击面（A6_partial）。 θ=0.60 下 7/8 configurations\n    K*=2 被接受，但 θ=0.70 下多数降至 K*=1 被 reviewer 放大—— \"The finding is highly sensitive\n    to threshold choice. At θ=0.70, the headline result  (K*=2 as dominant mode) collapses.\"\n    Qwen-cont CI lower=0.6015 被 A8_attacked 假设触发——reviewer 要求 sensitivity analysis  或额外\n    seeds 来确认这不是 noise。 论文需要在主文（非 appendix）展示 θ-sensitivity figure，正面呈现 K* 在 [0.55,\n    0.65]  范围内的稳定性，并以 Cohen''s h=0.20 和 AUC gap discontinuity 为 θ=0.60 选择辩护。 Permutation\n    test p<0.001 对所有 boundary pairs 提供统计支持，但 reviewer 指出  \"statistical significance\n    ≠ practical significance at these effect sizes\"。\n\n    '\n  tables:\n  - name: 'Table 4: K* sensitivity to threshold θ'\n    content: '| θ | K*=1 | K*=2 | K*=3 |\n\n      |------|------|------|------|\n\n      | 0.55 | 0/8  | 7/8  | 1/8  |\n\n      | 0.60 | 1/8  | 7/8  | 0/8  |\n\n      | 0.65 | 3-4/8 | 4-5/8 | 0/8 |\n\n      | 0.70 | 6-7/8 | 1-2/8 | 0/8 |\n\n      '\n  figures_description:\n  - '主文 Figure: θ-sensitivity heatmap，showing K* stability in [0.55, 0.65]'\n  - AUC gap discontinuity plot at K* boundary pair\n  analysis: 'θ-sensitivity 被 median 档 reviewer 视为 \"fair analysis\" 但 robustness concern\n    未完全消除。 关键辩护：θ=0.60 对应 Cohen''s h≈0.20（small effect size threshold）， 且 1v2 vs 2v3\n    的 AUC gap 远大于 θ 选择的 sensitivity range。 Reviewer 接受 [0.55, 0.65] 稳定性但仍认为 \"the result\n    is more about where you draw the line  than about the underlying phenomenon\"。\n\n    '\n- name: exp-008\n  plan_id: exp_008_retrain_chain_v2\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA, C4 5K docs, depth\n    0-4'\n  expected_results:\n    k_star: '>=4'\n    pairwise_auc_0v1: 0.9847\n    pairwise_auc_1v2: 0.9484\n    pairwise_auc_2v3: 0.8888\n    pairwise_auc_3v4: 0.7982\n  result_rationale: 'Retrain-chain K*≥4 与 prompt-chain K*=2 的对比是重要的 ecological validity\n    argument。 LoRA fine-tune 每代引入 cumulative model artifacts（vocabulary narrowing,\n    repetition bias）， 使各代高度可区分。Median 档下 reviewer 接受 \"prompt-chain isolates text-intrinsic\n    degradation\"  的论点，但 1 个 reviewer 认为这说明 \"in practice, retrain-chain contamination\n    is more  detectable, so K*=2 underestimates real-world detectability\"——这实际上对论文有利\n    （prompt-chain K*=2 是 conservative estimate），但 reviewer 的 framing 是  \"the paper\n    should discuss this more prominently\"。 3v4 AUC=0.7982 远超 θ=0.60，所有 pairs 在 retrain-chain\n    下都高度可区分， 证明 K* 的低有界性是 prompt-chain (text-intrinsic) 特有的。\n\n    '\n  tables:\n  - name: 'Table 6: Prompt-chain vs Retrain-chain comparison'\n    content: '| Pair | Prompt-chain AUC | Retrain-chain AUC |\n\n      |------|-----------------|-------------------|\n\n      | 0v1  | 0.993 | 0.985 |\n\n      | 1v2  | 0.654 | 0.948 |\n\n      | 2v3  | 0.552 | 0.889 |\n\n      | 3v4  | 0.515 | 0.798 |\n\n      '\n  figures_description:\n  - 'Dual-panel AUC decay: prompt-chain (sharp drop) vs retrain-chain (gradual decay)'\n  analysis: '强有力的 supporting evidence。Median 档 reviewer 肯定此实验的 ecological validity\n    贡献， 但建议正文讨论 \"real-world contamination likely falls between prompt-chain and retrain-chain\"。\n\n    '\n- name: exp-009\n  plan_id: exp_009_dose_50pct\n  description: 'Contamination dose-response: 10%/30%/50% ratio × 3 strategies × 5\n    seeds'\n  expected_results:\n    binary_consistently_best: true\n    graduated_equals_no_filter: true\n    hellaswag_binary_significant_all_ratios: true\n    mmlu_binary_30pct_p: 0.074\n    effect_size_increases_with_contamination: true\n  result_rationale: 'Dose-response 确认 binary filtering 在所有 contamination ratio 下一致最优，\n    graduated filtering 在每个 ratio 下都崩溃至 no-filter 水平。 在 median 档下： (a) HellaSwag 显著性是正面证据（p≤0.004\n    at all ratios） (b) MMLU 在 30% ratio 下 p=0.074 不显著——reviewer 注意到 \"inconsistent\n    significance  across benchmarks weakens the claim\"（A5_fail 部分触发） (c) Effect size\n    随 contamination ratio 增加（10%: +0.38pp, 30%: +0.61pp, 50%: +0.51pp HellaSwag），\n    但绝对值仍然小 (d) 一个 reviewer 肯定 dose-response 设计的 thoroughness，但另一个认为  \"50% synthetic\n    injection is unrealistic for current web data\"\n\n    '\n  tables:\n  - name: 'Table 7: Dose-response analysis'\n    content: '| Ratio | Strategy | MMLU | HellaSwag |\n\n      |-------|----------|------|-----------|\n\n      | 10% | binary | 0.6079 | 0.6727** |\n\n      | 10% | graduated | 0.6066 | 0.6700 |\n\n      | 10% | no-filter | 0.6058 | 0.6689 |\n\n      | 30% | binary | 0.6082 | 0.6725** |\n\n      | 30% | graduated | 0.6072 | 0.6665 |\n\n      | 30% | no-filter | 0.6069 | 0.6664 |\n\n      | 50% | binary | 0.6088 | 0.6731** |\n\n      | 50% | graduated | 0.6062 | 0.6679 |\n\n      | 50% | no-filter | 0.6063 | 0.6680 |\n\n      '\n  figures_description:\n  - 'Line plot: HellaSwag as function of contamination ratio, 3 strategies, with significance\n    markers'\n  analysis: 'Binary filtering 的 dose-response consistency 是 C3 的最强证据。 但 graduated=no-filter\n    的一致性同时说明 K*-aware graduated curation 无增量价值—— 这直接削弱了 \"K* informs curation granularity\"\n    的 narrative。 Median 档下 C3 的 reviewer 评分因此在 2.5-3.0 区间。\n\n    '\n- name: exp-010\n  plan_id: exp_010_ordinal_baseline\n  description: CORAL vs multiclass LightGBM vs ordinal logistic regression\n  expected_results:\n    obd_lgbm_best_accuracy: 0.4229\n    multiclass_lgbm_accuracy: 0.4182\n    ordinal_logreg_best_tau: 0.563\n    obd_lgbm_best_mae: 0.9836\n  result_rationale: 'OBD-LightGBM 在 accuracy 和 mean_pw_auc 上略优于 multiclass LightGBM，\n    但差异小（Δacc < 0.5pp）。Ordinal logistic regression MAE 最低但 accuracy 最差。 Median 档下\n    reviewer 不特别关注此实验——它是 methodology 的 supporting evidence， 不构成独立卖点。Reviewer 认为 \"the\n    choice between ordinal and multiclass classifiers  is an implementation detail,\n    not a contribution\"。 但 ordinal structure 的存在（CORAL MAE < multiclass MAE across\n    all models） 为论文的 \"depth is ordinal, not categorical\" framing 提供小幅支持。\n\n    '\n  tables:\n  - name: 'Table A3: Classifier comparison'\n    content: '| Method | Acc | MAE | τ_b | Mean PW-AUC |\n\n      |--------|-----|-----|-----|-------------|\n\n      | OBD-LightGBM | 0.423 | 0.984 | 0.552 | 0.621 |\n\n      | Multiclass-LightGBM | 0.418 | 1.016 | 0.537 | 0.625 |\n\n      | Ordinal LogReg | 0.364 | 0.911 | 0.563 | 0.502 |\n\n      '\n  figures_description: []\n  analysis: 'Appendix material。Median 档 reviewer 不质疑也不 highlight。\n\n    '\n- name: exp-011\n  plan_id: exp_011_llm_zeroshot\n  description: GPT-5.5 / Claude Opus 4.6 zero-shot depth estimation baseline\n  expected_results:\n    gpt55_5class_acc: 0.332\n    claude_5class_acc: 0.331\n    gpt55_binary_acc: 0.878\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n  result_rationale: 'Frontier LLMs 在 5-class depth estimation 上表现不如 OBD-LightGBM（33%\n    vs 39%）， 但 binary detection 高达 88%。这是一个 strong baseline comparison： (a) 证明 depth\n    estimation 需要 specialized features，不能 \"throw LLM at it\" (b) Binary detection 高但\n    fine-grained depth 失败，支持 \"binary ≠ depth\" 的 claim Median 档下 reviewer 对此实验评价较正面——\"Good\n    to include, demonstrates the problem  is not trivially solvable.\"但 1 个 reviewer\n    指出 OBD 也只有 39% accuracy， \"both methods are poor at fine-grained depth estimation,\n    which raises the question  of whether depth estimation beyond K* is even meaningful\"。\n    这实际上对 K* characterization 有利（K* 之后的深度确实无法区分）， 但被 reviewer 解读为对整体 contribution\n    的 dampener。\n\n    '\n  tables:\n  - name: 'Table 8: LLM zero-shot vs OBD baseline'\n    content: '| Method | 5-class Acc | MAE | Binary Acc |\n\n      |--------|------------|-----|-----------|\n\n      | GPT-5.5 | 0.332 | 1.102 | 0.878 |\n\n      | Claude Opus 4.6 | 0.331 | 1.150 | 0.882 |\n\n      | OBD-LightGBM | 0.386 | 1.107 | — |\n\n      '\n  figures_description:\n  - 'Per-depth accuracy heatmap: LLMs vs OBD, showing LLM failure at depth 1-4'\n  analysis: 'Median 档 reviewer 正面评价此 baseline，但 McNemar test non-significant (p~0.07-0.08)  被注意——\"The\n    advantage of OBD over frontier LLMs is not statistically significant.\"\n\n    '\n- name: exp-012\n  plan_id: exp_012_binary_confidence\n  description: DivEye/Binoculars binary detector confidence as depth proxy\n  expected_results:\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    spearman_rho_range: 0.06-0.46\n    auc_non_monotonic: true\n    six_class_accuracy_max: 0.199\n  result_rationale: 'Binary detectors K*≈1 vs OBD K*=2，6-class accuracy 接近 random（≤0.199\n    vs 0.167 random）。 Spearman correlation 弱且非单调。直接支持 \"binary confidence ≠ depth\"\n    的 claim。 Median 档下 reviewer 接受此结论——\"Well-designed experiment that justifies the\n    need for  depth-aware features beyond binary detection.\" 不被特别攻击。 但 reviewer 注意到\n    DivEye/Binoculars 都是 perplexity-based， 建议加入 watermark-based 或 learned detectors\n    作为 baseline。论文无此 baseline  被视为 minor weakness 而非 major concern。\n\n    '\n  tables:\n  - name: 'Table A4: Binary detector depth estimation'\n    content: '| Generator | 6-class Acc | ρ (ppl_ratio) | AUC monotonic? |\n\n      |-----------|------------|--------------|---------------|\n\n      | Qwen-rw | 0.199 | 0.119 | ❌ |\n\n      | Pythia | 0.130 | -0.392 | ❌ |\n\n      | OLMo | 0.127 | -0.407 | ❌ |\n\n      | Qwen-cont | 0.183 | -0.058 | ❌ |\n\n      '\n  figures_description:\n  - 'Scatter plot: binary detector confidence vs true depth, showing non-monotonicity'\n  analysis: 'Strong justification for the paper''s approach。Median 档下被 reviewer 正面引用。\n\n    '\n- name: exp-013\n  plan_id: exp_013_cross_transfer\n  description: 4×4 cross-model transfer matrix\n  expected_results:\n    pythia_olmo_retention: 91-92%\n    qwen_cont_cross_retention: 80-85%\n    qwen_rw_cross_retention: 61-63%\n    binary_0v1_cross_all_above_096: true\n  result_rationale: 'Cross-model transfer 是 C1'' \"text-intrinsic signal\" 的核心证据。 Pythia↔OLMo\n    91-92% retention 和 0v1 cross-AUC > 0.96 强力支持 depth signal 跨模型可迁移。 Median 档下 reviewer\n    正面评价： (a) \"The high transfer retention confirms K* is not a self-familiarity artifact\"\n    (b) Qwen-rewrite 低 transfer (61-63%) 进一步区分 generation mode effect vs depth signal\n    (c) 但 reviewer 指出 \"all models are ≤8B from similar training distributions,  transfer\n    to fundamentally different models (e.g., 70B, multilingual) remains unknown\" 这与\n    A3 (scale limitation) 呼应。\n\n    '\n  tables:\n  - name: 'Table 9: Cross-model transfer retention'\n    content: '| Transfer Direction | Accuracy Retention |\n\n      |-------------------|-------------------|\n\n      | Pythia → OLMo | 92% |\n\n      | OLMo → Pythia | 91% |\n\n      | Qwen-cont → Pythia | 85% |\n\n      | Qwen-cont → OLMo | 80% |\n\n      | Qwen-rw → Pythia | 63% |\n\n      | Qwen-rw → OLMo | 61% |\n\n      '\n  figures_description:\n  - 4×4 transfer heatmap in main text\n  analysis: 'Median 档 reviewer 评价：C1'' 的 strongest supporting evidence 之一。 Transfer\n    > 80% 在 continuation mode 下消除 scorer bias 质疑。\n\n    '\n- name: exp-014\n  plan_id: ''\n  description: 'Naturalistic validation: Common Crawl 2025/2026 snapshot depth prediction'\n  expected_results:\n    predicted_depth_distribution:\n      depth_0: 60-75%\n      depth_1: 15-25%\n      depth_2_plus: 5-15%\n    correlation_with_alignscore: Spearman ρ=0.15-0.30\n    correlation_with_vocab_richness: Spearman ρ=0.20-0.35\n    predicted_contamination_rate: 25-40%\n  result_rationale: 'Naturalistic validation 在 median 档下是 P2 优先级，未执行。 如果执行，预期结果：Common\n    Crawl 2025/2026 中约 25-40% 文本被预测为 depth ≥1（合成文本）， 与外部估计一致。但 ground truth 缺失使此实验无法做定量验证——\n    只能做 correlation with proxy metrics。AlignScore correlation 弱（ρ~0.15-0.30） 因为 AlignScore\n    度量的是事实一致性而非 generational depth。 Vocab richness correlation 略强（ρ~0.20-0.35）因为递归生成确实导致\n    vocabulary narrowing。 Median 档 reviewer 对此实验缺失不会严重扣分（P2 priority）， 但 1 个 reviewer\n    可能建议 \"a naturalistic study would strengthen the paper''s practical relevance\"。\n\n    '\n  tables: []\n  figures_description: []\n  analysis: '未执行。Median 档下不影响核心评分但作为 future work 建议出现在 reviewer comments 中。\n\n    '\n- name: exp-015\n  plan_id: exp_015_neural_probe\n  description: Frozen Qwen2.5-1.5B embeddings + MLP probe vs 15D features\n  expected_results:\n    pythia_k_star_neural: 2\n    olmo_k_star_neural: 2\n    qwen_cont_k_star_neural: 3\n    qwen_cont_2v3_neural_auc: 0.616\n    qwen_cont_2v3_neural_ci_lower: 0.6099\n  result_rationale: 'Neural probe 结果分裂：Pythia/OLMo K*_neural=2（与 15D 一致），Qwen-cont\n    K*_neural=3（高于 15D）。 Qwen-cont 的差异来自 self-scorer advantage——Qwen 的 embeddings\n    对自己生成的文本有额外 depth signal。 Median 档下 reviewer 解读： (a) Pythia/OLMo K*_neural=2 confirms\n    \"K*=2 is data-intrinsic, not feature-engineering artifact\" (b) Qwen K*_neural=3\n    被 reviewer 解读为 \"model-dependent K* exists in learned representations,  which contradicts\n    the ''K* is purely text-intrinsic'' narrative\" (c) 论文需要 careful framing：model-free\n    15D features 给出 universal K*， neural probe 给出 model-dependent K*——两者都是 valid 但\n    serve different purposes (d) 这实际上是 A8_attacked 的延伸——Qwen self-scorer 的 +1 bias\n    在 neural probe 中更明显\n\n    '\n  tables:\n  - name: 'Table A5: Neural probe vs 15D features'\n    content: '| Model | K*(15D) | K*(neural) | 2v3 AUC (neural) |\n\n      |-------|---------|-----------|-----------------|\n\n      | Pythia-1.4B | 2 | 2 | 0.596 |\n\n      | OLMo-1B | 2 | 2 | 0.589 |\n\n      | Qwen-cont | 2 | 3 | 0.616 |\n\n      '\n  figures_description:\n  - 'Comparison bar chart: 15D vs neural probe pairwise AUC, per model'\n  analysis: 'Median 档下 reviewer 接受 \"model-free features for headline K*\" 的选择， 但 Qwen\n    K*_neural=3 被部分 reviewer 用来质疑 K*=2 universality。 需要 framing: \"K*(neural) is representation-dependent;\n    K*(model-free) is the conservative,  universal measure we recommend for cross-model\n    comparisons.\"\n\n    '\n- name: exp-016\n  plan_id: exp_016_base_vs_instruct\n  description: Qwen2.5-1.5B base vs Instruct continuation mode comparison\n  expected_results:\n    k_star: 2\n    base_1v2_auc: 0.6262\n    base_ci_lower: 0.6168\n    instruct_1v2_auc: 0.6112\n    instruct_ci_lower: 0.6015\n    ci_overlap: true\n  result_rationale: 'Base 和 Instruct K* 一致=2，CI 重叠说明 instruction tuning 不改变 K*。 但\n    base 1v2 AUC (0.6262) > instruct (0.6112)，即 instruction tuning 轻微降低  depth discrimination\n    signal（可能因为 RLHF 增加了生成多样性）。 Median 档下 reviewer 不特别关注此实验——\"Expected result, instruction\n    tuning should  not fundamentally change text-intrinsic depth properties.\" 但 base\n    CI lower=0.6168 vs instruct CI lower=0.6015 的差距被注意—— 如果 instruction tuning 进一步降低\n    signal（如更强的 RLHF），K* 可能降至 1。\n\n    '\n  tables:\n  - name: 'Table A6: Base vs Instruct'\n    content: '| Variant | 1v2 AUC | 95% CI | K* |\n\n      |---------|---------|--------|-----|\n\n      | Base | 0.626 | [0.617, 0.635] | 2 |\n\n      | Instruct | 0.611 | [0.602, 0.621] | 2 |\n\n      '\n  figures_description: []\n  analysis: 'Supporting evidence for K* robustness across base/instruct variants。不是\n    highlight。\n\n    '\n- name: exp-017\n  plan_id: exp_017_qwen_continuation\n  description: Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5\n  expected_results:\n    k_star: 2\n    pairwise_auc_1v2: 0.6112\n    ci_1v2_lower: 0.6015\n    pairwise_auc_2v3: 0.5609\n  result_rationale: 'Qwen-cont 1v2 AUC=0.6112，CI lower=0.6015——仅高于 θ 0.15pp。 在 median\n    档下这是 A8_attacked 的核心：reviewer 单独点名 \"CI lower=0.6015 is dangerously  close to the\n    threshold. A few different random seeds could flip this to K*=1.\" 要求 sensitivity\n    analysis：(a) 额外 seeds/bootstrap resamples，(b) θ 微调下的稳定性， (c) cross-scorer validation\n    下的变化。 exp-022 中 qwen_cont256×pythia K*=1 (1v2=0.5979) 进一步加剧了这个 concern—— 当 scorer\n    从 Qwen 换成 Pythia 时，Qwen-cont 确实可以翻转为 K*=1。 论文需要承认 Qwen-cont 处于 K*=1 和 K*=2 的边界，并以此作为\n    θ-sensitivity 讨论的案例。\n\n    '\n  tables:\n  - name: 'Table 2 (row): Qwen2.5-1.5B-Instruct continuation'\n    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |\n\n      |-------|------|------|------|------|------|----|\n\n      | Qwen-1.5B-Inst cont | 0.997 | 0.611 | 0.561 | 0.541 | 0.514 | 2 |\n\n      | 95% CI (1v2) | — | [0.602, 0.621] | — | — | — | — |\n\n      '\n  figures_description: []\n  analysis: 'Median 档核心攻击目标。需要在论文中显式承认 borderline nature 并提供多层辩护。 Cross-scorer 和 θ-sensitivity\n    数据在正文中呈现而非藏在 appendix。\n\n    '\n- name: exp-018\n  plan_id: exp_018_llama8b_depth\n  description: LLaMA-3.1-8B, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B\n  expected_results:\n    k_star: 2\n    pairwise_auc_1v2: 0.6123\n    ci_1v2_lower: 0.6028\n    ci_1v2_upper: 0.6216\n  result_rationale: 'LLaMA-8B K*=2，CI lower=0.6028 (余量 +0.28pp)。 第三个模型家族确认 C4 K*=2，增强跨架构证据。\n    Median 档下 reviewer 接受 LLaMA 结果但注意到： (a) CI lower=0.6028 也较边缘（虽不如 Qwen-cont 的 0.6015\n    极端） (b) 0v1 AUC=0.9225 是所有模型中最低的——暗示 LLaMA 的 continuation  生成与原文更相似（model quality\n    更高），导致整体 signal 更弱 (c) 但 K* 仍=2，支持 \"K* is domain-determined regardless of absolute\n    signal strength\"\n\n    '\n  tables:\n  - name: 'Table 2 (row): LLaMA-3.1-8B C4 continuation'\n    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |\n\n      |-------|------|------|------|------|------|----|\n\n      | LLaMA-3.1-8B | 0.923 | 0.612 | 0.527 | 0.514 | 0.510 | 2 |\n\n      '\n  figures_description: []\n  analysis: 'LLaMA 的低 0v1 AUC (0.9225 vs others >0.96) 被 median 档 reviewer 解读为  \"larger\n    models produce more human-like text\"——这与 A3 (scale limitation) 呼应： 更大模型可能导致 0v1\n    也接近 threshold。\n\n    '\n- name: exp-019\n  plan_id: exp_019_mistral7b_depth\n  description: Mistral-7B-v0.3, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B\n  expected_results:\n    k_star: 1\n    pairwise_auc_1v2: 0.5935\n    ci_1v2_lower: 0.5835\n    ci_1v2_upper: 0.6032\n    p_auc_leq_060: 0.9017\n  result_rationale: 'Mistral K*=1 是唯一的 C4 outlier（7/8 K*=2 中的例外）。 1v2 AUC=0.5935 <\n    θ=0.60，CI upper=0.6032 仅微超 θ，说明 Mistral 一代后即 one-wash。 Median 档下的 reviewer 反应分裂：\n    (a) Reviewer A 接受 \"7/8 dominant mode K*=2, with Mistral as interpretable outlier\"\n    (b) Reviewer B 攻击 \"If 1/8 models gives K*=1, how can you claim K*=2 is universal?  This\n    is evidence of model×domain interaction, not pure domain dependence.\" Cross-scorer\n    validation (exp-019b) 确认 K*=1 是 text-intrinsic（non-scorer artifact）， 但这并不能回应 \"model\n    matters\" 的质疑。 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 是关键回应——同一模型在不同域给出不同 K*，\n    证明 domain 仍是 primary factor。但 reviewer 认为这只是 \"primary, not sole\"。 论文需要从 \"sole\n    determinant\" 降级为 \"primary factor, with residual model effects\"。\n\n    '\n  tables:\n  - name: 'Table 2 (row): Mistral-7B C4 continuation (K*=1 outlier)'\n    content: '| Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |\n\n      |-------|------|------|------|------|------|----|\n\n      | Mistral-7B | 0.984 | 0.594 | 0.540 | 0.523 | 0.518 | 1 |\n\n      | 95% CI (1v2) | — | [0.584, 0.603] | — | — | — | — |\n\n      '\n  figures_description:\n  - Highlighted outlier point in K* summary figure, with cross-scorer validation annotation\n  analysis: 'Median 档核心攻击点之一。论文需要正面讨论 Mistral K*=1 而非 downplay， 并用 Mistral arXiv K*=3\n    证明 domain 仍是 primary driver。 \"Sole determinant\" → \"primary factor\" 的降级措辞是 median\n    档的必要调整。\n\n    '\n- name: exp-020\n  plan_id: exp_020_pythia_decoding\n  description: 'Pythia-1.4B decoding ablation: 4 strategies, C4 5K docs, depth 0-5'\n  expected_results:\n    all_k_star_2: true\n    greedy_1v2: 0.8838\n    nuc09_1v2: 0.677\n    t07_1v2: 0.7265\n    t12_1v2: 0.6172\n  result_rationale: 'Pythia 上 4 种解码策略 K* 全部=2，跨模型复制 exp-003 的解码不变性。 Greedy 1v2=0.8838\n    极高——因为 greedy decoding 引入 repetition collapse， 使 depth 1 和 depth 2 文本差异大。T=1.2\n    的 1v2=0.6172 最低（高温增加随机性，模糊差异）。 Median 档下 reviewer 正面评价跨模型 decoding invariance：\n    \"K*=2 holds across 2 models × 4 decoding strategies = 8 conditions, which is convincing.\"\n    但 greedy 的异常高 AUC 被注意——\"greedy is a degenerate condition that amplifies artifacts,  it\n    shouldn''t be treated as equally valid.\"\n\n    '\n  tables:\n  - name: 'Table A7: Pythia decoding ablation'\n    content: '| Decoding | 1v2 AUC | 2v3 AUC | K* |\n\n      |----------|---------|---------|-----|\n\n      | greedy | 0.884 | 0.534 | 2 |\n\n      | nucleus p=0.9 | 0.677 | 0.555 | 2 |\n\n      | T=0.7 | 0.727 | 0.594 | 2 |\n\n      | T=1.2 | 0.617 | 0.523 | 2 |\n\n      '\n  figures_description: []\n  analysis: 'Supporting evidence，放 Appendix。Greedy 的 repetition collapse 作为 caveat\n    在正文中提及。\n\n    '\n- name: exp-021\n  plan_id: exp_021_length_ablation\n  description: 'Text length ablation: 128/256/512 tokens, Qwen continuation'\n  expected_results:\n    128tok_k_star: 2\n    256tok_k_star: 2\n    512tok_k_star: 2\n    512tok_1v2_ci_lower: 0.5979\n    512tok_verdict: BORDERLINE\n  result_rationale: 'K*=2 在三种长度下一致。但 512tok 的 CI lower=0.5979 < θ 是 borderline failure——\n    在 median 档下 reviewer 注意到 \"longer texts paradoxically reduce discriminability,  which\n    is counter-intuitive and requires explanation.\" 解释：512 tokens 的 continuation 更有空间\n    converge to the generator''s style， 使 depth 1 和 depth 2 更相似。这与 \"one-wash laundering\"\n    概念一致。 但 reviewer 认为 \"if the result flips at 512 tokens, the 256-token headline\n    results  may be cherry-picking the optimal length.\" 论文需要承认 length sensitivity\n    并在主文讨论。\n\n    '\n  tables:\n  - name: 'Table A8: Length ablation'\n    content: '| Length | 1v2 AUC | CI lower | K* |\n\n      |--------|---------|---------|-----|\n\n      | 128 tok | 0.622 | >0.60 | 2 |\n\n      | 256 tok | 0.628 | >0.60 | 2 |\n\n      | 512 tok | 0.607 | 0.598 | 2* |\n\n      '\n  figures_description: []\n  analysis: '512-token borderline 被 median 档 reviewer 视为 minor concern。 与 Qwen-cont\n    CI lower=0.6015 的边缘性一起被归入 \"robustness limitations\" 段。\n\n    '\n- name: exp-022\n  plan_id: exp_022_cross_scorer_matrix\n  description: '4×4 cross-scorer matrix: 4 generators × 4 scorers'\n  expected_results:\n    k_star_2_count: 11\n    k_star_1_count: 1\n    exception: qwen_cont256×pythia (1v2=0.5979)\n    scorer_delta_within_generator: <0.025\n  result_rationale: '11/12 combos K*=2 是 scorer independence 的强证据。 唯一例外 qwen_cont256×pythia\n    (K*=1) 被 reviewer 注意但不被严重攻击—— 因为 Qwen-cont 本身就是最 marginal 的 generator（CI lower=0.6015），\n    换 scorer 后 flip 到 K*=1 是 consistent with its borderline nature。 Median 档下 reviewer\n    正面评价：\"Scorer independence is well-established.  The paper correctly identifies\n    and discusses the single exception.\" 但 A8_attacked 的 reviewer 用这个数据加强攻击：\"Even\n    with different scorers,  Qwen-cont is unstable.\"\n\n    '\n  tables:\n  - name: 'Table 10: Cross-scorer matrix (selected)'\n    content: '| Generator × Scorer | 1v2 AUC | K* |\n\n      |-------------------|---------|-----|\n\n      | Qwen-base × OLMo | 0.605 | 2 |\n\n      | Qwen-base × Pythia | 0.617 | 2 |\n\n      | Qwen-cont × Pythia | 0.598 | 1 |\n\n      | Qwen-cont × Qwen-base | 0.628 | 2 |\n\n      '\n  figures_description:\n  - 4×4 heatmap of K* values in cross-scorer matrix\n  analysis: 'Scorer independence confirmed。论文在正文中展示完整矩阵以预防 \"self-scorer bias\" 攻击。\n\n    '\n- name: exp-023\n  plan_id: exp_023_domain_ablation\n  description: Wikipedia domain, Qwen2.5-1.5B base continuation, 5K docs, depth 0-5\n  expected_results:\n    k_star: 2\n    one_v_two_auc: 0.6193\n    all_folds_above_060: true\n  result_rationale: 'Wikipedia K*=2 (same-family scorer) 但经 D060 cross-scorer confound\n    分析后降为 K*=1。 这是 median 档中 scorer confound 的 key demonstration： Qwen same-family\n    scorer 在 Wikipedia 上给出 +1 bias（K*=2）， 换 Pythia cross-family scorer 后 K*=1。 论文正文报告\n    scorer-controlled K*=1 for Wikipedia, Appendix 披露 confound 细节。 Reviewer 接受 confound\n    控制但质疑：\"If the simplest domain already saturates at K*=1,  and web text at K*=2,\n    the range {1,2,3} is very narrow.  Is the finding essentially that recursive generation\n    quickly loses information?\" 这触发 A1 (\"somewhat expected\")。\n\n    '\n  tables:\n  - name: 'Table 11 (row): Wikipedia domain K*'\n    content: '| Domain | Scorer | 1v2 AUC | K* |\n\n      |--------|--------|---------|-----|\n\n      | Wikipedia | Qwen (same-family) | 0.619 | 2 |\n\n      | Wikipedia | Pythia (cross-family) | 0.585 | 1 |\n\n      | Wikipedia | scorer-controlled | — | 1 |\n\n      '\n  figures_description:\n  - 'Domain ladder figure: Wikipedia(1) < C4(2) < arXiv(3)'\n  analysis: 'Scorer confound on Wikipedia 是 honest reporting，增加论文可信度。 但 K*=1 for Wikipedia\n    被 reviewer 解读为 \"trivial — one generation washes everything.\"\n\n    '\n- name: exp-024\n  plan_id: exp_024_arxiv_domain\n  description: arXiv domain, Qwen2.5-1.5B base continuation, 5K docs, depth 0-5\n  expected_results:\n    k_star: 3\n    pairwise_auc_1v2: 0.858\n    pairwise_auc_2v3: 0.6427\n    ci_2v3_lower: 0.6275\n  result_rationale: 'arXiv K*=3 是 domain dependence 的最强证据——首个 K*>2 的条件。 2v3 AUC=0.6427,\n    CI lower=0.6275 >> θ=0.60（余量 +2.75pp）。 1v2 AUC=0.858 远超 C4/Wiki (~0.61-0.69)，arXiv\n    的 LaTeX/citation/math  结构特征提供额外 depth-distinguishing signal。 Median 档下 reviewer\n    反应： (a) 正面：K*=3 on arXiv is a genuinely interesting finding, domain dependence\n    is well-demonstrated (b) 攻击：A2 假设触发——\"3 domains is too few to claim ''domain is\n    the sole determinant''.  What about code, legal text, news, social media?\" (c)\n    建议：需要更多域来充分支持 domain hierarchy claim 论文需要降级措辞从 \"sole determinant\" 到 \"primary factor\"，\n    承认 3 domains 是 initial evidence 而非 exhaustive characterization。\n\n    '\n  tables:\n  - name: 'Table 11 (row): arXiv domain K*'\n    content: '| Domain | 1v2 AUC | 2v3 AUC | 3v4 AUC | K* |\n\n      |--------|---------|---------|---------|-----|\n\n      | arXiv | 0.858 | 0.643 | 0.544 | 3 |\n\n      '\n  figures_description:\n  - 'AUC decay curves: 3 domains overlaid, showing domain-dependent saturation points'\n  analysis: 'K*=3 on arXiv 是论文的 strongest individual finding，但 3-domain limitation\n    被 reviewer 攻击。 exp_027 LaTeX ablation (K*=3 preserved after stripping) 有效消除格式\n    confound。\n\n    '\n- name: exp-025\n  plan_id: exp_025_pythia_filtering\n  description: 'Pythia-1.4B filtering replication: 3 strategies × 3 seeds'\n  expected_results:\n    all_strategies_nearly_identical: true\n    max_delta_mmlu: 0.0017\n    binary_hellaswag_delta: '+0.0000'\n    key_finding: null result\n  result_rationale: 'Pythia-1.4B 上三种策略产生几乎相同结果（max Δ=0.0017 MMLU），filtering ordering\n    未确认。 Median 档下这是 C3 的严重打击（A5_fail 部分）： (a) Pythia 太小（1.4B, MMLU~0.26）对 filtering\n    signal 不敏感——模型 capacity 不足 (b) 但 reviewer 质疑 \"if filtering doesn''t help even\n    small models, why should we trust  it helps larger ones?\" (c) 论文需要 framing：Pythia\n    的 base capability 太低（MMLU=0.26 接近 random）， filtering 的 marginal benefit 在 low-capability\n    regime 被淹没 (d) 这个 null result 被 1 个 reviewer 肯定（\"honest reporting of negative\n    results\"）， 被另一个 reviewer 用来质疑 C3 整体证据链\n\n    '\n  tables:\n  - name: 'Table A9: Pythia filtering (null result)'\n    content: '| Strategy | MMLU | HellaSwag |\n\n      |----------|------|-----------|\n\n      | binary-ours | 0.259±0.000 | 0.525±0.000 |\n\n      | graduated α=0.9 | 0.256±0.001 | 0.525±0.001 |\n\n      | no-filter | 0.257±0.001 | 0.525±0.001 |\n\n      '\n  figures_description: []\n  analysis: 'Null result。放 Appendix 作为 honest reporting。 C3 的证据链因此完全依赖 exp-006 (Qwen)\n    和 exp-009 (dose-response)。 Median 档 reviewer 评价 C3 substance ~2.5。\n\n    '\n- name: exp-026",
      "numLines": 800,
      "startLine": 200,
      "totalLines": 1260
    }
  },
  "sourceToolAssistantUUID": "d5c70234-b9ce-4e87-9329-4d8d65c427c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑 核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domai…",
  "leafUuid": "9ab724ef-9c6e-4cfa-872f-78f8cf0de49d",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-dependent K* saturation with cross-model validation",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Tool call

_source line 20 · 2026-05-19T09:21:01.393Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AvmUixnMbe3QFbK2ZhVoV5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
  "offset": 999,
  "limit": 800
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ab724ef-9c6e-4cfa-872f-78f8cf0de49d",
  "isSidechain": false,
  "requestId": "req_011CbBgTDNwCajLSV7ZvySPo",
  "type": "assistant",
  "uuid": "c9ff52b8-50dd-4689-8892-70f3ff037419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RfLMUaZ7SKVHyN4jwgs6cM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15747,
      "cache_read_input_tokens": 79706,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 79706,
          "cache_creation_input_tokens": 15747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15747
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

### Tool result

_source line 21 · 2026-05-19T09:21:01.398Z_

<details><summary>↩ Tool result · `toolu_01AvmUixnMbe3QFbK2ZhVoV5`</summary>

```text
999	- name: exp-026
1000	  plan_id: exp_026_arxiv_filtering
1001	  description: 'arXiv graduated vs binary filtering: Qwen base + LoRA, K*=3 domain,
1002	    3 strategies × 5 seeds'
1003	  expected_results:
1004	    graduated_equals_no_filter: true
1005	    binary_mmlu_delta: '-0.0023'
1006	    binary_hellaswag_delta: '+0.0042'
1007	    graduated_mmlu_delta: '+0.0001'
1008	    graduated_hellaswag_delta: '-0.0001'
1009	    key_finding: null result — graduated ≈ no_filter on K*=3 domain
1010	  result_rationale: '这是 C3 的 fatal blow：即使在 K*=3 域（理论上 graduated 应该有优势）， graduated
1011	    ≈ no_filter，binary 有 metric-specific trade-off（MMLU -0.23pp, HellaSwag +0.42pp）。
1012	    Median 档下 A5_fail 完全触发： (a) "If graduated filtering fails even on K*=3 where it
1013	    should work best,  the entire K*-aware curation thesis is undermined" (b) 论文需要将
1014	    C3 降级为 "case study" 而非 "validation" (c) 关键 insight（放 Discussion）：K* characterizes
1015	    signal discriminability,  not data utility — depth 2-3 text is statistically distinguishable
1016	    but removing it  doesn''t improve training (d) Binary filtering 的 HellaSwag 优势可能来自
1017	    removing any synthetic data  (regardless of depth)，而非 depth-aware curation (e)
1018	    1 个 reviewer 肯定这个 negative result 的 honesty， 但另一个 reviewer 认为 C3 整体不成立
1019	
1020	    '
1021	  tables:
1022	  - name: 'Table 12: arXiv filtering results (negative)'
1023	    content: '| Strategy | MMLU | HellaSwag | Δ MMLU | Δ HellaSwag |
1024	
1025	      |----------|------|-----------|--------|-------------|
1026	
1027	      | no-filter | 0.590±0.001 | 0.660±0.000 | — | — |
1028	
1029	      | binary | 0.588±0.000 | 0.664±0.000 | -0.002 | +0.004* |
1030	
1031	      | graduated α=0.9 | 0.590±0.001 | 0.660±0.000 | +0.000 | -0.000 |
1032	
1033	      '
1034	  figures_description: []
1035	  analysis: 'Negative result honestly reported。Section 5 adds this as "boundary conditions
1036	    of K*-aware curation." Discussion adds key insight: "K* ≠ data utility."  Median
1037	    档 negative_result_credibility_boost = 0.0-0.5（modest boost from honesty,  offset
1038	    by weakened C3）。
1039	
1040	    '
1041	- name: exp-027
1042	  plan_id: exp_027_latex_ablation
1043	  description: LaTeX markup removal ablation on arXiv data
1044	  expected_results:
1045	    k_star_preserved: true
1046	    original_2v3: 0.6436
1047	    stripped_2v3: 0.6229
1048	    delta_2v3: -0.021
1049	  result_rationale: 'K*=3 在去除 LaTeX 标记后保持，2v3 AUC 从 0.6436 降至 0.6229 但仍 > θ=0.60。
1050	    LaTeX 格式贡献约 2pp AUC 但不是 K*=3 的 confound。 Median 档下 reviewer 正面评价："Good ablation
1051	    that rules out the obvious confound.  K*=3 on arXiv is driven by content structural
1052	    complexity, not just formatting." 但 reviewer 注意到 stripped 2v3=0.6229 余量仅 +2.29pp，如果进一步去除  other
1053	    structural markers (citation patterns, section numbering), K* 可能降至 2。
1054	
1055	    '
1056	  tables:
1057	  - name: 'Table A10: LaTeX ablation'
1058	    content: '| Condition | 1v2 AUC | 2v3 AUC | K* |
1059	
1060	      |-----------|---------|---------|-----|
1061	
1062	      | Original | 0.858 | 0.644 | 3 |
1063	
1064	      | LaTeX stripped | 0.830 | 0.623 | 3 |
1065	
1066	      | Δ | -0.028 | -0.021 | — |
1067	
1068	      '
1069	  figures_description: []
1070	  analysis: 'Effective confound control。Median 档 reviewer 不攻击此实验。
1071	
1072	    '
1073	- name: exp-028
1074	  plan_id: ''
1075	  description: 'Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples'
1076	  expected_results:
1077	    n_1000_k_star_2_rate: 6-7/10 (unstable)
1078	    n_2000_k_star_2_rate: 8-9/10 (mostly stable)
1079	    n_3000_k_star_2_rate: 9-10/10 (stable)
1080	    n_5000_k_star_2_rate: 10/10 (robust)
1081	    minimum_n_for_robust_k_star: ~2500-3000
1082	    ci_width_at_n_1000: ±0.025-0.030
1083	    ci_width_at_n_5000: ±0.010-0.012
1084	  result_rationale: 'Power analysis 在 median 档下是 reviewer 可能要求但非 P0 的实验。如果执行： n=1000
1085	    时 CI 太宽（±2.5-3.0pp），K*=2 判定在约 60-70% resamples 中成立——不 robust。 n=3000 时稳定，n=5000
1086	    完全 robust。 这回应了 reviewer 对 sample size 的潜在质疑，并提供 practical guidance： "K*=2 判定需要
1087	    ≥2500 samples per depth pair for 90% power." Median 档下如果缺少此实验，reviewer 可能在 Minor
1088	    Revisions 中要求补充。 如果存在，被评为 "useful methodological contribution for practitioners."
1089	
1090	    '
1091	  tables:
1092	  - name: 'Table A11: Subsampling power curve'
1093	    content: '| n | K*=2 rate | 1v2 CI width | Median 1v2 AUC |
1094	
1095	      |------|-----------|-------------|---------------|
1096	
1097	      | 1000 | 65% | ±0.028 | 0.652 |
1098	
1099	      | 2000 | 85% | ±0.019 | 0.653 |
1100	
1101	      | 3000 | 95% | ±0.015 | 0.654 |
1102	
1103	      | 4000 | 98% | ±0.012 | 0.654 |
1104	
1105	      | 5000 | 100% | ±0.010 | 0.654 |
1106	
1107	      '
1108	  figures_description:
1109	  - 'Power curve: K*=2 detection rate as function of sample size'
1110	  analysis: '未执行（planned）。如果在 rebuttal 中补充，可回应 "statistical power" 质疑。 Median 档 reviewer
1111	    不会因缺失此实验降分但可能作为 minor revision 要求。
1112	
1113	    '
1114	- name: exp_arXiv_cross_validation (5-model)
1115	  plan_id: exp_arXiv_llama8b / exp_arXiv_mistral7b / exp_arXiv_qwen7b / exp_025_pythia_arxiv
1116	  description: 'arXiv K*=3 cross-validation: 5 models × 4 architecture families'
1117	  expected_results:
1118	    qwen_1b5_k_star: 3
1119	    pythia_k_star: 3
1120	    llama_8b_k_star: 3
1121	    mistral_7b_k_star: 3
1122	    qwen_7b_k_star: 3
1123	    olmo_k_star: 1
1124	    domain_competent_models_k3_rate: 5/5 (100%)
1125	    olmo_capacity_failure: true
1126	  result_rationale: '五个 domain-competent 模型在 arXiv 上 100% 一致 K*=3（跨 4 架构族）。 OLMo-1B
1127	    K*=1 因 capacity failure（生成出域文本）。 Median 档下 reviewer 高度正面评价 domain dependence evidence：
1128	    "5/5 domain-competent models all yielding K*=3 on arXiv is strong cross-validation."
1129	    但 A2 仍被触发——"Even with 5-model cross-validation, 3 domains is still 3 domains.  The
1130	    domain hierarchy Wikipedia(1)&lt;C4(2)&lt;arXiv(3) could just be ordered by text complexity."
1131	    Reviewer 建议增加 code/legal/social media domains。 OLMo capacity failure 被正面引用："Correctly
1132	    identified as prerequisite analysis,  not counted against the domain claim."
1133	
1134	    '
1135	  tables:
1136	  - name: 'Table 13: arXiv K*=3 cross-validation'
1137	    content: '| Model | Family | 2v3 AUC | K* |
1138	
1139	      |-------|--------|---------|-----|
1140	
1141	      | Qwen-1.5B | Qwen | 0.643 | 3 |
1142	
1143	      | Pythia-1.4B | GPT-NeoX | 0.654 | 3 |
1144	
1145	      | LLaMA-8B | LLaMA | 0.622 | 3 |
1146	
1147	      | Mistral-7B | Mistral | 0.628 | 3 |
1148	
1149	      | Qwen-7B | Qwen | 0.626 | 3 |
1150	
1151	      | OLMo-1B | OLMo | 0.503 | 1 (capacity fail) |
1152	
1153	      '
1154	  figures_description:
1155	  - 'Bar chart: arXiv 2v3 AUC across 5 models, all > θ=0.60 (except OLMo marked separately)'
1156	  analysis: 'Domain dependence 的 crown jewel evidence。Mistral C4 K*=1 → arXiv K*=3
1157	    的跃变 是论文最有说服力的 single finding。Median 档 reviewer 评分： soundness 3.0-3.5 for C1''
1158	    domain dependence sub-claim。
1159	
1160	    '
1161	- name: exp_wiki_scorer_confound
1162	  plan_id: D060 scorer confound analysis
1163	  description: 'Wikipedia scorer confound: Qwen same-family vs Pythia cross-family
1164	    scorer'
1165	  expected_results:
1166	    qwen_scorer_k_star: 2
1167	    pythia_crossscorer_k_star: 1
1168	    critical_delta_1v2: -0.024
1169	    confound_verdict: confirmed
1170	  result_rationale: 'Wikipedia 上 Qwen same-family scorer 给出 K*=2，换 Pythia cross-family
1171	    scorer 后降为 K*=1。 Δ1v2=-0.024 证明 +1 bias 存在。Median 档下： (a) Reviewer 肯定 confound
1172	    detection and control："Good scientific practice to identify  and report scorer
1173	    bias." (b) 论文正文报告 K*=1 (scorer-controlled)，增加可信度 (c) 但 reviewer 追问："If same-family
1174	    scorer bias exists on Wikipedia,  could it also affect C4 results (e.g., Qwen-cont
1175	    CI lower=0.6015)?" (d) Exp-022 的 cross-scorer matrix 部分回应这个问题（C4 上 11/12 K*=2），
1176	    但 Qwen-cont×Pythia K*=1 加剧 concern
1177	
1178	    '
1179	  tables:
1180	  - name: 'Table A12: Wikipedia scorer confound'
1181	    content: '| Scorer | 1v2 AUC | K* |
1182	
1183	      |--------|---------|-----|
1184	
1185	      | Qwen (same-family) | 0.619 | 2 |
1186	
1187	      | Pythia (cross-family) | 0.587 | 1 |
1188	
1189	      '
1190	  figures_description: []
1191	  analysis: 'Honest reporting 增加论文可信度。Median 档 reviewer 正面评价但用此质疑 C4 结果。
1192	
1193	    '
1194	- name: exp_14b_c4
1195	  plan_id: scale extension
1196	  description: Qwen2.5-14B, continuation mode, C4, depth 0-5 — scale extension for
1197	    rebuttal
1198	  expected_results:
1199	    k_star: 2
1200	    pairwise_auc_1v2: 0.621
1201	    ci_1v2_lower: 0.6119
1202	    ci_1v2_upper: 0.6304
1203	  result_rationale: '14B scale 下 K*=2 维持，CI lower=0.6119 > θ（余量 +1.19pp）。 这是回应 A3
1204	    (scale limitation) 的关键 rebuttal evidence： "K*=2 is confirmed from 1.4B to 14B
1205	    (10× scale range), with consistent CI lower > θ." Median 档下如果在 rebuttal 中呈现： (a)
1206	    1 个 reviewer 接受 "14B extends the scale range meaningfully" (b) 但要求 32B 数据来确认 trend
1207	    (c) exp_32b_c4 正在运行——如果也是 K*=2，rebuttal 极大增强
1208	
1209	    '
1210	  tables:
1211	  - name: 'Rebuttal Table R1: Scale extension'
1212	    content: '| Scale | 1v2 AUC | CI lower | K* |
1213	
1214	      |-------|---------|---------|-----|
1215	
1216	      | 1.4B (Pythia) | 0.654 | 0.645 | 2 |
1217	
1218	      | 1.5B (Qwen) | 0.611 | 0.602 | 2 |
1219	
1220	      | 7B (Qwen) | 0.618 | 0.608 | 2 |
1221	
1222	      | 8B (LLaMA) | 0.612 | 0.603 | 2 |
1223	
1224	      | 14B (Qwen) | 0.621 | 0.612 | 2 |
1225	
1226	      '
1227	  figures_description:
1228	  - 'Scale plot: K* and 1v2 AUC as function of model size — flat trend confirms scale
1229	    invariance'
1230	  analysis: 'Rebuttal 核心证据。1.4B→14B 10× scale range 下 K*=2 一致。 如果 32B 也确认，可有效回应 A3，将
1231	    reviewer 从 "significant weakness" 降为 "minor limitation"。
1232	
1233	    '
1234	- name: exp_026_arxiv_filtering_integrated
1235	  plan_id: what_if
1236	  description: arXiv graduated filtering negative result integrated into paper narrative
1237	  expected_results:
1238	    section_5_addition: arXiv null result table with paired t-tests
1239	    discussion_insight: K* ≠ data utility
1240	    negative_result_credibility_boost: 0.0-0.5
1241	    c3_downgrade: validation → case study
1242	  result_rationale: '将 exp-026 negative result 正式整合入论文：Section 5 增加 arXiv null result，
1243	    Discussion 增加 "K* characterizes discriminability, not utility" 洞察。 Median 档下的效果：
1244	    (a) 1 个 reviewer 明确肯定 honest reporting："The authors'' willingness to report  negative
1245	    results and adjust claims accordingly is commendable." (b) 但 credibility boost
1246	    被 C3 整体弱化所抵消——honestly reporting failure  doesn''t make the contribution stronger,
1247	    it just makes the paper more trustworthy (c) "K* ≠ data utility" insight 被 1 个
1248	    reviewer 视为 "interesting secondary finding" 但另一个 reviewer 认为 "this undermines
1249	    the practical motivation of the paper" (d) C3 contribution 从 "validation that
1250	    K* informs optimal filtering granularity"  降级为 "case study demonstrating that
1251	    K*-aware binary filtering provides modest  improvement on web text, with boundary
1252	    conditions on other domains"
1253	
1254	    '
1255	  tables: []
1256	  figures_description: []
1257	  analysis: 整合 negative results 是 median 档下的最优策略。 完全不报告 → reviewer 如果知道了会更严厉；过度辩护
1258	    → 不可信。 "Case study" framing 是平衡点：承认 limitation 但保留 positive evidence (exp-006,
1259	    exp-009)。
1260	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9ff52b8-50dd-4689-8892-70f3ff037419",
  "isSidechain": false,
  "promptId": "59587622-660c-4957-a549-a3c2036a769c",
  "type": "user",
  "uuid": "cda8ecaf-53cb-4bbe-b7e6-3c56ef1b9502",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/dream_reports/dream_20260518T125757/median/imagined_experiments.yaml",
      "content": "- name: exp-026\n  plan_id: exp_026_arxiv_filtering\n  description: 'arXiv graduated vs binary filtering: Qwen base + LoRA, K*=3 domain,\n    3 strategies × 5 seeds'\n  expected_results:\n    graduated_equals_no_filter: true\n    binary_mmlu_delta: '-0.0023'\n    binary_hellaswag_delta: '+0.0042'\n    graduated_mmlu_delta: '+0.0001'\n    graduated_hellaswag_delta: '-0.0001'\n    key_finding: null result — graduated ≈ no_filter on K*=3 domain\n  result_rationale: '这是 C3 的 fatal blow：即使在 K*=3 域（理论上 graduated 应该有优势）， graduated\n    ≈ no_filter，binary 有 metric-specific trade-off（MMLU -0.23pp, HellaSwag +0.42pp）。\n    Median 档下 A5_fail 完全触发： (a) \"If graduated filtering fails even on K*=3 where it\n    should work best,  the entire K*-aware curation thesis is undermined\" (b) 论文需要将\n    C3 降级为 \"case study\" 而非 \"validation\" (c) 关键 insight（放 Discussion）：K* characterizes\n    signal discriminability,  not data utility — depth 2-3 text is statistically distinguishable\n    but removing it  doesn''t improve training (d) Binary filtering 的 HellaSwag 优势可能来自\n    removing any synthetic data  (regardless of depth)，而非 depth-aware curation (e)\n    1 个 reviewer 肯定这个 negative result 的 honesty， 但另一个 reviewer 认为 C3 整体不成立\n\n    '\n  tables:\n  - name: 'Table 12: arXiv filtering results (negative)'\n    content: '| Strategy | MMLU | HellaSwag | Δ MMLU | Δ HellaSwag |\n\n      |----------|------|-----------|--------|-------------|\n\n      | no-filter | 0.590±0.001 | 0.660±0.000 | — | — |\n\n      | binary | 0.588±0.000 | 0.664±0.000 | -0.002 | +0.004* |\n\n      | graduated α=0.9 | 0.590±0.001 | 0.660±0.000 | +0.000 | -0.000 |\n\n      '\n  figures_description: []\n  analysis: 'Negative result honestly reported。Section 5 adds this as \"boundary conditions\n    of K*-aware curation.\" Discussion adds key insight: \"K* ≠ data utility.\"  Median\n    档 negative_result_credibility_boost = 0.0-0.5（modest boost from honesty,  offset\n    by weakened C3）。\n\n    '\n- name: exp-027\n  plan_id: exp_027_latex_ablation\n  description: LaTeX markup removal ablation on arXiv data\n  expected_results:\n    k_star_preserved: true\n    original_2v3: 0.6436\n    stripped_2v3: 0.6229\n    delta_2v3: -0.021\n  result_rationale: 'K*=3 在去除 LaTeX 标记后保持，2v3 AUC 从 0.6436 降至 0.6229 但仍 > θ=0.60。\n    LaTeX 格式贡献约 2pp AUC 但不是 K*=3 的 confound。 Median 档下 reviewer 正面评价：\"Good ablation\n    that rules out the obvious confound.  K*=3 on arXiv is driven by content structural\n    complexity, not just formatting.\" 但 reviewer 注意到 stripped 2v3=0.6229 余量仅 +2.29pp，如果进一步去除  other\n    structural markers (citation patterns, section numbering), K* 可能降至 2。\n\n    '\n  tables:\n  - name: 'Table A10: LaTeX ablation'\n    content: '| Condition | 1v2 AUC | 2v3 AUC | K* |\n\n      |-----------|---------|---------|-----|\n\n      | Original | 0.858 | 0.644 | 3 |\n\n      | LaTeX stripped | 0.830 | 0.623 | 3 |\n\n      | Δ | -0.028 | -0.021 | — |\n\n      '\n  figures_description: []\n  analysis: 'Effective confound control。Median 档 reviewer 不攻击此实验。\n\n    '\n- name: exp-028\n  plan_id: ''\n  description: 'Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples'\n  expected_results:\n    n_1000_k_star_2_rate: 6-7/10 (unstable)\n    n_2000_k_star_2_rate: 8-9/10 (mostly stable)\n    n_3000_k_star_2_rate: 9-10/10 (stable)\n    n_5000_k_star_2_rate: 10/10 (robust)\n    minimum_n_for_robust_k_star: ~2500-3000\n    ci_width_at_n_1000: ±0.025-0.030\n    ci_width_at_n_5000: ±0.010-0.012\n  result_rationale: 'Power analysis 在 median 档下是 reviewer 可能要求但非 P0 的实验。如果执行： n=1000\n    时 CI 太宽（±2.5-3.0pp），K*=2 判定在约 60-70% resamples 中成立——不 robust。 n=3000 时稳定，n=5000\n    完全 robust。 这回应了 reviewer 对 sample size 的潜在质疑，并提供 practical guidance： \"K*=2 判定需要\n    ≥2500 samples per depth pair for 90% power.\" Median 档下如果缺少此实验，reviewer 可能在 Minor\n    Revisions 中要求补充。 如果存在，被评为 \"useful methodological contribution for practitioners.\"\n\n    '\n  tables:\n  - name: 'Table A11: Subsampling power curve'\n    content: '| n | K*=2 rate | 1v2 CI width | Median 1v2 AUC |\n\n      |------|-----------|-------------|---------------|\n\n      | 1000 | 65% | ±0.028 | 0.652 |\n\n      | 2000 | 85% | ±0.019 | 0.653 |\n\n      | 3000 | 95% | ±0.015 | 0.654 |\n\n      | 4000 | 98% | ±0.012 | 0.654 |\n\n      | 5000 | 100% | ±0.010 | 0.654 |\n\n      '\n  figures_description:\n  - 'Power curve: K*=2 detection rate as function of sample size'\n  analysis: '未执行（planned）。如果在 rebuttal 中补充，可回应 \"statistical power\" 质疑。 Median 档 reviewer\n    不会因缺失此实验降分但可能作为 minor revision 要求。\n\n    '\n- name: exp_arXiv_cross_validation (5-model)\n  plan_id: exp_arXiv_llama8b / exp_arXiv_mistral7b / exp_arXiv_qwen7b / exp_025_pythia_arxiv\n  description: 'arXiv K*=3 cross-validation: 5 models × 4 architecture families'\n  expected_results:\n    qwen_1b5_k_star: 3\n    pythia_k_star: 3\n    llama_8b_k_star: 3\n    mistral_7b_k_star: 3\n    qwen_7b_k_star: 3\n    olmo_k_star: 1\n    domain_competent_models_k3_rate: 5/5 (100%)\n    olmo_capacity_failure: true\n  result_rationale: '五个 domain-competent 模型在 arXiv 上 100% 一致 K*=3（跨 4 架构族）。 OLMo-1B\n    K*=1 因 capacity failure（生成出域文本）。 Median 档下 reviewer 高度正面评价 domain dependence evidence：\n    \"5/5 domain-competent models all yielding K*=3 on arXiv is strong cross-validation.\"\n    但 A2 仍被触发——\"Even with 5-model cross-validation, 3 domains is still 3 domains.  The\n    domain hierarchy Wikipedia(1)&lt;C4(2)&lt;arXiv(3) could just be ordered by text complexity.\"\n    Reviewer 建议增加 code/legal/social media domains。 OLMo capacity failure 被正面引用：\"Correctly\n    identified as prerequisite analysis,  not counted against the domain claim.\"\n\n    '\n  tables:\n  - name: 'Table 13: arXiv K*=3 cross-validation'\n    content: '| Model | Family | 2v3 AUC | K* |\n\n      |-------|--------|---------|-----|\n\n      | Qwen-1.5B | Qwen | 0.643 | 3 |\n\n      | Pythia-1.4B | GPT-NeoX | 0.654 | 3 |\n\n      | LLaMA-8B | LLaMA | 0.622 | 3 |\n\n      | Mistral-7B | Mistral | 0.628 | 3 |\n\n      | Qwen-7B | Qwen | 0.626 | 3 |\n\n      | OLMo-1B | OLMo | 0.503 | 1 (capacity fail) |\n\n      '\n  figures_description:\n  - 'Bar chart: arXiv 2v3 AUC across 5 models, all > θ=0.60 (except OLMo marked separately)'\n  analysis: 'Domain dependence 的 crown jewel evidence。Mistral C4 K*=1 → arXiv K*=3\n    的跃变 是论文最有说服力的 single finding。Median 档 reviewer 评分： soundness 3.0-3.5 for C1''\n    domain dependence sub-claim。\n\n    '\n- name: exp_wiki_scorer_confound\n  plan_id: D060 scorer confound analysis\n  description: 'Wikipedia scorer confound: Qwen same-family vs Pythia cross-family\n    scorer'\n  expected_results:\n    qwen_scorer_k_star: 2\n    pythia_crossscorer_k_star: 1\n    critical_delta_1v2: -0.024\n    confound_verdict: confirmed\n  result_rationale: 'Wikipedia 上 Qwen same-family scorer 给出 K*=2，换 Pythia cross-family\n    scorer 后降为 K*=1。 Δ1v2=-0.024 证明 +1 bias 存在。Median 档下： (a) Reviewer 肯定 confound\n    detection and control：\"Good scientific practice to identify  and report scorer\n    bias.\" (b) 论文正文报告 K*=1 (scorer-controlled)，增加可信度 (c) 但 reviewer 追问：\"If same-family\n    scorer bias exists on Wikipedia,  could it also affect C4 results (e.g., Qwen-cont\n    CI lower=0.6015)?\" (d) Exp-022 的 cross-scorer matrix 部分回应这个问题（C4 上 11/12 K*=2），\n    但 Qwen-cont×Pythia K*=1 加剧 concern\n\n    '\n  tables:\n  - name: 'Table A12: Wikipedia scorer confound'\n    content: '| Scorer | 1v2 AUC | K* |\n\n      |--------|---------|-----|\n\n      | Qwen (same-family) | 0.619 | 2 |\n\n      | Pythia (cross-family) | 0.587 | 1 |\n\n      '\n  figures_description: []\n  analysis: 'Honest reporting 增加论文可信度。Median 档 reviewer 正面评价但用此质疑 C4 结果。\n\n    '\n- name: exp_14b_c4\n  plan_id: scale extension\n  description: Qwen2.5-14B, continuation mode, C4, depth 0-5 — scale extension for\n    rebuttal\n  expected_results:\n    k_star: 2\n    pairwise_auc_1v2: 0.621\n    ci_1v2_lower: 0.6119\n    ci_1v2_upper: 0.6304\n  result_rationale: '14B scale 下 K*=2 维持，CI lower=0.6119 > θ（余量 +1.19pp）。 这是回应 A3\n    (scale limitation) 的关键 rebuttal evidence： \"K*=2 is confirmed from 1.4B to 14B\n    (10× scale range), with consistent CI lower > θ.\" Median 档下如果在 rebuttal 中呈现： (a)\n    1 个 reviewer 接受 \"14B extends the scale range meaningfully\" (b) 但要求 32B 数据来确认 trend\n    (c) exp_32b_c4 正在运行——如果也是 K*=2，rebuttal 极大增强\n\n    '\n  tables:\n  - name: 'Rebuttal Table R1: Scale extension'\n    content: '| Scale | 1v2 AUC | CI lower | K* |\n\n      |-------|---------|---------|-----|\n\n      | 1.4B (Pythia) | 0.654 | 0.645 | 2 |\n\n      | 1.5B (Qwen) | 0.611 | 0.602 | 2 |\n\n      | 7B (Qwen) | 0.618 | 0.608 | 2 |\n\n      | 8B (LLaMA) | 0.612 | 0.603 | 2 |\n\n      | 14B (Qwen) | 0.621 | 0.612 | 2 |\n\n      '\n  figures_description:\n  - 'Scale plot: K* and 1v2 AUC as function of model size — flat trend confirms scale\n    invariance'\n  analysis: 'Rebuttal 核心证据。1.4B→14B 10× scale range 下 K*=2 一致。 如果 32B 也确认，可有效回应 A3，将\n    reviewer 从 \"significant weakness\" 降为 \"minor limitation\"。\n\n    '\n- name: exp_026_arxiv_filtering_integrated\n  plan_id: what_if\n  description: arXiv graduated filtering negative result integrated into paper narrative\n  expected_results:\n    section_5_addition: arXiv null result table with paired t-tests\n    discussion_insight: K* ≠ data utility\n    negative_result_credibility_boost: 0.0-0.5\n    c3_downgrade: validation → case study\n  result_rationale: '将 exp-026 negative result 正式整合入论文：Section 5 增加 arXiv null result，\n    Discussion 增加 \"K* characterizes discriminability, not utility\" 洞察。 Median 档下的效果：\n    (a) 1 个 reviewer 明确肯定 honest reporting：\"The authors'' willingness to report  negative\n    results and adjust claims accordingly is commendable.\" (b) 但 credibility boost\n    被 C3 整体弱化所抵消——honestly reporting failure  doesn''t make the contribution stronger,\n    it just makes the paper more trustworthy (c) \"K* ≠ data utility\" insight 被 1 个\n    reviewer 视为 \"interesting secondary finding\" 但另一个 reviewer 认为 \"this undermines\n    the practical motivation of the paper\" (d) C3 contribution 从 \"validation that\n    K* informs optimal filtering granularity\"  降级为 \"case study demonstrating that\n    K*-aware binary filtering provides modest  improvement on web text, with boundary\n    conditions on other domains\"\n\n    '\n  tables: []\n  figures_description: []\n  analysis: 整合 negative results 是 median 档下的最优策略。 完全不报告 → reviewer 如果知道了会更严厉；过度辩护\n    → 不可信。 \"Case study\" framing 是平衡点：承认 limitation 但保留 positive evidence (exp-006,\n    exp-009)。\n",
      "numLines": 262,
      "startLine": 999,
      "totalLines": 1260
    }
  },
  "sourceToolAssistantUUID": "c9ff52b8-50dd-4689-8892-70f3ff037419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-19T09:21:59.154Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the previous median tier imagined experiments from dream_20260518T125757. But the user is asking me to generate a NEW median tier imagined experiments output based on the CURRENT state of experiments (which now includes Code domain results, 4-domain coverage, retrain K*=7, etc.).

The key differences from the previous dream:
1. Code domain is now a 4th domain (Wiki=1, C4=2, Code=2, arXiv=3)
2. LLaMA-8B Code K*=2 confirmed (cross-family)


3. Qwen-1.5B Code K*=2 and Pythia-1.4B Code K*=1 are in, while Mistral-7B and Qwen-7B Code results are still pending
4. I'm also tracking the retrain K*=7 experiments across Qwen and Pythia families, plus validating the Code domain findings with cross-scorer checks
5. The median tier framework needs to account for the partial Code domain confirmation and address reviewer concerns about the domain ceiling approach and θ-sensitivity
6. Looking at the specific results: Mistral-7B Code shows K*=1 consistent with the broader pattern, Qwen-7B Code reaches K*=2 but with marginal confidence intervals, and only 3 of 5 models hit the ceiling—so I should soften that claim to models with sufficient code training
7. The arXiv cross-scorer validation showed Qwen-7B dropping from K*=3 to K*=2, which suggests potential scorer confounds, and one reviewer flagged concerns about how the negative C3 results affect practical relevance
8. I'm examining the AUC ranges for Mistral-7B and Qwen-7B across the 1v2 comparison to assess the robustness of these findings and determine how much θ-sensitivity analysis I need to include.

Now I'm compiling the full metric ranges across all experiments and need to generate YAML predictions for each one, covering both the completed experiments with actual data and the running experiments where I'll provide median-tier estimates. I need to pull together all the experiments from the registry—the Code domain ones that are currently running, the arXiv and wiki experiments, plus the retrain chain work—and provide detailed data predictions for each one in the YAML output. I'm seeing the performance patterns across the code domain experiments—Mistral-7B maxes out at K*=1 with AUC around 0.56-0.62, while Qwen-7B reaches K*=2 but only marginally, and the ceiling of K*=2 is only achievable by three of the five models tested. There's also that concerning signal from the arXiv Qwen-7B cross-scorer where K* appears to drop from 3 to 2. Now I'm going to write out the complete YAML with all experiments, prioritizing detail for the new code domain work and the retrain depth experiments while keeping the established ones more concise. I need to clarify which experiments to include—the user is asking for the ones listed in the experiment_plan section of the CLAUDE.md file, which runs from mvp-001 through exp-028, rather than all the additional experiments in the registry that weren't part of the original plan. I need to organize all these experiments into a structured YAML format, grouping them by category: C4 domain work, decoding and methodology variations, domain-specific experiments, cross-model transfer, filtering approaches, and baselines.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cda8ecaf-53cb-4bbe-b7e6-3c56ef1b9502",
  "isSidechain": false,
  "requestId": "req_011CbBgTrTs5JC55rHVYi4RD",
  "type": "assistant",
  "uuid": "7fba02ca-31e3-4afa-8d04-049c98f87a54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvCQ7s7pGjXvH4wYvzL8w5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5421,
      "cache_read_input_tokens": 95453,
      "output_tokens": 30293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 30293,
          "cache_read_input_tokens": 95453,
          "cache_creation_input_tokens": 5421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5421
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

_source line 23 · 2026-05-19T09:30:28.767Z_

Now I have full context on the experiment plan, registry, and previous median dream. Let me generate the complete median-tier imagined experiments for the current state (with Code domain, 4-domain hierarchy, retrain K*=7, and RUNNING experiments).

```yaml
tier: median
narrative_guidance: >
  C1' 核心成立但 claims 需降级。Domain ceiling 从 "predictive framework" 调整为
  "empirical tendency with domain×competence interaction"：中间复杂度域（C4, Code）
  的 K* 受 model domain-specific competence 调制，极端域（Wiki, arXiv）稳健。
  Code 域叙事从 "ceiling=2 cross-family confirmed" 改为 "ceiling=2 observed in
  models with adequate code pretraining (Qwen, LLaMA); insufficient code competence
  yields K*=1 (Pythia, Mistral), consistent with C4 Mistral pattern"。C3 的 scope
  在 Limitations 中更显著呈现，承认 filtering advantage 限于 homogeneous web text +
  单一 base model (Qwen-1.5B)，不泛化到 arXiv 或其他 base models。补充实验：可能
  需要 arXiv cross-scorer bootstrap CI 的完整呈现、θ-sensitivity full sweep figure。
  目标 EMNLP Findings 或 borderline Main。审稿人对 Code 域结果的解读分裂：
  Reviewer A 认为 3/5 models at ceiling 已足够 establish pattern，Reviewer B 认为
  2/5 failure 暗示 ceiling 框架 overfits 已有数据。arXiv Qwen-7B cross-scorer
  K*=3→2 的下降被一位审稿人视为 scorer confound 未完全控制的证据。θ-sensitivity
  被要求做更详细分析（θ=0.55-0.70 全谱呈现）。整体 excitement 3.3-3.7，
  EMNLP Main accept prob 0.25-0.50。
imagined_experiments:
  - name: mvp-001
    plan_id: mvp_pilot_sat_v1
    description: Qwen2.5-1.5B-Instruct rewrite mode pilot, C4 5K docs, depth 0-5
    expected_results:
      k_star: 2
      pairwise_auc_0v1: 0.9956
      pairwise_auc_1v2: 0.6957
      pairwise_auc_2v3: 0.5893
      pairwise_auc_3v4: 0.5434
      pairwise_auc_4v5: 0.5343
      ci_1v2: "[0.6859, 0.7041]"
      ordinal_accuracy: 0.4182
      ordinal_mae: 1.0163
    result_rationale: >
      Rewrite mode 的 instruction-following 注入 mode-specific style artifacts（如固定的段落结构、
      总结性结尾句式），人为放大 depth signal 至 1v2 AUC=0.6957。在 median 档下，reviewer 注意到
      rewrite mode 的高 AUC 不能代表 canonical condition，要求论文明确将此实验定位为
      "pilot study demonstrating feasibility"。2v3=0.5893 < θ=0.60 确认 K*=2。
      Reviewer 接受此实验作为 motivation 但要求所有 cross-model claims 基于 continuation mode。
      与 continuation mode（1v2=0.6112）的 8.4pp gap 说明 generation mode 是显著 confound。
    tables:
      - name: "Table 1 (partial): Pairwise AUC — MVP pilot"
        content: |
          | Pair | AUC    | 95% CI           | > θ=0.60? |
          |------|--------|------------------|-----------|
          | 0v1  | 0.9956 | [0.9946, 0.9965] | ✅ (+39.5pp) |
          | 1v2  | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp)  |
          | 2v3  | 0.5893 | [0.5795, 0.5991] | ❌           |
          | 3v4  | 0.5434 | [0.5333, 0.5551] | ❌           |
          | 4v5  | 0.5343 | [0.5238, 0.5448] | ❌           |
    figures_description:
      - "AUC decay curve (rewrite mode) — Introduction motivation figure，展示 sharp K*=2 boundary"
    analysis: >
      Reviewer A 接受 rewrite mode 作为 pilot。Reviewer B 质疑为何论文以 rewrite AUC
      为 headline 而非 continuation——cherry-picking 嫌疑。Median 档下需在论文中明确标注
      mvp-001 为 pilot，所有 headline number 基于 continuation mode。

  - name: exp-001
    plan_id: exp_001_pythia_depth
    description: "Pythia-1.4B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5"
    expected_results:
      k_star: 2
      pairwise_auc_0v1: 0.9932
      pairwise_auc_1v2: 0.6539
      pairwise_auc_2v3: 0.5515
      pairwise_auc_3v4: 0.5153
      pairwise_auc_4v5: 0.5135
      ci_1v2: "[0.6454, 0.6630]"
      ordinal_accuracy: 0.383
      ordinal_mae: 1.14
    result_rationale: >
      Pythia-1.4B 作为第一个 continuation mode 跨模型验证，1v2 AUC=0.6539 距 θ=0.60
      有 +4.5pp 余量，是 C4 web text 上 K*=2 的稳健证据。2v3 AUC=0.5515 远低于 θ，
      sharp boundary 明确。Median 档下 reviewer 接受 K*=2 判定无争议（CI lower=0.6454 >> 0.60），
      但 Pythia-1.4B 代表性受限——较老架构、训练数据不同。Reviewer 认为此结果
      "expected given information-theoretic intuition"：递归生成快速退化是直觉合理的。
      Pythia 在 Code 域的 K*=1 结果（exp_code_pythia1b4）被 reviewer 用来论证
      domain-specific competence 的调制作用。
    tables:
      - name: "Table 2 (row): Pythia-1.4B C4 continuation"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
          |-------|------|------|------|------|------|----|
          | Pythia-1.4B | 0.993 | 0.654 | 0.552 | 0.515 | 0.514 | 2 |
    figures_description:
      - "Pairwise AUC heatmap 中的一行，展示 sharp 0v1→1v2 drop 和 2v3+ plateau"
    analysis: >
      稳健但不 exciting。Pythia 的较高 1v2 AUC (vs Qwen-cont 0.6112) 减少了 borderline
      concern。在 4-domain 框架下，Pythia 的 C4 K*=2 + Code K*=1 + arXiv K*=3 完整展现了
      domain×competence interaction：code competence 不足导致未达 ceiling。

  - name: exp-002
    plan_id: exp_002_olmo_depth
    description: "OLMo-1B, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5"
    expected_results:
      k_star: 2
      pairwise_auc_0v1: 0.997
      pairwise_auc_1v2: 0.6146
      pairwise_auc_2v3: 0.5497
      pairwise_auc_3v4: 0.509
      pairwise_auc_4v5: 0.5044
      ci_1v2: "[0.6045, 0.6247]"
      ordinal_accuracy: 0.3685
      ordinal_mae: 1.1813
    result_rationale: >
      OLMo-1B 1v2 AUC=0.6146，CI lower=0.6045，余量 +0.45pp。比 Pythia 更边缘但仍 pass。
      Median 档下 reviewer 注意到 CI lower 只比 θ 高 0.45pp，但未被单独点名
      （Qwen-cont 的 0.6015 更 marginal 吸引了注意力）。OLMo 在 arXiv 上的 capacity failure
      (K*=1) 被 reviewer 视为 "model competence prerequisite" 的证据，与 Code 域
      Pythia K*=1 形成类比：两者都是 domain-specific competence 不足的例子。
    tables:
      - name: "Table 2 (row): OLMo-1B C4 continuation"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
          |-------|------|------|------|------|------|----|
          | OLMo-1B | 0.997 | 0.615 | 0.550 | 0.509 | 0.504 | 2 |
    figures_description:
      - "Pairwise AUC heatmap 中的一行"
    analysis: >
      与 Pythia 一致，增强跨模型证据。OLMo 3v4/4v5 接近 0.50 (chance)，
      进一步确认 depth ≥3 后信号完全消失。OLMo 无 Code 域数据（未测试），
      不影响 Code ceiling 论证。

  - name: exp-003
    plan_id: exp_003_decoding_ablation
    description: "Qwen2.5-1.5B decoding strategy ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2"
    expected_results:
      k_star: 2
      k_star_robust: true
      greedy_1v2_auc: 0.6892
      nuc09_1v2_auc: 0.6862
      t07_1v2_auc: 0.6885
      t12_1v2_auc: 0.7037
      auc_1v2_range: "[0.6862, 0.7037]"
      all_k_star_2: true
      nuc09_2v3_ci_upper: 0.601
    result_rationale: >
      四种解码策略下 K* 完全一致=2，AUC range < 2pp。解码策略不变性消除了
      "K*=2 是特定 sampling 参数的 artifact" 的质疑。但此实验在 Qwen rewrite mode 上做
      （rewrite 的 higher baseline signal 使 K*=2 更容易 robust），exp-020 在 Pythia
      continuation 上复制增强了说服力。在 4-domain context 下，decoding invariance
      为 "domain ceiling 是 K* 主要决定因素" 提供额外支持：如果 decoding 不影响 K*，
      则 domain structure 对 K* 的决定作用更突出。
    tables:
      - name: "Table 3: Decoding strategy ablation"
        content: |
          | Decoding | 0v1 AUC | 1v2 AUC | 2v3 AUC | K* |
          |----------|---------|---------|---------|-----|
          | greedy   | 0.9796  | 0.6892  | 0.5612  | 2   |
          | nucleus p=0.9 | 0.9945 | 0.6862 | 0.5917 | 2 |
          | T=0.7    | 0.9877  | 0.6885  | 0.5901  | 2   |
          | T=1.2    | 0.9982  | 0.7037  | 0.5820  | 2   |
    figures_description:
      - "Bar chart showing K* invariance across decoding strategies"
    analysis: >
      Decoding invariance 是 C1' 的支柱。Median 档 reviewer 接受但权重较低
      （"somewhat expected"）。配合 exp-020 Pythia replication 形成完整论证。

  - name: exp-004
    plan_id: exp_004_7b_crossscale
    description: "Qwen2.5-7B, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B"
    expected_results:
      k_star: 2
      pairwise_auc_1v2: 0.6178
      ci_1v2: "[0.6079, 0.6261]"
      pairwise_auc_2v3: 0.546
      ci_2v3_upper: 0.5594
      pairwise_auc_4v5_perm_p: 0.0676
    result_rationale: >
      7B scale 下 K*=2 与 1.5B 一致，CI lower=0.6079 > θ（余量 +0.79pp）。
      Median 档下 reviewer 接受 1.5B→7B scale invariance 但力度不足：
      至少一个 reviewer 标记 "≤8B is a significant limitation"。14B (exp_14b_c4)
      和 32B (exp_32b_c4) 数据用于回应此 concern。Qwen-7B 在 Code 域的结果
      （预测 K*=2 but marginal）进一步扩展此模型的 multi-domain profile。
    tables:
      - name: "Table 2 (row): Qwen2.5-7B C4 continuation"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
          |-------|------|------|------|------|------|----|
          | Qwen2.5-7B | 0.964 | 0.618 | 0.546 | 0.523 | 0.509 | 2 |
    figures_description:
      - "Scale comparison subplot: 1.5B vs 7B vs 14B pairwise AUC curves"
    analysis: >
      Scale invariance 从 1.5B→14B 均确认 K*=2。如果 32B 也确认，
      rebuttal 中可有效回应 scale limitation concern。

  - name: exp-005
    plan_id: exp_005_degradation
    description: "Feature group ablation + degradation ordering analysis"
    expected_results:
      cross_model_spearman_rho_pythia_olmo: 0.95
      cross_model_spearman_rho_pythia_qwen_cont: 0.9143
      cross_model_spearman_rho_olmo_qwen_cont: 0.85
      shared_top_discriminators: "surp_d1_std, surp_std, surp_d2_std"
      1v2_tau_weakness: 0.37
    result_rationale: >
      Feature ordering 跨模型高度一致（ρ≥0.85），支持 depth signal 是 text-intrinsic。
      Median 档下 reviewer 接受 feature ranking consistency 但不视为独立贡献。
      1v2 pair 的 feature importance 一致性最弱（τ~0.37），在 boundary pair 信号最微弱处
      variance 大是合理的。Surprisal-based features 主导与 DPI 理论一致。
      在 4-domain 扩展后，Code 域的 feature ranking 是否保持一致成为新的验证点：
      Code 域 top features 同为 freq_entropy 和 surp_d1_mean，说明 feature ordering
      在 programming language text 上也成立。
    tables:
      - name: "Table A2: Cross-model feature ranking Spearman ρ"
        content: |
          | Model Pair | Spearman ρ |
          |------------|-----------|
          | Pythia ↔ OLMo | 0.950 |
          | Pythia ↔ Qwen-cont | 0.914 |
          | OLMo ↔ Qwen-cont | 0.850 |
    figures_description:
      - "Feature importance heatmap across models — Appendix"
    analysis: >
      Supporting evidence for text-intrinsic signal。不构成独立卖点。
      Code 域 feature ordering consistency 作为 4-domain 扩展的补充证据。

  - name: exp-006
    plan_id: exp_006_graduated_filtering
    description: "Downstream filtering evaluation: 6 strategies × 5 seeds, MMLU + HellaSwag"
    expected_results:
      binary_ours_mmlu: "0.5941±0.0008"
      binary_ours_hellaswag: "0.6701±0.0006"
      no_filter_mmlu: "0.5865±0.0010"
      no_filter_hellaswag: "0.6638±0.0008"
      delta_mmlu_binary_vs_nofilter: "+0.0076"
      delta_hellaswag_binary_vs_nofilter: "+0.0063"
      base_model_mmlu: 0.6018
      graduated_a09_mmlu: "0.5892±0.0008"
      dsir_mmlu: "0.5869±0.0003"
    result_rationale: >
      Binary-ours 在所有策略中最优，但 MMLU 增益仅 +0.76pp vs no-filter。
      在 median 档下，C3 的核心弱点被暴露：(a) MMLU Δ=0.76pp 被 reviewer 质疑
      practical significance；(b) 所有策略都 degrade vs base_model，说明
      contaminated data 的 fundamental harm 无法被 filtering 完全消除；
      (c) Graduated α 单调递增确认 K*=2 boundary，但被质疑 circular reasoning；
      (d) DSIR 表现差是正面结果，但公平性被质疑。一位 reviewer 认为 C3 negative
      results（Pythia exp-025, arXiv exp-026）削弱 practical relevance，
      要求 C3 降级为 "case study"。HellaSwag delta 在 median 档范围
      [3.8, 6.1]pp 的中间值约 5.0pp——对应 exp-009 dose-response 跨 ratio 的
      consistent binary advantage。
    tables:
      - name: "Table 5: Filtering strategy comparison (Qwen2.5-1.5B, 30% contamination)"
        content: |
          | Strategy | MMLU | HellaSwag | Δ MMLU vs no-filter |
          |----------|------|-----------|-------------------|
          | binary-ours | 0.5941±0.0008 | 0.6701±0.0006 | +0.0076* |
          | binary-Drayson | 0.5913±0.0009 | 0.6691±0.0004 | +0.0048* |
          | surprisal | 0.5894±0.0009 | 0.6641±0.0006 | +0.0029 |
          | graduated α=0.9 | 0.5892±0.0008 | 0.6701±0.0007 | +0.0027 |
          | DSIR | 0.5869±0.0003 | 0.6631±0.0007 | +0.0004 |
          | no-filter | 0.5865±0.0010 | 0.6638±0.0008 | — |
          | base (no contam.) | 0.6018 | 0.6821 | — |
    figures_description:
      - "Bar chart: filtering strategies ranked by MMLU, with base_model reference line"
      - "α sensitivity curve: graduated filtering MMLU as function of α"
    analysis: >
      Median 档 reviewer 给 C3 substance score ~2.5-3.0。核心攻击：effect size 太小、
      binary > graduated 说明 K*-aware granularity 增量微弱。C3 需从 "validation"
      降级为 "case study / demonstration"。

  - name: exp-007
    plan_id: exp_007_bootstrap_ci
    description: "K* sensitivity at θ=0.55/0.60/0.65/0.70 + bootstrap CI + permutation test"
    expected_results:
      all_1v2_ci_lower_above_060: true
      most_marginal: "Qwen-cont CI lower=0.6015"
      theta_055_k_star_distribution: "all models K*=2 or K*=3"
      theta_060_k_star_distribution: "7/8 K*=2, 1/8 K*=1 (Mistral)"
      theta_065_k_star_distribution: "4-5/8 K*=2, rest K*=1"
      theta_070_k_star_distribution: "most K*=1"
    result_rationale: >
      θ-sensitivity 是 median 档的关键攻击面。θ=0.60 下 7/8 configurations K*=2 被接受，
      但 θ=0.70 下多数降至 K*=1 被 reviewer 放大："The finding is highly sensitive to
      threshold choice." Qwen-cont CI lower=0.6015 被要求 sensitivity analysis 或额外
      seeds 确认。Median 档要求 θ=0.55-0.70 全谱 figure 在主文呈现。论文需正面呈现
      K* 在 [0.55, 0.65] 范围内的稳定性，并以 Cohen's h=0.20 和 AUC gap discontinuity
      为 θ=0.60 选择辩护。Permutation test p<0.001 提供统计支持，但 reviewer 指出
      "statistical significance ≠ practical significance"。在 4-domain 扩展后，
      θ-sensitivity 需分域呈现：arXiv 在 θ=0.65 仍 K*=3（2v3 AUC=0.6427 >> 0.65），
      Code 域在 θ=0.65 下 Qwen-1.5B 仍 K*=2（1v2=0.7382 >> 0.65）但 Qwen-7B
      变为 K*=1（marginal）。
    tables:
      - name: "Table 4: K* sensitivity to threshold θ (C4 domain)"
        content: |
          | θ | K*=1 | K*=2 | K*=3 |
          |------|------|------|------|
          | 0.55 | 0/8  | 7/8  | 1/8  |
          | 0.60 | 1/8  | 7/8  | 0/8  |
          | 0.65 | 3-4/8 | 4-5/8 | 0/8 |
          | 0.70 | 6-7/8 | 1-2/8 | 0/8 |
    figures_description:
      - "主文 Figure: θ-sensitivity heatmap (4 domains × θ range), showing K* stability in [0.55, 0.65]"
      - "AUC gap discontinuity plot at K* boundary pair"
    analysis: >
      θ-sensitivity 被 median 档 reviewer 视为 "fair analysis" 但 robustness concern
      未完全消除。关键辩护：1v2 vs 2v3 的 AUC gap 远大于 θ 选择的 sensitivity range。
      4-domain 呈现增强说服力——arXiv 和 Code 的 θ-robust 区间更宽。

  - name: exp-008
    plan_id: exp_008_retrain_chain_v2
    description: "Retrain-chain ecological validity: Pythia-1.4B LoRA, C4 5K docs, depth 0-4"
    expected_results:
      k_star: ">=4"
      pairwise_auc_0v1: 0.9847
      pairwise_auc_1v2: 0.9484
      pairwise_auc_2v3: 0.8888
      pairwise_auc_3v4: 0.7982
    result_rationale: >
      Retrain-chain K*≥4 与 prompt-chain K*=2 的巨大差异来源于 LoRA fine-tune 每代引入
      cumulative model artifacts（vocabulary narrowing, repetition bias）。在 median 档下
      reviewer 接受 "prompt-chain isolates text-intrinsic degradation"，但要求论文更
      prominently 讨论 retrain-chain 的 higher detectability。现在有 depth-7 数据
      （Qwen K*=7, Pythia K*=7）和 two-family cross-validation，retrain-chain 的
      evidence chain 大幅增强。一个 reviewer 正面解读："retrain-chain K*=7 vs prompt-chain
      K*=2 shows the method scales to deeper chains, and prompt-chain K*=2 is the
      conservative lower bound." 另一个 reviewer 质疑 "LoRA rank=16 引入的 artifacts
      是 setup-specific 的，不代表 full fine-tune 或 RLHF contamination。"
    tables:
      - name: "Table 6: Prompt-chain vs Retrain-chain comparison"
        content: |
          | Pair | Prompt-chain AUC | Retrain-chain AUC (depth 4) | Retrain-chain AUC (depth 7) |
          |------|-----------------|---------------------------|---------------------------|
          | 0v1  | 0.993 | 0.985 | 0.984 |
          | 1v2  | 0.654 | 0.948 | 0.897 |
          | 2v3  | 0.552 | 0.889 | 0.810 |
          | 3v4  | 0.515 | 0.798 | 0.760 |
          | 4v5  | — | — | 0.746 |
          | 5v6  | — | — | 0.702 |
          | 6v7  | — | — | 0.641 |
    figures_description:
      - "Dual-panel AUC decay: prompt-chain (sharp drop) vs retrain-chain (gradual decay to depth 7)"
    analysis: >
      Retrain K*=7 (two families, consistent) 是 rebuttal 级别证据。
      Median 档 reviewer 肯定 ecological validity 贡献但要求讨论
      "real-world contamination likely falls between prompt-chain and retrain-chain"。

  - name: exp-009
    plan_id: exp_009_dose_50pct
    description: "Contamination dose-response: 10%/30%/50% ratio × 3 strategies × 5 seeds"
    expected_results:
      binary_consistently_best: true
      graduated_equals_no_filter: true
      hellaswag_binary_significant_all_ratios: true
      mmlu_binary_30pct_p: 0.074
      effect_size_increases_with_contamination: true
      hellaswag_delta_10pct: "+0.38pp"
      hellaswag_delta_30pct: "+0.61pp"
      hellaswag_delta_50pct: "+0.51pp"
    result_rationale: >
      Dose-response 确认 binary filtering 在所有 contamination ratio 下一致最优，
      graduated filtering 崩溃至 no-filter 水平。HellaSwag 显著（p≤0.004 at all ratios）
      但 MMLU 在 30% ratio 下 p=0.074 不显著，被 reviewer 攻击 "inconsistent significance
      across benchmarks"。Effect size 随 contamination ratio 增加但绝对值仍小。
      一位 reviewer 认为这些 C3 negative results（加上 exp-025/026 null results）
      削弱 practical relevance：K* 虽然能 characterize discriminability boundary，
      但无法 reliably 转化为 filtering 收益。
    tables:
      - name: "Table 7: Dose-response analysis (HellaSwag)"
        content: |
          | Ratio | binary vs no-filter Δ | p-value |
          |-------|----------------------|---------|
          | 10%   | +0.0038              | 0.0017  |
          | 30%   | +0.0061              | 0.0036  |
          | 50%   | +0.0051              | <0.001  |
    figures_description:
      - "Line plot: HellaSwag as function of contamination ratio, 3 strategies, with significance markers"
    analysis: >
      Binary filtering dose-response consistency 是 C3 最强证据。
      但 graduated=no-filter 同时说明 K*-aware graduated curation 无增量价值。
      C3 reviewer 评分 2.5-3.0。

  - name: exp-010
    plan_id: exp_010_ordinal_baseline
    description: "CORAL vs multiclass LightGBM vs ordinal logistic regression"
    expected_results:
      obd_lgbm_best_accuracy: 0.4229
      multiclass_lgbm_accuracy: 0.4182
      ordinal_logreg_best_tau: 0.563
      obd_lgbm_best_mae: 0.9836
    result_rationale: >
      OBD-LightGBM 略优于 multiclass LightGBM（Δacc < 0.5pp），ordinal logistic regression
      MAE 最低但 accuracy 最差。Median 档下 reviewer 不特别关注——"implementation detail,
      not a contribution"。Ordinal structure 为 "depth is ordinal" framing 提供小幅支持。
    tables:
      - name: "Table A3: Classifier comparison"
        content: |
          | Method | Acc | MAE | τ_b | Mean PW-AUC |
          |--------|-----|-----|-----|-------------|
          | OBD-LightGBM | 0.423 | 0.984 | 0.552 | 0.621 |
          | Multiclass-LightGBM | 0.418 | 1.016 | 0.537 | 0.625 |
          | Ordinal LogReg | 0.364 | 0.911 | 0.563 | 0.502 |
    figures_description: []
    analysis: "Appendix material。Median 档 reviewer 不质疑也不 highlight。"

  - name: exp-011
    plan_id: exp_011_llm_zeroshot
    description: "GPT-5.5 / Claude Opus 4.6 zero-shot depth estimation baseline"
    expected_results:
      gpt55_5class_acc: 0.332
      claude_5class_acc: 0.331
      gpt55_binary_acc: 0.878
      claude_binary_acc: 0.882
      odb_baseline_5class_acc: 0.386
    result_rationale: >
      Frontier LLMs 在 5-class depth estimation 上不如 OBD-LightGBM（33% vs 39%），
      但 binary detection 高达 88%。证明 depth estimation 需要 specialized features。
      Median 档下 reviewer 正面评价 "Good to include"，但指出 OBD 也只有 39% accuracy，
      "both methods are poor at fine-grained depth estimation"。McNemar test
      non-significant (p~0.07-0.08) 被注意——OBD 优势不显著。
    tables:
      - name: "Table 8: LLM zero-shot vs OBD baseline"
        content: |
          | Method | 5-class Acc | MAE | Binary Acc |
          |--------|------------|-----|-----------|
          | GPT-5.5 | 0.332 | 1.102 | 0.878 |
          | Claude Opus 4.6 | 0.331 | 1.150 | 0.882 |
          | OBD-LightGBM | 0.386 | 1.107 | — |
    figures_description:
      - "Per-depth accuracy heatmap: LLMs vs OBD, showing LLM failure at depth 1-4"
    analysis: "Median 档 reviewer 正面评价但 McNemar non-significant 削弱 claim。"

  - name: exp-012
    plan_id: exp_012_binary_confidence
    description: "DivEye/Binoculars binary detector confidence as depth proxy"
    expected_results:
      binary_detector_kstar: 1
      obd_kstar: 2
      spearman_rho_range: "0.06-0.46"
      auc_non_monotonic: true
      six_class_accuracy_max: 0.199
    result_rationale: >
      Binary detectors K*≈1 vs OBD K*=2，6-class accuracy 接近 random。
      直接支持 "binary confidence ≠ depth" 的 claim。Median 档下 reviewer 接受结论，
      但建议加入 watermark-based 或 learned detectors 作为 baseline。
      在 4-domain 框架下，binary detector 在 Code 域同样 K*≈1，
      进一步证明 depth estimation 需要超越 binary 的方法。
    tables:
      - name: "Table A4: Binary detector depth estimation"
        content: |
          | Generator | 6-class Acc | ρ (ppl_ratio) | AUC monotonic? |
          |-----------|------------|--------------|---------------|
          | Qwen-rw | 0.199 | 0.119 | ❌ |
          | Pythia | 0.130 | -0.392 | ❌ |
          | OLMo | 0.127 | -0.407 | ❌ |
          | Qwen-cont | 0.183 | -0.058 | ❌ |
    figures_description:
      - "Scatter plot: binary detector confidence vs true depth"
    analysis: "Strong justification。Median 档 reviewer 正面引用。"

  - name: exp-013
    plan_id: exp_013_cross_transfer
    description: "4×4 cross-model transfer matrix"
    expected_results:
      pythia_olmo_retention: "91-92%"
      qwen_cont_cross_retention: "80-85%"
      qwen_rw_cross_retention: "61-63%"
      binary_0v1_cross_all_above_096: true
    result_rationale: >
      Cross-model transfer 是 C1' "text-intrinsic signal" 的核心证据。
      Pythia↔OLMo 91-92% retention 和 0v1 cross-AUC > 0.96 强力支持
      depth signal 跨模型可迁移。Median 档下 reviewer 正面评价但指出
      "all models are ≤8B from similar training distributions"。
      Code 域的 cross-scorer validation（Pythia scorer 重评 Qwen Code generations
      K*=2 confirmed，Δ=-1.9pp）进一步扩展 transfer 证据到新域。
    tables:
      - name: "Table 9: Cross-model transfer retention"
        content: |
          | Transfer Direction | Accuracy Retention |
          |-------------------|-------------------|
          | Pythia → OLMo | 92% |
          | OLMo → Pythia | 91% |
          | Qwen-cont → Pythia | 85% |
          | Qwen-cont → OLMo | 80% |
          | Qwen-rw → Pythia | 63% |
          | Qwen-rw → OLMo | 61% |
    figures_description:
      - "4×4 transfer heatmap in main text"
    analysis: >
      C1' strongest supporting evidence 之一。Transfer > 80% 在 continuation mode 下
      消除 scorer bias 质疑。

  - name: exp-014
    plan_id: ""
    description: "Naturalistic validation: Common Crawl 2025/2026 snapshot depth prediction"
    expected_results:
      status: planned_not_executed
      predicted_depth_distribution:
        depth_0: "60-75%"
        depth_1: "15-25%"
        depth_2_plus: "5-15%"
      correlation_with_alignscore: "Spearman ρ=0.15-0.30"
      correlation_with_vocab_richness: "Spearman ρ=0.20-0.35"
    result_rationale: >
      Naturalistic validation 未执行（P2 priority）。如果执行，预期 Common Crawl 中
      约 25-40% 文本被预测为 depth ≥1，与外部估计一致。但 ground truth 缺失使此实验
      无法做定量验证。Median 档 reviewer 不因缺失严重扣分，但 1 个 reviewer 建议
      "a naturalistic study would strengthen practical relevance"，
      特别是在 C3 negative results 削弱 practical motivation 之后。
    tables: []
    figures_description: []
    analysis: "未执行。作为 future work 出现在 reviewer comments 中。"

  - name: exp-015
    plan_id: exp_015_neural_probe
    description: "Frozen Qwen2.5-1.5B embeddings + MLP probe vs 15D features"
    expected_results:
      pythia_k_star_neural: 2
      olmo_k_star_neural: 2
      qwen_cont_k_star_neural: 3
      qwen_cont_2v3_neural_auc: 0.616
      qwen_cont_2v3_neural_ci_lower: 0.6099
    result_rationale: >
      Neural probe K*_neural 结果分裂：Pythia/OLMo=2 与 15D 一致，Qwen-cont=3 高于 15D。
      Qwen-cont 差异来自 self-scorer advantage。Median 档下 reviewer 解读：
      (a) Pythia/OLMo K*_neural=2 confirms "K*=2 is data-intrinsic"；
      (b) Qwen K*_neural=3 被部分 reviewer 解读为 "model-dependent K* exists"，
      与 "K* is purely text-intrinsic" narrative 矛盾；
      (c) 论文需 careful framing：model-free 15D features 给出 universal K*，
      neural probe 给出 model-dependent K*，前者是推荐的 cross-model measure。
    tables:
      - name: "Table A5: Neural probe vs 15D features"
        content: |
          | Model | K*(15D) | K*(neural) | 2v3 AUC (neural) |
          |-------|---------|-----------|-----------------|
          | Pythia-1.4B | 2 | 2 | 0.596 |
          | OLMo-1B | 2 | 2 | 0.589 |
          | Qwen-cont | 2 | 3 | 0.616 |
    figures_description:
      - "Comparison bar chart: 15D vs neural probe pairwise AUC per model"
    analysis: >
      Validates choice of model-free features for headline K*。
      Qwen K*_neural=3 被部分 reviewer 用来质疑 universality。

  - name: exp-016
    plan_id: exp_016_base_vs_instruct
    description: "Qwen2.5-1.5B base vs Instruct continuation mode comparison"
    expected_results:
      k_star: 2
      base_1v2_auc: 0.6262
      base_ci_lower: 0.6168
      instruct_1v2_auc: 0.6112
      instruct_ci_lower: 0.6015
      ci_overlap: true
    result_rationale: >
      Base 和 Instruct K* 一致=2，CI 重叠说明 instruction tuning 不改变 K*。
      Base 1v2 AUC (0.6262) > Instruct (0.6112)——instruction tuning 轻微降低
      depth signal（RLHF 增加生成多样性）。Median 档下 reviewer 不特别关注。
    tables:
      - name: "Table A6: Base vs Instruct"
        content: |
          | Variant | 1v2 AUC | 95% CI | K* |
          |---------|---------|--------|-----|
          | Base | 0.626 | [0.617, 0.635] | 2 |
          | Instruct | 0.611 | [0.602, 0.621] | 2 |
    figures_description: []
    analysis: "Supporting evidence。不是 highlight。"

  - name: exp-017
    plan_id: exp_017_qwen_continuation
    description: "Qwen2.5-1.5B-Instruct continuation mode, C4 5K docs, depth 0-5"
    expected_results:
      k_star: 2
      pairwise_auc_1v2: 0.6112
      ci_1v2_lower: 0.6015
      pairwise_auc_2v3: 0.5609
    result_rationale: >
      Qwen-cont 1v2 AUC=0.6112，CI lower=0.6015，仅高于 θ 0.15pp。
      Median 档核心攻击目标：reviewer 单独点名 "CI lower=0.6015 is dangerously close
      to the threshold." exp-022 中 qwen_cont256×pythia K*=1 (1v2=0.5979)
      进一步加剧 concern。论文需承认 Qwen-cont 处于 K*=1/K*=2 边界，
      作为 θ-sensitivity 讨论案例。但在 4-domain 框架下，Qwen-1.5B 在 Code 域
      的 K*=2（1v2=0.7382，远超 θ）抵消了 C4 边缘性的 concern——同模型在
      不同域的 signal strength 差异大但 K* 一致（Code 和 C4 均 ceiling=2）。
    tables:
      - name: "Table 2 (row): Qwen2.5-1.5B-Instruct continuation"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
          |-------|------|------|------|------|------|----|
          | Qwen-1.5B-Inst cont | 0.997 | 0.611 | 0.561 | 0.541 | 0.514 | 2 |
          | 95% CI (1v2) | — | [0.602, 0.621] | — | — | — | — |
    figures_description: []
    analysis: >
      Median 档核心攻击目标。需正文承认 borderline nature 并提供多层辩护。
      Cross-scorer 和 θ-sensitivity 在正文中呈现。

  - name: exp-018
    plan_id: exp_018_llama8b_depth
    description: "LLaMA-3.1-8B, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B"
    expected_results:
      k_star: 2
      pairwise_auc_1v2: 0.6123
      ci_1v2_lower: 0.6028
      ci_1v2_upper: 0.6216
    result_rationale: >
      LLaMA-8B K*=2，CI lower=0.6028 (余量 +0.28pp)。第三模型家族确认 C4 K*=2。
      0v1 AUC=0.9225 是所有模型中最低的——LLaMA continuation 与原文更相似（model quality
      更高），整体 signal 更弱但 K* 仍=2。LLaMA 在 Code 域也 K*=2（exp_code_llama8b,
      1v2=0.7394），且 Code cross-scorer K*=2 confirmed（D079），
      是 Code ceiling=2 cross-family 的核心证据。Median 档 reviewer 正面评价
      LLaMA 的 multi-domain consistency（C4=2, Code=2, arXiv=3），
      但 C4 的低 0v1 AUC 暗示 "larger models produce more human-like text"，
      与 scale limitation concern 呼应。
    tables:
      - name: "Table 2 (row): LLaMA-3.1-8B C4 continuation"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
          |-------|------|------|------|------|------|----|
          | LLaMA-3.1-8B | 0.923 | 0.612 | 0.527 | 0.514 | 0.510 | 2 |
    figures_description: []
    analysis: >
      LLaMA multi-domain profile (C4=2, Code=2, arXiv=3) 是 domain ceiling 框架的
      strongest evidence model——三个域均达到 ceiling。

  - name: exp-019
    plan_id: exp_019_mistral7b_depth
    description: "Mistral-7B-v0.3, continuation mode, C4 5K docs, scorer=Qwen2.5-1.5B"
    expected_results:
      k_star: 1
      pairwise_auc_1v2: 0.5935
      ci_1v2_lower: 0.5835
      ci_1v2_upper: 0.6032
      p_auc_leq_060: 0.9017
    result_rationale: >
      Mistral C4 K*=1 是 C4 唯一 outlier（8/9 K*=2 中的例外）。Cross-scorer validation
      确认 K*=1 是 text-intrinsic。Median 档 reviewer 反应分裂：
      Reviewer A 接受 "interpretable outlier"，Reviewer B 攻击 "model×domain interaction
      not pure domain dependence"。Mistral arXiv K*=3 是回应——domain 仍是 primary factor。
      在 4-domain 框架下，Mistral Code K*=1（median 档预测）进一步增强
      domain×competence interaction 论证：Mistral 在 C4 和 Code 两个 intermediate-
      complexity domains 均 K*=1，而在 extreme domain (arXiv) K*=3，
      说明 Mistral 对 intermediate domains 的 generation competence 系统性不足。
      论文需从 "sole determinant" 降级为 "primary factor"。
    tables:
      - name: "Table 2 (row): Mistral-7B C4 continuation (K*=1)"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | 3v4 | 4v5 | K* |
          |-------|------|------|------|------|------|----|
          | Mistral-7B | 0.984 | 0.594 | 0.540 | 0.523 | 0.518 | 1 |
          | 95% CI (1v2) | — | [0.584, 0.603] | — | — | — | — |
    figures_description:
      - "Highlighted outlier in K* summary figure"
    analysis: >
      Median 档核心攻击点之一。4-domain 框架下 Mistral 的 pattern
      （C4=1, Code=1, arXiv=3, Wiki=1）最清晰地展示 domain×competence interaction。

  - name: exp-020
    plan_id: exp_020_pythia_decoding
    description: "Pythia-1.4B decoding ablation: 4 strategies, C4 5K docs, depth 0-5"
    expected_results:
      all_k_star_2: true
      greedy_1v2: 0.8838
      nuc09_1v2: 0.677
      t07_1v2: 0.7265
      t12_1v2: 0.6172
    result_rationale: >
      Pythia 4 种解码策略 K* 全=2，跨模型复制 exp-003 的解码不变性。
      Greedy 1v2=0.8838 因 repetition collapse 异常高。T=1.2 1v2=0.6172 最低
      （高温增加随机性）。Median 档 reviewer 正面评价 "K*=2 holds across
      2 models × 4 decoding strategies = 8 conditions"，但 greedy 的异常高 AUC
      被注意——"greedy is a degenerate condition"。
    tables:
      - name: "Table A7: Pythia decoding ablation"
        content: |
          | Decoding | 1v2 AUC | 2v3 AUC | K* |
          |----------|---------|---------|-----|
          | greedy | 0.884 | 0.534 | 2 |
          | nucleus p=0.9 | 0.677 | 0.555 | 2 |
          | T=0.7 | 0.727 | 0.594 | 2 |
          | T=1.2 | 0.617 | 0.523 | 2 |
    figures_description: []
    analysis: "Supporting evidence, Appendix。Greedy repetition collapse 作为 caveat 提及。"

  - name: exp-021
    plan_id: exp_021_length_ablation
    description: "Text length ablation: 128/256/512 tokens, Qwen continuation"
    expected_results:
      128tok_k_star: 2
      256tok_k_star: 2
      512tok_k_star: 2
      512tok_1v2_ci_lower: 0.5979
      512tok_verdict: BORDERLINE
    result_rationale: >
      K*=2 在三种长度下一致。但 512tok CI lower=0.5979 < θ 是 borderline failure。
      Median 档 reviewer 注意到 "longer texts paradoxically reduce discriminability"。
      解释：512 tokens 的 continuation 更有空间 converge to generator's style。
      与 "one-wash laundering" 概念一致。被 reviewer 归入 "robustness limitations" 段。
    tables:
      - name: "Table A8: Length ablation"
        content: |
          | Length | 1v2 AUC | CI lower | K* |
          |--------|---------|---------|-----|
          | 128 tok | 0.622 | >0.60 | 2 |
          | 256 tok | 0.628 | >0.60 | 2 |
          | 512 tok | 0.607 | 0.598 | 2* |
    figures_description: []
    analysis: "512-token borderline 被 median 档 reviewer 视为 minor concern。"

  - name: exp-022
    plan_id: exp_022_cross_scorer_matrix
    description: "4×4 cross-scorer matrix: 4 generators × 4 scorers"
    expected_results:
      k_star_2_count: 11
      k_star_1_count: 1
      exception: "qwen_cont256×pythia (1v2=0.5979)"
      scorer_delta_within_generator: "<0.025"
    result_rationale: >
      11/12 combos K*=2 是 scorer independence 的强证据。唯一例外
      qwen_cont256×pythia (K*=1) 因 Qwen-cont 本身 marginal 而 flip。
      Median 档 reviewer 正面评价 scorer independence，但用 qwen_cont×pythia
      加强 Qwen-cont borderline 攻击。在 4-domain 框架下，Code 域 cross-scorer
      validation (Pythia scorer 重评 Qwen Code K*=2, Δ=-1.9pp) 和 arXiv 域
      cross-scorer 结果一起构成完整的 scorer independence 证据矩阵。
      但 arXiv Qwen-7B cross-scorer K*=3→2 的下降（exp_arXiv_qwen7b_crossscorer:
      2v3 AUC=0.5989 < θ）被一位 reviewer 视为 scorer confound 未完全控制的
      evidence——median 档核心假设之一。
    tables:
      - name: "Table 10: Cross-scorer matrix (selected)"
        content: |
          | Generator × Scorer | 1v2 AUC | K* |
          |-------------------|---------|-----|
          | Qwen-base × OLMo | 0.605 | 2 |
          | Qwen-base × Pythia | 0.617 | 2 |
          | Qwen-cont × Pythia | 0.598 | 1 |
          | Qwen-cont × Qwen-base | 0.628 | 2 |
    figures_description:
      - "4×4 heatmap of K* values in cross-scorer matrix"
    analysis: >
      Scorer independence confirmed overall。arXiv Qwen-7B cross-scorer K*=3→2
      是 median 档的新攻击面。cross_scorer_kstar_preservation_rate ~0.80
      在 median 档范围 [0.75, 0.85] 内。

  - name: exp-023
    plan_id: exp_023_domain_ablation
    description: "Wikipedia domain, Qwen2.5-1.5B base continuation, 5K docs, depth 0-5"
    expected_results:
      k_star_same_scorer: 2
      k_star_cross_scorer: 1
      one_v_two_auc_same: 0.6193
      one_v_two_auc_cross: 0.587
      scorer_confound_delta: -0.024
    result_rationale: >
      Wikipedia K*=2 (same-family scorer) 经 cross-scorer confound 控制后降为 K*=1。
      正文报告 scorer-controlled K*=1。6 个模型（包括 LLaMA-8B, Mistral-7B, Pythia,
      OLMo, Qwen-1.5B, Qwen-7B）在 cross-scorer 控制后均 K*=1。
      Qwen-7B same-scorer 的 K*=2 (1v2=0.6108) 也被 confound 解释。
      Median 档 reviewer 接受 confound 控制但质疑："If same-family scorer bias
      exists on Wikipedia, could it also affect C4 results?"
      在 4-domain 框架下，Wikipedia K*=1 是 "extreme simplicity" 端的锚点：
      简单域信号一代即饱和，结构化域（arXiv）可延伸至 3 代。
    tables:
      - name: "Table 11 (row): Wikipedia domain K*"
        content: |
          | Domain | Scorer | 1v2 AUC | K* |
          |--------|--------|---------|-----|
          | Wikipedia | Qwen (same) | 0.619 | 2 |
          | Wikipedia | Pythia (cross) | 0.587 | 1 |
          | Wikipedia | scorer-controlled | — | 1 |
    figures_description:
      - "Domain ladder figure: Wikipedia(1) < C4/Code(2) < arXiv(3)"
    analysis: >
      Scorer confound 的 honest reporting 增加可信度。K*=1 for Wikipedia
      被 reviewer 解读为 "trivial — one generation washes everything"。

  - name: exp-024
    plan_id: exp_024_arxiv_domain
    description: "arXiv domain, Qwen2.5-1.5B base continuation, 5K docs, depth 0-5"
    expected_results:
      k_star: 3
      pairwise_auc_1v2: 0.858
      pairwise_auc_2v3: 0.6427
      ci_2v3_lower: 0.6275
    result_rationale: >
      arXiv K*=3 是 domain dependence 最强证据——首个 K*>2 条件。
      2v3 AUC=0.6427, CI lower=0.6275 >> θ。五模型跨四架构族 100% 一致 K*=3
      （5/5 domain-competent models）。在 4-domain 框架下，arXiv K*=3 是
      "extreme complexity" 端的锚点。Median 档 reviewer 正面评价 domain dependence
      但攻击 "4 domains is still limited"（虽然从 3 域升级到 4 域增强了覆盖）。
      Reviewer 建议增加更多域（legal, news, social media）。
      arXiv Qwen-7B cross-scorer K*=3→2 的下降（2v3 AUC 从 0.626 降至 0.5989）
      被一位 reviewer 视为 scorer confound 未完全控制的证据。
    tables:
      - name: "Table 11 (row): arXiv domain K*"
        content: |
          | Domain | 1v2 AUC | 2v3 AUC | 3v4 AUC | K* |
          |--------|---------|---------|---------|-----|
          | arXiv (Qwen-1.5B) | 0.858 | 0.643 | 0.544 | 3 |
    figures_description:
      - "AUC decay curves: 4 domains overlaid, showing domain-dependent saturation points"
    analysis: >
      K*=3 on arXiv 是论文最强 individual finding。4-domain coverage
      增强了 domain hierarchy 证据链。arXiv cross-scorer concern 需
      完整 bootstrap CI 呈现回应。

  - name: exp-025
    plan_id: exp_025_pythia_filtering
    description: "Pythia-1.4B filtering replication: 3 strategies × 3 seeds"
    expected_results:
      all_strategies_nearly_identical: true
      max_delta_mmlu: 0.0017
      binary_hellaswag_delta: "+0.0000"
      key_finding: "null result"
    result_rationale: >
      Pythia-1.4B 三种策略几乎相同（max Δ=0.0017 MMLU），filtering ordering 未确认。
      Pythia base capability 太低（MMLU=0.26 接近 random），filtering marginal benefit
      在 low-capability regime 被淹没。一位 reviewer 认为这是 C3 negative results
      （结合 exp-026 arXiv null）削弱 practical relevance 的关键证据。
      另一位 reviewer 肯定 "honest reporting of negative results"。
      C3 证据链因此完全依赖 exp-006 (Qwen) 和 exp-009 (dose-response)。
    tables:
      - name: "Table A9: Pythia filtering (null result)"
        content: |
          | Strategy | MMLU | HellaSwag |
          |----------|------|-----------|
          | binary-ours | 0.259±0.000 | 0.525±0.000 |
          | graduated α=0.9 | 0.256±0.001 | 0.525±0.001 |
          | no-filter | 0.257±0.001 | 0.525±0.001 |
    figures_description: []
    analysis: >
      Null result 放 Appendix。C3 substance ~2.5 因 Pythia+arXiv dual null。

  - name: exp-026
    plan_id: exp_026_arxiv_filtering
    description: "arXiv graduated vs binary filtering: Qwen base + LoRA, K*=3 domain, 3 strategies × 5 seeds"
    expected_results:
      graduated_equals_no_filter: true
      binary_mmlu_delta: "-0.0023"
      binary_hellaswag_delta: "+0.0042"
      graduated_mmlu_delta: "+0.0001"
      key_finding: "null result — graduated ≈ no_filter on K*=3 domain"
    result_rationale: >
      C3 的 fatal blow：即使在 K*=3 域 graduated ≈ no_filter。Binary 有
      metric-specific trade-off（MMLU -0.23pp, HellaSwag +0.42pp）。
      Median 档 reviewer：(a) "graduated fails even where it should work best"
      → K*-aware curation thesis undermined；(b) C3 降级为 "case study"；
      (c) 关键 insight：K* characterizes discriminability, not data utility——
      depth 2-3 text 统计上可区分但移除不改善训练。
    tables:
      - name: "Table 12: arXiv filtering results (negative)"
        content: |
          | Strategy | MMLU | HellaSwag | Δ MMLU | Δ HellaSwag |
          |----------|------|-----------|--------|-------------|
          | no-filter | 0.590±0.001 | 0.660±0.000 | — | — |
          | binary | 0.588±0.000 | 0.664±0.000 | -0.002 | +0.004* |
          | graduated α=0.9 | 0.590±0.001 | 0.660±0.000 | +0.000 | -0.000 |
    figures_description: []
    analysis: >
      Negative result honestly reported。"K* ≠ data utility" insight
      被一位 reviewer 视为 "interesting secondary finding"。

  - name: exp-027
    plan_id: exp_027_latex_ablation
    description: "LaTeX markup removal ablation on arXiv data"
    expected_results:
      k_star_preserved: true
      original_2v3: 0.6436
      stripped_2v3: 0.6229
      delta_2v3: -0.021
    result_rationale: >
      K*=3 在去除 LaTeX 标记后保持，2v3 AUC 从 0.6436 降至 0.6229 但仍 > θ。
      LaTeX 格式贡献约 2pp AUC 但非 confound。Median 档 reviewer 正面评价
      "rules out the obvious confound"。Reviewer 注意到 stripped 余量 +2.29pp，
      如果进一步去除 citation/section numbering 可能降至 K*=2。
    tables:
      - name: "Table A10: LaTeX ablation"
        content: |
          | Condition | 1v2 AUC | 2v3 AUC | K* |
          |-----------|---------|---------|-----|
          | Original | 0.858 | 0.644 | 3 |
          | LaTeX stripped | 0.830 | 0.623 | 3 |
          | Δ | -0.028 | -0.021 | — |
    figures_description: []
    analysis: "Effective confound control。Median 档 reviewer 不攻击。"

  - name: exp-028
    plan_id: exp_028_power_curve
    description: "Subsampling power curve: C4 n={500,1000,2000,3000,4000,5000} × 10 resamples"
    expected_results:
      min_n_100pct: 2000
      n500_rate: 0.2
      n1000_rate: 0.3
      n2000_rate: 1.0
      n5000_rate: 1.0
    result_rationale: >
      n≥2000 给出 100% reliable K*=2 detection。n=1000 仅 30%。
      回应 reviewer sample size concern。Median 档 reviewer 评价
      "useful methodological contribution for practitioners"。
      在 4-domain 框架下，arXiv 和 Code 域的 n=2200 和 n=5000
      均满足 power requirements。
    tables:
      - name: "Table A11: Subsampling power curve"
        content: |
          | n | K*=2 detection rate | Mean 1v2 AUC |
          |------|-------------------|-------------|
          | 500 | 20% | 0.581 |
          | 1000 | 30% | 0.591 |
          | 2000 | 100% | 0.610 |
          | 3000 | 100% | 0.617 |
          | 5000 | 100% | 0.629 |
    figures_description:
      - "Power curve: K*=2 detection rate as function of sample size"
    analysis: "Power analysis 回应统计 concern。如在 rebuttal 中补充可回应 reviewer。"

  # ---- Code Domain Experiments (NEW for 4-domain framework) ----

  - name: exp_code_qwen1b5
    plan_id: "Code domain Qwen-1.5B"
    description: "Qwen2.5-1.5B, Code/Python (CodeSearchNet), continuation, depth 0-5"
    expected_results:
      k_star: 2
      auc_0v1: 0.9388
      auc_1v2: 0.7382
      ci_1v2: "[0.709, 0.767]"
      auc_2v3: 0.53
      jsd_1v2: 0.0443
      jsd_2v3: 0.0038
      jsd_cliff_ratio_1v2_to_2v3: 11.7
    result_rationale: >
      Qwen-1.5B Code K*=2 with 1v2 AUC=0.7382，远超 C4 同模型的 0.6262。
      Code 域的 depth signal 更强（programming language 的 syntactic structure
      提供额外 depth cues），但 K* ceiling 与 C4 相同=2。关键差异在 JSD cliff：
      Code 在 1v2→2v3 collapse（JSD ratio 11.7x），C4 在 0v1→1v2 有 large drop
      （JSD ratio ~9.8x）。这说明 domain structure 不仅决定 K* ceiling
      还影响 signal decay pattern。Median 档 reviewer 接受 Qwen-1.5B Code K*=2
      但指出仅一个模型不足以 claim "Code ceiling=2"。
    tables:
      - name: "Table 14 (row): Qwen-1.5B Code domain"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | K* | JSD cliff |
          |-------|------|------|------|----|-----------|
          | Qwen-1.5B | 0.939 | 0.738 | 0.530 | 2 | 1v2→2v3 (11.7x) |
    figures_description:
      - "JSD cliff comparison: Code vs C4, showing domain-specific signal decay patterns"
    analysis: >
      Code K*=2 with high 1v2 AUC 是 domain hierarchy 的重要扩展。
      JSD cliff difference (Code vs C4) 是 median 档论文的 nuanced finding。

  - name: exp_code_llama8b
    plan_id: "Code domain LLaMA-8B (D079)"
    description: "LLaMA-3.1-8B, Code/Python, continuation, scorer=Qwen, depth 0-5"
    expected_results:
      k_star: 2
      auc_0v1: 0.9161
      auc_1v2: 0.7394
      ci_1v2: "[0.729, 0.750]"
      auc_2v3: 0.5112
      jsd_cliff_ratio: 13.5
    result_rationale: >
      LLaMA-8B Code K*=2 是 cross-family validation 的核心证据：Code ceiling=2
      不是 Qwen 家族特有。1v2 AUC=0.7394 与 Qwen-1.5B 的 0.7382 高度一致，
      JSD cliff 13.5x。Scored by Qwen（cross-family scorer），排除 scorer artifact。
      Median 档 reviewer 正面评价 cross-family confirmation。但注意到仅有两个模型
      达到 ceiling（Qwen-1.5B, LLaMA-8B），需要更多模型验证。
      Pythia-1.4B Code K*=1 和 Mistral-7B Code K*=1（median 预测）说明
      Code ceiling=2 受 model code competence 调制。
    tables:
      - name: "Table 14 (row): LLaMA-8B Code domain (cross-family)"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | K* | Scorer |
          |-------|------|------|------|----|--------|
          | LLaMA-8B | 0.916 | 0.739 | 0.511 | 2 | Qwen (cross-family) |
    figures_description:
      - "Cross-family Code K* comparison bar chart"
    analysis: >
      Cross-family Code ceiling=2 confirmation。与 Qwen-1.5B AUC 几乎相同
      证明 Code K*=2 是 text-intrinsic。

  - name: exp_code_pythia1b4
    plan_id: "Code domain Pythia-1.4B"
    description: "Pythia-1.4B, Code/Python, continuation, depth 0-5"
    expected_results:
      k_star: 1
      auc_0v1: 0.9592
      auc_1v2: 0.5983
      ci_1v2_lower: 0.588
      ci_1v2_upper: 0.609
      auc_2v3: 0.5215
    result_rationale: >
      Pythia-1.4B Code K*=1，1v2 AUC=0.5983 < θ=0.60（CI straddles θ）。
      与 C4 上 Pythia K*=2 形成对比：Pythia 在 code generation 上 competence 不足
      （The Pile 训练，code 占比低），生成的 code 质量差到单次生成即令 depth signal
      饱和。这与 Mistral C4 K*=1 的 pattern 一致：model domain-specific competence
      不足时无法达到 domain ceiling。在 median 档 domain ceiling 框架下，
      Pythia Code K*=1 是 "ceiling=2 for models with sufficient code training"
      caveat 的关键 data point。Reviewer 接受此解释但指出
      "the ceiling framework is becoming unfalsifiable if every failure is attributed
      to insufficient competence。"
    tables:
      - name: "Table 14 (row): Pythia-1.4B Code domain (K*=1)"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | K* | Code competence |
          |-------|------|------|------|----|----------------|
          | Pythia-1.4B | 0.959 | 0.598 | 0.522 | 1 | Low (The Pile) |
    figures_description: []
    analysis: >
      Code K*=1 consistent with domain×competence interaction。
      但 "insufficient competence" 解释的 unfalsifiability 被 reviewer 挑战。

  - name: exp_code_qwen1b5_pythia_scorer
    plan_id: "Code domain cross-scorer (D080)"
    description: "Pythia-1.4B scorer re-evaluates Qwen Code generations"
    expected_results:
      k_star: 2
      auc_1v2: 0.7197
      delta_vs_same_scorer: -0.0185
    result_rationale: >
      Pythia scorer 重评 Qwen Code generations K*=2 confirmed，Δ=-1.9pp。
      与 Wiki 域的 scorer confound（same-family +1 bias）形成对比：
      Code 域 cross-scorer 下 K*=2 保持（Δ 小），说明 scorer confound
      是 domain-specific 而非 systematic。Median 档 reviewer 正面评价：
      "Code cross-scorer validation is clean, contrasting with the Wikipedia
      confound。" 但 arXiv Qwen-7B cross-scorer K*=3→2 的 drop 被
      另一位 reviewer 引用——scorer confound 在某些 domain×model 组合中
      仍存在，cross_scorer_kstar_preservation_rate ~80% 而非 100%。
    tables:
      - name: "Table 14b: Code cross-scorer validation"
        content: |
          | Generator | Scorer | 1v2 AUC | K* | Δ vs same-scorer |
          |-----------|--------|---------|-----|-----------------|
          | Qwen-1.5B Code | Qwen (same) | 0.738 | 2 | — |
          | Qwen-1.5B Code | Pythia (cross) | 0.720 | 2 | -1.9pp |
    figures_description: []
    analysis: >
      Code cross-scorer clean confirmation。与Wiki confound对比增强
      "scorer confound is domain-specific" narrative。

  - name: exp_code_mistral7b
    plan_id: "Code domain Mistral-7B (RUNNING)"
    description: "Mistral-7B, Code/Python, continuation, depth 0-5 — RUNNING"
    expected_results:
      k_star: 1
      auc_0v1: 0.948
      auc_1v2: 0.59
      ci_1v2_lower: 0.575
      ci_1v2_upper: 0.605
      auc_2v3: 0.518
      auc_3v4: 0.510
      auc_4v5: 0.505
      jsd_0v1: 0.068
      jsd_1v2: 0.007
      jsd_2v3: 0.004
      ordinal_mae: 1.31
      ordinal_accuracy: 0.335
    result_rationale: >
      Mistral-7B Code K*=1（1v2 AUC ~0.59，median 档范围 [0.56, 0.62] 中间值）。
      与 Mistral C4 K*=1 一致，形成 coherent pattern：Mistral 在两个 intermediate-
      complexity domains（C4 和 Code）均 K*=1，而在 arXiv K*=3。这不是因为 Mistral
      是 "bad model"——arXiv K*=3 证明其有能力——而是因为 Mistral 对 homogeneous
      text domains 的 continuation 生成质量足够好，使得 one generation 即令 depth
      signal 饱和。Code K*=1 进一步支持 domain×competence interaction：
      Mistral 的 code pretraining 可能不如 Qwen/LLaMA 充分（Mistral v0.3
      的 code 训练数据占比未公开但推测较低），导致 code generation 缺少
      足够的 syntactic fidelity 来在 depth 1 和 depth 2 之间产生可检测差异。
      Cross-scorer validation（如果执行）预期确认 K*=1 是 text-intrinsic。
      Median 档 reviewer 解读：code_models_at_ceiling2_of_5 = 3/5
      （Qwen-1.5B, LLaMA-8B, 可能 Qwen-7B），Mistral 和 Pythia 不达标。
      这要求 "ceiling=2" 软化为 "ceiling=2 for models with sufficient
      code training"，被 reviewer 视为 ceiling 框架的 overfit concern。
    tables:
      - name: "Table 14 (row): Mistral-7B Code domain (PREDICTED)"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | K* | Pattern |
          |-------|------|------|------|----|---------|
          | Mistral-7B | 0.948 | 0.590 | 0.518 | 1 | C4=1, Code=1, arXiv=3 |
    figures_description:
      - "Mistral multi-domain profile showing domain×competence interaction"
    analysis: >
      Mistral Code K*=1 与 C4 K*=1 模式一致，验证 domain ceiling 框架的
      competence prerequisite。但 2/5 models failing ceiling 使 reviewer
      质疑框架的 prescriptive power。

  - name: exp_code_qwen7b
    plan_id: "Code domain Qwen-7B (RUNNING)"
    description: "Qwen2.5-7B, Code/Python, continuation, depth 0-5 — RUNNING"
    expected_results:
      k_star: 2
      auc_0v1: 0.935
      auc_1v2: 0.63
      ci_1v2_lower: 0.605
      ci_1v2_upper: 0.655
      auc_2v3: 0.525
      auc_3v4: 0.512
      auc_4v5: 0.508
      jsd_0v1: 0.072
      jsd_1v2: 0.020
      jsd_2v3: 0.004
      ordinal_mae: 1.22
      ordinal_accuracy: 0.348
    result_rationale: >
      Qwen-7B Code K*=2 but marginal（1v2 AUC ~0.63，median 档范围 [0.60, 0.66]
      中间值偏下）。CI lower ~0.605 仅高于 θ 约 0.5pp。与 Qwen-1.5B Code 的
      1v2=0.7382 相比显著下降（Δ~-0.11），这是 counter-intuitive 的：
      7B 模型在 Code 域的 depth signal 竟然弱于 1.5B。可能解释：
      (a) 7B 模型生成更高质量 code，使 depth 1→2 差异更小（model quality effect）；
      (b) scorer (Qwen-1.5B) 对 7B 生成文本的 score 能力受限（cross-scale scoring）；
      (c) 7B 的 code continuation 风格更稳定，代际间 variation 被压缩。
      Median 档 reviewer 用 Qwen-7B Code 的 marginal result 挑战
      "Code ceiling=2" 的 robustness：CI lower=0.605 下 θ=0.65 即 flip to K*=1。
      但 K*=2 判定仍 pass θ=0.60，计入 code_models_at_ceiling2_of_5 = 3/5
      （Qwen-1.5B, LLaMA-8B, Qwen-7B）。一位 reviewer 质疑：
      "If 1.5B gives cleaner K*=2 than 7B on code, your ceiling framework
      doesn't predict signal strength, only ceiling. Is that useful?"
    tables:
      - name: "Table 14 (row): Qwen-7B Code domain (PREDICTED)"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | K* | vs Qwen-1.5B |
          |-------|------|------|------|----|-------------|
          | Qwen-7B | 0.935 | 0.630 | 0.525 | 2 | 1v2 Δ=-0.108 |
    figures_description:
      - "Code domain scale comparison: 1.5B vs 7B AUC decay"
    analysis: >
      Qwen-7B Code K*=2 marginal 是 median 档的关键不确定性。
      3/5 models at ceiling 使 domain ceiling 框架需 caveat。
      CI lower ~0.605 需在 θ-sensitivity 中特别讨论。

  # ---- arXiv Cross-Validation Experiments ----

  - name: exp_arXiv_5model_crossvalidation
    plan_id: "exp_arXiv_llama8b / exp_arXiv_mistral7b / exp_arXiv_qwen7b / exp_025_pythia_arxiv"
    description: "arXiv K*=3 cross-validation: 5 models × 4 architecture families"
    expected_results:
      qwen_1b5_k_star: 3
      pythia_k_star: 3
      llama_8b_k_star: 3
      mistral_7b_k_star: 3
      qwen_7b_k_star: 3
      olmo_k_star: 1
      domain_competent_k3_rate: "5/5 (100%)"
      qwen7b_2v3_auc: 0.626
      mistral7b_2v3_auc: 0.6275
    result_rationale: >
      五个 domain-competent 模型 100% 一致 K*=3。OLMo-1B K*=1 因 capacity failure。
      Median 档 reviewer 高度正面评价但仍攻击 "4 domains is still limited"。
      关键 concern：arXiv Qwen-7B cross-scorer K*=3→2 的下降
      （exp_arXiv_qwen7b_crossscorer: 2v3 AUC=0.5989 < θ）。
      Median 档核心假设：这被一位 reviewer 视为 scorer confound 未完全控制的证据。
      但其他模型的 cross-scorer K* 保持：LLaMA-8B cross-scorer K*=3
      (2v3=0.6201)，Mistral cross-scorer K*=3 (2v3=0.6075)，
      Qwen-1.5B cross-scorer K*=3 (2v3=0.6317)。
      整体 cross_scorer_kstar_preservation_rate = 3/4 = 0.75（Qwen-7B fail），
      在 median 档范围 [0.75, 0.85] 的下界。
    tables:
      - name: "Table 13: arXiv K*=3 cross-validation + cross-scorer"
        content: |
          | Model | Family | 2v3 AUC (same) | 2v3 AUC (cross) | K*(same) | K*(cross) |
          |-------|--------|---------------|----------------|---------|----------|
          | Qwen-1.5B | Qwen | 0.643 | 0.632 | 3 | 3 |
          | Pythia-1.4B | GPT-NeoX | 0.654 | — | 3 | — |
          | LLaMA-8B | LLaMA | 0.622 | 0.620 | 3 | 3 |
          | Mistral-7B | Mistral | 0.628 | 0.608 | 3 | 3 |
          | Qwen-7B | Qwen | 0.626 | 0.599 | 3 | 2 ⚠️ |
    figures_description:
      - "arXiv cross-scorer K* preservation: 3/4 models maintain K*=3"
    analysis: >
      Qwen-7B arXiv cross-scorer K*=3→2 是 median 档新攻击面。
      论文需呈现完整 bootstrap CI 并讨论 scorer interaction on arXiv。
      其他 3 个 cross-scorer 条件 K*=3 保持，整体证据链仍 positive。

  # ---- Wikipedia Multi-Model ----

  - name: exp_wiki_multimodel
    plan_id: "Wiki scorer-controlled analysis (D060)"
    description: "Wikipedia K*=1 (scorer-controlled): 6 models all K*=1 after cross-scorer control"
    expected_results:
      models_tested: 6
      all_cross_scorer_k_star_1: true
      qwen7b_same_scorer_k_star: 2
      qwen7b_cross_scorer_k_star: 1
      confound_pattern: "same-family scorer +1 bias on Wiki only"
    result_rationale: >
      所有 6 个模型在 cross-family scorer 控制后均 K*=1 on Wikipedia。
      Qwen-7B same-scorer K*=2 (1v2=0.6108) 被 confound 解释。
      Median 档 reviewer 接受 Wiki K*=1 为 domain hierarchy 的 floor。
      4-domain 框架下，Wiki K*=1 是 "extreme simplicity" 锚点。
      Reviewer 质疑："If we add social media (presumably even simpler than Wiki),
      would K* remain 1 or become 0 (i.e., even binary detection fails)?"
    tables:
      - name: "Table 11b: Wikipedia K*=1 (all models, scorer-controlled)"
        content: |
          | Model | Scorer | 1v2 AUC | K* |
          |-------|--------|---------|-----|
          | Qwen-1.5B | Pythia (cross) | 0.599 | 1 |
          | Pythia-1.4B | Qwen (cross) | 0.585 | 1 |
          | OLMo-1B | Qwen (cross) | 0.499 | 1 |
          | LLaMA-8B | Qwen (cross) | 0.595 | 1 |
          | Mistral-7B | Qwen (cross) | 0.555 | 1 |
          | Qwen-7B | Pythia (cross) | 0.587 | 1 |
    figures_description: []
    analysis: >
      Wiki K*=1 unanimous。Scorer confound 仅在 Wiki + same-family 触发，
      不影响 C4/Code/arXiv 主线结论。

  # ---- Retrain Chain Depth 7 ----

  - name: exp_retrain_depth7
    plan_id: "exp_qwen_retrain_depth7 / exp_pythia_retrain_depth7 (D077/D078)"
    description: "Retrain-chain K*=7: two families (Qwen-1.5B, Pythia-1.4B), depth 0-7"
    expected_results:
      qwen_k_star: 7
      pythia_k_star: 7
      qwen_6v7_auc: 0.641
      qwen_6v7_ci: "[0.638, 0.645]"
      pythia_6v7_auc: 0.634
      pythia_6v7_ci: "[0.628, 0.641]"
      cross_family_k_star_match: true
    result_rationale: >
      两个架构族在 retrain-chain 下一致 K*=7——尽管 LoRA effective capacity
      差异约 3x（Qwen fused QKV vs Pythia independent QKV），K* ceiling 完全一致。
      这进一步证明 K* 由 generation process 决定而非 model capacity。
      6v7 AUC 接近 θ=0.60（Qwen 0.641, Pythia 0.634）说明 depth 7 是
      retrain-chain 的 operational boundary。Median 档 reviewer 正面评价
      two-family consistency 但指出 "LoRA fine-tune 每代引入的 cumulative
      artifacts 是 setup-specific 的，不代表 full fine-tune 或 RLHF"。
      Prompt-chain K*=2 vs retrain-chain K*=7 的差距意味着
      "real-world contamination detectability depends on the contamination
      mechanism"——论文需讨论此 implication。
    tables:
      - name: "Table 6b: Retrain-chain K*=7 (two families)"
        content: |
          | Pair | Qwen-1.5B AUC | Pythia-1.4B AUC |
          |------|--------------|----------------|
          | 0v1 | 0.984 | 0.984 |
          | 1v2 | 0.897 | 0.947 |
          | 2v3 | 0.810 | 0.889 |
          | 3v4 | 0.760 | 0.800 |
          | 4v5 | 0.746 | 0.691 |
          | 5v6 | 0.702 | 0.650 |
          | 6v7 | 0.641 | 0.634 |
    figures_description:
      - "Retrain-chain AUC decay to depth 7, two families, showing convergence at 6v7"
    analysis: >
      Two-family K*=7 consistency 大幅增强 retrain-chain evidence。
      与 prompt-chain K*=2 的 gap 增强 "text-intrinsic vs model-artifact"
      的 methodological insight。

  # ---- Scale Extensions ----

  - name: exp_14b_c4
    plan_id: "Scale extension 14B"
    description: "Qwen2.5-14B, continuation, C4, depth 0-5 — scale extension"
    expected_results:
      k_star: 2
      pairwise_auc_1v2: 0.621
      ci_1v2: "[0.612, 0.630]"
    result_rationale: >
      14B K*=2 维持，CI lower=0.6119。Scale range 从 1.4B 扩展至 14B（10× range）。
      Median 档 reviewer：(a) 接受 14B 扩展 "extends scale range meaningfully"；
      (b) 但要求 32B 确认 trend；(c) 14B 1v2 AUC=0.621 与 1.5B 的 0.626/0.611
      无显著差异，支持 "K* is scale-invariant within 1-14B range"。
    tables:
      - name: "Table 2 (row): Qwen2.5-14B C4"
        content: |
          | Model | 0v1 | 1v2 | 2v3 | K* |
          |-------|------|------|------|----|
          | Qwen2.5-14B | 0.960 | 0.621 | 0.549 | 2 |
    figures_description:
      - "Scale invariance plot: 1.4B to 14B, K* flat at 2"
    analysis: >
      Rebuttal evidence for scale concern。如 32B 也确认，
      可有效回应 "≤8B limitation"。

  - name: exp_32b_c4
    plan_id: "Scale extension 32B (RUNNING)"
    description: "Qwen2.5-32B, continuation, C4, depth 0-5 — RUNNING"
    expected_results:
      k_star: 2
      auc_0v1: 0.945
      auc_1v2: 0.615
      ci_1v2_lower: 0.605
      ci_1v2_upper: 0.625
      auc_2v3: 0.545
    result_rationale: >
      32B K*=2 预期维持但 signal 可能略弱（0v1 AUC ~0.945 继续 LLaMA-8B 的
      下降趋势——更大模型生成更 human-like text）。1v2 AUC ~0.615，
      CI lower ~0.605 仍 > θ 但余量小。Scale range 扩展至 32B（23× from 1.4B）
      在 median 档下足以回应 scale concern：reviewer 从 "significant weakness"
      降为 "minor limitation (still no 70B+)"。如果 32B 结果 < θ 则 trigger
      worst-case scenario，但 median 档假设 K*=2 维持。
    tables:
      - name: "Rebuttal Table R1 (extension): Scale to 32B"
        content: |
          | Scale | 1v2 AUC | CI lower | K* |
          |-------|---------|---------|-----|
          | 1.4B (Pythia) | 0.654 | 0.645 | 2 |
          | 1.5B (Qwen) | 0.611 | 0.602 | 2 |
          | 7B (Qwen) | 0.618 | 0.608 | 2 |
          | 8B (LLaMA) | 0.612 | 0.603 | 2 |
          | 14B (Qwen) | 0.621 | 0.612 | 2 |
          | 32B (Qwen) | 0.615 | 0.605 | 2 |
    figures_description:
      - "Extended scale plot: 1.4B to 32B, K* invariant at 2"
    analysis: >
      32B confirmation 是 rebuttal 核心。23× scale range 下 K*=2 一致
      大幅缓解 scale concern。

  # ---- Supplementary θ-sensitivity (median 档要求) ----

  - name: theta_sensitivity_full_sweep
    plan_id: "Supplementary: θ=0.55-0.70 full sweep figure"
    description: "θ-sensitivity full sweep across 4 domains × all models"
    expected_results:
      wiki_stable_range: "K*=1 for all θ in [0.55, 0.70]"
      c4_stable_range: "K*=2 for θ ∈ [0.55, 0.63], K*=1 for θ ≥ 0.65 (most models)"
      code_stable_range: "K*=2 for θ ∈ [0.55, 0.63] (competent models), K*=1 always (Pythia, Mistral)"
      arxiv_stable_range: "K*=3 for θ ∈ [0.55, 0.65], K*=2 for θ ≥ 0.67"
      domain_ceiling_clean_fit_pct: 88
    result_rationale: >
      Median 档要求 θ=0.55-0.70 全谱呈现。结果显示：
      (a) 极端域（Wiki, arXiv）θ-robust：Wiki 对任何 θ 都 K*=1，
      arXiv 在 θ≤0.65 时 K*=3 稳健（2v3 AUC 范围 0.61-0.65 across models）；
      (b) 中间域（C4, Code）θ-sensitive：θ 从 0.60 升至 0.65 时
      C4 的 K*=2 models 中约一半 flip to K*=1；
      (c) domain_ceiling_clean_fit_pct ~88%：定义为 "在 θ=0.60 下，
      domain-competent models 的 K* 符合 domain ceiling 预测的比例"。
      5 models × 4 domains = 20 model-domain combinations（排除 OLMo arXiv
      capacity failure），domain ceiling 预测正确 ~17-18/20 = 85-90%。
      不完美匹配来自 Mistral C4 K*=1（ceiling=2）和 Pythia Code K*=1（ceiling=2）。
      Median 档 reviewer 认为 88% fit 合理但 "not clean enough to call
      it a framework — call it an empirical tendency"。
    tables:
      - name: "Figure 4 data: θ-sensitivity across 4 domains"
        content: |
          | Domain | θ=0.55 | θ=0.60 | θ=0.65 | θ=0.70 |
          |--------|--------|--------|--------|--------|
          | Wiki | all K*=1 | all K*=1 | all K*=1 | all K*=1 |
          | C4 | 8/9 K*=2 | 7/9 K*=2 | 4/9 K*=2 | 1-2/9 K*=2 |
          | Code | 3/5 K*=2 | 3/5 K*=2 | 2/5 K*=2 | 1/5 K*=2 |
          | arXiv | 5/5 K*=3 | 5/5 K*=3 | 4-5/5 K*=3 | 2-3/5 K*=3 |
    figures_description:
      - "主文 Figure 4: 4-domain θ-sensitivity heatmap, colored by K* value"
    analysis: >
      θ-sensitivity full sweep 是 median 档 reviewer 的 explicit request。
      4-domain 呈现比 C4-only 更有说服力——极端域的 θ-robustness 与
      中间域的 θ-sensitivity 形成 meaningful contrast。
      domain_ceiling_clean_fit_pct ~88% 在 median 档范围 [85, 92] 内。

  # ---- arXiv Cross-Scorer Bootstrap CI (median 档补充要求) ----

  - name: arxiv_cross_scorer_bootstrap_ci
    plan_id: "Supplementary: arXiv cross-scorer bootstrap CI"
    description: "Complete bootstrap CI for arXiv cross-scorer results, addressing Qwen-7B K*=3→2 drop"
    expected_results:
      qwen7b_crossscorer_2v3_auc: 0.5989
      qwen7b_crossscorer_2v3_ci: "[0.583, 0.615]"
      qwen7b_crossscorer_k_star: 2
      llama8b_crossscorer_2v3_ci: "[0.605, 0.635]"
      llama8b_crossscorer_k_star: 3
      mistral7b_crossscorer_2v3_ci: "[0.592, 0.623]"
      mistral7b_crossscorer_k_star: 3
      qwen1b5_crossscorer_2v3_ci: "[0.617, 0.647]"
      qwen1b5_crossscorer_k_star: 3
    result_rationale: >
      Qwen-7B arXiv cross-scorer 2v3 AUC=0.5989，CI [0.583, 0.615]——CI 横跨 θ=0.60，
      K*=2 判定 marginal。其他 3 个 cross-scorer 条件 K*=3 保持（CI lower > 0.60）。
      Median 档 reviewer 将 Qwen-7B drop 解读为："same-family scorer 在 arXiv 上
      给 Qwen-7B 一个 marginal boost (+2.7pp)，换 cross-family scorer 后消失。
      这与 Wikipedia scorer confound 是同一 phenomenon 的 weaker manifestation。"
      完整 bootstrap CI 的呈现被 reviewer 认为是 "necessary transparency"。
      cross_scorer_kstar_preservation_rate = 3/4 = 0.75，在 median 档范围 [0.75, 0.85]
      下界。论文需在正文讨论此 partial preservation 并承认 "scorer confound
      exists at varying degrees across domains, warranting cross-scorer validation
      as standard practice"。
    tables:
      - name: "Table 13b: arXiv cross-scorer bootstrap CI (complete)"
        content: |
          | Model | Scorer | 2v3 AUC | 95% CI | K* |
          |-------|--------|---------|--------|-----|
          | Qwen-1.5B | Pythia | 0.632 | [0.617, 0.647] | 3 ✅ |
          | LLaMA-8B | Pythia | 0.620 | [0.605, 0.635] | 3 ✅ |
          | Mistral-7B | Pythia | 0.608 | [0.592, 0.623] | 3 ✅ |
          | Qwen-7B | Pythia | 0.599 | [0.583, 0.615] | 2 ⚠️ |
    figures_description:
      - "arXiv cross-scorer CI forest plot, showing Qwen-7B as the only model with CI crossing θ"
    analysis: >
      Complete CI 呈现回应 scorer confound concern。3/4 preservation
      足以维持 "arXiv K*=3 is robust under cross-scorer for most models"
      的 claim，但需加 caveat for Qwen-7B。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fba02ca-31e3-4afa-8d04-049c98f87a54",
  "isSidechain": false,
  "requestId": "req_011CbBgTrTs5JC55rHVYi4RD",
  "type": "assistant",
  "uuid": "8249fd8d-498e-472d-923e-e037cd7309b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TvCQ7s7pGjXvH4wYvzL8w5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5421,
      "cache_read_input_tokens": 95453,
      "output_tokens": 30293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 30293,
          "cache_read_input_tokens": 95453,
          "cache_creation_input_tokens": 5421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5421
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑 核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domai…",
  "leafUuid": "8249fd8d-498e-472d-923e-e037cd7309b8",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-dependent K* saturation with cross-model validation",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Code 域 pending 结果部分确认（一个 K*=2 一个 K*=1，或两个均 marginal），domain ceiling 框架需加 caveat；或审稿人对 C3/θ 提出实质性质疑 核心假设：['Mistral-7B Code K*=1（与其 C4 K*=1 模式一致，code domai…",
  "leafUuid": "8249fd8d-498e-472d-923e-e037cd7309b8",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Domain-dependent K* saturation with cross-model validation",
  "sessionId": "bb9f5c87-e174-4459-9a60-98cfb2795a48"
}
```

---
