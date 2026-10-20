# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/0388255d-dcfe-409f-a64a-33fa9f9076a8.jsonl`
- **Structured JSON:** [`3be4a74bdf2d9e96a755.json`](../../sessions/3b/3be4a74bdf2d9e96a755.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:30:55.234Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:30:55.234Z",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: gen-depth-contamination\n\n## paper_framing.md\n\n# Paper Framing — gen-depth-contamination\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission May 25, 2026)\n- Fallback: EMNLP 2026 Findings\n- Backup: AAAI 2027 (abstract July 25, paper August 1)\n\n## Canonical Experimental Condition\n\n**Continuation mode 是 cross-model 结论的基础。**\n\n> \"We evaluate both generation modes because real-world recursive contamination can arise from either. Our analysis reveals generation mode as a significant confound, leading us to recommend continuation mode as the canonical condition for cross-model comparisons.\"\n\n| Condition | Pythia↔OLMo | Qwen↔others | 论文定位 |\n|-----------|-------------|-------------|---------|\n| Continuation | 90-92% retention | 80-85% retention | **主实验条件** — cross-model claims 的基础 |\n| Rewrite (instruction) | N/A | 61-63% retention | **upper bound with mode-specific confound** — 仅作 ablation |\n\n**原则**：\n- C1' 的跨模型 claim 必须基于 continuation mode 数据\n- Rewrite mode 的高 AUC (0.6957 vs cont 0.6114) 是 mode-specific signal amplification，不能作为泛化性证据\n- mvp-001 (Qwen-rewrite) 定位为 \"pilot study demonstrating feasibility\"，后续用 continuation mode rigorously validate\n- cont→rw 89% vs rw→cont 82% 不对称性 → continuation features 是 rewrite 的通用子集\n\n## Core Claims (2+1 结构, D012)\n\n### Primary: C1' (K* Characterization)\n首次系统测量递归合成文本的 generational discrimination boundary K*，并揭示其 universality。\n\nDPI 理论证明有限 K*_theory 必然存在（信息论 impossibility boundary）；我们首次在受控实验中测量 K*_empirical，它提供 K*_theory 的保守下界。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*_empirical 的行为，发现 K*=2 在所有 10 个测试条件下保持不变，展现出跨模型架构、跨解码策略、跨生成模式、跨模型规模（1B–7B）、跨 instruct/base 的 universality。\n\n**子组件：**\n\n**(a) K*=2 universality across architectures, generation modes, and decoding strategies**\n> **4/4 model-mode configurations 与 4/4 decoding strategies 全部 K*=2：**\n>\n> *Model × mode (exp-007):*\n> | Model | AUC 1v2 | 95% CI | CI lower > 0.60? |\n> |-------|---------|--------|-----------------|\n> | Qwen-rewrite | 0.6955 | [0.6859, 0.7041] | ✅ (+8.6pp) |\n> | Pythia-1.4B | 0.6539 | [0.6454, 0.6630] | ✅ (+4.5pp) |\n> | OLMo-1B | 0.6145 | [0.6045, 0.6247] | ✅ (+0.45pp) |\n> | Qwen-cont | 0.6112 | [0.6015, 0.6213] | ✅ (+0.15pp, 最边缘) |\n>\n> *Decoding strategy invariance (exp-003):*\n> | Decoding | AUC 1v2 | K* |\n> |----------|---------|-----|\n> | greedy | 0.6893 | 2 |\n> | nucleus p=0.9 | 0.6866 | 2 |\n> | temp=0.7 | 0.6887 | 2 |\n> | temp=1.2 | 0.7039 | 2 |\n>\n> - 全部 1v2 CI lower > 0.60, 全部 2v3 CI upper < 0.60, 全部 permutation p < 0.002\n> - 4 decoding strategies 的 AUC 1v2 range [0.6866, 0.7039]，K* 完全不变\n> - K*=2 在所有 10 个测试条件下保持不变（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）\n> - ⚠️ θ-sensitivity: θ=0.60 下 4/4 K*=2；θ=0.70 下仅 Config4-T12 K*=2（1v2=0.7039 仅超 0.70 阈值 0.004），其余 3 config K*=1。论文以 θ=0.60 为主结论，θ=0.70 边界效应作 footnote\n> - ⚠️ 特征排序分化: K* 跨 config 稳定，但特征重要性排序不完全一致——Greedy vs T1.2 Spearman=0.53, p=0.041（Bonferroni 校正后阈值 0.0083，不显著）。论文中措辞应为 \"suggestive\" 而非确定性结论。Config4-T12 正确 top-3 features: hapax_ratio, ttr, surp_skew（非 freq_entropy）\n> - ⚠️ K*=2 边缘性双端注意: Qwen-cont 1v2 CI lower=0.6015（+0.15pp 高于 θ）+ Qwen-rw 2v3 CI upper=0.5991（-0.09pp 低于 θ），K*=2 边界在两端都极边缘。Discussion/Limitations 需同时提及\n> - Paper 可写：\"K*=2 is established as a consistent discrimination boundary across all 8 tested conditions (4 model-mode configurations and 4 decoding strategies; bootstrap 95% CI for AUC₁ᵥ₂ > 0.60; AUC₂ᵥ₃ CI upper < 0.60), suggesting universality beyond the ≤1.5B scale studied.\"\n> - ⚠️ 措辞策略（D017 Reviewer 评估）：分两层——\"established as consistent\" 用确定性语言（8/8 有统计检验支撑），\"suggesting universality beyond\" 对外推 hedging。不升级为 \"establishing universal\"——3 模型 ≤1.5B 会引发审稿人质疑消耗 rebuttal 预算\n> - ⚠️ C1' 子组件定位：呈现为\"对同一 claim 的 4 个 evidence 维度\"而非 4 个独立 finding。§4 标题用 \"K* Characterization\"，每个子节开头显式回答一个 reviewer concern，子节间用 transitional sentences 链接\n\n**(b) Cross-model transfer**\n> - Pythia↔OLMo 90-92% accuracy retention → K*=2 不是 model self-familiarity artifact\n> - 0v1 AUC > 0.96 across all transfer pairs → binary contamination signal 完全跨模型可迁移\n> - 1v2+ transfer 取决于模型族相似度 → 与 K*=2 完美一致（K* 之上分辨力本就微弱）\n> - transfer retention 80-92% suggests depth signal has a large text-intrinsic component（不量化具体比例，因 transfer accuracy retention ≠ 信号分解）\n> - ⚠️ 数值精度：Pythia→OLMo 91.6%, OLMo→Pythia 90.3%，范围 90-92%（非 91-92%）；Qwen-cont↔Pythia 84.7%/85.2%，范围 84-85%（非 83-85%）\n\n**(c) Degradation ordering consistency**\n> - Spearman ρ ≥ 0.85 on single-feature AUC ranking（mode-controlled, continuation）\n> - Top discriminative features shared: surp_d1_std, surp_std, surp_d2_std\n> - Limitation: depth-pair level 一致性在 1v2 处较弱（τ~0.37）\n> - Metric: single-feature AUC ranking（model-free, not LightGBM split count）\n\n**(e) Representation dependence of K* (§4.x Neural Probe / §5.x Discussion)**\n> - exp-015 完整 3 模型结果（frozen self-embeddings + MLP probe, each model probing its own generations）:\n>   - Qwen-cont: K*(neural)=3, 2v3 AUC=0.6159, CI [0.6099, 0.6223], CI lower > 0.60 ✅\n>   - Pythia-1.4B: K*(neural)=2, 2v3 AUC=0.5963, CI [0.5892, 0.6033], CI lower < 0.60 ❌\n>   - OLMo-1B: K*(neural)=2, 2v3 AUC=0.5892, CI [0.5818, 0.5965], CI lower < 0.60 ❌\n> - **K*(neural) 不具备 universality**：仅 Qwen-cont 达到 K*=3，Pythia/OLMo 仍为 K*=2\n> - **Self-familiarity 解释**：每个模型用自己的 frozen embeddings 探测自己生成的文本。Qwen 对 Qwen-generated 文本更敏感（self-familiarity），K*=3 是 model-specific artifact 而非 universal signal\n> - **K*(theory) ≥ 3 弱化**：只能 claim \"K*(theory) ≥ 3 for Qwen representations\"，不能泛化为所有模型\n> - **Interpretability–deployability tradeoff 加强**：15D features 给出 universal K*=2（3/3 模型一致），neural probe 给出 model-dependent K*∈{2,3}。Model-free 方案的 universality 优势在 cross-model 结果下更明显\n> - 所有 3 模型 neural 2v3 AUC > lgbm 2v3 AUC（+3.9pp 到 +5.5pp），说明 learned representations 确实恢复了额外 depth signal，但不足以在所有模型上推过 θ=0.60\n> - 论文定位：**正面发现**——cross-model validation 揭示 K*(neural) 是 representation-dependent，验证了选择 model-free 15D features 作为 headline K* characterization 的正确性\n> - 预防审稿人 \"why bury the stronger result?\"：K*(neural)=3 仅对 Qwen 成立且是 self-familiarity driven，不适合作为 headline result；15D K*=2 的 universality（10/10 conditions + 3/3 models）才是可靠可部署的结论\n\n**(d) Generation mode analysis (§4.x Analysis subsection)**\n> - Signal strength: rewrite AUC 1v2=0.6957 vs continuation 0.6114（Δ=+8.4pp）\n> - Transferability: continuation 80-92% retention vs rewrite 61-63%\n> - Feature subset: cont→rw 89% > rw→cont 82% → continuation features 是 rewrite 的通用子集\n> - Interpretation: rewrite mode 的 instruction-following 引入 mode-specific style artifacts，放大 depth signal 但降低跨模型泛化性\n> - 论文定位：Analysis subsection（\"How does generation mode affect depth estimation?\"），不是独立 claim\n\n### Secondary: C3 (K*-Aware Data Curation Validation)\nK*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit: binary K*-aware filtering (0.5941 MMLU) outperforms graduated depth weighting (best 0.5892 at α=0.9), surprisal-based selection (0.5894), and DSIR distribution matching (~0.5867, ≈ no-filter level). K* serves as an actionable curation guideline — the discrimination boundary directly determines the optimal filtering granularity.\n\n### Supporting Analysis: Canonical Condition Selection\nGeneration mode 是 depth estimation 的显著混淆变量。Methodology 段落阐述 continuation mode 作为 canonical condition 的选择及理由（不作为独立 claim）。\n\n## Story Spine\n\n- **Problem**: Web 数据正被多代递归合成文本污染。当前检测方法将合成文本视为 binary 类别（real vs synthetic），但质量随代际深度非线性退化——首代合成文本与四代合成文本的质量差异巨大却被忽视。\n- **Existing approaches & gaps**: Binary detectors (DivEye, Min-K%++) 不区分代际；model collapse 文献 (Shumailov et al., Alemohammad et al. 2024, Dohmatob et al. 2024) 描述宏观现象但不提供检测工具；data selection methods (DSIR, D4, DoReMi) 做分布匹配但不估计递归深度；Drayson et al. (2025) 将 binary MGT detection 应用于 importance resampling 以防止 model collapse，是目前最接近的工作。然而这些方法均做二值判断，**不估计文本经历了多少轮递归生成，也不量化辨别能力的饱和边界。**\n- **Our framing**: 将递归生成建模为 iterated lossy channel，从信息论（DPI）推导出 K* 的必然存在。K* 是首次系统测量的 operational quantity——它告诉数据策展者\"在什么深度以下，depth-aware curation 比 binary detection 更有价值\"。通过 10 条件实验矩阵（5 model-mode configurations + 4 decoding strategies + 1 cross-scale 7B）系统表征 K*，揭示其 universality：**K*=2 在所有 10 个测试条件下不变**，表明递归生成存在一个与具体模型架构和解码策略无关的 universal discrimination boundary。这一发现为数据治理提供 actionable guidance——depth-aware filtering 在 K* 以内有效，且无需针对不同模型或解码配置分别调优。\n- **Headline result template**: \"Recursive generation has a universal discrimination boundary at K*=2: invariant across 4 model-mode configurations, 4 decoding strategies, and 1 cross-scale probe (10 conditions total, 1B–7B scale, base+instruct), with cross-model transfer retention of 80-92% confirming depth features are largely text-intrinsic. K*=2 correctly predicts that graduated refinement beyond the binary boundary provides no additional benefit — binary filtering at K* (0.5941 MMLU) outperforms all tested alternatives including graduated weighting, surprisal selection, and DSIR.\"\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Universality claim 只基于小模型，能推广到更大模型吗？\"** → exp-004 已将规模扩展至 7B（Qwen2.5-7B, continuation mode, scorer=Qwen2.5-1.5B），K*=2 依然成立，bootstrap 95% CI 确认。结合 4 个 ≤1.5B 架构族（GPT-2 style, Pythia, OLMo, Qwen），K*=2 在 1B–7B 范围内稳定。DPI 理论保证 K*_theory 对任意规模模型存在；进一步扩展至 13B+/70B+ 是重要 future work\n2. **\"只是 feature engineering + off-the-shelf classifier，方法贡献弱\"** → 贡献在 problem formulation + empirical characterization（首次测量 K*）+ 理论框架（DPI）+ universality 发现，不是分类器本身\n3. **\"Prompt-chain 不代表真实世界递归污染\"** → retrain-chain ecological validity check 作为补充；prompt-chain 是 controlled experiment 的标准方法\n4. **\"K*=2 太浅，graduated filtering 收益有限\"** → K*=2 恰好预测了这一结果：binary filtering at K* boundary (0.5941 MMLU) outperforms graduated weighting (best 0.5892), surprisal selection (0.5894), and DSIR (~0.5867). 这验证了 K* 作为 actionable curation guideline 的价值——discrimination boundary 直接决定了最优 filtering 粒度。K* 的 universality 意味着实践者无需为每个模型/解码配置单独标定阈值\n5. **\"同模型做生成和 surprisal 计算有 bias\"** → **exp-013 直接反驳**：Pythia↔OLMo 90-92% accuracy retention，0v1 transfer AUC > 0.96。Depth signal 主要编码在文本而非 model self-familiarity\n6. **\"为什么不用 learned representations\"** → **exp-015 直接回应**：frozen LLM embeddings + MLP probe 达到 K*=3（vs 15D K*=2），揭示 representation-dependent hierarchy: K*_theory ≥ K*_neural ≥ K*_15D。Hand-crafted 15D features 的优势在于 model-free transferability（80-92% cross-model retention）、可解释性（支持 degradation ordering 分析）、实用可部署性。Neural representations 多辨别 1 个深度级别但代价是 model dependence + ~100x 计算开销。这一 tradeoff 证明 15D features 是 practical choice，同时表明 theoretical boundary 延伸至 K*=2 之上\n7. **\"Graduated filtering 没和 data selection methods 比\"** → exp-006 包含 DSIR baseline + α sensitivity sweep\n8. **\"Decoding strategy 只测了 4 种，coverage 不够\"** → 覆盖了实践中最常见的 decoding 配置（greedy, nucleus sampling, temperature scaling high/low）；4/4 完全一致强化 universality claim；extreme decoding（top-k=1 之外的 pathological 配置）留作 future work\n9. **\"为什么不直接用 LLM 做 depth estimation\"** → **exp-011 直接反驳**：GPT-5.5 和 Claude Opus 4.6 在 500 样本 zero-shot 5-class depth 分类上仅 33.1-33.2% accuracy（MAE ~1.1），低于 OBD 15-feature LightGBM 的 38.6%。二者 binary detection 均 ~88%，说明 LLM 能区分 human vs synthetic 但无法估计递归深度。depth estimation 是非平凡任务，需要专用特征工程\n\n## Venue Fit\n\n- EMNLP 2026 special theme 明确呼吁 data contamination, synthetic data feedback loops, data governance 方向的工作\n- 2+1 claim 结构：C1' 是 comprehensive characterization study with universality finding，C3 是 practical application，generation mode analysis 增加深度\n- Universality narrative 比 controllability 更有 impact：从 \"K* depends on X, Y, Z\" 升级为 \"K*=2 is a universal boundary\"，审稿人更容易记住和传播\n- 风险：universality claim 在 ≤1.5B 规模下的外推性是最大攻击面 → 论文中 scope 明确、limitation 诚实、DPI 理论支撑泛化的合理性\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: 'Cross-model depth chain generation: Pythia-1.4B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5. 验证 K* 是否跨模型一致。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_001_pythia_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- id: exp-002\n  claim: 1\n  description: 'Cross-model depth chain generation: OLMo-1B, nucleus p=0.95 T=1.0,\n    C4 5K docs, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_002_olmo_depth\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- id: exp-003\n  claim:\n  - 1\n  - 3\n  description: 'Decoding strategy ablation on Qwen2.5-1.5B: greedy / nucleus p=0.9\n    / T=0.7 / T=1.2, C4 5K docs, depth 0-5. 测试解码策略对 K* 的调控效应。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: exp_003_decoding_ablation\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- id: exp-004\n  claim: 1\n  description: 'Cross-scale probe: Qwen2.5-7B, nucleus p=0.95 T=1.0, C4 5K docs, depth\n    0-5, scorer=Qwen2.5-1.5B. 测试 K* 是否随模型规模变化。（实际参数已从原计划 1K/depth 0-3 扩展以匹配其他实验配置）'\n  priority: P0\n  gpu_budget_hours: 18\n  deps: []\n  registry_id: exp_004_7b_crossscale\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- id: exp-005\n  claim: 2\n  description: 'Feature group ablation + degradation ordering analysis: 对每个模型的 depth\n    chain，按 feature group（surprisal/diversity/tail-thinning）分别计算 pairwise AUC 和饱和深度，绘制\n    degradation ordering heatmap。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_005_degradation\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- id: exp-006\n  claim: 3\n  description: 'Downstream filtering evaluation: 在 Qwen2.5-1.5B depth chain 上比较 no-filter\n    / binary-ours (同 15D 特征 binary classifier) / binary-Drayson (importance resampling)\n    / graduated / surprisal-based / DSIR 六种策略，用 continued pretraining + lm-eval-harness\n    (MMLU, HellaSwag) 评估。5 seeds（paired t-test 报 p-values）。graduated filtering 加 α\n    sensitivity sweep（α ∈ {0.1, 0.3, 0.5, 0.7, 0.9}）。关键对比：binary-ours vs graduated\n    （唯一变量 = binary/ordinal decision，公平验证 C3）。[Dream + Reviewer 行动项]'\n  priority: P0\n  gpu_budget_hours: 72\n  deps: []\n  registry_id: exp_006_graduated_filtering\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- id: exp-007\n  claim:\n  - 1\n  - 2\n  description: 'K* sensitivity + statistical rigor: 在 0.55/0.60/0.65/0.70 四个阈值下计算\n    K*， 展示 K* 对阈值选择的稳健性。加 bootstrap CI for AUC/JSD，permutation-test calibration 为\n    θ=0.60 提供 principled justification。显式报告 3-class accuracy。[Dream 行动项: 加 CI + permutation\n    test + 3-class metrics]'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  registry_id: exp_007_bootstrap_ci\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- id: exp-008\n  claim: 1\n  description: 'Retrain-chain ecological validity: Pythia-1.4B LoRA (rank=16, alpha=32),\n    C4 5K docs, depth 0-4. 对比 prompt-chain 和 retrain-chain 的 K* 和特征分布。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps:\n  - exp-001\n  registry_id: null\n  status: planned\n- id: exp-009\n  claim: 3\n  description: 'Contamination dose-response: 在 10%/30%/50% synthetic injection 比例下测试\n    graduated vs binary filtering 的收益差异。'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - exp-006\n  registry_id: null\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Ordinal vs multinomial vs regression baseline comparison: CORAL vs\n    standard multiclass vs ordinal regression，证明 ordinal structure 的必要性。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  registry_id: exp_010_ordinal_baseline\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- id: exp-011\n  claim: 1\n  description: 'LLM zero-shot depth estimation baseline: GPT-4o / Claude 3.5 对 depth\n    0-4 文本做 zero-shot depth 判断，验证 depth estimation 需要专门方法。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: exp_011_llm_zeroshot\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- id: exp-012\n  claim: 1\n  description: 'Binary detector confidence as depth proxy: 用 DivEye/Binoculars score\n    的 Spearman correlation with true depth，验证 binary confidence ≠ depth。'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp_012_binary_confidence\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: 4×4 transfer matrix（mvp-001 Qwen rewrite + exp-001\n    Pythia cont. + exp-002 OLMo cont. + exp-017 Qwen cont.）。在 model A 训练的 depth classifier\n    在 model B 的 depth chain 上的 transfer accuracy。回答同模型 bias 的根本质疑—— depth signal 是文本固有属性还是\n    model self-familiarity。4 套 features 可区分 generation mode 效应 vs model 效应。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  - exp-002\n  - exp-017\n  registry_id: exp_013_cross_transfer\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- id: exp-014\n  claim: 1\n  description: 'Naturalistic validation: 对 Common Crawl 2025/2026 snapshot 样本做 depth\n    预测，与 AlignScore 和独立 vocabulary richness 指标做 correlation。'\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - exp-005\n  registry_id: null\n  status: planned\n- id: exp-015\n  claim: 1\n  description: 'Learned representation baseline: frozen Qwen2.5-1.5B embeddings +\n    MLP vs hand-crafted 15D features。如果 neural probe 也给 K*=2 → C1'' claim 从 \"our features\n    find K*=2\" 升级为 \"K*=2 is data-intrinsic boundary\"。[D014 升级 P0：Reviewer 评估为最高边际价值实验]'\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: exp_015_neural_probe\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- id: exp-016\n  claim: 1\n  description: 'Base vs Instruct model comparison: Qwen2.5-1.5B base vs Instruct 的\n    K* 和特征分布差异。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_016_base_vs_instruct\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- id: exp-017\n  claim:\n  - 1\n  description: 'Generation mode control: Qwen2.5-1.5B-Instruct continuation mode,\n    C4 5K docs, depth 0-5. 与 mvp-001 (rewrite mode) 对比，分离 generation mode vs model\n    对 K* 的影响。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_017_qwen_continuation\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- id: mvp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MVP pilot saturation study: Qwen2.5-1.5B-Instruct, C4 5K docs, prompt-chain,\n    nucleus p=0.95 T=1.0, depth 0-5.'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: mvp_pilot_sat_v1\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- id: exp-018\n  claim: 1\n  description: 'Cross-family universality: LLaMA-3.1-8B, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 跨模型家族验证 K*。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_018_llama8b_depth\n  status: RUNNING\n  conclusion: null\n- id: exp-019\n  claim: 1\n  description: 'Cross-family universality: Mistral-7B-v0.3, continuation mode, nucleus\n    p=0.95 T=1.0, C4 5K docs, depth 0-5, scorer=Qwen2.5-1.5B.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_019_mistral7b_depth\n  status: RUNNING\n  conclusion: null\n- id: exp-020\n  claim:\n  - 1\n  - 3\n  description: 'Pythia-1.4B decoding ablation: greedy / nucleus p=0.9 / T=0.7 / T=1.2,\n    C4 5K docs, depth 0-5. 跨模型验证解码策略对 K* 的不变性。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: exp_020_pythia_decoding\n  status: RUNNING\n- id: exp-021\n  claim: 1\n  description: 'Text length ablation: Qwen2.5-1.5B-Instruct continuation, 128/256/512\n    tokens, C4 5K docs, depth 0-5. 验证 K* 对文本长度的敏感性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_021_length_ablation\n  status: RUNNING\n- id: exp-022\n  claim:\n  - 1\n  - 2\n  description: '4x4 cross-scorer matrix: 4 generators × 4 scorers, 验证 scorer independence\n    完整性。'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-021\n  registry_id: exp_022_cross_scorer_matrix\n  status: QUEUED\n- id: exp-023\n  claim:\n  - 1\n  description: 'Domain ablation: Wikipedia seed data, Qwen2.5-1.5B (base) continuation\n    mode, nucleus p=0.95 T=1.0, 5K docs, depth 0-5, scorer=Qwen2.5-1.5B. 验证 K*=2 是否跨数据域一致（C4\n    vs Wikipedia）。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: exp_023_domain_ablation\n  status: orphaned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_pilot_sat_v1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9956\n      1v2: 0.6957\n      2v3: 0.5893\n      3v4: 0.5434\n      4v5: 0.5343\n    pairwise_auc_std:\n      0v1: 0.0005\n      1v2: 0.0072\n      2v3: 0.012\n      3v4: 0.0053\n      4v5: 0.0091\n    pairwise_jsd:\n      0v1: 0.2669\n      1v2: 0.0163\n      2v3: 0.0069\n      3v4: 0.0047\n      4v5: 0.0041\n    k_star: 2\n    ordinal_mae: 1.0163\n    ordinal_accuracy: 0.4182\n- exp_id: exp_001_pythia_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pairwise_auc:\n      0v1: 0.9932\n      1v2: 0.6539\n      2v3: 0.5515\n      3v4: 0.5153\n      4v5: 0.5135\n    pairwise_auc_std:\n      0v1: 0.0007\n      1v2: 0.0069\n      2v3: 0.0137\n      3v4: 0.0084\n      4v5: 0.0078\n    pairwise_jsd:\n      0v1: 0.2142\n      1v2: 0.014\n      2v3: 0.0051\n      3v4: 0.0033\n      4v5: 0.0031\n    k_star: 2\n    ordinal_mae: 1.14\n    ordinal_accuracy: 0.383\n- exp_id: exp_002_olmo_depth\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.997\n      1v2: 0.6146\n      2v3: 0.5497\n      3v4: 0.509\n      4v5: 0.5044\n    pairwise_auc_std:\n      0v1: 0.0004\n      1v2: 0.0029\n      2v3: 0.004\n      3v4: 0.0084\n      4v5: 0.0136\n    pairwise_jsd:\n      0v1: 0.23941\n      1v2: 0.012972\n      2v3: 0.00735\n      3v4: 0.003968\n      4v5: 0.003851\n    ordinal_mae: 1.1813\n    ordinal_accuracy: 0.3685\n    top_features:\n    - surp_d1_mean\n    - surp_d1_skew\n    - freq_kurtosis\n    - surp_d2_mean\n    - surp_mean\n- exp_id: exp_003_decoding_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K_star: 2\n    K_star_robust: true\n    bootstrap_ci:\n      config1_greedy:\n        0v1:\n          auc: 0.9796\n          ci:\n          - 0.9772\n          - 0.982\n          perm_p: 0\n        1v2:\n          auc: 0.6892\n          ci:\n          - 0.6802\n          - 0.6982\n          perm_p: 0\n        2v3:\n          auc: 0.5612\n          ci:\n          - 0.5517\n          - 0.5705\n          perm_p: 0\n        3v4:\n          auc: 0.5405\n          ci:\n          - 0.5308\n          - 0.5502\n          perm_p: 0\n        4v5:\n          auc: 0.5137\n          ci:\n          - 0.5033\n          - 0.5238\n          perm_p: 0.0082\n      config2_nuc09:\n        0v1:\n          auc: 0.9945\n          ci:\n          - 0.9934\n          - 0.9956\n          perm_p: 0\n        1v2:\n          auc: 0.6862\n          ci:\n          - 0.6774\n          - 0.6951\n          perm_p: 0\n        2v3:\n          auc: 0.5917\n          ci:\n          - 0.5824\n          - 0.601\n          perm_p: 0\n          note: CI upper crosses theta=0.60\n        3v4:\n          auc: 0.5468\n          ci:\n          - 0.5369\n          - 0.5568\n          perm_p: 0\n        4v5:\n          auc: 0.5066\n          ci:\n          - 0.4959\n          - 0.5173\n          perm_p: 0.1199\n      config3_t07:\n        0v1:\n          auc: 0.9877\n          ci:\n          - 0.9857\n          - 0.9896\n          perm_p: 0\n        1v2:\n          auc: 0.6885\n          ci:\n          - 0.6797\n          - 0.697\n          perm_p: 0\n        2v3:\n          auc: 0.5901\n          ci:\n          - 0.5806\n          - 0.5996\n          perm_p: 0\n        3v4:\n          auc: 0.539\n          ci:\n          - 0.5288\n          - 0.5493\n          perm_p: 0\n        4v5:\n          auc: 0.5348\n          ci:\n          - 0.5243\n          - 0.5454\n          perm_p: 0\n      config4_t12:\n        0v1:\n          auc: 0.9982\n          ci:\n          - 0.9975\n          - 0.9987\n          perm_p: 0\n        1v2:\n          auc: 0.7037\n          ci:\n          - 0.6945\n          - 0.7126\n          perm_p: 0\n        2v3:\n          auc: 0.582\n          ci:\n          - 0.5722\n          - 0.5917\n          perm_p: 0\n        3v4:\n          auc: 0.5293\n          ci:\n          - 0.5185\n          - 0.5399\n          perm_p: 0\n        4v5:\n          auc: 0.5237\n          ci:\n          - 0.5132\n          - 0.5347\n          perm_p: 0.0001\n      resamples: 10000\n      method: GroupKFold(5) OOF + doc-level bootstrap + label permutation\n- exp_id: exp_017_qwen_continuation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9972\n      1v2: 0.6114\n      2v3: 0.5609\n      3v4: 0.5408\n      4v5: 0.5139\n    pairwise_jsd:\n      0v1: 0.28627\n      1v2: 0.005107\n      2v3: 0.003603\n      3v4: 0.003395\n      4v5: 0.003085\n    ordinal_mae: 1.1547\n    ordinal_accuracy: 0.3819\n    top3_features:\n    - freq_entropy\n    - surp_mean\n    - surp_std\n- exp_id: exp_013_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy_matrix:\n      Qwen_rw→Qwen_rw: 0.4229\n      Qwen_rw→Pythia: 0.259\n      Qwen_rw→OLMo: 0.2653\n      Qwen_rw→Qwen_cont: 0.3466\n      Pythia→Qwen_rw: 0.2718\n      Pythia→Pythia: 0.3856\n      Pythia→OLMo: 0.3531\n      Pythia→Qwen_cont: 0.3287\n      OLMo→Qwen_rw: 0.2768\n      OLMo→Pythia: 0.345\n      OLMo→OLMo: 0.3822\n      OLMo→Qwen_cont: 0.3244\n      Qwen_cont→Qwen_rw: 0.344\n      Qwen_cont→Pythia: 0.3284\n      Qwen_cont→OLMo: 0.3112\n      Qwen_cont→Qwen_cont: 0.3875\n    transfer_retention_accuracy:\n      Pythia↔OLMo: 91-92%\n      Qwen_rw→Pythia/OLMo: 61-63%\n      Qwen_cont↔Pythia: 83-85%\n      Qwen_cont↔OLMo: 80-85%\n    transfer_retention_tau:\n      Pythia↔OLMo: 85-86%\n      Qwen_rw→Pythia/OLMo: 45-50%\n      Qwen_cont↔others: 68-83%\n    mean_pw_auc_matrix:\n      within_avg: 0.6099\n      cross_avg: 0.5905\n      0v1_cross_all_above: 0.96\n    key_finding: depth signal ≈ 70-85% text-intrinsic + 15-30% model self-familiarity.\n      Binary contamination detection (0v1) highly transferable (>0.96 AUC). Fine-grained\n      depth transfer depends on model family similarity. Qwen-rewrite overfits style\n      features; Qwen-cont transfers much better.\n- exp_id: exp_005_degradation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_model_kendall_tau_by_first_auc:\n      Pythia_vs_OLMo: 0.733\n      Pythia_vs_Qwen_rewrite: 0.467\n      Pythia_vs_Qwen_cont: 0.695\n      OLMo_vs_Qwen_rewrite: 0.429\n      OLMo_vs_Qwen_cont: 0.543\n      Qwen_rewrite_vs_Qwen_cont: 0.733\n    cross_model_kendall_tau_by_avg_auc:\n      Pythia_vs_OLMo: 0.8476\n      Pythia_vs_Qwen_cont: 0.7524\n      OLMo_vs_Qwen_cont: 0.6762\n    cross_model_spearman_rho_single_feature_auc:\n      Pythia_vs_OLMo: 0.95\n      Pythia_vs_Qwen_cont: 0.9143\n      OLMo_vs_Qwen_cont: 0.85\n      metric_definition: Spearman ρ on per-feature AUC rankings (each feature independently\n        classifies depth pairs)\n    4model_tau_mean_continuation_by_first_auc: 0.657\n    4model_tau_mean_all_by_first_auc: 0.6\n    generation_mode_delta:\n      Pythia_vs_Qwen: '+0.228'\n      OLMo_vs_Qwen: '+0.114'\n    top3_features_ranking_by_first_auc:\n      Pythia:\n      - surp_d1_std\n      - surp_d2_std\n      - surp_std\n      OLMo:\n      - surp_std\n      - surp_d1_std\n      - surp_d2_std\n      Qwen_rewrite:\n      - freq_entropy\n      - surp_std\n      - surp_d1_std\n      Qwen_cont:\n      - surp_d1_std\n      - surp_std\n      - surp_d2_std\n    shared_top_discriminators: surp_d1_std, surp_std, surp_d2_std shared across all\n      architectures (single-feature AUC ranking)\n    degradation_ordering_consistency: Strong cross-model consistency (ρ≥0.85) on single-feature\n      AUC ranking under controlled generation mode.\n    residual_architecture_effect: Qwen-cont vs OLMo (τ=0.54 by_first_auc) still lower\n      than Pythia vs OLMo (τ=0.73), ~30-40% of ordering divergence from architecture\n    limitation_1v2_weakness: depth-pair level consistency weakest at 1v2 (τ~0.37),\n      near-generational feature importance ordering varies more across models\n- exp_id: exp_007_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      0v1:\n        auc: 0.9956\n        ci_lower: 0.9946\n        ci_upper: 0.9965\n        perm_p: 0.002\n      1v2:\n        auc: 0.6955\n        ci_lower: 0.6859\n        ci_upper: 0.7041\n        perm_p: 0.002\n      2v3:\n        auc: 0.5893\n        ci_lower: 0.5795\n        ci_upper: 0.5991\n        perm_p: 0.002\n      3v4:\n        auc: 0.5435\n        ci_lower: 0.5333\n        ci_upper: 0.5551\n        perm_p: 0.002\n      4v5:\n        auc: 0.534\n        ci_lower: 0.5238\n        ci_upper: 0.5448\n        perm_p: 0.002\n    pythia_cont:\n      0v1:\n        auc: 0.9932\n        ci_lower: 0.9921\n        ci_upper: 0.9943\n        perm_p: 0.002\n      1v2:\n        auc: 0.6539\n        ci_lower: 0.6454\n        ci_upper: 0.663\n        perm_p: 0.002\n      2v3:\n        auc: 0.5514\n        ci_lower: 0.5417\n        ci_upper: 0.5628\n        perm_p: 0.002\n      3v4:\n        auc: 0.5152\n        ci_lower: 0.5041\n        ci_upper: 0.526\n        perm_p: 0.006\n      4v5:\n        auc: 0.5136\n        ci_lower: 0.5021\n        ci_upper: 0.5249\n        perm_p: 0.008\n    olmo_cont:\n      0v1:\n        auc: 0.997\n        ci_lower: 0.9964\n        ci_upper: 0.9975\n        perm_p: 0.002\n      1v2:\n        auc: 0.6145\n        ci_lower: 0.6045\n        ci_upper: 0.6247\n        perm_p: 0.002\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5399\n        ci_upper: 0.5596\n        perm_p: 0.002\n      3v4:\n        auc: 0.5091\n        ci_lower: 0.4973\n        ci_upper: 0.52\n        perm_p: 0.064\n      4v5:\n        auc: 0.5045\n        ci_lower: 0.4932\n        ci_upper: 0.515\n        perm_p: 0.232\n    qwen_cont:\n      0v1:\n        auc: 0.9971\n        ci_lower: 0.9963\n        ci_upper: 0.9978\n        perm_p: 0.002\n      1v2:\n        auc: 0.6112\n        ci_lower: 0.6015\n        ci_upper: 0.6213\n        perm_p: 0.002\n      2v3:\n        auc: 0.5609\n        ci_lower: 0.5511\n        ci_upper: 0.5712\n        perm_p: 0.002\n      3v4:\n        auc: 0.5409\n        ci_lower: 0.5308\n        ci_upper: 0.5508\n        perm_p: 0.002\n      4v5:\n        auc: 0.5141\n        ci_lower: 0.5035\n        ci_upper: 0.5255\n        perm_p: 0.006\n    k_star_robust: true\n    all_1v2_ci_lower_above_060: true\n    most_marginal: Qwen-cont CI lower=0.6015, only 0.0015 above threshold\n- exp_id: exp_010_ordinal_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_rewrite:\n      obd_lgbm:\n        accuracy: 0.4229\n        mae: 0.9836\n        tau_b: 0.5518\n        mean_pw_auc: 0.6214\n      multiclass_lgbm:\n        accuracy: 0.4182\n        mae: 1.0163\n        tau_b: 0.5367\n        mean_pw_auc: 0.6246\n      ordinal_logreg:\n        accuracy: 0.3636\n        mae: 0.9105\n        tau_b: 0.563\n        mean_pw_auc: 0.5022\n    pythia:\n      obd_lgbm:\n        accuracy: 0.3856\n        mae: 1.1072\n        tau_b: 0.4745\n        mean_pw_auc: 0.6055\n      multiclass_lgbm:\n        accuracy: 0.3832\n        mae: 1.1399\n        tau_b: 0.4622\n        mean_pw_auc: 0.6062\n      ordinal_logreg:\n        accuracy: 0.3179\n        mae: 1.022\n        tau_b: 0.49\n        mean_pw_auc: 0.4767\n    olmo:\n      obd_lgbm:\n        accuracy: 0.3822\n        mae: 1.1469\n        tau_b: 0.4683\n        mean_pw_auc: 0.6015\n      multiclass_lgbm:\n        accuracy: 0.3685\n        mae: 1.1813\n        tau_b: 0.4497\n        mean_pw_auc: 0.5974\n      ordinal_logreg:\n        accuracy: 0.3265\n        mae: 1.0352\n        tau_b: 0.4656\n        mean_pw_auc: 0.4859\n- exp_id: exp_011_llm_zeroshot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gpt55_5class_acc: 0.332\n    gpt55_mae: 1.102\n    gpt55_spearman: 0.383\n    gpt55_binary_acc: 0.878\n    claude_5class_acc: 0.331\n    claude_mae: 1.15\n    claude_spearman: 0.416\n    claude_binary_acc: 0.882\n    odb_baseline_5class_acc: 0.386\n    odb_baseline_mae: 1.107\n    gpt55_per_depth_acc:\n      depth_0: 0.77\n      depth_1: 0.19\n      depth_2: 0.38\n      depth_3: 0.24\n      depth_4: 0.08\n    claude_per_depth_acc:\n      depth_0: 0.69\n      depth_1: 0.21\n      depth_2: 0.28\n      depth_3: 0.101\n      depth_4: 0.37\n    n_samples_per_model: 500\n    key_finding: Both frontier LLMs (GPT-5.5, Claude Opus 4.6) perform WORSE than\n      OBD-LightGBM on 5-class depth estimation (~33% vs 38.6% acc). Binary human/AI\n      detection is high (~88%) but fine-grained depth discrimination fails.\n- exp_id: exp_015_neural_probe\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3892\n      pairwise_auc:\n        0v1: 0.966\n        1v2: 0.676\n        2v3: 0.596\n        3v4: 0.555\n        4v5: 0.532\n    olmo:\n      k_star_neural: 2\n      k_star_lgbm: 2\n      accuracy: 0.3729\n      pairwise_auc:\n        0v1: 0.95\n        1v2: 0.657\n        2v3: 0.589\n        3v4: 0.547\n        4v5: 0.53\n    qwen_cont:\n      k_star_neural: 3\n      k_star_lgbm: 2\n      accuracy: 0.4368\n      pairwise_auc:\n        0v1: 0.988\n        1v2: 0.702\n        2v3: 0.616\n        3v4: 0.59\n        4v5: 0.566\n    key_finding: Neural probe K*_neural=2 for Pythia and OLMo (same as 15D), K*_neural=3\n      only for Qwen-cont (self-scorer). 2v3 AUC improved in all models vs LightGBM\n      but only Qwen-cont crosses θ=0.60. K*=2 is robust for cross-model probes.\n- exp_id: exp_006_graduated_filtering\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_runs: 51\n    binary_ours:\n      mmlu: 0.5941±0.0008\n      hellaswag: 0.6701±0.0006\n    binary_drayson:\n      mmlu: 0.5913±0.0009\n      hellaswag: 0.6691±0.0004\n    surprisal:\n      mmlu: 0.5894±0.0009\n      hellaswag: 0.6641±0.0006\n    graduated_a09:\n      mmlu: 0.5892±0.0008\n      hellaswag: 0.6701±0.0007\n    graduated_a07:\n      mmlu: 0.5892±0.0014\n      hellaswag: 0.6695±0.0004\n    graduated_a05:\n      mmlu: 0.5880±0.0013\n      hellaswag: 0.6687±0.0008\n    graduated_a03:\n      mmlu: 0.5877±0.0013\n      hellaswag: 0.6669±0.0005\n    graduated_a01:\n      mmlu: 0.5873±0.0019\n      hellaswag: 0.6640±0.0009\n    dsir:\n      mmlu: 0.5869±0.0003\n      hellaswag: 0.6631±0.0007\n    no_filter:\n      mmlu: 0.5865±0.0010\n      hellaswag: 0.6638±0.0008\n    base_model:\n      mmlu: '0.6018'\n      hellaswag: '0.6821'\n    best_strategy: binary-ours\n    key_finding: binary-ours is best filtering strategy. All strategies degrade vs\n      base_model. Graduated α monotonically increasing confirms K*=2 boundary. DSIR\n      below all other strategies except no-filter.\n- exp_id: exp_004_7b_crossscale\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.9644\n      1v2: 0.6178\n      2v3: 0.546\n      3v4: 0.5225\n      4v5: 0.5091\n    pairwise_auc_std:\n      0v1: 0.0034\n      1v2: 0.0081\n      2v3: 0.0028\n      3v4: 0.0113\n      4v5: 0.0052\n    bootstrap_ci:\n      0v1:\n        auc: 0.9638\n        ci_lower: 0.9607\n        ci_upper: 0.9665\n        perm_p: 0.0001\n      1v2:\n        auc: 0.6168\n        ci_lower: 0.6079\n        ci_upper: 0.6261\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5492\n        ci_lower: 0.5388\n        ci_upper: 0.5594\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5276\n        ci_lower: 0.517\n        ci_upper: 0.5375\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5085\n        ci_lower: 0.4988\n        ci_upper: 0.5191\n        perm_p: 0.0676\n    bootstrap_resamples: 1000\n    permutation_resamples: 10000\n    pairwise_jsd:\n      0v1: 0.127422\n      1v2: 0.010114\n      2v3: 0.004798\n      3v4: 0.004821\n      4v5: 0.003335\n    ordinal_mae: 1.2156\n    ordinal_accuracy: 0.3523\n    top_features:\n    - freq_entropy\n    - surp_d1_skew\n    - surp_std\n    - surp_d1_mean\n    - surp_mean\n    key_finding: K*=2 confirmed at 7B scale with bootstrap CI. 1v2 CI lower=0.6079>0.60\n      (robust). 2v3 CI upper=0.5594<0.60. 4v5 only non-significant pair (p=0.0676).\n      FR-4 Warning resolved.\n- exp_id: exp_A_alt_scorer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pythia_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9923\n      auc_1v2: 0.7012\n      auc_2v3: 0.587\n      mae: 1.006\n      accuracy: 0.417\n      spearman_rho_vs_baseline: 0.906\n    pythia_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.99\n      auc_1v2: 0.5923\n      auc_2v3: null\n      mae: 1.216\n      accuracy: 0.371\n      spearman_rho_vs_baseline: 0.942\n    olmo_qwen_rw:\n      k_star: 2\n      auc_0v1: 0.9918\n      auc_1v2: 0.6947\n      auc_2v3: null\n      mae: 1.016\n      accuracy: 0.413\n      spearman_rho_vs_baseline: 0.92\n    olmo_qwen_cont:\n      k_star: 1\n      auc_0v1: 0.989\n      auc_1v2: 0.5858\n      auc_2v3: null\n      mae: 1.229\n      accuracy: 0.368\n      spearman_rho_vs_baseline: 0.902\n    key_finding: 'K* splits by generator data, not scorer: Qwen-RW→K*=2, Qwen-cont→K*=1\n      (cross-scorer). Feature importance ρ≥0.90 across all 4 conditions confirms scorer\n      independence of feature ranking.'\n- exp_id: exp_B_14d_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    result: K*=2 stable across all 4 models after removing self_BLEU (14D)\n    key_finding: self_BLEU removal does not change K* boundary. FR-3 resolved.\n- exp_id: exp_C_permutation_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    resamples: 10000\n    all_boundary_pairs_p: <0.0001\n    key_finding: 10K permutation confirms all boundary p-values well below 0.01. FR-11\n      resolved.\n- exp_id: exp_D_obd_n500\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    obd_accuracy_final: 0.38\n    obd_ci:\n    - 0.34\n    - 0.422\n    mcnemar_vs_gpt55_p: 0.0809\n    mcnemar_vs_claude_p: 0.0693\n    mcnemar_significant: false\n    multi_seed_std: 0\n    per_depth:\n      d0: 0.96\n      d1: 0.39\n      d2: 0.14\n      d3: 0.19\n      d4: 0.22\n    prob_merge_accuracy: 0.444\n    prob_merge_d4_bias: 0.8\n    note: v2 logic (6-class argmax, no capping/merge) + seed=42. McNemar not significant\n      — supports discussion.tex narrative\n- exp_id: exp_E_paired_stats\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu_significant_pairs: 8/15\n    hellaswag_significant_pairs: 9/15\n    binary_ours_vs_all_mmlu: all significant\n    max_cohen_d_mmlu: 10.8\n    max_cohen_d_hellaswag: 8.98\n    graduated_a09_vs_dsir_corrected_p: 0.0523\n    cohen_d_method: d_av (Lakens 2013)\n    key_finding: 'binary-ours significantly outperforms all alternatives on MMLU.\n      On HellaSwag, binary-ours and graduated_a0.9 tied (p=1.0). FR-5 resolved. Holm-Bonferroni\n      cummax bug fixed: MMLU 10/15→8/15. Cohen''s d changed to d_av.'\n    bugfix_note: Holm-Bonferroni cummax variable was never updated, causing 2 MMLU\n      pairs to be incorrectly marked significant (graduated_a0.9 vs no-filter, surprisal\n      vs dsir). Cohen's d changed from d_z to d_av (Lakens 2013).\n- exp_id: exp_012_binary_confidence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_samples: 500\n    generators:\n    - qwen-rewrite\n    - pythia-1.4b\n    - olmo-1b\n    - qwen-cont\n    6class_accuracy:\n      qwen-rewrite: 0.1987\n      pythia-1.4b: 0.1303\n      olmo-1b: 0.127\n      qwen-cont: 0.1833\n      random_baseline: 0.1667\n    spearman_rho:\n      qwen-rewrite:\n        log_ppl_ref: -0.1233\n        log_ppl_obs: 0.0815\n        ppl_ratio: 0.1185\n      pythia-1.4b:\n        log_ppl_ref: -0.2972\n        log_ppl_obs: -0.4529\n        ppl_ratio: -0.392\n      olmo-1b:\n        log_ppl_ref: -0.378\n        log_ppl_obs: -0.4614\n        ppl_ratio: -0.4068\n      qwen-cont:\n        log_ppl_ref: -0.3887\n        log_ppl_obs: -0.162\n        ppl_ratio: -0.058\n    binary_detector_kstar: 1\n    obd_kstar: 2\n    auc_non_monotonic: true\n    key_finding: Binary detectors (DivEye/Binoculars) K*≈1 vs OBD K*=2. 6-class accuracy\n      ≤0.199 (random=0.167). Spearman |ρ|=0.06-0.46 (statistically significant but\n      practically weak). AUC non-monotonic — binary detectors cannot maintain depth\n      ordering. Confirms binary confidence ≠ depth estimation.\n- exp_id: exp_kstar_theta\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    output_files:\n    - kstar_theta_curve.pdf (32KB)\n    - kstar_theta_curve.png (335KB)\n    models:\n    - Qwen-rewrite\n    - Pythia\n    - OLMo\n    - Qwen-cont\n    depth_pairs: 5\n    key_finding: All 4 models show AUC ≥0.993 at 0v1, decaying to ~0.50-0.53 at 4v5.\n      θ=0.60 is justified as natural K*=2 boundary across all models. FR-1 Critical\n      resolved.\n- exp_id: exp_016_base_vs_instruct\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    k_star: 2\n    pairwise_auc:\n      0v1: 0.987\n      1v2: 0.6262\n      2v3: 0.5496\n      3v4: 0.5294\n      4v5: 0.5182\n    pairwise_auc_std:\n      0v1: 0.0015\n      1v2: 0.0152\n      2v3: 0.0067\n      3v4: 0.0132\n      4v5: 0.0139\n    pairwise_jsd:\n      0v1: 0.163726\n      1v2: 0.01081\n      2v3: 0.005311\n      3v4: 0.003942\n      4v5: 0.003522\n    ordinal_mae: 1.1691\n    ordinal_accuracy: 0.3719\n    top_features:\n    - freq_entropy\n    - surp_std\n    - surp_d1_skew\n    - surp_d1_mean\n    - surp_mean\n    n_samples: 30000\n    bootstrap_ci:\n      0v1:\n        auc: 0.987\n        ci_lower: 0.9853\n        ci_upper: 0.9885\n        perm_p: 0.0001\n      1v2:\n        auc: 0.626\n        ci_lower: 0.6168\n        ci_upper: 0.6353\n        perm_p: 0.0001\n      2v3:\n        auc: 0.5496\n        ci_lower: 0.5397\n        ci_upper: 0.56\n        perm_p: 0.0001\n      3v4:\n        auc: 0.5293\n        ci_lower: 0.5188\n        ci_upper: 0.5399\n        perm_p: 0.0001\n      4v5:\n        auc: 0.5181\n        ci_lower: 0.5075\n        ci_upper: 0.5288\n        perm_p: 0.0016\n    bootstrap_resamples: 10000\n    permutation_resamples: 10000\n    key_finding: K*=2 for base model confirmed with bootstrap CI. 1v2 AUC=0.626, 95%\n      CI=[0.6168, 0.6353], CI lower=0.6168 > θ=0.60 (PASS). All pairs significant\n      (p≤0.0016). Fold 0 1v2=0.5963 is an outlier but aggregate CI robustly above\n      threshold. Base 1v2 CI [0.6168, 0.6353] overlaps with Instruct 1v2 CI [0.6015,\n      0.6213] — no significant base-vs-instruct difference.\n- exp_id: exp_018_llama8b_depth\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: exp_019_mistral7b_depth\n  name: ''\n  status: RUNNING\n  conclusion: null\n  metrics: {}\n- exp_id: exp_020_pythia_decoding\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_021_length_ablation\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_022_cross_scorer_matrix\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:30:55.237Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:30:55.237Z",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-16T07:30:55.259Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0d85ab7c-092a-4dea-b746-9e04462e4353",
  "type": "user",
  "uuid": "8b99d697-26dc-4215-8279-7a7aece90dc0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:30:55.257Z_

```json
{
  "parentUuid": "8b99d697-26dc-4215-8279-7a7aece90dc0",
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
  "uuid": "9a47b20e-dc42-4422-9503-dbcb953d13f6",
  "timestamp": "2026-05-16T07:30:55.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:30:55.257Z_

```json
{
  "parentUuid": "9a47b20e-dc42-4422-9503-dbcb953d13f6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7df9a32d-fcd7-47da-b7c3-abe8d37d3629",
  "timestamp": "2026-05-16T07:30:55.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "7df9a32d-fcd7-47da-b7c3-abe8d37d3629",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define Dream simulation scenarios for gen-depth-contamination",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8"
}
```

---

### Assistant

_source line 8 · 2026-05-16T07:31:39.792Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research project carefully to define three tiers for the Dream simulation.

Key facts about the current state:
- Core claim: K*=2 universality across models, decoding strategies, scales
- Already completed: 10 conditions showing K*=2 (5 model-mode + 4 decoding + 1 cross-scale 7B)
- Running experiments: exp-018 (LLaMA-8B), exp-019 (Mistral-7B), exp-020 (Pythia decoding), exp-021 (length ablation)


- Queued: exp-022 (cross-scorer matrix)

The most marginal result so far is Qwen-cont with a CI lower bound of 0.6015, barely above the θ=0.60 threshold. C3 downstream filtering is already validated, and cross-model transfer shows strong retention at 80-92% in continuation mode. I'm targeting EMNLP 2026 Main with an ARR deadline of May 25, 2026.

The running experiments are crucial for solidifying the universality claim—LLaMA-8B and Mistral-7B will add new model families beyond what I currently have (GPT-2-style, Pythia, OLMo, Qwen), and the Pythia decoding results will further test whether K*=2 holds across different sampling strategies.

I'm also running length ablations to check robustness across text lengths and a cross-scorer matrix to see if the scoring function introduces dependencies. The main risks are that LLaMA or Mistral might deviate from K*=2, length could matter more than expected, or the scorer itself could be driving the results—especially given that Qwen-cont already showed K*=1 for some generators in earlier work. The best case is that everything confirms K*=2 universally, expanding the claim from 10 conditions to a much broader set.

In the median scenario, some new models might show K*=2 but with tighter confidence intervals, or one might edge toward K*=1, which would still support the universality claim but with caveats. The worst case is that LLaMA and Mistral break the pattern entirely, forcing a reframe from "universal K*" to something more architecture-dependent, or revealing that the scorer is the real driver of variation.

Now I'm working through the specific metrics for each scenario—looking at what AUC ranges and confidence intervals would constitute success versus marginal results across the different model families and sequence lengths.

For the median case, most conditions point to K*=2, though LLaMA-8B sits right at the boundary and Mistral-7B could go either way depending on how I interpret the evidence. The Pythia results are mixed, with most decoding strategies supporting K*=2 but one being borderline, and sequence length matters too—256 and 512 tokens favor K*=2 while 128 tokens suggest K*=1. I need to be careful about how I frame this claim, acknowledging that K*=2 holds under standard generation conditions but with important caveats.

The worst-case scenario reveals something more fundamental: when I look at LLaMA-8B and Mistral-7B together, they diverge significantly, with both showing K*=1 and AUC values that drop below 0.60. This breaks the universality assumption I was hoping for. Either K* is actually a function of the model family itself, or the scorer being used matters more than I thought—I already saw evidence of this with the Qwen-cont scorer in an earlier experiment. So I need to reframe the finding as K* being in {1,2} with predictable factors determining which, rather than claiming a single universal value.

The cross-scorer dependency is a real concern. When Qwen-cont features score Pythia or OLMo generations, K* drops to 1, which I've already documented. My current framing sidesteps this by using self-scoring or the original scorer and calling continuation mode features canonical, but if the cross-scorer matrix confirms this pattern is widespread, that undermines any universality claim. The worst case would be if LLaMA and Mistral both show K*=1 with weak 1v2 signals, combined with the length ablation showing 128-token sequences also favor K*=1—that would suggest K* is genuinely model and context dependent rather than universal.

But I need to recalibrate what "worst" actually means here. The paper already has 10 solid conditions across 4 model families showing K*=2. The real question is whether new experiments break the universality narrative or just refine it. Even if LLaMA and Mistral disappoint, I still have strong coverage at smaller scales plus Qwen at 7B. The gap I was trying to fill was whether the pattern holds at the 7-8B range with different architectures, but that's a refinement question, not a fundamental threat to what's already established.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7df9a32d-fcd7-47da-b7c3-abe8d37d3629",
  "isSidechain": false,
  "requestId": "req_011Cb5re8cdwS9J3ehvgoapv",
  "type": "assistant",
  "uuid": "c5eeff16-afcc-48bb-acda-915682ef17ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qg6NRaTbBLESqtQ75UuhR4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32601
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

_source line 9 · 2026-05-16T07:32:16.516Z_

```yaml
tiers:
  best:
    meaning: "所有 RUNNING 实验确认 K*=2，universality 从 10 条件扩展到 16+ 条件、6 模型族、1B-8B"
    key_assumptions:
      - LLaMA-8B 和 Mistral-7B 均 K*=2（1v2 CI lower > 0.60）
      - Pythia decoding ablation 4/4 K*=2，跨模型解码不变性成立
      - Length ablation 3/3 lengths (128/256/512) K*=2
      - Cross-scorer matrix 不引入新的 scorer-dependent K* 降级
    number_ranges:
      llama8b_1v2_auc: [0.615, 0.655]
      mistral7b_1v2_auc: [0.610, 0.645]
      pythia_decoding_1v2_range: [0.640, 0.680]
      length_128_1v2_auc: [0.605, 0.635]
      total_conditions_kstar2: [16, 18]
      cross_scorer_kstar2_fraction: [0.85, 1.0]
    narrative_direction: "K*=2 universality 从 '10 conditions, 4 families, 1B-7B' 升级为 '16+ conditions, 6 families, 1B-8B'。C1' 措辞从 'suggesting universality beyond ≤1.5B' 升级为 'demonstrating universality across 6 architecture families at 1B-8B scale'。Reviewer concern #1（小模型外推）被直接数据消解，rebuttal 预算释放给其他攻击面。EMNLP Main 高置信。"

  median:
    meaning: "新模型族结果混合——一个确认、一个边缘或失败；辅助实验部分成功。universality claim 需 scope 但不崩溃"
    key_assumptions:
      - LLaMA-8B K*=2 但边缘（CI lower 0.600-0.607），或 Mistral K*=1（1v2 AUC 0.58-0.60）
      - 两个新模型族中至少一个确认 K*=2
      - Pythia decoding 3/4 K*=2，一个配置边缘
      - Length ablation 128-token K*=1（信息量不足），256/512 K*=2
      - Cross-scorer exp_A 的 scorer-dependence 模式在 exp-022 中重现但可控
    number_ranges:
      new_family_best_1v2_auc: [0.610, 0.635]
      new_family_worst_1v2_auc: [0.580, 0.602]
      pythia_decoding_kstar2_fraction: [0.75, 1.0]
      length_128_1v2_auc: [0.575, 0.605]
      total_conditions_kstar2: [12, 15]
      cross_scorer_kstar2_fraction: [0.60, 0.85]
    narrative_direction: "Universality claim scoped 为 'K*=2 is consistent across all tested conditions meeting minimum information requirements (≥256 tokens; standard decoding)'。失败条件被分析为 principled boundary cases 而非 counterexamples——短文本信息不足导致 K* 降至 1 符合 DPI 预测，特定模型族的边缘性用 architecture-specific information loss rate 解释。增加一个 'Boundary conditions of universality' 分析段落。C1' 措辞降为 'K*=2 is a robust discrimination boundary under standard conditions'。仍冲 EMNLP Main，但需精心管理 reviewer #1 的 rebuttal（承认 scope + 强调已覆盖条件的一致性 + DPI 理论预测的泛化合理性）。"

  worst:
    meaning: "LLaMA 和 Mistral 均显示 K*=1 或 K*=3，universality 叙事崩溃；需 reframe 但不降级目标 venue"
    key_assumptions:
      - LLaMA-8B 和 Mistral-7B 均 K*≠2（1v2 AUC 0.56-0.59 → K*=1，或 2v3 AUC > 0.60 → K*=3）
      - 或 cross-scorer matrix 暴露 K* 强烈依赖 scorer choice（多数 cross 条件 K*=1）
      - Length ablation 128-token K*=1
      - Pythia decoding 可能 2/4 K*=2（模型族 × 解码交互效应）
      - 已完成的 10 条件 K*=2 结果不变——但其 scope 被限制为 "≤1.5B + Qwen-7B 自评"
    number_ranges:
      llama8b_1v2_auc: [0.560, 0.595]
      mistral7b_1v2_auc: [0.555, 0.590]
      total_conditions_kstar2: [10, 12]
      total_conditions_kstar_ne_2: [3, 6]
      cross_scorer_kstar2_fraction: [0.40, 0.60]
    narrative_direction: "放弃 'universal K*=2' 作为 headline。Reframe 为 'K* as a model-family-dependent characterization quantity'：K*∈{1,2,3} 取决于 (architecture, scale, representation) 三元组，但 K*≤3 是 DPI-bounded universal upper limit。新 headline result 变为 'We provide the first systematic measurement of K* and reveal it is bounded, small (≤3), and predictable from model family properties'。C1' 从 universality finding 转为 characterization methodology contribution——首次定义、测量、理论约束 K* 的框架。C3（downstream validation）不受影响（binary filtering 仍优于 graduated，因为 K*≤3 下 graduated 粒度收益有限）。Cross-model transfer 数据重新定位为 'explaining K* variation'——不同模型族的 information loss rate 差异解释 K* 差异。这一 framing 对 EMNLP 仍成立：systematic characterization + theoretical framework + practical guideline，只是从 'surprising universal constant' 降级为 'principled characterization with bounded variation'。Impact 略降但 novelty（首次测量 K*）不变。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5eeff16-afcc-48bb-acda-915682ef17ef",
  "isSidechain": false,
  "requestId": "req_011Cb5re8cdwS9J3ehvgoapv",
  "type": "assistant",
  "uuid": "b6321382-ac1b-4c4f-ad02-256e6773c254",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qg6NRaTbBLESqtQ75UuhR4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 32601,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32601,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 32601,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32601
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "b6321382-ac1b-4c4f-ad02-256e6773c254",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define Dream simulation scenarios for gen-depth-contamination",
  "sessionId": "0388255d-dcfe-409f-a64a-33fa9f9076a8"
}
```

---
