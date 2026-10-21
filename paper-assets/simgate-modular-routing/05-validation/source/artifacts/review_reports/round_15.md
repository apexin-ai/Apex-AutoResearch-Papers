---
round: 15
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-18T01:55:38.568158+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 15 审稿报告 — simgate-modular-routing

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**目标 Venue**: ACL Rolling Review (ARR) → EMNLP 2026
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性）
**轮次**: Round 15（继续审稿）

---

## Summary

本文提出 episode-level counterfactual 分析框架，含 dual-metric 分解（penalty-independent label fraction + penalty-dependent DAF），用于诊断模块化 LLM agent 中 routing signal 的来源。在 ScienceWorld（11 task types, 245 episodes）上发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动。三类 agent improvement baseline（retry/Reflexion/72B scaling）均无法消除 death dominance。MATH negative control（N=795, p=0.81）和 ALFWorld cross-environment 对比验证了框架诊断能力。

---

## Strengths

1. **方法论贡献清晰可复用**：Episode-level counterfactual labeling（Algorithm 1）+ DAF 分解 + SCI 构成完整诊断工具包。dual-metric 设计（78.9% penalty-independent + DAF penalty-dependent）避免了 tautology 指控。[R1-S1, R2-S1]

2. **DAF tautology concern 彻底解决**（R13-N1 resolved）：78.9% 为 primary metric，DAF 显式降级为 derived quantity，r=0.97 标注为 mathematical consequence。[R1-S2]

3. **统计分析严谨诚实**：Bootstrap CI (B=10,000)、LOO correlation、cluster bootstrap K=11 caveat（Cameron 2008）、anti-cherry-picking analysis、Llama pilot 标为 "directional consistency"。r=0.97 自标为数学推论而非经验发现——在 agent 领域不常见的诚实度。[R1-S3, R2-S3]

4. **实验控制设计充分**：Retry/Reflexion/72B 三角证据支撑 non-triviality；MATH negative control 有力（排除 ≥3.6pp routing signal）；ALFWorld 诊断出 information asymmetry 作为替代机制。[R1-S5, R2-S2]

5. **负面结果价值高**：Router 训练定位为 "Diagnostic Probe"——episode-level 47.1±2.2% 低于 chance，data scaling 无改善，reinforcing "death dominance renders routing trivial"。[R2-S4]

6. **写作质量好**：零 AI dash 痕迹，-ing 尾句极少，黑名单用词未检出。Limitations 有三个结构化 paragraph headers。[R2-S5]

7. **引用覆盖充分**：39 条引用，0 orphan，含 4 篇 2026 concurrent work + 4 篇 Safe RL。[R1-S6, R2-S6]

---

## Weaknesses

### Must-Fix（3 个，影响接收决定）

**[W-MF1] "Structural" claim 推断基础不足** [R1-N1, R2-W3 共识]
- 论文声称 death dominance 是 "structural property of the environment"。支撑证据：三种干预（retry/Reflexion/72B）均无法消除。
- 问题：Retry 无信息量（tautological），有效干预仅两种（Reflexion + 72B）。ToT/MCTS/frontier model 等未测试。"Structural" 暗示环境内禀属性，但论据仅为归纳性的。
- R2 补充：Reflexion 和 72B 通过不同机制收敛到 ~35%，比同一机制重复更有证据力，但仍不足以支撑 "structural"。
- **共识修复方向**：(a) 将 "structural" 弱化为 "robust under the three tested interventions"；(b) Discussion 增加 state observability 的简要理论论证（internal strategy 无 ground-truth state → state estimation error → irreducible death risk）；(c) 列出未测试干预作为 open directions。

**[W-MF2] 跨环境模态定义不一致** [R1-N2, R2 agree]
- 三个环境的 "deterministic" 含义根本不同：ScienceWorld = ground-truth observations；ALFWorld = ground-truth obs + admissible actions；MATH = code interpreter。
- Table 5 并列比较暗示可比性但实际不完全可比。ALFWorld 给 det 策略额外的 action-space pruning 优势（ScienceWorld 中不存在）。
- **共识修复方向**：§3.5 开头或 Table 5 caption 明确标注三环境模态定义差异；论证框架价值在于诊断能力（识别不同 mechanism）而非结论的跨环境一致性。

**[W-MF3] Contribution 1 "any environment" generalizability claim 过宽** [R2-N1, R1 agree]
- Contribution 1 声称 "applies to any environment with controllable modality comparison and binary catastrophic outcomes"。
- "Binary catastrophic outcomes" 前提很强——web navigation, code generation, multi-turn dialogue 等实际部署环境多不满足。
- Appendix D 自己显示 DAF@P=0 仅 7.5%，death dominance 强依赖惩罚量级。
- **共识修复方向**：(a) Contribution 1 从 "any" 改为 "designed for"；(b) Discussion 增加 1 段讨论框架在无 binary death 环境中的退化（predicts null / collapses to standard A/B testing）。

### Should-Fix（5 个，影响评分但不一票否决）

**[W-SF1]** Cluster bootstrap K=11 未使用 "sensitivity analysis" 术语，且 [73.3%, 100%] CI 未与 primary CI [81.6%, 98.8%] 在主文同段落并列。两位 reviewer 独立提出同一修改。[R1-W1, R2-W4]

**[W-SF2]** §3.7 "Augmentation scaling provides no improvement" 易被误读为 "data scaling 无用"。Paraphrase augmentation 无法增加 minority-class diversity（仅 9 个 internal-preferred），应在主文明确此 confound。[R1-W2, R2-W2 共识]

**[W-SF3]** Oracle margin (2.89) 与 mislabeling (27.7%) 逻辑层级不清。应明确：oracle margin 是 fundamental bound（routing 本身价值有限），mislabeling 是 secondary confound。[R1-W3, R2 agree]

**[W-SF4]** 72B 缺完整 DAF decomposition。Llama pilot N=70 仅 directional consistency，72B 只有 death rate 没有 label fraction。如有数据为 72B 报告 DAF 会显著加强 cross-scale evidence。[R2-W5, R1 agree]

**[W-SF5]** Triviality risk 的直接回应不足。Prior assumption 引用的工作（Toolformer/ART/Chameleon）是非交互式 tool use，与多步交互环境设置不同。建议直接回应 obvious-in-hindsight：surprise 在于 δ 的量级（26.6pp）和三种干预的 irreducibility。[R2-W3, R1 partial agree]

### Minor（4 个，不影响接收）

- Abstract 数字密度偏高（~9 个数字，R2 建议 5-6；R1 认为可接受→降级 info）
- signal_reversal.pdf 可能为 orphan figure
- gajcin2023counterfactual 只列一位作者（可能是 doctoral consortium paper），应补全 venue
- RTX 5090 (32GB) 规格需确认

---

## Reviewer Consensus

| Issue | R1 | R2 | 共识 |
|-------|-----|-----|------|
| "Structural" → "robust" | N1 (critical) | W3 (warning) + agree | **AGREE**：弱化措辞 + 增加理论论证 |
| 跨环境模态不一致 | N2 (critical) | agree (N1 的具体实例) | **AGREE**：Table 5 标注差异 |
| Contribution 1 过宽 | agree | N1 (critical) | **AGREE**：收窄措辞 |
| Cluster bootstrap 标注 | W1 | W4 | **AGREE**：同段落并列两种 CI |
| Augmentation vs real-data | W2 | W2 | **AGREE**：明确区分 + minority-class caveat |
| Oracle margin 层级 | W3 | agree | **AGREE** |
| 72B DAF 缺失 | agree | W5 | **AGREE** |
| Abstract 数字密度 | minor (rebut) | W1 (warning) | **DIVERGE**：R1 可接受，R2 认为偏高。Director 降级为 info |

## Reviewer Divergence

- **Abstract 数字密度**：R1 认为当前 ~9 个数字对 EMNLP long paper 可接受（rebut），R2 认为应精简至 5-6（warning）。Director 判断：降级为 info/optional，不影响评分。
- **三角证据强度**：R1 认为 retry 无信息量且 Reflexion+72B 收敛可能是巧合；R2 rebut 认为两种不同机制收敛比同机制重复更有证据力。Director 判断：R2 的 rebut 有道理但不改变修复方向（仍应弱化 "structural"）。

---

## Questions（需作者澄清）

1. Algorithm 1 的 death-priority labeling 如果改为 pure score comparison，78.9% 中有多少 labels 保持不变？（R1 推算：降至 ~51%=21/41）
2. 72B chemistry-mix death rate +5pp 的具体解释？是否与 larger model 的 exploratory behavior 有关？
3. 0.5B 的非单调 death rate（低于 7B）是否意味着 death dominance 可通过极端 scaling 消除？
4. 78.9% penalty-independent label fraction 是否应在 §2.4 给出形式化定义？
5. tool-overuse-illusion 的 model uncertainty 解释与 death-avoidance 机制的关系——互补还是竞争？

---

## Missing References

**共识**（两位 reviewer 均 agree）：
1. Inner Monologue (Huang et al., 2022, CoRL) — internal reasoning + external feedback in embodied agents
2. ToolACE (Zhang et al., 2025, ICLR) — tool-use learning via synthetic data
3. Risk-sensitive RL / CVaR optimization (Tamar et al., 2015) — catastrophic tail risk
4. Permadeath 环境中的 LLM agent 工作（NetHack/Crafter + LLM）

**R2 仅建议**（R1 rebut，优先级较低）：
- TaskWeaver / CodeAct — code-as-action 框架（R1 认为关联较弱）
- SWE-bench / DevBench — 非交互式环境（R1 认为优先级低）

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

两位 Reviewer 在所有维度完全一致：

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Overall | 3.5 | 3.5 | **3.5 Borderline Conference** |
| Soundness | 4/5 | 4/5 | 4/5 |
| Excitement | 3/5 | 3/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**判断依据**：
- 方法论和统计分析 sound（Soundness 4.0）
- 核心发现的 novelty/excitement 受限于 (a) 单一 primary environment 和 (b) 发现在陈述后不令人意外（Excitement 3.0）
- 跨环境验证因模态定义异质性和框架适用条件限制而说服力有限
- 负面结果（router failure）的报告诚实有价值但不增加 excitement

**提升至 4.0 (Conference) 的条件**（两个条件需同时满足）：
1. 弱化 "structural" 为 "robust" + 增加 state observability 理论论证
2. 收窄 Contribution 1 generalizability claim + 标注跨环境模态定义差异 + 讨论框架在无 binary death 环境中的退化

**当前定位**：Solid Findings（3.0+），Borderline Conference（3.5）。如果 Must-Fix 得到充分回应，可达 Conference（4.0）。

---

## Detailed Comments（逐节摘要）

### Title & Abstract
- 标题准确限定 scope（"on ScienceWorld"）✓
- Abstract 以 78.9% 为核心数字，DAF 未出现 ✓
- 数字密度偏高（info级，不阻碍）

### Introduction
- 五段结构完整，贡献列表清晰
- Contribution 1 "any environment" 需收窄 [W-MF3]
- Prior assumption 来自非交互式 tool use，与多步交互设置有语境差距 [W-SF5]

### Method
- Algorithm 1 设计合理，DAF 数学推导正确
- DAF 降级处理到位（"derived quantity", "mathematical consequence"）
- SCI 放 Appendix 合理

### Experiments
- §4.1 Death decomposition: 核心数字清晰，54/75 reduce to ties 有力
- §4.2 Cross-model: Llama pilot 定位恰当，但 72B DAF 缺失 [W-SF4]
- §4.3 Agent improvement: Retry n=220 vs baseline n=245 差异未解释（minor）
- §4.4 MATH: McNemar 正确，negative control 有力
- §4.5 Cross-env: 模态定义差异需标注 [W-MF2]
- §4.6 Router: Diagnostic probe 定位好，但 oracle margin vs mislabeling 层级不清 [W-SF3]

### Related Work
- 5 段覆盖 5 方向，positioning 清晰
- 缺 Inner Monologue + risk-sensitive RL [R15-M1]

### Discussion
- "Non-triviality" 段三角论证有力但 "structural" 过强 [W-MF1]
- "Scaling predictions" 中 0.5B N=15 过 preliminary
- "Framework applicability" 列出 NetHack/Crafter 合理

### Limitations
- 三段结构完整，scope/method/stats 覆盖
- Mislabeling 27.7% 与 DAF 的关系可更明确

### Format
- ACL template [review] ✓, Anonymous ✓, 8 pages ✓, Limitations ✓, Ethics ✓, Checklist ✓

---

## R14 Issues 验证总结

| 类别 | Resolved | In Progress | 说明 |
|------|----------|-------------|------|
| R14 Critical | R13-N1, R13-N3 | — | DAF framing 和 scope 已彻底修复 |
| R14 Warning | R13-W2, R13-W6, R13-W7, R14-W2, R14-W3, R14-M1, R14-M2 | R13-N2, R13-W5, R14-W1, R14-M3, R13-m2 | 多数修复，少数部分改善 |
| New R15 | — | R15-N1, R15-N2, R15-N3, R15-W1~W3, R15-M1 | 3 critical + 5 warning + 1 info 新发现 |

**结论**：论文在 R13-R14 标记的核心问题（DAF tautology, scope, page length, router confounds）上有显著改善。R15 的新发现（structural claim, modality inconsistency, generalizability claim）是更高层面的 framing 问题，属于从 Findings 向 Conference 提升所需的精细打磨。