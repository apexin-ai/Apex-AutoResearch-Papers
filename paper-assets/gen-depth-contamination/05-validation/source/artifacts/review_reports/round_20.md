---
round: 20
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T13:53:28.733239+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — gen-depth-contamination (Round 20)

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**目标 Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**轮次**: 1 轮收敛（关键问题共识，无需 Round 2）

---

## Summary

本文形式化定义了"generational depth estimation"这一新任务，提出 K*（discrimination boundary）为分类器能可靠区分相邻递归生成深度的最大值（Eq. 1, θ=0.60）。使用 15 维手工统计特征 + OBD-LightGBM，在 10 个模型配置（6 架构家族, 1B-32B）、4 个文本域（C4, Wikipedia, arXiv, Code）、4 种解码策略上系统测量。核心发现：C4 web text K*=2（7/9 continuation-mode 配置, 4/6 families），θ-invariant 域排序 arXiv(3) > C4=Code(2) > Wikipedia(1)，DeBERTa 建立 two-tier ceiling（低复杂度域无提升，高复杂度域 +1），retrain-chain K*=7 vs prompt-chain K*=2。

---

## Strengths

**S1. 问题形式化新颖且填补了真实空白。** [R1+R2 共识] K* 将 "递归生成文本在某深度后不可区分" 这一模糊直觉转化为可操作的量化指标，填补了 binary detection（无深度估计）和 population-level model collapse theory（无 per-text 工具）之间的空白。

**S2. 实验覆盖面和统计严谨性达到高水准。** [R1+R2 共识] 10 模型 × 4 域 × 4 解码策略的系统测量，每个 K* claim 由 bootstrap 95% CI + permutation test 支撑。Cross-scorer ANOVA、LOFO cross-validation、changepoint analysis (PELT)、DeBERTa upper bound、retrain-chain 对比提供多角度交叉验证。附录约 50 张 table/figure 的消融分析远超同类工作。

**S3. θ-invariant domain ordering 是论文最强、最鲁棒的发现。** [R1+R2 共识] arXiv > C4 = Code > Wikipedia 的排序在 θ∈[0.55, 0.70] 全范围、跨架构、跨规模、跨 scorer 保持不变。Mistral-7B 在 C4 上 K*=1 但 arXiv 上 K*=3，提供了域结构（而非模型身份）驱动 discriminability 的强证据。这是一个不依赖 θ 选择的发现。

**S4. Confound 控制系统到位。** [R1] Wikipedia scorer confound 通过 cross-family scoring 解决；self-BLEU fold 内计算 + 14D ablation (Δ≤0.003)；length confound 分析（depths 1-5 within-model ≤6 tokens）。

**S5. DeBERTa two-tier ceiling 和 retrain-chain 对比有价值。** [R1+R2] 从两侧界定 K* 范围：15D statistical features 给出 lower bound，DeBERTa 给出 feature-dependent upper bound（C4/Code 匹配, Wikipedia/arXiv +1/+2）；prompt-chain K*=2 vs retrain-chain K*=7 区分了文本内在信息损失与训练动态效应。

**S6. Limitations section 极为坦诚。** [R1] 9 个方面的 explicit limitation，包括 Qwen family balance、marginal CI margins、filtering effect size diminishing at lower contamination ratios。

---

## Weaknesses

### Must-Fix (3)

**[MF-1] DPI→adjacent-pair distinguishability 论证缺口** [R1 N1, critical]
Section 3.1: DPI 保证 I(X;Y₁) ≥ I(X;Y₂) ≥ ... ≥ 0（累积信息关于原始 X 的衰减），但 K* 衡量的是相邻对 (Y_{k-1}, Y_k) 的 pairwise AUC。这两个量之间缺乏形式化桥梁。Introduction line 28 "DPI implies...motivating a finite discrimination boundary K*" 暗示了比实际更强的理论保证。有限 K* 的真正来源是 Markov chain ergodic convergence（相邻转移趋同），非 DPI 本身。
→ 建议：将 DPI 限定为 motivational，补充 Markov mixing 论证或直接定位为 empirical finding。

**[MF-2] θ=0.60 后验选择的循环性 / K*=2 的 threshold 依赖性** [R1 N2 + R2 W2, critical, 两位 Reviewer 共识]
θ 选在 1v2 AUC cluster (0.611-0.695) 和 2v3 cluster (0.549-0.589) 的经验间隔处。K*=2 的 stability window 仅 5pp [0.575, 0.625]：θ=0.55 时部分配置达 K*=3，θ=0.70 时全部降为 K*=1。LOFO θ̂∈[0.5725, 0.6004] 上界恰好 = 0.60（边缘非中心），1/9 不一致。论文标题和 abstract 以 K*=2 为卖点，但这个数字的 robustness 远不如 θ-invariant domain ordering。changepoint analysis (PELT, 35/37 agree within ±1) 是最强的 θ-free 验证但仅附录一句话提及。
→ 建议：(1) Abstract/Title framing 从 "K*=2" 转向 "θ-invariant domain ordering + bounded K*≤3"；(2) PELT 结果提升到正文；(3) 显式承认 K* 是 feature-set-and-threshold-conditioned operational lower bound。

**[MF-3] 遗漏两篇高度相关并行/近期工作，gap statement 需修正** [R2 W1, critical]
(a) Mohamed et al. (ACL 2025 main), "LLM as a Broken Telephone: Iterative Generation Distorts Information" (arXiv:2502.20258, ACL Anthology 2025.acl-long.371)：研究 LLM 迭代生成中信息失真的累积，已发表于 ACL 主会议。
(b) Geng et al. (arXiv:2603.11228, March 2026), "Markovian Generation Chains in Large Language Models"：将迭代 LLM 推理形式化为 Markov chain，与 Section 3.1 的 formulation 几乎平行。
Introduction para 4 的 gap statement "No existing method estimates how many rounds of recursive generation a text has undergone" 需修正为更精确表述（如 "No existing method provides a per-text operational estimate of generational depth"）。
→ 建议：Section 2 新增 "Iterative generation dynamics" 段落讨论两篇工作，明确增量在于 per-text, per-depth operational tool。

### Should-Fix (10)

**[SF-1] Qwen 家族 5/10 配置偏重** [R1 W1 + R2 W5, 共识]
"7/9 continuation-mode" 含 4 个 Qwen，按 family 计为 "4/6 families"。建议 Abstract 和 Section 4.1 主 claim 以 "4/6 families" 为首要统计量。

**[SF-2] Cross-scorer 下 Qwen-cont K* 从 2 降至 1 未在主文充分报告** [R1 W2, R2 Q2 印证]
Table S13 显示 Pythia/OLMo scoring 下 Qwen-cont 1v2 AUC 降至 0.592/0.586。Under cross-scoring, "7/9" → "6/9"。建议 Section 4.2 显式报告此降级。

**[SF-3] Filtering contribution 效果量不足以列为独立 contribution** [R1 W4 + R2 W3, 共识]
100% synthetic: binary vs no-filter 0.76pp MMLU；10%: 0.21pp。Pythia replication: 0.17pp。所有策略均低于 base model（损害减轻而非净改善）。建议将 contributions (c) 降级为 consistency check，不与 (a)(b) 并列。

**[SF-4] OBD vs DeBERTa "two-tier ceiling" 表述过强** [R1 W3]
15D statistics vs 184M fine-tuned encoder 的 capacity 差异巨大。DeBERTa 在 Wikipedia 将 K* 从 1 提到 3，说明 K*=1 并非 domain 固有 ceiling。建议改为 "feature-set-dependent gap"，承认更强表示可能进一步提升 K*。

**[SF-5] Transfer aggregate (80-92%) 与 boundary fragility (4/6 pairs < θ) 表述张力** [R1 W2]
Abstract contribution (c) 强调 "80-92% accuracy retention" 但未提及 7B boundary-level 4/6 pairs 落在 θ 以下的脆弱性。建议在 Abstract 和正文中平衡报告。

**[SF-6] 方法论新颖性有限，未充分论证 empirical characterization study 的独立价值** [R2 W4]
15D 特征 + OBD-LightGBM 均为标准工具。论文 novelty 主要在问题定义和实证发现。建议在 Introduction 加 2-3 句 explicit rationale：简单方法建立 lower bound，任何更复杂方法只能提升（DeBERTa 已证明）。

**[SF-7] Conclusion 过于简短（6行）** [R2 W6]
未综合 Discussion 中的 broader implications（data curation 指导、model collapse 连接、framework 可扩展性、future directions）。建议扩展到 12-15 行。

**[SF-8] Prompt-chain vs retrain-chain 混合场景讨论不足** [R2 W7]
真实 web-scale 污染是 prompt-chain 和 retrain-chain 的混合体。建议 Discussion 增加 2-3 句讨论混合场景预期或声明为 open question。

**[SF-9] Scale 外推 "200-500B crossover" 仅基于 3 个点** [R1 W4]
1.5B/14B/32B 三点 log-linear 拟合，AUC 总降幅仅 0.8pp。建议改为定性表述（"scale trend suggests eventual decay"）。

**[SF-10] arXiv n=2,200 样本量风险** [R1 W5]
C4 subsampled to n=2,200 yields K*=1，cross-scorer 下仅 2/4 generators 通过 strict CI criterion。建议主文 arXiv K*=3 讨论时加入样本量限定。

### Minor (6)

- **[M-1]** Retrain-chain CI 用 z=1.96 但仅 K=5 folds，应用 t 分布 (t_{0.025,4}=2.776)，当前 CI 低估 ~42%。[R1]
- **[M-2]** Abstract 信息密度过高，建议分层呈现。[R2]
- **[M-3]** K*, K*_theory, K*_neural, K*_binary 符号系统缺统一符号表。[R2]
- **[M-4]** "model-free" 表述不准确（surprisal 需 scorer model），应改 "generator-independent"。[R1]
- **[M-5]** Bootstrap resample 数不一致 (1,000/10,000)，建议统一或说明标准。[R1]
- **[M-6]** bib 条目 first_author mismatch: alemohammad2024 (bib vs API), levy2008 (levy vs lévy)。[R2]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：
1. θ 后验选择循环性 / threshold 依赖性是核心方法论弱点 → Must-Fix
2. Domain ordering 是论文最鲁棒、最有价值的发现
3. Filtering 效果量不足以作为独立 contribution → 应降级
4. Qwen 5/10 配置偏重 → "4/6 families" 应为首要统计量
5. Cross-scorer Qwen-cont K* 降级应在主文报告
6. 实验覆盖面和统计严谨性出色

## Reviewer Divergence

**评分差异 (R1: 3.5, R2: 3.0)**：主要分歧在 Excitement 维度（R1: 3.5, R2: 2.5）。R2 认为方法论新颖性不足（standard features + standard classifier）限制了主会议接收资格；R1 对 K* 概念贡献和实验深度的评价更高。此分歧属于合理的学术判断差异，非事实矛盾。

**DPI 论证缺口**：R1 列为 Must-Fix，R2 未单独提出但在 S1 中承认 DPI 提供 motivation。Director 判断：R1 的技术观察正确（DPI ≠ adjacent-pair decay），列入 Must-Fix。

**遗漏文献**：R2 列为 Must-Fix（Mohamed et al., Geng et al.），R1 未覆盖此点。Director 判断：R2 的文献发现经验证确实高度相关（尤其 Geng et al. 的 Markov chain formulation），列入 Must-Fix。

---

## Questions（需作者澄清）

1. 是否观察到 AUC 非单调情况（如 AUC_2v3 < θ 但 AUC_3v4 > θ）？[R1]
2. 排除所有 margin < 1pp 的 boundary cases 后，K*=2 的 support 降到多少？[R2]
3. Qwen-cont self-scored K*=2 但 cross-scored K*=1：self-scorer 是否存在系统性偏差？所有 self-scored K*=2 配置是否都有此风险？[R1+R2]
4. DeBERTa 在 Wikipedia K*=1→3：K* 是 domain property 还是 classifier-feature-space property？[R1+R2]
5. Retrain-chain K*=7 在更大规模（7B+）或 full fine-tuning 下是否有变化预期？[R2]
6. Filtering 所有策略均低于 base model："损害减轻" vs "无损过滤" 的差距是否限制实用性？[R1]

---

## Missing References

1. **Mohamed et al. (ACL 2025)** "LLM as a Broken Telephone: Iterative Generation Distorts Information." arXiv:2502.20258. [R2, Must-cite]
2. **Geng et al. (2026)** "Markovian Generation Chains in Large Language Models." arXiv:2603.11228. [R2, Must-cite]
3. **Gillman et al. (ICML 2024)** "Self-Correcting Self-Consuming Loops for Generative Model Training." arXiv:2402.07087. [R2, recommended]
4. Multi-generational watermark tracking literature [R1, recommended]
5. Optimal threshold selection literature (Youden's J, cost-sensitive calibration) [R1, recommended]

---

## External Review

外部审稿未配置（项目 config 中无 external_review 设置）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已派发但超时（300s timeout）。未能完成 PDF 渲染和排版检查。用户可选择重新触发。

---

## Overall Assessment

### 评分: 3.0 (Findings)

**Soundness**: 3.5/5 — 实验设计严谨，统计验证充分（bootstrap CI, permutation test, ANOVA, LOFO, changepoint）。但 K*=2 的 threshold 依赖性（θ±5pp 改变结论）、DPI→K* 论证缺口、多个 marginal boundary cases 削弱量化 claim 强度。

**Excitement**: 3.0/5 — 问题定义（K*）新颖有启发性，θ-invariant domain ordering 是有价值的发现。但方法本身为标准工具组合，practical impact 有限（filtering 效果量小，prompt-chain only 限制适用性），方法论创新不足以支撑主会议。

**Reproducibility**: 4/5 — 实验细节充分，代码承诺 acceptance 后释放。

**置信度**: 4/5

### 判断依据

论文的核心贡献是问题定义（K*）和大规模实证发现（θ-invariant domain ordering, two-tier ceiling, K*≤3 under model-free features），而非方法创新。作为 empirical characterization study，实验严谨性出色。但以下因素使其更适合 Findings 而非主会议：

1. **方法论新颖性不足**：15D 手工特征 + OBD-LightGBM + DeBERTa probe 均为标准工具，论文未提出新方法。
2. **核心量化结论的 robustness**：K*=2 完全依赖 θ=0.60，且 θ 的 stability window 仅 5pp。真正 robust 的发现是 domain ordering，但当前 framing 以 K*=2 为主角。
3. **实用影响有限**：filtering consistency check 效果量极小（0.76pp MMLU），且仅在 100% synthetic 下测试；prompt-chain only 限制了对真实 web-scale 污染的适用性。
4. **3 个 Must-Fix 问题**待解决：DPI 论证缺口、θ framing、遗漏文献。

### 修改建议优先级

**如果修改到位（MF-1/2/3 + SF-1/2/3 充分解决），可达 3.5 (Borderline Conference)**：
1. 重新 framing：以 θ-invariant domain ordering 和 bounded K*≤3 为主要发现，K*=2 作为操作性结论
2. 补充 DPI→Markov mixing 论证 + 遗漏文献
3. 将 filtering 降级为 consistency check
4. 主 claim 改用 "4/6 families"，cross-scorer 降级在主文报告
5. PELT changepoint 结果提升到正文
6. 扩展 Conclusion

### Issue Tracker

已更新至 `projects/gen-depth-contamination/artifacts/review_issues.yaml`：3 critical (open), 10 warning (open), 6 minor (open)。
