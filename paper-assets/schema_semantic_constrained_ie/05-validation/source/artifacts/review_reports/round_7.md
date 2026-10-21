---
round: 7
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-18T13:08:45.889208+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告 — OntoCoDec: Type-Constrained IE via Compiled Ontology Constraints

**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿编排**: 2 名 Reviewer（R1: 方法/实验严谨性; R2: 新颖性/写作/格式）
**交叉验证**: 完成（双向 [AGREE]/[REBUT] 回应）

---

## Summary

OntoCoDec 将 IE 本体模式编译为两层可组合的 token 级解码约束：grammar 层（XGrammar CFG）保证 JSON 结构有效性和实体/关系词汇成员资格，semantic 层通过有状态实体注册表和动态 logit masking 保证逐三元组 domain/range 类型合规。在 3 个 7-8B 模型（Qwen3-8B, Llama-3.1-8B, Mistral-7B）和 3 个数据集（SciERC 7 关系, DocRED 96 关系, WikiEvents 56 事件类型）上验证，DR 违规降低 42-99%，F1 无显著损失。与 LoRA 组合后 DR≤0.20%。论文同时报告了 CF↔DR 权衡和 dual-factor 残差模式的描述性分析。

相对 Round 5，论文在多个关键问题上有实质性改进（R² 移除、缩写展开、em-dash 清理、post-hoc 平衡、reproducibility 补充），但引入了一个新的 must-fix 问题：Abstract/§1 的 "zero violations" claim 基于单一配置。

---

## Strengths

**S1** [共识] **实验设计全面且覆盖面广**：3 模型 × 3 数据集（含跨任务 RE→EE 泛化）、multi-ablation（grammar-only / semantic-only / full / S1 vs S2）、fine-tuning composability 验证、runtime 分析、sampling/beam search 兼容性、post-hoc filtering 完整对比。数据一致性好，Abstract/§5/Appendix 数字交叉核查无不匹配。

**S2** [共识] **方法形式化严谨**：pair-based sequential masking 的必要性有定量支撑（independent enforcement over-permits 33-37% spurious type pairs），non-rectangularity 分析为设计选择提供了定量基础（SciERC 0/7, DocRED 23/96 rectangular），decidability taxonomy（local / prefix-decidable / non-local）清晰分类约束可执行性。

**S3** [共识] **诚实的局限性与权衡**：CF↔DR trade-off 在 Abstract 和正文均有显式报告（ZS 下 CF 可达 12%，FT 下 ≤1.2%），Mistral 明确定位为 boundary condition，parse failure 的 denominator 处理有说明，dual-factor 限定为 "descriptive characterization"。相比 Round 5，Abstract 已纳入 CF caveat，§1 已平衡 post-hoc framing。

**S4** [共识] **Runtime overhead 极低**：Full S1 在 DocRED 96 关系上仅 +5.4%，FT regime 下 +2.3%，增强了实际部署可行性。

**S5** [共识] **Reproducibility 改善显著**：exp_id 追溯体系、完整 prompt templates（Appendix A）、greedy 实验确定性。Appendix 新增完整 LoRA 超参数（rank=16, alpha=32, dropout=0.05, target layers）、training 配置（AdamW, LR=2e-4, cosine, batch=16, bf16, 3 epochs）和 GPU 信息（RTX PRO 6000 Blackwell 98GB）。较 Round 5 有实质性提升。

**S6** [共识] **跨任务泛化验证有力**：WikiEvents 事件抽取（56 事件类型，80 角色）无架构修改即可适用，消除词汇违规（→0%），格式合规 additionally 启用实体抽取（Entity F1: 0%→12-18%）。框架的任务无关性是核心卖点的有力支撑。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**MF1** [critical, 共识, 🆕] **Abstract/§1 "zero violations" claim 仅基于 Qwen/SciERC 单一配置，构成泛化性 overclaim**

Abstract 第 13 行声称："With beam search (k=4), the full stack (LoRA + OntoCoDec + beam) achieves zero constraint violations across all four categories while preserving extraction quality"。§1 Contribution #3 第 32 行重复此 claim。

**问题**：
- appendix_beam_search.tex:94-95 明确证实此结果仅来自 **Qwen3-8B + SciERC + LoRA + beam k=4** 单一配置
- 无 Llama/Mistral 的 beam+LoRA 结果验证
- DocRED beam 仅 50 docs subset（非 998 全集），且 parse failure 增加至 6%
- SciERC（7 relations, κ=0.333）的松约束条件下实现 zero violations 不代表在 DocRED（96 relations, κ=0.842）上可复现
- Abstract 呈现方式使读者误以为 "zero violations" 是框架的通用属性

**建议**：(1) Abstract 将 "zero violations" 限定为 "on SciERC with Qwen3-8B" 或替换为 "near-zero violations across configurations"；(2) §1 Contribution #3 添加配置限定；(3) 若有时间，补充 Llama SciERC beam+LoRA 结果验证泛化性。

---

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 共识, 携带自 R5] **Beam search 结果仍主要在 Appendix**
- §1 Contribution #3 现已提及 beam（较 R5 有改善），但 §5 主实验部分无 beam 讨论
- Beam k=4 在 SciERC 全集 551 docs 上 DR=0%、CF=0.53%，同时解决主实验两大局限（DR 残差 + CF 爆炸），却仅在 Appendix 呈现
- **建议**：§5 末尾或 §7 添加 1-2 段 beam search 正文讨论，至少报告 SciERC 全集 beam 关键结果

**SF2** [warning, 共识, 携带自 R5, 改善] **-ing 分词短语仍可辨识**
- 从 R5 的 ~10 处减少至 ~7-8 处，但仍构成可辨识的 AI 写作模式
- Abstract: "suggesting that constraint effectiveness is predictable" (line 11), "confirming near-lossless composability" (line 12)
- §1: "enabling the semantic layer to look up domain/range rules" (line 22), "showing that violation rates are driven by" (line 28)
- §5: "confirming the enabling dependency" (scierc:92), "confirming orthogonal composability" (scierc:119), "confirming layer complementarity" (wiki:59)
- 密度降低但 "confirming..." 重复 4 次尤为突出
- **建议**：将 Abstract 和 §1 中的 -ing 结尾改写为独立句。特别是 4 处 "confirming" 应使用不同句式。

**SF3** [info→warning, 共识, 携带自 R5] **DocRED 有效 semantic constraint coverage 未显式报告**
- SciERC 在 Appendix 报告 63.4% effective coverage
- §5 DocRED 提到 "fallback rate (10.2%) closely tracking residual DR" 并引用 Appendix，但未给出显式 coverage 数字
- 读者无法直接判断 DocRED 约束的实际生效范围
- **建议**：在 §5 DocRED 段落或 Appendix 表格中报告 DocRED effective semantic constraint coverage

---

### Minor Issues（不影响接收）

**M1** [info, 共识, 降级自 SF5] **Llama DocRED parse failure confounding**
- Llama DocRED parse failure +34%（68→91），E-F1 impact -0.64pp
- R2 建议降级为 info：效应量过小（-0.64pp），confounding 方向单一（约束总是增加 parse failure，方向已知），不影响核心 DR 结论
- R1 接受降级

**M2** [info, 共识] **§1 Contribution #3 信息密度过高**
- 单条 Contribution 包含 5 个子结果（3 datasets DR, composability, CF trade-off, beam search），阅读负担大
- 建议拆分为 2-3 条或精简

**M3** [info, R1] **dual-factor pattern 在 §4 的呈现仍较 prominent**
- §4 虽未报告 R² 具体值，但 "dual-factor pattern (tightness × baseline model violation rate)" 仍作为独立段落呈现
- n=4 的 sample size limitation 在 §4 未提及（仅 Appendix 有 caveat）
- 对接收不构成障碍，但审稿人可能质疑

---

## Round 5 Issues Resolution（7/9 已修复 issues 验证）

| Issue (Round 5) | Round 6 Status | 验证依据 |
|-----------------|---------------|---------|
| MF1: R²=0.886 in Abstract | ✅ **Resolved** | Abstract line 11 改为 qualitative "residual DR correlates with..." |
| MF2: Abstract 缩写未展开 | ✅ **Resolved** | LLM/IE/DR/CF/LoRA 均已展开，CFG 改为描述文字 |
| SF2: Em-dash 过度使用 | ✅ **Resolved** | 主文件无内容 em-dash，仅表格占位符 --- |
| SF4: Code-gen §1 缺失 | ✅ **Resolved** | §1 line 23 + Contribution #2 显式区分 |
| SF6: Post-hoc framing 选择性 | ✅ **Resolved** | §1 line 14 承认 post-hoc F1 优势 |
| SF8: Reproducibility 不足 | ✅ **Resolved** | appendix_reproducibility.tex 完整 LoRA/training/GPU 详情 |
| SF9: §4 DR 范围不一致 | ✅ **Resolved** | §4 line 28 显式区分 "calibrated models" vs "full range" |
| SF1: Beam search in appendix | ⚠️ **Partially** | §1 提及但 §5 仍无讨论 |
| SF3: -ing 模式 | ⚠️ **Improved** | ~10→~7-8 处，但 Abstract/§1 仍有 |
| SF5: Parse failure | ⬇️ **Downgraded** | 共识降为 info（效应量过小） |
| SF7: DocRED fallback coverage | ⚠️ **Partially** | 提到 fallback rate 但无 explicit coverage |

**总结**: Round 5 的 2 个 critical must-fix 均已修复。9 个 should-fix 中 5 个完全修复，2 个部分修复，1 个降级，1 个仍在。同时引入 1 个新 critical issue（N1/MF1: "zero violations" overclaim）。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：
1. "Zero violations" claim 必须限定配置范围（MF1）
2. Beam search 应在 §5 正文讨论（SF1）
3. -ing 模式需进一步清理，特别是 "confirming" 重复（SF2）
4. DocRED fallback coverage 应显式报告（SF3）
5. Parse failure 降级为 info（M1）
6. 整体评分 3.5（Borderline Conference）

## Reviewer Divergence

**无重大分歧**。R2 在唯一一个争议点（SF5/parse failure 严重性）提出降级建议，R1 接受。其余所有 findings 双方达成 [AGREE]。这是 6 轮审稿以来共识度最高的一轮。

---

## Questions to Authors

**Q1** [共识] LoRA+beam "zero violations" 是否在 Llama SciERC 上也能复现？若能，claim 的泛化性大幅增强。若不能，需在 Abstract 中限定。

**Q2** [共识] DocRED beam search 仅用 50 docs subset，且 parse failure 增至 6%。是否有计划在更大 subset 上验证？parse failure 增加是否因 beam 生成更长序列导致 max-token 截断？

**Q3** [R1] §4 "dual-factor pattern" 段落呈现较 prominent，但 n=4 limitation 在 §4 未标注。审稿人是否会将此视为隐性 overclaim？

---

## Missing References

无新增缺失引用。Round 5 标记的引用问题（DORE/GenIE/EnriCo 已在 §6 主文本，BoostCD 已提及，GLiNER 为可选）维持原判。

---

## External Review

外部审稿：未配置（项目配置中 `external_review.paperreview_ai.enabled` 未启用）。

---

## Overall Assessment

**评分**: **3.5 — Borderline Conference**
**EMNLP 2026 ARR 评分制**: 3.5 = Borderline Conference（可被主会议接收的边界）
**置信度**: 4/5

**理由**：

论文在技术执行和实验覆盖面上达到会议水准。Round 5 的两个 critical issues（R² overclaim、Abstract 缩写）均已修复，7/9 should-fix 完全或实质性解决。方法贡献（将 IE 本体约束编译为可组合的 stateful token-level masking）有清晰技术价值，pair-based sequential masking 的正确性论证充分，跨任务泛化（RE→EE）增强了框架的通用性声明。

**从 Round 5 Weak Accept 调整至 Borderline Conference 的原因**：

1. 论文改进方向正确且执行到位，大量 Round 5 issues 被系统性修复
2. 新引入的 MF1（"zero violations" overclaim）虽为 critical，但修复成本低（限定配置范围即可）
3. 核心 excitement 仍有限。本质贡献是将 type-constrained decoding 从 code-gen 迁移到 IE，§1 line 23 和 Contribution #2 现已正确 position 此增量，但 novelty 不构成 strong accept
4. 两位 Reviewer 独立收敛于 3.5，无分歧

**Conference vs Findings 判断**：
- Conference 偏弱：novelty 增量清晰但不突破性；实验虽全面但核心结论（constrained decoding 降低 violations）直觉上显然
- Findings 合格：执行质量高、实验严谨、disclosure 诚实、reproducibility 好
- 若 MF1 修复（"zero violations" 限定配置），评分有可能上调至 Findings 可接收（3.5→接近 4）

**修复优先级**：
1. [提交前必做] MF1: 限定 "zero violations" claim 配置范围
2. [强烈建议] SF1: §5 讨论 beam search 结果 + SF2: 清理剩余 -ing 模式
3. [建议] SF3: DocRED fallback coverage
4. [可选] M1-M3

---

## Detailed Comments

### Abstract
- Round 5 的 R² 和缩写问题已修复（重大改善）
- 新问题：line 13 "zero violations" overclaim 是本轮唯一 critical issue
- line 11 "suggesting that..." 和 line 12 "confirming..." 的 -ing 结尾应改写
- 整体结构和信息密度较 Round 5 有改善

### §1 Introduction
- Code-gen 区分已添加（line 23, Contribution #2），审稿人现可在 §1 判断 novelty 增量
- Post-hoc framing 已平衡（line 14），诚实且有力
- Contribution #3 (line 31-32) 信息密度过高，且包含 "zero violations" overclaim
- line 22 "enabling" 和 line 28 "showing that" 为 -ing 结尾

### §3-4 Method / Composition
- 形式化质量维持高水平
- §4 "dual-factor pattern" n=4 limitation 应在段内标注（目前仅 Appendix 有 caveat）

### §5 Experiments
- 覆盖面广、数据一致
- 缺 beam search 正文讨论
- DocRED fallback coverage 仅隐含提及

### §6 Related Work
- Em-dash 已从 section6_related_work.tex 清除
- 引用覆盖充分

### §7 Discussion and Conclusion
- "Descriptive characterization" 措辞恰当（R² 不再出现）
- 仍缺 beam search 正文讨论

### Limitations
- 全面且诚实
- 覆盖 CF、parse failure、model scale、composability scope
- Greedy limitation + beam/sampling appendix 引用到位

### Appendix
- Reproducibility details 质量高（LoRA 配置、training、GPU 完整）
- Beam search 结果（appendix_beam_search.tex）质量高但应在正文体现
