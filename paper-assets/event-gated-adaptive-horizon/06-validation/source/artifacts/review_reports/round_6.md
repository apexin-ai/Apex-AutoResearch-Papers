---
round: 6
review_mode: continue
overall_score: borderline accept
timestamp: 2026-05-28T01:07:50.688986+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 6（修订版）

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: ICML 2026
**审稿日期**: 2026-05-28
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 数据完整性 | R2: Venue 合规 + 写作质量 + 贡献度）
**轮次**: Round 6 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
**上轮评分**: Round 5 Borderline Accept (7/10)
**修订说明**: 替换初版报告（初版基于 venue-confused 交叉回应 + Director 校正；本版基于 ICML 校准后的完整两轮交叉分享）

---

## Summary

Round 5 遗留的 3 个 open/in\_progress issues 中，2 个 RESOLVED（AUTHORERR 修复、正文扩至 8 页满 ICML 配额），1 个 PARTIALLY RESOLVED（色盲配色改善但未完全消除红/绿依赖）。论文在格式合规和内容密度上有实质改善。

Round 6 引入 3 个新 warning 级别透明度问题，两位 Reviewer 在交叉分享后达成完全共识：
1. **F6 (008e\_v3) 结果 180° 翻转**（Must-Fix）：种子集变更 + 结论从 "2/4 collapse" 翻转为 "0/4 CIVO onset" + 无解释
2. **"corrected-code rerun" 透明度**（warning）：008f 代码修正未交代内容和影响范围
3. **AUROC 演进透明度**（Should-Fix）：n=30→36 新增数据点不明，分离间隙仅 0.21×

三个问题叠加构成 **数据变更透明度的整体性关切**——论文两个关键 control（008e\_v3 和 008f）均涉及不透明代码修正。这不是方法论缺陷，而是 reporting 规范问题，可通过补充说明快速修复。

---

## Round 5 Open Issues — 修复状态

| Issue | Round 5 状态 | Round 6 状态 | R1 | R2 |
|-------|-------------|-------------|----|----|
| N-R5-1 AUTHORERR | in\_progress (info) | **RESOLVED** | ✅ 确认 | ✅ 确认 |
| N-R5-2 正文 6 页 / display 密度 | in\_progress (warning) | **RESOLVED** | ✅ 确认 | ✅ 确认 |
| N-R5-3 色盲友好 | in\_progress (info) | **PARTIALLY RESOLVED** | NOT VERIFIED → 接受 R2 判断 | ✅ PDF 验证：线型冗余改善，红/绿未完全消除 |

---

## Strengths

1. **Factorial design 系统严谨**（6 轮共识）：43 配置 × 4-5 seeds × 6 环境，Fisher exact test (p<0.001)
2. **NVE 完美分类**：AUROC=1.000, F1=1.000 (n=36)，LOEO 三折 + LOCO 36/36 双重交叉验证
3. **Cheetah 机制解离**：Walker 有 reward fidelity gap (1.63×) 而 Cheetah 无 (1.00×) 却有更高 CIVO severity (8.27×)——揭示多通路机制，深化了 Round 5 对 CIVO 的理解
4. **Temporal ordering (n=2)**：fidelity gap 先于 value overestimation ~10K 步 (r=0.81, p=0.002)，建立时间因果链
5. **Cartpole 负对照**：single-joint 0/3 CIVO，精确划定触发边界为 multi-joint locomotion
6. **Discussion 质量飞跃**：从 2 段扩至 7 段系统性分析（mechanism, causal role, intervention resistance, transferable protocol, practitioner guidelines, training horizon, scope precision），每段独立论点有证据支撑
7. **CIVO 机制图提升至 Introduction (Figure 1)**：full-width figure 在 page 2 提供直观理解
8. **ICML 格式完全合规**：icml2026.sty, double-blind, Broader Impact Statement, `\icmlcorrespondingauthor` 均到位
9. **正文充实至 8 页**：满 ICML 配额，6 display items / 8 页正文，信息密度合理

---

## Weaknesses（按严重性排序）

### Warning — Must-Fix

**W-W1. F6 (008e\_v3) 结果 180° 翻转，无透明解释 [2/2 共识，Must-Fix]**

Round 6 最严重的问题。两位 Reviewer 独立发现并在交叉分享中完全一致：

- Seeds 从 s1-s4 变为 s0, s1, s2, s5（s3, s4 被替换）
- 结论从 "2/4 collapse"（prior rounds）翻转为 "0/4 CIVO onset"
- NVE threshold 变化（1.5×→2.0×）不能解释此翻转——prior rounds NVE 值 (4.02×, 3.78×) 远超 2.0×
- "v3" 命名暗示代码迭代，但正文无版本变更声明（对比 008f 至少有脚注 f）
- 旧结论 "even dt=1 cannot fully prevent CIVO" 变为 "dt=1 eliminates CIVO"

**R2 交叉回应补充**（R1 AGREE）：这不仅是数据变更，更是 **论证逻辑重构**。旧 F6 支撑 intervention resistance 叙事，新 F6 支撑 "multi-step imagination is necessary for CIVO" 结论。两者互斥。论文选择了更 clean 的新结论，但读者无法评估此判断的可靠性。

**要求**：camera-ready 或 rebuttal 必须交代：(a) 008e→008e\_v3 的代码修正内容，(b) 旧结果作为参照，(c) seed 集合变更原因。

### Warning — Should-Fix

**W-W2. "corrected-code rerun" (Table 1 脚注 f) 缺乏细节 [2/2 共识，warning]**

R1 初评 info，交叉分享中被 R2 说服升级至 warning。核心论据：
- 008f 是 "Removed embedding" 控制组，Table 2 "Removed: 6/6 (100%)" 依赖其健康结论
- 与 008e\_v3 (W-W1) 构成 **两个关键控制配置均涉及不透明代码修正** 的 pattern

**缓解因素**（R1 交叉回应发现）：Table 3 脚注 l 提供 pre-correction 数据——"eval 503.0, NVE 0.97×, superseded"。修正前 NVE=0.97× 仍分类为 non-CIVO，**6/6 统计事实上不受影响**。但此信息埋在 appendix 脚注中，正文应直接交代。

**W-W3. AUROC/threshold 变更透明度 [2/2 共识，Should-Fix]**

- n=30→36：新增 6 个 data points 来源未列明
- Threshold 1.5×→2.0×：选择依据可更清晰
- 分离间隙仅 0.21×（最低 CIVO-positive 2.09× vs 最高 non-CIVO transient 1.88×，R1 发现）
- **缓解**：Appendix B.5 承认 post-hoc；LOEO 三折完美分类；LOCO 36/36
- **仍需**：列出新增 data points + 讨论 0.21× margin 在不同 reward scales 下的稳健性

### Info

**W-I1. 移除若干引用 [R1]**：DreamSmooth/NoisyNet/PETS/STEVE。若与论文主题直接相关需保留。

**W-I2. Table 1 "--- s1" 格式 [2/2]**：008f seed 1 行 Exp 编号空白。

**W-I3. Discussion "three-stage causal chain" 措辞 [R2 交叉回应]**：analysis.tex 中 "three-stage causal chain (n=2)" 与 results.tex "trace a predictive pathway" 不完全一致。R2 指出此措辞 "仍暗示比数据支撑更强的因果推断"。边界可接受但值得 camera-ready 注意。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| N-R5-1 AUTHORERR | RESOLVED | RESOLVED | **2/2** |
| N-R5-2 Display 密度 | RESOLVED | RESOLVED | **2/2** |
| N-R5-3 色盲 | NOT VERIFIED → 接受 R2 | PARTIALLY RESOLVED | **2/2 (R1 defer)** |
| N-R6-1 F6 翻转 | Must-Fix | Must-Fix | **2/2** |
| N-R6-2 AUROC | Should-Fix | Should-Fix | **2/2** |
| N-R6-3 corrected-code | warning (升级) | warning | **2/2** |
| Soundness | 3.25/4 (调整后) | 3/4 | **3-3.25** |
| Presentation | 3/4 | 3/4 | **3/4** |
| Originality | 3/4 | 3/4 | **3/4** |
| Significance (ICML) | 3/4 | 3/4 | **3/4** |
| Overall | 4.5/6 (调整后) | 4/6 | **4-4.5 Weak Accept** |

**完全共识**：Presentation, Originality, Significance, 所有 issue 严重性分级。
**窄幅分歧**（0.25-0.5 档）：Soundness, Overall。

---

## Reviewer Divergence

**Soundness (R1: 3.25/4 vs R2: 3/4) — 0.25 差距**

R1 初评 3.5/4，交叉分享中被 R2 说服下调至 3.25/4，承认 corrected-code 透明度权重应更高。R2 维持 3/4，认为 F6 透明度是 Soundness 问题（实验可验证性）而非仅 Presentation 问题。两者核心关切相同，权重微差。

**Director 裁决**：差异不构成实质分歧。Soundness **3.25/4**（取 R1 调整后值，兼顾方法论质量和透明度扣分）。

**Overall (R1: 4.5/6 vs R2: 4/6) — 0.5 差距**

核心分歧：是否在评分中预支 camera-ready 修复的信用。
- R1：科学贡献实质性达标，透明度问题可修复 → 4.5/6
- R2：F6 翻转非 minor issue，当前版本可信度有风险，不应预支 → 4/6

R2 明确表示 "不认为 R1 的评分不合理"，R1 也承认 R2 的 "三重叠加" 论点有说服力。两位均建议 **4.5/6 作为共识中间点**。

**Director 裁决**：接受 **4-4.5/6 Weak Accept** 区间。R2 的审慎原则（不预支 camera-ready 信用）是更保守但更稳健的立场。

---

## Questions for Authors

1. **008e\_v3 版本变更**（Must-Fix）：代码修正了什么？为什么更换 seeds？旧 seeds (s3, s4) 的结果是否可用？请提供版本变更日志和旧结果参照。
2. **008f corrected-code**（Should-Fix）：具体修正了什么 bug？影响范围是否波及 subsample=ON 的其他实验？建议将 Table 3 脚注 l 的 pre-correction 数据 (NVE=0.97×) 信息提升到正文 Table 1 脚注。
3. **AUROC n=30→36**（Should-Fix）：新增的 6 个 data points 分别来自哪些实验？
4. **NVE 分离间隙**：0.21× (2.09× vs 1.88×) 在不同 reward scales 或新环境中是否足够稳健？
5. **Discussion "three-stage causal chain"**：是否应统一为 "predictive pathway" 以与 results.tex 措辞一致？

---

## Missing References

无新增遗漏。DreamSmooth/NoisyNet/PETS/STEVE 的移除需确认是否影响覆盖面。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未请求**。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warnings, 7 info）。与 Round 5 对比：Critical 1→0（AUTHORERR 修复）。

**主要发现**：
1. **[warning] Pages 7-8 Discussion+Conclusion 连续纯文本**：无 figure/table 穿插。
2. **[warning] Page 24 ~40% 空白**：LaTeX float 问题。
3. **[warning] Page 31 最后页 ~70% 空白**。
4. **[info] Page 1 纯文本**（Figure 1 在 page 2，可接受）。
5. **[info] Figure 1 路径图文字偏小**。
6. **[info] Figure 9/14 热力图轴标签偏小**。
7. **[info] Appendix Tables 17-30 密度极高**。

---

## Overall Assessment

**评分: Borderline Accept (7/10)**
**置信度: High (4/5)**

**与 Round 5 (Borderline Accept, 7/10) 的变化**：

| 维度 | Round 5 | Round 6 | 变化 |
|------|---------|---------|------|
| AUTHORERR | info (open) | RESOLVED | ▲ |
| Display 密度 / 页数 | warning (open) | RESOLVED (8 pages) | ▲▲ |
| 色盲友好 | info (open) | PARTIALLY RESOLVED | ▲ |
| F6 数据透明度 | — | NEW warning (Must-Fix) | ▼▼ |
| corrected-code | — | NEW warning | ▼ |
| AUROC 透明度 | — | NEW warning (Should-Fix) | ▼ |

**评分维持 7/10 的理由**：

Round 5 的 open issues 基本解决（+），但 Round 6 引入 3 个新 warning（-），正负抵消。

- **正向**：格式完全合规、8 页满配额、Discussion 质量从 adequate 提升至 substantial、统计严谨性显著增强（AUROC=1.000, Fisher exact, temporal ordering）
- **负向**：F6 结果翻转 + corrected-code + AUROC 演进构成数据变更透明度的三重关切。两个关键控制配置（008e\_v3 和 008f）均涉及不透明代码修正，且恰好支撑两个核心结论

**关键判断**：透明度问题是 reporting 规范问题，不是方法论缺陷。核心方法论（factorial design, LOEO, Fisher exact）不受影响。008d（主要 CIVO 触发配置）不涉及版本变更，核心发现独立于 F6。Table 3 脚注 l 的 pre-correction 数据表明 008f 的 6/6 统计不受影响。修复路径清晰且不需要重新实验。

**如果 F6 透明度在 rebuttal/camera-ready 中解决**：评分可上调至 **7.5-8/10 (Weak Accept)**。两位 Reviewer 均明确表示届时无异议。

**综合维度评分**（Director 综合两位 Reviewer）：

| 维度 | 评分 | Round 5 | 变化 | 理由 |
|------|------|---------|------|------|
| Originality | 3.5/5 | 3.5/5 | — | CIVO 新颖，四级诊断框架有方法论价值 |
| Soundness | 3.25/5 | 3.5/5 | ▼ | 方法论可靠但 F6 + corrected-code 透明度拉低。R1 从 3.5→3.25，R2 维持 3。 |
| Clarity | 3.5/5 | 3.5/5 | — | Discussion 大幅改善，抵消 F6 叙事翻转的扣分 |
| Significance | 3/5 | 2.5/5 | ▲ | ICML 是正确 venue。RL diagnostic/failure mode 对 ICML 社区有广泛意义。两位 Reviewer 均给 Significance 3/4 for ICML。 |
| Relevance (ICML) | 4/5 | 4/5 | — | World-model RL + temporal abstraction 是 ICML RL track 核心话题 |

---

## Issue Tracker Summary (Round 6)

### 本轮解决 (2)
| Issue | 轮次历史 | 状态 |
|-------|---------|------|
| N-R5-1 AUTHORERR | R5 info → R6 RESOLVED | ✅ |
| N-R5-2 正文 6 页 / display 密度 | R5 warning → R6 RESOLVED | ✅ |

### 部分解决 (1)
| Issue | 状态 |
|-------|------|
| N-R5-3 色盲友好配色 | PARTIALLY RESOLVED（线型冗余改善，红/绿未完全消除）|

### 本轮新发现 (5)
| Issue | 严重性 | 优先级 | R1/R2 共识 |
|-------|--------|--------|-----------|
| N-R6-1 F6 seed/结果翻转 | warning | **Must-Fix** | 2/2 |
| N-R6-2 AUROC 透明度 | warning | Should-Fix | 2/2 |
| N-R6-3 corrected-code 细节 | warning | Should-Fix | 2/2 (R1 升级) |
| N-R6-4 移除引用 | info | Nice-to-Fix | 1/2 |
| N-R6-5 Table 1 格式 | info | Nice-to-Fix | 2/2 |

### 全局统计
- 总 issues: 32 (跨 6 轮)
- Resolved: 27
- Partially resolved: 1 (N-R5-3, info)
- Open: 5 (3 warning + 2 info)
- Wont\_fix: 1 (N-R5-W1 scope)
- **所有 critical 级别 issues 已清零**
- **3 个 warning 均为透明度问题，非方法论缺陷，修复路径明确**