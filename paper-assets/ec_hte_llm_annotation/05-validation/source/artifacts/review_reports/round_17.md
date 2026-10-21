---
round: 17
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T15:24:47.506299+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 审稿报告 — 圆桌合成

**论文**: When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1（方法严谨性）, R2（新颖性 + 完整性 + Related Work）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文推导了一个精确的偏差恒等式（Theorem 1）：当 LLM 标注器在不同子群具有不同误分类率时，标准的全局混淆矩阵校正会引入 δ_s · Δτ / (1−2π̄) 形式的子群级偏差，可能导致因果效应估计反号。基于此恒等式，论文提出 Δτ-free 诊断准则（Proposition 5）和分层贝叶斯校正方法 EC-HTE。实验覆盖 520 个合成配置（R²=0.994）、11 个真实 LLM 混淆矩阵（聚合 R²=0.975）和半合成 NLP 数据（TweetEval 情感、Civil Comments 仇恨言论）。

---

## Strengths

**S1. 核心理论结果正确且有实用价值。** R1 独立执行了完整的矩阵代数推导，确认 Theorem 1（bias = δ_s · Δτ / (1−2π̄)）在所述假设下为精确恒等式。三因子分解具有良好的可解释性：子群误差偏差 × CATE 异质性 × 逆矩阵放大。"全局校正可能有害"这一洞察对使用 LLM 标注做因果推断的研究者有实际警示价值。[R1: 4/5 Soundness, R2: 3.5/5 Soundness]

**S2. 实验验证全面且诚实。** 三层验证架构（合成→半合成→真实数据）设计合理。520 个合成配置 + 100 MC runs + 11 个真实 LLM CM 的覆盖面在同类论文中突出。特别值得肯定的是：论文诚实报告了方法失效的场景（hate speech 数据集、K=8 退化、诊断 AUC=0.63），明确列出五个操作条件，且坦承无真实 LLM-dataset 组合通过全部严格筛选。[两位 Reviewer 均肯定]

**S3. 丰富的敏感性分析。** 对所有五个假设（A1-A5）逐一进行放松验证，32 页附录提供了极为详尽的 robustness checks。方法论清晰（Algorithm 1 完整、DGP 参数全公开、匿名代码仓库提供）。[R1: 4.5/5 Reproducibility]

**S4. 与现有方法的定位清晰。** PPI = Global baseline, per-subgroup DSL = Stratified MLE, HB 增加 partial pooling——这个层级关系让读者准确理解增量贡献。与 Frazis-Loewenstein (2003) 的公式级区分（标量衰减 vs 校正后偏差分解）已在主文展示。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[Critical] W1: 引用完整性问题——三处引用作者归属错误**
- R2 经双重核实发现：(1) `sui2026ppci` 实际作者为 Yang Sui, Jin Zhou 等（UCLA），非论文标注的 "Yijun Sui + Candès"；(2) `audinet2025benchmarking` 实际作者为 Nicolas Audinet de Pieuchon, Adel Daoud 等，非论文标注的 Josias + Egami 等；(3) `ashwin2025bias` 实际作者为 Julian Ashwin, Aditya Chhabra 等，DOI 返回 404。
- 三处独立错误的模式与 LLM 生成的 bib 元数据一致（真实标题 + 错误作者名）。
- 这些引用在全文中被广泛使用（sui2026ppci 至少 6 处引用），修正可能涉及引用上下文的调整。
- **注意**：R1 未独立核实此问题。此发现仅来自 R2 的验证，需 Research Director 在修改时二次确认。
- **严重性判断**：虽然不影响论文的科学贡献，但在 ARR 审稿中构成学术诚信红旗。修复本身是机械性的（核实并修正 bib 条目），但全面审计的工作量不小。

**[Critical] W2: 诊断准则（Proposition 5）在真实 LLM 上接近失效（AUC=0.63）**
- 两位 Reviewer 独立确认并达成共识。合成数据 AUC=0.86，16 个真实 LLM-dataset 组合上降至 0.63（接近随机）。
- 根本原因（两位 Reviewer 的交叉分析一致）：(1) 诊断对 τ_s ≈ 0 的子群不敏感（Proposition 5 设计局限）；(2) 真实 LLM CM 高度非对称（GPT-4.1: FPR=0.38/FNR=0.04）而诊断在对称下推导——两因素交互放大退化。
- **当前状态**：论文已在 Section 5.4 报告 AUC=0.63 并声明操作条件。但 Introduction 贡献列表和 Abstract 仍将诊断列为核心贡献之一。
- **R1 评级**：should-fix（论文已诚实报告��framing 调整即可）。**R2 评级**：critical（AUC=0.63 意味着实践中不可靠，应从"核心贡献"降格）。
- **Director 判断**：鉴于论文确实已在正文报告此数据，且诊断是 identity 的自然推论（而非独立方法），调整为 should-fix 但 framing 修改必须完成。

### Should-Fix（影响评分）

**[Warning] W3: 理论新颖性声明需更精确界定**
- R2 认为 Theorem 1 是 F-L (2003) 标量衰减的 straightforward 子群级推广（数学推导仅需 M_global^{-1} M_s - I 展开）；R1 反驳指出概念层面的非平凡性（F-L 刻画不校正时的衰减 vs Theorem 1 刻画校正后引入的新偏差）。
- **交叉后共识**：数学推导确实 straightforward，但增量在应用语境（LLM annotation + HTE）、诊断可操作性（Δτ-free）和 sign reversal 定量刻画。建议将 "structurally distinct" 改为更准确的措辞（如 "structurally interpretable decomposition"）。
- **分歧**：R2 认为增量不够 Conference（3.0），R1 认为足够（4.0）。这是本轮评分差异的主要来源。

**[Warning] W4: NLP 任务覆盖过窄**
- 仅 TweetEval 情感和 Civil Comments 仇恨言论，均为二分类社交媒体文本任务。对 EMNLP 投稿缺少：多类分类、长文本、非社交媒体域、多语言场景。
- R1 未对此提出异议（隐含接受）。

**[Warning] W5: 操作条件高度限制——实际适用范围存疑**
- 五个操作条件（Δπ>0.15, n_expert≥250, K≤4, FNR<0.50, 非对称时 n_expert≥500）+ "No real LLM-dataset pair passes all screening"。两位 Reviewer 均认为需在 Abstract/Introduction 更早、更显著地声明这些限制。
- R2 交叉回应 REBUT R1-S5 关于 DGP 简单性的质疑：论文已有 K∈{2,4,8} 和 Corollary 6 多类推广。真正的可扩展性限制在 K=8 时已退化。

**[Warning] W6: (A2) 对称假设与真实 LLM 严重不符**
- 两位 Reviewer 共识：真实 LLM 的 FPR/FNR 差异通常 5-16 倍。Theorem 1 本身不依赖 A2（Remark 2），但简化公式和诊断准则均依赖 A2。放松后 R² 降到 0.73（仅 Δπ≥0.10）。主文对 A2 违反的讨论仍需加强。

**[Warning] W7: Appendix D 非对称扩展公式错误**
- R1 独立发现。`(1-FPR_s-1)` 化简为 `-FPR_s`；非对称 bias at z=0 应涉及 FNR_s 而非 FPR_s。虽是非正式扩展段落，但可能误导后续工作。

**[Warning] W8: NLP 社区价值定位不清**
- R2 认为核心贡献偏因果推断/计量经济学（测量误差偏差恒等式），NLP 社区入口仅通过 "LLM 作为标注器" 应用场景。Actionable takeaway 对 EMNLP 读者较窄。R1 未对此提出异议。
- 论文可能更适合 JASA/AISTATS 等因果推断 venue。

---

## Questions（需要作者在 rebuttal 中回答）

1. **引用来源**：三处引用作者归属错误的具体原因？是否使用了 LLM 生成的 bib 条目？全部引用是否经过系统性核实？
2. **诊断实用性**：在真实 LLM 上 AUC=0.63，实践者应如何使用此诊断？是否应总是直接使用 per-subgroup 校正（在满足预算时）而非依赖诊断？
3. **"Exact" 用词**：鉴于真实场景下 A1-A5 几乎无法同时满足，是否考虑用 "closed-form" 或 "analytic" 替代 "exact"？
4. **K 可扩展性**：K=16 或 K=32 时表现如何？K=8 已退化，实际 NLP 子群可能更多。
5. **新颖性定位**：作者认为相对于 F-L (2003) 的核心理论增量具体是什么？能否用一句话精确说明？

---

## Missing References

- **Veitch, Wang, and Blei (2020)** "Adapting Text Embeddings for Causal Inference" — R2 建议在 Related Work 加一句 positioning statement 将本文与 text-as-confounder 文献关联。R1 认为相关性有限（not should-fix），但 1-2 句引用有益。
- **Keith, Jensen, and O'Connor (2020)** "Text and Causal Inference: A Review" — 同上。Appendix F 中已引用但主文未提及。

---

## External Review

**状态：未请求。** 本轮未触发外部审稿。

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-24 15:03 UTC)

| 严重性 | 发现 |
|--------|------|
| ⚠️ Warning | Pages 3-5 连续 3 页无 figure/table（Related Work + 理论推导），可能引起视觉疲劳 |
| ⚠️ Warning | 正文 8 页仅 3 个 display items（Figure 1, Figure 2, Table 1），实验可视化全部在附录 |
| ⚠️ Warning | Table 1（主结果表）出现在正文最后一页，与 Conclusion/Limitations 共享空间，审稿人感觉实验部分被压缩 |
| ⚠️ Warning | Figure 2 红/绿配色对红绿色盲不友好（框内有文字标签辅助区分） |
| ℹ️ Info | Figure 1 蓝色圆点+红色三角形使用形状区分，色盲安全（好的实践） |
| ℹ️ Info | 附录单页包含 4 个 display items，略拥挤 |
| ℹ️ Info | Algorithm 1 出现在附录末尾（p32），可考虑移至正文或附录开头 |

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference**

### 评分理由

**支持 Conference (R1 视角)**：
- 核心理论结果正确且经独立验证（exact identity 而非 bound/approximation）
- 实验设计全面（520 configs + 11 real LLMs + 三层验证）
- 执行质量在同领域论文中属于上乘
- 诚实的适用性报告增强可信度
- 问题识别本身有价值："全局校正可能有害"是新颖且实用的洞察

**支持 Findings (R2 视角)**：
- 核心数学推导较直接（M_global^{-1} M_s - I 展开），对 F-L 的增量有限
- 诊断工具在真实部署场景下接近失效
- NLP 任务覆盖过窄（仅 2 个二分类社交媒体任务）
- 对 EMNLP 社区的 actionable takeaway 有限
- 引用完整性问题需要修复
- 操作条件严格限制了实际适用范围

**Director 裁定**：论文执行质量高，理论结果正确。但两个核心关切决定了 borderline 定位：(1) 诊断——作为第二核心贡献——在实际条件下不可靠（两位 Reviewer 共识）；(2) 新颖性是否足以超越 Findings——R1 认为概念增量成立，R2 认为推导过于直接。引用问题虽然严重（学术诚信信号）但可机械修复。NLP 任务覆盖和 venue fit 的关切有理但非致命。

综合评估 3.5（Borderline Conference）：如果作者能在 rebuttal 中 (a) 解释并修正引用问题，(b) 对诊断贡献做恰当降格，(c) 更精确地界定 vs F-L 的增量边界，论文可达 Conference。否则 Findings 更合适。

---

## Detailed Comments

### 交叉共识区（两位 Reviewer 一致）
1. (A2) 对称假设在真实 LLM 中普遍违反 → 诊断和简化公式受限
2. (A3) balanced Z 不现实 → Appendix T 经验缓解但非理论解决
3. Expert budget (n_expert≥250) 与 LLM 节省成本的动机存在张力 → 需量化 cost-benefit
4. 理论贡献的边界需要更精确的声明 → "correction-layer identity" + "empirically verified propagation"
5. Figure 2 红绿配色需修改

### 交叉分歧区（记录但不影响评分基准）
1. **新颖性**：R2 认为 Conference 不够 → R1 认为概念增量成立。Director 判断：合理分歧，取中。
2. **DGP 简单性**：R1 认为 K>2 覆盖不足 → R2 反驳论文已有 K∈{2,4,8} + Corollary 6。Director 判断：R2 的反驳成立。
3. **真实数据 CI 统计效力**：R2 认为 "所有 CI 含零" 是问题 → R1 认为 coverage 是更合适的评估标准。Director 判断：R1 的论证更严谨。
4. **Related Work (Veitch/Keith)**：R2 认为 should-fix → R1 认为相关性有限。Director 判断：1-2 句 positioning 有益但非必须。

### 给 Research Director 的修改优先级

| 优先级 | Issue | 性质 |
|--------|-------|------|
| P0 | 引用审计（W1） | 学术诚信信号，必须修正 |
| P1 | 诊断 framing 降格（W2） | Abstract/Intro 调整 |
| P1 | 新颖性声明精确化（W3） | "structurally distinct" → 更准确措辞 |
| P2 | Appendix D 公式修正（W7） | 机械性修改 |
| P2 | 14.9% sign reversal contextualization（R1-W4） | Abstract 加限定 |
| P3 | NLP 任务覆盖（W4） | 需额外实验——rebuttal 讨论 |
| P3 | NLP 社区价值定位（W8） | Framing 问题——rebuttal 讨论 |
| P3 | Figure 2 配色（R16-W7） | 低优先级视觉修改 |