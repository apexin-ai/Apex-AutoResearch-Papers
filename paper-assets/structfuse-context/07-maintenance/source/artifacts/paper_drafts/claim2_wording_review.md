# Claim 2 Wording Review: "Exploratory Observation" Consistency Audit

**Date**: 2026-05-15
**Scope**: All paper_framing.md + paper draft .md files
**Reference decision**: D035 — Claim 2 降级为 "exploratory observation with testable prediction"

---

## Summary

Claim 2 的 **[Exploratory observation]** 标签仅在 2 处出现（paper_framing.md Claim 定义 + introduction contribution list），但 body text 中有 **11 处** 使用了与 exploratory 不兼容的断言性措辞（"reveals", "explains", "predicts", "shows that"）。Discussion §5.2 是最严重的区域——标题和正文均用预测性语言，暗示 n=2 观察已构成 validated mechanism。

Claim 1（strong, confirmed）与 Claim 2（exploratory）的区分在 contribution list 中清晰，但在正文中逐渐模糊，特别是 introduction 最后一段、related work §2.3、discussion §5.2。

---

## 逐处审查

### paper_framing.md

| 位置 | 当前措辞 | 强度 | 问题 |
|------|----------|------|------|
| Core Claims - Claim 2 | "[Exploratory observation]...This is reported as an observation with mechanistic hypothesis, not an established finding." | ✅ 合适 | 明确标记+caveat |
| Story Spine - contribution (2) | "observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and provide mechanistic analysis" | ⚠️ 偏强 | 缺 "exploratory" 标签；"provide mechanistic analysis" 暗示已完成验证 |
| Headline result template | "representation geometry analysis via negative difficulty provides mechanistic explanation for when different mining strategies are effective" | ⚠️ 偏强 | "provides mechanistic explanation" 对 n=2 过于断言 |
| Core Insight | "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry." | ❌ 过强 | 无任何 hedge，读为 general claim，无 n=2/exploratory 标记 |
| Dual-Pillar Motivation - Secondary | "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments" | ❌ 过强 | 从 n=2 观察直接推出 practitioner guidance，暗示 validated predictive power |
| Reviewer Concerns - "Only 2 encoders" | "n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law" | ✅ 合适 | 明确承认 |
| Contingency | "Pivot to 2-claim paper...Drop Claim 2 to analysis observation" | ✅ 合适 | 有降级准备 |

### introduction_v1.md

| 位置 | 当前措辞 | 强度 | 问题 |
|------|----------|------|------|
| Para 3 (intro body) | "analysis of negative difficulty margins reveals that the encoder's pretrained representation geometry...mediates which strategy is most effective, providing a mechanistic explanation for when and why" | ⚠️ 偏强 | "reveals" + "providing a mechanistic explanation" 无 exploratory hedge；与紧接其后的 Contribution 2 的 hedging 形成矛盾 |
| Contribution 2 | "[Exploratory observation] We report that...This is reported as an observation with mechanistic hypothesis, pending multi-seed confirmation." | ✅ 合适 | 完整 hedge：标签+caveat+pending 声明 |

**矛盾**：Para 3 用 "reveals...provides mechanistic explanation"，Contribution 2 紧接着说 "observation with mechanistic hypothesis"。读者会注意到措辞强度骤降。

### experiments_v1.md

| 位置 | 当前措辞 | 强度 | 问题 |
|------|----------|------|------|
| §4.1 Encoders | "This divergence enables us to study how representation geometry mediates the effectiveness of different negative mining strategies." | ⚠️ 偏强 | "mediates" 预设因果，应为 "may mediate" 或 "appears to mediate" |
| §4.3 Pilot (ii) | "the dataflow-aware strategy's effectiveness is encoder-dependent—beneficial for Qwen but neutral-to-negative for StarCoder" | ✅ 合适 | 限定在 pilot 结果描述 |
| §4.4 Mechanistic hypothesis title | "Mechanistic hypothesis" | ✅ 合适 | 标题正确标记为 hypothesis |
| §4.4 Mechanistic hypothesis body | "When the pretrained space is saturated, the encoder has limited room...Embedding-distance negatives provide a direct optimization target...Dataflow-aware negatives...may not align with the encoder's most informative gradient direction" | ⚠️ 偏强 | 前半段读为已确认的解释（"the encoder has limited room"），后半段用 "may not align" 有 hedge。整体偏 explanatory 而非 hypothesis |
| §4.4 Difficulty gradient | "The steeper relative compression for Qwen suggests that..." | ✅ 合适 | "suggests" 恰当 |

### discussion_v2.md (最严重)

| 位置 | 当前措辞 | 强度 | 问题 |
|------|----------|------|------|
| §5.2 标题 | "Representation Geometry as a Predictor of Strategy Effectiveness" | ❌ 过强 | "Predictor" 暗示 validated predictive power，n=2 不支持 |
| §5.2 首句 | "reveals a practical insight: the pretrained encoder's representation geometry predicts whether structure-grounded negatives will provide benefit" | ❌ 过强 | "reveals" + "predicts" 双重断言 |
| §5.2 Qwen 解释 | "This explains the +0.8pp R@1 improvement" | ❌ 过强 | "explains" 对 n=2 correlational 观察过于因果 |
| §5.2 practical implication | "This interaction...has a practical implication: practitioners can compute pos_sim..." | ⚠️ 偏强 | 从 n=2 直接给出 practitioner recipe |
| §5.2 threshold | "though we note this threshold is derived from two encoder observations and should be validated more broadly" | ✅ 合适 | 明确 n=2 caveat |
| §5.3 Limitations | "enabling our interaction analysis—generalizing...requires further investigation" | ✅ 合适 | 承认泛化限制 |
| §5.4 Future Work | "Our observation that pos_sim predicts strategy effectiveness suggests..." | ⚠️ 偏强 | "predicts" 仍过强，但 "observation...suggests" 结构有 hedge |

### related_work_v1.md

| 位置 | 当前措辞 | 强度 | 问题 |
|------|----------|------|------|
| §2.3 末段 | "show that the relative effectiveness of mining strategies depends on the encoder's pretrained representation geometry" | ❌ 过强 | "show that...depends on" 是 confirmed finding 的措辞 |

### method_v1.md

| 位置 | 当前措辞 | 强度 | 问题 |
|------|----------|------|------|
| §3.1 | "analyze how their effectiveness interacts with the encoder's pretrained representation geometry" | ✅ 合适 | 描述研究行为，不做 claim |

---

## 统计

| 强度 | 数量 | 位置 |
|------|------|------|
| ✅ 合适 | 11 | paper_framing (3), intro contrib (1), experiments (3), discussion (2), method (1), figure_design (1) |
| ⚠️ 偏强 | 7 | paper_framing (2), intro para3 (1), experiments (2), discussion (2) |
| ❌ 过强 | 5 | paper_framing Core Insight (1), paper_framing Dual-Pillar (1), discussion §5.2 (3) |

---

## 建议修改

### 必须修改 (❌ 过强)

**1. paper_framing.md - Core Insight**
- 现在: "The effectiveness of hard negative mining strategies depends on the encoder's representation geometry."
- 建议: "Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation."

**2. paper_framing.md - Dual-Pillar Secondary**
- 现在: "enabling practitioners to predict which strategy suits their encoder without exhaustive experiments"
- 建议: "offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments"

**3. discussion_v2.md - §5.2 标题**
- 现在: "Representation Geometry as a Predictor of Strategy Effectiveness"
- 建议: "Representation Geometry and Strategy Effectiveness: An Exploratory Analysis"

**4. discussion_v2.md - §5.2 首句**
- 现在: "reveals a practical insight: the pretrained encoder's representation geometry predicts whether..."
- 建议: "suggests a hypothesis worth further investigation: the pretrained encoder's representation geometry may predict whether..."

**5. discussion_v2.md - §5.2 "explains"**
- 现在: "This explains the +0.8pp R@1 improvement"
- 建议: "This is consistent with the +0.8pp R@1 improvement"

**6. related_work_v1.md - §2.3**
- 现在: "show that the relative effectiveness of mining strategies depends on"
- 建议: "observe that the relative effectiveness of mining strategies appears to depend on"

### 建议修改 (⚠️ 偏强)

**7. paper_framing.md - Story Spine contribution (2)**
- 添加 "[exploratory]" 标签: "(2) [exploratory] observe that..."

**8. introduction_v1.md - Para 3**
- "reveals" → "suggests"
- "providing a mechanistic explanation" → "providing a candidate mechanistic explanation (Section 4.4)"

**9. experiments_v1.md - §4.1 Encoders**
- "mediates" → "may mediate"

**10. experiments_v1.md - §4.4 Mechanistic hypothesis body**
- 首句添加: "Based on our two-encoder comparison, we hypothesize the following mechanism:"

**11. discussion_v2.md - §5.4 Future Work**
- "predicts" → "appears to correlate with"

---

## Claim 1 vs Claim 2 区分度

| 文档位置 | 区分清晰度 | 说明 |
|----------|-----------|------|
| paper_framing Contribution list | ✅ 清晰 | Claim 1 无标签 (strong), Claim 2 有 [Exploratory observation] |
| introduction Contribution list | ✅ 清晰 | 同上，且 Claim 2 有 pending 声明 |
| introduction body (Para 3) | ❌ 模糊 | "central finding" 引出 Claim 1 后直接 "we observe" 引出 Claim 2，无强度差异标记 |
| experiments body | ⚠️ 部分模糊 | pilot 段落区分合理，但 §4.4 mechanistic hypothesis 读为与 §4.3 main results 同等强度 |
| discussion | ❌ 模糊 | §5.2 标题和正文与 §5.1 (methodology) 同等断言强度 |
| related work | ❌ 模糊 | 两个 claim 在 §2.3 末段同一句中出现，用相同强度的 "show that" |

**建议**: Introduction Para 3 中 Claim 2 部分添加括号注: "(an exploratory finding; see Section 4.4)"。Discussion §5.2 开头添加一句: "We present the following analysis as an exploratory observation from two encoders, not a validated mechanism."

---

## 审稿人攻击角度与预备 Rebuttal

### 攻击 1: "n=2 不足以支持任何 interaction claim"
**预期措辞**: "The authors claim representation geometry mediates strategy effectiveness, but with only two encoders this is an anecdote, not evidence."
**Rebuttal 要点**:
- 承认 n=2 是核心限制，这正是我们标记为 exploratory observation 而非 confirmed finding 的原因
- 但两个编码器有 meaningful variation: 不同预训练语料、不同 representation geometry (pos_sim 0.986 vs 0.799)、不同预训练目标
- 我们提供 testable prediction: pos_sim > 0.98 时 structure-grounded negatives 更有效。这比纯 empirical 结果更有 scientific value
- 论文主要贡献是 Claim 1 (embedding mining suffices)，Claim 2 是 bonus insight

### 攻击 2: "Mechanistic explanation 是 post-hoc rationalization"
**预期措辞**: "The representation geometry analysis is descriptive, not causal. You cannot conclude that saturation causes strategy interaction."
**Rebuttal 要点**:
- 正确，neg_difficulty analysis 是描述性的 (cosine similarity statistics)，不是实验操控
- 我们明确标记为 "mechanistic hypothesis" 而非 "causal proof"
- 但描述性证据仍有 explanatory value: margin compression (77% Qwen vs 65% StarCoder) 与 pilot 结果方向一致
- 完整因果验证需要控制实验 (e.g., 人工缩放 pos_sim 后测试策略效果)，留待 future work

### 攻击 3: "Exploratory observation 不算 contribution"
**预期措辞**: "If Claim 2 is merely an observation, the paper has only one real contribution (Claim 1) plus a methodology contribution (Claim 3)."
**Rebuttal 要点**:
- EMNLP 有 strong tradition of empirical analysis papers where observations + hypotheses are valued (cf. "Do Language Models..." papers)
- Claim 2 包含 testable prediction (pos_sim threshold)，不是 vacuous observation
- Claim 1 (challenging gradient-based assumption) + Claim 3 (scalable pipeline) + Claim 2 (explanatory observation) 的组合足够
- 如果审稿人认为不够，可考虑升级 Claim 3 的呈现方式或添加 BM25 baseline 作为第四个贡献点

### 攻击 4: "Paper 内部不一致——abstract/intro 说 exploratory，但 discussion 说 predicts/explains"
**预期措辞**: "The paper's own framing is inconsistent — Section 5.2 uses assertive language that contradicts the [Exploratory observation] tag."
**Rebuttal 要点**:
- 这是本 review 发现的核心问题。如果不修改，审稿人会指出 self-contradiction。
- **在提交前必须修复 discussion §5.2 的措辞**，否则审稿人有理由认为作者试图 overclaim。
- 一致性是可信度的基础——hedging 要么全做要么不做，不能 contribution list 说 exploratory 但 body text 说 established。

### 攻击 5: "Dataflow 两个编码器都不如 embedding，interaction 在哪?"
**预期措辞**: "Both encoders show dataflow < embedding. Where is the interaction? The pattern is uniformly negative."
**Rebuttal 要点**:
- Interaction 不是 "dataflow sometimes wins"，而是 gap magnitude is encoder-dependent (Qwen -1.2pp vs StarCoder -1.0pp, 或 full M2 数据)
- neg_difficulty margin 差异 (+17% vs +28%) 与 gap 方向一致
- 更根本的 interaction 是 dataflow vs random: Qwen +0.8pp, StarCoder -0.5pp (pilot)——方向相反
- 但要诚实: 如果 full M2 显示两个编码器 dataflow vs random 都为负，interaction claim 进一步弱化

---

## 缺失的 Hedging 元素清单

当前 Claim 2 的 hedge 应在**每个出现位置**包含以下至少 2/4 项:

| 元素 | paper_framing Claim 2 | intro Contrib 2 | intro Para 3 | exp §4.4 | disc §5.2 | RW §2.3 |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| "exploratory" / "observation" 标签 | ✅ | ✅ | ❌ | ⚠️(title only) | ❌ | ❌ |
| n=2 limitation | ❌(pending区) | ❌ | ❌ | ❌ | ✅(末尾) | ❌ |
| encoder-dependent caveat | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| testable prediction 前向声明 | ❌ | ❌ | ❌ | ❌ | ⚠️(partial) | ❌ |

**最薄弱**: related_work §2.3（0/4 元素）、intro Para 3（1/4）、discussion §5.2 body（1/4，仅末尾 caveat）。
