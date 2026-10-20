---
round: 25
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T05:01:25.912796+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告（Fresh Review）

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: R1（方法严谨性+实验设计）+ R2（新颖性+完整性+写作质量）
**审稿轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文提出 generation depth classification 任务（gen-0/gen-1/gen-2+），将传统二元检测扩展到递归生成深度分类。核心发现是 differential depth response (DDR)：7 个手工特征在 8 个 base model generators（5 families, 0.6B-8B）上系统分为 drifting (3)、intermediate (1)、near-stationary (3) 三组。XGBoost 集成分类器在 LOGO 评估下达到 leak-free binary F1=0.694。论文实验设计严谨（LOGO/LOFO/seed 控制/length confound），统计检验覆盖面广，但 DDR 的新颖性有限、base model 限制严重削弱 impact、下游应用价值未建立。

---

## Strengths

**S1. 问题形式化有价值且定位清晰。** 将递归生成深度分类作为独立任务首次系统性提出，与 binary detection、source attribution、production mode classification 形成正交维度。与 model collapse 文献互补但不重叠。[R1, R2 共识]

**S2. 实验设计严谨程度高于该领域平均水准。** Binary F1 排除 gen-0 消除 seed sharing 偏差；独立 seed 控制实验（F1=0.680）确认信号非 seed-specific；length-matched subsampling 三重控制 confound。LOGO/LOFO 双协议验证跨 generator/family 泛化。[R1, R2 共识]

**S3. 统计检验规范且多层验证。** Bootstrap CI (n=1000)、McNemar test、Bonferroni 校正、Levene test、KS test、TOST 等价性检验、Glass's Δ、Cliff's δ 等多种工具互相印证。这是该领域少见的严谨程度。[R1, R2 共识]

**S4. 对自身方法局限的透明度高。** "DDR is an empirical decomposition, not a claimed universal law"（§5 L6）。Limitations 对 base model 限制、temperature sensitivity、downstream 无效等问题的讨论诚实。论文明确 disclaim DDR 的 universality。[R1, R2 共识]

**S5. Baseline 比较定位诚实。** §4.3 明确将比较定位为 "contextualize depth discrimination ability rather than claim competitive advantage"，避免过度宣传。[R1]

**S6. 写作 AI 痕迹已基本清除。** 无 em-dash/en-dash（数字范围除外），无 Furthermore/Moreover/Additionally 堆叠，无黑名单用词。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [Critical, R1+R2 共识] DDR 新颖性不足以支撑 Main Conference 核心贡献。**
DDR 本质上是已知特征（NLL mean/TTR/hapax）在递归生成下行为差异的系统化表述。三个 drifting features 共享 92.3% variance（PCA），TTR-hapax r=0.97，"7-feature ensemble"实际是 ~4 维系统。在 model collapse 文献（vocabulary diversity 下降、NLL 分布 shift）的背景下，"location 特征漂移、shape 特征不变"是预期之中的发现。DDR 的"命名"（drifting/intermediate/near-stationary）和 3/1/3 partition 增加了术语但未带来概念突破。R1 补充：DDR 跨 8 个 generator 的一致性有价值，但对 Main 不够。

**N2 [Critical, R1+R2 共识] Base model 限制严重削弱实际 impact。**
Instruction-tuned models 下信号崩溃（OLMo-Instruct LOGO F1=0.338 vs 0.763 base），而 web 文本主要来自 instruction-tuned/RLHF-aligned models。Downstream 实验（n=3 seeds）显示 depth-aware curation 与 random subsampling 统计等价，且 random 反而略优（PPL 2367 vs 2387）。**关键未利用发现**：R1 在交叉回应中指出，instruct model 的 entropy mean ρ 从 -0.60 反转为 +0.48（6/7 features 反号 for OLMo/Qwen），说明 depth signal 存在但方向反转——retrain classifier with instruct data 可能恢复 F1。这一发现本身可成为独立 contribution，但论文仅用一句话带过。

**N3 [Critical, R1 提出 + R2 同意] Cohen's d 阈值 (0.75/0.10) 缺乏 principled 推导。**
DDR tri-partition 的核心分区阈值是 post-hoc 选择的——"the drifting boundary reflects the natural gap between hapax ratio (d=0.76) and entropy std (d=0.55)"是在看到所有 d 值后描述 gap，而非 pre-specified。0.10（near-stationary）阈值无类似 gap 论证。k=3 clustering 时 entropy_min 自成一类（Appendix V Table 25），说明 3/1/3 非最自然的数据驱动分区。R2 补充：若 partition 变化但 F1 不变，反而削弱 DDR 作为核心贡献的必要性。

### Should-Fix（影响评分但不一票否决）

**W1 [Major, R1 提出 + R2 降级] TOST 等价性检验对 near-stationary 特征部分失败。**
Tail decay 仅 4/8 generators 通过 TOST（ε=0.20），entropy max 6/8。R1 初评 Critical，R2 认为 Major 更合理——primary partition (k=2, silhouette=0.632) 不受影响，即使 tail decay 重分类为 intermediate (3/2/2) 核心叙事不变。**Director 采纳 Major。**

**W2 [Major, R1 提出 + R2 rebut 成功，降级] 异方差下 pooled Cohen's d 作为主要分区指标。**
Levene tests 拒绝等方差（方差比 1.86-2.21），但论文已在 Appendix V 提供 Glass's Δ + Cliff's δ 三重验证，partition gap ≥9.5× 在所有 metrics 下一致。正文 §4.2 也引用了 heteroscedasticity-robust metrics。R1 初评 Critical，R2 rebut 成功。**Director 降为 Major**——但 Glass's Δ 应在正文中更突出展示，而非仅放 Appendix。

**W3 [Major, R1+R2 共识] TTR-hapax r=0.97 + PCA 92.3%：保留三个 drifting 特征的理由是循环论证。**
"Individual features enable DDR decomposition" → 但 DDR 分解需要三个特征 → 三个特征证明 DDR 分解。PC1 替代仅损失 1.1pp (§4.2)。联合移除 TTR+hapax 的消融未报告。

**W4 [Major, R2 提出 + R1 同意] Generator subset 不一致（5/6/8-gen 混用）。**
至少 6 种 subset 配置分布于正文和附录。跨实验比较困难——温度消融 4-gen 结果能否推广到另外 4 个 generator 未讨论。

**W5 [Major, R2 提出 + R1 同意] 遗漏重要相关工作。**
Varshini et al., "Unveiling Attractor Cycles in Large Language Models" (ACL 2025) 直接分析连续 paraphrasing 中的 attractor 周期，与论文多处使用的 "generation attractor" 概念直接相关但未引用。

**W6 [Major, R1+R2 共识] Downstream 实验 n=3 seeds 严重 underpowered。**
Cohen's d 被极小 pooled std 膨胀到 86-120（论文自承 unreliable）。Discussion §5 基于此 null result 转向 "structure identification" framing，但如果 10+ seeds 后发现微弱效果，整个 framing 需要改变。

**W7 [Major, R1+R2 共识] Instruct model 退化缺乏 mechanistic 分析。**
论文仅描述性报告 F1 下降和 ρ 反号，未分析 WHY（特征分布变化？DDR 分区失效？RLHF 改变递归动态？）。R1 强调这是论文中最有潜力的 unrealized finding。

**W8 [Major, R2 提出 + R1 同意] Contribution 分量不均。**
C1（task formulation）和 C3（boundary conditions）更像标准实验设计而非独立贡献。DDR（C2）是唯一实质性发现。"一个观察被拆成三条来凑分量"的印象。

**W9 [Major, R1 提出 + R2 partially agree] Reference model same-family 偏差。**
Pythia-410M 与 Pythia generators 同家族。Cross-reference 验证仅在 5-gen subset 上（spread 0.013）。Pythia generators 获最高 F1 (0.724) 可能部分归因于亲和性。

**W10 [Major, R1 提出 + R2 同意] 温度消融 OLMo checkpoint 不一致。**
温度实验用 OLMo-2-0425-1B，主实验用原始 OLMo-2-1B-hf（已不可用）。Checkpoint 差异与 temperature 效应混淆。

**W11 [Major, R2 Q4 提出 + R1 同意] Cross-model chains F1=0.764 > single-gen LOGO F1=0.694 未解释。**
可能原因：generator heterogeneity 放大 depth signal（含 generator identity confound）。论文呈现为 positive evidence 但未排除 confound。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：
1. DDR 新颖性对 Main Conference 不足，Findings 级别合适 [N1]
2. Base model 限制是论文最大的 practical constraint [N2]
3. Cohen's d 阈值是 post-hoc gap-driven，非 principled [N3]
4. TTR-hapax 冗余和 PCA 单维度是实质问题 [W3]
5. Downstream n=3 underpowered，不足以支撑 framing 转向 [W6]
6. Instruct model ρ 反转是最有潜力的 unrealized finding [W7]
7. Contribution 分量不均 [W8]
8. ", confirming" 9+ 次是 AI 写作标志 [M1]

## Reviewer Divergence

以下问题经交叉讨论后解决（无遗留分歧）：
1. **R1-N3 (异方差/pooled d)**: R1 初评 Critical → R2 rebut（三重验证 + ≥9.5× gap）→ **Director 降为 Major** [W2]
2. **R2-W4 (引用验证)**: R2 初评 warning → R1 rebut（OpenAlex false negatives，非实质问题）→ **Director 采纳 R1 rebut，不列入报告**
3. **R1-Q3 (cross-ref subset)**: R2 rebut（0.013 spread 远小于 9.1pp generator 间差异）→ 降为 Minor 建议
4. **R1-Q4 (fundamental claim)**: R2 rebut（论文三处明确否认 DDR 是 universal/fundamental）→ 不构成问题

---

## Questions（需作者澄清）

**Q1.** DDR 的 location/shape decomposition 是否有理论解释？为什么 softmax 在递归条件下 location shift 但 shape 稳定？是否与 temperature 作为 shape 控制参数相关？[R1+R2 共识]

**Q2.** 为什么不直接用 PC1 替代三个 drifting features？如果 DDR decomposition 的解释性价值是唯一保留理由，为什么分类系统中不使用 PC1 简化？[R1+R2 共识]

**Q3.** Instruct model 的 entropy mean ρ 反号（-0.60→+0.48）是否意味着 depth signal 仍存在但方向反转？如果在 instruct data 上 retrain classifier，F1 是否恢复？这是论文应该展开的最重要方向。[R1+R2 共识]

**Q4.** Cross-model chains F1=0.764 > single-gen LOGO F1=0.694——是 generator heterogeneity 放大 depth signal，还是存在 generator identity confound？[R2 提出, R1 同意]

**Q5.** Depth classification 的 practical ceiling（Bayes error rate）是多少？QLoRA 的 binary F1 未报告，知道它可以帮助判断 7-feature ensemble 距 ceiling 多远。[R1]

**Q6.** 更深的链（gen-5+）中 DDR 特征是否完全 converge（inter-class KS→0）？这可为 attractor 叙事提供更强支撑。[R1]

---

## Missing References

1. **Varshini et al., "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" (ACL 2025)** — 直接分析连续 paraphrasing 中的 attractor 周期，与论文 "generation attractor" 概念直接相关。[R1+R2 共识]
2. **"How to Synthesize Text Data without Model Collapse?" (2024)** — 递归生成质量退化与 data provenance 叙事相关。[R2]
3. **Ordinal classification 方法文献覆盖不足** — CORAL/CORN 仅在 Appendix 一笔带过，正文 task formulation 为 ordinal classification 但无充分引用。[R1]

---

## External Review

外部审稿（Stanford Agentic Reviewer）：**未配置**。项目 config 中未启用 `external_review.paperreview_ai`。

---

## Overall Assessment

**Overall: 3.0 — Findings（可被 Findings 接收）**
**置信度: 4/5（两位 Reviewer 均仔细阅读全文含 29 页附录）**

### ACL ARR 维度评分（两位 Reviewer 平均）

| 维度 | R1 | R2 | 平均 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 2.5 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4.0 | 4.0 | 4.0 |

### 判断依据

**支持 Findings（3.0）的理由：**
- 问题形式化（depth classification beyond binary）有价值
- 实验设计和统计规范高于该领域平均
- DDR 三分区作为分析框架有整理价值
- 对自身 limitations 的透明度是正面信号

**不支持 Main Conference（≥3.5）的理由：**
- DDR 新颖性有限——本质是已知特征的行为分类，非概念突破
- Base model 限制严重——web 场景下几乎不适用
- Downstream 实验否定了实用价值
- 贡献分量不均，核心 insight 可用一段话概括
- Feature 冗余严重（7 features → ~4 独立维度）

**提升至 3.5 (Borderline Conference) 的条件：**
1. 展开 instruct model ρ 反转分析（retrain classifier + mechanistic 解释）——这可同时解决 novelty 和 applicability 问题
2. 提供 DDR location/shape 分离的理论解释（至少 informal conjecture）
3. 修复 Cohen's d 阈值的 principled justification

---

## Detailed Comments（逐节）

### Abstract
- 四个必答问题回答完整，篇幅适当（~120 words）
- Cohen's d 数值对非专业读者意义不大，建议用定性描述替代
- "restricting current applicability to base models" 最后一句设定期望是好选择

### Introduction
- 叙事线清晰：递归生成 → 二元检测不够 → depth classification → DDR → 贡献
- "No existing method provides a feature-level decomposition" 需确认 concurrent work 未做此事
- Contribution #3 过于技术化（temperature ranges, ρ 数值），适合 Results 而非 Introduction
- "empirical rather than methodological" 的自我定位是诚实的，但与 C3 "mechanistic boundary conditions" 有 tension

### Related Work
- 覆盖面广，positioning 清晰
- 对 concurrent work (broken_telephone, markovian_chains) 三重区分合理
- 遗漏 Varshini et al. (ACL 2025) attractor cycles
- 引用密度 ~70 条，对 EMNLP Long Paper 偏少但可接受
- §2.3 / §2.4 分界不够自然

### Method
- Task formulation、generation chain construction、feature extraction、evaluation protocol 结构清晰
- "entropy" as shorthand for NLL 的 convention acknowledgment 合理
- Feature selection a priori 是合理决策但限制了 feature space 探索

### Results
- Binary F1 作为 primary metric（排除 gen-0 leak）是 key methodological design
- DDR 分析是全文亮点也是最大弱点
- Baseline 比较定位正确（"contextualize"而非"compete"）
- gen-2+ 错分为 gen-1 是主要 failure point (40.2%)，应在正文提及
- Table 1 vs Table 2 的 F1 差异 (0.694 vs 0.706) 应更显著标注

### Discussion
- Location/shape decomposition 的 post-hoc 定位恰当
- Instruct model 讨论充分但缺少对策和 mechanistic 分析
- DDR vs model collapse 区分过于简短

### Conclusion
- 过于简短（3 句），未 highlight future work 方向

### Limitations
- 覆盖面全面，应增加 DDR 阈值选择局限性的 acknowledgment

### 格式合规性
- ✅ 正文 8 页（符合 Long paper 限制）
- ✅ 匿名化完整（"Anonymous ACL submission"）
- ✅ 行号开启，ACL template + [review] option
- ✅ Limitations 和 Ethics Statement 存在
- ⚠️ 无匿名代码/数据链接
- ⚠️ Responsible NLP Checklist 需确认已通过 OpenReview 提交
- ⚠️ ", confirming" 9+ 次 —— 轻微 AI 写作标志，需修复