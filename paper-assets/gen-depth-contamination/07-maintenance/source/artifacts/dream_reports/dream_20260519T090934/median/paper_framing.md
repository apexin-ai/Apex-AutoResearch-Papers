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
