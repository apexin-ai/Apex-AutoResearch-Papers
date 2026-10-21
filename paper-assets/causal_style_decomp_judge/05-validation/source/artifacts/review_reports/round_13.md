---
round: 13
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T05:41:26.971124+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 15 审稿报告 — The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation

**目标 venue**: EMNLP 2026 (ARR May cycle)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验设计 + 统计方法；R2: 新颖性 + 完整性 + 写作质量 + 格式合规）
**审稿模式**: Fresh（无上轮记忆）
**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题收敛，无需第二轮）

---

## Summary

论文提出 Controlled Style Decomposition (CSD)，一种 black-box 诊断方法，用于检测 LLM judge 在 Likert 和 pairwise 两种评分模式下对 style 的敏感度差异（称为 "Likert Blindspot"）。方法包含三个组件：NLI-gated content control、per-axis style decomposition、position-controlled pairwise comparison。在 4 个 target judges（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash）+ 1 个 negative control（Claude Sonnet 4）、3 个 benchmarks（LLMBar, AlpacaEval, MT-Bench）、2 个 primary style axes（formality, verbosity）上，pairwise 检测到显著 style preference（BT 63-77%, p<0.001）而 Likert 未达显著（p>0.17）。GEE conditional decomposition 进一步揭示 per-axis confound structure：verbosity 为 style-dominated（Style OR 8-13），formality 为 conditional effect（Style OR 2-5, Orig OR 2-5）。

---

## Strengths

1. **统计处理深度罕见**：7 种统计方法互相验证（BT, sign test, Likert ATE, ordinal regression, GEE, Wilcoxon, Mann-Whitney），bootstrap CI 10,000 次 pair-level resamples，power analysis，bootstrap attenuation analysis，NLI threshold sweep——在 NLP 方法论论文中树立了高标准。[AGREE R1+R2]

2. **GEE conditional decomposition 有独立方法论贡献**：将 BT 整体偏好分解为 style 和 originality 两个分量，揭示 verbosity（style-dominated）和 formality（conditionally style-driven）的结构性差异。即使 n=88 的 CI 较宽，分析框架本身有独立价值。[AGREE R1+R2]

3. **Confounder control 策略周全**：NLI gate + position swap + same-style double-rewrite control + direction-aware gating for verbosity + 6 controls for amplification risk（直接回应 Comparative Trap, Jeong et al. 2025）。每层均有对应 validation。[AGREE R1+R2]

4. **Bootstrap attenuation analysis 巧妙**：d 收敛到 0 而非保持 non-zero，区分了 power limitation 和 measurement attenuation——是 Likert signal genuinely absent 的强证据。[AGREE R1+R2]

5. **Limitations 诚实全面**：四段覆盖 quality-style confounding、evaluator-producer bias、scope boundary、validation methodology，主动承认三种机制解释无法区分。[AGREE R1+R2]

6. **格式合规**：8 页正文，ACL 模板正确使用（`\usepackage[review]{acl}`），double-blind 匿名性无泄露，Limitations section 位置正确。[R2 确认]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 共识] **"Blindspot" 因果归因超出证据——Title/framing 偏向 Likert attenuation 解释，但三种机制未区分**

论文命名 "Likert Blindspot" 暗示 Likert 有缺陷（盲区），但 Section 5.1 自身列出三种 non-exclusive 解释（attenuation / amplification / construct divergence）且承认无法区分。若最终是 construct divergence，则两种模式测量不同构念，不存在 "盲区"——实践含义截然不同。更关键的是，pairwise > Likert 的判别力是 Thurstone (1927) 以来的已知现象；power analysis 显示 Likert 需 4-206× 样本量，完全一致于经典 format sensitivity 差异。论文需论证观察到的 divergence 为何不仅仅是已知的 format sensitivity 差异在 LLM judge 场景下的复现。

R2 补充：GEE per-axis decomposition 超越了 Thurstone 框架，是真正的增量贡献，但被 "Blindspot" framing 遮蔽。

**建议**：(1) 在 Introduction 中给 construct divergence 同等篇幅；(2) 明确讨论 Thurstone discriminability 与本文发现的关系；(3) 将 "Blindspot" 改为更中性术语或明确定义为操作性描述而非因果性声明。

> ⚠️ 此问题自 Round 1 以来已持续 15 轮。历经多次 framing 修改（'the first' → 'a unified framework'、'reveals' → 'demonstrates'/'identifies'），但标题中的 "Blindspot" 持续被两位 Reviewer 质疑。

---

**MF2** [critical, 共识] **Negative control (Claude Sonnet 4) TOST 在 Δ=10pp 时统计力严重不足（power≈42%）**

Claude Sonnet 4 作为 negative control 是实验设计的关键支柱——用于证明 Blindspot 是 judge-specific 而非 format-inherent。但 TOST 在 Δ=15pp (BT=65%) 才显著（p=0.010），而 GPT-4o formality BT=63% 已被论文视为显著 style preference——即等效界限几乎涵盖了论文自己认定为显著的效应量。Δ=10pp 时 TOST 不显著（p=0.156, power≈42%）。BT=56.2% 的 6.2pp 偏差在 n=88 下无法排除 moderate effect。

**建议**：(1) 扩大 negative control n 至 200+，使 Δ=10pp 的 TOST 达到合理 power；(2) 或将 negative control 结论降级为 "suggestive but underpowered"；(3) 增加第二个 negative control judge。

---

**MF3** [critical, 共识] **GEE decomposition 在 n=88 下 CI 极宽，regime classification 可靠性存疑**

Qwen3 verbosity Style OR=13.10 [5.62, 30.55]，95% CI 跨越近 6 倍。n=88→n=355 时 Qwen3 formality Style OR 从 4.20 降到 2.15（缩水 49%），提示其他 judge 的 OR 也可能被高估。交互效应检验 power 极低（OR 0.45-2.60 全 p>0.13），non-significant interaction 不等于 additive model 正确。GEE 是区分 style-dominated vs quality-confounded 的唯一工具；如果在 n=88 下估计不可靠，per-judge regime classification 的可信度受损。

**建议**：(1) 至少在 verbosity 轴做 n=355 级别 scaled replication；(2) 讨论 OR 缩水 49% 的含义；(3) 报告 GEE minimum detectable OR 或 power analysis。

---

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 共识] **仅 2 个表层风格轴无法支撑 "systematic pattern" 的通用性 claim**
Formality + verbosity 均属 surface-level stylistic attributes，register 为 exploratory pilot 且有 evaluator-producer overlap。Semantic-level axes 被 NLI gate 系统性拒绝。两个轴间存在结构性相关（FK grade d=0.50 cross-axis 泄漏）。Abstract/Title 的通用性措辞超出实验覆盖范围。
**建议**：明确限定为 "surface-level style axes"，或增加 1-2 个轴的 pilot evidence。

**SF2** [warning, 共识] **Human annotation 验证规模偏小（50 pairs, κ=0.44）**
A2 pass precision 下界仅 65.3%，worst case 下约 1/3 gate-passed pairs 可能含内容变化。GPT-4o cross-validation 是 LLM 验证非独立人工验证。
**建议**：扩大至 100+ pairs，覆盖所有 axis。

**SF3** [warning, 共识] **100-point continuous Likert scale 实验仅在 Qwen3-32B 上测试**
无法排除 judge-specific 效应。
**建议**：至少在 GPT-4o 上 replicate。

**SF4** [warning, 共识] **FK grade d=0.50 cross-axis contamination 处理不够严谨**
论文归因为 FK 依赖句子长度但未正式验证。
**建议**：做 length-controlled FK 分析。

**SF5** [warning, 共识] **Evaluator-producer overlap mitigation 仅测试一个替代 rewriter**
GPT-4o 替代 rewriter 显示 22% Style OR 降幅，仅此一个配置不足以确认趋势稳定。
**建议**：增加至少一个额外 rewriter。

**SF6** [warning, 共识] **Table 1 信息密度过高**
15 行结果 + 6 行脚注挤在一个表中，读者认知负担大。
**建议**：拆分为 LLMBar primary 和 cross-benchmark replication 两表。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享中达成 [AGREE]：

1. "Blindspot" 因果归因超出证据（R1-N1 ↔ R2-N2）：**强共识**
2. Style axis 覆盖窄限制通用性 claim（R1-W1 ↔ R2-N1）：**强共识**
3. Negative control TOST underpowered（R1-N2，R2 升级）：**强共识**
4. GEE n=88 可靠性（R1-N3，R2 AGREE）：**强共识**
5. Table 1 密度（R1-M1 ↔ R2-W1）：共识
6. 100-point Likert 单 judge（R1-W5 ↔ R2-M5）：共识
7. Human annotation 规模（R2-W4，R1 AGREE 并补充）：共识
8. FK grade cross-axis（R1-W2，R2 AGREE）：共识
9. Rewriter independence 单配置（R1-W3，R2 AGREE）：共识

## Reviewer Divergence

1. **RATE 增量贡献**（R2 Must-Fix vs R1 REBUT）：R2 认为与 RATE 的区分不够清晰，R1 认为 CSD 在方法论层面有结构性差异（pairwise mode, GEE, NLI gating），增量贡献已充分展示。**Director 判断**：R1 的 REBUT 论证更有说服力——CSD 与 RATE 的差异是结构性的而非增量性的（RATE 从设计上无法检测 mode divergence），但同意 "may underestimate" claim 需更谨慎措辞。降为 SF 级。

2. **IIA assumption 讨论**（R1 Should-Fix vs R2 REBUT）：R1 认为 IIA 讨论不充分，R2 认为在 controlled pairs 设计下 IIA 威胁有限。**Director 判断**：R2 的 REBUT 合理——CSD 的 pairwise 比较是 controlled pairs 而非 open tournament，IIA 威胁确实有限。建议在正文（而非脚注）简短讨论即可。降为 Minor。

3. **Design Rationale 位置**（R1 move earlier vs R2 current OK）：Minor 分歧，不影响评分。

---

## Questions

1. 是否考虑过用 human raters 收集少量 ground-truth style bias ratings（如 50-100 pairs），以部分区分 attenuation vs amplification？
2. 如果将 "Blindspot" 重新定义为 "Likert-Pairwise Divergence" 或类似中性术语，是否会改变论文的叙事结构？
3. n=88→n=355 时 Qwen3 Style OR 缩水 49% 的原因是什么？是否其他 judge 也预期有类似缩水？
4. Claude Sonnet 4 的 BT=56.2% 是否反映了一个真实但较弱的 formality preference？如果是，negative control 的叙事需要如何调整？

---

## Missing References

两位 Reviewer 未指出重大遗漏。Related Work 覆盖较为全面（Thurstone 1927, Stevens 1946, RATE, Comparative Trap, CASSE, FairJudge 等均已引用）。R2-M4 指出部分引用格式不一致（arXiv preprint 与正式发表版本混用），建议统一检查。

---

## External Review (Stanford Agentic Reviewer)

未配置，未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（8 项 info，0 critical，0 warning）。主要发现：
- Page 2: Figure 1 pipeline 图节点内文字偏小（约正文字号 60%），建议放大或改用 figure* 全宽
- Page 5: Figure 3 散点图尺寸偏小，filled vs open diamond 灰度打印区分度不足
- Page 6: Table 1 脚注字号很小，scaled replication 说明易被忽略
- Page 7: Figure 4 x 轴刻度标签偏小（~6pt）；Table 2 与 Figure 4 同页但排布合理
- Page 11: 单页 4 个表格，行间距偏紧
- Page 14: Table 14 脚注字号极小
- Page 19: References 末页 40% 空白（可接受）

无阻塞性排版问题。

---

## Overall Assessment

**评分：3.5 / 5 — Borderline Conference**（两位 Reviewer 独立一致）

**置信度：4 / 5**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

**总体判断**：这是一篇方法论扎实、统计处理深度罕见的诊断性工作。CSD 方法论（NLI gating + position-controlled pairwise + GEE decomposition）的设计严谨，robustness checks 全面，切中 RLHF/DPO 依赖 pairwise 而 evaluation 依赖 Likert 的实践痛点。

但三个核心弱点限制了贡献：(1) "Blindspot" 的因果归因超出实验证据（三种机制未区分，且 pairwise > Likert 判别力是 Thurstone 1927 已知现象）；(2) negative control 的 TOST 统计力不足，无法排除 Claude 有 moderate style bias，削弱了 "judge-specific not format-inherent" 的论点；(3) GEE decomposition 在 n=88 下精度不足（CI 跨 6 倍，OR 缩水 49%），per-judge regime classification 的可靠性存疑。此外，仅 2 个表层风格轴限制了通用性 claim。

**对 EMNLP 2026 的接收建议**：当前版本处于 Borderline Conference / strong Findings 水平。如果作者能解决 MF1（framing 中性化）和 MF2（negative control 扩样本或降级声明），论文有望达到 Conference 水平。MF3（GEE scaled replication）如果无法在 deadline 前完成，至少应在正文中讨论 OR 缩水现象和 CI 宽度对结论的影响。

---

## Detailed Comments

### Section 1 (Introduction)
- Opening example（GPT-4o 对 formal vs casual 答案的评分反转）生动有效，但未在 Limitations 中讨论这是否是 cherry-picked
- "systematically divergent style sensitivity"（Abstract line 1）建议改为 "systematically divergent style sensitivity on surface-level axes"
- Contributions list 中 "GEE conditional decomposition reveals qualitatively distinct per-axis confound structures" 应提升为第一贡献（R2-N1 共识：GEE 是真正增量贡献）

### Section 2 (Related Work)
- Thurstone (1927) 被引用但未讨论其与 power analysis（Figure 4）的关系——如果 4-206× 样本量差异可用经典 discriminability 差异解释，需明确论证 LLM judge 场景下的新发现是什么
- RATE head-to-head 比较（Section 5.1）虽然结构性论证充分，但 "RATE's own style-related findings may underestimate" 是推测而非验证过的结论，需更谨慎措辞

### Section 3 (Method)
- Section 3.1: Rewriting prompt 完整文本应在 Appendix 中给出（R1+R2 共识）
- Section 3.5 Design Rationale 位置合理（R2 REBUT R1 合理）

### Section 4 (Experiments)
- Table 1: 建议拆分为 primary + cross-benchmark 两表（R1+R2 共识）
- Table 2: "Orig OR" 首次出现时应展开解释
- IIA 讨论应从脚注移至正文，简短讨论即可（2-3 句）

### Section 5 (Analysis)
- Section 5.1: 给 construct divergence 解释同等篇幅
- Section 5.2 (GEE): 讨论 n=88→n=355 OR 缩水现象
- "style bias" vs "style sensitivity" 术语应统一

### Limitations
- 诚实全面，但第四段 100-point scale 实验的单 judge 限制应标注
- 考虑增加对 human ground-truth validation 作为 future work 的更 prominent 讨论

### Format
- 正文 8 页，合规
- ACL 模板正确，double-blind 无泄露
- References: 部分 arXiv preprint 与正式发表版本混用，建议统一
