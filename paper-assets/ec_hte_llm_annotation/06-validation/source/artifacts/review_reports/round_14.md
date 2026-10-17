---
round: 14
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T11:55:01.023137+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh Review)

**论文**: *When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects*
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**审稿模式**: Fresh（无上轮记忆）

---

## Summary

本文研究 LLM 标注中子群误分类率异质性对因果效应估计的影响。核心贡献是一个精确偏差分解恒等式（Theorem 1），表明全局混淆矩阵校正在子群级产生乘积形式偏差 δ_s · Δτ / (1−2π̄)，分解为子群误差偏离、处理效应异质性和矩阵求逆放大三个因子。该恒等式导出一个 Δτ-free 诊断条件（Proposition 5），并由此提出 EC-HTE 方法（层级贝叶斯子群校正）。实验覆盖合成网格、半合成数据（TweetEval + 11 个经验 LLM 混淆矩阵）和真实仇恨言论数据集。

---

## Strengths

**S1. 理论贡献扎实且新颖。** [R1-S1, R2-S2, 共识] Theorem 1 是精确有限总体恒等式（非渐近近似或界），R1 手动验证了 Appendix B 的完整矩阵代数推导。乘积分解直观揭示三个独立因子的交互机制。R² ≥ 0.97（合成网格）和 R² ≥ 0.92（10/11 真实 LLM）的验证有效连接理论与实践。

**S2. Δτ-free 诊断具有独立实用价值。** [R1-S2, R2-S2, 共识] Proposition 5 的 |δ_s|/((1−2π̄)·π_s) > 1 条件仅依赖误分类率，打破了"需要先估计处理效应才能判断是否该校正"的循环依赖。即使不使用 EC-HTE，该诊断对从业者有指导意义。

**S3. 实验覆盖极为全面。** [R1-S3, R2-S3, 共识] 32 页论文含 24 页附录，涵盖先验敏感性、κ guard 消融、Bootstrap SE、类别不平衡、非对称误分类、处理依赖误分类、混杂处理、子群错误指定、多 LLM 验证、R-learner/CausalForest 兼容性等。穷举式鲁棒性检验在 NLP 会议论文中罕见。

**S4. 诚实披露失败案例和适用条件。** [R1-S4, R2-S5, 共识] 论文明确报告 EC-HTE 在仇恨言论数据集上表现不佳，给出清晰的适用条件（Δπ > 0.15, n_expert ≥ 250, K ≤ 4），并展示 Table 22 中无真实 LLM 通过所有严格条件。学术诚实值得肯定。

**S5. 与经典文献关系清晰。** [R1-S1, R2-S4, 共识] 与 Frazis-Loewenstein (2003) 标量衰减的公式级区分明确（correction-induced bias vs attenuation），Table 1 中 F-L 校正使 bias 恶化的实证数据有力支持 Theorem 1。

---

## Weaknesses

### Must-Fix

**MF1. [Major] (A2) 对称误分类假设过强，主文讨论不足。** [R1-W2 + R2-N2, 共识]
- Table 20 显示真实 LLM 高度不对称（GPT-4o-mini FPR=0.517 vs FNR=0.102，比值 5:1）
- 诊断 AUC 从对称下 0.86 降至非对称下 0.66
- Remark 1 的理论扩展正确（B_s·1=0 仍成立），但嵌在理论节中不够突出
- R1 补充关键澄清：EC-HTE **方法本身**不依赖 (A2)——Algorithm 1 估计完整混淆矩阵。(A2) 仅影响 Theorem 1 简化公式和 Proposition 5 诊断的简洁形式。Appendix Z.6 非对称验证 R² = 0.991，coverage ≥ 93.5%
- **建议**: Section 5.4 或 Limitations 加 1-2 句明确：(1) 方法不依赖 (A2)；(2) 简化诊断在 FPR≠FNR 下准确性受限，应配合 R² 验证

**MF2. [Major] Abstract AUC=1.0 报告需更谨慎限定。** [R1-W3, R2 同意, 共识]
- 当前 Abstract 报告三级 AUC（1.0/0.86/0.63），但 AUC=1.0 放在最前给读者"几乎完美"的印象
- 条件 Δτ > 0 排除了误诊无关紧要的子群——如果 Δτ = 0，诊断正确与否无实际影响
- 无条件 AUC：合成 0.86，真实 LLM 仅 0.63
- **建议**: Abstract 优先报告无条件 AUC（0.86），将 1.0 作为条件性补充，提及真实 LLM 上 0.63

### Should-Fix

**SF1. [Major] 适用条件窄——Table 22 筛选结果应在主文更显著展示。** [R1-W1, R2 同意, 共识]
- EC-HTE 要求 Δπ > 0.15、n_expert ≥ 250 (K=2)、FNR_s < 0.50、K ≤ 4
- Table 22 显示无真实 LLM-数据集组合通过所有严格条件
- Relaxed screening 下 79% 配置 RMSE 优于 Global，所有 16 组合 coverage ≥ 93%
- R2 补充：方法并非完全不可用，但主文未充分呈现这一关键结论
- **建议**: (1) Section 5.4 明确引用 Table 22 结果；(2) 讨论自适应退化策略（而非二元"用 EC-HTE vs 用 Global"）

**SF2. [Major] 缺乏真实因果推断数据集验证。** [R2-N3, R1 部分同意, 共识但程度有分歧]
- 所有定量评估在合成/半合成数据上，仇恨言论案例仅展示异质性存在但无 ground-truth CATE
- R1 指出 Limitations 已坦诚说明原因（领域固有困难）——需要同时具备真实 CATE 和 LLM 标注误差的数据集目前不存在，半合成策略是标准做法
- 不阻挡接收，但降低 Excitement

**SF3. [Major] 遗漏密切相关工作。** [R2-W1, R1 同意, 共识]
- Gligoric et al. (2025, NAACL): LLM 标注统计推断并行工作
- Knox, Lucas, Cho (2022, ARPS): ML 代理变量因果偏差基础论文，本文设定的直接前驱
- 中优先级: Ura (2018, QE) HTE+误测量（连续效应修饰变量，与本文二元离散有区别）；Zhang et al. (2025) 贝叶斯 LLM 测量误差

**SF4. [Minor] PPCI 组合理论基础不充分。** [R1-W5, R2 同意, 共识]
- 仅在 1 个 DGP 配置下验证（Appendix L）
- 两种校正的顺序应用是否引入高阶交互效应未讨论
- **建议**: 简要讨论组合有效的充分条件，或增加 DGP 配置

**SF5. [Minor] Eq.6 方差传播独立性假设未显式说明。** [R1-W6, R2 同意, 共识]
- se_corrected 推导假设 CausalForest SE 和 CM 估计误差独立
- Expert labels 从全数据集抽样，与 CausalForest 训练数据有重叠时假设可能被违反
- **建议**: 显式说明假设并讨论影响

**SF6. [Minor] (A3) P(Z=1)=0.5 假设讨论不足。** [R2-W2, R1 同意, 共识]
- Appendix T R² ≥ 0.976 at P(Z=1)=0.1 缓解了担忧，但 RMSE ratio 退化到 1.06-1.68 应在主文提及

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：

1. **Theorem 1 推导正确且新颖** — R1 手动验证，R2 独立确认
2. **(A2) 假设过强但可修复** — 方法不依赖 (A2)，主文讨论不足是呈现问题
3. **Abstract AUC 报告需调整** — 优先报告无条件 AUC
4. **适用条件窄但诚实披露** — 需在主文更显著展示
5. **遗漏 Knox et al. 和 Gligoric et al.** — 应补充
6. **半合成验证是领域标准做法** — 不阻挡接收

---

## Reviewer Divergence

**D1. R2-N1 参考文献伪造指控 → 已撤除。** [R1 REBUT, 证据充分]
- R2 声称 6 条引用"被篡改或伪造"，其中 1 条（"Adwin et al."）"疑似捏造"
- R1 逐条核实 bib 文件，证明 5/6 条的 bib 数据与真实论文完全一致。R2 的错误源于系统性 PDF OCR 误读（Ashwin→Adwin, Camuffo→Carnullo, Messing→Meissner, Pieuchon→Pouzilhac, Blette→Birete）
- 唯一存疑：Cheng et al. 一个名字拼写（Rachit vs Raveesh），属个别元数据问题而非系统性篡改
- **结论**: N1 指控不成立，从 Critical 完全撤除。参考文献无系统性问题。

**D2. MC 精度（R1-W4 Major → R2 降级 Minor）。** [R2 REBUT, 理由成立]
- R1：HB EC-HTE |bias|=0.008 的 MC SE ≈ 0.005，相对标准误 ~62.5%，"7.4×" 精度不足
- R2 反驳：(1) 核心验证是 520 配置的 R² 回归（≥0.97），非单点估计；(2) Table 14 paired t-tests 72.7% 显著；(3) 增加 MC 不改变主结论
- **裁定**: 降级为 Minor。定性结论可靠，但建议在 Table 1 报告 MC 标准误以增强精确量化的可信度。

**D3. "Debiasing hurts" 标题是否夸大（R2-W3 → R1 REBUT）。** [R1 REBUT, 理由成立]
- R1："When" 是条件性表述，Proposition 5 精确刻画充要条件；14.9% 仅是一个参数点（τ(0)=0.03），有完整参数依赖分析；所有 8 个真实 LLM 均放大偏差
- **裁定**: 标题恰当，不构成问题。

**D4. Proposition 2 (A5 relaxation) 贡献（R1-W7 → R2 REBUT）。** [R2 REBUT, 理由成立]
- R1 认为是 Theorem 1 直接推论，应降级为 Remark
- R2 认为传递的实践信号（A5 非必要条件）有独立价值
- **裁定**: 呈现偏好问题，不影响正确性或评分。

---

## Questions（合并需作者澄清的问题）

**Q1.** [R1-Q1] κ ∈ [10, 50] 时有限样本余项具体量级多大？identity 的有限样本近似在 κ 中等偏大时是否不准确？

**Q2.** [R1-Q2] Table 22 "放松筛选"下 21% 失败配置的失败模式是什么——coverage 崩溃、RMSE 爆炸、还是 bias 反增？

**Q3.** [R1-Q3] Bootstrap B=100 与 B=500 的 coverage 差异是否验证过？标准建议 B ≥ 500 用于 SE 估计。

**Q4.** [R1-Q4] 为什么不用自适应公式 κ_adapt = 10√(n_expert/K) 替代固定 κ=100？Appendix A.1 提到但未用作默认值。

**Q5.** [R2-Q3] n_expert ≥ 200 (K=4) 在实际 CSS 研究中是否现实？（R1 补充：Appendix K 显示 n_expert=50 时 HB EC-HTE 仍优于 Global）

**Q6.** [R2-Q5] TweetEval 半合成实验中子群定义（has_hashtag × text_length_bin）的选择标准？是否存在 forking paths 问题？

---

## Missing References

**高优先级（两位 Reviewer 共识）：**
1. Gligoric et al. (2025, NAACL) — LLM 标注统计推断并行工作
2. Knox, Lucas, Cho (2022, ARPS) — ML 代理变量因果偏差基础论文

**中优先级：**
3. Ura (2018, QE) — HTE + 误测量（连续效应修饰变量，与本文二元离散有区别）
4. Zhang et al. (2025) — 贝叶斯 LLM 测量误差并行工作
5. Knox et al. (2020) — 行政记录中的因果推断与种族误分类
6. Jiang et al. (2020) — 预训练语言模型跨子群鲁棒性

---

## External Review (Stanford Agentic Reviewer)

未配置，未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 个 warning，11 个 info）。

**主要发现：**
- **[Warning] Pages 4-7 连续 4 页无 figure/table**：从 Figure 1 (page 3) 到 Table 1 (page 8) 跨越 5 页的视觉空白带。虽然 pages 4-5 有密集数学公式作为视觉变化，但 pages 6-7（方法描述 + 实验 setup）也无 display item。
- **[Warning] 正文仅 2 个 display items**（Figure 1 + Table 1）：同类论文通常 4-6 个。大量有价值的可视化（Figure 2 amplification heatmap、Figure 3 budget curves、applicability frontier）全部在 appendix。
- **[Warning] 正文引用 "Figure 2" 但 Figure 2 在 Appendix (page 14)**：审稿人无法在阅读流中直接看到。
- **[Info] Figure 1 在第 3 页**：处于审稿人前 3 页视觉锚点窗口内，三面板设计合理，Title-Abstract-Figure 1 叙事一致性良好。
- **[Info] Table 1 使用 booktabs 风格**：最优结果加粗，格式规范。
- **[Info] Limitations section 简洁**：约半栏，覆盖 3 个关键点，符合 EMNLP 要求。
- **[Info] 数学公式渲染正确**：无 LaTeX 错误残留，编号连续。
- **[Info] 参考文献格式统一**：未见 [?] 未解析引用。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 4/5 | 3.5/5 | 4/5 |
| Excitement | 3.5/5 | 3.5/5 | 3.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |

**合并 Soundness 4/5 理由**: R2 给 3.5 的主要原因是 N1（参考文献问题），该指控经 R1 事实核查后撤除。扣除 N1 后 R2 的 Soundness 评估与 R1 一致。

**评分理由**:
- **支撑 Conference (4.0) 的因素**: 理论贡献扎实（精确恒等式 + 正确证明 + R² ≥ 0.97 验证），Δτ-free 诊断有独立实用价值，实验覆盖极为全面（24 页附录），诚实披露失败案例和适用条件
- **阻止达到 Conference 的因素**: (A2) 对称假设与真实 LLM 行为脱节但主文讨论不足（MF1），Abstract AUC 报告有误导性（MF2），适用条件窄且 Table 22 零通过未在主文充分呈现（SF1），缺乏真实因果数据验证（SF2），遗漏 2 篇密切相关工作（SF3）
- **修订潜力**: MF1 和 MF2 可在修订中完全解决（主文加 1-2 句 + Abstract 重排）。SF1 和 SF3 同样可修复。SF2 是领域固有困难，无法通过修订解决但不阻挡接收。修复后有潜力达到 **4.0 (Conference)**。

**Confidence**: 4/5 — 两位 Reviewer 均仔细验证了核心数学推导并阅读全文。对因果推断测量误差文献和 LLM 标注文献较熟悉。不确定性主要在于 NLP 社区对此类方法论贡献的接受程度。

---

## Detailed Comments

### Section 1 (Introduction)
- 叙事弧完整：problem → why it matters → what we do → what we find
- Figure 1 在第 3 页，位置合理，三面板设计有效传达核心信息
- 脚注 1 消歧 "debiasing" 含义，位置恰当

### Section 2 (Related Work)
- 与 PPI/DSL/PPCI/ForestIV 的差异阐述清晰
- 与 Frazis-Loewenstein 的公式级区分明确
- **缺失**: Gligoric et al. (2025) 和 Knox et al. (2022) 应补充

### Section 3 (Theory)
- Theorem 1 推导正确完整，乘积分解优雅
- 假设 (A1)-(A5) 明确列出
- Remark 1 正确处理非对称扩展，但可更突出
- Proposition 3 (A5 relaxation) 和 Corollary 4 (Aggregate Bias) 增加理论完整性
- **建议**: Proposition 5 的条件在真实 LLM 非对称误分类下效用下降，应在此处或 Section 5 提及

### Section 4 (Method)
- Algorithm 1 伪代码清晰，包含前置条件检查和 fallback
- 层级贝叶斯估计的技术细节充分
- Eq.6 方差传播独立性假设应显式说明
- PPCI 组合仅在 1 个 DGP 验证，理论基础可加强

### Section 5 (Experiments)
- DGP 设计合理（合成 + 半合成），参数网格系统
- R² 验证策略有效连接理论与实践
- Table 1 格式规范，数据充分
- Operating conditions (Section 5.4) 列出清晰，但 Table 22 筛选结果应从附录移至此处
- 仇恨言论数据集上的诚实负面结果是亮点

### Section 6 (Conclusion)
- 简洁准确，无 overclaim
- 适当提及条件性结论

### Limitations
- 简洁（约半栏），覆盖 expert budget、scalability、假设不可检验性三个关键点
- 符合 EMNLP 要求（3 个点左右）

### Abstract
- 179 words，在 200 words 限制内
- AUC 报告顺序需调整（先 0.86 后 1.0）
- "14.9% sign reversal" 已加 τ(0)=0.03 限定

### 格式合规
- 正文 8 页，符合 EMNLP 2026 限制
- ACL template + [review] 模式，double-blind
- Author: "Anonymous"，无身份泄露
- 参考文献格式统一，无 [?] 引用