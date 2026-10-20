---
round: 21
review_mode: continue
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T07:53:20.464619+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 21 审稿报告 — Solver Trace Ablation (EMNLP 2026 ARR Long Paper)

**审稿模式**: 继续审稿（基于 Round 20 修订评估）
**Reviewer 配置**: R1（方法严谨性 + 实验有效性）+ R2（新颖性 + 完整性 + 写作质量）
**轮次**: 2 轮（独立初审 + 交叉回应），关键问题达成共识

---

## Summary

论文在 Round 20 后进行了 R21 batch 修改，针对 11 个 issue 做了系统性修订。修订质量高：ISR 被重新定位为 component-necessity diagnostic（非 structural quality），SFT 被明确标注为 pre-RL reference（非 PR-matched control），5-seed 结果和 1.06× deconfounded ISR* 在 Table 1 主表呈现，N-H 定义为 upper bound，CMH 三处标注 N=3 caveat，ProofFOL C2 拆分为 confirmed/exploratory，rlsf bib 作者修正，4 篇缺失引用补齐。

双 Reviewer 确认 10/11 个 R20 issue 修复充分。唯一共识性残留问题是 Title/Abstract 与正文的系统性矛盾（Title 称 "Structural Degeneration"，正文 §3.2 明确 ISR 不衡量 structural quality）。

核心限制不变：单模型 Qwen3-4B、ISR-quality gap (ρ=−0.049)、3-seed 统计效力、有限的技术新颖性。这些是实验设计层面的 inherent limitations，无法通过文字修订解决。

---

## Strengths

**S1 [共识]**: R21 batch 的 claim calibration 达到高标准。ISR → component necessity 术语统一彻底（§3.2 line 44: "ISR quantifies component redundancy, not semantic faithfulness"），SFT 段落诚实承认 PR confound（§4.2 line 33），N-H 在方法段即定义为 upper bound（§4.1 line 12）。这种系统性 self-limitation 在投稿论文中不常见。

**S2 [共识]**: Table 1 结构性改进显著。5-seed 行（N-H=23% vs 3-seed N-H=6%）使 bimodal 分裂在主表可见；1.06×‡ 直接展示 deconfounded ISR*。读者不再需要 Appendix 考古即可获得完整画面。

**S3 [共识]**: C2 contribution 的 Prolog-confirmed / ProofFOL-exploratory 拆分（Introduction line 40）是精确的 claim calibration。结合 §4.1 前置声明 "ProofFOL results are exploratory"，p=0.10 结果的过度解读风险已消除。

**S4 [共识]**: 实验对照体系（6 种 reward condition + shuffled-ISR + premise-count matching）在修订后更加突出。Shuffled-ISR control 有效排除分布形状作为 Goodhart driver（双 Reviewer 共识 v16-R1-W4 降级为 info）。

**S5 [共识]**: 引用覆盖全面。rlsf 幻觉作者修正，DeepSeek-R1/NLProofS/V-STaR/Easy-to-Hard 补齐。Related Work 的 dataset-dependent asymmetry 新颖性定位有效。

---

## Weaknesses

**W1 [major, 新发现, 共识]**: **Title/Abstract 与正文系统性矛盾**。Title "Solver Trace Ablation Reveals Structural Degeneration" 暗示 STA/ISR 直接检测到结构退化，但正文 §3.2 明确 ISR 只衡量 component necessity（ρ=−0.049 with NLI）。从 ISR→0 到 "structural degeneration" 的推理需经 hacking taxonomy 中介（Method line 78），且 taxonomy recall 未知。双 Reviewer 交叉后统一为 STILL_OPEN [major]。建议 Title 改为 "Component-Level Collapse" 或 "Structural Shortcuts"，Abstract 首句同步修改。*（注：正文内部的概念统一已完成，此 issue 仅限 Title/Abstract。）*

**W2 [major, inherent, 共识]**: **单模型 Qwen3-4B 外部效度**。修订通过显式限定（"Qwen3-4B case study"、"in settings similar to ours"）解决了 framing 问题，但实验证据本身未增加。论文自引 Shao et al. (2025) 指出 RLVR effects may be Qwen-specific，使通用性推断存在风险。

**W3 [major, inherent, 共识]**: **ISR 与语义质量不相关**（ρ=−0.049, p=0.187）。修订通过术语统一和 taxonomy 中介缓解，但根本性效度 gap 不变。ISR 的诊断价值依赖 hacking taxonomy 的 mode classification，而 classifier recall 未知（论文自承）。

**W4 [moderate, inherent, 共识]**: **3 seeds 统计效力不足**。5-seed 扩展缓解但不解决——PR σ=47pp (3-seed) 和 σ=19pp (5-seed) 表明即使 5 seeds 也不收敛。N=3 真实重复的根本限制不变。

**W5 [moderate, 分歧]**: **技术新颖性有限**。R2 认为 LOO ablation 是标准技术、Goodhart 是已知现象，dataset-dependent asymmetry 是"有趣的经验观察而非概念进步"，缺乏理论深度（未解释 WHY FOLIO 被 game 而 ProofFOL 不会）。R1 认为 empirical contribution（8-mode taxonomy、shuffled-ISR deconfounding、practitioner guidelines）在 ACL venue 有独立价值。共识："适中"新颖性，足以支撑 Findings，Conference 需额外理论深度。

**W6 [minor, 共识]**: V-STaR bib 应更新为 COLM 2024 venue。Table 1 ISR (5-seed) ISR* 仅显示 "‡" 无具体值。新增引用整合略机械（NLProofS 定位、easy-to-hard 连接）。缩写密度高（Introduction ~15 个，8 页限制下难以避免）。

---

## Questions

Q1: 是否计划将 Title 修改为更精确反映 ISR 衡量内容的表述（如 "Component-Level Collapse" 或 "Component Necessity Collapse"）？当前 Title 与正文 §3.2 的定义存在明确矛盾。

Q2: 论文观察到 FOLIO 上 P→P yields ISR≥0.5 而 ProofFOL 上 hacking yields ISR=0——是否有进一步分析解释 WHY 两个数据集的 hacking geometry 不同（如 premise count 分布、问题结构差异如何决定 ISR gamability）？这将显著提升新颖性。

Q3: ISR (5-seed) 行 ISR* 仅显示 "‡"——是否可以提供 premise-count-matched 值，或在 caption 中明确说明省略原因？

---

## Missing References

R21 batch 已补齐 R20 标记的全部缺失引用。R21 新发现：
- V-STaR (Hosseini et al., 2024) 已被 COLM 2024 接收，bib 应更新 venue。
- 无其他缺失引用。

---

## External Review

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

**状态**: 完成（3 warning, 16 info, 0 critical）

主要发现：
- **Warning**: 首页纯文本无视觉锚点（Figure 1 在 page 2，功能正常但首印象偏文字密集）
- **Warning**: Pages 5-6 连续纯文本（Experiments §4.1-4.3），无 figure/table 穿插
- **Warning**: Pages 7-8 display items 堆积（Table 1 + Table 2 在 page 7，Figure 2 + Figure 3 在 page 8）
- 无 margin 溢出、LaTeX 错误、未解析引用
- 主文 8 页正文 + Limitations 开头，页数合规
- Figure 3 多类别柱状图色盲友好性待确认（建议补充 hatching）

视觉审查与 R20 一致：display items 分布不均（前密后疏），排版风险在 DDL 前不建议大改。

---

## Overall Assessment

### 评分: 3.0 (Findings)

| Reviewer | 初审 | 交叉后 | 维度侧重 |
|----------|------|--------|---------|
| R1 | 3.5 | 3.5 | 实验严谨性、claim calibration |
| R2 | 3.0 | 3.0 | 新颖性、理论深度 |

**评分分歧分析**: R1 (3.5) 与 R2 (3.0) 的分歧是 calibration 差异而非事实判断分歧——两人对论文优缺点的识别高度一致。R1 更重视实验设计严谨性和修订版的 claim calibration 质量（认为这在同分段论文中属于上乘），R2 更重视技术新颖性和理论深度（认为标准技术 + 经验观察不足以支撑 Conference）。

**Director 判定**: 采纳 3.0 (Findings) 作为主评分。理由：
1. R2 关于 "Conference 与 Findings 的分界线在于 substance 而非 framing" 的论据更具说服力——R21 batch 改善了 presentation 和 framing，但未增加新实验证据或理论深度
2. ISR-quality gap (ρ=−0.049)、单模型、3-seed power 三个 inherent limitations 共同约束了论文的 impact ceiling
3. R1 认为 Title 修改可推至 borderline 4.0 的判断被 R2 有效反驳——Title 修改解决的是表述错误，不增加 novelty 或 evidence

**但应记录**: 论文处于 Findings 上沿。修订版的 claim calibration、实验对照体系、数据透明度均超过多数同分段论文。如果补充第二个模型的验证或提供 hacking geometry 的理论分析，有潜力升至 Borderline Conference。

### Confidence: 4/5

---

## Detailed Comments

### R20 Issue 修复验证清单

| ID | 问题 | R1 | R2 | 共识 |
|----|------|-----|-----|------|
| v17-R12-W1 | 单模型通用性声明 | RESOLVED | RESOLVED | ✅ |
| v18-R12-W1 | ISR 概念滑移 | STILL_OPEN | RESOLVED→STILL_OPEN | ⚠️ Title/Abstract |
| v18-R1-W3 | SFT baseline 不公平 | RESOLVED | RESOLVED | ✅ |
| v19-R12-W1 | CMH pseudo-replication | RESOLVED | RESOLVED | ✅ |
| v19-R12-W3 | ProofFOL overcited | RESOLVED | RESOLVED | ✅ |
| v19-R1-W6 | Classifier recall unknown | RESOLVED | RESOLVED | ✅ |
| v20-R2-W7 | rlsf bib 作者错误 | RESOLVED | RESOLVED | ✅ |
| v20-R12-W4 | 5-seed 在 Table 1 | RESOLVED | RESOLVED | ✅ |
| v20-R12-W5 | 1.06× 呈现不足 | RESOLVED | RESOLVED | ✅ |
| v8-R12-N1 | Goodhart 新颖性定位 | RESOLVED | RESOLVED | ✅ |
| v16-MR | 缺失引用 | RESOLVED | RESOLVED | ✅ |

### R21 新发现

| ID | 问题 | 严重程度 | 共识 |
|----|------|---------|------|
| v21-R12-W1 | Title/Abstract 矛盾 | major | 双 Reviewer |
| v21-R2-N1 | V-STaR bib venue | info | 双 Reviewer |
| v21-R2-N2 | Table 1 5-seed ISR* 缺值 | info | 双 Reviewer |
| v21-R1-N1 | 引用整合机械 | info | R1+R2 partial |

### 仍在 In-Progress 的 Issue

| ID | 问题 | 严重程度 | R21 变化 |
|----|------|---------|---------|
| v17-R1-W9 | Seed 43 T=0.7 | info | 不变 |
| v16-R1-W2 | LOO 独立性未量化 | warning | 不变 |
| v16-R1-W4 | 乘法耦合混淆 | info | ↓ 从 warning 降级 |
| v13-R2-W4 | 缩写密度 | info | 不变 |
| v17-VISUAL-LAYOUT | Display items 不均 | warning | 不变 |
| v17-VISUAL-FONT | Figure 文字偏小 | info | 不变 |

### 与 R20 评分对比

| 维度 | R20 | R21 | 变化 |
|------|-----|-----|------|
| Overall | 3.0 | 3.0 | 不变 |
| Presentation | 改善空间大 | 显著改善 | ↑ |
| Claim calibration | 多处 overclaiming | 系统性 self-limitation | ↑↑ |
| Evidence strength | 受限于 inherent limitations | 不变 | → |
| Novelty | 不足 | 适中（dataset-dependent asymmetry） | ↑ |
| Transparency | 关键数据在 Appendix | Table 1 展示完整 | ↑ |

---

*Report generated: Round 21, 2026-05-21*
*Reviewers: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 写作质量)*
*Visual Check: Done (3W/16I/0C)*
*External Review: Not configured*