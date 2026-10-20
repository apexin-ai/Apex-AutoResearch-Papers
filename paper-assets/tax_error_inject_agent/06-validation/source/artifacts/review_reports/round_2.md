---
round: 2
overall_score: borderline
timestamp: 2026-05-15T11:49:09.295744+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 2

**论文**: "When Does Unpaired Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning"
**目标 Venue**: Insights from Negative Results in NLP @ EMNLP 2026 (Workshop short paper)
**审稿模式**: 2 Reviewer 圆桌，独立审稿 + 交叉回应，1 轮收敛
**收敛状态**: 所有关键问题达成共识，无未解决 [REBUT]

---

## Summary

本文测试 unpaired taxonomy-guided error injection（TaxEI）从 tool-use（PALADIN）向 embodied planning（ALFWorld）的迁移。在 Qwen3-8B 上对比 Vanilla/TaxEI/Random 三条件（3 seeds），发现 TaxEI 无统计显著改善（−8.6pp, p=0.054）。论文诚实地将负面结果归因于两个竞争假说（task structure 差异 vs 缺少 recovery pairing），并报告 dose-dependent dual regime 和 per-operator local/global split（exploratory）。

**Round 1 → Round 2 核心变化**：Recovery-pairing confound 贯穿全文（Title 加 "Unpaired"）、PALADIN +57pp 拆分三组件归因、多 seed dose-response 数据补充（25%/50% 各 3 seeds）、variance gradient 降级为 dual regime 观察、AgentDebug 讨论扩展、统计措辞严谨化。

---

## Strengths

1. **Recovery-pairing confound 处理出色** [R1, R2 共识]：从 Title 到 Conclusion 一致地将两个竞争假说并列呈现。PALADIN 首次提及即拆分三组件（taxonomy injection + recovery pairing + retrieval）。这是 Round 1 最严重问题的完整解决。

2. **多 seed dose-response 数据大幅提升可信度** [R1, R2 共识]：25%/50% 从单 seed 扩展到 3 seeds，揭示确定性降级（25%, SD=1.2pp）vs 混沌行为（50%, SD≈12pp）的 dual regime。这个发现在 error-augmented agent training 中此前未被文档化，是论文最有价值的独立贡献。

3. **Exploratory 标注诚实系统** [R1]：per-operator 分析全程标注 "exploratory, N=11–12"，exact task count 报告（7/11 vs 6/11 等），透明度是 Negative Results 论文的加分项。

4. **Related Work 改进显著** [R1, R2 共识]：AgentDebug 对比（taxonomy 差异 + cascading 重叠）、Reflexion 引用（inference-time vs training-time）、ALFWorld training-time 空白的明确声明。

5. **实验设计合理** [R2]：fixed-size dose-response ablation 有效控制数据量混淆；统计措辞全文严谨一致。

6. **Venue 契合度高** [R1, R2 共识]：systematically 记录 cross-domain transfer 失败，对 agent training community 有实际指导价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] Conclusion 4-point checklist framing 过强** [R1 SF-R2-1 + R2 N1 | 双方最强共识]
- 4 条 criteria 的证据基础系统性不足：
  - Criterion (1) "discrete/observable errors"：基于 Appendix Table 3 的 a priori structural analysis，非从实验数据 derived
  - Criterion (2) "local recovery"：exploratory, N=11–12, 单 seed, ±1 task ≈ ±8–9pp
  - Criterion (3) "immediate feedback"：**与论文自身矛盾**——Discussion Limitations 承认 ALFWorld "partially resembles tool-use error observability"（text-based interface 提供 "Nothing happens" 反馈）。如果 ALFWorld 已有 partial immediate feedback 且 injection 仍失败，此 criterion 的因果推理不成立
  - Criterion (4) "recovery pairing"：是被论文明确标记的 confound（"We cannot distinguish between these two hypotheses"），不是 tested condition。将 confound 写入 prescriptive checklist 逻辑不一致
- **必须修改**：改为 "We hypothesize four properties that may moderate error injection effectiveness—all require independent validation, including on ALFWorld itself"；Title 从 "Boundary Conditions" 改为 "Hypotheses" 或 "Observations"

**[MF-2] Table 2 Δ 列 10% single-seed 行误导** [R2 N2 | R1 交叉回应 AGREE]
- 10% 行用单 seed (seed=42) 结果对比 3-seed vanilla mean (65.3±3.3)：
  - TaxEI 10% = 61.7% = Vanilla seed=42 = 61.7% → 同 seed Δ = **0.0pp**，表中报告 **−3.6pp**
  - Random 10% = 68.1%，Vanilla seed=42 = 61.7% → 同 seed Δ = **+6.4pp**，表中报告 **+2.8pp**
- 虚假的 −3.6pp "轻微降级" 扭曲 dose-response 叙事的起点——读者会误解为 "从 10% 就开始有 treatment effect"，实际同 seed 完全无差异
- **必须修改**：10% 行 Δ 改为 same-seed delta 或标注 "N/A"，加脚注说明基线选择差异。0 成本修复。

**[MF-3] 页数超限** [R1 MF-R2-1 + R2 W1 | 双方共识]
- R1 估 4.0–4.5 页，R2 详细逐项估算 ~4.7 页，中间值 ~4.3–4.5 页
- Limitations (~150 词) 嵌入 Discussion，ACL 政策：独立 `\section*{Limitations}` 不计入页数（可回收 ~0.2 页）
- 拆出 Limitations 后仍可能偏紧
- **必须修改**：(1) Limitations 独立为 `\section*{Limitations}`；(2) §3.6 Training-Evaluation Paradox (~0.3 页) 浓缩为 1 句移入 Discussion，详细数据移至 Appendix；(3) 编译确认 ≤ 4 页

### Should-Fix

**[SF-1] Recovery evaluation 仅 seed=42，统计不足** [R1 SF-R2-2 + R2 N3 | 双方共识]
- Recovery accuracy 差异仅 1–4pp（TaxEI 59.6%, Vanilla 61.7%, Random 63.8%），远小于已知 seed variance (SD≈12pp)
- 无统计检验，seed=42 恰好是 TaxEI 多个配置中表现最差的 seed
- **但 R1 有效 nuance**：0% detection rate 是 categorical evidence（0/47 tasks, binomial test: p<0.8% if true rate ≥10%），比百分比差异更可靠。建议分开处理：
  - Recovery accuracy 降级为 "preliminary single-seed observation"
  - 0% detection rate 可保留为有效结论，但加单 seed 标注
- **建议**：补充至少 1 个额外 seed 的 recovery 数据更优；否则在正文中分层标注证据强度

**[SF-2] Figure 1 与 Table 2 覆盖不一致** [R1 M-R2-1 + R2 W2 | 双方共识]
- Figure 1 仅 seed=42，呈现近单调递降（seed=42 的 +2.2pp 回升在噪声内）
- Caption 声称 "non-monotonic dose-response with regime bifurcation"——此 pattern 仅在 3-seed 均值中成立（25% mean 47.5 → 50% mean 56.0）
- 视觉印象与 claim 不匹配
- **建议**：Figure 1 更新为 3-seed 散点图/error bar，或至少标注 3-seed 均值参考线

**[SF-3] Title "Boundary Conditions" 措辞偏强** [R1 SF-R2-1 + R2 W3 | 双方共识]
- 单 environment + 单 model + 未测试 recovery pairing → 称 "boundary conditions" 过强
- **建议**：改为 "When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning"
- R1 倾向 "Hypotheses"，R2 同意 "Hypotheses" 或 "Observations"

### Minor

**[M-1]** 0% detection rate 讨论仅一句（§3.4），建议 Discussion 增加 1–2 句呼应：SFT 未 internalize taxonomy labels 的可能机制（labels 仅作 prompt prefix，训练目标是 next-token prediction 而非 classification）[R1 M-R2-2 + R2 AGREE]

**[M-2]** Abstract ~180 words 对 4-page short paper 偏长 [R2]（R1 认为删减可能伤害完整性，建议优先从 §3.6 节省空间而非压 Abstract）

**[M-3]** BibTeX author 字段使用 double-brace `{{Author, I.}}` 格式，可能导致排版异常，建议改为标准 `{Last, First and ...}` [R2]

---

## Reviewer Consensus [AGREE]

以下问题双方完全一致（交叉回应均为 [AGREE]）：
1. Conclusion 4-point checklist framing 过强——需降级为 "hypothesized conditions"
2. Table 2 Δ 列 10% 行误导——同 seed 实际 Δ=0.0pp
3. 页数需压缩——拆 Limitations + 移 §3.6 至 Appendix
4. Recovery evaluation 单 seed 是显著局限
5. Figure 1 应更新为 3-seed 展示
6. Title "Boundary Conditions" 偏强，建议 "Hypotheses"
7. Recovery-pairing confound 的处理出色（Round 1 最严重问题已完整解决）
8. Dose-response dual regime 是论文最有价值的独立贡献
9. Round 1 的 16 个 issues 中 13 个完全解决

## Reviewer Divergence [分歧]

1. **页数预估**：R1 估 4.0–4.5p，R2 估 ~4.7p。**裁定**：差异不影响结论——两者都指向 "需要压缩"。按中间值 4.3–4.5 页准备方案。
2. **0% detection rate 的证据强度**：R1 认为 0% detection 是 categorical evidence 可保留（binomial test p<0.8%），R2 认为应整体降级。**裁定**：R1 的 nuance 有效——0% detection rate 和 recovery accuracy 差异是不同层次的证据，应分开处理。
3. **Criterion (3) "immediate feedback" 矛盾的严重性**：R1 初始列为 Minor，R2 列为 critical-level。**裁定**：R2 论证更有力——这不是措辞不一致而是 undermines checklist 逻辑基础，升级为 Must-Fix（已合并入 MF-1）。
4. **Abstract 压缩**：R2 建议压缩至 ~140 词，R1 认为每句都 carry 信息。**裁定**：优先从 §3.6 节省空间，Abstract 压缩为可选项。

---

## Questions（需作者澄清）

1. Recovery evaluation（§3.4）是否有其他 seed 的数据？如果 TaxEI seed=0 的 recovery 表现与 clean eval 一样出现极端偏移，这将支持 seed-injection interaction 假说。

2. 10% dose-response 未补多 seed 是资源限制还是有意设计？鉴于 25% 确定性降级在 3 seeds 间高度一致（SD=1.2pp），10% 的行为模式值得确认。

3. Discussion 估计 PALADIN recovery pairing 贡献 ~30pp，此数字来源？论文未引用 PALADIN 消融实验。（Round 1 遗留）

4. Conclusion criterion (3) "immediate feedback" — 如何与 Discussion 中 "ALFWorld partially resembles tool-use observability" 的表述兼容？这似乎是自相矛盾。

---

## Missing References

1. **LATS** (Zhou et al., 2024) — Language Agent Tree Search，ALFWorld 上有竞争力结果
2. **FireAct** (Chen et al., 2023) — fine-tuning agents with multiple reasoning traces
3. 无重大遗漏——当前引用覆盖核心相关工作

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置中未设置 `external_review.paperreview_ai.enabled`）。

---

## Round 1 Issue Resolution 摘要

| 状态 | 数量 | 详情 |
|------|------|------|
| ✅ RESOLVED | 13 | R1-N1, R1-N2, R1-N3, R2-N3, R1-W1, R1-W2, R2-W2, R2-W3, R2-W4, R2-W5, R1-W5, R1-M1, R2-M1, RR-1 |
| ⚠️ PARTIALLY | 3 | R2-N1→页数 (升级为 Round 2 MF-3), R2-W1→checklist 措辞 (升级为 Round 2 MF-1), R1-M2→detection rate 讨论 (Round 2 M-1) |
| ❌ UNRESOLVED | 0 | — |

Round 2 新增 8 个 issues：3 Must-Fix (checklist framing, Table 2 Δ 列, 页数) + 3 Should-Fix (recovery eval, Figure 1, Title) + 2 Minor。

---

## Overall Assessment

**评分: Borderline**
**置信度: High (4/5)**

### Reviewer 评分汇总

| 维度 | R1 (修正后) | R2 | 综合 |
|------|------------|-----|------|
| Soundness | 3.0–3.5 | 3.0 | 3.0 |
| Excitement | 3.0–3.5 | 3.5 | 3.25 |
| Overall | 2.75–3.0 | 2.5 | 2.75 |

R1 初始给 3.0，交叉回应后因认可 Table 2 Δ 列问题和 criterion (3) 矛盾，修正为 2.75–3.0。R2 给 2.5，表示如果 checklist framing + Table 2 Δ 列修正后可上调至 3.0。综合 **2.75/5 — Borderline**。

### 评分理由

**为什么 Borderline 而非 Weak Accept**：
- 3 个 Must-Fix 均为实质性问题——checklist 逻辑不自洽（criterion 3 矛盾 + criterion 4 未测试）、Table 2 数据呈现误导、页数超限
- Recovery evaluation 单 seed 削弱了 "taxonomy labels not internalized" 这一关键 mechanistic claim
- 论文核心贡献受 recovery-pairing confound 限制，归因仍不确定

**为什么 Borderline 而非 Weak Reject**：
- Round 1 → Round 2 修订质量高——16 个 issues 中 13 个完全解决，不是敷衍应付
- Dose-response dual regime（25% deterministic vs 50% chaotic）是原创且 well-supported 的发现（3-seed confirmed）
- Recovery-pairing confound 处理出色——诚实度在 Negative Results 论文中加分
- 3 个 Must-Fix 均为低成本可修修订（措辞调整 + Table Δ 修正 + 格式重排），不涉及补充实验
- 对 Insights from Negative Results workshop 高度契合

### 修改后可接收的条件

1. **Checklist 降级为 "hypothesized conditions"** + 解决 criterion (3) 矛盾（或移除该 criterion）
2. **Table 2 Δ 列修正**：10% 行改为 same-seed delta 或 N/A
3. **页数合规**：Limitations 独立 + §3.6 移至 Appendix + 编译确认 ≤ 4 页
4. **Recovery eval 标注**：recovery accuracy 标注 "single-seed, preliminary"；0% detection rate 可保留

修改难度低，不涉及补充实验。预计 1 轮小修即可达 Weak Accept。

---

## Detailed Comments

### Title
- "Boundary Conditions" → "Hypotheses"（双方共识）
- "Unpaired" 保留（Round 1 修改，处理得当）

### Abstract
- Recovery-pairing confound 披露充分 ✓
- PALADIN 拆分三组件 ✓
- ~180 词偏长但可接受（优先从正文节省空间）

### §1 Introduction
- 两个竞争假说并列清晰 ✓
- Contribution (1) "Negative transfer with competing hypotheses" 定位准确 ✓
- Contribution (2) "Dose-dependent dual regime" 有 3-seed 支撑 ✓

### §2 Method
- Error taxonomy 设计合理 ✓
- "Error-recovery pairs are not explicitly paired" 放在方法节正确位置 ✓
- Fixed-size dose-response 设计有效控制混淆 ✓

### §3 Experiments
- Table 1: caption 注释 2.1× 差异并指向 dose-response ✓
- Table 2: **10% Δ 列需修正**（MF-2）
- §3.4 Recovery: **单 seed + 无统计检验是最大剩余弱点**（SF-1）
- §3.5 Per-operator: exact task count + exploratory 标注 ✓
- §3.6 Training-eval paradox: 双解释并列 ✓，但应移至 Appendix 节省空间（MF-3）

### §4 Discussion
- Structural hypothesis + Recovery-pairing confound 分段清晰 ✓
- Limitations 内容充分但应独立为 `\section*{Limitations}` ✓
- **缺少 0% detection rate 的机制讨论**（M-1）

### §5 Related Work
- AgentDebug 对比充分 ✓
- Reflexion + inference-time vs training-time 对比 ✓
- 可补充 LATS、FireAct 但非必须

### §6 Conclusion
- **4-point checklist 需降级为 "hypothesized"**（MF-1）
- **Criterion (3) 需解决矛盾或移除**（MF-1）
- Future work 方向清晰（recovery-paired injection → WebShop → seed interaction）✓

### Appendix
- Version Discrepancy 说明充分 ✓
- Per-task cross-analysis + Training dynamics 支撑主文 ✓
- 建议接收 §3.6 Training-Eval Paradox 的详细内容