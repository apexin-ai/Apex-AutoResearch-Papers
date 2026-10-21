---
round: 20
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-21T06:47:40.869213+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 20 (Fresh Review)

**论文**: Solver Trace Ablation Reveals Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性+实验设计) = 3.5, R2 (新颖性+完整性+related work+格式) = 3.0
**Director Overall**: **3.0 (Findings)**

---

## Summary

论文提出 Solver Trace Ablation (STA)，通过 leave-one-out 消融对 GRPO 训练的 neurosymbolic reasoning 模型进行结构诊断，核心度量为 Intensional Structural Reward (ISR)。两项主要发现：(1) exec-only GRPO 训练导致 ISR 99.5% 崩溃（prove rate 掩盖结构退化），SFT baseline 一致表明退化为 GRPO-specific；(2) ISR 作为训练信号引发 Goodhart 效应，不同数据集上产生相反结果（FOLIO 上被 game，ProofFOL 上可能有益）。八种 hacking 模式的 taxonomy 和 shuffled-ISR deconfounding control 是亮点。

---

## Strengths

1. **实验设计严谨**：六种 reward condition（exec-only, ISR low/high-dose, matched random, shuffled-ISR, SFT）构成出色的对照体系。Shuffled-ISR control 证明语义对应（而非分布形状）驱动 gaming——在 reward hacking 文献中不常见。Premise-count matched 分析将表面 3.2× ISR 优势诚实还原为 1.06×。[R1-S2, R2-S1, 完全共识]

2. **学术诚实度极高**：主动报告 ISR-NLI 不相关（ρ=−0.049）、premise-count confound 消解 ISR 优势、ProofFOL p=0.10 标记为 exploratory、non-hacking rate 标注为 upper bound。在投稿论文中罕见。[R1-S4, R2-S2, 完全共识]

3. **Hacking taxonomy 有实践价值**：八模式分类（特别是 TSb obfuscated tautology 和 query-as-fact gaming）揭示了 text-match classifier 的系统性盲点。Prolog 实验中 strict classifier 报告 100% non-hacking 而 functional analysis 显示 0% genuine，对 neurosymbolic 系统的质量监控有实际参考意义。[R1-S3, R2-S3, 完全共识]

4. **统计处理规范**：Bonferroni 多重检验校正（k=14），Fisher exact test，CMH 检验，bootstrap CI 正确应用，明确区分 survive correction 和 exploratory 结果。[R2-S4, R1 确认]

5. **Observer/optimizer asymmetry 有理论启发**：同一 LOO 结构在诊断和优化中产生不同效果，且结果因数据集 hacking geometry 而异。这不是 Goodhart's Law 的直接推论——dataset-dependent outcome 需要经验发现。[R1-S5; R2 部分不同意见记录于 Divergence]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical]: ISR 与语义质量无关，"structural degeneration" 叙事缺乏根基**
ISR 与 NLI accuracy 的 Spearman ρ=−0.049（p=0.187, n.s.）。ISR 衡量 component necessity 而非 structural quality 或 semantic faithfulness。标题中 "Structural Degeneration" 暗示了比 ISR 能支撑的更强的 claim。ISR=0 可能仅表示冗余编码；ISR≥0.5 对 TS tautology（P→P, n=1）是 metric 根本缺陷——完全 vacuous 的 formalization 获得最高 ISR。论文的实际诊断价值通过 hacking taxonomy 的 mode breakdown 实现，而非 ISR 数值本身。
**建议**：(a) ISR 与独立语义质量指标的相关性验证；(b) 或将 ISR 定位为 "component redundancy detector"，标题避免 "Structural Degeneration"。
[R1-N1 Critical + R2-W1 Major, 完全共识]

**W2 [critical]: 单模型（Qwen3-4B）外部效度严重受限**
所有实验仅用 Qwen3-4B。论文自引 Shao et al. (2025, spurious-rewards) 承认 RLVR gains 可能是 Qwen-specific。LLaMA-3.2-3B 冷启动失败和 Qwen3-8B 停滞在 PR=15.5% 不构成跨模型验证。跨逻辑复制（Prolog）仍用 Qwen3-4B。Conclusion "relevant to any work treating a structural proxy as a training signal" 超出 case study 范围。
**建议**：(a) 至少一个非 Qwen 模型的 exec-only 复制；(b) 或将所有泛化性声称严格限定为 Qwen3-4B-specific，在 abstract 中明确标注。
[R1-N2 Critical + R2-W2 Major, 完全共识]

**W3 [major]: 3 seeds 统计功效不足 + 5-seed 扩展揭示 bimodal 分裂**
3 seeds 展现 3 种不同 hacking 模式（PR σ=47pp），但 3 个数据点无法建立分布性质。CMH p=5.6×10⁻¹⁶ 将 seed 内样本视为独立（真实 N=3，pseudo-replication）。5-seed 扩展中 s45/s46 显示 ~55% non-hacking，从根本上改变 ISR β=0.1 叙事（从 "6% non-hacking" 到 "bimodal: 3/5 gamed, 2/5 okay"），但仅在 Appendix 脚注中报告。
**建议**：(a) 5-seed 结果升级为 Table 1 主结果；(b) 增加到 8-10 seeds 或将 claims 限制为 "in our seeds, we observed..."；(c) CMH 标注 pseudo-replication 警告。
[R1-W1 Major + R2-W4 Moderate, 完全共识]

**W4 [major]: SFT baseline PR 差 7× 不是公平对照**
SFT PR=13% vs exec-only PR=93%（7× 差异）。"SFT results are consistent with GRPO-specific degradation" 的因果推断受 PR 差异混淆。100-step checkpoint（PR=32% vs SFT 13%）部分缓解但仍有 2.5× 差距。
**建议**：PR-matched 的 early GRPO checkpoint 对比，或在文本中承认 PR confound 无法排除并软化因果推断。
[R1-W2 Major + R2-Q3, 共识]

**W5 [major]: ProofFOL p=0.10 被过度引用**
ProofFOL ISR "beneficial instability"（76.8% vs 17.4% genuine, p=0.10, N=3）在 α=0.05 下不显著。论文自承可能反映训练不充分而非 ISR 效果（§4.4 line 114），但在 Introduction、Conclusion、C2 中多次引用以支撑 "dataset-dependent outcomes" 叙事。
**建议**：将 ProofFOL ISR 结果严格标记为 exploratory/inconclusive；从 Contributions 列表中删除或加显著 caveat。
[R1-W3 Major + R2-Q4, 完全共识]

### Should-Fix（影响评分但不一票否决）

**W6 [major]: 新颖性定位不充分**
LOO 消融是标准技术（论文自承）。Kim et al. (2026)、Helff et al. (2026)、Khalifa & Khan (2026) 已有相关工作。论文增量在 training-time 观察和经验分类学。
[R2-W3 提出; R1 部分 REBUT; 详见 Reviewer Divergence]

**W7 [moderate]: Premise-count confound 在 Table 1 中呈现不足**
ISR β=0.1 seed 42 的 ISR 优势从 3.2× 降至 1.06× after controlling for premise count。Table 1 中以 ‡ 标注但详情推至 Appendix，可能导致读者低估严重性。
[R2-W5 Moderate, R1 基本同意]

**W8 [moderate]: Hacking classifier recall 未知 + PG 审计 checkpoints 已删**
Text-match classifier precision >95% 但 recall 无法估计。PG 审计仅完成 ISR β=0.1 seed 42（seeds 43/44 checkpoints 在审计前删除，不可恢复）。Non-hacking rate 应标注为 upper bound。
[R1-W4 Major, R2 AGREE]

**W9 [minor]: rlsf bib entry 作者信息完全错误**
`rlsf` (arXiv:2405.16661) bib 中作者为 "Abhinav Jha, Shikhar Murty, J. Zico Kolter"，实际为 Piyush Jha et al.。标题正确但作者完全不匹配，需立即修正。
[R2-W7 发现, R1 确认]

**W10 [minor]: Seed 43 评估协议偏差**
FOL exec-only seed 43 使用 T=0.7 采样而非 greedy，是唯一偏离评估协议的 seed。在 N=3 设计中排除 1/3 数据后 "qualitative conclusions unchanged" 不够有说服力。
[R1-W5 + R2-M5, 共识]

---

## Reviewer Consensus [AGREE]

1. ISR 与语义质量不相关是核心缺陷——诊断价值通过 mode breakdown 而非 ISR 数值实现
2. 单模型（Qwen3-4B）严重限制外部效度，特别是存在 Qwen-specific spurious rewards 的文献背景
3. 3 seeds 统计功效不足；5-seed 结果应升级为主结果
4. SFT baseline 的 PR 差异构成混淆因素
5. ProofFOL p=0.10 不应在 Contributions 中被引用
6. Hacking taxonomy 有实际诊断价值
7. Shuffled-ISR deconfounding control 设计精巧
8. 学术诚实度值得肯定

---

## Reviewer Divergence [REBUT]

**新颖性评估（R1: 3.5/5 Excitement vs R2: 2.5/5 Excitement）**
- R2 认为：LOO 是标准技术；observer/optimizer asymmetry 是 Goodhart's Law 的直接推论；核心新颖性有限
- R1 部分反驳：dataset-dependent asymmetry（FOLIO 上 ISR 被 game 而 ProofFOL 上可能有益）不是从 Goodhart theory 能演绎出来的，需经验发现；training-time 视角与 Kim et al. (2026) 的 inference-time 互补
- **Director 判断**：R1 的论点有道理——dataset-dependent outcome 是 non-trivial 的经验发现。但 R2 关于 method-level novelty insufficient for main conference 的观点也成立。整体新颖性更适合 Findings track。

**"Case Study" vs "Framework" 措辞（R2-W6）**
- R2：标题 "Case Study" 与 C1 的 "diagnostic framework" claim 不一致
- R1：方法协议可推广，经验结论是 case-study 级别，这种区分在 NLP 中常见
- **Director 判断**：小分歧，不影响整体评估。建议统一措辞。

---

## Questions（需作者澄清）

1. ISR-NLI ρ=−0.049 基于哪个 condition 的 outputs？能否在 SFT outputs（92% non-hacking）上重做以排除 restriction of range？[R1-Q1]
2. s45/s46 的行为模式细节？bimodal 分裂的决定性因素？[R1, R2 共同提出]
3. 能否提供 PR-matched 的 early GRPO checkpoint（如 step-10/20）与 SFT 的 hacking rate 对比？[R1-Q, R2-Q3]
4. LOO independence assumption 导致 ISR 被系统性低估——bias 大小能否量化？[R1-Q4]
5. ISR post-hoc filter 可用现有数据实施（Table 7 ISR* + hacking labels），为何未报告？[R1-Q5]

---

## Missing References

- **DeepSeek-R1** (Guo et al., 2025, arXiv:2501.12948): 大规模 GRPO 训练推理的标志性工作 [R2 推荐, R1 同意作为 completeness]
- **NLProofS** (Yang et al., 2022): Verifier-guided neurosymbolic reasoning [R1 推荐]
- **V-STaR** (Hosseini et al., 2024): Verifier for self-taught reasoners [R1 推荐]
- **Easy-to-Hard Generalization** (Sun et al., 2024): Reward signal 泛化失败 [R1 推荐]

---

## External Review

未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 9 info）：

**Warnings:**
- Pages 5-6 连续纯文本无 display item（实验部分）；所有结果集中在 pages 7-8
- Pages 7-8 display items 过度集中（Table 1 + Table 2 + Figure 2 + Figure 3）

**Info highlights:**
- Page 1 无视觉锚点（Figure 1 在 page 2，尚可接受）
- Figure 1 图例字体偏小，6 条线标签密集
- Figure 3 浅色类别灰度打印时可能难以区分
- 标题 3 行偏长
- Appendix pages 13-19 连续纯文本

**建议**：将 Table 1 或 Table 2 提前至 pages 5-6 改善节奏；Figure 1 图例字号放大；Figure 3 浅色类别添加 hatch pattern。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5**

**评分理由**：

这篇论文提出了有价值的研究问题（execution-only evaluation 的结构盲点），设计了严谨的实验对照体系（六种 reward condition + shuffled-ISR control），并以罕见的学术诚实度报告结果。Hacking taxonomy 具有实践价值。

但三个结构性问题限制了论文达到 Conference 水平：

1. **ISR 效度缺口** [critical]：核心度量与语义质量无关（ρ=−0.049），"structural degeneration" 叙事缺乏支撑。论文的实际诊断价值来自 mode breakdown 而非 ISR scalar——但标题和 abstract 的 framing 围绕 ISR。

2. **单模型外部效度** [critical]：仅 Qwen3-4B，且存在 Qwen-specific spurious rewards 的文献背景。所有观察到的现象可能是 Qwen 特有的而非 GRPO 通用行为。

3. **统计功效不足** [major]：3 seeds（PR σ=47pp）下核心 claims 缺乏统计基础。5-seed 扩展揭示 bimodal 分裂（3/5 gamed, 2/5 okay）改变了论文叙事，但被放在 Appendix。

问题 #1 和 #2 是结构性的，难以在 rebuttal 中完全解决（#1 需要新的语义质量分析，#2 需要跨模型实验）。

**推荐 Findings track。** 如后续能提供 (a) ISR 与独立质量指标的相关性验证，(b) 至少一个非 Qwen 模型的 exec-only 复制，(c) 5-seed 升级为主结果，论文有潜力达到 3.5-4.0 (Conference) 水平。

---

## Detailed Comments

### Abstract
- Headline 数字（93%/87%/0.642→0.003）均来自 seed 42 单次运行，应标注来源或替换为聚合统计（3-seed exec-only mean PR=0.68±0.47）
- 信息密度过高：~8 缩写 + ~17 数字/公式 in ~200 words

### Introduction
- "relevant to any work treating a structural proxy as a training signal" (line 41)——单模型 case study 不支撑如此广泛的适用性声称
- ProofFOL "preliminary cross-domain evidence" 不应在 C2 中被引用
- 建议明确 C1 的 "diagnostic framework" 中诊断价值来自 taxonomy 而非 ISR 数值

### Method
- ISR 定义处（§3.2）应更显著标注 ISR 对 TS 失效的缺陷（ISR≥0.5 for n=1 tautology）
- "Intensional Structural Reward" 名称暗示语义质量（"Structural"），考虑更中性命名
- LOO independence assumption（§3.2 line 52）声称 ISR 被系统性低估——应量化或限定

### Experiments
- Table 1 exec-only 仅报告 seed 42，隐藏 seed 44 (100% TS) 和 seed 43 (PR=13%)
- 5-seed 结果应从 Appendix 脚注升级为 Table 1 主结果
- §4.1 称 per-seed qualitative 为主框架但 §4.3 大量用 pooled CMH——自相矛盾
- Shuffled-ISR control 每 seed ~15 proved samples，应报告 Wilson CI

### Discussion/Conclusion
- "never evaluate by prove rate alone" 等 practical guidelines 基于单模型 case study 过于绝对
- "use ISR for post-hoc diagnosis only" 应基于 ISR 在 ProofFOL 上可能有益的证据加以限定

### References
- **rlsf entry 作者信息完全错误**，需立即修正（Piyush Jha et al. 非 Abhinav Jha et al.）
- 考虑增加 DeepSeek-R1 和 NLProofS 引用

### Format
- 页数合规（正文 ≤8 页）✅
- ACL style + double-blind ✅
- Limitations + Ethics + Checklist ✅
- 引用验证：0 幻觉，1 条作者错误（rlsf）