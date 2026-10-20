---
round: 5
review_mode: continue
overall_score: borderline accept
timestamp: 2026-05-24T15:16:11.180727+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: ICML 2026
**审稿日期**: 2026-05-24
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 数据完整性 | R2: Venue 合规 + 写作质量 + 贡献度）
**轮次**: Round 5 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
**上轮评分**: Round 4 Weak Accept (6/10)

---

## Summary

Round 4 提出的 8 个 open/in_progress issues（含 3 个 CRITICAL）在 Round 5 中得到全面回应：模板切换至 icml2026.sty、Broader Impact Statement 已添加（~100 词，内容充实）、IQM 从 175.2 更正为 148.8（经两位 Reviewer 独立计算验证）、seed 数量叙述统一为 "4--5 seeds"、"gradient diversity" 替换为 "mechanisms that remain to be characterized"、"causal chain" 改为 "trace a predictive pathway"。7/8 issues RESOLVED，1 个（baseline vals）降级为 info。

新发现 1 个 info 级问题：PDF page 1 脚注显示 "AUTHORERR: Missing \icmlcorrespondingauthor"。

---

## Strengths

1. **Factorial design 系统严谨**（持续优势，5 轮共识）：43 配置 × 4-5 seeds × 5 环境
2. **LOEO 交叉验证统计可信度高**：AUROC=0.988 (LOEO)，全文数字一致
3. **四级干预层级分析**：gradient/output/representation/architecture，方法论示范价值
4. **数据完整性恢复**（Round 5 新增）：IQM 148.8 经独立验证、seed 叙述全文一致、因果语言统一
5. **ICML 格式合规**（Round 5 新增）：icml2026.sty、Broader Impact Statement、double-blind
6. **方法论措辞到位**："strongest predictor"、"hypothesized structural factor"、"trace a predictive pathway"、"mechanisms that remain to be characterized"——每处声明的强度与证据级别匹配
7. **Dual-critic convergence insight**：ρ > 0.999 揭示 imagination-based 训练中 pessimism 结构性失效
8. **exp_045 self-recovery 数据**：302K 步后完全恢复，回应了步数不对等问题

---

## Weaknesses（按严重性排序）

### Warning

**W-W1. Contribution scope 有限 [R2 主要 concern，R1 部分同意]**
- CIVO 仅在 DreamerV3 + locomotion 中确认，manipulation 中不出现
- 核心 actionable takeaway 仍是 "不要用 trained dt-embedding"
- 与 Henderson et al. (2018) 相比 scope 窄一个量级
- 但在 ICML 语境下，systematic diagnostic paper 的贡献模式可接受（R1/R2 共识）

**W-W2. 正文仅 6 页（ICML 允许 8 页）[视觉审查发现]**
- 主体有 2 页富余空间，display item 密度 0.67/页偏低
- Appendix 中的 Figure 6（CIVO 机制图）和 Figure 5（dt 退化趋势）可提升到正文增强视觉节奏
- 前 3 页无任何 display item，审稿人第一印象缺乏视觉锚定

### Info

**W-I1. PDF 显示 AUTHORERR [2/2 共识]**
Page 1 脚注 "AUTHORERR: Missing \icmlcorrespondingauthor"。交叉回应后共识为 info 级——可能是 icml2026.sty 匿名模式行为，但可见文字影响专业印象。建议提交前添加 `\icmlcorrespondingauthor{}` 修复。

**W-I2. StackCube/PegInsertion baseline eval 未测量 [降级为 info]**
Table 1 脚注已补充 Walker (915.7) 和 Cheetah (~409) 的 baseline。StackCube/PegInsertion 标注 "not separately measured"。因这些环境的结论是 CIVO 不出现，baseline 对判断无影响。两位 Reviewer 一致同意不再追踪。

**W-I3. Figure 4 红绿色块对色盲不友好 [视觉审查]**
建议改用 blue/orange 或添加纹理/标签区分。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识度 |
|------|----|----|--------|
| N-R4-1 模板 | RESOLVED | RESOLVED | **2/2 一致** |
| N-R4-2 Impact Statement | RESOLVED | RESOLVED | **2/2 一致** |
| N-R4-3 IQM 148.8 | RESOLVED (独立验证) | RESOLVED (独立验证) | **2/2 一致** |
| R3-N-new-2 gradient diversity | RESOLVED | RESOLVED | **2/2 一致** |
| N-R4-4 seed 数量 | RESOLVED | RESOLVED | **2/2 一致** |
| N-R4-5 "causal chain" | RESOLVED | RESOLVED | **2/2 一致** |
| R3-N-new-3 baseline vals | PARTIAL→info | PARTIAL→minor | **2/2 一致（降级）** |
| R2-N3 actionable | RESOLVED (ICML) | ACKNOWLEDGED | **实质一致** |
| AUTHORERR | info | info (交叉后) | **2/2 一致** |
| Soundness | 3/4 | 3/4 | **2/2 一致** |
| Presentation | 3/4 | 3/4 | **2/2 一致** |
| Originality | 3/4 | 3/4 | **2/2 一致** |
| Significance | **3/4 Good** | **2/4 Fair** | **分歧** |
| Overall | **5/6 Accept** | **4+/6 Weak Accept** | **分歧** |

---

## Reviewer Divergence

**Significance/Contribution（R1: 3/4 Good vs R2: 2/4 Fair）——唯一实质分歧**

R1 主张 Good 的理由：
- DreamerV3 是 imagination-based RL 最广泛使用的 baseline，failure mode 有直接实践价值
- Dual-critic convergence (ρ>0.999) 是 architecture-general insight
- 论文提供 3 层理解（为什么失败 + 为什么标准修复不 work + 什么条件下失败），超越简单 "don't do X"

R2 主张 Fair 的理由：
- CIVO 仅在 DreamerV3 + locomotion 中确认，受影响场景窄
- dt-conditioning in imagination-based RL 非主流方向（TAWM 用 MPC，Dreamer 用 fixed dt=1）
- 与 Henderson et al. 2018 相比 scope 窄一个量级

**Director 判断**：R1 的 Good 强调 mechanistic depth，R2 的 Fair 强调 scope breadth。两者各有道理。论文的 systematic rigor 有方法论示范价值（四级干预分析可被未来 RL 诊断研究复用），但受影响的研究者基数确实有限。综合约 **2.5/4 (Fair+)**。

交叉回应后 R2 微调至 4+ (Weak Accept, leaning Accept)，表示"如果 AC 倾向 Accept，不会反对"。分歧为 judgment call 而非技术分歧。

---

## Questions for Authors

1. PDF page 1 的 AUTHORERR 是否可通过添加 `\icmlcorrespondingauthor{Anonymous Author}{anon@anon.edu}` 消除？建议提交前验证。
2. 正文仅 6 页——是否考虑将 Figure 6（CIVO 机制图）和 Algorithm 1（Online Detector）从 Appendix 提升到正文？前 3 页无 display item 影响第一印象。
3. Figure 4 的红绿色块是否可改为 blue/orange 以提升色盲友好性？

---

## Missing References

无新增。Becker-Ehmck 2023 已在 Round 4 确认为 Benechehab et al. 2023 的混淆，后者已引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 critical, 3 warnings, 7 info）。

**主要发现**：
1. **[critical] AUTHORERR 渲染在 PDF page 1 脚注**：LaTeX 错误残留直接可见，影响专业性。
2. **[warning] 前 3 页无 display item**：主体前 50% 为连续纯文本，审稿人缺乏视觉锚定。
3. **[warning] 正文仅 6 页（ICML 允许 8 页）**：display item 密度 0.67/页偏低。Figure 6（CIVO 机制图）和 Figure 5 可提升到正文。
4. **[warning] Page 20 大面积空白**：Table 4-5 之间约 40% 空白。
5. **[info] Figure 4 红绿色块对色盲不友好**。
6. **[info] Table 3 字号偏小（~6-7pt）**。
7. **[info] Figure 1/2 图例字号偏小，建议增加 line style 辅助区分**。
8. **[info] Figure 6 是全文最清晰概念图，强烈建议提升到正文**。
9. **[info] Table 1 booktabs 格式规范，CIVO 标注到位**。

---

## Overall Assessment

**评分: Borderline Accept (7/10)**
**置信度: High (4/5)**

**与 Round 4 (Weak Accept, 6/10) 的变化**：

| 维度 | Round 4 | Round 5 | 变化 |
|------|---------|---------|------|
| 模板 | CRITICAL (corl_2026) | RESOLVED (icml2026) | ▲▲ |
| Impact Statement | CRITICAL (缺失) | RESOLVED (充实) | ▲▲ |
| IQM 数据完整性 | CRITICAL (175.2 错误) | RESOLVED (148.8 验证) | ▲▲ |
| gradient diversity | WARNING (复发×2) | RESOLVED (终于修复) | ▲ |
| Seed 叙述 | WARNING | RESOLVED | ▲ |
| "causal chain" | INFO | RESOLVED | ▲ |
| Baseline vals | WARNING | info (降级) | ▲ |
| AUTHORERR | — | NEW info | ▼ (minor) |

**核心判断**：

Round 4 报告预测"如果格式问题和 IQM 修复后：评分可上调至 Borderline Accept (6.5/10)"。Round 5 不仅修复了这些问题，还解决了复发两轮的 "gradient diversity" 术语、统一了 seed 叙述、修正了因果语言。论文现已达到 ICML 投稿的技术标准。

两位 Reviewer 在 Soundness/Presentation/Originality 上完全一致（均 Good 3/4），分歧仅在 Significance（3/4 vs 2/4），导致 Overall 差 1 档（Accept 5/6 vs Weak Accept 4+/6）。这是 borderline 论文的典型 reviewer 间 calibration 差异，不是技术分歧。

**评分上调至 7/10 的理由**：
1. 所有 CRITICAL 和 WARNING issues 已修复或降级
2. 数据完整性经独立验证恢复
3. ICML 格式完全合规
4. 方法论措辞与证据级别精确匹配
5. 残留问题均为 info 级（AUTHORERR、baseline vals、色盲友好性）

**未达 8/10 的理由**：
1. Contribution scope 限于 DreamerV3 + locomotion（R2 的核心 concern）
2. 正文仅 6 页，display item 密度偏低，前 3 页无视觉锚点
3. AUTHORERR 影响专业印象（虽为 info 级）

**综合维度评分**（Director 综合两位 Reviewer）：

| 维度 | 评分 | Round 4 | 变化 | 理由 |
|------|------|---------|------|------|
| Originality | 3.5/5 | 3.5/5 | — | CIVO 新颖，方法论框架标准 |
| Soundness | 3.5/5 | 3/5 | ▲ | IQM 修正，数据完整性恢复，因果语言一致 |
| Clarity | 3.5/5 | 3/5 | ▲ | ICML 格式正确，Impact Statement 到位，措辞精确 |
| Significance | 2.5/5 | 2.5/5 | — | 判断不变：ICML 宽容 diagnostic papers，但 scope 限制 |
| Relevance (ICML) | 4/5 | 4/5 | — | World-model RL 是 ICML RL track 核心话题 |

---

## Detailed Comments（逐节）

### Abstract
- ~150 词，数字指标从 6+ 降至 ~4，信息密度改善
- "identify" 和 "hypothesized structural factor" 措辞准确

### Introduction
- "isolate" 在 factorial ablation 语境下是标准方法论术语（2/2 共识）
- Contribution 列表 4 项清晰，detector 为 "preliminary"
- Robotics framing 作为 motivation 合理

### Experimental Setup (Section 3)
- "4--5 seeds (Walker Walk uses 5 seeds)" ✓ 全文一致
- Factorial design 四因素清晰

### Results (Section 4)
- IQM 148.8, n=5 ✓ 独立验证
- "trace a predictive pathway" ✓
- "mechanisms that remain to be characterized" ✓
- LOEO AUROC=0.988 全文一致
- 27/30, AUROC=0.957 全文一致

### Discussion (Section 5)
- "hypothesized structural factor" ✓
- exp_045 training horizon 数据充分

### Conclusion (Section 6)
- "4--5 seeds per configuration" ✓
- Limitations 诚实全面

### Broader Impact Statement
- 内容充实：detector 局限、simulation-only 声明
- 非 boilerplate，非过度渲染
- 位置正确（References 前）

### Format
- icml2026.sty ✓, \icmltitlerunning ✓, \icmlkeywords ✓, \bibliographystyle{icml2026} ✓
- Double-blind ✓
- 正文 6 页（ICML 允许 8 页）——有空间提升关键 Appendix 图表
- AUTHORERR 需修复

---

## Issue Tracker Summary (Round 5)

### 本轮解决 (7)
| Issue | 轮次历史 | 状态 |
|-------|---------|------|
| N-R4-1 模板 corl→icml | R4 CRITICAL → R5 RESOLVED | ✅ |
| N-R4-2 Impact Statement | R4 CRITICAL → R5 RESOLVED | ✅ |
| N-R4-3 IQM 175.2→148.8 | R4 CRITICAL → R5 RESOLVED | ✅ |
| R3-N-new-2 gradient diversity | R3→R4 复发×2 → R5 RESOLVED | ✅ |
| N-R4-4 Seed 叙述 | R4 WARNING → R5 RESOLVED | ✅ |
| N-R4-5 "causal chain" | R4 INFO → R5 RESOLVED | ✅ |
| R2-N3 Actionable | R1→R5 → RESOLVED (ICML 语境) | ✅ |

### 本轮降级 (1)
| Issue | 状态 |
|-------|------|
| R3-N-new-3 Baseline vals | PARTIAL → info (不再追踪) |

### 本轮新发现 (1)
| Issue | 严重性 |
|-------|--------|
| N-R5-1 AUTHORERR | info |

### 全局统计
- 总 issues: 27 (跨 5 轮)
- Resolved: 26
- Open: 1 (N-R5-1 AUTHORERR, info 级)
- **所有 critical 和 warning 级别 issues 已清零**