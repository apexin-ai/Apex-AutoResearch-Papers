---
round: 20
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T13:29:43.844631+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 20 (Fresh Review)

**论文**: DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewer 配置**: 2 人（R1: 方法严谨性 + 实验设计；R2: 新颖性 + 完整性 + 写作质量）
**圆桌轮次**: 1 轮独立审稿 + 1 轮交叉回应，关键问题已达成共识

---

## Summary

本文提出 DisPeD，一个两阶段多轮越狱检测流水线（Stage 1: DeBERTa encoder adaptation; Stage 2: frozen BiGRU classifier），核心贡献是系统消融框架：13 种编码器配置在 3 个规模（125M–355M）上分解 domain exposure、classification supervision、label granularity 对跨攻击泛化的贡献。主要发现为 domain exposure 是 OOD 泛化的首要因素，classification DAPT 优于 MLM 和 vanilla。该 hierarchy 在合成多轮数据上稳健，但在人类单轮数据（ToxicChat）上反转，在 mixed-LLM 场景下部分崩溃。

---

## Strengths

1. **实验控制设计系统性强**：7 个 Stage-1 变体沿多个轴（domain exposure, supervision type, label granularity）正交变化，共享同一 Stage-2 pipeline，是越狱检测领域控制最细致的消融研究之一。[AGREE R1+R2]
2. **诚实报告负面发现**：ToxicChat hierarchy 反转（JB-MLM 0.837 > 9-class 0.596）、WildChat FPR 68.1%、mean pooling ≈ BiGRU、mixed-LLM ActorAttack F1=0.504（chance level）等均如实呈现。[AGREE R1+R2]
3. **附录分析深度远超同类工作**：25+ 页附录覆盖 layer-wise analysis、SVD probe、random partition、frozen probing、cross-checkpoint variance 等，提供丰富的 mechanistic insight。[AGREE R1+R2]
4. **实用价值明确**：184M 参数编码器 + BiGRU 实现 24.3× 推理加速（vs LLM-as-judge），few-shot benign adaptation（10-shot）将 FPR 从 68.1% 降至 0%。[AGREE R1+R2]
5. **部分消融对比设计干净**：scrambled vs 9-class（隔离 label correctness）、Wiki MLM vs JB-MLM（隔离 domain exposure）控制得当，发现有指导价值。[AGREE R1+R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, AGREE R1+R2] **正文超过 8 页限制**
Sections 1–6（Introduction 到 Conclusion）占 9 页，超出 EMNLP 2026 正文 8 页限制 1 页。这是 ARR desk rejection 标准之一。R1 确认此为格式问题而非学术质量问题，技术上可通过压缩 Discussion 或将 Perturbation/Strategy Analysis 移至 Appendix 修复。

**MF2** [critical, AGREE R1+R2] **Evidence hierarchy 在 ToxicChat 上反转，核心 claim 外部有效性不足**
合成 OOD 上 9-class > MLM > vanilla，但 ToxicChat 上 JB-MLM（0.837）> 9-class（0.596），hierarchy 完全反转。R1 补充关键 nuance：domain exposure 本身仍成立（所有 DAPT 变体 > vanilla +40pp），反转的是 DAPT 类型间排序。两位共识：Abstract/Conclusion 中 "evidence hierarchy" 必须限定为 "on single-source synthetic multi-turn data"，ToxicChat 反转应作为同等重要的 finding 呈现而非 caveat。（对应历史 issue R9-W2，持续 12 轮仍 in_progress）

**MF3** [critical, AGREE R1+R2] **n=3 seeds 下 TOST 等价性检验统计效力严重不足**
每组仅 n=3 观测值（df≈4），TOST 功效极低。ActorAttack 上 TOST 全部未通过（p=0.407），无法区分"真不等价"与"检测力不足"。基于此得出 "label correctness is not a detection factor" 过于强。两位建议：增加至 ≥5-10 seeds，或降低 equivalence claims 强度为 "descriptive observation"，并报告 effect size（Cohen's d）。（对应历史 issue R15-SF6/R17-N1）

**MF4** [critical, AGREE R1+R2, nuance from R2] **Topic 变体控制设计存在未隔离混杂因素**
9-class vs Topic 对比同时变化 3 个因素：类别数（9 vs 5）、分类域（persuasion vs topic）、是否有 intent head。无法干净归因于 domain relevance。R2 补充重要 nuance：Wiki MLM vs JB-MLM 对比仍可干净隔离 domain exposure 效应，论文的 domain relevance claim 并非完全依赖有缺陷的 Topic 对比。建议：承认 Topic 混杂因素，将 domain relevance 论证重心移至 Wiki MLM vs JB-MLM。（本轮新发现 R20-N2）

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, AGREE R1+R2] **Mixed-LLM hedging 不足**：ActorAttack F1=0.504（≈chance level），Abstract/Conclusion 缺少明确 caveat。同时缺少 250 Qwen-only 控制组以拆解数据量与分布 shift 的混杂。（对应历史 issue R13-W4）

**SF2** [warning, R1 raised, R2 AGREE] **WildChat FPR 68.1% 分析不充分**：需分析 DAPT 是否学了 Qwen3-8B stylistic artifacts 而非 jailbreak features。（对应历史 issue R13-N2）

**SF3** [warning, AGREE R1+R2] **单一 Qwen3-8B 数据源偏差**：训练和 OOD 测试均来自 Qwen3-8B，模型可能利用 LLM-specific style bias。"OOD" 定义应明确为 attack-side OOD。（对应历史 issue R13-N1）

**SF4** [warning, R2-W4, R1 AGREE] **"Evidence hierarchy" 命名过于绝对**：仅在单源合成数据上稳定成立，应加范围限定词。（关联 MF2）

**SF5** [warning, R2-W2] **Abstract 词数接近 200 words 上限**：包含大量技术数字，建议精确计数确认。（对应历史 issue R13-W7）

**SF6** [warning, R1-W5, R2 AGREE] **Mean pooling ≈ BiGRU 讨论不足**：Appendix 显示差异 ≤1pp，但正文继续使用 BiGRU 作为默认配置未充分论证。更深层问题：temporal order 不重要与 "multi-turn structure matters" 的暗示叙事存在张力。（对应历史 issue R16-W1）

**SF7** [warning, R1-W4, R2 REBUT — 分歧] **缺乏与 DeepContext/BIID/G-Guard 直接对比**：BERT proxy ≠ 原系统。R2 认为 proxy 方案在无开源代码约束下合理，已做到 reasonable effort。（对应历史 issue R18-W1）

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致：
1. **[AGREE]** 正文超页必须修复（MF1）
2. **[AGREE]** ToxicChat hierarchy 反转是论文最大外部有效性威胁，claims 需限定范围（MF2）
3. **[AGREE]** n=3 seeds 下等价性统计推断过度，需降级或增加 seeds（MF3）
4. **[AGREE]** Topic 变体对比存在混杂（MF4，R2 补充 Wiki MLM vs JB-MLM 仍干净）
5. **[AGREE]** Mixed-LLM hedging 不足（SF1）
6. **[AGREE]** Evidence hierarchy 命名需限定（SF4）
7. **[AGREE]** Mean pooling ≈ BiGRU 的 implication 讨论不足（SF6）
8. **[AGREE]** 论文定位在 3.0–3.5 区间（Findings 至 Borderline Conference）

---

## Reviewer Divergence

**D1 — 新颖性评估 [R2 critical vs R1 REBUT]**
R2（N3）认为消融框架与 Gururangan 2020 DAPT 高度重叠，核心发现（domain-relevant pretraining > generic pretraining）在 NLP 迁移学习文献中已是常识，新颖性不足以支撑主会议。R1 反驳：(1) scrambled ≈ correct labels 说明 label semantics 不重要，这在迁移学习文献中非显然；(2) classification > MLM 的条件依赖性超越 Gururangan 2020；(3) hierarchy 的条件依赖性本身是新发现；(4) 7 变体正交分解框架可迁移至其他安全任务。分歧未解决。

**D2 — Related Work 遗漏 [R2-W1 vs R1 REBUT]**
R2 指出遗漏 JBShield、SafeInt、Jailbreak Antidote。R1 确认 JBShield 已在 Section 2 page 3 被引用（`\citep{zhang2025jbshield}`），R2 指控部分不成立。SafeInt 和 Jailbreak Antidote 待确认。

**D3 — Baseline 对比 [R1-W4 vs R2 REBUT]**
R1 认为缺乏与 DeepContext/BIID/G-Guard 直接对比是局限。R2 认为论文已解释无公开代码和兼容评估协议，BERT proxy 是 reasonable effort。

---

## Questions

1. Scrambled 若去掉 intent head，OOD 性能是否显著变化？（R1-Q1，可隔离 intent supervision 的作用）
2. ToxicChat 上 9-class 的额外 false negatives 集中在哪些对话类型？（R1-Q2，理解 hierarchy 反转机制）
3. 能否提供 data scaling learning curve（100/200/350/500/1000）？（R1-Q3，已有 Appendix R 部分数据）
4. Few-shot adaptation 是否尝试过仅调 threshold 不改权重？（R1-Q4，低成本但有实用价值的 baseline）

---

## Missing References

- **SafeInt** (2025). Shielding Large Language Models from Jailbreak Attacks via Safety-Aware Representation Intervention. arXiv:2502.15594. — 与 DisPeD 的 representation-level 检测直接相关。
- **Jailbreak Antidote** (2024). Runtime Safety-Utility Balance via Sparse Representation Adjustment. arXiv:2410.02298.
- 注：R2 指出遗漏 JBShield，但 R1 确认 JBShield (Zhang et al., 2025) 已在 Section 2 被引用。

---

## External Review (Stanford Agentic Reviewer)

**状态：未返回**（requested at 2026-05-23T13:10:50Z，仍处于 pending 状态）。外部审稿结果到达后将补充。

---

## Visual Layout Check（非评分项）

**状态：超时**（Agent 在 300s 后超时）。未产生有效排版检查结果。用户可选择重新触发视觉审查。

---

## Overall Assessment

**Overall**: 3.0 — Findings（可被 Findings 接收）

**Reviewer 评分**：R1 = 3.5（Borderline Conference），R2 = 3.0（Findings）

**综合评分依据**：

这是一篇执行质量较高的系统消融研究，在越狱检测领域提供了有价值的 empirical insight。实验设计在合成数据内部有效性强，附录分析深度远超同类工作。

限制主会议竞争力的核心因素：

1. **外部有效性不足**：evidence hierarchy 在唯一真实数据集（ToxicChat）上反转，在 mixed-LLM 场景下部分崩溃（ActorAttack F1=0.504），核心结论仅在单源合成数据上稳定成立。这是持续 12 轮（R9-R20）的核心问题。
2. **统计推断过度**：n=3 seeds 下的 TOST 等价性检验效力不足以支撑 "label correctness is not a factor" 等断言性结论。
3. **新颖性争议**（Reviewer 分歧）：消融框架与 Gururangan 2020 DAPT 的区分度，R1 认为条件依赖性发现构成新颖贡献，R2 认为核心发现在迁移学习语境下非新知。
4. **格式违规**：正文 9 页超出 8 页限制，有 desk rejection 风险（技术可修复）。

**Findings 推荐理由**：实验设计严谨、负面发现诚实呈现、附录详尽，对社区有实证参考价值。若修复超页、限定 claim 范围、增加 seeds（≥5）验证关键等价性结论，可进一步竞争 Borderline Conference（3.5）。

**置信度**: 4/5（两位 Reviewer 均仔细阅读全文及附录，在关键问题上达成共识）

---

## Detailed Comments

### Section-by-Section

**Abstract**: 包含 ToxicChat 反转和 mixed-LLM 限制的诚实陈述，但 "evidence hierarchy" 未加范围限定。词数可能接近 200 上限，建议精确计数。"benefits substantially from domain adaptation at base model scale" 措辞已修正为条件性表述。

**Introduction**: 清晰陈述研究问题和方法论。"the first, to our knowledge, such controlled factorial study" 措辞恰当。贡献列表中 C1 claim scope 需与 ToxicChat 反转保持一致。

**Related Work**: 覆盖面广（multi-turn attacks, defenses, computational persuasion, DAPT）。JBShield 已被引用。建议补充 SafeInt 和 Jailbreak Antidote 作为 representation-level intervention 的对比。

**Method**: 7 变体设计整体清晰。Topic 变体与 9-class 对比存在 3 因素混杂（类别数、分类域、intent head），建议在文中承认此局限并将 domain relevance 论证重心移至 Wiki MLM vs JB-MLM。

**Experiments**: 分析深入。Table 2/3 的 evidence hierarchy 呈现应加范围限定。Section 4.3 中 "label correctness is descriptively non-factors" 应降级为 "descriptive observation at n=3"。Section 4.4 Mean pooling ≈ BiGRU 的 implication（temporal order 不重要）应在 Discussion 中深入讨论。Section 4.5 Mixed-LLM 需明确标注 ActorAttack F1=0.504 ≈ chance level 并加 hedging。

**Discussion**: 包含 discriminative compression、ToxicChat 反转、length confound 的讨论。建议增加：(1) temporal modeling 冗余对 multi-turn defense 研究方向的启示；(2) Topic 混杂因素的承认；(3) DAPT 可能学习 stylistic artifacts 而非 jailbreak features 的替代解释。

**Conclusion**: 需压缩至 8 页内。

**Limitations**: 覆盖 3 个核心局限（synthetic data, IID benign, scope），篇幅适当。

**Appendix**: 极为详尽（25+ sections），是论文的重要资产。部分结论（mean pooling ≈ BiGRU, frozen probing verification）值得在主文中更充分讨论。