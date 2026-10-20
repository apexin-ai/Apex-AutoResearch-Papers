---
round: 40
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T15:23:18.205316+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: True
---

# 审稿报告 — Round 40 (Fresh) [交叉分享后最终版]

**论文**: When Does Test-Time Scaling Fail? A Diagnostic Framework for Named Entity Recognition
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: R1 方法严谨性, R2 新颖性/完整性
**模式**: Fresh（重新审稿），含完整交叉分享

---

## Summary

论文研究 test-time compute scaling（self-consistency、best-of-N）在 NER 上的失败机制。在 4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）上，发现 quality estimation 信号虽可预测输出质量（AUROC up to 0.82），但 instance-level selection 增益 <1pp——"correlation-selection gap"。提出三因素诊断框架（degeneracy D、oracle gap G_nd、signal alignment α）定位失败原因。Entity-level construction 在 Few-NERD 获条件性增益（+1.40pp），但 69% 的 N-transitions 出现 inverse scaling。附带 RE 和 SQL 探索性扩展。

---

## Strengths

1. **极其全面的经验分析**：45 页含 62+ 表格，覆盖 robustness（温度、seed、N-scaling）、多信号对比（5 signals × 9 method categories）、cross-dataset transfer、epoch confound、free-form ablation。[R1/R2 共识]

2. **统计报告规范性远超平均**：Holm-Bonferroni 全局校正（即使不利于自身结果）、bootstrap CI、permutation test、TOST 等价性检验、power analysis。[R1/R2 共识]

3. **科学诚实度高**：主动承认 bound looseness（3-12%）、epoch confound（+1.39→+0.12pp）、probe 架构限制、seed 不足。[R1/R2 共识]

4. **概念框架有实用价值**：degeneracy / signal alignment collapse / correlation-selection gap 三元分解对从业者有可操作的诊断价值。entity-level 粒度的三元分解在 concurrent work 中未见。[R1/R2 共识]

5. **Failure case 分析具体可信**：Appendix ag 的定性实例增强了定量发现的可信度。[R2]

---

## Weaknesses

### Must-Fix（5 个，交叉分享后共识确认）

**N1** [R1 Must-Fix, R2 AGREE] **Degeneracy bound 诊断价值不足**
Bound E[ΔF₁(A)] ≤ (1−D)·G_nd·α 仅恢复 actual gains 的 3-12%。两位 Reviewer 共识：形式化成本 > 洞察增量。"Degeneracy 限制增益"从定义本身就显然（degenerate instances 的 ΔF₁=0 是定义性的）。bound 近乎同义反复。R2 补充：α-decomposition（α 而非 D 是 binding constraint）有诊断价值，但不需要 formal bound 包装。
**建议**：明确论证 α 发现的独立价值；降低 bound 在论文中的地位为辅助观察。

**N2** [R1 Must-Fix, R2 AGREE] **核心正面 claim 在 Holm-Bonferroni 校正后 p_adj=0.055**
脚注5 承认 "most liberal core claim reaches p_adj=0.055"，但未点名具体 claim。R2 补充关键观察：核心负面叙事（scaling fails）不受影响，但若正面 claim（entity construction +1.4pp, LP selection +1.39pp）在 Holm 下不存活，论文退化为纯 negative result paper，对 EMNLP 接收标准不利。
**建议**：正文显著位置标注具体 claim；增加 seeds ≥5；或将正面 claim 降格为 suggestive evidence。

**N3** [R1 Must-Fix, R2 AGREE] **Mechanistic probes 用 Qwen2.5-7B 而非 Qwen3-8B**
§3 的 ESJ/MRSC/LSC/hidden-state probe 全部基于 Qwen2.5-7B。完全共识。R2 补充：Qwen3 有 thinking mode，reasoning capability 可能更强，ESJ AUROC=0.512（chance level）的结论可能不迁移。
**建议**：在 Qwen3-8B 上复现至少 hidden-state probe + ESJ；或将 §3 移至附录。

**N4** [R2 Must-Fix, R1 AGREE with nuance] **Novelty 与 concurrent work 重叠**
三个核心概念有 prior/concurrent work：correlation-selection gap (Landesberg 2026)、consistency-accuracy for IE (Yao 2026)、diversity collapse (Yun & Price 2025)。R1 认可 entity-level 三元分解的粒度是差异化贡献，但同意 §8 差异化论述不充分——仅各一段提及，缺 systematic comparison。
**建议**：§8 增加 comparison table（每篇 concurrent work 覆盖哪些维度 vs 本文新增什么）。

**N5** [R2 Must-Fix, R1 AGREE] **标题 overpromise**
"When Does Test-Time Scaling Fail?" 暗示一般性回答，但仅系统验证 NER。RE (n=397) 和 SQL (n=196) 为 exploratory。完全共识。
**建议**：修改标题明确 NER scope。

### Should-Fix（9 个，含交叉分享降级）

**W1** [messaging 问题，非逻辑矛盾] **Diagnostic/prescriptive 过渡不清晰**
R2 反驳有力：diagnostic→prescriptive 逻辑相容（diagnose→prescribe）。共识：messaging 需改进。
**建议**：§7.5 开头说明"框架事前诊断，诊断结果指导事后方法选择"。

**W2** [R1/R2 共识] **Seeds 不足 (2-3)**
Bootstrap 估计 instance-level 而非 seed-level variance。对 Few-NERD 正面结论尤其不足。
**建议**：核心配置增至 5 seeds。

**W3** [R1/R2 共识] **LP 效用与 constrained decoding 绑定**
Free-form ablation 显示 RE LP direction reverses。LP 表面相关性可能 partially spurious。
**建议**：Limitations 突出讨论；连接 Yun et al. 的 diversity collapse。

**W4** [R1/R2 共识] **Few-NERD +1.39pp 是 under-convergence 产物**
5-epoch 消除 91% gains。唯一正面结果依赖 under-converged state。未讨论 convergence-selection tradeoff。
**建议**：Abstract/§1 标注 epoch-dependent；讨论 tradeoff。

**W5** [降级为 minor] **Entity independence assumption**
R2 有效反驳：entity-level F1 固有假设，非 MBR 额外引入。
**建议**：Limitations 简要提及 F1 不捕获实体间依赖。

**W6** [分歧存在] **建设性贡献增益微弱**
R1 反驳：诊断论文不应以增益评判。Director 判断：R1 论点合理但 concern 客观存在。
**建议**：Abstract/§1 降低建设性贡献权重，突出诊断结论。

**W7** [R1 REBUT→降级] **论文结构（Related Work 在 §8）**
R1 反驳有力：*CL 常见结构，ARR 无硬性要求，formal defs 在附录因 8 页限制。从 critical 降级。
**建议**：可考虑调整但非必须。

**W8** [R1/R2 部分共识] **N=8 / 7-14B 局限**
N 已探索到 64，但 scale range 太小支撑 "not scale-dependent" claim。
**建议**：弱化该 claim；Discussion 讨论 70B+。

**W9** [R1/R2 共识] **Introspection boundary 未贯穿**
§3 引入后 §4-7 未引用。
**建议**：§4 连接回 introspection boundary。

---

## Reviewer Consensus [交叉分享后确认]

**完全共识**：N1 (bound), N2 (statistics), N3 (probe model), N5 (title), W2 (seeds), W3 (LP confound), W4 (epoch), W9 (terminology)

**交叉分享解决的分歧**：
- R2-N3 结构 → R1 REBUT → **降级为 W7**
- R1-W5 Entity independence → R2 REBUT → **降级为 minor**
- R2-W3 Over-hedging → R1 REBUT（与 N5 矛盾）→ **降级为 minor**
- R1-W1 Diagnostic/predictive → R2 REBUT → **降级为 messaging 问题**

## Reviewer Divergence [未完全解决]

**Overall score**: R1 3.5 vs R2 3.0 — 差异核心在 novelty 权重。R1 认为 entity-level 三元分解构成 incremental but valid novelty；R2 认为三个核心概念均有 concurrent work。Director 判断：novelty 存在但 incremental，Findings 更合适。

---

## Questions

1. p_adj=0.055 对应哪个具体 claim？
2. 为何不在 Qwen3-8B 上复现 probe？
3. "F1-degenerate but output-diverse" 有多常见？应区分 identical outputs vs same-F1-different-entities vs same-F1-different-boundaries。
4. θ 在 unseen datasets 上的迁移性？
5. LP 效用是否 fundamentally tied to constrained decoding？
6. Under-converged model 有 selection space 但 lower base performance — 如何平衡？

---

## Missing References

- Yee et al. (2019) "Simple and Effective Noisy Channel Modeling for NMT"
- Li et al. (2023) "Step-Aware Verifier"
- PRM/ORM for structured outputs (Lightman et al. 2024, Wang et al. 2024)
- E-NER (arXiv 2305.17854)
- arXiv 2311.08726 sequential labeling uncertainty

---

## External Review

未请求（项目未配置）。

---

## Visual Layout Check（非评分项）

已完成。0 critical, 1 warning, 8 info。
- **[WARNING]** p45：最后一页仅 ~20% 填充。
- **[INFO]** p1-2：Figure 1 在 p3，建议上移。
- **[INFO]** p7：单页 3 个 display items。
- **[INFO]** p14/15：子图轴标签偏小。
- **[INFO]** p22：Table 12 (57 行) 需 caption 引导。

---

## Overall Assessment

**评分：3.0 (Findings)**
**置信度：4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.0 | **3.0** |

**Findings 接收依据**：诊断框架的系统性和实验覆盖全面性超越现有 concurrent work；对 NER test-time scaling 的实践指导有价值；统计报告规范性值得社区参考。但 novelty incremental、核心正面 claim 统计边界、mechanistic 证据缺口阻碍主会议。

**提升至 Conference (3.5-4.0) 的路径**：
1. Qwen3-8B 上复现 probe → 修复 N3
2. 增加 seeds ≥5 使 p < 0.05 → 修复 N2
3. §8 comparison table + 标题修改 → 修复 N4/N5
4. Abstract/§1 标注 epoch-dependent + 降低建设性贡献权重 → 修复 W4/W6
5. 明确 diagnostic→prescriptive 过渡 → 修复 W1