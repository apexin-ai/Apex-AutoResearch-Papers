---
round: 24
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:47:10.252431+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 24 审稿报告

**Venue**: EMNLP 2026 (via ARR)
**论文**: Multi-Turn Jailbreak Detection via Disentangled Domain-Adaptive Pre-Training
**Reviewers**: R1, R2 | **交叉验证**: 完成 (14 AGREE, 3 minor REBUT)
**收敛状态**: Round 1 即达成共识，无需额外轮次

---

## Summary

本文提出两阶段框架用于多轮越狱攻击检测：Stage-1 对 RoBERTa 编码器进行领域自适应预训练（DAPT），Stage-2 用 BiGRU 做时序分类。通过 7 个预训练变体（9-class、Binary、Scrambled、MLM、Topic、Vanilla、Random Init）的因子分解消融，论文得出分类目标优于 MLM/vanilla 的"证据层级"。实验涵盖合成 OOD（Deceptive Delight、ActorAttack）和人类数据（ToxicChat）评估，184M 参数实现 24.3× 加速（vs LLM-as-judge）。

---

## Strengths

**S1 [R1+R2 共识]**: 因子分解实验设计严谨——7 个变体共享训练数据和 Stage-2 分类器，仅改变 Stage-1 目标（Table 1），在 NLP 安全领域属于罕见的受控消融。

**S2 [R1+R2 共识]**: Scrambled labels 发现具有原创性——打乱标签后在模板攻击（Crescendo、Deceptive Delight）上检测性能不降（TOST 等价），揭示分类目标的结构性角色而非语义内容驱动泛化。

**S3 [R1+R2 共识]**: 附录深度远超同类工作（17 页），涵盖 length stratification、representation geometry、SVD necessity、cross-LLM validation、dataset scale 等系统性消融。

**S4 [R1+R2 共识]**: 实用性佳——184M 参数、24.3× 加速、<5 分钟 Stage-2 训练、50 条对话近饱和。

**S5 [R1+R2 共识]**: 写作结构清晰，Section 3 方法描述和 Section 4 实验组织有逻辑性。

---

## Weaknesses (Must-Fix)

**N1 [R1+R2 共识, Critical]**: **"Evidence hierarchy" 在多个现实条件下反转，术语本身具有误导性。**

论文将 "evidence hierarchy"（Figure 2, Section 4.3）作为核心贡献，但该排序在至少四个场景下不稳定或反转：
1. **人类数据**: ToxicChat 上 MLM (0.837) >> 9-class (0.596)，差距 24pp（Table 5）
2. **策略多样攻击**: Scrambled 在 ActorAttack 上 TOST 失败（p=0.183, d=0.44, Table 16）
3. **大规模训练**: 1000 样本时 9-class OOD 性能反降（Table 14）
4. **WildChat 部署**: 9-class FPR = 68.1%，高于 vanilla (48.1%) 和 MLM (44.5%)（Table 20）

补充：即使在合成 OOD 的"稳定"条件下，hierarchy 顶部变体差异（1-4pp, Table 3）也远小于 3-seed 抽样误差，精细排序可能不稳健。

一个在多个现实场景下反转的排序不应被称为 "hierarchy"——它是一组条件依赖的观察。论文应重新命名（如 "condition-dependent performance landscape"）并在主文系统讨论各反转条件。当前 Section 4.6 仅用一句话带过 ToxicChat 反转，处理深度与问题严重性严重不匹配。

**N2 [R1+R2 共识, Critical]**: **"Unexpected findings" 新颖性定位过高。**

Classification DAPT > vanilla/MLM 是 Gururangan et al. (2020) DAPT 框架在新领域的可预期推论。论文标记为 "unexpected" 有拔高嫌疑。

R1 补充三层新颖性分析：
- 第一层（预期）: DAPT > vanilla → 低新颖性
- 第二层（非预期）: Scrambled ≈ correct labels on template attacks → 中等新颖性
- 第三层（最有价值但未充分开发）: Evidence hierarchy 在人类数据上反转 → 高信息量 negative finding

共识：论文的问题不在于完全缺乏新颖性，而在于**最具新颖性的发现（boundary conditions + negative findings）未被置于叙事中心**，反而被淹没在相对平凡的 "DAPT works" 结论中。建议重组叙事以 "why DAPT works, when it fails" 为主轴。

**N3 [R1+R2 共识, Critical]**: **Abstract/Conclusion overclaiming。**

Abstract 声称 "classification-based domain adaptation is the only consistently effective mechanism on synthetic multi-turn attacks"。"synthetic" 限定词位置容易被忽略，与标题 "Multi-Turn Jailbreak Detection"（无 synthetic 限定）存在张力。Section 5 "Deployment implications" 推荐 few-shot benign calibration 作为部署方案，但**未提及** ToxicChat 反转和 WildChat FPR 68.1% 对部署的约束。Claim 粒度与实验证据的复杂性不匹配。

---

## Weaknesses (Should-Fix)

**W1 [R2 提出, R1 强烈 AGREE]**: **BiGRU ≈ mean pooling 暗示 bag-of-turns 检测，挑战 "Multi-Turn" 核心叙事。**

Table 30 确认 mean pooling 在 ID/OOD 上与 BiGRU 完全等价（F1 gap < 1pp），turn-order shuffling 也无影响。推论：模型本质上做 per-turn [CLS] embedding 独立判别后取平均——bag-of-turns 检测。这直接挑战论文标题中 "Multi-Turn" 的叙事：模型未建模多轮动态（策略升级），而是 per-turn 独立检测并聚合。

论文在 Section 4.3 将此表述为正面发现但未讨论对方法定位的影响。R1 提出可能解释：多轮框架是工程需求（处理对话中嵌入的攻击）而非模型能力需求——但论文未做此区分。Discussion 应新增段落明确承认。

**W2 [R2 提出, R1 AGREE]**: **Section 4.6 "Human Data Validation" 标题误导。**

实验结果实际是 negative validation——论文推荐的方法在人类数据上表现最差。"Validation" 暗示确认性结果。且 ToxicChat 是单轮数据而论文标题聚焦 Multi-Turn。建议改为 "Transfer to Human-Authored Data"。

**W3 [R2 提出, R1 AGREE]**: **Related Work 对 multi-turn defense 方法覆盖不足。**

Section 2 引用 DeepContext、BIID、G-Guard 等方法但仅 1-2 句概括，未系统比较设计维度（编码器选择、时序建模、训练数据类型、评估范围）。建议增加结构化对比表。

**W4 [R1 提出, R2 AGREE]**: **350→1000 样本性能反常下降未解释。**

Table 14 显示 9-class OOD 在 1000 样本时性能反降（DD OOD 0.889 vs ~1.0 at 350）。论文未给出 training loss 曲线、data composition 分析或 seed 一致性验证。

**W5 [R2 提出, R1 部分 REBUT→Minor]**: **自创术语量。**

R2 列为 Should-Fix，R1 认为在消融研究中术语量可接受（Minor 级别），但同意 "partition sufficiency" 过于晦涩。Director 裁定：R23 已在 experiments.tex L6 添加 Terminology 定义段，维持 resolved 状态。但 "evidence hierarchy" 本身需因 N1 而重命名。

---

## Questions for Authors

**Q1**: ToxicChat 反转下的部署推荐——论文如何建议用户在面向真实用户对话（非合成攻击）时选择预训练策略？当前 Section 5 未区分合成 vs 人类数据场景。

**Q2**: 355M DAPT counterproductive 是否支持 "DAPT 补偿小模型容量不足" 的假设？如果是，这如何影响对 DAPT 机制的理论理解？

**Q3**: Scrambled 在模板攻击有效但策略多样攻击（ActorAttack）失效——作者是否有机制性解释？模板攻击的固定结构模式（stable self-transition patterns）是否是关键区分因素？

**Q4**: BiGRU ≈ mean pooling 是否意味着当前方法对 "slow-burn" 攻击（信号分散在多轮且单轮无法检测）本质上无效？

**Q5**: 50 条对话 near-saturation（Table 34）是否反映任务简单性或评估集规模不足（118 条测试）？

---

## Missing References

- **Arora et al. (2019)**: Representation compression 理论工作，可加强 "discriminative compression" 讨论的理论支撑
- **Proactive/early multi-turn detection 近期工作**: 加强 prefix-level detection 分析（Section 4.2, Table 7）的文献定位
- **Galinkin & Sablotny (2024)**: arXiv 2412.01547（R22 建议，状态待确认）
- **Perez and Wang (2022)**: Red teaming 工作（R23 建议，需确认是否已引用）

---

## External Review

**状态**: 未请求。

---

## Visual Layout Check（非评分项）

**状态**: 完成（0 critical, 3 warning, 19 info）

**Warnings**:
1. Page 8: Figure 5 坐标轴标签和图内注释文字字号偏小，灰度打印时线条可能难以区分。建议增大标注字号至正文 70% 以上。
2. Page 8: Figure 6（SVD 可视化）尺寸较小（约 1/4 column），散点和颜色标签打印时可能不够清晰。
3. Page 16: 单页含 3 figure + 1 table，视觉密度极高。Figure 8 CKA heatmap 并排排列，轴标签（层编号）非常小，打印时几乎不可读。

**正面发现**: 主正文 8 页符合 EMNLP 2026 限制；Limitations 节简洁（3 点）且位置正确；11 个 display items / 8 页分布均匀；所有表格最优结果加粗；float 位置合理；无 LaTeX 残留或 margin 溢出。

---

## Overall Assessment

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Overall | 3.0 | 3.0 | **3.0 (Findings)** |
| Soundness | 3/5 | 3.5/5 | 3.0-3.5 |
| Excitement | 3/5 | 2.5/5 | 2.5-3.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**:

论文在因子分解方法论和系统性消融方面有可识别的贡献，实验执行扎实（17 页附录、多 seed、统计检验）。但三个结构性问题限制了影响力：

1. **核心结论的条件依赖性**："evidence hierarchy" 仅在合成数据生态系统内成立，所有真实数据评估（ToxicChat、WildChat）均不支持——这不是 framing 问题，而是结论的有效范围根本性受限。

2. **新颖性定位偏差**: Classification DAPT > vanilla 可从先验工作预期；真正有价值的 boundary conditions 和 negative findings 未被置于叙事中心。

3. **"Multi-Turn" 叙事张力**: BiGRU ≈ mean pooling + turn-order 无关 = bag-of-turns 检测。标题承诺的多轮动态建模实际上未发生。

**结论**: 有方法论贡献和有价值的实证发现，但 claim 谨慎度、讨论深度和实际影响力限制了会议级别推荐。适合 **Findings** 接收（Overall 3.0），前提是修复 Must-Fix 中的 overclaiming 和讨论深度问题。

---

## Detailed Comments (Action Items 优先级排序)

### Must-Fix (阻碍 Findings 接收)

| # | Issue | Action |
|---|-------|--------|
| MF1 | Evidence hierarchy 条件依赖性 | 重命名术语；Section 4.6/Discussion 扩展反转分析为 1-2 段；Conclusion 条件性结论 |
| MF2 | Novelty 定位过高 | Section 1 "unexpected" → "systematic quantification"；重组叙事以 boundary conditions 为中心 |
| MF3 | Abstract/Conclusion overclaiming | 所有 claims 系统性加入条件限定；Deployment implications 加入 ToxicChat/WildChat 约束 |

### Should-Fix (提升论文质量)

| # | Issue | Action |
|---|-------|--------|
| SF1 | Bag-of-turns 张力 | Discussion 新增段落区分 engineering vs modeling requirement |
| SF2 | Section 4.6 标题误导 | 改为 "Transfer to Human-Authored Data" |
| SF3 | Related Work 覆盖不足 | 增加结构化对比表（Appendix 亦可） |
| SF4 | 350→1000 性能反降 | 报告 training loss / data composition 证据 |
| SF5 | WildChat FPR 讨论不充分 | Section 5 deployment 推荐中加入 distributional shift 约束 |

### Minor

| # | Issue | Action |
|---|-------|--------|
| M1 | Table 2 ±std 格式不统一 | 统一格式 |
| M2 | Figure 2/3 F1 类型未标注 | Caption 中明确 |
| M3 | McNemar "confirms equivalence" | 改为 "finds no significant difference" |
| M4 | Abstract "24.3× speedup" 无基准 | 标注 "vs LLM-as-judge" |
| M5 | Figure 5/6/8 标注字号偏小 | 增大至正文 70%+ |