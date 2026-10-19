---
round: 14
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-19T05:00:19.604865+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 15 (Fresh Review)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 via ARR May 2026 (截止 2026-05-25)
**Reviewer 编排**: R1 (方法严谨性) + R2 (新颖性/完整性)
**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛 (1 轮完成)

---

## Summary

本文研究推理模型中隐藏状态(HS)安全探针的层选择敏感性。核心方法论发现是：包含 crossing rate 的复合指标系统性选择 32B 模型的浅层，导致 HS 优势结论被逆转——这是对 probing 文献有普适警示意义的发现。修正后（threshold-dependent 指标选深层），论文报告四个模型均通过 Holm-Bonferroni 校正。但经验性 HS 优势是 conditional 的：受编码器质量制约（1024d BGE 下仅 1/4 HB），32B 模型统计效力不足（n=19-20），QwQ-32B 位置基线在 BA 上胜过 HS 探针。论文属于 characterization study，未提出新方法/算法/工具。

---

## Strengths

**S1. [共识] 层选择敏感性是重要的方法论发现。** Table 2 清晰展示有偏指标与纠正后指标选层差异（QwQ-32B: 3% vs 98% depth）。机制解释有数据支撑（浅层表示压缩 1.4-2.7x，Appendix C）。对整个 probing 文献有警示价值——不限于特定复合指标，pure BA 在 32B 上也产生 24 层 LOO-CV 跨度。(R1-S1, R2-S1)

**S2. [共识] 异常诚实的局限性披露和 evidence gradient。** Strong/moderate/qualified 三级证据分类贯穿全文，dagger notation 标记低样本量结论。R1-32B position-mediated (+1.9pp, p=0.914)、R1-8B FPR seed-fragile (3/5 HB)、QwQ-32B 位置基线竞争性——全部主动报告。Bug disclosure (Appendix N) 展现科学诚信。(R1-S2/S3, R2-S3/S4)

**S3. [共识] 实验矩阵覆盖面广。** 5 种选择指标、7 种 baseline 方法、3 种文本编码器（384d/1024d/4096d）、PCA 和 random projection 容量控制、position residualization、control task selectivity、multi-seed stability。26 个附录子节系统覆盖每个正文 claim。(R1-S4, R2-S2/S5)

**S4. [共识] 写作质量好。** 无 AI 写作痕迹（无 em-dash/en-dash/-ing 短语结尾/黑名单词/过渡词堆砌）。Related Work 组织清晰（4 主题），63 条引用覆盖完整无伪造。(R2 AI 风格检查全通过)

**S5. [共识] 容量控制设计合理。** PCA-384d（79-92% 方差保留）+ random projection（结构破坏性）+ MiniLM/E5-Mistral/BGE-large encoder gradient (4/4 → 2/4 → 1/4 HB)，形成单调递减梯度。(R1-S5)

---

## Weaknesses

### Must-Fix (影响接收决定)

**W1. [Critical, 共识] 正文页数超限 (~8.3 页)。**
- Section 5 (Discussion) "Deployment operating points" 段溢出至第 9 页，Section 6 (Conclusion) 完全在第 9 页
- ACL Long Paper 正文限制 8 页（不含 Limitations/Ethics/References）
- **Desk reject 风险**
- 修复方向：(1) 将 "Deployment operating points" 段移至附录（与 Appendix L K-ablation 重叠较多）；(2) 压缩 Discussion/Conclusion 重叠
- (R2-W1 Critical, R1 交叉 AGREE)

**W2. [Critical, 共识] 32B 超参数搜索空间与验证集规模严重不匹配。**
- 32B 验证集每类仅 4-10 条，搜索空间最多 2,240 配置 (Layer 64 × W 7 × K 5)
- 论文 Appendix M 三个反驳论点均有漏洞：
  - "指标独立收敛到 L63"：共享混淆矩阵 (effective DoF=2)，收敛可能反映共同偏差
  - "Bootstrap CI 量化不确定性"：不弥补验证集过小
  - "BA 层不稳定性是发现本身"：LOO-CV 跨 fold 变化 24 层，说明任何单一指标都不可靠
- **影响**：论文核心声明 "纠正后层选择下所有 4 个模型显著" 可能部分由超参数过拟合驱动
- 修复方向：(1) 嵌套交叉验证 (inner fold 选层+W+K, outer fold 评估)；(2) 或将 32B 声明降级为 "suggestive/directionally consistent but underpowered"
- (R1-W1 Critical, R2 交叉 AGREE + 补充定量论证)

**W3. [Critical, 共识] QwQ-32B 位置基线影响被系统性低估。**
- Position baseline BA (0.832) > HS BA (0.796)，margin = -3.6pp (Table 4)
- HS precision over position: +4.5pp (p=0.133), FPR: +2.5pp (p=0.279)——均不显著
- 论文将 QwQ-32B 分类为 "moderate" 但当位置基线在核心指标上胜出时，"moderate" 过于乐观
- **影响**：扣除 QwQ-32B (position dominates) 和 R1-32B (position-mediated, p=0.914)，实际仅 2/4 模型有无条件 HS 优势。"All four models show significant HS advantage" 的 claim 实质上是 "2/4 unconditional, 2/4 position-dominated or position-mediated"
- 修复方向：Abstract/Introduction 区分 7-8B (robust) 和 32B (conditional with model-specific caveats)
- (R1-W2 Critical, R2 交叉 AGREE + 与 R2-W4 叠加论证)

**W4. [Critical, 共识] Novelty scope 不足 Main track。**
- 三条 contributions 均为 empirical observations：层选择敏感性 (发现偏差)、encoder-quality boundary (更强编码器缩小差距)、negative results (7 种方法不行)
- 无新检测方法、probe 架构、或可复用开源工具
- Five-step audit (Section 5) 是非形式化建议，缺乏理论保证和前瞻性验证
- R1 caveat：方法论警示论文有 Main 先例 (Hewitt & Liang 2019)，但该文提出了可操作化的形式框架 (control task + selectivity metric)；本文的 audit 更像 checklist
- 修复方向：(a) 将 five-step audit 形式化为可自动执行的统计检验（如基于 LOO-CV 层稳定性的自动指标选择标准）；(b) 或接受 Findings 定位
- (R2-W2 Critical, R1 交叉 AGREE with caveat)

### Should-Fix (影响评分)

**W5. [Major, 共识] HS advantage 被 encoder quality 系统性制约。**
- 384d MiniLM: 4/4 HB → 1024d BGE-large: 1/4 HB → 4096d E5-Mistral: 2/4 HB
- 论文自己承认 "HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference"
- R1 统计补充：PCA-384d 容量匹配低估文本编码器能力——PCA 保留最大方差方向 ≠ text encoder 语义方向。Random projection 同理：证明不依赖 PCA 结构保持性质，但不排除维度匹配对 text encoder 不公平
- **影响**：经验贡献 shelf life 短，论文持久价值集中在方法论发现而非经验发现
- (R2-W3 Major, R1 交叉 AGREE)

**W6. [Major, 共识] 单一数据集限制泛化性。**
- 所有实验仅基于 HarmThoughts (632 traces, 4 模型)
- CP annotations 未经独立 IAA 评估；CP 标注方法（人工/算法）在正文中未描述
- 如果标注者倾向在特定 trace 位置标注 CP，位置信号会被人工放大
- Appendix J (CP 扰动) 测标注鲁棒性但不测数据集泛化
- (R1-W5 Major, R2-W5 Major, 交叉完全共识)

**W7. [Major, R1 提出] Bootstrap 方法类型未指定。**
- Section 3.5 仅说 "10,000 bootstrap resamples"，未指定 percentile/BCa/basic
- 小样本 (n=19-20) 下 percentile bootstrap 已知有偏且覆盖不足
- Appendix D exact sign-flip permutation test 部分缓解——但 CI 宽度仍重要
- (R1-W3 Major, R2 交叉 AGREE)

**W8. [Major, R1 提出, R2 确认为写作清晰性] HB 校正在 12-test 和 4-test 框架间反复切换。**
- Section 3.5: "3 metrics × 4 models = 12 tests" vs Section 3.3: "effective DoF = four"
- 两种框架下结论一致（R1-8B FPR p=0.044 在两种下均 pass），但写作不一致引起混淆
- (R1-W4 Major, R2 交叉 AGREE——写作清晰性问题)

### Minor

**W9. [Minor, 共识] Discussion 与 Conclusion 重叠度过高。** "Layer selection is critical DOF" 在 Introduction/Discussion/Conclusion 三处高度相似表述。(R2-W7 Minor, R1 AGREE)

**W10. [Minor, 共识] Abstract 信息密度过高。** 含过多术语 (HB/crossing rate/PCA/evidence gradient 等)，审稿人 30 秒内难判断核心价值。(R2-W8 Minor, R1 AGREE with caveat)

**W11. [Minor, R1 提出] GRU 双 split (70/30 vs 60/20/20) 附录混淆。** 正文 Section 4.5 引用正确的 60/20/20 结果 (Table 12)，但附录同时存在两种 protocol。影响有限——GRU 非核心贡献。(R1-W6 Major→降为 Minor, R2 PARTIAL AGREE)

**W12. [Minor, R1 提出] 控制任务 selectivity (11.1-16.8pp) 与 position contribution (9-20pp) 范围重叠未充分讨论。** 两者测量不同东西，但 safety-specific non-positional signal 可能很小。(R1-W7 Minor, R2 PARTIAL AGREE)

---

## Reviewer Consensus [AGREE]

以下关键问题两位 Reviewer 达成完全共识：

1. **Overall 3.0 (Findings)**：方法论发现有价值但不足以支撑 Main；经验贡献 conditional 且可能 temporary
2. **正文超页 (W1)**：~8.3 页，desk reject 风险，必须修复
3. **32B 统计效力不足 (W2)**：2,240 配置 vs 4-10 条验证样本，过拟合未充分排除
4. **QwQ-32B position dominates (W3)**：位置基线 BA 胜出，"moderate" 过于乐观
5. **Novelty scope = Findings (W4)**：纯 characterization study 无新方法产出
6. **Encoder-conditional HS advantage (W5)**：384d→1024d 从 4/4 降到 1/4 HB
7. **单数据集 (W6)**：HarmThoughts only, CP IAA 未报告
8. **写作质量好**：无 AI 痕迹，evidence gradient 诚实，引用完整

---

## Reviewer Divergence [REBUT]

**唯一实质分歧：Layer selection sensitivity 的适用范围 (R2-W6)**

- **R2 立场**：多少研究者会用 BA × crossing rate？如果几乎没有，impact 有限
- **R1 反驳 [REBUT]**：问题不限于特定复合指标——pure BA 在 32B 上也产生 24 层 LOO-CV 跨度 (Table 25)；多数 probing 论文不报告层选择标准；Liu et al. (2019) 和 Tenney et al. (2019) 系统报告各层性能但许多后续工作只报告最终结果
- **Director 裁定**：R1 反驳有效。层选择敏感性的适用范围超出特定复合指标，但论文确实应更明确论证广泛适用性——目前叙事过于聚焦 crossing rate bias 这一机制。建议在 Discussion 中补充 2-3 句论证更广泛适用性（引用 BA 不稳定性数据）。**降为 info 级别 suggestion，不影响评分。**

---

## Questions (需作者回应)

**Q1. [两位共识]** Bootstrap CI 使用 percentile/BCa/basic？对 32B 模型三种方法差异可达数个百分点。

**Q2. [R1]** K=5 到底是在什么时间点、基于什么信息 pre-selected 的？Section 3.5 的 "pre-selection" 与 "post-hoc rationale" 矛盾。

**Q3. [R1]** R1-32B threshold-dependent 指标在 LOO-CV 下的稳定性如何？论文仅报告 BA 的不稳定性。

**Q4. [R2]** OT-7B biased layer L0 (embedding layer) 为何未在正文突出讨论？这是论文最有力的例证。

**Q5. [两位共识]** HarmThoughts CP annotations 是人工标注还是算法生成？IAA 信息缺失。

**Q6. [R2]** Table 3 中 1024d 行 BA/FPR 为 "--"（未计算），为何不全算？减少可比性。

**Q7. [R1]** Five-step audit 是否在任何外部数据集上前瞻性验证？如果没有，"recommend" 是否过强？

---

## Missing References

两位 Reviewer 均确认引用覆盖完整（63 条 bib entries），无严重遗漏。以下为可选补充：

1. **DiCiccio & Efron (1996)** — Bootstrap CI 方法论，与论文统计方法直接相关 (R1 建议)
2. **Pimentel et al. (2020)** — MDL probing，control task selectivity 的信息论替代方案 (R1 建议)
3. **Tenney et al. (2019)** — 层选择问题的早期重要工作，已引用但可进一步讨论 (R1/R2 共同建议)

---

## External Review

未配置外部审稿（paperreview.ai 未启用）。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.5 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Overall | 3.0 | 3.0 | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | 4/5 |

### EMNLP 2026 ARR 评分标准映射

**Overall Assessment: 3.0 = Findings（可被 Findings 接收）**

### 一句话总结

**层选择敏感性是有价值的方法论发现，但论文是 characterization study（无新方法产出），核心经验发现受 encoder quality 制约（1/4 HB with BGE-1024d）、32B 结论统计效力不足（n=19-20, 2240 配置过拟合风险）、QwQ-32B 位置基线 BA 胜出，且正文超出 8 页限制。适合 Findings 而非 Main track。**

### 详细理由

**方法论发现 (Contribution 1) 是 sound 且有价值的：**
- 层选择作为 researcher DOF 可以逆转 probing 研究结论——这一发现对任何使用 best-layer probing 的研究有警示意义
- 机制解释（浅层表示压缩 → crossing rate 膨胀）有数据支撑
- 但发现本质上是"特定指标有偏差"而非"提出新方法"

**经验发现 (Contributions 2-3) 是 conditional 且可能 temporary 的：**
- HS advantage: 384d 下 4/4 HB，1024d 下 1/4 HB——随编码器改进会继续缩小
- 32B 结论：n=19-20 验证集 + 2,240 搜索空间，统计基础薄弱
- QwQ-32B: 位置基线 BA 胜出，HS 优势可能完全被位置解释
- 实际无条件 HS 优势：仅 OT-7B (strong) 和 R1-8B (moderate, FPR fragile) = 2/4 模型
- Negative results 有价值但 BOCPD/CUSUM 在 gradual transition 上失败是 expected 的

**格式问题：**
- 正文 ~8.3 页超限，必须在提交前修复

**论文的透明度和附录完整性值得高度肯定，但透明地报告弱点不能替代解决弱点。**

---

## Detailed Comments

### Abstract
- 信息密度过高：biased composite metric 机制细节、HB、crossing rate、PCA、evidence gradient、FPR 全部挤在单段中
- 建议：聚焦层选择敏感性核心信息，删除 encoder gradient 和 negative results 的具体数字

### Introduction (Section 1)
- 叙事结构完整 (问题→重要性→不足→发现→贡献)
- "layer selection has received almost no scrutiny in the probing literature" 略有过度声称——probing 文献有大量 layer-wise analysis。更准确："layer selection *metrics* have received almost no scrutiny"
- Contribution 2 过长（4 行），信息过密。建议拆分或简化
- "所有 4 个模型 HB 显著" 的措辞应弱化——区分 7-8B (robust) 和 32B (conditional)

### Related Work (Section 2)
- 4 主题组织清晰，63 条引用覆盖完整
- Positioning 准确："None of these conducts a systematic modality comparison for commitment detection"
- 引用验证：无伪造引用 (R2 在线验证 52/63 通过，9 条为 2025-2026 arXiv 预印本，2 条标题 mismatch 经手动验证为真)

### Method (Section 3)
- CP 定义清楚，但 "permanently ceases" 的 operationalization 需更多说明
- Table 1 数据量差异大 (OT-7B 228 vs QwQ-32B 95) 未解释
- Section 3.3 层敏感性分析详尽但段落过长 (~20 行)
- K=5 "pre-selection" 与 "post-hoc rationale" 表述矛盾 (Q2)
- HB 框架 12-test vs 4-test 切换需统一

### Experiments (Section 4)
- Evidence gradient 分类好，但 QwQ-32B "moderate" 在位置基线 BA 胜出时不合适
- Table 3 格式清晰，但 1024d 行 "--" 减少可比性
- Section 4.6 Negative Results 重要但过于压缩——BOCPD 0% detection on 3/4 models 值得更多讨论
- R1-32B coverage 仅 25% (5/20 traces)——如此低覆盖率下的 "显著性" 实际意义有限

### Discussion (Section 5)
- 4 段结构清晰
- "Deployment operating points" 段的 K=10 讨论（21% coverage, 8% FPR）是实用的，但 ~80% 攻击被遗漏在高风险场景下不一定可接受——应更诚实讨论 tradeoff
- Five-step audit 有价值但缺乏形式化
- **此段溢出第 8 页——首选压缩目标**

### Conclusion (Section 6)
- 与 Discussion 重叠度过高
- 建议压缩至 3-4 句

### Limitations (Section 7)
- 非常全面：statistical power、hyperparameter selection、CP annotation、scope、correlational
- 单数据集局限应排在更前位置
- MDE 分析 (Appendix V) 应在正文而非附录引用

### 格式
- ✅ `\usepackage[review]{acl}` 正确
- ✅ 匿名 "Anonymous ARR Submission"
- ✅ 行号启用
- ✅ booktabs 表格
- ✅ Responsible NLP Checklist (Appendix A)
- ✅ 引用格式完整
- ❌ **正文超 8 页限制 (W1)**
- ⚠️ Fig 1 heatmap 4 subplot 挤在 single column，打印后 legend 字号可能 <7pt