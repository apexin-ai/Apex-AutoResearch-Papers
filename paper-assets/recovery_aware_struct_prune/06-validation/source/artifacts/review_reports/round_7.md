---
round: 7
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T17:16:29.519417+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 7 Consolidated Review Report

**Paper**: How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs
**Venue**: EMNLP 2026 (via ARR)
**Reviewers**: 2 (R1: 方法严谨性 + 统计, R2: 新颖性 + 完整性)
**Rounds**: 1 (converged after cross-sharing)

---

## Summary

本文系统比较四种结构化 MLP 剪枝标准（CKA-only, Standard/importance, RASP, Random）在 reasoning LLM（DeepSeek-R1-Distill-Qwen-7B）上的 post-pruning recovery 表现。核心发现包括：(1) 剪枝标准比恢复方法（SFT vs GRPO）更显著地影响恢复质量，建立 "recovery capacity spectrum"；(2) 在 20-25% sparsity 下，不同标准的 GRPO accuracy 增量均 <1pp（reward-accuracy decoupling）；(3) CKA 权重 α 与恢复能力呈 inverted-U 关系。论文采用控制实验设计，固定除剪枝标准外的所有变量。

---

## Strengths

**S1. 实验设计理念优秀**：固定 recovery pipeline、超参数、硬件、calibration 数据，仅变化剪枝标准的 controlled comparison 在 LLM 剪枝文献中罕见，使因果推断更可靠。

**S2. Recovery capacity spectrum 有直觉价值**：将四种标准的 GRPO 行为划分为 active learning / stagnation / collapse 三种 regime，framing 清晰实用。

**S3. 核心对比统计严谨**：CKA-only vs Standard 的 4.55pp gap 经 3-seed Welch's t-test 验证（p=0.0009, Cohen's d=11.1, 95% CI [3.62, 5.47]pp），seed 范围不重叠。

**S4. Dose-response 设计有信息量**：α 系数连续变化 + inverted-U 发现比简单 A/B 对比更强。

**S5. 写作清晰**：结构合理，notation 一致，figures 质量好，叙事连贯。

**S6. 诚实的 Limitations**：明确承认单 seed RASP、架构/尺度局限、诊断边界。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [Consensus Critical] Dose-response 中 max_completion_length 混杂变量**
- *R1-N1, R2-N1 独立提出；交叉分享后部分收敛*
- **事实核查结论**：论文存在两组不同的 generation length 配置：
  - **主实验** (Table 1/2): CKA-only/Standard/RASP 均用 1,024 tokens，仅 Random 用 512 → 混杂仅影响 Random 比较 [warning]
  - **Dose-response** (Section 4.3 脚注, experiments.tex line 102): α=1.0 用 1,024 tokens，α=0.5/2.0/3.0/4.0 用 TRL 默认 512 → 混杂直接影响 inverted-U 曲线 [critical]
- R2 在交叉回应中试图 rebut R1（声称所有非 Random 方法均用 1024），但 R2 混淆了 Table 3 脚注（主实验配置）与 experiments.tex line 102 脚注（dose-response 配置）。
- Inverted-U 峰值 α=2.0（512 tokens）vs 谷底 α=1.0（1024 tokens）的绝对差距不可靠。论文的 "conservative estimate" 论证仅解决谷底（α=1.0 用更长 generation 仍最差），不解决峰值位置和曲线形状。
- **要求**：统一所有 α 值的 max_completion_length 重跑 dose-response，或至少在 α=2.0 处用 1024 tokens 复现。

**MF2. [Consensus Critical] RASP 单 seed 验证不足**
- *R1-N2, R2-W2，双方均同意 critical*
- CKA-only/Standard/Random 各 3 seeds，RASP 所有 sparsity 和 α 值仅 1 seed。Section 5 的 practitioner guideline "Use RASP at α≈2.0" 基于单次实验。α=1.0 collapse 表明 RASP landscape 对 α 高度敏感。Standard 3-seed std=0.38pp，RASP 真实方差可能更大。
- **要求**：至少 RASP α=2.0（推荐值）和 α=1.0（collapse 点）各跑 3 seeds。

**MF3. [Consensus Critical] 因果语言系统性过强**
- *R1-N3, R2 交叉回应中同意两个子问题*
- (a) Section 5 "causal driver"：dose-response 是 quasi-experimental，变化 α 同时改变 diversity 权重、被移除结构身份和 sparsity 分布。Appendix H 自承 gradient flow 证据是 correlational。
- (b) "reward-accuracy decoupling" 作为命名 phenomenon：仅在 20-25% sparsity 成立。15% 时 GRPO 仍 amplify CKA advantage by 1.51pp。将 sparsity-dependent 观察包装为普适性 phenomenon 是 overclaiming。
- R2 建议折衷用 "key determinant"（比 R1 的 "primary correlate" 稍强，反映 dose-response 的证据强度）。
- **要求**：全文语言审计——"causal driver" → "key determinant"；所有 decoupling claims 加 "at 20-25% sparsity" 限定。

**MF4. [Consensus Critical] Abstract overclaiming "holds across sparsity levels"**
- *R1-N4, R2 完全同意*
- Abstract "a pattern that holds across sparsity levels and benchmarks" 直接与数据矛盾（15% coupling, 30% collapse）。
- **要求**：改为 "at moderate sparsity (20–25%) across benchmarks" 或类似限定。

**MF5. [Consensus Critical] Decoupling 可能是训练不足的 artifact**
- *R2-N3 提出, R1 完全同意*
- GRPO 仅训练 100 步（extended 300 步），所有条件下 GRPO accuracy 增量 <1pp（CKA-only: +0.48pp, Standard: +0.55pp）。这可能仅说明 GRPO 还没来得及产生 accuracy 分化，而非 "recovery method choice becomes irrelevant"。
- Self-Healing (2025) 在更长训练中观察到 RLVR > SFT。论文无法排除 1000+ 步训练后 decoupling 消失的可能。
- R1 交叉回应新发现强化此点：SFT 贡献 ~60pp 恢复而 GRPO <1pp，论文叙事焦点（RLVR recovery）与实际恢复来源（SFT）存在错位。
- **要求**：至少在一个条件下（CKA-only vs Standard at 20%）运行 ≥1000 GRPO steps 验证 decoupling 是否持续；或将 claim 限定为 "within ≤300 GRPO steps"。

**MF6. [R2 New Finding] CKA-only layer 分布混杂**
- *R2 交叉回应中提出，R1 小问题中间接支持*
- CKA-only 将 72.5% 剪枝集中在 early layers (L0-9)，其优势可能来自 early-layer selective pruning（保留 late-layer 推理结构）而非 "representational diversity preservation"。
- Appendix R 的 depth-first baseline 在 layer-level granularity（移除整个 transformer blocks），主实验在 MLP channel-group level——granularity 不匹配无法有效解耦两种机制。
- **要求**：创建 same-granularity layer-biased baseline（MLP channel-group level，按 layer index 赋权优先剪早期层，不使用 CKA 信息），验证 layer 分布是否足以解释 CKA-only 的优势。

### Should-Fix（影响评分但不一票否决）

**SF1. [Divergence → Downgraded] CKA evaluation metrics diversity 不足**
- *R2-N2 原定 critical（循环论证）；R1 rebut 后降级*
- R1 有效论证：pruning 用 intra-layer pairwise CKA ≠ evaluation 用 inter-model layer-wise CKA。Gradient flow analysis (2.89× magnitude, Wilcoxon p<0.05) 提供独立证据。不构成 tautology。
- 但论文主叙事仍过度依赖 CKA 家族指标。补充一个完全独立的 diversity 度量（CCA、centered distance correlation 或 effective rank）可显著增强论证。

**SF2. [Consensus] 跨架构泛化严重不足**
- *R2-W1, R1 完全同意*
- 所有模型共享 Qwen2.5 base architecture。Appendix O "Cross-Architecture Validation" 标题具有误导性。1.5B 验证也是同架构不同规模。Claim 应限定为 "Qwen2.5-family models"。

**SF3. [Consensus] Decoupling 缺少形式化等价性检验**
- *R1-W3, R2 同意*
- |Δ|=0.54pp 声称 "near-identical" 未经 TOST 或等价性检验。应定义 practical equivalence margin（如 ε=1pp）并正式检验。

**SF4. [Consensus] MBPP 不显著结果用作支持证据**
- *R1-W4, R2 同意*
- Appendix G 承认统计不显著，但 Section 4.3 仍引用 MBPP 支持 decoupling claim。应在正文加注 "though not statistically significant"。

**SF5. [Consensus] Calibration 数据量 M 未指定**
- *R1-W1, R2 同意*
- Section 3.2 定义 D_cal 但从未指定 M 值。影响 reproducibility。

**SF6. [Consensus] "Generality across scales" 证据薄弱**
- *R1-W2, R2 同意*
- 仅 1.5B 和 7B（同家族 <5× 差异）。应改为 "preliminary evidence at 1.5B scale"。

**SF7. [Consensus] Throughput regression 未在 Limitations 讨论**
- *R2-W3, R1 部分同意*
- 20% sparsity: 28% memory savings 但 19% throughput decrease (72.0→58.3 tok/s)。Limitations 报告正面指标（memory, TTFT）但回避负面指标——构成选择性报告。

**SF8. [R1 New Finding] Title/叙事焦点与恢复来源错位**
- SFT 贡献 ~60pp 恢复，GRPO <1pp。论文以 "Post-RLVR Recovery" 为标题和叙事核心，但实际恢复工作主要发生在 SFT 阶段。GRPO 的独特贡献在于 reward trajectory 差异化（非 accuracy）。建议 Discussion 分离 SFT vs GRPO 角色，考虑 title 是否应为 "Post-Pruning Recovery"。

### Minor Issues（不影响接收）

- Abstract 字数 ~190-200 words，在 200-word 限制边界——建议精简几词留余量
- Table 1 Unpruned "Reward" = 0.027 含义不直观——加脚注解释 reward scale
- Figure 2 内部标注字体偏小，打印不清晰——增大字号或精简文字
- Appendix R depth-first baseline 与主实验 granularity 不同（已由 MF6 覆盖）
- Contribution list 仅 2 项，RASP 嵌入 Contribution 2——如视为 methodological contribution 建议独立列出
- Appendix 17 sections 组织散乱——建议按 training details → main extensions → robustness → analysis 重组
- "Post-RLVR" 在 title 中可能产生误解（见 SF8）
- Ethics/AI 披露完整透明

---

## Reviewer Consensus

以下问题双方达成 [AGREE]：

1. **RASP 单 seed 是 critical issue** — practitioner guideline 基于单次实验，inverted-U peak 不可靠
2. **"Causal driver" 语言必须软化** — dose-response 提供 suggestive 但非 causal 证据；"key determinant" 为折衷方案
3. **Decoupling scope 必须限定** — 仅 20-25% sparsity 成立，非 "across sparsity levels"
4. **Abstract overclaims** — 直接与论文数据矛盾
5. **跨架构验证具有误导性** — 所有模型共享 Qwen2.5 架构
6. **Decoupling 可能是训练长度 artifact** — 100-300 GRPO 步远低于典型 RLVR 训练
7. **统计/reproducibility gaps** — Calibration M、MBPP 显著性、TOST 等价性检验

## Reviewer Divergence

**D1. Generation length confound 的范围和严重性**
- R1: Critical，声称贯穿核心实验包括 dose-response
- R2: Warning，认为仅影响 Random 比较
- **Director 裁定**：R2 对主实验的判断正确（CKA-only/Standard/RASP 均用 1024，仅 Random 用 512）。但 R2 对 dose-response 的判断有误——experiments.tex line 102 脚注明确写 "α=1.0 uses 1024; other α values use TRL default 512"。R2 将 Table 3 脚注（主实验配置）与 dose-response 配置混淆。**主实验 warning，dose-response critical。**

**D2. CKA 循环论证**
- R2: Critical — CKA-pruned 模型必然展示不同的 CKA-to-dense profile，属 tautology
- R1: Rebuts — intra-layer pairwise CKA ≠ inter-model layer-wise CKA；gradient flow (2.89×) 是独立证据
- **Director 裁定**：R1 的 rebut 技术上成立——两种 CKA 操作在不同层次，观察到的 divergence 幅度是 empirical 的。但 metrics diversity 不足的关切合理。**降级为 should-fix (SF1)。**

**D3. "Diversity > importance" 的 non-obviousness（R2-W4）**
- R2: RL 需要 exploration/diversity 是已知理论，发现不 surprising
- R1: Rebuts — pruning 文献的 prior expectation 是 importance-based > diversity-based；本文恰恰推翻此领域共识；Section 5 解释是 post-hoc rationalization 不是 prior prediction
- **Director 裁定**：R1 rebut 有说服力。Novelty 在于 empirical 推翻 importance-first 假设。**从 should-fix 列表中移除。**

---

## Questions for Authors

1. 主实验使用的 calibration 样本数量 M 是多少？
2. 是否尝试过 GRPO 训练超过 300 步？如果是，decoupling 是否持续？
3. 每层的 CKA overlap score 与 layer depth index 的 Spearman 相关系数是多少？（量化 layer-distribution confound）
4. 是否愿意在 α=2.0 处用 max_completion_length=1024 重新运行，验证 dose-response 峰值是否 robust？

---

## Missing References

本轮未发现重大遗漏。Round 6 标记的缺失引用（RL Finetunes Small Subnetworks, layer pruning limits, online rollout pruning, LaCo）已在本版论文 Related Work 中出现。

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。本轮未配置外部审稿。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-24 16:47–16:52 UTC）。**0 critical / 0 warning / 4 info**：

1. **Pages 3-4**: Method 节连续 2 页无 figure/table，仅有方程式作为视觉间断。数学密集型内容可接受，但可考虑增加 pruning criteria 对比示意图。
2. **Page 5**: Figure 2 框架概览图内部标注文字偏小，打印尺寸下可能不清晰。
3. **Page 7**: 单页含 Figure 3（三子图）+ Figure 4，视觉密度较高。功能上合理但审稿人可能感到拥挤。
4. **Pages 7-8**: Figures 3-6 集中在连续两页，与 pages 3-4 纯文本区形成节奏反差。可考虑将 Figure 5/6 移至 appendix。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Soundness: 3.0/5** | **Excitement: 3.25/5** | **Reproducibility: 3.25/5**

两位 Reviewer 独立给出一致的 3.0 评分，交叉分享后未发生实质性上调或下调。

**论文的核心价值**在于实验设计理念（controlled comparison）和两个有信息量的经验发现（recovery capacity spectrum、reward-accuracy decoupling）。统计验证在核心对比上充分。

**阻碍主会议接收的五个核心问题**：
1. Dose-response generation length 混杂变量削弱了 inverted-U 这一核心因果证据
2. 100-300 步 GRPO 远低于典型 RLVR 训练水平，decoupling 可能是训练不足的 artifact 而非结构性发现
3. RASP 单 seed 使论文的 practical recommendation 不可靠
4. 因果语言系统性过强，多处 claim 超出 quasi-experimental 证据支持
5. CKA-only layer 分布混杂（72.5% early layers）未被有效排除

**上调路径**：若 MF1（统一 generation length）、MF2（RASP 多 seed）、MF5（验证长训练下 decoupling 持续性）得到解决，可上调至 **3.5 (Borderline Conference)**。

---

## Detailed Comments

### Section 1 (Introduction)
- "diversity > importance" 的叙事线有 novelty（推翻 pruning 文献中 importance-first 假设），但需更清晰地 articulate 为什么先验预期不明确——importance-based 保留更强 reasoning capability，直觉上应给 GRPO 更好起点

### Section 3 (Method)
- Eq. 3 的 CKA overlap scoring 定义清晰
- D_cal 的 M 值需要在此处或 Section 4.1 明确指定
- Two-stage recovery pipeline 描述完整，但 "identical GRPO configuration" 的声明需注明 Random 的例外

### Section 4.1 (Recovery Capacity Spectrum)
- Table 1 设计好，spectrum framing 清晰
- RASP 单 seed vs 其他方法 3 seeds 的不对称性需要在正文中更显著标注（不仅仅是 Table 2 caption）

### Section 4.2 (Reward-Accuracy Decoupling)
- 核心发现有说服力（|Δ| < 1pp across methods），但缺少 TOST 等价性检验
- 正式命名为 "phenomenon" 需要更严格的 scope 限定
- MBPP 引用应标注统计不显著

### Section 4.3 (Dose-Response)
- Inverted-U 设计思路好，但 generation length 混杂是致命伤
- 脚注披露了差异，但不够 prominent——应在正文中 discuss

### Section 4.5 (Extended Analysis)
- CKA heatmap (Figure 5) 不构成循环论证（两种 CKA 操作层次不同），但补充非 CKA diversity 度量可显著增强
- CKA-only early-layer concentration (72.5% in L0-9) 是重要发现，应给予更充分讨论和 ablation
- 300-step 延长训练仍然太短——1000+ 步是验证 decoupling 持续性的最低要求

### Section 5 (Conclusion)
- "causal driver" → "key determinant"
- Practitioner guideline 应加 caveat（single seed）
- 建议增加 SFT vs GRPO 角色分离的讨论
- Throughput regression 应加入 limitations

### Appendix
- 内容详实但组织可改进
- Appendix O "Cross-Architecture" 标题需重命名
- Appendix R depth-first baseline 因 granularity 不匹配价值有限（已在 MF6 讨论）