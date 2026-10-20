---
round: 9
overall_score: borderline
timestamp: 2026-05-15T19:05:20.100720+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告 — Phase-Modulated Compound Sparsity

**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + Related Work + 格式）
**交叉分享**: 完成。R1 对 R2 的 11 项 weakness 同意 8 项、部分反驳 3 项；R2 对 R1 的 10 项 weakness 同意 7 项、反驳 3 项。

---

## Summary

本文系统表征了 compound sparsity（attention head pruning + KV cache eviction 同时施加）的退化严重性在推理模型不同注意力稀疏度阶段中的差异。核心发现：importance-based eviction 产生随稀疏度单调递增的 phase-strategy 交互效应（DeepSeek Δ: 0.39→8.48, Qwen Δ: 0.07→3.16），而 random eviction 效应弱 3–17×。论文定位为 diagnostic study，方法论严谨（nonparametric bootstrap + Wilcoxon + JT test + 6 维 robustness），但核心 proxy（attention sparsity ↔ reasoning phase）未经独立验证，缺乏下游 accuracy 验证，novelty 深度不足以支撑主会议 long paper。

---

## Strengths

**S1. 问题定位精准，填补明确空白** — 识别了 compound compression 文献中 "交互效应生成过程中恒定" 的隐含假设，将 phase variation 引入 compound sparsity 分析。[R1, R2 共识]

**S2. 统计方法论高度严谨且异常透明** — nonparametric bootstrap (B=10,000) + Wilcoxon/Mann-Whitney + Bonferroni correction 对非正态分布（mean/median ratio 高达 97,640:1）完全恰当；BH-FDR 44-test robustness check 超出同类论文水准；JT test 与 Spearman (n=4) 明确分工。[R1 S2, R2 S1]

**S3. 鲁棒性验证全面** — segmentation granularity, min_phase_length, null model, asymmetric sparsity, outlier winsorization, permutation test 六维覆盖。[R1 S4, R2 S2]

**S4. 诚实的 hedging 和自我批评** — 通篇 "diagnostic study"、"correlational"、"preliminary" 限定。Limitations 覆盖 7 维度。Pilot mitigation 18% recovery 诚实报告。[R1 S3, R2 S3]

**S5. Crossover 效应有洞察力** — DeepSeek strategy ranking reversal 是此前文献未报告的定性现象，无法从单轴分析推导。[R1 S5]

**S6. 清晰的 factorial experimental design** — 2 models × 2 strategies × 4 sparsity levels × 3 phases × 4 conditions 的完整正交设计。[R2 S4]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical, consensus] Phase segmentation proxy 有效性未独立验证**
- R1-W1 + R2-W4 + 交叉共识
- Attention sparsity tercile segmentation 被用作 reasoning phase proxy。"低稀疏 = exploratory reasoning, 高稀疏 = structured computation" 的语义映射来自 ThinKV 引用，但 ThinKV 基于 `<think>` token 显式分隔符，不是 attention sparsity quantile。DeepSeek 有 `<think>` token 可做 ground-truth 验证但未做。Qwen 45.2% mid-phase null rate 进一步质疑 proxy 适用性。
- 论文 robust 了分割粒度（tercile/quartile/quintile）和 min_phase_length，但这仅验证 sensitivity-to-granularity，不验证 validity-of-proxy。
- 更严重的是 R2-W4 指出的 label-outcome coupling：segmentation 在 dense model 上计算（Appendix D Table 4 caption），但 §6 分析表明 pruning 改变 attention distribution (ΔH: -0.040 to -0.047)。Dense 下的 phase 划分与 compound sparsity 下的实际 phase 可能不一致。
- 如果 proxy 无效，"phase-modulated compound severity" 退化为 "attention-sparsity-correlated compound severity"——统计事实成立但语义解释不成立。标题、framing、contributions 都依赖语义解释。
- **建议**：(a) 用 DeepSeek `<think>` token 做 ground-truth 一致性分析；(b) 或显式讨论 dense-model segmentation trade-off 并 reframe 为 "attention-sparsity-modulated"。

**W2 [critical, consensus] 缺乏下游 accuracy 验证 + 93.2% 答案 token 天然屏蔽**
- R1-W2 + R2-W5 + 交叉共识
- §5.7 报告 93.2% 答案 token 落在 high-sparsity phase（compound interaction 接近零），reasoning-trace 退化 5.7–43.5× vs 答案 token 1.3–5.3×。
- "Silent reasoning errors" 是论证推理 token 退化重要性的唯一论据，但全文无 accuracy-level 验证。Limitations 承认 "requires future validation"，但 accuracy 评估计算开销极低（仅需答案提取），理应在当前论文中完成。
- 如果 accuracy 在 compound sparsity 下幸存（得益于 phase shielding），severity gradient 的实际部署意义大幅缩减，Discussion §7 的 implications 失去根基。
- **建议**：MATH-500 + GSM8K 上运行 compound sparsity 下的准确率评估（所有 16 条件），报告 accuracy delta alongside PPL-based II。
- 此问题自 Round 7 (R7-N1) 首次提出，Round 8 再次确认，至今未解决。

**W3 [critical, consensus] Novelty 不足以支撑主会议 long paper**
- R2-W1 + R1 交叉同意
- Introduction §1 自己承认 HIES (score collapse) + ThinKV (phase-aware eviction) + Sparse Frontier (strategy non-dominance) 的组合可 qualitatively predict phase-dependent compound degradation。论文的两个 "novel" quantitative patterns——strictly monotonic dose-response (JT z=33.7) 和 strategy ranking crossover——本质是 statistical confirmation of qualitatively expected interaction，非 counterintuitive finding。
- Crossover 仅 DeepSeek 出现、Qwen 不出现（model-dependent），进一步削弱 generality。
- 与 Voita (2019)/Michel (2019) 等 precedent diagnostic studies 对比：那些工作揭示了 counterintuitive findings（大量 heads 可安全移除），本文发现方向性不意外。
- **建议**：定位 Findings track；或补充 actionable method contribution（如 phase-aware adaptive budget allocator 超越 uniform baseline）。

**W4 [critical, consensus] 标题 "Mathematical Reasoning Models" 过度泛化**
- R2-W2 + R1-W4 + 交叉共识
- 实测 2 个 Qwen2ForCausalLM 7B 模型 + 1 个 LlamaForCausalLM (n=49, interaction ~1/40, 仅 s=0.30 显著)。标题暗示跨模型泛化但证据不支持。
- Abstract line 7 "preliminary cross-architecture evidence from a LlamaForCausalLM" 在 abstract 中出现给读者留下比 n=49/~1/40 effect 更强的印象。
- 此问题自 Round 7 (R7-W1) 首次提出，GSM8K 补充后有进展但标题仍未修正。
- **建议**：限定标题为 "Qwen2-family" 或 "7B-scale"，或至少移除暗示广泛泛化的 plural "Models"。

### Should-Fix

**W5 [warning] Multiplicative null G_× 方法论与主分析不一致**
- R1-W3 + R2 交叉同意（with nuance）
- 主分析 G 用 per-problem median of ratios (Eq.5)；Appendix B G_× = 21–64× 用 aggregate per-phase PPL ratios。Table 7 (profiling subset) 展示两种定义可差 10× (s=0.15: 7.5× vs 69×)。
- "Null-choice invariant" 声称依赖此 check，但 check 本身方法论不一致。R2 补充：multiplicative null 是 robustness check 非 primary result，但仍需修复以兑现声称。
- **建议**：用 per-problem median of ratios 重新计算 G_×。

**W6 [warning] "Cross-training-paradigm controlled comparison" 因果性过度声称**
- R2-W3 + R1 部分反驳 → 交叉达成 compromise
- §4 "enabling controlled comparison of training paradigm effects" — DeepSeek vs Qwen 除架构外，训练数据/tokens/teacher/hyperparameters 全部不同。R1 承认 quasi-experimental 合理但 "enabling controlled comparison" 措辞偏强。
- **建议**：改为 "within-architecture-family comparison"，移除 "isolates" 因果语言。

**W7 [warning] Discussion §7 实用价值暗示与 pilot 证据矛盾**
- R2-W6 + R1 交叉同意
- §7 仍用 "could inform phase-aware budget allocation"，但 Appendix F pilot oracle 仅恢复 18%（低于 pre-registered 30% gate），heuristic 32% 但 CI 跨零。
- 自 Round 6 (R7-W2) 首次提出。pilot 已移至 Appendix（进展），但主文暗示未修正。
- **建议**：§7 加显式 caveat 或删除实用价值暗示。

**W8 [warning] GSM8K n=50 缺乏 power analysis + Qwen 截断**
- R1-W5 + R2 交叉同意
- LLaMA n=49 有 power analysis 但 GSM8K n=50 没有。Qwen GSM8K 全部截断 (max_new_tokens=2047)。Random eviction 全部非显著可能仅因功效不足而非 task-complexity 解释。
- **建议**：补 GSM8K power analysis；标注 Qwen GSM8K 为 inconclusive。

**W9 [warning] Missing references: StreamingLLM (ICLR 2024), DuoAttention (2024)**
- R2-W8 + R1 部分同意
- StreamingLLM 是 KV cache 奠基工作，在 KV-cache-centric 论文中缺失是明显遗漏。DuoAttention 的 retrieval/streaming head classification 与 §6.1 structural specificity 直接互补。

### Minor

**M1** Abstract 信息密度过高（>15 个数字, 5 CI, 4 p-value），首次阅读不友好。建议精简到 2-3 key numbers。[R1-W10, R2-M1]

**M2** 术语变体残留："importance discrimination collapse" / "score collapse" / "score distribution collapse toward uniformity"。需统一。[R2-M2]

**M3** appendix_moved.tex 和 references.bib 保留内部追踪注释，应删除。[R2-M3, linked R8-M1]

**M4** Conclusion "extending to code/science reasoning" 但 GSM8K 已显示 benchmark 间形态差异大（quantitative → qualitative specificity shift），跨领域泛化承诺可能过于乐观。[R2-M4, R1 rebuts: future work framing appropriate]

**M5** CI inconsistency: Table 2 Qwen s=0.30 Δ CI = [2.80, 3.56] vs Table 3 = [2.78, 3.56]。Bootstrap 采样变异，但应统一。[R2-W7, R1 rebuts as minor]

**M6** Spearman ρ=1.0 (n=4) 无增量信息价值，建议删除或更强标注。[R1-W8]

**M7** Table 2 Qwen s=0.15 G "n.d." 含义虽有脚注解释但 readability 可改善（建议改 "undef."）。[R1-W9, R2 rebuts: footnote sufficient]

**M8** 4 个 bib entries (defensivekv-iclr2026, hies-2025, phase-transition-compression-2026, mustafar-neurips2025) 在 OpenAlex 未检索到，需 double-check venue 信息。[R2 Reference Verification]

**M9** 主文可能超 8 页限制（自 R8-M3 未验证），desk-reject 风险。[R8-M3]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全共识：

1. **Phase segmentation proxy 有效性未验证**（W1）— 核心方法论缺陷，DeepSeek `<think>` token 可做 ground-truth validation 但未做
2. **缺乏 accuracy 验证 + 93.2% 答案 token 天然屏蔽**（W2）— 实际部署意义存疑
3. **标题过度泛化**（W4）— 实测仅 Qwen2-family 7B + preliminary LLaMA
4. **Novelty 有 Findings-level 价值但不足以支撑 main conference**（W3）— statistical confirmation of expected interaction
5. **统计方法论是本文最强部分**（S2）— 超出同类论文水准

## Reviewer Divergence [REBUT]

分歧均为 minor，不影响整体判断：

| 问题 | R1 | R2 | 收敛结果 |
|------|----|----|----------|
| R2-W3 "controlled comparison" | 部分反驳：quasi-experimental, 措辞修正 | Critical | Compromise: "within-architecture-family comparison" |
| R1-W6 Bonferroni family size | Should-fix | 反驳：§4 已说明，BH-FDR 覆盖 | 写作清晰度问题非方法论错误 |
| R1-W7 IDC overframing | Should-fix | 反驳：§6 hedging 充分 | Hedging adequate, minor prominence concern |
| R2-W7 CI inconsistency | — | Should-fix | R1 rebuts: bootstrap variability, minor |
| R2-M4 Future work | — | Minor | R1 rebuts: future work framing appropriate |

---

## Questions（需作者澄清）

**Q1** DeepSeek 有 `<think>` token，是否已做 sparsity-based vs `<think>`-based segmentation 的一致性分析但未报告？如未做，技术障碍是什么？

**Q2** Phase segmentation 在 dense model 上计算——compound sparsity 下 attention 分布一致性是否验证过？如果 pruning-induced ΔH = -0.04 改变了 phase 边界，II 按 "旧" phase 统计是否引入偏差？

**Q3** MATH-500 上 compound sparsity 对最终 accuracy（\boxed{} 答案正确率）到底下降多少？问题级别的 accuracy 数据应 readily available。

**Q4** Pilot mitigation oracle 仅恢复 18%——是否暗示 phase-aware budget allocation 方向本身不可行？如果是，Discussion 的 implication 需要根本重写。

**Q5** G per-problem 定义中 II_high ≤ 0 时（bfloat16 noise）如何处理？是否排除这些 data points？这影响多少比例的数据？

---

## Missing References

1. **StreamingLLM** (Xiao et al., ICLR 2024) — KV cache 奠基工作，在以 KV cache eviction 为核心变量的论文中不应缺失
2. **DuoAttention** (Xiao et al., 2024) — retrieval/streaming head classification 与 §6.1 structural specificity（importance-pruned heads 的 Gini 特征）直接互补

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。

---

## Overall Assessment

**Overall Score**: **borderline**
**置信度**: 4/5（两位 Reviewer 仔细阅读全文及所有附录，交叉分享后高度收敛）

**推荐**: Findings track，而非 Main Conference。

**理由**:

论文在方法论层面表现出色——统计分析严谨、robustness 验证全面、hedging 诚实，是 compound sparsity 领域少见的高透明度实证分析。然而，四个因素共同阻碍主会议接收：

1. **Novelty 深度不足**：核心发现（phase-dependent compound severity）的方向性可从已有文献 qualitatively predict，定量贡献（monotonic dose-response + model-dependent crossover）是 statistical confirmation 而非 conceptual surprise。

2. **核心 proxy 未验证**：attention sparsity ↔ reasoning phase 的语义映射缺乏 ground-truth 验证（DeepSeek `<think>` token 可用但未用），且 dense-model-based segmentation 存在 label-outcome coupling。

3. **实际意义存疑**：93.2% 答案 token 天然屏蔽于 G≈1 phase，缺乏 accuracy 验证使 "severity gradient 影响部署" 的暗示缺乏证据支持。

4. **实验范围窄**：2 个同架构模型 (Qwen2ForCausalLM) + 1 个 preliminary LLaMA (n=49, ~1/40 effect) + 1 个 benchmark (MATH-500, GSM8K n=50 补充)，但标题声称 "Mathematical Reasoning Models"。

**R1 评分**: 3.0/5 Findings-level accept (Soundness 3.5, Excitement 2.5)
**R2 评分**: Borderline 2-3, Findings track (Soundness 3, Excitement 2)

**如果以下问题在 camera-ready 前解决，评分可提升至 weak accept**:
- W1: `<think>` token ground-truth validation
- W2: MATH-500 accuracy evaluation (16 conditions)
- W4: 标题限定为 Qwen2-family 或 7B-scale

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（>15 数字）。建议保留 Δ range, G range, 1 key p-value，其余移至 §5。
- "preliminary cross-architecture evidence from a LlamaForCausalLM" 给读者印象超出 n=49/~1/40 effect 的实际证据强度。

### §1 Introduction
- Novelty 论证结构已从 R8 的 "linear combination strawman" 改进为 "What does compound interaction add beyond single-axis findings?"——结构合理但核心问题（novelty depth）未解决。
- Contribution 1 "3–17×" 已正确限定为 significant-only range with footnote。

### §2 Related Work
- 覆盖全面（38 references），ThinK/ForesightKV/PtQ 已补充。
- 缺少 StreamingLLM 和 DuoAttention。
- 4 个近期 bib entries 需 double-check venue info。

### §3 Background
- "Conservative baseline" 论证合理（比 R8 的 "disjoint dimensions" 大幅改进）。
- Causal coupling 已 acknowledged。
- Phase segmentation "operationalization choice" 讨论有但不足——需 ground-truth validation 或更透明的 trade-off 讨论。

### §4 Experimental Setup
- Factorial design 清晰。
- "Enabling controlled comparison of training paradigm effects" 措辞偏强 → "within-architecture-family comparison"。
- Bonferroni k=4 family definition 有 BH-FDR backup 但主文解释可更清晰。

### §5 Results
- 核心统计结果严谨可靠。Table 2-3 数据一致（minor CI rounding 除外）。
- §5.5 Cross-architecture (LLaMA) 正确标注 "exploratory"/"preliminary"，但在 abstract 中出现仍给过强印象。
- §5.6 GSM8K 有价值但需 power analysis + Qwen 标注 inconclusive。
- §5.7 Answer-region analysis 实际削弱 severity gradient 实用意义——需 accuracy 验证挽救。

### §6 Analysis
- "Correlational diagnostics that do not fully explain" framing 现在恰当。
- Structural specificity evidence (r=0.62-0.76) 有说服力但 Frobenius/Gini magnitude sensitivity 的 partial circularity 已 acknowledged。
- Entropy redistribution 2/4 Qwen replication 如实报告。

### §7 Discussion
- "Could inform phase-aware budget allocation" 与 pilot 18% recovery 矛盾。需加 caveat。

### §8 Conclusion
- "Extending to code/science reasoning" 在 GSM8K 已显示形态差异的情况下应 tone down。

### Limitations
- 覆盖 7 维度（scale, architecture, task, mechanism, metric, range, throughput），全面。
- "Perplexity vs accuracy" 段落坦承但应更强调这是 acceptance-blocking gap。

### Appendix
- 内容丰富（multiplicative null, permutation, cross-arch, discrimination collapse, segmentation robustness, asymmetric, outlier, GSM8K, BH-FDR）。
- 残留内部注释需清除。
- Multiplicative null G_× 需用 per-problem methodology 重算。