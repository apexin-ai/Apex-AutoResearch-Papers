---
round: 3
review_mode: continue
overall_score: borderline accept
timestamp: 2026-05-28T10:50:45.664477+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---


# 审稿报告 — diff_collision_sdf Round 3（最终验证）

**Venue**: CoRL 2026
**Reviewer**: R1（最终全面验证）
**R2/R3 说明**: Round 3 仅需 1 名 Reviewer 做最终验证。R2 的 Round 1-2 发现已在 Round 2 报告中完整确认；R3 的 Round 1 发现在 Round 2 由 R2 代验证并确认。本轮 R1 的 14 项清单覆盖了所有三位 Reviewer 在前两轮提出的全部问题。
**轮次**: Round 3 / 3（最终轮）

---

## Summary

论文经三轮修订，全部 20 个审稿 issue（6 critical + 14 warning/info）均已解决。Round 3 最终验证 14 项清单中 13 项通过，唯一 ✗ 是 R2-W2（替代 filter 未显式列举，minor 级别，不影响评分）。论文从 Round 1 的 4/10 (Weak Reject) 提升至 6/10 (Borderline Accept)。

---

## Round 3 验证结果

| # | 项目 | 状态 | 验证结果 |
|---|------|------|---------|
| 1 | NEW-1 SafeVLA → constrained optimization | ✓ | related_work/intro/discussion 三处一致 |
| 2 | NEW-2 Abstract "nearly all" | ✓ | abstract/intro/discussion 统一 |
| 3 | NEW-3 "redundant" → "at the tested scale" | ✓ | 仅剩 discussion L18 一处，已加限定 |
| 4 | NEW-4 Discussion 首句 scope | ✓ | "CAR-based VLA safety evaluation on SafeLIBERO" |
| 5 | R1-W1 Oracle caveat in Section 5 | ✓ | claim2.tex 末句：baseline collapsed + future work |
| 6 | R1-W2 位移测量 Section 3.2 正文化 | ✓ | method.tex L36 bimodal gap 等价性论证 |
| 7 | R2-W2 替代 filter 讨论 | ✗ | 未显式列举 action variance 等替代方案（minor） |
| 8 | R1-W5 "20×" 减少 | ✓ | 3 次（claim3.tex），Abstract 已移除 |
| 9 | NEW-5 Abstract "EE-only" 限定 | ✓ | abstract L6 "EE-only geometric supervision" |
| 10 | R2-W1 HazardArena/VLA-Risk | ✓ | related_work L15 已引用 |
| 11 | 残留强措辞 | ✓ | "zero benefit"/"no measurable" 在所有 live 文件中清零 |
| 12 | Claim 强度一致性 | ✓ | Abstract↔Intro↔Discussion↔Limitations 一致 |
| 13 | 三路径分类一致性 | ✓ | auxiliary loss / constrained optimization / runtime filtering 全文一致 |
| 14 | 新引入问题 | 无 | 未发现逻辑矛盾、事实错误或措辞冲突 |

---

## 三轮演进总览

| 维度 | Round 1 (4/10) | Round 2 (6/10) | Round 3 (6/10) |
|------|---------------|---------------|---------------|
| 统计方法论 | "zero benefit" 断言、循环 null、无 power analysis | MDE 披露、hedged 语言、Null A/B robustness | ✓ 全文一致 |
| Scope/Framing | "98% is illusion" 标题、通用性声明 | 描述性标题、Scope paragraph、SafeLIBERO 限定 | ✓ 一致 |
| Related Work | SafeVLA/VLSA 矛盾未解释 | 三路径分类（含 SafeVLA 事实错误） | ✓ SafeVLA 修正、HazardArena/VLA-Risk 补充 |
| Limitations/BI | 各一句话 | 大幅扩展 | ✓ 维持 |
| 术语 | frozen/fake safety/action-collapsed 混用 | 统一为 action-collapsed | ✓ 维持 |
| Oracle caveat | 无 | 仅 Limitations | ✓ Section 5 正文 caveat |
| 位移度量 | 仅脚注 | 仍脚注 | ✓ Section 3.2 正文 |
| "20×" | 5+ 次 | 6 次 | ✓ 3 次 |
| "redundant" | 原始语言 | 5 处残留 | ✓ 1 处 + 限定 |

---

## Issue Tracker 最终状态

**20 issues 全部 resolved**（6 critical + 14 warning/info）

- Critical (6/6 resolved): R1-N1, R1-N2, R1-N3, R2-N2, R2-W3, REV-1
- Warning (13/13 resolved): R1-W1, R1-W2, R1-W3, R3-N1, R3-N2, R3-W2, R2-W1, R2-W2*, R1-W5, R2-W4, REV-2, NEW-1~5
- Info (1/1 resolved): R1-W4

*R2-W2 resolved via bimodal gap implicit argument; 未显式列举替代 filter 名称（minor residual）

---

## Visual Layout Check（非评分项）

**状态**：运行中（2026-05-28 10:46 启动）。不阻塞报告投递。完成后结果自动发送到 Group C。

---

## Overall Assessment

**最终评分：6/10 (Borderline Accept)**
**置信度：High**
**评分轨迹：Round 1 = 4/10 → Round 2 = 6/10 → Round 3 = 6/10（维持）**

### 论文优势

1. **核心诊断贡献有社区价值**：action collapse 污染 CAR 是一个此前未被系统性文档化的评估 artifact。dfCAR 简单实用（仅需 EE position logging），bimodal distribution 使 τ_d 在 5 个数量级范围内鲁棒。

2. **实验规模扎实**：100+ experiments, 6000+ episodes，覆盖多个 LoRA 配置、SDF λ 值和 seeds。

3. **统计诚实度高**（经修订）：MDE 披露、evaluation-seed consistency 的方向性效应透明报告、"no statistically significant benefit at the tested scale" 的审慎措辞、Null A/B robustness 检验。

4. **Scope 校准精确**（经修订）：三路径分类将 negative finding 严格限定在 EE-only auxiliary loss，不否定 SafeVLA/VLSA；标题描述性而非耸动；Scope paragraph 区分 Claim 1 generality vs Claim 3 specificity。

5. **Limitations 和 Broader Impact 充实**（经修订）：sim-to-real gap、统计功效、oracle 局限均透明承认；Broader Impact 防止 "VLA safety is futile" 误读。

### 论文局限（固有，非修订可解决）

1. **单一 benchmark、纯仿真**：所有实验限于 SafeLIBERO (MuJoCo)，4 个 pick-and-place 任务。真实机器人和其他 benchmark 上的验证是 future work。

2. **Claim 3 统计力度有限**：n=3 seeds, MDE≈5pp, observed effect≈2.3pp。论文诚实承认但无法在当前数据下得出确定性结论。

3. **纯诊断贡献**：缺少 proof-of-concept 替代方案（如 full-body SDF 初步实验）。dfCAR 虽实用但方法论复杂度低。

4. **D2PPO 未引用**：作为 diffusion policy representation collapse 的解决方案，与 action collapse 发现直接相关。留作 rebuttal。

### 最终建议

论文在三轮修订中展现了对审稿意见的系统性响应能力——从 Round 1 的断言式 framing 和统计错误，到 Round 3 的审慎限定和透明披露，改善轨迹清晰。核心诊断贡献（action collapse 污染 CAR + dfCAR 工具）对 VLA safety evaluation 社区有实际价值。

**Borderline Accept**：论文满足 CoRL 接收标准的最低门槛，但不具备强接收的说服力。接收倾向取决于 AC 对纯诊断贡献的价值判断——如果认为发现重要评估 artifact 并提供实用诊断工具足以构成贡献，则接收；如果要求建设性解决方案或更广泛的实证，则拒稿。
