---
round: 6
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-21T21:29:15.568926+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7 (Fresh Review)

**论文**: The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition
**Venue**: EMNLP 2026 (ARR), Long Paper
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量）
**审稿模式**: Fresh（初审）

---

## Summary

本文提出 Controlled Style Decomposition (CSD) 框架，通过 NLI-gated content control、per-axis style rewriting 和 position-controlled pairwise comparison 检测 LLM judge 的风格偏差。核心发现：(1) Likert Blindspot——Likert 评分系统性遗漏 pairwise comparison 检测到的风格偏差（BT 63–84% vs. Likert n.s.），moderate bias 下完全失灵（d→0 at n=355）；(2) GEE 条件分解揭示 per-axis confound 结构差异（verbosity: style-dominated, formality: conditional, register: judge-dependent）。实验覆盖 4 judge × 3 benchmark × 3 style axis。

---

## Strengths

1. **方法论设计精良**：CSD 三阶段流水线（rewriting → NLI gating → position-controlled comparison）逻辑清晰，DAG 因果语言校准上乘——§3.5 明确声明"interventional rather than formal causal evidence"，在同类论文中属罕见的诚实定位。
2. **统计分析层次丰富**：七种统计方法的 sensitivity hierarchy (Table 2) 系统展示了 Likert Blindspot 非特定检验的 artifact；100-point continuous Likert (Appendix M) 排除 scale granularity 解释。
3. **GEE per-axis confound structure 分解**：Table 3 的 regime classification（style-dominated / conditional / judge-dependent）是论文最具原创性的分析贡献，为后续研究提供可操作框架。
4. **NLI gate 多层验证**：11-threshold sweep、GPT-4o full-scale validation (200 decisions)、NLI-fail ablation (formality 反转至 41.7%)、direction-aware vs. bidirectional 对比——系统性 robustness 在同类工作中罕见。
5. **Cross-judge replication + negative control**：3 target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B) + Claude Sonnet 4 negative control 提供了有说服力的 discriminative validity。
6. **Blindspot severity spectrum 量化精细**：不仅证明存在，还刻画了效应量依赖性——moderate bias 完全失灵，stronger effects >60% 衰减——超出简单"Likert 不灵敏"结论。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. Evaluator-producer confound 控制不充分** [共识: R1-W1 = R2-W5, 双方交叉 AGREE]
- Qwen3-32B 同时担任所有实验的 rewriter。Cross-rewriter validation (Appendix D) 仅对 Qwen3-32B judge 做了 GPT-4o rewriter 替换（verbosity Style OR 降 22%: 13.10→10.17）。GPT-4o 和 Llama-70B 作为 judge 时从未用替代 rewriter 验证。22% 下降表明 evaluator-producer 效应 non-trivial，论文的 Contribution #3（cross-architecture consistency）可信度受损。Register 轴完全缺失 cross-rewriter test。
- **建议**: 至少对 GPT-4o judge 执行完整 cross-rewriter validation（用 GPT-4o 或 Llama 作 rewriter），证明 confound structure 在不同 rewriter 下一致。

**MF2. Section 4.1 与 Table 1 关于 register 分类的矛盾** [共识: R1-W2, R2 交叉 AGREE]
- Section 4.1 定义 primary family 为 8 tests（含 register），但 Table 1 将 register 标为 †_e (exploratory)。这直接影响 Holm-Bonferroni adjusted p-values（6-test vs 8-test family）。
- **建议**: 统一——建议将 register 从 primary family 移出（6-test family），因为 register 结果较弱且 evaluator-producer confound 最高。

**MF3. "The first framework" 声明过度** [共识: R2-W1, R1 交叉 AGREE]
- Abstract/Introduction 中"the first framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison"通过组合限定词构造唯一性。RATE、CASSE、FairJudge、Qiu et al. 各覆盖核心组件。
- **建议**: 改为"a unified framework"或"a framework that integrates"。

### Should-Fix（不阻塞接收但显著改善论文）

**SF1. Construct divergence 替代解释在框架层面未获同等权重** [分歧: R2 认为系统性弱化(Must-Fix), R1 REBUT 认为论文已在 §5.2/Abstract/Contribution#2 合理并列两种解释。Director 判定: Should-Fix]
- 论文标题 "Likert Blindspot" 和核心叙事框架倾向 measurement failure 解释。虽然 §5.2 讨论了 construct divergence，但标题和 Abstract 的第一印象偏颇。Tripathi et al. (2025) 发现 pairwise 更易被 distractor 操纵（flip rate 35% vs 9%），对 pairwise 作为 ground truth 的隐含假设构成挑战。
- **建议**: 在 Abstract 增加一句明确承认两种解释等权重；引用 Tripathi et al. 作为补充 evidence。

**SF2. TOST Δ=15pp 过宽** [共识: R1-W3, R2 交叉 AGREE]
- Claude Sonnet 4 的 TOST 在 Δ=10pp 下 underpowered (n=87)，在 Δ=15pp 下才 confirm equivalence。而 GPT-4o formality 确认偏差仅 +13pp (BT 63%)——与 equivalence zone 仅差 2pp。
- **建议**: 将语言从 "equivalence confirmed"/"no bias" 改为 "failed to detect bias; TOST provides an upper bound at Δ=15pp"。

**SF3. NLI FNR 估计存在循环性** [共识: R1-W4, R2 部分同意]
- 主要 FNR 8.4% 使用 Qwen3-32B annotator（与 rewriter 同模型）。GPT-4o cross-validation 存在但仅报告 precision，未报告 FNR。
- **建议**: 报告 GPT-4o validation 对应的 FNR，或将 8.4% 标注为"upper/lower bound"并提升 GPT-4o 验证为主要数据。

**SF4. Verbosity direction-aware NLI gate 17.4% FPR** [共识: R1-W5, R2 AGREE]
- GPT-4o validation 显示 verbosity pass precision 仅 82.6%（17.4% 通过 pairs 内容保存失败）。GEE Orig OR < 1 可部分吸收，但对 "blocking R→Q path" 的 content preservation claim 是实质性削弱。
- **建议**: 在正文 §5.1 报告此 FPR 数字并量化对 BT 估计的 potential bias。

**SF5. 全文零人工验证** [共识: R1-W6, R2 完全同意]
- 整个流水线完全依赖 LLM 系统（DeBERTa NLI + LLM rewriting/judging/validation）。在一篇关于 LLM judge bias 的论文中，完全用同类工具验证存在认识论循环。
- **建议**: 至少对 50 对 NLI gate decisions 做人工 annotation，报告 human-NLI agreement。如资源不足，在 Limitations 更明确标注此为关键局限（当前 Limitations 已部分覆盖但不够突出）。

**SF6. 基准多样性不足** [共识: R2-W3, R1 AGREE]
- 主要实验在 LLMBar (n=100) 上进行，cross-benchmark 验证仅覆盖少数配置（AlpacaEval 3/9, MT-Bench 2/9），全部英文单轮对话。n≤355 在绝对规模上有限。
- **建议**: 在 Conclusion 更明确标注 generalizability 边界条件。"Systematic"指方法论系统性而非数据规模系统性——需在措辞上区分。

**SF7. Abstract 信息密度过高** [共识: R1-detailed, R2-W4]
- 7 句中嵌入 4 组括号内统计数据（BT 范围, p-value, Cohen's d, n=355），首次阅读认知负担过重。
- **建议**: 将具体统计数字移至 Introduction，Abstract 聚焦定性结论和核心 message。

**SF8. 遗漏关键近期文献** [部分共识: R2-W6, R1 同意 Tripathi 和 Li 应引用]
- Tripathi et al. (2025) "Pairwise or Pointwise?" — pairwise 更易被 distractor 操纵，直接相关
- Li et al. (2026) "Grading Scale Impact on LLM-as-a-Judge" — 评分尺度影响，与 Likert Blindspot 讨论相关
- **建议**: 在 §5.2 Detection vs. amplification 段落引用 Tripathi et al. 与 Jeong et al. 并列；在 §2 或 §5.2 引用 Li et al.

### Minor

**M1. Cross-benchmark 选择性测试** [分歧: R1 认为 cherry-picking, R2 认为是覆盖面不足而非刻意选择]
- 仅在预期效应最强的配置做 replication。建议明确列出选择标准或标注 cross-benchmark 为 exploratory。

**M2. Table 1 第 6 列缺列标题** [共识: R1-R2]
- 包含 Blindspot/both sig./neither 标记的列无标题。建议添加 "Status" 或 "Finding"。

**M3. Appendix Table 5 (GEE CI) 7 个条目缺失 95% CI** [共识: R1-Q1, R2 AGREE]
- GPT-4o formality/verbosity/register 和 Qwen3 formality Orig OR 仅有点估计无 CI。必须补全。

---

## Reviewer Consensus [AGREE]

1. **Evaluator-producer confound 是核心不足**——两位 Reviewer 独立标注为最关键问题，交叉后双方 AGREE。22% Style OR 下降确认 inflation 存在，GPT-4o/Llama-70B judge 从未做 cross-rewriter validation。
2. **"First framework" overclaim 需修改**——改为 "a unified framework"。
3. **零人工验证是方法论缺陷**——在一篇关于 LLM judge 评估的论文中完全依赖 LLM 验证，存在循环论证风险。
4. **TOST 措辞过强**——"no bias" 应改为 "failed to detect bias"。
5. **Section 4.1 vs Table 1 register 分类矛盾**——直接影响多重比较校正的可信度。
6. **Abstract 过密**——需简化。

## Reviewer Divergence [REBUT]

1. **Construct divergence 的处理程度**: R2 认为论文框架系统性偏向 measurement failure（Must-Fix级别），R1 认为论文已在 §5.2、Abstract、Contribution #2 三处合理并列两种解释（Should-Fix即可）。**Director 判定**: Should-Fix——标题和核心叙事确有倾向性，但论文实质讨论已提供 balanced coverage。
2. **Thurstone (1927) 理论关系**: R2 认为核心发现可从近百年理论直接预测（novelty ceiling），R1 反驳称 severity spectrum、tie rate mechanism、per-axis interaction 是全新经验发现。**Director 判定**: 论文已在 Introduction 标注"predicted but unquantified"，Excitement 评分已内化此限制（3/5 和 3.5/5）。
3. **Cross-benchmark "selective testing" vs "coverage gap"**: R1 认为是选择性测试（cherry-picking），R2 认为是覆盖面不足但非刻意。**Director 判定**: 倾向 R2——实验覆盖确有限制但设计意图非 cherry-picking。

---

## Questions（需要作者回答）

1. GPT-4o 和 Llama-70B 作为 judge 时，是否有计划用非 Qwen3-32B rewriter 进行验证？如有，预期时间？
2. Section 4.1 的 primary family 是 6 还是 8 tests？register 的正式统计地位是什么？
3. 100-point continuous scale 的高 tie rate (51-66%) 是否支持 construct divergence 解释（judge 在 absolute mode 下对 style 确实不敏感）而非 measurement tool 缺陷？
4. Position-swap 后 43.9% inconsistency rate 为何未在正文讨论？是否影响 BT model reliability 判断？
5. NLI FNR 的 GPT-4o 对应数字是多少？是否可以替代 Qwen3-32B 自评估的 8.4%？
6. GEE confound structure 在不同 rewriter 下是否保持一致？是否有实验计划？

---

## Missing References

**两位 Reviewer 共识应补充：**
1. Tripathi et al. (2025). "Pairwise or Pointwise? Optimizing Evaluation Approaches for LLM-as-Judge." arXiv:2504.14716
2. Li et al. (2026). "Grading Scale Impact on LLM-as-a-Judge." arXiv:2601.03444

**单一 Reviewer 建议：**
3. Shankar et al. (2024). "Who Validates the Validators?" — LLM 评估验证循环性 [R1]
4. "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory." arXiv:2602.00521 [R2]
5. Huang et al. (2024). "Bias and Fairness in Large Language Models: A Survey" [R1]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态：error。** 视觉审查 Agent 因配额限制未能完成（"You've hit your limit · resets May 25, 8am UTC"）。无排版审查数据。用户可在配额重置后重新触发。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Overall | 3.5 | 3.5 | 3.5 |
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3.25/5 |
| Reproducibility | 3/5 | 4/5 | 3.5/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合评价**：

论文在方法论设计和统计分析上表现出色——七种方法的 sensitivity hierarchy、NLI gate 的多层验证、GEE per-axis confound structure 分解在同类论文中属于上乘水准。Likert Blindspot 的量化对 LLM evaluation 社区有直接实践价值。

但三个 Must-Fix 问题需要关注：(1) evaluator-producer confound 的不充分控制削弱了 cross-architecture replication 的可信度；(2) primary family 定义与 Table 1 标注的矛盾是方法论硬伤；(3) "first framework" overclaim 需要措辞修正。前两者中 MF1 涉及补充实验（可能需要额外计算资源），MF2 和 MF3 是纯文本修改。

核心 novelty 受限于经典 measurement theory 已有的理论预测（Thurstone 1927），论文的增量贡献在于 LLM judge 场景的具体量化——severity spectrum、per-axis interaction、tie rate mechanism。这足以支撑 Findings 级别接收，Conference 级别需要 MF1 的充分回应（cross-rewriter validation 覆盖至少 2/3 judges）和人工验证的补充。

**可行修改路径**：
- MF2 + MF3：纯文本修改，<1h
- SF1-SF8：文本调整 + 补充 2 篇引用，<2h
- MF1（cross-rewriter validation）：需额外实验，~4-8h GPU 时间
- SF5（人工验证）：需用户标注，~1-2 天
- M1-M3：排版修正，<30min

---

## Detailed Comments（逐节）

### Abstract
- "the first framework" → "a unified framework" [MF3]
- 4 组括号统计数据造成认知负担 → 保留 1-2 个核心数字，其余移至 Introduction [SF7]
- 两种解释的并列("measurement attenuation and construct divergence")处理得当

### Introduction
- Gap statement 合理但"per-instance diagnostics"requirement 在实验中体现不足——主要结果为 aggregate
- Figure 1 (pipeline diagram) 清晰展示 sample attrition，好的实验报告实践

### Related Work (§2)
- 覆盖全面，Jeong et al. (2025) 已引用
- 缺 Tripathi et al. (2025) 和 Li et al. (2026) [SF8]
- 对 RATE 的批判性分析可更 balanced

### Method (§3)
- §3.5 因果语言校准上乘 [S1]
- §3.2 已修改为 "filtering-based confounder control"，与 §3.5 hedging 一致
- Temperature 0.7 选择未 justify
- 各 axis pass rate 需在正文直接报告（目前需从 Table 1 footnote 间接推导）

### Experiments (§4)
- Section 4.1 primary family 定义需与 Table 1 统一 [MF2]
- Table 1 第 6 列需添加列标题 [M2]
- pre-registration vs post-hoc 分类值得肯定但未说明分类时点

### Analysis (§5)
- §5.1 NLI Gate Validation 最为 thorough；Gwet's AC1 vs κ 讨论专业
- §5.2 Likert vs Pairwise 的 dual interpretation 框架成熟；6 controls 回应 Comparative Trap 结构清晰
- §5.4 (Rewriter Independence) 覆盖面不足 [MF1]
- §5.6 (GEE) regime classification threshold 未明确定义

### Conclusion (§6)
- "should adopt pairwise" 措辞仍偏强，需加 amplification risk caveat
- Generalizability 边界需更明确

### Limitations
- 三个关键点覆盖合理
- 可增加：人工验证缺失的显式标注、register 轴 evaluator-producer risk 的更强措辞

### Format Compliance
- ✅ 主正文 ≤ 8 页
- ✅ Limitations section 存在
- ✅ 匿名 (Anonymous, review mode)
- ✅ natbib 引用格式
- ⚠️ Table 1 第 6 列缺列标题
- ⚠️ Appendix Table 5 缺 7 个 CI
