---
round: 5
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:35:37.261791+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 审稿报告：G-MFRM (Gated Multi-Facet Rasch Model)

**Venue**: EMNLP 2026 (ARR)  
**Reviewers**: R1, R2  
**轮次**: Round 5 (fresh review)  
**交叉回应**: R1 ↔ R2 完成，高度收敛

---

## Summary

本文提出 Gated Multi-Facet Rasch Model (G-MFRM)，通过在传统 MFRM 中引入 bilinear contamination-exposure 交互项 (c_n · e_i)，试图在 LLM-as-a-judge 评测中联合校准 judge severity 和 benchmark contamination。理论框架包含 OVB 分析（motivating observation）、identifiability 证明（Theorem 1, Cauchy-Schwarz + Schur complement）、以及 Murphy-Topel variance correction。实验在 Arena-Hard benchmark 上评估 N=8 和 N=17 模型。

核心矛盾：论文标题声称 "Fair Scores via Joint Calibration"（暗示排名改进），但主实验中 G-MFRM 排名准确度低于或仅持平 baseline。模型拟合（LOO-ELPD）显著优于 MFRM-only，但模型拟合优势未转化为排名改善。

---

## Strengths

1. **Problem formulation 清晰且有价值**：首次在 LLM-as-a-judge 文献中用 OVB 框架形式化 judge bias 与 contamination 的 confounding 结构。问题真实存在且随 LLM 评测规模扩大日益重要。

2. **Identifiability 证明技术正确**：Theorem 1 通过 Fisher information block 分解 + Cauchy-Schwarz + Schur complement 建立 gated IRT 首个形式化可辨识性条件。完整证明在 Appendix A，两位 Reviewer 确认技术正确。

3. **综合消融与合成验证**：20-seed 消融实验（binary vs continuous gating, with/without d_j）、合成数据 c_n recovery (r=0.81)、权重 sensitivity (ρ≥0.998)。实验设计系统且透明。

4. **LOO-ELPD 显著**：ΔELPD = −55.7, |Δ/SE| = 5.9——contamination signal 是 real 的，G-MFRM 确实捕获了数据中的 contamination-exposure 共变结构。

5. **诚实呈现 negative results**：论文区分 predictive fit 和 ranking accuracy 两条评估线，明确承认排名改善不显著，未过度宣称。

---

## Weaknesses

### Must-Fix（阻塞接收）

**[MF-1] 主实验排名准确度低于或持平 baseline（R1-N1 ≈ R2-N3, 共识 critical）**

- N=8: G-MFRM τ = 0.786（全 coverage）= 7 个 baseline（raw average, BT-MLE, Elo, etc.）完全相同
- N=17 Exposed-only (231 items): G-MFRM τ = 0.779 = raw average
- N=17 Filtered (≥75% coverage): G-MFRM τ = 0.838 优于 baseline 0.786，但这来自 item filtering（从 500→231 items 中筛选高覆盖 items），而非 contamination 校准本身
- **替代假说未排除**：item filtering 移除高噪声 item 本身可能提升排名，与 contamination 参数无关。需 random e_i placebo test 验证 c_n 的增量价值
- Bootstrap Δτ CI = [−0.071, 0.071] 包含零，Power ~50%
- 标题 "Fair Scores via Joint Calibration" 暗示排名改进，与实际结果不符

**[MF-2] c_n 验证存在循环性，缺乏独立外部验证（R2-N2, 共识 critical）**

- Model age 与 c_n 的相关性（Figure 5a）仅为 face validity，不构成 causal validation
- 合成 recovery (r = 0.81) 在已知 ground truth 下有效，但不验证 real-data c_n 的语义正确性
- LOO-ELPD 证明模型拟合优势，不证明 c_n 参数的语义（contamination）解释正确
- 缺乏与独立 contamination indicator（membership inference, Min-K%, 训练数据日期截断对比）的关联验证
- c_n 可能仅反映 "differential performance on high-exposure items" 而非真实污染程度

**[MF-3] CI coverage 67.9–71% 严重偏离 95% 名义水平——结构性问题（R1-N2, 共识 critical, 跨 5 轮未解决）**

- 从 Round 1 持续至今的核心问题
- N=8 时 67.9%, N=50 时 71%——几乎不随样本量改善，说明非小样本问题而是结构性缺陷（乘性耦合 + HalfNormal 边界约束）
- Table 6（Appendix M）仍标注 "95% CI" 无 caveat，对读者有误导性
- Murphy-Topel correction 基于渐近理论（经验 N≥30），N=8 远不满足
- SBC (Simulation-Based Calibration) 是标准实践，不应作为 future work
- 对测量模型论文，uncertainty quantification 可靠性是核心质量指标

### Should-Fix

**[SF-1] 单一 benchmark (Arena-Hard) 无法支撑通用性声明（R2-N1, 共识）**

标题/abstract 使用 "LLM Evaluation" 泛化表述，但 Stage 2 exposure pipeline 针对 pairwise comparison 设计。在选择题、代码生成等 benchmark 上行为未知。Claims 应限定为 "pairwise open-ended evaluation" 或增加验证。

**[SF-2] Anchor model (gpt-4-0314) 自身 contamination 可能系统性偏倚 e_i（R1-Q3, R2 strongly agree）**

gpt-4-0314 作为 Stage 2 anchor，若其本身对部分 items exposed，则这些 items 的 e_i 被系统性低估（anchor high performance 归因于 ability），进而 c_n 偏倚。比 e_i pipeline 内部一致性问题（ρ≥0.998）更根本。

**[SF-3] 52% items misfit（92/176）无排除后 sensitivity analysis（R1-W2, R2 escalates）**

Appendix Q: 176 items 中 92 个 flagged（74 underfit MNSQ<0.5, 18 overfit MNSQ>1.5）。52% 远超 Rasch 常规可接受范围（<20%）。缺排除后 θ_n 和 c_n 稳定性分析。

**[SF-4] N=8 pilot c_n 跨配置不稳定（GPT-3.5: 5.60→2.57）（R1+R2 共识）**

论文解释为 hierarchical shrinkage，但 >2× 变化异常。N=8 用 9 judges vs N=17 用 6 judges，panel 完全不同可能是原因。强化 c_n 可靠性担忧。

**[SF-5] OVB 线性近似 r=0.80, 36% 方差未解释（R1 maintains, R2 rebuts）**

[分歧] R1 认为应标注 "Approximate Observation"；R2 认为论文已标注近似性质且实际估计不依赖此近似，作为 directional motivation 足够。**Director 判定**：presentation fix，加 "Approximate" 限定词。

**[SF-6] MCMC 收敛阈值声明偏宽（R1-W1, trivial fix）**

实际结果（R̂≤1.003, ESS≥1,240）远优于声明阈值（R̂<1.05, ESS>100）。按 Vehtari et al. (2021) 更新为 R̂<1.01 即可。

**[SF-7] e_i pipeline 缺乏 ground truth 验证（R2-W3, 共识）**

Appendix K 权重 robustness（ρ≥0.998）证明内部一致性，不证明准确度。如果 e_i 的 bias 是系统性的，σ_crit 分析框架不适用。

### Minor

- Table 1 caption 列 5 个 baseline 但实际 7 个，不完整
- Batsuren et al. 2024 (IRT for LLM evaluation) 直接相关应引用
- Abstract 可能仍超 200 词（EMNLP 2026 硬约束），需确认并压缩

---

## Questions

1. 如果将 e_i 替换为 random permutation（placebo test），c_n 估计是否退化为零？这将区分 contamination signal 和 item filtering effect。

2. N=17 100% coverage 下 G-MFRM 与 raw average τ 相同（0.779），是否意味联合校准对排名无增量价值？论文是否应重新定位为诊断工具？

3. 67.9–71% coverage 是 Murphy-Topel 修正后还是修正前的结果？如果是修正后，则修正基本无效——需要替代方案（SBC/parametric bootstrap）。

4. gpt-4-0314 作为 anchor 若本身对部分 items contaminated，e_i 估计系统性偏倚方向和幅度是多少？是否有替代 anchor 的对照实验？

5. 52% item misfit 是否为 pairwise comparison 数据的固有特性？排除 misfitting items 后核心结论是否改变？

---

## Missing References

- **Batsuren et al. (2024)** — IRT for LLM evaluation，直接相关（共识应引用）
- **Stureborg et al. (2024)** — 相关但非必须

---

## External Review

**状态：Pending（未返回）**

Stanford Agentic Reviewer 外部审稿已于 2026-05-25T21:15:29Z 发起，截至报告合成时仍未返回。

---

## Visual Layout Check（非评分项）

**状态：Done** | 0 critical, 1 warning, 3 info

- ⚠️ **Page 18**: 近空白页——"Use of AI Assistants" 节最后 1 个 bullet 溢出到第 18 页，仅 2 行内容，~95% 页面空白。建议压缩收入第 17 页。
- ℹ️ **Page 14**: Appendix 3 个 figure + 1 个 table 堆积同页，Figure 10 偏小。
- ℹ️ **Page 16**: 5 个 table 密集排列，作为 appendix 可接受。
- ℹ️ **Page 1**: 首页无 display item（Figure 1 在第 2 页顶部），非硬伤。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| Reviewer | Score | 主要理由 |
|----------|-------|----------|
| R1 | 3.5 (Borderline Conference) | 理论贡献（identifiability proof + error propagation）有独立价值；empirical weakness 可通过 reposition 缓解 |
| R2 | 3.0 (Findings) | 模型新颖性为增量组合；主实验无正向结果不能支撑 main conference |
| **Consensus** | **3.0** | 两位 Reviewer 在 3 个 Must-Fix 问题上高度一致；分歧仅在理论贡献权重 |

**评分理由**：

论文的理论框架（OVB formalization + identifiability + error propagation）确有方法论贡献，problem formulation 清晰有价值。但核心实验无法支撑标题宣称的 "Fair Scores"——主实验排名不优于 baseline，contamination 参数缺乏独立验证，uncertainty quantification 结构性不可靠（CI coverage 跨 5 轮未解决）。

如果进行以下调整，论文可升至 3.5 (Borderline Conference)：
1. 重新定位为 contamination diagnostic tool（而非 ranking improvement method）
2. 提供 c_n 的独立验证（placebo test 或外部 indicator 对比）
3. 实施 SBC 修复 CI coverage 或诚实放弃 CI 相关 claims

当前版本适合 Findings track：理论分析和模型设计有学术价值，但 empirical claims 与实际证据不匹配。

---

## Detailed Comments

### 对 Reviewer 分歧的 Director 裁定

1. **R2-W3（技术新颖性为增量组合）vs R1 REBUT**：这是影响评分最大的分歧。R1 认为完整理论分析体系（OVB→identifiability→error propagation→Murphy-Topel）构成系统性贡献；R2 认为各部分单独看均为已知工具的领域应用。**Director 裁定**：两种视角均有道理。作为 system contribution 有价值（Findings 级别），但不足以仅凭理论链支撑 main conference，除非实验证据配合。

2. **R3-N1（OVB 近似 r=0.80）**：R1 列为 Must-Fix，R2 rebut 为 Should-Fix。**Director 裁定**：Should-Fix（presentation fix）。论文已标注近似性质，G-MFRM 使用完整非线性模型，不依赖此近似。加 "Approximate" 标注即可。

3. **R2-W4（Chatbot Arena ground truth 偏差）**：R1 rebut 为领域共性问题。**Director 裁定**：有效批评但不独属本文。在 Limitations 承认即可。

### 跨轮次持续问题

本文已经历 5 轮审稿。以下问题从 Round 1 持续至今未根本解决：
- CI coverage 68-71%（R1-W5，Round 1 至今）
- Murphy-Topel N=8 适用性（R1-MT，Round 1 至今）
- 主实验排名不优于 baseline（R2-N3，Round 2 至今）

这些持续性问题表明它们可能是方法论的内在局限（而非写作不足），需要新实验数据或根本性方法调整。

### Rebuttal 建议优先级

如果进入 rebuttal 阶段，建议按以下优先级响应：
1. **[最高]** Random e_i placebo test + 重新定位论文 claims
2. **[高]** SBC implementation 或放弃 CI claims
3. **[中]** Anchor robustness check（换用不同 anchor model）
4. **[低]** 52% item misfit sensitivity + 标题/abstract 限定

---

*Report generated: 2026-05-25 | Round 5 | Reviewers: R1, R2 | Cross-responses: R1↔R2 complete*