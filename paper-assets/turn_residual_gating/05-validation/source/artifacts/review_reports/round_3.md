---
round: 3
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-22T23:09:51.600558+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Re-Review)

**论文**：Why Per-Layer Residual Gating Fails to Fix Multi-Turn Attention Degradation: A Mechanistic Analysis
**目标 venue**：EMNLP 2026 (ARR May cycle, Long paper)
**Reviewer 编排**：2 人（R1: 方法严谨性+实验设计 / R2: 新颖性+写作完整性）
**审稿模式**：Fresh（无上轮记忆）

---

## Summary

本文提出 ThreadGate，一种在 transformer 每层残差路径上添加 content-and-turn-conditioned MLP gate 的方法，目标是恢复多轮对话中衰减的 system prompt 注意力（GAR）。通过五路对照实验（ThreadGate / +PCGrad / Uniform Gate / LoRA-only / Base），作者发现 teacher-forced GAR 收敛至 0.50，但自回归生成时坍塌至 0.015–0.025（20–33× gap）。论文通过 PCGrad 排除梯度方向冲突、gate 值分析排除架构缺陷，将失败归因于 exposure bias。β-steering（β=5）在推理时恢复 GAR 至 0.727，scheduled sampling（单 seed）将 gap 从 31× 压缩至 1.57×。跨模型验证在 Llama-3.1-8B 上确认了 27× gap。

---

## Strengths

**S1. 实验设计严谨的五路对照框架。** 每对配置精确隔离一个因素（turn conditioning / gating mechanism / gradient conflict / fine-tuning），逻辑链条清晰。PCGrad 排除实验遵循 modus tollens 推理范式。[R1, R2 共识]

**S2. 负面结果的诚实报告与深入诊断。** 论文系统追溯失败机制：gate 值反转（§5.1, 27/28 layers, Wilcoxon p=3.73×10⁻⁸）→ 排除梯度冲突（§5.2）→ 分布偏移归因（§5.3）→ 机制特异性确认（§5.4）→ 跨模型泛化（§5.5）。诊断深度在负面结果论文中少见。[R1, R2 共识]

**S3. Exposure bias 对辅助注意力损失的选择性破坏是有价值的发现。** 先前 exposure bias 文献聚焦于主生成目标的质量退化。本文展示 exposure bias 可选择性摧毁辅助注意力目标（GAR 20–33× 坍塌），同时保留主任务（NTP/PPL 不变）。[R2 强调新颖性；R1 认为可预见性较强——见 Divergence]

**S4. β-steering 实验提供建设性证据。** 通过直接操控注意力 logits 恢复 GAR（0.064→0.727），有效区分"表征退化"和"注意力路由失败"。N=50 验证增强可信度。[R1, R2 共识]

**S5. 写作中 scoping hedges 使用得当。** 频繁使用 "under the tested conditions", "consistent with our evidence", "proximal cause" 等限定语。Limitations 章节全面诚实。[R2 正面评价]

**S6. β steering phase transition（β=2→3 跳变）是有趣发现。** [R1 正面评价]

---

## Weaknesses

### Critical Must-Fix（3 项，影响接收决定）

**C1. 自回归评估样本量严重不足（N=5）** [R1-N1, R2 确认]
- 核心发现（TF GAR 0.50 → AR GAR 0.015-0.025）完全基于 Qwen 上 5 条自回归对话。N=5 无法提供有意义的统计推断力。0.015 vs 0.025（ThreadGate vs LoRA-only）的差异无法判断统计显著性。Llama AR 评估同样使用 N=5 pilot（§5.5 提到 N=20 mid-turn 但含义模糊）。
- **要求**：AR 评估扩展到 N≥50；报告 bootstrap 95% CI；条件间做成对显著性检验。

**C2. Scheduled sampling 结果承载过重但仅单 seed** [R1-N3/W3, R2-N2]
- SS 是论文中唯一展示 training-time mitigation 可行性的证据，在 abstract、contribution (2)、discussion、conclusion 中均被引用。但仅基于单 seed，且两个 seed（GAR 0.318 vs 0.418，即 gap 1.57× vs 1.20×）差异达 31%，说明方差极高。Abstract 以确定性语气呈现（"compresses the gap to 1.57×"）存在 overclaim。
- **要求**：至少 3 seeds + mean±std；abstract/conclusion 标注 "preliminary" 或弱化措辞。

**C3. GAR 指标与下游任务性能缺乏因果验证** [R2-N1, R1-W4]
- 论文核心叙事建立在 GAR 之上，但从未验证 GAR 提升是否改善指令遵循质量。唯一下游评估（Appendix C instruction retention）McNemar p=0.077 不显著、r=0.200。β=10 时 PPL 退化到 4.22 说明 GAR 极端提升可能有害。所有 fine-tuned variants PPL≈2.78 且残差流 AUC≈0.98，GAR 改善与生成质量脱节。
- R1 认为 GAR-PPL 脱节是 Should-Fix，R2 将其升级为 Critical——Director 裁定为 **Critical**，因为这影响论文核心 claim 的实际意义。
- **要求**：在 β=0/3/5 条件下评估实际指令遵循质量（IFEval/MT-Bench/自定义 compliance metric）；若无法完成，需在论文中明确承认局限并显著降低 claim 强度。

### Should-Fix（7 项，影响评分但不一票否决）

**S1. Exposure bias 归因缺乏替代假说排除** [R1-N2 Critical, R2-M4 Minor → Director 裁定 Should-Fix]
- §6 承认 KV cache drift 未排除，§8 留给 future work。对宣称 "mechanistic analysis" 的论文，将核心替代假说完全留给 future work 不够充分。但论文已使用 "proximal cause" 等 hedging 语言，且 R2 认为在 scoping 存在的情况下可接受。
- **建议**：设计 TF→AR 切换实验（teacher-forced prefix 到第 k 轮后切换 AR，观察 GAR 退化转折点），或在 §6 用 2-3 句话更充分讨论为什么当前证据倾向 exposure bias 而非 KV cache drift。

**S2. 标题误导 + 副标题 overclaim** [R2-W1, R1-W2]
- 标题 "Why Per-Layer Residual Gating Fails" 暗示 gating 固有失败，但 LoRA-only（无 gate）表现完全相同——真正的发现是 TF 辅助损失在 AR 下通用失效。"Mechanistic Analysis" 副标题与实际分析深度（宏观层面而非 circuit-level）不匹配。
- **建议**：标题更准确反映 exposure bias 核心发现；副标题改为 "Diagnostic Analysis"。

**S3. 跨模型验证不完整** [R1-W1, R2-W4]
- Llama 仅覆盖 3/5 条件（缺 PCGrad + Uniform Gate）。仅两个 7-8B 模型家族。§5.5 使用 median 而主实验使用 mean，有 metric selection 之嫌。§5.5 标题 "Cross-Model Generality" 暗示过强。
- **建议**：补齐 Llama 5-way；mean/median 双报；标题改为 "Cross-Model Replication"。

**S4. 缺少与直接竞争者的实验对比** [R2-W2]
- Split-softmax (Li et al. 2024) 和 Rhea (Hong et al. 2025) 在 related work 中被讨论但无实验对比。论文声称它们 "cannot address exposure bias" 但缺乏实验验证。
- **建议**：至少在一个模型上运行 split-softmax baseline，或明确承认缺乏对比是局限。

**S5. "To our knowledge, the first" 声称不可证伪** [R2-W3]
- Contribution (2) 的 "first" 声称过于狭窄（niche 太窄导致不可证伪），不增加实际新颖性论证。
- **建议**：删除 "first" 修饰语，直接陈述贡献内容。

**S6. 关键数字重复过多** [R2-W5]
- "20-33× gap" 在论文中出现至少 7 次，"0.064 to 0.727" 出现 4+ 次。降低信息密度，给人 padding 感。
- **建议**：abstract/核心结果保留精确数字，后续用 "the TF-AR gap (Table 1)" 回指。

**S7. 无代码/数据发布承诺** [R1, R2]
- 负面结果论文可复现性是最后防线。ARR reproducibility 评分受影响。
- **建议**：投稿时附匿名 GitHub repo。

### Minor（8 项）

- **M1**: GAR-D 全条件接近零（TF 下 ThreadGate GAR-D = 0.02），干预仅在 τ-masked last token 成功，泛化性未讨论 [R1-W5]
- **M2**: Table 1 精度与正文不一致——§4.2 称 spread 0.75pp 但表格两位小数显示 1pp [R2-W6]
- **M3**: r_min 数值正文未报告 [R1-M1]
- **M4**: Table 1 AR 列缺 GAR-D 和 PPL [R1-M2]
- **M5**: Abstract 过密（约 180 词），首次阅读难以消化 [R2-M1]
- **M6**: §7 Conclusion 仅 3 句话，可能过于简短 [R2-M5]
- **M7**: Bib 格式不一致——Raposo et al. 2024 应更新为 ICML @inproceedings；Gromov et al. 年份需确认 [R2-M3]
- **M8**: Figure 4/6 双栏打印尺寸下辨认困难，Figure 5 (c)(d) y 轴标签重叠 [R1-M4, 视觉审查]

---

## Reviewer Consensus [AGREE]

1. **N=5 AR 样本量不可接受**——两位 Reviewer 独立列为 Critical Must-Fix，无分歧
2. **Scheduled sampling 单 seed 不可靠**——两位 Reviewer 均列为 Critical/高优先 Warning
3. **五路对照设计原则上严谨**——两位 Reviewer 均列为核心 Strength
4. **诊断链完整性**——两位 Reviewer 均认可 gate reversal → PCGrad exclusion → distribution shift → TRC 证据链
5. **跨模型验证不完整**——两位均指出 Llama 3/5 条件是弱点
6. **代码未发布**——两位均提出
7. **关键数字重复过多**——两位均注意到 "20-33×" 出现过多次

## Reviewer Divergence [REBUT]

1. **Exposure bias 新颖性**：R1 认为 "可预见性较强"（Excitement 3/5），R2 认为 "真正新颖的发现——先前文献未系统研究 exposure bias 对辅助注意力损失的选择性破坏"（Excitement 3/5，但 S3 强调了具体贡献）。
   - **Director 裁定**：R2 的论证更有说服力——虽然 exposure bias 本身是已知现象，但对辅助注意力损失的选择性破坏（主任务 PPL 不变而 GAR 坍塌 20-33×）确实是文献中未被系统研究的方面。但新颖性受限于缺乏下游验证（C3）。

2. **KV cache drift 严重性**：R1 列 Critical（核心因果声明漏洞），R2 列 Minor（scoping hedges 存在即可）。
   - **Director 裁定**：Should-Fix（S1）。论文已使用 "proximal cause" 等 hedging 语言，但对自称 "mechanistic analysis" 的论文，完全不排除替代假说仍是弱点。需要更充分讨论，但不必强制要求新实验。

3. **GAR 下游验证严重性**：R2 列 Critical，R1 列 Should-Fix。
   - **Director 裁定**：Critical（C3）。GAR 是整个论文的核心指标，缺乏下游验证影响论文实际意义。

---

## Questions to Authors

1. Table 1 中 LoRA-only AR GAR (0.025) 高于所有 gating variants (0.015-0.016)。这是否意味着 gate 在推理时略微有害？多 seed 下是否稳定？
2. β-steering 中 N=5 baseline GAR=0.028 vs N=50 baseline GAR=0.064，差异超过 2×。GAR 对对话长度是否高度敏感？这是否削弱跨设置可比性？
3. Scheduled sampling 两 seed 间 AR GAR 相差 31%（0.318 vs 0.418）。方差来源是什么？是否暗示效果对初始化敏感？
4. 是否尝试过更高 LoRA rank（64/128）？gate 无效性是否可能部分归因于 LoRA 容量已饱和？
5. Teacher-forced prefix 到第 k 轮后切换 AR，GAR 退化临界 k 是多少？这一实验可区分 exposure bias 和 KV cache drift。
6. r_min 具体数值是多少？
7. 是否计划开源代码？

---

## Missing References

1. **Zhang et al. (2024) "Tell Your Model Where to Attend"** — 推理时注意力操控方法，与 β-steering 思路相似，应在 §2 讨论 [R2]
2. **Multi-turn instruction following benchmarks** (IFEval multi-turn variant, MT-Bench) — 论文缺少标准化下游评估 [R2]
3. **Raposo et al. (2024)** Mixture-of-Depths — bib 条目应更新为 ICML 2024 正式版本 [R2]
4. 需核实 Dongre et al. GAR 全称——论文使用 "Goal Attention Ratio"，arXiv 原文应为 "Goal Accessibility Ratio"（跨轮遗留问题） [历史追踪]

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：已完成（0 critical, 3 warning, 10 info）

主要发现：
- **[warning]** Page 3-4 连续两页无 figure/table，纯文本感较强
- **[warning]** Page 7 视觉密度最高——Figure 5 (c)(d) y 轴标签重叠或过于密集，在 150dpi 下已显拥挤
- **[warning]** Page 13 Figure 10 caption 与 Table 3 之间有约 1/3 页空白
- **[info]** Figure 1 右侧 "Mechanism analysis" 区域文字偏小（约 6-7pt），打印/低分辨率下难辨认
- **[info]** Figure 4 bar chart 层号标签字号极小（约 5-6pt）
- **[info]** 无 [?] 未解析引用，色彩语义一致性好，booktabs 风格表格专业

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings**

**Reviewer 评分**：R1 = 3.0 (Findings) / R2 = 3.5 (Borderline Conference)
**Director 综合评分**：3.0 (Findings)

**理由**：

论文在实验设计上表现出色——五路对照框架、PCGrad 排除、多维度诊断链的完整性在该领域论文中少见。Exposure bias 对辅助注意力损失的选择性破坏（主任务 PPL 不变而 GAR 坍塌 20-33×）是有理论价值的发现。

但论文存在三个 Critical 级别的方法论缺陷阻碍其达到 Conference 水平：

1. **统计基础薄弱**：核心量化证据基于 N=5 AR 评估和单种子实验。5 路对比中仅 ThreadGate 有 2 seeds，其余条件单 seed。Scheduled sampling 两 seed 方差 31%。这些共同导致核心结论（"gating produces no measurable benefit"、"all variants collapse equally"）缺乏统计可靠性。

2. **GAR 指标未经验证**：整篇论文围绕一个注意力统计量（GAR）展开，但从未证明 GAR 改善对用户可感知的对话质量有意义。唯一的下游评估不显著（p=0.077）。这使得 "GAR 坍塌 = 失败" 的核心叙事基础不稳固。

3. **Scheduled sampling 作为独立贡献不成立**：单 seed、高方差、确定性语气呈现。

**修改后预期**：如果补充 (1) N≥50 AR 评估 + 3 seeds 全条件覆盖 + 统计检验，(2) β-steering 条件下的下游指令遵循评估，(3) SS 多 seed 结果，论文可达 3.5–4.0（Borderline Conference 至 Conference）水平。当前状态适合 Findings 接收。

**置信度**：4/5——两位 Reviewer 均有高置信度（4/5），核心问题（统计不足）明确且可操作。

---

## Detailed Comments（逐节）

**Title & Abstract**：标题暗示 gating 固有失败但实际发现是 exposure bias 对 TF 辅助损失的通用问题，存在误导。Abstract 约 180 词，信息密度极高但首次阅读难消化。"compresses the gap to 1.57×" 以确定性语气呈现单 seed 结果。

**§1 Introduction**：贡献罗列清晰但 "to our knowledge, the first" 声称过于狭窄。关键数字重复从此处开始。

**§2 Related Work**：覆盖较全面，但缺 Zhang et al. (2024) 推理时注意力操控方法。Split-softmax 和 Rhea 仅定性讨论，无实验对比。

**§3 Method**：ThreadGate 设计描述清晰，Eq. 1-7 技术上正确。r_min 数值未报告。UG（Uniform Gate）描述不够清晰——未说明仍为可学习 MLP。

**§4 Experiments**：五路对照设计原则上严谨，但 N=5 AR 评估和单种子严重削弱定量证据。Table 1 精度与正文不一致（spread 0.75pp vs 表格显示 1pp）。AR 列缺 GAR-D 和 PPL。

**§4.3 β-steering**：Phase transition（β=2→3）是有趣发现。N=50 验证增强可信度。但 β=0 baseline GAR 在不同 N 下差异大（0.028 vs 0.064），引发 GAR 对对话长度敏感性的问题。

**§5 Analysis**：诊断链逻辑清晰。§5.1 gate reversal（Wilcoxon p=3.73×10⁻⁸）有说服力。§5.2 PCGrad 排除合理但仅排除 directional conflict（未排除 magnitude imbalance）。§5.3 exposure bias 归因在 hedging 存在时可接受，但 KV cache drift 替代假说讨论不足。§5.5 Llama 仅 3/5 条件，median/mean 混用。

**§6 Discussion**：KV cache drift 仅一句话讨论，不够充分。Instruction retention 段落占篇幅但结果不显著（p=0.077），建议移入 Appendix。

**§7 Conclusion**：仅 3 句话，可适当扩展 future directions。

**§8 Limitations**：全面诚实，符合 EMNLP 规范。

**Format**：页数合规（8 页正文）。匿名性合规。Bib 格式需统一（Raposo et al. 应更新为 ICML 版本）。