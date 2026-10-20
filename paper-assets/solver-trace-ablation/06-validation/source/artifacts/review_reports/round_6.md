---
round: 6
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T16:35:06.203857+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 6

**论文**: Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation
**Venue**: EMNLP 2026 via ACL Rolling Review (May cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+格式合规+完整性）
**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成共识，无需 Round 2）

---

## Summary

论文提出 Solver Trace Ablation (STA)，对 GRPO 训练的 neurosymbolic formalizer 的 solver 输入进行 leave-one-out 消融，生成 Intensional Structural Reward (ISR) 指标。ISR 作为诊断工具有效揭示了 execution-based evaluation 隐藏的结构崩溃（99.5% degradation），但作为训练信号时在所有 4 个测试剂量下触发 Goodhart collapse。论文覆盖 6 reward conditions、5 seeds、2 logic types、2 model scales，cataloging 了 9 种 hacking 模式。

---

## Strengths

**S1. 实验覆盖面广且透明度高**
多 seed（3-5 per condition）、matched random controls、CMH 分层检验、1000-step trajectory analysis、premise-count-matched comparison——该领域少见的统计严谨度。论文坦诚披露所有已知局限（ISR premise-count confound、OR 方向反转、checkpoint 丢失、eval 协议不一致），自我批评充分。[共识: R1+R2]

**S2. 叙事核心有说服力**
"ISR: reliable as observer, unreliable as optimizer at any dose" 是一个清晰、有警示价值的结论。对 neurosymbolic RL 社区有实际操作意义。[共识: R1+R2]

**S3. Hacking taxonomy 有独立操作价值**
9 种 hacking mode 的定义、示例和 ISR 交互分析对从业者有直接参考价值。Cross-validation 思维（text-match + functional LOO analysis）发现了 H7b obfuscated tautology 和 query-as-fact gaming，体现 careful empirical work。[共识: R1+R2]

**S4. Control design 正确**
SFT control（分离 RL-specific vs data exposure）、random control（分离 ISR-specific vs generic variance）、matched dose design 的实验逻辑清晰。[R1 优势 #5; R2 隐含同意]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] ISR 核心指标命名不一致** [v6-R2-N1]
Abstract 将 ISR 定义为 "Irreducible Solver Rate" (abstract.tex:3)，Introduction/Method 定义为 "Intensional Structural Reward" (method.tex:44)。核心概念的名称冲突是严重的写作错误，损害可信度。此外，"Reward" 一词暗示应被用作 reward，与论文核心结论矛盾 (v6-R2-W5)。
- **建议**: 统一为不含 "Reward" 的名称（如 "Irreducible Solver Rate"）。
- **共识**: R1 [AGREE] + R2 [提出]

**MF2. [critical] Abstract 数据过载，30 秒内无法消化核心贡献** [v5-R2-W1, 复发]
Abstract (~220 words) 包含 15+ 数字/统计量（97±2%, 99.5%, 92%, β∈{0.05,0.1,0.2,0.3}, 3/3 seeds, 0%, 6 conditions, 2 logic types, 2 model scales, 5 seeds, 9 hacking modes）。读感像压缩的 results table，核心 insight 被数字淹没。此问题在 Round 3 修复后（重写为 ~170 words）再次膨胀。
- **建议**: 保留 ≤4 个关键数字，移除 β 列表、seed counts、condition counts。
- **共识**: R1 [AGREE] + R2 [提出]

**MF3. [critical] Table 1 比较框架不对称** [v5-R1-N3, 持续存在]
Table 1 exec-only 行为单 seed (s42)、500-step，而 ISR/Random 为 5-seed pooled。3-seed 1000-step exec-only 数据（PR=97±2%, N-H≈2%）在附录但不在主表。主表是审稿人第一眼看到的比较基准，不对称的比较框架损害所有下游 claim 的可信度。
- **建议**: Table 1 增加 exec-only 3-seed 1000-step 行。
- **共识**: R1 [提出] + R2 [AGREE]

**MF4. [critical] OR=3.48 vs OR=0.61 方向反转的 framing 不够诚实** [v4-R12-N3, 持续存在]
5-seed uncorrected OR=3.48 基于包含 2 个 checkpoint 已删除 seed 的不完整数据，3-seed H8+FN-corrected OR=0.61 是唯一有完整审计的比较。论文将二者 frame 为 "bound the true effect from above and below"，但应将 corrected 分析作为 primary sensitivity，明确 "genuine-rate advantage is not robust to H8 correction"。CMH OR=3.37 (p<10⁻⁹) 方向一致，说明正面效应非纯粹 artifact，但 framing 仍需修正。
- **建议**: (a) 3-seed corrected 提升为 primary sensitivity; (b) Abstract/Intro 弱化 "initially yields more genuine" 措辞; (c) 正文讨论 "transient benefit 是否真实存在的不确定性"。
- **共识**: R1 [提出] + R2 [AGREE with nuance]

**MF5. [critical] SFT vs RL 比较中 PR 严重混淆** [v5-R12-SFT-PR, 持续存在]
SFT PR=13% (n=39) vs RL PR=93%+。C1 "localizing the failure to RL" 的证据链有根本性 PR confound：无法知道 SFT 在高 PR 时是否也会 hack。100-step checkpoint (PR=32%, hacking=31.2%) 部分缓解但 PR 仍为 SFT 的 2.5 倍。机制论证（SFT 无 exploration-exploitation dynamics）是合理的 reasoning 但非 empirical evidence。
- **建议**: C1 弱化为 "consistent with RL-specific failure"；正文承认 "whether SFT would hack at higher PR remains unknown"。
- **注意**: R2 补充——SFT 比较是一个 confound 但不影响论文核心贡献（ISR collapse diagnostic, Goodhart at all doses, taxonomy）。
- **共识**: R1 [提出] + R2 [AGREE]

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] 新颖性 framing 不足** [v5-R2-N3 + v4-R2-W9, 持续存在]
"Diagnostic becomes optimization target" 是 Goodhart's Law 的定义，不是新发现。LOO ablation 是标准方法。论文需说服 reader 为什么这个经验实例值得一篇论文。
- **Director 裁决**: R2 正确指出概念层面可预测，但 R1 正确指出 stochastic bifurcation timing、H7b triple gaming、cross-logic mode divergence、OR 方向反转是理论无法预测的经验现象。论文应将 framing 从 "we discover Goodhart effects" 转为 "Goodhart collapse is predictable, but these specific phenomena are not"。
- **分歧记录**: R1 Excitement=3.5, R2 Excitement=2.0

**SF2. [warning] 1.7B cross-scale claims 仅单 seed** [v3-R12-NI-1, 持续存在]
4B scale 下 3 seeds 产生 3 种截然不同的 hacking mode，说明单 seed 几乎不具备代表性。§4.5 "No safe scale was observed" 是 n=1 的存在性声明。
- **建议**: 弱化为 "No safe scale was observed in this single-seed comparison"。
- **共识**: R1+R2

**SF3. [warning] "At all tested doses" claim 缺 β=0.3/0.05 trajectory 数据** [v4-R12-N2, 持续存在]
1000-step trajectory 仅对 β=0.1 两个 seed 进行。β=0.3 和 β=0.05 仅 500-step snapshot。论文自身方法论认为 snapshot 不足以判断 long-run 行为，但对自己的 claims 使用了 snapshot。
- **建议**: 弱化为 "collapse observed at 500-step snapshot across all doses; trajectory-confirmed at β=0.1"。
- **共识**: R1+R2

**SF4. [warning] Deleted checkpoints 导致 N-H rate 不完整** [v4-R12-W7, 持续存在]
ISR β=0.1 s43/s44 checkpoint 丢失，5-seed pooled N-H=23% 是 uncorrected upper bound。
- **建议**: Table 1 报告为区间或标注 "upper bound"；Limitations 明确列出影响。
- **共识**: R1+R2

**SF5. [warning] Dose-response claim 基于 4 β、不均匀 seed 数** [v6-R1-W2, 新]
β=0.1 用 5 seeds，其余用 3 seeds。"Non-monotonic dose-response" 统计上无法支撑。
- **建议**: 弱化为 "the pattern across four tested doses suggests..."。
- **共识**: R1+R2

**SF6. [warning] §4.3 β 值呈现顺序非升序** [v6-R2-W2, 新]
0.1→0.05→0.2→0.3 增加认知负荷。
- **建议**: 升序呈现或解释当前顺序的叙事理由。
- **共识**: R1 [AGREE] + R2 [提出]

**SF7. [warning] Table 1 caption 过长 (~120 words + 6 脚注)** [v5-R2-W6, 持续存在]
- **建议**: Caption 压缩至 ≤60 words，条件说明移正文。
- **共识**: R1+R2

**SF8. [warning] Introduction \paragraph{} 结构争议** [v5-R2-W3, 持续存在]
- **分歧**: R2 认为 5 个 \paragraph{} 碎片化叙事; R1 认为结构服务于逻辑链，问题在于段内数据密度。
- **Director 裁决**: 两种修改方向均可接受。

### Nice-to-Have（info 级别）

- **NF1.** Pooled Fisher vs CMH 在 Appendix Table 4 中的排列顺序应调整（CMH 置于 Fisher 前）[v4-R1-N4, R2 部分 REBUT 后降级]
- **NF2.** LOO 缩写未在首次使用时定义 [v6-R2-W6-LOO]
- **NF3.** 100 eval samples 对 per-seed claims 效力有限；小 n seed 应报告 CI [v4-R1-W8]
- **NF4.** Seed 43 exec-only eval 协议不一致（T=0.7），Appendix 标注不够显著 [v4-R12-W6]
- **NF5.** Hacking taxonomy 部分 mode 为单点观察，建议标注 evidence strength [v6-R2-W8]
- **NF6.** 引用偏少（37 条），建议增加 Amodei 2016, Geirhos 2020 (shortcut learning), DeepSeek-R1 2025 [v5-R2-MR]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识：

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| ISR 命名不一致 | AGREE | 提出 | 必须统一 |
| Abstract 数据过载 | AGREE | 提出 | 必须精简 |
| Table 1 不对称比较 | 提出 | AGREE | 必须修正 |
| OR 反转 framing | 提出 | AGREE | 必须修正 framing |
| SFT PR confound | 提出 | AGREE | C1 claim 弱化 |
| Checkpoint 丢失影响 | 提出 | AGREE | 标注 upper bound |
| 1.7B 单 seed | AGREE | AGREE | 弱化 claims |
| β=0.3/0.05 缺 trajectory | AGREE | AGREE | 弱化 "at all doses" |
| Dose-response 4 点不足 | 提出 | AGREE | 弱化 claim |
| Table 1 caption 过长 | AGREE | 提出 | 精简 |
| β 呈现顺序 | AGREE | 提出 | 升序或解释 |
| LOO 缩写未定义 | AGREE | 提出 | 简单修复 |

---

## Reviewer Divergence

**D1. Soundness 评分: R1=2.5/5, R2=4.0/5**
- R1 聚焦于比较框架不对称（Table 1 exec-only 单 seed vs ISR 5-seed pooled）、OR 反转 framing、SFT PR confound、统计层级倒置，认为这些是根本性缺陷。
- R2 认为论文的 multi-seed 设计、matched controls、CMH stratification 在该领域是 above-average 标准，上述问题是 framing issues 而非根本性缺陷。
- **Director 裁决**: Soundness 约 3.0-3.5。R1 的具体指摘均有效，但多数可通过 framing 修正解决，不需要新实验。R2 对 SFT confound 的补充（不影响核心贡献）有道理。

**D2. Excitement 评分: R1=3.5/5, R2=2.0/5**
- R1 认为 cautionary value 高，taxonomy 有实用性，stochastic bifurcation 等现象非平凡。
- R2 认为核心 insight 是 Goodhart's Law 的直接推论，empirical increment 有限。
- **Director 裁决**: Excitement 约 2.5-3.0。概念层面确实可预测（R2 正确），但 empirical details 有增量（R1 正确）。论文的 framing 需要更好地突出理论无法预测的具体现象。

**D3. Introduction \paragraph{} 结构: R1 REBUT, R2 提出**
- R1 认为 5 个 \paragraph{} 服务于两个 story arc 的逻辑链，问题在段内数据密度。
- R2 认为 \paragraph{} 碎片化叙事，建议减少到 2-3 个或去掉。
- **Director 裁决**: 不裁决，两种方向均可接受。

**D4. Taxonomy principled-ness: R1 REBUT, R2 提出**
- R1 认为分类标准统一（基于 mechanism），cross-validation 证明非 post-hoc。
- R2 认为 9 种 mode 缺乏理论完备性论证。
- **Director 裁决**: 降级为 info。标注 evidence strength 即可。

---

## Questions（需作者澄清）

1. ISR 应统一为哪个名称？如果 "Irreducible Solver Rate"，Method §3 需要大幅修改描述语言。
2. 是否有可能补跑 1-2 个 β=0.3 1000-step trajectory 以支撑 "at all doses" claim？
3. s43/s44 checkpoint 丢失是技术事故还是存储策略？是否有防止未来类似丢失的措施？
4. 如果 3-seed corrected OR=0.61 是更可靠的估计，是否考虑将 ISR β=0.1 的 transient genuine window 完全从核心叙事中降级？

---

## Missing References

两位 Reviewer 共识的缺失引用：
1. **Amodei et al. (2016)**, "Concrete Problems in AI Safety" — reward hacking 讨论的基础性引用
2. **Geirhos et al. (2020)**, shortcut learning 综述 — 与 "degenerate shortcuts" 直接对话
3. **DeepSeek-R1 (2025)** — 使用 GRPO 的代表性工作

可选增加：
4. Christiano et al. (2017), RLHF — 边际相关
5. AlphaProof 或 LEGO-Prover — neurosymbolic proof generation at scale

当前 37 条引用对 EMNLP 偏少（典型 40-60 条），增加 3-5 条即可。

---

## Overall Assessment

**评分: 3.0 (Findings)**
**置信度: 4/5**

**理由**:
论文是一篇实验认真、报告透明的经验性研究。核心发现（ISR 作为 diagnostic 有效但作为 reward 在所有测试剂量下触发 Goodhart collapse）对 neurosymbolic RL 社区有实际警示价值。实验覆盖面广（6 conditions × 5 seeds × 2 logics × 2 scales），统计分析（CMH + matched controls + trajectory analysis）在该领域属 above-average。

主要扣分因素：
1. **新颖性有限** (Excitement 约 2.5): 核心 insight 是 Goodhart's Law 的直接推论；LOO ablation 是标准方法；论文坦诚承认 "our contribution lies in applying it"。论文需更好地 frame 理论无法预测的经验现象。
2. **写作问题多** (MF1+MF2): ISR 命名不一致是不应出现的错误；Abstract 数据过载是复发问题（Round 3 修复后再次膨胀）。
3. **比较框架不对称** (MF3+MF4+MF5): Table 1 exec-only 单 seed vs ISR 5-seed pooled；OR 反转 framing 不够诚实；SFT PR confound 未充分控制。
4. **实验范围窄**: 单一模型族 (Qwen3) + 单一数据集 (FOLIO)；1.7B 仅单 seed。

**修改后潜力**: 多数 Must-Fix 是 framing/写作问题，可在一轮修改中解决，无需新实验（除可能的 β=0.3 trajectory 补跑）。修复后有望达到 3.5 (Borderline Conference)。是否达到 4.0 (Conference) 取决于 novelty framing 能否让审稿人信服 empirical contribution 的增量足够。

---

## Detailed Comments

### §Abstract (abstract.tex)
- **[MF1]** L3 "Irreducible Solver Rate" 与 Method §3 "Intensional Structural Reward" 冲突。统一名称。
- **[MF2]** 15+ 数字过载。建议结构: (1) 问题+方法 2 句; (2) ISR-as-diagnostic 核心数字 1 个; (3) ISR-as-reward 核心结论 1 句; (4) breadth statement 1 句。目标 ≤4 数字。
- L7 "exhibits qualitatively distinct gaming modes in single-seed 1.7B evaluation" — 措辞暗示比单 seed 更强的 generalization。

### §1 Introduction (introduction.tex)
- **[SF8]** 5 个 \paragraph{} 争议。至少精简 ¶4 "ISR as reward" 段内数据密度（当前含 4 β 值、5 seeds bifurcation、2 trajectory、OR 值）。
- L22 C1 "localizing the failure to RL" — **[MF5]** 弱化为 "consistent with RL-specific failure"。
- L27 "ISR initially yields more genuine output than random controls, but this benefit reverses under stricter classification" — **[MF4]** framing 应将 stricter classification 的反转放在更显著位置。
- L29 "preliminarily observed at 1.7B scale" — 好的限定语，但 "exhibits qualitatively distinct gaming modes" 仍暗示 robust finding。

### §2 Related Work (related_work.tex)
- L20 "primarily regressional, with extremal elements" — Goodhart variant 已指定，v5-R1-W5 可能已解决。
- 建议增加 Amodei 2016, Geirhos 2020 (shortcut learning), DeepSeek-R1 2025。

### §3 Method (method.tex)
- **[MF1]** L44 "Intensional Structural Reward" — 与 Abstract 不一致。
- L56 premise-count confound 讨论完整且诚实，是论文的一个亮点。
- Algorithm 1 仅 6 行 — 方法贡献薄，但论文已诚实定位为 empirical study。

### §4 Experiments (experiments.tex)
- **[MF3]** Table 1 exec-only 行应增加 3-seed 1000-step 数据。Caption 需精简。
- **[SF6]** §4.3 β 呈现顺序应改为升序。
- L91 reward landscape 分析（H7=1+0.75β vs genuine≈1+0.26β）— v5-R1-W6 可能已解决。
- L94 CMH 确实是正文中 first-mentioned test — v4-R1-N4 的严重性在交叉后降级。
- L96 "bound the true effect from above and below" — **[MF4]** 不够准确，需修正。
- §4.5 L141 "No safe scale was observed" — **[SF2]** 改为 "...in this single-seed comparison"。

### §5 Discussion and Conclusion (conclusion.tex)
- 仅 7 行，对实验发现丰富的论文来说讨论不够充分。建议增加 2-3 句讨论：(a) 理论无法预测的经验现象; (b) 对 neurosymbolic RL 的操作建议。

### §6 Limitations (limitations.tex)
- 内容充实，涵盖 temporal snapshot、seed counts、cross-scale、data scale。
- 建议增加 checkpoint 丢失的影响讨论。

### §7 Ethics (ethics.tex)
- 存在且合理。

### Format Compliance
- ✅ 正文 §1-§5 在 8 页内（§5 在 page 8 结束，§6 Limitations 从 page 9 开始）
- ✅ Limitations 位于 Conclusion 之后、References 之前
- ✅ Ethics Statement 存在
- ✅ Double-blind 匿名化（"Anonymous ACL submission"）
- ✅ ACL template with review option
- ⚠️ Table 1 caption 过长
- ⚠️ LOO 缩写未正式定义

---

**报告结束。**

Reviewer 1 评分: 3.5 (Borderline Conference) | Soundness 2.5 | Excitement 3.5
Reviewer 2 评分: 3.0 (Findings) | Soundness 4.0 | Excitement 2.0
Director 综合评分: **3.0 (Findings)** | Soundness ~3.0 | Excitement ~2.5