---
round: 6
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T10:14:58.528938+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — gen-depth-contamination (Round 8)

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性)
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文提出 "generational depth estimation" 任务，定义 K*（discrimination boundary）衡量递归合成文本中相邻代际可被可靠区分的最大深度。使用 15 维统计特征 + OBD-LightGBM 分类器，在 9 个模型配置（5 个架构族, 1B–14B）、3 个领域、4 种解码策略上测得 K*∈{1,2,3}：web 文本 K*=2（8/9 配置），arXiv K*=3，Wikipedia K*=1。论文还展示了 80–92% 的跨模型迁移率和下游数据过滤验证。

---

## Strengths

**S1. 问题定义新颖且形式化清晰** [R1-S1, R2-S1, 共识]
Generational depth estimation 作为新任务首次明确提出。K* 通过 AUC 阈值操作化，形成可复现的测量框架。在现有 binary detection 和 model collapse 文献之间填补了重要空白。

**S2. 实验覆盖面广且统计严格** [R1-S2/S3, R2-S2, 共识]
9 模型×3 域×4 解码策略。Bootstrap CIs、permutation tests、ANOVA、Holm-Bonferroni、Cohen's h。对 marginal cases 的透明报告（Qwen-cont CI lower bound 仅超 θ 0.002、LLaMA-8B borderline）值得肯定。统计处理在同类工作中高于平均水平。

**S3. 域排序结果有洞察力** [R1-S2, R2-S3, 共识]
arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1) 在跨模型、跨评分器条件下一致保持。Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，支持域主导而非模型主导。

**S4. 消融分析充分** [R1-S4, R2-S4, 共识]
Self-BLEU 移除消融、特征子集稳定性、segment length、neural probe 对比、binary detector 对比、阈值敏感性、dose-response——系统性地覆盖了主要质疑角度。

**S5. 写作质量与诚实报告** [R1-S5, R2-S5, 共识]
无明显 AI 写作痕迹（无解释性 em-dash、无过度分段、无 -ing 短语结尾）。Limitations 列出 7 条具体限制并在 Appendix 扩展。边界案例均被主动报告。

---

## Weaknesses

### Critical

**C1. θ=0.60 阈值的"三重论证"包装过度** [R1-W1, R2 AGREE]

Section 3.1 的三条论证存在系统性问题：
- 论证 (a) Cohen's h ≈ 0.20：脚注已自承为 "motivating analogy rather than a formal justification"，但正文将其作为"第一条独立证据"展示，措辞不匹配
- 论证 (b) permutation test：仅证明 AUC > chance (0.50)，对 θ 的具体取值没有区分力——任何 θ∈(0.50, observed AUC) 都通过此检验
- 论证 (c) gap observation：本质是 post-hoc 数据描述，不应包装为"独立证据"

实际后果：θ=0.55 时两个 Qwen 配置升至 K*=3；θ=0.70 时全部降至 K*=1。OLMo (1v2=0.6145) 和 Qwen-cont (1v2=0.6112) 的 K*=2 余量仅 1–1.5 pp。K* 是论文核心贡献，θ 选择的论证方式直接影响可信度。

R2 补充：Figure 3 和 Table 8 展示的 gap-based robustness 分析实际上比三条论证更有说服力，应作为主要支撑。

**建议**: 放弃"三条独立证据"包装，坦率承认 θ 为 data-driven operational choice。重点展示 Figure 3 的 gap-based robustness 分析和域排序的 θ-invariance。

**C2. "Generator-independent" / "text-intrinsic" 措辞与 scorer 依赖性存在系统性矛盾** [R1-W2, R2 AGREE — R2 称此为"R1 最精准的技术批评"]

多条证据表明 K* 对 scorer 选择敏感：
- Cross-scorer 验证：Qwen-cont K* 从 2 降至 1（1v2 AUC: 0.6112→0.5923/0.5858; Table crossscorer）
- Wikipedia：same-family scoring K*=2，cross-family 降回 K*=1（Δ = -2.4pp; Table wiki_domain）
- ANOVA Scorer η²_p = 0.192：论文淡化为 "practically minor relative to Depth-Pair"，但按 Cohen convention 为 large effect。与此同时，Section 3.1 使用 Cohen's h convention 论证 θ=0.60——对同一统计框架的选择性引用
- 9 个 C4 配置中至少 2 个（Qwen-cont, Mistral）换 scorer 后 K* 改变
- arXiv cross-scorer：Mistral-7B CI [0.593, 0.622] 和 Qwen-7B CI [0.584, 0.613] 均跨越 θ

**建议**: (1) "generator-independent" → "generator-transferable under fixed scorer"; (2) Introduction contribution list 增加 scorer 依赖作为 caveat; (3) ANOVA η²_p 解读与 Section 3.1 对 Cohen convention 的使用保持一致。

---

### Major

**M1. 下游过滤效应量极小，实际意义不确定** [R1-W3, R2-W2/W3, 高度共识——两位均认为此为论文最大实践弱点]

- 100% 合成设定：binary-ours MMLU 0.5941 vs. no-filter 0.5865 = +0.77pp，但 base model = 0.6018，所有策略均在退化
- Dose-response 10% 污染：binary vs. no-filter = +0.21pp MMLU、+0.38pp HellaSwag（MMLU 差异在 30%/50% Holm-Bonferroni 校正后不显著）
- Pythia 复制：+0.17pp MMLU（baseline 0.2568 近乎随机）
- "~50% reduction in degradation" 是相对量，绝对量 <1pp
- Section 5 标题 "K*-Aware Data Filtering" 但实际因 K*=2 退化为 binary filtering，名不副实
- **关键缺失验证**：arXiv (K*=3) 域的 graduated vs. binary filtering 对比——这是展示 K*-aware filtering 真正增量价值的唯一途径

**建议**: (1) 明确区分"统计显著"和"实际有意义"; (2) 在正文报告绝对和相对改善量; (3) 将 filtering 降级为 downstream validation 而非独立 contribution; (4) 理想情况下补充 arXiv graduated filtering 实验。

**M2. 方法技术贡献偏薄** [R2-W1 critical, R1 REBUT → Review Director 降为 major]

方法为 15D 手工统计特征 + OBD (Frank & Hall 2001) + 现成 LightGBM 的直接组合，无新模型架构、新训练目标、新理论结果。

R1 反驳：本文是 measurement paper，ARR H7 类别接受此类工作；neural probe 对比（Section 4.4）证明 handcrafted features 在 transferability 上的 trade-off 合理性。

**Review Director 判断**: 降为 major。EMNLP Findings 接受 empirical/measurement studies，但方法创新不足确实限制了主会议竞争力。

**M3. DPI 理论动机技术精度不足** [R1-W4, R2 AGREE with nuance]

DPI 保证 I(X; Y_k) 单调递减，但 K* 基于相邻代际 (Y_{k-1}, Y_k) 的可区分性——两者不是同一量。I(X; Y_k) → 0 不蕴含 Y_k 与 Y_{k+1} 在分布上趋同。"Together with Markov chain convergence" 需要遍历性/不可约性假设，LLM 输出空间是否满足未讨论。

R2 补充：非零温度采样可论证 full support（从而满足遍历性的一个必要条件），但论文跳过了这一步。

不影响经验结果有效性，但影响 "information-theoretic guarantee" 叙事的严谨性。

**建议**: 降低理论声明强度，定位为 motivation 而非 guarantee。区分 DPI 和 Markov chain convergence 各自的贡献和所需假设。

**M4. "Domain structural complexity" 缺乏操作化定义** [R1-W5, R2 AGREE]

论文反复声称 "source-domain structural complexity" 是 K* 的首要因素（Section 4.5, Section 6），但从未被形式化定义或独立测量。arXiv K*=3 的解释（"formulaic features: LaTeX formatting, citation patterns, mathematical notation degrade slowly"）引发替代假说：分类器可能在检测 LaTeX 格式退化而非内容层 depth signal。JSD 的 λ 值是 K* 的后果而非原因。

**建议**: (a) 对 arXiv 做 LaTeX markup 去除后的 ablation，验证 K*=3 是否依赖格式特征; (b) 或坦率承认为经验性术语，给出可测量的 proxy（如 vocabulary entropy、格式标记密度）。

**M5. Related Work 引用密度偏低，重要方向缺失** [R2-W4, R1 partial AGREE]

34 篇引用对 EMNLP 偏少。缺失方向：
- **Watermarking**（Kirchenbauer et al. 2023）——作为合成文本追踪的替代范式完全未讨论，两位 Reviewer 独立指出
- **大规模数据质量工程**（FineWeb/Penedo et al. 2024）——data curation 段仅 2 行
- **早期统计检测**（GLTR/Gehrmann et al. 2019）——与本文 feature 设计高度相关
- Related Work 仅 22 行正文 4 个 paragraph

R1 建议补 3-5 篇，R2 建议 8-10 篇。**Review Director 判断**: 至少补充 watermarking 段（proactive vs. post-hoc 对比）和 data curation 段扩展，4-6 篇。

**M6. 论文身份不够清晰** [R2-W5, R1 REBUT]

同时声称 measurement/detection/curation 三类贡献，权重不均且逻辑连接不紧密。K*=2 实际上否定了 web 文本上 depth-aware curation 的必要性，使 curation 叙事自相矛盾。

R1 反驳：Primary identity 为 measurement paper 已清晰，filtering 是 downstream validation。建议降为 minor。

**Review Director 判断**: 维持 major。三线并行的结构确实造成审稿人困惑，需要重组 contribution list（primary: measurement, secondary: transfer, tertiary: validation）。

**M7. Prompt-chain K* 对实际部署场景适用性边界** [R1-Q3, R2-Q3, 共识]

Prompt-chain K*=2 而 retrain-chain K*≥4（Appendix E, Table 6），差距巨大。实际 web contamination 更可能涉及 retrain-chain（模型在前代输出上微调后生成新内容）。论文的 K* 框架对最需要它的场景（retrain-chain）的适用性需要更明确讨论。Limitations (2) 已承认但措辞较轻。

---

### Minor

**m1. Abstract 数字堆砌** [R2-W6, R1 AGREE]
~190 words 中 ~15 个数字，审稿人 30 秒内无法消化。建议保留 2-3 个关键数字（K*=2/3 域差异 + transfer retention）。

**m2. 跨模型迁移 "80–92%" 呈现方式** [R1-W6, R2 partial REBUT]
Retention rate 作为 transfer metric 合理（控制了任务难度），但 Abstract 未说明是 retention rate 而非 absolute accuracy（基线 6-class ~0.35），可能误导读者。建议 Abstract 明确说明 "80–92% accuracy retention"。

**m3. Qwen 家族过度代表** [R2-W7, R1 AGREE but low severity]
9 配置中 5 个 Qwen 变体。不影响核心结论但削弱"跨架构"claim。建议 Limitations 更明确承认。

**m4. arXiv/C4 样本量差异影响 CI** [R1-W7, R2 AGREE]
C4 子采样至 n=2,200 后 K* 降至 1——暴露 C4 K*=2 在小样本下不稳定。论文应讨论至少需要多少样本才能 reliably 判定 K*=2，这对实践部署至关重要。

**m5. ANOVA per-fold AUC 非独立性** [R1-Q2, R2 AGREE]
N=300 中 per-fold AUC 作为 DV 时 fold 非独立性可能导致 Scorer 显著性被高估。主要结论不太可能受影响。

**m6. Zero-shot baseline 缺 prompt 细节** [R1-Q4, R2 AGREE]
GPT-5.5 和 Claude Opus 4.6 的 prompt template、input format 未报告，影响 reproducibility。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成共识（交叉回应后确认）：

1. **下游 filtering 效应量不足以支撑 contribution 级 claim** [R1-W3, R2-W2/W3] — 论文最大实践弱点
2. **θ=0.60 的"三重论证"包装需修正** [R1-W1, R2 AGREE] — 改为 data-driven choice
3. **"Generator-independent" 措辞与 scorer 依赖矛盾** [R1-W2, R2 AGREE] — 改为 "generator-transferable under fixed scorer"
4. **Watermarking 引用必须补充** [R1-Q5/Missing, R2-Missing #1] — proactive vs post-hoc 讨论
5. **Prompt-chain K* 适用性边界需更明确讨论** [R1-Q3, R2-Q3] — retrain-chain K*≥4 vs prompt-chain K*=2
6. **DPI 理论引用精度需改进** [R1-W4, R2 AGREE with nuance] — motivation not guarantee
7. **Domain structural complexity 缺操作化定义** [R1-W5, R2 AGREE]
8. **引用密度偏低** [R1-Missing, R2-W4] — 至少补充 4-6 篇

## Reviewer Divergence [REBUT]

1. **方法技术新颖性的严重性**：R2 定为 critical（EMNLP 对 method contribution 有期望），R1 反驳降为 major（measurement paper，ARR H7 类别）。**Review Director 采纳 major**。
2. **论文身份清晰度**：R2 定为 major，R1 反驳降为 minor（primary identity 已明确为 measurement）。**Review Director 维持 major**。
3. **引用补充量**：R1 建议 3-5 篇，R2 建议 8-10 篇。**Review Director 判断 4-6 篇**。
4. **Transfer retention rate 呈现**：R1 认为掩盖低绝对精度，R2 部分反驳（retention rate 控制了任务难度）。**Review Director 判断 metric 合理但 Abstract 需澄清**。

---

## Questions（需作者澄清）

Q1. θ=0.60 的选择是否应坦率定位为 data-driven choice 而非三条独立证据支撑？
Q2. arXiv (K*=3) 域是否有 graduated vs. binary filtering 对比实验？这是展示 K*-aware filtering 增量价值的关键。
Q3. Prompt-chain K*=2 vs retrain-chain K*≥4——论文的 K* 框架对实际 web contamination（更可能涉及 retrain-chain）的适用性如何？
Q4. Cross-scorer ANOVA N=300 中 per-fold AUC 的非独立性是否被处理？
Q5. Zero-shot baseline (GPT-5.5, Claude Opus 4.6) 的 prompt template 和 input format？
Q6. OBD vs. multiclass LightGBM 的 MAE 差异 (0.984 vs. 1.016) 是否有配对统计检验？
Q7. K* 与 K_theory 之间的 gap 估计？Neural probe K*=3 (Qwen) 是否暗示 15D 特征集显著低估了可辨别深度？

---

## Missing References

**必须补充** [两位 Reviewer 独立共识]：
- Kirchenbauer et al. (2023) "A Watermark for Large Language Models" (ICML 2023) — watermarking 作为替代追踪范式
- Penedo et al. (2024) FineWeb/RefinedWeb — 大规模数据质量工程

**强烈建议**：
- Gehrmann et al. (2019) "GLTR: Statistical Detection and Visualization of Generated Text" (ACL 2019) — 早期统计检测，与本文 feature 设计相关
- Pan et al. (2024) "Waterfall" (EMNLP 2024) — watermarking provenance
- Ippolito et al. (2020) "Automatic Detection of Generated Text is Easiest when Humans are Fooled" (ACL 2020)
- 1-2 篇 ordinal classification survey（现仅引 Frank & Hall 2001）

---

## External Review (Stanford Agentic Reviewer)

未配置，跳过。

---

## Overall Assessment

**Score: 3.0 (Findings)**
**Confidence: High**（两位 Reviewer 独立得出一致评分 3.0，交叉回应后共识进一步加强，无核心评判分歧）

### 评分依据

本文提出了一个新颖且有价值的问题（generational depth estimation），实验覆盖面广、统计处理严谨、limitations 报告诚实。这些是论文的核心优势，足以支撑 Findings 收录。

但存在系统性问题阻碍主会议接收：

1. **核心参数 θ 的论证方式需要更诚实的定位**——三条"独立证据"中两条实质上不成立，应坦率定位为 data-driven choice
2. **"Generator-independent" framing 与 scorer 依赖性之间存在需要正面解决的矛盾**——至少 2/9 配置在换 scorer 后 K* 改变，ANOVA scorer effect 按 Cohen convention 为 large
3. **方法层面为已有技术的直接组合**——15D features + OBD + LightGBM 缺乏技术深度（但 measurement paper 可接受）
4. **K*=2 使论文的 depth-aware curation 叙事在 web 文本上等价于已有的 binary detection**——与 Drayson et al. (2025) 的实践增量有限
5. **下游 filtering 效应量 <1pp**——统计显著但实际意义存疑，且缺少 arXiv K*=3 的 graduated filtering 验证

这些问题不否定经验发现的有效性，但 claims 与 evidence 之间存在落差。作为 Findings paper，问题新颖性 + 实验系统性的组合充分。作为 Main Conference paper，需在 framing 严谨性、方法深度或下游实用性上取得实质性突破。

### 官方维度打分（ACL ARR Review Form，Reviewer 平均）

| 维度 | R1 | R2 | 平均 | 理由摘要 |
|------|----|----|------|----------|
| Soundness | 3.0/5 | 3.5/5 | 3.25/5 | 实验设计合理，统计恰当；θ 论证/scorer 依赖/DPI 精度存在 gap |
| Excitement | 3.5/5 | 2.5/5 | 3.0/5 | 问题新颖，K* 有学术潜力；K*=2 限制实践 excitement，方法无创新 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 | 特征定义、超参数、数据集描述充分；代码承诺释放 |
| Overall | 3.0/5 | 3.0/5 | 3.0/5 | Findings 水平：新颖问题 + 充分实验 + 诚实报告，但 claims 需校准 |
| Confidence | 4/5 | 4/5 | 4/5 | 两位仔细阅读全文和附录，判断一致 |

---

## Detailed Comments

### Abstract
信息密度过高（~15 个数字在 ~190 words 中）。保留 K*=2/3 域差异 + 一个 transfer 数字即可。"Generator-independent statistical features" → "generator-transferable statistical features (under fixed scorer)"。"80–92% cross-model transfer" → "80–92% accuracy retention among continuation-mode generators"。

### Introduction
Contribution list 需重组。当前 (a)(b)(c)(d) 混合 measurement/detection/curation。建议：primary = K* definition + empirical mapping (measurement), secondary = cross-model transfer methodology, tertiary = downstream filtering validation (降级)。每条 contribution 需有对应 section/table 支撑。

### Section 3.1 (Threshold Choice)
放弃"三条独立证据"包装。保留 gap-based analysis (Figure 3) 作为主要支撑，坦率承认 θ 为 data-driven operational choice。讨论不同 θ 下 K* 的完整分布，让读者自行判断。

### Section 3.1 (DPI Motivation)
区分 DPI（保证 I(X;Y_k) 衰减）和 Markov chain convergence（保证相邻代际最终不可区分）各自的贡献。讨论 LLM 输出空间满足遍历性的条件（如非零温度采样赋予 full support），或降低声明强度为 motivation。

### Section 3.2 (Method)
OBD vs. multiclass LightGBM 比较缺配对统计检验。Self-BLEU 部署替代方案的讨论充分（14D ablation |ΔAUC|≤0.003），但 deployment feature set ≠ training feature set 应被更明确承认。

### Section 4.2 (Transfer/Scorer)
"Generator-independent" → "generator-transferable"。ANOVA η²_p=0.192 的解读需与 Section 3.1 对 Cohen convention 的使用保持一致——不能在 θ 论证中引用 Cohen 作为支撑、在 scorer effect 中又淡化 Cohen 的分类标准。

### Section 4.5 (Domain)
"Structural complexity" 需定义或降级为经验性术语。arXiv K*=3 是否部分依赖 LaTeX 格式特征（而非内容层 depth signal）需要讨论或 ablation。给出可测量的 structural complexity proxy。

### Section 5 (Filtering)
标题 "K*-Aware Data Filtering" 名不副实（K*=2 → 实际为 binary filtering）。需明确区分统计显著性和实际意义（绝对改善 <1pp）。100% synthetic 设定在首次提及时标注 upper-bound caveat。缺 arXiv graduated filtering 验证——这是核心实验缺口。

### Section 6 (Discussion)
需正面讨论 K*=2 作为 negative result 的积极意义（measurement value, domain diagnostic, binary-sufficiency 定量证据）。DPI 引用精度改进。Prompt-chain 适用性边界需更明确讨论。Mistral K*=1 例外需机制讨论。

### Related Work
补充 watermarking 段（Kirchenbauer et al. 2023 + proactive vs. post-hoc 对比）。扩展 data curation 段（FineWeb/Penedo et al. 2024）。补充 GLTR (Gehrmann et al. 2019) 作为早期统计检测先驱。目标引用数 40+。

### Limitations
已较充分。建议补充：(1) sample size 对 K*=2 判定的影响——至少需多少样本 reliably 判定？(2) Qwen 过度代表。(3) Prompt-chain 适用性边界措辞加强。

### Appendix
Zero-shot baseline (GPT-5.5, Claude Opus 4.6) 需补充完整 prompt template 和 input format。

---

## Issue Tracker 同步

已更新 `review_issues.yaml`。本轮新增 12 条 issue（2 critical, 7 major, 9 minor），复发 8 条 Round 7 in_progress issue。详见 tracker 文件。