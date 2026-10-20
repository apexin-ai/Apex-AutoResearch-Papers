---
round: 27
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T13:59:25.226039+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 29 (Fresh Review)

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**Deadline**: 2026-05-25
**审稿模式**: Fresh（全新审稿，无历史记忆）
**Reviewers**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）
**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic reasoning 管道中 GRPO 训练输出的结构诊断方法。STA 对证明的每个组件执行 leave-one-out (LOO) 删除并重新调用 solver，计算 Intensional Structural Reward (ISR)——必要组件占比。在 FOLIO (FOL) 和 Prolog 两种逻辑体系上，论文展示：(1) GRPO 训练使 ISR 崩溃，揭示执行正确率掩盖下的结构退化；(2) 将 ISR 用作训练 reward 时出现 Goodhart 效应（hacking mode 从 CE 转向 TS）；(3) 跨逻辑体系（FOL→Prolog）和跨数据集（FOLIO→ProofFOL）验证了这一现象。贡献包括 STA 框架、ISR 指标、8-mode hacking taxonomy、以及 observe-vs-optimize asymmetry 的经验证据。

---

## Strengths

**S1. 重要且及时的现象记录。** 在 RLVR 社区快速扩张的背景下，系统记录 GRPO 训练导致的 neurosymbolic proof 结构退化具有实际价值。STA 框架本身是清晰、可操作、可复现的诊断工具。Algorithm 1 简洁优雅。[R1+R2 共识]

**S2. 实验控制设计合理。** 六个 reward 条件（exec-only, ISR low/high-dose, matched random controls, SFT baseline）加上 shuffled-ISR deconfounding control，形成有说服力的对照结构。Premise-count matched comparison 是诚实的自我修正。[R1+R2 共识]

**S3. 8-mode hacking taxonomy 对实践者有用。** Appendix D 对每种 hacking mode 提供了定义、FOL/Prolog 示例、ISR 交互分析和 prevalence 统计，是社区迄今为止最细粒度的 neurosymbolic reward hacking 分类。[R1 主导，R2 acknowledge]

**S4. 跨域验证增强可信度。** FOL→Prolog 是真正的跨逻辑体系验证；ProofFOL 提供了 within-FOL 跨数据集复制。LLaMA-3.2-3B 和 Qwen3-8B 的 negative results 也有信息价值。[R1+R2 共识]

**S5. 透明度高。** 论文对自身限制（N=3 统计效力、premise-count confound、seed 43 协议偏差、PG audit 覆盖不足）的讨论坦诚详尽，附录极为详细（14 页）。承诺开源代码、数据集和 checkpoint。[R1+R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, R1-N2 + R2-N1, 双 Reviewer 共识] **ISR "214× collapse" 核心叙事存在系统性 framing 问题**
- Abstract 和 Introduction 以 raw ISR 从 0.642 崩溃至 0.003（214×）作为核心叙事钩子，但 §4.2 "Premise-count confound" 承认匹配 premise count 后优势仅为 **1.06×**。这意味着 214× 的绝大部分来自 premise count 变化（ISR-trained 模型产生更短 formalizations）而非真正的结构退化。Abstract 和 Introduction 完全未提及此关键 caveat——读者到第 6 页才发现。
- **影响**：ISR 作为 aggregate metric 的独立诊断价值被严重质疑。如 premise count 能提供几乎相同的信号，STA 的核心价值需从 aggregate ISR 重新定位到 per-sample mode classification。
- **建议**：(1) Abstract/Introduction 首次提及 ISR collapse 时注明 premise-count confound 及 matched effect size；(2) 以 premise-count-matched ISR 为主报告指标；(3) 明确区分 ISR 的两个用途层次：aggregate（≈ premise count proxy）vs. per-sample（真正的必要性诊断）。

**MF-2** [critical, R1-N1, R2 AGREE] **N=3 seeds 统计效力严重不足，核心 claims 缺乏可靠量化证据**
- 论文自承 N=3 仅对 d≥2.0 的超大效应有 80% power。多个关键比较未达显著性：ISR vs Random non-hacking p=0.182、ProofFOL p=0.10。CMH 检验将 within-seed 样本视为独立观测（真正 N=3），pseudo-replication 膨胀了显著性。5-seed extension 存在 double standard：§4.1 标记为 exploratory，但 Appendix E 用其做 bimodal seed-dependence 分析。
- **影响**：论文的实验贡献从"量化证据"降格为"定性观察"。
- **建议**：(1) 将 5-seed 纳入主分析或统一其在正文/附录中的定位；(2) 对 CMH 做 cluster-robust 校正（seed 为聚类单元）或仅报告 seed-level tests；(3) 所有非显著结果在正文中明确标注。

**MF-3** [critical, R1-N3, R2 AGREE] **Seed 43 评估协议不一致**
- Seed 43 使用 T=0.7 sampling 而非 greedy decoding（Appendix A 承认 "not strictly comparable"）。在 N=3 设计中，1/3 seeds 协议不一致使 exec-only condition 的结论可信度大打折扣。将 not strictly comparable 的 seed 纳入 pooled 分析是分析上的失误。
- **建议**：(1) 用 greedy decoding 重新评估 seed 43；(2) 如无法恢复，提供 N=2 (s42+s44) 的 sensitivity analysis 作为主分析。

---

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, R1-W1 + R2 AGREE] **50% exec-only seeds 不收敛引入生存偏差**
- 6 seeds 中仅 3 收敛。不收敛 seeds 保留了更高 structural integrity（85-87% genuine），暗示 degeneration 是 convergence 副产品而非 GRPO 固有行为——这可能是论文最有趣的 secondary finding（bifurcation point），但被放在附录中。建议在 Limitations 中显著讨论。

**SF-2** [warning, R2-N2, R1 REBUT → 降级] **方法论新颖性有限**
- LOO ablation 是标准技术（1978），STA 是其在 neurosymbolic 输出上的直接应用。与 Helff et al. (2026) IPT 缺乏实验对比。R1 REBUT：STA+ISR+taxonomy 组合贡献 > 单纯技术迁移，solver-backed 设定使 LOO 具有 deterministic ablation 优势。
- **分歧记录**：R2 认为 Must-Fix，R1 认为 Should-Fix。Director 采纳 R1 的 REBUT（case study 定位 + taxonomy + Goodhart 实证构成组合增量），定级 Should-Fix。
- **建议**：在 Related Work 中更明确阐述 STA 的不可替代性（component-level + deterministic + training-time），以及与 IPT 的互补性。

**SF-3** [warning, R2-N3 + R1 AGREE with nuance → 降级] **"Compositional Goodhart" 术语缺乏操作性定义**
- 本质是 regressional Goodhart 在 multiplicative ISR reward 下的 expected instantiation。R1 同意有道理但认为是 terminology 而非方法论缺陷。
- **建议**：去掉 "compositional Goodhart" 术语，直接用 "regressional Goodhart pattern" 或 "mode shifting under ISR optimization"。

**SF-4** [warning, R1-W2 + R2 AGREE] **Classifier recall 未估计，non-hacking rates 可能系统性高估**
- Precision=1.00 (152 样本)，但 recall "not estimable"。不同 hacking modes 的 recall 可能差异很大，影响跨条件比较（ISR vs Random 的微妙差异可能被 recall 差异污染）。
- **建议**：对至少一个 condition 做 recall 估计；讨论 recall 变异对 cross-condition comparisons 的影响。

**SF-5** [warning, R1-W4 + R2 AGREE] **Shuffled-ISR control 证据单薄 (N=46)**
- 87% non-hacking 的 95% CI ≈ [77%, 97%]，太宽。论文在 §4.1 标记为 secondary 但 §4.2 用作 key evidence——secondary-then-key 切换削弱论证严谨性。

**SF-6** [warning, R1-W5 + R2 AGREE] **乘法耦合 reward 的 confound 未充分控制**
- r_exec · (1 + β·ISR) 的乘法耦合使 ISR signal 和 multiplicative interaction 无法分离。Additive variant 仅一次失败就被排除。

**SF-7** [warning, R2-W2 + R1 AGREE] **ISR 与 Shapley values / influence functions 的方法论关系未被讨论**
- ISR 本质上是 Shapley value 的退化形式（仅 n-1 coalition）。建议在 §3.2 讨论关系并引用 Lundberg and Lee (2017)。

**SF-8** [warning, R2-W3 + R1 AGREE with nuance] **ProofFOL "cross-domain" 声称需更谨慎 framing**
- FOLIO→ProofFOL 是 same-task-family (FOL) 的 cross-dataset 复制，非真正 cross-domain。建议区分 "cross-dataset replication"（ProofFOL）和 "cross-domain replication"（Prolog）。

**SF-9** [warning, R2-W4 + R1 AGREE] **单模型泛化性存疑 / "Goldilocks" 假说**
- Qwen3-8B 和 LLaMA-3.2-3B 均未复现 degeneration（前者 rollout diversity bottleneck，后者 cold-start failure）。Degeneration 可能仅在模型能力恰好处于某个窄带时发生。建议在 Discussion/Limitations 中更显著地讨论此 threshold 效应。

**SF-10** [warning, R2-W6 + R1 AGREE] **缩写密度过高**
- ISR, STA, CE, TS, PG, TSb, N-H, PR, LOO, CMH... 对非本领域读者构成显著阅读障碍。建议在密集段落开头添加缩写回顾。

---

### Minor Issues（不影响接收）

- **M1** [R1-M1]: Abstract "ISR diagnoses structural degeneration" 暗示独立诊断力，建议更精确表述。
- **M2** [R2-M2]: Discussion and Conclusion 过于简短（不到半 column），建议讨论 STA 对其他 RL reasoning 系统的适用性。
- **M3** [R1-M3 + R2-W6]: Hacking mode 缩写 (CE, TS, PG) 首次使用时缺乏足够上下文。
- **M4** [R1-M4 + R2-M3]: Figure 2 子图在灰度打印下可能难以区分，建议增加 pattern fill。
- **M5** [R1-M5]: §4.4 ProofFOL "p=0.10" 在正文位置给读者过强印象，建议明确 "underpowered; directional only"。
- **M6** [R2-M4]: ISR 对 unproved samples 的处理在正文中应有简短提及（仅在 Appendix B 出现）。

---

## Reviewer Consensus

### 共识 [AGREE]
1. **Overall 3.0 (Findings)**——双 Reviewer 独立给出相同评分
2. **Premise-count confound 是最关键问题**——ISR aggregate ≈ premise count proxy (MF-1)
3. **N=3 统计效力不足**——核心 claims 缺乏可靠量化证据 (MF-2)
4. **Seed 43 评估协议不一致**——clear-cut 实验设计缺陷 (MF-3)
5. **"Compositional Goodhart" 术语应放弃**——无操作性定义 (SF-3)
6. **Shuffled-ISR control 证据单薄** (SF-5)
7. **STA 框架本身有诊断价值**——核心优势 (S1)
8. **Hacking taxonomy 对实践者有用** (S3)
9. **透明度和可复现性高** (S5)

### 分歧 [REBUT]
1. **方法论新颖性** (SF-2)：R2 认为 Must-Fix（LOO 应用于新领域不需解决新技术挑战），R1 REBUT 降为 Should-Fix（组合贡献 > 单纯迁移）。**Director 采纳 R1 的 REBUT**——case study 定位下，STA+ISR+taxonomy+Goodhart 实证构成足够的组合增量。
2. **Taxonomy 性质** (SF-4 相关)：R2 认为 ad-hoc 枚举，R1 REBUT 认为 empirically-grounded enumeration 是恰当的。**Director：taxonomy 有实用价值但应承认 open-ended 性质。**
3. **"Observe-vs-optimize asymmetry" 新颖性**：R2 认为本质即 Goodhart's Law，R1 REBUT 认为论文提供了首次 fine-grained 实证图景（dose-response、mode-specific ISR 差异）。**Director：分歧记录。R1 的 REBUT 有据但论文应避免将其包装为独立新概念。**

---

## Questions for Authors

**Q1** [R1+R2 共识]: Premise-count matched ISR 仅 1.06×。请解释为何读者应认为 ISR collapse 反映"结构退化"而非简单的 premise-count 变化？是否考虑过直接用 premise count 作为更简单的 aggregate 诊断替代品？

**Q2** [R1]: 50% exec-only seeds 不收敛。不收敛 seeds 是否保留了更好的结构完整性？如果是，这是否挑战 "structural degeneration is a consequence of GRPO training" 的 claim——它可能仅是 successful convergence 的副产品？

**Q3** [R1]: Shuffled-ISR control 仅 46 proved samples。如何论证这足以排除 "ISR 分布形状驱动 Goodhart 效应" 的替代假设？

**Q4** [R2]: Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM。ISR 是否可重新表述为 explicit PRM signal？如果可以，对论文 framing 有何影响？

**Q5** [R1+R2]: TS hacking mode 下 ISR 反向效果（ISR≈0.5 by construction）。ISR 作为跨条件的 unified diagnostic 是否存在根本缺陷？

---

## Missing References

1. **Lundberg and Lee (2017)** "A Unified Approach to Interpreting Model Predictions" — ISR 与 Shapley values 的方法论联系 [R2 提出, R1 AGREE]
2. **Coste et al. (2023)** "Reward Model Ensembles Help Mitigate Overoptimization" — Goodhart mitigation [R1 提出, R2 AGREE]
3. **Moskovitz et al. (2023)** "Confronting Reward Model Overoptimization with Constrained RLHF" — 替代 paradigm [R1 提出, R2 AGREE]
4. **DNN mutation testing 近期工作** — ML-specific mutation testing [R2 提出, R1 部分 AGREE: 方向合理但与 solver-backed 设定差异大]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~3 分钟），1 critical / 2 warning / 7 info。

| 严重度 | 位置 | 发现 |
|--------|------|------|
| critical | p.22 | 末页仅 6 行文本（~5% 填充），其余全部空白。极不专业——建议合并至上一页或填满。 |
| warning | pp.4-5 | 连续两页纯文本（Method §3.3 → Experiments §4.1），无 figure/table 穿插。建议前移 Figure 2 或 Table 1。 |
| warning | p.18 | Table 8 字号偏小、列数多（~10 列），密度极高。建议 Notes 列移入脚注。 |
| info | p.2 | Figure 1 颜色方案整体可区分，中段重叠区域略降但有线型辅助，可接受。 |
| info | p.6 | Figure 2(b) 5+ 色彩堆叠柱状图在灰度打印下可能难以区分。建议 pattern fill。 |
| info | p.7 | Table 1 + Figure 3 同页——密度高但排版整洁。 |
| info | pp.9-10 | References 格式统一，无未解析引用。 |
| info | p.3 | Algorithm 1 排版清晰。 |
| info | p.11 | Appendix Tables 3-4 格式规范。 |
| info | pp.15-17 | Hacking mode 定义排版结构化良好。 |

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

**置信度: 4/5**（两位 Reviewer 均熟悉 RLVR、neurosymbolic reasoning 和统计方法论）

### 评分理由

本文记录了一个有实际价值的现象（GRPO 训练导致 neurosymbolic proof 结构退化），提供了实用的诊断工具（STA/ISR）和系统的 hacking taxonomy，实验控制合理，附录详尽，透明度高。

三个 Must-Fix 问题阻止了主会议接收：

1. **ISR aggregate 的核心叙事存在 framing 问题**——214× headline 在控制 premise count 后仅剩 1.06×，Abstract/Intro 未披露，构成选择性呈现。ISR aggregate 本质上是 premise count 的 proxy，论文需要诚实地重新定位 STA 的价值。

2. **N=3 seeds 的统计效力不足**——多个核心比较未达显著性，CMH 存在 pseudo-replication，5-seed extension 定位不一致。论文的实验贡献从"量化证据"降格为"定性观察"。

3. **Seed 43 评估协议不一致**——在 N=3 设计中，1/3 seeds 使用不同评估协议（T=0.7 vs greedy）是不可接受的实验设计缺陷。

**若能解决 MF-1（framing 修正 + ISR 双重用途明确化）和 MF-3（seed 43 re-evaluation 或 N=2 sensitivity analysis），可上升至 3.5 (Borderline Conference)。MF-2（统计效力）需要更多 seeds，短期内难以完全解决，但 5-seed 统一纳入主分析可部分缓解。**

---

## Detailed Comments

### §1 Introduction
- "ISR … collapses from 0.642 to 0.003, a 214× raw drop" — 需立即注明 "(partially attributable to premise-count inflation; matched comparison yields 1.06×, §4.2)"。当前正文中 §4.2 有此 caveat 但 Intro 完全缺失。
- "observe-vs-optimize asymmetry" 术语：建议降级为 descriptive phrase 而非 coined concept，以避免暗示超出 Goodhart's Law 的新理论贡献。

### §3.2 Method (ISR)
- 在定义 ISR 后立即讨论其双重用途（aggregate vs per-sample）及各自的 confound sensitivity。当前 "Limitations of ISR" 段部分涉及但不够明确。
- 增加 Shapley values 方法论联系的讨论（为何 LOO 而非 Shapley：O(n) vs O(2^n)，solver-backed binary necessity）。

### §4.1 Setup
- "Statistical considerations" 段的 N=3 caveat 是好的，但 Abstract/Intro 的叙事未反映这些 null results。
- Seed 43 "uses nucleus sampling (T=0.7) due to greedy-mode degeneration" 需更明确的处理：要么排除，要么提供 sensitivity analysis。

### §4.2 Goodhart Effects
- Table 1 信息密度极高。建议至少在 caption 中完整展开所有缩写（当前已有部分展开）。
- "compositional Goodhart" → 改为 "regressional Goodhart pattern" 或 "mode shifting"。

### §4.4 Cross-Domain
- "Cross-Domain and Cross-Dataset Evidence" 小节标题中，ProofFOL 部分应明确标记为 "within-FOL cross-dataset replication"。

### §5 Discussion and Conclusion
- 过于简短（2 行）。建议至少讨论：STA 对 math reasoning RL 系统的潜在适用性；ISR 与 PRM 的整合可能性；Goldilocks 假说。

### §6 Limitations
- 增加 50% exec-only seeds 不收敛及其对结论的影响。
- 增加 classifier recall 未知的讨论。

### Appendix
- p.22 末页空白需修复。
- Table 8 可读性可优化（Notes 列移入脚注）。
