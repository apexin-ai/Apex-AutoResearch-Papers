---
round: 10
overall_score: 3.0 - Findings
timestamp: 2026-05-18T11:58:25.366951+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 11

**Paper**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性 + 实验评估, Confidence 4/5), R2 (新颖性 + 完整性 + 写作质量, Confidence 4/5)

---

## Summary

本文系统比较了 hidden-state (HS) probes 和 text-based monitors 在 4 个推理模型（2 架构 × 2 规模）上的 safety commitment detection 表现。核心方法论发现是 layer selection metric 中的 crossing rate 成分系统性偏向浅层，在 32B 模型上逆转 HS 优势结论。论文在 384d text encoder 基线下报告了统计显著的 HS 精度优势（+15.4 to +32.5pp, Holm-Bonferroni corrected），但在 1024d encoder 下优势大幅缩窄（仅 1/4 模型通过 HB）。所有方法的 FPR 高达 39-52%，论文将结果定位为"现象刻画"而非生产检测器。

---

## Strengths

**S1 [共识]** 层选择敏感性是新颖且可操作的方法论贡献。五指标消融 + LOO-CV 稳定性验证清楚展示 crossing rate 的偏差机制（representation compression at shallow layers），可直接推广到其他 probing 研究。

**S2 [共识]** 统计方法论在同类论文中属上乘。HB step-down correction（12-test + 4-test model-level 双重校正）、10k null-centered bootstrap、穷举 sign-flip permutation test（2^19/2^20 枚举）、control task selectivity（Hewitt framework, 12.5-19.7pp）构成完整证据链。

**S3 [共识]** 异常坦诚的自我批评和透明度。M002 bug disclosure（Appendix G）、QwQ-32B position-mediation 详尽分析（Section 4.4, Appendix K）、R1-32B seed-0 离群值识别（Table L.3）、R1-8B FPR 跨 seed 脆弱性报告（Table L.2）。投稿论文中罕见的透明度水平。

**S4 [共识]** 负面结果的系统性报告有独立信息价值。7 种替代方法逐一分析失败原因：BOCPD 因 gradual transition 失败（0% detection on 3/4 models）、Mahalanobis 信号在 minor PCs、RepE 模型依赖性（QwQ 0.756 vs R1-32B 0.559）。

**S5 [共识]** 写作质量高。无 AI 写作痕迹，主线统一（layer selection sensitivity 贯穿全文），术语定义完整（CP, crossing rate 等首次出现均有定义）。

---

## Weaknesses

### Critical (2)

**W1 [Critical, 完全共识] HS 优势高度 encoder-conditional，384d 基线过弱削弱核心贡献**
- 来源：R1-W2 + R2-W1，交叉回应双方 AGREE
- Against BGE-large-1024d，4 模型中仅 OT-7B precision 通过 HB（Table 3 1024d 行）。R1-8B p=0.185, QwQ p=0.132, R1-32B p=0.042 均不通过 HB。所有 3 个非显著模型的 95% CI 包含 0。
- Abstract/Introduction 的 headline numbers（"+15.4 to +32.5pp"）全部基于 384d MiniLM 基线。1024d 结果仅以 1 句 caveat 出现在 Abstract 末尾（"only 1/4 models retain significance under Holm-Bonferroni, and the directional advantage narrows substantially"），叙事权重严重失衡。
- PCA-384d 维度控制（Section 4.3）论证"非纯粹容量差异"，但存在张力：如果 HS 优势并非容量效应，为何 1024d encoder 几乎消除差距？PCA 选择最大方差方向（可能包含 text-leakage 相关成分），与 text encoder 的语义编码空间信息结构不同。
- **建议**：(a) encoder-conditional 应作为核心发现而非 caveat。Abstract 应并列 384d 和 1024d 结果。(b) Discussion 应明确讨论"HS 优势是否主要反映 text encoder 的不足，而非 hidden states 的内在信息优势"。(c) "dimensionality control" 改为 "capacity control"，加一句说明 PCA 与 text encoder 空间的信息结构差异。

**W2 [Critical, 完全共识] 32B 规模下超参数搜索空间与验证集大小严重不匹配**
- 来源：R1-W1 + R2-W2，交叉回应双方 AGREE
- Limitations 报告 2,240 configurations (64L × 7W × 5K)，但 32B 验证集仅 n=4-9 per-class traces（QwQ ~57 total traces, 60/20/20 → ~11 validation, 二分类后每类 4-7）。
- Joint (layer, W) grid search 仅覆盖 QwQ-32B（Appendix A, 192 configs, W∈{1,3,5}），R1-32B 完全缺失。论文承认"full leave-one-fold-out validation of the (layer, W) pair... remain for future work"。
- Multi-seed 不稳定性：R1-32B precision std=0.128, FPR std=0.145（Table L.3）。Seed-0 FPR=0.483 为离群值（其余 4 seeds 0.109-0.221）。Point estimate ±1σ 从 0.466 到 0.722。
- R1-32B 仅在 W=1 时通过 HB（因维度灾难 51200×W for n=20，W≥3 无法显著），coverage 仅 25%（5/20 traces）。在论文推荐的 deployment configuration (W=3-15) 下无法达到显著性。
- **建议**：(a) 明确区分"7-8B: robust"和"32B: preliminary"，两级 framing 从 Limitations 提升至 Abstract/Introduction 级别。(b) R1-32B 报告绝对检测数字（5/20 traces）并讨论 coverage 阈值下显著性的实际意义。(c) 如可能，提供嵌套 CV 或 bootstrap-out-of-sample 估计量化 selection bias。

### Major (4)

**W3 [Major, 完全共识] 单数据集（HarmThoughts），CP 标注 IAA 未报告**
- 来源：R2-W3，R1 交叉 AGREE（承认自己审稿遗漏）
- CP 标注是整个实验的 ground truth 基础（所有 binary labels、precision/FPR 计算都依赖 CP 定义），但论文未讨论标注者数量、资质、inter-annotator agreement。
- "safety reasoning permanently ceases"（Section 3.1）的判断在实践中有模糊性。如果 CP 标注误差 ≥2 steps，则论文报告的 lead time（+4.5 to +13 steps）可能部分在标注噪声范围内。
- **建议**：至少在 Limitations 中讨论 CP 标注不确定性，引用 HarmThoughts 原始标注方法论。

**W4 [Major, 共识（R2 有 qualification）] QwQ-32B 的 HS 优势主要由位置信息驱动，"all four models" claim misleading**
- 来源：R1-W3 Major，R2 AGREE with qualification
- Position-only baseline BA (0.832) > HS probe (0.796)。HS vs position precision (+4.5pp, p=0.133) 和 FPR (+2.5pp, p=0.279) 均不显著。Position-residualized probe 降低 18.3pp BA（0.796 → 0.612）。HS lead time 为负（-1.2 to +1.9 steps vs text 3.7-12.3）。
- Abstract "precision gains of +15.4 to +32.5 percentage points... across all four models (Holm-Bonferroni corrected)" 技术上正确（HS vs text 384d），但将 QwQ-32B 与 7-8B 的 robust 结果放在同一个 "all four" claim 中 misleading。
- R2 qualification：在 HS vs 384d text 比较下 QwQ-32B 确实通过 HB，只是不是 genuine representational advantage。
- **建议**：Abstract 加 parenthetical qualification（"though QwQ-32B's advantage is predominantly position-mediated"）或改为"three of four models show genuine representational advantage"。

**W5 [Major, 完全共识] R1-32B W=1 coverage 25%（5/20 traces）缺乏实际意义**
- 来源：R1-W4 + R2 AGREE
- 在 20 条 test traces 中仅检测 5 条的 probe，即使在那 5 条上精度很高，对安全监控也缺乏实际价值。
- 在论文推荐的 deployment configuration (W=3-15) 下因维度灾难无法达到显著性。
- **建议**：在 Table 4 或正文中明确报告绝对数字（5/20），讨论 coverage 低于某阈值时显著性的实际意义。

**W6 [Major, 完全共识] FPR 39-52% 与 detection/deployment framing 存在张力**
- 来源：R2-W5 + R1 AGREE
- 论文正文多处声明"characterize rather than constitute production detectors"（Abstract, Introduction 末尾, Limitations），但以下元素与此 framing 矛盾：
  - Discussion: "We recommend temporal windowing (W=3-15) combined with principled layer selection... as deployment defaults"
  - Table 4 caption: "R1-32B provides early warning with narrow coverage"
  - Section 4.5: "false positives on pre-CP steps waste intervention resources"
- **建议**：Discussion 中的 deployment recommendations 调整为条件性语言。Table 4 "early warning" 审慎化。

### Minor (5)

**W7 [Minor, 共识（从 R1 Major 降级）] R1-8B FPR p=0.044 边缘通过 + 跨 seed 脆弱**
- R1 列为 Major，R2 partial REBUT 建议降级。共识：Minor。
- R1-8B FPR 在 HB step-down 中以 0.006 margin 通过（rank 12）。Table L.2 显示 5 seeds 中仅 1 个 p<0.05（seed 1），其余 0.021-0.440。但 precision（主指标）std<4pp 极稳定。
- **建议**：主文在报告"all 12 tests pass"后注明 R1-8B FPR 跨 seed 脆弱性。

**W8 [Minor, 共识（R2 有 qualification）] GRU 70/30 split 的 validation 策略不清晰**
- GRU 使用 70/30 split 但声称 early stopping 基于 validation loss。70/30 下 validation = test？存在信息泄漏可能。
- Table 10 已提供 60/20/20 下 GRU 结果。
- **建议**：明确 70/30 下 GRU 是否从 70% 中再分 validation。

**W9 [Minor, 完全共识] PCA-384d "dimensionality matching" 措辞过强**
- PCA 最大方差方向 ≠ MiniLM 语义空间。且 PCA 去掉的 8-21% variance 可能含 safety-discriminative minor components（论文自己在 Mahalanobis 分析中指出 discriminative signal in minor PCs）。
- **建议**：改为 "capacity control"，说明信息结构差异。

**W10 [Minor, 部分共识] 缺少 probing 方法论基础引用**
- R2 建议补充 Jawahar 2019, Liu 2019, Voita & Titov 2020, Pimentel 2020。
- R1 部分 REBUT：这些工作研究的是"哪些层编码什么信息"，本文的发现是"selection metric 的方法论偏差逆转结论"，层面不同。补引用合理，但 novelty claim 不需收窄。
- **建议**：补充引用以完善 probing 方法论背景，claim scope 不变。

**W11 [Minor, 完全共识] RepE vs LR 的参数化方式差异未明确**
- RepE 使用 class labels 计算 mean-difference direction（解析解），LR 通过 LBFGS 优化 cross-entropy（优化解）。关键差异是参数化方式而非 supervision 有无。
- **建议**：Section 4.5 加 1-2 句说明。

**[额外 Minor]** Bib 条目 3 处 "and others" 需改为完整作者列表（ACL style 要求）。Abstract 语法："only 1/4 models retains" → "retain"。

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全共识（7 个 AGREE）：

1. **[AGREE]** HS 优势是 encoder-conditional，384d 基线过弱（W1 Critical）
2. **[AGREE]** 32B 样本量 + 超参数搜索空间不匹配（W2 Critical）
3. **[AGREE]** 单数据集 + CP 标注 IAA 缺失（W3 Major）
4. **[AGREE]** QwQ-32B 优势主要由位置信息驱动（W4 Major）
5. **[AGREE]** R1-32B 25% coverage 缺乏实际意义（W5 Major）
6. **[AGREE]** FPR vs detection framing 张力（W6 Major）
7. **[AGREE]** 两位独立给出 Overall 3.0 (Findings), Confidence 4

---

## Reviewer Divergence

分歧均为 minor，不影响 overall assessment：

1. **R1-8B FPR 严重性**：R1 评 Major, R2 partial REBUT 建议 Minor。R2 论点：precision（主指标）std<4pp 极稳定，FPR 是单模型单指标边缘问题。**共识降为 Minor**。
2. **Layer selection novelty scope**：R2 建议收窄到 "crossing rate 在 composite metric 中的特定偏差"，R1 认为 claim 可保留。**共识：补引用，claim 不变**。
3. **Abstract 可读性**：R2 认为缺 motivation，R1 认为第一句已建立 motivation 但技术密度偏高。**共识：减少技术细节**。

---

## Questions（汇总 10 条）

1. HarmThoughts CP 标注的 inter-annotator agreement？标注者数量和资质？(R2-Q1)
2. 是否尝试 mean pooling 而非 last-token hidden state extraction？(R2-Q2)
3. 7-8B 模型是否也做了 position residualization？(R2-Q3)
4. Layer selection sensitivity 是否可在非 safety probing 任务上复现？(R2-Q4)
5. 3 个 metrics (bal_acc, precision, FPR) 间的实际 bootstrap resample 相关系数？如 <0.5，4-test correction 可能不够保守。(R1-Q1)
6. Bootstrap 检验是 trace-level 还是 step-level？32B trace-level metric 分布是否近似对称？(R1-Q2)
7. K=5 是 design pre-selection 还是 post-hoc？Appendix F Table 6 报告了 K∈{1,3,5,7,10} 结果——K=5 在看到这些结果之前还是之后选择？(R1-Q3)
8. R1-32B 被检测的 5 条 traces 是否有共同特征（trace 长度、CP 位置、harmful content 类别）？(R1-Q4)
9. Bug disclosure 的 code review 是否确认其他 3 个模型的 text features 无类似问题？(R1-Q5)
10. 为什么不用更多 text encoder baselines（如 GTE-large, E5-large）确定 HS advantage 的变化趋势？(R2-Q5)

---

## Missing References

R2 建议补充（R1 部分同意）：
1. **Jawahar et al. (2019)** — What Does BERT Look At? (BERT 层信息分析) — *应补*
2. **Liu et al. (2019, NAACL)** — Linguistic Knowledge and Transferability of Contextual Representations — *应补*
3. **Voita & Titov (2020)** — Information-Theoretic Probing with MDL — *应补*
4. **Pimentel et al. (2020, ACL)** — Information-Theoretic Probing for Linguistic Structure — *应补*
5. **Ravfogel et al. (2022)** — Linear Adversarial Concept Erasure — *可选*
6. **Li et al. (2024)** — Inference-Time Intervention — *可选*

R1 引用审计：54 条 bib 全部被引用，无孤立条目。12 条为 2025-2026 arXiv preprints，属索引延迟，非虚假引用。

---

## Overall Assessment

**Overall Score: 3.0 — Findings（可被 Findings 接收）**

**ARR 维度打分**: Soundness 3.5/5, Excitement 3.0/5, Reproducibility 3.5/5

**评分理由**:

这是一篇执行质量很高的 empirical/methodology study。Layer selection sensitivity 作为方法论发现是新颖的、可操作的，且对 probing 社区有直接泛化价值——证明一个看似合理的 composite metric 中的 crossing rate 成分可以逆转研究结论，这一发现对所有使用 threshold-based detection + layer selection 的 probing 研究都有警示意义。统计方法论（HB step-down + exact permutation + control task + multi-seed）显著高于同类工作平均水平。论文的透明度（bug disclosure, position-mediation 分析, oracle gap 报告, seed-level breakdown）在投稿论文中属罕见，增强了整体可信度。负面结果（7 种方法系统失败 + 失败原因分析）有独立信息价值。

但实证贡献在经过所有 caveats 后实质收窄：

1. **Encoder-conditional [Critical]**: HS 优势的 headline numbers 完全基于 384d MiniLM 这一较弱基线。换用 1024d BGE-large 后仅 1/4 模型保持 HB 显著。HS 优势可能主要反映 text encoder 的不足而非 hidden states 的内在信息优势。这一发现本身有价值（"modality advantage is encoder-conditional"），但当前 framing 将其作为 caveat 而非核心发现处理。

2. **32B 证据脆弱 [Critical]**: n=19-20 test traces, n=4-9 per-class validation traces 上搜索 2,240 个超参数配置。R1-32B 仅在 W=1 时显著（coverage 25%, 5/20 traces），multi-seed precision std=0.128。QwQ-32B 优势主要由位置信息驱动（residualized -18.3pp, HS vs position p-values 不显著）。

3. **外部效度不足 [Major]**: 单数据集（HarmThoughts），CP 标注 IAA 未报告。所有结论的泛化性未经验证。

4. **实用距离远 [Major]**: 39-52% FPR + 85.5% oracle gap。论文的 characterization framing 是诚实的，但 Discussion 中的 deployment recommendations 与此 framing 矛盾。

方法论贡献（layer selection sensitivity）+ 系统性负面结果 + 高透明度足以支撑 **Findings 接收**。但 32B 证据的脆弱性、encoder-conditional 的实质限制、以及有限的 excitement/novelty 使其 **不足以达到主会议水平**。

---

## Detailed Comments

### Section-by-Section

**Abstract** (~168 words)
- Grammar: "only 1/4 models retains" → "retain"
- 技术密度偏高（crossing rate 机制、HB 术语、384d/1024d 具体数字在 ~168 words 中占比过高）。建议减少 HB/crossing rate 细节，增加 problem significance。
- 384d 和 1024d 结果叙事权重需平衡（384d ~35 words vs 1024d ~20 words）。

**Introduction**
- 叙事线连贯：问题（self-jailbreak）→ 缺口（无 controlled HS vs text 比较）→ 洞察（layer selection reverses conclusions）→ 方法（5-metric ablation）→ 贡献列表。
- Contribution 2 标题 "Encoder-conditional directional advantage" 诚实，但 body 中 384d 权重过高（3 bullet points 讨论 384d，1 句提及 1024d）。
- 末尾 characterization scope statement（"characterize... rather than constitute production detectors: false positive rates remain 39-52%"）有效。

**Related Work**
- 结构清晰（sub-headings: Attack characterization / Detection / Mitigation / Hidden-State Safety Detection / Probing Methodology / Change-Point Detection）。
- 54 references 数量达标。建议补充 Jawahar 2019, Liu 2019, Voita & Titov 2020, Pimentel 2020 以完善 probing 方法论背景。

**Method**
- 5 指标 layer selection 消融设计严谨。LOO-CV 验证 layer 稳定性。
- "dimensionality control" → "capacity control"。

**Experiments**
- 核心结果 well-presented。Table 3 footnote for R1-32B std 有效。
- QwQ-32B "all four models" claim 需 qualification。R1-32B 应报告绝对检测数字（5/20）。

**Discussion**
- Deployment recommendations ("temporal windowing W=3-15 as deployment defaults") 与 characterization framing 矛盾。
- 建议调整为条件性语言（"if future work achieves acceptable FPR, our results suggest..."）。

**Limitations**
- 坦诚且全面。建议增加 CP 标注不确定性讨论。

**Appendix**
- 内容丰富，支撑充分。GRU 70/30 validation 策略需澄清。

---

## Action Items Summary（按优先级）

### Must-Fix (影响 Findings 接收)
1. **Abstract/Intro framing**: encoder-conditional 从 caveat 提升为核心发现；384d/1024d 并列呈现。
2. **两级 framing**: "7-8B robust / 32B preliminary" 从 Limitations 提升至 Abstract/Intro。
3. **QwQ-32B "all four" claim**: 加 parenthetical qualification 或改为 "three of four"。
4. **Discussion deployment language**: 条件化，与 characterization framing 一致。

### Should-Fix (提升论文质量)
5. CP 标注 IAA / 不确定性讨论（Limitations）。
6. R1-32B 绝对检测数字（5/20 traces）。
7. "dimensionality control" → "capacity control"。
8. 补充 4 篇 probing 方法论引用。
9. RepE vs LR 参数化差异说明。
10. GRU 70/30 validation 策略澄清。

### Nice-to-Have
11. Bib "and others" → 完整作者列表。
12. Abstract "retains" → "retain"。
13. R1-8B FPR 跨 seed 脆弱性在主文注明。