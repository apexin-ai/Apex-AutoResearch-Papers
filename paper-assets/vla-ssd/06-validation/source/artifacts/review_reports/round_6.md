---
round: 6
overall_score: borderline
timestamp: 2026-05-18T13:47:19.345008+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 7 审稿汇总报告

**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
**Venue**: CoRL 2026 (deadline 2026-05-29)
**审稿模式**: 继续审稿（基于 Round 6 修改稿）
**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)
**本轮评分**: R1 = 6/10, R2 = 5/10 → 共识 5.5/10 Borderline

---

## Summary

本轮审查基于 Round 6 报告提出的 2 个 CRITICAL + 4 个 WARNING + 若干 INFO 级 issue，评估修改稿的回应充分性。论文在方法论严谨性上有实质进步（demo-level split 消除时间泄漏、task-level RSA bootstrap、routing-first 叙事重写、trajectory analysis 新增），但核心结构性问题（无 behavioral validation）仍未解决，且修改引入了新的 internal inconsistency。

---

## Resolved Issues（本轮确认解决）

### R6-C2 [RESOLVED] Probe train/test split + 时间自相关
Method §3.5 明确 demo-level sequential split (demos 0-39 train / 40-49 test)，完全消除时间泄漏风险。这是本轮最重要的方法论改进。

### R6-W1 [RESOLVED] RSA pairwise dependency 未处理
Method §3.4 新增 task-level block resampling 说明 + Nili 2014 引用。N=10 tasks 的统计功效有限但属固有限制。

---

## Open Issues

### 🔴 CRITICAL

#### R6-C4 [STILL OPEN] 缺 behavioral validation，对 CoRL 结构性缺口
**状态**: 新增 open-loop action trajectory analysis (Cohen's d=0.65, 72.3% token divergence)，但这不是 behavioral validation。72.3% 的 action token 改变不告诉读者 task success 变好还是变差。对 CoRL（机器人学习会议）而言，"representational analysis without any task success metric" 是结构性缺口。

**具体问题**:
- Discussion line 11 "confirms the causal role" 措辞过强——trajectory divergence 只证明 causal influence on output，不证明 functional role
- Limitations 段落（Discussion lines 14-15）未承认 behavioral gap，仅讨论 single-model generalization
- MuJoCo 版本不兼容是可理解的技术障碍，但论文应明确承认此限制

**建议修复**:
- Discussion: "confirms the causal role" → "demonstrates causal influence on action output"
- Limitations 新增: "Our analyses are representational and open-loop; connecting these findings to task success requires closed-loop behavioral evaluation, which we leave to future work."
- 如能在 deadline 前解决 MuJoCo 兼容问题并提供哪怕 1-2 个 task 的 success rate，将大幅增强论文说服力

---

### 🟡 WARNING

#### R6-C1 [DOWNGRADED → WARNING] Ablation 因果推断方向
**状态**: 从 CRITICAL 降级。"routing-first specialization" 叙事比 "dual function" 更准确，trajectory analysis 提供了 output-level 因果证据。但存在 internal inconsistency:
- R² 衡量连续动作维度的改善，trajectory 效应集中在 gripper 离散维度（shift 0.291 vs <0.034）——两个 metric 在讲不同维度的故事（→ R7-W1）
- "Per-head effects are comparable" 削弱 instruction-dominant heads 作为 functionally distinct group 的叙事（→ R7-W2）
- N=10 random subsets 偏少（z=-2.73 基于 10 个样本的正态假设）

#### R6-C3 [DOWNGRADED → WARNING] 单模型 overclaim 残余
**状态**: 从 CRITICAL 降级。Abstract line 7 "in the model studied" ✓。但 Introduction lines 16-20 "Three findings emerge" 仍用一般化措辞，Contribution (i) 和 (iii) 未限定模型，Discussion "early-layer parameters may suffice" 仍 unqualified。

**建议修复**: Introduction findings 段落加 "In OpenVLA-7B on LIBERO" 前缀；Contribution (i)(iii) 各加 model-specific 限定。

#### R7-W1 [NEW] 维度分离未讨论
Ablation R² 改善测的是连续维度，trajectory divergence 集中在 gripper（shift 0.291 vs continuous <0.034）。论文将两者并列呈现仿佛互相支撑，但实际测量的是不同 action space 维度。如果 routing 主要影响 gripper control，claim scope 应更精确限定。

#### R7-W2 [NEW] Per-head comparability + Discussion 自相矛盾
Experiments line 86 "Per-head effects are comparable" 意味着 instruction-dominant heads 的 per-head 影响力与非 instruction-dominant heads 相当，削弱了将这 24 个 heads 作为 functionally distinct group 的叙事。Discussion line 12 前半句 "the effect distributes across L1 heads rather than concentrating in instruction-dominant ones" 与后半句 "yet L0-L1 routing concentration suggests early-layer parameters may suffice for adaptation" 逻辑矛盾：如果效应均匀分布，不能同时推论 routing concentration 的特殊意义。

#### R7-W3 [NEW] CKA 矛盾正文讨论不足
Method §3.6 "Why RSA over CKA" justification 已加强，但 CKA 完全反转 inverted-U（monotonically increasing）这一重要矛盾结果仅在 Introduction line 20 一句括号中提及。读者不翻 Appendix 不知道 C3 的 metric-dependency 有多严重。建议 Section 4.4 加 1-2 句正文讨论。

---

### ℹ️ INFO (升级建议)

#### R4-I1 [PERSISTENT] conclusion.tex 未编译
Round 4 发现至今未修复。main.tex 无 `\input{conclusion}`。conclusion.tex 含 code release 声明被浪费。修复成本极低（一行代码）。建议升级至 WARNING：CoRL 要求完整论文结构，缺 Conclusion 可能被审稿人视为不完整。

---

## Strengths（修改后新增/增强）

**S1. 方法论严谨性显著提升**: Demo-level split 彻底解决时间泄漏（Round 6 最严重的方法论问题），task-level block resampling 正确处理 RSA pairwise dependency。这两项修改使统计推断的可信度大幅提高。

**S2. Routing-first 叙事更准确**: 从 "dual function" 改为 "routing-first specialization" 是正确方向——承认 R² increase 而非 post-hoc 强行解释。

**S3. Trajectory analysis 增加因果证据**: Open-loop action trajectory comparison (d=0.65, 72.3% divergence) 虽非 behavioral validation，但比纯 representational analysis 更接近 output-level 证据。Gripper 维度的 selective effect (0.291 vs <0.034) 是有趣发现。

**S4. 三条件 factorial 设计**: Trained/Pretrained/Untrained 三条件交叉 instruction presence 的设计仍是本文最大方法论贡献，在 VLA 分析文献中具有参考价值。

**S5. RSA justification 加强**: Method 新增 RSA 功能性论证（"captures relative distance structure directly governing action prediction quality"），说服力提升。

---

## Weaknesses（当前版本）

**W1 [CRITICAL]. 缺 behavioral validation**: 对 CoRL 是结构性缺口。Open-loop trajectory divergence ≠ task success。论文未在 Limitations 中承认此 gap。

**W2 [WARNING]. 维度分离未讨论**: Ablation R² 和 trajectory analysis 分别测量连续/离散维度，但论文未讨论这一分离。

**W3 [WARNING]. Discussion 内部矛盾**: 效应均匀分布 vs routing concentration 特殊意义的逻辑不一致。

**W4 [WARNING]. Overclaim 残余**: Introduction findings + Contribution (i)(iii) + Discussion 仍有 unqualified generalizations。

**W5 [WARNING]. CKA 矛盾正文讨论不足**: C3 的 metric-dependency 仅括号提及。

---

## Questions to Authors

Q1. Trajectory analysis 显示 72.3% action tokens 改变——其中有多少朝 ground-truth 方向改变、多少偏离？哪怕粗略的方向性分析也能大幅增强因果推断。

Q2. 如果 routing 效应主要影响 gripper (discrete) 维度而 R² 改善测的是 continuous 维度，这两个结果是否在测量不同的 L1 功能？如果是，C2 的 claim scope 应如何调整？

Q3. 既然 per-head effects 在 instruction-dominant 和 non-dominant heads 之间 comparable，将 24/32 heads 标记为 "instruction-dominant" 的分析价值是什么？attention pattern 与 functional contribution 的解耦应如何理解？

---

## Missing References

本轮无新的 missing reference。Round 6 建议的四篇（Hewitt 2019, Nili 2014, Bills 2023, Templeton 2024）已全部添加。

---

## Overall Assessment

**评分: 5.5/10 — Borderline (Weak Reject 倾向)**

论文从 Round 6 的 4.5/10 提升至 5.5/10，方法论严谨性有实质改善。核心阻碍仍是 **缺乏 behavioral validation**——对 CoRL 这个机器人学习会议，纯 representational/open-loop analysis 论文面临天然劣势。

**当前论文如提交 CoRL 2026 的预期评价**:
- 方法论: 中上（factorial design 有参考价值，统计处理得当）
- 新颖性: 中等（C1 是 verification，C2 routing reorganization 是核心 insight，C3 metric-dependent）
- 完整性: 中下（无 behavioral validation，Discussion 有内部矛盾）
- 写作: 中上（结构清晰，但有 overclaim 残余和 CKA 讨论不足）

**可操作的改善路径（按优先级）**:
1. **[HIGH]** Limitations 承认 behavioral gap（0.5h 修复，消除审稿人最可能的 "fatal flaw" 判断）
2. **[HIGH]** Discussion "confirms the causal role" 改为 "demonstrates causal influence"（5min 修复）
3. **[HIGH]** main.tex 加 `\input{conclusion}`（1min 修复）
4. **[MEDIUM]** Introduction findings + Contribution (i)(iii) 加 model-specific 限定（30min）
5. **[MEDIUM]** 讨论维度分离 + 修复 Discussion 矛盾（1h）
6. **[MEDIUM]** Section 4.4 加 CKA 正文讨论（15min）
7. **[LOW → HIGH if feasible]** 任何 closed-loop behavioral 数据（哪怕 1-2 tasks）

R1 评论: "我维持 6/10 但承认 5/10 也有合理依据——取决于审稿人对 'CoRL 是否接受无 behavioral validation 的纯分析论文' 这个 meta-question 的判断。"

R2 评论: "方法论改善是真实的。但 CoRL 审稿人会问：这些 findings 能帮我训练更好的 robot 吗？目前论文无法直接回答这个问题。"

---

## Detailed Score Breakdown

| Criterion | Score | Notes |
|-----------|-------|-------|
| Novelty | 5/10 | C2 routing reorganization 是 genuine insight; C1=verification, C3=metric-dependent |
| Soundness | 6/10 | 方法论大幅改善; ablation 仍有 internal inconsistency |
| Significance | 4/10 | 无 behavioral validation 限制 impact; CoRL community needs actionable |
| Clarity | 6/10 | 结构好但有 overclaim + Discussion 矛盾 |
| Completeness | 5/10 | 缺 conclusion section + behavioral + CKA 正文讨论 |
| **Overall** | **5.5/10** | **Borderline — 倾向 Weak Reject** |

---

## Issue Tracker 同步状态

- **RESOLVED (本轮)**: R6-C2, R6-W1
- **CRITICAL (仍 open)**: R6-C4 (behavioral validation)
- **WARNING (仍 open)**: R6-C1, R6-C3, R7-W1, R7-W2, R7-W3
- **INFO → WARNING**: R4-I1 (conclusion.tex)
- **完整 issue tracker**: `projects/vla-ssd/artifacts/review_issues.yaml`

---

*Reviewed by: R1 (方法/实验), R2 (新颖性/完整性). Cross-responses completed by both reviewers with full consensus on all issues.*