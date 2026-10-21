---
round: 0
review_mode: 
overall_score: Best: 3.5 Borderline Conference / Median: 3.0 Findings
timestamp: 2026-05-21T04:29:29.760930+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Dream 审稿报告（Best + Median）：EC-HTE

**项目**: ec_hte_llm_annotation
**目标 Venue**: EMNLP 2026 (via ARR)
**Dream ID**: 20260521T032758
**审稿范围**: Best 版本（R1+R2 交叉完成）+ Median 版本（R1 单独审稿）

---

## ⚠️ 审稿完整性说明

- **Best 版本**：R1 实际阅读 PDF 并审稿，R2 基于 R1 审稿发现完成交叉回应。R1+R2 达成**完全共识**。
- **Median 版本**：R1 实际阅读 PDF 并审稿。R2 未审阅 Median 版本。
- **R2 此前基于错误摘要的 V2 评估（2.0 Reject）已作废**，不影响本报告任何评分。

---

## Part A: Best 版本

### Summary

论文形式化了 LLM 标注 HTE 中的失效模式，核心为 Theorem 1（精确恒等式）：全局校正偏差等于误分类率与 CATE 的加权协方差 Cov_w(π, τ)。提出 EC-HTE + 展示与 PPCI 的正交互补性（4-DGP 正交实验，both-errors DGP 下 97% bias reduction）。在 TweetEval 半合成和 UC Berkeley Hate Speech 真实数据上验证。

### V1 → V2 修复状态

| V1 问题 | 严重性 | 状态 | R1+R2 确认 |
|---------|--------|------|-----------|
| Proposition 1 rigor + K=2 限制 | Critical ×2 | ✅ 已修复 | 精确恒等式, tightness 1.003-1.023 |
| Real data ground truth | Critical | ✅ 已修复 | UC Berkeley 公开数据 + illustrative 定位 |
| HB 模型规格 | Critical | ✅ 已修复 | Stan/NUTS/4-chain/Appendix D |
| 相关工作遗漏 | Major | ✅ 已修复 | 30+ 引用，全部遗漏覆盖 |
| 信息密度 | Major | ✅ 已修复 | 5 tables + 4 figures |
| 方法新颖性 | Major | ⚠️ 唯一残留 Major | 有 mitigating factors |

**前一轮全部 4 个 Critical + 2 个 Major 问题已解决。**

### Strengths

**S1.** Theorem 1 精确恒等式是 clean 的理论贡献。Cov_w(π,τ) 形式优雅可解释，tightness 1.003-1.023 几乎精确。R2 确认：非 trivially 从 Carroll et al. 导出。[R1+R2]

**S2.** 4-DGP 正交实验设计（covariate-only/outcome-only/both/none）精确分离误差来源。EC-HTE+PPCI 97% bias reduction 定量验证互补性。属方法比较 best practice。[R1+R2]

**S3.** 11/11 实验全覆盖，主文 8 + 附录 3，分布合理。[R1]

**S4.** HB 完整规格 + singularity guard。R2 给 Reproducibility 4.5/5。[R1+R2]

**S5.** RMSE tradeoff 诚实披露（+28%）+ Figure 4 budget crossover 分析。[R1]

**S6.** 30+ 引用覆盖全部关键领域。Novelty claim "No existing work addresses correction when the mismeasured variable defines the heterogeneity structure" 在此文献景观下 defensible。[R1, R2 确认]

**S7.** Real data 恰当定位为 illustrative application + CATE shift in SE + domain consistency。[R1]

**S8.** Robustness 分析展示 graceful degradation，HB shrinkage 在 irrelevant subgroup 下几乎完全回退到 global（shrinkage weight 0.92）。[R1]

### Weaknesses

**[W1, Major]** 方法新颖性仍属增量。EC-HTE = 标准 HB CM + 标准校正 + 标准 CausalForestDML。[R1+R2 共识，唯一 Major]

**Mitigating factors**（R1+R2 共同确认）：
- (a) Theorem 1 精确恒等式是 genuine theoretical contribution
- (b) EC-HTE+PPCI 97% 超出 obvious combination
- (c) 4-DGP 正交设计属方法学创新

R2 综合判断：从 V1 的 "dealbreaker" 降级为 "acceptable limitation"。处于 Major 下限。

**[W2, Minor]** 诊断准则 AUC=0.75 作为 Abstract 第四贡献有 over-claim。建议降级为 practical finding。[R1+R2 共识]

**[W3, Minor]** 半合成 CATE injection 机制不够透明。[R1, R2 交叉同意]

**[W4, Minor]** Moderate regime 下 EC-HTE 实用价值有限（K=2/moderate crossover 永不发生）。R2 指出这实际上支撑 Theorem 1 的预测能力。[R1, R2 部分同意]

**[W5, Minor]** Imai & Yamamoto (2010) 区分仅一句话，需扩展（treatment variable vs effect modifier 误分类的结构差异）。[R1, R2 交叉强化]

**[W6, Minor]** Causal forest uncertainty propagation 不清楚（plug-in vs full propagation）。[R1, R2 交叉同意]

### Best 版本评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4.0 | 4.0 | **4.0** |
| Excitement | 3.5 | 3.5 | **3.5** |
| Reproducibility | — | 4.5 | **4.5** |
| **Overall (ARR)** | **3.5** | **3.5** | **3.5 (Borderline Conference)** |
| Director Scale | 4 | 4 | **4 (Weak Accept)** |
| Confidence | 4 | 3.5 | **4** |

**R1+R2 达成完全共识：所有维度评分一致。**

---

## Part B: Median 版本

### 与 Best 版本的关键差异

| 维度 | Best | Median | 影响 |
|------|------|--------|------|
| 实验覆盖 | 11/11 | 4/4（但缺 7 个关键实验） | Claim-evidence gap |
| Theorem 1 验证 | R²≥0.97, 3600 MC | 无直接验证 | Borderline Major |
| PPCI 验证 | 4-DGP, 97% reduction | 零实验 | **Major gap** |
| 诊断分析 | AUC + ROC + CV | AUC 仅在 Abstract | **Major gap** |
| Figures | 4 张主文图 | 0 张图 | 可读性显著下降 |
| Causal forest 结果 | Table 4 (bias -61%) | 无 | 方法仅在 DIM 上验证 |

### Median 特有的 Major Issues

**[MED-W1, Major]** PPCI 互补性列为 Abstract 第 3 贡献但零实验证据。Section 4.3 仅概念性描述。Claim-evidence mismatch。

**[MED-W2, Major]** 诊断 AUC=0.75 仅出现在 Abstract，正文无 ROC/sensitivity/specificity/CV。Orphan claim。

**[MED-W3, Borderline Major]** Theorem 1 缺直接 MC 验证。3 个 LLM 的间接观察不足以验证 quantitative identity。

### Median 版本评分（R1 单独）

| 维度 | R1 |
|------|-----|
| Soundness | **3.0** |
| Excitement | **3.0** |
| **Overall (ARR)** | **3.0 (Findings)** |
| Confidence | 4 |

---

## Part C: 综合判断

### Best vs Median 的核心教训

Median 版本的问题**不在于实验质量**（已覆盖的 4 个实验执行良好），而在于 **claims 超出了 evidence 的支撑范围**。R1 明确指出：如果 Median 版本将 Abstract 缩减为仅声明 bias identity + EC-HTE framework 两个贡献（删除 PPCI 互补性和 diagnostic AUC），soundness 会好得多，分数可上调至 3.5。

**对 Research Director 的关键信息**：

1. **必须包含的实验**（Best 有 / Median 缺，直接影响 0.5 分差距）：
   - 4-DGP 正交 PPCI 实验（支撑 PPCI 互补性声称）
   - Theorem 1 MC 验证（3600+ configs, R², tightness ratio）
   - 诊断 ROC 分析 + cross-validated AUC
   - 至少 2-3 张主文 figures

2. **如果时间不够做上述全部实验**：将 Abstract 收缩为仅 2 个有证据支撑的贡献（bias identity + EC-HTE），即可达到 Median 版本的最高潜力（~3.5 Borderline Conference）。

3. **方法新颖性是两个版本共有的唯一 Major issue**（R1+R2 共识）。Rebuttal 策略：强调 Theorem 1 精确恒等式非 trivially 从 Carroll et al. 导出 + 4-DGP 设计的方法学创新 + EC-HTE+PPCI 97% 的非平凡协同效果。

### Overall Assessment

| 版本 | ARR Score | 定位 | 置信度 |
|------|-----------|------|--------|
| **Best** | **3.5 (Borderline Conference)** | Findings 强候选 / Conference borderline | 高（R1+R2 共识） |
| **Median** | **3.0 (Findings)** | Findings 可接受 | 中（R1 单独） |

### 与 Round 1 的进展

| 轮次 | 综合评分 | 关键变化 |
|------|---------|---------|
| Round 1 (V1) | 3.0 Findings | 4 Critical + 2 Major |
| Round 2 Best | **3.5 Borderline Conference** ↑ | 全部 Critical 解决，1 Major 残留 |
| Round 2 Median | 3.0 Findings | 理论和 HB 改善，但 claim-evidence gap |

---

## Questions for Authors

1. PPCI 互补性：是否有 4-DGP 分离实验结果？如果没有，是否应从 Abstract 删除此贡献？
2. Diagnostic AUC=0.75：正文中对应的 ROC 分析在哪里？
3. Theorem 1 直接 MC 验证：是否有 R²/tightness ratio 数据？
4. 半合成 CATE injection：具体 τ_g 值和注入函数形式？
5. Moderate regime 实际普遍性：CSS 研究中 Δπ 通常在什么范围？
6. DSL per-subgroup baseline 为何劣于 EC-HTE？
7. Causal forest uncertainty propagation：plug-in 还是 full posterior？
8. 诊断准则是否愿意从 "contribution" 降级为 "practical finding"？

---

## Missing References

**V2 已补齐所有 V1 标记的遗漏。** 30+ 引用全面覆盖。无新的重大遗漏。R1 建议 Imai & Yamamoto 区分需扩展（非遗漏，而是讨论深度不足）。

---

## External Review

**状态：未请求。**

## Visual Layout Check

**状态：未派发。** Best 版本有 4 张主文图（R1 确认可读性大幅提升）；Median 版本 0 张图。

---

## Detailed Comments

### Theorem 1
- Best：精确恒等式 + MC 验证 → clean contribution
- Median：同一数学形式但无直接验证 → 可信度受限

### EC-HTE Framework
- HB 规格完整（两版本一致）
- Causal forest integration 描述仍薄（两版本一致）
- PPCI composition：Best 有 4-DGP 验证 / Median 零实验

### Experiments
- Best：11/11 覆盖，4-DGP 设计是亮点，RMSE tradeoff 诚实
- Median：4/4 覆盖，已做实验质量好，但缺关键对照实验
- 半合成 CATE injection 两版本均不够透明

### Presentation
- Best：5 tables + 4 figures，可读性好
- Median：0 figures，纯文字+表格，可读性差
- 两版本相关工作均全面（30+/22+）