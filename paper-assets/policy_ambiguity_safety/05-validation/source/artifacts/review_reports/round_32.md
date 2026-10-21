---
round: 32
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-24T12:51:38.089250+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

## Consolidated Review Report — Round 32 (Fresh Review) [修订版]

**修订说明**：本版本纳入 Reviewer 2 的完整交叉回应，对 MF2（convergent nocuity framing）的建议做了实质性修正，对 SF7（TOST margin）做了降级处理，并修正了温度 pilot 样本量的事实性错误。

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
**Venue**: EMNLP 2026 via ARR (May cycle)
**Reviewers**: R1 (方法严谨性 + 实验设计) · R2 (新颖性 + 完整性 + 格式合规)
**交叉分享**: 完成，两位 Reviewer 均完成逐条 [AGREE]/[REBUT] 回应

---

### 1. Summary

本文通过 matched-pair 因果设计研究 policy ambiguity 对 LLM agent 安全性的因果效应。在 τ²-bench 上构建 300 对 ambiguous/unambiguous 条款对，跨 5 个模型（~3,000 episodes）测试，报告歧义条款使违规率增加 +34.0pp（排除 incompleteness 后 +31.0pp）。论文提出 "convergent nocuity" 概念——41.3% 的歧义条款在多个模型间触发一致性错误（77% permissive bias）。探索性发现 type-mechanism dissociation（V=0.45, LLM-coded）表明歧义类型预测失败机制而非失败概率。

---

### 2. Strengths

**S1. 严谨的因果设计（R1+R2 共识）** — Matched-pair perturbation 设计是本文最大方法论优势。Perturbation control（Δ_perturb = −0.67pp）、confound-minimized coreferential type（+18.7pp with Δtoken≈7.8 words）、logistic regression 控制信息量差异——令人信服地隔离了歧义的因果效应。显著优于 DRIP-R 的 correlational 设计。

**S2. Convergent nocuity 概念价值（R1+R2 共识）** — 将 Berry & Kamsties (2004) 的 nocuous/innocuous 框架从人类扩展到 LLM agents，发现 LLM 的 nocuity 是 convergent 而非 divergent。Cross-family Jaccard = 0.46 接近 within-family 0.54（Δ=0.084, p<0.0001），77% permissive attractor——对 multi-agent consensus 作为安全 proxy 的主流假设构成直接挑战。概念有价值，但 framing 需区分实践 claim 与理论 claim（见 MF2）。

**S3. Claim 分级透明（R2 提出，R1 共识）** — 论文清晰区分 primary supported claims (C1, C2)、inconclusive (C3 layer effect)、exploratory (C4 type-mechanism dissociation)。

**S4. 充分的稳健性检验（R1+R2 共识）** — SOPBench 跨 benchmark 复制（+12.7pp）、healthcare 跨域 pilot（+58.8pp）、7 模型扩展、temperature=0.7 pilot（50 clause pairs × 2 models，85-97% clause-level agreement）、bootstrap clustering、TOST 多 margin 敏感性分析——覆盖面远超同类工作。

**S5. Related work 覆盖全面（R2 提出，R1 共识）** — 五个维度均有充实覆盖，与并发工作的差异化论述清晰。

**S6. Limitation 透明度高（R1 提出）** — Statistical limitations 主动报告，包括 C3 未过 Bonferroni、温度限制、incompleteness confound。

---

### 3. Weaknesses

#### Must-Fix（影响接收决定）

**MF1. Incompleteness 在 "ambiguity" 框架下的概念张力未充分解决**
[R2-N1 MF, R1 交叉回应从 SF 升级为 AGREE-MF | 两位 Reviewer 共识 MF | 跨轮追踪: R30-SF6 升级]

Incompleteness 是效应量最高的类型（+49.2pp），但在认识论上与其他五种歧义类型存在根本区别：添加全新条件（如 return policy 中缺失的 damaged items 规则）与消解同一条款的多义性属于不同操作。论文 §3 已承认 incompleteness 是 "information-addition rather than disambiguation manipulation"，但这一承认与将其纳入统一 "ambiguity" taxonomy 之间的张力未被充分讨论。

Abstract 中 "+34.0 percentage points (31.0 pp excluding incompleteness)" 的括号处理容易被忽略，且 §1 contribution list 仅使用 +34.0pp。R2 补充：即使添加 "new condition count" 作为回归控制变量，incompleteness 的 confound 本质上可能无法通过回归解决——因为操作层面就是 "信息添加" 而非 "歧义消解"，这是定义层面的问题。

**需要**：(1) Abstract 中将 31.0pp 提升为与 34.0pp 并列的主要数字，而非括号补充；(2) §3 增加一段更深入的认识论讨论，论证 agent policy specification 场景下纳入 incompleteness 的合理性（可引用 Dalpiaz et al. 2018 co-occurrence argument 和 RE 社区 inclusive tradition）；(3) Table 2/Figure 3 视觉区分 incompleteness（如 ‡ 标记或 dashed line）；(4) §1 contribution list 同步修改。

**MF2. Convergent nocuity 的双层 claim 未被区分——41.3% 与 ~9pp 回答不同问题**
[R1-MF1 vs R2-W4: 两位 Reviewer 存在实质性分歧 | 跨轮追踪: R30-SF5 升级]

**核心分歧**：R1 认为论文应以 excess rate (~9pp above independence baseline 32.4%) 而非 total convergent rate (41.3%) 为主角，因为 78% 的 convergent violations 可由独立性基线解释。R2 反驳：41.3% 和 ~9pp 回答不同问题——

- **41.3% 回答实践安全问题**："多少比例的歧义条款触发 multi-model 一致性错误？"——即使 32.4% 来自模型独立地各自犯同样的错，multi-agent consensus 作为 safety proxy 已不可靠。对论文的核心实践论点（"agreement-based monitoring is blind to systematic failures"），41.3% 是正确的主角。
- **~9pp excess 回答理论机制问题**："模型间是否存在超越独立性的 shared bias？"——cross-family Jaccard = 0.46 接近 within-family 0.54 证明 convergence 不仅是各自高 violation rate 的巧合。

**Director 判定**：R2 的论证更具说服力——两个数字服务于不同 claim，不应互相替代。但论文当前 framing 将两层 claim 合并呈现，读者无法区分 "consensus 不可靠"（实践层面）和 "存在 shared bias"（机制层面）。维持 Must-Fix，但修改建议方向。

**需要**（与初版报告不同）：(1) 在 §6.3 和 Discussion 中明确区分两层 claim——实践层面（41.3% 表明 multi-model consensus 作为 safety proxy 不可靠）和机制层面（~9pp excess + Jaccard 分析揭示超越独立性的 shared bias）；(2) Abstract 保留 41.3% 但需在 §6.3 中引入独立性基线对比（32.4%），使读者能自行判断两层效应的相对贡献；(3) 报告排除 incompleteness 后的 convergent rate 是否仍显著高于 baseline；(4) 增加实践语境讨论——在部署场景中这两层效应分别意味着什么。

#### 高优先级 Should-Fix（一位 Reviewer 列 Must-Fix，另一位 Should-Fix 或 REBUT）

**SF1. Human mechanism coding κ=0.32/0.41 削弱 type-mechanism dissociation 证据力**
[R2-N2 MF, R1 同意实质但判 SF | 跨轮追踪: R30-MF1 延续]

Human mechanism coding κ=0.32（raw）/0.41（collapsed）远低于 κ≥0.60 阈值。论文报告 LLM-coded V=0.45 但未报告 human-coded Cramér's V，无法对比上下界。V=0.45 在 abstract（无 upper-bound 修饰）、§6（有明确修饰）、contribution #3（部分修饰）三处呈现力度不一致。

R1 指出 type-mechanism dissociation 已标记为 [Exploratory]，且在 contribution list 中不作为独立 contribution——R2 建议 "从 contribution list 分离" 实际已被满足。R2 交叉回应坚持循环论证警告：LLM coding κ=0.52 vs human κ=0.32/0.41 的差异本身可能是 convergent nocuity 在 annotation 层面的体现——用自己提出的概念解释支撑该概念的方法论弱点存在循环风险。

**需要**：(1) 报告 human-coded Cramér's V 以对比 LLM V=0.45 的上下界；(2) 如果 human V 显著低于 0.45，降低 Discussion 中 type-specific mitigation 建议的置信度；(3) 统一三处 V=0.45 的 upper-bound 措辞。

**SF2. Authorization scope 测量质量差——κ=0.385, construct validity 存疑**
[R1-MF2, R2 交叉回应 AGREE 并补充 | 跨轮追踪: R31-SF1 延续]

Authorization scope 的 per-type κ=0.385 仅 "fair agreement"，跨模型 violation rate 范围 12-64%（最大变异）。R1 补充：Appendix AC 显示 Claude judge 对 Claude 模型评 30% vs GPT judge 评 12%——52pp judge 差异远超 treatment effect。R2 交叉回应补充两点：(1) Table 2 脚注 ‡ 级别的警告不够，C4 interaction 和 mitigation 最大效应 (-18.0pp) 均建立在此 type 上；(2) 模型间方差可能部分是 judge noise 而非真实差异。R2 还指出 Appendix O 已做 C4 sans-auth-scope 分析，但 C1/C2 的 sans-auth-scope 分析未显式报告。

**需要**：(1) §5.2 标记 auth scope 为 measurement-unreliable type；(2) Figure 3 视觉区分；(3) Discussion 讨论 construct validity；(4) 补充 C1/C2 排除 auth scope 后的 sensitivity analysis。

**SF3. 合成 vs 自然 2.7× 效应衰减——external validity framing**
[R1-MF3, R2 交叉回应 REBUT 降级为 SF | 跨轮追踪: R30-SF1 延续]

τ²-bench +34.0pp vs SOPBench +12.7pp（unweighted mean）。R1 列 MF。R2 反驳：(1) 论文 Discussion 已明确定位 τ²-bench 为 upper bound、SOPBench 为 lower bound，framing 诚实；(2) Abstract 已包含 SOPBench 效应量（"+12.7 pp unweighted mean; all five Δ > 0"）；(3) 在因果研究中以主实验（完整因果控制）为 headline 是标准做法，将 replication study 提升为并列 headline 会模糊两种设计的不同性质。2.7× 衰减是合成 vs 自然设计的预期差异。

**Director 判定**：R2 的论证有道理——论文的 upper/lower bound framing 是诚实的。降级为 Should-Fix。但 Introduction contribution list 仅提及 +34.0pp，未提及 SOPBench 方向一致性，存在选择性呈现。

**需要**：(1) §1 contribution list 补充一句 SOPBench 复制的方向一致性（+12.7pp, all Δ > 0）；(2) §7 用 ~120 words 分析 63% 衰减来源；(3) 报告 SOPBench per-type significance。

#### Should-Fix（不一票否决但影响评分）

**SF4. Temperature=0 限制——pilot underpowered** [R1-SF2, R2 AGREE | R30-SF2 延续]
所有主实验在 T=0。Temperature pilot 规模为 50 clause pairs × 2 models（R1 原报 n=20 有误，R2 交叉回应纠正），相比完整 300 × 5 设计仍有限。未报告效应量 CI 或 statistical power。R2 补充：matched-pair 设计使温度效应在两个 conditions 之间抵消——理论上成立但需更强实证。**需要**：在 §4 或 Limitations 中量化 pilot 的 detectable effect size at 80% power。

**SF5. Cross-judge 术语 + allocation 不对称** [R1-SF3, R2-W5/M1 共识 | R30-SF4 延续]
GPT-5.4 judge 3 models，GPT-4.1 judge 2 models（3/5 来自 OpenAI）。Matched-pair Δpp 中 systematic bias 抵消，但 convergent nocuity 分析依赖绝对 violation rates。**需要**：(1) 全文 'cross-judge' → 'cross-model judge assignment'；(2) Appendix 分别报告 per-judge convergent nocuity rate。

**SF6. Table 2 颜色编码暗示未验证的层级结构** [R2-W3, R1 AGREE | R31-SF2 延续]
C3（layer effect）未通过 Holm-Bonferroni（p=0.017 > 0.0125），但 Table 2 用红蓝颜色编码暗示实验支持的层级差异。**需要**：保留层标签但移除颜色编码，或在 caption 加注。

#### Minor（不影响接收）

**M1.** Introduction contribution list 数字密度过高（8+ 数字单段），精简为 2-3 核心数字。[R2-W1, R1 AGREE]
**M2.** Figure 1 panels (b)-(c) 信息密度不均，中 panel 仅列模型名。[R2-W2, R1 AGREE]
**M3.** SESOI ±15pp 正文未引用 Appendix A cost anchoring。[R1-SF5, R2 REBUT 降级: 论文 Table 3 已报告 ±5pp 至 ±20pp 完整 TOST 敏感性分析，主文 §5.2 已提及 ±10pp 结果。R2 指出 R1 要求 "报告 ±10pp TOST" 在论文中已被满足。Director 判定降为 Minor：正文引用 Appendix A cost anchoring 即可。]
**M4.** §1 pilot audit 未引用 Appendix 编号（Appendix AD）。[R2-M2]
**M5.** 参考文献格式不完全统一：部分 arXiv 条目有 submission date，部分没有。[R2-M3]
**M6.** AI usage disclosure（Page 27）位置确认是否符合 venue 要求。[R2-M4]
**M7.** §4.2 annotation verification 96% agreement 的 scope 需更具体说明。[R2-M5]
**M8.** Per-type κ CI 很宽（n≈17），需更强 caveat。[R1-M2, R2 AGREE]
**M9.** 'primary risk factor' 应限定为 'among measured predictors'。[R1-M3, R2 AGREE]
**M10.** \enlargethispage 格式操纵状态确认——R31 列为 Must-Fix，R32 两位 Reviewer 未独立提出，需确认是否已修复。[跨轮追踪: R30-MF2]

---

### 4. Questions（需要作者回答）

**Q1.** Incompleteness 的 unambiguous variant 添加了多少新信息（beyond token count）？能否提供 information-theoretic 度量或 "新条件数量" 来量化 confound？[R2-Q1, R1 AGREE]

**Q2.** Human mechanism coding 的 Cramér's V 是多少？如果 human V << 0.45（LLM V），type-mechanism dissociation 的可靠性如何？[R2-Q2, R1 AGREE — R1 称此为 R2 审稿中最有价值的新问题之一]

**Q3.** 排除 incompleteness 类型后，convergent nocuity rate 是否仍显著高于 independence baseline？[R2-Q3, R1 AGREE — R1 补充：如果排除后 excess convergence 消失，convergent nocuity 可能主要是 incompleteness 的附带现象]

**Q4.** SOPBench per-type 效应是否均显著？还是某些类型复制失败？[R2-Q4, R1 AGREE — R1 推测每 type 样本量可能很小，per-type 结果很可能不显著]

**Q5.** Healthcare domain pilot 的 +58.8pp 是否包含 incompleteness 类型？排除后效应量是多少？[R1-Q2]

**Q6.** Authorization scope 的低 κ 是否源于 type 定义本身的模糊性？如果 type 本身难以区分，type-level 分析的根基是否稳定？[R1-Q5]

**Q7.** Convergent nocuity 的 excess rate bootstrap CI 是多少？在部署场景中 9pp excess 意味着多少额外的 "multi-model consensus 伪阴性"？[R1-Q3, R2-W4]

**Q8.** "first matched-pair causal study" 的 claim——RE 领域是否有类似 controlled experiment（非 LLM context）？[R2-Q5 提出, R1 REBUT: claim 已三重限定 (matched-pair + causal + LLM agents)，在此范围内准确。Director 倾向 R1 立场。]

---

### 5. Missing References

**R1.** "Can AI Agents Agree?" (arXiv 2603.01213, 2026) — AI agent 间 agreement/disagreement，与 convergent nocuity 高度相关。[R2 提出, R1 AGREE but notes need to verify existence]

**R2.** "Aligning Language Models to Explicitly Handle Ambiguity" (arXiv 2404.11972, 2024) — LLM 显式处理歧义，与 disambiguation neglect 相关。[R2 提出, R1 AGREE]

**R3.** "Enhancing Software Requirements Quality: Ambiguity Detection and Resolution Using Large Language Models" (Springer, 2025) — RE + LLM + ambiguity 交叉领域。[R2 提出, R1 AGREE]

---

### 6. External Review

**状态：未请求**

---

### 7. Visual Layout Check（非评分项）

**状态：已完成** (2026-05-24, ~4 min)
**结果：0 critical / 0 warning / 8 info**

主要发现：Figure 1 面板内文字偏小；Figure 3 forest plot 尺寸较小；Table 2 列多但无溢出；Figure 4 heatmap 色盲友好性可接受；末页约 35% 空白（Appendix 末页可接受）。

**结论**：排版无硬伤，Camera-ready 阶段可优化字号和图表尺寸。

---

### 8. Overall Assessment

**Overall: 3.5 / 5（Borderline Conference）**
**Confidence: 4 / 5（Quite sure）**

两位 Reviewer 独立评分完全一致。

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3/5 | 3.5/5 | **3.25/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |

**一句话总结**：扎实的因果设计和丰富的稳健性检验使论文方法论水准显著高于 agent safety 领域平均水准，但两个核心贡献的 framing 均存在需要校准的问题——convergent nocuity 需要区分实践 claim（41.3%，consensus 不可靠）和理论 claim（~9pp excess，shared bias 存在），incompleteness 作为最强效应类型（+49.2pp）在概念上最可争议——需要通过更精确的叙事而非额外实验来解决。

**接收条件**：如果作者能 (1) 重新 frame incompleteness 的呈现方式（并列 31.0pp），(2) 区分 convergent nocuity 的实践和理论两层 claim，(3) 报告 human-coded V 并据此调整 Discussion 的置信度——论文有望从 Borderline Conference 提升至 Conference 水平。这些修改不需要新实验，仅需更精确的叙事。

---

### 9. Detailed Comments

#### 两位 Reviewer 的分歧与 Director 判定

| 问题 | R1 severity | R2 severity | 最终判定 | Director 理由 |
|------|------------|------------|---------|--------------|
| Incompleteness 概念张力 | SF → MF | MF | **MF** | 两位共识 |
| Convergent nocuity framing | MF（替换为 ~9pp） | SF（41.3% 是正确主角） | **MF（区分两层 claim）** | R2 论证更有说服力：两个数字回答不同问题，应区分而非替代 |
| Human mechanism coding | SF | MF | **高 SF** | R1 论证已标记 exploratory 且未独立列为 contribution |
| Auth scope κ=0.385 | MF | AGREE+补充 | **高 SF** | R2 交叉回应补充脚注不够 + C1/C2 缺 sans-auth-scope 分析 |
| Synthetic vs natural decay | MF | REBUT→SF | **SF** | R2 论证合理：upper/lower bound framing 诚实，2.7× 是设计预期差异 |
| SESOI margin sensitivity | SF | REBUT→Minor | **Minor** | R2 事实性纠正：±10pp 已在 Table 3 和 §5.2 报告 |
| "first" claim scope | 准确 | 需限定 | **R1 立场更合理** | claim 已三重限定 |

#### 跨轮次问题追踪摘要

| 问题 | 首次提出 | 本轮状态 | 趋势 |
|------|---------|---------|------|
| Human κ 不足 (R30-MF1) | R22 | open, R32 新增 human V 需求 | 持续未解决 |
| \enlargethispage (R30-MF2) | R28 | R32 未被提出，可能已修复 | 待确认 |
| 合成 vs 自然衰减 (R30-SF1) | R28 | SF, R2 论证 framing 已诚实 | 降级 |
| Temperature pilot (R30-SF2) | R24 | open, 样本量纠正为 50 pairs | 持续 |
| Convergent nocuity baseline (R30-SF5) | R29 | 升级为 critical, 建议改为区分两层 claim | 方向修正 |
| Incompleteness 概念张力 (R30-SF6) | R29 | 升级为 critical | 恶化 |
| Auth scope 质量 (R31-SF1) | R31 | R2 补充新证据（脚注不够 + C1/C2 缺分析） | 加深 |