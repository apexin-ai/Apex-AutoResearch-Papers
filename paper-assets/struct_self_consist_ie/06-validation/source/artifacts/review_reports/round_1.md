---
round: 1
overall_score: borderline
timestamp: 2026-05-15T02:09:02.469376+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 1 圆桌审稿

**论文**: "Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"
**目标 Venue**: EMNLP 2026 (ARR)
**Reviewer 配置**: R1（方法严谨性 + 实验设计 + 统计有效性）+ R2（新颖性 + 完整性）
**轮次**: Round 1（交叉分享后已收敛，无需第二轮）

---

## Summary

本文系统比较 5 种 training-free confidence signals（Log-Probability、Entropy、Set Jaccard、Token Jaccard、Exact-Match）在 LLM-based 结构化信息抽取（NER/RE）中的 quality estimation 和 best-of-N sample selection 能力。核心概念贡献是将 quality estimation（ranking correlation）与 sample selection（F1 gain over greedy）解耦，发现二者存在 "correlation-selection gap"——即使信号与 F1 有中等正相关（SJ ρ≈0.42），实际 selection 也未能稳定超越 greedy baseline (p=0.39)。实验覆盖 3 个 NER 数据集 + 1 个 RE 数据集，2 个 8B 模型，多 seed/多温度/OOD 等消融维度。

---

## Strengths

**S1. Quality estimation vs sample selection 的概念解耦** [R1+R2 共识]
将 ranking correlation 与 selection F1 gain 分离是有价值的概念贡献，对后续 test-time scaling 研究有直接指导意义——不论负面结论是否最终成立。

**S2. 实验设计的系统性** [R1+R2 共识]
5 signals × 3 signal families × 3 NER datasets × 1 RE dataset × 2 models × 2 N × 2 T + task difficulty gradient (CoNLL/SciERC/WNUT) + 多项辅助分析（LOO circularity、conditional filtering、capability stratification、inverted-U pattern）。

**S3. Task difficulty gradient 设计** [R1 提出，R2 认可]
CoNLL（easy）→ SciERC（medium）→ WNUT（hard）的难度梯度设计合理，信号排序随难度变化的发现有实用价值。

**S4. Conditional filtering analysis** [R2 提出，R1 认可]
Appendix 中移除 zero-F1 instance 后 RE 信号恢复（SJ ρ=0.405, EM ρ=0.417），揭示了 EM 在 non-trivial subset 上的优势，提供了 "task difficulty determines signal choice" 的额外证据。

**S5. Limitations section 全面诚实** [R1 提出]
主动承认模型规模、RE 数据集、logprob 温度数据等限制。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**C1. Bootstrap 检验细节严重不足，核心负面结论无法验证** [R1 提出 critical, R2 完全同意 critical]

论文核心负面结论（"no signal reliably surpasses greedy"）建立在 Section 5.3 的 "p=0.39, 3-seed bootstrap; Cohen's d=0.038" 上，但以下关键细节均未报告：
- Bootstrap 迭代次数
- Paired 还是 unpaired bootstrap
- 检验统计量
- "3-seed bootstrap" 含义不明——对 3 个 seed 做 bootstrap (n=3, 完全无统计功效) 还是每个 seed 内对 instance 做 bootstrap 再合并？

该 p 值在论文 5 处被重复引用（Abstract、Introduction ×2、Section 5.3、Conclusion），支撑标题 ("Weak Selectors")、Contribution #2（correlation-selection gap）及 Discussion 对 trained verifier 的呼吁。若检验无效，核心贡献坍塌为 "没有足够统计功效来判断 selection 是否有效"——完全不同的结论。

**C2. Correlation-selection gap 的理论贡献被定义性质部分削弱，logprob 失败分析缺失** [R2 提出, R1 部分同意]

4/5 个 signals（Entropy, SJ, TJ, Voting）是 instance-level 的——它们不能做 per-sample selection 在定义上是预期结果（Section 3.1 Eq. 5–8 只产出单一 score），而非实证发现。R1 补充：Section 3.3 通过 consensus-proximity 将 instance-level signals 转化为 per-sample 排序，这不完全是 trivial 的，但效果确实差（Table 5: SJ=0.645 vs Greedy=0.644）。

真正需要深入分析的是唯一 per-sample signal logprob 为何也失败——calibration 问题？length bias？constrained decoding 干扰？论文仅在 Section 5.1 提到 conditional filtering 后 "logprob RE collapses to ρ=0.011"，Discussion 简要提及 constrained decoding 可能影响，但无实验验证。

**C3. 对 Nedellec et al. (2026) 增量贡献论证不足 + 引用作者错误** [R2 提出 critical, R1 同意]

bib 文件中 `nedellec2026consistency` 第一作者为 Yao，但全文引用为 "Nédellec et al."——事实性错误。三个区分点的说服力不足：
- Selection 结论是负面的（未能超越 greedy）
- Multi-domain 是标准做法
- SJ 优势不一致（CoNLL: EM ρ=0.451 > SJ ρ=0.436; conditional filtering 后 EM 在所有 4 个配置领先）

R1 补充：negative selection result 本身有学术价值（Nedellec 未涉及 selection），问题在于论证方式不够有力，而非贡献不存在。

**C4. 仅 8B 模型 "model-agnostic" overclaim** [R1 critical, R2 降为 should-fix — 存在分歧]

仅 Qwen3-8B 和 LLaMA-3.1-8B-Instruct 两个同规模模型。Discussion 使用 "model-agnostic" 但 Limitations 承认 "Whether our findings hold for larger models (70B+) remains untested"——构成内部矛盾 (ARR R4 overclaiming)。

**R2 立场**：修复成本低——将 "model-agnostic" 替换为 "consistent across tested model families" 即可，核心发现（structural > logprob 在两个模型上一致）本身有效。应为 should-fix。
**R1 立场**：70B+ 模型可能产生更高质量更多样的样本，从根本上改变 gap 形态。应为 critical。
**Director 定级**：Critical（保守取高），但记录 R2 的缓和意见。

**C5. RE 结论仅基于 SciERC, 44% zero-F1 floor effect 扭曲评估** [R1 critical, R2 降为 high-warning — 存在分歧]

RE 所有结论来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。

**R2 缓和因素**：(1) Conditional filtering 后 SJ RE ρ=0.405, EM RE ρ=0.417——non-trivial subset 上信号有区分力；(2) Capability stratification 中高复杂度 RE 子集 Voting ρ=0.630。
**R1 立场**：论文声称覆盖 "NER and RE" 但 RE 基础极其薄弱，"universal bottleneck" 需降级。
**Director 定级**：Critical for "NER and RE" / "universal bottleneck" 措辞；Warning if 仅要求限定 RE 结论的泛化范围。

---

### Should-Fix

**W1. Per-sample signal 探索单薄** [R2 提出, R1 部分同意]
5 个 signals 中仅 logprob 1 个能做 per-sample selection，论文却声称 "systematic comparison"。R1 反驳：consensus-proximity (Table 5 SJ 行) 数学上等价于 LOO-SJ 排序——是表述问题非实验缺失。但两位共识：per-sample 维度极度单薄。

**W2. 约束解码对 sampling diversity 的影响** [R1 warning, R2 认为应升级]
Constrained decoding (Outlines/vLLM) 强制输出符合预定义 schema，压缩 token-level 自由度和 per-sample variance。Correlation-selection gap 可能部分是实验 artifact 而非结构化 IE 固有属性。Discussion 用 random baseline (0.608) vs greedy (0.644) 的 gap (3.6pp) 论证 "variance exists"，但这是约束解码下的 variance。

**W3. Soft Jaccard 形式化有歧义** [R1 提出, R2 同意]
Eq. (4) 中 g_i/g_j 未定义，sim 具体公式缺失（token-level IoU? character-level?），Hungarian algorithm 匹配阈值未说明。影响 reproducibility。

**W4. Entity voting 与 SJ 的冗余度未分析** [R1 提出, R2 同意并补充]
Mean frequency 聚合未讨论替代选择。R2 补充：entity voting 和 SJ 概念上 overlap，instance-level correlation 未报告——若高度相关则 "两个 structural signal 优于 surface signal" 论证被削弱。

**W5. Logprob 温度数据缺失** [R1+R2 共识]
Logprob 是唯一 per-sample signal，T=0.7 数据 "unavailable"，但论文声称 "signals robust across temperatures"。应限定为 "consistency-based signals are robust; logprob temperature sensitivity remains uncharacterized"。

**W6. ρ=0.38 缺乏 contextualization** [R1 提出, R2 部分反驳]
R1 认为仅解释 ~14% F1 方差，未与 uncertainty estimation 文献对比。R2 反驳：论文用 "effective" 和 "strongest"（比较级）而非 "strong"（绝对值），AUROC=0.749 是面向应用的核心证据。但 R2 同意缺乏与 semantic entropy、P(True) 等方法的 ρ 对比。

**W7. WNUT-17 "establishing capability boundary" 措辞** [R1+R2 共识]
p=0.106, fail to reject null ≠ accept null。ρ=0.082 效应量小 + 54% zero-F1 支持实质结论，但统计措辞应改为 "consistent with" 或 "suggests"。

**W8. 模型训练设置不对称** [R1 提出, R2 同意]
Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct——后者是否经过 fine-tuning 未说明。若为 off-the-shelf vs task-specific LoRA，则 cross-model comparison 混淆了 architecture 和 training strategy。

**W9. "first systematic evaluation" claim 过强** [R2 提出, R1 同意]
需收窄为 "first to compare signals from multiple families for both quality estimation and sample selection in generative IE"。

**W10. 遗漏引用** [R2 提出, R1 部分同意]
- **共识应引用**：Optimal Self-Consistency (arXiv:2511.12309)、Difficulty-Adaptive SC (NAACL 2025 Findings)——与论文核心主题 (task difficulty determines signal choice) 高度相关
- **R2 认为应引用, R1 反驳为非 critical**：Singer et al. (2026) conformal NER, ICLR 2025 conformal structured prediction——属不同研究路线 (supervised conformal vs unsupervised consistency)
- **待确认**：Generative Self-Aggregation (arXiv:2503.04104)

**W11. ρ-AUROC dissociation 机制分析浅** [R2 提出, R1 同意]
EM=1 同时包含 all-correct 和 all-wrong 的压缩效应仅在 Appendix D 讨论，应在主文明确阐述。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致：
1. **Overall 评分**: 3/5 (Findings)
2. **Bootstrap 细节不足 (C1)**: 本文最关键的方法论缺陷，影响核心贡献成立性
3. **Logprob 失败分析缺失**: 唯一 per-sample signal 值得专门深入分析
4. **Nedellec 引用错误**: Yao → Nédellec 是事实性错误
5. **约束解码 confound**: 应至少讨论其对 diversity 和 gap 的潜在影响
6. **"model-agnostic" 措辞矛盾**: 需与 Limitations 一致
7. **WNUT-17 措辞**: "establishing" → "consistent with" / "suggests"
8. **"first systematic" 需限定**
9. **Quality estimation vs selection 解耦**: 本文最有价值的概念贡献

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | Director 定级 |
|------|---------|---------|---------------|
| C4 模型规模 overclaim | Critical（70B 可能根本改变 gap） | Should-fix（措辞修正即可） | Critical（保守取高） |
| C5 RE 单数据集 | Critical（RE 基础极其薄弱） | High-warning（conditional analysis 部分缓解） | Critical for "universal" 措辞 |
| W1 LOO-SJ selection | 已隐式测试（Table 5 SJ 行 = consensus-proximity） | 未测试，应显式报告 | Warning（是表述问题，但 per-sample 维度确实单薄） |
| W6 ρ contextualization | 缺乏对比 | 论文措辞准确（比较级），AUROC 是核心证据 | Warning（补充对比即可） |
| W2 约束解码严重程度 | Warning | 应升级（可能解释 gap 的根本原因） | Warning（论据充分但无约束解码对比数据） |
| W10 Conformal prediction 引用 | 非 critical omission（不同路线） | 应引用 | Warning（在 Related Work 中讨论） |

---

## Questions（需作者澄清）

1. **Bootstrap 检验完整规范**：迭代次数、paired/unpaired、统计量、"3-seed bootstrap" 确切含义？若 n=3，则需在每个 seed 内对 instance 做 paired bootstrap 并报告合并策略。
2. **LLaMA-3.1-8B-Instruct 是否经过 LoRA/SFT fine-tuning**？若未 fine-tune，cross-model comparison 混淆了 architecture 和 training strategy。
3. **Consensus-proximity selection 与 LOO-SJ 的等价关系**：Table 5 SJ 行是否等价于 LOO-SJ selection？若是，应在正文中显式说明。
4. **Logprob 在 constrained decoding 下的行为**：constrained decoding 是否系统性扭曲了 logprob 的 calibration？是否有 unconstrained 对比数据？
5. **Entity voting 与 SJ 的 instance-level correlation**：Spearman ρ 是多少？高冗余度是否削弱 "两类 structural signal 独立验证" 的论证？
6. **Logistic regression proxy**：Limitations 提到但正文/Appendix 无结果——是否计划展示？

---

## Missing References

### 共识应引用
1. **Optimal Self-Consistency** (arXiv:2511.12309) — 与 selection 机制直接相关
2. **Difficulty-Adaptive Self-Consistency** (NAACL 2025 Findings) — 与论文核心发现 "task difficulty determines signal choice" 高度相关

### 建议引用（存在分歧）
3. Singer et al. (2026) "UQ for NER via Conformal Prediction" (arXiv:2601.16999)
4. Conformal Structured Prediction (ICLR 2025)
5. Generative Self-Aggregation (arXiv:2503.04104)

### 引用错误
- `nedellec2026consistency`: 第一作者应为 Yao，全文 "Nédellec et al." 引用有误

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**评分**: 3/5 (Findings) — 两位 Reviewer 完全一致
**Director Scale**: 3.5/6 (Borderline — Weak Accept for Findings)
**置信度**: 4/5

### 定位判断

Findings 可接受（需修复 C1 bootstrap 细节），Main 不足。

论文的概念贡献（quality estimation vs selection 解耦）和系统实验设计有 Findings 水准的价值，但 5 个 critical 问题共同限制了竞争力：

1. **C1 Bootstrap 细节** — 核心负面结论的统计基础无法验证（最优先修复）
2. **C2 Gap 解释力** — 4/5 signals 的 selection 失败有定义性成分，logprob 失败机制未分析
3. **C3 Nedellec 增量** — 贡献论证弱 + 引用错误
4. **C4 Model-agnostic** — Overclaim，但修复成本低（措辞修正）
5. **C5 RE 单数据集** — "Universal bottleneck" 仅单数据集支撑

### 与 Round 0 的对比

Round 0 的部分 critical 问题可能已修复（零图表、成本分析均未被本轮 Reviewer 提及），但新的 critical 问题浮现（bootstrap 细节、gap 定义性、Nedellec 增量）。模型规模和 RE 数据集问题持续存在。整体评分与 Round 0 持平（3/5），论文在不同维度有进步和退步。

### 修改建议优先级

- **P0（决定性）**: 补充 bootstrap 检验完整规范 + 修正 Nedellec 引用错误 + 降级 "model-agnostic"/"universal"/"establish" 措辞
- **P1（强烈建议）**: 深入分析 logprob selection 失败原因 + 讨论约束解码 confound + 补充 Optimal SC / Difficulty-Adaptive SC 引用 + 显式说明 consensus-proximity = LOO-SJ selection
- **P2（改善质量）**: SJ 形式化补全 + entity voting/SJ 冗余度分析 + ρ contextualization + 温度 robustness 限定 + LLaMA fine-tuning 状态说明

---

## Detailed Comments

### Abstract
- "Weak Selectors" 结论建立在 p=0.39 上——若 bootstrap 细节补全后确认有效则可保留，否则需重新表述

### Section 1 (Introduction)
- "+18pp on GSM8K" 未注明具体模型 (PaLM-540B)，与本文 8B 规模差异大
- "first systematic evaluation" 需加限定语

### Section 3 (Method)
- Eq. (4) SJ: g_i/g_j 定义、sim 公式、Hungarian 阈值需补全
- Section 3.3 consensus-proximity selection 应显式说明与 LOO-SJ 排序的等价关系
- Entity voting mean frequency 聚合未讨论替代选择

### Section 5 (Results)
- Section 5.3: bootstrap 检验规范必须完整报告
- Section 5.4: "model-agnostic" → "consistent across tested model families"
- Section 5.4: Cross-model Δ=0.005 应报告是否在 CI 内
- WNUT-17: "establishing the capability boundary" → "consistent with a capability boundary"
- Logprob T=0.7 缺失应在温度 robustness 结论中明确限定

### Section 6 (Discussion)
- 补充约束解码对 sampling diversity 和 correlation-selection gap 的讨论
- "Universal bottleneck" 需降级或增加 RE 数据集
- Logistic regression proxy: 展示结果或删除提及

### Related Work
- 补充 Optimal SC、Difficulty-Adaptive SC
- 讨论 conformal prediction for structured prediction（可简要说明与本文研究路线的关系）
- 更充分讨论 trained approaches (verifier/reward model) 作为 upper bound context

### References
- 修正 nedellec2026consistency 第一作者 (Yao → 正确引用)
- 检查 snell2024scaling bib 作者格式

### Appendix
- ρ-AUROC dissociation / EM=1 压缩效应应在主文至少简要提及
- Appendix D \textsc 编译检查