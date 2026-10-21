---
round: 3
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T04:37:45.971979+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 3 审稿报告 — clkc_mech_interp

**Venue**: EMNLP 2026 (via ARR)
**Reviewers**: R1 (方法严谨性) + R2 (新颖性/完整性)
**交叉回应**: 完成，收敛（1 轮交叉即达共识）

---

## Summary

本文研究 Llama-3.1-8B、Qwen3-8B、Gemma-3-4B 中英-中知识冲突信号的线性可探测性与因果相关性。主要发现：(1) 三模型均存在可探测的冲突信号且方向 asymmetry（ZH→EN 比 EN→ZH 高约 7pp）与已知跨语言能力差异一致；(2) 仅 Llama L13 的 steering 产生显著行为翻转，Qwen/Gemma 未成功——论证 detection ≠ causal relevance。论文经过前两轮审稿的实质性修改（前轮所有 issue 已 resolved），当前版本在 framing 和统计严谨性上有明显进步，但仍存在等价性主张过强、因果证据范围有限、贡献定位与证据强度不匹配等问题。

---

## Strengths

1. **研究问题有价值**：跨语言知识冲突的 mechanistic 分析连接 multilingual NLP、knowledge editing 和 interpretability 三个社区，是 timely 且重要的方向。

2. **方向性不对称是非平凡发现**：ZH→EN 迁移比 EN→ZH 高约 7pp，三模型方向一致（Llama +7.3pp [0.4, 14.0]，Qwen +7.2pp，Gemma +6.6pp [1.9, 11.1]）。这不能从 "共享空间存在" 直接推出——共享空间不保证对称迁移，不保证线性可分性。XNLI 基线显示非冲突任务也存在相同方向不对称，将观测归因到通用跨语言结构而非冲突特异编码——这是一个正面发现（排除了替代假说），而非 null result。

3. **"Detection ≠ Decision" 区分**：Llama 正面结果 + Qwen/Gemma 负面结果的对比设计论证 probing accuracy 不意味着因果相关性。虽然原则已有先行文献（Basu et al. 2026），但跨语言场景引入的混淆排除设计有独立实验价值。

4. **统计方法多样化**：TOST + Bayesian BF + binomial + bootstrap CI 多证据链，论文诚实报告 TOST 功效不足（1.4%），展示统计诚信。

5. **多证据链混淆排除**：COMET tercile + token overlap (Jaccard 3-4%) + EN-DE 对照（Jaccard 14.8% 但 Δ=+1.2pp n.s.），EN-DE 对照设计巧妙且有力。

---

## Weaknesses

### Must-Fix（不修复则不可接收）

**[R3-N1] 标题 "Mirror" 等价性主张与统计证据不匹配** [R1 提出, R2 AGREE]

TOST 功效仅 1.4%（需 ±12.5pp margin 才达 80% power），BF₀₁ ≈ 1.5 仅 "directionally consistent but modest"。论文转向 CI 重叠 + 6/6 方向一致性（binomial p = 0.016）作为替代论据，但 CI 重叠不等同于等价检验。标题中 "Mirror" 是全文最强等价性 claim，与正文 "consistent with" 的谨慎措辞不一致。Figure 3 的 ±2pp 灰色带视觉暗示 TOST 有效但功效不支持。

**建议**：标题改为 "... Are Consistent With General Cross-Lingual Asymmetries"；删除或注释 Figure 3 灰色带。

**[R3-N2] COMET tercile 消融 MDD=25.3pp 功效不足** [R1 提出, R2 部分反驳]

MDD=25.3pp 意味着该分析无法检测 <25pp 真实效应。Gemma Δ=+10.3pp 方向与 confound hypothesis 一致但不显著（应在 Limitations 更明确讨论，而非仅被整体无显著性掩盖）。R2 反驳称多证据链（token overlap + EN-DE 对照）部分弥补——特别是 EN-DE 对照：token overlap 4× 于 EN-ZH 但 asymmetry 近零，如果 overlap 驱动 asymmetry 应该在 EN-DE 更强但事实相反。

**共识建议**：(1) 明确标注 COMET tercile 为 underpowered；(2) 补充连续 COMET 回归分析；(3) 论证重心从 COMET tercile 转向 token overlap + EN-DE 对照。

**[R3-N3] 因果证据限于 Llama L13，贡献定位过强** [R1 提出, R2 AGREE]

Contribution 2 "Architecture-dependent causal localization" 暗示跨架构系统性比较发现，实际为一个正面结果（Llama L13, p=0.002）加两个 null（Qwen best p=0.785, Gemma best p=0.148）。Section 5 三个假说（非线性交互、superposition、架构差异）全部 untested。当假说用于支撑独立贡献时，证据标准需更高。

**建议**：(1) Contribution 2 改为 "Causal localization in Llama with negative evidence in Qwen and Gemma"，降级为 exploratory finding；(2) 至少对一个假说提供初步验证（如 Qwen/Gemma L13 probe direction vs steering direction 余弦相似度，或线性 vs 非线性 probe 精度对比）；(3) 考虑 activation patching 等替代因果方法——steering 失败可能反映方法局限而非模型缺乏因果结构。

### Should-Fix（不修复降低论文质量但不阻止接收）

**[R3-W1] 单一 train/test split 缺乏 cross-validation** [R1 提出, R2 AGREE]

Probing 领域标准做法为 k-fold CV（Belinkov 2022）。Cross-seed ±0.12-1.90% 和 seed=123 steering 复现提供部分稳健性，但 bootstrap CI 捕获 within-split variability 而非 across-split variability。

**[R3-W2] Qwen 双重角色** [R1 提出, R2 AGREE]

Qwen 同时作为翻译模型和实验对象。Qwen EN→ZH transfer accuracy 最高（67.3%），方向与 "翻译输出对 Qwen 自然更 aligned" 一致。最干净控制需独立翻译模型。

**[R3-W3] Probe selectivity 未正式评估** [R1 提出, R2 AGREE]

引用 Hewitt & Liang (2019) control task 思路但未执行。缺少随机标签 baseline 或 selectivity 指标。与 Ravichander et al. (2021) "Probing the Probing Paradigm" 高度相关但未引用。

**[R3-W4] 缺少 AUROC** [R1 提出, R2 AGREE]

Balanced accuracy 在单一阈值下操作。AUROC 对 Gemma（88.9% bal acc + zero steering flips）尤其有诊断价值——帮助理解 probe 判别能力是否真如 bal acc 暗示的那样强。

**[R3-W5] α 值选择缺乏理论依据** [R1 提出, R2 AGREE]

α ∈ {±20, ±10, ±5, ±2, ±1} 无规范化。同一 α 在不同模型/层代表不同扰动强度。应用 probe weight norm 或 residual stream std 规范化（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）。

**[R3-NOV] 新颖性被 Basu et al. (2026) 部分削弱** [R2 提出, R1 AGREE with nuance]

"Detection ≠ decision" 原则作为独立贡献增量有限（Basu 2026 已建立 98.2% AUROC + steering 完全失败的先例）。但 R1 指出跨语言维度的混淆排除设计有独立价值。

**建议**：将 Contribution 5 ("detectability does not predict causal relevance") 合并到 Contribution 2/4 中作为支撑证据，而非独立贡献点。保留跨语言实例化的实验设计价值，但不重复 claim 已知原则。

**[R3-W6] Discussion 假说过于投机** [R2 提出, R1 AGREE]

三个假说全部 untested。建议至少提供一个假说的初步验证——如检查 probe direction 与 residual stream 主成分的对齐度，或比较线性 vs 非线性 probe 精度差异。

---

## Reviewer Consensus [AGREE]

1. "Mirror" 等价性 claim 过强，证据仅支持 "consistent with"
2. 因果证据（steering）仅 Llama L13，不足以支撑跨架构普遍性主张
3. Contribution 2 应降级为 exploratory finding
4. Contribution 5 应合并而非独立列出
5. Probe selectivity 未正式评估是方法论缺口
6. α 值应规范化
7. 单一 split 不满足 probing 领域标准
8. Qwen 双重角色需更好控制或更充分讨论
9. Discussion 假说至少需一个初步验证
10. 所有 minor issues (COMET 版本号/代码可用性/Figure 3 灰色带) 应修复

## Reviewer Divergence [REBUT]

1. **R3-N2 严重性**：R1 认为 COMET tercile "本质上无效"；R2 认为 token overlap + EN-DE 对照部分弥补，整体 confound exclusion 仍可接受。**Director 判断**：R2 的论证更有说服力——EN-DE 对照是独立的强证据，但 COMET tercile 本身确实应标注为 underpowered。

2. **跨语言可检测性是否 "expected"**：R2 认为这是共享空间的自然推论，增量有限；R1 REBUT 指出方向性不对称（~7pp）不可直接推出，XNLI 基线是正面发现（归因到通用跨语言结构）而非 null result，共享空间不保证线性可分。**Director 判断**：R1 论证有力——asymmetry 确实是 non-trivial empirical finding，但论文需要更清晰地将 asymmetry（而非 detectability 本身）定位为核心贡献。

3. **Gurgurov et al. (2026) 引用要求**：R2 列为遗漏引用；R1 质疑该文献在双盲截止前是否可公开获取。**Director 判断**：作者需验证该文献的公开时间线，如在投稿前可获取则应引用。

---

## Questions for Authors

1. 是否有计划用独立翻译模型（非 Qwen）重做翻译以排除 Qwen 双重角色混淆？
2. 能否提供 AUROC 数值和 selectivity control task 结果（即使放在 Appendix）？
3. α 值规范化后，Llama L13 的 steering 效果是否仍然显著？
4. 连续 COMET score 作为回归变量与 probing accuracy 的关系如何？
5. Basu et al. (2026) 的发现与本文的具体差异化贡献是什么（beyond 跨语言扩展）？
6. 能否对 Section 5 三个假说中至少一个提供初步验证数据？
7. Qwen/Gemma steering 失败是否可能是方法局限（如 activation patching 是否会给出不同结论）？

---

## Missing References

1. **Ravichander et al. (2021)** "Probing the Probing Paradigm: Does Probing Accuracy Entail Task Relevance?" — 直接论证 probing accuracy 不意味着 task relevance，与本文核心论点高度相关
2. **Pimentel & Cotterell (2021)** — information-theoretic probing 框架，与本文 probe methodology 讨论相关
3. **Gurgurov et al. (2026) "CLaS-Bench"** — 跨语言 steering benchmark（需验证公开可获取性，若投稿前已公开则应引用）

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求**

本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成** (耗时 ~2.5 min)

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | Pages 3-4 | 连续 2 页纯文本（Related Work + Method 开头），无 figure/table/display equation。建议将核心公式提为 display equation 打破视觉单调 |
| ⚠️ Warning | Pages 7-8 | Page 7 仅顶部 Table 3，其余纯文本；Page 8 整页纯文本。建议部分 discussion 定量对比以 summary table 呈现 |
| ℹ️ Info | Page 2 | Figure 1 图内标注文字偏小（~6-7pt），打印边缘可读性可能下降 |
| ℹ️ Info | Page 5 | Figure 2 三子图横向压缩，x 轴 tick label 密集 |
| ℹ️ Info | Page 1 | Abstract 视觉上较长（接近 200 words 上限） |
| ℹ️ Info | Page 9 | Limitations + AI Use + Appendix 共处一页，紧凑但合理 |

统计：0 critical, 2 warning, 4 info。整体排版质量可接受，无严重布局问题。

---

## Overall Assessment

**评分：3.0 — Findings（可被 Findings 接收）**

| Reviewer | 评分 | 核心关注 |
|----------|------|----------|
| R1 | 3.5 (Borderline Conference) | 方法严谨性：TOST power / confound exclusion / CV；但认可 asymmetry 为 non-trivial 贡献 |
| R2 | 3.0 (Findings) | 新颖性：Basu et al. preemption + 贡献定位过强 |

**综合判断**：论文经过三轮修改后在 framing 和统计报告上有显著进步（前两轮所有 issue 已 resolved），研究问题有价值，实验设计整体合理。方向性不对称（~7pp, 三模型一致）是非平凡的实证贡献，混淆排除管线设计（特别是 EN-DE 对照）展示了实验功力。

但当前版本的核心问题是 **claims 范围超出证据支撑**：(1) "Mirror" 标题暗示等价但 TOST 无功效；(2) Contribution 2 暗示跨架构系统性发现但实为 1 正 2 负；(3) Contribution 5 重复已知原则。如果作者将贡献重新定位为 "(a) 跨语言冲突信号的方向性不对称 + (b) Llama 特异性因果定位 + (c) 混淆排除方法论"，论文的贡献-证据匹配度会大幅改善。

Findings 接收合理——贡献足够但存在实质性改进空间。主会议接收需要：(1) 解决标题/贡献的 overclaim；(2) 补充 AUROC + selectivity control + α 规范化；(3) 对至少一个 mechanistic 假说提供初步验证；(4) 明确差异化 vs Basu et al.。

**置信度**：高（双 Reviewer 在核心问题上高度一致，分歧均在严重性程度而非方向）

---

## Detailed Comments

### Abstract & Introduction
- Abstract 最后一句对 Llama-only 的限定出现太晚，建议前移
- Contribution 2 措辞需更精确反映 "一正两负" 结果模式
- Contribution 5 建议合并到 Contribution 2/4 中
- 需加强 vs Basu et al. (2026) 的差异化定位：跨语言混淆排除设计是增量价值所在

### Method (§3)
- §3.3 引用 Hewitt & Liang 但未执行 → 读者期望被违反
- §3.6 α 值选择无 justification，跨模型不可比
- 建议添加 α 规范化公式（如 α_norm = α / ||w_probe|| 或 α / std(h_l)）

### Results (§4)
- §4.3 方向性不对称是最强贡献——建议更突出呈现而非仅作为 "mirror" 支撑
- §4.4 TOST 功效 1.4% 报告是好实践，但结论部分仍倾向 positive framing
- §4.5 COMET tercile 应明确标注 "inconclusive due to low power"；Gemma Δ=+10.3pp 不应被整体无显著性掩盖
- 建议添加 Table: AUROC alongside balanced accuracy
- Table 1 脚注 "Δ_asym is the mean of paired bootstrap differences..." 重要但容易被忽略，建议移入正文 §4.3

### Discussion (§5)
- EN-DE 对照是 strongest confound evidence — 应更突出
- 三个 mechanistic 假说全部 untested → 至少验证一个（如余弦相似度或非线性 probe）
- 与 Basu et al. 的关系未充分讨论

### Limitations
- Cross-seed 报告有效但不替代正式 CV
- Qwen dual role caveat 可更 prominently 呈现
- Gemma COMET Δ=+10.3pp 应在 Limitations 单独讨论而非被整体分析掩盖

### Format & References
- COMET 版本号缺失
- 无代码/数据可用性声明
- Figure 3 灰色带误导性
- 补充 Ravichander et al. (2021)、Pimentel & Cotterell (2021)
- 核实 Marks & Tegmark (2024) venue
- 验证 Gurgurov et al. (2026) 公开可获取性后决定是否引用