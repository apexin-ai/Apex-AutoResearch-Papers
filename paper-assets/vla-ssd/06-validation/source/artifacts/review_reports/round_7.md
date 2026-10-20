---
round: 7
overall_score: borderline accept
timestamp: 2026-05-18T14:19:37.215344+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 8 审稿汇总报告

**论文**: Vision Encodes, Language Routes: Token-Level Functional Specialization in a Vision-Language-Action Model
**Venue**: CoRL 2026 (deadline 2026-05-29)
**审稿模式**: 继续审稿（基于 Round 7 修改稿）
**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性/格式)
**本轮评分**: R1 = 7/10, R2 = 6.5/10 → 共识 **6.5-7/10 Borderline Accept**

---

## Summary

本轮审查验证了 Round 7 报告中 7 个 in_progress issues 的修复情况。论文经历了质量实质性提升：Discussion 完全重写消除了所有 internal inconsistency，Limitations 显式承认 behavioral gap，CKA 矛盾进入正文，全文 model-specific qualifiers 到位。**所有 CRITICAL 和 WARNING 级 issues 均已 resolved 或降级为 acknowledged limitations。** 仅剩 4 个 INFO 级 polishing items。

---

## Resolved Issues（本轮确认）

### R6-C4 [CRITICAL → WARNING → RESOLVED as acknowledged limitation] Behavioral validation
- Discussion line 12: "demonstrates causal influence on action output"（从 "confirms the causal role" 弱化）
- Limitations line 22（新增）: "Our analyses are representational and open-loop; connecting routing reorganization to task success requires closed-loop evaluation, which we leave to future work."
- Predictions lines 17-18: 将 behavioral validation 定位为 falsifiable prediction 而非已有结论

**两位 Reviewer 共识**: Limitations 声明精准，消除了 "论文不知道自己缺什么" 的 rejection risk。Gap 仍存在但已诚实界定。

### R6-C1 + R7-W1 + R7-W2 [WARNING → RESOLVED] Ablation 逻辑矛盾 + 维度分离 + Per-head comparability
Discussion 完全重写，三个问题一并解决：
- **维度分离** (line 13): "The R² improvement reflects information gain in continuous dimensions (removing routing signals frees bandwidth), while the gripper-concentrated trajectory effect reflects discrete manipulation sensitivity."
- **Per-head comparability** (line 14): "Routing reorganization is the observable signature of L1's acquired collective role, not a property of individual heads."
- **What-vs-how 区分** (line 14): Attention analysis = what the model learns; ablation = how the function is implemented (distributed)

**R1 评价**: "本轮最大改进。自相矛盾消除。"
**R2 评价**: "彻底修复了 Round 7 的 self-contradiction。逻辑一致性显著提升。"

### R6-C3 [WARNING → RESOLVED] 单模型 overclaim
逐处验证通过：
- Introduction line 15: "Three findings emerge from our analysis of OpenVLA-7B on LIBERO"
- Contribution (i): "in the model studied"; (iii): "in this architecture"
- Abstract line 7: "in the model studied"
- Predictions: 用 "should"（预测性语气）
- Conclusion: generic "VLA" 但 context 足够

### R7-W3 [WARNING → RESOLVED] CKA 正文讨论不足
Section 4.4 line 124 新增: "Under linear CKA, the inverted-U disappears (per-layer similarity increases monotonically) and encoder ordering reverses. The non-monotonic trajectory reported here characterizes RSA-specific rank-order geometry; its generality across similarity metrics remains open."

### R5-N4 [WARNING → RESOLVED] Behavioral gap in Limitations
与 R6-C4 合并解决。

### R4-I1 [INFO → RESOLVED] conclusion.tex 未编译
main.tex line 33: `\input{conclusion}`。持续 4 轮的格式问题终于修复。

---

## Remaining Issues（仅 INFO 级）

### R8-I1 [INFO] "Establishing" 措辞不一致
Discussion line 8 "establishing a causal link from routing to output" 与 line 12 "demonstrates causal influence" 和 Limitations line 22 的 open-loop acknowledgment 强度不一致。一词修复: establishing → supporting/providing evidence for。

### R8-I2 [INFO] R² +0.059 来源不明
Discussion line 8 引用 "+0.059 at L1"，但 Experiments 报告 +0.042（dominant heads）和 +0.077（random mean）。数值不可追溯。

### R8-I3 [INFO] Conclusion 偏短
2 句话（~40 words）偏短。可加 broader impact 或 future direction。

### R8-I4 [INFO] Prediction-ablation 张力未显式讨论
Prediction (2)（"L1 ablation should produce task degradation"）与 Experiments（ablation increases R²）之间有隐含张力。R²-behavior dissociation 的逻辑合理但未 explicit。Camera-ready 建议加一句。

---

## Strengths

**S1. Discussion 质量飞跃**: 从 Round 7 的 self-contradictory 半页变为四段完整讨论（Synthesis → Mechanistic interpretation → Predictions → Limitations），逻辑通畅，每段各司其职。

**S2. Predictions 段落**: 两条 testable predictions 使论文从 descriptive analysis 升级为 falsifiable framework。对其他 decoder-only VLAs 的 architectural prediction 和对 L1 ablation behavioral consequence 的 functional prediction 均有明确的 boundary conditions。R2 评价: "本轮最有价值的新增之一。"

**S3. Claim-evidence 匹配**: 全文 claim 强度现在与证据基本匹配。Model-specific qualifiers 遍及 Introduction/Contributions/Abstract，CKA 矛盾在正文透明讨论，Limitations 诚实界定 scope。

**S4. 方法论基础坚实**: Demo-level split、task-level RSA bootstrap、FDR correction、cross-benchmark replication、seed sensitivity 等——统计推断的各个环节均已得到妥善处理。

**S5. 三条件 factorial 设计**: Trained/Pretrained/Untrained × instruction presence 仍是本文最大的方法论贡献，在 VLA 分析文献中具有参考价值。

---

## Weaknesses（当前版本）

**W1 [Acknowledged limitation]. 无 behavioral validation**: 对 CoRL 是 inherent scope limitation，但论文已在 Limitations 显式承认并在 Predictions 提出可验证假设。不再是 hidden weakness。

**W2 [Structural]. 单模型 + 单 benchmark**: OpenVLA-7B on LIBERO only。论文通过 LIBERO-Spatial cross-benchmark replication 和 model-specific qualifiers 缓解。

**W3 [Minor]. N=10 random subsets**: Ablation 的 random-subset control 统计功效有限。不影响核心 findings 但限制了 z-test 的 precision。

---

## Overall Assessment

**评分: 6.5-7/10 — Borderline Accept**

| Criterion | Round 7 | Round 8 | 变化 |
|-----------|---------|---------|------|
| Novelty | 5/10 | 5.5/10 | Predictions 段增加科学价值 |
| Soundness | 6/10 | 7/10 | Discussion 逻辑一致性修复 |
| Significance | 4/10 | 5/10 | Limitations 诚实 + Predictions falsifiable |
| Clarity | 6/10 | 7/10 | 全文 claim-evidence 匹配 |
| Completeness | 5/10 | 6.5/10 | CKA 正文讨论 + conclusion 编译 |
| **Overall** | **5.5/10** | **6.5-7/10** | **↑ 1-1.5 分** |

**论文从 Round 1 (4.5/10) → Round 7 (5.5/10) → Round 8 (6.5-7/10) 的改善轨迹是持续且实质的。**

R1 (7/10) 认为方法论 internal consistency 修复将论文推过 acceptance bar，剩余问题均为 acknowledged scope limitations。R2 (6.5/10) 认同修复质量但对 CoRL venue fitness 更保守——单模型 representational analysis 无 behavioral validation 在 robotics 会议面临天然劣势。

**核心共识**: 论文在方法论 rigor 和 transparency 上已达到 CoRL acceptable 水准。Structural limitations 是 inherent scope choice，已被诚实承认，不构成方法论缺陷。

**如果提交 CoRL 2026**:
- 建议在提交前完成 4 个 INFO 级 polishing items（总计 ~30 分钟工作量）
- 如能在 deadline 前获得哪怕 1-2 个 task 的 closed-loop success rate，将大幅增强 significance（但非 required）
- 当前版本提交的预期评分区间: 5-7/10（取决于 AC 对分析论文的态度）

---

## Issue Tracker 同步状态

- **本轮 RESOLVED**: R6-C4, R6-C1, R6-C3, R7-W1, R7-W2, R7-W3, R5-N4, R4-I1 (共 8 个)
- **CRITICAL open**: 0
- **WARNING open**: 0
- **INFO open**: R8-I1, R8-I2, R8-I3, R8-I4 (共 4 个, 均为 polishing)
- **完整 issue tracker**: `projects/vla-ssd/artifacts/review_issues.yaml`

---

*Reviewed by: R1 (方法/实验), R2 (新颖性/完整性). Cross-responses completed by both reviewers with full consensus on all factual judgments. Score divergence (7 vs 6.5) reflects venue fitness calibration, not substantive disagreement.*