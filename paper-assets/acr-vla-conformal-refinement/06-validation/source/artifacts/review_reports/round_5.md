---
round: 5
review_mode: continue
overall_score: borderline reject
timestamp: 2026-05-27T15:39:40.285111+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3 (Continue Review)

**论文**: "ACR-VLA: Adaptive Conformal Refinement for Frozen Flow-Matching VLAs"
**目标 venue**: CoRL 2026 Main Conference
**Deadline**: 2026-05-29（距今 2 天）
**审稿模式**: Continue（基于 Round 2 的修订评估）
**Reviewer 编排**: 2 人（R1: 方法/实验/统计严谨性; R2: 新颖性/Related Work/完整性）
**外部审稿**: 未请求
**视觉审查**: 已完成（非评分项）

---

## Round 2 → Round 3 重大改版摘要

论文在 Round 2 至 Round 3 间经历了 **结构性改版**，核心变化：

| 维度 | Round 2 | Round 3 |
|------|---------|---------|
| 标题 | "Correction Over Selection: Dissecting..." | "ACR-VLA: Adaptive Conformal Refinement..." |
| Pipeline | K=10 sample + CRM | K=2 batched + adaptive gating + CRM |
| Baseline 性能 | 11.6% (Object) | 77.7% (Object), 58-83% (全 4 suites) |
| 核心 claim | Correction > Selection | *When* to correct > correction strength |
| Latency | K=10 ~500ms 未量化 | K=2 ~170ms (= K=1), Table 2 量化 |
| 跨 VLA 分析 | 无 | π₀.₅ (3.6B, Section 4.5) + OpenVLA-OFT boundary |
| 效果量 | +6pp (11.6→17.6%) | +1.5/+0.1/+1.3/−0.3 pp |

**Round 2 的 7 个 critical 中 5 个已 resolved/substantially addressed**：latency (Table 2)、绝对性能 (58-83%)、motivation-evaluation disconnect (Intro 重写)、"Dissecting" 标题 (更改)、seed 不平衡 (统一 n=3)。但新版本引入了 **新的核心问题**：效果量缩至噪声水平、"Conformal" 命名无理论基础、ε confound。

---

## Summary

ACR-VLA 提出一个面向 frozen flow-matching VLA 的 adaptive inference-time correction pipeline。核心设计：抽 K=2 个 action sample（batched forward pass，与 K=1 同延迟），用 pairwise L₂ distance 作为 per-step uncertainty probe（ρ=0.9979 vs K=10 sample variance），gate 一个 327K 参数的 Correction Residual Module (CRM)。在 SmolVLA (0.4B) 上跨 LIBERO 4 个 suite 评估，并在 π₀.₅ (3.6B) 上做跨 VLA 分析。核心发现：unconditional CRM correction 在 2/4 suites 退化，adaptive gating 在全部 4 suites 上 match 或 exceed baseline + unconditional correction。

---

## Strengths

**S1: 清晰的机制洞察 — gating > correction** [R1, R2 共识]
"When to correct matters more than correction strength" 是一个有说服力的发现。Figure 3 展示 trigger rate 与 improvement 的单调相关性：high-uncertainty suites (Spatial 20%, Goal 10%) 获益，low-uncertainty suites (Object 4%, Long 4%) 保持 baseline。这为 inference-time compute 分配提供了有价值的 design principle。

**S2: 高效的 K=2 设计** [R1, R2 共识]
K=2 batched inference 与 K=1 延迟相同（~170ms，shared prefix encoding），uncertainty probe 零额外开销，CRM 仅 +0.25ms。相比 K=10 方法节省 5× VLA forward passes。这是对 Round 2 latency 问题的出色回应。

**S3: 诚实的统计报告** [R1, R2 共识]
论文在 Section 4.2 明确承认 paired improvements 在 n=3 下不显著（p≈0.27），Figure 3 标注 "all suites n.s. (p ≥ 0.05, n=3)"，Limitations section 全面披露 effect size、scope、probe 局限性。这种诚实值得肯定，但诚实报告弱结果不等于结果足够强。

**S4: 跨 VLA 分析增加深度** [R1, R2 共识]
Section 4.5 的 π₀.₅ 分析（94-99% baseline）揭示了 model capability dependency：unconditional correction 在强 VLA 上退化更严重（up to −17pp），adaptive gating 恢复 19-38% 损失。这建立了跨能力水平的 pattern，比 Round 2 单一 VLA 有实质提升。

**S5: 写作质量高** [R1, R2 共识]
Exposition 清晰，符号一致，AI 写作痕迹极低。Pipeline 描述精确（Section 3.5 三步 protocol），贡献列表（4 项）与实验 section 结构对齐。

---

## Weaknesses

### Must-Fix [Critical] — 3 项共识

**W1. 统计功效不足：1-2pp 效果量在 n=3 下不显著** [R1-N1, R2-W2 — CONSENSUS]
Table 1 核心数据：Adaptive vs VLA-only Δ = +1.5 (Spatial) / +0.1 (Object) / +1.3 (Goal) / −0.3 (Long) pp。n=3 matched seeds per suite。Spatial p≈0.27，远未达 α=0.05 threshold。

8-seed extended analysis（Appendix E, p=0.017）仅覆盖 Spatial（1/4 suites）。其余 3 suites 仍为 n=3，无法排除改进来自噪声。

更严峻的对照问题：Δ_CRM（Adaptive vs CRM always-on）= +1.0 to +1.9 pp，论文称此为 "stronger empirical claim"。但 Adaptive 使用 ε=0.2 而 CRM always-on 使用 ε=0.05（Section 3.4）——4× norm bound 差异使该对比非 apple-to-apple（见 W6）。

**结论**：当前统计证据仅支持 "directional consistency"（3/4 suites positive），不支持 "ACR-VLA improves performance" 的 positive claim。

**W2. "Conformal" 标题无理论基础** [R1-N2, R2-W1 — CONSENSUS]
标题 "Adaptive **Conformal** Refinement" 暗示 formal conformal prediction guarantees。Section 3.5（lines 170-172）自承："We use the term 'conformal' loosely to denote calibrated thresholding on held-out data; ACR-VLA does not implement formal conformal prediction guarantees [25]."

这是标题级别的 misleading：
- 搜索 conformal prediction + robotics 的读者会找到此文并发现它不实现 CP
- "Loosely" 使用一个有严格数学定义的术语不可接受
- 实际做的是 percentile thresholding on empirical d₂ distribution（与 CP 无关）

建议替代：Adaptive Residual Refinement / Adaptive Uncertainty-Gated Refinement / Adaptive Threshold Refinement

**W3. Sim-only 评估，单一核心 backbone** [R1-W4, R2-W3 — CONSENSUS]
所有核心实验在 LIBERO simulation 上运行，仅 SmolVLA (0.4B) 一个 backbone 有完整 ablation。π₀.₅ 分析（Section 4.5）仅报告 success rates 无 component decomposition。OpenVLA-OFT boundary 分析（Appendix A）为 negative result。

CoRL 2026 鼓励 real-robot experiments 或 sim-to-real transferability evidence。论文两者皆无。标题用 "Frozen Flow-Matching VLAs"（复数）但完整评估仅一个。

虽然 Round 2 → 3 增加了 π₀.₅ 和 OpenVLA-OFT 分析，scope 仍 narrow by CoRL standards。

### Should-Fix [Warning] — 5 项

**W4. CRM train/eval task overlap 缺 held-out suite 验证** [R1-N3 critical, R2 rebuts to warning — DIVERGENCE]
CRM 在目标 LIBERO suites 的 demonstration data 上训练（Section 4.1: 3-suite 或 4-suite CRM）。R1 认为无法区分 memorization vs generalization（critical）。R2 认为 rollout-level split 是标准做法，CRM 输入为 observation embedding + selected action（非 task identity），但同意缺少 leave-one-suite-out 测试是弱点。

**Director 裁定**：WARNING。Rollout split 确实是标准做法（非 data leakage），但缺少 held-out suite 泛化测试仍然是实验完整性的缺口。至少应报告将 CRM 训练在 3 suites 上然后在第 4 suite 上测试的结果。

**W5. 页面超限** [R1-W2, R2 agree]
Limitations section (Section 6) 始于 PDF 第 9 页。源文件 discussion.tex 有 `\enlargethispage{6\baselineskip}` 和 `\vspace{-8pt}` hack。CoRL 2026 允许 8 页正文（excluding references and appendix）。如 Limitations 计入正文则超限，存在 desk-reject 风险。

**W6. ε confound 在 Adaptive vs CRM always-on 对比中** [R2 — new finding]
论文的 "stronger claim" 是 Δ_CRM = Adaptive − CRM always-on = +1.0 to +1.9 pp。但两个方法使用不同 ε：Adaptive ε=0.2，CRM always-on ε=0.05。Section 3.4 解释 gating 允许更宽松的 ε，但读者无法分离 gating 效果和 norm bound 效果。需要 CRM always-on (ε=0.2) ablation 来消除 confound，或在文中明确讨论此限制。

**W7. 缺少 K=2 argmin baseline** [R1, R2 — CONSENSUS]
当前 methods 包含 K=10 argmin 和 K=2 mean，但无 K=2 argmin（K=2 sample, argmin selection, no CRM）。这是在相同 sample budget (K=2) 下分离 selection 和 correction 贡献的关键 ablation。

**W8. 8-seed 分析仅限 Spatial** [R1-W5, R2 — CONSENSUS]
Appendix E 的 8-seed 扩展分析（p=0.017）仅覆盖 Spatial。Object、Goal、Long 仍为 n=3。统计 claim 的覆盖面不完整。

---

## Reviewer Consensus [AGREE]

| # | 问题 | R1 | R2 | 严重程度 |
|---|------|----|----|---------|
| 1 | 效果量 1-2pp 在 n=3 下不显著 | N1 (must-fix) | W2 (critical) | **Critical** |
| 2 | "Conformal" 标题无理论基础 | N2 (must-fix) | W1 (critical) | **Critical** |
| 3 | Sim-only + 单一核心 VLA | W4 (should-fix) | W3 (critical) | **Critical** |
| 4 | π₀.₅ CRM 训练 setup 不透明 | W1 (should-fix) | AGREE | Warning |
| 5 | 页面超限 | W2 (should-fix) | AGREE | Warning |
| 6 | 8-seed 仅 Spatial | W5 (should-fix) | AGREE | Warning |
| 7 | 缺 K=2 argmin baseline | minor | AGREE | Warning |
| 8 | Missing references (STEER, CP-robotics) | minor | AGREE | Info |

## Reviewer Divergence [REBUT]

| # | 问题 | R1 | R2 | Director 裁定 |
|---|------|----|----|--------------|
| 1 | CRM train/eval overlap 严重程度 | Critical: 无法区分 memorization | Warning: rollout split 标准做法，但缺 held-out | **Warning**: rollout split 合理，但需 held-out suite 验证 |
| 2 | A2C2 实验对比必要性 | Should-fix: A2C2 可 attach 到同一 VLA | Rebut: concurrent work, 解决不同问题 | **Warning → 写作改善**: textual positioning 可接受，但需更明确解释不可直接对比的原因 |
| 3 | CRM 隐层维度描述 | 缺失 | Rebut: Section 3.3 已有 Linear(n_in,256)→ReLU→Linear(256,256)→ReLU→Linear(256,H·d) | **R2 正确**: 信息在正文中，R1 可能遗漏 |

---

## Questions for Authors

1. **ε confound**: 能否提供 CRM always-on (ε=0.2) 的结果，以分离 gating 效果和 norm bound 效果？
2. **K=2 argmin**: K=2 argmin-to-centroid selection（无 CRM）在 4 suites 上的 success rate？
3. **Held-out suite**: 在 3-suite CRM 上测试 held-out suite（如 Long 训练在 Spatial+Object+Goal 的 CRM 上评估）的结果？
4. **π₀.₅ CRM**: π₀.₅ 的 CRM 是否与 SmolVLA 使用相同协议训练？n_obs 为 2048？training data source？
5. **Per-suite p-values**: Object、Goal、Long 的 paired comparison p-value（Adaptive vs VLA-only）？
6. **"Conformal" 命名**: 是否有计划移除或替换标题中的 "Conformal"？

---

## Missing References

**R1 + R2 共识**：
- **STEER** (Structured Evaluation of Embodied Robot agents) — 相关 embodied evaluation benchmark
- **CP in robotics** — 标题使用 "Conformal" 但仅引用 Angelopoulos & Bates [25] 的 tutorial。应补充实际在 robotics 中应用 CP 的文献（如 Lindemann et al. 2023 conformal prediction for safe planning）

**遗留自 Round 2**：
- RT-2/OpenVLA/Octo 的 bib entries 仍为 @misc，需更新为正式 venue 信息

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成 (2026-05-27T15:15 → 15:17, ~2.5 分钟)

| 严重程度 | 页面 | 发现 |
|---------|------|------|
| ⚠️ Warning | p.11 | 参考文献尾页仅 2 条 entry ([27]-[28])，>80% 空白。LaTeX 在 Appendix 前强制换页所致。 |
| ⚠️ Warning | p.14 | 附录末页 Table 7 + 2 行文字仅占 ~25%，>60% 空白。建议扩展或合并。 |
| ℹ️ Info | p.1-2 | 前两页纯文本无 display item。Figure 1 在 p.3 顶部，提前至 p.2 可增强第一印象。 |
| ℹ️ Info | p.6 | Table 1 格式正确（booktabs, 加粗最优）。Figure 2 颜色在灰度下区分度可能不足，建议加 hatching。 |
| ℹ️ Info | p.7 | Figure 3 清晰可读，"all suites n.s." 注释框有助快速抓取结论。 |

无 critical 级排版问题。

---

## Overall Assessment

**Score: 5/10 — Borderline Reject**
**Confidence: High**

| Reviewer | Score | 量表 | 对齐 |
|----------|-------|------|------|
| R1 (方法/实验/统计) | 5/10 | Borderline | ← |
| R2 (新颖性/完整性) | 2/4 | Weak Reject | ≈ 4-5/10 |

**核心判断**：

论文自 Round 2 以来有 **实质性进步**——K=2 设计解决了 latency 瓶颈，baseline 性能从 11.6% 提升至 58-83%，跨 VLA 分析增加了深度，写作质量保持高水平。Round 2 的 7 个 critical 中 5 个已 resolved。这是值得肯定的响应能力。

但改版后浮现的新核心问题同样严峻：

1. **统计证据不足** [Critical]：效果量缩至 1-2pp（Round 2 为 +6pp），n=3 下全部不显著。这不是 "需要更多 seeds" 的简单问题——即使 8-seed Spatial 仅达 p=0.017（单一 suite），其余 3 suites 是否重现不确定。论文诚实报告了这一点，但诚实 ≠ 结论成立。

2. **"Conformal" 命名 misleading** [Critical]：标题核心术语无理论支撑，Section 3.5 自承 "loosely"。这会误导搜索 conformal prediction 方法的读者，且在审稿中会被严厉 flag。

3. **评估范围** [Critical for CoRL]：Sim-only + 单一核心 VLA + 单一 benchmark family。π₀.₅ 分析有帮助但仅 success rate 无 ablation。

**与 Round 2 对比**：
- ✅ 解决了：latency、低 baseline 性能、motivation disconnect、Dissecting 标题、seed 格式不统一
- ❌ 持续存在：sim-only scope、CRM 泛化未验证、bib 格式
- 🆕 新问题：效果量缩小至噪声水平、Conformal 命名、ε confound
- 总体：论文改善方向正确但尚未达到 CoRL 2026 接收水平

**Deadline 考量**（距 submission 2 天）：W1 (统计功效) 和 W3 (scope) 不可能在 2 天内解决。W2 (Conformal 命名) 可通过 title rename 快速修复。W5 (页面) 可快速修复。建议 Research Director 权衡投稿 vs 撤回至下一 venue 周期。

---

## Detailed Comments

### Section 1 (Introduction)
- Intro 重写后叙事连贯：frozen deployment → unconditional correction 不稳定 → adaptive gating 解决。比 Round 2 的 LIBERO+ distribution shift framing 更准确。
- "A2C2 [5] learns a correction head on action chunks but applies it unconditionally" (line 26-28)：定位清晰但简短。如果 A2C2 不做实验对比（R2 认为可以），应在此处或 Related Work 更充分解释为何不可直接对比。

### Section 3.3 (CRM)
- DAgger citation (line 50): "Gaussian noise augmentation on a_base to improve generalization to the closed-loop state distribution [28]"。DAgger 是 interactive dataset aggregation，不是 static noise augmentation。应引用 domain randomization 文献或删除引用。[遗留自 Round 2, R1-W5-new]

### Section 3.4 (Magnitude Control)
- ε=0.2 (adaptive) vs ε=0.05 (unconditional) 差异需更明确讨论。当前表述暗示 gating 允许更大 ε，但 Table 1 的 Δ_CRM 对比未控制此变量。

### Section 3.5 (Adaptive Inference-Time Compute)
- "We use the term 'conformal' loosely" (line 170-172)：这句自承不应出现在正文——如果需要为术语使用道歉，说明术语本身选择有问题。

### Section 4.1 (Setup)
- SmolVLA checkpoint 仍无 commit hash [遗留自 Round 2, R3-W9-new]
- Precompute random seed 仍未明确 [遗留自 Round 2, R3-W10-new]

### Section 4.2 (Main Results)
- Table 1: K=2 mean 在 Spatial 列标 "—"，Long 标 n=1 superscript。建议在 table note 解释缺失原因。
- "The stronger empirical claim is Adaptive vs. CRM always-on" (implied in statistical note)：需要 ε-controlled ablation 才能称 "stronger"。

### Section 4.5 (Cross-VLA Analysis)
- π₀.₅ 分析有价值但不够深：仅 Table 3 success rates，无 trigger rate、per-task breakdown、CRM training details。如果 π₀.₅ 是论文贡献之一，需要同等水平的实验报告。

### Section 6 (Limitations)
- 三段式 limitations 诚实全面。但 "real-robot transfer remains future work" 在 CoRL 2026 context 下是显著弱点。

### References
- RT-2 [39]、OpenVLA [88]、Octo [77]、π₀ [21]、π₀.₅ [30] 仍为 @misc。建议更新已发表论文的 venue 信息。[遗留自 Round 2, M4]
