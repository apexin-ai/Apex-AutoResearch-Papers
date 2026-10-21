# Paper Framing — clkc_mech_interp

> 最后更新: 2026-05-22 | 目标: EMNLP 2026 via ARR (DDL 2026-05-25, 3天)

## Core Insight

多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致。**关键发现（plan_110 XNLI 基线）**：该不对称性并非冲突特有——非冲突语义任务 (XNLI) 展现几乎相同幅度的迁移不对称性（Qwen +6.72pp, Llama +5.97pp）。这说明冲突信号**编码在模型的通用跨语言表征空间中**，继承其方向性偏置，而非独立的专用机制。

**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。

## Narrative Structure

**机制分析驱动**（非 "发现新现象"）：

1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity 决定跨语言冲突解决，但未提供机制解释
2. **Mechanistic question**: 冲突信号在模型内部如何编码？与一般跨语言语义表征的关系是什么？
3. **Our answer**: 冲突信号可线性检测且跨架构一致，但其跨语言迁移模式（方向不对称性）**与一般语义任务 (XNLI) 无异**——冲突检测 piggyback 在模型已有的跨语言对齐结构上，而非专用子空间。通过层结构分析和因果干预验证这一机制。
4. **Methodological contribution**: 严格的 confound exclusion pipeline (COMET ablation + token overlap) + 非冲突基线对照，为跨语言 probing 研究树立方法论标准

**Secondary framing**: 跨语言 probing 中方向性偏置的普遍性——English-dominant 模型的固有属性，影响所有跨语言迁移研究的结论解读

## Competing Hypotheses (pre-registered)

**H1 — English-anchored universal detection**:
冲突检测信号本身是 language-independent 的（"是否存在冲突" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。
- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)
- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）

**H2 — Language-pair-specific encoding**:
冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。
- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late
- 预测: 探针迁移准确率与语言对 typological distance 强相关

**MVP + plan_110 证据倾向**:
ZH→EN 迁移优势（~7pp）在冲突和 XNLI 任务中均存在且幅度一致，说明这是模型跨语言表征的固有属性（H1 部分支持：英语锚点存在，但非冲突特有）。冲突信号编码在通用跨语言空间中。非线性成分（MLP EN→ZH gains）是否冲突特有待 XNLI 上的 MLP 对照验证。

## Core Claims

### Claim 1: Cross-lingual conflict detectability
**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。
**Evidence needed**:
- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.6%, Qwen 75.0%)
- Permutation test p < 0.001 ✅ (all directions)
- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)
**Status**: MVP 已验证 ✅

### Claim 2: Cross-lingual transfer asymmetry as general model property [REFRAMED per D008]
**Statement**: 跨语言探针迁移呈方向一致的不对称（ZH→EN > EN→ZH ~7pp），但 **XNLI 非冲突基线展现几乎相同幅度的不对称性**（Qwen +6.72pp, Llama +5.97pp），说明这是 English-dominant 模型的一般跨语言迁移属性，非冲突特有。冲突信号继承了模型的通用跨语言表征结构。
**Evidence**:
- 冲突不对称性: Llama +7.22pp CI[1.1,13.6], Qwen +7.18pp CI[-1.2,13.4] ✅
- XNLI 不对称性: Llama +5.97pp CI[0.92,11.33], Qwen +6.72pp CI[2.36,11.73] ✅
- 两者量级无显著差异，CI 大幅重叠 ✅
- Token overlap 排除 ✅ | COMET confound 排除 ✅
- ≥1 additional architecture 验证 ❌ (plan_102 Gemma 进行中)
**Status**: XNLI 基线已完成，C2 reframed ✅⚠️ (待第三模型确认)

### Claim 3: Non-linear encoding trend [DEAD — D012 双模型 CI 含零]
**Statement**: ~~冲突信号包含非线性成分~~ → 降为 supporting observation，不作为独立 claim。
**Evidence**:
- 冲突 MLP Δ (EN→ZH): Qwen +3.84pp CI[-3.57,+11.31] 含零 ❌; Llama +5.21pp CI[-2.21,+12.87] 含零 ❌
- XNLI MLP Δ (EN→ZH): Qwen -2.0pp, Llama -0.5pp — 方向对比成立但不显著
- **双模型 bootstrap 均不显著**，方向一致（冲突正、XNLI 负）可作为 suggestive trend 在 discussion 中提及
**Status**: ❌ 不作为论文 claim。Discussion 中作为 observation 报告。

### Claim 4: Layer-wise conflict signal structure
**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。
**Evidence needed**:
- Layer-wise probe accuracy curves for ≥3 models ❌
- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌
- 与 "Lost in Multilinguality" 的 language transition 层对比 ❌
**Status**: 未验证 ❌

### Claim 5: Cross-lingual SAE conflict features (Track 2)
**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。
**Evidence needed**:
- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌
- LangFIR random-token filtering 控制 ❌
- Cross-lingual feature Jaccard 分析 ❌
**Status**: 未开始 ❌

### Claim 6: Causal evidence via representation steering (Track 3) [Llama-specific SUCCESS]
**Statement**: 探针权重方向在 Llama 中具有因果意义——沿此方向 steering 可改变模型冲突解决行为。跨模型验证失败，steering 是 architecture-dependent。
**Evidence**:
- Probe-weight steering 显著改变 p↔c flip rate (vs random control) ✅ (Llama L13)
- ≥1 layer/position 配置 Fisher p < 0.05 ✅ (α=+5 p=0.002, α=-20 p=0.0009)
**L13 result (D014, SUCCESS)**: Llama L13, last-token — α=+5 p=0.002 (19.9% vs 6.6%), α=-20 p=0.0009 (36.0% vs 17.6%)。方向性正确：正α→p→c, 负α→c→p。
**L28/L18/L28-all NEGATIVE**: 因果节点在 mid-layer (L13, ~40% depth), NOT probe peak (L28, ~88%)。
**跨模型验证 NEGATIVE**:
- Qwen L14 (39%): negative, 但 underpowered (9.5% parametric baseline, 8 samples) → uninformative
- Qwen L23 (64%): negative (all p=1.0)
- **Gemma L17 (40%)**: negative, adequate sample size, probe acc 75.3% → **informative negative**，确认 steering 是 architecture-dependent
- Gemma L21 (50%): ⏳ running, 预期 negative
**核心机制发现**: Detection ≠ Decision — 模型在 late-layer 编码可检测信号，但因果决策在 mid-layer 形成。且因果效应是 architecture-dependent：同一深度的 probe weight 方向在 Llama 有因果力但在 Gemma/Qwen 没有。
**Status**: Llama L13 ✅ SUCCESS, 跨模型 ❌ NEGATIVE (Llama-specific)

## Anticipated Reviewer Concerns

### RC1: Translation quality confound [RESOLVED ✅]
**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败
**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。
**Remaining**: Llama test COMET 完成后重复此分析确认一致性。

### RC2: Token overlap confound [RESOLVED ✅]
**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动
**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**

### RC3: Model coverage insufficient [HIGH]
**Concern**: 只有 2 个模型，无法声称 "架构无关"
**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性
**Experiment**: P0 — additional model verification

### RC4: Dataset size and diversity [MEDIUM]
**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对
**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）
**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)

### RC5: Linear probe expressiveness [LOW]
**Concern**: 线性探针可能遗漏复杂非线性信号
**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化
**Experiment**: Done — MLP vs Linear comparison

### RC6: SAE base/instruct mismatch [MEDIUM]
**Concern**: Qwen-Scope SAE 训练在 base model 上，用于 instruct model 分析可能失配
**Mitigation**: Track 2 用 base model 做 SAE 分析 + 与 Track 1 instruct probe 交叉验证
**Experiment**: Track 2 设计已考虑

### RC7: Steering failure precedent [MEDIUM]
**Concern**: "Interpretability without actionability" 证明 SAE steering 可能完全无效
**Mitigation**: 知识冲突与临床分诊的 5 维差异（SpARE 已证明知识冲突场景 steering 有效）；Track 3 显式报告失败模式
**Experiment**: Track 3 包含 negative result framing

### RC8: Causal claims without intervention [RESOLVED ✅ — L13 steering success D014]
**Concern**: 探针只证明信号可检测，不证明因果关系
**Result**: L13 steering (Llama) 提供因果证据 — α=+5 p=0.002, α=-20 p=0.0009。L28/L18 均 NEGATIVE，说明因果节点在 mid-layer。Detection-vs-Decision 层分离本身是核心机制发现。
**Remaining**: Qwen L13 跨模型验证进行中。

### RC9: Non-conflict semantic baseline [CRITICAL — Dream 三档一致]
**Concern**: X→EN > EN→X 不对称性可能是英语主导模型的一般跨语言迁移属性，非冲突特异性
**Mitigation**: 用相同 pipeline 探针非冲突语义任务（sentiment/NLI），验证不对称性是否消失
**Experiment**: P0 — plan_110 (非冲突语义基线)
**判断标准**: 非冲突任务的不对称性 < 2pp → conflict-specific confirmed；2-5pp → partially specific（报告为 "general cross-lingual component exists but conflict amplifies asymmetry"）；≥ 5pp → reframe as general cross-lingual property

### RC10: Bootstrap n 不足 [MAJOR — Dream 三档一致]
**Concern**: n=100 bootstrap 低于 Efron & Tibshirani (1993) 标准 n≥1000，CI endpoints 波动大
**Mitigation**: 升级至 n≥2000
**Experiment**: P0 — plan_111

### RC11: Typological diversity 不足 [MAJOR — Dream 三档一致]
**Concern**: 仅 CJK 语言对，无法支撑 "universal" 声明
**Mitigation**: 添加 Indo-European 语言对 EN↔DE
**Experiment**: P0 — plan_112

## Paper Structure (Updated for EMNLP 2026, 8-page limit)

1. **Introduction**: CLEAR gap → mechanistic question → probing approach → key findings (detection + XNLI comparison)
2. **Related Work**: Cross-lingual knowledge conflicts → Probing methodology → Cross-lingual representations
3. **Method**: Data construction (ConflictQA + translation + COMET verification) → Residual stream probing → Non-conflict baseline (XNLI) → Confound controls
4. **Experiments & Results**:
   - 4.1 Cross-lingual conflict detectability (C1) — within/cross-language probe accuracy
   - 4.2 Transfer asymmetry + XNLI comparison (C2) — asymmetry is general cross-lingual property
   - 4.3 Methodological controls (token overlap, COMET ablation, bootstrap)
   - 4.4 Layer-wise probe accuracy structure (from existing data)
5. **Discussion**: Mechanism implications → MLP non-linearity trend (C3 observation) → Steering negative finding → Limitations → Connection to CLEAR
6. **Conclusion**

## Scope Control (EMNLP 2026, DDL May 25)

**投稿最低要求 (must-have)**:
- C1 fully supported (cross-lingual detectability, ≥2 models) ✅
- C2 fully supported (XNLI non-conflict comparison) ✅
- Token overlap control ✅
- COMET translation quality validation ✅
- Bootstrap n≥2000 (plan_111, 运行中)

**可能来得及 (best-effort, 完成即补入)**:
- Gemma 第三模型验证 (probe training 中)
- EN↔DE 第二语言对 (translate 即将完成)
- Steering v2 variants 结果 (L13/L18/Qwen)
- Layer-wise probe acc curves (从已有数据提取，无需新 GPU 实验)

**不做 (out of scope for this submission)**:
- Track 2 SAE analysis
- Track 3 full steering (作为 negative finding 报告)
- CKA/SVCCA layer analysis
- 多于 2 个语言对
