---
round: 17
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-22T11:04:12.780813+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人圆桌
- Reviewer 1: 方法严谨性 + 实验设计
- Reviewer 2: 新颖性 + 完整性 + 写作质量

---

## Summary

OntoCoDec 提出将 IE ontology 自动编译为 token-level 解码约束的两层架构：grammar layer（基于 XGrammar 的 CFG，保证 JSON 结构 + 词表合规）和 semantic layer（有状态 entity registry 实现 cross-field 类型约束）。论文在 3 个数据集（SciERC, DocRED, WikiEvents）、4 个模型族（7B–70B）上系统评估，报告 LoRA + S1 可将 DR 降至 ≤0.09%，但引入 CF 违规（FT ≤1.3%, ZS 最高 12.02%）作为 violation conversion 的结构性代价。附 24 页 appendix 含消融、causal tracing、scalability 等详细分析。

---

## Strengths

**S1. 系统化的评估覆盖度（两位 Reviewer 一致认可）**
3 数据集 × 4+ 模型 × ZS/FT × greedy/beam/sampling，加上五路消融（Table 1）、四路消融（Table 3）、跨模型验证（Table 4）、per-relation breakdown、causal tracing（Table 7）、dual-factor analysis（Figure 2）。Bootstrap 10,000 iterations + Bonferroni correction。在同类工作中属于上乘。

**S2. 诚实透明的 Limitations 和 CF-DR trade-off 分析**
Appendix C 的 causal tracing、CF-priority fallback 消融（Table 8）、dual-factor 定量分析坦诚承认 CF-DR trade-off 是结构性而非可调参数。Limitations section 覆盖了约束范围、评估覆盖、工程约束等关键限制。

**S3. 理论基础有原创性**
Decidability taxonomy（Level 1/2/3）将 IE 类型约束按可判定性分层，Proposition 1（Appendix O）通过 pumping lemma 证明 cross-field type consistency 超出 CFG 表达能力，为两层架构提供形式化依据。

**S4. 低运行时开销**
Greedy S1 仅增加 10–13% latency，constraint compilation < 0.5s，scalability benchmark 到 200 entity types / 1,000 relations 保持 2–3% overhead。

**S5. 可复现性优秀**
Appendix G 报告硬件/种子/超参，3 seeds cross-GPU variance（Table 24），prompt templates 完整展示（Table 6），承诺开源代码。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] Abstract/Intro DR 降幅数字自相矛盾 [AGREE: R1+R2]**
- Abstract: "45–99% DR reduction"
- Introduction: "DR drops 76–99% for calibrated models"
- Table 4 实际全范围: **42–99%**（Mistral DocRED 42% 被排除未说明）
- DocRED Qwen（calibrated model）仅 45%，远低于 Intro 声称的 76% 下界
- 建议：统一为 "42–99%" 或明确限定条件并说明排除理由

**MF2. [critical] Abstract CF ≤1.3% bound 被 70B LoRA CF=1.33% 违反 [AGREE: R1+R2]**
- 差异虽小（0.03pp），但 Abstract 将其作为 bound 呈现
- 70B 是论文明确涵盖的配置（Abstract 说 "five autoregressive LMs (7–70B)"）
- 建议：修正为 "≤1.4%" 或限定为 8B 模型

**MF3. [critical] CF violation 在主文叙事中被系统性低估 [AGREE: R1+R2]**
- Zero-shot Llama DocRED CF 高达 **12.02%**，但主文 §5.1-§5.3 叙述中仅出现 "CF ≤ 1.3%"（仅限 FT）
- Abstract "substantially reduces type violations"——但 zero-shot DocRED Llama total violation (DR+CF) 从 26.24% 仅降至 14.57%（改善 ~44%），远不如 DR 单项 90% 降幅
- 数据在 Table 4 中透明呈现，**问题是叙事 framing 而非数据隐瞒**
- 建议：主文 §5 明确报告 CF 最差情况，Abstract 区分 ZS 和 FT CF 范围

**MF4. [critical] "five autoregressive LMs" 但实际仅 4 个模型——事实错误 [AGREE: R1+R2]**
- 全文仅出现 Qwen3-8B, Llama-3.1-8B, Mistral-7B, Llama-3.3-70B = 4 个模型
- Limitations 也说 "three 8B-class and one 70B-class model" = 4
- 疑似早期版本残留
- 建议：修正 "five" → "four"

**MF5. [critical/should-fix, 分歧] 缺少与现有 constrained decoding 方法的直接实验对比**
- 论文大量讨论 GCD/BoostCD/CRANE/GoLLIE（§6, Appendix B），但无 head-to-head 实验
- 唯一"对比"是自行实现的 Trie-Only Baseline（Table 15, Appendix D）
- §5.4 "BoostCD only 3% DR reduction" 来自方法论等价推断（grammar-only ablation），非运行 BoostCD 代码
- **分歧**: R1 列为 critical（最大短板），R2 交叉认为 should-fix（grammar-only 作为 GCD 代理合理，但 GoLLIE 缺失更严重）
- **Director 判定**: 维持 critical——对于定位为推进 constrained decoding for IE 的论文，缺少 head-to-head 基准对比是核心实验缺口。grammar-only 消融的等价推断在方法论上可辩护，但在实际评审中说服力不足，尤其是该问题已被多轮审稿反复指出。至少应运行 GCD 官方代码或明确论证 grammar-only = GCD 的等价性

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] κ̄ (constraint tightness) 在 n=3 schema 上声称 "predictive factor" [AGREE: R1+R2]**
- Abstract: "establishing constraint tightness (κ̄) as a predictive factor"
- 实际仅 3 个 schema（SciERC κ̄=0.333, DocRED κ̄=0.842, WikiEvents κ̄≈0.82）
- Figure 2 仅 4 数据点线性拟合（R²=0.886, p=0.058 不显著）
- x 轴使用 κ̄ × RV_baseline（model-dependent），使 κ̄ 自身 predictive power 不明确
- 建议："establishing...predictive factor" → "introducing...descriptive metric"

**SF2. [warning] WikiEvents fine-tuning composability 仅 n=20 文档 [AGREE: R1+R2]**
- Per-document variance > 0.5，bootstrap CI 极宽
- WikiEvents EE 不涉及 cross-field type constraints，仅验证 grammar layer
- 建议：Table 5 加 confidence interval，明确标注为 preliminary

**SF3. [warning] "Deployment-grade compliance" 叙事被 CF trade-off 结构性削弱 [AGREE: R1+R2]**
- CF 是 DR enforcement 的系统性副产品，zero-shot 最高 12.02%
- "Deployment-grade" 暗示接近零违规，系统在 CF 维度做不到
- 建议：软化为 "near-complete DR elimination with residual CF trade-off"

**SF4. [warning] "Enabling dependency" 声明范围不清 [AGREE: R1+R2]**
- "neither layer alone exceeds 24% DR reduction" 仅限 SciERC
- DocRED grammar-only **增加** DR 42%，与 SciERC 模式截然不同
- 建议：改为 "on SciERC, neither layer alone exceeds 24%"

**SF5. [warning] Entity registry 顺序依赖未量化 [AGREE: R1+R2]**
- 首次类型分配错误会传播到所有后续引用
- Limitations 承认但无量化分析
- CF 是间接量化但不等价于 propagation rate
- 建议：post-hoc 分析首次提及错误率和传播频率

**SF6. [warning] S2 (two-pass pipeline) 描述与评估不匹配 [AGREE: R1+R2]**
- §3.4 花半页描述但仅 Table 1 一行结果
- 8 页限制下建议方案 A（压缩 §3.4）而非补充完整实验

### Minor（不影响接收）

**M1.** §6 Related Work 仅约半栏，严重依赖 Appendix B。主文读者无法仅从 §6 评估覆盖充分性。[R1+R2 AGREE]
**M2.** "S1"/"Full S1" 术语不统一（§5.1 vs §5.4）。[R2]
**M3.** Figure 1 信息密度过高。[R2]
**M4.** Table 4 Mistral CF=56.87% dagger 脚注解释位置不佳。[R2]
**M5.** Introduction "48% predictions discarded" 未 cite 来源表格。[R2]
**M6.** Proposition 1 position-based vs name-based 桥接缺乏形式化 corollary。[R1+R2 AGREE, 低严重度]
**M7.** 70B AWQ INT4 量化对约束 enforcement 的潜在影响未讨论。[R1+R2 AGREE]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成完全共识：
1. **DR/CF 数字精确性**：Abstract/Intro 存在多处数字不一致或 bound 违反（MF1-MF4）
2. **CF 叙事偏乐观**：主文 framing 系统性低估 CF 代价（MF3, SF3）
3. **κ̄ 过度声称**：n=3 不支持 "predictive factor"（SF1）
4. **WikiEvents 统计效力不足**：n=20 不支持 generalization 结论（SF2）
5. **可复现性优秀**：评估设计全面，Appendix 详尽（S1, S2, S5）

## Reviewer Divergence

| 议题 | R1 | R2 | Director 判定 |
|------|-----|-----|-------------|
| **Baseline 实验对比严重度** | Critical（最大短板） | Should-Fix（grammar-only 代理合理） | **Critical**——连续多轮未解决，对于 constrained decoding 论文是核心实验缺口 |
| **新颖性** | Excitement 3/5（Proposition 1 decidability taxonomy 有原创性） | Excitement 2.5/5（已知组件集成） | **2.75/5**——系统集成 + 全面评估有价值，但核心组件确为已知技术。建议调整贡献定位 |
| **CF 呈现严重度** | Critical | Warning (framing 而非隐瞒) | **Critical**——数据透明但叙事不匹配，abstract 是审稿人最先读到的部分 |

---

## Questions（需要作者澄清）

**Q1.** Abstract/Intro DR 降幅范围不一致（45–99% vs 76–99%），"calibrated models" 如何定义？DocRED Qwen（calibrated）仅 45% 如何与 76% 下界调和？

**Q2.** Multi-type entity（一个 entity 在 ontology 中合法拥有多个类型）如何处理？当前 first-assignment-wins 设计是否导致 false positive CF？

**Q3.** Llama DocRED CF 12.02% vs Qwen 2.57%——根因是 Llama 的 entity typing 能力弱还是 DocRED schema 特殊性？

**Q4.** 是否考虑过 constrained decoding + post-hoc filtering 的组合策略？

**Q5.** BoostCD "only 3% DR reduction"——请明确标注此结论来自 grammar-only ablation 的方法论等价推断而非运行 BoostCD 代码。

**Q6.** Grammar-only 在 DocRED 上增加 DR 42%——这对 "enabling dependency" 的通用性有什么影响？

---

## Missing References

论文在 constrained decoding + IE 领域的覆盖相当全面。以下可能值得提及但非必要：
- **Schmidt & Cimiano (2025)**: Grammar-constrained decoding for structured IE in biomedical domain (Bioinformatics)
- **Microsoft Guidance**: 工程工具，constrained generation 讨论中常被提及
- 建议检查 **EMNLP 2025** proceedings 是否有遗漏的近期 accepted papers

**引用真实性**: Reviewer 2 验证全部 46 个 bib 条目均来自真实论文/预印本，格式统一，未发现伪造引用。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未启用外部审稿配置）

---

## Visual Layout Check（非评分项）

**状态**: 已完成 (4 warnings, 0 critical, 9 info)

主要发现：
- **[warning]** Pages 1-2 连续纯文本（Title/Abstract/Intro/Background），首个 display item（Figure 1）直到 page 3 才出现
- **[warning]** Pages 4-5 连续纯文本（Method），无公式 display 或图表穿插
- **[warning]** Pages 6-7 display items 分布严重不均：5 张 table 集中在 2 页，page 7 尤其密集（Tables 3-5 挤在一页）
- **[warning]** Page 8（Related Work + Conclusion）全部纯文本，无视觉元素收尾
- **[info]** 主正文 8 页仅 1 figure + 5 tables，figure 数量偏少。Appendix 中 Figure 2/3 若能提升到主文可改善阅读体验
- **[info]** 无 margin 溢出、无 LaTeX 渲染错误、无 [?] 未解析引用。格式符合 ACL 匿名投稿模板

---

## Overall Assessment

### 评分

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | **3.5/5** | 方法论合理，消融设计系统，但 Abstract/Intro 数字不一致削弱可信度；CF framing 偏乐观；缺少 baseline head-to-head |
| **Excitement** | **2.75/5** | 问题重要且实用，但核心组件（XGrammar + runtime type check）均为已知技术。Proposition 1 的 decidability taxonomy 有理论贡献但影响面有限。主要贡献是系统集成和全面评估 |
| **Reproducibility** | **4.5/5** | Appendix G 详尽，bootstrap CI，seed 报告，代码承诺开源 |
| **Overall Assessment** | **3.5 — Borderline Conference** | R1 和 R2 独立评分一致 |
| **Confidence** | **4/5** | 两位 Reviewer 仔细阅读全文含 34 页 appendix |

### 总评

一项系统化但新颖性有限的工程贡献。将已知组件（CFG enforcement + runtime type checking）组合为 IE ontology 约束解码管道，配以出色的评估覆盖度和诚实的 limitations 分析。核心障碍是：(1) Abstract/Intro 存在多处数字不一致和 bound 违反，削弱论文可信度；(2) 缺少与 GCD/BoostCD 等现有方法的直接实验对比；(3) CF violation 的主文叙事系统性偏乐观。修正数字错误（MF1-MF4）和调整叙事 framing（MF3, SF3）可提升至 Conference 水平；补充 baseline 对比（MF5）可进一步巩固贡献。当前状态适合 Findings 接收，距离 Conference 主会议接收有明确但可修复的差距。

---

## Detailed Comments（逐节）

### Abstract
- DR 降幅 "45–99%" 与 Intro "76–99%" 不一致（MF1）
- "CF ≤ 1.3%" 被 70B 的 1.33% 违反（MF2）
- "five autoregressive LMs" 实际 4 个（MF4）
- "establishing constraint tightness (κ̄) as a predictive factor" 过度声称（SF1）
- "substantially reduces type violations" 在 DR↓+CF↑时需更精确表述
- 写作质量高，信息密度适当

### §1 Introduction
- Contribution 2 "neither layer alone exceeds 24%" 仅限 SciERC，读者自然误解为通用结论（SF4）
- "deployment-grade type compliance" 被 CF trade-off 削弱（SF3）
- "Post-hoc filtering improves precision but discards up to 48%"——未 cite 来源表格（M5）
- 问题动机和叙事逻辑清晰

### §2 Background
- IE ontology 的形式化定义清楚
- 约束可判定性三级分类是有用的概念框架
- Proposition 1 定位为 "necessary condition" 恰当

### §3 Method
- Grammar layer 和 semantic layer 描述清晰
- Continuation masking 机制解释充分
- Grammar-first fallback 设计决策合理且有 causal tracing 验证
- §3.4 S2 描述占半页但实验中一句带过（SF6）

### §4 Constraint Composition
- Mask composition 公式简洁
- Asymmetric conjunction 解释清楚

### §5 Experiments
- Table 1 五路消融是最强的实验贡献
- DocRED grammar-only DR 增加 42% 值得主文更详细讨论（SF4）
- WikiEvents n=20 统计效力不足（SF2）
- 70B 定位为 feasibility check 基本恰当，但仍被纳入 Abstract 统计声明
- 缺少与 GCD/BoostCD 的 head-to-head 实验（MF5）

### §6 Related Work
- 覆盖面合理但主文仅约半栏（M1）
- GCD, GoLLIE, EnriCo 的对比定位准确
- 建议将 Appendix B 中关键对比移入主文

### §7 Discussion and Conclusion
- 数字继承了 Abstract/Intro 的不一致问题

### Limitations
- 全面且诚实（S2），三段分别覆盖约束范围、评估覆盖、工程考量
- CF trade-off 定性为 "fundamental trade-off" 合理

### Ethics Statement & Checklist
- Ethics statement 简洁充分
- Checklist 填写认真，各项回答与论文内容一致
- Responsible NLP Checklist 在 OpenReview submission form 中填写（符合 EMNLP 2026 要求）

### 格式
- 正文 8 页 ✓
- `\usepackage[review]{acl}` ✓（匿名，行号）
- "Anonymous ACL submission" ✓
- 未发现 self-citation leaks 或 identifying information
- Limitations/Ethics 在 \clearpage 后，不计入页数 ✓
- 参考文献格式统一，无 [?] 未解析引用