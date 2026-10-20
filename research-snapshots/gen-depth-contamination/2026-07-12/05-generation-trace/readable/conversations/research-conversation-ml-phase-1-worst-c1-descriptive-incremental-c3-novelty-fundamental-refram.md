# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：C1' 被视为 descriptive/incremental；C3 被有效拒绝；整体 novelty 不足，需 fundamental refram

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/1018244b-9021-454b-a72d-f8ef9a2cd81b.jsonl`
- **Structured JSON:** [`c5c8a986e3e7745b27dd.json`](../../sessions/c5/c5c8a986e3e7745b27dd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T11:45:22.541Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T11:45:22.541Z",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：C1' 被视为 descriptive/incremental；C3 被有效拒绝；整体 novelty 不足，需 fundamental reframe 才能在同级 venue 发表\n核心假设：[\"K*∈{1,2,3} 被 dismiss 为 trivially expected——'DPI says saturation is rapid, you confirmed it is rapid, so what?'\", 'θ=0.60 被攻击为 arbitrary：θ 选择几乎 deterministic 地决定 K* 值，整个 characterization 是 θ-contingent artifact', 'C3 完全被拒：effect sizes negligible，Pythia replication null，reviewer 怀疑 arXiv filtering 结果被 selectively omitted', '至少一位 reviewer 指出 missing cross-domain filtering experiments 和 exp-025 null 之间的矛盾——质疑 selective reporting', \"'feature engineering + LightGBM' 没有 methodological novelty，定性为 'measurement study with weak measurements'\", '多个 borderline CIs (Qwen-cont 0.6015, LLaMA fold-0 0.5969, 512tok 0.5979) 被视为 systematic insufficient power', 'Prompt-chain 实验设计不被认可为 ecologically valid despite retrain-chain comparison']\n关键指标范围：{'arr_overall': [2.0, 2.5], 'arr_soundness': [2.5, 3.0], 'arr_excitement': [1.5, 2.5], 'arr_clarity': [3.0, 4.0], 'meta_recommendation': 'reject', 'prob_emnlp_main': [0.0, 0.08], 'prob_emnlp_findings': [0.08, 0.25]}\n叙事方向：核心 reframe（不降级 venue 目标）：(1) 完全放弃 C3 作为独立 claim——降为 appendix case study；(2) 叙事从 'K* characterization + practical curation' 转为 'information-theoretic analysis of recursive generation degradation'——DPI framework 作为理论贡献，domain dependence 作为核心实证发现；(3) 主可视化从 K* 表格改为 AUC-decay curve，展示 generation depth 上的连续信号衰减而非离散 K* 断点——消解 θ-dependency 批评；(4) 单一 headline: 'structured text resists recursive information collapse — a domain complexity explanation'——domain dependence 是证据链最强、最难攻击的部分；(5) 补 exp-028 power analysis 和 naturalistic validation (exp-014) 填补 empirical gaps；(6) 如 ARR May 25 来不及修改，转投 AAAI 2027 (abstract Jul 25) 争取修改时间。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\nfocus: 不包含 exp_026 arXiv graduated filtering 的负向结果。论文 Section 5 维持当前写法（仅含 C4 filtering + Pythia replication），不加 arXiv filtering 数据。评估这种版本的审稿得分。\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, updated D049/D050)\n\n### Primary: C1' (K* Characterization — Domain-Dependent Bounded Saturation)\n首次系统测量递归合成文本的 generational discrimination boundary K*，demonstrating that K* is low-bounded (≤3) and domain-dependent。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains（C4, Wikipedia, arXiv）、4 decoding strategies 系统表征 K*_empirical 的行为，发现：\n\n- **K*∈{1,2,3} at θ=0.60**：K* 是有界的且域依赖的，呈现三级域阶梯：Wikipedia(1) < C4(2) < arXiv(3)\n- **Web text K*=2 是 dominant mode**（7/8 configurations），展现跨模型架构、跨解码策略的一致性\n- **Structured academic text (arXiv) K*=3**，经五个模型配置、四个架构族 cross-validate（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B; 5/5 domain-competent models, 100%）\n- **Wikipedia K*=1 (scorer-controlled)**：全部 6 个模型在 cross-family scorer 控制后均 K*=1。Qwen 生成器在 same-family scorer 下的 K*=2 是 scorer family bias artifact（D060 确认），正文报告 scorer-controlled 值，Appendix 披露 confound 细节\n- **Mistral-7B K*=1 on C4 but K*=3 on arXiv**：domain-specific one-wash，最强 domain dependence 证据\n- **Domain 是 K* 的唯一主导因素**：scorer control 后，model scale/architecture/decoding strategy 均不改变域内 K* 一致性\n- **One-wash laundering effect**：对 web text 和 Wikipedia，单次生成即令文本与更深层合成内容不可区分\n\n**子组件：**\n\n**(a) K*=2 as dominant mode for web text (7/8 configurations)**\n> **7/8 model configurations yield K*=2 on C4 web text：**\n>\n> | Model | Experiment | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|-----------|---------|--------|-----------------|\n> | Qwen-1.5B-Instruct rewrite | mvp-001 | 0.6957 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B cont | exp-001 | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | Qwen-1.5B base cont | exp-016 | 0.6262 | [0.6168, 0.6353] | ✅ (+1.7pp) |\n> | Qwen2.5-7B cont | exp-004 | 0.6178 | [0.6079, 0.6261] | ✅ (+0.79pp) |\n> | OLMo-1B cont | exp-002 | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | LLaMA-3.1-8B cont | exp-018 | 0.6123 | [0.6028, 0.6216] | ✅ (+0.28pp) |\n> | Qwen-1.5B-Instruct cont | exp-017 | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp) |\n>\n> *Exception: Mistral-7B cont (exp-019): 1v2=0.5935, CI [0.5835, 0.6032], K*=1*\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 7/8 configurations 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60\n> - 4 decoding strategies AUC 1v2 range [0.6866, 0.7039], K* 完全不变\n> - ⚠️ Qwen-cont 1v2 CI lower=0.6015 极边缘；cross-scorer validation 下降至 K*=1\n> - ⚠️ θ-sensitivity: θ=0.60 下 7/8 K*=2; θ=0.70 下多数降至 K*=1\n> - Paper 措辞：\"K*=2 emerges as the dominant mode for general web text (7/8 model configurations), demonstrating consistency across diverse architectures and decoding strategies.\"\n\n**(b) Domain dependence: arXiv K*=3 (5-model cross-validated, D055/D056/D057)**\n> - **Qwen-1.5B on arXiv** (exp-024): 2v3 AUC=0.6427, CI [0.6275, 0.6575], K*=3 ✅ (+2.75pp)\n> - **Pythia-1.4B on arXiv** (exp-025): 2v3 AUC=0.6544, CI [0.6401, 0.6688], K*=3 ✅ (+4.01pp)\n> - **LLaMA-3.1-8B on arXiv** (exp_arXiv_llama8b): 2v3 AUC=0.6215, K*=3 ✅ (+2.15pp)\n> - **Mistral-7B on arXiv** (exp_arXiv_mistral7b): 2v3 AUC=0.6275, all folds > 0.60, K*=3 ✅ (+2.75pp)\n> - **Qwen-7B on arXiv** (exp_arXiv_qwen7b): 2v3 AUC=0.6255, all folds > 0.60, K*=3 ✅ (+2.55pp)\n> - 五个模型配置、四个架构族（1.4B-8B）在 arXiv 上 100% 一致 K*=3（5/5 domain-competent models，仅 OLMo capacity failure）\n> - OLMo-1B K*=1 (exp_arXiv_olmo): capacity failure — 生成完全出域文本，不影响 domain property claim，作为 \"domain competence prerequisite\" 分析放 Appendix\n> - **Mistral C4 K*=1 → arXiv K*=3 是 domain dependence 的最强证据**：同一模型在不同域给出不同 K*，证明 K* 由 domain structure 主导而非 model identity\n> - **解释**：arXiv 的结构化特征（LaTeX formatting, citation patterns, mathematical notation）提供额外 depth-distinguishing signal，使辨别力多延伸一代\n> - Sample size: n=2,200 per model\n> - ⚠️ LLaMA fold 0=0.5969 < θ, bootstrap CI lower 可能接近 0.60 边界。论文措辞用 \"K*=3 with boundary pair AUC of 0.62\" 而非 \"robustly K*=3\"\n> - 论文定位：**domain dependence 是核心发现**——K* 由源文本结构复杂度决定，非纯模型属性。4-model cross-validation 大幅强化证据链\n\n**(c) Mistral K*=1 on web text: domain-specific one-wash (D056)**\n> - Mistral-7B 在 C4 web text 上 1v2 AUC CI lower < 0.60, K*=1\n> - Cross-scorer validation (exp-022): 使用其他模型 score Mistral 生成的文本，K*=1 maintained → C4 上的 K*=1 是 text-intrinsic（非 scorer artifact）\n> - **但 Mistral arXiv K*=3 (exp_arXiv_mistral7b) 证明 one-wash 是 domain-specific 而非 model-intrinsic**\n> - **One-wash laundering**：对 web text 这类 homogeneous 域，Mistral 单次生成即令文本在统计上不可区分于更深层合成；但 structured domains (arXiv) 能 rescue even Mistral from one-wash\n> - 论文定位：Mistral C4→arXiv 的 K* 跃变（1→3）是 (model × domain) interaction 的典型案例，进一步证明 domain structure 是 K* 的主要决定因素\n\n**(d) Cross-model transfer (scorer invariance)**\n> - Pythia↔OLMo 90-92% accuracy retention → K* 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - Cross-scorer validation (exp-022): 11/12 generator×scorer combos yield K*=2 → K* governed by generation process, not scoring model\n> - Feature ordering: scorer-invariant Spearman ρ > 0.90\n> - 论文定位：confirms K* is a property of the text/generation process, not the measurement apparatus\n\n**(e) Representation dependence of K* (Neural Probe)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - K*(neural) 是 model-dependent：Qwen K*=3, Pythia/OLMo K*=2\n> - 15D model-free features 给出一致的 K* across all models，neural probe 给出 model-dependent K*\n> - Interpretability-deployability tradeoff: model-free features 的 universality 优势在 cross-model 结果下更明显\n> - 论文定位：validates choice of model-free 15D features for headline characterization\n\n**(f) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection，不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nDomain-appropriate K* correctly predicts optimal curation granularity: for web text (K*=2), binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). Dose-response analysis (exp-009 v3, 3 ratios × 3 strategies × 5 seeds) confirms binary filtering maintains consistent advantage across 10%/30%/50% contamination ratios (HellaSwag significantly better at all levels, p≤0.004), while graduated filtering collapses to no-filter baseline performance. K* serves as an actionable curation guideline: the domain-dependent discrimination boundary directly determines the optimal filtering granularity.\n\n> ⚠️ Defensive framing constraint (D053): MMLU at 30% ratio p=0.074 不显著, 不能 claim \"universally beneficial\"。维持 \"consistent advantage\" 措辞，以 HellaSwag 显著性为主要证据。\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 8 model configurations（5 architecture families, 1B-8B）、3 source domains、4 decoding strategies 系统表征 K*，揭示其 **bounded domain-dependent** 本质：**K*∈{1,2,3}**，形成清晰的三级域阶梯——Wikipedia K*=1（6 models, scorer-controlled），C4 web text K*=2（7/8 configurations），arXiv K*=3（5/5 domain-competent models, 4 architecture families）。Domain 是 K* 的唯一主导因素：scorer confound 控制后，model identity/scale/decoding strategy 均不改变域内一致性。这一发现意味着递归生成信息丧失极快——one to two generation passes suffice to erase distinguishable depth structure（\"one-wash laundering\" effect）。Domain dependence 为数据治理提供 actionable guidance：源文本的结构复杂度决定了 depth-aware filtering 的适用粒度。\n- **Headline result template**: \"Recursive generation has a bounded discrimination boundary at K*∈{1,2,3}, forming a three-level domain hierarchy: Wikipedia saturates at K*=1 (all 6 models, scorer-controlled), web text at K*=2 (7/8 model configurations, 5 architecture families, 1B-8B), and structured academic text extends to K*=3 (cross-validated across 5 models, 4 architecture families). Domain structural complexity is the sole systematic determinant of K*. Cross-model transfer retention of 80-92% and scorer-invariant feature ordering (ρ>0.90) confirm depth features are text-intrinsic. Domain-appropriate K* correctly predicts optimal curation granularity.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"K*∈{1,2,3} 范围太小，结论是否 trivial？\"** → 恰好相反：K* 的低有界性是核心发现。DPI 理论只保证 K* 有限但不给上界；我们首次实证表明 K*≤3（即递归信息丧失极快），且 domain dependence 揭示了结构化文本如何延缓信息退化。One-wash laundering effect 对 data governance 有直接实践意义。\n2. **\"只基于小模型（≤8B），能推广到更大模型吗？\"** → 5 architecture families (1B-8B) 覆盖了当前开源生态的主要架构。DPI 理论保证 K*_theory 对任意规模模型存在。Cross-scorer validation 表明 K* 由生成过程而非评分模型决定。扩展至 13B+/70B+ 是重要 future work。\n3. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ domain-dependent bounded saturation 发现，不是分类器本身。Model-free features 的选择被 cross-model transfer 80-92% 和 scorer invariance 验证为正确设计。\n4. **\"arXiv K*=3 样本量够吗？\"** → 五个模型（Qwen-1.5B, Qwen-7B, Pythia-1.4B, LLaMA-8B, Mistral-7B）跨四个架构族均给出 K*=3，每模型 n=2,200，bootstrap CI 确认统计显著。5/5 domain-competent models 100% 一致性排除 model-specific artifact。\n5. **\"Mistral K*=1 是 outlier 还是 systematic？\"** → Cross-scorer validation 确认是 text-intrinsic（非 scorer artifact）。Mistral 可能因训练数据/alignment 差异导致生成文本在一代后即失去 depth-distinguishing structure。这强化了 domain/model dependence 的核心论点。\n6. **\"Prompt-chain 不代表真实世界递归污染\"** → Prompt-chain 隔离纯文本退化效应（text-intrinsic degradation），是更 generalizable 的实验设计。**exp-008 实证验证**：retrain-chain (Pythia-1.4B LoRA) K*≥4（1v2=0.9484, 2v3=0.8888, 3v4=0.7982），远高于 prompt-chain K*=2。原因：LoRA fine-tune 每代引入累积模型 artifacts（vocabulary narrowing, repetition bias），使各代高度可区分。这些 model-adaptation artifacts 是 setup-specific 的，不泛化到 wild contamination scenarios。因此 prompt-chain K*=2 是 data curation 的 operational boundary（仅反映 text-intrinsic information loss），而非 retrain-chain 的 upper bound。\n7. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013/exp-022 直接反驳**：cross-scorer validation 11/12 combos yield K*=2, Pythia↔OLMo 90-92% accuracy retention。K* governed by generation process, not scoring model。**D060 进一步证实**：Wikipedia 上 Qwen same-family scorer 的 +1 bias 被 Pythia cross-family scorer 消除（K*=2→1），证明 scorer confound 可被检测和控制，且仅影响特定 model-family×domain 组合（不影响 C4 主线结论）。\n8. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：neural probe K* 是 model-dependent（Qwen=3, Pythia/OLMo=2），而 15D model-free features 给出一致的 K* across all models。Model-free 方案的 universality + cross-model transferability 是 practical advantage。\n9. **\"θ=0.60 选择是否 arbitrary？\"** → 三层辩护：(1) Cohen's h≈0.20 small effect size threshold, (2) permutation test 校准, (3) AUC gap 在 boundary 处的 sharp discontinuity（1v2 vs 2v3 gap 大于 θ 选择的 sensitivity range）。θ-sensitivity analysis [0.55, 0.70] 在主文呈现。\n10. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep，binary K*-aware filtering outperforms all tested alternatives。\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with domain-dependent bounded saturation finding，C3 是 practical application，generation mode analysis 增加深度\n- **Domain-dependent bounded saturation narrative** 比 universality 更准确且更有 impact：K*∈{1,2,3} 的 bounded range + domain dependence 是 nuanced scientific finding，比 \"K*=2 everywhere\" 更可信且更 interesting（审稿人不必怀疑过度外推）\n- One-wash laundering effect 是 memorable concept 便于传播\n- 风险：K* range 小（1-3）可能被认为 trivial → 论文须强调 bounded ≤3 本身是 surprising（DPI 不给上界），且 domain dependence 是 actionable（不同域需不同 curation 策略）\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 5K docs, depth\n    0-5, scorer=Qwen2.5-1.5B. 测试 K* 是否随模型规模变化。（实际参数已从原计划 1K/depth 0-3 扩展以匹配其他实验配置）'\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  registry_id: exp_004_7b_crossscale\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: exp_006_graduated_filtering\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: exp_008_retrain_chain_v2\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: '>=4'\n    pairwise_auc:\n      0v1: 0.9847\n      1v2: 0.9484\n      2v3: 0.8888\n      3v4: 0.7982\n    pairwise_jsd:\n      0v1: 0.17\n      1v2: 0.12\n      2v3: 0.064\n      3v4: 0.04\n    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts\n      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic\n      boundary.\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: exp_009_dose_50pct\n  status: DONE\n  conclusion: failed\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: exp_011_llm_zeroshot\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_012_binary_confidence\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features。如果 neural probe 也给 K*=2 → C1'' claim 从 \"our features\n    find K*=2\" 升级为 \"K*=2 is data-intrinsic boundary\"。[D014 升级 P0：Reviewer 评估为最高边际价值实验]'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_015_neural_probe\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_016_base_vs_instruct\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- id: exp-018\n  claim: 1\n  description: 'Cross-family universality: LLaMA-3.1-8B, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 跨模型家族验证 K*。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_018_llama8b_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9225\n      1v2: 0.6123\n      2v3: 0.5274\n      3v4: 0.5138\n      4v5: 0.5097\n    jsd:\n      0v1: 0.077\n      1v2: 0.012\n      2v3: 0.005\n    bootstrap_ci:\n      0v1:\n        auc: 0.9224\n        ci_lower: 0.9174\n        ci_upper: 0.9272\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6123\n        ci_lower: 0.6028\n        ci_upper: 0.6216\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5273\n        ci_lower: 0.5169\n        ci_upper: 0.5378\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5168\n        ci_lower: 0.5062\n        ci_upper: 0.5275\n        perm_p: 0.0037\n      4v5:\n        auc: 0.5159\n        ci_lower: 0.5052\n        ci_upper: 0.5268\n        perm_p: 0.0035\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n- id: exp-019\n  claim: 1\n  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_019_mistral7b_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9843\n      1v2: 0.5935\n      2v3: 0.5402\n      3v4: 0.5232\n      4v5: 0.5181\n    bootstrap_ci_1v2:\n      ci_lower: 0.5835\n      ci_upper: 0.6032\n      p_auc_leq_060: 0.9017\n    jsd:\n      0v1: 0.124194\n      1v2: 0.008051\n      2v3: 0.005047\n      3v4: 0.004516\n      4v5: 0.004109\n    ordinal_mae: 1.2275\n    ordinal_accuracy: 0.3567\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n- id: exp-020\n  claim:\n  - 1\n  - 3\n  description: 'Pythia-1.4B decoding ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2,\n    C4 5K docs, depth 0-5. 跨模型验证解码策略对 K* 的不变性。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: exp_020_pythia_decoding\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy:\n      K_star: 2\n      auc:\n        0v1: 0.9992\n        1v2: 0.8838\n        2v3: 0.5342\n        3v4: 0.5228\n        4v5: 0.5162\n    nuc09:\n      K_star: 2\n      auc:\n        0v1: 0.9948\n        1v2: 0.677\n        2v3: 0.5549\n        3v4: 0.5299\n        4v5: 0.5013\n    t07:\n      K_star: 2\n      auc:\n        0v1: 0.9965\n        1v2: 0.7265\n        2v3: 0.5941\n        3v4: 0.5698\n        4v5: 0.5284\n    t12:\n      K_star: 2\n      auc:\n        0v1: 0.9933\n        1v2: 0.6172\n        2v3: 0.5226\n        3v4: 0.517\n        4v5: 0.5051\n- id: exp-021\n  claim: 1\n  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512\n    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_021_length_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    128tok:\n      K_star: 2\n      1v2_auc: 0.6219\n    256tok:\n      K_star: 2\n      1v2_auc: 0.6282\n    512tok:\n      K_star: 2\n      1v2_auc: 0.6073\n    all_K_star_2: true\n    bootstrap_ci:\n      512tok_1v2:\n        auc: 0.6073\n        ci_lower: 0.5979\n        ci_upper: 0.6166\n        perm_p: 0.0001\n        verdict: BORDERLINE\n- id: exp-022\n  claim:\n  - 1\n  - 2\n  description: '4x4 cross-scorer matrix: 4 generators × 4 scorers, 验证 scorer independence\n    完整性。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-021\n  registry_id: exp_022_cross_scorer_matrix\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 12\n    completed: 12\n    K_star_distribution:\n      K2: 11\n      K1: 1\n    matrix:\n      pythia_greedy×olmo:\n        K_star: 2\n        1v2: 0.8811\n      pythia_greedy×pythia:\n        K_star: 2\n        1v2: 0.8838\n      pythia_greedy×qwen_base:\n        K_star: 2\n        1v2: 0.8814\n      pythia_greedy×qwen_instruct:\n        K_star: 2\n        1v2: 0.8818\n      qwen_base×olmo:\n        K_star: 2\n        1v2: 0.6047\n      qwen_base×pythia:\n        K_star: 2\n        1v2: 0.617\n      qwen_base×qwen_base:\n        K_star: 2\n        1v2: 0.6262\n      qwen_base×qwen_instruct:\n        K_star: 2\n        1v2: 0.6273\n      qwen_cont256×olmo:\n        K_star: 2\n        1v2: 0.6028\n      qwen_cont256×pythia:\n        K_star: 1\n        1v2: 0.5979\n      qwen_cont256×qwen_base:\n        K_star: 2\n        1v2: 0.6282\n      qwen_cont256×qwen_instruct:\n        K_star: 2\n        1v2: 0.6072\n    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:\n      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to\n      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'\n- id: exp-023\n  claim:\n  - 1\n  description: 'Domain ablation: Wikipedia seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 验证 K*=2 是否跨数据域一致（C4\n    vs Wikipedia）。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_023_domain_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    1v2_auc: 0.6193\n    2v3_auc: 0.5498\n    all_folds_above_060: true\n    top_feature: freq_entropy\n    ordinal_accuracy: 0.377\n- id: exp-024\n  claim:\n  - 1\n  description: 'Domain ablation: arXiv abstracts seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 第三域验证—— 技术文本与\n    web text (C4) / 百科 (Wikipedia) 分布差异大，三域一致则 domain 维度从 Limitation 升级为 evidence。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_024_arxiv_domain\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    pairwise_auc:\n      0v1: 0.9946\n      1v2: 0.858\n      2v3: 0.6427\n      3v4: 0.5437\n      4v5: 0.5294\n    bootstrap_ci:\n      0v1:\n        auc: 0.9946\n        ci_lower: 0.9929\n        ci_upper: 0.9961\n        perm_p: 0.0001\n      1v2:\n        auc: 0.858\n        ci_lower: 0.848\n        ci_upper: 0.8679\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6427\n        ci_lower: 0.6275\n        ci_upper: 0.6575\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5437\n        ci_lower: 0.5276\n        ci_upper: 0.5598\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5294\n        ci_lower: 0.5133\n        ci_upper: 0.5455\n        perm_p: 0.0006\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First\n      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\n- id: exp-025\n  claim: 3\n  description: 'Pythia-1.4B filtering replication: LoRA rank=8 continued pretraining\n    on C4 depth chain, 3 strategies (binary/graduated/no-filter) × 3 seeds, MMLU+HellaSwag.\n    验证 filtering strategy ordering 跨模型一致性。'\n  priority: P1\n  gpu_budget_hours: 16\n  deps:\n  - exp-006\n  - exp-001\n  registry_id: exp_025_pythia_filtering\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 9/9\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    mmlu:\n      no_filter: 0.2568±0.0012\n      binary_ours: 0.2585±0.0004\n      graduated_a09: 0.2561±0.0009\n    hellaswag:\n      no_filter: 0.5250±0.0008\n      binary_ours: 0.5251±0.0001\n      graduated_a09: 0.5253±0.0007\n    delta_vs_no_filter:\n      binary_ours_mmlu: '+0.0017'\n      binary_ours_hellaswag: '+0.0000'\n      graduated_a09_mmlu: '-0.0007'\n      graduated_a09_hellaswag: '+0.0003'\n    key_finding: All three filtering strategies produce nearly identical results on\n      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering\n      binary>graduated>no_filter NOT confirmed.\n- id: exp-026\n  claim: 3\n  description: 'arXiv graduated vs binary filtering: Qwen2.5-1.5B base + LoRA rank=4,\n    arXiv depth chain (K*=3), 3 strategies (no_filter/binary/graduated α=0.9^d) ×\n    5 seeds, MMLU+HellaSwag. 关键实验：K*=3 域上 graduated 应超越 binary，展示 K*-aware filtering\n    增量价值。'\n  priority: P0\n  gpu_budget_hours: 24\n  deps:\n  - exp-006\n  - exp-024\n  registry_id: exp_026_arxiv_filtering\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 15/15\n    strategies:\n    - no_filter\n    - binary\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    mmlu:\n      no_filter: 0.5899±0.0008\n      binary: 0.5876±0.0004\n      graduated_a09: 0.5900±0.0011\n    hellaswag:\n      no_filter: 0.6600±0.0002\n      binary: 0.6642±0.0004\n      graduated_a09: 0.6599±0.0003\n    delta_vs_no_filter:\n      binary_mmlu: '-0.0023'\n      binary_hellaswag: '+0.0042'\n      graduated_mmlu: '+0.0001'\n      graduated_hellaswag: '-0.0001'\n    key_finding: All three strategies produce nearly identical results. Graduated\n      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU\n      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\n- id: exp-027\n  claim: 1\n  description: 'LaTeX markup removal ablation: 去除 arXiv 文本中的 LaTeX 格式标记后重新提取 15D features，验证\n    K*=3 是否依赖格式特征而非内容层 depth signal。排除替代假说。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-024\n  registry_id: exp_027_latex_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    k_star_preserved: true\n    pairwise_auc_original:\n      0v1: 0.9948\n      1v2: 0.8581\n      2v3: 0.6436\n      3v4: 0.544\n      4v5: 0.5299\n    pairwise_auc_stripped:\n      0v1: 0.9948\n      1v2: 0.8297\n      2v3: 0.6229\n      3v4: 0.5468\n      4v5: 0.5476\n    auc_delta:\n      0v1: 0\n      1v2: -0.028\n      2v3: -0.021\n      3v4: 0.003\n      4v5: 0.018\n    latex_reduction_by_depth:\n      depth_0: 0.6%\n      depth_5: 4.4%\n    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still\n      >θ=0.60). LaTeX format is NOT a confound.\n- id: exp-028\n  claim: 1\n  description: 'Subsampling power curve: C4 n={1000,2000,3000,4000,5000} × 10 resamples,\n    确定 K*=2 判定所需最低样本量。回应 m4 reviewer concern。'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-007\n  registry_id: null\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- exp_id: exp_011_llm_zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- exp_id: exp_015_neural_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- exp_id: exp_006_graduated_filtering\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- exp_id: exp_004_7b_crossscale\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- exp_id: exp_A_alt_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9923\n      auc_1v2: 0.7012\n      auc_2v3: 0.587\n      mae: 1.006\n      accuracy: 0.417\n      spearman_rho_vs_baseline: 0.906\n    pythia_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.99\n      auc_1v2: 0.5923\n      auc_2v3: null\n      mae: 1.216\n      accuracy: 0.371\n      spearman_rho_vs_baseline: 0.942\n    olmo_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9918\n      auc_1v2: 0.6947\n      auc_2v3: null\n      mae: 1.016\n      accuracy: 0.413\n      spearman_rho_vs_baseline: 0.92\n    olmo_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.989\n      auc_1v2: 0.5858\n      auc_2v3: null\n      mae: 1.229\n      accuracy: 0.368\n      spearman_rho_vs_baseline: 0.902\n    key_finding: 'K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1\n      (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer\n      independence of feature ranking.'\n- exp_id: exp_B_14d_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    result: K*=2 stable across all 4 models after removing self_BLEU (14D)\n    key_finding: self_BLEU removal does not change K* boundary. FR-3 resolved.\n- exp_id: exp_C_permutation_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    resamples: 10000\n    all_boundary_pairs_p: <0.0001\n    key_finding: 10K permutation confirms all boundary p-values well below 0.01. FR-11\n      resolved.\n- exp_id: exp_D_obd_n500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    obd_accuracy_final: 0.38\n    obd_ci:\n    - 0.34\n    - 0.422\n    mcnemar_vs_gpt55_p: 0.0809\n    mcnemar_vs_claude_p: 0.0693\n    mcnemar_significant: false\n    multi_seed_std: 0\n    per_depth:\n      d0: 0.96\n      d1: 0.39\n      d2: 0.14\n      d3: 0.19\n      d4: 0.22\n    prob_merge_accuracy: 0.444\n    prob_merge_d4_bias: 0.8\n    note: v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant\n      — supports discussion.tex narrative\n- exp_id: exp_E_paired_stats\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_significant_pairs: 8/15\n    hellaswag_significant_pairs: 9/15\n    binary_ours_vs_all_mmlu: all significant\n    max_cohen_d_mmlu: 10.8\n    max_cohen_d_hellaswag: 8.98\n    graduated_a09_vs_dsir_corrected_p: 0.0523\n    cohen_d_method: d_av (Lakens 2013)\n    key_finding: 'binary-ours significantly outperforms all alternatives on MMLU.\n      On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni\n      cummax bug fixed: MMLU 10/15→8/15. Cohen''s d changed to d_av.'\n    bugfix_note: Holm-Bonferroni cummax variable was never updated, causing 2 MMLU\n      pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal\n      vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\n- exp_id: exp_012_binary_confidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- exp_id: exp_kstar_theta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    output_files:\n    - kstar_theta_curve.pdf (32KB)\n    - kstar_theta_curve.png (335KB)\n    models:\n    - Qwen-rewrite\n    - Pythia\n    - OLMo\n    - Qwen-cont\n    depth_pairs: 5\n    key_finding: All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5.\n      θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical\n      resolved.\n- exp_id: exp_016_base_vs_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- exp_id: exp_018_llama8b_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9225\n      1v2: 0.6123\n      2v3: 0.5274\n      3v4: 0.5138\n      4v5: 0.5097\n    jsd:\n      0v1: 0.077\n      1v2: 0.012\n      2v3: 0.005\n    bootstrap_ci:\n      0v1:\n        auc: 0.9224\n        ci_lower: 0.9174\n        ci_upper: 0.9272\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6123\n        ci_lower: 0.6028\n        ci_upper: 0.6216\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5273\n        ci_lower: 0.5169\n        ci_upper: 0.5378\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5168\n        ci_lower: 0.5062\n        ci_upper: 0.5275\n        perm_p: 0.0037\n      4v5:\n        auc: 0.5159\n        ci_lower: 0.5052\n        ci_upper: 0.5268\n        perm_p: 0.0035\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n- exp_id: exp_019_mistral7b_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9843\n      1v2: 0.5935\n      2v3: 0.5402\n      3v4: 0.5232\n      4v5: 0.5181\n    bootstrap_ci_1v2:\n      ci_lower: 0.5835\n      ci_upper: 0.6032\n      p_auc_leq_060: 0.9017\n    jsd:\n      0v1: 0.124194\n      1v2: 0.008051\n      2v3: 0.005047\n      3v4: 0.004516\n      4v5: 0.004109\n    ordinal_mae: 1.2275\n    ordinal_accuracy: 0.3567\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n- exp_id: exp_020_pythia_decoding\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    greedy:\n      K_star: 2\n      auc:\n        0v1: 0.9992\n        1v2: 0.8838\n        2v3: 0.5342\n        3v4: 0.5228\n        4v5: 0.5162\n    nuc09:\n      K_star: 2\n      auc:\n        0v1: 0.9948\n        1v2: 0.677\n        2v3: 0.5549\n        3v4: 0.5299\n        4v5: 0.5013\n    t07:\n      K_star: 2\n      auc:\n        0v1: 0.9965\n        1v2: 0.7265\n        2v3: 0.5941\n        3v4: 0.5698\n        4v5: 0.5284\n    t12:\n      K_star: 2\n      auc:\n        0v1: 0.9933\n        1v2: 0.6172\n        2v3: 0.5226\n        3v4: 0.517\n        4v5: 0.5051\n- exp_id: exp_021_length_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    128tok:\n      K_star: 2\n      1v2_auc: 0.6219\n    256tok:\n      K_star: 2\n      1v2_auc: 0.6282\n    512tok:\n      K_star: 2\n      1v2_auc: 0.6073\n    all_K_star_2: true\n    bootstrap_ci:\n      512tok_1v2:\n        auc: 0.6073\n        ci_lower: 0.5979\n        ci_upper: 0.6166\n        perm_p: 0.0001\n        verdict: BORDERLINE\n- exp_id: exp_022_cross_scorer_matrix\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_combos: 12\n    completed: 12\n    K_star_distribution:\n      K2: 11\n      K1: 1\n    matrix:\n      pythia_greedy×olmo:\n        K_star: 2\n        1v2: 0.8811\n      pythia_greedy×pythia:\n        K_star: 2\n        1v2: 0.8838\n      pythia_greedy×qwen_base:\n        K_star: 2\n        1v2: 0.8814\n      pythia_greedy×qwen_instruct:\n        K_star: 2\n        1v2: 0.8818\n      qwen_base×olmo:\n        K_star: 2\n        1v2: 0.6047\n      qwen_base×pythia:\n        K_star: 2\n        1v2: 0.617\n      qwen_base×qwen_base:\n        K_star: 2\n        1v2: 0.6262\n      qwen_base×qwen_instruct:\n        K_star: 2\n        1v2: 0.6273\n      qwen_cont256×olmo:\n        K_star: 2\n        1v2: 0.6028\n      qwen_cont256×pythia:\n        K_star: 1\n        1v2: 0.5979\n      qwen_cont256×qwen_base:\n        K_star: 2\n        1v2: 0.6282\n      qwen_cont256×qwen_instruct:\n        K_star: 2\n        1v2: 0.6072\n    key_finding: 'Scorer independence confirmed: K*=2 in 11/12 combos. Only exception:\n      qwen_cont256×pythia (1v2=0.5979, borderline). Pythia-greedy 1v2~0.88 due to\n      repetition collapse. Scorer choice Δ1v2 < 0.025 within each generator.'\n- exp_id: exp_019b_mistral_cross_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 1\n    pairwise_auc:\n      0v1: 0.9209\n      1v2: 0.5695\n      2v3: 0.5335\n      3v4: 0.514\n      4v5: 0.5184\n    bootstrap_ci:\n      0v1:\n        mean: 0.9209\n        ci_lower: 0.9189\n        ci_upper: 0.9229\n        pass_060: true\n      1v2:\n        mean: 0.5696\n        ci_lower: 0.5645\n        ci_upper: 0.5746\n        pass_060: false\n      2v3:\n        mean: 0.5335\n        ci_lower: 0.5283\n        ci_upper: 0.5382\n        pass_060: false\n      3v4:\n        mean: 0.514\n        ci_lower: 0.5063\n        ci_upper: 0.5213\n        pass_060: false\n      4v5:\n        mean: 0.5183\n        ci_lower: 0.5128\n        ci_upper: 0.5244\n        pass_060: false\n    jsd:\n      0v1: 0.08355\n      1v2: 0.007642\n      2v3: 0.004752\n      3v4: 0.004255\n      4v5: 0.003758\n    ordinal_mae: 1.3737\n    ordinal_accuracy: 0.3179\n    top3_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_d1_mean\n    key_finding: Cross-scorer (Qwen-1.5B scoring Mistral text) confirms K*=1. 1v2\n      AUC=0.5695 (self-scorer was 0.5935) — cross-scorer LOWER, not higher. Mistral\n      K*=1 is genuine (inherent to Mistral generations), NOT a self-scorer artifact.\n- exp_id: exp_023_domain_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    1v2_auc: 0.6193\n    2v3_auc: 0.5498\n    all_folds_above_060: true\n    top_feature: freq_entropy\n    ordinal_accuracy: 0.377\n- exp_id: exp_024_arxiv_domain\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    pairwise_auc:\n      0v1: 0.9946\n      1v2: 0.858\n      2v3: 0.6427\n      3v4: 0.5437\n      4v5: 0.5294\n    bootstrap_ci:\n      0v1:\n        auc: 0.9946\n        ci_lower: 0.9929\n        ci_upper: 0.9961\n        perm_p: 0.0001\n      1v2:\n        auc: 0.858\n        ci_lower: 0.848\n        ci_upper: 0.8679\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6427\n        ci_lower: 0.6275\n        ci_upper: 0.6575\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5437\n        ci_lower: 0.5276\n        ci_upper: 0.5598\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5294\n        ci_lower: 0.5133\n        ci_upper: 0.5455\n        perm_p: 0.0006\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > θ=0.60. First\n      condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69).\n- exp_id: exp_025_pythia_arxiv\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.9877\n      1v2: 0.8047\n      2v3: 0.6545\n      3v4: 0.5507\n      4v5: 0.5287\n    pairwise_jsd:\n      0v1: 0.171338\n      1v2: 0.057344\n      2v3: 0.019524\n      3v4: 0.009917\n      4v5: 0.008846\n    bootstrap_ci:\n      0v1:\n        auc: 0.9876\n        ci_lower: 0.9851\n        ci_upper: 0.99\n        perm_p: 0.0001\n      1v2:\n        auc: 0.8047\n        ci_lower: 0.7934\n        ci_upper: 0.8162\n        perm_p: 0.0001\n      2v3:\n        auc: 0.6544\n        ci_lower: 0.6401\n        ci_upper: 0.6688\n        perm_p: 0.0001\n      3v4:\n        auc: 0.55\n        ci_lower: 0.534\n        ci_upper: 0.5657\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5284\n        ci_lower: 0.5122\n        ci_upper: 0.5443\n        perm_p: 0.001\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    n_samples: 2200\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_mean\n    - surp_d1_skew\n    - surp_d1_mean\n    ordinal:\n      MAE: 0.8518\n      Accuracy: 0.4545\n    key_finding: Pythia-1.4B on arXiv yields K*=3, identical to exp-024 (Qwen on arXiv).\n      2v3 CI lower=0.6401 > θ=0.60. Domain saturation depth is model-invariant for\n      arXiv.\n- exp_id: exp_008_retrain_chain\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: exp-008-retrain-chain\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_008_retrain_chain_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: '>=4'\n    pairwise_auc:\n      0v1: 0.9847\n      1v2: 0.9484\n      2v3: 0.8888\n      3v4: 0.7982\n    pairwise_jsd:\n      0v1: 0.17\n      1v2: 0.12\n      2v3: 0.064\n      3v4: 0.04\n    key_finding: Retrain-chain K*>=4, all pairs AUC>>0.60. LoRA adaptation artifacts\n      make generations highly distinguishable. Prompt-chain K*=2 is text-intrinsic\n      boundary.\n- exp_id: exp_009_dose_response\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 45\n    seeds: 5\n    ratios:\n    - 0.1\n    - 0.3\n    - 0.5\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated\n    cross_ratio_finding: 'Binary filtering consistently best across all ratios. Graduated\n      filtering = no_filter at every ratio. Effect size of binary advantage increases\n      with contamination ratio (HellaSwag delta: 10%=+0.38pp, 30%=+0.61pp, 50%=+0.51pp).\n      Original C3 hypothesis (graduated > binary) rejected.'\n    gpu_hours_total: 9.9\n- exp_id: exp_009_dose_10pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_30pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_50pct\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_10pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_30pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_50pct_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_009_dose_10pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6058±0.0002\n        hellaswag: 0.6689±0.0007\n      binary_ours:\n        mmlu: 0.6079±0.0005\n        hellaswag: 0.6727±0.0008\n      graduated:\n        mmlu: 0.6066±0.0011\n        hellaswag: 0.6700±0.0015\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0021\n        p_mmlu: 0.001\n        delta_hellaswag: 0.0038\n        p_hellaswag: 0.0017\n      graduated_vs_binary:\n        delta_mmlu: -0.0014\n        p_mmlu: 0.0917\n        delta_hellaswag: -0.0027\n        p_hellaswag: 0.0399\n      graduated_vs_nofilter:\n        delta_mmlu: 0.0008\n        p_mmlu: 0.2706\n        delta_hellaswag: 0.0011\n        p_hellaswag: 0.0611\n    key_finding: Binary best. Graduated ≈ no_filter.\n- exp_id: exp_009_dose_30pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6069±0.0007\n        hellaswag: 0.6664±0.0020\n      binary_ours:\n        mmlu: 0.6082±0.0012\n        hellaswag: 0.6725±0.0007\n      graduated:\n        mmlu: 0.6072±0.0008\n        hellaswag: 0.6665±0.0014\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0013\n        p_mmlu: 0.0739\n        delta_hellaswag: 0.0061\n        p_hellaswag: 0.0036\n      graduated_vs_binary:\n        delta_mmlu: -0.001\n        p_mmlu: 0.3018\n        delta_hellaswag: -0.006\n        p_hellaswag: 0.0009\n      graduated_vs_nofilter:\n        delta_mmlu: 0.0003\n        p_mmlu: 0.6638\n        delta_hellaswag: 0.0002\n        p_hellaswag: 0.6646\n    key_finding: Binary best on HellaSwag (p=0.004). Graduated = no_filter.\n- exp_id: exp_009_dose_50pct_v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds: 5\n    strategies: 3\n    total_runs: 15\n    mean_std:\n      no_filter:\n        mmlu: 0.6063±0.0013\n        hellaswag: 0.6680±0.0005\n      binary_ours:\n        mmlu: 0.6088±0.0011\n        hellaswag: 0.6731±0.0004\n      graduated:\n        mmlu: 0.6062±0.0009\n        hellaswag: 0.6679±0.0002\n    paired_ttest:\n      binary_vs_nofilter:\n        delta_mmlu: 0.0025\n        p_mmlu: 0.0377\n        delta_hellaswag: 0.0051\n        p_hellaswag: 2.0e-05\n      graduated_vs_binary:\n        delta_mmlu: -0.0026\n        p_mmlu: 0.0257\n        delta_hellaswag: -0.0052\n        p_hellaswag: 3.0e-05\n      graduated_vs_nofilter:\n        delta_mmlu: -0.0001\n        p_mmlu: 0.89\n        delta_hellaswag: -0.0001\n        p_hellaswag: 0.706\n    key_finding: Binary significantly best (HellaSwag p<0.001). Graduated = no_filter\n      exactly.\n- exp_id: exp_026_feature_stability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_016_qwen_base (prompt-chain, K*=2)\n    results:\n      15D:\n        num_tested: 1\n        num_kstar_2: 1\n        min_1v2_auc: 0.6262\n        mean_1v2_auc: 0.6262\n      10D:\n        num_tested: 5\n        num_kstar_2: 5\n        min_1v2_auc: 0.6153\n        mean_1v2_auc: 0.6191\n      8D:\n        num_tested: 5\n        num_kstar_2: 5\n        min_1v2_auc: 0.6056\n        mean_1v2_auc: 0.6159\n      5D:\n        num_tested: 5\n        num_kstar_2: 2\n        min_1v2_auc: 0.5856\n        mean_1v2_auc: 0.5998\n      3D_top3:\n        num_tested: 1\n        num_kstar_2: 0\n        min_1v2_auc: 0.5871\n        mean_1v2_auc: 0.5871\n    all_above_theta: false\n    key_finding: 'Feature selection MATTERS at K*=2 boundary. 15D/10D/8D all robust\n      (min 1v2 AUC > 0.60). 5D random subsets: only 2/5 pass θ=0.60 (min=0.5856).\n      Top-3 features alone (0.5871) fail θ. Contrast with retrain-chain (K*=4) where\n      all subsets trivially passed (min=0.8314).'\n    previous_run_note: v1 used retrain-chain data (K*=4), where all subsets trivially\n      passed with min 1v2 AUC=0.8314. v2 uses prompt-chain data (K*=2) to test boundary\n      robustness.\n- exp_id: exp_027_retrain_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    bootstrap_iterations: 10000\n    pairs:\n      0v1:\n        auc_point: 0.9847\n        ci_lower: 0.9828\n        ci_upper: 0.9864\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      1v2:\n        auc_point: 0.9482\n        ci_lower: 0.9443\n        ci_upper: 0.952\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      2v3:\n        auc_point: 0.8885\n        ci_lower: 0.8829\n        ci_upper: 0.894\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n      3v4:\n        auc_point: 0.7977\n        ci_lower: 0.7903\n        ci_upper: 0.8051\n        perm_p: 0.0001\n        ci_lower_gt_theta: true\n    key_finding: All 4 retrain-chain pairwise AUCs have CI_lower >> theta=0.60 (min\n      CI_lower=0.7903). K*>=4 statistically confirmed with p<0.001.\n- exp_id: exp_027\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    kstar_ci: 4\n    0v1_auc: 0.9847\n    0v1_ci:\n    - 0.9828\n    - 0.9864\n    0v1_perm_p: 0.0001\n    1v2_auc: 0.9482\n    1v2_ci:\n    - 0.9443\n    - 0.952\n    1v2_perm_p: 0.0001\n    2v3_auc: 0.8885\n    2v3_ci:\n    - 0.8829\n    - 0.894\n    2v3_perm_p: 0.0001\n    3v4_auc: 0.7977\n    3v4_ci:\n    - 0.7903\n    - 0.8051\n    3v4_perm_p: 0.0001\n    all_ci_lower_above_theta: true\n- exp_id: exp_026_feature_stability_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp_001_pythia prompt-chain (K*=2)\n    results:\n      15D:\n        num_tested: 1\n        num_pass: 1\n        min_1v2_auc: 0.6262\n        mean_1v2_auc: 0.6262\n      10D:\n        num_tested: 5\n        num_pass: 5\n        min_1v2_auc: 0.6153\n        mean_1v2_auc: 0.6191\n      8D:\n        num_tested: 5\n        num_pass: 5\n        min_1v2_auc: 0.6056\n        mean_1v2_auc: 0.6159\n      5D:\n        num_tested: 5\n        num_pass: 2\n        min_1v2_auc: 0.5856\n        mean_1v2_auc: 0.5998\n      3D_top3:\n        num_tested: 1\n        num_pass: 0\n        min_1v2_auc: 0.5871\n        mean_1v2_auc: 0.5871\n    key_finding: 8+ features sufficient for robust K*=2 (all pass θ=0.60). 5D fragile\n      (2/5 pass). Top-3 alone fails. Feature diversity matters at the K* boundary.\n- exp_id: exp_arXiv_olmo\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.9958\n    auc_1v2: 0.5034\n    auc_2v3: 0.5069\n    auc_3v4: 0.5021\n    auc_4v5: 0.5037\n    jsd_0v1: 0.329\n    ordinal_acc: 0.33\n- exp_id: exp_arXiv_llama8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 3\n    auc_0v1: 0.9754\n    auc_1v2: 0.8447\n    auc_2v3: 0.6215\n    auc_3v4: 0.5362\n    auc_4v5: 0.5331\n    jsd_0v1: 0.1296\n    jsd_1v2: 0.0785\n    jsd_2v3: 0.0177\n    ordinal_acc: 0.4549\n    ordinal_mae: 0.8806\n- exp_id: exp_wiki_pythia\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_wiki_olmo\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_wiki_pythia_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.975\n    auc_1v2: 0.5846\n    auc_2v3: 0.5445\n    auc_3v4: 0.5205\n    auc_4v5: 0.5168\n    jsd_0v1: 0.080065\n    jsd_1v2: 0.007773\n    ordinal_acc: 0.3503\n- exp_id: exp_wiki_olmo_v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    auc_0v1: 0.9932\n    auc_1v2: 0.4986\n    auc_2v3: 0.5012\n    auc_3v4: 0.5057\n    auc_4v5: 0.5009\n    jsd_0v1: 0.1688\n    ordinal_acc: 0.3227\n- exp_id: exp_arXiv_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.983\n      1v2: 0.835\n      2v3: 0.626\n      3v4: 0.544\n      4v5: 0.513\n    pairwise_jsd:\n      0v1: 0.1656\n      1v2: 0.0668\n      2v3: 0.0156\n      3v4: 0.0089\n      4v5: 0.0061\n    ordinal_mae: 0.9\n    ordinal_accuracy: 0.446\n- exp_id: exp_wiki_llama8b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    K_star: 1\n    ordinal_mae: 1.2954\n    ordinal_accuracy: 0.3313\n    auc_0v1: 0.9316\n    auc_1v2: 0.5954\n    auc_2v3: 0.5392\n    auc_3v4: 0.5221\n    auc_4v5: 0.5212\n    jsd_0v1: 0.06169\n    jsd_1v2: 0.00931\n- exp_id: exp_arXiv_mistral7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    pairwise_auc:\n      0v1: 0.9848\n      1v2: 0.8201\n      2v3: 0.6275\n      3v4: 0.5295\n      4v5: 0.5295\n    jsd:\n      0v1: 0.14249\n      1v2: 0.076232\n      2v3: 0.018972\n      3v4: 0.009908\n      4v5: 0.008877\n    ordinal_mae: 0.8958\n    ordinal_accuracy: 0.4474\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_mean\n    - surp_d2_mean\n- exp_id: exp_wiki_mistral7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 1\n    ordinal_mae: 1.3445\n    ordinal_accuracy: 0.3273\n    auc_0v1: 0.9607\n    auc_1v2: 0.5552\n    auc_2v3: 0.5236\n    auc_3v4: 0.5181\n    auc_4v5: 0.5012\n    jsd_0v1: 0.054134\n    jsd_1v2: 0.005678\n    jsd_2v3: 0.003698\n    jsd_3v4: 0.003459\n    jsd_4v5: 0.003274\n- exp_id: exp_14b_c4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9598\n      1v2: 0.621\n      2v3: 0.5494\n      3v4: 0.5243\n      4v5: 0.5154\n    pairwise_jsd:\n      0v1: 0.1097\n      1v2: 0.0112\n      2v3: 0.0062\n      3v4: 0.0044\n      4v5: 0.0036\n    bootstrap_ci:\n      0v1:\n      - 0.9564\n      - 0.963\n      1v2:\n      - 0.6119\n      - 0.6304\n      2v3:\n      - 0.5392\n      - 0.5594\n      3v4:\n      - 0.514\n      - 0.5346\n      4v5:\n      - 0.5045\n      - 0.5265\n    permutation_p:\n      0v1: <0.001\n      1v2: <0.001\n      2v3: <0.001\n      3v4: <0.001\n      4v5: <0.001\n    k_star_statistically_confirmed: true\n    ordinal_mae: 1.2266\n    ordinal_accuracy: 0.3497\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_d2_mean\n    key_finding: K*=2 confirmed at 14B scale with bootstrap CI. 1v2 CI lower (0.6119)\n      > theta=0.60; 2v3 CI upper (0.5594) < theta=0.60. All permutation p<0.001.\n- exp_id: exp_32b_c4\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_wiki_qwen7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    auc_0v1: 0.9673\n    auc_1v2: 0.6108\n    auc_2v3: 0.5562\n    auc_3v4: 0.5297\n    auc_4v5: 0.529\n    jsd_0v1: 0.083514\n    jsd_1v2: 0.010991\n    jsd_2v3: 0.00555\n    jsd_3v4: 0.004611\n    jsd_4v5: 0.003894\n    ordinal_mae: 1.2501\n    ordinal_accuracy: 0.3532\n- exp_id: exp_wiki_scorer_confound\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    confound_verdict: confirmed\n    auc_0v1: 0.9404\n    auc_1v2: 0.587\n    auc_2v3: 0.5456\n    auc_3v4: 0.525\n    auc_4v5: 0.5172\n    critical_delta_1v2: -0.0238\n- exp_id: exp_wiki_scorer_confound_1b5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 1\n    confound_verdict: confirmed\n    auc_0v1: 0.9729\n    auc_1v2: 0.5994\n    auc_2v3: 0.533\n    auc_3v4: 0.5214\n    auc_4v5: 0.5068\n    jsd_0v1: 0.0886\n    ordinal_mae: 1.2995\n    ordinal_accuracy: 0.3466\n- exp_id: exp_arXiv_qwen7b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    k_star: 2\n    auc_0v1: 0.9575\n    auc_1v2: 0.8171\n    auc_2v3: 0.5989\n    auc_3v4: 0.5417\n    auc_4v5: 0.5192\n    jsd_0v1: 0.137085\n    jsd_1v2: 0.059688\n    jsd_2v3: 0.013508\n    jsd_3v4: 0.009125\n    jsd_4v5: 0.006738\n    ordinal_mae: 0.9617\n    ordinal_accuracy: 0.4255\n- exp_id: exp_arXiv_qwen1b5_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    auc_0v1: 0.9748\n    auc_1v2: 0.8105\n    auc_2v3: 0.6317\n    auc_3v4: 0.5437\n    auc_4v5: 0.5294\n    jsd_0v1: 0.154297\n    jsd_1v2: 0.066782\n    jsd_2v3: 0.019268\n    jsd_3v4: 0.008867\n    jsd_4v5: 0.006991\n    ordinal_mae: 0.9017\n    ordinal_accuracy: 0.4402\n- exp_id: exp_arXiv_llama8b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    auc_0v1: 0.9629\n    auc_1v2: 0.8433\n    auc_2v3: 0.6201\n    auc_3v4: 0.523\n    auc_4v5: 0.5245\n    jsd_0v1: 0.1214\n    jsd_1v2: 0.0815\n    jsd_2v3: 0.0195\n    jsd_3v4: 0.0083\n    jsd_4v5: 0.0082\n    ordinal_mae: 0.9025\n    ordinal_accuracy: 0.4407\n    scorer: pythia-1.4b\n- exp_id: exp_arXiv_mistral7b_crossscorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    scorer: pythia-1.4b\n    auc_0v1: 0.9798\n    auc_1v2: 0.8141\n    auc_2v3: 0.6075\n    auc_3v4: 0.5489\n    auc_4v5: 0.5391\n    jsd_0v1: 0.135575\n    jsd_1v2: 0.078\n    jsd_2v3: 0.020452\n    jsd_3v4: 0.010992\n    jsd_4v5: 0.008831\n    ordinal_mae: 0.9061\n    ordinal_accuracy: 0.4412\n- exp_id: exp_025_pythia_filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 9/9\n    strategies:\n    - no_filter\n    - binary_ours\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    mmlu:\n      no_filter: 0.2568±0.0012\n      binary_ours: 0.2585±0.0004\n      graduated_a09: 0.2561±0.0009\n    hellaswag:\n      no_filter: 0.5250±0.0008\n      binary_ours: 0.5251±0.0001\n      graduated_a09: 0.5253±0.0007\n    delta_vs_no_filter:\n      binary_ours_mmlu: '+0.0017'\n      binary_ours_hellaswag: '+0.0000'\n      graduated_a09_mmlu: '-0.0007'\n      graduated_a09_hellaswag: '+0.0003'\n    key_finding: All three filtering strategies produce nearly identical results on\n      Pythia-1.4B. Deltas are within noise (max 0.0017 MMLU). Hypothesized ordering\n      binary>graduated>no_filter NOT confirmed.\n- exp_id: exp_026_arxiv_filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    runs_completed: 15/15\n    strategies:\n    - no_filter\n    - binary\n    - graduated_a09\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    mmlu:\n      no_filter: 0.5899±0.0008\n      binary: 0.5876±0.0004\n      graduated_a09: 0.5900±0.0011\n    hellaswag:\n      no_filter: 0.6600±0.0002\n      binary: 0.6642±0.0004\n      graduated_a09: 0.6599±0.0003\n    delta_vs_no_filter:\n      binary_mmlu: '-0.0023'\n      binary_hellaswag: '+0.0042'\n      graduated_mmlu: '+0.0001'\n      graduated_hellaswag: '-0.0001'\n    key_finding: All three strategies produce nearly identical results. Graduated\n      ≈ no_filter; binary slightly better on HellaSwag (+0.004) but worse on MMLU\n      (-0.002). Hypothesized ordering graduated>binary>no_filter NOT confirmed.\n- exp_id: exp_027_latex_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 3\n    k_star_preserved: true\n    pairwise_auc_original:\n      0v1: 0.9948\n      1v2: 0.8581\n      2v3: 0.6436\n      3v4: 0.544\n      4v5: 0.5299\n    pairwise_auc_stripped:\n      0v1: 0.9948\n      1v2: 0.8297\n      2v3: 0.6229\n      3v4: 0.5468\n      4v5: 0.5476\n    auc_delta:\n      0v1: 0\n      1v2: -0.028\n      2v3: -0.021\n      3v4: 0.003\n      4v5: 0.018\n    latex_reduction_by_depth:\n      depth_0: 0.6%\n      depth_5: 4.4%\n    key_finding: K*=3 preserved after LaTeX removal. 2v3 AUC 0.6436→0.6229 (still\n      >θ=0.60). LaTeX format is NOT a confound.\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-18T11:45:22.545Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T11:45:22.545Z",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-18T11:45:22.568Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：C1' 被视为 descriptive/incremental；C3 被有效拒绝；整体 novelty 不足，需 fundamental reframe 才能在同级 venue 发表
核心假设：["K*∈{1,2,3} 被 dismiss 为 trivially expected——'DPI says saturation is rapid, you confirmed it is rapid, so what?'", 'θ=0.60 被攻击为 arbitrary：θ 选择几乎 deterministic 地决定 K* 值，整个 characterization 是 θ-contingent artifact', 'C3 完全被拒：effect sizes negligible，Pythia replication null，reviewer 怀疑 arXiv filtering 结果被 selectively omitted', '至少一位 reviewer 指出 missing cross-domain filtering experiments 和 exp-025 null 之间的矛盾——质疑 selective reporting', "'feature engineering + LightGBM' 没有 methodological novelty，定性为 'measurement study with weak measurements'", '多个 borderline CIs (Qwen-cont 0.6015, LLaMA fold-0 0.5969, 512tok 0.5979) 被视为 systematic insufficient power', 'Prompt-chain 实验设计不被认可为 ecologically valid despite retrain-chain comparison']
关键指标范围：{'arr_overall': [2.0, 2.5], 'arr_soundness': [2.5, 3.0], 'arr_excitement': [1.5, 2.5], 'arr_clarity': [3.0, 4.0], 'meta_recommendation': 'reject', 'prob_emnlp_main': [0.0, 0.08], 'prob_emnlp_findings': [0.08, 0.25]}
叙事方向：核心 reframe（不降级 venue 目标）：(1) 完全放弃 C3 作为独立 claim——降为 appendix case study；(2) 叙事从 'K* characterization + practical curation' 转为 'information-theoretic analysis of recursive generation degradation'——DPI framework 作为理论贡献，domain dependence 作为核心实证发现；(3) 主可视化从 K* 表格改为 AUC-decay curve，展示 generation depth 上的连续信号衰减而非离散 K* 断点——消解 θ-dependency 批评；(4) 单一 headline: 'structured text resists recursive information collapse — a domain complexity explanation'——domain dependence 是证据链最强、最难攻击的部分；(5) 补 exp-028 power analysis 和 naturalistic validation (exp-014) 填补 empirical gaps；(6) 如 ARR May 25 来不及修改，转投 AAAI 2027 (abstract Jul 25) 争取修改时间。

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
tier: worst
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
  "promptId": "f10ee06e-994e-4fc7-ad1d-abac6f9a97ff",
  "type": "user",
  "uuid": "3a29ee95-8e27-4762-8339-2e896df18737",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T11:45:22.565Z_

```json
{
  "parentUuid": "3a29ee95-8e27-4762-8339-2e896df18737",
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
  "uuid": "8738bb5a-a600-4e0c-ac14-d4ae07feb4ee",
  "timestamp": "2026-05-18T11:45:22.565Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T11:45:22.566Z_

```json
{
  "parentUuid": "8738bb5a-a600-4e0c-ac14-d4ae07feb4ee",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e1580ec1-bc0e-4ddd-b711-7f59f45a86a9",
  "timestamp": "2026-05-18T11:45:22.566Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1' 被视为 descriptive/incremental；C3 被有效拒绝；整体 novelty 不足，需 fundamental reframe 才能在同级 venue 发表 核心假设：[\"K*∈{1,2,3} 被 dismiss 为 trivially expected——'DPI says sa…",
  "leafUuid": "e1580ec1-bc0e-4ddd-b711-7f59f45a86a9",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Recursive generation depth characterization and domain-dependent saturation",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---

### Assistant

_source line 8 · 2026-05-18T11:45:29.417Z_

I'll analyze each planned experiment under the worst-tier scenario and generate detailed predictions.

Let me first check what experiments are in "planned" status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1580ec1-bc0e-4ddd-b711-7f59f45a86a9",
  "isSidechain": false,
  "requestId": "req_011Cb9yfP9N1rNK7ydjj3BNq",
  "type": "assistant",
  "uuid": "ac871e9e-e61d-4151-b106-959f9fbc8f64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Yj3BLAPQASarRBz2miyUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 49402,
      "cache_read_input_tokens": 11841,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 49402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 145,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 49402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 49402
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

_source line 9 · 2026-05-18T11:45:29.883Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GV8UpExqBxSMWBpfLfbSbR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac871e9e-e61d-4151-b106-959f9fbc8f64",
  "isSidechain": false,
  "requestId": "req_011Cb9yfP9N1rNK7ydjj3BNq",
  "type": "assistant",
  "uuid": "2415a58b-a1cb-44e0-8960-8ea0fb09ded7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Yj3BLAPQASarRBz2miyUZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 49402,
      "cache_read_input_tokens": 11841,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 49402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 145,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 49402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 49402
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

_source line 10 · 2026-05-18T11:45:29.898Z_

<details><summary>↩ Tool result · `toolu_01GV8UpExqBxSMWBpfLfbSbR`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2415a58b-a1cb-44e0-8960-8ea0fb09ded7",
  "isSidechain": false,
  "promptId": "f10ee06e-994e-4fc7-ad1d-abac6f9a97ff",
  "type": "user",
  "uuid": "e002e422-dabf-4226-b349-8cb30b89519c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）",
      "numLines": 5,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "2415a58b-a1cb-44e0-8960-8ea0fb09ded7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T11:46:07.287Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predictions for each "planned" experiment in the experiment_plan under the "worst" tier scenario.

Let me identify the planned experiments:
1. exp-014: Naturalistic validation (status: planned)
2. exp-028: Subsampling power curve (status: planned)

These are the only two with status "planned". Let me generate detailed worst-tier predictions for each.

Under the worst tier:
- ARR overall: 2.0-2.5
- Soundness: 2.5-3.0
- Excitement: 1.5-2.5


- Clarity: 3.0-4.0
- Meta recommendation: reject
- prob_emnlp_main: 0.0-0.08
- prob_emnlp_findings: 0.08-0.25

The worst-case scenario hinges on several critical vulnerabilities: the K* findings get dismissed as trivial consequences of DPI, the θ=0.60 threshold is attacked as arbitrary and K*-dependent, C3 is completely rejected due to negligible effect sizes and failed Pythia replication, and there's a glaring contradiction between the missing cross-domain filtering experiments and exp-025's null results, with no methodological resolution offered.

Reviewers would also flag the lack of genuine methodological novelty beyond standard feature engineering and LightGBM, treat the borderline confidence intervals as evidence of systematic underpowering, and question whether the prompt-chain design has ecological validity.

For exp-014 on Common Crawl, the naturalistic validation would likely show weak or null correlations with AlignScore and vocabulary metrics, and reviewers would dismiss it as just correlating one noisy proxy with another. Meanwhile, exp-028's subsampling power curve would actually backfire—revealing that robust K*=2 determination requires n≥4000 and showing instability at smaller sample sizes, which would reinforce rather than counter the critique about insufficient power across existing experiments.

Now I'm working through the specifics of exp-014 more carefully. The depth predictor trained on controlled prompt chains would struggle to generalize to messy real-world Common Crawl text, likely clustering most predictions at shallow depths and showing weak correlations with AlignScore (around 0.08-0.15) since AlignScore measures factual consistency rather than generational depth. The vocabulary richness correlation would be modest and directionally expected (around -0.12 to -0.20), but the fundamental problem is that without ground truth depth labels in Common Crawl, this becomes a purely correlational exercise with no validation anchor.

For exp-028, I'm examining the power curve across different sample sizes from C4 to determine when K*=2 becomes reliably detectable. The results suggest that robust determination of K*=2 requires around 3500-4000 samples for 80% power at θ=0.60, whereas smaller samples like n=1000 would only detect K*=2 in roughly 40-50% of resamples, indicating substantial instability at lower sample sizes.

What's concerning is that even n=5000—which several cross-model experiments used—still shows borderline confidence intervals, implying that 5000 might barely meet the threshold for adequate power. The Qwen-cont result with a CI lower bound of 0.6015 appears to be a fortunate resample; at that effect size, achieving 80% power would actually demand n≥6000 or higher. This power analysis essentially undermines the paper's credibility by suggesting the primary experiments are underpowered, giving reviewers a clear line of critique.

Now I'm constructing the full YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e002e422-dabf-4226-b349-8cb30b89519c",
  "isSidechain": false,
  "requestId": "req_011Cb9yfvyHWhxAUnjGtMbVx",
  "type": "assistant",
  "uuid": "4f6e1ebf-29d5-46c9-b7ab-618d1b72b11e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGnq6y18uUYd5U4Z7ZEeVF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 61243,
      "output_tokens": 7759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7759,
          "cache_read_input_tokens": 61243,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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

_source line 12 · 2026-05-18T11:48:08.178Z_

从 experiment_plan 中识别出两个 `status: planned` 的实验：exp-014 和 exp-028。

```yaml
tier: worst
narrative_guidance: >
  在 worst 档位下，reviewer 的核心立场是：(1) DPI 已经预测了 rapid saturation，你确认它确实 rapid——
  这不构成贡献；(2) θ=0.60 是 arbitrary threshold，K* 完全是 θ 的函数而非数据的固有属性；
  (3) C3 被有效拒绝（Pythia replication null + arXiv filtering null + effect sizes negligible）；
  (4) 多个 borderline CI 被视为 systematic underpowering 而非恰好通过；(5) prompt-chain 设计
  不具 ecological validity。在此框架下，两个 planned 实验的预期结果均会被 reviewer 解读为
  confirmatory of their negative assessment——exp-014 的弱相关被视为 "proxy correlating with proxy"，
  exp-028 的 power curve 暴露现有实验 borderline 结果的统计脆弱性，反而为 reviewer 提供攻击弹药。

imagined_experiments:
  - name: "Naturalistic Validation (Common Crawl 2025/2026)"
    plan_id: "exp-014"
    description: >
      对 Common Crawl 2025/2026 snapshot 随机抽样 ~50K 文档，用训练好的 15D+LightGBM 深度分类器
      做 depth 预测，与 AlignScore 和独立 vocabulary richness 指标（type-token ratio, hapax ratio,
      Yule's K）做 Spearman correlation。目标是验证实验室 prompt-chain 中发现的 depth signal
      在 wild data 中是否可观测。
    expected_results:
      predicted_depth_distribution:
        depth_0: "62-68% of documents"
        depth_1: "22-28% of documents"
        depth_2_plus: "8-12% of documents"
        note: "分布严重右偏——大多数文档被预测为 human 或 gen-1"
      spearman_rho_alignscore_vs_predicted_depth: -0.09  # 范围 [-0.14, -0.05]
      spearman_rho_alignscore_p_value: 0.03  # 技术上 significant（n 大），但 practically trivial
      spearman_rho_ttr_vs_predicted_depth: -0.13  # 范围 [-0.18, -0.08]
      spearman_rho_hapax_vs_predicted_depth: -0.11
      spearman_rho_yules_k_vs_predicted_depth: 0.08  # Yule's K 与 depth 弱正相关（repetitiveness 增加）
      false_positive_rate_on_known_human_subset: 0.18  # 18% 的已知 human text 被预测为 depth≥1
      classifier_confidence_calibration:
        mean_max_prob_depth0: 0.52  # 置信度低——接近 uniform
        mean_max_prob_depth1: 0.38
        mean_max_prob_depth2plus: 0.31
      cross_temporal_drift:
        cc_2025_vs_cc_2026_depth_distribution_jsd: 0.015  # 时间漂移极小，但也意味着 depth signal 不随时间变化——reviewer 会质疑是否真的在测 depth
    result_rationale: >
      在 worst 档位下，naturalistic validation 的核心问题是 "没有 ground truth"。
      
      (1) 预测分布严重右偏（depth 0-1 占 ~90%）：这符合现实——大多数 web 文本确实是 human-written 或
      single-pass AI generated。但 reviewer 会指出：分类器可能只是学到了一个 "text quality" proxy，
      把低质量 human text 错分为 AI-generated（18% false positive rate 支持此解读）。没有 ground truth
      就无法区分 "正确检测到 depth≥1" 与 "错误分类低质量 human text"。
      
      (2) 与 AlignScore 的弱相关（ρ≈-0.09）：AlignScore 测量事实一致性，与 generational depth 之间
      没有理论上的强联系。ρ=-0.09 在大样本下虽然 statistically significant，但 practically negligible
      （解释 <1% 方差）。Reviewer 会说 "you're correlating one noisy proxy with another noisy proxy，
      neither has validation"。
      
      (3) 与 vocabulary richness 的相关稍强（ρ≈-0.13）但仍弱：vocabulary richness 下降与 generational
      depth 之间有理论预期（DPI 预测 diversity 随迭代下降），但 ρ=-0.13 远不够证明因果关系。更关键的是，
      vocabulary richness 本身被 text length、domain、language register 强烈混淆——没有控制这些变量，
      相关不可解释。
      
      (4) 校准很差（mean max prob ~0.38-0.52）：模型在 wild data 上置信度远低于实验室数据，
      说明 distribution shift 严重。Reviewer 会质疑 "if your classifier is barely above random 
      confidence on real data, how can the K* characterization from lab data generalize?"
      
      (5) 时间漂移极小（JSD=0.015）：本意是展示稳定性，但 reviewer 会反转解读——"如果 AI contamination
      确实在 2025-2026 间快速增长，为什么你的 depth distribution 没有变化？要么你的检测器不敏感，
      要么你测的不是 depth。"
      
      综合效果：worst-tier reviewer 把 exp-014 定性为 "correlational analysis with no ground truth,
      effect sizes trivially small, and systematic confounds uncontrolled"。它不仅不能救 C1' 的
      ecological validity 问题，还暴露了 prompt-chain → wild transfer 的 gap。
    tables:
      - title: "Table X: Naturalistic Validation — Correlation with Quality Proxies"
        columns: ["Proxy Metric", "Spearman ρ vs Predicted Depth", "p-value", "95% CI", "Variance Explained"]
        rows:
          - ["AlignScore", "-0.09", "0.03", "[-0.14, -0.05]", "<1%"]
          - ["Type-Token Ratio", "-0.13", "0.002", "[-0.18, -0.08]", "1.7%"]
          - ["Hapax Legomena Ratio", "-0.11", "0.008", "[-0.16, -0.06]", "1.2%"]
          - ["Yule's K", "+0.08", "0.04", "[+0.03, +0.13]", "<1%"]
      - title: "Table Y: Predicted Depth Distribution on Common Crawl"
        columns: ["Predicted Depth", "Proportion", "Mean Classifier Confidence", "95% CI"]
        rows:
          - ["0 (human)", "65.2%", "0.52", "[0.50, 0.54]"]
          - ["1", "24.1%", "0.38", "[0.36, 0.40]"]
          - ["2", "7.3%", "0.33", "[0.30, 0.36]"]
          - ["3+", "3.4%", "0.31", "[0.28, 0.34]"]
    figures_description:
      - "Fig A: Scatter plot of predicted depth vs AlignScore on CC 2025 sample. 
        Massive point cloud with barely visible negative trend. Regression line nearly flat (slope ≈ -0.02). 
        Reviewer 一眼即判 'no meaningful relationship'。"
      - "Fig B: Predicted depth distribution histogram showing extreme right skew (depth 0 dominant bar).
        与 calibration curve (predicted prob vs observed freq) 对比，显示 severe miscalibration 
        on wild data — predicted depth≥2 严重 overconfident relative to any plausible ground truth。"
    analysis: >
      Worst-tier reviewer response: "The authors attempt naturalistic validation but this section 
      raises more questions than it answers. The correlations with quality proxies are negligibly 
      small (max |ρ|=0.13), and without ground truth depth labels in Common Crawl, these correlations 
      are uninterpretable. The 18% false positive rate on known-human text is concerning — it suggests 
      the classifier conflates text quality with generational depth. The severe calibration degradation 
      (lab confidence ~0.65 → wild confidence ~0.38) indicates substantial distribution shift that 
      undermines the external validity of the entire K* characterization. This experiment, rather than 
      validating the lab findings, highlights the gap between controlled prompt-chain settings and 
      real-world recursive contamination."
      
      Impact on scores: exp-014 结果不会改善任何 worst-tier 分数。Soundness 可能因 calibration 问题
      进一步受质疑（从 2.75 → 2.5 边界）。Excitement 不变（reviewer 已认定核心 claim trivial）。
      唯一微弱正面：论文至少尝试了 external validation，避免被 reviewer 批评 "no attempt at real-world 
      applicability"——但结果本身是 negative signal。

  - name: "Subsampling Power Curve for K*=2 Determination"
    plan_id: "exp-028"
    description: >
      在 C4 domain 上，从已有 n=5000 的 depth chain 数据中做 subsampling：
      n∈{500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000}，每个 n 做 10 次
      无放回抽样，对每个 resample 重新跑 5-fold GroupKFold + bootstrap CI，记录 (i) K*=2 的
      判定成功率（1v2 CI lower > θ=0.60 的比例），(ii) 1v2 AUC point estimate 分布，
      (iii) CI width 与 n 的关系。用 4 个 continuation-mode 模型（Pythia, OLMo, Qwen-cont, 
      LLaMA-8B）的数据分别计算 power curve，再叠加呈现。
    expected_results:
      power_at_n:
        # 定义：proportion of 10 resamples where 1v2 CI lower > 0.60
        # 分模型报告，因为 effect size 不同
        pythia_1.4b:
          n_500: 0.1
          n_1000: 0.2
          n_1500: 0.4
          n_2000: 0.5
          n_2500: 0.6
          n_3000: 0.7
          n_3500: 0.8
          n_4000: 0.9
          n_4500: 0.9
          n_5000: 1.0
          power_80_threshold_n: 3500
        olmo_1b:
          n_500: 0.0
          n_1000: 0.1
          n_1500: 0.2
          n_2000: 0.3
          n_2500: 0.4
          n_3000: 0.5
          n_3500: 0.6
          n_4000: 0.6
          n_4500: 0.7
          n_5000: 0.8
          power_80_threshold_n: ">5000"
          note: "OLMo 1v2 AUC=0.6145——effect size 小，80% power 需要 n>5000"
        qwen_cont:
          n_500: 0.0
          n_1000: 0.0
          n_1500: 0.1
          n_2000: 0.1
          n_2500: 0.2
          n_3000: 0.3
          n_3500: 0.3
          n_4000: 0.4
          n_4500: 0.5
          n_5000: 0.6
          power_80_threshold_n: ">5000"
          note: "Qwen-cont 1v2 AUC=0.6112, CI lower=0.6015——effect size 最小，80% power 需要 n≈7000-8000"
        llama_8b:
          n_500: 0.0
          n_1000: 0.1
          n_1500: 0.2
          n_2000: 0.3
          n_2500: 0.3
          n_3000: 0.4
          n_3500: 0.5
          n_4000: 0.6
          n_4500: 0.7
          n_5000: 0.8
          power_80_threshold_n: ">5000"
          note: "LLaMA 1v2 AUC=0.6123, similar to OLMo"
      ci_width_at_n5000:
        pythia: 0.018  # [0.6454, 0.6630]
        olmo: 0.020  # [0.6045, 0.6247]
        qwen_cont: 0.020  # [0.6015, 0.6213]
        llama_8b: 0.019  # [0.6028, 0.6216]
      ci_width_at_n2000:
        pythia: 0.031
        olmo: 0.033
        qwen_cont: 0.033
        llama_8b: 0.032
      mean_1v2_auc_stability:
        # AUC point estimate 的 SD across 10 resamples
        n_1000_sd: 0.015
        n_2000_sd: 0.010
        n_3000_sd: 0.008
        n_5000_sd: 0.005
      fraction_models_reaching_80pct_power_at_n5000: "1/4"
      fraction_models_reaching_80pct_power_at_n5000_detail: >
        仅 Pythia (effect size 最大, 1v2 AUC=0.654) 在 n=5000 达到 80% power。
        OLMo 和 LLaMA 恰好在 n=5000 的 80% 边界。Qwen-cont 在 n=5000 仅 ~60% power。
      implied_n_for_90pct_power_qwen_cont: "~10000"
    result_rationale: >
      在 worst 档位下，exp-028 的 power analysis 结果会成为 reviewer 手中的武器。核心逻辑链：
      
      (1) Effect size 极小导致 power 要求极高：C4 continuation mode 下的 1v2 AUC 集中在 
      0.611-0.654 区间（Cohen's h ≈ 0.20-0.31）。这是 "small effect" 区间。在 θ=0.60 下
      判定 K*=2 需要 CI lower > 0.60，即需要排除 AUC=0.60。当真实 AUC 仅 0.611（Qwen-cont），
      真实值与阈值之差仅 0.011——这要求极窄的 CI，进而需要极大的 n。
      
      (2) n=5000 仅对 Pythia 充分：Pythia 的 1v2 AUC=0.654（距 θ 0.054 pp margin）在 n=5000 
      下 power≈100%。但 OLMo（AUC=0.6145, margin=0.0145）和 LLaMA（AUC=0.6123, margin=0.0123）
      在 n=5000 下 power 仅 ~80%（恰好边界），Qwen-cont（AUC=0.6112, margin=0.0112）power 仅 
      ~60%。Reviewer 会指出："你论文中 4 个 continuation-mode 模型，有 3 个在 n=5000 的 power 
      不足 80%——你 claim 的 '7/8 configurations K*=2' 有多少是 lucky resamples？"
      
      (3) Qwen-cont CI lower=0.6015 被确认为统计侥幸：power analysis 显示 Qwen-cont 在 n=5000 
      下仅 60% 的 resamples 能给出 CI lower > 0.60。这意味着 Qwen-cont K*=2 的判定有 40% 
      概率在另一次采样中翻转为 K*=1。这直接确认了 reviewer 的 "systematic insufficient power" 
      批评——Qwen-cont 的 K*=2 不是 robust finding，而是 stochastic outcome。
      
      (4) θ-dependency 批评被强化：如果 θ 从 0.60 移至 0.62（仅 +0.02），则 Qwen-cont 和 LLaMA 
      立即变为 K*=1，OLMo 的 power 也大幅下降。Power curve 本质上是 θ-sensitivity analysis 的
      另一种呈现——它展示了 K* 判定对 (θ, n) 二维参数空间的敏感性。Reviewer 会说 "K* is not a 
      property of the data but a joint function of your arbitrary threshold and your sample size"。
      
      (5) 对 arXiv K*=3 的间接负面影响：arXiv 实验每模型仅 n=2200。如果 C4 在 n=5000 下都
      power 不足，arXiv 在 n=2200 下的 2v3 boundary pair（AUC≈0.62-0.65）power 估计仅 50-70%。
      虽然 arXiv 的 effect size 稍大（2v3 AUC 0.62-0.65 vs C4 1v2 AUC 0.61-0.65），但 n 
      减半的效应更大。Reviewer 不需要看 arXiv power curve 就能推断 "your arXiv K*=3 claims 
      are equally fragile"。
      
      (6) 唯一 partial mitigation：Pythia 在 n≥3500 已达 80% power，且 Pythia 的 K*=2 判定
      robust。这保住了 "至少有一个模型 robustly K*=2" 的最低线。但从 "7/8 configurations K*=2" 
      退化为 "1/4 robustly, 3/4 borderline" 是 devastating for the universality narrative。
      
      综合效果：exp-028 是一把双刃剑。在 best/mid tier 下它展示方法论严谨性；但在 worst tier 下，
      reviewer 会用它来论证 "the authors' own power analysis demonstrates that their headline 
      claim of K*=2 universality is an artifact of barely-sufficient sample sizes and an 
      arbitrary threshold"。这直接击中 worst tier 的两个核心假设：θ-contingent artifact 和
      systematic insufficient power。
    tables:
      - title: "Table X: Power to Detect K*=2 (1v2 CI lower > θ=0.60) by Sample Size"
        columns: ["Model", "True 1v2 AUC", "Margin over θ", "n for 80% Power", "Power @ n=5000", "Power @ n=2000"]
        rows:
          - ["Pythia-1.4B", "0.654", "+0.054", "~3500", "1.00", "0.50"]
          - ["OLMo-1B", "0.615", "+0.015", ">5000", "0.80", "0.30"]
          - ["LLaMA-3.1-8B", "0.612", "+0.012", ">5000", "0.80", "0.30"]
          - ["Qwen-1.5B cont", "0.611", "+0.011", "~7000-8000", "0.60", "0.10"]
          - ["Qwen-7B", "0.618", "+0.018", "~4500", "0.90", "0.30"]
      - title: "Table Y: CI Width Scaling with Sample Size (averaged across 4 models)"
        columns: ["n", "Mean CI Width", "Mean Power", "Fraction Models K*=2 Robust"]
        rows:
          - ["500", "0.055", "0.03", "0/4"]
          - ["1000", "0.038", "0.10", "0/4"]
          - ["2000", "0.032", "0.30", "0/4"]
          - ["3000", "0.025", "0.48", "0/4"]
          - ["3500", "0.023", "0.55", "1/4"]
          - ["4000", "0.020", "0.65", "1/4"]
          - ["5000", "0.019", "0.80", "1/4 (Pythia only robust)"]
    figures_description:
      - "Fig A: Power curve — x-axis: sample size n (500-5000), y-axis: proportion of resamples 
        with 1v2 CI lower > 0.60. Four colored lines (one per model). Pythia rises steeply and 
        reaches 1.0 at n=5000. OLMo and LLaMA rise slowly, reaching ~0.80 at n=5000. Qwen-cont 
        is the flattest curve, reaching only ~0.60 at n=5000. Horizontal dashed line at power=0.80.
        Key visual takeaway: only 1/4 models crosses the 80% power line at n=5000. Reviewer reads 
        this as 'systematic underpower'."
      - "Fig B: Spaghetti plot of 1v2 AUC point estimates across 10 resamples at each n for 
        Qwen-cont. Shows high variance at small n (SD≈0.015 at n=1000) with several resamples 
        dipping below 0.60. Even at n=5000, 4/10 resamples give CI lower < 0.60. Visually 
        communicates instability of the K*=2 determination for borderline models."
    analysis: >
      Worst-tier reviewer response: "The power analysis in exp-028, while methodologically 
      commendable, actually undermines the paper's central claims. The authors show that only 
      1 of 4 continuation-mode models (Pythia-1.4B) achieves 80% power for K*=2 detection 
      at their sample size of n=5000. The remaining 3 models — including Qwen-cont (CI lower 
      = 0.6015, power ≈ 60%), OLMo (power ≈ 80% borderline), and LLaMA (power ≈ 80% borderline) 
      — are systematically underpowered. The Qwen-cont result is particularly damning: the 
      authors' own analysis shows a 40% chance that an independent replication would yield K*=1 
      instead of K*=2. This transforms the '7/8 configurations yield K*=2' headline into 
      'the majority of configurations are at or below the minimum power threshold for reliable 
      detection.' Combined with the θ-sensitivity concern (moving θ by +0.02 would flip 3 of 
      4 models to K*=1), this analysis suggests K*=2 is not a robust empirical finding but 
      rather a contingent outcome of the specific (θ, n) parameterization chosen by the authors."
      
      Impact on scores: exp-028 在 worst tier 下是净负面。它被 reviewer 用作 "authors provided 
      the rope to hang their own claims" 的典型案例。Soundness 分数受打击（从 2.75 → 2.5 区间
      下端），因为 reviewer 现在有了 quantitative evidence for underpower。Excitement 不变
      （已经很低）。唯一好处：Clarity 分数可能因为 "transparent reporting" 微升（3.0 → 3.25），
      但不影响 meta recommendation。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f6e1ebf-29d5-46c9-b7ab-618d1b72b11e",
  "isSidechain": false,
  "requestId": "req_011Cb9yfvyHWhxAUnjGtMbVx",
  "type": "assistant",
  "uuid": "6160eb62-46fa-43d6-9bc4-b69edd1a5640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XGnq6y18uUYd5U4Z7ZEeVF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 61243,
      "output_tokens": 7759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 255,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7759,
          "cache_read_input_tokens": 61243,
          "cache_creation_input_tokens": 255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 255
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1' 被视为 descriptive/incremental；C3 被有效拒绝；整体 novelty 不足，需 fundamental reframe 才能在同级 venue 发表 核心假设：[\"K*∈{1,2,3} 被 dismiss 为 trivially expected——'DPI says sa…",
  "leafUuid": "6160eb62-46fa-43d6-9bc4-b69edd1a5640",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Recursive generation depth characterization and domain-dependent saturation",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C1' 被视为 descriptive/incremental；C3 被有效拒绝；整体 novelty 不足，需 fundamental reframe 才能在同级 venue 发表 核心假设：[\"K*∈{1,2,3} 被 dismiss 为 trivially expected——'DPI says sa…",
  "leafUuid": "6160eb62-46fa-43d6-9bc4-b69edd1a5640",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Recursive generation depth characterization and domain-dependent saturation",
  "sessionId": "1018244b-9021-454b-a72d-f8ef9a2cd81b"
}
```

---
