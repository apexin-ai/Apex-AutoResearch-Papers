# Related Work — Structured Notes

> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。

## (a) G-theory & Variance Decomposition in NLP/ML

### [Mesting et al., 2026] — TEE: Generalizability Theory for NLG Evaluation
- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估；发现 judge 选择贡献 43.8% 方差，prompt 在开源模型中贡献~50%、商用模型~25%；标准 95% CI 实际覆盖率仅 79%
- **与本工作关系**: extends — 我们直接继承其 TEE 框架和 REML 方法，将其扩展到 infrastructure facets
- **差异化**: Mesting 只分解方法论 facets（item/prompt/judge/temp），未纳入硬件/精度等基础设施因素；我们的 G-theory 框架联合分解 infrastructure × methodology

### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition
- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量
- **与本工作关系**: complements — 提供了 prompt 方差的细粒度分解视角，其 articulation 分量对应我们框架中 prompt paraphrase facet
- **差异化**: 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的交叉设计

### [Nalisnick et al.] — GeneralizIT: Software for G-theory in ML
- **核心发现**: 为 ML 场景提供 G-theory 计算工具包，简化 REML 估计和 D-study 设计流程
- **与本工作关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现
- **差异化**: 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget

## (b) Infrastructure Variance

### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance
- **核心发现**: BF16 推理导致 9% 的 accuracy 标准差，FP32 接近 0%；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存；推理模型受影响最大
- **与本工作关系**: addresses limitation of — 量化了精度对推理结果的影响，但未将其纳入统一的方差分解框架
- **差异化**: Yuan 只刻画精度这一个 infrastructure 因素并提出缓解方案；我们将精度作为 G-theory 框架中的一个 facet，与方法论因素联合分解

### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation
- **核心发现**: 即使 T=0，API 模型仍存在 "背景随机性"：GPT~0.075、Gemini~0.065、Claude~0 有效温度；提出 reference calibration 方法量化为单一标量 T_bg
- **与本工作关系**: complements — 揭示了一类此前被忽视的 infrastructure 方差源（硬件层面的非确定性），为我们纳入硬件 facet 提供实证依据
- **差异化**: Messina 聚焦 API 层面的背景温度刻画，未进行多因素交叉分解；我们将此类硬件非确定性纳入 G-theory 的交叉设计

### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference
- **核心发现**: T=0 下 1000 次推理产生 80 种不同输出；根因是 RMSNorm/GEMM/attention 的 batch-size 依赖性而非随机种子；提出确定性内核方案，代价为 1.6-2.1× 延迟
- **与本工作关系**: addresses limitation of — 发现并解释了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程修复
- **差异化**: 仅刻画 batch-size 这一个因素并提出工程缓解方案；我们将 batch 非确定性与其他 infrastructure/methodology 因素一起纳入 G-theory 分解

## (c) Prompt Sensitivity & Methodological Variance

### [Brittlebench, 2026] — Prompt Brittleness Benchmark
- **核心发现**: 系统性评估 prompt 脆弱性；通过 ANOVA 分解 V_data + V_brittleness；prompt 措辞贡献约 50% 方差（开源模型），商用模型约 25%
- **与本工作关系**: complements — 提供了大规模 prompt 脆弱性的实证基准，其 V_brittleness 分量对应我们框架中 prompt facet 的方差
- **差异化**: 使用传统 ANOVA 而非 G-theory，只分解 data vs. brittleness 两个分量；我们的框架支持更多 facets 的联合分解和交互项估计

### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation
- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 后 rank correlation 从 0.30 跃升至 0.95
- **与本工作关系**: complements — 警示区分"真实方差"与"评估 artifact"的重要性，为我们的实验设计提供方法论参考
- **差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献

### "Same Prompt, Different Outcomes" — Seed/Sampling Variance
- **核心发现**: [需补充]
- **与本工作关系**: [需补充] — 预期与我们框架中 seed facet 直接相关
- **差异化**: [需补充]

### [Bui et al.] — Seed Sensitivity in LLM Evaluation
- **核心发现**: [需补充]
- **与本工作关系**: [需补充] — 预期聚焦 seed 这一单一因素
- **差异化**: [需补充]

## 定位总结

本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。
