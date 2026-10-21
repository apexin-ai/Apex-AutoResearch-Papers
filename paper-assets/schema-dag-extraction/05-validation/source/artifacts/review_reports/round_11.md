---
round: 11
overall_score: borderline
timestamp: 2026-05-17T09:13:40.463488+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 11 审稿报告 — schema-dag-extraction

**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**审稿人**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/写作/格式）
**日期**: 2026-05-17

---

## Summary

本文通过 Schema Confusability Score (SCS) 及其 batch 聚合 BCS，在 NER/RE/ED 四个数据集上将 zero-shot LLM IE 的 schema-induced degradation 分解为两个维度：count-related recall decline（主导）和 confusability-related type substitution（次要）。实验设计系统且 sensitivity analyses 充分，negative results（SDGD 失败）诚实报告并提供了 merge amplification 的机制性解释。但核心 confusability effect 极小（typical gap 仅 2.2pp），且仅在 RE 任务的 batch-level 上可靠——NER batch-level 方向相反，MAVEN 被 centrality confound 完全解释。

---

## Strengths

1. **实验设计系统且互补**：Count curves + BCS-controlled 两种范式构成合理的准实验策略；within-pool 控制有效隔离 pool composition confound。
2. **统计工具箱完整**：Bootstrap CI、permutation tests、TOST equivalence、cluster bootstrap、variance decomposition、partial correlation——选择得当且报告透明。
3. **负结果诚实且有诊断价值**：SDGD 失败的根因分析（merge amplification 导致 precision 崩塌；constrained decoding 消除 confidence signal）是对社区有直接价值的发现。
4. **Centrality confound 发现**：MAVEN per-type BCS 正相关是 centrality artifact 的分析是方法论贡献，对后续使用 embedding similarity 做 label analysis 的工作有直接 warning。
5. **多层次 sensitivity analyses**：四种 prompt variant、两种 embedding、SCS ablation、split-origin covariate、cross-seed variance decomposition——覆盖主要潜在 confound。
6. **Limitations 极其透明**：8 条 + multiple comparisons paragraph，难得的 disclosure 质量。
7. **DocRED 独立 replication**：96-type schema + document-level context 下 R²=0.53，增强 RE 结论外部效度。

---

## Weaknesses

### Critical（必须修复）

**C1. NER Dimension 2 batch-level 证据方向相反，但论文 title/abstract 泛化为 cross-task。**
[共识: R1 W3 Critical + R2 W4 Warning + 交叉强共识]

NER batch-level BCS–F1 correlation 为正（r = +0.50 v1, +0.58 v2），与 confusability hypothesis 预测方向**相反**。论文将其归因于 type-frequency confound 并依赖 pairwise r=0.112 作为 NER primary evidence，但：
- Batch-level 是实际部署相关的粒度——方向相反 = BCS 在 NER 上会给 wrong signal
- MAVEN 同样被 centrality confound 完全解释（partial r non-significant）
- Dimension 2 在 8B NER 上 attenuate to near-zero

**影响**：论文 title 含 "Information Extraction"（泛化），Contribution 3 虽加 caveat 但实质仅 RE 支持。需明确限定 Dimension 2 的 practical applicability 为 RE-specific。

**C2. 核心效应量过小，practical significance 存疑。**
[共识: R2 W1 Critical + R1 AGREE with nuance]

- Typical-batch gap: 2.2pp (CI [0.4, 4.0])——在部署中几乎不可察觉
- Pairwise r² = 1.3–1.7%——对实际系统设计指导极有限
- R²=22% 有科学价值（理解现象），但 absolute magnitude 不支撑 actionable design principle
- Extreme-batch gap 31.2pp 依赖人为极端化 BCS

**影响**：Analysis paper 的核心 finding 是 "confusability 可检测但在 typical conditions 下 negligible"，这一结论虽方法论严格，但 excitement/actionability 有限。

**C3. TOST ±3pp margin 相对于 main effect (2.2pp) 过于宽松。**
[共识: R1 W1 Critical + R2 AGREE]

- ±3pp = typical-batch main effect 的 136%
- ±1pp 时 equivalence inconclusive (p=0.278) = 无法排除 interaction 达 main effect ~50%
- "Bounded association" 声称的强度依赖 margin 选择

**建议**：以 ±2pp (p=0.047) 为 primary report；讨论 what-if interaction=1.5pp 的影响。

**C4. Pair-to-batch R² aggregation 叙事 framing 误导。**
[共识: R1 W2 Critical + R2 AGREE with nuance]

- Batch R²=0.218 是直接测量 (valid)
- 但 simulation 用 conditional R²=7%（非零 confusion pairs only）匹配 0.218，而 unconditional R²=1.3% 仅产生 0.044
- 论文 narrative 让 reader 记住 "22%" 而淡化 "1.3%" 的 unconditional reality

**建议**：明确区分 "R²=22% 是 batch-level 直接测量" 与 "pair-level 对 practitioners 实际可用的预测力仅 1.3%"。

### Warning（应该修复）

**W1. Title "Shape" 暗示因果性。**
[共识: R1 W4 + R2 AGREE]
Limitations 承认 "does not establish interventional causality"；建议改为 "Predict" 或保留问号但 Introduction 首段声明 study design 因果限制。

**W2. Abstract/Introduction 信息过载、叙事不清晰。**
[共识: R2 W2 Critical + R1 AGREE]
- Abstract: 数字密度过高（4-5 个具体值），BCS 未展开定义
- Introduction "五发现"：~100 词单句，5 个嵌套子句不可读
- Contribution list：每条 2-3 行含具体数字，像 result summary 而非 contribution statement

**W3. Discussion/Conclusion 过于简短。**
[共识: R2 W8 + R1 AGREE]
~15 行 Discussion + 3 行 Conclusion 对 analysis paper 不够。缺：practitioner recommendations、training-based IE 对比、BCS actionable conditions。

**W4. TOST 术语未展开。**
[共识: R2 W6 + R1 AGREE]
首次出现应写 "Two One-Sided Tests (TOST)"。

**W5. Prompt variant analysis (n=10) underpowered + 无 multiple comparison correction。**
[共识: R1 W8 + R2 AGREE with nuance]
Count 8 全部 n.s.；count 32 有 2/4 p<0.05 无 correction。

**W6. Supplementary 与 main appendix 重复。**
[R2 W5; R1 REBUT — 可能符合 ARR 规范]
需确认后决定。

**W7. Cross-model validation 仅两个开源模型。**
[共识: R1 W5 + R2 AGREE with qualification]
Discussion 应明确限定 model family scope。

---

## Reviewer Consensus

以下问题两人达成完全共识 [AGREE]：
1. NER batch-level BCS 方向为正 = Dimension 2 practical claim 仅 RE 支持
2. Typical gap 2.2pp 对 practitioners 不 actionable
3. TOST ±3pp margin 相对 main effect 过宽
4. Title "Shape" 超出因果证据边界
5. Abstract/Introduction 需要精简
6. Discussion 需要扩展
7. Contribution list 应改为方法论声明格式

## Reviewer Divergence

**Novelty bar（R1=3.5 vs R2=3.0 的主要来源）**：
- R2：核心 findings（count > confusability, r²<2%）somewhat expected + not actionable → Findings 更合适
- R1 [REBUT]：controlled experimental framework + centrality confound discovery + merge amplification diagnosis 是 non-trivial 方法论贡献；novelty 在 borderline
- **Director 判断**：R1 的 REBUT 有效——三个发现的组合（count dominates 20×, NER U-shape, merge amplification root cause）不是 trivially expected。但 R2 对 excitement 的质疑也成立：paper 未产出 actionable tool/method。

---

## Questions（需作者回答）

1. **NER frequency-residualized BCS**：是否尝试对 type frequency 做 partial correlation？如果 batch-level 仍为正/n.s.，Dimension 2 对 NER 的 practical claim 如何成立？
2. **Practical significance 论证**：在什么具体场景下（schema 类型、ontology 规模、应用领域），2.2pp typical gap 具有实际意义？
3. **TOST floor effect**：高 BCS batches 已接近 51% floor——interaction 是否在 logit scale 上计算？Floor effect 是否压缩了 apparent interaction magnitude？
4. **Seed SD=0.88pp at count 80**：Greedy decoding 下此 variance 来源？
5. **Unconditional → batch R² gap (0.044 vs 0.218)**：除 "active confusable pairs" 外，是否 BCS 与 type frequency dispersion 的 correlation 也贡献了 batch-level R²？

---

## Missing References

[两人共识]
1. Levy et al. (2024) "Same Task, More Tokens" — prompt-length confound 是 Dimension 1 的 alternative explanation
2. Dror et al. (2018) "The Hitchhiker's Guide to Testing Statistical Significance in NLP"
3. GenRES/ULTRA (2025) — recent schema-aware extraction

[R1 单独提出]
4. Zhao et al. (2021) "Calibrate Before Use" / Kadavath et al. (2022) — LLM calibration under constrained decoding

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 config 中无 `external_review.paperreview_ai.enabled` 设置）。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 4/5 | 3.75/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4.0/5 | 4.5/5 | 4.25/5 |
| Clarity | — | 3/5 | 3/5 |

**Overall Score: Borderline (3.25/5)**

- R1: 3.5 (Borderline Conference / strong Findings)
- R2: 3.0 (Borderline)
- Director 综合: **3.25 — Borderline，倾向 Findings track**

**核心判断**：方法论严谨的 analysis paper，统计工作 above-average（Soundness 高），但：
1. **Excitement 不足**：核心 confusability effect 过小（2.2pp typical）且仅 RE batch-level 支持；未产出 actionable tool/method
2. **Generalization overclaim**：title/abstract 暗示 cross-task 但 Dimension 2 仅 RE 可靠
3. **Writing gap**：Abstract/Introduction 信息过载降低 first impression；Discussion 过短

**接收条件（如果修复以下所有 critical issues 可能达到 weak accept）**：
1. 收窄 NER/ED generalization claims — Contribution 3 和 title 限定为 RE
2. 加强 Discussion — actionable recommendations + practical significance 论证
3. TOST margin 以 ±2pp 为 primary
4. Abstract/Intro 精简 + Contribution list 改写

**推荐 track**：
- 如不修改 → Findings (borderline reject from Main)
- 如完成上述 4 项修改 → Main Conference 下限可接受

**置信度**: 4/5（两位 Reviewer 在关键问题上达成共识，分歧限于价值判断）