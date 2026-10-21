---
round: 4
review_mode: continue
overall_score: weak accept
timestamp: 2026-05-24T09:47:33.409986+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: ICML 2026（Round 4 从 CoRL 切换）
**审稿日期**: 2026-05-24
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Novelty + 贡献度 + 写作质量）
**轮次**: Round 4 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
**上轮评分**: Round 3 Weak Reject (5/10, CoRL)

---

## Summary

论文从 Round 3 (Weak Reject 5/10, CoRL) 转投 ICML 2026 并进行了多项修订：(1) TAWM/MPC 对比措辞弱化为 "hypothesized structural factor"；(2) Discussion 新增 exp_045 self-recovery 数据（302K 步后 NVE 4.91× → 0.05×, eval 94.7% baseline），解决了步数不对等问题；(3) Online CIVO Detector 降级为 "preliminary diagnostic" 并披露 Clopper-Pearson CI；(4) Walker Walk 扩展至 5 seeds。

然而，模板仍为 corl_2026（未切换 icml2026.sty），缺少 ICML 要求的 Impact Statement，且存在 IQM 计算错误（n=5 seeds 报告了 n=4 的 IQM 值 175.2，正确值应为 148.8）和 seed 数量叙述不一致（methodology/conclusion 说 4 seeds，results 说 n=5）。

---

## Strengths

1. **Factorial design 系统严谨**（2/2 共识，持续优势）：43 配置 × 4-5 seeds × 5 环境，primary/secondary comparison 清晰标注
2. **LOEO 交叉验证统计可信度高**：AUROC=0.981 (LOEO, 3 folds)
3. **四级干预层级分析**：gradient/output/representation/architecture 提供系统性 negative result。Gradient magnitude ≠ causal importance 的发现有洞见
4. **ManiSkill discriminative validity**：NVE 诊断正确区分 CIVO 与 transient
5. **Dual-critic convergence insight**：ρ > 0.999 揭示 imagination-based 训练中 Double Q pessimism 的结构性失效
6. **exp_045 self-recovery 数据**（Round 4 新增）：302K 步后完全恢复（eval 94.7% baseline），充分证明 105K 步足以观察 onset 且 recovery 计算成本高
7. **Venue 切换至 ICML**：消除了 Round 3 的核心矛盾（CIVO locomotion-specificity vs CoRL manipulation focus）
8. **措辞诚实度提升**："hypothesized structural factor"、"preliminary diagnostic"、Limitations 诚实全面

---

## Weaknesses（按严重性排序）

### Critical（影响接收决定）

**W-C1. 模板仍为 corl_2026，未切换至 icml2026.sty [2/2 共识，Round 4 新发现]**
main.tex:5 仍使用 `\usepackage{corl_2026}`，PDF 页脚显示 "Submitted to the 10th Conference on Robot Learning (CoRL, 2026)"。ICML 2026 要求使用 icml2026.sty 模板。**Desk reject 风险极高。**

**W-C2. 缺少 Impact Statement [R2 发现，R1 承认审查遗漏]**
ICML 2026 要求论文在 References 前包含 Impact Statement section。当前论文完全没有此 section。**Desk reject 风险。**

**W-C3. IQM 计算错误——数据完整性问题 [R2 发现并独立验证]**
results.tex:81 报告 "IQM $175.2$, $n{=}5$"，但经验证：
- Walker 5 seeds eval: {63.6, 82.8, 95.8, 267.9, 268.0}
- n=4 IQM（trim 1 each side）: mean(82.8, 267.9) = **175.35 ≈ 175.2** ✓
- n=5 IQM（trim 1 each side）: mean(82.8, 95.8, 267.9) = **148.8** ≠ 175.2

IQM 175.2 是 n=4 的正确值；添加第 5 个 seed（eval 95.8）后未重新计算。对于一篇以统计严谨性为卖点、引用 Agarwal et al. (2021) 的 diagnostic paper，此错误损害可信度。**错误性质为 careless 而非 systematic，不影响核心结论（CIVO 在所有 5 seeds 中出现），但必须修复。**

### Warning（影响评分但不一票否决）

**W-W1. Seed 数量叙述全文不一致 [R1 提出，R2 系统验证]**
| 位置 | 文本 | 问题 |
|------|------|------|
| methodology.tex:32 | "Key configurations use **4** seeds" | 实际 Walker 是 5 seeds |
| results.tex:81 | "all **five** Walker Walk seeds...n=5" | 正确 |
| conclusion.tex:10 | "Statistical power with **4** seeds" | 与 n=5 不一致 |
| Figure 2 caption | "n=3 seeds plotted; seed 4 data in Table" | 未提及 seed 5 |

**W-W2. "gradient diversity" 术语无支撑证据 [2/2 共识，PARTIALLY RESOLVED]**
results.tex:166: "the min operation in wide dual-critic may instead regularize through gradient diversity (Appendix G)"。Appendix G 未提供 gradient diversity 的量化证据。建议改为 "may instead function through a capacity-dependent mechanism during early training" 或 "the mechanism is an open question"。introduction.tex:13 的 "different mechanism" 措辞更恰当。

**W-W3. 贡献模式——scope 和 significance 有限 [延续 Round 3，2/2 共识]**
- 核心结论仍是 negative（no reliable intervention eliminates CIVO）
- 最有效 "solution" 是不使用该功能（embedding removed = 100% prevention）
- CIVO 仅在 locomotion 中复现
- 在 ICML 语境下，systematic negative result 的贡献度评价比 CoRL 更宽容，严重性降级

**W-W4. ManiSkill 和 Cheetah Run baseline eval 值缺失 [延续 Round 3，未修复]**
Table 1 中这些环境缺少 vanilla DreamerV3 baseline eval 值，读者无法判断相对性能。

### Minor

**W-M1. "causal chain" 措辞 [R2 建议]**
results.tex:4 中 "establish a causal chain" 暗示因果推断，factorial ablation 提供 predictive/associative 证据。建议改为 "trace a pathway" 或 "establish a predictive chain"。

**W-M2. Abstract "isolate" 残留 [R1 minor，R2 REBUT 降级]**
R2 认为 "isolate" 在 factorial ablation 语境中是标准用语，不构成 overclaim。Director 同意——minor at most。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识度 |
|------|----|----|--------|
| 模板 corl_2026 (NEW) | CRITICAL | CRITICAL (AGREE) | **2/2 一致** |
| Impact Statement 缺失 (NEW) | 承认遗漏 | CRITICAL | R2 独立发现 |
| IQM 计算错误 (NEW) | — | CRITICAL (验证) | R2 独立发现 |
| Seed 数量不一致 (NEW) | 提出 | AGREE (更严重) | **2/2 一致** |
| R1-W2 步数不对等 | RESOLVED | AGREE RESOLVED | **2/2 一致** |
| R2-W1 TAWM 对比 | RESOLVED | AGREE RESOLVED | **2/2 一致** |
| R3-N-new-1 Detector 样本量 | RESOLVED | AGREE RESOLVED | **2/2 一致** |
| R3-N-new-2 Dual-critic | PARTIALLY | AGREE PARTIALLY | **2/2 一致** |
| R2-W4 Becker-Ehmck | 仍未引用 | 接受混淆解释 | **R2 覆盖，non-issue** |
| Significance | Good (borderline) | Fair | **分歧（minor）** |

---

## Reviewer Divergence

**1. Significance（R1: Good borderline vs R2: Fair）**
- R1：dual-critic convergence insight 和 systematic negative result 在 ICML 社区有价值
- R2：negative result + no reliable fix 的贡献模式 significance 有限
- **Director 判断**：R1 borderline Good 合理但偏乐观。ICML RL track 接受 systematic negative results，但论文的 actionable output 确实有限。综合约 Fair+ (2.5/4)。

**2. "isolate" 严重性（R1: minor vs R2: non-issue）**
- R1：与 "strongest predictor" 不一致
- R2：factorial ablation 中 "isolate" 是标准用语
- **Director 判断**：同意 R2。Minor at most。

---

## Questions for Authors

1. IQM 175.2 是 n=4 的值——请重新计算 n=5 的 IQM（经计算应为 ~148.8）并更新 results.tex:81。
2. methodology.tex:32 说 "4 seeds"，results.tex:81 说 "n=5"——Walker Walk 的实际 seed 数是多少？请统一全文叙述（methodology.tex:32, conclusion.tex:10, Figure 2 caption）。
3. 是否计划切换到 icml2026.sty 并添加 Impact Statement？这两项是 desk reject 风险。
4. results.tex:166 中 "gradient diversity" 在 Appendix G 中是否有量化支撑？如果没有，是否考虑弱化措辞？
5. Wide dual-critic 在 Walker 3/4 prevention 但 Cheetah 0/1——是否有对 environment-dependence 的解释？

---

## Missing References

Round 3 遗留的 Becker-Ehmck 2023 问题已解决：R2 确认混淆解释合理（实为 Benechehab et al. 2023，已引用于 related_work.tex）。无新增缺失引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 critical, 4 warnings, 12 info）。

**主要发现**：
1. **[critical] 前 4 页无 display item**：连续 4 页纯文本，第一个视觉锚点（Table 1）直到第 5 页。建议将 Figure 6（CIVO 机制图，当前 Appendix page 17）提前到 Section 1/3。
2. **[warning] 正文 display item 密度偏低**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），实证型论文通常期望 6+。
3. **[warning] Section 3 跨 2 页纯文本**：复杂实验设计无图示辅助。
4. **[warning] Discussion + Conclusion 挤在同一页全纯文本**。
5. **[warning] 最后一页 Table 22 仅占 35-40%**，大面积空白。
6. **[info] 图表质量良好**：Figure 1/2 清晰，Table 1/2 booktabs 规范，ROC 曲线标注清晰。
7. **[info] Figure 6（CIVO mechanism diagram）是全文最有解释力的图**，强烈建议简化版移入正文。

---

## Overall Assessment

**评分: Weak Accept (6/10)**
**置信度: High (4/5)**

**与 Round 3 (Weak Reject, 5/10, CoRL) 的变化**：

| 维度 | Round 3 | Round 4 | 变化 |
|------|---------|---------|------|
| Venue fit | STILL_OPEN (CoRL mismatch) | **RESOLVED** (→ ICML) | ▲▲▲ |
| 步数不对等 | STILL_OPEN | RESOLVED (exp_045 data) | ▲▲ |
| TAWM 对比 | STILL_OPEN | RESOLVED (hypothesized) | ▲▲ |
| Detector 样本量 | OPEN | RESOLVED (preliminary) | ▲ |
| Becker-Ehmck 引用 | PARTIALLY | RESOLVED (混淆解释) | ▲ |
| 模板合规 | RESOLVED (CoRL PMLR) | **NEW CRITICAL** (仍是 CoRL) | ▼▼ |
| Impact Statement | — | **NEW CRITICAL** (ICML 要求) | ▼▼ |
| IQM 数据完整性 | — | **NEW CRITICAL** (n=5 报 n=4 值) | ▼ |
| Seed 叙述一致性 | — | **NEW WARNING** | ▼ |

**核心判断**：

Venue 切换是 Round 4 最重要的变化。Round 3 的两个核心障碍（CoRL venue fit + deployment-oriented 社区的贡献期望）在 ICML 语境下大幅缓解——ICML RL track 接受 systematic diagnostic/negative results，factorial design + LOEO 验证的方法论水平匹配 ICML 标准。Round 3 报告本身也预测了"如果提交到 ICML：Borderline Accept (6/10)"。

新发现的格式问题（模板、Impact Statement）是 desk reject 风险但容易修复；IQM 错误虽不影响核心结论但损害可信度。

**如果格式问题和 IQM 修复后**：评分可上调至 Borderline Accept (6.5/10)。

**综合维度评分**（Director 综合两位 Reviewer）：

| 维度 | 评分 | 理由 |
|------|------|------|
| Originality | 3.5/5 | CIVO 现象新颖，gradient ≠ causal importance 有洞见，方法论框架标准 |
| Soundness | 3/5 | Factorial design 严谨，LOEO 有力，但 IQM 错误 + gradient diversity 无支撑损害可信度 |
| Clarity | 3/5 | 结构清晰，但模板错误 + 缺 Impact Statement + seed 叙述不一致 |
| Significance | 2.5/5 | 四级干预有系统贡献，ICML 对 negative results 更宽容，但 actionable output 有限 |
| Relevance (ICML) | 4/5 | World-model RL + temporal abstraction 是 ICML RL track 核心话题 |
| Limitations | 4/5 | 诚实全面 |

---

## Detailed Comments（逐节）

### Abstract
- 约 150 词，长度合理
- "isolate" 在 factorial ablation 语境中可接受（R2 判断）
- 统计数据密度仍偏高（6+ 数字指标），建议精简

### Introduction
- Robotics framing 保留（从 CoRL 延续），在 ICML 中不加分也不减分
- Contribution 列表 4 项清晰，detector 已降级为 "preliminary"

### Experimental Setup (Section 3)
- methodology.tex:32 "Key configurations use 4 seeds" 与实际 n=5 不一致——**必须修复**
- Factorial design 展示专业，四因素清晰

### Results (Section 4)
- **IQM 175.2 是 n=4 值，n=5 应为 148.8——必须修复**
- Figure 2 caption 提到 "seed 4" 但未提及 seed 5
- "gradient diversity" (results.tex:166) 无 Appendix 支撑——建议弱化
- exp_045 self-recovery 数据有效回应了步数不对等问题
- "establish a causal chain" (results.tex:4) 建议改为 "trace a pathway"

### Discussion (Section 5)
- "hypothesized structural factor" 措辞准确
- exp_045 training horizon 讨论充分

### Conclusion (Section 6)
- conclusion.tex:10 "4 seeds" 与 n=5 不一致——**必须修复**
- Limitations paragraph 诚实全面

### Format Issues（Desk Reject 风险）
- **模板**: main.tex:5 仍为 `\usepackage{corl_2026}` → 需切换 icml2026.sty
- **Impact Statement**: 缺失 → 需在 References 前添加
- **Keywords**: `\keywords{}` 为 CoRL 特有，ICML 模板需处理
- 切换模板后需重新确认页数限制

---

## Issue Tracker Summary (Round 4)

### 本轮新解决 (5)
| Issue | 状态 |
|-------|------|
| R1-N3 CoRL venue fit | RESOLVED (venue → ICML) |
| R1-W2 步数不对等 | RESOLVED (exp_045 data) |
| R2-W1 TAWM 无实证 | RESOLVED (hypothesized) |
| R3-N-new-1 Detector 样本量 | RESOLVED (preliminary) |
| R2-W4 Becker-Ehmck | RESOLVED (混淆解释) |

### 本轮新发现 (5)
| Issue | 严重性 |
|-------|--------|
| N-R4-1 模板 corl_2026 | CRITICAL |
| N-R4-2 Impact Statement 缺失 | CRITICAL |
| N-R4-3 IQM 计算错误 | CRITICAL |
| N-R4-4 Seed 数量不一致 | WARNING |
| N-R4-5 "causal chain" 措辞 | INFO |

### 遗留未解决 (4)
| Issue | 严重性 | 状态 |
|-------|--------|------|
| R2-N3 Actionable 贡献弱 | WARNING (降级) | in_progress |
| R3-N-new-2 gradient diversity | WARNING | in_progress |
| R3-N-new-3 Baseline eval 缺失 | WARNING | open |
| N-R4-5 "causal chain" | INFO | open |

### 全局统计
- 总 issues: 26
- Resolved: 18
- In Progress: 2
- Open: 6