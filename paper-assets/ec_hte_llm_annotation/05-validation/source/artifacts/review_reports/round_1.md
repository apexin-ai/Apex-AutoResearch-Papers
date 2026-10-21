---
round: 1
review_mode: continue
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-21T11:46:06.627774+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 1 审稿报告（Continue Mode — 实际投稿论文）

**论文**: Error-Corrected Heterogeneous Treatment Effects: When LLM Annotation Debiasing Hurts
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
**格式**: Long paper, 8-page limit (正文) + unlimited references + Limitations
**审稿人**: Reviewer 1 (方法/实验严谨性) + Reviewer 2 (新颖性/写作/完整性)
**轮次**: Round 1 Continue (基于 Round 0 Dream Review 遗留问题)
**交叉回应**: R1↔R2 完成，关键问题全部达成共识

---

## Summary

论文证明了一个精确的偏差恒等式（Theorem 1）：当 LLM 标注的子群误分类率异质时，全局混淆矩阵校正引入的偏差与 δ_s · Δτ / (1-2π̄) 成正比，导致 50% 的参数配置下 debiasing 反而有害（最高 5.9× amplification）。提出 EC-HTE（HB 子群特异混淆矩阵 + CausalForestDML + plug-in SE），在 520 个合成配置（100 MC runs each）、TweetEval 半合成和 UC Berkeley Hate Speech 真实数据上验证，并与 PPCI 正交互补（bias 0.179→0.007 in both-errors DGP）。

**核心贡献结构**：强问题识别 + 干净理论刻画 + 增量方法 + 全面实验设计。

---

## Strengths

**S1. Theorem 1 精确恒等式——干净的理论贡献 [R1+R2 共识]**
Population-level exact identity（非 bound 或近似），R²=0.994 (K=2) / 0.974 (K=4) 实证验证。"50% of configurations where debiasing hurts" 是有冲击力的定量结论。Remark 2 推广到 asymmetric confusion matrices（R²=0.991）。Corollary 4 处理多类情况。Proposition 3 给出全局校正何时增加偏差的精确阈值，具有直接实践指导意义。

**S2. 诚实度异常高——学术诚信标杆 [R1+R2 共识]**
论文不隐藏 EC-HTE 的弱点：(a) TweetEval 半合成中 Global 优于 EC-HTE（bias 0.023 vs 0.027, RMSE 0.124 vs 0.225），明确报告并解释原因；(b) moderate regime 下 EC-HTE 无优势（Section 5.3/5.5/Limitations 三处一致）；(c) 小预算下 RMSE 达 naive 的 3.5×；(d) diagnostic setting-level AUC=0.47（随机水平）在 Section 5.4 和 Figure 3 中显式呈现；(e) UC Berkeley 案例为 null result（FNR=43.3% 导致 underpowered），恰当定位为 illustrative application。这种程度的诚实在 top venue 审稿中是显著加分项。

**S3. HB 模型规格完整且可复现 [R1+R2 共识]**
Gibbs sampler, 4 chains, 4000 iterations (2000 warmup), R̂<1.0034, ESS>1618, Gamma(3,1) hyperprior, sensitivity <5% under 2× perturbation, singularity guard (κ>100→fallback)。R1 评价为"同类 HB 方法论文中最详尽的 MCMC 报告之一"。

**S4. 4-DGP 正交设计 + PPCI 互补性验证 [R1+R2 共识]**
Section 5.5 + Appendix J Table 4：4 个 DGP 正交分离 covariate/outcome/both/none error。EC-HTE+PPCI 在 DGP C（both errors）将 bias 从 0.179 降至 0.007（97% reduction）。这不是 obvious 组合结果——需验证两种校正不互相干扰。

**S5. 相关工作全面且有区分度 [R1+R2 共识]**
25-30+ 引用覆盖：Carroll (2006), Imai & Yamamoto (2010), Dawid & Skene (1979), Passonneau & Carpenter (2014), PPI/DSL/PPCI/ForestIV。每个关键引用都有技术区分。Appendix E 展开 treatment vs effect-modifier misclassification。

**S6. Cross-model consistency [R1+R2 共识]**
6 个 OpenAI 模型跨 3 代，Δπ 范围 0.090-0.198，Spearman ρ=0.82-1.00 (p<0.05 all pairs)。证明 misclassification heterogeneity 是结构性问题。

**S7. Plug-in SE 限制被明确量化 [R1+R2 共识]**
Section 4.3 明确 plug-in approach + 合理性条件 (n_expert≥100) + Limitations 详细讨论 full Bayesian propagation left to future work。

---

## Weaknesses

**W1. [Major — borderline, 处于 Major 下限] 方法新颖性仍属增量 [R1+R2 共识]**
EC-HTE = Dirichlet-Multinomial HB（Dawid-Skene variant）+ 混淆矩阵反演（Carroll 2006 standard）+ CausalForestDML（Wager & Athey 2018 existing）。三个组件各自都是 well-known techniques。论文的 novelty 在于：(a) Theorem 1（genuine 新理论结果），(b) 问题识别（"debiasing can hurt"），(c) 4-DGP 实验设计，(d) PPCI 互补性验证。这些将方法新颖性不足从 dealbreaker 降级为 acceptable limitation。

**R1+R2 一致建议**：论文应 reframe 为 problem-identification paper 而非 novel methodology paper。Lead with Theorem 1 as main contribution, frame EC-HTE as the natural solution enabled by this theoretical insight。当前 Abstract 和 Introduction 的 framing 偏 "novel method"，与实际贡献结构不匹配。

**W2. [Minor] Abstract 中 diagnostic AUC 报告不对称 [R1+R2 共识]**
Abstract 写 "AUC = 0.83 in cross-validated evaluation" 但未注明是 subgroup-level。Setting-level AUC=0.47（不优于随机）仅在 Section 5.4 出现。读者仅看 Abstract 会高估诊断能力。建议加 "at the subgroup level" 限定。

**W3. [Minor] 100 MC runs 无 standard error 报告 [R1+R2 共识]**
Table 1 报告 point estimates 无 MC SE。对 extreme regime 差异（如 0.059 vs 0.011）大概率 statistically significant，但 moderate regime 差异（如 0.009 vs 0.005）MC SE 可能 overlap。建议在 Table 1 添加括号内 SE 或 appendix 报告。

**W4. [Minor] 加法式 CATE 注入未在 Limitations 讨论 [R1+R2 共识]**
Appendix D 的 DGP 使用纯加法 CATE：Y(1) = Y(0) + τ(Z)。未讨论 multiplicative 或 CATE×covariate interaction 注入是否改变结论。Limitations 应增加一条。

**W5. [Minor] 无正面 real-data evidence [R1+R2 共识]**
UC Berkeley 案例为 null result。缺少 EC-HTE demonstrably 改变 qualitative conclusions 的真实 CSS 分析。非 dealbreaker（主要验证来自 520 configs + TweetEval），但 positive real-data case 会显著增强说服力。

**W6. [Minor] Multi-LLM 验证仅覆盖单一提供商 [R2 提出, R1 采纳]**
6 模型全部 OpenAI。缺开源模型（Llama, Qwen）和其他商业模型。Δπ heterogeneity 可能是 OpenAI 特有现象。至少补充 1 个非 OpenAI 模型的数据点可增强 generalizability。R1 部分缓解：6 模型跨 3 代 + Theorem 1 是 model-agnostic 数学结果。

---

## Questions

1. **Novelty framing**：是否愿意 reframe 为 problem-identification paper（lead with Theorem 1）而非 method paper（lead with EC-HTE）？
2. **MC SE**：100 MC runs 的 MC standard error 量级？Table 1 中所有方法间差异是否 statistically significant at α=0.05？
3. **Additive CATE**：是否在更复杂 DGP（CATE×covariate interaction, heteroskedastic errors）上测试过？
4. **Real-data case**：是否考虑过 Ashwin et al. (2025) 难民数据作为 positive real-data case？
5. **Diagnostic workflow**：给定 setting-level AUC=0.47，practitioners 应如何使用 diagnostic？具体 workflow 是什么？
6. **EC-HTE+PPCI composition**：97% bias reduction 有理论保证还是仅经验观察？
7. **Asymmetric case**：Remark 2 的 asymmetric bias amplification factor 能否给出 closed-form 或数值上界？
8. **Estimator agnosticism**：corrected pseudo-outcomes 是否可 plug into 其他 HTE estimators（X-learner, R-learner, DR-learner）？

---

## Missing References

论文引用覆盖全面，无 critical missing references。可选补充：
- **Nie & Wager (2021)** R-learner — 与 estimator-agnostic 讨论相关
- **Battistin & Chesher (2014)** — measurement error in treatment effects 的 econometrics 文献
- 建议在 Related Work 或 Limitations 中增加一句 EC-HTE 对其他 HTE estimators 的适用性说明

---

## External Review

外部审稿：**未请求**（项目配置未启用 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成，4 warnings / 12 info / 0 critical：

**Warnings:**
1. **首页无视觉锚点** — Page 1 全为 Abstract + Introduction 纯文本，Figure 1 出现在 page 2。首页缺少视觉着力点，第一印象偏"理论/文字密集"。
2. **Figure 1 内部文字偏小** — 子图标题和轴标签在打印尺寸下可能低于正文字号 70% 的可读性阈值。
3. **Pages 3-6 连续 4 页无 display item** — Related Work→Theory→Method→Experiment Setup 纯文字。建议在 Section 4 插入方法流程图或算法伪代码框。
4. **主文 display item 密度过低** — 8 页主文仅 3 个 display items（Figure 1, Figure 2, Table 1），低于实证论文典型密度 (5-8/8页)。大量结果在 Appendix。

**Info (positive):**
- Figure 2 heatmap 设计良好（蓝-红 diverging, 文字标注清晰）
- Table 1 排版规范（booktabs, 加粗最优, ↓/↑ 方向指示）
- 数学排版整洁（Theorem 1, Proposition 3 格式规范）
- 参考文献格式一致，无 [?] 未解析引用
- 无 margin 溢出、section heading 孤悬或 widow/orphan 问题
- Limitations 篇幅适中，符合 EMNLP 要求
- NLP Checklist 完整填写

---

## Overall Assessment

### 维度评分（R1+R2 共识）

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 4.0/5 | 4.0/5 | **4.0** |
| Excitement | 3.5/5 | 3.5/5 | **3.5** |
| Reproducibility | — | 4.0/5 | **4.0** |
| Overall (ARR) | 3.5/5 | 3.5/5 | **3.5 (Borderline Conference)** |
| Confidence | 4/5 | 4/5 | **4** |

### Overall Assessment: **3.5 — Borderline Conference**

**唯一 Major weakness**：方法新颖性（标准组件组合），处于 Major 下限，被 Theorem 1 精确恒等式 + PPCI 互补性验证 + 4-DGP 实验设计部分补偿。

**R1+R2 共识判断**：论文在问题识别、理论贡献（Theorem 1）、实验科学性（诚实报告、正交设计）和学术规范（全面引用、完整 MCMC、详尽 Limitations）方面达到高标准。**推荐 Findings 接收（高置信度），Borderline Conference（有条件）。**

**升级至 Conference (4.0) 的条件**（R1+R2 共识）：
1. **Reframe** 为 problem-identification paper（lead with Theorem 1，非 EC-HTE framework）
2. **Abstract AUC** 加 "at the subgroup level" 限定
3. **MC SE** 至少在 appendix 报告
4. **Cross-provider LLM** 补充至少 1 个非 OpenAI 模型的 Δπ 数据点

以上 4 项中，(1)(2) 为文字修改可在 camera-ready 完成，(3)(4) 需少量额外实验但工作量有限。

---

## 遗留问题追踪状态

### Round 0 → Round 1 变化

| 状态 | Round 0 | Round 1 | 变化 |
|------|---------|---------|------|
| Resolved | 9 | 20 | +11 |
| In-Progress | 2 | 0 | -2 (→resolved) |
| Open | 13 | 6 | -7 (→resolved) |
| **Total** | **24** | **26** | +2 new |

### 当前 Open Issues (6 个)

| ID | Summary | Severity | Action |
|----|---------|----------|--------|
| R2-W1 | 方法新颖性增量 | warning (Major 下限) | Reframe 为 problem-ID paper |
| R2-W5 | Abstract AUC 选择性报告 | info | 加限定语 |
| R1-W2 | 加法 CATE 未讨论 | info | Limitations 增加一条 |
| R1-RD1-W3 | MC SE 未报告 | info | Table 1 或 appendix 补充 |
| R2-RD1-W3 | Multi-LLM 单一提供商 | info | 补充 1+ 非 OpenAI 模型 |
| R1-RD1-W5 | 无正面 real-data evidence | info | 可选：补充 positive case |

### 关键改善

论文相比 Round 0 Dream 版本有质的飞跃：
- Theorem 1 从近似 bound 升级为精确恒等式
- MCMC 规格从"几乎为空"到"同类最详尽之一"
- 相关工作从"严重遗漏"到"30+ refs 全面覆盖"
- 信息密度从"16 tables 0 figures"到"3 display items 主文 + 充实附录"
- 所有 critical issues (4/4) 已解决
- 所有 warning issues (6/6) 从 Round 0 已解决