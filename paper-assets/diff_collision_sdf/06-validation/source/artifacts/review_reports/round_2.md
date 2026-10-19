---
round: 2
review_mode: continue
overall_score: borderline accept
timestamp: 2026-05-28T06:40:07.707908+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---


# 审稿报告 — diff_collision_sdf Round 2（修订评估）

**Venue**: CoRL 2026
**Reviewers**: R1 (方法/统计修复验证), R2 (写作/Framing/相关工作)
**R3 说明**: Round 2 未派发 R3（修订评估仅需 2 人）。R3 的 Round 1 发现（R3-N1 Limitations, R3-N2 Broader Impact, R3-W2 术语统一）均由 R2 在 Round 2 中逐条验证并确认修复状态。
**交叉回应**: 免除（2 位 Reviewer 评分与判断高度一致，无分歧）
**轮次**: Round 2（基于 Round 1 修订）

---

## Summary

论文针对 Round 1 提出的 14 个问题（5 critical + 9 warning/info）进行了修订。所有 5 个 critical issues 已解决，其中 4 个修复质量优秀，1 个修复充分但有遗漏。4 个 in_progress 项中 1 个已解决，3 个仍未在指定位置执行。修订新引入 5 个 warning/info 级别问题，其中 SafeVLA 分类错误最需关注。

---

## Round 1 Issues 修复状态总览

### Critical Issues（5/5 已解决）

| Issue | Round 1 | Round 2 | 修复质量 | 验证者 |
|-------|---------|---------|---------|--------|
| R1-N1 Permutation test 循环论证 | critical | resolved | WEAK | R1 |
| R1-N2 Absence-of-evidence 错误 | critical | resolved | GOOD | R1, R2 |
| R1-N3 实验范围过窄 | critical | resolved | GOOD | R1 |
| R2-N2 SafeVLA/VLSA 矛盾 | critical | resolved | GOOD* | R2 |
| R2-W3 标题耸动 | critical | resolved | GOOD | R2 |

*含新引入的 SafeVLA 分类事实性错误（NEW-1）

### Warning/Info Issues（6/9 已解决）

| Issue | Round 1 | Round 2 | 备注 | 验证者 |
|-------|---------|---------|------|--------|
| R1-W1 Oracle 生态效度 | in_progress | **still_open** | Section 5 正文无 caveat | R1 |
| R1-W2 位移测量不一致 | in_progress | **still_open** | 仍在脚注非正文 | R1 |
| R1-W3 n=3 统计力度 | resolved | resolved-good | Power Analysis 完成 | R1 |
| R3-N1 Limitations 不足 | resolved | resolved-good | sim-to-real 覆盖充分 | R2 (代 R3 验证) |
| R3-N2 Broader Impact 不足 | resolved | resolved-good | 三维度覆盖 | R2 (代 R3 验证) |
| R3-W2 术语混用 | in_progress | **resolved** | 执行彻底 | R2 (代 R3 验证) |
| R2-W1 缺失引用 | open | **partially** | 3 补 / 3 缺 | R2 |
| R2-W2 替代 filter 讨论 | in_progress | **still_open** | 未添加 | R2 |
| R1-W5 "20×" 过度强调 | open | **still_open** | 仍 6 次 | R1, R2 |
| R2-W4 Future work 简略 | open | resolved-weak | 可接受 | R2 |
| R1-W4 spatial_bowl 局限 | resolved | resolved | Limitations 覆盖 | R1 |
| REV-1 Phase 2 数据错误 | resolved | resolved-good | 58.0% + 18K 脚注 | R1 |
| REV-2 p>0.05 for all | resolved | resolved-good | 全文 5 处已清除 | R1 |

---

## 修复质量详评

### RESOLVED-GOOD（高质量修复）

**R1-N2 — Statistical power disclosure**：claim3.tex 新增 "Statistical power"（MDE≈5pp 计算验证正确：df=4, t_{0.05,4}=2.132, t_{0.20,4}=0.941, MDE≈5.02pp）和 "Evaluation-seed consistency"（诚实报告 λ=0.1 跨 3 seeds 一致 +1.5/+2.5/+5.5pp，承认 underpowered）。"Whether this consistent directional pattern reflects a genuine small benefit or residual confounding cannot be resolved at the current sample size" 措辞优秀。全文 "zero benefit" → "no statistically significant benefit at the tested scale" 贯穿一致。[R1 验证]

**R1-N3 — Scope narrowing**：新增 "Scope and generalizability" 段落，明确区分 Claim 1 structural generality vs Claim 3 EE-only specificity。Abstract/Intro/Conclusion 一致限定为 SafeLIBERO 诊断研究。标题从 "When 98% of Collision Avoidance is an Illusion" 改为 "How Action Collapse Creates Illusory Safety in VLA Collision Avoidance Evaluation"。[R1, R2 验证]

**R2-N2 — SDF integration pathways**：三路径分类框架（auxiliary loss / constrained optimization / runtime filtering）结构清晰，全文一致引用。Scope paragraph 明确限定 "specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways"。（SafeVLA 具体描述有误，见 NEW-1）[R2 验证]

**R3-N1 + R3-N2 — Limitations & Broader Impact**：Limitations 显著扩展，覆盖 sim-to-real gap（碰撞检测差异、传感器噪声、真机 action collapse）、统计功效、oracle 基线局限。Broader Impact 三维度覆盖（dfCAR 定位为诊断补充、评估方法论洞察非安全研究否定、防止 "VLA safety is futile" 误读），语气平衡无 defensive tone。[R2 代 R3 验证]

**R3-W2 — 术语统一**：逐节检查确认 "action-collapsed" 贯穿全文。Section 4 标题改为 "The Action-Collapsed Safety Problem"，Table 2 caption 改为 "Action-collapse decomposition"。"Fake safety" 仅在 Introduction 首次引入时加引号使用（"colloquially, 'fake safety'"）。所有 active 文件中无 "frozen episodes" 残留。[R2 代 R3 验证]

### RESOLVED-WEAK（修复充分但有遗漏）

**R1-N1 — Null construction robustness**：Null A（仅 LoRA-only, C(6,3)=20）和 Null B（pooled, C(9,3)=84）并行报告，数学正确（R1 独立枚举验证 Null A: 3/20 sum≥171.0, p=0.150）。**遗漏**：(a) 未承认 C(6,3)=20 的 p 值分辨率局限——最小可能 one-tailed p=1/20=0.05，Null A 在设计上几乎无法检测任何效应；(b) 将 Null A 定位为 "alternative" 而非承认原始 Null B 的方法论争议性。[R1 验证]

### STILL_OPEN（3 项未在指定位置执行）

**R1-W1**：claim2.tex (Section 5) 正文无任何关于基础模型 TSR≈0%/Collapsed=99.4% 的 caveat。Limitations 有一句但不等价于正文 caveat。建议添加 1 句："Note that the base model is itself largely action-collapsed (99.4% collapsed episodes); the structural finding should hold regardless of base-policy activity, but validation on a functional policy remains future work."

**R1-W2**：位移测量不一致（Pi0 obstacle displacement vs Pi0.5 EE displacement）仍仅在 claim1.tex 脚注中说明，method.tex Section 3.2 无变化。建议在 Eq. 1 后补充正文段落论证 bimodal gap 下两种度量的等价性。

**R2-W2**：bimodal gap 论证了 τ_d 阈值 robust，但未回答"为什么选 displacement 而非 action variance 或 velocity"。建议补 1-2 句："Alternative displacement metrics (e.g., action variance, mean velocity) would yield equivalent classification given the five-order-of-magnitude bimodal gap; we adopt maximum displacement for interpretability."

---

## Round 2 新发现问题

### NEW-1 [warning] SafeVLA 分类事实性错误

`related_work.tex` "SDF integration pathways" 段将 SafeVLA 归类为 "(b) Constraint-based planning...using SDF constraints **during planning rather than training**." SafeVLA（Zhang et al. 2025, NeurIPS Spotlight）标题 "via Constrained Learning"，核心方法 ISA 基于 CMDP 在**训练时**约束优化，非 planning-time。

**修复**：改 "Constraint-based planning" → "Constrained training"，改 "during planning rather than training" → "embedding safety constraints directly into the training objective (CMDP)"。核心差异是 auxiliary supervision (a) vs constrained optimization (b) vs runtime filtering (c)。[R2 发现]

### NEW-2 [warning] Abstract "all" vs Discussion "nearly all"

abstract.tex: "demonstrations alone account for **all** measured avoidance gains"
discussion.tex: "collision-free demonstrations account for **nearly all** measured avoidance gains"

与 evaluation-seed consistency 段落的 "consistent directional pattern" 一致，Abstract 应同步为 "nearly all"。[R1 发现]

### NEW-3 [warning] 5 处 "redundant/redundancy" 与 hedged 语言冲突

`related_work.tex` L12, `discussion.tex` L11/L20, `appendix.tex` L229/L235。"Redundant" = confirmed equivalence，比正文 "no statistically significant benefit at the tested scale" 更强。建议统一为 "absence of statistically significant benefit" 或加 "at the tested scale"。[R1 发现]

### NEW-4 [warning] Discussion 首句覆盖面超出实验 scope

discussion.tex: "current VLA safety evaluation is **structurally unreliable**" — 覆盖整个 VLA 评估领域，与 Scope paragraph 矛盾。建议限定为 "CAR-based VLA safety evaluation on the tested benchmark" 或 "as currently practiced on SafeLIBERO"。[R1 发现]

### NEW-5 [info] Abstract "geometric supervision" 宽于论文 scope

Abstract 末句 "rather than geometric supervision" 应为 "rather than EE-only geometric supervision"，与 Scope paragraph 限定一致。[R2 发现]

---

## Reviewer Consensus

两位 Reviewer 在以下判断上完全一致：
1. **改善程度显著**——Statistical power disclosure、scope narrowing、标题修改、Limitations/BI 扩展质量好
2. **评分上调**：均从 5/10 → 6/10 (Borderline Accept)
3. **残留问题均为低成本修复**——最大的 NEW-1 改几个词即可
4. **3 个 still_open 项**影响有限但应修复
5. **"20×" (6 次) 和 "redundant" (5 处) 残留**造成论文内部 tone 不一致

---

## Missing References（仍缺 3 项）

- **HazardArena** (arXiv 2604.12447)：VLA 安全评估 benchmark，最直接相关
- **VLA-Risk** (OpenReview 2025)：VLA physical robustness benchmark
- **D2PPO** (arXiv 2508.02644)：Diffusion policy representation collapse 解决方案

已补充的（Round 2 新增）：Dong 2025 ✓, VLA safety survey ✓, CSSDF-Net ✓, SafeDiffuser ✓, CAPE ✓, CDF ✓, RDF ✓

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：已完成 (2026-05-28 06:31) | 0 critical, 0 warning, 7 info（Round 1: 3 warning → 0 warning）

主要 info items:
- Figure 2 标注字号偏小（Round 1 遗留，建议增大或用缩写+图例）
- Figure 4 x 轴 categorical vs continuous 歧义——建议 caption 注明 "x-axis is categorical, not to scale"
- Table 2 "n/a" 单元格可补充具体 episode 数
- Figure 5 p-value 标注略拥挤

---

## Overall Assessment

**评分：6/10 (Borderline Accept)**
**置信度：High（两位 Reviewer 评分一致、判断对齐）**
**相比 Round 1：4/10 → 6/10，+2 分**

### 改善总结

论文在最关键的三个维度上实现了实质性改善：

1. **统计诚实度**（R1-N2）：从 "zero benefit / redundant" 的断言式语言转向 "no statistically significant benefit at the tested scale"，并透明报告 MDE、evaluation-seed consistency 的方向性效应。从违反统计推断基本原则转变为审慎的科学表述。

2. **Scope 校准**（R1-N3）：标题去掉 "98%"，全文限定为 SafeLIBERO 诊断研究，新增 Scope paragraph 区分 Claim 1 generality vs Claim 3 specificity。

3. **Related Work 定位**（R2-N2）：三路径分类框架将负面发现严格限定在 EE-only auxiliary loss 路径，不否定 SafeVLA/VLSA。（需修正 SafeVLA 描述。）

### 修订建议优先级

- **P0（投稿前必须）**: NEW-1 SafeVLA 分类错误（改几个词）; NEW-2 Abstract "all" → "nearly all"
- **P1（强烈建议）**: NEW-3 清除 5 处 "redundant"; NEW-4 Discussion 首句限定 scope; R1-W1 Section 5 添加 1 句 oracle caveat
- **P2（建议）**: R1-W2 Section 3.2 位移度量正文化; R2-W2 替代 filter 1-2 句; R1-W5 "20×" 减至 2-3 次; NEW-5 Abstract "geometric supervision" 限定
- **P3（可留 rebuttal）**: R2-W1 补充 3 个缺失引用

### 接收倾向

**Borderline Accept 理由**：(a) 核心诊断贡献（action collapse 污染 CAR）真实且有社区影响力；(b) 100+ 实验规模扎实；(c) 修订版统计处理达到可接受水平；(d) dfCAR 工具有实际采用价值。

**未达 Weak Accept 理由**：(a) 纯诊断论文缺少建设性 proof-of-concept；(b) 单 benchmark、纯仿真；(c) SafeVLA 事实性错误需修正；(d) 部分 warning 项在两轮修订后仍未执行。

如果 P0 + P1 项在投稿前完成，论文满足 CoRL 接收标准。
