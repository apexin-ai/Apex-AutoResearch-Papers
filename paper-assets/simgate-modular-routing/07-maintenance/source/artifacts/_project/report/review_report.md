# 论文初稿一致性审查报告

**日期**: 2026-05-14  
**目标会议**: EMNLP 2026 ARR short paper (4 pages + references)  
**审查范围**: abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, references.bib

---

## 🔴 Critical（必须修复才能提交）

### C1. Logit/Generation 准确率来自不同实验，但论文暗示同一模型

**位置**: experiments.tex §4.4 (Router Training as Diagnostic), 第 53–54 行附近

**问题**: 论文写道：

> "At the logit level, routing patterns emerge: accuracy reaches 74.5% with balanced accuracy of 79%"
> "At the generation level, however, accuracy drops to 65.36% with internal recall of 51.5%"

"drops to" 的措辞暗示这是同一模型在 logit/generation 两种评估方式下的表现。但实际上：

- **74.5% logit accuracy** 来自 `plan-004-v5`（GA=1, seed=42）
- **65.36% generation accuracy** 来自 `plan-004-ablation-b`（GA=8, seed=42）

这是两个不同训练配置的模型。单一模型的真实数据：

| 配置 | Logit Acc | Gen Acc | Logit-Gen Gap |
|------|-----------|---------|---------------|
| v5 (GA=1) | 74.5% | **53.3%** | 21.2pp |
| ablation-b (GA=8) | 65.4% | **65.4%** | **0** |

v5 (GA=1) 的 generation 实际是 53.3%（degenerate, internal recall 仅 26.7%），远低于论文报告的 65.36%。ablation-b (GA=8) 根本没有 logit-generation gap。

论文混合两个不同实验的最优数字，制造了一个不存在的"中等 gap"（74.5%→65.4%），实际上要么 gap 巨大（v5: 74.5%→53.3%），要么不存在（ablation-b: 65.4%→65.4%）。

**影响**: 数据诚信问题。Reviewer 交叉检查会发现。registry 中 v5 的 notes 明确写道 "Generation-based routing eval 推翻了此前 logit-level 的 success 结论"。

**建议修复**: 分配置报告，例如：

> "With gradient accumulation of 8, the implicit router achieves 65.4% accuracy at both logit and generation levels with 51.5% internal recall—no logit-generation gap. With gradient accumulation of 1, logit-level accuracy rises to 74.5% (balanced accuracy 79%), demonstrating that the counterfactual labels encode learnable structure, but generation degenerates to 53.3% accuracy (internal recall 26.7%). The best logit-level patterns do not transfer to generation under small effective batch size."

同时需要修改 introduction.tex 贡献 C2 中引用的 "logit accuracy 74.5%, balanced accuracy 79%" 相关描述，说明这是 GA=1 的 logit-level 上界。

---

### C2. 缺少 main.tex — 无法编译

**问题**: 没有顶层 LaTeX wrapper 文件（`main.tex` 或 `paper.tex`），缺少 `\documentclass`、`\begin{document}`、`\input{}`/`\include{}` 指令、以及 `\bibliography{references}` 引用。

**建议**: 创建 `main.tex`，使用 ACL 2023 模板（ARR 通用），`\input` 各 section 文件。

---

### C3. Figure 引用悬空 — `\ref{fig:decomposition}` 无对应 figure

**位置**: experiments.tex 第 12 行

> "as shown in Figure~\ref{fig:decomposition}"

**问题**: 没有任何文件定义 `\label{fig:decomposition}`，也没有对应的图片文件。编译时会产生 "undefined reference" 警告，PDF 显示 **??**。

paper_framing.md 规划了 Figure 1 (Death Decomposition 图) 和 Figure 2 (Correlation scatter plot)，均未创建。

**建议**: 
- 绘制 scatter plot：x 轴 = per-task death rate differential (internal − deterministic), y 轴 = Δ_full，11 个点 + 回归线 + r/p 标注
- 或者改为引用 Table 形式展示 per-task 分解结果

---

### C4. 页数大概率超限

**估算**:
| Section | 估算页数 |
|---------|---------|
| Abstract | ~0.2 |
| Introduction | ~0.9（含长 contribution list） |
| Method | ~1.2（4 subsections） |
| Experiments | ~1.8（含 Table + 5 subsections） |
| Related Work | ~0.5 |
| Conclusion | ~0.4（含重复 Limitations + Future Work） |
| **合计** | **~5.0** |

4 页限制下超出约 1 页。即使 Related Work 缩短，仍可能超限。

**建议**:
1. 删除 experiments.tex 中的 Limitations subsection（与 conclusion.tex 重复，见 I1）
2. Method §3.4 (Rule-Based Baseline) 可压缩为 Experiments 中的 1 段
3. Method §3.3 (DAF) 中的数值结果（Δ_full=+29.60 等）移至 Experiments，Method 只留公式定义
4. 加 Figure 后会更挤 — 可能需要将 Figure 作为 Table 的一部分或改为 inline 描述

---

## 🟡 Important（强烈建议修复）

### I1. Limitations 段落重复出现

**位置**: experiments.tex §4.5 (第 62–65 行) 和 conclusion.tex §6 "Limitations" 段 (第 7 行)

**问题**: 两处 Limitations 内容几乎相同，都提到 single benchmark、single LLM backbone、-100 death penalty、episode granularity。4 页 short paper 中这种重复浪费 ~0.15 页。

**建议**: 删除 experiments.tex 中的 §4.5 Limitations，仅保留 conclusion.tex 中的 Limitations 段。

---

### I2. Method 和 Experiments 大量数值重复

**位置**: 
- method.tex §3.3 第 34 行: "Δ_full = +29.60, Δ_no_death = +2.84, yielding DAF = 90.41%"
- method.tex §3.3 第 35 行: "r = 0.9698 (p = 8.12 × 10^{-7})"
- experiments.tex §4.2 第 10–11 行: 相同数字再次出现

Method 应只定义 DAF 公式和分析框架，具体数字应首次出现在 Experiments。当前写法让 Experiments 读起来像是在重述已知结论。

**建议**: Method §3.3 删除最后一段的具体数值（"On 245 episodes across 11 task types..."），替换为 "We report DAF and correlation results in §4.2."

---

### I3. DAgger gap / 分布偏移未讨论

**位置**: 缺失项

**问题**: paper_framing.md 明确列出 "DAgger gap" 为 Anticipated Reviewer Concern #5，要求 "Acknowledge explicitly (cite Ross et al. 2011)"。但论文没有任何提及。Router 训练在 pure-internal / pure-deterministic 轨迹上，但部署时是 mixed-strategy — 这是标准的 off-policy 问题。

**建议**: 在 experiments.tex §4.4 末尾或 Limitations 中添加一句：

> "Our router trains on pure-strategy trajectories but deploys in a mixed-strategy setting, introducing distribution shift (Ross et al., 2011). The episode-level label granularity partially mitigates this by avoiding per-step tie-breaking artifacts, but trajectory-level differences remain."

需要在 references.bib 中添加 Ross et al. 2011 (DAgger)。

---

### I4. references.bib 条目不完整

| 条目 | 问题 |
|------|------|
| `art-2023` | `@article` 但缺少 `journal` 字段 |
| `chameleon-2024` | `@article` 但缺少 `journal` 字段 |
| `dynathink-2025` | author = "Anonymous" — 匿名论文引用可能引起 reviewer 质疑 |
| `envsimbench-2026` | author = "Anonymous"，无 arXiv ID，无 journal — 条目最不完整 |

**建议**: 
- `art-2023`: 补充 `journal = {arXiv preprint arXiv:2303.09014}` 或正确会议信息
- `chameleon-2024`: 补充 `journal = {arXiv preprint arXiv:2304.09842}` 或正确会议信息
- `dynathink-2025` 和 `envsimbench-2026`: 补充 arXiv ID；如果仍在匿名审稿，考虑是否必须引用或用 "Anonymous" + 年份格式

---

### I5. 96.2% oracle match rate 可能是 96.3%

**位置**: introduction.tex 第 7 行, experiments.tex 第 43 行

**计算**: 如果 oracle 在 no_preference 时默认选 deterministic，则 oracle 选择 deterministic 的比例 = (86 det_preferred + 150 no_preference) / 245 = 236/245 = **96.33%**，四舍五入 96.3%，而非论文中的 96.2%。

**可能原因**: oracle 实现中对某些 no_preference episode 的处理与默认不同，或小数点截断。

**建议**: 确认 eval_end_to_end.py 中 oracle 的具体实现逻辑，如果确实是 96.3% 则统一修正。

---

### I6. 98.2% tie rate 缺乏 registry 实验支撑

**位置**: abstract.tex 第 2 行, introduction.tex 第 5 行, method.tex 第 6 行, conclusion.tex 第 3 行

**问题**: "98.2% of steps produce identical scores regardless of modality" 在 4 个 section 中重复出现，但 registry 中没有任何实验记录这个数字的来源。硬约束要求 "所有定量 claim 必须有 registry 中的 experiment 支撑"。

**建议**: 确认 98.2% 的数据来源并在 registry 中补录，或在论文中说明计算方式（如："across N steps from M episodes, N×0.982 steps produced identical intermediate scores"）。

---

## 🟢 Minor（可选优化）

### M1. Abstract 信息密度过高

Abstract 仅 2 句话，但包含 Δ_full、Δ_no_death、DAF、r、p 五个数值 + 百分比 + episode 数。对不了解 ScienceWorld 的 reviewer，第一次阅读认知负担较大。

**建议**: 考虑删减 r/p 值到正文，abstract 保留核心发现（DAF ~90%）和方法论关键词。

---

### M2. Introduction 贡献列表中 C2 混入 router 训练细节

**位置**: introduction.tex 第 12 行

贡献 C2 主体是 "Death avoidance dominates routing signal"，但末尾添加了 router 训练作为诊断探针的详细数字（logit accuracy 74.5% 等）。这让 C2 承载了两个不同层面的贡献。

**建议**: router diagnostic 可简化为 "Router training as a diagnostic probe confirms that the counterfactual labels encode learnable patterns beyond majority-class prediction (§4.4)"，具体数字留在 Experiments。（同时也能回避 C1 中 logit/generation 混源问题。）

---

### M3. -100 死亡惩罚对泛化性的影响讨论不充分

**位置**: experiments.tex §4.5, conclusion.tex Limitations

两处都只说 "ScienceWorld's severe -100 death penalty may amplify the death avoidance signal"，但没有定量分析。例如：如果死亡惩罚改为 -10，DAF 会如何变化？

**建议**: 可加一句定性讨论，如 "Under a less severe penalty (e.g., -10), the DAF would mechanically decrease as death-related score gaps shrink, but the qualitative finding—death avoidance as the primary routing mechanism—would persist as long as death rate asymmetry remains."

---

### M4. Related Work 对 CogRouter 的数字引用缺乏可比性说明

**位置**: related_work.tex 第 11 行

> "CogRouter achieves 82.3% on ScienceWorld"

论文自己的 Table 1 报告的是 raw score（-10.70 等），而 CogRouter 的 82.3% 是 success rate 或 normalized score。不同 metric 直接并列容易误导。

**建议**: 加注 "(success rate, different evaluation protocol)" 或删除具体数字，只说 "CogRouter achieves strong performance on ScienceWorld by routing among cognitive depth levels."

---

### M5. Conclusion 中 Future Work 可删减以节省空间

**位置**: conclusion.tex 第 9 行

"Step-level counterfactual labeling..." 和 "Extension to code-interpreter routing..." 各占一句。在页数紧张的情况下，可压缩为半句：

> "Extensions include step-level labeling with denser rewards and code-interpreter routing (e.g., MATH)."

---

## 缺失项清单

| 缺失项 | 优先级 | 说明 |
|--------|--------|------|
| `main.tex` | 🔴 | 无法编译 |
| Figure 1 (Death Decomposition scatter plot) | 🔴 | `\ref{fig:decomposition}` 悬空 |
| Figure 2 (Correlation scatter plot) | 🟡 | paper_framing.md 规划但未创建；可与 Figure 1 合并 |
| Ross et al. 2011 bib entry | 🟡 | DAgger 引用 |
| 98.2% tie rate registry 记录 | 🟡 | 定量 claim 需实验支撑 |

## Framing 一致性检查（Option B: 方法论贡献）

✅ 无 "成功训练 router" 或 "首个非退化 router" 等表述  
✅ Router 训练一致定位为 "diagnostic probe"  
✅ 不声称 selective routing > unconditional deterministic  
✅ 贡献定位为 empirical finding + diagnostic methodology  

## 强度词审计

| 词 | 出现位置 | 是否合理 |
|----|---------|---------|
| "significantly" | experiments.tex 第 58 行 "did not significantly outperform" | ✅ 统计意义（CI 重叠） |
| "consistent" | experiments.tex 第 12 行 "This concentration is consistent across task types" | ✅ r=0.9698 支撑 |
| "near-equivalent" | experiments.tex 第 19 行 | ✅ Δ_no_death=+2.84 支撑 |
| "nearly sufficient" | method.tex 第 35 行, experiments.tex 第 12 行 | ✅ r=0.97 接近 1 |
| "dramatically" | 未出现 | — |
| "novel" | 未出现 | — |
| "consistently" | 未出现（用了 "consistent"） | — |

## 数字一致性交叉验证

所有核心数字在各 section 间一致，且与 registry 匹配：

| 数字 | Abstract | Intro | Method | Experiments | Conclusion | Registry |
|------|----------|-------|--------|-------------|------------|----------|
| Δ_full=+29.60 | ✅ | ✅ | ✅ | ✅ | ✅ | plan-012-full ✅ |
| Δ_nd=+2.84 | ✅ | ✅ | ✅ | ✅ | ✅ | plan-012-full ✅ |
| DAF=90.41% | ✅ | ✅ | ✅ | ✅ | ✅ | plan-012-full ✅ |
| r=0.9698 | ✅ | ✅ | ✅ | ✅ | ✅ | plan-012-full ✅ |
| p=8.12e-7 | ✅ | ✅ | ✅ | ✅ | ✅ | plan-012-full ✅ |
| 11 tasks / 245 eps | ✅ | ✅ | ✅ | ✅ | ✅ | plan-012-full ✅ |
| Trained Router=-10.70 | — | — | — | Table 1 ✅ | — | plan-003-e2e-ablation-b-correct ✅ |
| Always-Det=-9.47 | — | — | — | Table 1 ✅ | — | plan-003-eval-implicit ✅ |
| Death 42.9%/16.3% | — | ✅ | — | ✅ | — | plan-012-full ✅ |
| Labels 86/9/150 | — | ✅ | ✅ | ✅ | — | plan-012-full ✅ |

**唯一例外**: logit 74.5% / generation 65.36% 来自不同实验（见 C1）。
