---
round: 10
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T11:56:04.908239+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 Consolidated Review Report

## Summary

本文系统研究 model collapse（语言模型在自身输出上迭代训练导致的退化）的可检测性，通过在 contamination ratio (α) 和训练代数 (T) 构成的二维空间上映射"检测景观"。使用 permutation Granger causality (PermG) 作为核心统计工具，应用于 canary metrics（token entropy, distinct-n diversity），刻画检测边界、识别四种检测 regime，并展示 proof-of-concept 干预。在五个模型族上进行跨架构验证。目标投稿 EMNLP 2026 (ARR)。

## Strengths

1. **系统性实验设计**：首次在密集 (α, T) 网格（13 个 α 值 × 多个 T 值）上映射 model collapse 可检测性。Robustness 验证全面：specification curve analysis (1,160 configurations)、Shapley value decomposition、power simulation、CUSUM comparison、transfer entropy analysis。

2. **方法论严谨度高于领域平均**：Multi-seed replication、BH-FDR correction、multi-method consensus test (MMCT)、leave-one-T-out cross-validation。执行质量超过该领域多数现有工作。

3. **方法敏感性的警示价值**：同一数据上五种统计方法给出截然不同结论（从 universal detection 到 complete null），对后续工作有真正的警示意义——不能依赖单一检验下结论。

4. **Phase diagram 可视化**：Figure 1 热力图有效压缩复杂多维结果为直观视觉，提供清晰的检测"地图"。

5. **可重复性**：实验细节详尽（超参、seed、FDR 阈值），附录提供完整 specification curve 和消融分析。

## Weaknesses

### Must-Fix（5 个，共识）

**MF-1** [Consensus AGREE] **Abstract 模型规模范围事实性错误**
Abstract 声称 "345M–6.9B" 但 Table 2 (p.8) 最大模型为 SmolLM3-3B (~3B)。Limitations (p.9) 明确声明 ">7B is untested"。"Five families" 同样夸大——Table 2 仅含 3 个可辨识独立 family (Pythia, GPT-2, SmolLM3)；同 family 不同 scale 不构成独立 family。Abstract 中的事实性错误。
*Tracker: R10-MF5 + F2-W2b*

**MF-2** [Consensus AGREE] **"Detectability Landscape" 承诺超过交付**
完整 (α, T) grid 仅存在于 Pythia-410M。跨架构验证仅覆盖 α=1.0（最极端条件）。4/15 跨架构条件不支持 forward detection（27% 失败率）。Title "Characterizing the Detectability Landscape" 暗示通用性，但实验证据不支持。Abstract 应明确将 landscape scope 限定于 Pythia-410M 并注明跨架构局限性。
*Tracker: F2-W2b（Round 2→10，持续 open）*

**MF-3** [Consensus AGREE] **PermG FPR CI [1.2%, 30.4%] 动摇方法推荐**
点估计 11.1% 已超标准 5% 阈值。CI 上界 30.4% 意味着最坏情况 ~1/3 null condition false reject。GPT-2 medium FPR=50% 揭示 architecture-dependence。削弱 Section 6 整个方法推荐框架的可信度。论文承认 FPR>5% 但未充分讨论 CI 对实际使用的影响。
*Tracker: F3-J4（Round 3→10，持续 open）*

**MF-4** [Consensus AGREE] **Power-law 检测边界统计基础薄弱**
α_c(T) = A·T^{-γ} 用 2 参数拟合仅 11 个数据点（排除 ~25% sync-dip cells 后）。此样本量下 R²=0.969 无说服力。γ CI 跨 [0.24, 0.78]（3× 范围）。未与更简单替代模型（linear, log-linear）进行 AIC/BIC 正式比较。LOO-CV MAE=0.037 未报告 CI 宽度分布。仍以 "Proposition 3" 形式呈现，此前多轮已要求降级。
*Tracker: F2-W4b + F2-W6（Round 2→10，持续 open）*

**MF-5** [Consensus AGREE] **Intervention 证据不足但高调呈现**
Section 5.6 intervention 仅在 N=2 seeds、α=1.0（最极端条件）、Pythia-410M 上测试，无置信区间。Abstract 中 "64% perplexity reduction" 给人稳健通用结论的印象。Seed variability 证据（Table 8: seed 42 p=0.001 vs seed 43 p=0.058）说明 N=2 不足。至少应在 abstract 加 "proof-of-concept" 限定词。
*Tracker: F2-W7（Round 2→10，持续 open）*

### Should-Fix（7 个）

**SF-1** [Partial Consensus] **Design Principles overclaimed as "formal/theoretical"**
R2 判定循环论证（经验证据 = 待证结论）；R1 部分反驳（结构是标准假说-演绎法，非循环），但同意 "formal design rationale" 过度。Appendix X propositions 依赖未独立验证的 mode amplification 假设。SmolLM3-3B non-monotonic entropy 可能是假设失效实例。共识：从 "formal design rationale" / "theoretical contribution" 降级为 "theoretically motivated, empirically validated design principles"，不与实证贡献并列为同等权重。
*Tracker: F5-N1 + F5-W1（Round 5→10）*

**SF-2** [Consensus AGREE] **Sync-dip 解释是 post-hoc**
Canary-triggered cessation 机制是实验设计的产物（基于人工设定的 entropy threshold），非通用 regime。排除 sync-dip cells 后声称 "15/15 match theory" 是方法论上的 cherry-picking。应重新定位为 setting-specific artifact 或提供其他训练协议中也存在的证据。
*Tracker: F2-W1（Round 2→10）*

**SF-3** [Consensus AGREE] **Bivariate confounding 替代解释不足**
Entropy 和 diversity 可能同受 underlying distribution shift 驱动，entropy 作为连续指标的测量灵敏度天然高于 diversity 的离散 n-gram 阈值。观察到的 "entropy leads diversity" 可能仅反映灵敏度差异而非因果先后。论文讨论不足。
*Tracker: R10-SF5（新）*

**SF-4** [Partial Consensus] **方法敏感性 "3%–92%" framing 有误导性**
NaiveXCorr FPR=91.7% 是失效方法而非"敏感"方法。R1 部分反驳：纳入有警示价值，但同意 abstract "3% to 92%" framing 暗示五种方法形成连续谱，实际是 4 合格方法 (2.8%–38.9%) + 1 失效方法。共识：保留正文分析，修正 abstract 表述区分 "失效基线" 与 "合格方法间的真正 sensitivity"。
*Tracker: R10-SF4（新）*

**SF-5** [Consensus AGREE] **缺少与 AI text detection 文献的联系**
Related Work (§2) 完全未提及 AI-generated text detection (DetectGPT 等)。Single-generation token-level detection vs. multi-generation distributional detection 是值得讨论的关键区别。遗漏可能被 reviewer 标记为重大 gap。
*Tracker: R10-REF2*

**SF-6** [Consensus AGREE] **每 cell 仅 8 pairs → 极宽 binomial CI**
6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]。Phase diagram 相邻 cell 差异可能在统计上不显著，削弱 "sharp onset" narrative (§5.2)。
*Tracker: R10-SF6（新）*

**SF-7** [Consensus AGREE] **3-4 seeds replication power 有限**
Seed variability 有记录（Table 8）但未系统量化。Specification curve (1,160 configs) 部分补偿，但评估的是方法稳健性而非采样稳健性。
*Tracker: R10-SF7（新）*

### Minor Issues（9 个）

- **m1**: Figure 3 y 轴标签 "FDR-significant pairs" 需括注说明（如 "out of 8 canary→downstream pairs"）[R2-m1, R1 AGREE]
- **m2**: Table 2 "x/8" 列含义未在 table caption 定义（定义在 Figure 1 caption，相隔 5 页）[R2-m2, R1 partial]
- **m3**: §5.1 前向引用 "five families (§5.5)" 首次出现时缺上下文 [R2-m3, R1 AGREE]
- **m4**: Granger precedence vs. causality 术语——R2 认为不一致，R1 反驳（PermG 是文献标准名称，论文已三层处理）。共识：§3/§4 开头增加 1-2 句澄清 [DIVERGENCE]
- **m5**: 小样本 bootstrap CI 可靠性应标注 caveat [R1-m5, R2 AGREE]
- **m6**: BH-FDR PRDS 假设——R1 标为 should-fix，R2 反驳：K=8 下 BH vs BY 差异 ~log(8)≈2× 调整，应降为 minor。共识：minor，加一句说明 [R1-SF-3 降级]
- **m7**: Figure 1 legend 符号偏小，打印分辨率下勉强可读 [visual check]
- **m8**: 第 1-2 页和第 4-5 页连续纯文本无 display item，"文字墙"第一印象 [visual check]
- **m9**: Appendix 18 页 (~3× 正文)——R2 认为增加审阅负担，R1 反驳（ARR 无长度限制，thoroughness 是优点）[DIVERGENCE]

## Reviewer Consensus

两位 Reviewer 独立给出 **Overall 3.5 (Borderline Conference)**，在以下核心问题上高度一致：

1. **系统性 overclaim 模式**：Abstract/Title 承诺超过实验交付（模型规模范围、landscape 通用性、intervention 稳健性）
2. **统计基础需加强**：PermG FPR CI 过宽不足以支撑推荐、power-law boundary 拟合不足、全文多处小样本
3. **执行质量是真正优势**：实验方法论、robustness 验证、文档记录高于领域平均
4. **存在接收路径**：如修正 overclaim 并诚实呈现统计 caveat，实证贡献足以达到 Conference 水平

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | 结论 |
|------|---------|---------|------|
| Design Principles 循环论证 (R2-N3) | 标准假说-演绎法，非循环；但 "formal" 过度 | 循环论证：经验证据 = 待证结论 | 部分收敛：均同意 overclaimed，对机制有分歧 |
| NaiveXCorr 纳入 (R2-W2) | 纳入有真正警示价值；但 abstract framing 误导 | 失效方法不应与合格方法并列 | 部分收敛：保留正文，修正 abstract framing |
| Granger 术语 (R2-W4) | 论文术语 disciplined；PermG 是标准名称 | 不一致，对 NLP 读者困惑 | Minor 分歧：加澄清句 |
| Appendix 长度 (R2-m4) | Thoroughness 支持 reproducibility；ARR 无限制 | 审阅负担；部分 appendix 是 extras | Minor 分歧：不可操作 |
| Excitement | 3.5（问题及时性） | 3.0（标准工具，新颖性有限） | 分歧 |

## Questions for Authors

1. 为什么跨架构验证仅在 α=1.0 下进行？能否对一个非 Pythia 架构补充 3-5 个中间 α 值以支撑 "landscape" claim？
2. Sync-dip 在 Pythia-1.4B 上是否也存在？如果是 scale-dependent，对 four-regime narrative 意味什么？
3. 实际部署中（无 canary-triggered cessation），PermG 的检测价值如何体现？
4. 鉴于 FPR 从 2.8% 到 91.7%，是否考虑过 MMCT 按 FPR 控制能力加权投票？
5. 能否提供 power-law vs. linear/log-linear boundary model 的 AIC/BIC 比较？
6. 在 data accumulation（vs. replacement）和 lower-temperature decoding 下，检测边界的预期方向如何？

## Missing References

两位 Reviewer 共识：
- **Mitchell et al. (2023)** "DetectGPT" — AI text detection，方法论相邻
- **Runge et al. (2019)** — 短时间序列因果发现，与 T≤25 设置直接相关
- **Padmakumar et al. (2024)** — LM 对文本多样性影响的互补视角
- **Montgomery "Statistical Quality Control"** — SPC 框架，与 CUSUM 讨论相关
- **Steegen et al. (2016)** — Multiverse analysis，与 specification curve (Appendix E) 直接相关
- **Hataya et al. (2023)** — ICCV model collapse（image generation 视角）
- **Gerstgrasser et al. (2024)** — Data accumulation vs. replacement paradigm

## External Review (Stanford Agentic Reviewer)

未请求外部审稿。

## Visual Layout Check（非评分项）

**状态: 已完成**（耗时 ~5 分钟）

- **[CRITICAL]** 第 9 页：Discussion §6 "Broader implications" 段落溢出到第 9 页顶部，属主文内容（非 Limitations/Ethics），可能违反 EMNLP 2026 八页主文限制。需压缩 Discussion 至第 8 页内或将该段移入不计页数区域。
- **[WARNING]** 第 1-2 页：连续 2 页纯文本无 display item，Figure 1 直到第 3 页。审稿人前 2 分钟无视觉锚点。
- **[WARNING]** 第 4-5 页：Method §4 + Experiments §5.1 连续密集文本，Table 1 直到第 6 页。
- **[INFO]** Figure 1 legend 符号偏小（150dpi 勉强可读）；Figure 2 axis tick labels 约正文 60-65%，接近可读下限。色盲友好度尚可。全文无 margin overflow、LaTeX 错误残留。

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3 | 3.5 | 3 |
| Excitement | 3.5 | 3 | 3 |
| Reproducibility | — | 4 | 4 |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | — | 4 | 4 |

**判断依据**：实证贡献扎实（系统性 landscape mapping + 方法敏感性警示），但存在系统性 overclaim 模式（Abstract 模型规模虚报、landscape 通用性暗示、intervention 证据强度夸大），统计基础在多处偏弱（PermG FPR CI、power-law 拟合、小样本），方法新颖性有限（标准计量经济学工具的领域迁移）。

**如果作者能**：(1) 修正所有事实性错误；(2) 将 Title/Abstract scope 收窄至实际覆盖范围；(3) 将 Design Principles 从 "theoretical contribution" 降级；(4) 在正文中诚实讨论 PermG FPR CI 和 boundary model 局限性；(5) 给 intervention 加 "proof-of-concept" 限定——论文有潜力达到 4.0 (Conference) 水平。当前状态为 Borderline Conference。

**Confidence: 4/5** — 两位 Reviewer 均熟悉 model collapse 文献和 Granger causality 方法论，核心判断高度一致。

## Detailed Comments（逐节）

### Abstract
- 修正 "345M–6.9B" 为实际范围 (~345M–3B)
- 修正 "five families" 为准确数量
- "3% to 92%" framing 应区分失效方法与合格方法
- "64% perplexity reduction" 加 "proof-of-concept" 限定

### §1 Introduction
- Contribution 2 的 "formal design rationale" 降级为 "empirically grounded design heuristics"
- Contribution 3 的 "power-law" 限定统计支撑程度

### §2 Related Work
- 增加与 AI text detection 文献的定位讨论（single-generation vs. multi-generation）
- 增加 data accumulation vs. replacement paradigm 讨论

### §3 Design Rationale
- "Design Principles" 框架降级，不使用 "formal" / "theoretical contribution" 措辞
- 标注 mode amplification 假设的局限性和适用条件

### §4 Method
- PermG FPR CI [1.2%, 30.4%] 在正文中讨论含义（而非仅在附录引用）
- "Five statistical methods" 比较中区分合格方法与失效基线
- Proposition 3 从 "Proposition" 降级为 empirical observation

### §5 Experiments
- 明确 primary landscape 来自 Pythia-410M
- Cross-architecture 27% 失败率在叙述中呈现
- Sync-dip 定位为 setting-specific artifact
- Intervention 加充分 scope limitation

### §6 Discussion
- 压缩至第 8 页内（视觉审查 critical finding）
- 增加 accumulation vs. replacement 定性讨论
- 增加 decoding strategy 影响定性讨论

### Limitations
- 模型规模上界与 abstract 一致
- 补充 single decoding strategy 讨论
- bf16/fp32 precision sensitivity 加一句

### References
- 补充 7 篇缺失引用