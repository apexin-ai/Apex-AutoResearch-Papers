---
round: 5
overall_score: borderline
timestamp: 2026-05-16T11:40:01.938399+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 5 (Fresh Review)

**论文**: *Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?*
**Venue**: ACL ARR May 2025 (Main Conference, Long Paper)
**Reviewers**: 3 (R1: 方法/实验, R2: 新颖性/Framing, R3: 写作/格式)
**交叉验证**: 完成（3/3 Reviewers 完成 [AGREE]/[REBUT] 回应）

---

## Summary

论文首次系统分离了 training-free LLM 信息抽取中 schema-induced degradation 的两个来源：type count 和 type confusability。引入 Schema Confusability Score (SCS) 及其 batch-level 聚合 BCS，在 Few-NERD (NER)、FewRel/DocRED (RE)、MAVEN (ED) 四数据集上用 Qwen3-32B 评估，设计了 count curves 和 BCS-controlled 两种互补实验范式。主要发现：count 驱动 recall 下降（最大 −49pp）、confusability 驱动 type substitution（quartile gap −5.3pp, extreme-batch gap −31.2pp, typical-batch gap ≈2.2pp）。SDGD schema decomposition 因 merge amplification 在 NER 上失败，RE batch composition 未达显著性（+1.4pp, p≈0.19）。

---

## Strengths

**S1. 严谨的控制变量实验设计 [3/3 共识]**
Count curves + BCS-controlled 两种范式互补，within-pool 分析（从 80-rel pool 抽 16-type 子集）进一步控制 pool composition confound。FewRel balanced design (700 instances/type) 排除 type frequency 混淆。Permutation test 确认跨 pool slopes 一致 (p=0.598)。这是零样本 IE 领域首次使用这一实验设计水平。

**S2. 负面结果的诚实报告 [3/3 共识]**
SDGD 失败、merge amplification 诊断、p=0.19 batch composition、non-significant factorial interaction (p=0.50)、80-rel condition p=0.762 均如实报告。无选择性隐藏不利证据。这种透明度值得赞赏，merge amplification 的诊断对 decompose-then-merge 范式有直接警示价值。

**S3. 统计报告规范 [3/3 共识]**
全文一致报告 95% bootstrap CIs、permutation tests、effect sizes (r, r², R²)。多层效应量汇报（pairwise → batch-level）清晰。远超多数 NLP 论文水准。

**S4. 多数据集多任务覆盖 [3/3 共识]**
跨 NER/RE(sentence+document)/ED 四任务四数据集，含 cross-model validation (Llama-3.1-8B)。DocRED 扩展至 96-type document-level RE，独立复现 BCS slopes。

**S5. Centrality confound 识别与处理 [3/3 共识]**
§4.5 对 MAVEN 正相关异常的归因（frequency + degree centrality）和 Appendix partial correlation 控制展示了对混淆变量的高度警觉，对未来 schema complexity 研究有方法论参考价值。

---

## Weaknesses

### Must-Fix（6 个 Critical 问题）

**W-C1. SCS justification 事实性错误 [3/3 AGREE — critical]**

§3.2 声称 SCS 仅用 type name 计算 "to reflect the information available to the model at inference time"。但 Appendix H (§H.4) 明确写道 "All prompts include per-type natural-language definitions"，prompt 格式为 `{type_name}: {definition}`。模型推理时同时看到 name + definition，SCS 仅编码 name similarity。§3.2 的理由自相矛盾。

- **Impact**: SCS 是两大实验范式的核心度量。虽然 empirical validation (r=0.112-0.129, p≪0.001) 证明 proxy 有信号，但 stated justification 错误削弱方法论叙事。Name 相近但 definition 区分度高的 type pairs 可能被 SCS 误标高混淆。
- **Required fix**: (1) 删除 "to reflect the information available" 的伪理由；改为 "lightweight pre-hoc proxy, a simplifying choice rather than a principled one"; (2) 提供 name+definition SCS ablation; (3) 讨论 name-only vs definition-inclusive tradeoff。

**W-C2. 因果语言超出 quasi-experimental 设计 [3/3 AGREE — critical]**

全文使用 "channels"、箭头 (→)、"independently degrade"、"drives" 暗示因果机制。但 Limitations #6 自认 "correlational evidence with controlled stratification"。BCS-controlled 实验控制了 count（FewRel 亦控制 type frequency），但 definition quality 和 prompt position 未控制。

- R1 指出 BCS-controlled 属 stratified controlled comparison，高于纯 observational 但低于 interventional/do-calculus 意义上的因果推断。
- **Required fix**: (1) "channels" → "components" / "patterns"; (2) "independently degrade" → "separately associated with degradation"; (3) 删除 → 符号; (4) 消除正文与 Limitations #6 的内部矛盾。

**W-C3. Contribution #1 "across NER, RE, and ED" 但 MAVEN 是反例 [2/3 critical, 1 warning]**

MAVEN count curve 增长 (F1 0.106→0.247)，§4.5 详细解释了 centrality confound。但 Contribution #1 仍声称 "degrade...across...ED"。R1 认为 severity 可降为 warning（论文已充分讨论反转），R2/R3 认为 contribution list 的措辞本身就是 overclaim。

- **Required fix**: Contribution #1 改为区分 cross-domain schemas（NER, RE: degradation confirmed）和 same-domain schemas（ED: centrality confound reverses count trends, pairwise confusability signal persists）。

**W-C4. SCS novelty overclaim [3/3 AGREE — critical]**

SCS = cos(embed(name_i), embed(name_j))，与 LLM-PEE 使用 type embedding similarity 进行 schema partitioning 技术同构。"Introducing the Schema Confusability Score (SCS)" 暗示 metric novelty。实际 novelty 在 controlled experimental framework（隔离 count vs confusability），非 metric 本身。

- **Required fix**: (1) "introducing" → "operationalizing"; (2) §2 Related Work 明确与 LLM-PEE 技术等价性；强调区分在 analytical use vs engineering use。

**W-C5. 31.2pp extreme-batch headline vs 2.2pp typical-batch framing 失衡 [3/3 AGREE — critical]**

31.2pp（extreme-batch construction, maximizing BCS contrast）在 Abstract/Introduction/Results/Conclusion 出现 7+ 次。Typical-batch gap ≈2.2pp (IQR-based, §4.3 "Practical magnitude") 仅出现 3 次。R3 指出 Abstract 叙述顺序先 typical 后 extreme，但正文 repetition 严重失衡。

- **Required fix**: (1) 所有 31.2pp 出现处附带 typical-batch magnitude; (2) Discussion/Conclusion 以 typical magnitude (2.2pp / quartile 3.9-5.3pp) 为主锚点; (3) Table 2 caption 加入 "extreme-batch construction; see §4.3 for typical magnitudes"。

**W-C6. RE batch composition +1.4pp (p≈0.19) 列为 Contribution #4 [2/3 AGREE, 1 partial rebut]**

p=0.19, n=1 graph-coloring configuration, rank 13/15 random seeds, BCS margin 0.006。R1/R2 认为是 null result 不应列为 contribution。R3 辩护 contribution 是诊断性发现 (merge amplification + oracle routing +29.8pp) 而非 +1.4pp 本身。

- **Required fix**: Reframe Contribution #4 为 negative/diagnostic finding: "schema decomposition is structurally infeasible for NER (merge amplification) and yields no statistically significant improvement for RE at current granularity"。移除 "directionally consistent" 对 +1.4pp 的描述。

### Should-Fix（11 个 Warning 问题）

**W-W1. "Cross-model replication" 表述过度 [3/3 AGREE]**
仅两模型 (Qwen3-32B, Llama-3.1-8B)。Channel 2 在 8B NER 上 floor effects。§4.1 Summary "Both channels replicate" 与 Limitations #1 矛盾。
→ Fix: "preliminary cross-model evidence"; §4.1 加 "for RE" qualifier; 全文 "cross-model replication" → "cross-model consistency check"。

**W-W2. §5 SDGD 篇幅严重不足 [2/3 AGREE, R1 partial rebut]**
RQ3 是三个核心问题之一但 §5 仅 ~0.5 页。SDGD comparison table、confidence gating 分析全在 Appendix。fig_sdgd_comparison.pdf 存在但未使用。R1 认为 negative result 不需同等篇幅，但 R2/R3 认为 merge amplification 是论文最直接可操作的发现，值得正文展开。
→ Fix: §5 扩至 ≥1 页；移入核心 table 和 figure。

**W-W3. Discussion + Conclusion 过于单薄 [3/3 AGREE]**
Discussion 仅 3 段，Conclusion 1 段。缺：(1) 为什么 cosine similarity 能预测 LLM confusion 的 mechanistic intuition; (2) 具体 practitioner guidance (BCS threshold 如何设); (3) 与 schema-guided dialogue scaling (SGD) 的联系。
→ Fix: 扩至 ≥1 页。

**W-W4. 正文仅 2 个 Figure [2/3 AGREE]**
8 页正文 2 个 figure 对实验密集型论文不足。fig_sdgd_comparison.pdf 未使用。
→ Fix: 加入 §5; 考虑 cross-model 或 DocRED 可视化。

**W-W5. FewRel train+val merge — data contamination 风险未讨论 [3/3 AGREE]**
FewRel training split (2018) 广泛使用；Qwen3/Llama3 预训练语料可能包含。R2 补充：核心发现是 relative effects (high vs low BCS)，contamination 需差异性影响不同 BCS 条件才混淆结论，但仍应讨论。
→ Fix: Limitations 加一条; 如可行比较 train-split vs val-split relation accuracy。

**W-W6. Bootstrap CIs: pair-level 在主表, cluster bootstrap 埋在正文 [2/3 AGREE]**
Table 2 主报 pair-level bootstrap CI；type-level cluster bootstrap 仅正文一句带过且 cluster 定义不清。R3 补充 cluster CIs 仍显著，结论不受影响。
→ Fix: Table 2 改报或 dual-report cluster-robust CIs; 明确 cluster 定义。

**W-W7. Related Work 覆盖缺口 [2/3 AGREE]**
缺: SGD (Rastogi 2020), SGD-X (Lee 2022) — schema-guided dialogue 中的 schema scaling; Li et al. 2023 (ChatGPT IE evaluation); Volkanovska et al. 2024 (LLM NER errors)。R1 认为 SGD relevant but non-essential。
→ Fix: §2 加 "Schema complexity in related NLP tasks" 段。

**W-W8. 参考文献时间线不一致 [procedural, flagged for AC]**
reflect-learn-2026 (arXiv 2025-08), gliner2-2025 (arXiv 2025-07) 等引用在声称的 May 2025 截止日后才存在。R2 argues ARR revision 允许更新 refs，属 procedural issue 非 scientific soundness concern。
→ Fix: 核实并修正; 在 cover letter 说明 revision 中新增的引用。

**W-W9. DocRED 采样细节正文缺失 [3/3 AGREE]**
"Sample balanced instances" 无具体数量/per-type 策略。Table 1 有 n=1,000 但正文描述不完整。
→ Fix: §3.1 补充 "1,000 balanced instances (~10 per relation type)"。

**W-W10. vLLM 版本号 v0.20.2 可能有误 [3/3 AGREE]**
截至 2025-05, vLLM 公开版本约 0.4.x–0.6.x。v0.20.2 不符合已知版本编号。
→ Fix: 核实。

**W-W11. p-value 格式不统一 [3/3 AGREE]**
至少 5 种格式变体。
→ Fix: 统一为 p=X.XXX (显著) / p<0.001 (极小)。

---

## Reviewer Consensus

| Issue | R1 | R2 | R3 | 最终判定 |
|-------|----|----|----|----|
| SCS justification 错误 (W-C1) | ✅ critical | ✅ critical | ✅ critical | **强共识: must-fix** |
| 因果语言 (W-C2) | ✅ agree | ✅ critical | ✅ agree | **强共识: must-fix** |
| MAVEN overclaim (W-C3) | ✅ warning | ✅ critical | ✅ critical | **共识: fix; severity 2:1 critical** |
| SCS novelty overclaim (W-C4) | ✅ agree | ✅ critical | ✅ agree | **强共识: must-fix** |
| 31.2pp framing (W-C5) | ✅ critical | ✅ agree | ✅ agree | **强共识: must-fix** |
| +1.4pp contribution (W-C6) | ✅ agree | ✅ agree | ⚠️ partial rebut | **多数: reframe** |
| Cross-model wording (W-W1) | ✅ agree | ✅ agree | ✅ agree | **强共识** |
| §5 too short (W-W2) | ⚠️ partial rebut | ✅ agree | ✅ agree | **多数: expand** |
| Discussion thin (W-W3) | ✅ agree | ✅ agree | ✅ agree | **强共识** |

## Reviewer Divergence

| Issue | 各方立场 | 处理 |
|-------|---------|------|
| R1-N3 amplification severity | R1: critical; R2: should-fix (batch R² 直接测量); R3: agree needs support | **降级**: amplification 是 explanatory, batch results 独立成立; argument 需 formal support 或删除 |
| R1-W3 within-pool CI 跨零 | R1: warning; R2/R3: rebut (slope p=0.027 显著, quartile 是 power 问题) | **已解决**: paper 处理恰当; permutation test 确认一致 slopes |
| R1-W6 v1 vs v2 选择 | R1: warning; R2/R3: rebut (text-match 不受 offset hallucination 影响) | **已解决**: 非 validity concern |
| R3-N1 引用时间线 | R3: critical; R2: procedural; R1: conditional agree | **降级**: procedural issue, flag for AC |
| R2-W5 abstract 缺 r² | R2: warning; R3: rebut (abstract 已含 r²=1.3-1.7%) | **已解决**: R2 事实错误 |

---

## Questions for Authors

1. **[3/3]** 是否尝试过 name+definition SCS？结果如何与 name-only 对比？
2. **[R1, R3]** 能否提供 simulation 证明 pairwise r²≈1.5% 在观测的 pair correlation structure 下聚合为 batch-level R²≈22-53%？
3. **[R1]** FewRel training-split relation 的准确率是否系统性高于 validation-split relation（contamination check）？
4. **[R1]** 在相同 BCS range 下，v1 和 v2 prompt gap 如何对比（disentangle BCS range 缩窄 vs prompt 改进）？
5. **[R2]** SCS 与 LLM-PEE type embedding similarity 在技术实现上的本质区别是什么？

---

## Missing References

1. **Rastogi et al. (2020)** "Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset" (AAAI) — schema complexity in DST
2. **Lee et al. (2022)** "SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems" (AAAI) — schema linguistic variation
3. **Li et al. (2023)** "Evaluating ChatGPT's Information Extraction Capabilities" — LLM IE with type count degradation observed
4. **Volkanovska et al. (2024)** "A Study of Errors in the Output of LLMs for NER" (JLCL) — LLM NER error taxonomy including type confusion

---

## External Review (Stanford Agentic Reviewer)

未配置（`external_review.paperreview_ai.enabled` not set in project config）。

---

## Overall Assessment

**Score: borderline**（leaning weak accept with revisions）
**Confidence: high**（3 Reviewers with complementary expertise, full cross-validation）

| Reviewer | Overall | Soundness | Excitement |
|----------|---------|-----------|------------|
| R1 (方法/实验) | 3.5/5 | 3/5 | 4/5 |
| R2 (新颖性/Framing) | 3.5/5 | 3.5/5 | 3/5 |
| R3 (写作/格式) | 3/5 | 3.5/5 | 3/5 |

**Rationale**:

论文在一个有价值的研究问题上（首次控制分离 count vs confusability）展示了高质量的实验设计。BCS-controlled + within-pool 分析是优雅的控制变量方法。负面结果的诚实报告和统计规范性远超多数 NLP 论文。

但六个 critical 问题阻止明确接收：
1. SCS justification 事实性错误（可修复但影响方法论叙事完整性）
2. 因果语言超出 quasi-experimental 设计（可修复）
3. 多处 framing overclaim（MAVEN 跨任务泛化、SCS novelty、+1.4pp 贡献、31.2pp prominence）累积产生了膨胀的整体印象
4. SCS 作为 metric 无新颖性（novelty 在实验框架）
5. Practical effect size modest (typical 2.2pp) 被极端构造数字淹没
6. Discussion/Conclusion 对分析性论文偏薄

**核心判断**：实验发现（count degradation curves, BCS-controlled slopes, merge amplification 诊断）本身是 sound 的。问题集中在 framing、presentation 和一个可修复的方法论缺口 (name+definition SCS)。大部分问题可在一轮修订中解决。

**Recommendation**: Revise and resubmit。修复 SCS justification + name+definition ablation，校准因果语言和全文 framing，扩展 Discussion，以 typical magnitude 为主叙事锚点。修复后适合 **ACL Findings track**。

---

## Detailed Comments

**§1 Introduction**: Contribution list 需全面修订——#1 区分 cross-domain/same-domain; #4 reframe 为 negative/diagnostic; "introducing SCS" → "operationalizing"。5 个 findings 的 framing 需与 evidence 对齐（特别是 typical vs extreme magnitude hierarchy）。

**§2 Related Work**: 补充 schema-guided dialogue (SGD/SGD-X) 作为 cross-domain bridge。明确 SCS 与 LLM-PEE 技术等价性。清理 orphan bib entries。

**§3.2 SCS Definition**: 删除 "to reflect the information available to the model at inference time"（事实错误）。改为 "SCS is a lightweight pre-hoc proxy using type name embeddings; this name-only choice is a practical simplification — definitions provide additional discriminative information not captured by SCS"。补充 name+definition ablation。

**§4.1-4.5 Results**: 实验结论 sound。Minor fixes: "Both channels replicate" 加 "for RE" qualifier; §4.3 "Practical magnitude" 应更早出现在叙事中（不应埋在 §4.3 末尾）。

**§5 SDGD**: 扩至 ≥1 页。Merge amplification 是最直接可操作的发现——从 Appendix 移入正文。加入 fig_sdgd_comparison.pdf。Oracle routing 的 +29.8pp 是有力的正面结果（消除 count degradation），值得在正文突出。

**§6 Discussion**: 当前 3 段过薄。扩展: (1) 理论——为什么 embedding cosine similarity 能预测 LLM 在 ICL 中的 type confusion（与 representation space geometry / attention pattern 的联系）; (2) 实用——具体 schema design workflow + BCS threshold 建议; (3) 跨域——与 DST schema scaling 的联系; (4) Scaling——effect size 与 model scale 的关系（已有两个数据点）。

**§7 Conclusion**: 不要压缩 results summary，而是 synthesize takeaway message。

**Abstract**: 精简至 ~200 words。以 typical-batch gap 为 primary magnitude，extreme-batch 为 secondary。移除属于 body text 的 qualifications (如 "with attenuated magnitude under improved prompts")。

**格式**: 统一 p-value 格式; 核实 vLLM 版本; 处理引用时间线。