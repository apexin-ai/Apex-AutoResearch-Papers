---
round: 1
review_mode: continue
overall_score: weak reject
timestamp: 2026-05-28T05:16:59.789463+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---


# 审稿报告 — diff_collision_sdf Round 1

**Venue**: CoRL 2026
**Reviewers**: R1 (方法/实验/统计), R2 (新颖性/相关工作/贡献), R3 (写作/格式/伦理)
**交叉回应**: 3/3 完成
**轮次**: 1 轮收敛（关键问题已达成共识）

---

## Summary

论文提出 displacement-filtered Collision Avoidance Rate (dfCAR) 来诊断 VLA 安全评估中 action collapse 导致的 CAR 指标虚高现象，并通过 oracle SDF refinement 和 training-time SDF auxiliary loss 两组实验论证 EE-only SDF 集成在碰撞避免上的无效性。实验基于 SafeLIBERO benchmark，测试 Pi0 和 Pi0.5 两个模型族。

---

## Strengths

1. **诊断贡献有实际价值**：action collapse 污染 CAR 是一个此前未被系统性文档化的评估 artifact。dfCAR 作为诊断工具简单有效，Table 2 显示 Pi0 Full-FT 的 99.4% "safe" episodes 实为 action collapse——这一定量发现令人震惊且具社区影响力。[3/3 共识]

2. **实验规模可观**：100+ experiments, 6000+ episodes 的系统性实证，覆盖多个 LoRA 配置、SDF λ 值和 seeds，工作量扎实。

3. **Bimodal distribution 发现非 trivial**：Appendix A Figure 5 中位移分布的 5 个数量级 gap (<1μm vs >200mm) 使 τ_d 阈值在 [2, 200]mm 范围内高度鲁棒（Appendix B Table 6），这不是先验可预测的。

4. **排版质量良好**：booktabs 风格表格、无未解析引用、marker 形状区分模型族兼顾色盲友好性。

---

## Weaknesses（按严重性排序）

### Must-Fix (Critical)

**W1. 统计方法论存在根本缺陷 [R1-N1, R1-N2 | 3/3 共识]**

(a) Permutation test 的 null distribution 将 λ=0.005 数据纳入 null group，理由是"观察到它与 LoRA-only 无差异"——这是 data-dependent null construction，违反假设检验的基本原则。C(9,3)=84 的排列粒度使 p 值分辨率极低。

(b) p=0.131 的 non-significance 被解读为 "SDF adds zero benefit"，犯了经典的 absence of evidence ≠ evidence of absence 错误。论文自身数据（Appendix J Table 13）显示 λ=0.1 在全部 3 个 eval seeds 上一致高于 LoRA-only（+1.5, +2.5, +5.5 pp），且 SDF σ=0.9pp < LoRA σ=2.0pp。在 n=3 seeds 功效极低的前提下，这种一致方向性提升提示可能存在小但真实的正效应。论文未报告 statistical power 或 effect size 分析。

**W2. 实验范围过窄，无法支撑论文的通用性声明 [R1-N3, R2-N1, R3-N1 | 3/3 共识]**

仅 1 个 benchmark (SafeLIBERO)、2 个模型族 (Pi0, Pi0.5)、4 个 pick-and-place 任务、仿真环境。标题和 abstract 做出关于 "VLA safety evaluation" 的通用声明，但证据仅覆盖极窄的实验条件。Pi0.5 的 dfCAR=28.5% 表明 fake safety 问题并非普遍存在。缺少：(a) 其他 benchmark (e.g., RoboCasa, CALVIN)；(b) 其他模型架构 (OpenVLA, RT-2)；(c) 真实机器人验证。

**W3. 标题 framing 过度 [R2-W3, R3-W1 | 3/3 共识]**

"When 98% of Collision Avoidance is an Illusion" 中 98% 仅出现在 Pi0+A1——一个因 parameter-name mismatch 导致 LoRA 未加载的 broken 配置（Table 2, Fake Safe = 99.6%）。Pi0.5 完全不受影响（dfCAR = raw CAR = 28.5%）。标题暗示 universality 但数据仅支持 specificity。

**W4. 与 SafeVLA/VLSA 正向结果的矛盾未充分解释 [R2-N2 | 3/3 共识]**

论文仅测试了 EE-only auxiliary SDF loss 这一特定集成方式，但叙事框架暗示 SDF-based safety 方法普遍无效。SafeVLA (CMDP + constrained optimization) 和 VLSA (control barrier functions) 在不同集成路径上报告了正向结果——论文未解释差异来源，也未在 Discussion 中区分三种 SDF 集成路径。

### Should-Fix (Warning)

**W5. Oracle 实验生态效度 [R1-W1 | 3/3 共识]**：主要 oracle 实验基于 Pi0+A1 (TSR≈0%)，在不产生有意义动作的策略上测试碰撞避免的有效性，推广意义有限。Section 5 正文应更突出这一 caveat。

**W6. dfCAR 位移测量不一致 [R1-W2 | 3/3 共识]**：Pi0 使用 obstacle displacement，Pi0.5 使用 EE displacement，仅以脚注说明。核心 metric 的测量基础不一致应在 Section 3.2 正文中论证等价性。

**W7. n=3 seeds 统计力度不足 [R1-W3 | 3/3 共识]**：支撑 Claim 3 的核心实验仅 3 seeds，Phase 2 ablation 仅 1 seed。论文未在主文中讨论 statistical power 限制。

**W8. Limitations 不充分 [R3-N1 | 3/3 共识]**：未明确声明全部实验在仿真环境完成；缺少 sim-to-real gap 讨论（碰撞检测差异、传感器噪声对 dfCAR 的影响、action collapse 在真实机器人上是否同样存在）。

**W9. Broader Impact 严重不足 [R3-N2 | 3/3 共识]**：挑战现有安全评估范式的论文仅一句 broader impact 声明，未讨论 dfCAR 误用风险、responsible disclosure、或"VLA safety research is futile"的潜在误读。

**W10. 术语混用 [R3-W2 | 3/3 共识]**：frozen episodes / action-collapsed episodes / fake safety 交替使用，增加认知负担。应统一为 "action-collapsed episodes"。

**W11. 相关工作可能遗漏 [R2-W1 | 2/3]**：HazardArena、VLA safety survey (arXiv 2604.23775)、VLA-Risk、D2PPO 等 2025-2026 文献未被引用。

**W12. dfCAR 未与替代 filter 对比 [R2-W2 | 2/3]**：未讨论 action variance、velocity-based filter 等替代方案，削弱方法论贡献的说服力。

**W13. λ 搜索粒度过粗 [R1-W5 | 2/3]**：仅 3 个点 (0.005, 0.01, 0.1)，0.01-0.1 间跨 10 倍。"20× range" 反复强调（5+ 次）在 3 个数据点支撑下有 overselling 之嫌。

**W14. Discussion future work 过于简略 [R2-W4 | 2/3]**：三个方向各一句话，无具体方案。诊断性论文缺少建设性展望削弱平衡感。

---

## Reviewer Consensus [AGREE]

以下问题获 3/3 Reviewer 独立提出或在交叉回应中一致同意：

1. **实验范围过窄** → 无法支撑通用性声明（最高优先级）
2. **统计 claim 超越证据支撑** → "zero benefit" 断言过强，Appendix J 数据反驳自身论点
3. **标题夸大** → "98%" 仅适用于 broken 配置
4. **Permutation test 方法论** → data-dependent null 违反假设检验原则
5. **Limitations/Broader Impact 不足** → 仿真限制和社会影响讨论缺失
6. **SafeVLA/VLSA 矛盾未解释** → 论文 scope 与叙事 scope 不匹配

## Reviewer Divergence [REBUT]

以下问题存在分歧，以多数决记录：

1. **Claim 1 新颖性**：R2 认为 "action collapse → inflated CAR" 概念上直觉。R1/R3 REBUT——实证规模（99.4% fake safe rate）和 bimodal distribution 发现有独立价值。**多数判定**：Claim 1 的贡献在于系统性实证文档化，非概念新颖性。论文 framing 应调整为"首次大规模实证确认"。

2. **Claim 2/3 独立性**：R2 认为两个 claim 是同一 insight 的两面。R1/R3 REBUT——Claim 2 测试 inference-time oracle (architectural failure)，Claim 3 测试 training-time loss (signal redundancy)，机理不同。**多数判定**：两者逻辑独立，但论文行文可更清晰地说明区分。

3. **Figure 1 位置**：R3 认为应在第 1 页。R2 REBUT——PMLR/CoRL 格式中 Figure 1 在第 2 页是标准做法。**多数判定**：非问题。

4. **Abstract 压缩度**：R3 认为信息密度过高。R1/R2 REBUT——8 页限制下当前压缩合理。**多数判定**：可微调措辞但非结构性问题。

---

## Questions（需作者回应）

1. Permutation test 中将 λ=0.005 纳入 null group 的决策是否在实验设计阶段预注册，还是在观察数据后决定？如果仅用 LoRA-only 3 seeds 构建 null，Claim 3 的结论是否改变？

2. 论文是否进行了 statistical power analysis？在 n=3 seeds 的样本量下，最小可检测效应量 (MDE) 是多少？Appendix J 中 λ=0.1 的一致正效应 (+1.5 ~ +5.5 pp) 是否计划在更大样本量下验证？

3. dfCAR 中 Pi0 使用 obstacle displacement、Pi0.5 使用 EE displacement 的具体原因是什么？是否有实验证据表明两种度量在判断 action collapse 时等价？

4. SafeVLA 的 CMDP 方法和 VLSA 的 CBF 方法是否绕过了 EE-only 的结构性限制？如果是，论文的 "architectural failure" 论证是否反而支持了这些方法的有效性？

5. 标题中 "98%" 来自哪个具体实验配置？作者是否考虑使用更具代表性的数字或限定 scope？

---

## Missing References

以下文献被 Reviewer 标记为可能遗漏（需作者确认存在性和相关性）：
- HazardArena (arXiv 2604.12447) — VLA 安全评估 benchmark
- VLA safety survey (arXiv 2604.23775) — 领域系统综述
- VLA-Risk — safety-aware VLA training
- D2PPO — safety-aware training method
- Dong et al. 2025 — diffusion policy loss / action collapse

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。本轮未启用外部审稿线。

---

## Visual Layout Check（非评分项）

**状态**：已完成 (2026-05-28 05:02)

**Warnings (3)**:
- **Page 17**: 最后一页内容仅占约 55%，底部约 45% 空白。可将 Table 15 上移或扩展文本填充。
- **Page 5**: Figure 2 散点图数据点标注字号偏小，部分标注存在轻微重叠，打印时可能难以辨认。
- **Page 7**: Figure 4 x 轴标注为连续变量 λ，但实际刻度 (0, 0.005, 0.01, 0.1) 以等间距排列——数值间隔分别为 0.005、0.005、0.09，视觉上可能误导读者认为 λ 线性变化。建议改用分类轴或对数轴。

**Info (7)**:
- Figure 1 caption 约 15 行 + 4 bullet point，偏长但信息充分
- 全文无方法概念图/流程图——作为评估分析型论文非硬伤，但一张 CAR vs dfCAR 概念图可大幅帮助理解
- Figure 6 分组柱状图 bar 较窄、标注字号小
- Figure 2 marker 形状兼顾色盲友好性 ✓
- 表格 booktabs 风格规范 ✓
- 公式渲染正确 ✓
- 参考文献格式一致 ✓

---

## Overall Assessment

**评分：4/10 (Weak Reject)**
**置信度：High (三位 Reviewer 在所有关键问题上达成共识)**

论文识别了 VLA 安全评估中 action collapse 污染 CAR 指标这一真实且重要的问题，dfCAR 作为诊断工具有实际价值。然而，当前版本存在以下根本性障碍：

1. **统计方法论缺陷**（W1）：循环 null construction + 将 non-significance 等价于 no effect——这两个问题直接削弱 Claim 3 的可信度，而论文自身数据（Appendix J）实际暗示 SDF 可能有小但一致的正效应。

2. **实验-声明 gap**（W2-W4）：1 个 benchmark、2 个模型族、4 个任务、纯仿真——这样的实验规模可以支撑一篇 case study，但论文标题和叙事做出了关于"VLA safety evaluation"的通用断言。Pi0.5 的 dfCAR=28.5% 直接反驳了"98% is illusion"的标题。

3. **缺乏建设性贡献**（W14）：对 CoRL 来说，纯诊断论文的贡献门槛较高。缺少 proof-of-concept 替代方案（哪怕是初步的 full-body SDF 实验）使论文停留在"发现问题"而未推进解决。

**修订建议的优先级**：
- **P0**: 修正统计方法论——独立 null construction、报告 power analysis 和 effect size、弱化 "zero benefit" 为 "no statistically significant benefit at tested scale"
- **P0**: 限定标题和 claims 的 scope，使之与实验范围匹配
- **P1**: 增加至少一个额外 benchmark 或模型架构的实验
- **P1**: 补充 Limitations（sim-to-real gap）和 Broader Impact 讨论
- **P2**: 统一术语、补充 missing references、Figure 4 x 轴修正

---

## Detailed Comments

### Section 3 (Method / dfCAR)
- Eq. 1 的 d_max(e) = Σ||a_t|| 定义清晰，但 Pi0 vs Pi0.5 的位移度量不一致（obstacle vs EE displacement）需在正文中论证等价性而非脚注处理 [W6]
- Bimodal distribution (Figure 5) 和 τ_d robustness (Table 6) 是论文最强的方法论贡献——但未与 action variance 等替代 filter 对比 [W12]

### Section 4 (Claim 1 / Fake Safety)
- Table 2 的定量发现震撼但解读需注意：Pi0+A1 的 99.6% fake safe 来自完全 broken 的配置（LoRA 未加载），不应作为 headline 数字
- Pi0.5 dfCAR = raw CAR = 28.5% 说明 dfCAR 对功能性策略无过滤效果——应在正文中讨论这一正面验证

### Section 5 (Claim 2 / Oracle SDF)
- 核心发现（EE-only SDF gradient 推动 EE 但可能导致 intermediate links 进入障碍物）有清晰的物理直觉
- 但主要实验基于 TSR≈0% 的 Pi0+A1，生态效度存疑 [W5]
- Table 3 中 LoRA-based oracle (TSR 70-80%) 的结果更有说服力——建议突出这部分而非 Pi0+A1 结果

### Section 6 (Claim 3 / SDF Training Redundancy)
- **核心统计问题**：null construction 和 absence-of-evidence 错误 [W1]
- Appendix J 的数据（λ=0.1 跨 3 seeds 一致 +1.5~5.5 pp, σ_SDF < σ_LoRA）在主文中完全未讨论，这是对读者的信息隐瞒
- "Across the full tested range" 反复出现但仅 3 个 λ 值，overselling [W13]

### Section 7 (Discussion)
- "The failure is architectural" 是因果断言，超越了实验证据——实验仅证明 EE-only auxiliary loss 无效，非所有 SDF-based 方法
- Future work 三个方向各一句话，缺少具体性 [W14]
- Limitations 段轻描淡写实验范围限制 [W8]
- Broader Impact 一句话 [W9]

### Related Work (Section 2)
- 未区分 EE-only SDF (本文) vs constraint-based planning (SafeVLA) vs CBF-based filtering (VLSA) 的本质差异 [W4]
- 可能遗漏 2025-2026 最新文献 [W11]

### 格式和写作
- 术语不统一 [W10]
- Figure 4 x 轴刻度误导 [视觉审查]
- Figure 2 标注字号偏小 [视觉审查]
- 建议增加一张方法概念图展示 CAR vs dfCAR 计算差异 [视觉审查]
