# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃 核心假设：['LLa

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/0d5a8c45-5ab9-4dc5-be52-9b903e3787c6.jsonl`
- **Structured JSON:** [`f0eaaabc1e42384eecfe.json`](../../sessions/f0/f0eaaabc1e42384eecfe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:46:40.437Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:46:40.437Z",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃\n核心假设：['LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）', '两个新模型族中至少一个确认 K*=2', 'Pythia decoding 3/4 K*=2，一个配置边缘', 'Length ablation 128-token K*=1（信息量不足），256/512 K*=2', 'Cross-scorer exp_A 的 scorer-dependence 模式在 exp-022 中重现但可控']\n关键指标范围：{'new_family_best_1v2_auc': [0.61, 0.635], 'new_family_worst_1v2_auc': [0.58, 0.602], 'pythia_decoding_kstar2_fraction': [0.75, 1.0], 'length_128_1v2_auc': [0.575, 0.605], 'total_conditions_kstar2': [12, 15], 'cross_scorer_kstar2_fraction': [0.6, 0.85]}\n叙事方向：Universality claim scoped 为 'K*=2 is consistent across all tested conditions meeting minimum information requirements (≥256 tokens; standard decoding)'。失败条件被分析为 principled boundary cases 而非 counterexamples——短文本信息不足导致 K* 降至 1 符合 DPI 预测，特定模型族的边缘性用 architecture-specific information loss rate 解释。增加一个 'Boundary conditions of universality' 分析段落。C1' 措辞降为 'K*=2 is a robust discrimination boundary under standard conditions'。仍冲 EMNLP Main，但需精心管理 reviewer #1 的 rebuttal（承认 scope + 强调已覆盖条件的一致性 + DPI 理论预测的泛化合理性）。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gen-depth-contamination\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, D012)\n\n### Primary: C1' (K* Characterization)\n首次系统测量递归合成文本的 generational discrimination boundary K*，并揭示其 universality。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*_empirical 的行为，发现 K*=2 在所有 10 个测试条件下保持不变，展现出跨模型架构、跨解码策略、跨生成模式、跨模型规模（1B–7B）、跨 instruct/base 的 universality。\n\n**子组件：**\n\n**(a) K*=2 universality across architectures, generation modes, and decoding strategies**\n> **4/4 model-mode configurations 与 4/4 decoding strategies 全部 K*=2：**\n>\n> *Model × mode (exp-007):*\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|---------|--------|-----------------|\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\n> - 4 decoding strategies 的 AUC 1v2 range [0.6866, 0.7039]，K* 完全不变\n> - K*=2 在所有 10 个测试条件下保持不变（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）\n> - ⚠️ θ-sensitivity: θ=0.60 下 4/4 K*=2；θ=0.70 下仅 Config4-T12 K*=2（1v2=0.7039 仅超 0.70 阈值 0.004），其余 3 config K*=1。论文以 θ=0.60 为主结论，θ=0.70 边界效应作 footnote\n> - ⚠️ 特征排序分化: K* 跨 config 稳定，但特征重要性排序不完全一致——Greedy vs T1.2 Spearman=0.53, p=0.041（Bonferroni 校正后阈值 0.0083，不显著）。论文中措辞应为 \"suggestive\" 而非确定性结论。Config4-T12 正确 top-3 features: hapax_ratio, ttr, surp_skew（非 freq_entropy）\n> - ⚠️ K*=2 边缘性双端注意: Qwen-cont 1v2 CI lower=0.6015（+0.15pp 高于 θ）+ Qwen-rw 2v3 CI upper=0.5991（-0.09pp 低于 θ），K*=2 边界在两端都极边缘。Discussion/Limitations 需同时提及\n> - Paper 可写：\"K*=2 is established as a consistent discrimination boundary across all 8 tested conditions (4 model-mode configurations and 4 decoding strategies; bootstrap 95% CI for AUC₁ᵥ₂ > 0.60; AUC₂ᵥ₃ CI upper < 0.60), suggesting universality beyond the ≤1.5B scale studied.\"\n> - ⚠️ 措辞策略（D017 Reviewer 评估）：分两层——\"established as consistent\" 用确定性语言（8/8 有统计检验支撑），\"suggesting universality beyond\" 对外推 hedging。不升级为 \"establishing universal\"——3 模型 ≤1.5B 会引发审稿人质疑消耗 rebuttal 预算\n> - ⚠️ C1' 子组件定位：呈现为\"对同一 claim 的 4 个 evidence 维度\"而非 4 个独立 finding。§4 标题用 \"K* Characterization\"，每个子节开头显式回答一个 reviewer concern，子节间用 transitional sentences 链接\n\n**(b) Cross-model transfer**\n> - Pythia↔OLMo 90-92% accuracy retention → K*=2 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\n> - transfer retention 80-92% suggests depth signal has a large text-intrinsic component（不量化具体比例，因 transfer accuracy retention ≠ 信号分解）\n> - ⚠️ 数值精度：Pythia→OLMo 91.6%, OLMo→Pythia 90.3%，范围 90-92%（非 91-92%）；Qwen-cont↔Pythia 84.7%/85.2%，范围 84-85%（非 83-85%）\n\n**(c) Degradation ordering consistency**\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\n\n**(e) Representation dependence of K* (§4.x Neural Probe / §5.x Discussion)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe, each model probing its own generations）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - **K*(neural) 不具备 universality**：仅 Qwen-cont 达到 K*=3，Pythia/OLMo 仍为 K*=2\n> - **Self-familiarity 解释**：每个模型用自己的 frozen embeddings 探测自己生成的文本。Qwen 对 Qwen-generated 文本更敏感（self-familiarity），K*=3 是 model-specific artifact 而非 universal signal\n> - **K*(theory) ≥ 3 弱化**：只能 claim \"K*(theory) ≥ 3 for Qwen representations\"，不能泛化为所有模型\n> - **Interpretability–deployability tradeoff 加强**：15D features 给出 universal K*=2（3/3 模型一致），neural probe 给出 model-dependent K*∈{2,3}。Model-free 方案的 universality 优势在 cross-model 结果下更明显\n> - 所有 3 模型 neural 2v3 AUC > lgbm 2v3 AUC（+3.9pp 到 +5.5pp），说明 learned representations 确实恢复了额外 depth signal，但不足以在所有模型上推过 θ=0.60\n> - 论文定位：**正面发现**——cross-model validation 揭示 K*(neural) 是 representation-dependent，验证了选择 model-free 15D features 作为 headline K* characterization 的正确性\n> - 预防审稿人 \"why bury the stronger result?\"：K*(neural)=3 仅对 Qwen 成立且是 self-familiarity driven，不适合作为 headline result；15D K*=2 的 universality（10/10 conditions + 3/3 models）才是可靠可部署的结论\n\n**(d) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection（\"How does generation mode affect depth estimation?\"），不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nK*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit: binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). K* serves as an actionable curation guideline — the discrimination boundary directly determines the optimal filtering granularity.\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*，揭示其 universality：**K*=2 在所有 10 个测试条件下不变**，表明递归生成存在一个与具体模型架构和解码策略无关的 universal discrimination boundary。这一发现为数据治理提供 actionable guidance——depth-aware filtering 在 K* 以内有效，且无需针对不同模型或解码配置分别调优。\n- **Headline result template**: \"Recursive generation has a universal discrimination boundary at K*=2: invariant across 4 model-mode configurations, 4 decoding strategies, and 1 cross-scale probe (10 conditions total, 1B–7B scale, base+instruct), with cross-model transfer retention of 80-92% confirming depth features are largely text-intrinsic. K*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit — binary filtering at K* (0.5941 MMLU) outperforms all tested alternatives including graduated weighting, surprisal selection, and DSIR.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Universality claim 只基于小模型，能推广到更大模型吗？\"** → exp-004 已将规模扩展至 7B（Qwen2.5-7B, continuation mode, scorer=Qwen2.5-1.5B），K*=2 依然成立，bootstrap 95% CI 确认。结合 4 个 ≤1.5B 架构族（GPT-2 style, Pythia, OLMo, Qwen），K*=2 在 1B–7B 范围内稳定。DPI 理论保证 K*_theory 对任意规模模型存在；进一步扩展至 13B+/70B+ 是重要 future work\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ universality 发现，不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\n4. **\"K*=2 太浅，graduated filtering 收益有限\"** → K*=2 恰好预测了这一结果：binary filtering at K* boundary (0.5941 MMLU) outperforms graduated weighting (best 0.5892), surprisal selection (0.5894), and DSIR (~0.5867). 这验证了 K* 作为 actionable curation guideline 的价值——discrimination boundary 直接决定了最优 filtering 粒度。K* 的 universality 意味着实践者无需为每个模型/解码配置单独标定阈值\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013 直接反驳**：Pythia↔OLMo 90-92% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\n6. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：frozen LLM embeddings + MLP probe 达到 K*=3（vs 15D K*=2），揭示 representation-dependent hierarchy: K*_theory ≥ K*_neural ≥ K*_15D。Hand-crafted 15D features 的优势在于 model-free transferability（80-92% cross-model retention）、可解释性（支持 degradation ordering 分析）、实用可部署性。Neural representations 多辨别 1 个深度级别但代价是 model dependence + ~100x 计算开销。这一 tradeoff 证明 15D features 是 practical choice，同时表明 theoretical boundary 延伸至 K*=2 之上\n7. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\n8. **\"Decoding strategy 只测了 4 种，coverage 不够\"** → 覆盖了实践中最常见的 decoding 配置（greedy, nucleus sampling, temperature scaling high/low）；4/4 完全一致强化 universality claim；extreme decoding（top-k=1 之外的 pathological 配置）留作 future work\n9. **\"为什么不直接用 LLM 做 depth estimation\"** → **exp-011 直接反驳**：GPT-5.5 和 Claude Opus 4.6 在 500 样本 zero-shot 5-class depth 分类上仅 33.1-33.2% accuracy（MAE ~1.1），低于 OBD 15-feature LightGBM 的 38.6%。二者 binary detection 均 ~88%，说明 LLM 能区分 human vs synthetic 但无法估计递归深度。depth estimation 是非平凡任务，需要专用特征工程\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with universality finding，C3 是 practical application，generation mode analysis 增加深度\n- Universality narrative 比 controllability 更有 impact：从 \"K* depends on X, Y, Z\" 升级为 \"K*=2 is a universal boundary\"，审稿人更容易记住和传播\n- 风险：universality claim 在 ≤1.5B 规模下的外推性是最大攻击面 → 论文中 scope 明确、limitation 诚实、DPI 理论支撑泛化的合理性\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 5K docs, depth\n    0-5, scorer=Qwen2.5-1.5B. 测试 K* 是否随模型规模变化。（实际参数已从原计划 1K/depth 0-3 扩展以匹配其他实验配置）'\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  registry_id: exp_004_7b_crossscale\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: exp_006_graduated_filtering\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n  status: planned\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: exp_011_llm_zeroshot\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_012_binary_confidence\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features。如果 neural probe 也给 K*=2 → C1'' claim 从 \"our features\n    find K*=2\" 升级为 \"K*=2 is data-intrinsic boundary\"。[D014 升级 P0：Reviewer 评估为最高边际价值实验]'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_015_neural_probe\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_016_base_vs_instruct\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- id: exp-018\n  claim: 1\n  description: 'Cross-family universality: LLaMA-3.1-8B, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 跨模型家族验证 K*。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_018_llama8b_depth\n  status: RUNNING\n  conclusion: null\n- id: exp-019\n  claim: 1\n  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_019_mistral7b_depth\n  status: RUNNING\n  conclusion: null\n- id: exp-020\n  claim:\n  - 1\n  - 3\n  description: 'Pythia-1.4B decoding ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2,\n    C4 5K docs, depth 0-5. 跨模型验证解码策略对 K* 的不变性。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: exp_020_pythia_decoding\n  status: RUNNING\n- id: exp-021\n  claim: 1\n  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512\n    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_021_length_ablation\n  status: RUNNING\n- id: exp-022\n  claim:\n  - 1\n  - 2\n  description: '4x4 cross-scorer matrix: 4 generators × 4 scorers, 验证 scorer independence\n    完整性。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-021\n  registry_id: exp_022_cross_scorer_matrix\n  status: QUEUED\n- id: exp-023\n  claim:\n  - 1\n  description: 'Domain ablation: Wikipedia seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 验证 K*=2 是否跨数据域一致（C4\n    vs Wikipedia）。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_023_domain_ablation\n  status: orphaned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- exp_id: exp_011_llm_zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- exp_id: exp_015_neural_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- exp_id: exp_006_graduated_filtering\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- exp_id: exp_004_7b_crossscale\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- exp_id: exp_A_alt_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9923\n      auc_1v2: 0.7012\n      auc_2v3: 0.587\n      mae: 1.006\n      accuracy: 0.417\n      spearman_rho_vs_baseline: 0.906\n    pythia_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.99\n      auc_1v2: 0.5923\n      auc_2v3: null\n      mae: 1.216\n      accuracy: 0.371\n      spearman_rho_vs_baseline: 0.942\n    olmo_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9918\n      auc_1v2: 0.6947\n      auc_2v3: null\n      mae: 1.016\n      accuracy: 0.413\n      spearman_rho_vs_baseline: 0.92\n    olmo_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.989\n      auc_1v2: 0.5858\n      auc_2v3: null\n      mae: 1.229\n      accuracy: 0.368\n      spearman_rho_vs_baseline: 0.902\n    key_finding: 'K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1\n      (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer\n      independence of feature ranking.'\n- exp_id: exp_B_14d_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    result: K*=2 stable across all 4 models after removing self_BLEU (14D)\n    key_finding: self_BLEU removal does not change K* boundary. FR-3 resolved.\n- exp_id: exp_C_permutation_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    resamples: 10000\n    all_boundary_pairs_p: <0.0001\n    key_finding: 10K permutation confirms all boundary p-values well below 0.01. FR-11\n      resolved.\n- exp_id: exp_D_obd_n500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    obd_accuracy_final: 0.38\n    obd_ci:\n    - 0.34\n    - 0.422\n    mcnemar_vs_gpt55_p: 0.0809\n    mcnemar_vs_claude_p: 0.0693\n    mcnemar_significant: false\n    multi_seed_std: 0\n    per_depth:\n      d0: 0.96\n      d1: 0.39\n      d2: 0.14\n      d3: 0.19\n      d4: 0.22\n    prob_merge_accuracy: 0.444\n    prob_merge_d4_bias: 0.8\n    note: v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant\n      — supports discussion.tex narrative\n- exp_id: exp_E_paired_stats\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_significant_pairs: 8/15\n    hellaswag_significant_pairs: 9/15\n    binary_ours_vs_all_mmlu: all significant\n    max_cohen_d_mmlu: 10.8\n    max_cohen_d_hellaswag: 8.98\n    graduated_a09_vs_dsir_corrected_p: 0.0523\n    cohen_d_method: d_av (Lakens 2013)\n    key_finding: 'binary-ours significantly outperforms all alternatives on MMLU.\n      On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni\n      cummax bug fixed: MMLU 10/15→8/15. Cohen''s d changed to d_av.'\n    bugfix_note: Holm-Bonferroni cummax variable was never updated, causing 2 MMLU\n      pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal\n      vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\n- exp_id: exp_012_binary_confidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- exp_id: exp_kstar_theta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    output_files:\n    - kstar_theta_curve.pdf (32KB)\n    - kstar_theta_curve.png (335KB)\n    models:\n    - Qwen-rewrite\n    - Pythia\n    - OLMo\n    - Qwen-cont\n    depth_pairs: 5\n    key_finding: All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5.\n      θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical\n      resolved.\n- exp_id: exp_016_base_vs_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- exp_id: exp_018_llama8b_depth\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: exp_019_mistral7b_depth\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: exp_020_pythia_decoding\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_021_length_ablation\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_022_cross_scorer_matrix\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:46:40.441Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:46:40.441Z",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-16T07:46:40.466Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃
核心假设：['LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）', '两个新模型族中至少一个确认 K*=2', 'Pythia decoding 3/4 K*=2，一个配置边缘', 'Length ablation 128-token K*=1（信息量不足），256/512 K*=2', 'Cross-scorer exp_A 的 scorer-dependence 模式在 exp-022 中重现但可控']
关键指标范围：{'new_family_best_1v2_auc': [0.61, 0.635], 'new_family_worst_1v2_auc': [0.58, 0.602], 'pythia_decoding_kstar2_fraction': [0.75, 1.0], 'length_128_1v2_auc': [0.575, 0.605], 'total_conditions_kstar2': [12, 15], 'cross_scorer_kstar2_fraction': [0.6, 0.85]}
叙事方向：Universality claim scoped 为 'K*=2 is consistent across all tested conditions meeting minimum information requirements (≥256 tokens; standard decoding)'。失败条件被分析为 principled boundary cases 而非 counterexamples——短文本信息不足导致 K* 降至 1 符合 DPI 预测，特定模型族的边缘性用 architecture-specific information loss rate 解释。增加一个 'Boundary conditions of universality' 分析段落。C1' 措辞降为 'K*=2 is a robust discrimination boundary under standard conditions'。仍冲 EMNLP Main，但需精心管理 reviewer #1 的 rebuttal（承认 scope + 强调已覆盖条件的一致性 + DPI 理论预测的泛化合理性）。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gen-depth-contamination

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

## Core Claims (2+1 结构, D012)

### Primary: C1' (K* Characterization)
首次系统测量递归合成文本的 generational discrimination boundary K*，并揭示其 universality。

DPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*_empirical 的行为，发现 K*=2 在所有 10 个测试条件下保持不变，展现出跨模型架构、跨解码策略、跨生成模式、跨模型规模（1B–7B）、跨 instruct/base 的 universality。

**子组件：**

**(a) K*=2 universality across architectures, generation modes, and decoding strategies**
> **4/4 model-mode configurations 与 4/4 decoding strategies 全部 K*=2：**
>
> *Model × mode (exp-007):*
> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |
> |-------|---------|--------|-----------------|
> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |
> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |
> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |
> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |
>
> *Decoding strategy invariance (exp-003):*
> | Decoding | AUC 1v2 | K* |
> |----------|---------|-----|
> | greedy | 0.6893 | 2 |
> | nucleus p=0.9 | 0.6866 | 2 |
> | temp=0.7 | 0.6887 | 2 |
> | temp=1.2 | 0.7039 | 2 |
>
> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002
> - 4 decoding strategies 的 AUC 1v2 range [0.6866, 0.7039]，K* 完全不变
> - K*=2 在所有 10 个测试条件下保持不变（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）
> - ⚠️ θ-sensitivity: θ=0.60 下 4/4 K*=2；θ=0.70 下仅 Config4-T12 K*=2（1v2=0.7039 仅超 0.70 阈值 0.004），其余 3 config K*=1。论文以 θ=0.60 为主结论，θ=0.70 边界效应作 footnote
> - ⚠️ 特征排序分化: K* 跨 config 稳定，但特征重要性排序不完全一致——Greedy vs T1.2 Spearman=0.53, p=0.041（Bonferroni 校正后阈值 0.0083，不显著）。论文中措辞应为 "suggestive" 而非确定性结论。Config4-T12 正确 top-3 features: hapax_ratio, ttr, surp_skew（非 freq_entropy）
> - ⚠️ K*=2 边缘性双端注意: Qwen-cont 1v2 CI lower=0.6015（+0.15pp 高于 θ）+ Qwen-rw 2v3 CI upper=0.5991（-0.09pp 低于 θ），K*=2 边界在两端都极边缘。Discussion/Limitations 需同时提及
> - Paper 可写："K*=2 is established as a consistent discrimination boundary across all 8 tested conditions (4 model-mode configurations and 4 decoding strategies; bootstrap 95% CI for AUC₁ᵥ₂ > 0.60; AUC₂ᵥ₃ CI upper < 0.60), suggesting universality beyond the ≤1.5B scale studied."
> - ⚠️ 措辞策略（D017 Reviewer 评估）：分两层——"established as consistent" 用确定性语言（8/8 有统计检验支撑），"suggesting universality beyond" 对外推 hedging。不升级为 "establishing universal"——3 模型 ≤1.5B 会引发审稿人质疑消耗 rebuttal 预算
> - ⚠️ C1' 子组件定位：呈现为"对同一 claim 的 4 个 evidence 维度"而非 4 个独立 finding。§4 标题用 "K* Characterization"，每个子节开头显式回答一个 reviewer concern，子节间用 transitional sentences 链接

**(b) Cross-model transfer**
> - Pythia↔OLMo 90-92% accuracy retention → K*=2 不是 model self-familiarity artifact
> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移
> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）
> - transfer retention 80-92% suggests depth signal has a large text-intrinsic component（不量化具体比例，因 transfer accuracy retention ≠ 信号分解）
> - ⚠️ 数值精度：Pythia→OLMo 91.6%, OLMo→Pythia 90.3%，范围 90-92%（非 91-92%）；Qwen-cont↔Pythia 84.7%/85.2%，范围 84-85%（非 83-85%）

**(c) Degradation ordering consistency**
> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）
> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std
> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）
> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）

**(e) Representation dependence of K* (§4.x Neural Probe / §5.x Discussion)**
> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe, each model probing its own generations）:
>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅
>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌
>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌
> - **K*(neural) 不具备 universality**：仅 Qwen-cont 达到 K*=3，Pythia/OLMo 仍为 K*=2
> - **Self-familiarity 解释**：每个模型用自己的 frozen embeddings 探测自己生成的文本。Qwen 对 Qwen-generated 文本更敏感（self-familiarity），K*=3 是 model-specific artifact 而非 universal signal
> - **K*(theory) ≥ 3 弱化**：只能 claim "K*(theory) ≥ 3 for Qwen representations"，不能泛化为所有模型
> - **Interpretability–deployability tradeoff 加强**：15D features 给出 universal K*=2（3/3 模型一致），neural probe 给出 model-dependent K*∈{2,3}。Model-free 方案的 universality 优势在 cross-model 结果下更明显
> - 所有 3 模型 neural 2v3 AUC > lgbm 2v3 AUC（+3.9pp 到 +5.5pp），说明 learned representations 确实恢复了额外 depth signal，但不足以在所有模型上推过 θ=0.60
> - 论文定位：**正面发现**——cross-model validation 揭示 K*(neural) 是 representation-dependent，验证了选择 model-free 15D features 作为 headline K* characterization 的正确性
> - 预防审稿人 "why bury the stronger result?"：K*(neural)=3 仅对 Qwen 成立且是 self-familiarity driven，不适合作为 headline result；15D K*=2 的 universality（10/10 conditions + 3/3 models）才是可靠可部署的结论

**(d) Generation mode analysis (§4.x Analysis subsection)**
> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）
> - Transferability: continuation 80-92% retention vs rewrite 61-63%
> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集
> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性
> - 论文定位：Analysis subsection（"How does generation mode affect depth estimation?"），不是独立 claim

### Secondary: C3 (K*-Aware Data Curation Validation)
K*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit: binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). K* serves as an actionable curation guideline — the discrimination boundary directly determines the optimal filtering granularity.

### Supporting Analysis: Canonical Condition Selection
Generation mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。

## Story Spine

- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。
- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**
- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者"在什么深度以下，depth-aware curation 比 binary detection 更有价值"。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*，揭示其 universality：**K*=2 在所有 10 个测试条件下不变**，表明递归生成存在一个与具体模型架构和解码策略无关的 universal discrimination boundary。这一发现为数据治理提供 actionable guidance——depth-aware filtering 在 K* 以内有效，且无需针对不同模型或解码配置分别调优。
- **Headline result template**: "Recursive generation has a universal discrimination boundary at K*=2: invariant across 4 model-mode configurations, 4 decoding strategies, and 1 cross-scale probe (10 conditions total, 1B–7B scale, base+instruct), with cross-model transfer retention of 80-92% confirming depth features are largely text-intrinsic. K*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit — binary filtering at K* (0.5941 MMLU) outperforms all tested alternatives including graduated weighting, surprisal selection, and DSIR."

## Anticipated Reviewer Concerns & Responses

1. **"Universality claim 只基于小模型，能推广到更大模型吗？"** → exp-004 已将规模扩展至 7B（Qwen2.5-7B, continuation mode, scorer=Qwen2.5-1.5B），K*=2 依然成立，bootstrap 95% CI 确认。结合 4 个 ≤1.5B 架构族（GPT-2 style, Pythia, OLMo, Qwen），K*=2 在 1B–7B 范围内稳定。DPI 理论保证 K*_theory 对任意规模模型存在；进一步扩展至 13B+/70B+ 是重要 future work
2. **"只是 feature engineering + off-the-shelf classifier，方法贡献弱"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ universality 发现，不是分类器本身
3. **"Prompt-chain 不代表真实世界递归污染"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法
4. **"K*=2 太浅，graduated filtering 收益有限"** → K*=2 恰好预测了这一结果：binary filtering at K* boundary (0.5941 MMLU) outperforms graduated weighting (best 0.5892), surprisal selection (0.5894), and DSIR (~0.5867). 这验证了 K* 作为 actionable curation guideline 的价值——discrimination boundary 直接决定了最优 filtering 粒度。K* 的 universality 意味着实践者无需为每个模型/解码配置单独标定阈值
5. **"同模型做生成和 surprisal 计算有 bias"** → **exp-013 直接反驳**：Pythia↔OLMo 90-92% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity
6. **"为什么不用 learned representations"** → **exp-015 直接回应**：frozen LLM embeddings + MLP probe 达到 K*=3（vs 15D K*=2），揭示 representation-dependent hierarchy: K*_theory ≥ K*_neural ≥ K*_15D。Hand-crafted 15D features 的优势在于 model-free transferability（80-92% cross-model retention）、可解释性（支持 degradation ordering 分析）、实用可部署性。Neural representations 多辨别 1 个深度级别但代价是 model dependence + ~100x 计算开销。这一 tradeoff 证明 15D features 是 practical choice，同时表明 theoretical boundary 延伸至 K*=2 之上
7. **"Graduated filtering 没和 data selection methods 比"** → exp-006 包含 DSIR baseline + α sensitivity sweep
8. **"Decoding strategy 只测了 4 种，coverage 不够"** → 覆盖了实践中最常见的 decoding 配置（greedy, nucleus sampling, temperature scaling high/low）；4/4 完全一致强化 universality claim；extreme decoding（top-k=1 之外的 pathological 配置）留作 future work
9. **"为什么不直接用 LLM 做 depth estimation"** → **exp-011 直接反驳**：GPT-5.5 和 Claude Opus 4.6 在 500 样本 zero-shot 5-class depth 分类上仅 33.1-33.2% accuracy（MAE ~1.1），低于 OBD 15-feature LightGBM 的 38.6%。二者 binary detection 均 ~88%，说明 LLM 能区分 human vs synthetic 但无法估计递归深度。depth estimation 是非平凡任务，需要专用特征工程

## Venue Fit

- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作
- 2+1 claim 结构：C1' 是 comprehensive characterization study with universality finding，C3 是 practical application，generation mode analysis 增加深度
- Universality narrative 比 controllability 更有 impact：从 "K* depends on X, Y, Z" 升级为 "K*=2 is a universal boundary"，审稿人更容易记住和传播
- 风险：universality claim 在 ≤1.5B 规模下的外推性是最大攻击面 → 论文中 scope 明确、limitation 诚实、DPI 理论支撑泛化的合理性


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
  registry_id: null
  status: planned
- id: exp-009
  claim: 3
  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试
    graduated vs binary filtering 的收益差异。'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - exp-006
  registry_id: null
  status: planned
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
  status: RUNNING
  conclusion: null
- id: exp-019
  claim: 1
  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus
    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_019_mistral7b_depth
  status: RUNNING
  conclusion: null
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
  status: RUNNING
- id: exp-021
  claim: 1
  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512
    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  registry_id: exp_021_length_ablation
  status: RUNNING
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
  status: QUEUED
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
  status: orphaned


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
  status: RUNNING
  conclusion: null
  metrics: {}
- exp_id: exp_019_mistral7b_depth
  name: ''
  status: RUNNING
  conclusion: null
  metrics: {}
- exp_id: exp_020_pythia_decoding
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_021_length_ablation
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_022_cross_scorer_matrix
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}

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
  "promptId": "d0d6bcbb-95a4-4230-8dcb-0d3e1160a685",
  "type": "user",
  "uuid": "23937103-033b-46aa-a665-be56a84ea903",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:46:40.464Z_

```json
{
  "parentUuid": "23937103-033b-46aa-a665-be56a84ea903",
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
  "uuid": "ef7f3cd7-d6de-49fd-8b87-bfddc83052c4",
  "timestamp": "2026-05-16T07:46:40.464Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:46:40.464Z_

```json
{
  "parentUuid": "ef7f3cd7-d6de-49fd-8b87-bfddc83052c4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bc069296-78f7-4d9f-a179-b777324fdeb5",
  "timestamp": "2026-05-16T07:46:40.464Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃 核心假设：['LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）', '两个新模型…",
  "leafUuid": "bc069296-78f7-4d9f-a179-b777324fdeb5",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 median-tier empirical characterization with universality scoping",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---

### Assistant

_source line 8 · 2026-05-16T07:46:43.813Z_

I'll analyze the experiment plan and generate detailed median-tier predictions for each RUNNING/QUEUED/planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc069296-78f7-4d9f-a179-b777324fdeb5",
  "isSidechain": false,
  "requestId": "req_011Cb5sqoqjAK4BnbmV3YiQW",
  "type": "assistant",
  "uuid": "02755f04-ca18-4eba-a304-0c11e88110ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6yMpRQBnEbd7VfHsEw3oz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32979,
      "cache_read_input_tokens": 11841,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32979,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 139,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32979
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

_source line 9 · 2026-05-16T07:46:45.105Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HEHfW4pEqw5HKyMn3ioiKe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02755f04-ca18-4eba-a304-0c11e88110ed",
  "isSidechain": false,
  "requestId": "req_011Cb5sqoqjAK4BnbmV3YiQW",
  "type": "assistant",
  "uuid": "11e7f2d8-438f-4ba0-a8bc-dd93c5753025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6yMpRQBnEbd7VfHsEw3oz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32979,
      "cache_read_input_tokens": 11841,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32979,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 139,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32979,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32979
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

_source line 10 · 2026-05-16T07:46:45.124Z_

<details><summary>↩ Tool result · `toolu_01HEHfW4pEqw5HKyMn3ioiKe`</summary>

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
  "parentUuid": "11e7f2d8-438f-4ba0-a8bc-dd93c5753025",
  "isSidechain": false,
  "promptId": "d0d6bcbb-95a4-4230-8dcb-0d3e1160a685",
  "type": "user",
  "uuid": "17efad84-df3a-4bae-b410-c550a50013ef",
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
  "sourceToolAssistantUUID": "11e7f2d8-438f-4ba0-a8bc-dd93c5753025",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-16T07:51:47.614Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the median tier definition and generate detailed predictions for each planned/running/queued experiment.

The median tier is defined as:
- 新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功
- universality claim 需 scope 但不崩溃

Key assumptions for median:
1. LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）


2. 两个新模型族中至少一个确认 K*=2，Pythia decoding 中 3/4 配置达到 K*=2 但有一个边缘，length ablation 显示 128-token 信息不足（K*=1）而 256/512 token 确认 K*=2
3. Cross-scorer 实验中的 scorer-dependence 模式在后续实验中重现但保持可控范围

Now I'm looking at the expected metric ranges for the new model families, with the best 1v2 AUC falling between 0.61-0.635.

For exp-018 with LLaMA-3.1-8B, I'm expecting this to be one of the confirming new families in the median tier, showing K*=2 with a marginal confidence interval around 0.600-0.607, and the 1v2 AUC should land in that best new family range.

Now looking at exp-019 with Mistral-7B, this appears to be the edge case where we'd see K*=1 with lower 1v2 AUC scores around 0.58-0.60, making it the worst performer among the new families we're testing.

For exp-020, I'm examining the Pythia decoding ablation where we expect 3 out of 4 configurations to show K*=2 with one edge case, though the signal strength here is weaker compared to what we saw with Qwen's decoding results.

The length ablation in exp-021 is showing the expected pattern where shorter sequences (128 tokens) yield K*=1 due to insufficient information, while both 256 and 512-token lengths stabilize at K*=2, which aligns with our DPI predictions about information density.

For the remaining experiments, exp-022 will give us a comprehensive cross-scorer matrix with some variation in K* values across different scorers, while the planned experiments—retrain-chain, contamination dose-response, and naturalistic validation—will test ecological validity and real-world performance on Common Crawl data.

Now I'm working through the exp-018 results with LLaMA-8B, where the median 1v2 AUC around 0.62 suggests this model generates higher-quality text that retains more information across generations, likely due to its 8B capacity advantage. The cross-scorer setup with Qwen as the evaluator introduces some noise but gives us a cleaner measure of text-intrinsic degradation rather than model-specific artifacts, and the 0v1 comparison should show near-perfect separation while 2v3 drops below 0.60.

For exp-019 with Mistral-7B, I'm seeing the weakest performance at 1v2 AUC around 0.59 with a lower CI bound near 0.58, which points to K*=1. The sliding window attention mechanism creates a unique compression pattern that differs fundamentally from standard full-attention models, and when Qwen's full-attention scoring evaluates this, there's a maximum architectural mismatch that makes the 15D features less effective at capturing Mistral's specific degradation signature.

For exp-020 with Pythia, most decoding configs hit K*=2 except for one marginal case, and the baseline 1v2 AUC of 0.6539 leaves less room to work with compared to Qwen. I'm checking whether greedy decoding is the outlier here since Pythia's greedy output tends toward repetition, making the 1v2 distinction harder to detect—and comparing back to Qwen's exp-003 where temperature 1.2 performed best, followed by greedy and temperature 0.7, then nucleus sampling, I suspect Pythia's greedy or nucleus p=0.9 is the marginal performer. Looking at the exp-003 results for Qwen, the decoding methods cluster pretty closely around 0.686-0.704 for 1v2 AUC, with T=1.2 showing the strongest performance. For Pythia with its weaker baseline signal, I'm thinking T=0.7 or greedy would likely produce the marginal result since they constrain the generation space more, whereas higher temperature creates faster information degradation that might actually boost the AUC metric. T=0.7 looks like the marginal case with an AUC around 0.608 and CI lower near 0.597, which technically puts it at K*=1 but just barely. The other three decoding configs should land at K*=2. Now moving to the length ablation experiment where 128 tokens gives K*=1.

For longer sequences, performance improves—256 tokens reaches K*=2 with AUC in the 0.615-0.625 range, and 512 tokens pushes it further to 0.625-0.640. The default setup across other experiments likely uses 512+ tokens. The reason 128 fails makes sense from an information theory perspective: with fewer tokens, the statistical estimators built on surprisal distributions and frequency entropy have much higher variance, so the feature vectors lose discriminative power. It's a measurement limitation rather than a fundamental signal problem.

Now looking at the cross-scorer matrix experiment with 4 generators and 4 scorers...

I'm trying to understand the pattern. Most self-scorer conditions hit K*=2, while cross-scorer conditions are more mixed. About 60-85% of the 16 cells show K*=2, meaning roughly 10-14 conditions succeed. The failures cluster predictably around continuation-mode generators paired with architecturally distant scorers.

For exp-022's 4×4 matrix with four generators and four scorers, I'm expecting around 11 out of 16 cells to land on K*=2—about 69%—based on what I saw in exp_A where generator mode matters more than scorer choice.

Looking ahead at the planned experiments, exp-008 should show similar K*=2 results with the retrain chain versus prompt chain, though the AUC values might diverge since retraining is noisier but more realistic. For exp-009's dose-response with synthetic injection at different rates, the filtering benefit should scale with injection level, but the binary versus graduated distinction should stay minimal across all rates. Exp-014 with Common Crawl data will likely show moderate correlation since real-world text is messier than controlled settings. Exp-023 on domain ablation with Wikipedia is orphaned for now.

Now I'm constructing the full YAML with detailed result rationales. I need to frame the universality claim carefully—K*=2 holds across all tested conditions with sufficient information (≥256 tokens, standard decoding), while failures are principled boundary cases rather than counterexamples. Short text fails to meet information requirements and drops to K*=1 as DPI predicts, and architecture-specific edge cases can be explained through information loss rates. I should add a section on the boundary conditions of universality.

Generating YAML structure... 我需要验证 scorer independence 的完整性，特别是 exp-022 对 exp-021 数据的依赖关系。虽然 exp-022 的 4×4 跨 scorer 矩阵看起来是在测试 scorer 独立性，但它实际上需要用到 exp-021 的长度消融数据或特定配置。现在我在推导 exp-018（LLaMA-8B）的预测结果：这个新的中位数层级家族在 1v2 对比中应该达到约 0.625 的 AUC（置信区间 [0.607, 0.643]），K*=2 得到确认但在置信区间下界处略显边际，0v1 跨 scorer 对比约 0.972，而 2v3 则降至 0.555 以下。

LLaMA-3.1-8B 采用分组查询注意力机制，这导致生成文本的统计特征略有不同，较大的模型容量使得人类与生成文本的区分变得稍微困难一些（0v1 低于 1.5B 模型，接近 Qwen-7B 的 0.9644），但 1v2 的判别能力受益于 LLaMA 学到的冗余模式——每个生成步骤都引入可测量的信息损失。置信区间下界约 0.607 超过阈值，因为尽管 LLaMA 在测试矩阵中是新的，但它使用标准 Transformer 块，其信息压缩遵循相同的 DPI 通道模型。对于 exp-019（Mistral-7B），这是表现不佳的新家族，1v2 AUC 约 0.593（置信区间 [0.582, 0.604]），K*=1，置信区间下界 0.582 低于 0.60 阈值。

Mistral 的滑动窗口注意力创造了不同的信息瓶颈，局部注意力窗口意味着长距离统计依赖以不同的速率处理，生成的文本保留局部连贯性但以不同的速率丧失全局分布模式。不过我需要检查一下——Mistral-7B-v0.3 实际上在 v0.3 版本中可能不使用滑动窗口注意力。

让我重新考虑。Mistral-7B-v0.3 使用标准注意力，滑动窗口为 131072 个令牌（对于典型序列实际上是完全注意力），但它仍然使用分组查询注意力。真正的差异可能来自训练数据组成和分词器差异——Mistral 使用不同的 BPE 分词器。不过评分器（Qwen2.5-1.5B）是在生成的文本上直接计算困惑度，用自己的分词器重新分词，所以分词器不匹配可能不是主要因素。更好的解释是 Mistral-7B 生成的延续文本在分布属性上与输入非常接近。

这种高保真特性意味着每一步生成的信息损失较低，使得在深度 1→2 处的判别变得更加困难。加上 Qwen 作为评分器只能捕捉通用文本质量下降而错过 Mistral 特定的微妙变化，进一步降低了 1v2 的 AUC。

现在看 Pythia 解码的实验结果，贪心搜索给出 1v2 AUC 约 0.645，置信区间 [0.635, 0.655]，K* 等于 2；nucleus p=0.9 的情况下 AUC 约 0.640，置信区间 [0.629...

我在检查中位数层级的数据，pythia_decoding_kstar2_fraction 范围是 [0.75, 1.0]，这意味着 3/4 或 4/4 的配置达到 K*=2。让我调整数值，确保有一个配置明确显示 K*=1 或边界情况。重新计算后，贪心搜索 AUC 约 0.648，置信区间 [0.637, 0.659]；nucleus p=0.9 的 AUC 约 0.638，置信区间 [0.626, 0.650]；温度 0.7 的情况...

现在我看到温度 0.7 应该产生更接近贪心的确定性文本，但实际 AUC 约 0.612，置信区间 [0.598, 0.626]，这表明 K*=1，而温度 1.2 的 AUC 约 0.662，置信区间 [0.651, 0.673]，确实是 K*=2。我需要重新考虑这些解码方法的顺序——在 Qwen 实验中，贪心、nucleus 和温度变体的范围非常紧凑（0.6862-0.7037），但 Pythia 的表现差异更大。

对于 Pythia，我预期温度 1.2 会产生最高的 AUC（更多随机性导致更多信息丧失），而温度 0.7 的行为更难预测——较低的温度使模型更确定性，这意味着每一步生成都更可预测，导致输出更加刻板化。

这种均匀的退化模式用 15 维特征更难检测出来。我现在意识到核采样 p=0.9 实际上比 p=0.95 更具限制性（保留的 token 更少），所以它更接近贪心方向。考虑到这些复杂性，我选择 T=0.7 作为边界情况，因为它为 Pythia 产生最少的多样性文本，使深度判别最困难。现在看一下长度消融实验的结果，128 个 token 时的 1v2 AUC 约为 0.590。

随着序列长度增加到 256 和 512 个 token，AUC 分别提升到 0.618 和 0.632，所需的特征维度也相应增加。128 个 token 失败的原因是样本太小——统计特征如惊喜度标准差和词汇多样性的估计方差急剧增加，大约 100 个独特 token 的文本使分布统计变得很嘈杂，低于 DPI 框架所需的最小信息阈值。

现在转向交叉评分矩阵实验，涉及 4 个生成器和 4 个评分器的组合。

根据现有数据，这些生成器应该是 Qwen-rw、Qwen-cont、Pythia 和 OLMo，评分器也是相同的 4 个模型。从之前的实验中看到一个关键模式：K* 值由生成器决定而非评分器决定——当生成器是 Qwen 时 K*=1，当是 Pythia 或 OLMo 时 K*=2，这表明生成深度的特征信号主要来自文本本身的生成过程。 Looking at the actual numbers from exp_A: K*=2 appears in the rewrite conditions and K*=1 in the continuation conditions, regardless of which scorer was used. The feature extraction method seems to depend on whether Qwen was used as a reference model for rewrite versus continuation distributions, but the key point is that K* varies by feature type, not by scorer choice.

For exp-022, if the median tier predicts cross_scorer_kstar2_fraction between 0.6 and 0.85, that suggests roughly 10-14 cells out of 16 would show K*=2. I'd estimate around 11 cells (0.69 fraction), with failures concentrated in continuation-mode generators paired with architecturally distant scorers—particularly OLMo and Qwen in continuation mode when scored by mismatched models.

For exp-008 with the retrain-chain approach, K*=2 holds up, though the 1v2 AUC drops slightly to around 0.63 compared to 0.654 in the prompt-chain setup, and the feature distributions show more noise. The ecological validity still checks out despite these complications.

The dose-response experiment shows K*=2 predictions remaining stable across injection rates—at 10% both methods barely beat the no-filter baseline, but by 30% binary pulls ahead, and at 50% binary clearly dominates. For naturalistic validation, the AlignScore correlation sits around 0.35-0.50, and the depth predictions align with expected shifts in the 2025/2026 data, which is supportive if not definitive. The domain ablation work shows Wikipedia maintains K*=2 with a 1v2 AUC near 0.62, confirming the domain effect exists without changing the core finding.

Now I'm ready to write out the full YAML, focusing on the running experiments first.

Looking at the median tier results, the pattern is becoming clearer: LLaMA confirms K*=2 as the best new family, Mistral edges toward K*=1 as the worst, Pythia decoding shows 3 out of 4 conditions at K*=2, the 128-token context hits K*=1 while longer contexts shift to K*=2, and the cross-scorer setup lands around 11 out of 16 conditions at K*=2. Tallying everything up, I've got 10 existing conditions with K*=2 from the baseline model-mode and decoding experiments, plus another 4 from cross-scale work. I'm tallying up the K*=2 conditions across all the new experiments—looks like I'm getting around 16 total, but the metric range suggests 12-15, so I need to recount more carefully and figure out whether this is counting just the new experiments or something else entirely. Looking at the breakdown by experiment, I'm getting 17 total conditions with K*=2, which overshoots the [12, 15] range. Let me adjust exp-022 down to 8 conditions instead of 11, bringing the total to 14—that fits nicely. Now I'm checking the cross_scorer fraction constraint, which should fall between 0.6 and 0.85 of the 16 conditions in exp-022.

Actually, maybe I'm thinking about this wrong. Perhaps total_conditions_kstar2 only counts the new primary conditions being added to the universality claim, not the robustness checks. So exp-018 through exp-021 contribute their K*=2 counts (1+0+3+2 = 6), while exp-022 serves as validation rather than adding to the primary condition total. = 6 out of 9

But [12,15] doesn't match 6/9 either.

I think total_conditions_kstar2 counts the TOTAL across all experiments (old + new) that the paper reports:
- Old: mvp-001, exp-001, exp-002, exp-003 (×4), exp-004, exp-016, exp-017 = 10
- New: exp-018 (1), exp-019 (0), exp-020 (3), exp-021 (2) = 6
- Total: 16... hmm, still above [12,15].

Let me reconsider. Maybe in median tier, some of the old experiments' conditions are re-evaluated and some become marginal. Or maybe the count is just for the "new round" of experiments being expanded.

Actually, I think the most natural interpretation is: total_conditions_kstar2 = total K*=2 conditions across ALL experiments the paper will report. The existing canonical conditions (excluding Qwen-rewrite) give me 9, and adding the new models and decoding variants gets me into the [12,15] range. If I count LLaMA as +1, Pythia decoding variants as +3, and length variants as +2, I land at 15—the upper bound. The sweet spot for median would be around 14, accounting for some variants being marginal or only partially K*=2.

I'll settle on 14 total K*=2 conditions and move forward with writing the YAML. I also need to include the planned/orphaned experiments (exp-008, exp-009, exp-014, exp-023) since the user asked for details on every planned experiment in the experiment plan.

For each experiment, I'm structuring the output with name, plan_id, description, expected_results with detailed metrics, result_rationale explaining the median-tier numbers, tables, figures, and analysis sections. This will be comprehensive but focused.

I'm also reconsidering the temperature=0.7 edge case for Pythia decoding—in exp-003 with Qwen, T=0.7 gave 1v2 AUC of 0.6885 compared to the baseline Qwen-cont at 0.6114 and Qwen-rw at 0.6957, so I need to account for that variance in my projections.

For Pythia specifically, with a baseline of 1v2=0.6539 at nucleus p=0.95 T=1.0, the decoding strategies should cluster around this point, and T=0.7 represents the marginal case where the confidence interval lower bound hits 0.597, making it technically K*=1—the tighter token distribution creates a more constrained channel that could push performance either direction.

Now I'm thinking through the cross-scorer matrix setup in exp-022. It's testing 4 generators against 4 scorers, likely building on the length ablation work from exp-021 to examine how scorer independence affects the 15D feature predictions. The generators are probably Qwen, Pythia, OLMo, and possibly LLaMA or a length variant, while the scorers are the four models computing the feature vectors. This connects back to what exp_A showed about scorer dependence. Looking at the key finding more carefully—it says K* splits by generator data and mode, not the scorer. So rewrite mode gives K*=2 while continuation mode gives K*=1, regardless of which model scores the text. But this seems to contradict the earlier results where self-scoring conditions in continuation mode also showed K*=2, so I need to reconcile what's actually happening across these experiments. -scorer. So the issue is specifically CROSS-scorer on continuation mode text.

OK so the pattern is:
- Self-scored continuation: K*=2 (exp-001, exp-002, exp-017)
- Cross-scored continuation: K*=1 (exp_A)
- Rewrite mode: K*=2 regardless of scorer (exp_A)

So for exp-022 (4×4 cross-scorer matrix), with 4 generators and 4 scorers in continuation mode:
- Self-scorer diagonal (4 cells): K*=2
- Cross-scorer off-diagonal (12 cells): some K*=2, some K*=1

Based on exp_A, cross-scorer continuation gave K*=1. But exp-013 showed cross-model transfer retention of 80-92% for continuation mode. The difference might be that exp_A used Qwen as scorer on Pythia/OLMo text specifically.

For exp-022 in the median tier, I'm expecting the cross-scorer K*=2 fraction to land between 0.6 and 0.85. The diagonal should give me 4 cells with K*=2, while architecturally similar pairs like Pythia and OLMo scoring each other's text should retain that high transfer rate around 91-92%. The more distant scorer-generator pairs would likely show mixed results, with maybe 4-6 additional K*=2 cells out of the remaining 12 cross-scorer positions. of remaining 10

Total: 4 + 2 + 5 = 11/16 = 0.69 → in [0.6, 0.85] ✅

Let me refine: 
- Self-scored (4): all K*=2
- Pythia→OLMo: K*=2
- OLMo→Pythia: K*=2
- Qwen→Pythia: K*=2 (edge, CI lower ~0.601)
- Qwen→OLMo: K*=1 (CI lower ~0.595)
- Pythia→Qwen: K*=1 (CI lower ~0.590)
- OLMo→Qwen: K*=1 (CI lower ~0.588)
- Generator 4 interactions: depends on what generator 4 is

I need to figure out which models are actually being used as the four generators and scorers. Looking at the project context, I have Qwen-1.5B, Pythia-1.4B, OLMo-1B available, but I'm not certain about the fourth model—it could be LLaMA-8B, Qwen-7B, or possibly a variant like Qwen-base versus Qwen-instruct. Let me work with the three confirmed smaller models and determine what the fourth one is based on the experimental setup. I'm tallying up the median tier results—Qwen-7B shows decent cross-scoring capacity with 3 out of 6 interactions hitting K*=2, bringing the total to 11 out of 16 edges. Rather than continue second-guessing myself, I'm going to commit to these predictions and move forward with writing them out.

Now I'm working through the remaining experiments: the Pythia decoding variants show a range from 0.612 to 0.665 AUC depending on the sampling strategy, with temperature 1.2 performing best, while the length ablation experiments reveal that longer context windows improve performance, climbing from 0.590 at 128 tokens up to 0.634 at 512 tokens.

The cross-scorer validation confirms K*=2 in 11 out of 16 cases with strong agreement, and I'm seeing consistent patterns across the other experiments—the retrain-chain and domain experiments both land around 0.618-0.631, the dose-response shows binary outperforming graduated at all levels, and the naturalistic correlation with AlignScore sits at a moderate 0.40.

I'm now compiling the YAML output with precise numbers and checking that my LLaMA baseline of 0.625 fits within the expected range for the new family.

Now I'm verifying the metrics against the experimental data—the Mistral worst-case at 0.593 checks out, the Pythia K*=2 fraction is exactly 0.75, and the length-128 condition validates at 0.590. Counting up all the K*=2 conditions across the new experiments gives me 8 total, which falls within the expected range. Looking at the breakdown across the new experiments, I'm counting the K*=2 conditions for each: exp-018 has 1, exp-019 has 0, exp-020 has 3, exp-021 has 2, exp-022 has 11, and exp-023 has 1. That gives me 18 total K*=2 conditions across these six experiments, though I need to figure out whether exp-008, exp-009, and exp-014 should be included in the primary count since they're P1/P2 rather than P0.

The [12, 15] range might be narrower than I thought—perhaps it only counts non-cross-scorer conditions, which would give me around 7 new ones plus the existing 10 for a total of 17. I'm probably overthinking the exact categorization here. The most straightforward reading is that the metric tracks all conditions where K*=2 across the entire paper, but limited to the primary conditions that matter for the main claims. I'll treat [12, 15] as a constraint and move forward with that understanding. I'm realizing the paper probably groups configurations at the model level rather than counting every individual config separately, so I shouldn't worry about the exact total matching up—I should just make sure my individual experiment predictions stay consistent with what would fit in the median tier.

Now I'm laying out the specific results tables for each experiment, starting with the depth comparison metrics showing AUC scores and statistical significance across different layer pairs. Looking at the rest of exp-019's results, the AUC drops to 0.506 for the deepest comparison with a non-significant p-value of 0.12. Now I'm examining exp-022's design more carefully—it's a 4×4 cross-scorer matrix testing whether different scorers produce consistent rankings across 4 generators, and it depends on exp-021's length ablation findings, likely using the optimal sequence length identified there as a baseline for the scorer independence analysis. sense given all these have existing depth chain data.

Now I'm mapping out the self-scored diagonal of the cross-scorer matrix, pulling the K* and AUC values from previous experiments. Qwen-1.5B scores itself at K*=2 with ~0.611 AUC, Pythia-1.4B at K*=2 with ~0.654 AUC, OLMo-1B at K*=2 with ~0.615 AUC, and Qwen-7B at K*=2 with ~0.618 AUC—though I need to double-check that last one since the scorer in exp-004 was actually Qwen-1.5B, not Qwen-7B itself.

For the off-diagonal cells, I'm estimating that models within the same architecture family show mild AUC drops around 0.58-0.62 while staying at K*=2, whereas cross-family comparisons mostly hold K*=2 but with some marginal or failing cases. Rather than detailing all 16 cells, I'll present a compact matrix showing roughly 11 out of 16 cells at K*=2.

Now I'm turning my attention to exp-008 and the retrain-chain setup to think through how that experiment fits into the picture.

For this experiment with Pythia-1.4B using LoRA fine-tuning on the model's own generations across depths 0-4, I expect K*=2 to hold but with a different feature distribution than the prompt-chain baseline. The LoRA retraining should cause more dramatic parameter shifts, potentially pushing the 1v2 AUC higher to around 0.64-0.66, though the shallower depth chain might moderate this somewhat. The feature importance ranking should track similarly to prompt-chain but with notable differences.

Looking at the specific predictions: 1v2 AUC around 0.637 with feature correlations at Spearman ρ ~0.82, 0v1 AUC slightly lower at ~0.985 since LoRA retraining keeps generated text closer to the original distribution, and 2v3 AUC dropping below 0.60 to around 0.56. The key insight is that LoRA fine-tuning with rank=16 modifies only a constrained parameter subspace, creating information loss that's correlated with but distinct from prompt-chain degradation. The fact that K*=2 persists across both mechanisms suggests it's a fundamental property of the information channel rather than an artifact of the contamination method, and the comparable degradation rates between the two approaches actually support the ecological validity of the retrain-chain setup. Looking at the dose-response results from exp-009, the binary filtering approach shows a clear advantage that grows with contamination level—at 10% synthetic injection there's barely any improvement, but by 50% it matches the pattern from exp-006 with a meaningful gap over the no-filter baseline. Graduated filtering consistently underperforms binary across all doses, which aligns with the K*=2 prediction. Now examining the naturalistic validation results from exp-014...

For the CC data, I'm seeing moderate correlations with alignment scores around 0.42 and vocabulary richness at 0.38, though the depth predictions skew higher in the 2026 snapshots compared to 2025. The main constraint here is lacking ground truth depths to validate against. Turning to exp-023 with Wikipedia as the seed source, the K*=2 pattern holds with a 1v2 AUC of 0.618, slightly lower than the C4 results likely because Wikipedia's structured format introduces different confounding features, though the top-ranked features remain largely consistent with domain-specific variations.

Now I'm preparing the YAML output and making the tables more concrete by including key pairwise AUC values. Looking at the JSD patterns across existing experiments, I can see the relationship between AUC and divergence—Qwen-rw shows 1v2 JSD of 0.0163 while 0v1 is much higher at 0.2669, and the newer Qwen-cont variant drops to 0.005107. I'll use these as reference points to estimate JSD values for the new experiments like LLaMA-8B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17efad84-df3a-4bae-b410-c550a50013ef",
  "isSidechain": false,
  "requestId": "req_011Cb5srACLYDUBrqS4fQmKJ",
  "type": "assistant",
  "uuid": "304dfd0c-86cb-4550-a427-3947c77a4d8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUnUgXZ6LocXV1HEuGpXJw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 44820,
      "output_tokens": 32362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32362,
          "cache_read_input_tokens": 44820,
          "cache_creation_input_tokens": 311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 311
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

_source line 12 · 2026-05-16T07:56:40.510Z_

```yaml
tier: median
narrative_guidance: >
  Universality claim scoped 为 'K*=2 is consistent across all tested conditions meeting
  minimum information requirements (≥256 tokens; standard decoding)'。Mistral 的失败被分析为
  architecture-specific information compression rate 导致的 principled boundary case（SWA/GQA 架构
  在 cross-scorer 条件下 15D features 信号不足），128-token 的失败用 DPI 的 minimum mutual information
  threshold 解释。Pythia T=0.7 的边缘性用 low-temperature channel narrowing 解释——temperature 过低导致
  vocabulary distribution 预先收窄，减少了 generational degradation 的可测量空间。增加 §5.x 'Boundary
  conditions of universality' 段落，将三类失败条件（短文本/低温/跨架构 scorer mismatch）统一在 DPI
  framework 下。C1' 措辞降为 'K*=2 is a robust discrimination boundary under standard
  conditions (≥256 tokens, T≥0.9, compatible scorer architecture)'。仍冲 EMNLP Main——14/19
  primary conditions K*=2 的一致性足够强，且失败条件均有理论预测支撑。Rebuttal 策略：承认 scope +
  强调已覆盖条件的 100% 一致性 + DPI 预测三类 boundary 的准确性作为理论泛化的证据。

imagined_experiments:
  - name: "LLaMA-3.1-8B cross-family depth chain"
    plan_id: "exp-018"
    description: >
      LLaMA-3.1-8B continuation mode, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5,
      scorer=Qwen2.5-1.5B。新模型族中表现较好的一个。
    expected_results:
      k_star: 2
      pairwise_auc:
        0v1: 0.9718
        1v2: 0.6253
        2v3: 0.5548
        3v4: 0.5212
        4v5: 0.5083
      pairwise_auc_std:
        0v1: 0.0028
        1v2: 0.0092
        2v3: 0.0058
        3v4: 0.0095
        4v5: 0.0071
      bootstrap_ci:
        0v1: {auc: 0.9718, ci_lower: 0.9693, ci_upper: 0.9743, perm_p: 0.0001}
        1v2: {auc: 0.6253, ci_lower: 0.6072, ci_upper: 0.6434, perm_p: 0.0001}
        2v3: {auc: 0.5548, ci_lower: 0.5447, ci_upper: 0.5649, perm_p: 0.0001}
        3v4: {auc: 0.5212, ci_lower: 0.5108, ci_upper: 0.5316, perm_p: 0.0012}
        4v5: {auc: 0.5083, ci_lower: 0.4978, ci_upper: 0.5188, perm_p: 0.0892}
      pairwise_jsd:
        0v1: 0.1384
        1v2: 0.0108
        2v3: 0.0049
        3v4: 0.0038
        4v5: 0.0031
      ordinal_mae: 1.198
      ordinal_accuracy: 0.357
      top_features: [freq_entropy, surp_d1_mean, surp_std, surp_d1_skew, hapax_ratio]
    result_rationale: >
      LLaMA-3.1-8B 使用 GQA + RoPE 的标准 Transformer 架构，与 Qwen-7B（exp-004）同为 7-8B
      continuation mode + cross-scorer 条件。Qwen-7B 1v2=0.6178（CI lower 0.6079），LLaMA-8B
      预期略高于 Qwen-7B（0.625 vs 0.618）因为 LLaMA 的训练数据更侧重英文 web text 与 C4 分布更匹配，
      生成文本的统计特征与 Qwen scorer 的 surprisal 计算有更好的 calibration。但 CI lower 仅 0.607，
      比 θ=0.60 高 0.7pp——边缘但 robust。0v1 AUC 0.972 低于 ≤1.5B 模型的 0.99+ 是因为 8B 模型
      生成文本质量更高，human-gen0 到 gen1 的跨越更小。4v5 non-significant（p=0.089）与 Qwen-7B
      的 4v5 p=0.0676 pattern 一致——大模型的深层代际几乎不可区分。
    tables:
      - title: "Table: LLaMA-3.1-8B pairwise depth discrimination"
        columns: [depth_pair, auc, ci_95, perm_p, k_star_boundary]
        rows:
          - [0v1, 0.9718, "[0.9693, 0.9743]", "<0.001", "-"]
          - [1v2, 0.6253, "[0.6072, 0.6434]", "<0.001", "K*=2 ✅ (CI lower 0.607>0.60)"]
          - [2v3, 0.5548, "[0.5447, 0.5649]", "<0.001", "below θ"]
          - [3v4, 0.5212, "[0.5108, 0.5316]", "0.001", "-"]
          - [4v5, 0.5083, "[0.4978, 0.5188]", "0.089", "n.s."]
    figures_description:
      - "AUC decay curve: 与 Qwen-7B (exp-004) overlay，showing similar decay profile but LLaMA consistently ~0.7pp higher at 1v2"
      - "Feature importance bar chart: top-5 features 与 Qwen-7B 共享 4/5（freq_entropy, surp_d1_mean, surp_std, surp_d1_skew），hapax_ratio 替代 surp_mean 进入 top-5"
    analysis: >
      LLaMA-8B 确认 K*=2 在第二个大规模模型族（非 Qwen 系列）上成立。CI lower=0.607 高于 θ 但属
      median 档预期的边缘范围（0.600-0.607）。与 Qwen-7B 的 CI lower=0.608 高度一致，说明 7-8B
      规模 + cross-scorer 条件下的 1v2 边界是 systematic 而非 random。Top features 中
      hapax_ratio 进入 top-5 是 LLaMA 特有——LLaMA 的 BPE 词表与 Qwen 不同，rare token 分布
      在 generational degradation 下的变化模式略有差异。但 surp_d1_std/surp_std/surp_d2_std
      仍在 top-10 内，与 exp-005 的 shared_top_discriminators 一致。Paper 可将 LLaMA-8B
      作为 universality evidence 的第 6 个独立模型族。

  - name: "Mistral-7B-v0.3 cross-family depth chain"
    plan_id: "exp-019"
    description: >
      Mistral-7B-v0.3 continuation mode, nucleus p=0.95 T=1.0, C4 5K docs, depth 0-5,
      scorer=Qwen2.5-1.5B。新模型族中表现较差的一个，K* 降至 1。
    expected_results:
      k_star: 1
      pairwise_auc:
        0v1: 0.9681
        1v2: 0.5934
        2v3: 0.5487
        3v4: 0.5195
        4v5: 0.5068
      pairwise_auc_std:
        0v1: 0.0031
        1v2: 0.0098
        2v3: 0.0062
        3v4: 0.0088
        4v5: 0.0075
      bootstrap_ci:
        0v1: {auc: 0.9681, ci_lower: 0.9652, ci_upper: 0.9710, perm_p: 0.0001}
        1v2: {auc: 0.5934, ci_lower: 0.5821, ci_upper: 0.6047, perm_p: 0.0001}
        2v3: {auc: 0.5487, ci_lower: 0.5382, ci_upper: 0.5592, perm_p: 0.0001}
        3v4: {auc: 0.5195, ci_lower: 0.5092, ci_upper: 0.5298, perm_p: 0.0034}
        4v5: {auc: 0.5068, ci_lower: 0.4963, ci_upper: 0.5173, perm_p: 0.1340}
      pairwise_jsd:
        0v1: 0.1312
        1v2: 0.0079
        2v3: 0.0044
        3v4: 0.0035
        4v5: 0.0028
      ordinal_mae: 1.241
      ordinal_accuracy: 0.342
      top_features: [surp_d1_mean, freq_entropy, surp_std, surp_mean, surp_d1_skew]
    result_rationale: >
      Mistral-7B-v0.3 是 median 档的核心 boundary case。1v2 AUC=0.593，CI lower=0.582，
      CI upper=0.605——CI 上界刚好跨过 θ=0.60 但下界远低于阈值。K*=1 的根因分析：(1) Mistral 的
      GQA(8 heads) + 大 vocabulary (32K) 组合意味着每个 generation step 的 information loss rate
      低于 Pythia/OLMo——Mistral 是一个更"高保真"的 iterated channel，DPI 预测 K*_theory 更高但
      K*_empirical 被 15D features 的检测灵敏度 cap 住；(2) cross-scorer 条件（Qwen-1.5B 计算
      surprisal）引入 tokenizer/architecture mismatch——Mistral 使用 SentencePiece BPE 而 Qwen 使用
      不同的 BPE scheme，相同文本的 token boundary 不同导致 surprisal-derived features 精度降低；
      (3) JSD 1v2=0.0079 是所有模型中最低的（Pythia 0.014, OLMo 0.013, Qwen-cont 0.005 但
      Qwen-cont 是 self-scorer），说明 gen1→gen2 的分布变化确实很小。论文定位：Mistral 不是
      counterexample 而是 principled boundary——它验证了 DPI 框架的预测，即高容量低损耗模型的
      K*_empirical 受限于 feature 灵敏度而非信号不存在。exp-015 的 neural probe 结果（neural
      representations 比 15D 多辨别 1 个深度）暗示如果用 Mistral 自身 embeddings 做 probe
      可能恢复 K*=2。
    tables:
      - title: "Table: Mistral-7B pairwise depth discrimination"
        columns: [depth_pair, auc, ci_95, perm_p, k_star_boundary]
        rows:
          - [0v1, 0.9681, "[0.9652, 0.9710]", "<0.001", "-"]
          - [1v2, 0.5934, "[0.5821, 0.6047]", "<0.001", "K*=1 ❌ (CI lower 0.582<0.60)"]
          - [2v3, 0.5487, "[0.5382, 0.5592]", "<0.001", "below θ"]
          - [3v4, 0.5195, "[0.5092, 0.5298]", "0.003", "-"]
          - [4v5, 0.5068, "[0.4963, 0.5173]", "0.134", "n.s."]
      - title: "Table: New model family comparison"
        columns: [model, 1v2_auc, ci_lower, k_star, scorer]
        rows:
          - [LLaMA-3.1-8B, 0.6253, 0.6072, 2, Qwen-1.5B]
          - [Mistral-7B-v0.3, 0.5934, 0.5821, 1, Qwen-1.5B]
          - [Qwen2.5-7B (exp-004), 0.6178, 0.6079, 2, Qwen-1.5B]
          - [Qwen2.5-1.5B base (exp-016), 0.6262, 0.6168, 2, self]
    figures_description:
      - "AUC decay comparison across all 7-8B models: LLaMA, Mistral, Qwen-7B overlay showing Mistral's flatter decay curve (lower information loss rate)"
      - "JSD heatmap: Mistral's 1v2 JSD visibly lowest among all models, linking to DPI channel capacity interpretation"
    analysis: >
      Mistral K*=1 是 median 档的 defining result。论文处理策略：(1) 在 §4.1 universality 结果表中
      标注 Mistral 为 boundary case（CI upper 0.605 跨 θ）；(2) 在 §5.x Boundary Conditions
      段落中分析三个 contributing factors（low info loss rate, cross-scorer tokenizer mismatch,
      feature sensitivity ceiling）；(3) 引用 DPI 理论论证 K*_theory ≥ 2 但 K*_empirical 受限于
      measurement precision——类比物理实验中测量精度与真实值的关系；(4) 与 exp-015 neural probe
      结果对照，论证更精细的 representation 可能恢复更高 K*。关键 rebuttal 准备：如果 reviewer 说
      "Mistral 证伪了 universality"，回应 1v2 AUC=0.593 仍远高于 chance (0.50)，信号存在但
      被 θ=0.60 阈值 cut off——这是 operational threshold choice 而非 physical boundary。

  - name: "Pythia-1.4B decoding strategy ablation"
    plan_id: "exp-020"
    description: >
      Pythia-1.4B 上复现 exp-003 的解码策略实验（greedy / nucleus p=0.9 / T=0.7 / T=1.2），
      验证解码不变性是否跨模型成立。3/4 配置确认 K*=2，T=0.7 边缘。
    expected_results:
      config1_greedy:
        k_star: 2
        pairwise_auc:
          0v1: 0.9748
          1v2: 0.6482
          2v3: 0.5504
          3v4: 0.5163
          4v5: 0.5098
        bootstrap_ci:
          1v2: {auc: 0.6482, ci_lower: 0.6378, ci_upper: 0.6586, perm_p: 0.0001}
          2v3: {auc: 0.5504, ci_lower: 0.5401, ci_upper: 0.5607, perm_p: 0.0001}
      config2_nuc09:
        k_star: 2
        pairwise_auc:
          0v1: 0.9911
          1v2: 0.6397
          2v3: 0.5468
          3v4: 0.5138
          4v5: 0.5072
        bootstrap_ci:
          1v2: {auc: 0.6397, ci_lower: 0.6271, ci_upper: 0.6523, perm_p: 0.0001}
          2v3: {auc: 0.5468, ci_lower: 0.5363, ci_upper: 0.5573, perm_p: 0.0001}
      config3_t07:
        k_star: 1
        pairwise_auc:
          0v1: 0.9812
          1v2: 0.6118
          2v3: 0.5472
          3v4: 0.5186
          4v5: 0.5114
        bootstrap_ci:
          1v2: {auc: 0.6118, ci_lower: 0.5973, ci_upper: 0.6263, perm_p: 0.0001}
          2v3: {auc: 0.5472, ci_lower: 0.5368, ci_upper: 0.5576, perm_p: 0.0001}
      config4_t12:
        k_star: 2
        pairwise_auc:
          0v1: 0.9967
          1v2: 0.6648
          2v3: 0.5537
          3v4: 0.5171
          4v5: 0.5126
        bootstrap_ci:
          1v2: {auc: 0.6648, ci_lower: 0.6542, ci_upper: 0.6754, perm_p: 0.0001}
          2v3: {auc: 0.5537, ci_lower: 0.5432, ci_upper: 0.5642, perm_p: 0.0001}
      kstar2_fraction: 0.75
      summary:
        all_0v1_above_097: true
        all_2v3_below_060: true
        t07_ci_lower: 0.5973
        t07_marginal_note: "CI lower 0.597 < θ=0.60 by 0.3pp"
    result_rationale: >
      Pythia-1.4B 的 baseline 1v2 AUC=0.6539（nucleus p=0.95 T=1.0），比 Qwen 的 baseline
      低约 4-8pp（Qwen-rw 0.696, Qwen-cont 0.611）。在 Qwen 上 4/4 decoding configs 均 K*=2
      是因为 Qwen 的 1v2 signal 有足够 headroom（最低 0.686）。Pythia 的 headroom 更小。
      T=0.7 成为 edge case 的机制：低温使 Pythia 的 token selection 更集中在高概率区域，每代
      生成文本的 vocabulary distribution 已经被 temperature 预先收窄（entropy reduction），
      留给 generational degradation 的可测量空间减少。具体来说，T=0.7 下 freq_entropy 和
      hapax_ratio 的 baseline variance 更低，surp_std 的 depth-wise gradient 变平——这些
      恰好是 1v2 discrimination 的关键 features。CI lower=0.597 仅低于 θ 0.3pp，属于
      measurement noise 边界。T=1.2 给出最高 1v2（0.665）因为高温放大了 generation noise，
      加速信息损失→1v2 contrast 增强。Greedy（0.648）高于 nucleus p=0.9（0.640）因为
      greedy 的完全确定性使得 generational drift 在 repetition/diversity features 上
      更容易被捕捉。
    tables:
      - title: "Table: Pythia decoding ablation pairwise AUC"
        columns: [config, 0v1, 1v2, "1v2 CI", 2v3, k_star]
        rows:
          - [greedy, 0.9748, 0.6482, "[0.638, 0.659]", 0.5504, "2 ✅"]
          - ["nuc p=0.9", 0.9911, 0.6397, "[0.627, 0.652]", 0.5468, "2 ✅"]
          - ["T=0.7", 0.9812, 0.6118, "[0.597, 0.626]", 0.5472, "1 ⚠️"]
          - ["T=1.2", 0.9967, 0.6648, "[0.654, 0.675]", 0.5537, "2 ✅"]
      - title: "Table: Qwen (exp-003) vs Pythia (exp-020) decoding comparison"
        columns: [config, qwen_1v2, pythia_1v2, delta, both_kstar2]
        rows:
          - [greedy, 0.6892, 0.6482, "-4.1pp", "✅"]
          - ["nuc p=0.9", 0.6862, 0.6397, "-4.7pp", "✅"]
          - ["T=0.7", 0.6885, 0.6118, "-7.7pp", "❌ (Pythia fails)"]
          - ["T=1.2", 0.7037, 0.6648, "-3.9pp", "✅"]
    figures_description:
      - "Side-by-side AUC decay curves: Qwen (exp-003) vs Pythia (exp-020) for each decoding config, highlighting T=0.7 divergence"
      - "Temperature vs 1v2 AUC scatter: both models show positive correlation, Pythia curve shifted ~4-5pp lower"
    analysis: >
      3/4 K*=2 的结果使 decoding invariance claim 从 "absolute" 降级为 "robust under standard
      conditions"。T=0.7 的失败是 model-specific：Qwen T=0.7 的 1v2=0.689 远高于阈值（CI lower
      0.680），但 Pythia T=0.7 仅 0.612（CI lower 0.597）。Qwen→Pythia 的 delta 在 T=0.7
      时最大（-7.7pp vs 其他 config 的 -3.9 到 -4.7pp），说明 Pythia 对低温更敏感——可能因为
      Pythia 的 vocabulary size 更小（50K vs Qwen 的 151K），低温下的 effective vocabulary
      收窄更剧烈。论文处理：在 §4.x Decoding 段落中报告 7/8 跨模型×decoding configs K*=2，
      T=0.7 × Pythia 作为 boundary case 放入 §5.x。措辞 "K*=2 is invariant to decoding
      strategy for T≥0.9; at T=0.7, model-dependent sensitivity emerges"。

  - name: "Text length ablation (128/256/512 tokens)"
    plan_id: "exp-021"
    description: >
      Qwen2.5-1.5B-Instruct continuation, 三个文本长度（128/256/512 tokens），验证 K* 的
      minimum information requirement。128-token 预期 K*=1。
    expected_results:
      length_128:
        k_star: 1
        pairwise_auc:
          0v1: 0.9893
          1v2: 0.5902
          2v3: 0.5481
          3v4: 0.5327
          4v5: 0.5189
        bootstrap_ci:
          0v1: {auc: 0.9893, ci_lower: 0.9872, ci_upper: 0.9914, perm_p: 0.0001}
          1v2: {auc: 0.5902, ci_lower: 0.5762, ci_upper: 0.6042, perm_p: 0.0001}
          2v3: {auc: 0.5481, ci_lower: 0.5342, ci_upper: 0.5620, perm_p: 0.0001}
          3v4: {auc: 0.5327, ci_lower: 0.5188, ci_upper: 0.5466, perm_p: 0.0008}
          4v5: {auc: 0.5189, ci_lower: 0.5050, ci_upper: 0.5328, perm_p: 0.0243}
        pairwise_jsd:
          0v1: 0.2614
          1v2: 0.0038
          2v3: 0.0029
          3v4: 0.0024
          4v5: 0.0021
        ordinal_mae: 1.223
        ordinal_accuracy: 0.361
      length_256:
        k_star: 2
        pairwise_auc:
          0v1: 0.9948
          1v2: 0.6187
          2v3: 0.5572
          3v4: 0.5378
          4v5: 0.5148
        bootstrap_ci:
          0v1: {auc: 0.9948, ci_lower: 0.9937, ci_upper: 0.9959, perm_p: 0.0001}
          1v2: {auc: 0.6187, ci_lower: 0.6078, ci_upper: 0.6296, perm_p: 0.0001}
          2v3: {auc: 0.5572, ci_lower: 0.5467, ci_upper: 0.5677, perm_p: 0.0001}
          3v4: {auc: 0.5378, ci_lower: 0.5273, ci_upper: 0.5483, perm_p: 0.0001}
          4v5: {auc: 0.5148, ci_lower: 0.5043, ci_upper: 0.5253, perm_p: 0.0052}
        pairwise_jsd:
          0v1: 0.2748
          1v2: 0.0046
          2v3: 0.0033
          3v4: 0.0030
          4v5: 0.0027
        ordinal_mae: 1.172
        ordinal_accuracy: 0.375
      length_512:
        k_star: 2
        pairwise_auc:
          0v1: 0.9971
          1v2: 0.6341
          2v3: 0.5632
          3v4: 0.5413
          4v5: 0.5156
        bootstrap_ci:
          0v1: {auc: 0.9971, ci_lower: 0.9963, ci_upper: 0.9979, perm_p: 0.0001}
          1v2: {auc: 0.6341, ci_lower: 0.6228, ci_upper: 0.6454, perm_p: 0.0001}
          2v3: {auc: 0.5632, ci_lower: 0.5529, ci_upper: 0.5735, perm_p: 0.0001}
          3v4: {auc: 0.5413, ci_lower: 0.5310, ci_upper: 0.5516, perm_p: 0.0001}
          4v5: {auc: 0.5156, ci_lower: 0.5051, ci_upper: 0.5261, perm_p: 0.0041}
        pairwise_jsd:
          0v1: 0.2871
          1v2: 0.0052
          2v3: 0.0036
          3v4: 0.0032
          4v5: 0.0029
        ordinal_mae: 1.148
        ordinal_accuracy: 0.384
      length_effect_summary:
        auc_1v2_by_length: {128: 0.5902, 256: 0.6187, 512: 0.6341}
        kstar_by_length: {128: 1, 256: 2, 512: 2}
        minimum_length_for_kstar2: 256
    result_rationale: >
      128-token K*=1 的根因是统计估计器的 sample size 效应，而非 depth signal 不存在。15D features
      中的 distributional statistics（freq_entropy 基于 unigram 频率分布，hapax_ratio 基于
      unique token 比例，surp_std/surp_skew 基于 surprisal 分布的高阶矩）在 128 tokens 下
      有极高的 estimation variance。以 hapax_ratio 为例：128 tokens 中 ~80-100 unique tokens，
      hapax 数量的 Poisson 噪声使得 depth 0 和 depth 1 的 hapax_ratio 分布严重重叠。
      surp_std 的 standard error 在 n=128 时约为 σ/√(128) ≈ σ/11.3，而 n=512 时约为 σ/22.6，
      precision 差 2 倍。JSD 1v2 从 512（0.0052）到 128（0.0038）的下降（-27%）直接反映了
      这个 estimation noise 效应。1v2 AUC=0.5902 的 CI upper=0.6042 刚过 θ=0.60，说明
      信号存在但 buried in noise。256 tokens 是 minimum viable length（CI lower=0.608 > 0.60
      且 margin 合理）。512→默认长度（exp-017 使用的长度）时 AUC 进一步提升至 0.634，但
      256→512 的增量（+1.5pp）远小于 128→256 的增量（+2.9pp），说明 256 已捕获主要
      statistical precision gains。DPI interpretation：每个 generation step 的 mutual
      information loss 是 per-token 的常数 ε，但 15D features 只能在 aggregate statistics
      上测量——aggregate 的 precision 需要 sufficient sample size，128 tokens 低于这个
      threshold。
    tables:
      - title: "Table: Length ablation summary"
        columns: [length, 1v2_auc, "1v2 CI", 1v2_jsd, k_star, "feature CI width (mean)"]
        rows:
          - [128, 0.5902, "[0.576, 0.604]", 0.0038, "1 ❌", "±0.014"]
          - [256, 0.6187, "[0.608, 0.630]", 0.0046, "2 ✅", "±0.011"]
          - [512, 0.6341, "[0.623, 0.645]", 0.0052, "2 ✅", "±0.008"]
      - title: "Table: Per-feature AUC at 1v2 by length"
        columns: [feature, auc_128, auc_256, auc_512]
        rows:
          - [freq_entropy, 0.554, 0.571, 0.582]
          - [surp_std, 0.548, 0.565, 0.578]
          - [surp_d1_std, 0.542, 0.558, 0.573]
          - [hapax_ratio, 0.536, 0.555, 0.569]
          - [ttr, 0.533, 0.551, 0.566]
    figures_description:
      - "Length vs 1v2 AUC curve with CI bands: showing monotonic increase with diminishing returns, vertical line at 256 marking 'minimum viable length'"
      - "Feature-level AUC heatmap (length × feature × depth pair): 128-token row visibly noisier with wider CI bands"
      - "Bootstrap CI width vs length: demonstrating √n scaling of precision"
    analysis: >
      Length ablation 的关键贡献：(1) 建立 K* 的 minimum information requirement（≥256 tokens），
      将 universality claim 的 scope 精确化；(2) 提供 DPI framework 的 quantitative validation
      ——如果 per-token information loss 是常数 ε，则 aggregate MI scales with n，预测 longer
      text → higher K*_empirical（or at least more precise measurement），实验数据完美符合；
      (3) 为 practitioner 提供 actionable guidance——对 128 tokens 以下的短文本不应尝试 depth
      estimation。128-token 的 CI upper=0.604 跨过 θ 但 lower=0.576 远低于——如果 θ 设为
      0.575 则 128 tokens 也 "pass"，但这样会让其他多个条件变得不可靠。这进一步证明
      θ=0.60 是 well-calibrated 的 operational threshold。

  - name: "4×4 cross-scorer matrix"
    plan_id: "exp-022"
    description: >
      4 generators × 4 scorers 完整交叉验证，量化 scorer independence。重现 exp_A 中的
      scorer-dependence 模式但在更大矩阵上验证其可控性。
    expected_results:
      generators: [Qwen-1.5B-cont, Pythia-1.4B, OLMo-1B, Qwen2.5-7B]
      scorers: [Qwen-1.5B, Pythia-1.4B, OLMo-1B, Qwen2.5-7B]
      kstar_matrix:
        Qwen1.5_Qwen1.5: 2
        Qwen1.5_Pythia: 1
        Qwen1.5_OLMo: 1
        Qwen1.5_Qwen7B: 2
        Pythia_Qwen1.5: 2
        Pythia_Pythia: 2
        Pythia_OLMo: 2
        Pythia_Qwen7B: 2
        OLMo_Qwen1.5: 2
        OLMo_Pythia: 2
        OLMo_OLMo: 2
        OLMo_Qwen7B: 2
        Qwen7B_Qwen1.5: 2
        Qwen7B_Pythia: 1
        Qwen7B_OLMo: 1
        Qwen7B_Qwen7B: 2
      kstar2_count: 12
      kstar2_fraction: 0.75
      auc_1v2_matrix:
        Qwen1.5_Qwen1.5: 0.6114
        Qwen1.5_Pythia: 0.5887
        Qwen1.5_OLMo: 0.5843
        Qwen1.5_Qwen7B: 0.6078
        Pythia_Qwen1.5: 0.6412
        Pythia_Pythia: 0.6539
        Pythia_OLMo: 0.6361
        Pythia_Qwen7B: 0.6387
        OLMo_Qwen1.5: 0.6058
        OLMo_Pythia: 0.6127
        OLMo_OLMo: 0.6146
        OLMo_Qwen7B: 0.6093
        Qwen7B_Qwen1.5: 0.6178
        Qwen7B_Pythia: 0.5932
        Qwen7B_OLMo: 0.5891
        Qwen7B_Qwen7B: 0.6248
      self_scorer_avg_1v2: 0.6262
      cross_scorer_avg_1v2: 0.6095
      cross_scorer_delta: -0.0167
      feature_ranking_spearman_across_scorers:
        mean_rho: 0.912
        min_rho: 0.873
        max_rho: 0.958
    result_rationale: >
      Cross-scorer matrix 重现 exp_A 的核心 pattern：K* 主要由 generator 决定而非 scorer，
      但 generator-scorer 之间的 architectural distance 调制 signal strength。12/16 K*=2
      （0.75）在 median 指标范围 [0.6, 0.85] 内。4 个 K*=1 failure 的结构化分析：
      (1) Qwen-1.5B-cont 作为 generator 被 Pythia/OLMo scored 时 K*=1——Qwen-cont 的
      1v2 signal 本身最弱（self-scored 仅 0.611，CI lower 0.6015），cross-scorer 增加的
      noise（~-2pp）足以将其推到 θ 以下；(2) Qwen-7B 被 Pythia/OLMo scored 时 K*=1——
      同理，7B 模型的 self-scored 1v2=0.618 已在边缘，加上 7B→1.4B/1B scorer 的 scale
      mismatch（smaller scorer 的 surprisal resolution 不足以捕捉 7B 模型的精细 depth
      signal）。注意 Pythia 和 OLMo 作为 generator 时完全 robust（4/4 scorers 都 K*=2），
      因为它们的 self-scored 1v2 较高（0.654 和 0.615）且与其他模型的 architectural distance
      较小。Feature ranking ρ≥0.87 跨所有 scorer 组合，确认 exp_A 的 ρ≥0.90 finding
      在完整矩阵上 hold（略低因为 include 了更多 distant pairs）。
    tables:
      - title: "Table: K* cross-scorer matrix (generator × scorer)"
        columns: [generator_scorer, Qwen-1.5B, Pythia-1.4B, OLMo-1B, Qwen-7B]
        rows:
          - ["Qwen-1.5B-cont", "K*=2 (0.611)", "K*=1 (0.589)", "K*=1 (0.584)", "K*=2 (0.608)"]
          - ["Pythia-1.4B", "K*=2 (0.641)", "K*=2 (0.654)", "K*=2 (0.636)", "K*=2 (0.639)"]
          - ["OLMo-1B", "K*=2 (0.606)", "K*=2 (0.613)", "K*=2 (0.615)", "K*=2 (0.609)"]
          - ["Qwen-7B", "K*=2 (0.618)", "K*=1 (0.593)", "K*=1 (0.589)", "K*=2 (0.625)"]
      - title: "Table: Cross-scorer feature ranking consistency"
        columns: [scorer_pair, spearman_rho, p_value]
        rows:
          - ["Qwen-1.5B vs Pythia", 0.921, "<0.001"]
          - ["Qwen-1.5B vs OLMo", 0.908, "<0.001"]
          - ["Qwen-1.5B vs Qwen-7B", 0.958, "<0.001"]
          - ["Pythia vs OLMo", 0.947, "<0.001"]
          - ["Pythia vs Qwen-7B", 0.896, "<0.001"]
          - ["OLMo vs Qwen-7B", 0.873, "<0.001"]
    figures_description:
      - "K* heatmap (4×4): color-coded by K* value, with 1v2 AUC annotated in each cell. Clear pattern: diagonal and Pythia/OLMo rows green, Qwen rows mixed"
      - "1v2 AUC heatmap: showing the systematic ~2pp cross-scorer penalty and generator-specific baseline differences"
      - "Feature ranking Spearman ρ network graph: nodes=scorers, edge thickness=ρ, all edges ≥0.87"
    analysis: >
      12/16 K*=2 足以支撑 scorer independence claim（with scope）。论文措辞："K*=2 is scorer-
      independent for generators with self-scored 1v2 AUC ≥ 0.63 (Pythia, OLMo); for
      marginal generators (Qwen-cont, Qwen-7B with self-scored 1v2 AUC ≈ 0.61-0.62),
      cross-scorer noise can push measurements below θ"。这与 exp_A 的 K*=1 finding（Qwen-cont
      cross-scored）完全一致。实际意义：实践者可以用任意 scorer 模型，只要 target generator 的
      depth signal 不在阈值边缘。Feature ranking ρ≥0.87 强化了 "scorer 影响的是 magnitude 而非
      feature structure" 的论点。与 exp-013（cross-model transfer）对照：exp-013 的 cross-model
      transfer retention 80-92% 测量的是 classifier 的 generalization，exp-022 测量的是
      feature computation 的 scorer-dependence——两者从不同角度确认 depth signal 主要是
      text-intrinsic。

  - name: "Retrain-chain ecological validity"
    plan_id: "exp-008"
    description: >
      Pythia-1.4B LoRA retrain-chain (rank=16, alpha=32), depth 0-4, 与 prompt-chain
      对比验证 ecological validity。
    expected_results:
      k_star: 2
      pairwise_auc:
        0v1: 0.9847
        1v2: 0.6312
        2v3: 0.5583
        3v4: 0.5224
      pairwise_auc_std:
        0v1: 0.0019
        1v2: 0.0085
        2v3: 0.0072
        3v4: 0.0098
      bootstrap_ci:
        0v1: {auc: 0.9847, ci_lower: 0.9822, ci_upper: 0.9872, perm_p: 0.0001}
        1v2: {auc: 0.6312, ci_lower: 0.6187, ci_upper: 0.6437, perm_p: 0.0001}
        2v3: {auc: 0.5583, ci_lower: 0.5472, ci_upper: 0.5694, perm_p: 0.0001}
        3v4: {auc: 0.5224, ci_lower: 0.5108, ci_upper: 0.5340, perm_p: 0.0018}
      prompt_vs_retrain_comparison:
        prompt_chain_1v2: 0.6539
        retrain_chain_1v2: 0.6312
        delta: -0.0227
        feature_spearman_rho: 0.841
        shared_top3: true
      ordinal_mae: 1.152
      ordinal_accuracy: 0.372
    result_rationale: >
      Retrain-chain K*=2 确认了 prompt-chain 的 ecological validity，但 1v2 AUC 低 2.3pp
      （0.631 vs 0.654）。差异的机制：LoRA rank=16 仅修改模型参数空间的一个低秩子空间，
      每代 fine-tuning 的 distribution shift 比 prompt-chain 更 gradual（prompt-chain 中
      每代的 output distribution 是 model(model(...)) 的嵌套，信息损失是 multiplicative；
      retrain-chain 的损失是 parameter-space 的 additive drift，被 LoRA 的低秩约束抑制）。
      Feature ranking Spearman ρ=0.84（vs prompt-chain），top-3 features 共享（surp_d1_std,
      surp_std, surp_d2_std），说明两种 chain 的 degradation mechanism 虽然不同但在 feature
      space 上高度一致。0v1 AUC=0.985 略低于 prompt-chain 的 0.993——retrain-chain 的 gen1
      更接近 human text（因为模型是在 human text 上 fine-tune 后再 generate，而非直接
      prompt model to continue）。
    tables:
      - title: "Table: Prompt-chain vs retrain-chain comparison (Pythia-1.4B)"
        columns: [chain_type, 0v1, 1v2, 2v3, 3v4, k_star, feature_ρ]
        rows:
          - [prompt-chain, 0.9932, 0.6539, 0.5515, 0.5153, 2, "-"]
          - [retrain-chain, 0.9847, 0.6312, 0.5583, 0.5224, 2, 0.841]
    figures_description:
      - "AUC decay curves: prompt-chain vs retrain-chain overlay, showing parallel but offset decay profiles"
      - "Feature importance comparison: side-by-side bar charts highlighting shared top discriminators"
    analysis: >
      Ecological validity confirmed: K*=2 和 top features 在两种 chain type 间一致。1v2 的
      -2.3pp gap 可解释为 LoRA 的 information-preserving bias（低秩约束 = 正则化 = 更慢
      的 degradation）。论文定位：supporting experiment，在 §4.1 的 footnote 或 Appendix
      中报告。为 reviewer concern #3（"prompt-chain 不代表真实污染"）提供直接回应。
      注意 depth 仅到 4（非 5），因为 retrain-chain 的 GPU cost 更高（每代需要 fine-tune）。

  - name: "Contamination dose-response"
    plan_id: "exp-009"
    description: >
      在 10%/30%/50% synthetic injection 比例下，比较 binary vs graduated filtering 的
      downstream benefit scaling。
    expected_results:
      dose_10pct:
        binary_ours_mmlu: 0.5879
        graduated_a09_mmlu: 0.5876
        no_filter_mmlu: 0.5873
        binary_vs_nofilter_delta: "+0.06pp"
        binary_vs_graduated_p: 0.42
      dose_30pct:
        binary_ours_mmlu: 0.5912
        graduated_a09_mmlu: 0.5897
        no_filter_mmlu: 0.5858
        binary_vs_nofilter_delta: "+0.54pp"
        binary_vs_graduated_p: 0.08
      dose_50pct:
        binary_ours_mmlu: 0.5941
        graduated_a09_mmlu: 0.5892
        no_filter_mmlu: 0.5865
        binary_vs_nofilter_delta: "+0.76pp"
        binary_vs_graduated_p: 0.003
      dose_response_slope:
        binary_benefit_per_10pct: "+0.016pp MMLU"
        graduated_gap_widens: true
      key_finding: "binary advantage scales with contamination dose; graduated never outperforms binary at any dose level"
    result_rationale: >
      Dose-response 结果直接从 K*=2 的 information-theoretic implication 推导：因为 K*=2，
      depth ≥2 的文本与 depth 1 的文本在 feature space 中几乎不可区分，所以 graduated weighting
      （试图利用 fine-grained depth signal beyond K*）无法比 binary filtering（只区分 depth 0
      vs depth ≥1）做得更好。在低 contamination dose（10%）时，filtering 的 absolute benefit
      极小（~0.06pp MMLU），因为 contaminated fraction 本身很小——这使得所有策略的 difference
      在统计噪声中不可分辨（p=0.42）。随着 dose 增加到 30% 和 50%，binary filtering 的优势
      开始统计显著（50% dose: p=0.003），因为有更多 contaminated samples 可被正确过滤。
      Graduated 在 50% dose 时的 MMLU（0.5892）与 exp-006 完全一致（实验复现）。
      Binary-vs-graduated gap 从 10%（+0.03pp, n.s.）扩大到 50%（+0.49pp, p=0.003），
      说明 graduated 的 over-fitting to noise beyond K* 在高 contamination 下更有害。
    tables:
      - title: "Table: Dose-response MMLU comparison"
        columns: [dose, binary_ours, graduated_a09, no_filter, "binary vs no-filter Δ", "binary vs grad p"]
        rows:
          - ["10%", 0.5879, 0.5876, 0.5873, "+0.06pp", "0.42 (n.s.)"]
          - ["30%", 0.5912, 0.5897, 0.5858, "+0.54pp", "0.08 (marginal)"]
          - ["50%", 0.5941, 0.5892, 0.5865, "+0.76pp", "0.003 **"]
    figures_description:
      - "Dose vs MMLU line plot: three strategies (binary, graduated, no-filter) showing divergence with increasing dose"
      - "Binary-vs-graduated delta vs dose: monotonically increasing gap, annotated with p-values"
    analysis: >
      Dose-response 是 C3 claim 的重要补充。Key message: K*-aware binary filtering 的优势
      不是 dose-specific artifact——它在所有测试 dose 下都是最优策略（虽然在低 dose 下差异
      不显著）。Graduated filtering 的 failure 同样 dose-invariant，验证了 K*=2 作为
      universal curation guideline 的 actionability。Limitation: 仅测了 3 个 dose 点，
      连续 dose-response curve 留作 future work。论文定位：exp-006 (50% dose) 的
      补充 ablation，放在 Appendix 或 §4.3 的 subsection。

  - name: "Naturalistic Common Crawl validation"
    plan_id: "exp-014"
    description: >
      对 Common Crawl 2025/2026 snapshot 样本做 depth prediction，与 AlignScore 和
      vocabulary richness 指标做 correlation analysis。
    expected_results:
      n_documents: 50000
      predicted_depth_distribution:
        cc_2025: {depth_0: 0.72, depth_1: 0.18, depth_2: 0.07, "depth_3+": 0.03}
        cc_2026: {depth_0: 0.65, depth_1: 0.22, depth_2: 0.09, "depth_3+": 0.04}
      correlation_with_alignscore:
        spearman_rho: 0.418
        p_value: "<0.001"
        interpretation: "moderate positive: higher predicted depth ↔ lower text quality"
      correlation_with_vocab_richness:
        ttr_spearman: -0.372
        hapax_spearman: -0.341
        freq_entropy_spearman: -0.389
      temporal_shift:
        mean_predicted_depth_2025: 0.42
        mean_predicted_depth_2026: 0.51
        shift_p_value: "<0.001"
    result_rationale: >
      Naturalistic validation 是 median 档最不确定的实验。AlignScore correlation ρ=0.42 是
      moderate 而非 strong，原因：(1) Common Crawl 包含大量非递归合成文本（SEO spam, template
      text, translation artifacts）会被误判为有 depth 信号；(2) AlignScore 主要衡量 factual
      consistency 而非 distributional degradation，两者 correlated 但不 identical；(3) 没有
      ground truth depth labels，所有分析都是 correlational。Vocabulary richness 指标与
      predicted depth 的负相关（ρ=-0.34 到 -0.39）符合 degradation ordering 预期：更深代次
      的文本 vocabulary diversity 更低。2025→2026 的 predicted depth 增加（mean 0.42→0.51）
      与公开报告的合成文本增长趋势一致，但 confounded by CC 爬取策略变化。
    tables:
      - title: "Table: Predicted depth distribution in Common Crawl snapshots"
        columns: [snapshot, "depth 0", "depth 1", "depth 2", "depth 3+", mean_depth]
        rows:
          - ["CC 2025-Q1", "72%", "18%", "7%", "3%", 0.42]
          - ["CC 2026-Q1", "65%", "22%", "9%", "4%", 0.51]
      - title: "Table: Correlation with text quality indicators"
        columns: [indicator, spearman_ρ, p_value, direction]
        rows:
          - [AlignScore, 0.418, "<0.001", "higher depth → lower quality"]
          - [TTR, -0.372, "<0.001", "higher depth → lower diversity"]
          - [Hapax ratio, -0.341, "<0.001", "higher depth → fewer rare words"]
          - [Freq entropy, -0.389, "<0.001", "higher depth → lower entropy"]
    figures_description:
      - "Predicted depth histogram: 2025 vs 2026 side-by-side showing rightward shift"
      - "Scatter plots: predicted depth vs AlignScore / TTR / freq_entropy with regression lines"
    analysis: >
      Naturalistic validation 提供 suggestive 而非 conclusive evidence。论文措辞谨慎：
      "Predicted depth distributions are consistent with reported trends in synthetic
      content prevalence" + "moderate correlation with independent quality measures
      provides convergent validity for the OBD framework"。明确 limitation：no ground
      truth, correlational only, confounded by non-recursive synthetic text。
      论文定位：§5 Discussion 的一个 subsection 或 Appendix。

  - name: "Wikipedia domain ablation"
    plan_id: "exp-023"
    description: >
      Wikipedia seed data, Qwen2.5-1.5B base continuation, 验证 K*=2 是否跨数据域一致。
      Status: orphaned（可能因优先级调整被搁置）。
    expected_results:
      k_star: 2
      pairwise_auc:
        0v1: 0.9912
        1v2: 0.6183
        2v3: 0.5518
        3v4: 0.5247
        4v5: 0.5112
      bootstrap_ci:
        0v1: {auc: 0.9912, ci_lower: 0.9895, ci_upper: 0.9929, perm_p: 0.0001}
        1v2: {auc: 0.6183, ci_lower: 0.6074, ci_upper: 0.6292, perm_p: 0.0001}
        2v3: {auc: 0.5518, ci_lower: 0.5415, ci_upper: 0.5621, perm_p: 0.0001}
        3v4: {auc: 0.5247, ci_lower: 0.5142, ci_upper: 0.5352, perm_p: 0.0003}
        4v5: {auc: 0.5112, ci_lower: 0.5007, ci_upper: 0.5217, perm_p: 0.0312}
      c4_vs_wiki_comparison:
        c4_1v2: 0.6262
        wiki_1v2: 0.6183
        delta: -0.0079
        feature_ranking_rho: 0.878
      ordinal_mae: 1.178
      ordinal_accuracy: 0.369
      top_features: [surp_std, freq_entropy, surp_d1_std, surp_d1_skew, surp_mean]
    result_rationale: >
      Wikipedia K*=2 与 C4 一致但 1v2 AUC 低 0.8pp（0.618 vs 0.626）。差异的来源：
      Wikipedia 文本有更强的 structural formatting（section headers, lists, citations, 
      infobox-derived text），这些 domain-specific patterns 在 continuation mode 下被
      model 部分保留，减少了 generation-specific degradation signal。freq_entropy 在 Wikipedia
      上的 discriminative power 略低，因为 Wikipedia 的 vocabulary distribution 本身更集中
      （专业术语 + 百科体裁的 formulaic expressions）。Feature ranking ρ=0.878 vs C4 说明
      degradation mechanism 跨域一致但 feature importance 的具体排列有 domain-specific shift。
      整体结论：K*=2 是 domain-independent，支持 universality claim 的 scope 扩展。
    tables:
      - title: "Table: C4 vs Wikipedia domain comparison (Qwen-base)"
        columns: [domain, 0v1, 1v2, "1v2 CI lower", 2v3, k_star]
        rows:
          - [C4, 0.987, 0.6262, 0.6168, 0.5496, 2]
          - [Wikipedia, 0.9912, 0.6183, 0.6074, 0.5518, 2]
    figures_description:
      - "AUC decay curves: C4 vs Wikipedia overlay showing near-identical profiles"
      - "Feature importance comparison: highlighting freq_entropy's domain-specific rank shift"
    analysis: >
      Domain ablation 是 universality claim 的 low-hanging fruit supplement。K*=2 holds，
      feature ranking 高度一致（ρ=0.878），domain 对 K* 没有影响。但 orphaned status 意味着
      这个实验可能不会在 EMNLP submission 前完成——如果时间不够，可以将其定位为 "future work:
      systematic domain ablation across web, academic, and code domains"。如果完成，
      放入 Appendix 作为 universality 的额外 data point。

aggregate_median_summary:
  total_new_conditions_tested: 19
  total_new_kstar2: 14
  fraction_kstar2: 0.737
  failure_conditions:
    - "Mistral-7B cross-scorer: architecture-specific low info loss rate + tokenizer mismatch"
    - "Pythia T=0.7: low-temperature channel narrowing reduces measurable degradation space"
    - "128-token length: insufficient sample size for distributional feature estimation"
    - "Cross-scorer matrix: 4/16 cells where marginal generators + architectural distance compound"
  boundary_conditions_unified_by_dpi:
    short_text: "n < 256 tokens → aggregate MI from 15D features below detection threshold"
    low_temperature: "T < 0.9 on small models → pre-narrowed vocabulary reduces generational contrast"
    cross_architecture_scorer: "scorer-generator architectural distance adds ~2pp noise to 1v2 AUC"
  updated_universality_claim: >
    K*=2 is established as a robust discrimination boundary in 14/19 new experimental
    conditions (73.7%). All 5 failure cases are predicted by the DPI framework as
    principled boundary conditions: insufficient text length, low-temperature vocabulary
    narrowing, and cross-architecture scorer noise. Under standard conditions (≥256
    tokens, T≥0.9, compatible scorer), K*=2 holds in 14/14 conditions (100%).
  paper_impact:
    c1_prime_wording: >
      'K*=2 is a robust discrimination boundary under standard conditions, invariant
      across 6 model families (1B-8B), 8 decoding configurations, base and instruct
      variants, and 2 data domains'
    emnlp_viability: "Strong — 14/14 under scoped conditions + principled DPI explanations for boundary cases"
    rebuttal_budget_allocation:
      universality_scope: "40% — preemptively addressed by Boundary Conditions section"
      scale_limitation: "30% — LLaMA-8B confirmation helps but 13B+ gap remains"
      mistral_counterexample: "20% — DPI framework + neural probe precedent (exp-015)"
      dose_response: "10% — appendix supplement"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "304dfd0c-86cb-4550-a427-3947c77a4d8d",
  "isSidechain": false,
  "requestId": "req_011Cb5srACLYDUBrqS4fQmKJ",
  "type": "assistant",
  "uuid": "a078bf89-0c05-4d79-b763-f8ecc622762c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUnUgXZ6LocXV1HEuGpXJw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 44820,
      "output_tokens": 32362,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32362,
          "cache_read_input_tokens": 44820,
          "cache_creation_input_tokens": 311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 311
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃 核心假设：['LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）', '两个新模型…",
  "leafUuid": "a078bf89-0c05-4d79-b763-f8ecc622762c",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 median-tier empirical characterization with universality scoping",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃 核心假设：['LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）', '两个新模型…",
  "leafUuid": "a078bf89-0c05-4d79-b763-f8ecc622762c",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 median-tier empirical characterization with universality scoping",
  "sessionId": "0d5a8c45-5ab9-4dc5-be52-9b903e3787c6"
}
```

---
