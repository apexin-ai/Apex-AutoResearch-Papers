---
round: 1
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T04:41:04.814881+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告：Aggregate Convergence, Per-Example Divergence

**论文**: Aggregate Convergence, Per-Example Divergence: Decoupled Effects of Attention in Hybrid Recurrent Architectures
**Venue**: EMNLP 2026 (ARR June 2026)
**类别**: Long Paper
**审稿模式**: 圆桌审稿（2 Reviewer × 1 轮独立审稿 + 交叉回应）
**日期**: 2026-05-20

---

## Summary

本文利用 Wang et al. (2025) 的 hybrid recurrent model zoo（GatedDeltaNet/RetNet/HGRN2 × 5 种 attention ratio × 2 种 scale），在 10 个 benchmark 上系统分析 attention 对跨架构一致性的影响。核心发现：在 LAMBADA 上，aggregate 层面跨架构方差随 attention 单调递减（ρ = −1.0, BCa 95% CI [−1.0, −0.7]），但 per-example helped/hurt set 的 Jaccard similarity 在最低 attention 比例即饱和（~0.10），不再随 attention 增加提升。作者将此称为 "decoupling"，连接到 underspecification 框架。

---

## Strengths

1. **研究问题有价值且切入角度新颖**：aggregate convergence vs per-example divergence 的分离框架连接了 underspecification 文献和 hybrid model 设计实践，cross-architecture dose-response 分析是既有文献（D'Amour et al., McCoy et al.）未涉及的维度。

2. **受控实验设计**：使用共享 model zoo 消除训练数据和超参数混淆变量，隔离 attention ratio 效应，实验控制得当。

3. **统计方法论标准高**：exact permutation test（120 种排列全枚举）、BCa bootstrap CI（10,000 重采样）、Bonferroni 校正、permutation test for Jaccard，在分析性论文中属于高标准。

4. **高透明度**：Limitations 部分主动讨论 6 项局限（统计功效、scope、scale、架构覆盖、观察性设计、仅 pre-training），Appendix A-G 提供丰富的 robustness check 和 sensitivity analysis。

5. **写作清晰**：Figure 1 三面板设计有效传达核心发现，叙事结构逻辑通顺。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1 [统计功效根本性不足]** ⟨R1-N1, R1-N2 | 共识⟩
核心定量 claim（ρ = −1.0）基于 n=5 attention ratios，Bonferroni 校正后 adjusted p = 0.100 未达 α = 0.05。作者转向 CI 作为 primary evidence，但这是 post-hoc 的证据标准切换。更严重的是，替代证据——n=3 架构级 bootstrap CI——仅有 24 种非退化组合（3³ - 3 = 24），10,000 次迭代只是在这 24 种结果中反复抽样，CI 宽度不携带有意义的不确定性信息。核心统计证据链在两个关键环节上同时不可靠。

**MF-2 [Decoupling claim 可能是 floor effect]** ⟨R1-N3 | 共识⟩
Jaccard ~0.094–0.104 仅为随机基线（~0.039）的约 2.5 倍。Helped set 仅占总样本 9–12%（~400–600/5,153），两个同等大小弱相关集合的 Jaccard 自然停留在低水平。"饱和" 可能只是 "从未离开过底部"。论文未计算 Jaccard 理论上界，也未报告相对于基线的 effect size，decoupling claim 缺乏充分支撑。

**MF-3 [GDN confound 实质性削弱核心结果]** ⟨R1-N4 | 共识⟩
GDN h3-1 使用 16 heads（vs 其他配置 32 heads）。移除 GDN 后 LAMBADA ρ 从 −1.0 降至 −0.7（p = .233），MMLU 从 −0.7 反转为 +0.6。核心 convergence 发现在很大程度上受单一有混淆变量的架构驱动。此分析仅在 Appendix C，正文讨论严重不足。

**MF-4 [泛化性严重不足]** ⟨R2-N1, R1-W1 | 共识⟩
10 个 benchmark 中仅 LAMBADA 一个展示 monotonic convergence，且该 benchmark 的 Bonferroni 校正后 p = .100 亦未通过严格阈值。即便仅看 6 个 pre-registered benchmark 也仅 1/6 命中，兼容 family-wise error rate 控制后的偶然发现解释。标题和 abstract 暗示通用发现，与证据覆盖范围不匹配。

**MF-5 [缺少关键相关工作]** ⟨R2-N3 | 共识⟩
遗漏三条重要文献线：(1) Waleffe et al. (2024) "An Empirical Study of Mamba-based Language Models"——8B 规模系统比较 hybrid 架构的里程碑工作；(2) Predictive multiplicity 文献（Marx et al. 2020; Watson-Daniels et al. 2023; Hsu & Calmon 2022）——cross-architecture prediction 分歧正是 predictive multiplicity 的定义，概念匹配度高于 underspecification；(3) Basu (2025) "When Does Content-Based Routing Work?"——直接研究 hybrid 模型中 attention 分配。

### Should-Fix

**SF-1** ⟨W-scale | 共识⟩ Scale comparison 仅 340M 和 1.3B 两个点，"sufficient scale as necessary condition" 结论过度，应降级为 preliminary observation。

**SF-2** ⟨W-title | 共识⟩ 标题 scope 远大于实际贡献。建议加入 "on LAMBADA"、"A Case Study" 或其他限定语。

**SF-3** ⟨W-preregistration | 共识⟩ Pre-registration 声称仅在 Appendix A，无外部可验证性。应提供 OSF 时间戳或改为 confirmatory/exploratory split 措辞。

**SF-4** ⟨W-entropy | 共识⟩ HGRN2 ΔH = +0.0420 vs GDN −0.0009（~47 倍差异），"all negligible" 的 blanket conclusion 忽略架构间异质性，应分架构讨论。

**SF-5** ⟨W-practical | 部分共识⟩ Practical implications 薄弱，缺乏具体可操作的架构选择或 ensemble 策略建议（R1 部分反驳：ARR 不应因缺少 recipe 惩罚分析论文）。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下问题上完全达成一致：

1. **统计证据链结构性薄弱**：n=5 检验功效不足 + n=3 bootstrap 退化 + Bonferroni 后不显著，三重叠加使核心 claim 的统计基础不稳固
2. **Jaccard floor effect 是 decoupling claim 的关键替代解释**，论文未排除
3. **GDN confound 必须在正文充分讨论**，当前仅在 Appendix 不可接受
4. **泛化性不足**：1/10（或 1/6 pre-registered）benchmark 支撑核心 claim
5. **Scale 结论过度**：2 个数据点不支撑 "necessary condition" 声明
6. **缺少 predictive multiplicity 文献线和 Waleffe et al.**
7. **标题 scope 需缩窄**

## Reviewer Divergence [REBUT]

1. **新颖性评估**：R1 认为 cross-architecture dose-response 分析维度有框架增量（≠ D'Amour/McCoy 的同架构不同 seed），excitement 可达 3/5；R2 认为本质是已知现象在新领域的验证，excitement 仅 2/5。双方均同意缺乏机制解释是共同弱点。

2. **引用数量**：R2 认为 30 篇偏少；R1 认为是质量问题而非数量问题，补上遗漏的 3-5 篇即可。

3. **纯分析论文定位**：R2 认为无训练/无新方法需额外强 insight 补偿；R1 认为 ARR guidelines (H5, H7) 不应因论文类型惩罚。

---

## Questions（需作者在 rebuttal 中回答）

1. 能否计算 Jaccard 理论上界并报告相对 effect size，以区分 "true saturation" 和 "floor effect"？
2. 能否补充 example-level bootstrap CI（利用现有 5,153 个样本）替代退化的 architecture-level bootstrap？
3. 移除 GDN 后，RetNet-HGRN2 两架构的 per-example decoupling 是否仍然成立？
4. 是否存在其他 retrieval 类 benchmark（如 Natural Questions, TriviaQA）可用于验证 LAMBADA 发现的复现性？
5. 相对于 McCoy et al. (2020) 的具体增量贡献是什么——是架构类型不同、attention ratio 连续变量、还是 timescale 分离？
6. Underspecification 框架 vs predictive multiplicity 框架，哪个更精确匹配本文的 cross-architecture 设定？

---

## Missing References

1. **Waleffe et al. (2024)** "An Empirical Study of Mamba-based Language Models" — 8B 规模 hybrid 架构系统比较
2. **Marx et al. (2020)** "Predictive Multiplicity in Classification" — predictive multiplicity 奠基文献
3. **Watson-Daniels et al. (2023)** "Predictive Multiplicity in Probabilistic Classification" — predictive multiplicity 扩展
4. **Hsu & Calmon (2022)** "Rashomon Capacity: A Metric for Predictive Multiplicity in Classification" — multiplicity 度量
5. **Basu (2025)** "When Does Content-Based Routing Work?" — hybrid 模型 attention 分配

---

## External Review (Stanford Agentic Reviewer)

**状态：未返回（pending）**

外部审稿请求已于 2026-05-20T04:28 发送，截至报告投递时仍处于 pending 状态。外部结果到达后将作为补充材料发送至 Group C。

---

## Visual Layout Check（非评分项）

**状态：已完成** | 0 critical / 3 warning / 7 info

### Warnings
1. **Pages 3-5**：连续 3 页纯文本（Related Work + Method），无任何 figure/table/equation 穿插，缺乏视觉锚点。建议在 Method 段加入架构概览图或实验设计示意图。
2. **Pages 1-8**：主体正文仅 4 个 display items（2 figure + 2 table），对实证论文偏少（通常 5-8 个）。大量结果（Tables 3-12）全部堆在附录，主体说服力被稀释。
3. **Page 14**：末页仅约 1/3 有内容，下方约 2/3 空白，附录空间未充分利用。

### Info
- Figure 1 子图 axis label 和 legend 字号偏小（约正文 60%）
- Figure 2 数据点密集，部分重叠，考虑全宽展示或加 jitter
- 第 1 页无视觉锚点，Figure 1 在第 2 页顶部，建议提升至第 1 页底部
- Table 1 格式规范，LAMBADA 行已加粗标注
- Table 2 Net 列 +/- 数值未加粗标注极值
- References 格式一致，无 [?] 未解析引用
- 附录表格格式规范

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 2.5 | 3.5 | 3.0 |
| Excitement | 3.0 | 2.0 | 2.5 |
| Reproducibility | 4.0 | — | 4.0 |
| Confidence | 4.0 | 4.0 | 4.0 |
| **Overall** | **3.0** | **2.5** | **3.0** |

**评分理由**：

研究问题有价值（aggregate vs per-example 行为的分离），实验设计利用受控 model zoo 消除混淆变量，统计方法论框架在意图上严谨。但核心统计证据链存在结构性弱点：(1) n=5 检验 Bonferroni 后不显著且 p→CI 转向是 post-hoc；(2) n=3 bootstrap CI 退化；(3) decoupling claim 的 Jaccard 证据可能是 floor effect；(4) GDN confound 使核心结果受单一架构驱动；(5) 仅 1/10 benchmark 支撑核心 claim。这些问题叠加后，证据力度不足以支撑主会议（4.0）接收，但研究问题的价值和分析框架的创意使其适合 Findings track。

**置信度**: 4/5（两位 Reviewer 均熟悉统计方法和 hybrid architecture 文献）

**Rebuttal 可能上调条件**（R2 明确提出）：提供 Jaccard 理论上界分析 + 外部交叉验证 + 正文讨论 GDN confound → 可考虑上调至 3.5（Borderline Conference）。

---

## Detailed Comments

### Section 1 (Introduction)
- Figure 1 有效传达核心发现，但首页无视觉元素，建议提升
- Contribution bullets 准确但 scope 暗示过于通用

### Section 2 (Related Work)
- 缺少 predictive multiplicity 文献线（与 underspecification 有关键区别：后者是同一 pipeline 不同 run，前者关注不同模型间的 prediction 分歧，更匹配本文设定）
- 缺少 Waleffe et al. (2024) 和 Basu (2025)
- 现有引用覆盖面在 hybrid architecture 和 per-example analysis 方面合理

### Section 3 (Method)
- Task taxonomy pre-registration 声称需外部可验证性
- Pages 3-5 纯文本缺乏视觉锚点，建议加入架构概览图

### Section 4 (Experiments)
- Table 1：应同时报告含/不含 GDN 的结果
- Section 4.3-4.4：Jaccard floor effect 需正面讨论
- Section 4.4：HGRN2 和 GDN 的 entropy 差异不应用 blanket "negligible" 概括
- Section 4.5：Robustness analysis 揭示 GDN 依赖性，应在正文（非仅 Appendix）充分讨论

### Section 5 (Conclusion)
- "sufficient scale as necessary condition" 措辞应降级
- Future work 方向合理但 practical implications 可更具体

### Limitations
- 坦诚全面，是论文的一个亮点

### Appendix
- 丰富完整，但部分关键分析（GDN confound, entropy heterogeneity）应上移到正文

### 格式合规性
- ACL 两栏模板 ✅
- Double-blind 匿名 ✅
- Limitations 节 ✅
- Ethics Statement ✅
- 正文页数需确认是否 ≤ 8 页（视觉审查显示 8 页正文 + appendix）