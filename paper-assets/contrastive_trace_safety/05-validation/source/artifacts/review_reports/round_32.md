---
round: 32
review_mode: continue
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T02:28:29.626723+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 32 审稿报告（Continue Review）

**论文**：Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**：EMNLP 2026 ARR (Long Paper)
**审稿模式**：Continue（基于 R31 报告复审修改）
**Reviewer 编排**：2 人（沿用 R31）
- Reviewer 1：方法严谨性（MF1/MF3/SF1/SF2/SF6 验证）
- Reviewer 2：新颖性/完整性（MF2/R2-N1/SF4 验证）

---

## Summary

基于 R31 报告的 3 Must-Fix 和 6 Should-Fix 意见，论文进行了 5 次 commit 修改。复审结果：**11 项 RESOLVED**，3 项 PARTIALLY_RESOLVED，1 项 STILL_OPEN（页数违规）。所有 R31 Must-Fix 均已解决。无新增问题。

---

## R31 Issue Resolution Matrix

| ID | Issue | R31 Severity | R32 Status | 说明 |
|----|-------|-------------|------------|------|
| MF1 | 32B exploratory caveat | Critical | ✅ RESOLVED | Sec 4.4 开头独立 caveat 段落 + Table 4 *标记 + Discussion 7-8B/32B 分离 |
| MF2 | Multi-layer probing 文献 | Critical | ✅ RESOLVED | Related Work 新增段落覆盖 CLAP/BERTology/Kim |
| MF3 | Conditional inference | Critical | ✅ RESOLVED | Method 3.5 新增段落 + Berk/Lee 引用 + 32B nested CV 缺失标注 |
| SF1 | Position residualization | Warning | ⚠️ PARTIAL | 4/4 模型数据完整；confound vs genuine signal 解读缺失 |
| SF2 | Cosine 因果链 | Warning | ✅ RESOLVED | Discussion + Limitations 双重 correlational caveat |
| SF4 | 页数超限 | Warning | ❌ OPEN | Discussion + Conclusion 仍在 p9 |
| SF6 | K=5 per-model | Warning | ✅ RESOLVED | Method 报告 K=3-7 范围 + 结论方向一致 |
| R2-N1 | C1 新颖性 | Critical | ⚠️ PARTIAL | Framing 改善但 Voita MDL 对比仍浅 |
| R2-W3 | BA 锚定张力 | Warning | ⚠️ PARTIAL | Ensemble 实证缓解，理论讨论缺 |
| R2-W4 | Negative results 关联 | Warning | ✅ RESOLVED | 单段 + 信号属性映射 |
| R2-W5 | Scope 张力 | Warning | ✅ RESOLVED | Practical mitigation 移至附录 |

---

## Strengths（沿用 R31 + R32 新增）

1. **Random-label control 设计精巧**（不变）：通过替换 CP labels 为随机标签，直接证实 CR-composite 的浅层偏好是 label-independent 的几何伪影。两位 Reviewer 均高度评价。
2. **Two-stage design + nested CV**（不变）：validation 探索 + held-out 确认的分离设计，配合 7-8B 的 5-fold nested CV（10/10 folds HS advantage 一致），在 probing 文献中严谨度不常见。
3. **极其详尽的附录**（不变）：26 页覆盖 layer sweep、random-label controls、cosine analysis、multi-seed stability、post-hoc power analysis、nested CV 等。透明度达到 Findings 级别及以上论文的典范标准。
4. **Bug disclosure（Appendix M）**（不变）：主动披露开发中发现的 bug 并完整报告修正过程，展示高度科学诚信。
5. **[R32 新增] Multi-layer probing 上下文化**：Related Work 新段落将 CLAP、BERTology aggregator、Kim et al. 与本文诊断方案清晰定位——"we identify the mechanism; they propose architectural solutions"——形成互补叙事。
6. **[R32 新增] Ensemble 提供可操作解决方案**：三层 ensemble（precision-best + BA-best + inverse-FPR-best），所有 4 模型 p≤0.002，诚实标注 cross-validation 限制。从"发现问题"升级为"发现+解决"。
7. **[R32 新增] Evidence gradient 贯穿全文**：cross-validated / significant / exploratory 三级分类，32B 标注显著改善（独立段落 + MDE + Table 4 * 标记）。

---

## Weaknesses（R32 剩余）

### 格式违规（Critical）

**页数超限**（R22-N5，持续 11 轮未解决）[consensus]

discussion.tex 使用 `\enlargethispage{12\baselineskip}`（12 行强制拉伸），但 Discussion 尾部（~2-3 行）+ 完整 Conclusion 仍在 p.9。按 EMNLP 2026 规定，Sections 1-6（含 Conclusion）必须在 8 页内。两位 Reviewer 均确认违规。commit message 声称 "SF4-fix: Conclusion fully on p8" 但 PDF 实测不符。

R2 建议的压缩策略：Discussion 中 C1/C2 的再次总结与 Introduction 和 Experiments 重复，删除后可缩至 5-6 行，将 Conclusion 挤入 p8。或合并 Conclusion 为 Discussion 末句。

⚠️ 视觉审查 Agent 在 p.9 条目中报告"主文 8 页符合 EMNLP 要求"，与 Reviewer 人工核实矛盾——视觉 Agent 可能将 Conclusion 误归入豁免区域。以 Reviewer 判断为准。

### 新颖性分歧（Persistent，10 轮未收敛）

**C1 概念新颖性**（R23-N3）[divergence: R1 3.5 vs R2 3.0]

- **R1 (3.5, Borderline Conference)**：机制解释（cosine compression → crossing-rate inflation）+ random-label control + ensemble diagnostics 超越了 Belinkov 的一般性讨论。"quantifying severity of a known issue in a high-stakes domain + diagnostic tools" 构成充分增量。类比 Goodhart's Law：已知概念，但在具体领域量化破坏性并提供诊断仍有价值。
- **R2 (3.0, Findings)**：核心发现是 "applying known insight to new domain"。Conference-level 论文需要 conceptual novelty（新方法/新理论/对现有理论的实质挑战），而非 known issue 在新 domain 的量化。Ensemble 是 engineering solution，增加实用价值但不改变概念贡献。
- **Voita & Titov MDL 对比**（双方共识缺失）：MDL probe 基于 description length 而非 threshold，理论上可能天然回避 crossing-rate 问题。若 MDL 在本场景下选深层→支撑 C1；若选浅层→C1 的 "threshold-based 更可靠" 结论需修正。论文仅引用未对比。
- **R1 建议的折中 framing**："We quantify the severity of metric-induced layer selection bias in safety probing, showing it can produce qualitative reversals..."——先定位"量化"，再用"reversal"作具体证据。R2 表示可接受。
- **Director 判断**：R2 的核心批评成立——如果 MDL probe 天然避免 bias，C1 的实际影响需重新评估。但 R1 的反驳也有道理——机制解释 + 诊断工具超越了一般性讨论。novelty 处于 Findings-Conference 边界。Director 倾向 R2，定位 Findings。

### Minor Remaining（Warning）[consensus]

1. **SF1 confound vs genuine signal**（R26-W2/R31-W2）：quadratic residualization 数据完整（4/4 模型），但 QwQ-32B/R1-32B 的 advantage 被吸收是 confound removal 还是 genuine signal removal 未讨论。两位 Reviewer 共识建议加 1-2 句："Whether quadratic residualization removes a confound or genuine position-correlated safety signal cannot be determined from the current design; disentangling these requires causal interventions on position encoding."
2. **Abstract 信息密度**（R23-W4）：结构改善（"robust finding" vs "conditional finding" 分层），但 ~180 words 单段含大量数字，信息过载风险仍在。
3. **BA 锚定张力**（R31-W5）：ensemble 从实证角度充分缓解（三指标聚合后仍显著），理论讨论缺但 minor。

---

## Questions（R32 更新）

1. ~~conditional selective inference~~（已在 Method 3.5 正式引用 Berk/Lee）→ RESOLVED
2. QwQ-32B quadratic residualization 完全吸收 HS advantage：是 confound removal 还是 genuine signal removal？→ OPEN
3. ~~对浅层做 whitening 后是否消除浅层偏好~~（已标注为 correlational + future work）→ ACKNOWLEDGED
4. ~~其他模型的 optimal K~~（已在 Method 报告 K=3-7）→ RESOLVED
5. MDL probe（Voita & Titov 2020）是否存在类似的 metric-induced layer selection bias？若否，C1 的贡献需要什么重新定位？→ OPEN（核心新颖性问题）

---

## Missing References

R31 提出的 5 条均已添加（CLAP, Kim et al., Meyoyan & Del Corro, Berk et al., Lee et al.）。R32 无新增缺失引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warnings, 13 info）。

**Warnings**（与 R31 一致）：
1. **pp3-5 连续纯文本无 display item**：Related Work → Methods 形成"文字墙"。建议将 Figure 1 或方法概览图前移至 p3-4。
2. **Figure 1 直到 p6 才出现**：前 5 页仅 Table 1（p2 顶部，5 行小表）作为唯一 display item，视觉锚点不足。
3. **主文仅 1 Figure + 4 Tables = 5 display items**：对实证论文偏低（推荐 5-8）。附录有 Figure 3 (Pareto front) 和 Figure 4 (probe trajectories) 可考虑提升到主文。

**⚠️ 注意**：视觉 Agent 在 p.9 条目中报告"主文 8 页符合 EMNLP 要求"，与两位 Reviewer 人工核实矛盾。Reviewer 确认 Discussion 尾部 + Conclusion 均在 p.9，主文实际 9 页。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**R31 → R32 变化**：3.0 → 3.0（维持，上界接近 3.5）

**Reviewer 评分**：
- R1: 3.5 (Borderline Conference) — 维持
- R2: 3.0 (Findings, Excitement 2.5→3.0) — 维持
- Director: 3.0 (Findings)

**Confidence: 4/5**

**理由**：

论文在 R32 中完成了高质量的修改——3 项 Must-Fix 全部解决，多层 probing 文献缺口填补，ensemble 提供可操作解决方案，32B exploratory 标注显著改善，conditional inference 正式引用。修改方向准确且执行到位。R32 修改解决率 78.6%（11/14），无新增问题。

维持 3.0 而非上调至 3.5 的原因：

1. **页数违规未修复**（R22-N5）：Discussion + Conclusion 在 p.9，EMNLP hard constraint。持续 11 轮未解决。`\enlargethispage{12\baselineskip}` 是激进排版 hack。
2. **C1 概念新颖性**（R23-N3）：Director 倾向 R2 立场——核心发现是已知 probing sensitivity 在 safety domain 的量化，增量贡献定位于 Findings。Voita & Titov MDL 对比仍缺实质性分析。
3. **SF1 confound 解读缺失**：次要但反映方法论深度不足。

**上调路径**（R2 明确给出）：
- C1 framing 改为 "quantifying severity + diagnostic tools"（而非 "demonstrating a qualitative reversal"）
- 加入 Voita & Titov MDL 对比（即使只是 2-3 句讨论）
- 页数合规

三项全部修复后，R2 可接受 3.5，R1 可考虑 3.5-4.0 上端。

**Findings 定位理由**：经验性方法论贡献扎实（random-label control, nested CV, ensemble diagnostics），实验透明度高（26 页附录 + bug disclosure），对 safety probing 实践有直接参考价值。论文的整体完整性（problem→mechanism→diagnosis→solution）在 R32 中显著提升。

---

## Detailed Comments

### R32 修改质量评估

**高质量修改**：
- MF1 (32B caveat)：独立段落 + 表格标记 + Discussion 分离——三层次修改，全部到位
- MF2 (multi-layer probing)：Related Work 新段落不仅引用到位，还分析了 CLAP 在 CoT 场景的 scalability 限制，体现了领域理解
- MF3 (conditional inference)：从"附录脚注"提升到"主文段落+正式引用"，严谨度显著提升
- SF6 (K robustness)：不仅报告了 K range，还明确了结论方向一致性——超出了最低修改要求
- R2-W4 (negative results)：从多段列举压缩为单段信号属性映射——信息密度提升且与主线关联更紧

**待改善**：
- R22-N5 (page limit)：commit message 声称修复但 PDF 不符——建议在 commit 前验证编译后 PDF
- SF1 (confound)：数据层面完整但解读层面缺失——需要 1-2 句讨论 confound vs genuine signal
- R23-N3 (C1 novelty)：Voita & Titov MDL 仅引用未对比——应讨论 MDL 是否天然避免 threshold-crossing bias

### 持续追踪项

| Issue | 轮次跨度 | 状态 | 备注 |
|-------|---------|------|------|
| R22-N5 页数 | R22→R32 (11轮) | ❌ OPEN | 格式 hard constraint，desk-reject 风险 |
| R23-N3 C1 novelty | R23→R32 (10轮) | ⚠️ IN_PROGRESS | 持续 R1/R2 分歧，Director 倾向 R2；R2 给出收敛条件 |
| R26-W2 QwQ quadratic | R26→R32 (7轮) | ⚠️ IN_PROGRESS | 数据完整，confound 解读缺 |
| R31-W5 BA 锚定 | R31→R32 (2轮) | ⚠️ IN_PROGRESS | Ensemble 实证缓解，minor |

### R32 修改统计

- **5 commits**，覆盖 related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, references.bib
- **11/14 R31 issues RESOLVED**（78.6% 解决率）
- **0 新增 Must-Fix**
- **0 新引入问题**
- **R32 剩余**：1 Critical（页数）+ 1 Persistent divergence（C1 novelty）+ 3 Minor warnings