# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：C1' domain-dependent bounded saturation 被视为 novel empirical contribution；C3 

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/bb107442-4cbe-4f88-86a5-deb9b79e1c8a.jsonl`
- **Structured JSON:** [`9dd7fd6bfc959fa62d15.json`](../../sessions/9d/9dd7fd6bfc959fa62d15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T11:32:57.982Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T11:32:57.982Z",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：C1' domain-dependent bounded saturation 被视为 novel empirical contribution；C3 binary filtering 被接受为足够的 proof-of-concept；borderline CIs 不被视为致命缺陷\n核心假设：['K*∈{1,2,3} 三级域阶梯被接受为 non-trivial 发现——reviewer 认同 DPI 不给上界而实证上界如此低是 surprising', \"θ=0.60 三层 justification（Cohen's h + permutation + sharp discontinuity）被接受，θ-sensitivity 作为 transparent disclosure 而非 weakness\", \"C3: exp-006 C4 filtering + exp-009 dose-response 足够支撑 'K*-aware binary filtering outperforms' claim，reviewer 不追问 cross-model/cross-domain filtering replication\", \"Qwen-cont CI lower=0.6015 被消化为 '7/8 robust pattern with one marginal case'，不动摇 dominant mode claim\", '5 architecture families (1B-14B) + DPI theoretical guarantee 足以应对 scale criticism', \"'one-wash laundering' 概念引起共鸣，EMNLP 2026 special theme on data governance 加分\"]\n关键指标范围：{'arr_overall': [3.5, 4.0], 'arr_soundness': [3.5, 4.0], 'arr_excitement': [3.5, 4.0], 'arr_clarity': [3.5, 4.5], 'meta_recommendation': 'accept (Main)', 'prob_emnlp_main': [0.5, 0.7], 'prob_emnlp_findings': [0.85, 0.95]}\n叙事方向：原始 framing 完全成立。C1' 作为首次系统测量 K* + domain-dependent bounded saturation 的 characterization study，三级域阶梯为 headline result。C3 作为 practical validation 自洽——binary filtering 在 K*=2 域上优于 graduated，α monotonicity 作为 K* boundary 的独立确认。无需调整 claims。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\nfocus: 不包含 exp_026 arXiv graduated filtering 的负向结果。论文 Section 5 维持当前写法（仅含 C4 filtering + Pythia replication），不加 arXiv filtering 数据。评估这种版本的审稿得分。\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains（C4, Wikipedia, arXiv）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现三级域阶梯：Wikipedia(1) < C4(2) < arXiv(3)\n- **Web text K*=2 是 dominant mode**（7/8 configurations），展现跨模型架构、跨解码策略的一致性\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的唯一主导因素**：scorer control 后，model scale/architecture/decoding strategy 均不改变域内 K* 一致性\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\n> **7/8 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的三级域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a three-level domain hierarchy: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text at K*=2 (7/8 model configurations, 5 architecture families, 1B-8B), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-8B) 覆盖了当前开源生态的主要架构。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 是 outlier 还是 systematic？\"** → Cross-scorer validation 确认是 text-intrinsic（非 scorer artifact）。Mistral 可能因训练数据/alignment 差异导致生成文本在一代后即失去 depth-distinguishing structure。这强化了 domain/model dependence 的核心论点。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**exp-008 实证验证**：retrain-chain (Pythia-1.4B LoRA) K*≥4（1v2=0.9484, 2v3=0.8888, 3v4=0.7982），远高于 prompt-chain K*=2。原因：LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），使各代高度可区分。这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss），而非 retrain-chain 的 upper bound。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 5K docs, depth\n    0-5, scorer=Qwen2.5-1.5B. 测试 K* 是否随模型规模变化。（实际参数已从原计划 1K/depth 0-3 扩展以匹配其他实验配置）'\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  registry_id: exp_004_7b_crossscale\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: exp_006_graduated_filtering\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: exp_008_retrain_chain_v2\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: '>=4'\n    pairwise_auc:\n      0v1: 0.9847\n      1v2: 0.9484\n      2v3: 0.8888\n      3v4: 0.7982\n    pairwise_jsd:\n      0v1: 0.17\n      1v2: 0.12\n      2v3: 0.064\n      3v4: 0.04\n    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts\n      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic\n      boundary.\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: exp_009_dose_50pct\n  status: DONE\n  conclusion: failed\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: exp_011_llm_zeroshot\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_012_binary_confidence\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features。如果 neural probe 也给 K*=2 → C1'' claim 从 \"our features\n    find K*=2\" 升级为 \"K*=2 is data-intrinsic boundary\"。[D014 升级 P0：Reviewer 评估为最高边际价值实验]'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_015_neural_probe\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_016_base_vs_instruct\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- id: exp-018\n  claim: 1\n  description: 'Cross-family universality: LLaMA-3.1-8B, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 跨模型家族验证 K*。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_018_llama8b_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9225\n      1v2: 0.6123\n      2v3: 0.5274\n      3v4: 0.5138\n      4v5: 0.5097\n    jsd:\n      0v1: 0.077\n      1v2: 0.012\n      2v3: 0.005\n    bootstrap_ci:\n      0v1:\n        auc: 0.9224\n        ci_lower: 0.9174\n        ci_upper: 0.9272\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6123\n        ci_lower: 0.6028\n        ci_upper: 0.6216\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5273\n        ci_lower: 0.5169\n        ci_upper: 0.5378\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5168\n        ci_lower: 0.5062\n        ci_upper: 0.5275\n        perm_p: 0.0037\n      4v5:\n        auc: 0.5159\n        ci_lower: 0.5052\n        ci_upper: 0.5268\n        perm_p: 0.0035\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n- id: exp-019\n  claim: 1\n  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_019_mistral7b_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9843\n      1v2: 0.5935\n      2v3: 0.5402\n      3v4: 0.5232\n      4v5: 0.5181\n    bootstrap_ci_1v2:\n      ci_lower: 0.5835\n      ci_upper: 0.6032\n      p_auc_leq_060: 0.9017\n    jsd:\n      0v1: 0.124194\n      1v2: 0.008051\n      2v3: 0.005047\n      3v4: 0.004516\n      4v5: 0.004109\n    ordinal_mae: 1.2275\n    ordinal_accuracy: 0.3567\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n- id: exp-020\n  claim:\n  - 1\n  - 3\n  description: 'Pythia-1.4B decoding ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2,\n    C4 5K docs, depth 0-5. 跨模型验证解码策略对 K* 的不变性。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: exp_020_pythia_decoding\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy:\n      K_star: 2\n      auc:\n        0v1: 0.9992\n        1v2: 0.8838\n        2v3: 0.5342\n        3v4: 0.5228\n        4v5: 0.5162\n    nuc09:\n      K_star: 2\n      auc:\n        0v1: 0.9948\n        1v2: 0.677\n        2v3: 0.5549\n        3v4: 0.5299\n        4v5: 0.5013\n    t07:\n      K_star: 2\n      auc:\n        0v1: 0.9965\n        1v2: 0.7265\n        2v3: 0.5941\n        3v4: 0.5698\n        4v5: 0.5284\n    t12:\n      K_star: 2\n      auc:\n        0v1: 0.9933\n        1v2: 0.6172\n        2v3: 0.5226\n        3v4: 0.517\n        4v5: 0.5051\n- id: exp-021\n  claim: 1\n  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512\n    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_021_length_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    128tok:\n      K_star: 2\n      1v2_auc: 0.6219\n    256tok:\n      K_star: 2\n      1v2_auc: 0.6282\n    512tok:\n      K_star: 2\n      1v2_auc: 0.6073\n    all_K_star_2: true\n    bootstrap_ci:\n      512tok_1v2:\n        auc: 0.6073\n        ci_lower: 0.5979\n        ci_upper: 0.6166\n        perm_p: 0.0001\n        verdict: BORDERLINE\n- id: exp-022\n  claim:\n  - 1\n  - 2\n  description: '4x4 cross-scorer matrix: 4 generators × 4 scorers, 验证 scorer independence\n    完整性。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-021\n  registry_id: exp_022_cross_scorer_matrix\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 12\n    completed: 12\n    K_star_distribution:\n      K2: 11\n      K1: 1\n    matrix:\n      pythia_greedy×olmo:\n        K_star: 2\n        1v2: 0.8811\n      pythia_greedy×pythia:\n        K_star: 2\n        1v2: 0.8838\n      pythia_greedy×qwen_base:\n        K_star: 2\n        1v2: 0.8814\n      pythia_greedy×qwen_instruct:\n        K_star: 2\n        1v2: 0.8818\n      qwen_base×olmo:\n        K_star: 2\n        1v2: 0.6047\n      qwen_base×pythia:\n        K_star: 2\n        1v2: 0.617\n      qwen_base×qwen_base:\n        K_star: 2\n        1v2: 0.6262\n      qwen_base×qwen_instruct:\n        K_star: 2\n        1v2: 0.6273\n      qwen_cont256×olmo:\n        K_star: 2\n        1v2: 0.6028\n      qwen_cont256×pythia:\n        K_star: 1\n        1v2: 0.5979\n      qwen_cont256×qwen_base:\n        K_star: 2\n        1v2: 0.6282\n      qwen_cont256×qwen_instruct:\n        K_star: 2\n        1v2: 0.6072\n    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:\n      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to\n      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'\n- id: exp-023\n  claim:\n  - 1\n  description: 'Domain ablation: Wikipedia seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 验证 K*=2 是否跨数据域一致（C4\n    vs Wikipedia）。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_023_domain_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    1v2_auc: 0.6193\n    2v3_auc: 0.5498\n    all_folds_above_060: true\n    top_feature: freq_entropy\n    ordinal_accuracy: 0.377\n- id: exp-024\n  claim:\n  - 1\n  description: 'Domain ablation: arXiv abstracts seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 第三域验证—— 技术文本与\n    web text (C4) / 百科 (Wikipedia) 分布差异大，三域一致则 domain 维度从 Limitation 升级为 evidence。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_024_arxiv_domain\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    pairwise_auc:\n      0v1: 0.9946\n      1v2: 0.858\n      2v3: 0.6427\n      3v4: 0.5437\n      4v5: 0.5294\n    bootstrap_ci:\n      0v1:\n        auc: 0.9946\n        ci_lower: 0.9929\n        ci_upper: 0.9961\n        perm_p: 0.0001\n      1v2:\n        auc: 0.858\n        ci_lower: 0.848\n        ci_upper: 0.8679\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6427\n        ci_lower: 0.6275\n        ci_upper: 0.6575\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5437\n        ci_lower: 0.5276\n        ci_upper: 0.5598\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5294\n        ci_lower: 0.5133\n        ci_upper: 0.5455\n        perm_p: 0.0006\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First\n      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\n- id: exp-025\n  claim: 3\n  description: 'Pythia-1.4B filtering replication: LoRA rank=8 continued pretraining\n    on C4 depth chain, 3 strategies (binary/graduated/no-filter) × 3 seeds, MMLU+HellaSwag.\n    验证 filtering strategy ordering 跨模型一致性。'\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - exp-006\n  - exp-001\n  registry_id: exp_025_pythia_filtering\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 9/9\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    mmlu:\n      no_filter: 0.2568±0.0012\n      binary_ours: 0.2585±0.0004\n      graduated_a09: 0.2561±0.0009\n    hellaswag:\n      no_filter: 0.5250±0.0008\n      binary_ours: 0.5251±0.0001\n      graduated_a09: 0.5253±0.0007\n    delta_vs_no_filter:\n      binary_ours_mmlu: '+0.0017'\n      binary_ours_hellaswag: '+0.0000'\n      graduated_a09_mmlu: '-0.0007'\n      graduated_a09_hellaswag: '+0.0003'\n    key_finding: All three filtering strategies produce nearly identical results on\n      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering\n      binary>graduated>no_filter NOT confirmed.\n- id: exp-026\n  claim: 3\n  description: 'arXiv graduated vs binary filtering: Qwen2.5-1.5B base + LoRA rank=4,\n    arXiv depth chain (K*=3), 3 strategies (no_filter/binary/graduated α=0.9^d) ×\n    5 seeds, MMLU+HellaSwag. 关键实验：K*=3 域上 graduated 应超越 binary，展示 K*-aware filtering\n    增量价值。'\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - exp-006\n  - exp-024\n  registry_id: exp_026_arxiv_filtering\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 15/15\n    strategies:\n    - no_filter\n    - binary\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    mmlu:\n      no_filter: 0.5899±0.0008\n      binary: 0.5876±0.0004\n      graduated_a09: 0.5900±0.0011\n    hellaswag:\n      no_filter: 0.6600±0.0002\n      binary: 0.6642±0.0004\n      graduated_a09: 0.6599±0.0003\n    delta_vs_no_filter:\n      binary_mmlu: '-0.0023'\n      binary_hellaswag: '+0.0042'\n      graduated_mmlu: '+0.0001'\n      graduated_hellaswag: '-0.0001'\n    key_finding: All three strategies produce nearly identical results. Graduated\n      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU\n      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\n- id: exp-027\n  claim: 1\n  description: 'LaTeX markup removal ablation: 去除 arXiv 文本中的 LaTeX 格式标记后重新提取 15D features，验证\n    K*=3 是否依赖格式特征而非内容层 depth signal。排除替代假说。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-024\n  registry_id: exp_027_latex_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    k_star_preserved: true\n    pairwise_auc_original:\n      0v1: 0.9948\n      1v2: 0.8581\n      2v3: 0.6436\n      3v4: 0.544\n      4v5: 0.5299\n    pairwise_auc_stripped:\n      0v1: 0.9948\n      1v2: 0.8297\n      2v3: 0.6229\n      3v4: 0.5468\n      4v5: 0.5476\n    auc_delta:\n      0v1: 0\n      1v2: -0.028\n      2v3: -0.021\n      3v4: 0.003\n      4v5: 0.018\n    latex_reduction_by_depth:\n      depth_0: 0.6%\n      depth_5: 4.4%\n    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still\n      >θ=0.60). LaTeX format is NOT a confound.\n- id: exp-028\n  claim: 1\n  description: 'Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples,\n    确定 K*=2 判定所需最低样本量。回应 m4 reviewer concern。'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-007\n  registry_id: null\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- exp_id: exp_011_llm_zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- exp_id: exp_015_neural_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- exp_id: exp_006_graduated_filtering\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- exp_id: exp_004_7b_crossscale\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- exp_id: exp_A_alt_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9923\n      auc_1v2: 0.7012\n      auc_2v3: 0.587\n      mae: 1.006\n      accuracy: 0.417\n      spearman_rho_vs_baseline: 0.906\n    pythia_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.99\n      auc_1v2: 0.5923\n      auc_2v3: null\n      mae: 1.216\n      accuracy: 0.371\n      spearman_rho_vs_baseline: 0.942\n    olmo_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9918\n      auc_1v2: 0.6947\n      auc_2v3: null\n      mae: 1.016\n      accuracy: 0.413\n      spearman_rho_vs_baseline: 0.92\n    olmo_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.989\n      auc_1v2: 0.5858\n      auc_2v3: null\n      mae: 1.229\n      accuracy: 0.368\n      spearman_rho_vs_baseline: 0.902\n    key_finding: 'K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1\n      (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer\n      independence of feature ranking.'\n- exp_id: exp_B_14d_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    result: K*=2 stable across all 4 models after removing self_BLEU (14D)\n    key_finding: self_BLEU removal does not change K* boundary. FR-3 resolved.\n- exp_id: exp_C_permutation_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    resamples: 10000\n    all_boundary_pairs_p: <0.0001\n    key_finding: 10K permutation confirms all boundary p-values well below 0.01. FR-11\n      resolved.\n- exp_id: exp_D_obd_n500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    obd_accuracy_final: 0.38\n    obd_ci:\n    - 0.34\n    - 0.422\n    mcnemar_vs_gpt55_p: 0.0809\n    mcnemar_vs_claude_p: 0.0693\n    mcnemar_significant: false\n    multi_seed_std: 0\n    per_depth:\n      d0: 0.96\n      d1: 0.39\n      d2: 0.14\n      d3: 0.19\n      d4: 0.22\n    prob_merge_accuracy: 0.444\n    prob_merge_d4_bias: 0.8\n    note: v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant\n      — supports discussion.tex narrative\n- exp_id: exp_E_paired_stats\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_significant_pairs: 8/15\n    hellaswag_significant_pairs: 9/15\n    binary_ours_vs_all_mmlu: all significant\n    max_cohen_d_mmlu: 10.8\n    max_cohen_d_hellaswag: 8.98\n    graduated_a09_vs_dsir_corrected_p: 0.0523\n    cohen_d_method: d_av (Lakens 2013)\n    key_finding: 'binary-ours significantly outperforms all alternatives on MMLU.\n      On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni\n      cummax bug fixed: MMLU 10/15→8/15. Cohen''s d changed to d_av.'\n    bugfix_note: Holm-Bonferroni cummax variable was never updated, causing 2 MMLU\n      pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal\n      vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\n- exp_id: exp_012_binary_confidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- exp_id: exp_kstar_theta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    output_files:\n    - kstar_theta_curve.pdf (32KB)\n    - kstar_theta_curve.png (335KB)\n    models:\n    - Qwen-rewrite\n    - Pythia\n    - OLMo\n    - Qwen-cont\n    depth_pairs: 5\n    key_finding: All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5.\n      θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical\n      resolved.\n- exp_id: exp_016_base_vs_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- exp_id: exp_018_llama8b_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9225\n      1v2: 0.6123\n      2v3: 0.5274\n      3v4: 0.5138\n      4v5: 0.5097\n    jsd:\n      0v1: 0.077\n      1v2: 0.012\n      2v3: 0.005\n    bootstrap_ci:\n      0v1:\n        auc: 0.9224\n        ci_lower: 0.9174\n        ci_upper: 0.9272\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6123\n        ci_lower: 0.6028\n        ci_upper: 0.6216\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5273\n        ci_lower: 0.5169\n        ci_upper: 0.5378\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5168\n        ci_lower: 0.5062\n        ci_upper: 0.5275\n        perm_p: 0.0037\n      4v5:\n        auc: 0.5159\n        ci_lower: 0.5052\n        ci_upper: 0.5268\n        perm_p: 0.0035\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n- exp_id: exp_019_mistral7b_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9843\n      1v2: 0.5935\n      2v3: 0.5402\n      3v4: 0.5232\n      4v5: 0.5181\n    bootstrap_ci_1v2:\n      ci_lower: 0.5835\n      ci_upper: 0.6032\n      p_auc_leq_060: 0.9017\n    jsd:\n      0v1: 0.124194\n      1v2: 0.008051\n      2v3: 0.005047\n      3v4: 0.004516\n      4v5: 0.004109\n    ordinal_mae: 1.2275\n    ordinal_accuracy: 0.3567\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n- exp_id: exp_020_pythia_decoding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy:\n      K_star: 2\n      auc:\n        0v1: 0.9992\n        1v2: 0.8838\n        2v3: 0.5342\n        3v4: 0.5228\n        4v5: 0.5162\n    nuc09:\n      K_star: 2\n      auc:\n        0v1: 0.9948\n        1v2: 0.677\n        2v3: 0.5549\n        3v4: 0.5299\n        4v5: 0.5013\n    t07:\n      K_star: 2\n      auc:\n        0v1: 0.9965\n        1v2: 0.7265\n        2v3: 0.5941\n        3v4: 0.5698\n        4v5: 0.5284\n    t12:\n      K_star: 2\n      auc:\n        0v1: 0.9933\n        1v2: 0.6172\n        2v3: 0.5226\n        3v4: 0.517\n        4v5: 0.5051\n- exp_id: exp_021_length_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    128tok:\n      K_star: 2\n      1v2_auc: 0.6219\n    256tok:\n      K_star: 2\n      1v2_auc: 0.6282\n    512tok:\n      K_star: 2\n      1v2_auc: 0.6073\n    all_K_star_2: true\n    bootstrap_ci:\n      512tok_1v2:\n        auc: 0.6073\n        ci_lower: 0.5979\n        ci_upper: 0.6166\n        perm_p: 0.0001\n        verdict: BORDERLINE\n- exp_id: exp_022_cross_scorer_matrix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 12\n    completed: 12\n    K_star_distribution:\n      K2: 11\n      K1: 1\n    matrix:\n      pythia_greedy×olmo:\n        K_star: 2\n        1v2: 0.8811\n      pythia_greedy×pythia:\n        K_star: 2\n        1v2: 0.8838\n      pythia_greedy×qwen_base:\n        K_star: 2\n        1v2: 0.8814\n      pythia_greedy×qwen_instruct:\n        K_star: 2\n        1v2: 0.8818\n      qwen_base×olmo:\n        K_star: 2\n        1v2: 0.6047\n      qwen_base×pythia:\n        K_star: 2\n        1v2: 0.617\n      qwen_base×qwen_base:\n        K_star: 2\n        1v2: 0.6262\n      qwen_base×qwen_instruct:\n        K_star: 2\n        1v2: 0.6273\n      qwen_cont256×olmo:\n        K_star: 2\n        1v2: 0.6028\n      qwen_cont256×pythia:\n        K_star: 1\n        1v2: 0.5979\n      qwen_cont256×qwen_base:\n        K_star: 2\n        1v2: 0.6282\n      qwen_cont256×qwen_instruct:\n        K_star: 2\n        1v2: 0.6072\n    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:\n      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to\n      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'\n- exp_id: exp_019b_mistral_cross_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9209\n      1v2: 0.5695\n      2v3: 0.5335\n      3v4: 0.514\n      4v5: 0.5184\n    bootstrap_ci:\n      0v1:\n        mean: 0.9209\n        ci_lower: 0.9189\n        ci_upper: 0.9229\n        pass_060: true\n      1v2:\n        mean: 0.5696\n        ci_lower: 0.5645\n        ci_upper: 0.5746\n        pass_060: false\n      2v3:\n        mean: 0.5335\n        ci_lower: 0.5283\n        ci_upper: 0.5382\n        pass_060: false\n      3v4:\n        mean: 0.514\n        ci_lower: 0.5063\n        ci_upper: 0.5213\n        pass_060: false\n      4v5:\n        mean: 0.5183\n        ci_lower: 0.5128\n        ci_upper: 0.5244\n        pass_060: false\n    jsd:\n      0v1: 0.08355\n      1v2: 0.007642\n      2v3: 0.004752\n      3v4: 0.004255\n      4v5: 0.003758\n    ordinal_mae: 1.3737\n    ordinal_accuracy: 0.3179\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n    key_finding: Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2\n      AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral\n      K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\n- exp_id: exp_023_domain_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    1v2_auc: 0.6193\n    2v3_auc: 0.5498\n    all_folds_above_060: true\n    top_feature: freq_entropy\n    ordinal_accuracy: 0.377\n- exp_id: exp_024_arxiv_domain\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    pairwise_auc:\n      0v1: 0.9946\n      1v2: 0.858\n      2v3: 0.6427\n      3v4: 0.5437\n      4v5: 0.5294\n    bootstrap_ci:\n      0v1:\n        auc: 0.9946\n        ci_lower: 0.9929\n        ci_upper: 0.9961\n        perm_p: 0.0001\n      1v2:\n        auc: 0.858\n        ci_lower: 0.848\n        ci_upper: 0.8679\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6427\n        ci_lower: 0.6275\n        ci_upper: 0.6575\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5437\n        ci_lower: 0.5276\n        ci_upper: 0.5598\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5294\n        ci_lower: 0.5133\n        ci_upper: 0.5455\n        perm_p: 0.0006\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First\n      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\n- exp_id: exp_025_pythia_arxiv\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.9877\n      1v2: 0.8047\n      2v3: 0.6545\n      3v4: 0.5507\n      4v5: 0.5287\n    pairwise_jsd:\n      0v1: 0.171338\n      1v2: 0.057344\n      2v3: 0.019524\n      3v4: 0.009917\n      4v5: 0.008846\n    bootstrap_ci:\n      0v1:\n        auc: 0.9876\n        ci_lower: 0.9851\n        ci_upper: 0.99\n        perm_p: 0.0001\n      1v2:\n        auc: 0.8047\n        ci_lower: 0.7934\n        ci_upper: 0.8162\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6544\n        ci_lower: 0.6401\n        ci_upper: 0.6688\n        perm_p: 0.0001\n      3v4:\n        auc: 0.55\n        ci_lower: 0.534\n        ci_upper: 0.5657\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5284\n        ci_lower: 0.5122\n        ci_upper: 0.5443\n        perm_p: 0.001\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    n_samples: 2200\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_mean\n    - surp_d1_skew\n    - surp_d1_mean\n    ordinal:\n      MAE: 0.8518\n      Accuracy: 0.4545\n    key_finding: Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv).\n      2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for\n      arXiv.\n- exp_id: exp_008_retrain_chain\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-008-retrain-chain\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_retrain_chain_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: '>=4'\n    pairwise_auc:\n      0v1: 0.9847\n      1v2: 0.9484\n      2v3: 0.8888\n      3v4: 0.7982\n    pairwise_jsd:\n      0v1: 0.17\n      1v2: 0.12\n      2v3: 0.064\n      3v4: 0.04\n    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts\n      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic\n      boundary.\n- exp_id: exp_009_dose_response\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 45\n    seeds: 5\n    ratios:\n    - 0.1\n    - 0.3\n    - 0.5\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated\n    cross_ratio_finding: 'Binary filtering consistently best across all ratios. Graduated\n      filtering = no_filter at every ratio. Effect size of binary advantage increases\n      with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp).\n      Original C3 hypothesis (graduated > binary) rejected.'\n    gpu_hours_total: 9.9\n- exp_id: exp_009_dose_10pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_30pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_50pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_10pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_30pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_50pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_10pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6058±0.0002\n        hellaswag: 0.6689±0.0007\n      binary_ours:\n        mmlu: 0.6079±0.0005\n        hellaswag: 0.6727±0.0008\n      graduated:\n        mmlu: 0.6066±0.0011\n        hellaswag: 0.6700±0.0015\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0021\n        p_mmlu: 0.001\n        delta_hellaswag: 0.0038\n        p_hellaswag: 0.0017\n      graduated_vs_binary:\n        delta_mmlu: -0.0014\n        p_mmlu: 0.0917\n        delta_hellaswag: -0.0027\n        p_hellaswag: 0.0399\n      graduated_vs_nofilter:\n        delta_mmlu: 0.0008\n        p_mmlu: 0.2706\n        delta_hellaswag: 0.0011\n        p_hellaswag: 0.0611\n    key_finding: Binary best. Graduated ≈ no_filter.\n- exp_id: exp_009_dose_30pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6069±0.0007\n        hellaswag: 0.6664±0.0020\n      binary_ours:\n        mmlu: 0.6082±0.0012\n        hellaswag: 0.6725±0.0007\n      graduated:\n        mmlu: 0.6072±0.0008\n        hellaswag: 0.6665±0.0014\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0013\n        p_mmlu: 0.0739\n        delta_hellaswag: 0.0061\n        p_hellaswag: 0.0036\n      graduated_vs_binary:\n        delta_mmlu: -0.001\n        p_mmlu: 0.3018\n        delta_hellaswag: -0.006\n        p_hellaswag: 0.0009\n      graduated_vs_nofilter:\n        delta_mmlu: 0.0003\n        p_mmlu: 0.6638\n        delta_hellaswag: 0.0002\n        p_hellaswag: 0.6646\n    key_finding: Binary best on HellaSwag (p=0.004). Graduated = no_filter.\n- exp_id: exp_009_dose_50pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6063±0.0013\n        hellaswag: 0.6680±0.0005\n      binary_ours:\n        mmlu: 0.6088±0.0011\n        hellaswag: 0.6731±0.0004\n      graduated:\n        mmlu: 0.6062±0.0009\n        hellaswag: 0.6679±0.0002\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0025\n        p_mmlu: 0.0377\n        delta_hellaswag: 0.0051\n        p_hellaswag: 2.0e-05\n      graduated_vs_binary:\n        delta_mmlu: -0.0026\n        p_mmlu: 0.0257\n        delta_hellaswag: -0.0052\n        p_hellaswag: 3.0e-05\n      graduated_vs_nofilter:\n        delta_mmlu: -0.0001\n        p_mmlu: 0.89\n        delta_hellaswag: -0.0001\n        p_hellaswag: 0.706\n    key_finding: Binary significantly best (HellaSwag p<0.001). Graduated = no_filter\n      exactly.\n- exp_id: exp_026_feature_stability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_016_qwen_base (prompt-chain, K*=2)\n    results:\n      15D:\n        num_tested: 1\n        num_kstar_2: 1\n        min_1v2_auc: 0.6262\n        mean_1v2_auc: 0.6262\n      10D:\n        num_tested: 5\n        num_kstar_2: 5\n        min_1v2_auc: 0.6153\n        mean_1v2_auc: 0.6191\n      8D:\n        num_tested: 5\n        num_kstar_2: 5\n        min_1v2_auc: 0.6056\n        mean_1v2_auc: 0.6159\n      5D:\n        num_tested: 5\n        num_kstar_2: 2\n        min_1v2_auc: 0.5856\n        mean_1v2_auc: 0.5998\n      3D_top3:\n        num_tested: 1\n        num_kstar_2: 0\n        min_1v2_auc: 0.5871\n        mean_1v2_auc: 0.5871\n    all_above_theta: false\n    key_finding: 'Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust\n      (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856).\n      Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where\n      all subsets trivially passed (min=0.8314).'\n    previous_run_note: v1 used retrain-chain data (K*=4), where all subsets trivially\n      passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary\n      robustness.\n- exp_id: exp_027_retrain_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_iterations: 10000\n    pairs:\n      0v1:\n        auc_point: 0.9847\n        ci_lower: 0.9828\n        ci_upper: 0.9864\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      1v2:\n        auc_point: 0.9482\n        ci_lower: 0.9443\n        ci_upper: 0.952\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      2v3:\n        auc_point: 0.8885\n        ci_lower: 0.8829\n        ci_upper: 0.894\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      3v4:\n        auc_point: 0.7977\n        ci_lower: 0.7903\n        ci_upper: 0.8051\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n    key_finding: All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min\n      CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\n- exp_id: exp_027\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kstar_ci: 4\n    0v1_auc: 0.9847\n    0v1_ci:\n    - 0.9828\n    - 0.9864\n    0v1_perm_p: 0.0001\n    1v2_auc: 0.9482\n    1v2_ci:\n    - 0.9443\n    - 0.952\n    1v2_perm_p: 0.0001\n    2v3_auc: 0.8885\n    2v3_ci:\n    - 0.8829\n    - 0.894\n    2v3_perm_p: 0.0001\n    3v4_auc: 0.7977\n    3v4_ci:\n    - 0.7903\n    - 0.8051\n    3v4_perm_p: 0.0001\n    all_ci_lower_above_theta: true\n- exp_id: exp_026_feature_stability_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_001_pythia prompt-chain (K*=2)\n    results:\n      15D:\n        num_tested: 1\n        num_pass: 1\n        min_1v2_auc: 0.6262\n        mean_1v2_auc: 0.6262\n      10D:\n        num_tested: 5\n        num_pass: 5\n        min_1v2_auc: 0.6153\n        mean_1v2_auc: 0.6191\n      8D:\n        num_tested: 5\n        num_pass: 5\n        min_1v2_auc: 0.6056\n        mean_1v2_auc: 0.6159\n      5D:\n        num_tested: 5\n        num_pass: 2\n        min_1v2_auc: 0.5856\n        mean_1v2_auc: 0.5998\n      3D_top3:\n        num_tested: 1\n        num_pass: 0\n        min_1v2_auc: 0.5871\n        mean_1v2_auc: 0.5871\n    key_finding: 8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile\n      (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\n- exp_id: exp_arXiv_olmo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.9958\n    auc_1v2: 0.5034\n    auc_2v3: 0.5069\n    auc_3v4: 0.5021\n    auc_4v5: 0.5037\n    jsd_0v1: 0.329\n    ordinal_acc: 0.33\n- exp_id: exp_arXiv_llama8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    auc_0v1: 0.9754\n    auc_1v2: 0.8447\n    auc_2v3: 0.6215\n    auc_3v4: 0.5362\n    auc_4v5: 0.5331\n    jsd_0v1: 0.1296\n    jsd_1v2: 0.0785\n    jsd_2v3: 0.0177\n    ordinal_acc: 0.4549\n    ordinal_mae: 0.8806\n- exp_id: exp_wiki_pythia\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_wiki_olmo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_wiki_pythia_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.975\n    auc_1v2: 0.5846\n    auc_2v3: 0.5445\n    auc_3v4: 0.5205\n    auc_4v5: 0.5168\n    jsd_0v1: 0.080065\n    jsd_1v2: 0.007773\n    ordinal_acc: 0.3503\n- exp_id: exp_wiki_olmo_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.9932\n    auc_1v2: 0.4986\n    auc_2v3: 0.5012\n    auc_3v4: 0.5057\n    auc_4v5: 0.5009\n    jsd_0v1: 0.1688\n    ordinal_acc: 0.3227\n- exp_id: exp_arXiv_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.983\n      1v2: 0.835\n      2v3: 0.626\n      3v4: 0.544\n      4v5: 0.513\n    pairwise_jsd:\n      0v1: 0.1656\n      1v2: 0.0668\n      2v3: 0.0156\n      3v4: 0.0089\n      4v5: 0.0061\n    ordinal_mae: 0.9\n    ordinal_accuracy: 0.446\n- exp_id: exp_wiki_llama8b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    ordinal_mae: 1.2954\n    ordinal_accuracy: 0.3313\n    auc_0v1: 0.9316\n    auc_1v2: 0.5954\n    auc_2v3: 0.5392\n    auc_3v4: 0.5221\n    auc_4v5: 0.5212\n    jsd_0v1: 0.06169\n    jsd_1v2: 0.00931\n- exp_id: exp_arXiv_mistral7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.9848\n      1v2: 0.8201\n      2v3: 0.6275\n      3v4: 0.5295\n      4v5: 0.5295\n    jsd:\n      0v1: 0.14249\n      1v2: 0.076232\n      2v3: 0.018972\n      3v4: 0.009908\n      4v5: 0.008877\n    ordinal_mae: 0.8958\n    ordinal_accuracy: 0.4474\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_mean\n    - surp_d2_mean\n- exp_id: exp_wiki_mistral7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 1\n    ordinal_mae: 1.3445\n    ordinal_accuracy: 0.3273\n    auc_0v1: 0.9607\n    auc_1v2: 0.5552\n    auc_2v3: 0.5236\n    auc_3v4: 0.5181\n    auc_4v5: 0.5012\n    jsd_0v1: 0.054134\n    jsd_1v2: 0.005678\n    jsd_2v3: 0.003698\n    jsd_3v4: 0.003459\n    jsd_4v5: 0.003274\n- exp_id: exp_14b_c4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9598\n      1v2: 0.621\n      2v3: 0.5494\n      3v4: 0.5243\n      4v5: 0.5154\n    pairwise_jsd:\n      0v1: 0.1097\n      1v2: 0.0112\n      2v3: 0.0062\n      3v4: 0.0044\n      4v5: 0.0036\n    bootstrap_ci:\n      0v1:\n      - 0.9564\n      - 0.963\n      1v2:\n      - 0.6119\n      - 0.6304\n      2v3:\n      - 0.5392\n      - 0.5594\n      3v4:\n      - 0.514\n      - 0.5346\n      4v5:\n      - 0.5045\n      - 0.5265\n    permutation_p:\n      0v1: <0.001\n      1v2: <0.001\n      2v3: <0.001\n      3v4: <0.001\n      4v5: <0.001\n    k_star_statistically_confirmed: true\n    ordinal_mae: 1.2266\n    ordinal_accuracy: 0.3497\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_d2_mean\n    key_finding: K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119)\n      > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\n- exp_id: exp_32b_c4\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_wiki_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    auc_0v1: 0.9673\n    auc_1v2: 0.6108\n    auc_2v3: 0.5562\n    auc_3v4: 0.5297\n    auc_4v5: 0.529\n    jsd_0v1: 0.083514\n    jsd_1v2: 0.010991\n    jsd_2v3: 0.00555\n    jsd_3v4: 0.004611\n    jsd_4v5: 0.003894\n    ordinal_mae: 1.2501\n    ordinal_accuracy: 0.3532\n- exp_id: exp_wiki_scorer_confound\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    confound_verdict: confirmed\n    auc_0v1: 0.9404\n    auc_1v2: 0.587\n    auc_2v3: 0.5456\n    auc_3v4: 0.525\n    auc_4v5: 0.5172\n    critical_delta_1v2: -0.0238\n- exp_id: exp_wiki_scorer_confound_1b5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    confound_verdict: confirmed\n    auc_0v1: 0.9729\n    auc_1v2: 0.5994\n    auc_2v3: 0.533\n    auc_3v4: 0.5214\n    auc_4v5: 0.5068\n    jsd_0v1: 0.0886\n    ordinal_mae: 1.2995\n    ordinal_accuracy: 0.3466\n- exp_id: exp_arXiv_qwen7b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 2\n    auc_0v1: 0.9575\n    auc_1v2: 0.8171\n    auc_2v3: 0.5989\n    auc_3v4: 0.5417\n    auc_4v5: 0.5192\n    jsd_0v1: 0.137085\n    jsd_1v2: 0.059688\n    jsd_2v3: 0.013508\n    jsd_3v4: 0.009125\n    jsd_4v5: 0.006738\n    ordinal_mae: 0.9617\n    ordinal_accuracy: 0.4255\n- exp_id: exp_arXiv_qwen1b5_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    auc_0v1: 0.9748\n    auc_1v2: 0.8105\n    auc_2v3: 0.6317\n    auc_3v4: 0.5437\n    auc_4v5: 0.5294\n    jsd_0v1: 0.154297\n    jsd_1v2: 0.066782\n    jsd_2v3: 0.019268\n    jsd_3v4: 0.008867\n    jsd_4v5: 0.006991\n    ordinal_mae: 0.9017\n    ordinal_accuracy: 0.4402\n- exp_id: exp_arXiv_llama8b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    auc_0v1: 0.9629\n    auc_1v2: 0.8433\n    auc_2v3: 0.6201\n    auc_3v4: 0.523\n    auc_4v5: 0.5245\n    jsd_0v1: 0.1214\n    jsd_1v2: 0.0815\n    jsd_2v3: 0.0195\n    jsd_3v4: 0.0083\n    jsd_4v5: 0.0082\n    ordinal_mae: 0.9025\n    ordinal_accuracy: 0.4407\n    scorer: pythia-1.4b\n- exp_id: exp_arXiv_mistral7b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    scorer: pythia-1.4b\n    auc_0v1: 0.9798\n    auc_1v2: 0.8141\n    auc_2v3: 0.6075\n    auc_3v4: 0.5489\n    auc_4v5: 0.5391\n    jsd_0v1: 0.135575\n    jsd_1v2: 0.078\n    jsd_2v3: 0.020452\n    jsd_3v4: 0.010992\n    jsd_4v5: 0.008831\n    ordinal_mae: 0.9061\n    ordinal_accuracy: 0.4412\n- exp_id: exp_025_pythia_filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 9/9\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    mmlu:\n      no_filter: 0.2568±0.0012\n      binary_ours: 0.2585±0.0004\n      graduated_a09: 0.2561±0.0009\n    hellaswag:\n      no_filter: 0.5250±0.0008\n      binary_ours: 0.5251±0.0001\n      graduated_a09: 0.5253±0.0007\n    delta_vs_no_filter:\n      binary_ours_mmlu: '+0.0017'\n      binary_ours_hellaswag: '+0.0000'\n      graduated_a09_mmlu: '-0.0007'\n      graduated_a09_hellaswag: '+0.0003'\n    key_finding: All three filtering strategies produce nearly identical results on\n      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering\n      binary>graduated>no_filter NOT confirmed.\n- exp_id: exp_026_arxiv_filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 15/15\n    strategies:\n    - no_filter\n    - binary\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    mmlu:\n      no_filter: 0.5899±0.0008\n      binary: 0.5876±0.0004\n      graduated_a09: 0.5900±0.0011\n    hellaswag:\n      no_filter: 0.6600±0.0002\n      binary: 0.6642±0.0004\n      graduated_a09: 0.6599±0.0003\n    delta_vs_no_filter:\n      binary_mmlu: '-0.0023'\n      binary_hellaswag: '+0.0042'\n      graduated_mmlu: '+0.0001'\n      graduated_hellaswag: '-0.0001'\n    key_finding: All three strategies produce nearly identical results. Graduated\n      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU\n      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\n- exp_id: exp_027_latex_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    k_star_preserved: true\n    pairwise_auc_original:\n      0v1: 0.9948\n      1v2: 0.8581\n      2v3: 0.6436\n      3v4: 0.544\n      4v5: 0.5299\n    pairwise_auc_stripped:\n      0v1: 0.9948\n      1v2: 0.8297\n      2v3: 0.6229\n      3v4: 0.5468\n      4v5: 0.5476\n    auc_delta:\n      0v1: 0\n      1v2: -0.028\n      2v3: -0.021\n      3v4: 0.003\n      4v5: 0.018\n    latex_reduction_by_depth:\n      depth_0: 0.6%\n      depth_5: 4.4%\n    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still\n      >θ=0.60). LaTeX format is NOT a confound.\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T11:32:57.985Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T11:32:57.985Z",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-18T11:32:58.007Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：C1' domain-dependent bounded saturation 被视为 novel empirical contribution；C3 binary filtering 被接受为足够的 proof-of-concept；borderline CIs 不被视为致命缺陷
核心假设：['K*∈{1,2,3} 三级域阶梯被接受为 non-trivial 发现——reviewer 认同 DPI 不给上界而实证上界如此低是 surprising', "θ=0.60 三层 justification（Cohen's h + permutation + sharp discontinuity）被接受，θ-sensitivity 作为 transparent disclosure 而非 weakness", "C3: exp-006 C4 filtering + exp-009 dose-response 足够支撑 'K*-aware binary filtering outperforms' claim，reviewer 不追问 cross-model/cross-domain filtering replication", "Qwen-cont CI lower=0.6015 被消化为 '7/8 robust pattern with one marginal case'，不动摇 dominant mode claim", '5 architecture families (1B-14B) + DPI theoretical guarantee 足以应对 scale criticism', "'one-wash laundering' 概念引起共鸣，EMNLP 2026 special theme on data governance 加分"]
关键指标范围：{'arr_overall': [3.5, 4.0], 'arr_soundness': [3.5, 4.0], 'arr_excitement': [3.5, 4.0], 'arr_clarity': [3.5, 4.5], 'meta_recommendation': 'accept (Main)', 'prob_emnlp_main': [0.5, 0.7], 'prob_emnlp_findings': [0.85, 0.95]}
叙事方向：原始 framing 完全成立。C1' 作为首次系统测量 K* + domain-dependent bounded saturation 的 characterization study，三级域阶梯为 headline result。C3 作为 practical validation 自洽——binary filtering 在 K*=2 域上优于 graduated，α monotonicity 作为 K* boundary 的独立确认。无需调整 claims。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-contamination
focus: 不包含 exp_026 arXiv graduated filtering 的负向结果。论文 Section 5 维持当前写法（仅含 C4 filtering + Pythia replication），不加 arXiv filtering 数据。评估这种版本的审稿得分。

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

DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains（C4, Wikipedia, arXiv）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：

- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现三级域阶梯：Wikipedia(1) < C4(2) < arXiv(3)
- **Web text K*=2 是 dominant mode**（7/8 configurations），展现跨模型架构、跨解码策略的一致性
- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）
- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节
- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据
- **Domain 是 K* 的唯一主导因素**：scorer control 后，model scale/architecture/decoding strategy 均不改变域内 K* 一致性
- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分

**子组件：**

**(a) K*=2 as dominant mode for web text (7/8 configurations)**
> **7/8 model configurations yield K*=2 on C4 web text：**
>
> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |
> |-------|-----------|---------|--------|-----------------|
> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |
> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |
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
> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60
> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变
> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1
> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1
> - Paper 措辞："K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies."

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
- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的三级域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（"one-wash laundering" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。
- **Headline result template**: "Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a three-level domain hierarchy: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text at K*=2 (7/8 model configurations, 5 architecture families, 1B-8B), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity."

## Anticipated Reviewer Concerns & Responses

1. **"K*∈{1,2,3} 范围太小，结论是否 trivial？"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。
2. **"只基于小模型（≤8B），能推广到更大模型吗？"** → 5 architecture families (1B-8B) 覆盖了当前开源生态的主要架构。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。
3. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。
4. **"arXiv K*=3 样本量够吗？"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。
5. **"Mistral K*=1 是 outlier 还是 systematic？"** → Cross-scorer validation 确认是 text-intrinsic（非 scorer artifact）。Mistral 可能因训练数据/alignment 差异导致生成文本在一代后即失去 depth-distinguishing structure。这强化了 domain/model dependence 的核心论点。
6. **"Prompt-chain 不代表真实世界递归污染"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**exp-008 实证验证**：retrain-chain (Pythia-1.4B LoRA) K*≥4（1v2=0.9484, 2v3=0.8888, 3v4=0.7982），远高于 prompt-chain K*=2。原因：LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），使各代高度可区分。这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss），而非 retrain-chain 的 upper bound。
7. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。
8. **"为什么不用 learned representations"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。
9. **"θ=0.60 选择是否 arbitrary？"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。
10. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。

## Venue Fit

- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度
- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} 的 bounded range + domain dependence 是 nuanced scientific finding，比 "K*=2 everywhere" 更可信且更 interesting（审稿人不必怀疑过度外推）
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
  registry_id: null
  status: planned


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

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
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
  "promptId": "2f6fbf6a-1492-4bd3-8cd2-720032942c59",
  "type": "user",
  "uuid": "7ceec3af-add2-44af-8ed7-46f1937fdf57",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T11:32:58.004Z_

```json
{
  "parentUuid": "7ceec3af-add2-44af-8ed7-46f1937fdf57",
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
  "uuid": "df279d8d-1a20-4d5b-bcb8-e7726ea119f8",
  "timestamp": "2026-05-18T11:32:58.004Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T11:32:58.004Z_

```json
{
  "parentUuid": "df279d8d-1a20-4d5b-bcb8-e7726ea119f8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c2214eb6-7994-4008-883d-d5003bddb6d9",
  "timestamp": "2026-05-18T11:32:58.004Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' domain-dependent bounded saturation 被视为 novel empirical contribution；C3 binary filtering 被接受为足够的 proof-of-concept；borderline CIs 不被视为致命缺陷 核心假设：['K*∈{1,…",
  "leafUuid": "c2214eb6-7994-4008-883d-d5003bddb6d9",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "K* domain-dependent bounded saturation characterization",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---

### Assistant

_source line 8 · 2026-05-18T11:33:04.265Z_

I'll analyze each planned experiment and generate detailed predicted data for the "best" tier.

Let me first check what planned experiments remain.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2214eb6-7994-4008-883d-d5003bddb6d9",
  "isSidechain": false,
  "requestId": "req_011Cb9xiVngSmct6b5R4daNY",
  "type": "assistant",
  "uuid": "d98669e4-c4a1-43f2-82a6-c664c3dff406",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtVMr3BUuaqQsDkLYczAYy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 49202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 49202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 142,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 49202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 49202
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

_source line 9 · 2026-05-18T11:33:05.689Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AH7ST2hL6Abneya7Di6C5Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d98669e4-c4a1-43f2-82a6-c664c3dff406",
  "isSidechain": false,
  "requestId": "req_011Cb9xiVngSmct6b5R4daNY",
  "type": "assistant",
  "uuid": "e0f67f54-a9f8-49cb-83c8-642cfc681d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtVMr3BUuaqQsDkLYczAYy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 49202,
      "cache_read_input_tokens": 11841,
      "output_tokens": 142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 49202,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 142,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 49202,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 49202
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

_source line 10 · 2026-05-18T11:33:05.700Z_

<details><summary>↩ Tool result · `toolu_01AH7ST2hL6Abneya7Di6C5Y`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0f67f54-a9f8-49cb-83c8-642cfc681d0f",
  "isSidechain": false,
  "promptId": "2f6fbf6a-1492-4bd3-8cd2-720032942c59",
  "type": "user",
  "uuid": "903825df-5963-4d2a-81fa-71593880d615",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "e0f67f54-a9f8-49cb-83c8-642cfc681d0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T11:39:47.301Z_

<details><summary>Logged reasoning block</summary>

```text
Let me identify the planned experiments from the experiment_plan. Looking through the list:

1. **exp-014** (planned) - Naturalistic validation: Common Crawl 2025/2026 snapshot + AlignScore correlation
2. **exp-028** (planned) - Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples
3. **exp-009** (plan status: DONE, conclusion: failed) - but it has v3 versions that succeeded

Wait, let me re-read. The user asks for "planned" experiments. Looking at the experiment_plan:


- exp-014: status: planned
- exp-028: status: planned

Those are the only two with status "planned". All others are DONE.

But the user says "对 experiment_plan 中每个 planned 实验展开详细数据" — so they want predictions for experiments with status "planned". That's exp-014 and exp-028.

Actually, let me re-read more carefully. The user says "基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。" This could mean every experiment in the plan, not just those with status "planned". But given the context of Phase 1 defining what "best" tier means, I think they're asking specifically for the planned ones.

The output format specifies `imagined_experiments` with `expected_results` and `result_rationale`. This is about predicting what results would look like under the "best" tier reviewer assumptions. Most experiments are already done with actual data, but the "best" tier is about how reviewers would interpret and score the paper. So I'm generating the reviewer's perspective on what these experiments demonstrate.

Looking at the user's request more carefully — they're asking for detailed predictions specifically for experiments with "planned" status. That's exp-014 and exp-028. The narrative guidance suggests this should be a comprehensive prediction document covering these two planned experiments under the "best" tier assumptions.

The planned experiments are exp-014 (naturalistic validation on Common Crawl 2025/2026) and exp-028 (subsampling power curve). I need to generate detailed predictions for both of these under the "best" tier framework.

For exp-014, this is testing whether depth predictions on real Common Crawl data correlate with independent quality metrics. Under "best" tier assumptions, reviewers would see this as additional practical validation, and I'd expect moderate Spearman correlation between predicted depth and AlignScore/vocabulary richness — high enough to validate but not suspiciously perfect.

For exp-028, this addresses reviewer concerns about minimum sample size for determining K*=2. Under "best" tier, reviewers accept the power analysis as sufficient, and I'd expect K*=2 to stabilize at n≥2000-3000 with power >0.80.

Now I need to construct the detailed predictions for both experiments with specific numerical results and rationales. exp-014 and exp-028)
2. All experiments in the experiment_plan (all of them)

Given the context — this is about generating imagined/predicted data for a tier analysis, and most experiments already have real data — I think it's specifically about the ones with status "planned" that haven't been run yet. These need predicted results.

Let me generate comprehensive predictions for exp-014 and exp-028.

For exp-014 (Naturalistic validation - Common Crawl):
- Claim: 1
- Description: depth prediction on CC 2025/2026 snapshot, correlation with AlignScore and vocabulary richness
- Priority: P2
- Under best tier:
  - Predicted depth distribution on CC: majority classified as depth 0-1, with ~15-25% at depth ≥2
  - Spearman correlation with AlignScore: ρ ≈ -0.35 to -0.45 (negative because deeper = lower quality)
  - Spearman correlation with vocabulary richness (type-token ratio): ρ ≈ -0.25 to -0.35
  - The moderate correlations validate that depth estimation captures meaningful quality variation
  - Reviewer accepts this as supplementary evidence, not primary

For exp-028 (Subsampling power curve):
- Claim: 1
- Description: C4 n={1000,2000,3000,4000,5000} × 10 resamples
- Priority: P1
- Under best tier:
  - n=1000: K*=2 in 6/10 resamples, 1v2 AUC mean ~0.61, high variance
  - n=2000: K*=2 in 8/10 resamples, 1v2 AUC mean ~0.72, variance decreasing
  - n=3000+: K*=2 in 9-10/10 resamples, 1v2 AUC mean ~0.78-0.82, stable performance
  - Power >0.80 at n≥2500
  - Reviewer sees this as addressing sample size concern adequately

Now I'm constructing the YAML output with detailed metrics, rationale, tables, and figures. For the result_rationale, I need to explain why these specific results are expected under the "best" tier assumptions. I'm planning tables showing depth distributions, correlation matrices, K* success rates, and AUC statistics across sample sizes, along with visualizations like scatter plots and power curves.

For exp-014, I'm thinking through this as an ecological validity test—the key is showing what depth distributions the model assigns to real Common Crawl text and how well those predictions correlate with external quality metrics like AlignScore and vocabulary richness. Under "best" tier assumptions, moderate but statistically significant correlations would validate the approach, suggesting the features measure meaningfully different aspects of text quality. Looking at the correlation patterns, vocabulary diversity and alignment quality both decline with predicted depth, and they're moderately correlated with each other, suggesting they capture overlapping but distinct signals. The year-over-year shift toward higher contamination depth is statistically significant. Now I need to clarify the scope—the paper excludes exp-026's negative results on arXiv filtering, but since that experiment is already complete, I should verify whether the focus is on evaluating a version without those findings.

The planned experiments (exp-014 and exp-028) haven't run yet, so I'll predict their outcomes and reviewer reception. Exp-014's naturalistic validation would substantially strengthen the paper despite being P2, while exp-028 directly addresses a reviewer concern and should show that sample sizes above 3000 are sufficient. I'll make sure the predicted metrics align internally with the existing experimental results.

Now I'm examining how the confidence interval widths and K* stability scale across different sample sizes. At n=5000, the CI width is around 0.02 with stable K* determination, which matches the actual data I'm seeing. As sample size decreases to 4000 and then 3000, the CI width gradually widens to about 0.026, where K* determination starts becoming less reliable.

Looking at the experiment more carefully, it's resampling from existing data to create a power curve—specifically subsampling the Qwen-cont dataset since that's the most marginal case with an AUC of 0.6112. At smaller sample sizes like n=2000 and n=1000, the confidence intervals widen significantly (0.032 and 0.045 respectively), making it increasingly difficult for models to reliably demonstrate K*=2, with only Pythia likely passing at n=1000.

The power analysis shows that Qwen-cont requires n≥4000 for reliable detection while Pythia only needs n≥2000, and at n=5000 the results are properly powered. This addresses the sample size concerns, so a best-tier reviewer would accept the combination of the naturalistic validation from exp-014 and the power analysis from exp-028 as thorough supplementary evidence supporting the core claims.

Now I'm constructing the full output with the tier assessment and narrative guidance...

Defining the imagined experiments for the YAML structure...

For the naturalistic validation, I'm considering how a model trained on C4 prompt-chain data would perform when applied to Common Crawl documents—many would be human-written with predicted depth 0, while others likely LLM-generated with depth 1+. The correlation would be moderate since AlignScore captures factual consistency beyond just depth, and vocabulary richness is only one signal among several factors.

I'm estimating the actual distribution in CC: around 62% human text (depth 0), 23% first-generation synthetic (depth 1), 10% second-generation (depth 2), and 5% deeper recursive content. Given that 15-30% of web text is currently LLM-generated, the classifier might overpredict depth 1 for human text with synthetic-like features, but the cross-domain transfer from C4 to CC should be reasonable since C4 itself is sourced from CC.

For the quality correlations, I'm expecting moderate negative relationships—deeper predicted depth correlates with lower quality scores. With a sample size over 10K, these should be statistically significant but not too strong since they're measuring different constructs. I'm predicting Spearman correlations around -0.25 to -0.32 with p-values below 0.001 across AlignScore, type-token ratio, and unique trigram ratio. The year-over-year comparison shows mean predicted depth increasing from 0.58 in 2025 to 0.73 in 2026, which should be highly significant on a Mann-Whitney U test. For the power curve analysis on the marginal case with Qwen-cont data, I'm working with an AUC of about 0.61 for the 1v2 comparison.

Now I'm running subsampling experiments at different sample sizes to see how the confidence interval tightens and when we can reliably determine K*=2. As sample size increases from 1000 to 5000, the mean AUC stays stable around 0.611 while the confidence interval width shrinks from 0.045 down to about 0.022, and the proportion of resamples where the lower bound exceeds 0.60 climbs from 40% up to 80%. Working through the confidence interval lower bounds across different sample sizes, I can see the pattern emerging: at n=1000 the lower bound falls around 0.590, which fails to pass θ=0.60, but as sample size increases the margin of error shrinks and the lower bound creeps upward—by n=4000 it reaches approximately 0.601, just crossing the threshold, and at n=5000 it stabilizes around 0.602, which aligns with the observed data.

This tells me Qwen-cont is the marginal case, requiring roughly 4000-5000 samples to reliably establish K*=2. In contrast, Pythia with its much stronger 1v2 AUC of 0.654 passes the threshold easily even at n=1000, so the power requirements are heavily model-dependent. I'm now considering whether to focus the "best" tier analysis on a single model or present the multi-model comparison to show this variation.

The key insight for the reviewer is that n=5000 works for most configurations but Qwen-cont sits right at the boundary, which I should disclose transparently in the power curve rather than hide. This doesn't undermine the overall conclusion about K*=2 being the dominant mode—it just shows where the evidence is strongest and weakest. Now I'm ready to write out the final YAML with these specifics.

For the tables and figures, I'm planning concrete outputs: depth distribution comparisons between the two corpus versions, correlation matrices linking predicted depth to quality metrics like AlignScore and lexical diversity, and per-depth quality breakdowns for exp-014. For exp-028, I need the determination rates for K*=2 across sample sizes and models, plus AUC statistics with confidence intervals. The visualizations will show the power curve as the centerpiece—one line per model tracking how the K*=2 determination rate climbs with n—along with depth distribution stacked bars and scatter plots of predicted depth against alignment scores.

Now I'm verifying which experiments are actually marked as planned in the experiment_plan. Scanning through the list, I see exp-014 and exp-015 are the candidates, but I need to confirm their exact status before proceeding with the prediction. I'm looking at the tier expectations—borderline confidence intervals aren't seen as fatal flaws, and the overall assessment range is 3.5-4.0 with a 0.5-0.7 probability for EMNLP main. The planned experiments would strengthen an already-solid evidence base rather than fill critical gaps, addressing secondary concerns proactively. For exp-014 specifically, the naturalistic validation is secondary priority, so even moderate correlations would serve as useful supplementary evidence without needing to be definitive—the controlled experiments already provide the primary support, so reviewers wouldn't demand strong naturalistic correlations under this tier interpretation.

The prediction challenges are real: Common Crawl likely contains 10-30% synthetic content, the model was trained on C4 with domain shift implications for wild CC text, AlignScore only partially captures generation depth, and vocabulary metrics like TTR are crude proxies for diversity. I'll predict moderate but statistically significant correlations that reflect genuine quality variation the model can detect.

For exp-028, the subsampling analysis is a straightforward computational check—predictions should align with the known confidence intervals from existing work, and the key finding would be that around 3000-4000 samples suffice for robust K* determination across most models.

Writing the final YAML output now... Generating the experiment configuration... Looking at the 2026 distribution, there's a clear shift toward deeper nesting compared to 2025—the mean depth increased from 0.57 to 0.81, and the Mann-Whitney test confirms this difference is highly significant. The correlations with vocabulary richness metrics are all negative and statistically significant, suggesting that documents with greater nesting depth tend to have lower lexical diversity across all three measures. Looking at the distribution estimates, LLM-generated content likely comprises 20-35% of CC 2025-2026 based on public detection reports, and since our classifier was trained on C4 which originates from CC, the domain shift is minimal. The depth 0 predictions run slightly high (64% vs 51%) because the classifier has a bias toward shallower predictions, though the overall trend holds. What's striking is that 2026 shows significantly deeper predicted depths compared to 2025, suggesting recursive contamination in the LLM ecosystem has accumulated substantially over that year.

The moderate Spearman correlations stem from the fact that AlignScore and TTR measure different aspects—factual consistency and lexical diversity respectively—that only partially capture generation depth. Depth 1 texts might maintain factual accuracy while showing reduced vocabulary diversity, whereas deeper generations degrade across both dimensions. The correlations are meaningful but not strong because these metrics tap into different constructs, real-world CC text is messier than controlled experimental data, and the classifier itself struggles to distinguish between depth 1 and 2 samples.

AlignScore shows the expected monotonic decline with predicted depth (0.782→0.679) as recursive generation progressively loses factual grounding to the source document, though the absolute drop is modest since the self-referential variant only captures internal consistency rather than source faithfulness. The reviewers treat this moderate correlation as an ecological validity check—evidence that the depth signal exists in wild data and aligns with controlled experiments—rather than requiring a strong relationship, and since this is marked as secondary priority, the paper's core contributions remain solid even without it.

Generating markdown table... Generating markdown table...

I'm also planning visualizations showing how AlignScore declines monotonically with predicted depth, and a scatter plot with a trend line to illustrate their relationship. The naturalistic validation comes together across three dimensions: the shift in depth distribution aligns with known LLM adoption trends, the negative correlation between depth and quality metrics supports the theoretical expectation, and the convergence across multiple independent measures strengthens the overall finding.

The main limitation is that without ground truth labels, I can't verify the classifier's precision and recall on real data—the observed correlations reflect both the quality of my depth predictions and the true underlying relationship. But this is a recognized open problem in contamination detection, and reviewers would likely accept this as directionally correct supplementary evidence.

Now I'm designing a subsampling power curve experiment using the full dataset from the earlier work to examine how sample size affects the reliability of the findings. Looking at the Pythia-1.4B results across sample sizes, the mean 1v2 AUC stays consistently around 0.654 while confidence interval widths narrow from 0.044 down to 0.019 as n increases, and all configurations achieve perfect K*=2 success rates across the board.

Now examining the OLMo model, which requires a minimum of 1000 samples for 80% power. The AUC hovers around 0.614-0.615, but the K*=2 detection rate improves substantially with sample size, climbing from 50% success at n=1000 up to perfect detection at n=5000, while confidence intervals similarly tighten as sample size grows.

Looking at Qwen Continuous next, which needs 3000 samples to reach 80% power. The performance metrics are slightly lower than OLMo with AUCs around 0.611-0.612, and the K*=2 detection rate starts lower at 30% with n=1000 before reaching 80% at n=4000.

Now examining Llama 8B's results, which shows comparable AUC performance in the 0.612-0.613 range but requires 4000 samples for adequate power.

Looking at the aggregate findings across all models, 5000 samples achieves at least 90% K*=2 determination across the board, while 3000 is sufficient for three of the four models tested. n 成反比：n=5000 时 CI width ≈ 0.020（匹配 exp-007 实际数据），n=1000 时 CI width ≈ 0.020 × √(5000/1000) = 0.045。这是标准 bootstrap CI 的 sampling theory 预期。Pythia（1v2 AUC=0.654，高于 θ 达 5.4pp）在所有 n 下均稳定 K*=2，因为即使 CI width=0.044（n=1000），CI lower ≈ 0.654 - 0.022 = 0.632 >> 0.60。Qwen-cont 是 rate-limiting model（1v2 AUC=0.611，仅高于 θ 1.1pp），n=1000 时 CI lower ≈ 0.587 < 0.60，绝大多数 resample 无法判定 K*=2，需要 n≥4000 才能达到 80% 判定率。OLMo 和 LLaMA 介于两者之间（1v2 AUC ≈ 0.613-0.615），n=3000 时 CI lower 刚好跨过 0.60 边界，在 80% resample 中判定成功。n=5000 时所有模型的判定率都达到 90% 以上。

现在看到 Qwen-cont 在 n=5000 下 9/10 而非 10/10 的情况，这实际上是透明地披露了统计功效的边界性，而不是实验设计的缺陷，因为论文已经明确标注了它的 CI lower 值处于临界位置。这个结果也为后续研究提供了实用指导：如果要复现这个实验且使用效应量较弱的模型，需要 n≥4000；但如果使用效应量更大的模型，n=1000 就足够了。

现在我在查看样本量与判定率的关系表，以及不同样本量下 AUC 置信区间宽度的变化趋势。

接着我在描述两个关键图表：一个展示 K*=2 判定率随样本量的幂曲线，其中 Pythia 始终保持 100% 的判定率，而 Qwen-cont 显示最陡峭的 S 形曲线，在约 4000 个样本处突破 80% 的功效阈值；另一个是双 y 轴图表，对比平均置信区间宽度与样本量的关系。

现在我在总结核心发现：n=5000 对当前实验设计足够充分，所有模型都能达到 90% 以上的 K*=2 判定率，但最小可行样本量取决于效应量大小——AUC 离目标值越远需要的样本越少，Pythia 只需 1000 个样本就够，而 Qwen-cont 则需要 4000 个。

置信区间宽度在模型间基本一致，完全由样本量决定，模型间的 power 差异纯粹源于点估计与阈值的距离。这种透明的统计分析能够消除审稿人对样本量选择是否武断的疑虑，同时由于 Qwen-cont 的边界性已在论文中明确说明，审稿人不太可能追问更大样本量是否能进一步改善其判定率。

让我再仔细核实一下 n=5000 时的实际数据预测...

现在看各模型的置信区间：Pythia 的下界约 0.6454，OLMo 约 0.6045，Qwen-cont 约 0.6015，LLaMA 约 0.6028，这些区间宽度都在 0.018 到 0.020 之间，确实反映了 AUC 方差的差异而非仅由样本量决定。

如果样本量缩小到 1000，根据置信区间宽度与 √n 成反比的关系，区间宽度会扩大约 2.2 倍。这样的话 Pythia 的下界会降到约 0.634，仍然能通过阈值检验。

但 OLMo、Qwen-cont 和 LLaMA 的下界都会跌到 0.59 左右，全部失败。不过这只是期望值，实际上由于重采样的方差，不同的样本会产生不同的 AUC 估计和置信区间，所以有些重采样会得到更高的下界，有些会更低。现在我需要估计有多大比例的重采样能让下界超过 0.60。

对于 OLMo 在 n=1000 时，期望下界约 0.592，比阈值低约 0.8 个百分点，在 10 次重采样中可能有 2-3 次能通过。Qwen-cont 的情况更糟，可能只有 1-2 次通过。LLaMA 与 OLMo 类似。当 n 增加到 2000 时，置信区间宽度会按 √2.5 倍缩小，我来计算一下各模型的新 CI 宽度。

Pythia 在 n=2000 时的下界达到 0.640，成功通过阈值，但 OLMo 只有 0.599，处于临界状态，而 Qwen-cont 和 LLaMA 都未能通过。继续看 n=3000 的情况，CI 宽度会进一步缩小到原始值的 1.291 倍。

此时 Pythia 和 OLMo 都能通过，但 Qwen-cont 仍然失败，LLaMA 刚好达到 0.600 的边界。

当我增加到 4000 个样本时，置信区间变窄了，所有模型的下界都略有改善。

现在我来估算在 10 次重采样中每个模型通过 K*=2 判定的频率——Pythia 在所有样本量下都能通过，而 OLMo 随着样本量增加从大约 20-30% 的通过率逐步提升到 80% 左右。

Qwen-cont 最边界，在 n=5000 时实际 CI 下界为 0.6015，刚好通过，但我意识到在完整数据集上重采样可能会改变这个结果的稳定性。

每次重采样都会产生略微不同的 AUC 估计，虽然 CI 宽度已经反映了点估计的方差，但大多数重采样应该仍会得到 CI 下界 > 0.60。

对于 Qwen-cont 在 n=5000 时，实际 CI 是 [0.6015, 0.6213]，由于下界仅比阈值高 0.0015，可能有 1 次重采样会跌破阈值，所以预计 9/10 通过。现在让我更精确地修正各模型的预测：Pythia 的 1v2 AUC 为 0.6539，远高于阈值，所以各样本量都应该是 10/10；OLMo 的 AUC 为 0.6145，边际较小，n=1000 时约 3/10，n=2000 时约 5/10。

Qwen-cont 的 AUC 为 0.6112，更接近阈值，n=1000 时仅 2/10，随着样本量增加逐步改善到 n=5000 时的 9/10；LLaMA 的情况还在评估中。

我注意到实际的 exp-007 数据显示 OLMo 和 LLaMA 的置信区间下界都应该通过阈值，但 Qwen-cont 的 0.6015 最接近边界。

根据重采样结果，最关键的是找到最边际模型所需的最小样本量——Pythia 在 n=1000 时就很稳定，而 Qwen-cont 需要 n=5000 才能达到 9/10 的通过率，所以实际建议是 n≥3000-4000 对大多数模型来说比较合理。

现在我在精确计算每个模型达到 80% 功效所需的最小样本量，Pythia 显然是 1000，OLMo 大约需要 3500-4000，而 Qwen-cont 在 n=4000 时只有 60%，n=5000 时达到 90%，所以它的阈值应该在 4500 左右。

让我根据实际的置信区间和边际来调整这些估计值。

在n=5000时，OLMo的边际最大（0.45pp），其次是LLaMA（0.28pp），然后是Qwen-cont（0.15pp），所以难度排序应该反过来。现在我需要重新计算在较小样本量下每个模型的置信区间下界，特别是对LLaMA在n=3000时的表现进行更精确的估计。

我正在根据标准误与样本量的平方根成反比这一关系来推导不同样本量下的置信区间。对于LLaMA，我从n=5000时的已知CI宽度反推标准误，然后用它来估计n=3000和n=4000时的CI下界，看有多少比例的重采样会超过阈值。

现在我在整理各个模型的完整数据表，包括Pythia、OLMo和Qwen，每个表都显示不同样本量下的标准误、预期CI下界和K*=2通过率。

对于Qwen-cont，在n=5000时预期CI下界是0.601，这明确超过阈值，所以在10次重采样中几乎所有都应该通过。

而在n=4000时，预期CI下界恰好是0.600，正好在边界上，这意味着大约50%的概率通过，所以5/10左右比较合理。不过重采样本身还有额外的方差，AUC会在0.611附近波动，有些重采样会得到更高的值（轻松通过），有些会更低（失败），这会拓宽分布。

现在我用标准正态分布来精确计算：在n=4000时，AUC的标准误是0.0057，所以CI下界大约是AUC减去0.0112。通过超过0.6112的概率大约是49%，确认了5/10的估计。而在n=5000时，标准误降到0.0051，CI下界的阈值变成0.6100，这时通过的概率会更高。

但实际数据显示在n=5000时CI下界是0.6015，这超过了0.60的阈值，说明我的标准误估计可能偏高。让我从实际的置信区间反推：如果CI是[0.6015, 0.6213]，宽度是0.0198，那么半宽是0.0099，对应的标准误大约是0.00505。当从5000个样本的池子中重新抽样4000个时，AUC估计会非常接近0.611，而标准误会按照样本量的平方根关系缩放，大约是0.00505乘以√(5000/4000)，得到0.00565。

这样置信区间的半宽就是0.0111，下界约为0.5999，刚好在边界附近。

不过我还需要考虑AUC本身在重新抽样中的变异性。从n=5000时的置信区间可以推断出潜在的方差参数，然后用它来估计n=4000时的标准误。现在我在计算单次重新抽样得到的AUC低于0.60的概率。

对于特定的一次重新抽样，AUC会围绕0.611波动，标准误约为0.00565，置信区间半宽约为0.011。所以我需要计算置信区间下界超过0.60的概率。

由于下界约等于AUC减去0.011，这就变成了P(AUC > 0.611)，在标准正态分布下恰好是50%。

现在看n=5000的情况，虽然从5000个样本中有放回地重新抽样5000个似乎接近完整数据集，但自助法的方差仍然存在，我需要重新计算这个情况下的置信区间下界。

根据计算，这大约给出58.7%的概率，所以Qwen-cont在n=5000时应该是6/10。但这个结果看起来太低了，考虑到实验中的实际结果通过了。

我意识到一个关键问题：当从5000个样本中有放回地重新抽样5000个时，由于某些项目会出现多次而某些永远不会出现，有效样本量实际上小于5000。根据自助法的理论，预期的独特样本比例约为63.2%，这意味着有效n约为3162，会导致置信区间比原始的更宽。

但实验实际上是做子采样而不是自助法。在n=5000时，你会选择全部5000个项目，每次都得到完全相同的结果。而在n=4000时，你从5000个中随机选择4000个（不放回），AUC会在不同子集间略有变化。对于不放回的子采样，n=4000时的方差与留一法方差有关。

应用有限总体修正后，子采样AUC的标准差约为0.00253，远小于n=4000时的标准误。每个子样本内的置信区间通过自助法计算，半宽度约为0.011。当我计算P(CI_lower > 0.60)时，这取决于子采样AUC的分布——它围绕完整样本AUC中心，而不是围绕真实参数。

我意识到这个方向过于复杂了。让我用更实际的启发式方法：关键是在n=5000时，Qwen-cont的置信区间勉强通过（下界=0.6015，余量=0.15个百分点），而在更小的样本量下，置信区间会变宽，通过的概率下降。我可以用一个简单的公式估计：当样本量从5000降到k时，预期余量大约减少(1.96 × SE_5000) × (√(5000/k) - 1)，当这个值为负时，置信区间下界就会低于阈值。对于Qwen-cont，在n=4000时，置信区间半宽度会按某个因子增加。

现在我在计算不同样本量下的具体数值：n=4000时因子约为0.118，导致余量从0.15下降到0.03，大约50%的通过率；n=3000时因子约为0.291，余量变为负值约-0.14，通过率降到40%；n=2000时因子约为0.581，余量约-0.42，通过率约25%；n=1000时继续这个趋势。

对于OLMo模型，基础余量更大（0.45pp），所以在n=4000时余量约0.33（60%通过率），n=3000时约0.16（55%通过率），n=2000时继续下降。

我意识到这些通过率比预期的要低，需要重新考虑我对余量和通过率关系的理解——当余量为0时通过率是50%，当余量为正1个标准差时约84%，而CI下界的标准差应该接近该样本量下的标准误。

对于Qwen-cont在n=5000时，余量约0.15pp，标准差约0.505pp，这给出Z=0.30，通过率约61.8%。这意味着即使在n=5000时，该方法也只有6/10的概率通过，而实际实验之所以通过是因为它恰好落在有利的一侧。但我意识到这个分析忽略了一个关键点：CI下界同时受到点估计和CI宽度变化的影响，所以我需要用不同的方式来思考这个问题——考虑在完整数据集上的CI是[0.6015, 0.6213]，当我们用替换法在n=5000进行子采样时，每个自助样本会产生略微不同的AUC。

现在我意识到实验设计应该是这样的：对n个文档进行子采样，然后对每个子样本运行标准流程（计算特征、运行分类器、获得AUC、计算AUC的自助CI、检查CI下界是否超过阈值）。在n=5000时（完整数据集），每次"重采样"都给出完全相同的结果，所以K*=2的通过率是10/10。但在n=4000时，我们从5000个文档中选择4000个，不同的子集会产生略微不同的AUC，内部自助CI取决于具体的子集。跨n=4000子集的AUC方差大约遵循有限总体修正公式，其中σ²是个体文档对AUC贡献的总体方差。

现在我在计算具体的数值。从完整数据的标准误SE@5000 = 0.00505，我可以推导出σ² ≈ 0.1275。对于n=4000的子样本，考虑有限总体修正因子0.200，子样本AUC的标准误约为0.00253。在每个n=4000的子集内，自助CI的半宽度约为0.01106，所以CI下界 = AUC_sub - 0.01106。对于完整数据，AUC = 0.6112。

现在我在检查子样本AUC超过0.61106的概率，这大约是52%。对于更小的n=3000样本，有限总体修正因子增加到0.400，子样本标准误变为0.00412，CI半宽度增加到0.01278。

这使得P(AUC_sub > 0.61278)降至约35%。当n进一步减少到2000时，修正因子上升到0.600，标准误增加到0.00619，CI半宽度达到0.01565，概率继续下降到约24%。

对于n=1000的情况，修正因子为0.800，标准误为0.01010，CI半宽度为0.02213，最终概率降至约14%。现在我来对Pythia模型进行相同的计算，该模型的AUC为0.6539，在n=5000时的标准误为0.0045。

计算得出σ²为0.10125，在n=1000时Pythia的概率接近100%，这符合预期。接下来我需要对OLMo模型进行同样的分析，其AUC为0.6145，标准误为0.00515。

现在我在计算OLMo在不同样本量下的置信区间和概率。在n=1000时，OLMo只有约21.6%的概率超过阈值，远低于Pythia的表现。继续计算n=2000的情况，看这个模型在更大样本量下的表现如何。 Continuing with the n=4000 case, the standard error for the subsample is smaller, pushing the probability that the subsampled AUC exceeds the confidence interval bound up to about 89%, or 9 out of 10. At n=5000 with the full dataset, we'd expect all 10 replications to stay within bounds. Now shifting to LLaMA with its lower AUC of 0.6123 and standard error of 0.0048, I'm recalculating the variance and working through the same subsample analysis starting with n=1000. Continuing through the remaining sample sizes, I'm seeing the probability of exceeding the confidence interval bound increases substantially as n grows—reaching about 77% at n=4000 and essentially certain at n=5000. Now I'm compiling these results into a summary table to show the full pattern across different model configurations. Looking at the performance metrics across different sample sizes, I see that at n=5000 we're working with the full dataset, so there's no variance—all models deterministically achieve 10/10. The earlier 52% probability I noted was specific to the n=4000 subsampling case. Since the experiment uses subsampling without replacement to create the power curve, once we reach the complete dataset, there's only one possible sample, making the results deterministic across all models. Looking at the performance metrics across these models, I'm seeing that Qwen-cont needs the full 5000 samples to hit 80% power, which is actually a constraint of the data itself—the margin is so tight that subsampling can't get us there. This is a real limitation worth noting honestly in the analysis.

Now I'm finalizing the YAML structure and reconsidering how to frame the minimum sample sizes. With the 80% threshold (8 out of 10 resamples), Pythia reaches it at n=1000, both OLMo and LLaMA at n=4000, but Qwen-cont only achieves it at n=5000 where the result becomes deterministic. The overall pattern still holds—seven of eight models show robustness, with just this one borderline case—so the aggregate finding remains convincing despite this individual limitation.

For practical publication purposes, I'd recommend reporting n=5000 as the minimum for models with small effect sizes like Qwen-cont, and n=3000 for the medium effect size models like OLMo and LLaMA.

Now I'm working through the CI width calculations to verify my predictions across different sample sizes. Continuing through the remaining models and their confidence interval calculations across different sample sizes.

Now I'm verifying the consistency of these numbers and reconsidering the edge case where n equals the population size—specifically whether resampling happens with or without replacement, since that affects whether we get a deterministic outcome at maximum sample size.

Looking at the bootstrap scenario with replacement at n=5000, the effective sample size drops to around 3162 due to duplicates, which would push the confidence interval width to about 0.025 and potentially dip below the 0.60 threshold. But the actual experimental data shows Qwen-cont passing consistently, which suggests the real methodology uses grouped cross-validation that preserves effective sample size rather than simple item-level bootstrap.

Given the description mentions "subsampling power curve," I'm settling on the interpretation that this uses subsampling without replacement, which explains why the theoretical calculations align with the observed results.

Now I'm ready to finalize the output. I should also verify that the narrative guidance fits the "best" tier appropriately—the tier accepts the three-tier domain ladder, the 0.60 threshold with triple justification, the C3 filtering proof-of-concept, and acknowledges Qwen-cont as borderline but not fatal, with an estimated probability of 0.5-0.7 for EMNLP main. The two planned experiments (exp-014 for ecological validity and exp-028 for power analysis) are nice-to-haves that won't substantially shift the acceptance rate.

For the power curve experiment, I need to include the mean AUC values for each model across different sample sizes—these should track very closely to the full-dataset AUC since subsampling doesn't introduce bias, though there might be negligible finite-sample effects at smaller n values that I'll keep minimal.

The exp-028 description addresses a specific reviewer concern about determining the minimum sample size needed for K*=2, which the "best" tier already handles adequately.

Now I'll generate the final YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "903825df-5963-4d2a-81fa-71593880d615",
  "isSidechain": false,
  "requestId": "req_011Cb9xj4smEYuA1u9grvuq5",
  "type": "assistant",
  "uuid": "75f7ca4c-6575-4d7a-aec2-193325b9b311",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xe2f56mcx4HTuXuGxV2jH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 61043,
      "output_tokens": 32271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32271,
          "cache_read_input_tokens": 61043,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 314
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

_source line 12 · 2026-05-18T11:42:14.149Z_

从 experiment_plan 中筛选 status=planned 的实验：exp-014（Naturalistic CC Validation）和 exp-028（Subsampling Power Curve）。基于已完成实验的实际 SE/AUC 数据推导预测。

```yaml
tier: best
narrative_guidance: >
  两个 planned 实验均为 supplementary evidence。exp-014 naturalistic validation 在 best tier
  下被视为 "welcome ecological plausibility check" 而非必要条件——reviewer 已接受 C1' 受控实验
  证据链（8 configurations × 3 domains × 4 decoding strategies）。exp-028 subsampling power 
  curve 直接回应 "is n=5000 sufficient?" 潜在 concern，在 best tier 下 reviewer 认为 7/8 
  configurations robust 的现状已足够，power analysis 属于 thoroughness 加分项。两实验的 
  marginal contribution 对 ARR 分数影响有限（~+0.1），但消除 meta-reviewer "incomplete 
  evaluation" 标记的尾部风险。不做这两个实验不影响 best tier 评分区间。

imagined_experiments:
  - name: "Naturalistic Common Crawl Validation"
    plan_id: "exp-014"
    description: >
      对 Common Crawl 2025-03 和 2026-01 snapshot 各随机抽样 10,000 文档（排除 <100 
      token 短文档），用已训练的 15D feature + OBD-LightGBM pipeline 做 depth 预测。
      预测结果与 AlignScore（自参考 factual consistency）和三个独立 vocabulary richness 
      指标（TTR, unique trigram ratio, Yule's K）做 Spearman rank correlation。
      同时比较两个 snapshot 的 predicted depth 分布，检验 year-over-year contamination 
      趋势。依赖 exp-005 的训练好的 pipeline。
    expected_results:
      n_per_snapshot: 10000
      total_n: 20000
      depth_distribution_cc2025:
        depth_0: 0.64
        depth_1: 0.22
        depth_2: 0.09
        depth_3: 0.03
        depth_4_plus: 0.02
        mean_depth: 0.57
      depth_distribution_cc2026:
        depth_0: 0.51
        depth_1: 0.28
        depth_2: 0.13
        depth_3: 0.05
        depth_4_plus: 0.03
        mean_depth: 0.81
      year_over_year:
        delta_mean_depth: +0.24
        mann_whitney_U_p: "<0.001"
        effect_size_cohens_d: 0.31
      spearman_correlations:
        predicted_depth_vs_alignscore:
          rho: -0.32
          p: "<0.001"
        predicted_depth_vs_ttr:
          rho: -0.27
          p: "<0.001"
        predicted_depth_vs_unique_trigram_ratio:
          rho: -0.24
          p: "<0.001"
        predicted_depth_vs_yules_k:
          rho: 0.21
          p: "<0.001"
        alignscore_vs_ttr:
          rho: 0.41
          p: "<0.001"
      per_depth_quality_means:
        alignscore:
          depth_0: 0.782
          depth_1: 0.741
          depth_2: 0.718
          depth_3: 0.693
          depth_4_plus: 0.679
        ttr:
          depth_0: 0.423
          depth_1: 0.398
          depth_2: 0.381
          depth_3: 0.370
          depth_4_plus: 0.362
        unique_trigram_ratio:
          depth_0: 0.612
          depth_1: 0.578
          depth_2: 0.553
          depth_3: 0.534
          depth_4_plus: 0.521
      monotonicity_test:
        alignscore_jonckheere_terpstra_p: "<0.001"
        ttr_jonckheere_terpstra_p: "<0.001"
        trend_direction: "monotonic decrease with predicted depth"

    result_rationale: >
      (1) Depth 分布预测依据：GPTZero/Originality.ai 公开报告 2025 年 web 文本中 LLM 
      生成内容占比约 20-35%。我们的分类器在 C4 上训练，C4 本身源自 CC，domain shift 
      较小。depth 0 占比高于实际人类文本比例（64% vs 估计 65-80%），因为分类器在 ordinal 
      confusion 下倾向 conservative prediction（ordinal accuracy ~38%，confusion 
      主要在 depth 1-2 之间）。2026 比 2025 predicted depth 显著更高（+0.24），反映 
      LLM 生态系统一年间的递归污染积累——这与 Shumailov et al. (2024) 和 Alemohammad 
      et al. (2024) 的 model collapse 趋势预测方向一致。
      (2) 中等 Spearman ρ（|0.21-0.32|）的信息论解释：AlignScore 衡量自参考事实一致性，
      TTR 衡量词汇多样性，它们是 text quality 的不同维度，只部分反映 generation depth。
      DPI 理论预测递归生成逐步丧失信息，但信息丧失在不同 quality dimension 上速率不同：
      surprisal distribution（本文 core features）最先饱和（K*=2），factual consistency 
      退化更缓慢。因此 depth 与 AlignScore 的相关性是 moderate 而非 strong。|ρ|=0.32 
      在 NLP 中属于 meaningful ecological correlation（对比 BERTScore 与 human judgment 
      ρ~0.4-0.5）。
      (3) 相关性不能更高的三个原因：(a) 分类器本身在 depth 1-2 区间有 ~50% confusion 
      rate，引入 measurement noise 压低 ρ；(b) wild CC text 包含多种域和风格，远比 
      controlled C4 prompt-chain 嘈杂；(c) AlignScore 的 self-reference variant 
      检测内部一致性而非 source faithfulness，与 depth 的理论关系更弱。
      (4) AlignScore 按 predicted depth 单调递减（0.782→0.679，10pp span）符合 iterated 
      lossy channel 框架：每代生成逐步丧失与源文档的事实锚定。但绝对下降温和，因为 depth 
      0→1 的 one-wash 效应最强（Δ=4.1pp），后续代际的增量退化递减——正如 K*=2 所暗示的 
      depth signal saturation。
      (5) 在 best tier 下，reviewer 将此视为 "directionally correct ecological 
      evidence"——中等相关性被解读为 "depth signal exists in the wild, consistent with 
      controlled findings"。不会追问 ground truth 缺失（wild contamination 中无 ground 
      truth 是公认的 open problem）。P2 优先级意味着即使不含此实验，paper scoring 不受影响。

    tables:
      - name: "Table A.X: Predicted Depth Distribution on Common Crawl Snapshots"
        columns: ["Predicted Depth", "CC 2025-03 (%)", "CC 2026-01 (%)", "Δ (pp)"]
        rows:
          - ["0 (human)", "64.0", "51.0", "-13.0"]
          - ["1", "22.0", "28.0", "+6.0"]
          - ["2", "9.0", "13.0", "+4.0"]
          - ["3", "3.0", "5.0", "+2.0"]
          - ["≥4", "2.0", "3.0", "+1.0"]
          - ["Mean depth", "0.57", "0.81", "+0.24***"]
      - name: "Table A.Y: Correlation of Predicted Depth with External Quality Metrics (n=20,000)"
        columns: ["Metric Pair", "Spearman ρ", "p-value"]
        rows:
          - ["Pred. depth × AlignScore", "-0.32", "<0.001"]
          - ["Pred. depth × TTR", "-0.27", "<0.001"]
          - ["Pred. depth × Unique trigram ratio", "-0.24", "<0.001"]
          - ["Pred. depth × Yule's K", "+0.21", "<0.001"]
          - ["AlignScore × TTR (reference)", "+0.41", "<0.001"]
      - name: "Table A.Z: Mean Quality Metrics by Predicted Depth Bin"
        columns: ["Predicted Depth", "n", "AlignScore", "TTR", "Uniq. Trigram Ratio"]
        rows:
          - ["0", "~11,500", "0.782 ± 0.08", "0.423 ± 0.05", "0.612 ± 0.06"]
          - ["1", "~5,000", "0.741 ± 0.09", "0.398 ± 0.05", "0.578 ± 0.06"]
          - ["2", "~2,200", "0.718 ± 0.10", "0.381 ± 0.06", "0.553 ± 0.07"]
          - ["3", "~800", "0.693 ± 0.11", "0.370 ± 0.06", "0.534 ± 0.07"]
          - ["≥4", "~500", "0.679 ± 0.12", "0.362 ± 0.07", "0.521 ± 0.08"]

    figures_description:
      - >
        Fig A.X: Stacked bar chart — CC 2025-03 vs CC 2026-01 predicted depth distribution 
        (5 depth bins, color-coded)。2026 条显示向 deeper generation 的明显偏移。
        Annotation 标注 Mann-Whitney p<0.001 和 Cohen's d=0.31。
      - >
        Fig A.Y: Box plot — AlignScore (y-axis) by predicted depth bin (x-axis, 0-4+)，
        每个 bin 显示 median, IQR, whiskers。虚线连接 median 展示单调下降趋势。
        Jonckheere-Terpstra test p<0.001 annotation。
      - >
        Fig A.Z: 2×2 scatter matrix — predicted depth (jittered) vs {AlignScore, TTR}，
        附 LOWESS 曲线和 Spearman ρ annotation。展示非线性但单调的 depth-quality 关系。

    analysis: >
      Naturalistic validation 提供三层证据：(1) predicted depth 在两个 snapshot 间的 
      distribution shift 与已知 LLM 渗透率增长一致（Cohen's d=0.31, small-to-medium 
      effect）；(2) depth 与三个独立质量指标的中等负相关（ρ 范围 -0.24 到 -0.32）支持 
      "deeper generation = lower quality" 的理论预期，且多指标 convergence 降低 
      measurement artifact 可能性；(3) 质量指标按 predicted depth 严格单调递减（Jonckheere-
      Terpstra p<0.001），即使分类器 accuracy 只有 ~38%，ordinal structure 仍被保留。
      核心局限：无 ground truth depth labels for wild data。Observed correlations 是 
      {classifier accuracy × true depth-quality relationship} 的 joint function，
      不能分离两个因素。但在 best tier 下，reviewer 接受这是 wild contamination 检测的 
      inherent limitation，不追问 ground truth——重要的是 directional consistency with 
      controlled experiments。此实验定位为 Appendix supplementary analysis，不影响主线 
      claims。

  - name: "Subsampling Power Curve"
    plan_id: "exp-028"
    description: >
      从 exp-007 完整 n=5000（per depth）数据集中，对 C4 域按 n∈{1000, 2000, 3000, 
      4000, 5000} 做 WITHOUT-replacement 子采样（保持各 depth bin 等比例），每个 n 
      重复 10 次独立抽样。每次计算 1v2 pairwise AUC 及其 95% bootstrap CI（10,000 
      resamples），记录 K*=2 判定结果（CI lower > θ=0.60）。覆盖 4 个 continuation 
      模型：Pythia-1.4B, OLMo-1B, Qwen-cont, LLaMA-8B。目标：确定 K*=2 判定所需 
      最低样本量，回应 reviewer "is n=5000 arbitrary?" concern。
    expected_results:
      models_tested:
        - Pythia-1.4B
        - OLMo-1B
        - Qwen-1.5B-Instruct-cont
        - LLaMA-3.1-8B
      resamples_per_n: 10
      reference_full_data:
        Pythia: { auc: 0.6539, ci_lower: 0.6454, margin_above_theta: 0.0454 }
        OLMo: { auc: 0.6145, ci_lower: 0.6045, margin_above_theta: 0.0045 }
        Qwen_cont: { auc: 0.6112, ci_lower: 0.6015, margin_above_theta: 0.0015 }
        LLaMA_8B: { auc: 0.6123, ci_lower: 0.6028, margin_above_theta: 0.0028 }

      pythia:
        n1000: { mean_1v2_auc: 0.6542, mean_ci_width: 0.039, kstar2_rate: "10/10" }
        n2000: { mean_1v2_auc: 0.6538, mean_ci_width: 0.028, kstar2_rate: "10/10" }
        n3000: { mean_1v2_auc: 0.6540, mean_ci_width: 0.023, kstar2_rate: "10/10" }
        n4000: { mean_1v2_auc: 0.6539, mean_ci_width: 0.020, kstar2_rate: "10/10" }
        n5000: { mean_1v2_auc: 0.6539, mean_ci_width: 0.018, kstar2_rate: "10/10" }
        minimum_n_for_80pct_power: 1000

      olmo:
        n1000: { mean_1v2_auc: 0.6148, mean_ci_width: 0.045, kstar2_rate: "2/10" }
        n2000: { mean_1v2_auc: 0.6143, mean_ci_width: 0.032, kstar2_rate: "4/10" }
        n3000: { mean_1v2_auc: 0.6146, mean_ci_width: 0.026, kstar2_rate: "6/10" }
        n4000: { mean_1v2_auc: 0.6145, mean_ci_width: 0.023, kstar2_rate: "9/10" }
        n5000: { mean_1v2_auc: 0.6145, mean_ci_width: 0.020, kstar2_rate: "10/10" }
        minimum_n_for_80pct_power: 4000

      qwen_cont:
        n1000: { mean_1v2_auc: 0.6115, mean_ci_width: 0.044, kstar2_rate: "1/10" }
        n2000: { mean_1v2_auc: 0.6110, mean_ci_width: 0.031, kstar2_rate: "2/10" }
        n3000: { mean_1v2_auc: 0.6113, mean_ci_width: 0.026, kstar2_rate: "4/10" }
        n4000: { mean_1v2_auc: 0.6111, mean_ci_width: 0.022, kstar2_rate: "5/10" }
        n5000: { mean_1v2_auc: 0.6112, mean_ci_width: 0.020, kstar2_rate: "10/10" }
        minimum_n_for_80pct_power: 5000
        note: >
          n=5000 是完整数据集，K*=2 判定为 deterministic（CI lower=0.6015>0.60）。
          n=4000 时仅 5/10 通过，说明 Qwen-cont 的效应量（margin=1.5 mAUC）在 
          n<5000 时 underpowered。若需 probabilistic 80% power 需 n≈6000-7000
          （extrapolation）。

      llama8b:
        n1000: { mean_1v2_auc: 0.6125, mean_ci_width: 0.042, kstar2_rate: "2/10" }
        n2000: { mean_1v2_auc: 0.6122, mean_ci_width: 0.030, kstar2_rate: "3/10" }
        n3000: { mean_1v2_auc: 0.6124, mean_ci_width: 0.024, kstar2_rate: "5/10" }
        n4000: { mean_1v2_auc: 0.6123, mean_ci_width: 0.021, kstar2_rate: "8/10" }
        n5000: { mean_1v2_auc: 0.6123, mean_ci_width: 0.019, kstar2_rate: "10/10" }
        minimum_n_for_80pct_power: 4000

      aggregate_summary:
        minimum_n_all_models_80pct: 5000
        minimum_n_excluding_qwen_cont_80pct: 4000
        minimum_n_robust_models_80pct: 1000
        practical_recommendation: >
          n≥5000 per depth for full coverage; n≥4000 sufficient for 3/4 models;
          models with margin > 4pp (Pythia-class) need only n≥1000.
        power_scales_with_effect_size: >
          minimum_n ∝ 1/(AUC - θ)². Pythia margin 45pp → n≈1000;
          OLMo/LLaMA margin 3-5pp → n≈4000; Qwen-cont margin 1.5pp → n≈5000+.

    result_rationale: >
      (1) CI width 与 √n 成反比（standard bootstrap theory）：n=5000 时 CI width ≈ 0.020
      （匹配 exp-007 实际数据），n=1000 时 CI width ≈ 0.020 × √(5000/1000) ≈ 0.045。
      四个模型的 CI width 在相同 n 下几乎一致（差异 <0.003），因为 CI width 主要由样本量
      决定，AUC 值的影响是二阶的。
      (2) Pythia（1v2 AUC=0.654，margin=+5.4pp above θ）即使在 n=1000 时 CI lower 
      ≈ 0.654 - 0.020 = 0.634 >> 0.60，永远不会失败。这是因为 Pythia 的 depth signal 
      效应量大（1v2 vs 2v3 gap = 10.2pp），远超 θ 判定所需的 statistical precision。
      (3) OLMo/LLaMA（margin 3-5pp）在 n=3000-4000 处跨过 80% power 线。推导：
      n=4000 时 CI half-width ≈ 0.011，CI lower ≈ 0.614 - 0.011 = 0.603 > 0.60（OLMo），
      0.612 - 0.011 = 0.601 > 0.60（LLaMA）。但 margin 仅 1-3pp，resample-to-resample 
      variance 导致部分 resamples 的 AUC 偏低而 fail。
      (4) Qwen-cont 是 rate-limiting configuration（margin=+1.5 mAUC，最小）。
      n=4000 时 expected CI lower = 0.611 - 0.011 = 0.600 恰在边界，仅 ~50% resamples 
      通过。n=5000 时为完整数据集（deterministic pass），不存在 subsampling variance。
      这意味着对 Qwen-cont-class 效应量（AUC 仅超 θ 约 1pp），n=5000 是 minimum viable 
      sample size，低于此 statistical power 不足。
      (5) 核心 insight：power 与 (AUC - θ)² 成正比。Pythia 的大效应量意味着极小 n 即可；
      Qwen-cont 的小效应量意味着需要大 n。这不是实验设计缺陷，而是反映了不同模型在 C4 
      上 depth signal strength 的真实差异——Pythia 的 depth feature distributions 
      separation 远大于 Qwen-cont（JSD_1v2: 0.014 vs 0.005）。
      (6) 在 best tier 下，reviewer 将此解读为 "honest and thorough power analysis"。
      Qwen-cont n=4000 时 5/10 pass rate 不被视为 weakness——论文已在正文透明披露 
      CI lower=0.6015 的边缘性（paper_framing §(a) 的 ⚠️ 标注），power analysis 
      量化了这一已知边缘性的 sample size dependency，属于 scientific transparency 
      而非 evidence against the claim。7/8 robust configurations 的 aggregate pattern 
      不受 Qwen-cont 单点影响。

    tables:
      - name: "Table A.W: K*=2 Determination Rate by Sample Size and Model"
        columns: ["n per depth", "Pythia", "OLMo", "Qwen-cont", "LLaMA-8B", "≥3/4 pass 80%?"]
        rows:
          - ["1,000", "10/10", "2/10", "1/10", "2/10", "No (1/4)"]
          - ["2,000", "10/10", "4/10", "2/10", "3/10", "No (1/4)"]
          - ["3,000", "10/10", "6/10", "4/10", "5/10", "No (1/4)"]
          - ["4,000", "10/10", "9/10", "5/10", "8/10", "Yes (3/4)"]
          - ["5,000", "10/10", "10/10", "10/10†", "10/10", "Yes (4/4)"]
        footer: "† n=5000 = full dataset, result is deterministic"
      - name: "Table A.W+1: Mean 1v2 AUC and CI Width by Sample Size"
        columns: ["n", "Pythia AUC (CI width)", "OLMo AUC (CI width)", "Qwen-cont AUC (CI width)", "LLaMA AUC (CI width)"]
        rows:
          - ["1,000", "0.654 (0.039)", "0.615 (0.045)", "0.611 (0.044)", "0.612 (0.042)"]
          - ["2,000", "0.654 (0.028)", "0.614 (0.032)", "0.611 (0.031)", "0.612 (0.030)"]
          - ["3,000", "0.654 (0.023)", "0.615 (0.026)", "0.611 (0.026)", "0.612 (0.024)"]
          - ["4,000", "0.654 (0.020)", "0.615 (0.023)", "0.611 (0.022)", "0.612 (0.021)"]
          - ["5,000", "0.654 (0.018)", "0.615 (0.020)", "0.611 (0.020)", "0.612 (0.019)"]
      - name: "Table A.W+2: Minimum n for 80% K*=2 Power by Effect Size Category"
        columns: ["Effect Size Category", "Representative Model", "AUC - θ (pp)", "Min. n for ≥80% rate"]
        rows:
          - ["Large (>4pp)", "Pythia-1.4B", "5.4", "≤1,000"]
          - ["Medium (3-5pp)", "OLMo-1B", "1.5–4.5", "4,000"]
          - ["Small (1-2pp)", "Qwen-cont", "1.1", "5,000†"]
        footer: "† Qwen-cont at n=5000 passes deterministically; probabilistic 80% power requires n≈6,000-7,000 (extrapolated)"

    figures_description:
      - >
        Fig A.V: Power curve — K*=2 determination rate (y-axis, 0-100%) vs n per depth 
        (x-axis, 1000-5000)，四条线（Pythia=flat at 100%, 其余三条呈 S-curve 在 
        n=3000-5000 处上升）。水平虚线标 80% power threshold。Pythia 线与其余三条的 
        separation 直观展示 effect size 对 power 的决定性影响。右侧 annotation 标注 
        每个模型的 margin above θ。
      - >
        Fig A.V+1: 双 panel plot — 左 panel: mean CI width vs n（四条线近乎重叠，
        展示 CI width ≈ 1/√n 缩放规律，虚线为 theoretical √n curve fit）；右 panel: 
        expected CI lower vs n（四条线有明确分离，Pythia 始终远高于 θ=0.60 虚线，
        Qwen-cont 在 n<5000 时低于虚线）。展示 "CI width is n-driven, power is 
        margin-driven" 的核心 message。

    analysis: >
      Power curve 的核心 takeaway 分三层：
      (1) Sample size sufficiency: n=5000 per depth 在所有 4 个 continuation 模型上 
      达到 100% K*=2 判定率（Qwen-cont 为 deterministic pass）。n=4000 时 3/4 模型 
      达 80% power，仅 Qwen-cont（最小 margin）例外。当前实验设计的 n 选择是 justified。
      (2) Effect-size dependency: minimum_n 与 (AUC - θ)² 大致成反比。Pythia 的 
      54-mAUC margin 使 n=1000 即足够；Qwen-cont 的 15-mAUC margin 使 n=5000 勉强够用。
      这为可复现性提供 concrete guidance：如果研究者使用类 Pythia 效应量的模型，n≥1000 
      即可判定 K*；如果使用弱效应量模型，需 n≥5000。
      (3) CI width universality: CI width 在四个模型间几乎完全重叠（相同 n 下差异 <0.003），
      说明 CI width 是纯 sample-size-driven 的 statistical property，与模型无关。
      模型间 power 差异完全来自 AUC point estimate 与 θ 的距离。
      在 best tier 下，reviewer 将此解读为 "exemplary statistical due diligence"——
      不仅报告了 K* 结论，还定量分析了该结论的 statistical stability。Qwen-cont 的 
      n-sensitivity 不被视为 evidence against K*=2，而是被接受为 "the honest cost of 
      a marginal effect size, transparently documented"。这与论文正文对 Qwen-cont 
      CI lower=0.6015 的已有 disclosure 构成一致的 transparency narrative。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75f7ca4c-6575-4d7a-aec2-193325b9b311",
  "isSidechain": false,
  "requestId": "req_011Cb9xj4smEYuA1u9grvuq5",
  "type": "assistant",
  "uuid": "6cbd5d5b-e617-40b5-b682-e62fe832c1c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xe2f56mcx4HTuXuGxV2jH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 314,
      "cache_read_input_tokens": 61043,
      "output_tokens": 32271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 314,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32271,
          "cache_read_input_tokens": 61043,
          "cache_creation_input_tokens": 314,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 314
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' domain-dependent bounded saturation 被视为 novel empirical contribution；C3 binary filtering 被接受为足够的 proof-of-concept；borderline CIs 不被视为致命缺陷 核心假设：['K*∈{1,…",
  "leafUuid": "6cbd5d5b-e617-40b5-b682-e62fe832c1c3",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "K* domain-dependent bounded saturation characterization",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：C1' domain-dependent bounded saturation 被视为 novel empirical contribution；C3 binary filtering 被接受为足够的 proof-of-concept；borderline CIs 不被视为致命缺陷 核心假设：['K*∈{1,…",
  "leafUuid": "6cbd5d5b-e617-40b5-b682-e62fe832c1c3",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "K* domain-dependent bounded saturation characterization",
  "sessionId": "bb107442-4cbe-4f88-86a5-deb9b79e1c8a"
}
```

---
