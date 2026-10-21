---
round: 20
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-19T15:00:31.383643+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 18 审稿报告 — simgate-modular-routing

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛，无需第 2 轮）

---

## Summary

本文提出 episode-level counterfactual 诊断框架，分析模块化 LLM agent 中 routing signal 的组成。在 ScienceWorld 上（245 episodes, 11/30 task types, Qwen2.5-7B-Instruct），发现 78.9% 的 non-tie routing labels 来自 death asymmetry（internal strategy 的 hallucination 触发 catastrophic death，deterministic strategy 存活），DAF=90.4%。框架在 MATH（null check, p=0.81）和 ALFWorld（识别 information asymmetry 替代机制）做了跨环境探测，在 Llama-3.1-8B 做了跨模型复现（10/10 directional consistency）。四类干预（retry/Reflexion/10× scaling/action filtering）均未消除 death dominance。Router 训练作为 diagnostic probe 显示 step-level routing signal 不可学习（balanced accuracy 54.1±5.4% ≈ chance）。

---

## Strengths

**S1. 形式化贡献扎实** [R1, R2 共识]
Counterfactual labeling function（Algorithm 1）和 DAF 分解（Eq. 4-5）定义清晰，框架可复用于任何有 binary fatal outcome 的环境。

**S2. 统计方法论严谨** [R1, R2 共识]
四种并行推断方法（standard cluster-robust, wild cluster bootstrap, exact permutation, non-clustered bootstrap），SCI 量化 signal 集中度，leave-one-task-out 验证。在 NLP 经验研究中属上乘水准。

**S3. 多维度验证体系** [R1, R2 共识]
跨模型（Llama 3.1-8B, 10/10 directional consistency）、跨环境（MATH null check, ALFWorld qualitative）、四类干预、per-seed breakdown、labeling quality audit。覆盖面远超一般 agent 论文。

**S4. 78.9% penalty-independent label fraction 是干净的经验发现** [R1, R2 共识]
该数字不依赖 death penalty P 的大小，是论文最有说服力的定量结论。

**S5. 诚实的自我批判** [R1, R2 共识]
论文主动报告 DAF 的 P-dependence、K=11 limitation、27.7% mislabeling rate。Practitioner Decision Framework（Appendix R）提供实操指导。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, R1-N1 + R2-N1, 强共识] **DAF 指标在高惩罚下近乎 tautological，核心 framing 有误导性**

DAF = δP/(δP + Δ_nd) 在 P=100 时数学上必然趋近 1。论文自己承认这是 "a mathematical consequence"（§3.1, §5），但 title 和 abstract 仍以 DAF=90.4% 为核心叙事。Penalty-independent label fraction 78.9% 是更 honest 的指标但被置于次要位置。

**Director 裁决**：必须修改。以 78.9% 为主指标，DAF 降级为 P-dependent 辅助指标。正文需呈现 DAF vs P 敏感性曲线（Appendix K 数据已有）。标题和 abstract 不应以 DAF 数值为叙事锚点。

**MF2** [critical, R1-N3 + R2-N3, 强共识] **Episode-level 到 step-level 的 granularity gap 削弱框架实用性**

论文定义 routing signal 为 episode-level pure-strategy performance gap，但实际 routing 发生在 step level。Router 训练（step-level balanced accuracy 54.1±5.4% ≈ chance）暴露了这一断层。27.7% 的 episode-level 标签在 step-level 上不一致，且集中在 death-asymmetry episodes。

R2 补充：论文应明确声明框架是 episode-level 诊断工具（回答"是否值得建 router"），不是 step-level 训练信号来源。R1 进一步指出应分析 mislabeling 对 router 训练的具体影响。97.4% step-level tie rate 为 episode-level 方法提供了合理辩护，但需要在 Method 部分而非仅 Limitations 中说明。

**Director 裁决**：必须在 §2 末尾或 §3.6 增加正式讨论，明确框架适用边界。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, R2-N2 提出, R1 rebut 降级] **跨环境 generalizability 证据不足**

R2 列为 Must-Fix（需 permadeath 环境完整 DAF 分解或标题加限定）。R1 rebut：标题已含 "on ScienceWorld" 限定，generality claim 是方法论层面非经验层面，Discussion 对未测试环境是 future work 指向。

**Director 裁决**：维持 Should-Fix。R1 rebuttal 成立——标题已限定 scope。但 ALFWorld 应提供完整 DAF 定量分解（当前仅 Figure 4 标签分布，缺 DAF 数值）。补充第二个 permadeath 环境能显著提升竞争力但不是 Must-Fix。

**SF2** [warning, R1-N2 提出, R2 rebut 降级] **Cluster bootstrap K=11 推断可靠性**

R1 列为 Critical。R2 rebut：(1) 四种并行方法均 p<0.001，方向 robust；(2) exact permutation p=0.002 不依赖渐近近似；(3) 核心发现是描述性统计量，bootstrap 仅提供 uncertainty quantification。

**Director 裁决**：维持 Warning。R2 的 rebuttal 有力。建议正文以 non-clustered bootstrap 为主要推断，cluster bootstrap 标注为 conservative sensitivity check。

**SF3** [warning, R2-W2, R1 agree] **Non-triviality 论证不足**

§5 "Non-triviality of death dominance" 段的论证（resistance to intervention → non-trivial）不充分。Hallucination-induced death 是 hard problem 在 LLM agent 文献中已有共识。更有效的论证应从 routing 文献 prior assumptions 出发——现有工作假设 signal 来自 capability/quality difference，本文揭示在 interactive environments 中不成立。

**SF4** [warning, R1-W1] **Signal concentration + 63% task exclusion 的 scope limitation**

SCI=0.21，信号集中在少数 tasks。63% 被排除 tasks 的 ΔDR=+38.2pp 支持非 cherry-picking，但排除率仍构成 scope limitation。R2 rebut：排除标准是 methodological，所有 death-prone tasks 100% death dominance。应在正文明确讨论。

**SF5** [warning, R1-W3, R2 部分 agree] **Router 实验 confounds**

(a) Step→episode gap 可能来自 compounding errors 而非 binary signal；(b) train/val split 方式需在主文明确（Appendix J 已报告 episode-level split 排除 leakage，但主文不清晰）。

**SF6** [warning, R1-W4, R2 agree] **Agent improvement 实验统计功效不足**

Reflexion N=5 × 10 tasks = 50 data points，Figure 3 error bars 严重重叠。Retry n=200 与 Reflexion N=5 compute budget 不对等，论文未报告 per-intervention compute cost。

**SF7** [warning, R2-W3, R1 agree] **Safe RL 相关工作覆盖偏薄**

§4 safe RL 段落仅一句话带过五篇引用。缺 irreversible action avoidance 形式化、safe exploration 文献。

### Minor Issues

- **m1** [info] Figure 2 caption 需添加 "structural consequence of the DAF decomposition" caveat [R1, R2 agree]
- **m2** [info] "modality" 术语歧义——建议改用 "computation mode" 或 "strategy" [R1]
- **m3** [info] Webb (2023) 引用年份需核实（可能是 2014 working paper vs 2023 正式发表）[R1, R2]
- **m4** [info] Appendix 缺索引（17 个 appendices A-R）[R1]
- **m5** [info] §3.1 "54 sole-identified labels" 首次出现未定义 [R2]
- **m6** [info] Appendix N failure categories 基于 manual inspection，缺 inter-annotator agreement [R2]
- **m7** [info] 100% deaths 来自同一 action pattern (focus on [object])——应讨论 signal trivially binary 的 implication [R2]

---

## Reviewer Consensus

1. **DAF framing 需修正** [R1-N1 = R2-N1]：DAF=90.4% 是 P=100 的数学产物，78.9% penalty-independent label fraction 应为主指标。
2. **Episode→step gap 需正式讨论** [R1-N3 ≈ R2-N3]：框架的 episode-level 定位与 step-level routing 需求之间的鸿沟需在 Method 部分讨论。
3. **Non-triviality 论证需加强** [R2-W2, R1 agree]：当前论证不足以化解 obvious-in-hindsight 风险。
4. **Safe RL 覆盖需扩展** [R2-W3, R1 agree]。
5. **Figure 2 caption 需 caveat** [R2-W5, R1 agree]。
6. **统计方法论值得肯定** [R1-S2, R2-S2]：四种并行推断方法在 NLP 经验研究中属上乘。
7. **形式化贡献清晰** [R1-S1, R2-S1]：Algorithm 1 和 DAF 分解可直接复用。

---

## Reviewer Divergence

| 分歧点 | R1 | R2 | Director 裁决 |
|--------|-----|-----|--------------|
| Cluster bootstrap K=11 严重程度 | Critical | Warning — 四种方法均 p<0.001 | **Warning** — R2 论据更充分 |
| Generalizability 严重程度 | Should-Fix | Critical — 需 permadeath replication | **Should-Fix** — 标题已限定 scope |
| Abstract 数字密度 | Rebut（数字是证据） | Warning — 8+ 数字过多 | **不列入正式 weakness** |
| Cross-model 主文表格 | Rebut（appendix 标准做法） | Warning | **Minor** — 可选添加 2-row summary |
| Router practical value | Warning — 未转化为改进 | Rebut — diagnostic 定位明确 | **分歧保留** — 双方各有道理 |

---

## Questions for Authors

1. DAF 在 P=10、P=1 时分别降至多少？78.9% label fraction 在 P=0 时如何变化？
2. 27.7% mislabeled episodes 中，step-level 实际错误比例是多少？分布在哪些 task types？
3. 如果在 task-type level 训练 lookup table（而非 step-level router），balanced accuracy 是多少？
4. Step budget 从 30 增加到 50/100 时，被排除的 19 个 tasks 是否产生有效 routing signal？
5. Oracle routing 上随机翻转 x% 决策的 episode-level 退化曲线如何？

---

## Missing References

1. **Moldovan & Abbeel (2012)** "Safe Exploration in Markov Decision Processes" — irreversible/catastrophic states 形式化 [R2, R1 agree]
2. **Ruan et al. (2024)** LLM agent failure taxonomy [R2]
3. **Graves (2016)** "Adaptive Computation Time for RNNs" — adaptive routing 经典前身 [R2]
4. 近期 LLM agent catastrophic action prevention 工作 [R1]

---

## External Review (Stanford Agentic Reviewer)

未配置，跳过。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已派发但**超时**（elapsed: 655s）。无排版质量评估可用。

格式合规由 Reviewer 手动检查：
- ✅ 正文 ≤ 8 页
- ✅ `\usepackage[review]{acl}` double-blind
- ✅ Author "Anonymous"，无身份泄露
- ✅ Limitations section 存在且充分
- ✅ Ethics Statement 存在
- ✅ Responsible NLP Checklist 完整
- ✅ 引用格式一致（ACL natbib），46 条引用，无虚假引用

---

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

| 维度 | R1 | R2 | 加权判断 |
|------|-----|-----|---------|
| Soundness | 3/5 | 3.5/5 | 3.5/5 — R2 对统计方法论的肯定更准确 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 — obvious-in-hindsight 风险实质存在 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**理由**：

1. **方法论价值确认**：Counterfactual diagnostic framework 设计严谨，形式化清晰，统计处理在 NLP 经验研究中属上乘。78.9% penalty-independent label fraction 是一个干净的经验发现。这些优点支撑 Findings 接收。

2. **Framing 问题严重**：DAF=90.4% 作为标题级叙事锚点，但其数值主要由 P=100 的惩罚结构决定，是数学产物而非独立经验发现。这构成 framing 与证据之间的系统性张力，是阻碍 Conference 接收的核心问题。

3. **Novelty 风险**：R1 Excitement 3/5, R2 Excitement 2.5/5。"避免死亡比优化 score 更重要"在直觉上并不令人惊讶。论文的价值更多在 quantification 和 methodology 而非 finding 本身，但 non-triviality 论证不足以充分化解这一风险。

4. **Scope 受限**：完整分析仅在 ScienceWorld（11/30 tasks）上完成。跨环境 probes（MATH, ALFWorld）深度有限。MiniHack pilot 结果为 negative（项目实验记录），进一步限制了 generalizability 证据。

5. **Episode→step gap**：框架的 diagnostic 输出无法直接指导 step-level routing 设计（router ≈ chance），实际 actionability 有限。

**提升至 3.5（Borderline Conference）的明确路径**：
1. 修正 DAF framing（以 78.9% 为核心，DAF 降级为 P-dependent 辅助指标）
2. 补充第二个 permadeath 环境的完整 DAF 分解（或至少 ALFWorld 完整定量）
3. 加强 non-triviality 论证（从 routing 文献 prior assumptions 出发）
4. 明确框架的 episode-level diagnostic 定位和适用边界

---

## Detailed Comments

### §1 Introduction
- 核心叙事 reframe：从 "death avoidance dominates routing signal" 转向 "death dominance resists standard interventions"，突出 intervention robustness 的非先验可预测性 [SF3]

### §2 Method
- §2 末尾增加 episode-level vs step-level granularity gap 的正式讨论 [MF2]
- 说明 97.4% step-level tie rate 为 episode-level 方法提供的合理性辩护 [MF2]
- "modality" 考虑改为 "computation mode" 或 "strategy" [m2]

### §3 Experiments
- §3.1: 以 78.9% 为主指标，DAF 降级；呈现 DAF vs P 敏感性曲线 [MF1]
- §3.2: 可选添加 Qwen vs Llama 2-row summary inline 对比 [minor]
- §3.3: Agent improvement 实验增加 paired test 或报告 minimum detectable effect size [SF6]
- §3.4: ALFWorld 需完整 DAF 定量分解 [SF1]
- §3.6: 主文明确 train/val 是 episode-level split [SF5]

### §4 Related Work
- Safe RL 段落扩展至 3-5 句，补充 Moldovan & Abbeel 2012 等 [SF7]

### §5 Discussion
- "Non-triviality" 段从 routing 文献 prior assumptions 出发重写 [SF3]
- "Anatomy of catastrophic failure" 讨论 single action pattern 的 implication [m7]

### Figures/Tables
- Figure 2 caption 添加 structural consequence caveat [m1]

### References
- 核实 Webb (2023) 年份 [m3]
- 补充 Moldovan & Abbeel 2012, Ruan et al. 2024, Graves 2016 [SF7]

### 引用验证
46 条 bib 条目：36 verified, 6 minor mismatch (author encoding), 4 not_found (OpenAlex 索引延迟), 0 orphan, 0 missing, 0 fake。整体引用质量良好。