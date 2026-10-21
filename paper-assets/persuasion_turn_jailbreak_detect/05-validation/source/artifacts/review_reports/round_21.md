---
round: 21
review_mode: continue
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T14:33:18.971413+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 21 审稿报告 — DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection

**Venue**: EMNLP 2026 (ARR May 2026)
**模式**: 继续审稿（基于 Round 20 评分 3.0 Findings）
**Reviewer**: R1（方法严谨性+实验设计）、R2（新颖性+写作+完整性）
**交叉分享**: 完成，无实质分歧

---

## Summary

本文提出 DisPeD，一个两阶段多轮越狱检测管线（Stage 1: DeBERTa encoder DAPT; Stage 2: frozen BiGRU），通过 7 个 Stage-1 变体的控制消融，分解跨攻击泛化的因素（域暴露、分类监督、标签粒度）。在合成数据上，classification DAPT 恢复 OOD 检测（F1=0.97-1.0 vs vanilla 0.26-0.31）；但在 ToxicChat 人类数据上层级反转（MLM 0.837 vs 9-class 0.596），且 mixed-LLM 训练下策略多样攻击降至 chance level（AA F1=0.504）。

---

## Strengths

1. **控制消融框架设计精良**：7 个 Stage-1 变体 + 6 个 cross-encoder 配置，每个变体严格隔离单一因素，实验设计严谨度在该领域少见。
2. **统计严谨性显著提升**：TOST 扩展至 n=10 seeds 确认 DD/FITD 等价性（p<10⁻⁸），同时诚实报告 ActorAttack 未通过等价检验（p=0.183, d=0.44）。所有方差声明改为 "descriptively" 限定。
3. **ToxicChat 反转作为核心发现呈现**：Abstract、Figure 3（新增面板）、Conclusion 三处一致将层级反转作为 complementary finding，而非 caveat。论文诚实承认 "condition-specific rather than universal"。
4. **Claim hedging 全面改善**：Mixed-LLM AA 标注 "chance level"，scale-dependent 在三处承认 "counterproductive at 355M"，所有 hierarchy 声明限定 "on synthetic data"。
5. **混杂因素透明披露**：Topic 变体三个混杂因素（类别数/域/intent head）在 method.tex 和 experiments.tex 明确承认，指向 Wiki-MLM vs JB-MLM 作为更干净的域效应隔离。
6. **页数合规**：主文 Sections 1-6 严格控制在 8 页内（Round 20 的 N1 critical issue 确认为 FALSE POSITIVE 后维持合规）。

---

## Weaknesses

### Should-Fix（2 项）

**W1. [R13-W1] 新颖性论证深度不足**（R1 AGREE, R2 首提；降级自 critical）
- Introduction 定位为 "the contribution is the decomposition, not the pipeline"，叙事一致。但缺乏关键论证：为什么 DAPT 消融在越狱检测场景中产生的 insight 对已读过 Gururangan et al. (2020) 的读者是 non-trivial 的。
- 具体缺失：classification DAPT vs MLM DAPT 在 OOD safety detection 上的巨大差距（60+ pp）、scrambled ≈ correct labels 的反直觉发现、以及层级在不同条件下的反转——这些发现在 prior DAPT 文献中未被报告，但论文未显式论证其 surprise value。
- **建议**：Introduction 中增加 1-2 句论证 why these findings are unexpected given prior DAPT literature。

**W2. [R14-N1] 数据规模扩大后性能反常下降未解释**（R1 首提, R2 AGREE）
- Appendix J (Table 14) 显示 500→1000 conversations 后，9-class DD OOD 从 0.994 降至 0.889（-10.5 pp），MLM 崩溃至 vanilla 水平。论文仅报告数字，未给出任何解释。
- 该现象与 mixed-LLM 下降有结构性相似（数据多样化→性能下降），但论文未将两者统一解释。
- **建议**：Appendix J 增加 1-2 句可能的解释（topic diversity dilution? distribution shift in new seed topics?）。

### Minor（7 项）

**M1. [R13-W7] Abstract 信息密度 borderline + 句法模糊**（R1+R2 共识）
- 词数逼近 200 上限（EMNLP 硬限制）。R2 指出 "this hierarchy reverses" 后长句修饰对象模糊。建议精简并拆分复杂句。

**M2. [R17-W1] TOST δ=5pp margin 无 justification**（R1+R2 共识）
- δ 值选择看起来 arbitrary。一句 practical significance 论证即可（如 "5pp is the minimum operationally meaningful difference for deployment"）。

**M3. [R13-W5] 跨架构比较混杂参数量差异**（R1+R2 共识）
- DeBERTa-v3-base (184M) vs RoBERTa-large (355M) 混杂架构和 scale。BERT-base proxy 提供部分跨架构证据。建议 Limitations 加一句。

**M4. [R9-M1] Llama Guard 3 1.8% 缺 "zero-shot" 限定词**（R1+R2 共识）
- Abstract 中仍无 "zero-shot" 限定，读者可能误解为 Llama Guard 3 经过 domain training 后仍只检测 1.8%。

**M5. [R16-W2] 24.3× speedup 缺参数量差异标注**（R2 首提，R1 REBUT 指出 Introduction 已有 43× 标注）
- Introduction 已标注 "parameter counts differ by 43×"，但 Abstract 未标注。R1 建议紧凑处理："24.3× speedup (43× fewer parameters)"。

**M6. [R17-M1] 三篇 potentially missing references**（R1+R2 共识）
- ADEPT, Echo Chamber Attack, Representation Bending 未引用。需确认是否有意省略。

**M7. [R15-VIS1] Figure 2 axis labels 偏小**（R1+R2 共识）
- Axis labels 约正文字号 55-65%，打印可接受但屏幕阅读偏小。

---

## Questions

1. Appendix J 的 dataset scaling 下降（9-class DD 0.994→0.889）是否有初步解释？新增 500 conversations 的 topic distribution 是否与原始 OOD 测试集重叠更少？
2. TOST δ=5pp 的选择依据是什么？是否做过 δ=3pp 或 δ=10pp 的 sensitivity analysis？
3. ADEPT、Echo Chamber Attack、Representation Bending 三篇论文未引用是有意省略还是遗漏？

---

## Missing References

- ADEPT（adaptive jailbreak attack）
- Echo Chamber Attack（multi-turn manipulation）
- Representation Bending（representation-level defense）

以上三篇需确认相关性后决定是否引用。

---

## External Review

**状态**: skipped（Round 20 请求，已跳过）

---

## Visual Layout Check（非评分项）

**状态**: done（0 critical, 1 warning, 7 info）

- **[warning] Page 8**: Discussion (~5行) + Conclusion (~8行) + Limitations 三个 section 挤在最后一页正文，给审稿人"收尾仓促"的印象。Discussion 部分尤其单薄。
- **[info] Page 1**: 首页无视觉锚点（全文字），Figure 1 在 p2 顶部，可接受。
- **[info] Page 5**: Figure 2 legend 和 axis label 字号偏小 (~7pt)，与 R1/R2 的 R15-VIS1 一致。
- **[info] Page 6**: Figure 3 与 Figure 2 风格一致，颜色语义连贯。
- **[info] Page 8**: Figure 4 CKA 热力图子图标签偏小，但色阶清晰。
- **[info] Page 14**: Figure 5 transition matrix 单元格内数字极小 (~5-6pt)，打印不可读（appendix 内，影响有限）。

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**

**从 Round 20 (3.0 Findings) 上调 0.5 分的依据**：

1. **9 个 Critical issues 全部 RESOLVED**（Round 20 的全部 Must-Fix 均已修复）
2. **统计严谨性显著提升**：TOST n=3→n=10，方差声明 descriptive hedging
3. **ToxicChat 反转呈现升级**：从 caveat 到 core finding
4. **Claim scope 全面收窄**：synthetic data 限定、condition-specific 承认、scale-dependent 披露
5. **混杂因素透明化**：Topic 变体三个混杂因素明确承认

**限制评分上升的因素**：

1. **新颖性论证不够显式**：controlled ablation 框架有价值，但论文未充分论证 why findings are surprising given prior DAPT literature
2. **外部有效性仍受限**：evidence hierarchy 仅在合成数据成立；WildChat FPR=68.1% 暴露 stylistic feature 学习；mixed-LLM 核心优势消失
3. **数据 scaling 下降未解释**：500→1000 后 9-class 也降 10.5 pp，质疑框架 scalability

**Reviewer 共识**：两位 Reviewer 独立给出 3.5，基于不同维度（R1: 实验设计/统计严谨性; R2: novelty/framing），无实质分歧。若 W1（novelty argumentation）和 W2（scaling explanation）修复，评分有 3.5→4.0 的提升空间。

---

## Detailed Comments

### Round 20→21 修复追踪

| Issue | Severity | R20 Status | R21 Status | 验证 |
|-------|----------|------------|------------|------|
| R9-W1 长度混淆 | critical | in_progress | **RESOLVED** | R1+R2 |
| R9-W2 ToxicChat反转 | critical | in_progress | **RESOLVED** | R1+R2 |
| R13-N1 合成数据scope | critical | in_progress | **RESOLVED** | R1 |
| R13-W4 Mixed-LLM hedging | critical | in_progress | **RESOLVED** | R1+R2 |
| R16-N1 Partition vs Topic | critical | in_progress | **RESOLVED** | R1 |
| R18-N1 Structural complexity | critical | in_progress | **RESOLVED** | R1 |
| R19-E1 Cohen's d数值 | critical | in_progress | **RESOLVED** | R1 |
| R20-N2 Topic混杂 | critical | in_progress | **RESOLVED** | R1+R2 |
| R20-N3 TOST n不一致 | critical | in_progress | **RESOLVED** | R1+R2 |
| R13-W1 新颖性 | critical→warning | in_progress | **STILL_OPEN** | R1+R2 降级 |
| R14-N1 Data scaling | warning | in_progress | **STILL_OPEN** | R1+R2 |

### 本轮新发现

| Issue | Severity | 说明 |
|-------|----------|------|
| R21-N1 | info | Abstract第二长句句法模糊 |

### Issue Tracker 统计

- 总 issues: 55
- 本轮 RESOLVED: 25
- 仍 open/in_progress: 10（2 should-fix + 7 minor + 1 stale in_progress）
- wont_fix: 1（R20-N1 页数合规 FALSE POSITIVE）