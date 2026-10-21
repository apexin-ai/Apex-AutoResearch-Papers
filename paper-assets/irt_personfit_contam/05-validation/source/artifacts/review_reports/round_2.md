---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T21:24:50.598170+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：What Can Binary Response Patterns Reveal About Benchmark Contamination? An IRT Person-Fit Characterization

**Venue**: EMNLP 2026 (via ACL Rolling Review, Long Paper)
**Reviewers**: R1 (方法严谨性/实验设计/统计推断) + R2 (新颖性/完整性/写作质量)
**轮次**: Round 1 (fresh review)
**日期**: 2026-05-21

---

## Summary

本文首次将心理测量学中的 person-fit 统计量（ℓz*）系统性地应用于 LLM benchmark 污染检测，使用 Δℓz* 差分设计 (DiD) 在三个 7-8B 模型族上进行控制实验，识别出四个 IRT 特有的行为边界：non-monotonic dose-response、model-specific θ-shift dynamics、detection-diagnosis tradeoff、以及 preliminary post-RL residual pattern。论文定位为 characterization 而非 tool，诚实展示了 ℓz* 在检测力上远弱于简单 accuracy z-score 的局限性，将其价值定位于诊断能力。

---

## Strengths

**S1 [共识]** 跨学科连接真正新颖——psychometric person-fit → LLM contamination detection 是自然但尚未被探索的类比，将心理测量学四十年积累的作弊检测理论引入 NLP 评估。

**S2 [共识]** 方法论设计巧妙——Δℓz* DiD 设计优雅处理 57/60 baseline misfit 问题，将 IRT 假设违反从障碍转为可管理的技术条件。Appendix 中的 local dependence 模拟（shared + asymmetric LD）和参数扰动分析提供充分的鲁棒性证据。

**S3 [共识]** 异常诚实的 self-assessment——论文坦诚展示 accuracy z-scores 的压倒性检测优势（|d| 10-36×），将 ℓz* 定位为诊断工具而非检测工具，这种自我克制在竞争性投稿中罕见且值得肯定。

**S4 [共识]** θ-shift absorption 机制洞察力强——fixed-θ 验证效果显著（Qwen |d| 1.90→14.52, 7.6× amplification），且 Table 2 的 free/fixed 对比为实操提供清晰建议。

**S5 [共识]** 附录异常充实——每个方法论质疑（IRT 假设违反、local dependence、参数噪声、seed sensitivity）都有对应的模拟或实验分析，学术严谨性高。

**S6 [R2]** Detection-diagnosis tradeoff 的 two-stage workflow（先 z-score 筛选，后 ℓz* 诊断）清晰可操作，有实用价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [共识, R1-N1=R2-N3, 交叉双方 AGREE]** 仅两个污染水平 (15%, 50%) 不足以支撑 "non-monotonic dose-response characterization" 的核心 claim。
- 两个非零水平只能说 "Qwen 在 15% 的 |d| 大于 50%"——是观察而非曲线刻画
- Qwen 15% CI=[-15.2,-4.5] 和 50% CI=[-5.0,-1.0] 存在重叠，两水平间差异未经正式统计检验
- Non-monotonic 仅在 Qwen 上观察到；Mistral 和 Llama 为单调/近单调——泛化性存疑
- Appendix A simulation 覆盖 7 个水平，说明框架支持更细粒度采样但 controlled experiments 选择不做
- QLoRA 7B 模型微调成本极低，补充 5%/10%/25%/30% 完全可行
- **建议**：补充中间污染水平，或将 "non-monotonic dose-response" 降级为 "observed difference between two levels, consistent with simulation-predicted non-monotonicity"

**N2 [共识, R2-N1, R1 交叉 AGREE]** "Minimal-information point" framing 与实际信息需求矛盾。
- Abstract/Introduction/Related Work 反复强调 "binary responses only"，但框架强依赖 PSN-IRT 4PL item bank（基于 13,000+ 模型的 leaderboard 数据校准）
- Fixed-θ estimation 还需 clean baseline，进一步提高信息门槛
- 来自 target model 的信息确实是 minimal，但来自 item population 的外部信息是 substantial
- **建议**：改 framing 为 "minimal information from the target model"，显式区分 target model access（binary only）和 external item bank（substantial prior knowledge）

**N3 [共识, R1-N2, R2 交叉 AGREE (略低严重度)]** QLoRA SFT 生态效度与 Introduction 的 pretraining contamination 动机脱节。
- Introduction 以 pretraining contamination 为动机（line 3-6），但实验用 QLoRA SFT (rank=16, α=32)
- SFT 在低秩空间产生的集中记忆化信号远强于 pretraining 的分布式嵌入，报告的高 Cohen's d 可能反映 SFT 特有效应
- Section 3.3 和 Limitations 的 scoping 负责任，但 Introduction 叙事未对齐
- **建议**：Introduction 前置 SFT scope 限定，将 pretraining contamination 作为 motivation context 而非 direct target

**N4 [共识, R2-N3=R1-W4, 交叉双方 AGREE]** 实验规模偏窄，削弱 generalization claims。
- 仅 3 个 7-8B 模型、2 个 benchmark（MMLU + ARC-C）、仅 SFT 污染
- ARC-C 上仅 Qwen 结果，Llama/Mistral 缺失——Section 4.3 的 ceiling effect 讨论缺乏对照
- "Baseline ability 与 detection sensitivity 负相关" 仅基于 3 个数据点，不足以建立系统性关系
- 标题/abstract 措辞暗示泛化性，但 scope 仅限 SFT 污染一隅
- **建议**：补齐 Llama/Mistral ARC-C；标题/abstract 明确 scope 为 SFT-stage characterization

### Should-Fix（影响评分但不一票否决）

**W1 [共识, R1-W1=R2-W1, 交叉完全一致]** Post-RL finding (N=1) 不应列为核心 contribution。
- N=1（Qwen, GRPO, 15% MMLU），无统计推断，但 Abstract/Introduction 将其与 n=10 控制实验并列为四大发现
- ℓz* 从 2.91 增至 7.69——可能是 GRPO-induced θ-shift 或 ability reorganization 而非 contamination residual pattern
- 需要 clean Qwen + GRPO 作为 control 来 disentangle GRPO 本身的效应
- Section 4.5 的 caveats 充分但 Abstract/Conclusion 未匹配
- **建议**：降级为 "preliminary observation"，从 Abstract 核心列表移除或显著降低权重

**W2 [R1-N3, R2 交叉 REBUT 降级]** Mistral n=6 seeds 统计效力不足。
- 因服务器退役丢失 4/10 checkpoints；Table 2 fixed-θ CI 跨度达 [1.45, 9.00]——约束力极低
- R2 认为降级为 Should-Fix（Table 1 CI 均不含零，Mistral 不独立支撑 unique finding），R1 原列为 critical
- QLoRA 成本极低，补跑完全可行
- **建议**：补至 n=10

**W3 [共识, R1-W2, R2 交叉 AGREE]** ℓz* 诊断价值论证不足——item-level AUROC=0.53 近乎随机。
- Accuracy z-score |d| 是 ℓz* 的 10-36×
- Seen/unseen decomposition 的 item-level AUROC=0.53 (Table 8) 接近随机，削弱诊断 claim
- θ-shift mechanism 有洞察力但更像框架理论（导出 fixed-θ 建议有实操价值——R2 补充）
- Structural sensitivity (57/60 flagged) 反映 IRT misfit 普遍性，论文已正确用作 DiD 设计动机
- **建议**：加强 tradeoff 论证，增加具体 practitioner use case；诚实报告 item-level near-random

**W4 [共识, R1-W3, R2 交叉 AGREE]** PSN-IRT 参数循环依赖风险。
- PSN-IRT 基于可能受 contamination 影响的 leaderboard 数据校准
- Appendix F 的高斯扰动分析有价值但不能模拟结构性偏差
- Section 3.1 提到 MML-EM refit r_a=0.127 但实验细节缺失
- **建议**：补充 MML-EM refit 实验描述；讨论 leaderboard 校准污染影响

**W5 [部分共识, R2-N2, R1 交叉 REBUT 部分同意]** 缺少与 ConStat 的实证对比。
- R2 要求与 ConStat/MIA/CoDeC 对比；R1 指出 MIA 对比不合理（不同信息层级），但 ConStat 对比合理且可行
- ConStat 同为 performance-based，Discussion 仅一句概念性提及不足
- **建议**：补充 ConStat 实证对比，或至少给出详细定性分析说明 ℓz* 的互补优势

**W6 [共识, R1-W5, R2 交叉 AGREE]** Bootstrap CI 方法类型和小样本可靠性。
- Reproducibility Statement 已说明 percentile method，但 n=3/6 下 percentile bootstrap 可能 anti-conservative
- Appendix C 中 n=3 的 analytic CI 跨零而 bootstrap CI 不跨——可能反映小样本 anti-conservatism
- **建议**：补充 BCa sensitivity check；Llama fixed-θ 15% CI 包含零 [0, 2.37] 应在正文讨论

**W7 [R2-W4, R1 部分 REBUT]** Related Work 遗漏若干相关方法。
- PaCoST (EMNLP 2024 Findings)、Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023) 高度相关应讨论
- 未解释从 36 种 person-fit 统计量中仅选 ℓz* 和 HT 的理由
- 经典心理测量引用偏少：Reise (1990), Levine &amp; Drasgow (1988), Embretson &amp; Reise (2000)
- R1 认为 Watermarking-based detection 相关性较低

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全或实质性共识：

1. **[AGREE]** 两个污染水平不足以支撑 non-monotonic dose-response 的核心 claim（R1-N1 = R2-N3）
2. **[AGREE]** "Minimal-information point" framing overclaim（R2-N1, R1 交叉 AGREE）
3. **[AGREE]** QLoRA SFT 生态效度与 Introduction 叙事脱节（R1-N2, R2 交叉 AGREE）
4. **[AGREE]** 实验规模偏窄，ARC-C 缺失 Llama/Mistral（R1-W4 = R2-N3）
5. **[AGREE]** Post-RL N=1 不应列为核心 contribution（R1-W1 = R2-W1）
6. **[AGREE]** GRPO 后 ℓz* 增加需排除 θ-shift confound（R1-Q4 = R2-Q5）
7. **[AGREE]** ℓz* 诊断价值比论文暗示的弱，但非零（R1-W2, R2 交叉 AGREE）
8. **[AGREE]** PSN-IRT 循环依赖和 MML-EM refit 细节缺失（R1-W3, R2 交叉 AGREE）
9. **[AGREE]** ConStat 实证对比合理且可行（R2-N2, R1 交叉部分 AGREE）
10. **[AGREE]** Bootstrap percentile 小样本可靠性需验证（R1-W5, R2 交叉 AGREE）

---

## Reviewer Divergence

**D1** Findings 新颖性定级——IRT 理论可预测 vs empirical quantification 有独立价值。
- R2: θ-shift absorption 是 IRT 教科书知识，ceiling effect 是已知现象——四个 findings 中两个可先验预测
- R1 [REBUT]: IRT 文献未量化 LLM 场景下 θ-shift 幅度（7.6× amplification）；ARC-C reversal 涉及 item count × baseline ability 非线性交互；模型特异性（Qwen 非单调 vs Mistral 单调）不可先验预测。论文定位就是 "首次在 LLM 场景下量化边界"
- **Director 判断**：R1 反驳有力。理论可预测不等于已被验证——empirical characterization in a new domain 有独立贡献价值，但论文应更好 acknowledge prior IRT literature 的理论基础

**D2** Mistral n=6 严重程度。
- R1: critical（统计效力不足，应阻止接收）
- R2: should-fix（CI 不含零，不独立支撑 unique finding，不构成 reject 理由）
- **Director 判断**：R2 论证更有说服力。Mistral n=6 的 CI 均不含零且结论方向与 n=10 模型一致。定为 Should-Fix，但应优先补跑。

---

## Questions（需作者澄清）

1. 为何不增加中间污染水平（5%/10%/25%/30%）？QLoRA 成本极低，这是有意的 scope 限制还是资源约束？
2. "57/60 model-benchmark cells" 的 60 具体构成是什么？（12 models × 5 benchmarks = 60?）
3. Fixed-θ 的 clean-model mean anchor 在实际部署中不可得——论文提到的 cross-benchmark θ estimation 替代方案是否有实验评估？
4. GRPO 后 ℓz* 从 2.91 增至 7.69——这与 "residual contamination pattern" 叙事如何一致？是否可能是 GRPO 本身引入新 aberrance？需 clean+GRPO control 排除。
5. Llama/Mistral 为何未评估 ARC-C？
6. 从 Karabatsos (2003) 的 36 种 person-fit 统计量中为何仅选 ℓz* 和 HT？是否有系统性比较？
7. PSN-IRT 的 4PL 参数校准中是否包含本实验模型系列的变体？若包含，是否存在 information leakage？
8. MML-EM refit 得到 r_a=0.127 的实验设置是什么？数据来源和模型配置？

---

## Missing References

**高相关性（应讨论）**：
1. PaCoST (EMNLP 2024 Findings) — performance-based 污染检测
2. Don't Make Your LLM an Evaluation Benchmark Cheater (Zhou et al., 2023)
3. How Much Can We Forget about Data Contamination? (arXiv 2410.03249)
4. MEDIRT (arXiv 2509.24186) — IRT 应用于 LLM 评估

**中等相关性（建议引用）**：
5. Data Contamination Calibration for Black-box LLMs (arXiv 2405.11930)
6. Reise (1990) — person-fit 作弊检测
7. Levine &amp; Drasgow (1988) — appropriateness indices 分类
8. Embretson &amp; Reise (2000) — IRT 教科书

**低相关性（可选）**：
9. Detecting Benchmark Contamination Through Watermarking (arXiv 2502.17259)

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（耗时 ~3 分钟）
**发现**: 5 项 info 级别，0 项 critical/warning

1. **Page 5**: Figure 2 heatmap 中浅蓝单元格上白色注释文字对比度低，灰度打印可能不清晰——建议对浅色单元格使用深色文字
2. **Page 6**: Figure 3 单栏图轴标签和 legend 文字接近可读性下限（约正文字号 70%）——若空间允许可放大
3. **Page 8**: Figure 4 双 y 轴设计增加认知负荷——考虑拆为上下两个 sub-panel
4. **Page 12**: 单页 5 个表格（Tables 4-8）视觉密度高——作为附录可接受
5. **Page 5**: Figure 2 灰色缺失单元格建议图内添加 "not tested" 注脚

---

## Overall Assessment

**评分**: 3.0 — Findings

**置信度**: 4/5（两位 Reviewer 独立给出一致评分，交叉验证后共识度高）

**理由**:

论文的跨学科连接（IRT person-fit → LLM contamination detection）是真正新颖的贡献，DiD 设计优雅，学术严谨性高。然而，四个核心问题将其推至 Findings 而非主会议：

1. **核心 claim 证据不足**：Non-monotonic dose-response 作为首要发现仅基于两个污染水平，且仅在 Qwen 一个模型上观察到，不构成 characterization
2. **Framing 偏差**："Minimal-information point" 实际强依赖外部 4PL item bank，fixed-θ 还需 clean baseline——信息需求被系统性低估
3. **生态效度**：QLoRA SFT 与 Introduction 的 pretraining contamination 动机脱节，高 Cohen's d 可能反映 SFT 特有效应
4. **Post-RL overclaim**：N=1 结果被列为核心 contribution，与正文的审慎 hedging 不匹配

论文在 characterization 定位、诚实 self-assessment、和方法论严谨性上表现出色（Appendix 充实），适合 Findings 接收。升级至主会议需要：补充中间污染水平、修正 framing、扩展实验规模、降级 post-RL finding。

---

## Detailed Comments

### Abstract/Introduction
- Abstract ~250 词偏长，建议精简至 150-180 词，压缩 post-RL 描述
- "binary response patterns alone" (Abstract line 2) 改为 "binary response patterns from the target model, combined with externally calibrated item parameters"
- "the first systematic characterization" claim 需验证是否确实是首次——建议检查 MEDIRT 等近期工作
- Introduction 应前置 SFT scope 限定（当前第 57 行才出现）

### Method (Section 3)
- Section 3.1: MML-EM refit r_a=0.127 实验细节需补充（至少 appendix）
- Section 3.2: DiD 假设（clean 和 contaminated 共享相同 misfit）的成立条件需更显式讨论——contamination 可能改变 item 间依赖结构
- Section 3.3: "n=10 seeds each" 需在首次出现时标注 Mistral n=6 及原因，不应仅在 Table 脚注

### Results (Section 4)
- Section 4.2: "Non-monotonic dose-response" 标题建议改为 "Observed dose-response pattern"；增加 15% vs 50% 的正式统计检验
- Section 4.3: "negative correlation" 基于 3 个数据点——改为 "observed trend"
- Section 4.4: 增加 ConStat 对比或详细定性分析；补充具体 practitioner use case
- Section 4.5: 标题建议改为 "Preliminary Observation: Post-RL Residual Pattern (N=1)"；讨论 ℓz* 增加的可能解释（GRPO-induced θ-shift vs contamination residual）

### Discussion (Section 5)
- 应显式讨论 ConStat 的互补关系（当前仅一句话）
- "minimal information point" 措辞需与修正后的 Abstract 对齐

### Limitations
- 当前涵盖充分但可增加：(1) IRT local independence/unidimensionality 违反的具体影响量化引用（Sinharay 2016）；(2) 4PL item bank 作为 critical dependency 的替代方案

### Appendix
- Appendix C 的 n=3 结果标注 "superseded by n=10" 很好——建议考虑移除以节省空间
- Bootstrap CI: 正文或 Appendix 补充 BCa sensitivity check

### Figures
- Figure 1: "red diamonds" 需确保灰度可辨识——建议改用形状区分（× vs ○）
- Figure 2: 浅色单元格文字改深色
- Figure 3: 放大轴标签字号
- Figure 4: 考虑拆为 sub-panels 减少双 y 轴认知负荷

### References
- 33 篇引用偏少（EMNLP long paper 常见 40-50 篇），需补充 PaCoST、MEDIRT 等
- 显式说明 ℓz* + HT 选择理由（引用 Karabatsos 2003）