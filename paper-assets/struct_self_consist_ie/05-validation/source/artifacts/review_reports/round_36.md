---
round: 36
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T11:14:16.153263+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 36 (Fresh)

**论文**: "When Does Test-Time Scaling Fail? Boundary Conditions for Information Extraction"
**Venue**: EMNLP 2026 (Long Paper, via ARR)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作）
**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识）

---

## Summary

本文研究 test-time compute scaling（self-consistency / best-of-N）在信息抽取中何时失效，以 NER 为主要案例（4 数据集、2 模型家族），附带 RE 和 SQL 的探索性扩展。核心发现是 "correlation-selection gap"：质量估计信号能预测输出质量（AUROC ≤0.82），但 instance-level 选择增益 <1 pp。论文提出四阶段诊断框架，将失效归因于 output degeneracy（12-68%）和 signal alignment collapse（α→0）。作为探索性改进，LP-weighted entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006, per-family k=10; 全局 k=57 下 p_adj=0.055）。实验覆盖 9 个方法类别、N=2-64 scaling、4B-72B model scale ablation，附录达 46 页。

---

## Strengths

**S1. 极为全面的实证调查 [共识]**
9 个方法类别、5 个 confidence signals、4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N=2-64 scaling、4B-72B 规模消融、free-form decoding 消融。46 页附录覆盖 60+ 张表格和 10+ 张图。这可能是目前对 NER 中 self-consistency 行为最详尽的实证研究。

**S2. 统计方法论严谨且诚实 [共识]**
Holm-Bonferroni (k=57)、BH FDR、bootstrap 95% CI、paired bootstrap p-values、TOST 等效检验、power analysis——论文不仅使用了这些方法，还诚实报告了核心发现在全局校正下的边缘状态（p_adj=0.055）。这种统计透明度在 NLP 实证论文中罕见。

**S3. Correlation-selection gap 有实质贡献 [共识]**
Quality estimation ρ 可达 0.38-0.45 但不转化为 selection gain（Table 3/Table 1），这一发现清晰、可复现，对 test-time scaling 的实践部署有直接指导意义。

**S4. 实用的诊断框架 [共识]**
即便术语有待商榷（见 W3），degeneracy/headroom/compression/alignment 四要素分解为从业者提供了可操作的预部署检查清单——"先检查 degeneracy rate，若 >50% 则不值得做 selection"。

**S5. 负面结果的系统化呈现 [共识]**
论文系统排除了 ESJ、MRSC、LSC、supervised combination、trained verifier 等多种潜在方案，充分论证了问题的结构性（structural bottleneck）。

**S6. 跨模型家族一致性 [共识]**
Qwen3-8B 和 LLaMA-3.1-8B 结果高度一致，加上 4B/14B 消融和 GPT-5.5 frontier 证据，增强了发现的泛化性。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [Critical, 共识] 标题范围显著超出实际证据**
标题 "Boundary Conditions for Information Extraction" 暗示对 IE 各子任务的全面研究。实际证据 ~95% 来自 NER（4 数据集 × 2 模型家族完整分析）。RE 仅有 SciERC 1 个数据集的探索性结果（n=397, single seed），SQL 仅在 Discussion 中一句话提及（n=196）。NER 的 set-valued output 与 RE 的 tuple-valued output 有本质结构差异——论文自己在 §7.3 观察到 RE 的失效机制不同（40% zero-F1 来自上游 entity span 错误）。
→ **建议**: 标题改为 "Boundary Conditions for Named Entity Recognition" 或 "...for Information Extraction: Evidence from NER"。

**MF2. [Critical, 共识] 核心正面发现在全局多重比较校正下边缘不显著**
Few-NERD LP selection (+1.39pp) 和 LP-weighted construction (+1.40pp) 在全局 Holm-Bonferroni (k=57) 下 p_adj=0.055，未通过 α=0.05。正文仅使用 per-family 校正（k=21/k=10），全局结果仅在附录 Table 12 中报告。Per-family correction 在统计学中是可辩护的标准做法，但 §7.5 的 prescriptive 建议建立在这个统计边缘的结果之上。
→ **建议**: (1) 在 §7 正文中明确讨论全局校正下 p_adj=0.055 的边缘性；(2) 将 prescriptive results 定位为 exploratory 而非 confirmatory；(3) 强调核心贡献是 diagnostic framework（负面结论），而非 LP construction（正面结论）。

**MF3. [Critical, 共识] SciERC 作为主要测试平台统计 power 有限**
SciERC (n=529) 是论文多项核心分析的主要测试平台（Table 3 quality estimation、Table 1 selection gap、§4 diagnostic analysis），但仅单 seed 且 power analysis 显示 MDE≈1.5pp，而观测效果 +0.2pp 远低于 MDE。不影响 "no signal beats greedy" 结论，但影响 SciERC-specific 诊断细节的可靠性。多数据集设计（CoNLL n=3453, Few-NERD n=32560）部分缓解。
→ **建议**: (1) 在正文讨论 power 限制对 SciERC 结论的含义；(2) 报告 TOST 结果在正文中；(3) 补充多 seed 实验增强说服力。

### Should-Fix（影响评分但不一票否决）

**SF1. [Warning, 共识] "Diagnostic cascade" 术语误导因果解读**
§4 承认 "stages resist decomposition into independent effects (R²<0)" 且 degeneracy 不独立预测 LP gain，这与 "cascade"（暗示顺序依赖）矛盾。实际是两个需同时满足的必要条件（低 degeneracy + 高 LP-F1 alignment），非顺序筛选。ML 社区对 "cascade" 有明确技术含义（Viola-Jones 等）。
→ **建议**: 全文改用 "diagnostic framework" 或 "diagnostic checklist"。

**SF2. [Warning, 共识] Few-NERD 训练 epoch 差异构成混淆变量**
Few-NERD 是唯一 LP selection 显著正向的数据集（+1.39pp），也是唯一使用 3 epochs（而非 5 epochs）训练的。Appendix u 显示 5-epoch 训练使 degeneracy 从 13% 升至 31%、LP 增益减半。Few-NERD 的低 degeneracy（使 LP selection 成功的关键条件）可能部分是 undertraining 产物。论文在 Appendix 有数据但未将其框架化为混淆变量。
→ **建议**: 在正文明确讨论 epoch 差异作为混淆变量，报告 Few-NERD 5-epoch LP selection 结果。

**SF3. [Warning, 共识降级] Novelty 定位不够精确**
"Correlation-selection gap" 作为核心发现，calibration ≠ ranking 在决策理论中是已知原则，Chen et al. (2024a) 和 Yun & Price (2025) 已记录 SC 失效。R2 原列为 Must-Fix，R1 反驳认为诊断框架本身有原创性（9 方法类别系统测试、LP compression 机制解析、entity-level partial match 特有 failure mode），非简单 "新领域应用"。最终共识降级为 Should-Fix（framing 问题非 soundness 问题）。
→ **建议**: §1 明确区分：(a) SC 失效作为一般现象是已知的，(b) 本文贡献是 NER 领域首个系统化量化诊断框架。

**SF4. [Warning, 共识] Related Work 缺失直接相关方向**
缺失：conformal prediction for structured prediction（Fisch et al. 2021, Angelopoulos & Bates 2023）、token-level uncertainty estimation for sequence labeling、trained verifiers 更广泛讨论（Cobbe et al. 2021 在 NER 场景的启示）、structured MBR（Chen et al. 2025）。
→ **建议**: §8 增加一段覆盖这些方向。

**SF5. [Warning, 共识] Capability-diversity tension 证据不足以支撑 claim 强度**
模型规模 4B-14B 有限，GPT-5.5 仅 200 实例 zero-shot 单数据集，72B 仅 "preliminary"。§9 描述为 "structural constraint" 但证据不足。
→ **建议**: 弱化为 "observed tendency within tested scales"，Abstract 移除 "extends beyond NER" 或加限定。

**SF6. [Warning, 共识] §3 自验证实验使用不同模型家族**
ESJ/MRSC/LSC 使用 Qwen2.5-7B 而非主模型 Qwen3-8B。"Models cannot self-verify" 结论可能不直接推广到主模型。结论方向与主实验负面结果一致，但严谨性要求使用相同模型或讨论原因。

**SF7. [Warning, 共识] Constrained decoding 对 LP compression 贡献未充分量化**
LP 在 constrained decoding 下压缩严重（60% 实例 LP range < 0.041 nats），但 free-form ablation 中缺少 LP range/tied fraction 的直接定量对比。
→ **建议**: 补充 constrained vs free-form LP compression 指标对比。

**SF8. [Warning, 共识] Responsible NLP Checklist 不应在 PDF 中**
按 EMNLP 2026 ARR 规定，checklist 应在 OpenReview 表单中填写。当前 PDF 包含 ~1.5 页 checklist（pages 9-10）。
→ **建议**: 提交前从 PDF 移除。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 独立发现并完全一致：
1. 标题范围超出证据（MF1）— 双方列为 critical
2. Cascade 术语误导（SF1）— 双方独立提出相同关切
3. Checklist 格式不合规（SF8）— 双方一致
4. SciERC power 有限（MF3）— R1 提出，R2 完全同意
5. 全局 Holm 校正边缘（MF2）— R1 提出，R2 同意并补充 per-family 校正辩护
6. Related Work 缺失（SF4）— R2 详列，R1 大部分同意
7. Few-NERD epoch 混淆变量（SF2）— R1 发现，R2 交叉回应中高度认可（"自己审稿中未充分注意到的有效关切"）

## Reviewer Divergence [REBUT]

1. **R2-N2 (novelty positioning) 的严重性**: R2 列为 Must-Fix (critical)，认为 correlation-selection gap 在更广泛 ML 文献中非全新。R1 反驳（[REBUT]），认为诊断框架本身有原创性——9 个方法类别的系统测试、LP compression 的机制解析远超 "在新领域观察已知现象"。R1 建议降级为 Should-Fix。**Director 判断**: 采纳 R1 的降级建议——novelty 问题确实存在但属 framing 层面，非 soundness 缺陷。已在 SF3 中体现。

2. **R2-W5 (理论分析 §6 价值有限)**: R2 认为 Proposition 1 bound 过松（3-12%）、entity independence 假设不成立、§6 叙事突兀。R1 反驳（[REBUT]），认为 bound 的诊断价值不依赖 tightness，MBR 联系和 α_crit 有独立贡献。**Director 判断**: 双方各有道理。Proposition 1 的诊断价值有限但不为零；§6 的结构组织确需改善。已在 SF 中保留为 "改善 §6 结构衔接"（issue R35-W5）。

---

## Questions for Authors

1. Few-NERD 使用 3 epochs 而非 5 epochs 是否有特定原因（如过拟合）？是否有 5-epoch Few-NERD 的 LP selection 结果？
2. §3 的自验证实验选择 Qwen2.5-7B 而非主模型 Qwen3-8B 的原因是什么？
3. Free-form decoding 下的 LP tied fraction 具体是多少？与 constrained decoding 的 60.3% 如何对比？
4. 如果 diagnostic cascade 的各阶段不独立（R²<0），那么将 α 识别为 "bottleneck" 的结论是否依赖于各因素可分解的假设？
5. 是否考虑过 token-level uncertainty estimation 作为绕过 entity-level alignment 问题的替代路径？
6. Entity-level construction 在什么样的 degeneracy rate × alignment 条件组合下可以期望显著增益？

---

## Missing References

- Fisch, A., Schuster, T., Jaakkola, T., & Barzilay, R. (2021). Few-shot conformal prediction with auxiliary tasks. ICML.
- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. Foundations and Trends in ML.
- Token-level uncertainty estimation for sequence labeling 文献（具体文献需作者搜索补充）
- Chen et al. (2025) Structure-conditional minimum Bayes risk decoding（已引用但 §8 讨论不足）
- Li et al. (2024) Self-consistency for structured prediction（如直接相关）
- Yao et al. (2024) Tree of Thoughts / Algorithm of Thoughts（作为 test-time compute 替代方法简要提及）

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: Agent 超时（300s timeout）。未产出排版审查结果。如有需要可由用户重新触发。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**置信度: 4/5**

**评分理由**:
- R1 给出 3.5（Borderline Conference），R2 给出 3.0（Findings）
- 交叉分享后共识强化了多项关切：标题 scope overclaim（双方 critical）、正面发现统计边缘性（双方 agree）、SciERC power 限制（双方 agree）、Few-NERD epoch 混淆（R2 交叉后新增认可）
- 论文的实证严谨性突出（S1-S2），但核心正面发现在全局校正下仅 p_adj=0.055（MF2），且唯一正面数据集存在训练配置混淆（SF2）
- 新颖性主要体现为系统化诊断分析而非突破性发现（SF3），这更适合 Findings track
- 标题范围需要收窄以匹配实际证据（MF1）

**Conference vs Findings 判断**:
论文在 NER 领域提供了极为详尽的 test-time scaling 失效诊断，统计方法论达到高标准。但三个因素使其更适合 Findings 而非主会议：(1) 核心正面发现统计边缘；(2) 新颖性偏向系统化梳理；(3) 标题范围与证据不匹配。修复 MF1（标题收窄）和 MF2（正文讨论全局校正）后，作为 Findings 论文有较强竞争力。如能额外解决 SF2（Few-NERD epoch 混淆）和 SF3（novelty 精确定位），有潜力升至 Borderline Conference (3.5)。

---

## Detailed Comments

### §1 Introduction
- Abstract 和 Introduction 的 claim scope 需与证据匹配（MF1）
- "we identify a correlation-selection gap" 定位为发现已知现象在新领域的系统化诊断更准确（SF3）
- Abstract "ρ < 1 pp" 措辞混淆，应改为 "gain < 1 pp"
- Abstract 末句 "extends beyond NER" 超出证据范围，建议移除或加限定

### §2 Diagnostic Framework
- "Diagnostic cascade" → "diagnostic framework" 或 "diagnostic checklist"（SF1）
- 首次使用时明确限定 "we use this term to denote a diagnostic decomposition, not a causal chain"

### §3 How Self-Verification Fails
- 使用 Qwen2.5-7B 而非主模型 Qwen3-8B 需要讨论（SF6）
- ESJ/MRSC/LSC 缩写后续使用频率低，考虑减少缩写

### §4 Where Single-Signal Selection Fails
- SciERC-specific 分析受 n=529 power 限制（MF3），需在此 section 或 Limitations 中讨论
- LP compression 需补充 constrained vs free-form 定量对比（SF7）

### §5 Adaptive Methods
- Cross-model SC（§5.1）和 trained verifiers（§5.2）深度与 §3-4 不成比例，值得更多讨论

### §6 Threshold Regime Analysis
- §6 在全文叙事中有些突兀，建议改善与前后章节的衔接
- Proposition 1 bound 松紧度的 implications 需更明确讨论
- MBR 联系（Proposition 2）有独立价值但可考虑部分内容移入 Appendix

### §7 Experiments
- §7.5 prescriptive results 需明确为 exploratory（MF2）
- Few-NERD epoch 差异需在正文讨论（SF2）
- 全局 Holm-Bonferroni 结果需在 §7 正文出现（MF2）

### §8 Related Work
- 增加 conformal prediction、token-level uncertainty、structured MBR 讨论（SF4）
- Yun & Price (2025) 差异化讨论可进一步加强
- Trained verifiers 文献讨论不足

### §9 Discussion and Conclusion
- "Capability-diversity tension" 弱化为 "observed tendency"（SF5）
- Cascade 阈值的 task-specificity 需讨论

### Limitations
- 当前长度约 3 段，基本合适
- 确认 N-budget 描述已更新到 N≤64

### Format
- Checklist 从 PDF 移除（SF8）
- 确认正文在 8 页内