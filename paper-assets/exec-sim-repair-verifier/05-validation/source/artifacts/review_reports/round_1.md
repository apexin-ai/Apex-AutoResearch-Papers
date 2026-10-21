---
round: 1
review_mode: 
overall_score: borderline
timestamp: 2026-05-18T18:22:14.404222+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 2（修订版论文）

**论文**: The Formulation Design Space for Execution-Free Code Verification: A Controlled Empirical Study
**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**截止日期**: 2026-05-25
**Reviewer**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作）
**圆桌模式**: Round 2 独立审稿 → Step 2 交叉分享 → Step 3 收敛判定（1 轮收敛）
**注意**: 本报告覆盖修订版论文，是对 Round 1 报告（Overall 2.5/5 Weak Reject）的更新。

---

## 修订版 vs Round 1 变化概要

论文从 Round 1 进行了大幅修订：
- **标题**：从 advocacy ("Classification Scales Where Generation Stalls") 改为中性 ("The Formulation Design Space...")
- **新实验**：DeepSeek-Coder 跨模型验证、CWM 8B repo-level (65.17%)、LoRA rank 32 消融、relaxed matching 消融（反直觉降低 CWM）、匹配上下文消融（98% gap 来自 formulation）、TOST sensitivity 分析（±1/±2/±3pp）、0-shot/3-shot baselines、re-repair pilot (n=44, p=0.42 负结果)
- **引用**：26 → 47 条，补充 LEVER/CodeT/Andrews/Just 等
- **Framing**：从 "CLS is superior" 转为 "formulation × model × complexity interaction"
- **Claim 校准**：条件性表述、abstract 用 19-26pp 范围、负结果诚实报告

Round 1 的 17 个 issue 中 **12 个已 resolved**，3 个 in_progress，2 个演化为 Round 2 新问题。

---

## Summary

本文系统比较 execution-free 代码修复验证的三种 formulation（CLS/CWM/TRAJ），跨两个模型家族（Qwen3, DeepSeek-Coder）、两个复杂度层级（function/repo），使用受控实验设计。核心发现：函数级三种 formulation 近似等效（5 seeds × 2 model families）；仓库级 CWM 大幅退化（19-26pp），方向 formulation-inherent，幅度 model-contingent。修订版通过消融实验系统封堵了 LoRA capacity、exact matching penalty、input context disparity 三个替代解释。

---

## Strengths（Round 2 共识）

**S1. Framing 根本性改善（R1-S1, R2-S1, 共识）。** 从 advocacy 转为中性 design space study。每个 claim 以条件性表述限定范围。Abstract 用 "19-26pp" 范围替代单点 "25.59pp"。科学姿态与证据强度匹配。

**S2. DeepSeek 跨模型验证——最重要的实质性改进（R1-S2, R2-S2, 共识）。** Table 1 中 DeepSeek-Coder-6.7B 的三 formulation 结果独立确认函数级等价性。Repo-level degradation pattern 跨模型一致方向（CWM 退化）支持 "formulation-inherent direction, model-contingent magnitude"。从单模型观察提升为初步 generalizable finding。

**S3. 消融实验系统封堵替代解释（R1-S3, R2-S3, 共识）。** (1) LoRA rank 32 排除 capacity bottleneck；(2) Relaxed matching 反降 CWM 准确率（反直觉，排除 exact match penalty）；(3) 匹配上下文消融 98% gap 来自 formulation（排除 input context disparity）。三组消融共同收窄因果解释空间。

**S4. TOST sensitivity 分析（R1-S4, R2-S4, 共识）。** 三档 margin (±1/±2/±3pp) + minimum margin 1.63pp + deployment-significance 论证。直接回应 Round 1 质疑。

**S5. 负结果诚实报告（R1-S5, R2-S1, 共识）。** Re-repair pilot 负结果、majority voting 失败、CWM 8B parseable<4B、relaxed matching 更差。增强论文可信度和信息密度。

**S6. 全面覆盖和报告质量（R1-S6, R2-S6, 共识）。** 47 references、Appendix hyperparameter/mutation distribution tables、0-shot/3-shot baselines、217× throughput benchmark。Reproducibility 显著提高。

---

## Weaknesses

### Critical（影响接收决定）

**[C1] Table 6 核心结果表含 TBD/preliminary 条目。（R1-W1 + R2-W1/W3, 完全一致）**
Qwen3 TRAJ repo-level "TBD"，DeepSeek CWM "~60 preliminary"。投稿论文核心表格的 TBD 是审稿红旗。
- **Asymmetric risk**：若 Qwen3 TRAJ repo-level 强于 CLS（如 DeepSeek TRAJ 75.35% > CLS 74.93%），论文 contribution ranking 需重大调整。
- **Preliminary → 确定性 claim**：Section 4.6 用 "confirms formulation-inherent divergence" 修饰 preliminary data。
- **要求**：完成所有 TBD 实验后再提交。若 deadline 前无法完成，在 abstract 和 Table caption 系统标注 final/preliminary 状态。

**[C2] DeepSeek CLS (74.93%) ≤ TRAJ (75.35±5.00) at repo-level，Contribution 4 scope 实质缩窄。（R1-W2, R2 AGREE "R1独有重要发现"）**
C4 声称 "per-test diagnostic granularity at equivalent trajectory-level accuracy"。但 DeepSeek repo-level 显示 CLS 不优于 TRAJ（甚至略低）。论文回避了此比较。
- C4 scope 从 "跨条件通用" 缩窄为 "Qwen3 函数级"。
- 叠加 re-repair 负结果 (C3)，per-test granularity 实际价值薄弱。
- **要求**：(1) Section 4.6 增加 DeepSeek CLS vs TRAJ 明确比较和讨论；(2) C4 限定适用范围。

**[C3] Re-repair 负结果 (n=44, p=0.42) 低调处理，实质削弱 C4 下游 utility。（R1-W3 + R2-W6, 完全一致）**
Introduction 多次以 "targeted re-repair" 作为 motivation，但 pilot 负结果仅 Conclusion Future Work 单句。C4 混合 trivially true 的 throughput claim (217×) 和 unvalidated 的 utility claim。
- **要求**：(1) 提升负结果到 main text，报告实验细节（agent、format、power analysis）；(2) C4 拆分为 efficiency (formulation-inherent) 和 diagnostic utility (unvalidated)。

**[C4] 单 seed repo-level 同尺寸对比仍未实质解决。（Round 1 遗留, R1+R2 一致）**
Abstract 改用 19-26pp 范围（改进），但 Table 6 中 Qwen3 4B-4B 仍为 seed 42 单点。CLS 4B s123=75.33% 仅在 Limitations 披露。CWM 8B 也是单 seed。从 Round 1 到 Round 2 此问题未实质改善。

### Warning（应修复）

**[W1] TRAJ 训练配置与 CLS/CWM 不完全受控。（R1-W4, R2 AGREE "R1独有重要观察"）**
TRAJ lr=2×10⁻⁴ (CLS/CWM 5×10⁻⁵)，训练集 ~8K (CLS/CWM 70K)。CLS-TRAJ TOST 等价混淆 formulation effect 和 data volume effect。建议 CLS 降采样 ~8K 消融。

**[W2] DeepSeek TRAJ repo-level ±5pp std (6 seeds) 极端不稳定。（R1-W5, R2 AGREE）**
95% CI 约 [65,86]，跨越 majority baseline (72.96%)。未报告逐 seed 准确率，未分析方差来源。

**[W3] Oracle ICC 层级不匹配。（R2-W5, R1 AGREE "好发现，两轮未识别"）**
Oracle frontier 使用 function-level ICC=0.191，但 repo-level ICC=0.3146 已可用未用。当前估计 conservative（方向不变），但方法论上是 level-of-analysis 错误。应同时报告两种 ICC 下的 oracle 结果。

**[W4] %%SCENARIO-A%% 条件标记未清理。（R1-W6 + R2-W1, 完全一致）**
abstract/intro/experiments/conclusion 中可见。标准 LaTeX 下为注释不影响 PDF，但暗示 work-in-progress。被注释内容可能包含有价值的 robustness 分析。提交前必须清理。

---

## Reviewer Consensus

Round 2 交叉分享中两位 Reviewer 在所有 Weakness 上达成一致。关键新发现：
- R1 新提出 C2（DeepSeek CLS≈TRAJ）和 W1（TRAJ confound）：R2 均 AGREE
- R2 新提出 W3（Oracle ICC 不匹配）：R1 AGREE

---

## Reviewer Divergence

**唯一实质分歧：Overall Score**

| | R1 | R2 |
|---|---|---|
| Soundness | ~3.5/5 | 3.5/5 |
| Excitement | 3/5 | 2.5/5 |
| **Overall** | **4/5 (Weak Accept)** | **3/5 (borderline)** |

R1 理由：conditional on TBD 完成，anti-informative parseable predictions + formulation×model interaction + 反直觉消融超越 "quantifying expected trend"。practitioner 决策价值具体。
R2 理由：Table 6 TBD 是投稿硬伤；C4 scope 被 DeepSeek CLS≈TRAJ + re-repair 负结果大幅缩窄；C2 跨模型 claim 依赖 preliminary 数据。

**两人均推荐 Findings track。**

---

## Questions（汇总）

1. DeepSeek TRAJ 6 seeds 逐个准确率？方差来源？（R1-Q1）
2. DeepSeek CLS < TRAJ at repo-level，C4 scope？（R1-Q2）
3. Re-repair pilot 实验设计细节？n=44 power？（R1-Q3, R2-Q3）
4. CLS/CWM 降采样 ~8K 准确率？（R1-Q4）
5. Table 2 seed 基础 vs bootstrap seed 基础是否一致？（R1-Q5）
6. %%SCENARIO-A%% 在 PDF 中是否可见？（R2-Q1）
7. DeepSeek CWM final results 何时完成？（R2-Q2）
8. CWM 8B parseable acc < 4B 是否 Qwen3-specific？（R2-Q4）
9. ICC=0.191 是否在 DeepSeek 上复现？（R2-Q5）

---

## Round 1 → Round 2 Issue Resolution

| Issue | R1 Status | R2 Status | 综合 |
|---|---|---|---|
| R1-N1 单 seed | in_progress | in_progress | **未解决** |
| R1-N2 CWM 8B | resolved | resolved | **已解决** |
| R1-N3 LoRA rank | resolved | resolved | **已解决** |
| R2-W1 novelty | improved | improved | **改善但未消除** |
| R2-W4 标题 | resolved | resolved | **已解决** |
| R1-W1 TOST margin | resolved | resolved | **已解决** |
| R1-W2 scaling arg | resolved | resolved | **已解决** |
| R1-W3 val-test shift | resolved | resolved | **已解决** |
| R1-W4 relaxed match | resolved | resolved | **已解决** |
| R1-W5 ecology | resolved | resolved | **已解决** |
| R2-W5 re-repair | evolved → C3 | evolved → C3 | **负结果存在但报告不充分** |
| R2-W6 LEVER/CodeT | resolved | resolved | **已解决** |
| R2-W8 引用 | resolved | resolved | **已解决** |
| 5× Info issues | all resolved | all resolved | **全部已解决** |

**Resolution rate: 12/17 (71%) fully resolved, 3 partially addressed, 2 evolved into new issues.**

---

## Overall Assessment

**Overall Score: Borderline (ARR 3 / Findings)**

**综合评分：**

| 维度 | R1 | R2 | 综合 | vs Round 1 |
|------|----|----|------|-----------|
| Soundness | ~3.5/5 | 3.5/5 | **3.5/5** | **+1.0** |
| Excitement | 3/5 | 2.5/5 | **2.75/5** | **+0.75** |
| Overall | 4/5 | 3/5 | **3.5/5** | **+1.0** |
| Confidence | 4/5 | 4/5 | **4/5** | 不变 |

### 核心判断

修订版在方法论严谨性上有实质性进步。消融实验、跨模型验证、TOST sensitivity、负结果报告共同将 Soundness 从 2.5 提升到 3.5。Framing pivot 和 claim 校准使论文的科学姿态与证据匹配。

**仍存在的核心障碍**：

1. **Table 6 不完整**（C1）：核心结果表含 TBD/preliminary 是投稿质量问题。
2. **C4 证据基础薄弱**（C2+C3）：DeepSeek CLS ≤ TRAJ at repo-level + re-repair 负结果 → per-test granularity 的跨条件价值和下游 utility 均未充分验证。
3. **单 seed 未解决**（C4）：4B-4B 同尺寸 repo-level 对比仍为单 seed。
4. **Novelty 有限但有争议**（~0.5 分差距）：两人均认为适合 Findings 而非 Main。

### 建议路径

**推荐**：完成 Table 6 所有 TBD → 根据 TRAJ repo-level 结果调整 C4 → 提升 re-repair 负结果到 main text → 清理 SCENARIO-A → 投 Findings track。

**如果 Qwen3 TRAJ repo-level > CLS**：重构 C4 为 context-dependent formulation choice（CLS for function-level + diagnostic, TRAJ for repo-level robustness）。

**不建议**：当前状态（含 TBD）直接提交。

---

*圆桌审稿 Round 2 完成。论文从 Round 1 的 Weak Reject (2.5/5) 改善为 Borderline Findings (3-3.5/5)。两位 Reviewer 在所有 weakness 上达成共识，唯一分歧为 novelty/overall score (~0.5-1 分)。Issue Tracker 已同步更新（26 issues: 15 resolved, 6 open, 5 in_progress）。*