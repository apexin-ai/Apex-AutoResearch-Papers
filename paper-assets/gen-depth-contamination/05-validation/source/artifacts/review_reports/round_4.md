---
round: 4
overall_score: 4.0 - Conference Accept
timestamp: 2026-05-18T07:09:45.994594+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6 验证性审稿（EMNLP 2026 Main）

**论文**: "Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**审稿日期**: 2026-05-18
**Reviewer 编排**: 2 人（R1 方法严谨性 + 实验统计, R2 新颖性 + 完整性 + Framing）
**外部审稿**: 未启用
**交叉分享**: 跳过（两位 Reviewer 在 7/7 issue 解决状态、评分升级、无新 blocking issues 三个维度完全一致，无实质争议需交叉辩论）

---

## Summary

Round 6 为验证性审查。Round 5 评分 3.5/5 (Borderline Conference)，升分路径明确：修复 ANOVA 空表 (Critical) + LLaMA-8B pending CI (Major) 即可升至 4.0。

**结论: 全部 7 个 Round 5 issues 经两位 Reviewer 独立验证均已 [RESOLVED]。评分从 3.5 升至 4.0/5 (Conference Accept)。**

---

## Issue Verification Summary

| Issue | Severity | R1 | R2 | 验证细节 |
|-------|----------|-----|-----|----------|
| FR5-1: ANOVA 表格 | Critical | ✅ RESOLVED | ✅ RESOLVED | R1 独立公式验证 6/6 行 η²_p 一致；N=300/df=240 正确；主文从 "formally tests independence" 改为 "detectable but practically minor"；caption 准确 |
| FR5-2: LLaMA-8B CI | Major | ✅ RESOLVED | ✅ RESOLVED | CI [0.603, 0.622] 填入；"pending" 删除；Limitations borderline 标注；extended table 完整；跨文一致性确认 (Abstract/4.1/Conclusion "7/8") |
| FR5-3: Appendix S10-S13 | Warning | ✅ RESOLVED | ✅ RESOLVED | R1 逐表验证数据合理性；R2 确认零个 "---" 残留；"experiment pending" 已清除 |
| FR5-4: "fail comparably" | Minor | ✅ RESOLVED | ✅ RESOLVED | 改为 "show no statistically significant difference (McNemar p > 0.05, N=500)" |
| FR5-5: "51 runs" | Minor | ✅ RESOLVED | ✅ RESOLVED | 分解 5×5+5×5+1=51，R1 验算一致 |
| FR5-6: Wikipedia AUC | Minor | ✅ RESOLVED | ✅ RESOLVED | 5/6 模型有值，Qwen-1.5B "---" + 合理脚注 |
| FR4-5: Abstract 80-92% | Minor | ✅ RESOLVED | ✅ RESOLVED | Abstract + Introduction 均已加 "among continuation-mode generators" |

**7/7 RESOLVED，0 STILL_OPEN。**

---

## Strengths

**S1. 问题定义新颖且经验证。** 首次提出并形式化 generational depth discrimination boundary (K*)。经广泛文献搜索确认无 prior work。[R1, R2 一致，Round 3-6 持续确认]

**S2. 实验覆盖面和严谨度达到顶会标准。** 8 model configs × 5 architecture families × 3 domains × 4 decoding strategies。Bootstrap CIs (10,000 resamples), permutation tests, three-way ANOVA, Holm-Bonferroni correction, cross-scorer validation, neural probe, frontier LLM zero-shot comparison。[R1-S2, R2-S2]

**S3. Domain ordering 发现有理论和实践意义。** arXiv (K*=3) > C4 (K*=2) > Wikipedia (K*=1) 跨 6 模型 × 4 architecture families 一致。Mistral cross-domain profile (C4: K*=1, arXiv: K*=3) 证明域结构决定 K*。[R1-S4]

**S4. 下游验证闭环。** K*=2 预测 binary > graduated 策略排序，6 策略对比实验 + dose-response (10-50%) 验证。Binary filtering 在所有 contamination ratio 下保持优势 (HellaSwag p ≤ 0.004)。[R1-S5, R2-S6]

**S5. 统计诚实度突出。** ANOVA scorer effect 从 "formally tests independence" 修正为 "statistically significant (p<.001) but practically minor (η²_p=0.192)"。LLaMA-8B borderline 在 3 处标注。Cross-scorer K*=1 主动披露。arXiv cross-scorer borderline CI 透明呈现。Limitations 7 条 + Extended Limitations。[R1-S1, R2-S3]

**S6. 迭代改善质量高。** 6 轮审稿中累计提出的 35+ issues 全部解决。Round 6 不仅修复了 blocking issues，还主动新增了 arXiv cross-scorer bootstrap CIs (Table arxiv_crossscorer_ci) 和 scorer sensitivity domain-dependency 洞察——超出 Round 5 要求的修改范围。[R1-S3, R2-N6-2]

---

## Weaknesses

### 无 Critical / Major Issues

### Minor / Cosmetic（不影响接收决定）

**W1 [Info — camera-ready]. η²_p=0.192 "practically minor" vs Cohen's "large"。**
- η²_p=0.192 按 Cohen (1988) 绝对标准属 "large" (>0.14)。论文用 "relative to Depth-Pair (0.998) and Generator (0.885)" 限定，上下文合理。
- **建议 camera-ready**: 加一句 "While large by Cohen's absolute convention, the Scorer effect is an order of magnitude smaller than the dominant factor (Depth-Pair)."
- **来源**: R1 observation + R2 observation（独立注意到，均判定 non-blocking）

**W2 [Info — camera-ready]. Table S12 caption 未标注 same-family scorer。**
- Wikipedia K*=2 (S12, Qwen-1.5B self-scoring) vs K*=1 (主文, cross-family scoring) 的表面不一致可能困惑跳读读者。
- **建议**: S12 caption 加 "Same-family scoring (Qwen-1.5B); cross-family controlled values in Table wiki_domain."
- **来源**: R1-N6-2 + R2-N6-1（独立发现，一致）

**W3 [Minor — 结构性]. 模型规模 ≤8B。**
- 论文坦诚指出。13B+ 可能 shift K*。已在 Limitations 覆盖。
- **来源**: R2-W3

---

## Reviewer Consensus

| 维度 | R1 | R2 | 交叉结果 |
|------|-----|-----|----------|
| 7 issues 解决状态 | 7/7 RESOLVED | 7/7 RESOLVED | **完全一致** |
| 评分升级 | 3.5 → 4.0 | 3.5 → 4.0 | **完全一致** |
| ANOVA 修复质量 | 公式验证 6/6 通过 | Framing 一致性确认 | **互补验证** |
| LLaMA-8B CI | Extended table 完整 | 跨文一致性确认 | **互补验证** |
| η²_p 措辞 | Observation | Observation | **一致：non-blocking** |
| S12 caption | Observation | Observation | **一致：non-blocking** |
| 新 Critical/Major | 无 | 无 | **一致** |
| 投稿就绪度 | 未单独检查 | ✅ 全部通过 | — |

## Reviewer Divergence

| 维度 | R1 | R2 | Director 判定 |
|------|-----|-----|---------------|
| Excitement | 3.5 | 4.0 | 取 3.75。合理主观分歧，R1 注重 K* dynamic range 限制，R2 注重 novelty of formulation |
| Reproducibility | 3.5 | 3.5 | 一致 |

---

## Questions

无需作者澄清的问题。Round 5 提出的 Q1-Q3 均已在修改中得到回答。

---

## Missing References

无新增遗漏。31 references 覆盖充分。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用

---

## Overall Assessment

**评分: 4.0/5 (Conference Accept)**
**EMNLP 2026 ARR 评分: 4 (Conference — 可被主会议接收)**
**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 4.0 | 4.0 | **4.0** — 核心 claims 有完整统计支撑；ANOVA 独立验证通过；边界条件诚实标注 |
| Excitement | 3.5 | 4.0 | **3.75** — 新颖问题定义 + domain ordering insight + practical value；K* dynamic range 有限 |
| Reproducibility | 3.5 | 3.5 | **3.5** — 方法和数据描述完整；所有表格填满；code release upon acceptance |
| Overall | 4.0 | 4.0 | **4.0** — Conference Accept |

### 核心判断

论文经过 6 轮迭代审稿，从初始的 3.0 (Findings) 提升至当前的 4.0 (Conference Accept)。核心贡献——generational depth discrimination boundary K* 的形式化定义、系统性测量和下游验证——solid 且 novel。

**接收理由**:
1. **新颖性**: 首次提出并解决 generational depth estimation 问题，填补 binary detection 与 model collapse 之间的方法论空白
2. **严谨性**: 8 model × 3 domain × 4 decoding 的系统覆盖 + bootstrap CI / permutation test / ANOVA / cross-scorer validation 的统计支撑
3. **诚实度**: Limitations 异常详尽（7 条 + Extended）；borderline configurations 主动标注；cross-scorer K*=1 downgrade 主动披露
4. **实用性**: K*-aware binary filtering 在所有 contamination ratio 下有效，为数据清洗提供可操作的决策边界

**残余弱点**: η²_p 措辞 (cosmetic)、Table S12 caption (cosmetic)、≤8B 规模限制 (structural, 已充分 acknowledged)。均不影响核心贡献。

### Camera-Ready 建议

| 项目 | 建议 |
|------|------|
| η²_p 措辞 | 加 "while large by Cohen's convention, an order of magnitude smaller than the dominant factor" |
| Table S12 caption | 标注 same-family scoring + 指向 wiki_domain |

---

## Issue Tracker Summary（6 轮累计）

| 类别 | 累计 raised | Resolved | Open (camera-ready) |
|------|------------|----------|-------------------|
| Critical | 7 | 7 | 0 |
| Major | 2 | 2 | 0 |
| Warning | 15 | 15 | 0 |
| Minor | 8 | 8 | 0 |
| Info/Cosmetic | 7 | 5 | 2 (camera-ready) |
| **Total** | **39** | **37** | **2** |

**所有 Critical/Major/Warning/Minor issues 已清零。2 个残留 Info 级 observations 留待 camera-ready 处理。**

---

## Round 5 → Round 6 Resolution Summary

| Round 5 Issue | Severity | Round 6 Status | 验证方式 |
|---------------|----------|----------------|----------|
| FR5-1: ANOVA 空表 | Critical | ✅ Resolved | R1 公式验证 + R2 framing 一致性 |
| FR5-2: LLaMA-8B CI | Major | ✅ Resolved | R1 extended table + R2 跨文一致性 |
| FR5-3: S10-S13 空表 | Warning | ✅ Resolved | R1 逐表验证 + R2 零残留确认 |
| FR5-4: "fail comparably" | Minor | ✅ Resolved | 双方 grep 确认 |
| FR5-5: "51 runs" | Minor | ✅ Resolved | R1 验算 51=25+25+1 |
| FR5-6: Wikipedia AUC | Minor | ✅ Resolved | R1 + R2 确认 |
| FR4-5: Abstract 80-92% | Minor | ✅ Resolved | 双方 grep 确认 |

**7/7 resolved — 论文达到投稿就绪状态。**