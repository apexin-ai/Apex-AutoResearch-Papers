---
round: 37
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T12:21:45.032772+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 37 (Fresh Review)

**论文**: "When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition"
**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)
**Reviewer 编排**: R1（方法严谨性 + 实验充分性）、R2（新颖性 + 完整性 + 写作质量）
**审稿模式**: 重新审稿（fresh）

---

## Summary

本文以 NER 为主要 case study（4 个英文数据集、主要使用 7-14B fine-tuned 模型），辅以 RE 和 SQL 的 exploratory extension，系统研究 test-time compute scaling（self-consistency, best-of-N）在 structured IE 上的失败边界条件。核心发现是一个 **correlation-selection gap**：quality estimation 信号能预测输出质量（AUROC 最高 0.82），但 instance-level selection 几乎无增益（<1pp even at N=64）。论文提出一个 diagnostic framework，将失败归因于 output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）两个 co-occurring factors。Entity-level construction 在特定条件下部分绕过了 sample-level bottleneck（+1.40pp on Few-NERD）。

---

## Strengths

**S1. 研究问题重要且及时 [R1, R2 共识]**
在 test-time scaling 被广泛应用于 reasoning tasks 的背景下，系统研究其在 structured prediction 上的失败模式对社区有明确价值。这是一个需要有人回答的问题。

**S2. 实证规模和统计严谨性罕见 [R1, R2 共识]**
44 页含 66 张表格、11 张图，覆盖 4 NER + 1 RE + 1 SQL 数据集、9 种方法类别、7 种 verification 模式。每个 claim 配有 bootstrap CI、permutation test、多重比较校正（Holm-Bonferroni + BH FDR）。这种 thoroughness 在 NLP 论文中极为罕见。

**S3. 诚实的自我限定 [R1, R2 共识]**
论文多处坦承 framework 是 diagnostic 而非 predictive（$R^2 < 0$）、bound 过松（3-12%）、RE/SQL 是 exploratory。这种 intellectual honesty 增强了 credibility。

**S4. Correlation-selection gap 分解有洞察力 [R1, R2 共识]**
将 "signals predict quality but can't select better outputs" 分解为 degeneracy（输出空间坍缩）+ alignment collapse（信号与 gain 脱耦），这个 decomposition 即使降级为 "co-occurring factors" 也提供了有用的分析框架。

**S5. Negative result 符合 ARR H6 guideline [R2]**
"If something systematically does not work where it could be expected to, the community does need to know about it."

**S6. Entity-level construction 提供了 constructive positive direction [R1]**
在以 negative result 为主的论文中，§7.5 的 entity-level construction 证明了绕过 instance-level bottleneck 的可行路径（proof of concept）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. Holm-Bonferroni correction 策略选择存在 cherry-picking 风险 [R1 N1, R2 AGREE]**
全局 Holm-Bonferroni 在 k=57 下 $p_{\text{adj}}=0.055$，未达 α=0.05。论文转而采用 per-family correction（k=10），得到 $p_{\text{adj}}=0.006$。正文引用 per-family 结果，全局结果仅出现在 Appendix/Limitations。两位 Reviewer 一致认为：
- 缺乏 pre-registration 证据证明 family 划分是 pre-specified 的
- 从 k=57 切换到 k=10 降低校正力度约 5.7 倍，构成 post-hoc adjustment
- 核心 claim "LP is the only signal achieving significant positive selection" 在最保守校正下不成立
- 正文需透明报告两种结果并承认边界情况

**MF2. "Simultaneously necessary conditions" 过度 claim [R1 N2, R2 AGREE]**
论文声称 degeneracy 和 signal alignment collapse 是 "simultaneously necessary conditions"（§4, §6.3, Abstract），但：
- 证据结构是 correlational co-occurrence，非 logical necessity
- Bound $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 只 capture 3-12% actual gains——88-97% 的 variance 未被解释
- 移除 degeneracy（如 cross-model ensemble）只 "partially bypasses" bottleneck，不能完全恢复 gains
- 建议改为 "two co-occurring factors that characterize the gap"

**MF3. Framework 无预测力与 title/abstract 暗示的预测性存在张力 [R1 N3; R2 部分同意但认为严重性低于 Must-Fix]**
- Title "Boundary Conditions" 暗示可预测性，但 $R^2 < 0$
- $\theta_{\text{crit}}=0.70$ 是从数据拟合的经验阈值，缺乏 held-out cross-dataset validation
- 论文的 practitioner guidance（"measure degeneracy with N=8 before investing"）依赖某种预测力，但 framework 实际只能 post-hoc 解释
- R2 认为 post-hoc diagnostic 仍有价值（类比医学病理分析），建议降级为 Should-Fix + 修改标题措辞
- **Director 判断**：定为 Must-Fix——title/abstract 的 framing 与实际能力的 mismatch 是可修复的，但不修复会误导读者

**MF4. 与 Yao et al. (2026) 的增量新颖性区分不充分 [R2 N1; R1 部分 REBUT]**
- Yao et al. 已报告 NER/RE 上的 QE correlation（ρ up to 0.47），结论方向一致
- R2 认为：instance-level 分析更细粒度但核心 insight 无质变
- R1 反驳：decomposition（degeneracy + alignment collapse）是实质增量，Yao et al. 没有 failure mechanism 解释
- **Director 判断**：论文确实提供了超越 Yao et al. 的 mechanistic decomposition，但 §1 对此区分严重不足。定为 Must-Fix（positioning 问题可修复）。需在 Introduction 明确说明 instance-level 诊断揭示了哪些 task-level 分析无法发现的现象。

### Should-Fix（影响评分但不一票否决）

**SF1. "Capability-diversity tension" 概念非原创 [R2 N2, R1 AGREE]**
"模型能力越强，输出越收敛" 是 well-known 现象。Yun & Kim (2025) 的 "diversity collapse" 已描述类似机制。Table 66 的 "definitional difference" 过于表面。建议承认已知现象，明确贡献是 NER 上的量化刻画。

**SF2. Related Work 覆盖存在缺口 [R2 N3, R1 部分 AGREE]**
缺少 2024-2025 年的重要进展：
- Conformal Structured Prediction (ICLR 2025)
- NER conformal prediction (arXiv 2601.16999)
- Token-level uncertainty transmission (He et al., NAACL 2024 Findings)
- GPT-NER self-verification (ACL 2025)
R1 认为缺口存在但不应列为 critical——论文核心方向（TTS/SC/MBR）已覆盖。**Director 定为 Should-Fix**。

**SF3. Hidden-state probe 模型不一致 [R1 W1, R2 AGREE]**
主实验用 Qwen3-8B，probe 用 Qwen2.5-7B。Footnote 不充分——probe 结论（"quality information encoded in hidden representations"）未在主模型上验证。

**SF4. 模型多样性不足以支撑 generalization claim [R1 W2, R2 AGREE]**
主要结果来自两个 8B 级别开源模型。4B/14B 是 ablation，72B 是 tentative，GPT-5.5 仅 200 instances。generalization claim 应限定为 "7-14B fine-tuned open-weight models"。

**SF5. RE/SQL 证据过薄但 abstract 呈现偏强 [R1 W3, R2 AGREE]**
RE 仅 SciERC（n=397），SQL 是 pilot（n=196）。Abstract "Cross-task validation on RE" 用词偏强（建议 → "exploration"）。

**SF6. Few-NERD 3 epoch confound [R1 W4, R2 AGREE]**
Few-NERD 唯一使用 3 epoch（其他 5 epoch），也是唯一 positive LP selection 结果。5-epoch degeneracy 从 13% 升至 31%，LP Δ 从 +1.39 降至 +0.12pp。"Feature not bug" 的论证不完全令人信服——需展示 3 vs 5 epoch 的 SC selection gain 变化全貌。

**SF7. θ_crit=0.70 稳定性未系统验证 [R1 W5, R2 AGREE]**
Table 22 的 sensitivity analysis 仅在 SciERC 上做。不同 degeneracy regime（SciERC 12.2% vs Few-NERD 68%）下同一阈值是否合理未论证。

**SF8. Abstract 信息密度过高 [R2 W2, R1 AGREE]**
9 句话含 8+ 数字/符号。建议精简至 2-3 个关键数字。

**SF9. Discussion/Conclusion 过于单薄 [R2 W4, R1 AGREE]**
仅 3 段约 15 行，缺少：框架对其他 structured prediction 的适用性、GPT-5.5 行为差异、practitioner actionable guidance。

**SF10. 术语不一致 [R2 W5, R1 AGREE]**
degeneracy / output convergence / convergence 交替使用。建议统一。

### Minor（不影响接收）

- **M1**: Figure 1 因果箭头暗示了未建立的因果关系
- **M2**: §2.1 前向引用造成理解中断
- **M3**: Proposition 1 entity-wise independence 假设被自身数据部分违反（split-half r≈0.58-0.64），应在主文中注明
- **M4**: Table 3 AUROC binarization threshold 缺 sensitivity analysis
- **M5**: §8 Yun et al. (2025) 对比不够具体
- **M6**: Figure 4 轴标签字号接近可读下限
- **M7**: Appendix 比例 4.5:1（36 页 vs 8 页正文）暗示正文可能遗漏重要信息（如 Holm 分析应在正文总结）

---

## Reviewer Consensus [AGREE]

1. **Holm-Bonferroni correction 策略需要更透明的处理**——核心 LP claim 在全局校正下处于边界
2. **"Simultaneously necessary conditions" 应降级为 "co-occurring factors"**
3. **Capability-diversity tension 不应声称为新概念**——贡献在于量化而非发现
4. **Abstract 信息过载、Discussion 过薄、术语不一致**需要修复
5. **Hidden-state probe 模型不一致、RE/SQL 证据薄、Few-NERD confound、θ_crit 稳定性**均需改善
6. **实验规模、统计严谨性、诚实的自我限定**是论文的突出优势

## Reviewer Divergence [分歧]

1. **与 Yao et al. 的新颖性区分**：R2 认为增量不足以达主会议水平；R1 认为 instance-level decomposition 是实质增量，需更好 positioning
2. **Related Work 缺口的严重性**：R2 列为 critical；R1 认为是 should-fix
3. **Framework 预测力问题的严重性**：R1 列为 must-fix；R2 认为 post-hoc diagnostic 有独立价值，建议 should-fix
4. **Entity-level construction 的意义**：R2 认为 +1.40pp 实际意义有限；R1 认为 proof of concept 价值不应低估

---

## Questions（需要作者澄清）

Q1. 全局 Holm-Bonferroni 的 family 划分是 pre-specified 还是 post-hoc？
Q2. 新任务上 diagnostic framework 的具体使用流程是什么？需要多少 compute 才能得出诊断？
Q3. Entity-wise independence 假设下 bound 只 capture 3-12%——是否考虑过 entity-group level decomposition 来 tighten the bound？
Q4. Qwen 同族变体（如 Qwen3-8B + Qwen3-4B）ensemble 是否能区分 architectural vs random initialization diversity？
Q5. WNUT-17 51% zero-F1 instances 的成因是 entity type rarity 还是 model failure？
Q6. 如果将 Few-NERD 训练到 5 epoch 使 degeneracy 从 13% 升至 31%，对应的 LP selection gain 变化全貌如何？

---

## Missing References

1. Conformal Structured Prediction (ICLR 2025)
2. Uncertainty Quantification for NER via Full-Sequence and Subsequence Conformal Prediction (arXiv 2601.16999, 2025)
3. He et al. (NAACL 2024 Findings) — Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission
4. GPT-NER (ACL 2025 Findings) — LLM-based NER self-verification
5. Xiao & Wang (2021) — LLM Calibration on Structured Outputs（如存在）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 external_review 未开启）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 16 info）。

**Warnings**:
1. **Page 8-9**: 主正文末尾连续 2 页纯文本（Related Work + Discussion + Limitations + Ethics + References），无 display item 收尾。建议在 Discussion 中加总结性 figure/table。
2. **Page 17-20**: Appendix 连续 4 页纯文本（Appendices h-m），无 figure/table 穿插。

**Positive findings**:
- Figure 1 有效传达核心 message，颜色方案色盲友好
- 主正文 8 页含 4 figures + 4 tables = 8 display items（1.0/页），密度合理
- 所有表格使用 booktabs 风格，格式规范
- 无 LaTeX 错误、无 margin overflow、无未解析引用
- Double-blind 合规

---

## Overall Assessment

**评分**: 3.0–3.5 (Findings – Borderline Conference)
- R1: 3.5 (Borderline Conference)
- R2: 3.0 (Findings)

**Director 综合判断**: **3.0 (Findings)**

理由：
1. **统计基础处于边界**（MF1）：论文最核心的 positive claim（LP selection）在最保守校正下 p=0.055，这不是致命缺陷但限制了 claim 的强度
2. **新颖性增量存在但需更好 positioning**（MF4）：instance-level decomposition 超越 Yao et al.，但论文未能在 Introduction 中清晰建立这一区分
3. **Framework 定位存在 mismatch**（MF2, MF3）：title/abstract 暗示的预测性与实际 diagnostic 能力之间的张力需要修复
4. **核心 negative result 有社区价值**：SC 在 NER 上系统失效的证据、correlation-selection gap 的分解、9 种方法的系统比较——这些对 Findings track 有充分贡献
5. **修复路径清晰**：4 个 Must-Fix 均为 framing/reporting 问题而非实验缺陷，revision 可在不增加实验的情况下 address

**置信度**: 4/5（两位 Reviewer 均熟悉 TTS/SC/NER 方法论，仔细阅读了全文 44 页）

**对 Research Director 的建议**（仅为参考，非审稿人职责范围）：
- MF1-MF4 均为 framing/statistical reporting 问题，不需要新实验
- SF6（Few-NERD confound）和 SF7（θ_crit validation）可能需要少量补充分析
- 如果 revision 能 (1) 透明报告全局 HB 结果、(2) 降级 necessity claim、(3) 修正 title/abstract framing、(4) 在 §1 清晰定位 vs Yao et al.，论文可冲击 3.5 (Borderline Conference)