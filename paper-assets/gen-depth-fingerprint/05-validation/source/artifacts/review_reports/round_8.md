---
round: 8
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-17T13:45:12.309758+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告（修订评估）

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**目标 venue**: EMNLP 2026 ARR (Long Paper)
**审稿轮次**: Round 9（基于 Round 8 修订的 continuation review）
**Reviewer**: R1 (方法/实验严谨性), R2 (新颖性/完整性)
**交叉分享**: 完成，强共识

---

## Summary

本轮评估 Round 8 报告中全部 open/in_progress issue 的修复情况，以及一个新的 framing 变更（Contribution 3 恢复为正式贡献）。Round 8 的所有技术性、一致性、准确性问题均已修复，论文在实验可信度和叙事一致性上达到投稿标准。唯一残留争议是 Contribution 3 的 claim scope。

---

## Round 8 Issue 修订状态

### 已解决（6/7）— 两位 Reviewer 一致确认

| Issue | 修复验证 |
|-------|---------|
| R1-W1 (method.tex vs Table 4 超参) — 原 BLOCKING | method.tex L76 和 Table 4 caption 均写 "identical hyperparameters (200/6)"。完全一致 ✓ |
| R7-W1/R8-N2 (Abstract binary F1) | Abstract L7 同时报告 3-class 和 binary F1，数字与 Table 1 一致 ✓ |
| R7-M1 ("strong"→"substantial") | method.tex L62、Figure 1 caption、results.tex L61 三处均为 "substantial" ✓ |
| R8-N1 (entropy_std 分组) | method.tex (moderate drift)、Figure 1 caption (intermediate)、Discussion (borderline case) 全文一致 ✓ |
| R8-RV1 (虚构 R²=0.082) | 替换为 ρ=-0.286（R1 从源文件确认）✓ |
| R8-RV2 (LOFO delta) | results.tex L14 确认 Δ=-0.8pp，数学验证通过 (0.694-0.686=0.008) ✓ |

### 部分解决（1/7）

| Issue | 状态 |
|-------|------|
| R7-M2 (bib orphans + author) | 旧 orphans 已删。dolma/fineweb 仍在 bib 中但 tex 中无引用（R1 确认源文件中无 \cite{dolma} 或 \cite{fineweb}）。Author 字段为 arXiv 官方署名，可接受。Minor。 |

---

## Round 9 新发现

### R9-N1 [warning]: Contribution 3 恢复为 "Detectable ≠ harmful" — overclaim

**两位 Reviewer 一致认定为 overclaim。**

Round 8 中双方共识：Contribution 3 应从 enumerate 移为散文句。本轮作者恢复为正式编号贡献，标题改为 "Detectable ≠ harmful"。无新实验支撑。

**问题核心**：

| Claim scope | Evidence coverage |
|---|---|
| "harmful"（泛称） | 仅测 perplexity |
| "training utility" | 仅 1 model (OLMo-2-0425-1B) |
| "decoupling"（因果性措辞） | 仅 observational equivalence |
| "downstream harm"（Abstract） | 未测 benchmark, toxicity, factuality |

Abstract L8 写 "decoupling detectability from downstream harm" 但无 "perplexity" 限定；Conclusion L5 有 "as measured by perplexity" 限定——不一致。

**Reviewer 建议**：
- 选项 A（首选）：恢复为散文句（回到 Round 8 共识）
- 选项 B（可接受）：保留为编号贡献但标题限定为 "Detectable drift ≠ perplexity harm"，Abstract L8 加 "as measured by perplexity"

### R2 NEW-1 事实核查结果：binary F1 差距 — 不成立

R2 声称 Table 4 中 binary F1 差距为 8.8pp（7-feature 0.700 vs 4-det+surface 0.788）。

**经 Director 和 R1 双重验证**，results.tex 源文件数据为：
- 4-det+surface: Bin F1 = **0.708**
- 7-feature: Bin F1 = **0.705**
- 差距 = **0.3pp**

R2 的 0.788 在源文件中不存在。R2 混淆了表格行或读取了不同版本的 PDF。Section 4.3 文本 "statistically indistinguishable (≤0.3pp)" 与源文件完全一致。**论文不存在选择性报告问题。**

---

## Strengths

1. **全部技术性问题彻底解决**: Round 8 的 blocking issue（method.tex 矛盾）和所有一致性问题均已修复，论文实验可信度完整
2. **指标报告体系规范**: Abstract 双指标、Table 1 primary metric 声明、gen-0 overlap 讨论形成完整闭环
3. **DDR 叙事成熟**: "tendency not guarantee" + entropy_std borderline case + sampling ablation acknowledgement 构成审慎、可信的机制解释
4. **实验控制全面**: 8 generators / 5 families / LOGO+LOFO / length matching / cross-model chains / prompt-type ablation / domain generalization
5. **efficiency 定位清晰**: 2.4× faster / 3.2× less memory 作为 trade-off 而非 superiority claim
6. **TOST 等价检验**: downstream 负结论有适当统计支撑

## Weaknesses

1. **Contribution 3 overclaim** (Should-Fix): "Detectable ≠ harmful" 的 evidence scope 不足以支撑 "harmful" 的泛化语义。这是当前版本唯一的方法论问题，但属于 framing 而非 experimental flaw，可快速修复。
2. **方法新颖性有限** (Structural): 7 个已知特征 + XGBoost，无算法创新。DDR 是经验观察。这是论文的结构性上限，无法通过修订解决。
3. **dolma/fineweb bib orphans** (Minor): 简单清理。

## Questions for Authors

1. Contribution 3 的 "harmful" 是否可以限定为 "perplexity-harmful"？当前 evidence 仅覆盖 perplexity，"harmful" 涵盖的 toxicity/factuality/diversity 维度均未测试。
2. dolma 和 fineweb 是否应在 Introduction 中引用（作为 pretraining corpora 实例），或从 bib 中删除？

---

## Overall Assessment

### 评分

| Reviewer | R8 Score | R9 Score | 变化理由 |
|----------|----------|----------|---------|
| R1 | 3.5 | **3.5** | 维持。所有技术修复确认；Contribution 3 是可修复的 framing 问题。 |
| R2 | 3.0 | **3.0** | 维持。但 R2 的一个扣分理由（binary F1 选择性报告）经核查不成立。R2 表示若 Contribution 3 修复则可上调至 3.5。 |

### Director 综合评分: **3.5/5 (Borderline Conference)**

**从 Round 8 的 3.0 上调至 3.5，理由：**

1. **Round 8 blocking issue 完全解决**: method.tex 与 Table 4 超参一致性、Abstract 指标报告、术语统一、entropy_std 分组、虚构数据替换——所有技术性问题清零。论文实验可信度不再有任何质疑。

2. **R2 的 NEW-1 不成立**: R2 维持 3.0 的两个理由中，"binary F1 选择性报告"经核查为事实错误（实际差距 0.3pp，非 8.8pp）。移除此因素后，R2 维持 3.0 的唯一理由是 Contribution 3 overclaim——而 R2 自己表示修复后可上调至 3.5。

3. **Contribution 3 是 framing 问题非 experimental flaw**: 两位 Reviewer 均确认实验本身有效（TOST 正确），问题仅在于 claim 标题的 scope 超出 evidence。将 "harmful" 限定为 "perplexity harm" 是 ≤30 分钟的文本修改，不应将论文评分锁定在 Findings。

4. **论文的实际贡献清晰**: (a) 新任务定义（ordinal depth estimation），(b) 系统性 empirical characterization（DDR），(c) 高效 single-reference approach。即使方法新颖性有限，这些在 EMNLP Findings-Conference 边界是合理贡献。

### ARR 维度评分

| 维度 | 评分 | 说明 |
|------|------|------|
| Soundness | 4.0 | 所有技术问题已清零；实验方法论严谨（统一超参、TOST、LOGO/LOFO、length matching）|
| Excitement | 2.5-3.0 | 新任务 + DDR finding 有价值，但方法层面无创新；base-model-only 限制范围 |
| Reproducibility | 4.0 | 超参、数据规模、统计检验完整报告；代码承诺发布 |
| Confidence | 4.0 | 两位 Reviewer 完整审读 + 交叉分享达成强共识 |

### 必须修复项（投稿前）

1. **Contribution 3 framing**: 选项 A（散文句）或选项 B（限定标题 + Abstract 加 "as measured by perplexity"）
2. **dolma/fineweb**: 删除 bib 条目或恢复 Introduction 引用

### 推荐

**Borderline Conference / Strong Findings**。修复 Contribution 3 framing 后，论文在 Soundness 和 Reproducibility 维度达到 Conference 标准；Excitement 维度因方法新颖性有限而处于 Findings-Conference 边界。最终接收层级取决于 AC 对 empirical contribution paper 的态度和该 cycle 的竞争强度。

与 Round 8 对比：论文质量有实质提升——所有技术性问题清零，唯一残留问题是一个可快速修复的 framing 选择。