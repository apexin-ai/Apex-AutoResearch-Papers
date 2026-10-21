---
round: 5
review_mode: continue
overall_score: weak accept
timestamp: 2026-05-22T08:21:00.556169+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 审稿报告 — importance_margin_vla_compress

**Venue**: CoRL 2026 | **Deadline**: 2026-05-29 | **审稿模式**: Continue（基于 Round 4）
**Reviewer 1**: 方法严谨性 + 实验验证 | **Reviewer 2**: 新颖性 + 完整性 + venue fit
**交叉分享**: 完成（R1↔R2 逐条 AGREE/REBUT）| **收敛**: 1 轮达成

---

## Summary

本轮为 Round 4（Weak Reject）后的修订评估。论文对 Round 4 提出的 15 个 issues（4 critical + 11 should-fix/info）进行了全面回应，两位 Reviewer 一致确认**全部 15 个 issues 已 RESOLVED**。核心修改包括：(1) 因果语言系统性降级（determines→associated, predicts→correlates, falsifies→demonstrates），(2) SmolVLA 官方 checkpoint 多 k 值验证确认 cliff 为架构属性，(3) 正文从 ~13 页压缩至 8 页，(4) 新增 Section 4.7 cross-suite generalization 与 hypergeometric cliff model，(5) Appendix N confound analysis。两位 Reviewer 均上调评分一档。新发现 5 个 warning 级问题和 1 个 critical 级视觉问题（Figure 4 placeholder），均为 camera-ready 可修复项。

---

## Strengths

**S1. 系统性因果语言降级（R1+R2 共识）**
论文对 claim 强度进行了全文一致的校准："determines"→"strongly associated with"，"predicts"→"correlates with"，"falsifies"→"demonstrates"，"framework"→"diagnostic protocol"。Grep 确认无残留。降级幅度恰当——核心发现仍然清晰，但不再超出数据支撑。这是本轮最重要的改进。

**S2. 官方 checkpoint 多 k 值验证（R1+R2 共识）**
SmolVLA 官方 HF checkpoint（57.2% SR baseline）在 k∈{0.95, 0.9, 0.5} 下均为 0% SR，dual evaluation protocol（59.2% / 57.2%）交叉验证。VTR M=32 恢复至 60.1±1.3%。彻底解决了 Round 4 "cliff 可能是 undertrained checkpoint artifact" 的核心质疑。

**S3. Limitations 的诚实度（R2 特别指出）**
Section 5 Limitations 明确列出：simulation-only、N=3 connector 类型、CV 仅 3 模型 × 2 k 值、π₀ offline-only、hypergeometric model 不解释 V-shape recovery。R2 评价："我审过的论文中最诚实的 Limitations 之一。"

**S4. 新增分析深度（R1+R2 共识）**
Section 4.7 cross-suite generalization（Object/Spatial/Goal）+ hypergeometric cliff model H(N=768, C=91, T=6) 将定性 cliff 观察提升为定量假说。Appendix N confound analysis 是实质性的方法论贡献。

**S5. 正文压缩与结构重组（R1+R2 共识）**
从 ~13 页压缩至 8 页正文，Discussion 从 5 subsection 压缩为 2 段，大量 mechanistic analysis 移入 Appendix。符合 CoRL 8 页限制。

---

## Weaknesses

### Camera-Ready Must-Fix

**W-V1 [critical] Figure 4 占位符未替换（视觉审查）**
Page 17 的 Figure 4 显示 "[Placeholder: token importance heatmap]" 灰底文字框，未替换为实际图片。已提交论文中出现 placeholder 是严重疏忽。必须在提交前替换为实际 token importance heatmap 可视化。

### Camera-Ready Should-Fix

**W-N1 [warning] π₀.5 V-shape 非单调 recovery 与 hypergeometric model 解释力缺口（R1 提出, R2 强烈 AGREE）**
π₀.5 在 LIBERO-Object 上：k=0.95 (69.4%) → k=0.85 (5.0%) → k=0.7 (77.2%)，72pp swing。Hypergeometric model 预测单调 collapse probability，从逻辑上无法解释 k=0.7 处的恢复。Section 5 一句带过 "does not explain V-shape recovery at k≤0.7" 不够充分。R2 指出这直接削弱了 CV diagnostic 的实用性——最优 k 值不是从 CV 单调推导的。
- **建议**: Section 4.7 增加模型适用边界说明；Section 4.4 或 Appendix 讨论 V-shape 可能机制。

**W-N2 [warning] Hypergeometric model C=91 参数来源不明（R1+R2 独立收敛）**
C=91（critical tokens）是 hypergeometric model 的关键自由参数，但正文和 Appendix C.8 均未说明其确定方法。如果 C 从 SR 曲线反向拟合，模型退化为 curve fitting，无独立预测力；如果从 attention heatmap 独立测量，模型有真正的预测价值。两位 Reviewer 独立收敛于此问题。
- **建议**: Appendix C.8 明确 C 的确定方法。

**W-N3 [warning] SmolVLA baseline 数字不一致（R1 提出, R2 AGREE）**
Section 4.2: "57.2% SR"，Table 2: "59.2% baseline"。来自不同评估协议但首次提及时未说明。
- **建议**: Section 4.2 首次提及时写 "57.2%–59.2% across two evaluation protocols (Appendix B)"。

**W-N4 [warning] Discussion 过度压缩（R1 提出, R2 AGREE）**
旧版 ~3 页的 mechanistic insights（connector→token independence 系统性分析）压缩为 2 段 ~10 行。内容移入 Appendix J-K 但正文无显式指引。
- **建议**: Discussion 增加一句 "For extended mechanistic analysis, see Appendices J–K"。

**W-N5 [warning] "All tokens carry equal weight" 措辞不精确（R2 提出, R1 部分 REBUT 但 AGREE on precision）**
Section 4.4 中 L2 norm 均匀被等同于 "equal weight"，但 L2 norm 均匀不等于 task-relevant information 均匀。R1 指出 R2 误引了原文语境，但同意措辞应更精确。
- **建议**: 改为 "near-uniform L2 norms (CV=0.038) suggest no token subset carries disproportionate information"。

---

## Questions

1. Hypergeometric model 的 C 参数是从 collapse curve 反向拟合的，还是从 token importance heatmap（Figure 4）独立测量的？如果是后者，阈值如何选择？
2. π₀.5 在 k=0.7 恢复到 77.2% 的机制假说是什么？是否可能与 position re-indexing 或 computation regime transition 有关？
3. VTR 的 M=32 vs M=128 在 official checkpoint 上的 SR 差异是多少？（当前数据仅报告了 M=32 的 60.1%）

---

## Missing References

Round 5 无新增缺失引用。Round 4 建议的引用已基本覆盖（~46 citations）。R1+R2 共识：质量和相关性到位。

---

## External Review

未启用。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（2026-05-22 08:06→08:09）。

| 严重度 | 位置 | 发现 |
|--------|------|------|
| **Critical** | p17 | **Figure 4 为占位符**——灰底文字框 "[Placeholder: token importance heatmap]"，未替换为实际图片 |
| Warning | pp3-4 | 连续 2 页纯文本（Related Work + Methods 开头），无 display item |
| Warning | pp1-9 | 正文仅 4 个 display items（2 figures + 2 tables），对实证论文偏少 |
| Warning | p6 | 整页纯文本，夹在 Table 1 (p5) 和 Table 2 (p7) 之间 |
| Warning | p27 | 末页底部约 35% 空白 |
| Info | p8 | Figure 2 axis label 和 legend 字号偏小（~60-65% 正文字号） |
| Info | p5 | Table 1 格式良好——booktabs 风格、加粗、CI 标注清晰（亮点）|
| Info | p2 | Figure 1 架构图清晰专业，颜色区分度好 |
| Info | pp13-15 | 附录表格密度高，per-task breakdown 完整 |
| Info | p23 | Figure 7 双面板图配色方案与 Figure 2 一致 |
| Info | pp9-11 | References 无未解析引用，格式统一 |

---

## Overall Assessment

### 评分汇总

| Reviewer | Round 4 | Round 5 | 变化 |
|----------|---------|---------|------|
| R1 | Borderline (leaning weak reject) | **Weak Accept** | +1 档 |
| R2 | Weak Reject (borderline) | **Borderline (leaning weak accept)** | +1 档 |

### 共识与分歧

**完全共识（无分歧）：**
- Round 4 全部 15 个 issues 已 RESOLVED
- 因果语言降级彻底且一致
- 新增内容（cross-suite、hypergeometric model、official checkpoint）增强了贡献
- Limitations 诚实度高于平均水平
- 论文展现了出色的迭代改进能力
- W-N1 到 W-N4 均为 camera-ready 可修复项，不影响接收决定

**半档评分差异的来源（已解释，非未解决分歧）：**
1. **Venue fit**: R2 对 simulation-only 在 CoRL 的适配度权重更高；R1 认为架构理解类研究合理使用仿真
2. **N=3 limitation**: R2 认为 claim 降级是必要非充分条件；R1 认为降级已充分弥补
3. **VTR 贡献评估**: 一致认为 incremental 但定位诚实；对评分影响的权重略有差异

### Camera-Ready 条件

如果接收，以下为 camera-ready 必须完成的修改：
1. ★ 替换 Figure 4 placeholder 为实际 token importance heatmap
2. Section 4.7 增加 hypergeometric model 适用边界说明
3. Appendix C.8 明确 C 参数确定方法
4. Section 4.2 统一 SmolVLA baseline 数字表述
5. Discussion 增加 Appendix J-K 指引
6. Section 4.4 精确化 "equal weight" 措辞

### 综合评分: **Weak Accept**

**Confidence**: High

**理由**: 两位 Reviewer 均从 reject 区间上调至 accept 边界。Round 4 的 4 个 critical issues 全部彻底修复，claim 强度与数据支撑现已匹配。新增实证（cross-suite、official checkpoint）和分析（hypergeometric model、confound analysis）增加了实质价值。剩余弱点（N=3 connector、sim-only、hypergeometric model 局限）是 inherent scope limitations，非方法论缺陷，且已在 Limitations 中诚实承认。论文对 CoRL 社区的核心价值——系统性揭示 VLA connector 与 pruning 行为的关联，并提供 CV 零成本诊断指标——清晰、有证据支撑、且被适度表述。Figure 4 placeholder 是提交前必须修复的严重疏忽，但不影响学术评价。

---

## Detailed Comments

### 对作者的建议（按优先级排序）

1. **Figure 4 placeholder**（提交前必修）: 当前为灰底文字框，需替换为实际 heatmap。如果数据已有（D141 visualization），应立即集成。

2. **Hypergeometric model 边界**（camera-ready）: Section 4.7 在报告 RMSE=0.025 后增加："The model captures onset sharpness at high retention but does not generalize to moderate retention where compensatory mechanisms may emerge (see §5 Limitations)."

3. **C 参数透明化**（camera-ready）: Appendix C.8 增加一段说明 C 的来源——是从 Figure 4 heatmap 用某个 importance threshold 独立计算的，还是从 SR 数据最小化 RMSE 反向拟合的。如果是前者，说明 threshold 选择；如果是后者，承认这是 curve fitting。

4. **Baseline 数字统一**（camera-ready）: Section 4.2 首次提及 SmolVLA 时改为 "57.2%–59.2% SR across two evaluation protocols (Appendix B)"，避免读者在 Section 4.2 和 Table 2 之间产生困惑。

5. **Discussion 指引**（camera-ready）: 在 Section 5 第一段末尾增加 "Full mechanistic analysis of how connector architecture creates the observed token independence structure appears in Appendices J–K."

6. **"Equal weight" 精确化**（camera-ready）: Section 4.4 的 "all tokens carry equal weight" 改为 "near-uniform L2 norms (CV = 0.038) suggest that no token subset carries disproportionate information, so random removal preserves spatial coverage."

### 给 AC 的建议

本文在 5 轮审稿中展现了持续的、高质量的改进。如果需要在 borderline 论文中取舍：

**优势**:
- 跨架构覆盖广度（7 models, 3 connectors, 3 suites）在 VLA token compression 领域无出其右
- Negative results（linear projection 不可 prune、low-CV models 的 uniform criticality）有高实用价值
- Limitations 的诚实度和 confound transparency 高于平均水平
- CV 作为零成本诊断指标有明确的实践路径

**风险**:
- N=3 connector 类型是基本瓶颈——增加 Perceiver-based VLA（如 RoboFlamingo）将显著增强说服力
- Simulation-only 在 CoRL 的 venue fit 有短板，但论文定位为 diagnostic analysis 而非 system deployment
- Hypergeometric model 的预测力未经独立验证（C 参数来源不明）