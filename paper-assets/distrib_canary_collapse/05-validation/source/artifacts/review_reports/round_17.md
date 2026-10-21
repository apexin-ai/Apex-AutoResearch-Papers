---
round: 17
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-25T21:38:43.418615+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 审稿报告

**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse
**Venue**: EMNLP 2026 Long Paper (via ARR)
**ARR Submission Deadline**: 2026-05-25 (AoE)
**Commitment Deadline**: 2026-08-02
**审稿模式**: fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法严谨性 / R2 新颖性与完整性）

---

## Summary

本文系统绘制了迭代 model collapse 的"可检测性景观"——在 contamination fraction (α)、observation window (T) 和统计方法三个维度上映射检测能力。核心实验基于 Pythia-410M + WikiText-103，通过 5 种 lead-lag 检测方法在 13 个 α 水平上的系统比较，发现：(1) 在 α_c ≈ 0.50 处存在陡峭检测跃迁（PermG 从 0/8 跃至 6/8）；(2) 检测边界随 T 增长左移；(3) 五方法 FPR 跨度 6.7%–94.4%，显示方法选择决定结论；(4) token entropy 以 ≥1 代领先于 diversity 下降，支持 proof-of-concept 干预（降低 64% 峰值困惑度）。跨架构评估在 α=1.0 下覆盖 5 个模型族（345M–6.9B），11/15 conditions 确认前向检测。

---

## Strengths

1. **S1 [Consensus]** Detectability landscape 框架首创性：将 model collapse 检测从"能否检测"推进到"在什么条件下能检测"的系统化分析，phase diagram（Figure 1）是有效的概念贡献。

2. **S2 [Consensus]** 多方法系统比较：首次在 model collapse 领域对 5 种检测方法做同数据对比，配合 BH-FDR 校正、Shapley 分解和 specification curve（288 configurations），填补了实验空白。

3. **S3 [Consensus]** 方法灵敏度发现（FPR 6.7%–94.4%, κ=0.187）是重要实践警示，表明单方法分析不可靠，对领域后续工作有直接指导价值。

4. **S4 [Consensus]** 实验规模充分（~1,500 统计检验，5 模型族，multi-seed replication），统计方法严谨（置换检验、bootstrap CI、FDR 校正）。

5. **S5 [Consensus]** 附录深度模范级别（37 页），几乎每个潜在质疑都有对应 robustness 检查。匿名代码链接、详细超参数、种子策略清晰，复现文档完备。

6. **S6 [R1]** Cascade ordering 形式化（Observations 1–2）逻辑清晰，从 mode amplification 假设出发推导，提供可测试理论预测。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**MF1 [Consensus: R1-N1 critical, R2 AGREE]** "Within 2 percentage points" 陡峭跃迁 claim 源自 sigmoid 模型拟合而非直接观测。
- 实际 α 网格分辨率为 5pp（0.45→0.50），"2pp"来自 Appendix S 的 sigmoid 回归拟合（k=15.7, Δα=0.028, 用 7 个数据点拟合 3 个参数）。将模型推断精度呈现为实验观测精度属于 overclaim。这是论文的 headline claim（Abstract, Introduction, Conclusion 均引用），精度失实会直接传播到后续文献。
- **Action**: 改为 "between α=0.45 and α=0.50 (5 percentage points)" 或补充 α∈[0.46, 0.49] 的密集采样。

**MF2 [Consensus: R1-N2 critical, R2 AGREE]** Power-law 检测边界 α_c(T) = A·T^{-η} 严重过度拟合。
- 3–4 个数据点拟合 3 个自由参数（A, η, σ），η 95% CI [0.64, 2.08] 跨越一个数量级，无法区分 sub-linear 和 super-linear 衰减。论文自身承认 "wide enough to preclude distinguishing"（p.5），但仍将 power-law boundary 作为 Contribution 2 呈现。
- **Action**: 降级为定性观察（"检测边界随 T 下移"），或增加 T 采样点至 ≥8 使拟合有统计意义。
- **跨轮追踪**: 此问题自 Round 2 (F2-W4b) 持续存在，15 轮仍 in_progress。

**MF3 [Consensus: R1-N3 critical, R2 AGREE]** FPR 估计精度不足以支撑 "controlled FPR" claim。
- PermG FPR 6.7% 基于 ~60 null-control 测试，95% CI [1.8%, 16.2%]，上界超过名义 5% 水平的 3 倍。论文不应声称 FPR 是 "controlled" 的。MMCT 的 FPR-inverse 权重也受 FPR 估计不确定性影响（PermG w≈14.9 vs NaiveXCorr w≈1.06 的差异可能被 CI 覆盖）。
- **Action**: 增加 null-control seeds 至 30–50 以收窄 CI；或弱化 "controlled FPR" 措辞，附 CI。
- **跨轮追踪**: 自 Round 3 (F3-J4) 持续存在。

**MF4 [Consensus: R2-N1 critical, R1 AGREE with nuance]** 核心技术贡献的新颖性有限。
- 五种方法（NaiveXCorr, DiffXCorr, ThresholdOnset, PermG, Toda-Yamamoto）均为成熟统计方法的直接应用。MMCT 的 FPR-inverse weighting 是标准逆误差加权方案。R1 承认实验设计框架有概念新颖性（phase diagram, Shapley 分解），但同意这更适合 Findings 而非 Conference。
- **Action**: 明确定位为 empirical study/benchmark；或开发针对 model collapse 短序列特性的定制方法。
- **跨轮追踪**: 自 Round 5 (F5-N1) 起为结构性天花板（wont_fix），但每轮重新出现。

**MF5 [Consensus: R2-N2 critical, R1 AGREE]** Blind zone（α<0.50）与论文 early-warning 动机存在根本张力。
- Introduction 引用 Dohmatob et al. (2025) 的 "vanishingly small synthetic fractions can trigger collapse"，但框架在 α<0.50 时完全失效（0/8），此时 distinct-1 已下降 ~40%（Table 4）。论文动机（early warning）与核心发现（仅 α≥0.50 可检测）之间存在根本矛盾。当前 Limitations 仅一句话提及，Discussion 的 "confirmation tool" 定位未前移到 Abstract/Introduction。
- **Action**: Abstract/Introduction 中预告 blind zone 并重新框定 scope 为 "detection feasibility boundary characterization" 而非 "early-warning tool"。
- **跨轮追踪**: 自 Round 14 (R14-N1) 持续存在。

**MF6 [Consensus: R2-N3 critical, R1 AGREE with reservation]** "Detectability landscape" 覆盖范围窄于论文标题暗示。
- 核心 phase diagram 仅基于 Pythia-410M + WikiText-103 + full-replacement。跨架构验证仅在 α=1.0（最有利条件）。α_c ≈ 0.50 的检测边界是否跨架构成立完全未测试。R1 的 reservation：论文沿 α × T 两维展开 + 288-configuration specification curve，比单纯 dose-response 更丰富，但在架构维度上未充分探索。
- **Action**: 至少在 1–2 个额外架构上测试 α∈{0.25, 0.50, 0.75} 的检测边界；或调整标题/claim 范围。
- **跨轮追踪**: 自 Round 2 (F2-W2b) 持续存在，16 轮仍 in_progress。

### Should-Fix（影响评分但不一票否决）

**SF1 [Consensus]** 3 seeds 不足以支撑 phase diagram 可靠性。Appendix R 的 per-seed FPR 分析显示 seed 间变异显著（seeds 45, 50 贡献所有 4 个 false positives）。在检测边界附近（α=0.45–0.50），结论可能完全取决于种子选择。

**SF2 [Consensus]** α=0.60 non-monotonic anomaly 的 "temporal lag compression" 解释为 post-hoc conjecture，缺乏独立实验验证（如合成 DGP 实验或更多 seeds 的复现性检验）。

**SF3 [Consensus]** Intervention 实验 scope 过窄——仅 α=1.0（最极端条件）、2 seeds。"reducing peak perplexity by 64%" 的 claim 不能推广到更现实的 α 值。

**SF4 [R2, R1 AGREE with nuance]** Cascade ordering 新颖性有限：连续度量（entropy）先于离散度量（distinct-n）响应在数学上是预期行为。R1 认为经验量化（lag ≥1 gen, 跨 seed 一致性）仍有价值但不构成独立贡献。

**SF5 [R2, R1 AGREE]** SmolLM3-3B 违反 cascade ordering 核心假设（entropy 不单调下降），5 架构中 1 个（20%），但正文讨论不足。缺乏 fallback 策略和先验判断新架构是否符合假设的方法。

**SF6 [Divergence: R2 raise, R1 REBUT]** Full-replacement 范式限制生态效度。R1 反驳：full-replacement 是 Shumailov et al. (2024), Dohmatob et al. (2025) 等核心文献的标准范式，且 α<1.0 时已模拟混合场景。记录为分歧。

**SF7 [Divergence: R2 raise, R1 REBUT]** Appendix-to-main-text 比例（~3.4:1）。R1 反驳：ACL/ARR 格式鼓励长附录，正文自包含则附录深度是优点。记录为分歧。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致或仅有细微差异：

1. **[AGREE]** "2pp" transition width 来自模型拟合，不是直接观测（MF1）
2. **[AGREE]** Power-law boundary 过度拟合，无统计约束力（MF2）
3. **[AGREE]** FPR CI 过宽，不能声称 "controlled"（MF3）
4. **[AGREE with nuance]** 方法新颖性有限，适合 Findings 而非 Conference（MF4）
5. **[AGREE]** Blind zone 与 early-warning 动机存在张力（MF5）
6. **[AGREE with reservation]** Landscape 覆盖范围窄于标题暗示（MF6）
7. **[AGREE]** 跨架构仅 α=1.0 不足以验证检测边界泛化性（SF1 related）
8. **[AGREE]** 3 seeds 偏少（SF1）
9. **[AGREE]** α=0.60 anomaly 解释为 post-hoc（SF2）
10. **[AGREE]** Intervention scope 过窄（SF3）
11. **[AGREE]** SmolLM3-3B 违反核心假设讨论不足（SF5）

---

## Reviewer Divergence

1. **Full-replacement 范式**（SF6）: R2 认为限制生态效度；R1 反驳为领域标准范式，论文不应因遵循标准做法受罚。
2. **Appendix 比例**（SF7）: R2 认为正文过于压缩、关键内容依赖附录；R1 认为正文自包含、长附录是深度 robustness 检查的体现、是优点。

两处分歧均为 Should-Fix 级别，不影响 Must-Fix 共识和 Overall 评分。

---

## Questions for Authors

1. **FPR seed 数量不一致**: 主文说 "10 seeds"，Appendix R 说 "nine seeds (54 pairs, 6-pair basis)"。请确认。
2. **Sigmoid 拟合过拟合风险**: 7 个 α 值、3 参数拟合的 sigmoid 回归，如何排除过拟合？是否对每个 seed 分别拟合？
3. **SmolLM3-3B 框架适配**: MMCT 在 cascade ordering 不成立时应如何部署？是否有 pre-deployment calibration 协议？
4. **Blind zone 内的替代方案**: 5 种方法在 α<0.50 全部失败是否反映基本统计 power 限制？是否有方法组合能检测 weak signal？
5. **First-differencing 的 power 损失**: Appendix O 显示 power 下降 ~33%。如果使用 raw PermG（接受更高 FPR），α_c 是否会下移？这是一个值得正文讨论的 power-FPR tradeoff。
6. **跨架构检测边界**: 是否测试过非 Pythia 架构在 α<1.0 时的检测边界？Pythia-1.4B 的 α-sweep 数据是否可用？
7. **Partial replacement**: Full-replacement 下每代生成最大分离的合成语料。在 partial replacement 下检测边界预计如何移动？

---

## Missing References

1. **Watermarking 对比不足** [Consensus]: Section 2.1 仅一句话区分 reactive（本文）vs proactive（watermarking）检测。应讨论为何在 watermarking 可用时仍需 reactive 检测（legacy 数据、第三方数据不可控等场景）。
2. **Data provenance / data attribution 文献缺失** [R2, R1 AGREE]: 在检测训练数据是否被合成数据污染的问题上，influence functions 等 data attribution 方法是相关替代路径，未讨论。
3. **arXiv:2410.12341** [R2]: "Characterizing Model Collapse Using Semantic Networks"——使用语义网络视角，与本文 token-level 统计度量互补。需验证引用真实性。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。项目配置中未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: Agent 超时（300s timeout）。未生成排版审查结果。

备注：视觉审查 Agent 启动后 300 秒超时，未能完成 PDF 逐页审查。用户可在需要时重新触发。从 PDF 概览来看：
- 使用 ACL review 模板，A4 页面，双栏
- 正文约 8 页（Conclusion 在第 8 页结束，Limitations 从第 8 页底部开始——不计入页数限制）
- Abstract 脚注包含匿名代码链接（R11-FMT1 历史 issue，非标准但不违规）
- 6 个 main-text figures + 2 tables + 1 algorithm，视觉密度中等偏高

---

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

**R1 评分**: 3.0 (Findings) | Soundness 3/5 | Excitement 3.5/5 | Reproducibility 4/5 | Confidence 4/5
**R2 评分**: 3.0 (Findings) | Soundness 3.5/5 | Excitement 2.5/5 | Reproducibility 4/5 | Confidence 4/5

**评分理由**:

论文的核心框架（detectability landscape）是该领域的真正概念进步，实验深度和透明度模范级别。然而，六个 Must-Fix 问题共同指向一个核心缺陷：**论文的定量 claim 精度系统性地超过了数据支撑**。

- "2pp transition width" 来自模型拟合而非观测（MF1）
- Power-law boundary 是 3 点插值不是统计回归（MF2）
- FPR 的 CI 宽度使 "controlled" 声明不成立（MF3）
- 方法新颖性有限，是成熟工具的领域应用（MF4）
- Blind zone 与 early-warning 动机的张力未在 framing 中充分承认（MF5）
- Landscape 覆盖范围窄于标题暗示（MF6）

其中 MF1–MF3 是可修复的写作/实验校准问题（调整 claim 精度、增加 null seeds、降级 power-law）。MF4（方法新颖性）是结构性天花板。MF5–MF6 需要实验扩展（跨架构 α<1.0 验证）或显著缩窄 claim 范围。

论文作为 Findings 级别的实证贡献是有价值的——首次系统比较、方法灵敏度发现、phase diagram 概念——但当前状态下核心定量结论的可信度不足以支撑 Conference 接收。

**置信度**: 高。两位 Reviewer 在所有 Must-Fix 问题上达成共识（11/13 项 [AGREE]，0 项存在实质性 [REBUT] 矛盾），仅在 2 个 Should-Fix 项上存在分歧。

---

## Detailed Comments（逐节）

### Abstract
- Word count 接近 200 限制（需确认不超）
- "within two percentage points" 需改为 "between α=0.45 and α=0.50"（MF1）
- "five model families (345M–6.9B)" 的 6.9B 规模需核实——Table 3/Appendix Z.1 最大为 SmolLM3-3B（R2-M1）
- "canary" 首次出现未定义（R2-M2）
- Intervention claim "reducing peak perplexity by 64%" 应附 "at α=1.0" scope（MF5 相关）

### Introduction
- Early-warning 叙事过于乐观，与 blind zone 发现不一致（MF5）
- 建议在设定动机后预告 blind zone 存在
- Contribution 4 "practical applications" 应明确限定为 proof-of-concept

### Related Work (Section 2)
- Model collapse 核心文献覆盖完整
- 与 watermarking 的对比过于简短（R17-REF1）
- 缺少 data provenance / attribution 文献（R17-REF2）
- "detection" 一词同时指回顾性诊断和前瞻性监测，应在 Introduction 区分（R2-M5）

### Method (Section 3)
- Cascade ordering 形式化逻辑清晰，但 Observation 1 更多是度量性质的形式化而非机制洞察（SF4）
- MMCT（Algorithm 1）是标准逆误差加权方案（MF4）
- Granger "precedence" vs "causality" 区分在 Section 3.2 首次使用时应明确（R2-M6）
- Detection boundary Eq.(2) 应降级为定性趋势描述（MF2）

### Experiments (Section 4)
- Phase diagram（Figure 1）仅 Pythia-410M，"landscape" 范围需限定（MF6）
- Table 1 与 Appendix R 在 pair 数量上不一致（8 pairs vs 6 pairs）
- Dose-response sigmoid 拟合的 "2pp" claim 需校准（MF1）
- Cross-architecture 仅 α=1.0 是最严重的泛化性缺陷（MF6）
- Intervention 仅 α=1.0, 2 seeds，scope 过窄（SF3）

### Discussion (Section 5)
- Blind zone 的实际部署含义讨论不足（MF5）
- SmolLM3-3B 违反核心假设应在此处更突出讨论（SF5）
- Entropy 测量分辨率 concern（continuous vs discrete）应从附录提升到正文（R15-W1 历史 issue）

### Limitations
- 覆盖三个关键局限（scope, statistical power, causal interpretation），合规且诚实
- 但 blind zone 的讨论深度不足——需量化 α∈[0.25, 0.50) 区间内 diversity loss 的实际影响

### Format Compliance
- ✅ ACL review 模板 (\usepackage[review]{acl})
- ✅ Double-blind（Author: Anonymous）
- ✅ 正文 ≤8 页（Conclusion 第 8 页结束，Limitations 不计入）
- ✅ Mandatory Limitations section 存在
- ⚠️ Abstract 脚注非标准但不违规
- ⚠️ FPR seed 数量主文/附录不一致（R17-W3）

---

## 跨轮 Issue 追踪摘要（Round 17）

**长期未解决 critical issues（≥3 轮 open/in_progress）:**
- F2-W4b: 幂律边界过拟合 (Round 2→17, 16 轮)
- F2-W2b: Landscape framing 超出交付 (Round 2→17, 16 轮)
- F3-J4: PermG FPR 超出 nominal (Round 3→17, 15 轮)
- F5-N1: 方法新颖性天花板 (Round 5→17, wont_fix)
- R14-N1: Blind zone 实用性 (Round 14→17, 4 轮)

**本轮新增:**
- R17-N1: "2pp" claim 精度失实 (critical, new)
- R17-W1: Cascade ordering 新颖性 (warning, new)
- R17-W2: SmolLM3-3B 讨论不足 (warning, new)
- R17-W3: FPR seed 数量不一致 (info, new)
- R17-REF1/REF2: Watermarking + data provenance 引用 (warning, new)