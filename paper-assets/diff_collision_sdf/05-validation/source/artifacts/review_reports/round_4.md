---
round: 4
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-28T11:49:10.894579+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# Round 4 审稿报告（Fresh Review）

**论文**: How Action Collapse Creates Illusory Safety in VLA Collision Avoidance Evaluation
**Venue**: CoRL 2026
**审稿模式**: Fresh（两位 Reviewer 无历史轮次记忆）
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计分析; R2: 新颖性/贡献度 + 相关工作 + Framing + CoRL 受众适配）。Reviewer 3 本轮未分配任务（2 人编排足以覆盖所需审查维度）。

---

## Summary

论文揭示 VLA 碰撞回避评估中 action collapse 导致 CAR 指标虚增的问题，提出 displacement-filtered CAR (dfCAR)。在 SafeLIBERO benchmark 上，Pi0.5 的 95.1% CAR 几乎全部来自 action collapse（>99% collision-free episodes 为 action-collapsed）而非真正的回避行为。同时测试 SDF 辅助监督作为 EE-only 碰撞回避策略，得出负面结论。

---

## Strengths

**S1. 重要的诊断洞察**: action collapse 虚增 CAR 是真实且被忽视的评估陷阱，论文首次系统量化（Table 2 显示 Pi0.5 的 5732 个 "safe" episodes 中 >99% 为 action-collapsed），对未来 VLA safety 评估有直接指导价值。

**S2. 严谨的实验方法论**: 包含 displacement threshold sensitivity analysis (Appendix B)、null distribution 构建 (Appendix G)、per-task 分解 (Appendix C-D)、evaluation seed robustness (Appendix K)、MDE 分析。统计检验意识在 robotics 论文中较为少见且值得肯定。

**S3. 诚实的负面结果**: SDF supervision 的负面发现 (Section 5, Table 3, Figure 3) 对社区有警示价值。论文系统分析了 EE-only SDF gradient 将碰撞重新分配到 arm links 的机制。

**S4. 有效的可视化**: Figure 2 (TSR vs. CAR/dfCAR 散点图) 清晰展示 action collapse 的影响——右上象限的 collapse cluster 和左下象限的真实性能一目了然。

**S5. Oracle 对照设计巧妙**: 用 ground-truth SDF 建立 EE-only refinement 性能上界，包含 full-body 变体，实验设计思路值得肯定（尽管 collapsed policy 限制了解释力）。

**S6. 充分的消融与附录**: sensitivity analysis、per-task breakdown、seed robustness 等附录材料体现了良好的实验科学素养。

---

## Weaknesses

### Must-Fix（两位 Reviewer 共识）

**W1 [Critical] n=3 seeds 统计力严重不足**
- R1-MF2 提出, R2 [AGREE]，两位 Reviewer 均认为这是论文最致命的方法论缺陷
- MDE≈5pp，对 2-4pp 效应量几乎无检测力
- absence of evidence ≠ evidence of absence：从 "未检测到显著差异" 到 Section 5 标题 "Cannot Ensure Full-Body Safety" 存在巨大推理跳跃
- Figure 4 (p.8) 的 error bars 横跨整个效应范围，进一步证实低统计力
- "Collision-free demonstrations suffice" 的 claim 同样未报告 p-value 或 confidence interval
- **要求**: 明确将 SDF 结论降级为 suggestive negative evidence，或增加 seeds 至 n≥5 使 MDE 降至 2pp 以下

**W2 [Critical] 实验范围过窄 vs. 声明过强**
- R1-MF4 + R2-W2，两位 Reviewer 从不同角度独立得出相同结论
- 仅覆盖: 1 benchmark (SafeLIBERO), 2 VLA 家族 (Pi0/Pi0.5, 均 flow-matching), 1 collision scope (EE-only), 1 fine-tuning 方式 (LoRA)
- 关键缺口: 缺少 non-diffusion VLA (RT-2, Octo 等 autoregressive policy) 验证，无法判断 action collapse 是 diffusion/flow 架构特有还是 VLA 通病
- Pi0 和 Pi0.5 都是 flow-matching 架构，不构成架构多样性
- "Collision-free demonstrations suffice" 仅在 Pi0.5 + LoRA 上验证，未在 Pi0 或 full fine-tuning 下测试
- 标题 "VLA Collision Avoidance Evaluation" 暗示通用性，与实验覆盖严重不匹配
- **要求**: 缩小声明范围（标题限定 "Diffusion-Based VLA"），或增加至少一个 non-diffusion VLA baseline

**W3 [Critical] 贡献点冗余，主要贡献偏轻**
- R2-W1 提出, R1 [AGREE]
- C1 (dfCAR metric) 和 C3 (action-collapse diagnosis) 本质上是同一发现的工具面和现象面
- C4 (demonstration sufficiency) 是 C1/C3 的自然推论
- 精简为两个核心贡献更诚实: (1) dfCAR + action collapse 诊断框架, (2) EE-only SDF 的 suggestive 负面证据
- R1 补充: dfCAR 的价值在于揭示的问题严重程度（>99% inflation），不在于技术复杂度。简单工具解决重要问题不是缺陷，但需更强实验支撑弥补技术新颖性不足，而论文在 scope 和统计力上恰好薄弱

**W4 [Critical] Oracle 实验在 99.4% collapsed 模型上进行**
- R1-MF3 提出, R2 [AGREE]
- 在几乎不产生有意义动作的 policy 上，任何辅助信号的效果都无法被可靠评估
- Table 3 中 baseline Collapsed=99.4%，Oracle variants 也在 96-99% 范围，non-collapsed episodes 样本量极小，noise 主导
- "structurally counterproductive" 的 claim 缺乏充分 empirical evidence
- R2 补充: 叠加 EE-only 设计的考量（虽 R1 指出论文含 full-body oracle），SDF 负面结论受质疑
- **要求**: 将 SDF 结论归因于 base policy collapse 状态而非 SDF 方法论固有限制

**W5 [Critical] Permutation test 论证瑕疵**
- R1-MF1 提出, R2 [AGREE with nuance]
- R2 澄清: permutation test 统计机制本身合法（pool 两组是标准做法）
- 真正问题: post-hoc null construction——先观察 λ=0.005 与 LoRA-only 接近，再将其 pool 入 null，有膨胀 null variance 的嫌疑
- 缓解因素: Appendix G 的 Null A 构建（仅用 LoRA-only 3 seeds）结论一致 (p=0.20 for λ=0.1)，说明 pool λ=0.005 非结论必要条件
- 但主文未充分讨论这一替代构建
- R2 判断: 本质上与 W1 (n=3 统计力不足) 是同一根本问题的两个表现

### Should-Fix

**W6 缺失关键引用: "Demystifying Diffusion Policies" (CoRL 2025 Workshop)**
- R2-W3 提出, R1 [AGREE]
- Zheng et al. (arXiv:2505.05787) 论证 diffusion policies 本质上在做 action memorization，为 action collapse 提供直接的机制性解释
- 同 venue (CoRL) 上一届的直接相关工作未引用是明显减分项
- 讨论 action collapse 与 action memorization 的关系可加强论文理论深度
- R1 补充: 该引用若成立，也凸显 W2——如果 action collapse 是 diffusion policy 固有属性，claim 应限定在 diffusion-based VLA
- ⚠️ 两位 Reviewer 均未独立验证此引用的存在和内容，建议确认后再补充

**W7 对 CoRL 受众建设性不足**
- R2-W6 提出, R1 [AGREE]
- Section 8 Future Work 仅三句话，方向过于 generic (full-body supervision / cross-architecture / planning-layer)
- 诊断性论文被接受的前提是提供足够的 actionable insight
- 论文发现 collision-free demonstrations 有效 (Table 4, Section 6)，但未发展为具体数据策略建议（需多少 demos？什么比例？有无 diminishing returns？）

**W8 dfCAR 阈值 bimodal gap 主文讨论不足**
- R2-W5 提出阈值敏感性担忧, R1 [REBUT on interpretation, AGREE on presentation]
- R1 澄清: R2 对 Table 5 的解读有误——所有合理阈值 (0.001mm-10mm) 给出一致分类，bimodal gap (>5 个数量级) 使结论对阈值选择不敏感，这是鲁棒性证据而非脆弱性证据
- 但核心指标的关键参数在主文仅一句话带过，讨论确实不足
- R1 补充: bimodal gap 可能是 SafeLIBERO 仿真特有 artifact，其他环境中位移分布可能呈连续分布，届时阈值选择将变困难

**W9 SDF 结论 framing 过强**
- R2-W4 提出 EE-only circularity, R1 [PARTIAL REBUT]
- R1 指出: 论文已测试 full-body oracle SDF (Table 3, Oracle-fixed GT full body)，CAR 仍下降 (83.0% → 76.6%)，因此 circularity 指控不完全成立
- 但共识: 核心问题回到 W4——所有 oracle 在 collapsed policy 上进行，无法区分 "SDF 无效" vs "collapsed policy 上任何 refinement 都无效"
- Section 5 标题 "EE-Only SDF Cannot Ensure Full-Body Safety" 应更准确归因

### Minor

**W10 Figure 1 信息密度** — R2-W7 提出（4 个 sub-figure 空间不足），R1 反驳（4-panel summary figure 是 CoRL 标准做法）。分歧记录，不影响评分。

**W11 "Illusory Safety" 标题措辞** — R2-W8 建议 "Illusory Progress" 或 "Inflated Metrics"，R1 反驳（"Illusory Safety" 精确指向安全判断的虚假性，替代方案过于 generic）。当前标题可接受。

**W12 修辞策略** — R2-W9 提出, R1 [AGREE but low impact]。Abstract 中 "The problem appears close to solved. It is not." 等对比修辞有轻微戏剧化倾向，部分 reviewer 可能反感，但数据支撑成立则属写作风格问题。

---

## Reviewer Consensus

以下为两位 Reviewer 独立得出且交叉确认的共识：

1. **Action collapse 诊断 + dfCAR 是论文核心有价值贡献**（R1 strengths, R2 S1/S2）
2. **n=3 seeds 是最致命的方法论缺陷**（R1-MF2, R2 AGREE，统计力不足贯穿全文多个 claim）
3. **实验范围过窄 vs. 声明过强**（R1-MF4, R2-W2，独立得出相同结论）
4. **SDF 负面结论过于绝对**（R1-MF3 + R2-W4，从不同角度质疑，但共识问题在于 collapsed policy 而非 SDF 本身）
5. **贡献点应精简为 2 个**（R2-W1, R1 AGREE）
6. **Overall 评分一致**: 5/10, marginally below acceptance threshold

## Reviewer Divergence

1. **SDF circularity (R2-W4 vs R1)**: R2 认为 EE-only 设计构成循环论证；R1 指出论文已含 full-body oracle 实验 (Table 3)，circularity 不完全成立。**共识**: 真正问题是 collapsed model 上测试无效 (W4)，而非 EE-only scope。

2. **dfCAR 阈值敏感性 (R2-W5 vs R1)**: R2 认为 Table 5 显示结论对阈值敏感；R1 反驳 bimodal gap (>5 数量级) 使结论鲁棒，R2 是数据误读。**共识**: 数据解读 R1 正确，但主文讨论确实不足 (W8)。

3. **Figure 1 (R2-W7 vs R1-W7)**: R2 认为过密，R1 认为标准做法。Minor disagreement。

4. **标题 (R2-W8 vs R1)**: R2 建议替代方案，R1 认为当前更精确。Minor disagreement。

---

## Questions（需作者澄清）

**Q1** [关键]: Action collapse 是否是 diffusion/flow-based policy 特有现象？有无 autoregressive VLA (RT-2 系列) 的 evidence？如果仅出现在 diffusion 架构，论文 scope 和 title 需调整。(R2-Q1, R1 AGREE)

**Q2**: Pi0 Full-FT 99.4% collapsed——SafeLIBERO 是否对 Pi0 太难，collapse 只是任务失败的表现而非独立的安全评估现象？需区分 task-appropriate minimal motion vs genuine action collapse (policy 输出趋近零向量)。(R2-Q2, R1 AGREE with supplement)

**Q3**: Pi0.5 baseline dfCAR n*=0 意味着每次真正运动都碰撞。"Illusory safety" framing 与 "complete inability to avoid collisions when moving" 的 implications 不同，论文应明确讨论。(R2-Q3, R1 AGREE)

**Q4**: SDF decoder 架构 (2-layer MLP, 1024→256) 的选择依据？负结果论文有义务证明不是 implementation artifact。Oracle 实验部分缓解但不完全消除此担忧。(R2-Q4, R1 AGREE)

**Q5**: Collision-free demonstrations 的实际数据量和比例？如果 >90% demos 都是 collision-free，"suffice" claim 趋向 trivial。(R2-Q5, R1 AGREE)

---

## Missing References

1. **[最关键]** "Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives" (Zheng et al., CoRL 2025 Workshop, arXiv:2505.05787) — action memorization 机制直接解释 action collapse。⚠️ 未经独立验证。
2. "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms" (arXiv:2604.23775) — VLA safety 综合 survey。⚠️ 未验证。
3. "VLATest: Testing and Evaluating Vision-Language-Action Models" (Wang et al., FSE 2025) — VLA 评估 metrics。⚠️ 未验证。
4. "UniLACT: Depth-Aware RGB Latent Action Learning" (arXiv:2602.20231) — depth-aware VLA 学习。⚠️ 未验证。

---

## External Review

未请求外部审稿（项目配置未启用 `external_review.paperreview_ai`）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成（2026-05-28 11:28→11:31，耗时 ~3 分钟）
**统计**: 0 critical / 3 warnings / 17 infos

### Warnings
1. **Figure 4 x 轴误导** (p.8): λ∈{0, 0.005, 0.01, 0.1} 使用等间距排列，但 0.01→0.1 是 10 倍跳跃。Categorical axis 伪装为 continuous，可能误导读者对趋势感知。建议 log-scale 或明确标注为 categorical conditions。
2. **Discussion 压缩过度** (p.8): Section 7 (Discussion + Conclusion) + Limitations + Future Work + Broader Impact 全部压缩在 ~1.5 页，Discussion 显得仓促。与 W7 (建设性不足) 交叉佐证。
3. **末页大面积空白** (p.18): 最后一页仅 ~1/3 内容，~2/3 空白，给人未完成感。

### Notable Infos
- 主体 8 页含 4 figures + 4 tables = 1.0 display items/页，密度优秀
- 所有表格最优值加粗，booktabs 风格，格式规范
- 颜色语义跨图一致（LoRA 蓝色、SDF 绿/橙系、Oracle 紫系），色盲友好度尚可
- 全文无 margin 溢出、公式渲染错误、overfull hbox 或 Section heading 孤悬
- 参考文献 29 条，无未解析 [?] 项

---

## Overall Assessment

**Overall Score: 5/10 — Weak Reject (marginally below acceptance threshold)**

**置信度: 4/5**（两位 Reviewer 独立评估完全一致，核心问题在交叉分享后充分确认，无重大分歧）

**一句话总结**: 论文提出了有价值的诊断洞察（action collapse 虚增 CAR），但技术贡献偏轻（dfCAR 本质是位移阈值过滤）、实验范围过窄（仅 diffusion-based VLA + 1 benchmark）无法支撑一般性声明、n=3 seeds 的统计力不足贯穿全文多个关键 claim、且缺乏对 CoRL 受众的建设性方案。

**接受门槛分析**:
- **支持接受**: 有价值的 diagnostic insight、严谨的统计方法设计意识、诚实的负面结果、优秀的可视化
- **阻碍接受**: 技术新颖性不足、scope-claim 严重不匹配、n=3 统计力不足使 SDF 及 demo sufficiency 的 claim 均不可靠、缺少非 diffusion VLA 验证、建设性方案不足
- **最小修改路径**: (a) 增加 ≥1 个 non-diffusion VLA baseline 或诚实限定 scope, (b) seeds 增至 n≥5 并报告 CI/p-value, (c) 精简贡献点为 2 个, (d) SDF 结论降级为 suggestive evidence 并归因于 base policy collapse, (e) 补充具体 mitigation strategy (如 data curation pipeline), (f) 验证并补充 "Demystifying Diffusion Policies" 引用

---

## Detailed Comments

### Section 1 (Introduction)
- 四个 contribution 应精简为两个: (1) dfCAR + action collapse 诊断框架, (2) EE-only SDF 的 suggestive 负面证据
- "The problem appears close to solved. It is not." 对比修辞风格对部分 CoRL reviewer 可能是双刃剑，建议适度 tone down

### Section 3.2 (dfCAR Definition)
- τ_d = 0.1mm 的 bimodal gap 论证应从 Appendix 提升到主文（至少 2-3 句定量描述 5 数量级间隔）
- 应讨论 bimodal gap 在非 SafeLIBERO 环境中的适用性（连续 vs bimodal 分布的可能性）
- 应与替代 filter 方案（action variance, mean velocity, joint-space distance）对比讨论

### Section 3.3 (SDF Supervision Setup)
- SDF decoder (2-layer MLP, 64³ voxel grid, 64 query points) 设计选择需要 justification
- 负结果论文有义务论证不是 implementation artifact

### Section 4 (Demonstration Sufficiency)
- 缺少 collision-free demonstrations 的具体数据量和比例统计
- ~20pp dfCAR 提升效应量大，但仍需报告 p-value/CI 支撑 "suffice" claim
- 仅在 Pi0.5 + LoRA 上验证，应讨论 cross-model/cross-method 的推广性

### Section 5 (SDF Results)
- 标题从 "Cannot Ensure" 改为 "Does Not Ensure at Tested Scale" 或类似 hedged 表述
- 明确归因: base policy 的 99.4% collapse 是主要限制因素
- Full-body oracle 结果 (Table 3) 应在主文更突出讨论——当前读者容易忽略这一关键实验
- SDF gradient 将碰撞重新分配到 arm links 的机制解释是 reasonable hypothesis，但在 collapsed policy 条件下缺乏充分 empirical support

### Section 6 (Statistical Analysis)
- MDE≈5pp 的讨论应更突出——直接限制所有 "no effect" 结论的可信度
- Null A 构建 (仅 LoRA-only seeds) 与 Null B 的比较应从 Appendix 移入主文讨论
- 确保 "p>0.05" 不被读者误读为 "evidence of no effect"

### Section 7-8 (Discussion / Future Work)
- 视觉审查也指出 Discussion 压缩过度 (~1.5 页装 4 个 subsection)
- Future Work 应包含至少一个 concrete 方向 + preliminary evidence
- 应讨论 action collapse 与 action memorization 的理论关系（如 Zheng et al. 2025 确认存在的话）
- 应明确区分 task-appropriate minimal motion 与 genuine action collapse

### Related Work
- 补充 "Demystifying Diffusion Policies" 及其与 action collapse 的理论联系（验证后）
- 补充 VLA safety survey（验证后）
- 讨论 action collapse 是否已在 diffusion policy 文献中被讨论过，如果是，本文的增量贡献需更清晰定位