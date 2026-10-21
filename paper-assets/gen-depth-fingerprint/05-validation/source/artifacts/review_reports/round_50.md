---
round: 50
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T02:02:50.794251+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 50 (Fresh Review)
## gen-depth-fingerprint → EMNLP 2026 (ARR)

**Reviewers**: R1 (方法严谨性+实验设计) + R2 (新颖性+完整性)
**交叉回应**: 完成。关键问题共识充分，2处轻微分歧已记录。
**视觉审查**: 完成（0 critical, 2 warning, 9 info）。
**外部审稿**: 未配置。

---

## Summary

论文提出 *depth profiling*——将文本按递归生成深度（gen-0/gen-1/gen-2+）进行序数分类，并通过分解 NLL 分布的 location drift 与 shape stability 发现了 *differential depth response* (DDR) 这一实证规律。实验覆盖 8 个 base-model 生成器（5 个架构家族，0.6B-8B），使用 LOGO 交叉验证，leak-free binary F1=0.694，3-class F1=0.762。附录 28 页包含大量消融和鲁棒性分析。

---

## Strengths

**S1** [consensus] **任务定义新颖且有意义**——从 binary human/machine 检测扩展到 ordinal depth classification，对数据溯源和语料审计具有直接价值。两位 Reviewer 均将此列为首要优势。

**S2** [consensus] **实验覆盖面广且控制严格**——8 个生成器×5 个架构家族，LOGO 交叉验证，加上长度控制、独立种子验证 (F1=0.680)、参考模型鲁棒性 (F1 spread=0.013)、跨温度/跨域/跨解码策略验证等大量控制实验。28 页附录体现了对方法局限的深入认识。

**S3** [consensus] **DDR 分解提供了可解释的分析框架**——location drift vs. shape stability 的分解不仅服务于分类，也是对递归生成如何改变文本分布的结构化理解。Cohen's d、TOST、bootstrap stability 等统计刻画严谨。

**S4** [consensus] **轻量级且可部署**——仅需单个 410M 参考模型和 7 个可解释标量特征，无需 GPU 推理或专用检测器，具备实际部署可行性。

**S5** [consensus] **对 limitations 的诚实报告**——base-model-only scope、instruction tuning 失败、3-class ceiling、English-only、fixed decoding 均被明确披露。

**S6** [R2] **与 concurrent work 的对比清晰**——Table 48（Appendix）将本文与 Mohamed et al. (2025) 和 Geng et al. (2026) 进行了详细的维度对比。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical; R2-N1 raised, R1 AGREE] **Shape feature "enables" cross-generator transfer 的因果声称缺乏直接证据**
- Abstract 声称 "shape features provide a cross-generator reference that enables coarse ordinal depth classification"——这是因果声明。
- LOFO 分析（Appendix f, Table 8/9）显示 shape features 边际贡献极小：entropy_min Δ=−1.5pp, tail_decay Δ=−0.8pp, entropy_max Δ=+0.1pp。
- Permutation Importance 中 near-stationary 平均重要性仅为 drifting 的 18%（0.034 vs. 0.187）。
- XGBoost 中跨深度近似恒定的特征不会获得有意义的分裂节点；如果它按生成器变化，反而充当生成器判别器——与"cross-generator reference"是相反机制。
- **R1 补充**：论文可能想表达 shape features 的稳定性作为归纳偏置（inductive bias），但此论点未被显式提出或验证。
- **建议**：(a) 提供消融实验（如仅用 3 个 drifting 特征 vs 全部 7 个的 LOGO F1 对比）验证因果关系，或 (b) 将声称从因果性降级为描述性观察。

**MF2** [critical; R1-N1 raised, R2 AGREE] **Gen-0 种子共享在 LOGO 评估中造成 train-test 信息泄漏，3-class F1=0.762 被高估约 3pp**
- ~1,000 条共享 Wikipedia 种子跨全部 8 个生成器。LOGO hold-out 时，被测生成器的 gen-0 特征向量与训练集 gen-0 完全一致。Appendix confusion matrix 报告 gen-0 准确率 ~99.4%。
- 论文已有缓解：(a) Section 3.2 承认泄漏，(b) 提供 leak-free binary F1=0.694，(c) 标注 binary F1 为 "primary conservative metric"。
- **R2 补充**：即使高估 3pp，核心 DDR 分析基于 per-feature Cohen's d，不依赖分类器性能。Binary F1=0.694 是 leak-free 的。
- **建议**：(a) 将 binary F1 升格为并列主指标（Abstract/Table 2 同等强调），或 (b) 补充不相交种子池的 3-class 评估。

**MF3** [critical; R1-N2 raised, R2 AGREE with nuance] **DDR 分区的事后定义缺乏前置理论驱动**
- DDR 分区通过观察 7 个特征在 (|ρ|, d) 空间后事后定义。k-means 验证使用同一数据存在弱循环。
- **缓解因素**（R2 强调）：(a) Holdout generator split validation (Table 35, Δ(d)≤0.05)——最有力证据但被埋在附录；(b) Per-generator replication——每个生成器独立复现相同分区；(c) Threshold robustness——分区在 ε∈[0.10, 0.75] 范围内稳定。
- R2 认为对于 empirical study，post-hoc observation + rigorous cross-validation 是合法研究路径。
- **建议**：将 Table 35 holdout split validation 提升至主文 Section 4.2。

**MF4** [critical; R2-N2 raised, R1 AGREE with nuance] **Instruction tuning 失效是主要实用性限制，主文讨论不足**
- Appendix k 显示 instruction tuning 使 3-class F1 下降 3.7-19.9pp，DDR 结构被根本性改变。
- 主文 Limitations 仅一句话量化。Section 5 (Discussion) 完全未提及。
- 论文动机（"data provenance, contamination monitoring"）与 base-model-only 适用范围存在脱节。
- **R1 补充**：base model 场景非零（训练数据合成、model collapse monitoring、pre-training contamination detection），不应完全否定方法的实用价值。
- **建议**：Discussion 增加段落（~150词）讨论 instruction tuning 影响并显式界定适用范围。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning; R2-W1 + R1 AGREE] **"Depth profiling" 命名暗示超出实际能力的精细粒度**
- 5-class F1 仅 0.521 (Appendix d)，实际为 3-class 粗粒度分类。建议在标题/摘要中使用更精确表述，或首次使用时限定含义。

**SF2** [warning; R2-W2 + R1 AGREE] **"Entropy" 术语贯穿全文但实际指 reference-model NLL**
- Section 3.3 和 Table 1 有一次澄清，但全文所有表格/图表继续使用 "entropy"。R32-W3 同类问题在之前修复不够彻底。建议在关键位置统一使用 "reference-model NLL" 或 "cross-entropy"。

**SF3** [warning; R1-W5 + R2 AGREE] **Entropy_std 的 "intermediate" 地位 (d=0.55) 挑战 DDR 的 binary partition 叙事**
- DDR 实际为三组结构 (drifting/intermediate/near-stationary)，但 Abstract/Introduction 简化为二元叙事 ("location vs. shape")。建议从顶层叙事开始承认三组结构。

**SF4** [warning; R1-W1 + R2 AGREE] **TOST 等价性边界 |d|≤0.20 缺乏任务特异性校准**
- ε=0.20 来自 Cohen (1988) 社会科学惯例。实际影响有限（near-stationary 特征实际 d<0.10，远低于阈值；分区在 ε∈[0.10, 0.75] 完全稳定）。建议显式引用 LOFO 结果作为任务内校准证据。

**SF5** [warning; R1-W3 + R2 AGREE] **3-class F1 低于最强 baseline (4-det+surface 0.798 vs 0.762) 但主文未充分讨论**
- Section 4.3 聚焦 binary 比较用 "matches" 表述，对 3-class 劣势轻描淡写。建议明确量化效率-性能权衡（单一 410M reference vs 多模型推理）。

**SF6** [warning; R1-W4 + R2 AGREE] **Bootstrap CI 的重采样单位是文本级别，可能低估生成器级泛化不确定性**
- 论文已有 per-generator binary F1 分布（SD=0.028, IQR=[0.692, 0.714]），但未在 CI 报告中突出。建议补充 LOGO fold 级别的 mean±std 作为 generator-level uncertainty 的主要度量。

**SF7** [warning; R2-W5 + R1 AGREE] **Related work 在 stylometry/authorship attribution 方向覆盖不足**
- TTR/hapax ratio 是计算文体学核心特征（Stamatatos, 2009），但论文未讨论 depth profiling 与 authorship attribution 的方法论联系。

### Director 更正

**DC1** [R2-W4 "跨 family 泛化未被显式测试" — 论文已有 LOFO 结果]
- 两位 Reviewer 均认为论文缺乏 leave-one-family-out 测试。但论文 **Table 2 底行** 和 **Section 3.4** 明确报告了 LOFO binary F1=0.686（"LOGO does not isolate family-level effects; Leave-One-Family-Out (LOFO) addresses this by holding out entire model families"；"holding out all three Qwen models (F1=0.686) provides the strictest family-level test"）。
- 此 should-fix 已被论文解决。两位 Reviewer 均未注意到，说明 LOFO 结果可更突出呈现。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（均 [AGREE]）：

1. **Shape feature 因果声称需弱化** (MF1)：LOFO/PI 证据直接矛盾
2. **Gen-0 泄漏真实存在** (MF2)：论文有部分缓解但主指标仍被高估
3. **DDR post-hoc 定义需加强呈现** (MF3)：holdout validation 有效但被埋在附录
4. **Instruction tuning 讨论不足** (MF4)：base model 场景非零但主文需界定适用范围
5. **Entropy 术语问题** (SF2)：与 R32-W3 同类，需更彻底修复
6. **Entropy_std 三组结构** (SF3)：顶层叙事应与实际分区一致
7. **Bootstrap CI 层级** (SF6)：应补充 generator-level 不确定性
8. **Stylometry related work** (SF7)：自然关联方向缺失

## Reviewer Divergence

**DIV1: Contribution #2 的表述——描述性观察 vs 分析贡献**
- R2 认为 DDR 仅是描述性观察，"enables" 表述混淆了观察与方法。
- R1 反驳：DDR 分区具有独立分析价值（holdout validation、k-means、TOST、跨温度/跨域一致性），但同意措辞应更精确。
- **Director 判断**：DDR 的分析价值超出纯描述性观察，但措辞需修订为 "empirical regularity with analytical utility"。

**DIV2: QLoRA 与 XGBoost 的比较基础**
- R1 认为 6-gen QLoRA vs 8-gen XGBoost 不可比。
- R2 反驳：Appendix e 已提供同子集公平对比 (0.905 vs 0.789)，+11.6pp 在公平条件下测量。
- **Director 判断**：同意 R2——同子集对比已存在，但主文呈现应更清晰。

---

## Questions for Authors

1. 能否设计消融实验（如人工打乱 shape features 或仅用 3 个 drifting 特征训练）直接验证 shape features 在跨生成器泛化中的因果作用？
2. 能否提供使用不相交种子池的 3-class LOGO F1 以量化 gen-0 泄漏？
3. QLoRA 在完整 8-gen 上的 LOGO F1？
4. Instruction tuning 下如果直接在 instruct chain data 上训练分类器，信号能否恢复？
5. DDR 分解在 >8B 模型上是否成立？

## Missing References

- **Stamatatos, E. (2009).** A survey of modern authorship attribution methods. *JASIST* — 与 TTR/hapax ratio 特征直接相关的基础综述 [R2+R1 AGREE]
- **Krishna et al. (2024).** Paraphrasing evades detectors — paraphrase attack robustness [R1]
- Ordinal regression/classification 更广泛的文献覆盖 [R2]

## External Review (Stanford Agentic Reviewer)

未配置/未请求。

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 9 info）：
- **[warning]** p.14: Figure 5（7个 violin 子图）占整页约 90% 面积，空间效率偏低。建议调整布局。
- **[warning]** p.36: 最后一页底部约 30% 空白。
- **[info]** 主文 8 页含 4 figures + 3 tables = 7 个 display items，密度合理（~0.88/页）。所有 float 在首次引用附近。无 margin 溢出或未解析引用。
- **[info]** p.7: Figure 3/4 部分标注字号偏小（正文的 60-65%），建议放大。
- **[info]** 页面合规：主文 8 页，Limitations 不计入页数限制，格式合规。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.5/5 | 3.0/5 | 3.25/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.5 | **3.5** |

两位 Reviewer 独立给出 3.5 分。论文在一个有新意的任务（depth profiling）上提供了全面系统的实证分析，DDR 分解具有真实的分析价值，实验覆盖面在 empirical study 中属于上乘。

**核心问题均为 framing/presentation 性质**（非实验设计缺陷），具体为：
1. Shape feature 的因果声称需弱化为描述性观察
2. 3-class F1 的 gen-0 泄漏需在主指标呈现中解决
3. DDR holdout validation 需从附录提升至主文
4. Instruction tuning 失效需在 Discussion 显式讨论

如果上述 4 个 Must-Fix 在修订中得到充分解决（均为文字修改，不需要新实验），论文有望达到 Conference (4.0) 水平。核心实证发现——DDR 分解、跨生成器泛化、大量控制实验——是扎实的。

---

## Detailed Comments

### Abstract
- "shape features provide a cross-generator reference that **enables**..." → 弱化因果措辞 [MF1]
- 3-class F1=0.762 和 binary F1=0.694 应并列呈现并注明 3-class 受 gen-0 共享影响 [MF2]

### Introduction
- Contribution #1 应将 DDR 定位为 "empirical regularity with analytical utility" [DIV1]
- 应在 base-model scope 前置说明处更早限定 [MF4]

### Section 3.2 (Generation Chain)
- Seed sharing 的 leakage 讨论已有，但量化不足 [MF2]

### Section 4.1 (Classification Performance)
- "our primary conservative metric" 已标注 binary F1，但 Abstract/Intro 仍以 3-class 为主 [MF2]
- 补充 per-generator fold-level mean±std [SF6]

### Section 4.2 (DDR)
- 将 Table 35 holdout split validation 从附录提升至此处 [MF3]
- Entropy_std 的三组结构应在此处明确呈现 [SF3]
- Cohen's d 阈值选择应连接 LOFO 结果 [SF4]

### Section 4.3 (Baselines)
- "matches multi-detector ensembles" 表述需附加 3-class F1 差距的诚实讨论 [SF5]

### Section 5 (Discussion)
- 增加 instruction tuning 影响段落（~150 词），界定方法适用范围 [MF4]
- Shape features 的贡献定位需修订 [MF1]

### Section 2 (Related Work)
- 补充 stylometry/authorship attribution 方向讨论 [SF7]

### Limitations
- 已较全面，可加强 instruction tuning 失效的原因分析