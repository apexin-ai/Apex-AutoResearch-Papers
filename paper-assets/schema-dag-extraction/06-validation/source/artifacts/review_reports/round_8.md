---
round: 8
overall_score: weak reject
timestamp: 2026-05-16T16:53:41.705782+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 8

**论文**: "Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)
**截止日期**: 2026-05-25
**审稿人**: Reviewer 1（方法论+统计推断+实验设计）、Reviewer 2（新颖性+相关工作+整体贡献+framing）
**审稿模式**: Fresh review（独立于历史轮次）
**外部审稿**: 未启用
**Reviewer 3 说明**: 本轮因 EMNLP Main Conference 编排（2 人：方法严谨性 + 新颖性/完整性），Reviewer 3 未被分配任务。历史 Reviewer 3（格式+可复现性）的典型关注点已由 R1/R2 在各自侧重中覆盖。

---

## Summary

本文研究 training-free LLM IE 中 schema 复杂度导致的性能下降，提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化 type 间语义相似度，通过 count curves 和 BCS-controlled 两种实验范式在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-level RE)、MAVEN (ED) 四个数据集上进行 controlled study。核心发现：(1) type count 驱动 recall 下降（-42% to -56%），type confusability 驱动 type substitution（typical gap 2.2pp, CI [0.4, 4.0]）；(2) pairwise SCS 与 type confusion 显著相关（r=0.112-0.129, r²=1.3-1.7%）；(3) 两通道在 RE 上 consistent with additive separability（TOST p=0.003），但 NER factorial 不显著（p=0.50）；(4) schema 分解对 NER 因 merge amplification 失败，对 RE 在 oracle routing 下无显著改善（+1.4pp, p≈0.19）。

---

## Strengths

**S1. 精良的 controlled experimental design**（两人共识）
BCS-controlled 范式在 zero-shot IE 文献中属首次。Within-pool analysis 排除 pool composition confound，permutation test (p=0.60) 确认 slope 跨条件一致。Count curves + BCS-controlled 双范式有效解耦 schema size 和 confusability。

**S2. 高度诚实的负面结果报告**（两人共识）
SDGD 全面失败（F1 0.445→0.251）、MAVEN centrality confound、factorial tests 多数不显著、mitigation 无显著改善——全部如实报告并深入分析。在 NLP 论文中罕见且值得赞赏。

**S3. Centrality confound 分析**（两人共识）
识别 MAVEN 上 per-type BCS 正相关为 centrality artifact，通过 partial correlation 控制后信号消失（p>0.2）。对社区有方法论示范价值，是论文最有洞察力的部分。

**S4. 统计报告的高透明度**（两人共识）
Bootstrap CI、cluster bootstrap、TOST equivalence test、permutation test、Monte Carlo aggregation simulation——方法论规范。非显著结果（factorial p=0.50, SDGD +1.4pp p≈0.19, within-pool quartile CI 过零）、modest effect sizes（r²=1.3-1.7%）均如实报告。

**S5. 跨任务/跨模型 replication**
Channel 1 在 Llama-3.1-8B 完全复现（per-batch r=0.725），Channel 2 在 RE 跨模型复现。DocRED 扩展到 document-level（R²=0.53）。Prompt sensitivity analysis (v1/v2) 少见但重要。Limitations 质量极高（7 条具体、可操作）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical — 两人共识] 核心发现 novelty 不足，不满足 main conference 门槛**

SCS 与 LLM-PEE 的 partitioning criterion 形式相同（论文 §2 自己承认）。核心结论——"语义相似的 type 更容易混淆"——是 IE 从业者的 common sense 级别直觉。论文的 controlled factorial design 是标准方法论，应用到新问题域不构成方法论创新。R1 补充：controlled evidence 的价值在于量化方向（2.2pp 远小于直觉预期），non-obvious findings（NER coupling, merge amplification）有一定贡献，但整体属于 Findings-level novelty 而非 main conference level。

→ 建议：(1) 明确定位为 empirical confirmation paper，Contribution 1 改为 "Controlled empirical evidence for two degradation dimensions"；(2) 强调 non-obvious findings（2.2pp typical 远小于直觉、NER coupling、merge amplification 诊断）。

**W2 [Critical — 两人共识] 典型效应量 2.2pp 的实用意义可疑**

Typical confusability gap 仅 2.2pp（95% CI: [0.4, 4.0]），CI 下界 0.4pp 接近零实际意义。Pairwise r²=1.3-1.7%，98.3%+ variance 由其他因素解释。Count effect（-42% to -56%）与 confusability typical effect (2.2pp) 差两个数量级，"two-channel" 对称 framing 不成立。Abstract 以 extreme-batch gap (-31.2pp) 和 "up to 53%" (DocRED 单一条件) 为 headline，放大了感知效应量。论文 §4.3 做了诚实披露但高曝光位置（Abstract/Intro/Conclusion）未反映 typical 数字。

→ 建议：(1) Abstract 以 typical 2.2pp 和 quartile 5.3pp 为 headline，extreme 31.2pp 限制为 "methodological upper bound"；(2) 讨论 practical significance vs statistical significance；(3) 考虑重新定位为 "confusability is detectable but not the primary driver"。

**W3 [Critical — 两人共识] Factorial separability claim 建立在选择性测试上**

论文声称 count 和 confusability "cleanly separable in RE"，但三项 factorial 检验中只有一项通过：
- Few-NERD 2×2 factorial: p=0.50（不显著）
- FewRel 2×2 factorial (n=54): p_TOST=0.56（不显著）
- FewRel full regression (n=69, 5 count levels): p_TOST=0.003（显著）

R1 认为这构成 garden of forking paths；R2 认为更接近 power difference（regression 用 69 batches vs 2×2 的 54 points）但同意 "cleanly separable" 是 overclaim。两人共识：需限定表述。

→ 建议：Abstract/Conclusion 改为 "consistent with additive separability (TOST p=.003) under full-range regression; lower-powered 2×2 designs did not reach equivalence"。

**W4 [Critical — 两人共识] Contribution #4 "Diagnosis to mitigation" framing 误导**

NER SDGD: F1 从 0.445 降至 0.251（全面崩塌）；RE graph-coloring: +1.4pp, p≈0.19, n.s.（rank 13/15 random seeds）。"Mitigation" 暗示成功缓解，但 RQ3 答案是 negative result。Section 6 标题 "Schema Decomposition: Failure, Diagnosis, and Mitigation" 比 Contribution statement 更诚实。

→ 建议：Contribution #4 改为 "Schema decomposition reveals structural barriers"——merge amplification 诊断和 oracle ceiling (+29.8pp) 仍是有价值的贡献。

**W5 [Critical — R1 主导, R2 同意] Conditioning on non-zero pairs 引入选择偏差，且作为后续分析基础**

论文将 unconditional r²=1.3% 和 conditional r²=7%（non-zero pairs only）并列报告。Appendix I 的 Monte Carlo aggregation simulation 使用 conditional R²=0.074 作为输入，模拟得到 batch-level R²=0.219，"匹配" 观测值。但用 unconditional r²=0.013 作为输入，R2 估计 simulated batch R²≈0.039，远低于观测的 0.218。Conditioning on dependent variable（non-zero confusion）有偏。

→ 建议：(1) 用 unconditional r² 重新运行 simulation 作为 lower bound，并报告两种输入的结果；(2) 讨论 discrepancy 来源；(3) 明确标注 7% 为 conditional estimate。

### Should-Fix（影响评分但不一票否决）

**W6 [Warning — R2 主导, R1 部分同意] Hierarchical classification / label confusion 文献覆盖不足**

§2 Related Work 只引了 Deng et al. (2010) ImageNet。遗漏：Zhou et al. (NAACL 2025), Guo et al. (AAAI 2021), Novack et al. (ICML 2023, CHiLS), ZERONER (ACL Findings 2025)。R1 部分反驳："first" claim 有 triple qualification（controlled + isolating confusability from count + zero-shot LLM IE），如果这些论文不在 zero-shot LLM 场景则 claim 可能成立。但两人共识：无论是否撤回 "first" claim，§2 应更全面覆盖 label confusion 文献。

→ 建议：逐一核实 4 篇缺失引用是否涉及 zero-shot LLM IE；补充 hierarchical classification label confusion 文献段落。

**W7 [Warning — 两人共识] Single-seed evaluation 无法量化推断不确定性**

Greedy decoding (temp=0) 理论上确定，但 FP8 quantization + vLLM batching 可能引入 non-determinism。更关键的是 batch sampling variability 未跨 seed 验证。

→ 建议：至少对 core claims 报告 3 seeds 方差。

**W8 [Warning — 两人共识] Count curve 每 level 仅 5 batches，稳定性存疑**

5 batches 的 SD 估计自由度仅 4。Count=8-16 时组合空间巨大，5 batches 远不足代表 population。

→ 建议：增至 25+ batches 或报告 bootstrap CI on mean。

**W9 [Warning — 两人共识] 跨数据集 embedding 不一致**

Few-NERD 用 extraction model 自身 hidden states (Qwen3-32B)，其余用 MiniLM。Cross-check 方向一致（r=0.172 vs 0.138, matrix corr 0.894），但 shared-representation bias（用提取模型自身 embedding 计算 SCS）是更根本的问题。

→ 建议：Limitations 补充 shared-representation bias caveat；对 Few-NERD 补充完整 MiniLM 分析或声明跨任务比较非论文目标。

**W10 [Warning — 两人共识] FewRel train+val 合并的 contamination 风险**

Train-origin relations 准确率低 8.8pp (p=0.06, borderline)。虽方向与 contamination 假说相反，但不排除 split-level confound。

→ 建议：BCS-controlled 分析中加入 split-origin 作 covariate。

**W11 [Warning — R1 主导, R2 部分反驳] TOST margin ±3pp justification 非标准**

SESOI 应基于 practitioner decision boundary，而非相对于 prompt noise 的比例。但 sensitivity analysis（±2pp marginally equivalent, p=0.047; interaction=0.47pp, 90% CI [-1.0, 2.0]pp）表明具体 margin 选择不 critical。

→ 建议：从 practitioner decision boundary 角度重新论证；引用 Lakens (2017)。

### Minor

- FewRel r=0.187 在 §3.2 引用为 evidence 但 Table 2 省略——逻辑应统一
- Rothman (1990) 辩护不做 family-wise correction 在 NLP 有争议，至少 acknowledge 对立观点
- Abstract 数字密度过高，建议结构化为 problem→method→findings→implication
- 引用验证：gliner2-2025, sclar-sensitivity-2024, json-schema-bench-2025, li2023evaluating 在 OpenAlex 中未精确匹配

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识 [AGREE]：
1. **Effect size 太小**（2.2pp typical / r²=1.3-1.7%）削弱核心 claims 的实用意义
2. **Abstract/Intro framing** 过于乐观，cherry-pick extreme numbers
3. **"Mitigation" framing 误导**——RQ3 答案是 negative result
4. **Separability "cleanly separable" overclaim**——3/4 factorial tests 失败
5. **Single-seed + 5 batches/level** 影响 claim 稳健性
6. **Novelty 不足**——Findings-level, 非 main conference level

## Reviewer Divergence

| 议题 | R1 | R2 | 分歧程度 |
|------|----|----|----------|
| Excitement | 3.5/5（方法论贡献有价值） | 2.5/5（findings 缺乏惊喜感） | 中等 |
| Missing references 严重性 | Partially rebut（取决于是否覆盖 zero-shot LLM IE） | Critical（文献覆盖不足） | 中等 |
| Factorial cherry-picking vs power difference | Garden of forking paths | Power difference | 低（结论一致） |
| LLM-PEE 对比深度 | §2 differentiation 足够 | 需讨论 merge strategy | 低 |
| TOST margin | Warning | Sensitivity analysis 足够 | 低 |

---

## Questions to Authors

1. 如果用 unconditional r²=0.013（而非 conditional R²=0.074）重新运行 Monte Carlo aggregation simulation，simulated batch-level R² 是多少？如果远低于 observed 0.218（R2 估计约 0.039），如何解释 discrepancy？
2. 5 random batches per count level 中，batch-to-batch variance 有多大？是否有 batch 组合使 count curve 非单调？
3. Full regression TOST (n=69, 5 count levels) 通过而两个 2×2 factorial 不通过——能否提供 pre-specification 论证说明 full regression 为什么是 primary test（而非 post-hoc 选择最有利的结果）？
4. NER 的 positive batch-level BCS-F1 correlation (r=+0.50/+0.58) 归因于 type-frequency confound。在 BCS-controlled design 中，controlling BCS 是否间接 controlled frequency？Few-NERD 是否需要类似 MAVEN 的 centrality/frequency partial correlation 分析？
5. R2 列出的 4 篇缺失引用（Zhou et al. NAACL 2025, Guo et al. AAAI 2021, Novack et al. ICML 2023, ZERONER ACL Findings 2025）中，有任何一篇在 zero-shot LLM IE 中做过 controlled confusability analysis 吗？

---

## Missing References

- Zhou et al. (NAACL 2025) "Semantic Similarity through Classification Confusion"
- Guo et al. (AAAI 2021) "Label Confusion Learning"
- Novack et al. (ICML 2023) "CHiLS"
- ZERONER (ACL Findings 2025)
- Lakens (2017) "Equivalence Tests: A Practical Primer"
- Simmons et al. (2011) "False-Positive Psychology"
- Stefan et al. (2019) — SESOI determination methods for TOST

---

## External Review (Stanford Agentic Reviewer)

项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。

---

## Overall Assessment

**Overall Score: Weak Reject (Main Conference) / Accept (Findings)**

**R1**: 3.5/5 | **R2**: 3.0/5 | **Consolidated**: 3.25/5

**Confidence**: 4/5 (High)

本文在实验设计和统计方法上表现出色——BCS-controlled paradigm、within-pool analysis、centrality confound 诊断、负面结果的诚实报告——这些在 NLP empirical 论文中属于上乘水平。论文对自身局限性的 self-awareness（§4.3 practical magnitude, Limitations 7 条）也值得肯定。

然而，核心发现存在三个根本性问题：(1) **novelty 不足**——SCS 与 LLM-PEE 形式相同，"similar types cause confusion" 是可预测的直觉，controlled design 本身不构成足够创新；(2) **效应量太小**——typical 2.2pp (CI [0.4, 4.0]) 远小于 count effect (-42% to -56%)，"two-channel" 对称 framing 与效应量不对称之间的张力未解决；(3) **framing 系统性乐观**——headline 数字选择 (31.2pp / "up to 53%")、"cleanly separable" (3/4 tests 失败)、"Diagnosis to mitigation" (mitigation 失败) 均使论文呈现的画面比实际证据更强。

**推荐**: 不满足 EMNLP 2026 Main Conference 的 novelty 和 excitement 门槛。建议作者：(1) 修正 framing 以诚实反映 typical effect size 和负面结果；(2) 补充缺失的 label confusion 文献；(3) 用 unconditional r² 重跑 aggregation simulation；(4) 考虑投向 Findings track——论文的方法论质量和负面结果诊断在 Findings 定位下是有价值的贡献。

---

## Detailed Comments

### §1 Introduction
- "cleanly separable in RE (TOST p=0.003)" 需加限定（W3）
- "batch-level BCS explains up to 53%" 应报告 range "22-53%"（W2）
- Contribution #4 "Diagnosis to mitigation" 改为 negative result framing（W4）
- "First controlled study" → "To our knowledge, the first systematic controlled study"（W6）

### §2 Related Work
- SCS novelty 段落：不要暗示 SCS 是 novel metric
- 补充 hierarchical classification / label confusion 文献段落（W6）
- LLM-PEE 对比：讨论其 merge strategy 是否受 merge amplification 影响

### §3 Experimental Setup
- §3.2: 明确 Few-NERD 使用 Qwen3 embedding 的 rationale 及 shared-representation bias caveat（W9）
- §3.3: 声明 full regression 为 primary separability test 并给出 rationale（W3）
- §3.5: 讨论 single-seed + FP8 non-determinism（W7）

### §4 Results
- §4.2: FewRel r=0.187 与 Table 2 省略处理需统一
- §4.3: Practical magnitude 讨论需在 abstract/intro 前置（W2）；conditioning on non-zero pairs 的 selection bias 需讨论（W5）
- §4.4: "cleanly separable" 限定为 "consistent with additive separability under sufficient power"（W3）
- §4.5: MAVEN centrality analysis 是论文亮点

### §5-6 SDGD & Discussion
- Contribution 措辞修改（W4）
- 讨论 prompt length vs count confound
- 讨论 practical significance of 2.2pp

### Appendix
- Monte Carlo simulation: 用 unconditional r² 重跑作为 lower bound（W5）
- TOST: 从 practitioner perspective 论证 margin（W11）
- 引用 Lakens (2017)