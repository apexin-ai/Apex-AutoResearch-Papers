# Director coordination — Part 2 of 5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/34/344e7a91893ffee82516.json)

## Round 28

### User

_source line 359 · 2026-05-17T17:35:53.937222+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: 标题与核心发现之间的叙事断裂**

同意。标题 "Decomposing Contamination from Calibration" 暗示框架能有效分解两者，但论文的核心结论恰恰是 aggregate level 上无需分解（~0.6-0.7pp, raw accuracy 最佳）。论文试图用 "diagnostic value" 叙事挽救，但这个 pivot 在 Introduction (§1) 第四段才出现，且与 Contribution 1 ("Empirical decomposition of contamination effects") 的措辞矛盾——"decomposition" 暗示分出了有意义的成分，而实际结果是 contamination 成分接近零。

R2 建议改为实证调查风格是合理的。我补充认为，如果保留当前标题，Introduction 的叙事线需要从第一段就铺设 "decomposition 的结果可能是 null" 的预期，而非在 Results 才 reveal surprise。当前写法（§1 para 4: "Our experiments yield a surprising null result"）是典型的实验报告风格，不符合顶会论文的故事驱动写法。

**[AGREE] R2-N2: Null finding 的泛化性严重受限**

完全同意，这与我的 N1 一致。SFT injection 在 ≤3B 模型上的 null finding 不能推广到 pretraining contamination。R2 引用的 arXiv 2601.04301 我无法独立核实，但论文自身在 Limitations (§7, "SFT ecological validity" paragraph) 已承认 "Pretraining-stage leakage... may produce qualitatively different contamination signatures"。更关键的是，论文已引用的 Zhang et al. (2024, GSM1K) 发现了 original vs regenerated items 之间的 performance gap，这提供了 pretraining contamination effect 可能非零的间接证据——但论文从未将自己的 SFT 结果与这个已知参照点做定量对比。

我补充一点：即使无法在 7B 上复现（计算资源限制），论文至少应该在 Discussion 中做一个 back-of-envelope 估算——如果 pretraining contamination 的 effect size 是 SFT 的 5-10 倍（基于已有文献），ContamCal 在 J=50 条件下是否有足够 power 检测到？这种 prospective power analysis 能大幅增强论文的前瞻价值。

**[AGREE with nuance] R2-N3: RRF multi-signal fusion 的实际贡献被自身实验否定**

大部分同意，但有细微补充。R2 正确指出 §5.2 承认 "RRF fusion degrades to S1-only performance"——但这一表述主要针对 0.5B scale。在 3B 上，S2 的 Cohen's d ≈ +0.7（§5.2），具有中等判别力，RRF 理论上应优于 S1-only。**问题在于论文未提供 RRF vs S1-only 在 1.5B/3B 上的直接 ablation 对比**（τ, MAE, γ significance）。这是一个明显的实验缺口。

我部分 rebut R2 "multi-signal fusion 无 added value" 的绝对表述：RRF 的设计动机（training-free, 避免 meta-circularity）在方法论层面是合理的（§3.1），且如果 S2 在更大模型上判别力更强，RRF 的 value 会显现。但在当前实验条件下，R2 的批评成立——论文需要在 3B 上展示 RRF > S1-only 的实证证据，否则 RRF 作为贡献确实站不住脚。

---

### Should-Fix

**[AGREE] R2-W1: Oracle ablation 解释不充分——"effect heterogeneity" vs "model misspecification" 未区分**

完全同意，这与我的 N2 一致。Oracle ablation (§5.1: γ = -0.012, CI [-0.145, 0.119], PPP=0.41) 是论文中最重要的消融实验之一，但作者将 non-significant γ 归因于 "effect heterogeneity" 而未考虑 model misspecification。如我在 N2 中详述：additive linear γ 可能在 item-level effects 方向相反时被平均为零，这是模型规范问题而非数据问题。论文需要测试 item-level γ_i 或交互项模型来区分这两种解释。

**[AGREE with reservation] R2-W2: 五个贡献过多且分散**

部分同意。五个 contributions 确实分散了论文焦点——(1) null finding, (2) item filtering, (3) Min-K%++ reversal, (4) identifiability boundaries, (5) domain diagnosis 覆盖了从 "contamination 不重要" 到 "detection signal 失效" 到 "IRT 样本量要求" 的跨度过大。核心 story 应该是 (1)+(2)+(4)，即 "IRT 框架在什么条件下能诊断 contamination"。

但我也理解作者的困境：null finding 作为 sole contribution 难以支撑 long paper，因此需要 side findings 填充。我建议将 (3) Min-K%++ reversal 和 (5) domain diagnosis 整合为 "empirical observations" 子节，而非独立 contributions。

**[AGREE in principle] R2-W3: 重要相关工作遗漏**

我无法独立核实 R2 引用的三篇具体论文（Han et al. EACL Findings 2026; arXiv 2601.04301; Chen et al. EMNLP 2025 survey），但如果 Han et al. 确实在 psychometric evaluation 框架下研究 LLM contamination，这是最直接的 concurrent work，必须引用和比较。作者应通过 web search 核实这些引用的存在性和相关性，并在 Related Work §2 "IRT for LLM evaluation" 段落中加入讨论。

我在自己的审稿中也指出了引用缺失：论文未引用 Bayesian model comparison (WAIC/LOO-CV) 和 Bayesian workflow 的标准参考文献，这对先验选择和模型比较的严谨性有影响。

**[AGREE] R2-W4: Cross-family validation J=3-4 统计功效不足**

完全同意，与我的 W4 一致。MMLU 上排除 d100 后仅 J=3 Llama models，单一 seed。论文声称 "post-hoc power calculations in Appendix E" 但我在 Appendix 中未找到独立的 Appendix E 内容（Appendix 只有 A-D 节）。如果 power analysis 未实际提供，这是一个 missing evidence 的问题。

**[AGREE] R2-W5: Table 2 (domain γ) 缺少所有 domain 的 PPP 值**

完全同意，与我的小问题列表一致。Per-domain PPP 对判断 domain-level IRT model fit 至关重要。鉴于 ARC 已知 PPP < 0.05（§5.4），MMLU 的某些 domain（特别是 item 数较少的 domain）也可能存在 misfit。省略 PPP 值让读者无法判断 domain-level γ 估计是否可靠。

**[AGREE] R2-W6: Abstract ~258 words，超过 ACL 推荐 150-250 words，数字过密**

同意。Abstract 数字密度过高（~0.6-0.7pp, τ = 0.73 vs 0.46, Δτ = 0.27, γ = -0.57, Cohen's d = -1.55 to -1.98, MAE 0.108-0.314, AUC ≥ 0.55, J ≥ 50），审稿人 30 秒内难以提取核心信息。Abstract 应聚焦 2-3 个关键数字，其余移入正文。

---

### 综合意见

R2 和我的审稿在核心判断上高度一致：**null finding 的外部效度（N1/N2 ↔ 我的 N1）**和 **linear γ 假设的充分性（W1 ↔ 我的 N2）**是最关键的两个问题。R2 额外提出的 RRF 贡献被自身实验否定（N3）是一个我未充分展开但同意的重要观察。

两位 reviewer 均给出 Overall 3.0 (Findings)，反映了一致的判断：方法框架有价值，但当前实验证据不足以支撑核心 claims 的普遍性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 360 · 2026-05-17T17:35:58.636938+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 29

## Round 29

2 recorded events


### User

_source line 361 · 2026-05-17T17:36:01.096276+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。对 R2 的 9 个问题中，我给出 7 个 [AGREE]、2 个 [AGREE with nuance/reservation]，核心共识集中在 SFT ecological validity、linear γ misspecification 风险、以及 cross-family 统计功效不足三个方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 362 · 2026-05-17T17:36:05.897872+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 30

## Round 30

8 recorded events


### User

_source line 363 · 2026-05-17T17:36:28.840396+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 意见

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: SFT injection ecological validity 不足以支撑核心 claim**

完全同意。这与我的 N2 一致。Abstract 第 4 句 "Raw accuracy is already well-calibrated" 未加任何限定条件，Conclusion §6 ¶1 同样以无条件语气声称。但这个结论仅建立在 LoRA SFT injection (α=32, r=16) 于 ≤3B 上的结果。

补充证据：近期 arXiv 2601.04301 ("Quantifying the Effect of Test Set Contamination on Generative Evaluations", 2026) 在 pretraining level 做 dose-response 实验，发现 contamination effect 在 pretraining 阶段显著更大——即使单次 test set replica 就能让 loss 低于 uncontaminated irreducible error。这直接反驳了 "raw accuracy is well-calibrated" 作为 general claim 的可信度。

作者至少应在 Abstract/Introduction/Conclusion 中加 "under SFT injection at ≤3B scale" 的限定，并引用 pretraining contamination 的反面证据。

---

**[AGREE] R1-N2: Additive linear γ 假设验证不足，oracle ablation 解释存在逻辑漏洞**

同意，这与我的 W1 一致但 R1 的分析更深入。关键逻辑问题：oracle ablation 的两种解释——(a) 真的没效应（heterogeneity 导致 cancel out）vs. (b) 有效应但 linear additive γ 捕捉不到（model misspecification）——在论文中没有被区分开。

论文自己在 Limitations ¶9 承认 "contamination exhibits threshold-like behavior... the linear γ will be diluted toward zero"，又在 §5.1 oracle ablation 中将 non-significant γ 归因于 heterogeneity。这两个解释互相冲突：如果是 heterogeneity（opposing directions cancel），那 domain-level fitting 应该能解决；如果 domain-level 也不 work（只有 1/8 significant），更可能是 model misspecification。

R1 建议的 item-level γ_i 或 γ × a_i 交互模型是检验 misspecification 的直接方法。

---

**[AGREE] R1-N3: 域级 γ 显著性缺多重比较校正**

同意。论文 Contribution 5（§1, line 17）自己写了 "without multiple comparison correction"，但这不应该只是一个脚注式说明——它直接影响 Social Sciences γ = -0.57 (CI [-1.05, -0.10]) 这个发现是否成立。

Bonferroni 校正后 α = 0.05/8 = 0.00625。Social Sciences 的 95% CI 上界为 -0.10，非常接近零。99.375% CI（对应 Bonferroni 校正）几乎肯定会包含零。即使用更宽松的 BH 校正，8 个检验中只有 1 个 < 0.05，BH adjusted p-value 也大概率 > 0.05。

这意味着论文唯一的 "significant domain-level finding" 在校正后可能不再显著。Contribution 5 和 Abstract 中 "Social Sciences shows a significant negative effect" 的措辞需要修改。

---

**[AGREE with nuance] R1-N4: ARC PPP < 0.05 但仍纳入 Table 3**

基本同意，但有一个 nuance。

**同意的部分**：§5.4 明确指出 "ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)"。在此条件下，Table 3 的 ARC 列中 IRT-based methods (B3, ContamCal) 的结果缺乏可靠性基础，Table 3 应对 ARC 列加 PPP 注脚。

**部分反驳**：R1 建议 "从 Abstract 移除 ARC 具体数值"，但 Abstract 中 "~0.7pp" 这个数字来自 raw accuracy 跨 dosage 的变化量（§5.1 ¶2），不依赖 IRT model fit。它是一个 empirical observation，不受 PPP 问题影响。Abstract 可以保留这个数字，但应明确标注来源是 raw data 而非 IRT calibration。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: J 值不一致且远低于 identifiability threshold**

同意。Table model_sets（Appendix B）解释了 J 变化的原因（domain-level runs 先于 3B retraining），但这个解释应在主文 §4.1 更 prominently 呈现。更关键的问题是：论文自己的 simulation（§5.3）说 J ≥ 50 才能可靠恢复 γ，但所有实际分析都在 J = 13-16，远低于此阈值。这意味着所有 γ-based 结论（包括 Social Sciences 的 "significance"）本质上都是 underpowered。

---

**[AGREE] R1-W2: RRF-filtered 300 items vs random 2000 items 存在 item discrimination confound**

同意。这是一个我之前未注意到的好问题。RRF filtering 可能系统性选择高 discrimination (a_i) 的 items——因为 high-discrimination items 更容易被 detection signals 区分。如果 τ 的提升来自 item quality 而非 contamination-guided selection，那 Contribution 2 的归因就有问题。

论文的 exclusion sensitivity analysis（§5.1, removing 0-50% top-exposure items from random subsets）是一个部分控制，但它不能区分 "RRF 选出了 high-a items" 和 "RRF 选出了 contamination-informative items"。需要报告 RRF-selected vs random subset 的平均 a_i 来排除 confound。

---

**[AGREE] R1-W3: CI coverage 应在主文讨论**

同意。MMLU over-covers（50% CI: 83%）和 ARC under-covers（50% CI: 45%）是 model fit 质量的重要指标。仅放在 Limitations 中降低了可见性，特别是 ARC under-coverage 与 ARC PPP < 0.05（R1-N4）互相印证，说明 ARC 上的 IRT 结果整体不可靠。

---

**[AGREE] R1-W4: Cross-family power analysis 内容缺失**

强烈同意。§4.2 声称 "we report post-hoc power calculations in Appendix E using Qwen J=13 effect sizes as reference"。但 Appendix E（§Full Baseline Comparison, label sec:full_baselines）的实际内容是 baseline comparison tables（Tables 5-6），完全不包含 power analysis。这是一个 **内容缺失/引用错误**——论文声称提供的分析实际不存在。这比 R1 的 "未找到" 更严重：不是找不到，是 Appendix E 根本不是 power analysis。

---

**[AGREE] R1-W5: γ ~ N(0,1) 先验 sensitivity analysis 缺失**

同意。N(0,1) 对于一个 additive log-odds shift 来说是相对宽的先验（覆盖 ±2 个 log-odds 单位）。如果 contamination 的真实 effect 很小（如 null finding 所示），prior 的选择可能对 posterior inference 有实质影响。至少应测试 N(0, 0.5) 和 N(0, 2) 两个替代先验。

---

**[AGREE] R1-W6: Min-K%++ reversal 因果解释仅为假设**

同意。§5.2 的解释（"SFT injection at 0.5B disrupts the token-level surprisal landscape so severely that contaminated items paradoxically show reduced token-level fluency"）是合理的 post-hoc 假设，但没有直接验证（如比较 clean vs contaminated models 的 token-level perplexity distributions）。不过这是 minor issue——empirical finding 本身（reversal 存在）已经充分文档化，因果机制的完整解释可以留给后续工作。

---

### 总结

10 个问题中我 **AGREE** 9 个，**AGREE with nuance** 1 个（R1-N4 关于 ARC ~0.7pp 在 Abstract 中的处理）。

R1 和我的审稿意见高度一致，核心关切相同：(1) null finding 的 generalizability；(2) 2PL+γ model specification 的充分性；(3) Social Sciences γ significance 的 robustness。R1 额外发现了两个我遗漏的重要问题：W2（item discrimination confound）和 W4（Appendix E power analysis 内容缺失）。后者尤其严重——论文引用了不存在的内容。

整体评分维持 **Overall 3.0 (Findings)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-17T17:36:39.596376+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-17T17:36:39.697828+00:00_

1	- id: "R2-N1"
2	  summary: "γ parameter provides no calibration benefit over vanilla 2PL — core narrative mismatch"
3	  category: framing
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 2
7	  last_seen_round: 3
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling. 两位 Reviewer 三轮一致列为 #1 must-fix."}
11	  action_items:
12	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
13	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
14	    - {round: 3, action: "D134: Retire 53% MAE claim, reframe as null finding", assigned_to: "paper_agent", status: "done"}
15	  resolution: "Title changed to 'Decomposing Contamination from Calibration'. Abstract rewritten around null finding (D134). All contributions reframed."
16	  resolution_round: null
17	
18	- id: "R2-N2"
19	  summary: "CI coverage systematically fails — 50% CI achieves only 35% empirical coverage"
20	  category: method
21	  severity: critical
22	  status: in_progress
23	  first_raised_round: 2
24	  last_seen_round: 3
25	  mentions:
26	    - {round: 2, reviewers: "R1,R2", note: "Need 80%/95% coverage + root cause diagnosis."}
27	    - {round: 3, reviewers: "R1,R2", note: "§5.1 only reports 50%. 80%/95% completely missing."}
28	  action_items:
29	    - {round: 2, action: "Report 80% and 95% CI empirical coverage", assigned_to: "main_agent", status: "done"}
30	    - {round: 2, action: "Diagnose CI miscalibration cause", assigned_to: "main_agent", status: "done"}
31	    - {round: 3, action: "Discuss local independence violation", assigned_to: "paper_agent", status: "done"}
32	    - {round: 3, action: "Note CI coverage comp
…[truncated 22332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-17T17:39:40.046133+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation ('does contamination need calibration?') rather than method paper ('here is ContamCal')\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without qualification. Pretraining contamination (arXiv 2601.04301) shows significantly larger effects. All claims must be scoped to 'under SFT injection at ≤3B scale'. Both reviewers AGREE unanimously.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims in Abstract/Intro/Conclusion to 'under SFT injection at ≤3B'\", assigned_to: \"paper_agent\", status: \"pending\"}\n    - {round: 4, action: \"Cite and discuss pretraining contamination dose-response literature as contrast\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation (AUC=1.0, γ=-0.012 non-sig) has two interpretations: (a) genuine null effect (heterogeneity cancels), (b) model misspecification (linear γ cannot capture threshold/interaction effects). Paper adopts (a) without testing (b). Limitations ¶9 acknowledges threshold possibility but §5.1 oracle section ignores it. Both reviewers AGREE this is fundamental ambiguity.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i or γ×a_i interaction model as misspecification check\", assigned_to: \"main_agent\", status: \"pending\"}\n    - {round: 4, action: \"If not testable, explicitly scope claim as 'under linear additive specification'\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"8 independent domain tests, only Social Sciences significant at α=0.05. Bonferroni α=0.00625; CI upper bound -0.10 would likely include zero. BH correction also unlikely to survive 1/8 pattern. This is the sole evidence for 'diagnostic value' narrative. Both AGREE correction needed.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results for domain-level γ\", assigned_to: \"paper_agent\", status: \"pending\"}\n    - {round: 4, action: \"If non-significant after correction, reframe as 'suggestive pattern requiring higher-powered replication'\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations but results still in main table\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at J=8, 13, 16 per §5.4. Table 3 still reports ARC IRT results without PPP annotation. R2 nuance: ARC ~0.7pp from raw data is valid, but IRT-derived numbers are unreliable. Both AGREE Table 3 needs PPP annotation and ARC IRT results need caveat.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column in Table 3\", assigned_to: \"paper_agent\", status: \"pending\"}\n    - {round: 4, action: \"Discuss ARC misfit source (item pool heterogeneity vs model specification)\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion degrades to S1-only — no RRF vs S1-only ablation at 1.5B/3B\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical by R2. S2 reverses at 0.5B, S4 near-random below 1.5B. §5.2 admits RRF degrades to S1-only. No direct RRF vs S1-only ablation (τ, MAE, γ) at 1.5B/3B where S2 d≈+0.7. R1 partially rebuts absolute claim but agrees ablation is missing. Contribution 2 unsupported without this evidence.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2 in D134 reframing\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation at 1.5B and 3B (τ, MAE, γ significance)\", assigned_to: \"main_agent\", status: \"pending\"}\n    - {round: 4, action: \"If RRF ≤ S1-only, downgrade Contribution 2 to 'item filtering improves IRT' without RRF-specific claim\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically fails — reported only in Limitations\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"§5.1 only reports 50%. 80%/95% completely missing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"CI coverage now reported in Limitations: MMLU 83%/89%/100%, ARC 45%/65%/90%. ARC under-coverage corroborates PPP<0.05 misfit. Both AGREE this should be in main results, not just Limitations.\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage discussion to main results section\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses (13/16/24/28) and all below paper's own J≥50 threshold\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Contribution 4 combines simulation + empirical. Should split.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"J inconsistency from experimental timeline (domain runs before 3B retraining). All γ conclusions at J=13-16 are underpowered by paper's own standard. Both AGREE needs prominent caveat and ideally unified J.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J and model composition prominently in each table/figure\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 (300 RRF) vs 0.46 (2000 random) may reflect higher average a_i in RRF-selected items, not contamination signal value. Need discrimination-matched random subset comparison or report average a_i of RRF vs random sets.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items; add discrimination-matched control\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-C2\"\n  summary: \"Cross-family validation J=3-4 insufficient — Appendix E power analysis content missing\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"'Validated' too strong for single-seed N=3-4.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"§4.2 references 'Appendix E post-hoc power calculations' but Appendix E (sec:full_baselines) contains baseline tables, not power analysis. This is missing content, not just hard to find. Both strongly AGREE.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Write and include actual Appendix E power analysis OR remove the reference\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis missing\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50. Prior N(0,1) dominance?\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"γ~N(0,1) covers ±2 logit units. No prior sensitivity analysis. Need at least N(0,0.5) and N(0,2) alternatives. Also need e_ij distribution (mean, SD) to interpret γ effect size. Both AGREE.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2); report e_ij distribution\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption at 0.5B but provides no direct evidence (e.g., perplexity distributions). Alternative explanations (position bias confound, near-full-rank LoRA catastrophic forgetting) not ruled out. R2 considers minor since empirical finding is well-documented. R1 wants either evidence or explicit 'mechanism TBD'.\"}\n  action_items:\n    - {round: 4, action: \"Either provide token-level perplexity comparison or reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Five contributions too many — dilutes core story\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span null finding, item filtering, signal failure, identifiability, domain diagnosis. R2 suggests consolidate to 2-3. R1 agrees with reservation (null finding alone too thin for long paper). Suggest: (1) framework+null finding, (2) signal reliability boundaries (merge C3+C4), demote C5 to observation.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. (EACL Findings 2026) 'Quantifying Data Contamination in Psychometric Evaluations of LLMs' is most direct concurrent work — combines IRT + contamination. arXiv 2601.04301 provides pretraining dose-response data contradicting null finding scope. Chen et al. EMNLP 2025 survey. R1 cannot independently verify but agrees in principle they should be checked and cited.\"}\n  action_items:\n    - {round: 4, action: \"Verify and cite Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025 survey\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'. Per-domain model fit unverifiable. Especially critical for Social Sciences (sole significant domain). Both AGREE must report.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values in Table 2\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"Abstract ~258 words with excessive numeric density\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers crowd out narrative. Both AGREE should trim to ~200 words with 2-3 key numbers.\"}\n  action_items:\n    - {round: 4, action: \"Trim Abstract to ≤220 words, reduce to 2-3 key numbers\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Appendix E referenced but contains baseline tables, not power analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"§4.2 says 'post-hoc power calculations in Appendix E' but Appendix E (sec:full_baselines) has Tables 5-6 baseline comparison. Content is missing, not misplaced. R2 flags as more severe than typical missing appendix.\"}\n  action_items:\n    - {round: 4, action: \"Write actual power analysis for cross-family setting or remove the reference\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues — carried forward for tracking\n- id: \"R1-C1\"\n  summary: \"Missing 1.5B/3B experimental data in Tables\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Table 1 only 0.5B.\"}\n    - {round: 3, reviewers: \"\", note: \"Subsumed by R2-W5 and R3-N5.\"}\n  action_items: []\n  resolution: \"Resolved. Table 4 now J=16 (8×1.5B + 8×3B) with all baselines.\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Triple impossibility over-generalized\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"DCR existence is counter-example.\"}\n    - {round: 3, reviewers: \"\", note: \"Triple impossibility removed from draft.\"}\n  action_items: []\n  resolution: \"Resolved — triple impossibility claim removed.\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Fisher Information simulation now has heatmap visualization\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Figure 2 with heatmap now present.\"}\n  action_items: []\n  resolution: \"Resolved — Figure 2 with heatmap now present.\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"Observational experiments over-interpret causal claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Paper restructured, observational experiments no longer present.\"}\n  action_items: []\n  resolution: \"Resolved — paper restructured.\"\n  resolution_round: 3\n\n- id: \"R1-W7\"\n  summary: \"Table 2 title misleading\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Table captions rewritten.\"}\n  action_items: []\n  resolution: \"Resolved — table captions updated.\"\n  resolution_round: 3\n\n# Issues from prior rounds not raised in R4 — annotated\n- id: \"R2-N6\"\n  summary: \"Format non-compliance: Limitations after references + missing Ethics Statement\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Limitations is subsection under Discussion.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations still after bibliography. Ethics absent.\"}\n    - {round: 4, reviewers: \"\", note: \"R4 format check confirms Limitations before references, Ethics Statement present. Issue resolved.\"}\n  action_items:\n    - {round: 2, action: \"Move Limitations before references\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Add Ethics Statement\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Resolved. Limitations and Ethics both present before bibliography. Confirmed in R4.\"\n  resolution_round: 4\n\n- id: \"R3-N5\"\n  summary: \"Baseline configuration inconsistency — main table J vs appendix J\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Main Table J=13 vs appendix J=8.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now unified J=16 with 7 baselines. Model set table in Appendix B. Issue resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Table 3 unified at J=16 with all 7 baselines. Model sets documented.\"\n  resolution_round: 4\n\n- id: \"R2-W5\"\n  summary: \"Main table incomplete — only 3/7 baselines shown\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"7 baselines defined but only 3 in main table.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now contains B0/B1b/B3/B4/B5b/B6/ContamCal. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. All 7 baselines in Table 3.\"\n  resolution_round: 4\n\n- id: \"R2-W8\"\n  summary: \"Related Work too thin — PSN-IRT/Kocyigit/Holland uncited\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"33 citations.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT, Kocyigit, Holland now cited. But new gaps: Han et al. EACL 2026, arXiv 2601.04301, Chen EMNLP 2025 survey. See R4-W4.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Prior gaps fixed. New gaps identified in R4-W4.\"\n  resolution_round: null\n\n- id: \"R2-W7\"\n  summary: \"GSM8K 11× overcorrection ratio — no decision rules\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"11× removed. Decision rules present in §6. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. 11× removed, decision rules added.\"\n  resolution_round: 4\n\n- id: \"R2-W4\"\n  summary: \"Independent per-domain IRT fitting sacrifices common θ scale\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Independent fitting produces incomparable θ scales.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"STEM γ=+0.50 identical.\"}\n    - {round: 4, reviewers: \"\", note: \"Not independently raised in R4. θ incomparability acknowledged in method. Lower priority given domain-level analysis is exploratory.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N8\"\n  summary: \"Table 5 ARC γ=-1.46 data provenance error\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"internal_reviewer\", note: \"ARC γ=-1.46 from N=8 (含 0.5B), not J=13.\"}\n    - {round: 4, reviewers: \"\", note: \"Current paper reports ARC γ=-1.46 with PPP=0.03 caveat in Table 2. R4 reviewers flag PPP<0.05 as problematic (see R3-N3 R4 update). Data provenance error partially addressed but ARC IRT results remain unreliable.\"}\n  action_items:\n    - {round: 3, action: \"Remove ARC row from Table 5\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Oracle Exposure ablation — interpretation needs balanced discussion\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Ground-truth injection labels never used as oracle.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Oracle done but interpretation one-sided.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Oracle ablation present (§5.1). But 'effect heterogeneity' interpretation adopted without equal weight to 'model misspecification' alternative. Subsumed by R3-W10 elevation to critical.\"}\n  action_items: []\n  resolution: \"Oracle ablation exists. Interpretation issue tracked under R3-W10.\"\n  resolution_round: null\n\n- id: \"R3-N7\"\n  summary: \"Novelty insufficient — limited technical contribution beyond standard IRT+DIF\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT now cited. But Han et al. EACL 2026 (IRT+contamination) uncited — potentially closer concurrent work. Technical novelty remains limited: 2PL+γ is standard explanatory IRT/DIF. Value is empirical, not methodological.\"}\n  action_items: []\n  resolution: \"PSN-IRT cited. Novelty positioning improved but fundamentally empirical paper.\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Insufficient differentiation from DCR\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"DCR reimplemented as B6. MAE=0.108/0.314 shows systematic overcorrection. Clear differentiation achieved.\"}\n  action_items: []\n  resolution: \"Resolved. DCR clearly differentiated via reimplementation and direct comparison.\"\n  resolution_round: 4\n\n- id: \"R1-W2\"\n  summary: \"Narrative pivot from calibration to diagnostic\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Consider retitling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Subsumed by R2-N1 R4 update. Title changed but framing still methods-paper style.\"}\n  action_items: []\n  resolution: \"Tracked under R2-N1.\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Limited technical novelty in IRT modeling\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N7. Novelty is empirical not methodological.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N7.\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"SFT vs real contamination gap\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 (elevated to critical in R4).\"}\n  action_items: []\n  resolution: \"Tracked under R2-W6.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"≤3B model scale limits practical applicability\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 ecological validity discussion.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-A1\"\n  summary: \"ARC PPP systematic misfit\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N3.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N3.\"\n  resolution_round: null\n\n- id: \"R1-A2\"\n  summary: \"ARC gamma direction wrong in method_notes.md\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Internal doc issue. Not paper-relevant.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-A3\"\n  summary: \"Eckerly (2017) citation needs verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Still cited. R4 reference audit: 9/43 not in OpenAlex (may be indexing delay for books/chapters). Eckerly is a Routledge book chapter — plausible but unverifiable online.\"}\n  action_items:\n    - {round: 1, action: \"WebSearch to verify Eckerly 2017\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-A4\"\n  summary: \"3B_d000 GSM8K anomaly needs explanation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Not raised in R4. Lower priority.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"46% model exclusion rate — sensitivity analysis done\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Exclusion sensitivity analysis present in §5.1 (τ 0.46-0.60, no monotonic trend). Model sets documented in Appendix B. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Sensitivity analysis shows results not sensitive to exclusion rate.\"\n  resolution_round: 4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation ('does contamination need calibration?') rather than method paper ('here is ContamCal')\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without qualification. Pretraining contamination (arXiv 2601.04301) shows significantly larger effects. All claims must be scoped to 'under SFT injection at ≤3B scale'. Both reviewers AGREE unanimously.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims in Abstract/Intro/Conclusion to 'under SFT injection at ≤3B'\", assigned_to: \"paper_agent\", status: \"pending\"}\n    - {round: 4, action: \"Cite and discuss pretraining contamination dose-response literature as contrast\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation (AUC=1.0, γ=-0.012 non-sig) has two interpretations: (a) genuine null effect (heterogeneity cancels), (b) model misspecification (linear γ cannot capture threshold/interaction effects). Paper adopts (a) without testing (b). Limitations ¶9 acknowledges threshold possibility but §5.1 oracle section ignores it. Both reviewers AGREE this is fundamental ambiguity.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i or γ×a_i interaction model as misspecification check\", assigned_to: \"main_agent\", status: \"pending\"}\n    - {round: 4, action: \"If not testable, explicitly scope claim as 'under linear additive specification'\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"8 independent domain tests, only Social Sciences significant at α=0.05. Bonferroni α=0.00625; CI upper bound -0.10 would likely include zero. BH correction also unlikely to survive 1/8 pattern. This is the sole evidence for 'diagnostic value' narrative. Both AGREE correction needed.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results for domain-level γ\", assigned_to: \"paper_agent\", status: \"pending\"}\n    - {round: 4, action: \"If non-significant after correction, reframe as 'suggestive pattern requiring higher-powered replication'\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations but results still in main table\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at J=8, 13, 16 per §5.4. Table 3 still reports ARC IRT results without PPP annotation. R2 nuance: ARC ~0.7pp from raw data is valid, but IRT-derived numbers are unreliable. Both AGREE Table 3 needs PPP annotation and ARC IRT results need caveat.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column in Table 3\", assigned_to: \"paper_agent\", status: \"pending\"}\n    - {round: 4, action: \"Discuss ARC misfit source (item pool heterogeneity vs model specification)\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion degrades to S1-only — no RRF vs S1-only ablation at 1.5B/3B\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical by R2. S2 reverses at 0.5B, S4 near-random below 1.5B. §5.2 admits RRF degrades to S1-only. No direct RRF vs S1-only ablation (τ, MAE, γ) at 1.5B/3B where S2 d≈+0.7. R1 partially rebuts absolute claim but agrees ablation is missing. Contribution 2 unsupported without this evidence.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2 in D134 reframing\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation at 1.5B and 3B (τ, MAE, γ significance)\", assigned_to: \"main_agent\", status: \"pending\"}\n    - {round: 4, action: \"If RRF ≤ S1-only, downgrade Contribution 2 to 'item filtering improves IRT' without RRF-specific claim\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically fails — reported only in Limitations\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"§5.1 only reports 50%. 80%/95% completely missing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"CI coverage now reported in Limitations: MMLU 83%/89%/100%, ARC 45%/65%/90%. ARC under-coverage corroborates PPP<0.05 misfit. Both AGREE this should be in main results, not just Limitations.\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage discussion to main results section\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses (13/16/24/28) and all below paper's own J≥50 threshold\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Contribution 4 combines simulation + empirical. Should split.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"J inconsistency from experimental timeline (domain runs before 3B retraining). All γ conclusions at J=13-16 are underpowered by paper's own standard. Both AGREE needs prominent caveat and ideally unified J.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J and model composition prominently in each table/figure\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 (300 RRF) vs 0.46 (2000 random) may reflect higher average a_i in RRF-selected items, not contamination signal value. Need discrimination-matched random subset comparison or report average a_i of RRF vs random sets.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items; add discrimination-matched control\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-C2\"\n  summary: \"Cross-family validation J=3-4 insufficient — Appendix E power analysis content missing\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"'Validated' too strong for single-seed N=3-4.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"§4.2 references 'Appendix E post-hoc power calculations' but Appendix E (sec:full_baselines) contains baseline tables, not power analysis. This is missing content, not just hard to find. Both strongly AGREE.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Write and include actual Appendix E power analysis OR remove the reference\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis missing\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50. Prior N(0,1) dominance?\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"γ~N(0,1) covers ±2 logit units. No prior sensitivity analysis. Need at least N(0,0.5) and N(0,2) alternatives. Also need e_ij distribution (mean, SD) to interpret γ effect size. Both AGREE.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2); report e_ij distribution\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption at 0.5B but provides no direct evidence (e.g., perplexity distributions). Alternative explanations (position bias confound, near-full-rank LoRA catastrophic forgetting) not ruled out. R2 considers minor since empirical finding is well-documented. R1 wants either evidence or explicit 'mechanism TBD'.\"}\n  action_items:\n    - {round: 4, action: \"Either provide token-level perplexity comparison or reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Five contributions too many — dilutes core story\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span null finding, item filtering, signal failure, identifiability, domain diagnosis. R2 suggests consolidate to 2-3. R1 agrees with reservation (null finding alone too thin for long paper). Suggest: (1) framework+null finding, (2) signal reliability boundaries (merge C3+C4), demote C5 to observation.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. (EACL Findings 2026) 'Quantifying Data Contamination in Psychometric Evaluations of LLMs' is most direct concurrent work — combines IRT + contamination. arXiv 2601.04301 provides pretraining dose-response data contradicting null finding scope. Chen et al. EMNLP 2025 survey. R1 cannot independently verify but agrees in principle they should be checked and cited.\"}\n  action_items:\n    - {round: 4, action: \"Verify and cite Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025 survey\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'. Per-domain model fit unverifiable. Especially critical for Social Sciences (sole significant domain). Both AGREE must report.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values in Table 2\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"Abstract ~258 words with excessive numeric density\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers crowd out narrative. Both AGREE should trim to ~200 words with 2-3 key numbers.\"}\n  action_items:\n    - {round: 4, action: \"Trim Abstract to ≤220 words, reduce to 2-3 key numbers\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W7\"\n  summary: \"Appendix E referenced but contains baseline tables, not power analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"§4.2 says 'post-hoc power calculations in Appendix E' but Appendix E (sec:full_baselines) has Tables 5-6 baseline comparison. Content is missing, not misplaced. R2 flags as more severe than typical missing appendix.\"}\n  action_items:\n    - {round: 4, action: \"Write actual power analysis for cross-family setting or remove the reference\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues — carried forward for tracking\n- id: \"R1-C1\"\n  summary: \"Missing 1.5B/3B experimental data in Tables\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Table 1 only 0.5B.\"}\n    - {round: 3, reviewers: \"\", note: \"Subsumed by R2-W5 and R3-N5.\"}\n  action_items: []\n  resolution: \"Resolved. Table 4 now J=16 (8×1.5B + 8×3B) with all baselines.\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Triple impossibility over-generalized\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"DCR existence is counter-example.\"}\n    - {round: 3, reviewers: \"\", note: \"Triple impossibility removed from draft.\"}\n  action_items: []\n  resolution: \"Resolved — triple impossibility claim removed.\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Fisher Information simulation now has heatmap visualization\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Figure 2 with heatmap now present.\"}\n  action_items: []\n  resolution: \"Resolved — Figure 2 with heatmap now present.\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"Observational experiments over-interpret causal claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Paper restructured, observational experiments no longer present.\"}\n  action_items: []\n  resolution: \"Resolved — paper restructured.\"\n  resolution_round: 3\n\n- id: \"R1-W7\"\n  summary: \"Table 2 title misleading\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Table captions rewritten.\"}\n  action_items: []\n  resolution: \"Resolved — table captions updated.\"\n  resolution_round: 3\n\n# Issues from prior rounds not raised in R4 — annotated\n- id: \"R2-N6\"\n  summary: \"Format non-compliance: Limitations after references + missing Ethics Statement\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Limitations is subsection under Discussion.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations still after bibliography. Ethics absent.\"}\n    - {round: 4, reviewers: \"\", note: \"R4 format check confirms Limitations before references, Ethics Statement present. Issue resolved.\"}\n  action_items:\n    - {round: 2, action: \"Move Limitations before references\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Add Ethics Statement\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Resolved. Limitations and Ethics both present before bibliography. Confirmed in R4.\"\n  resolution_round: 4\n\n- id: \"R3-N5\"\n  summary: \"Baseline configuration inconsistency — main table J vs appendix J\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Main Table J=13 vs appendix J=8.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now unified J=16 with 7 baselines. Model set table in Appendix B. Issue resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Table 3 unified at J=16 with all 7 baselines. Model sets documented.\"\n  resolution_round: 4\n\n- id: \"R2-W5\"\n  summary: \"Main table incomplete — only 3/7 baselines shown\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"7 baselines defined but only 3 in main table.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now contains B0/B1b/B3/B4/B5b/B6/ContamCal. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. All 7 baselines in Table 3.\"\n  resolution_round: 4\n\n- id: \"R2-W8\"\n  summary: \"Related Work too thin — PSN-IRT/Kocyigit/Holland uncited\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"33 citations.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT, Kocyigit, Holland now cited. But new gaps: Han et al. EACL 2026, arXiv 2601.04301, Chen EMNLP 2025 survey. See R4-W4.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Prior gaps fixed. New gaps identified in R4-W4.\"\n  resolution_round: null\n\n- id: \"R2-W7\"\n  summary: \"GSM8K 11× overcorrection ratio — no decision rules\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"11× removed. Decision rules present in §6. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. 11× removed, decision rules added.\"\n  resolution_round: 4\n\n- id: \"R2-W4\"\n  summary: \"Independent per-domain IRT fitting sacrifices common θ scale\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Independent fitting produces incomparable θ scales.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"STEM γ=+0.50 identical.\"}\n    - {round: 4, reviewers: \"\", note: \"Not independently raised in R4. θ incomparability acknowledged in method. Lower priority given domain-level analysis is exploratory.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N8\"\n  summary: \"Table 5 ARC γ=-1.46 data provenance error\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"internal_reviewer\", note: \"ARC γ=-1.46 from N=8 (含 0.5B), not J=13.\"}\n    - {round: 4, reviewers: \"\", note: \"Current paper reports ARC γ=-1.46 with PPP=0.03 caveat in Table 2. R4 reviewers flag PPP<0.05 as problematic (see R3-N3 R4 update). Data provenance error partially addressed but ARC IRT results remain unreliable.\"}\n  action_items:\n    - {round: 3, action: \"Remove ARC row from Table 5\", assigned_to: \"paper_agent\", status: \"in_progress\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Oracle Exposure ablation — interpretation needs balanced discussion\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Ground-truth injection labels never used as oracle.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Oracle done but interpretation one-sided.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Oracle ablation present (§5.1). But 'effect heterogeneity' interpretation adopted without equal weight to 'model misspecification' alternative. Subsumed by R3-W10 elevation to critical.\"}\n  action_items: []\n  resolution: \"Oracle ablation exists. Interpretation issue tracked under R3-W10.\"\n  resolution_round: null\n\n- id: \"R3-N7\"\n  summary: \"Novelty insufficient — limited technical contribution beyond standard IRT+DIF\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT now cited. But Han et al. EACL 2026 (IRT+contamination) uncited — potentially closer concurrent work. Technical novelty remains limited: 2PL+γ is standard explanatory IRT/DIF. Value is empirical, not methodological.\"}\n  action_items: []\n  resolution: \"PSN-IRT cited. Novelty positioning improved but fundamentally empirical paper.\"\n  resolution_round: null\n\n- id: \"R1-W1\"\n  summary: \"Insufficient differentiation from DCR\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"DCR reimplemented as B6. MAE=0.108/0.314 shows systematic overcorrection. Clear differentiation achieved.\"}\n  action_items: []\n  resolution: \"Resolved. DCR clearly differentiated via reimplementation and direct comparison.\"\n  resolution_round: 4\n\n- id: \"R1-W2\"\n  summary: \"Narrative pivot from calibration to diagnostic\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Consider retitling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Subsumed by R2-N1 R4 update. Title changed but framing still methods-paper style.\"}\n  action_items: []\n  resolution: \"Tracked under R2-N1.\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Limited technical novelty in IRT modeling\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N7. Novelty is empirical not methodological.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N7.\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"SFT vs real contamination gap\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 (elevated to critical in R4).\"}\n  action_items: []\n  resolution: \"Tracked under R2-W6.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"≤3B model scale limits practical applicability\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 ecological validity discussion.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-A1\"\n  summary: \"ARC PPP systematic misfit\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N3.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N3.\"\n  resolution_round: null\n\n- id: \"R1-A2\"\n  summary: \"ARC gamma direction wrong in method_notes.md\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Internal doc issue. Not paper-relevant.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-A3\"\n  summary: \"Eckerly (2017) citation needs verification\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Still cited. R4 reference audit: 9/43 not in OpenAlex (may be indexing delay for books/chapters). Eckerly is a Routledge book chapter — plausible but unverifiable online.\"}\n  action_items:\n    - {round: 1, action: \"WebSearch to verify Eckerly 2017\", assigned_to: \"main_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R1-A4\"\n  summary: \"3B_d000 GSM8K anomaly needs explanation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Not raised in R4. Lower priority.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N3\"\n  summary: \"46% model exclusion rate — sensitivity analysis done\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Exclusion sensitivity analysis present in §5.1 (τ 0.46-0.60, no monotonic trend). Model sets documented in Appendix B. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Sensitivity analysis shows results not sensitive to exclusion rate.\"\n  resolution_round: 4"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-17T17:39:40.197690+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 27662}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-17T17:42:09.316037+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0",
  "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"Decomposing Contamination from Calibration: An IRT Approach to LLM Benchmark Evaluation\"\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)\n**截止日期**: 2026-05-25\n\n**Reviewer 编排**: 2 名 Reviewer\n- Reviewer 1: 方法严谨性 + 实验设计 + 统计推断\n- Reviewer 2: 新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（无 REBUT，1 轮即达共识）\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 通过 Reciprocal Rank Fusion (RRF) 融合多种 contamination detection signals 生成 per-item exposure scores；Stage 2 将 exposure scores 嵌入 contamination-augmented IRT model (2PL+γ) 估计 decontaminated ability。核心实验在 Qwen2.5 (0.5B-3B) 上通过 LoRA SFT injection 在 MMLU/ARC/GSM8K 上进行受控 contamination 实验。主要发现是 null result：SFT-injected contamination 的 aggregate effect 仅 ~0.6-0.7pp，raw accuracy 已是最佳估计器，ContamCal 不优于 raw accuracy（Table 3: MAE 0.006 vs 0.009）。论文转向 diagnostic value 叙事，报告 γ 在 ARC 上 CI excluding zero 以及 MMLU Social Sciences 域级显著性。附带发现包括 Min-K%++ 在 0.5B 的 directional reversal 和 γ recovery 需 J≥50 的 identifiability 边界。\n\n---\n\n## Strengths\n\n1. **受控实验设计精良**：24 个模型（3 scales × 4 dosages × 2 seeds）的 within-family design 在 contamination 研究中少见，严格隔离 dosage 为唯一自变量（§4.1）。\n\n2. **诚实的科学态度**：坦率承认核心方法不优于 raw accuracy（Table 3），九项 limitations 全面且具体，negative result 的透明报告值得肯定。\n\n3. **Identifiability analysis 有理论价值**：Simulation study（20 conditions × 10 seeds × 200 runs）建立的 AUC/J 边界（§5.3, Figure 2）为未来 IRT-based contamination diagnosis 提供定量指导。\n\n4. **Min-K%++ directional reversal 发现有实用价值**：0.5B 上 Cohen's d = -1.55 to -1.98 的 reversal（§5.2）是重要的 practitioner warning，具有独立引用价值。\n\n5. **跨领域理论连接**：将 IRT item compromise/explanatory IRT/DIF 框架引入 LLM contamination analysis（§2 ¶3），理论基础扎实。\n\n6. **写作质量整体良好**：无 AI 写作标志（无 em-dash、-ing phrases 可控），术语定义完整（calibration disambiguation §2 ¶4），引用格式规范。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，6 项）\n\n**[MF1] 标题/framing 与核心发现的叙事断裂** [R1: AGREE, R2: raised]\n- 标题 \"Decomposing Contamination from Calibration\" 暗示有效分解框架，但核心结论是 aggregate level 无需分解（~0.6-0.7pp）。论文以 methods paper 包装了 negative result。\"Diagnostic value\" pivot 在 §1 ¶4 才出现，与 Contribution 1 \"Empirical decomposition\" 措辞矛盾。\n- **建议**: 重新定位为实证调查（\"Does contamination need calibration?\"），而非方法论文（\"Here is ContamCal\"）。Introduction 从第一段即铺设 null 预期。\n\n**[MF2] SFT injection 的 ecological validity 不足以支撑无条件 claim** [R1: raised, R2: AGREE]\n- \"Raw accuracy is already well-calibrated\"（Abstract, §6）未加任何限定条件，但仅基于 LoRA SFT injection at ≤3B。Pretraining contamination 通过 trillion-token web crawl 分布式暴露，效应机制根本不同。Limitations §7 承认 \"qualitatively different signatures\"，但 claim 不受限。近期 pretraining-level dose-response 研究（arXiv 2601.04301）表明 pretraining contamination 效应显著更大。\n- **建议**: (1) Abstract/Introduction/Conclusion 所有 claim 限定为 \"under SFT injection at ≤3B scale\"；(2) 引用 pretraining contamination 文献作为对比锚点。\n\n**[MF3] Additive linear γ 假设未验证，oracle ablation 解释存在根本歧义** [R1: raised, R2: AGREE]\n- Oracle ablation（AUC=1.0 perfect labels, γ = -0.012, CI [-0.145, 0.119], PPP=0.41）有两种同等合理的解释：(a) 真的没效应（item-level heterogeneity 抵消）；(b) 有效应但 additive linear γ 捕捉不到（model misspecification）。论文只采信 (a)，但 Limitations ¶9 自己承认 threshold 行为可能导致 γ 被稀释为零。如果解释 (b) 成立，整个 2PL+γ 框架的诊断价值受质疑。\n- **建议**: 测试 item-level γ_i 或 γ×a_i 交互模型排除 misspecification；不可行则在所有 claim 中明确 \"under the linear additive specification\"。\n\n**[MF4] 域级 γ 显著性（Social Sciences 1/8）缺多重比较校正** [R1: raised, R2: AGREE]\n- 8 个 domain 独立检验，仅 Social Sciences 在 α=0.05 达到显著（γ = -0.57, CI [-1.05, -0.10]）。Bonferroni 校正后 α = 0.00625，CI 上界 -0.10 极可能越过零。BH 校正下 1/8 pattern 也大概率不通过。这是 \"diagnostic value\" 叙事的主要实证支撑——校正后消失则 Contribution 5 失去支持。\n- **建议**: 报告 Bonferroni/BH 校正后结果；校正后不显著则重新表述为 \"suggestive pattern requiring higher-powered replication\"。\n\n**[MF5] ARC PPP < 0.05 但 IRT 结果仍出现在主表** [R1: raised, R2: AGREE with nuance]\n- ARC 在所有 J 配置（8, 13, 16）下 PPP < 0.05（§5.4），2PL+γ 模型拟合不合格。但 Table 3 报告 ARC IRT 结果无 PPP 注脚。ARC 的 ~0.7pp raw data observation 有效，但 IRT-derived 数值不可靠。\n- **建议**: Table 3 ARC 列加 PPP 注脚；区分 raw observation vs IRT estimate 的可信度。\n\n**[MF6] RRF multi-signal fusion 被自身实验否定** [R2: raised, R1: AGREE with nuance]\n- S2 (Min-K%++) 在 0.5B 方向反转，S4 (Self-Critique) 在 <1.5B 近乎随机，§5.2 承认 \"RRF fusion degrades to S1-only\"。Contribution 2 声称 RRF-guided filtering 价值，但无 RRF vs S1-only 在 1.5B/3B 的直接消融。R1 补充：S2 在 3B 有 d≈+0.7，RRF 可能有 value，但必须提供实证。\n- **建议**: 提供 RRF vs S1-only 在 1.5B/3B 的对比（τ, MAE, γ）；如 RRF ≤ S1-only，降格 Contribution 2。\n\n---\n\n### Should-Fix（影响评分，11 项）\n\n**[SF1]** J 值跨分析不一致（13/16/24/18-28），全部远低于论文自证的 J≥50 threshold。所有 γ-based 结论本质上 underpowered。[R1, R2 AGREE]\n\n**[SF2]** RRF-filtered 300 items vs random 2000 items 的 τ 对比（0.73 vs 0.46）可能存在 item discrimination confound。RRF 可能系统性选出高 a_i items，与 contamination signal 无关。需报告 RRF vs random subset 的平均 a_i。[R1 raised, R2 AGREE]\n\n**[SF3]** CI coverage（MMLU 83%/89%/100%, ARC 45%/65%/90%）仅在 Limitations 报告。ARC under-coverage 与 PPP<0.05 互相印证 model misfit，应在主文讨论。[R1, R2 AGREE]\n\n**[SF4]** Cross-family validation J=3-4（Llama 单 seed），且 §4.2 引用的 \"Appendix E power analysis\" 实际内容为 baseline tables（sec:full_baselines），power analysis 内容缺失。[R1, R2 AGREE; R2 确认为 content error]\n\n**[SF5]** γ~N(0,1) 先验 sensitivity analysis 缺失。覆盖 ±2 logit units，若 effect 很小则 prior 选择对 posterior 影响实质性。需测试 N(0,0.5)/N(0,2) 并报告 e_ij 分布。[R1, R2 AGREE]\n\n**[SF6]** Min-K%++ reversal 因果解释（\"token-level surprisal disruption\"）仅为 post-hoc 假设，无直接验证。替代解释（position bias confound、near-full-rank LoRA）未排除。[R1 raised, R2: AGREE but considers minor]\n\n**[SF7]** Oracle ablation（§5.1）仅采信 \"effect heterogeneity\" 解释，未平衡讨论 \"model misspecification\" 可能性。[与 MF3 关联]\n\n**[SF8]** 五个 Contributions 覆盖 null finding / item filtering / signal failure / identifiability / domain diagnosis，方向过于分散。建议合并为 2-3 个核心贡献。[R2 raised, R1: AGREE with reservation]\n\n**[SF9]** 重要相关工作遗漏：Han et al. (EACL Findings 2026) \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" 是最直接的 concurrent work；arXiv 2601.04301 pretraining dose-response；Chen et al. (EMNLP 2025) contamination survey。此外缺 Bayesian workflow/model comparison 参考（WAIC/LOO-CV）。[R2 raised, R1: AGREE in principle]\n\n**[SF10]** Table 2 (domain γ) PPP 列全为 \"---\"——per-domain model fit 不可验证，特别是 Social Sciences 作为唯一 significant domain。[R1, R2 AGREE]\n\n**[SF11]** Abstract ~258 words（超 ACL 推荐 150-250），包含 ~10 个具体数字，信息过密。[R2 raised, R1 AGREE]\n\n---\n\n### Minor Issues（6 项）\n\n1. B2 (Single2PL+γ) 在 §4.4 定义但 Table 3 中缺失\n2. \"-ing phrases\" 在 Related Work 中偏多（\"confirming that...\", \"enabling both...\"）\n3. §3.2 \"Adaptation 1/2/3\" 命名风格偏 didactic\n4. `habba_2025_growing_pains` bib key 写 2025 但实际 year=2026\n5. Eq. 2 additive interpretation (\"difficulty shift by γ_k·e_ij/a_i\") 仅在 linearization 下成立，非精确\n6. 无法编译确认正文是否 ≤ 8 页\n\n---\n\n## Reviewer Consensus\n\n所有关键问题达成共识。交叉回应中：\n- R1 对 R2 的 9 个问题：7 × [AGREE]，2 × [AGREE with nuance]（R2-N3 RRF 和 R2-W2 贡献数量）\n- R2 对 R1 的 10 个问题：9 × [AGREE]，1 × [AGREE with nuance]（R1-N4 ARC ~0.7pp 来源区分）\n- 无任何 [REBUT]\n\n核心共识：\n1. **Null finding 的外部效度**是首要问题——SFT at ≤3B 不能泛化为 contamination 的一般性质\n2. **Linear additive γ 的模型充分性**存在根本歧义——oracle ablation 无法区分 null effect vs misspecification\n3. **Domain-level γ significance** 在多重比较校正后可能消失，削弱 diagnostic narrative\n4. **RRF** 在当前实验条件下缺乏超越 S1-only 的实证支持\n\n---\n\n## Reviewer Divergence\n\n无实质性分歧。仅有微小差异：\n- R1 对 RRF 贡献被否定的程度略保守（S2 在 3B 有 d≈+0.7），R2 更绝对\n- R2 认为 ARC ~0.7pp 在 Abstract 中可保留（来自 raw data 非 IRT），R1 倾向移除\n\n---\n\n## Questions（需作者澄清）\n\n1. Table 2 各 MMLU domain 的 PPP 值是多少？如果 Social Sciences PPP < 0.05，其 γ significance 是否可信？\n2. §4.2 声称 \"post-hoc power calculations in Appendix E\"——Appendix E (sec:full_baselines) 实际为 baseline tables。Power analysis 是否存在？\n3. 在 1.5B/3B 上，RRF (S1+S2+S4) vs S1-only 的 τ/MAE/γ significance 对比结果如何？\n4. 如果将 γ 替换为 item-level γ_i 或 γ×a_i 交互项，oracle ablation 中是否能检测到 item-level contamination effects？\n5. RRF-selected 300 items 的平均 discrimination (a_i) 与 random 2000 items 相比如何？\n\n---\n\n## Missing References\n\n| 论文 | 严重程度 | 理由 |\n|------|----------|------|\n| Han et al. (EACL Findings 2026) \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" | **高** | 直接将 psychometric/IRT + contamination 结合，最接近的 concurrent work |\n| arXiv 2601.04301 (2026) \"Quantifying the Effect of Test Set Contamination on Generative Evaluations\" | **高** | Pretraining-level dose-response，与 null finding 形成关键对比 |\n| Chen et al. (EMNLP 2025) contamination survey | **中** | 领域最全面综述 |\n| arXiv 2411.03923 \"Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?\" | **中** | Contamination measurement meta-analysis |\n| Gelman et al. (2020) \"Bayesian Workflow\" / Gabry et al. (2019) Bayesian visualization | **低** | 先验选择和 PPP 的标准方法论参考 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分依据 (EMNLP 2026 ARR scale)**:\n- 3.0 = Findings（可被 Findings 接收）\n\n**理由**:\n论文提出了一个有价值的研究问题（IRT 能否分离 contamination 和 ability），实验设计严谨（受控 SFT injection, within-family design），且诚实报告 null result。Identifiability 分析和 Min-K%++ reversal 发现有独立价值。\n\n但核心问题阻碍了 Main Conference 接收：\n1. **方法不 work**: ContamCal 在其自身实验中不优于 trivial baseline (raw accuracy)\n2. **Null finding 范围受限**: 仅 SFT at ≤3B，不能推广到 pretraining contamination（最实际的场景）\n3. **Model specification 歧义**: Linear γ 的 null result 可能是 misspecification artifact\n4. **统计推断问题**: 域级显著性缺多重校正，ARC model fit 不合格，Appendix E power analysis 缺失\n\n要达到 Main Conference (≥4.0)，需要：\n(a) 至少一个 pretraining contamination 或 7B+ 模型的验证案例\n(b) 替代 γ 规范（item-level 或 interaction）的消融实验\n(c) 多重比较校正后仍成立的 domain-level evidence\n(d) RRF vs S1-only 的直接实证对比\n\n当前版本修复 claim scoping（MF1-MF2）、补充 PPP/校正（MF4-MF5）、提供 RRF ablation（MF6）后可作为有价值的 Findings paper。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ~258 words，超 ACL 推荐上限；数字过密（~10 个）\n- \"Raw accuracy is already well-calibrated\" 缺限定条件\n- 建议精简至 ~200 words，保留 2-3 关键数字\n\n### Introduction (§1)\n- 五段结构基本完整，但 \"surprising null result\" reveal 在 ¶4 才出现，更像实验报告而非故事驱动\n- 五个 Contributions 方向分散，建议合并为 2-3 个\n- Contribution 5 \"without multiple comparison correction\" 的脚注式说明不够——这直接影响结论成立性\n\n### Related Work (§2)\n- 四段结构清晰（detection, IRT, DIF, calibration disambiguation）\n- PSN-IRT 已引用且有 differentiation\n- 缺 Han et al. EACL 2026（最直接 concurrent work）\n- 缺 pretraining dose-response 文献\n- DIF 段落质量好，psychometric 连接准确\n\n### Method (§3)\n- 2PL+γ 模型公式规范，additive structure 解释清晰\n- RRF 的 meta-circularity 避免论证合理\n- 三个 Adaptations 在方法论上合理但呈现方式偏 didactic\n- 缺 e_ij 的经验分布报告\n- Identifiability 分析（Fisher information）论证充分\n\n### Experimental Setup (§4)\n- 受控实验设计是论文最强部分\n- 0.5B 排除有充分理由（position bias）\n- J=16 vs J=13 的差异来源（实验进度）应更 prominently 说明\n- §4.2 cross-family 引用了不存在的 Appendix E power analysis\n\n### Results (§5)\n- §5.1 calibration results 清晰呈现 null finding\n- Oracle ablation 是关键消融但解释一边倒\n- §5.2 signal failure modes 是有价值的 empirical finding\n- §5.3 identifiability boundaries 是重要理论贡献\n- §5.4 domain analysis: Table 2 缺 PPP，Social Sciences significance 缺多重校正\n- §5.5 cross-family: Table 4 呈现清晰，但 J=3-4 功效太低\n\n### Discussion & Conclusion (§6)\n- \"Why not just use raw accuracy\" 段落直接回应关键质疑，是好的写法\n- 但 Conclusion 仍以无条件语气声称 null finding\n- Future work 段过短，未讨论 pretraining contamination 的路径\n\n### Limitations\n- 九项 limitations 全面具体\n- CI coverage 和 additive γ linearity 的讨论应移入主文\n- SFT ecological validity 讨论有实质内容\n\n### Ethics Statement\n- 简洁合规\n\n### Appendix\n- Appendix A-D 内容合理\n- Appendix E 内容错误（标称 power analysis 实为 baseline tables）\n- Table 2 (domain γ) 和 Tables 5-6 补充了主文\n\n### 格式合规\n- ACL template + [review] option ✓\n- Double-blind ✓\n- Limitations/Ethics 位置正确 ✓\n- Em-dash/en-dash 检查通过 ✓\n- 引用格式 (natbib) 正确 ✓\n- 页数无法编译确认 ⚠️"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0",
    "report": "# 审稿报告 — Round 4 (Fresh Review)\n\n**论文**: \"Decomposing Contamination from Calibration: An IRT Approach to LLM Benchmark Evaluation\"\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026 cycle)\n**截止日期**: 2026-05-25\n\n**Reviewer 编排**: 2 名 Reviewer\n- Reviewer 1: 方法严谨性 + 实验设计 + 统计推断\n- Reviewer 2: 新颖性 + 论文完整性 + 写作质量 + 格式合规\n\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（无 REBUT，1 轮即达共识）\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 通过 Reciprocal Rank Fusion (RRF) 融合多种 contamination detection signals 生成 per-item exposure scores；Stage 2 将 exposure scores 嵌入 contamination-augmented IRT model (2PL+γ) 估计 decontaminated ability。核心实验在 Qwen2.5 (0.5B-3B) 上通过 LoRA SFT injection 在 MMLU/ARC/GSM8K 上进行受控 contamination 实验。主要发现是 null result：SFT-injected contamination 的 aggregate effect 仅 ~0.6-0.7pp，raw accuracy 已是最佳估计器，ContamCal 不优于 raw accuracy（Table 3: MAE 0.006 vs 0.009）。论文转向 diagnostic value 叙事，报告 γ 在 ARC 上 CI excluding zero 以及 MMLU Social Sciences 域级显著性。附带发现包括 Min-K%++ 在 0.5B 的 directional reversal 和 γ recovery 需 J≥50 的 identifiability 边界。\n\n---\n\n## Strengths\n\n1. **受控实验设计精良**：24 个模型（3 scales × 4 dosages × 2 seeds）的 within-family design 在 contamination 研究中少见，严格隔离 dosage 为唯一自变量（§4.1）。\n\n2. **诚实的科学态度**：坦率承认核心方法不优于 raw accuracy（Table 3），九项 limitations 全面且具体，negative result 的透明报告值得肯定。\n\n3. **Identifiability analysis 有理论价值**：Simulation study（20 conditions × 10 seeds × 200 runs）建立的 AUC/J 边界（§5.3, Figure 2）为未来 IRT-based contamination diagnosis 提供定量指导。\n\n4. **Min-K%++ directional reversal 发现有实用价值**：0.5B 上 Cohen's d = -1.55 to -1.98 的 reversal（§5.2）是重要的 practitioner warning，具有独立引用价值。\n\n5. **跨领域理论连接**：将 IRT item compromise/explanatory IRT/DIF 框架引入 LLM contamination analysis（§2 ¶3），理论基础扎实。\n\n6. **写作质量整体良好**：无 AI 写作标志（无 em-dash、-ing phrases 可控），术语定义完整（calibration disambiguation §2 ¶4），引用格式规范。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定，6 项）\n\n**[MF1] 标题/framing 与核心发现的叙事断裂** [R1: AGREE, R2: raised]\n- 标题 \"Decomposing Contamination from Calibration\" 暗示有效分解框架，但核心结论是 aggregate level 无需分解（~0.6-0.7pp）。论文以 methods paper 包装了 negative result。\"Diagnostic value\" pivot 在 §1 ¶4 才出现，与 Contribution 1 \"Empirical decomposition\" 措辞矛盾。\n- **建议**: 重新定位为实证调查（\"Does contamination need calibration?\"），而非方法论文（\"Here is ContamCal\"）。Introduction 从第一段即铺设 null 预期。\n\n**[MF2] SFT injection 的 ecological validity 不足以支撑无条件 claim** [R1: raised, R2: AGREE]\n- \"Raw accuracy is already well-calibrated\"（Abstract, §6）未加任何限定条件，但仅基于 LoRA SFT injection at ≤3B。Pretraining contamination 通过 trillion-token web crawl 分布式暴露，效应机制根本不同。Limitations §7 承认 \"qualitatively different signatures\"，但 claim 不受限。近期 pretraining-level dose-response 研究（arXiv 2601.04301）表明 pretraining contamination 效应显著更大。\n- **建议**: (1) Abstract/Introduction/Conclusion 所有 claim 限定为 \"under SFT injection at ≤3B scale\"；(2) 引用 pretraining contamination 文献作为对比锚点。\n\n**[MF3] Additive linear γ 假设未验证，oracle ablation 解释存在根本歧义** [R1: raised, R2: AGREE]\n- Oracle ablation（AUC=1.0 perfect labels, γ = -0.012, CI [-0.145, 0.119], PPP=0.41）有两种同等合理的解释：(a) 真的没效应（item-level heterogeneity 抵消）；(b) 有效应但 additive linear γ 捕捉不到（model misspecification）。论文只采信 (a)，但 Limitations ¶9 自己承认 threshold 行为可能导致 γ 被稀释为零。如果解释 (b) 成立，整个 2PL+γ 框架的诊断价值受质疑。\n- **建议**: 测试 item-level γ_i 或 γ×a_i 交互模型排除 misspecification；不可行则在所有 claim 中明确 \"under the linear additive specification\"。\n\n**[MF4] 域级 γ 显著性（Social Sciences 1/8）缺多重比较校正** [R1: raised, R2: AGREE]\n- 8 个 domain 独立检验，仅 Social Sciences 在 α=0.05 达到显著（γ = -0.57, CI [-1.05, -0.10]）。Bonferroni 校正后 α = 0.00625，CI 上界 -0.10 极可能越过零。BH 校正下 1/8 pattern 也大概率不通过。这是 \"diagnostic value\" 叙事的主要实证支撑——校正后消失则 Contribution 5 失去支持。\n- **建议**: 报告 Bonferroni/BH 校正后结果；校正后不显著则重新表述为 \"suggestive pattern requiring higher-powered replication\"。\n\n**[MF5] ARC PPP < 0.05 但 IRT 结果仍出现在主表** [R1: raised, R2: AGREE with nuance]\n- ARC 在所有 J 配置（8, 13, 16）下 PPP < 0.05（§5.4），2PL+γ 模型拟合不合格。但 Table 3 报告 ARC IRT 结果无 PPP 注脚。ARC 的 ~0.7pp raw data observation 有效，但 IRT-derived 数值不可靠。\n- **建议**: Table 3 ARC 列加 PPP 注脚；区分 raw observation vs IRT estimate 的可信度。\n\n**[MF6] RRF multi-signal fusion 被自身实验否定** [R2: raised, R1: AGREE with nuance]\n- S2 (Min-K%++) 在 0.5B 方向反转，S4 (Self-Critique) 在 <1.5B 近乎随机，§5.2 承认 \"RRF fusion degrades to S1-only\"。Contribution 2 声称 RRF-guided filtering 价值，但无 RRF vs S1-only 在 1.5B/3B 的直接消融。R1 补充：S2 在 3B 有 d≈+0.7，RRF 可能有 value，但必须提供实证。\n- **建议**: 提供 RRF vs S1-only 在 1.5B/3B 的对比（τ, MAE, γ）；如 RRF ≤ S1-only，降格 Contribution 2。\n\n---\n\n### Should-Fix（影响评分，11 项）\n\n**[SF1]** J 值跨分析不一致（13/16/24/18-28），全部远低于论文自证的 J≥50 threshold。所有 γ-based 结论本质上 underpowered。[R1, R2 AGREE]\n\n**[SF2]** RRF-filtered 300 items vs random 2000 items 的 τ 对比（0.73 vs 0.46）可能存在 item discrimination confound。RRF 可能系统性选出高 a_i items，与 contamination signal 无关。需报告 RRF vs random subset 的平均 a_i。[R1 raised, R2 AGREE]\n\n**[SF3]** CI coverage（MMLU 83%/89%/100%, ARC 45%/65%/90%）仅在 Limitations 报告。ARC under-coverage 与 PPP<0.05 互相印证 model misfit，应在主文讨论。[R1, R2 AGREE]\n\n**[SF4]** Cross-family validation J=3-4（Llama 单 seed），且 §4.2 引用的 \"Appendix E power analysis\" 实际内容为 baseline tables（sec:full_baselines），power analysis 内容缺失。[R1, R2 AGREE; R2 确认为 content error]\n\n**[SF5]** γ~N(0,1) 先验 sensitivity analysis 缺失。覆盖 ±2 logit units，若 effect 很小则 prior 选择对 posterior 影响实质性。需测试 N(0,0.5)/N(0,2) 并报告 e_ij 分布。[R1, R2 AGREE]\n\n**[SF6]** Min-K%++ reversal 因果解释（\"token-level surprisal disruption\"）仅为 post-hoc 假设，无直接验证。替代解释（position bias confound、near-full-rank LoRA）未排除。[R1 raised, R2: AGREE but considers minor]\n\n**[SF7]** Oracle ablation（§5.1）仅采信 \"effect heterogeneity\" 解释，未平衡讨论 \"model misspecification\" 可能性。[与 MF3 关联]\n\n**[SF8]** 五个 Contributions 覆盖 null finding / item filtering / signal failure / identifiability / domain diagnosis，方向过于分散。建议合并为 2-3 个核心贡献。[R2 raised, R1: AGREE with reservation]\n\n**[SF9]** 重要相关工作遗漏：Han et al. (EACL Findings 2026) \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" 是最直接的 concurrent work；arXiv 2601.04301 pretraining dose-response；Chen et al. (EMNLP 2025) contamination survey。此外缺 Bayesian workflow/model comparison 参考（WAIC/LOO-CV）。[R2 raised, R1: AGREE in principle]\n\n**[SF10]** Table 2 (domain γ) PPP 列全为 \"---\"——per-domain model fit 不可验证，特别是 Social Sciences 作为唯一 significant domain。[R1, R2 AGREE]\n\n**[SF11]** Abstract ~258 words（超 ACL 推荐 150-250），包含 ~10 个具体数字，信息过密。[R2 raised, R1 AGREE]\n\n---\n\n### Minor Issues（6 项）\n\n1. B2 (Single2PL+γ) 在 §4.4 定义但 Table 3 中缺失\n2. \"-ing phrases\" 在 Related Work 中偏多（\"confirming that...\", \"enabling both...\"）\n3. §3.2 \"Adaptation 1/2/3\" 命名风格偏 didactic\n4. `habba_2025_growing_pains` bib key 写 2025 但实际 year=2026\n5. Eq. 2 additive interpretation (\"difficulty shift by γ_k·e_ij/a_i\") 仅在 linearization 下成立，非精确\n6. 无法编译确认正文是否 ≤ 8 页\n\n---\n\n## Reviewer Consensus\n\n所有关键问题达成共识。交叉回应中：\n- R1 对 R2 的 9 个问题：7 × [AGREE]，2 × [AGREE with nuance]（R2-N3 RRF 和 R2-W2 贡献数量）\n- R2 对 R1 的 10 个问题：9 × [AGREE]，1 × [AGREE with nuance]（R1-N4 ARC ~0.7pp 来源区分）\n- 无任何 [REBUT]\n\n核心共识：\n1. **Null finding 的外部效度**是首要问题——SFT at ≤3B 不能泛化为 contamination 的一般性质\n2. **Linear additive γ 的模型充分性**存在根本歧义——oracle ablation 无法区分 null effect vs misspecification\n3. **Domain-level γ significance** 在多重比较校正后可能消失，削弱 diagnostic narrative\n4. **RRF** 在当前实验条件下缺乏超越 S1-only 的实证支持\n\n---\n\n## Reviewer Divergence\n\n无实质性分歧。仅有微小差异：\n- R1 对 RRF 贡献被否定的程度略保守（S2 在 3B 有 d≈+0.7），R2 更绝对\n- R2 认为 ARC ~0.7pp 在 Abstract 中可保留（来自 raw data 非 IRT），R1 倾向移除\n\n---\n\n## Questions（需作者澄清）\n\n1. Table 2 各 MMLU domain 的 PPP 值是多少？如果 Social Sciences PPP < 0.05，其 γ significance 是否可信？\n2. §4.2 声称 \"post-hoc power calculations in Appendix E\"——Appendix E (sec:full_baselines) 实际为 baseline tables。Power analysis 是否存在？\n3. 在 1.5B/3B 上，RRF (S1+S2+S4) vs S1-only 的 τ/MAE/γ significance 对比结果如何？\n4. 如果将 γ 替换为 item-level γ_i 或 γ×a_i 交互项，oracle ablation 中是否能检测到 item-level contamination effects？\n5. RRF-selected 300 items 的平均 discrimination (a_i) 与 random 2000 items 相比如何？\n\n---\n\n## Missing References\n\n| 论文 | 严重程度 | 理由 |\n|------|----------|------|\n| Han et al. (EACL Findings 2026) \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" | **高** | 直接将 psychometric/IRT + contamination 结合，最接近的 concurrent work |\n| arXiv 2601.04301 (2026) \"Quantifying the Effect of Test Set Contamination on Generative Evaluations\" | **高** | Pretraining-level dose-response，与 null finding 形成关键对比 |\n| Chen et al. (EMNLP 2025) contamination survey | **中** | 领域最全面综述 |\n| arXiv 2411.03923 \"Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?\" | **中** | Contamination measurement meta-analysis |\n| Gelman et al. (2020) \"Bayesian Workflow\" / Gabry et al. (2019) Bayesian visualization | **低** | 先验选择和 PPP 的标准方法论参考 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n**Confidence: 4/5**\n\n**评分依据 (EMNLP 2026 ARR scale)**:\n- 3.0 = Findings（可被 Findings 接收）\n\n**理由**:\n论文提出了一个有价值的研究问题（IRT 能否分离 contamination 和 ability），实验设计严谨（受控 SFT injection, within-family design），且诚实报告 null result。Identifiability 分析和 Min-K%++ reversal 发现有独立价值。\n\n但核心问题阻碍了 Main Conference 接收：\n1. **方法不 work**: ContamCal 在其自身实验中不优于 trivial baseline (raw accuracy)\n2. **Null finding 范围受限**: 仅 SFT at ≤3B，不能推广到 pretraining contamination（最实际的场景）\n3. **Model specification 歧义**: Linear γ 的 null result 可能是 misspecification artifact\n4. **统计推断问题**: 域级显著性缺多重校正，ARC model fit 不合格，Appendix E power analysis 缺失\n\n要达到 Main Conference (≥4.0)，需要：\n(a) 至少一个 pretraining contamination 或 7B+ 模型的验证案例\n(b) 替代 γ 规范（item-level 或 interaction）的消融实验\n(c) 多重比较校正后仍成立的 domain-level evidence\n(d) RRF vs S1-only 的直接实证对比\n\n当前版本修复 claim scoping（MF1-MF2）、补充 PPP/校正（MF4-MF5）、提供 RRF ablation（MF6）后可作为有价值的 Findings paper。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- ~258 words，超 ACL 推荐上限；数字过密（~10 个）\n- \"Raw accuracy is already well-calibrated\" 缺限定条件\n- 建议精简至 ~200 words，保留 2-3 关键数字\n\n### Introduction (§1)\n- 五段结构基本完整，但 \"surprising null result\" reveal 在 ¶4 才出现，更像实验报告而非故事驱动\n- 五个 Contributions 方向分散，建议合并为 2-3 个\n- Contribution 5 \"without multiple comparison correction\" 的脚注式说明不够——这直接影响结论成立性\n\n### Related Work (§2)\n- 四段结构清晰（detection, IRT, DIF, calibration disambiguation）\n- PSN-IRT 已引用且有 differentiation\n- 缺 Han et al. EACL 2026（最直接 concurrent work）\n- 缺 pretraining dose-response 文献\n- DIF 段落质量好，psychometric 连接准确\n\n### Method (§3)\n- 2PL+γ 模型公式规范，additive structure 解释清晰\n- RRF 的 meta-circularity 避免论证合理\n- 三个 Adaptations 在方法论上合理但呈现方式偏 didactic\n- 缺 e_ij 的经验分布报告\n- Identifiability 分析（Fisher information）论证充分\n\n### Experimental Setup (§4)\n- 受控实验设计是论文最强部分\n- 0.5B 排除有充分理由（position bias）\n- J=16 vs J=13 的差异来源（实验进度）应更 prominently 说明\n- §4.2 cross-family 引用了不存在的 Appendix E power analysis\n\n### Results (§5)\n- §5.1 calibration results 清晰呈现 null finding\n- Oracle ablation 是关键消融但解释一边倒\n- §5.2 signal failure modes 是有价值的 empirical finding\n- §5.3 identifiability boundaries 是重要理论贡献\n- §5.4 domain analysis: Table 2 缺 PPP，Social Sciences significance 缺多重校正\n- §5.5 cross-family: Table 4 呈现清晰，但 J=3-4 功效太低\n\n### Discussion & Conclusion (§6)\n- \"Why not just use raw accuracy\" 段落直接回应关键质疑，是好的写法\n- 但 Conclusion 仍以无条件语气声称 null finding\n- Future work 段过短，未讨论 pretraining contamination 的路径\n\n### Limitations\n- 九项 limitations 全面具体\n- CI coverage 和 additive γ linearity 的讨论应移入主文\n- SFT ecological validity 讨论有实质内容\n\n### Ethics Statement\n- 简洁合规\n\n### Appendix\n- Appendix A-D 内容合理\n- Appendix E 内容错误（标称 power analysis 实为 baseline tables）\n- Table 2 (domain γ) 和 Tables 5-6 补充了主文\n\n### 格式合规\n- ACL template + [review] option ✓\n- Double-blind ✓\n- Limitations/Ethics 位置正确 ✓\n- Em-dash/en-dash 检查通过 ✓\n- 引用格式 (natbib) 正确 ✓\n- 页数无法编译确认 ⚠️"
  }
}
```

</details>

---


### Tool result

_source line 369 · 2026-05-17T17:42:13.391476+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4075
}
```

</details>

---


### Assistant

_source line 370 · 2026-05-17T17:42:24.089566+00:00_

审稿报告已投递至 Research Director。

**审稿完成总结**：

- **Overall Score: 3.0 (Findings)**，两位 Reviewer 评分一致
- **Must-Fix 6 项**: 叙事断裂、SFT ecological validity 未限定、linear γ misspecification 歧义、域级多重比较缺失、ARC PPP<0.05 未标注、RRF 缺 ablation
- **Should-Fix 11 项**: J 值不一致、item discrimination confound、CI coverage 位置、cross-family power（含 Appendix E 内容缺失）、prior sensitivity、Min-K%++ 因果假设、oracle 解释偏颇、贡献过散、missing references（Han et al. EACL 2026 最紧急）、Table 2 PPP 缺失、Abstract 过长
- **共识度极高**: 交叉回应中 0 个 REBUT，核心分歧仅在措辞程度

Review issues tracker 已同步更新至 `artifacts/review_issues.yaml`（Round 4）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 31

## Round 31

2 recorded events


### User

_source line 371 · 2026-05-17T17:42:26.542010+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。R1 的 10 个问题中 AGREE 9 个、AGREE with nuance 1 个。关键新发现：Appendix E 声称包含 power analysis 但实际内容是 baseline comparison tables，属于内容缺失/引用错误。评分维持 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 372 · 2026-05-17T17:42:39.881667+00:00_

审稿报告已于交叉回应收敛后提交至 Research Director。

**本轮审稿完成总结**：

- **Overall Score**: 3.0 (Findings)
- **Reviewer 共识**: 完全收敛（0 REBUT），1 轮即达共识
- **6 个 Must-Fix**: 标题叙事断裂、SFT ecological validity 无条件 claim、additive γ misspecification 歧义、域级多重比较校正缺失、ARC PPP<0.05 主表无注脚、RRF 缺 S1-only 消融
- **11 个 Should-Fix**: J 值不一致/underpowered、item discrimination confound、CI coverage 位置、cross-family power+Appendix E 内容缺失、prior sensitivity、Min-K%++ 因果解释、oracle ablation 解释、贡献过多、missing references (Han et al. EACL 2026 等)、Table 2 PPP 缺失、Abstract 超长
- **Issue Tracker**: 已同步更新至 `artifacts/review_issues.yaml`（含 Round 4 全部新发现、复发问题、已解决标注）
- **报告已投递**: `submit_review_report_to_research_director` 完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 32

## Round 32

2 recorded events


### User

_source line 373 · 2026-05-17T17:48:07.630266+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：idle 240min
  本轮累计 1 条消息 / 4h 2min

⚠️ 你自己的 context 状态：已 1 条消息 / 4h 2min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 374 · 2026-05-17T17:48:13.482558+00:00_

审稿报告已在本轮完成并投递，圆桌会议已收敛，无后续审稿任务。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 33

## Round 33

2 recorded events


### User

_source line 375 · 2026-05-17T19:27:41.803213+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：idle 240min
  本轮累计 2 条消息 / 4h 2min

⚠️ 你自己的 context 状态：已 2 条消息 / 4h 2min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 376 · 2026-05-17T19:27:48.954787+00:00_

审稿报告已通过 `submit_review_report_to_research_director` 投递完成，Issue Tracker 已同步更新。本轮审稿工作全部收敛，无待处理任务。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 34

## Round 34

2 recorded events


### User

_source line 377 · 2026-05-17T20:30:09.693691+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：运行时长 8h18m
  本轮累计 80 条消息 / 8h 18min

⚠️ 你自己的 context 状态：已 80 条消息 / 8h 18min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 378 · 2026-05-17T20:30:21.434570+00:00_

[RESET BOTH]

本轮审稿已完成：审稿报告已通过 `submit_review_report_to_research_director` 投递，issue tracker 已更新至 Round 4。无待办事项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 35

## Round 35

2 recorded events


### User

_source line 379 · 2026-05-17T21:38:14.745008+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 4h54m
  本轮累计 26 条消息 / 4h 54min

⚠️ 你自己的 context 状态：已 26 条消息 / 4h 54min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 380 · 2026-05-17T21:38:26.654897+00:00_

本轮审稿已完成——审稿报告已通过 `submit_review_report_to_research_director` 投递，issue tracker 已同步更新。我的工作已收敛。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 36

## Round 36

2 recorded events


### User

_source line 381 · 2026-05-17T21:52:19.526410+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：idle 240min
  本轮累计 1 条消息 / 4h 3min

⚠️ 你自己的 context 状态：已 1 条消息 / 4h 3min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 382 · 2026-05-17T21:52:25.833053+00:00_

本轮审稿工作已全部完成。审稿报告已通过 `submit_review_report_to_research_director` 投递，Issue Tracker 已同步更新。没有待处理的审稿任务。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 37

## Round 37

2 recorded events


### User

_source line 383 · 2026-05-17T23:49:20.845962+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：idle 240min
  本轮累计 1 条消息 / 4h 20min

⚠️ 你自己的 context 状态：已 1 条消息 / 4h 20min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 384 · 2026-05-17T23:49:30.409072+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 38

## Round 38

2 recorded events


### User

_source line 385 · 2026-05-18T01:05:16.205511+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：idle 316min
  本轮累计 1 条消息 / 5h 36min

⚠️ 你自己的 context 状态：已 1 条消息 / 5h 36min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 386 · 2026-05-18T01:05:22.910090+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 39

## Round 39

2 recorded events


### User

_source line 387 · 2026-05-18T01:05:24.416085+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：idle 120min
  本轮累计 7 条消息 / 3h 26min

⚠️ 你自己的 context 状态：已 7 条消息 / 3h 26min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 388 · 2026-05-18T01:05:29.903792+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 40

## Round 40

70 recorded events


### User

_source line 389 · 2026-05-18T01:26:53.788676+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contamcal-irt-calibration
- 论文路径: projects/contamcal-irt-calibration/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Findings
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-18T01:27:00.503365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 391 · 2026-05-18T01:27:00.554921+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 392 · 2026-05-18T01:27:03.668265+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 393 · 2026-05-18T01:27:03.769502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 394 · 2026-05-18T01:27:07.991767+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,director_post_to_reviewer,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,director_post_to_reviewer,request_external_review,get_external_review_status,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-18T01:27:08.042679+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-18T01:27:11.228955+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-18T01:27:11.280832+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-18T01:27:15.354792+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 399 · 2026-05-18T01:27:16.764402+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (278 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_006_mmlu_vanilla_2pl_fullitems | Full MMLU 14k items vanilla 2PL IRT to compute more robust Kendall tau ranking correlation (replacing 300 subsampled items version) | — | — | — |\n\n## 待处理\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\n- signals_05B_s123_batch（准备中）\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\n- exp_001_sft_15B_d025_s123（准备中）\n- exp_001_sft_3B_d000_v4（准备中）\n- exp_001_sft_3B_d000_s42（准备中）\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\n- exp_001_sft_d005_05B_r3: 0.5B d005 SFT retry #3 after OOM, superseded by later successful runs (v3 PID 239729)（准备中）\n- exp_001_eval_3B_d025_s123: 3B d025 seed=123 aligned eval for pooled IRT N
…[truncated 2657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1409
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-18T01:27:16.865452+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-18T01:27:17.217646+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Does LLM Benchmark Contamination Need Calibration?\\An IRT Decomposition Study}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{conclusion}
29	
30	\input{limitations}
31	\input{ethics}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-18T01:27:17.368734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-18T01:27:17.720570+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-18T01:27:24.890578+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

I found information about EMNLP 2026 submission guidelines related to ARR (ACL Rolling Review). Here are the key findings:

## EMNLP 2026 Submission Struct
…[truncated 1414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 7521
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-18T01:27:24.941388+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7220
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-18T01:27:29.781091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit template ARR deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit template ARR deadline"
  }
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-18T01:27:30.134605+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format guidelines page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format guidelines page limit"
  }
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-18T01:27:31.724896+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-18T01:27:31.976857+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-18T01:27:32.032808+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-18T01:27:32.083796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-18T01:27:36.420355+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit template ARR deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's what I found about EMNLP 2026 submission guidelines:

## ARR Deadline
The ARR submission deadline is May 25, 2026.

## Submission Guidelines
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Page Limits
Unfortunately, the search results don't includ
…[truncated 834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6639
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-18T01:27:36.421032+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format guidelines page limit"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here are the submission format guidelines and page limits for ACL Rolling Review 2026:

## Page Limits

All ARR submissions are anonymous and in the format of a short paper (up to 4 pages) or long paper (up to 8 pages). Additionally, review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references.

For short papers specifically, short papers may consist of up to four (4) p
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6286
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-18T01:27:41.734774+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-18T01:27:41.785631+00:00_

1	Training data contamination undermines the validity of Large Language Model (LLM) benchmark comparisons, yet existing detection methods stop at binary flags without quantifying score inflation. We investigate whether Item Response Theory (IRT) can separate genuine ability from contamination artifacts on existing benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B--3B) and three benchmarks (MMLU, ARC-Challenge, GSM8K), we find that under SFT injection at $\leq$3B, contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7 percentage points, smaller than the estimation noise of any correction method; raw accuracy is already well-calibrated. We develop ContamCal, a two-stage pipeline combining signal-guided item filtering with a contamination-augmented IRT model (2PL+$\gamma$). Item filtering improves calibration ($\tau = 0.73$ on 300 RRF-selected items vs.\ $\tau = 0.46$ on random 2000-item subsets, $\Delta\tau = 0.27$). The $\gamma$ parameter reveals domain-level heterogeneity: Social Sciences shows the strongest negative effect ($\gamma = -0.57$, posterior $P(\gamma<0) = 99.1\%$) within the Qwen family, a pattern requiring higher-powered replication. We further document that Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$). Simulation studies establish that reliable $\gamma$ recovery requires signal AUC $\geq 0.55$ and $J \geq 50$, exposing a structural gap between current practice and the statistical requirements for contamination diagnosis via IRT.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-18T01:27:42.291451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-18T01:27:42.698809+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination undermines the validity of these scores in ways that current evaluation cannot quantify \citep{hendrycks2021mmlu,chang2025benchmarking}. When models encounter test items during training, observed accuracy conflates genuine capability with memorization, and practitioners have no principled way to determine how much of a reported score reflects real understanding. The problem is compounded by the scale of modern training corpora: trillion-token web crawls make contamination pervasive and instance-level measurement infeasible \citep{oren2024proving}. Post-hoc calibration that quantifies contamination effects despite imperfect detection is therefore essential for trustworthy evaluation.
4	
5	Two developments make this gap urgent. First, \citet{sun2025emperor} systematically evaluate twenty contamination mitigation strategies (rephrasing, option shuffling, dynamic benchmark regeneration, and others) and demonstrate that none restores clean performance after contamination has occurred. This result forecloses the ``prevent contamination'' approach for models already trained on unrestricted web data. Second, contamination-free benchmarks \citep{white2024livebench} offer a partial solution but sacrifice the comparability and institutional knowledge accumulated around established benchmarks. Dynamic regeneration of test items may also be contaminated within weeks as web crawlers index benchmark repositories \citep{dong_2024_cdd}. The field therefore needs post-hoc statistical tools that can separate genuine ability from contamination artifacts on existing benchmarks.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at detection. They d
…[truncated 3792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 407
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-18T01:27:42.699399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-18T01:27:43.160869+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination detection and mitigation.}
5	Membership inference for contamination detection builds on the foundations of training data extraction \citep{carlini_2021_extracting} and membership inference attacks \citep{shokri_2017_mia}. Current approaches include Min-K\% \citep{shi_2023_minkprob} and Min-K\%++ \citep{zhang_2024_minkpp} (token-level surprisal), ConStat \citep{dekoninck2024constat} (accuracy gaps on paraphrased items), CDD/TED \citep{dong_2024_cdd} (completion-based probes), KDS \citep{choi_2025_kds} (kernel divergence), TS-Guessing \citep{deng_2024_tsguessing} (temporal splits), and Time Travel \citep{golchin_2024_time_travel} (guided generation probes). Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method for RL-trained models. \citet{kocyigit2025impact} show that post-training procedures (RLHF, DPO) degrade detection signal reliability; token-level methods become unreliable on instruction-tuned models. \citet{zhang_2024_gsm1k} construct GSM1K as a parallel test set to quantify GSM8K contamination: performance gaps between original and regenerated items serve as a natural experiment for contamination measurement. Recent surveys \citep{chen2025benchmarking,singh2024evaluation} systematically categorize these approaches. These methods flag contamination but do not produce adjusted scores. On the mitigation side, \citet{sun2025emperor} systematically evaluate twenty approaches and find that none reliably restores clean performance; inference-time decontamination \citep{yang2024inference} and decontamination via forgetting \citep{zhang2025forget} similarly show limited effectiveness. DCR \citep{xu2025dcr} estimates decontaminated scores via fuzzy inference but produces point estimates without uncertainty quantification or domain-level diagnosis. ContamCal consumes detection signals as inputs and feeds them into a calibration framework that estimates decon
…[truncated 2815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 461
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-18T01:27:43.161415+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-18T01:27:44.120404+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Shared item pool.} A fixed item set is shared across all models, introducing residual correlations beyond scalar $\theta_j$ \citep{sanmartin_2009_irt}; we mitigate by fitting per-benchmark models.
14	\textit{Continuous exposure.} We replace binary leakage indicators with continuous scores $e_{ij} \in [0,1]$ derived from detection signals, as LLM contamination is graded rather than binary.
15	\textit{Counterfactual ability.} Training regime changes (SFT vs.\ RL) alter both representations and signal reliability; we recover clean ability via counterfactual inference (setting $e_{ij}=0$) rather than regime-specific parameters.
16	
17	\subsection{Stage 1: Multi-Signal Exposure Mapping}
18	\l
…[truncated 5746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-18T01:27:44.271801+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-18T01:27:44.624508+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 \citep{qwen2024qwen25} at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with Low-Rank Adaptation \citep[LoRA;][]{hu2022lora} ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123), yielding 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B models from MMLU and ARC IRT due to answer-position bias that correlates with dosage (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). Three initial 3B checkpoints trained with inconsistent LoRA hyperparameters were retrained under the unified protocol ($\alpha=32$, lr$=5\times10^{-5}$; Appendix~\ref{sec:exclusion_details}). Our pooled calibration analysis (Table~\ref{tab:baselines}) uses $J=16$ respondents for MMLU/ARC (1.5B$\times$8 + 3B$\times$8) and $J=24$ for GSM8K (all scales retained). Domain-level $\gamma$ analysis (Table~\ref{tab:domain_gamma}, \S\ref{sec:domain_differential}) uses $J=13$ (1.5B$\times$8 + 3B$\times$5), as it preceded completion of the 3B retraining. The eight 1.5B d000 models serve as the clean reference anchor in both configurations.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B \citep{grattafiori202
…[truncated 2344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 424 · 2026-05-18T01:27:44.625044+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-18T01:27:45.130029+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.46$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, enabling sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates. The $\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\text{exposure}, a_i} = -0.013$).
9	
10	\paragraph{RRF vs.\ single-signal ablation.}
11	Replacing RRF with S1-only exposure for item selection and IRT fitting causes convergence failure: MMLU S1-only yields $\hat{R} = 1.53$ (ESS$=$7), while ARC S1-only converges to a degenerate solution ($\gamma = 6.84$, PPP$=$0.000). The root cause is exposure variance compression: S1-only top-300 items concentrate in a narrow score band ($[0.749, 0.867]$), creating collinearity between $\gamma \cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions that enable $\gamma$ identification. RRF's value is therefore not only signal quality aggregation but exposure variance for IRT parameter separability. To control for subset size, we evaluated random 300-item subsets (5 seeds, $J=16$): $\tau = 0.554 \pm 0.048$, significantly lower than RRF-selected items ($\tau = 0.731$, $\Delta\tau = 0.177$), confirming that signal-guided item selection provides a mea
…[truncated 14646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-18T01:27:45.130513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-18T01:27:45.583405+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We investigated whether IRT can separate ability from contamination artifacts on LLM benchmarks, finding three results: (1)~under SFT injection at $\leq$3B, aggregate contamination effects are negligible (${\sim}$0.6--0.7pp), so raw accuracy is already well-calibrated and no correction method improves upon it; (2)~Min-K\%++ exhibits directional reversal at small scales; (3)~domain-level $\gamma$ is exploratory at $J=13$, requiring $J \geq 50$ for confirmation.
4	
5	\paragraph{Why not just use raw accuracy?}
6	Under SFT injection at $\leq$3B, the contamination effect is near zero (${\sim}$0.6--0.7pp), making raw accuracy the best aggregate estimator. IRT's value is not in improving MAE but in the decomposition analysis that \textit{explains why}: $\gamma$ quantifies that the effect is too small to distort rankings, provides a contamination existence diagnostic (Social Sciences posterior $P(\gamma<0) = 99.1\%$, robust to prior specification; Appendix~\ref{sec:prior_sensitivity}), and reveals domain-level heterogeneity invisible to aggregate scoring. If future contamination produces larger effects (e.g., pretraining-phase exposure), the framework applies directly with no methodological changes. B6-DCR's systematic overcorrection (MAE 0.108--0.314) demonstrates the practical risk of correction methods that assume large effects without measurement-theoretic grounding.
7	
8	\paragraph{Circularity.}
9	Filtering items by exposure signal and then fitting IRT is not circular: $\tau$ measures $\theta$-dosage rank correlation, not $\gamma$ significance, and the oracle ablation confirms that even perfect binary labels do not produce a significant pooled $\gamma$.
10	
11	\paragraph{Implications and future work.}
12	Min-K\%++ should not be trusted at the 0.5B scale. The negligible aggregate effect under SFT injection does not preclude larger effects under pretraining contamination \citep{schaeffer2026causally}; scali
…[truncated 90 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-18T01:27:45.583807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-18T01:27:46.041015+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify nine limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Signal coverage.}
10	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
11	
12	\paragraph{Ensemble size and per-domain power.}
13	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$) yields a strong directional signal (posterior $P(\gamma<0) > 99\%$) for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
14	
15	\paragraph{Position bias.}
16	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100), necessitating exclusion from MC IRT analyses and reducing ensemble size.
17	
18	\paragraph{Credible interval coverage.}
19	CI coverage is benchmark-dependent (\S\ref{sec:calibration_results}), computed on 18 checkpoints for MMLU and 20 for ARC. The model does not provide uniformly calibrated uncertainty across benchmarks.
20	
21	\paragraph{Model misfit in non-STEM domains.}
22	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. Richer specifications may be required.
23	
24	\paragraph{SFT ecological validity.}
25	We use LoRA-based SFT injection exclusively. Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures: distributed exposure across many training steps rather than concentrated fine-tuning. The position bias observed at 0.5B (A-option rate escalating from 46\% t
…[truncated 1091 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-18T01:27:46.041470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-18T01:27:47.001550+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5 and Llama-3.2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 960
}
```

</details>

---


### Tool call

_source line 432 · 2026-05-18T01:27:47.153250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-18T01:27:47.508962+00:00_

1	\appendix
2	
3	\section{4PL Extension}
4	\label{sec:4pl_details}
5	
6	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
7	\begin{equation}
8	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
9	\end{equation}
10	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
11	
12	\section{Model Exclusion Details}
13	\label{sec:exclusion_details}
14	
15	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
16	
17	\paragraph{Model sets across analyses.}
18	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
19	
20	\begin{table}[h]
21	\centering
22	\caption{Model set composition across analyses.}
23	\label{tab:model_sets}
24	\footnotesize
25	\begin{tabular}{lcll}
26	\toprule
27	Analysis & $J$ & Model Set & Section \\
28	\midrule
29	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
30	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
31	Cross-family & 16--
…[truncated 7143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-18T01:27:48.012770+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers page limit long short paper anonymity",
  "allowed_domains": "['2026.emnlp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers page limit long short paper anonymity",
    "allowed_domains": "['2026.emnlp.org']"
  }
}
```

</details>

---


### Tool call

_source line 435 · 2026-05-18T01:27:48.520027+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_checklist.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "paper_checklist.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 436 · 2026-05-18T01:28:03.227579+00:00_

Web search results for query: "EMNLP 2026 call for papers page limit long short paper anonymity"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Organizing Committee - EMNLP 2026 - SIGDAT","url":"https://2026.emnlp.org/organization/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

I found information about the anonymity policy, but I need to search more specifically for the page limits for long and short papers at EMNLP 2026.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorial
…[truncated 5409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 15214
}
```

</details>

---


### Tool result

_source line 437 · 2026-05-18T01:28:03.278578+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 14758
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-18T01:28:08.689652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review call for papers 2026 page limit long paper short paper format requirements",
  "allowed_domains": "['aclrollingreview.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review call for papers 2026 page limit long paper short paper format requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 439 · 2026-05-18T01:28:10.203923+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 440 · 2026-05-18T01:28:10.558618+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 354
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-18T01:28:11.222618+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 442 · 2026-05-18T01:28:11.575227+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-18T01:28:11.575704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-18T01:28:11.828506+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices"
3	  category: framing
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 2
7	  last_seen_round: 4
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
12	  action_items:
13	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
14	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
15	    - {round: 4, action: "Reframe as empirical investigation ('does contamination need calibration?') rather than method paper ('here is ContamCal')", assigned_to: "paper_agent", status: "done"}
16	  resolution: ""
17	  resolution_round: null
18	
19	- id: "R2-W6"
20	  summary: "SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property"
21	  category: experiment
22	  severity: critical
23	  status: in_progress
24	  first_raised_round: 2
25	  last_seen_round: 4
26	  mentions:
27	    - {round: 2, reviewers: "R1,R2", note: "Intro motivates with pretraining but experiments only SFT."}
28	    - {round: 3, reviewers: "R1,R2", note: "Limitations one sentence only."}
29	    - {round: 4, reviewers: "R1,R2", note: "Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without
…[truncated 31432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-18T01:28:14.906776+00:00_

Web search results for query: "ACL Rolling Review call for papers 2026 page limit long paper short paper format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Changelog – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/changelog"}]

Based on the search results from the ACL Rolling Review Call for Papers, here are the key page limit and format requirements fo
…[truncated 1040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6217
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-18T01:28:45.294071+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-18T01:28:46.401169+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 1107
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-18T01:28:46.552240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-18T01:28:46.603294+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{carlini_2021_extracting,
6	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
7	  title     = {Extracting Training Data from Large Language Models},
8	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
9	  year      = {2021},
10	  url       = {https://arxiv.org/abs/2012.07805}
11	}
12	
13	@inproceedings{choi_2025_kds,
14	  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},
15	  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},
16	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
17	  year      = {2025},
18	  url       = {https://arxiv.org/abs/2502.00678}
19	}
20	
21	@inproceedings{cormack_2009_rrf,
22	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
23	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
24	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
25	  pages     = {758--759},
26	  year      = {2009},
27	  publisher = {ACM},
28	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
29	}
30	
31	@book{deboeck_2004_explanatory_irt,
32	  author    = {De Boeck, Paul and Wilson, Mark},
33	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
34	  publisher = {Springer},
35	  year      = {2004},
36	  address   = {New York},
37	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
…[truncated 21099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-18T01:28:51.351706+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-18T01:28:51.402430+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_director_c2ad40d8.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-18T01:28:54.179559+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-18T01:28:54.281660+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T155040/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/dream_20260513T171200/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/dream_reports/
…[truncated 6795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-18T01:29:48.312124+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "project": "contamcal-irt-calibration",
  "text": "## Round 5 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (通过 ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper ≤ 8 页正文 + 无限 references/appendix; Limitations/Ethics 不计入页数\n- **模板**: ACL style, `[review]` option, double-blind\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n`projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节为独立 .tex 文件：abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n\n### 你的审查侧重\n**方法严谨性 + 实验有效性**，重点关注：\n\n1. **IRT 建模**\n   - 2PL+γ 模型的统计假设是否合理（additive linear γ, independent per-domain fitting）\n   - γ identifiability 分析（Fisher information, simulation study 设计）\n   - 贝叶斯推断设置（priors, convergence diagnostics, PPP interpretation）\n   - Prior sensitivity analysis 的充分性\n\n2. **实验设计**\n   - SFT injection 作为 contamination proxy 的生态效度（ecological validity）\n   - Model exclusion 逻辑（0.5B 排除、3B checkpoint 重训练、Llama d100 排除）\n   - J 值在不同分析中的不一致性（13/16/24/28）及其对结论的影响\n   - Cross-family analysis（Llama J=4, single seed）的统计功效\n\n3. **核心发现的可靠性**\n   - Null finding（~0.6-0.7pp aggregate effect）是否可能是 SFT artifact 而非 general property\n   - Oracle ablation 的双重解释（genuine null vs model misspecification）\n   - Social Sciences γ=-0.57 是否在多重比较校正下存活\n   - ARC PPP < 0.05 对 ARC 相关结论的影响\n\n4. **信号分析**\n   - RRF vs S1-only ablation 的完整性\n   - Min-K%++ directional reversal 的因果解释\n   - Signal AUC heatmap 的覆盖度\n\n### 历史审稿关键 issue（供参考，但请独立评估当前论文）\n- R2-W6 (critical): SFT ecological validity — 所有 claims 是否已限定为 \"under SFT injection at ≤3B\"\n- R3-W10 (critical): Additive linear γ assumption — oracle ablation 是否同时讨论了 null effect 和 misspecification 两种解释\n- R4-N1 (critical): 8 domains 中仅 1 个 significant — 是否有多重比较讨论\n- R3-N3 (critical): ARC PPP < 0.05 — IRT-derived ARC 结果是否有充分 caveat\n- R2-W1 (critical): RRF 在 1.5B/3B 退化为 S1-only — 是否有 ablation 证据\n\n请提供完整审稿报告，包括 Summary, Strengths, Weaknesses（逐条编号），Questions, Overall Assessment（使用 EMNLP 评分标准），Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "project": "contamcal-irt-calibration",
    "text": "## Round 5 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (通过 ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper ≤ 8 页正文 + 无限 references/appendix; Limitations/Ethics 不计入页数\n- **模板**: ACL style, `[review]` option, double-blind\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n`projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节为独立 .tex 文件：abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n\n### 你的审查侧重\n**方法严谨性 + 实验有效性**，重点关注：\n\n1. **IRT 建模**\n   - 2PL+γ 模型的统计假设是否合理（additive linear γ, independent per-domain fitting）\n   - γ identifiability 分析（Fisher information, simulation study 设计）\n   - 贝叶斯推断设置（priors, convergence diagnostics, PPP interpretation）\n   - Prior sensitivity analysis 的充分性\n\n2. **实验设计**\n   - SFT injection 作为 contamination proxy 的生态效度（ecological validity）\n   - Model exclusion 逻辑（0.5B 排除、3B checkpoint 重训练、Llama d100 排除）\n   - J 值在不同分析中的不一致性（13/16/24/28）及其对结论的影响\n   - Cross-family analysis（Llama J=4, single seed）的统计功效\n\n3. **核心发现的可靠性**\n   - Null finding（~0.6-0.7pp aggregate effect）是否可能是 SFT artifact 而非 general property\n   - Oracle ablation 的双重解释（genuine null vs model misspecification）\n   - Social Sciences γ=-0.57 是否在多重比较校正下存活\n   - ARC PPP < 0.05 对 ARC 相关结论的影响\n\n4. **信号分析**\n   - RRF vs S1-only ablation 的完整性\n   - Min-K%++ directional reversal 的因果解释\n   - Signal AUC heatmap 的覆盖度\n\n### 历史审稿关键 issue（供参考，但请独立评估当前论文）\n- R2-W6 (critical): SFT ecological validity — 所有 claims 是否已限定为 \"under SFT injection at ≤3B\"\n- R3-W10 (critical): Additive linear γ assumption — oracle ablation 是否同时讨论了 null effect 和 misspecification 两种解释\n- R4-N1 (critical): 8 domains 中仅 1 个 significant — 是否有多重比较讨论\n- R3-N3 (critical): ARC PPP < 0.05 — IRT-derived ARC 结果是否有充分 caveat\n- R2-W1 (critical): RRF 在 1.5B/3B 退化为 S1-only — 是否有 ablation 证据\n\n请提供完整审稿报告，包括 Summary, Strengths, Weaknesses（逐条编号），Questions, Overall Assessment（使用 EMNLP 评分标准），Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-18T01:30:11.140717+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 22828
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-18T01:30:11.191609+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "project": "contamcal-irt-calibration",
  "text": "## Round 5 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (通过 ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper ≤ 8 页正文 + 无限 references/appendix; Limitations/Ethics 不计入页数\n- **模板**: ACL style, `[review]` option, double-blind\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n`projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节为独立 .tex 文件：abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n\n### 你的审查侧重\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **新颖性与贡献评估**\n   - 核心技术贡献（2PL+γ）相对 standard explanatory IRT/DIF 的增量\n   - 与 Han et al. EACL 2026 (IRT+contamination), PSN-IRT (IRT+prompt sensitivity) 的差异化\n   - Null finding 作为 EMNLP Findings 论文的贡献是否足够\n   - \"框架虽然不改善 calibration 但有 diagnostic value\" 这个 pitch 是否有说服力\n\n2. **叙事一致性（最重要）**\n   - Title (\"Does LLM Benchmark Contamination Need Calibration?\") → Abstract → Introduction → Results → Conclusion 是否一条主线\n   - Contribution 1-3 是否在前文有充分铺垫\n   - \"Null finding + diagnostic value\" 叙事是否自洽：如果 aggregate effect 只有 0.6-0.7pp，为什么还需要 IRT 框架？论文是否回答了这个自然质疑？\n   - Framing 是 empirical investigation（测试一个假设）还是 method paper（提出 ContamCal）？两种 framing 是否有混淆？\n\n3. **Related Work 完整性**\n   - 引用覆盖度（43 条引用）是否达到 EMNLP 标准\n   - 与最相关工作的对比深度：DCR, Han et al. EACL 2026, PSN-IRT, HiBayES\n   - DIF/explanatory IRT 文献的覆盖（教育测量领域的经典工作）\n   - 是否有遗漏的重要参考文献\n\n4. **写作质量**\n   - Abstract 是否在 150-250 words 内清楚回答四个核心问题\n   - 是否有 AI 写作痕迹（em-dash, -ing phrases, 过度分段, 术语堆砌）\n   - 图表信息密度和视觉质量\n   - Limitations 是否充分覆盖（9 条是否遗漏关键限制）\n   - Ethics Statement 是否完整\n\n5. **格式合规**\n   - 页数是否在 8 页正文限制内\n   - Limitations 和 Ethics 位置（应在 conclusion 后、references 前）\n   - 匿名化（作者信息、代码链接、自引处理）\n   - 引用格式（natbib 兼容性）\n\n### 历史审稿关键 issue（供参考，但请独立评估当前论文）\n- R2-N1 (critical): Title/framing mismatch — 标题承诺 decomposition+calibration 但核心发现是 raw accuracy suffices\n- R4-W3 (warning): 贡献列表是否精简到 2-3 条核心 contribution\n- R4-W6 (warning): Abstract 是否已精简到 ≤250 words 且数字密度适中\n- R3-N7 (warning): Novelty — 技术贡献有限（standard IRT+DIF），价值在 empirical 层面\n- R2-W8 (warning): Related Work 引用覆盖度\n\n请提供完整审稿报告，包括 Summary, Strengths, Weaknesses（逐条编号），Questions, Missing References, Overall Assessment（使用 EMNLP 评分标准），Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "project": "contamcal-irt-calibration",
    "text": "## Round 5 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 (通过 ACL Rolling Review)\n- **Deadline**: 2026-05-25\n- **格式**: Long paper ≤ 8 页正文 + 无限 references/appendix; Limitations/Ethics 不计入页数\n- **模板**: ACL style, `[review]` option, double-blind\n- **评分标准**: EMNLP 2026 通过 ARR 统一审稿，Overall Assessment: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 论文路径\n`projects/contamcal-irt-calibration/docs/paper/main.tex`（各章节为独立 .tex 文件：abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n\n### 你的审查侧重\n**新颖性 + 完整性 + 写作质量**，重点关注：\n\n1. **新颖性与贡献评估**\n   - 核心技术贡献（2PL+γ）相对 standard explanatory IRT/DIF 的增量\n   - 与 Han et al. EACL 2026 (IRT+contamination), PSN-IRT (IRT+prompt sensitivity) 的差异化\n   - Null finding 作为 EMNLP Findings 论文的贡献是否足够\n   - \"框架虽然不改善 calibration 但有 diagnostic value\" 这个 pitch 是否有说服力\n\n2. **叙事一致性（最重要）**\n   - Title (\"Does LLM Benchmark Contamination Need Calibration?\") → Abstract → Introduction → Results → Conclusion 是否一条主线\n   - Contribution 1-3 是否在前文有充分铺垫\n   - \"Null finding + diagnostic value\" 叙事是否自洽：如果 aggregate effect 只有 0.6-0.7pp，为什么还需要 IRT 框架？论文是否回答了这个自然质疑？\n   - Framing 是 empirical investigation（测试一个假设）还是 method paper（提出 ContamCal）？两种 framing 是否有混淆？\n\n3. **Related Work 完整性**\n   - 引用覆盖度（43 条引用）是否达到 EMNLP 标准\n   - 与最相关工作的对比深度：DCR, Han et al. EACL 2026, PSN-IRT, HiBayES\n   - DIF/explanatory IRT 文献的覆盖（教育测量领域的经典工作）\n   - 是否有遗漏的重要参考文献\n\n4. **写作质量**\n   - Abstract 是否在 150-250 words 内清楚回答四个核心问题\n   - 是否有 AI 写作痕迹（em-dash, -ing phrases, 过度分段, 术语堆砌）\n   - 图表信息密度和视觉质量\n   - Limitations 是否充分覆盖（9 条是否遗漏关键限制）\n   - Ethics Statement 是否完整\n\n5. **格式合规**\n   - 页数是否在 8 页正文限制内\n   - Limitations 和 Ethics 位置（应在 conclusion 后、references 前）\n   - 匿名化（作者信息、代码链接、自引处理）\n   - 引用格式（natbib 兼容性）\n\n### 历史审稿关键 issue（供参考，但请独立评估当前论文）\n- R2-N1 (critical): Title/framing mismatch — 标题承诺 decomposition+calibration 但核心发现是 raw accuracy suffices\n- R4-W3 (warning): 贡献列表是否精简到 2-3 条核心 contribution\n- R4-W6 (warning): Abstract 是否已精简到 ≤250 words 且数字密度适中\n- R3-N7 (warning): Novelty — 技术贡献有限（standard IRT+DIF），价值在 empirical 层面\n- R2-W8 (warning): Related Work 引用覆盖度\n\n请提供完整审稿报告，包括 Summary, Strengths, Weaknesses（逐条编号），Questions, Missing References, Overall Assessment（使用 EMNLP 评分标准），Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-18T01:30:12.757030+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1565
}
```

</details>

---


### Assistant

_source line 458 · 2026-05-18T01:30:21.033761+00:00_

Round 5 审稿任务已分配：
- **Reviewer 1**（方法严谨性 + 实验有效性）— 已触发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）— 已触发

等待两位 Reviewer 返回独立初审结果，收到后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 41

## Round 41

2 recorded events


### User

_source line 459 · 2026-05-18T01:34:23.587761+00:00_

[Reviewer 1 审稿意见]:
## Round 5 审稿报告 — Reviewer 1（方法严谨性 + 实验有效性）

**论文**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall Assessment**: 3.0 (Findings)
**一句话总结**: 方法框架合理且报告诚实，但核心 null finding 受限于 SFT 生态效度、additive γ 可能 misspecified、唯一 significant domain finding 未经多重比较校正，实际贡献度有限。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法论总体合理但存在关键假设未验证（additive linear γ vs oracle null）、多重比较缺失、ARC model fit 不合格仍报告结果 |
| Excitement | 2.5/5 | 问题本身有价值（bridging detection and calibration），但 null finding + 严格限定条件（SFT ≤3B）大幅降低实际影响力 |
| Reproducibility | 4/5 | 实验细节充分，模型配置、超参、排除逻辑均有说明；Stan 代码未提及是否开源 |
| Confidence | 4/5 | 我对 IRT、贝叶斯推断、LLM 评估文献熟悉，对本文方法和统计分析有信心评估 |

---

## Summary

本文提出 ContamCal，一个两阶段框架：Stage 1 用 RRF 融合多个检测信号生成连续 exposure score，Stage 2 将其嵌入 2PL+γ IRT 模型进行校准。在 Qwen2.5 (0.5B-3B) 的 SFT injection 实验中发现：(1) 聚合 contamination 效应仅~0.6-0.7pp，raw accuracy 已是最优估计；(2) Min-K%++ 在 0.5B 出现方向反转；(3) domain-level γ 在 Social Sciences 显示 P(γ<0)=99.1% 的方向信号。论文对 null finding 的报告坦诚透明，identifiability simulation 和 prior sensitivity analysis 增加了方法论价值。

---

## 主要优势

1. **问题定位精准**: 将 detection 和 calibration 两条独立文献桥接，填补了 "检测后怎么办" 的空白（§1, Related Work §2）。
2. **Null finding 的负责任报告**: 不过度渲染方法有效性，坦承 raw accuracy 优于所有校正方法（Table 3），并解释 why（效应太小，校正 overshoot）。
3. **Identifiability simulation 有方法论价值**: J≥50 at AUC≥0.55 的边界条件为社区提供了 IRT-based contamination 研究的操作指南（Figure 2, §4.3）。
4. **RRF vs S1-only ablation 信息量大**: 揭示了 exposure variance compression 导致 IRT convergence failure 的机制（§4.1），不仅是方法设计决策的 justification，也是对 IRT 应用的实践洞察。
5. **Prior sensitivity analysis 区分了 prior-dominated vs data-dominated 结论**: Pooled γ 随 prior 变化 2.6×，Social Sciences 仅变化 1.2×（Appendix C, Table 6），方法论上严谨。
6. **写作质量高**: 逻辑清晰、主线统一、limitations 部分诚实（9条），讨论部分直面 "why not raw accuracy" 的核心质疑。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Oracle ablation 无法区分 genuine null 与 model misspecification，但结论未充分限定

- 具体位置：§4.1 Oracle ablation paragraph, §6 Limitations "Additive γ linearity"
- 问题：Oracle ablation（ground-truth binary labels, AUC=1.0）产出 γ=-0.012 (CI [-0.145, 0.119])，论文提出两种解释：(a) 真实效应接近零，(b) additive linear γ 是 misspecified。但论文在 Abstract、Introduction contribution list、Conclusion 中将 "aggregate contamination effects are negligible" 作为核心发现，未在这些位置同等强调 misspecification 可能性。如果 γ 是 misspecified（例如 threshold-like effect），则 "0.6-0.7pp" 这个数字本身可能就是 model artifact，不能作为 "不需要校准" 的证据。
- 为什么影响接收：这是论文的核心 claim（Contribution 1），如果两种解释不能区分，claim 的可信度被根本性削弱。
- 建议修改方向：(1) 在 Abstract/Introduction 中明确写 "under the additive linear specification" 或 "assuming linear contamination effects"；(2) 提供 non-linear specification（如 threshold model 或 piecewise linear）的 oracle 结果作为对比；如果不可行，至少将 misspecification caveat 提升到 Conclusion 的显著位置而非仅在 Limitations 中提及。

**N2** [critical] Social Sciences γ=-0.57 未经多重比较校正

- 具体位置：§4.4 Table 4, §4.1 "Diagnostic value of γ" paragraph
- 问题：8 个 MMLU domain 独立检验，仅 Social Sciences 达到 P(γ<0)=99.1%。按 Bonferroni 校正（α=0.05/8=0.00625），阈值为 P(γ<0)≥99.375%，Social Sciences 不通过。按 Holm-Bonferroni 或 FDR 控制结果类似。论文完全没有讨论多重比较问题。
- 为什么影响接收：这是论文 Contribution 3 的核心证据。如果校正后不显著，论文的三个贡献中有两个是纯 null finding（Contribution 1 和 3），大幅降低 novelty。
- 建议修改方向：(1) 报告 Bonferroni/FDR-adjusted p-values；(2) 如果校正后不显著，将 Social Sciences finding 明确降级为 "suggestive pattern requiring replication"（目前措辞已接近但不够明确）；(3) 考虑用 hierarchical prior (partial pooling across domains) 替代独立 domain fitting 来自然控制 shrinkage。

**N3** [critical] ARC PPP<0.05 下的 ARC 结果呈现方式

- 具体位置：Table 3 caption ("PPP=0.003; IRT-derived ARC estimates should be interpreted with caution"), §4.4 ("ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)")
- 问题：PPP=0.003 表明 2PL+γ 模型对 ARC 数据的 fit 不可接受。论文仍在 Table 3 中与 MMLU 并列报告 ARC 的 MAE 和 τ，给读者留下两者同等可靠的印象。Caption 中的 caveat 很容易被忽略。更严重的是，§4.4 确认 ARC 在所有 J 配置下 PPP 都 <0.05，这意味着 2PL+γ 从结构上不适合 ARC 数据，而非样本量不足。
- 为什么影响接收：Table 3 是论文支撑 Contribution 1（raw accuracy 最优）的核心证据。如果 ARC 列的 IRT 结果无效，则 "calibration across benchmarks" 的结论仅靠 MMLU 一个 benchmark 支撑。
- 建议修改方向：(1) 将 ARC IRT 结果移入 Appendix 并标注 "model fit unacceptable"；(2) 或在 Table 3 中用灰色/删除线标注 ARC IRT 行；(3) 讨论 ARC 为什么 fit 差（item discrimination 分布？ceiling effect？format mismatch？）。

**N4** [critical] SFT injection 生态效度限制了核心 claim 的适用范围

- 具体位置：§3.1, §6 Limitations "SFT ecological validity", Abstract ("Under SFT injection at ≤3B"), Title
- 问题：论文标题 "Does LLM Benchmark Contamination Need Calibration?" 暗示的是通用结论，但所有证据仅来自 LoRA SFT injection at ≤3B。真实世界 contamination 发生在 pretraining 阶段（trillion-token web crawl），机制完全不同：(a) exposure 分布在数百万 training steps 中而非集中在几百步 SFT；(b) pretraining contamination 不会引入 instruction formatting artifact；(c) pretraining 对 larger models 的效应可能更大。论文在 Limitations 中承认这一点并引用 Schaeffer et al. (2026)，但 Introduction §1 para 4 ("Our experiments yield a surprising null result") 和 Conclusion 的 framing 不够限定。
- 为什么影响接收：如果 SFT injection 是一个不能代表真实 contamination 的 proxy，则整个实验装置的外部有效性存疑。审稿人会问：为什么我应该相信 SFT injection 的 null finding 能推广到 pretraining contamination？
- 建议修改方向：(1) 标题改为更限定的版本，如 "IRT Decomposition of SFT-Injected Benchmark Contamination"；(2) Introduction 中显式讨论 SFT vs pretraining contamination 的已知差异，而非仅在 Limitations 中提及；(3) 如有 pretraining contamination 的间接证据（如 Schaeffer et al. 的数据），进行简要对比。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] J 值跨分析的不一致性削弱方法论连贯性

- 具体位置：§3.1 (J=16/24), §4.4 (J=13), Table 5 (cross-family J=18/28/20), Appendix B Table 1
- 问题：核心分析使用 J=13（domain-level），pooled baselines 使用 J=16，cross-family 使用 J=18-28。差异原因是 "domain-level runs preceded completion of 3B retraining"（§3.1）。这意味着 domain-level analysis（论文最有趣的 finding）是在不完整数据上进行的，后续的完整数据（J=16）并没有用于重新验证 domain-level 结果。
- 建议：在 J=16 配置下重跑 domain-level γ 分析，或解释为什么没有这样做。

**W2** [warning] Cross-family analysis (Llama J=4, single seed) 统计功效不足以支撑结论

- 具体位置：§3.2, §4.5
- 问题：Llama 分析仅 4 个模型（d000/d005/d025/d100 各 1 个 seed）。论文标注为 "exploratory" 但仍在 §4.5 得出结论："calibration generalizes; diagnosis does not" 和 "θ estimation generalizes across model families"。从 J=4 single-seed 数据得出跨 family 泛化结论过于强烈。另外 Llama d100 MMLU 被排除（catastrophic format collapse），说明 Llama 的 SFT injection 机制与 Qwen 根本不同，进一步质疑跨 family 结论的有效性。
- 建议：降低结论强度为 "preliminary evidence"，或增加 Llama 的 seed 数量。

**W3** [warning] RRF 在 1.5B/3B 实际上被 S1 主导，但论文强调 "multi-signal fusion is necessary"

- 具体位置：§4.2 Signal reliability, §4.1 RRF vs S1 ablation
- 问题：Figure 1 显示 S1 在所有 scale/dosage 组合下 AUC>0.95，而 S2/S4 在 0.5B 近似随机、1.5B+ 仅 marginal。那么在 1.5B/3B，RRF 本质上是 S1 signal + noise from S2/S4。论文声称 "multi-signal fusion is necessary"（§4.1），但实际的 ablation 证据仅表明 S1-only *item selection* 导致 exposure variance compression（score band [0.749, 0.867]）。这是 item selection 的属性，不是 signal quality aggregation 的属性。RRF 的价值可能仅仅是引入了 rank-based variance，而非真正的 multi-signal information gain。
- 建议：区分 "RRF is necessary for exposure variance" 与 "RRF provides superior signal quality"。目前的表述混淆了这两个概念。可以报告 S1 + random perturbation 是否也能达到类似的 exposure variance。

**W4** [warning] Min-K%++ 方向反转的因果解释不充分

- 具体位置：§4.2 "Min-K%++ directional reversal" paragraph
- 问题：Cohen's d=-1.55 to -1.98 是非常大的 effect size。论文提出三个可能解释（SFT 破坏 token-level fluency、position bias confound、near-full-rank LoRA）但均未验证。如果 position bias 是真正原因（0.5B 模型 A-option rate 达 98%），那这不是 Min-K%++ 本身的 failure，而是 SFT injection 在 0.5B 产生了 catastrophic behavior 的副产品。论文已排除 0.5B from IRT analyses，但仍将 Min-K%++ reversal 作为独立 finding（Contribution 2），这可能是在描述 SFT artifact 而非 Min-K%++ 的固有缺陷。
- 建议：测试 Min-K%++ 在 non-SFT 0.5B models（如原始 Qwen2.5-0.5B vs 其他公开 0.5B models）上的行为，以区分 scale-dependent failure 和 SFT-specific artifact。

**W5** [warning] Credible interval coverage 不均匀且解释不足

- 具体位置：§4.1 "Credible interval coverage is benchmark-dependent"
- 问题：MMLU 严重 over-coverage（50% CI covers 83%），ARC under-coverage（50% CI covers 45%）。论文仅说 "reflecting differential model fit quality" 但未深入。Over-coverage 意味着 posterior 过度 dispersed（CI 太宽），实际上不提供有意义的 uncertainty quantification。在 MMLU 上，95% CI 覆盖 100% 意味着 CI 完全无信息。
- 建议：讨论 over-coverage 的原因（prior 太宽？model 过参数化？item response heterogeneity？）并考虑是否影响 "ContamCal provides calibrated uncertainty" 的 claim。

---

## 小问题（不影响接收）

1. §2 Method Eq.1: RRF normalization 是 per-model min-max，这意味着不同 model 之间的 $e_{ij}$ 不可比较。但 IRT 将不同 model 的 response 放在同一模型中，$\gamma_k \cdot e_{ij}$ 的 cross-model 解释需要讨论。
2. Table 3: B1b 的 "b" 未解释（似乎有 B1a 但未在正文中出现）。
3. §4.4: "ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)" — 在多个 J 下都不 fit 的事实应更早引入（在 Table 3 之前），否则读者先看到 ARC 结果再被告知不可靠。
4. Appendix B: "three 3B checkpoints were removed: two had mismatched naming conventions" — 这暗示 pipeline 工程问题而非有原则的排除。应更清楚地说明这些 checkpoint 是否包含有效数据。
5. Ethics Statement 过于简短，未讨论 ContamCal 被用于不当目的（如 gaming 排行榜）的可能性。
6. §1 "our primary pipeline uses the remaining three signals (S = {S1, S2, S4})" — 但 S2/S4 在大部分 scale 上 near-random，这意味着 "primary pipeline" 实质上接近 S1-only。

---

## Questions for Authors

1. 是否可以在 J=16 配置下重跑 domain-level γ 分析以确认 Social Sciences finding？
2. Oracle ablation 中，是否尝试过 non-linear specifications（如 $\gamma \cdot \mathbb{1}[e_{ij} > \tau]$ 或 piecewise linear）来区分 genuine null 和 misspecification？
3. RRF 的 exposure variance 贡献是否可以通过 S1 + uniform noise 复现？如果可以，那 S2/S4 的实际 signal contribution 是什么？
4. 如何回应以下质疑：SFT injection 在 ≤3B 可能根本不是 contamination 的有效 proxy（因为 SFT 修改的参数比例远大于 pretraining exposure），因此 null finding 只说明 "SFT 不能有效制造 contamination-like score inflation"？
5. Stan 代码和实验数据是否计划开源？

---

## Overall Assessment

**3.0 — Findings**

论文提出了一个有价值的框架（将检测信号嵌入 IRT 进行校准），实验设计在受控条件下合理，null finding 的报告诚实透明。但存在以下根本限制：(1) SFT injection 作为 contamination proxy 的生态效度存疑，核心 null finding 可能仅反映 proxy 的局限性而非 contamination 的真实属性；(2) additive linear γ 的 oracle ablation 无法区分 genuine null 和 misspecification；(3) 唯一 significant domain finding 未经多重比较校正；(4) ARC benchmark 上 model fit 不可接受但仍与 MMLU 并列报告。这些问题使得三个贡献中有效贡献度有限：Contribution 1 受 N1/N4 限制，Contribution 3 受 N2 限制，Contribution 2（signal failure mode documentation）是 solid 但属于 empirical observation 而非方法论贡献。综合来看，论文适合 Findings track：方法框架有参考价值，null finding 对社区有信息量，但证据强度和影响力不足以支撑主会议接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 460 · 2026-05-18T01:34:30.832548+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 461 · 2026-05-18T01:34:33.470765+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交。

核心评价：**Overall 3.0 (Findings)**。方法框架合理、null finding 报告诚实，但四个 critical issue 限制了贡献度——(1) oracle ablation 无法区分 genuine null 与 γ misspecification 却未在核心 claim 中充分限定，(2) Social Sciences 唯一 significant finding 不过 Bonferroni 校正，(3) ARC PPP=0.003 下结果仍并列呈现，(4) SFT injection 生态效度限制了 "不需要校准" 这一核心结论的外推性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 462 · 2026-05-18T01:34:40.387836+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 43

## Round 43

6 recorded events


### User

_source line 463 · 2026-05-18T01:39:51.088075+00:00_

[Reviewer 2 审稿意见]:
## Round 5 审稿报告 — Reviewer 2（新颖性 + 完整性 + 写作质量）

**论文**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 方法论严谨、null finding 有价值的实证研究，但技术新颖性有限（标准 explanatory IRT/DIF 的领域迁移）、实验范围过窄（SFT injection ≤3B），且主要页面超限。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法严谨（Bayesian IRT + NUTS + convergence diagnostics），但结论受限于 SFT-only ≤3B 范围；null finding 在此范围内充分支撑，但无法回答 pretraining contamination 或 7B+ 模型的关键问题 |
| Excitement | 2.5/5 | Null finding 本身有信息量但不令人兴奋；Min-K%++ reversal 和 identifiability boundaries 是实用贡献，但框架未能超越 raw accuracy 削弱了方法论的影响力 |
| Reproducibility | 4/5 | LoRA 超参、Stan priors、convergence criteria、dosage levels 均有详细说明；但代码和数据未公开（blind review 可理解） |
| Overall Assessment | 3.0 | Findings 级别：有用的实证知识，但新颖性和范围限制了影响力 |
| Confidence | 4/5 | 熟悉 IRT、contamination detection 和 LLM evaluation 领域 |

---

## Summary

本文提出 ContamCal，一个两阶段框架：Stage 1 通过 RRF 融合多个 contamination detection signals 生成连续 exposure scores；Stage 2 在 2PL IRT 模型中加入 γ 参数建模 contamination 效应。在 Qwen2.5 (0.5B-3B) 上通过 SFT injection 进行 controlled experiments，得到核心 null finding：aggregate contamination effect 仅 ~0.6-0.7pp，raw accuracy 已经 well-calibrated。框架的价值被重新定位为 diagnostic（domain-level γ 异质性分析）而非 calibration。附带贡献包括 Min-K%++ 在 0.5B 的 directional reversal 发现和 γ recovery 的 identifiability boundary 分析。

---

## 主要优势

**S1. 诚实的 null finding 报告。** 在 publication bias 严重的领域中，坦诚报告框架未能超越 raw accuracy 是值得肯定的。论文没有 cherry-pick 有利结果，而是系统性地展示了为什么 correction 不必要（Section 5.1, Table 3）。

**S2. 严谨的统计方法论。** Bayesian inference via NUTS with proper convergence diagnostics（split-R̂ < 1.01, bulk ESS > 400），prior sensitivity analysis（Appendix C, Table showing Social Sciences γ is data-dominated），oracle ablation（replacing RRF with ground-truth labels），simulation study for identifiability boundaries——这些都超出了 NLP 论文的典型统计规范。

**S3. Min-K%++ directional reversal 的发现。** Section 5.2 documenting Cohen's d = -1.55 to -1.98 at 0.5B 是一个 practically important 且此前未报告的 failure mode，对 contamination detection 实践有直接指导意义。

**S4. Identifiability boundary analysis。** Figure 2 和 Section 5.3 建立了 γ recovery 需要 AUC ≥ 0.55 + J ≥ 50 的定量条件，为未来 IRT-based LLM evaluation 提供了 actionable design guidelines。

**S5. 写作质量整体良好。** 无 em-dash，无显著 AI 写作痕迹。Calibration disambiguation paragraph（Related Work 最后一段）是一个很好的预防性澄清。Limitations section 涵盖 9 条，覆盖面广。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 页面超限：主要内容超出 8 页
- 具体位置：PDF page 9
- 问题：Tables 2 和 3（属于 Section 5 Results 的主体内容）float 到 page 9 顶部，Discussion and Conclusion 的尾部文本也延续到 page 9，Limitations 约在 page 9 的 60% 处才开始。主要内容（含 floating tables）约占 8.5-8.6 页。ACL Long paper 限制 ≤ 8 页正文（Limitations/Ethics/References/Appendix 不计）。
- 为什么影响接收：页面超限可能导致 desk reject。即使不被 desk reject，也会给审稿人留下作者不尊重格式要求的印象。
- 建议修改方向：(1) 将 Table 2（per-domain γ）移至 Appendix，正文只保留 Social Sciences 的关键数字和 Figure 3 的引用；(2) 压缩 Section 5.1 的 "RRF vs. single-signal ablation" 段落（当前 ~15 行），核心 message 可用 3-4 句概括；(3) Table 3 可考虑 inline 报告 MAE/τ 数值，省略表格格式。

**N2** [critical] 技术新颖性有限：2PL+γ 本质上是 standard explanatory IRT / DIF 的领域应用
- 具体位置：Section 3.2 (Eq. 2), Related Work paragraph 3
- 问题：论文自己在 Related Work 中承认 "ContamCal's γ parameter is formally an instance of explanatory DIF"。与 Han et al. EACL 2026 的差异仅在于 continuous (vs. binary) exposure scores 和 domain-level stratification——这是 modeling 细节的变体，不是方法论创新。PSN-IRT 也在类似框架下将 item covariates 嵌入 IRT。2PL+γ 的 additive 结构（Eq. 2）是 DIF 文献中的标准形式。
- 为什么影响接收：对于 method paper 而言，核心贡献应有显著的技术增量。如果定位为 empirical study，则 ContamCal 的方法论贡献被进一步弱化。
- 建议修改方向：(1) 明确定位为 empirical investigation 而非 method paper——标题和 Introduction 暗示方法贡献，但实际贡献在 empirical 层面；(2) 更坦诚地在 Introduction 中说明 2PL+γ 建模本身不是创新，创新在于将其与 multi-signal fusion 结合并在 controlled setting 下进行系统性验证；(3) 与 Han et al. 做更细致的对比实验，而非仅在 Related Work 中文字区分。

**N3** [critical] 叙事不一致：Framing 在 method paper 和 empirical investigation 之间摇摆
- 具体位置：Title, Introduction (¶1-3 vs. ¶4-5), Contribution list, Conclusion
- 问题：
  - Title 副标题 "An IRT Decomposition Study" 暗示 method contribution
  - Introduction ¶1-3 花大量篇幅论证 "post-hoc calibration is essential"，建立了 calibration 是核心目标的期待
  - 但 Results 发现 raw accuracy 最好（Table 3），framework 的价值被转向 diagnostic
  - Contribution 1 是 null finding，Contribution 2 是 signal filtering 的技术细节，Contribution 3 是 exploratory diagnosis——三条贡献分属不同类型（empirical finding / engineering trick / exploratory analysis），缺乏统一主线
  - "Why not just use raw accuracy?" 段落（Conclusion）在反驳自己论文存在的必要性
- 为什么影响接收：审稿人在读完 Introduction 后期待一个 calibration 方法的改进结果，却在 Section 5 得到 null finding。这种期待落差会严重影响论文的说服力。
- 建议修改方向：从第一段就以 empirical investigation 的 framing 切入："We ask whether IRT-based calibration is necessary for contaminated LLM benchmarks, and find that under SFT injection at ≤3B, it is not." 将 ContamCal 定位为研究工具（investigative instrument）而非最终产品。Contribution list 精简为 2 条：(1) 实证发现 + identifiability analysis；(2) 诊断价值 + signal failure modes。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Abstract 数字密度过高
- 具体位置：abstract.tex（202 words，8-9 个具体数值）
- 问题：Abstract 中包含 ~0.6-0.7pp, τ=0.73, τ=0.46, Δτ=0.27, γ=-0.57, P(γ<0)=99.1%, d=-1.55 to -1.98, AUC≥0.55, J≥50 等数字。每 ~22 个单词就有一个数字，读起来像 Results 的压缩版而非独立故事。
- 建议：保留 2-3 个最关键的数字（aggregate effect ~0.6-0.7pp, identifiability threshold J≥50），其余用定性描述替代。例如 "item filtering substantially improves IRT calibration" 替代具体 τ 值。

**W2** [warning] 实验范围过窄，null finding 的普适性存疑
- 具体位置：Section 4.1 (SFT injection only, ≤3B)
- 问题：论文结论仅基于 SFT injection（LoRA fine-tuning）在 ≤3B 模型上的实验。论文自己承认 "pretraining-phase contamination, which may produce larger effects, remains an open question"（Introduction ¶4）和 "Larger models (7B+) may exhibit qualitatively different contamination dynamics"（Limitations ¶1）。现实中最关心的 contamination 场景是 pretraining phase 的 web crawl contamination（如 GPT-4, Llama-70B 等），而本文的 SFT injection 设置与之差异很大。
- 建议：(1) 在 Introduction 中更早、更明确地 scope 论文的发现（"We investigate SFT injection contamination at small scales; pretraining contamination at larger scales may produce different results"）；(2) 如果可能，增加 1-2 个 naturally contaminated model（如使用 GSM1K 的 parallel test set 数据）作为生态效度验证。

**W3** [warning] "Diagnostic value" 叙事的说服力不足
- 具体位置：Section 5.1 ¶3 "Diagnostic value of γ", Conclusion ¶1
- 问题：论文将 γ 的价值从 calibration 转向 diagnosis，声称其揭示了 "domain-level heterogeneity"。但 (1) 只有 8 个 MMLU domain 中的 1 个（Social Sciences）显示 strong directional signal（P(γ<0)=99.1%）；(2) 论文自己的 identifiability analysis 说明 J=13 不足以做 confirmatory analysis；(3) domain patterns 是 family-specific 的，不跨架构推广。一个在 8 个 domain 中只有 1 个显著、且被论文自己标记为 "exploratory" 和 "requiring higher-powered replication" 的发现，作为核心 contribution 之一的支撑显得单薄。
- 建议：降低对 diagnostic value 的 claim 强度。将 Contribution 3 ("Exploratory domain-level diagnosis") 从正式贡献降级为 "preliminary observation"，或在 Contribution 描述中更明确标注这只是一个 suggestive pattern。

**W4** [warning] Cross-family validation 统计效力不足
- 具体位置：Section 4.2, Section 5.5
- 问题：Llama-3.2-3B 只用 single seed 产生 J=4 个 model，且 d100 on MMLU 因 catastrophic format collapse 被排除。这不是真正的 "validation"——single-seed, J=4, 排除异常点后 effective dosage range 只到 d025。论文称之为 "exploratory" 是正确的，但 Section title "Cross-Family Validation" 暗示了更强的验证力度。
- 建议：将 Section 5.5 标题改为 "Cross-Family Exploration" 或 "Preliminary Cross-Family Analysis"。

**W5** [warning] 与 Han et al. EACL 2026 的差异化不够深入
- 具体位置：Related Work ¶2（最后两句）
- 问题：Han et al. 同样使用 psychometric DIF 来 quantify contamination effects on item parameters，这与 ContamCal 的核心思路高度重叠。论文仅用一句话 "Neither models contamination as a continuous covariate for score calibration" 来区分，但 (1) 连续 vs. 二值 exposure 只是 modeling choice，不是 paradigm shift；(2) 论文自己的 oracle ablation（Section 5.1）用 binary labels（AUC=1.0）也未产生显著 γ，说明 continuous vs. binary 的区别在此设置下不影响结论。
- 建议：增加 1-2 段对比分析，说明两种方法在相同或可比设置下的行为差异。如果无法做实验对比，至少在 conceptual level 说明 ContamCal 提供了什么 Han et al. 不能提供的 insight。

**W6** [warning] -ing 分词短语结尾模式
- 具体位置：散见于多个 section
- 问题：method.tex line 11 "adapting these frameworks through three structural modifications for LLM evaluation"；method.tex line 29 "avoiding the meta-circularity of learned aggregators"；method.tex line 20 "making it applicable to any benchmark"。虽然密度不高，但多处出现-ing 分词短语收尾，属于轻度 AI 写作痕迹。
- 建议：改写为完整句子。如 "adapting..." → "we adapt..."；"avoiding..." → "which avoids..."。

---

## 小问题（不影响接收）

**M1.** Introduction ¶3 "No existing method bridges detection signals and a measurement-theoretic calibration framework to produce decontaminated ability estimates with credible intervals." 这个 novelty claim 需要考虑 Han et al. EACL 2026 是否已经部分 bridge 了这个 gap。

**M2.** Table 3 caption 中 "ARC IRT results use pooled J=16 with PPP=0.003; IRT-derived ARC estimates should be interpreted with caution due to marginal model fit" 放在 caption 里过长，建议移至正文。

**M3.** Conclusion "Min-K%++ should not be trusted at the 0.5B scale" 措辞过强——directional reversal 是在 SFT injection 设置下观察到的，是否推广到 pretraining contamination 场景未经验证。

**M4.** Ethics Statement 过于简略（4 句），可补充对 contamination detection 的 dual-use 风险讨论（例如恶意利用 detection signals 来优化 contamination 策略）。

**M5.** 引用验证发现 10 条 "not_found"（多为较新论文或书籍章节，OpenAlex 未收录），10 条 "mismatch"（多为 author name format 差异）。无严重引用问题，但建议核实 holland_1993_dif（API 返回 year=2009, author=Osterlind）和 deboeck_2004_explanatory_irt（API 返回 year=2005）的元数据准确性。

**M6.** 未引用 IRT 经典文献（Lord 1980; Hambleton, Swaminathan & Rogers 1991）。虽然论文主要建立在 explanatory IRT 传统上（已引 De Boeck & Wilson 2004），但作为深度使用 2PL 模型的论文，引用 Birnbaum (1968) 或 Lord (1980) 是学科惯例。

**M7.** Method Section 3.1 定义了 $y_{ijk}$ 中的 $k$ 为 benchmark index，但在 Eq. 2 中 $k$ 变成了 stratum/domain index。这个符号复用虽在上下文可理解，但应明确说明 $k$ 在不同公式中的含义变化。

---

## Missing References（可能遗漏的重要参考文献）

1. **Lord, F. M. (1980).** "Applications of Item Response Theory to Practical Testing Problems." ETS. — IRT 奠基性教科书，使用 2PL 模型的论文通常引用。
2. **Hambleton, R. K., Swaminathan, H., & Rogers, H. J. (1991).** "Fundamentals of Item Response Theory." Sage. — 另一本 IRT 标准参考。
3. **Liang, P., et al. (2023).** "Holistic Evaluation of Language Models (HELM)." TMLR. — LLM evaluation 的重要框架，与本文的 evaluation 主题高度相关。
4. **Magar, I. & Schwartz, R. (2022).** "Data Contamination: From Memorization to Exploitation." ACL. — 直接讨论 data contamination 机制，与本文主题相关。

---

## 格式合规检查

| 项目 | 状态 | 说明 |
|------|------|------|
| 页数 | ❌ | 主要内容（含 floating tables）约 8.5 页，超出 8 页限制 |
| 模板 | ✅ | ACL style, `[review]` option |
| 匿名化 | ✅ | author = "Anonymous"，PDF 显示 "Anonymous ACL submission" |
| 行号 | ✅ | Review 模式行号可见 |
| Limitations 位置 | ✅ | Conclusion → Limitations → Ethics → References → Appendix |
| 引用格式 | ✅ | natbib, citep/citet 使用正确 |
| em-dash | ✅ | 全文无 em-dash (—) |
| en-dash | ✅ | 全文无解释性 en-dash ( – ) |
| 引用完整性 | ✅ | 48 bib entries, 48 unique cited keys, 0 orphan, 0 missing |

---

## Questions for Authors

**Q1.** 如果在 7B+ 模型上 SFT injection 产生 >5pp 的 aggregate effect（超出 estimation noise），ContamCal 的 γ correction 是否能 outperform raw accuracy？您是否有初步数据支持或反驳这一推测？

**Q2.** Han et al. EACL 2026 使用 binary DIF 在类似设置下的结论是什么？如果他们也得到 null finding，那两种方法（continuous vs. binary exposure）的差异就不构成有意义的区分。如果结论不同，差异来源是什么？

**Q3.** Oracle ablation（Section 5.1）用 perfect binary labels 仍得到 non-significant γ。论文给出两个解释（effect heterogeneity 和 model misspecification）。是否尝试过 non-linear γ 规范（如 threshold model 或 interaction terms）来区分这两个假说？

**Q4.** Social Sciences domain 的 negative γ 被解释为 "SFT injection on factual QA pairs disrupting contextual reasoning"（Section 5.4）。这个因果解释有什么直接证据支持？是否检查过 Social Sciences items 的具体 error patterns？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-18T01:40:29.532207+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "5",
  "project": "contamcal-irt-calibration",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿原文\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## Reviewer 1 评分\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5, **Excitement**: 2.5/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] Oracle ablation 无法区分 genuine null 与 model misspecification，但结论未充分限定\n- §4.1 Oracle ablation paragraph, §6 Limitations \"Additive γ linearity\"\n- Oracle ablation（ground-truth binary labels, AUC=1.0）产出 γ=-0.012 (CI [-0.145, 0.119])。论文提出两种解释：(a) 真实效应接近零，(b) additive linear γ 是 misspecified。但 Abstract、Introduction contribution list、Conclusion 将 \"aggregate contamination effects are negligible\" 作为核心发现，未在这些位置同等强调 misspecification 可能性。如果 γ 是 misspecified（threshold-like effect），则 \"0.6-0.7pp\" 这个数字本身可能就是 model artifact。\n- 建议：在 Abstract/Introduction 中明确写 \"under the additive linear specification\"；或提供 non-linear specification 对比。\n\n**N2** [critical] Social Sciences γ=-0.57 未经多重比较校正\n- §4.4 Table 4, §4.1 \"Diagnostic value of γ\"\n- 8 个 MMLU domain 独立检验，仅 Social Sciences 达到 P(γ<0)=99.1%。Bonferroni 校正（α=0.05/8=0.00625）阈值为 P(γ<0)≥99.375%，Social Sciences 不通过。\n- 建议：报告校正后结果；如不显著，降级为 \"suggestive pattern requiring replication\"。\n\n**N3** [critical] ARC PPP<0.05 下的 ARC 结果呈现方式\n- Table 3 caption, §4.4\n- PPP=0.003 表明模型对 ARC 数据 fit 不可接受。Table 3 中与 MMLU 并列报告给读者留下同等可靠的印象。\n- 建议：将 ARC IRT 结果移入 Appendix 或用灰色标注。\n\n**N4** [critical] SFT injection 生态效度限制了核心 claim 的适用范围\n- §3.1, §6 Limitations, Abstract, Title\n- 标题暗示通用结论，但所有证据仅来自 LoRA SFT injection at ≤3B。真实 contamination 发生在 pretraining 阶段。\n- 建议：标题改为更限定版本；Introduction 中显式讨论 SFT vs pretraining 差异。\n\n## Should-Fix 问题\n\n**W1** J 值跨分析不一致（13/16/24/28），domain-level 最有趣的 finding 使用不完整数据（J=13）。\n\n**W2** Cross-family analysis (Llama J=4, single seed) 统计功效不足，但 Section 标题为 \"Cross-Family Validation\"。\n\n**W3** RRF 在 1.5B/3B 被 S1 主导。论文声称 \"multi-signal fusion is necessary\" 但实际 ablation 证据仅表明 S1-only item selection 导致 exposure variance compression，不是 signal quality aggregation 的贡献。应区分 \"RRF is necessary for exposure variance\" 与 \"RRF provides superior signal quality\"。\n\n**W4** Min-K%++ 方向反转的因果解释不充分。Cohen's d=-1.55 to -1.98 可能是 SFT artifact 而非 Min-K%++ 固有缺陷。\n\n**W5** CI coverage 不均匀（MMLU 50% CI covers 83%, ARC 50% CI covers 45%）。Over-coverage 意味着 CI 无信息，under-coverage 意味着 uncertainty 被低估。\n\n---\n\n请对以上每条 N1-N4 和 W1-W5 逐一给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "5",
    "project": "contamcal-irt-calibration",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿原文\n\n请逐条回应 Reviewer 1 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## Reviewer 1 评分\n**Overall**: 3.0 (Findings)\n**Soundness**: 3/5, **Excitement**: 2.5/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] Oracle ablation 无法区分 genuine null 与 model misspecification，但结论未充分限定\n- §4.1 Oracle ablation paragraph, §6 Limitations \"Additive γ linearity\"\n- Oracle ablation（ground-truth binary labels, AUC=1.0）产出 γ=-0.012 (CI [-0.145, 0.119])。论文提出两种解释：(a) 真实效应接近零，(b) additive linear γ 是 misspecified。但 Abstract、Introduction contribution list、Conclusion 将 \"aggregate contamination effects are negligible\" 作为核心发现，未在这些位置同等强调 misspecification 可能性。如果 γ 是 misspecified（threshold-like effect），则 \"0.6-0.7pp\" 这个数字本身可能就是 model artifact。\n- 建议：在 Abstract/Introduction 中明确写 \"under the additive linear specification\"；或提供 non-linear specification 对比。\n\n**N2** [critical] Social Sciences γ=-0.57 未经多重比较校正\n- §4.4 Table 4, §4.1 \"Diagnostic value of γ\"\n- 8 个 MMLU domain 独立检验，仅 Social Sciences 达到 P(γ<0)=99.1%。Bonferroni 校正（α=0.05/8=0.00625）阈值为 P(γ<0)≥99.375%，Social Sciences 不通过。\n- 建议：报告校正后结果；如不显著，降级为 \"suggestive pattern requiring replication\"。\n\n**N3** [critical] ARC PPP<0.05 下的 ARC 结果呈现方式\n- Table 3 caption, §4.4\n- PPP=0.003 表明模型对 ARC 数据 fit 不可接受。Table 3 中与 MMLU 并列报告给读者留下同等可靠的印象。\n- 建议：将 ARC IRT 结果移入 Appendix 或用灰色标注。\n\n**N4** [critical] SFT injection 生态效度限制了核心 claim 的适用范围\n- §3.1, §6 Limitations, Abstract, Title\n- 标题暗示通用结论，但所有证据仅来自 LoRA SFT injection at ≤3B。真实 contamination 发生在 pretraining 阶段。\n- 建议：标题改为更限定版本；Introduction 中显式讨论 SFT vs pretraining 差异。\n\n## Should-Fix 问题\n\n**W1** J 值跨分析不一致（13/16/24/28），domain-level 最有趣的 finding 使用不完整数据（J=13）。\n\n**W2** Cross-family analysis (Llama J=4, single seed) 统计功效不足，但 Section 标题为 \"Cross-Family Validation\"。\n\n**W3** RRF 在 1.5B/3B 被 S1 主导。论文声称 \"multi-signal fusion is necessary\" 但实际 ablation 证据仅表明 S1-only item selection 导致 exposure variance compression，不是 signal quality aggregation 的贡献。应区分 \"RRF is necessary for exposure variance\" 与 \"RRF provides superior signal quality\"。\n\n**W4** Min-K%++ 方向反转的因果解释不充分。Cohen's d=-1.55 to -1.98 可能是 SFT artifact 而非 Min-K%++ 固有缺陷。\n\n**W5** CI coverage 不均匀（MMLU 50% CI covers 83%, ARC 50% CI covers 45%）。Over-coverage 意味着 CI 无信息，under-coverage 意味着 uncertainty 被低估。\n\n---\n\n请对以上每条 N1-N4 和 W1-W5 逐一给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-18T01:40:46.512857+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16980
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-18T01:40:46.613732+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "5",
  "project": "contamcal-irt-calibration",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿原文\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Reviewer 2 评分\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5, **Excitement**: 2.5/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 页面超限：主要内容超出 8 页\n- Tables 2 和 3 float 到 page 9 顶部，Discussion and Conclusion 尾部文本延续到 page 9。主要内容约 8.5-8.6 页。ACL Long paper 限制 ≤ 8 页正文（Limitations/Ethics/References/Appendix 不计）。\n- 建议：将 Table 2（per-domain γ）移至 Appendix，压缩 §5.1 RRF ablation 段落，Table 3 考虑 inline 报告。\n\n**N2** [critical] 技术新颖性有限：2PL+γ 是 standard explanatory IRT/DIF 的领域应用\n- 论文自己承认 \"ContamCal's γ parameter is formally an instance of explanatory DIF\"。与 Han et al. EACL 2026 差异仅在 continuous vs binary exposure 和 domain-level stratification——这是 modeling detail 变体。\n- 建议：明确定位为 empirical investigation；与 Han et al. 做更细致对比。\n\n**N3** [critical] 叙事不一致：Framing 在 method paper 和 empirical investigation 之间摇摆\n- Title 副标题暗示 method contribution；Introduction ¶1-3 建立 calibration 是核心目标的期待；但 Results 发现 raw accuracy 最好。Contributions 1-3 分属不同类型（empirical finding / engineering trick / exploratory analysis），缺乏统一主线。\n- 建议：从第一段就以 empirical investigation 切入。将 ContamCal 定位为 investigative instrument 而非最终产品。\n\n## Should-Fix 问题\n\n**W1** Abstract 数字密度过高（~202 words, 8-9 个数值，每 ~22 词一个数字）。\n\n**W2** 实验范围过窄（SFT injection only, ≤3B），null finding 普适性存疑。\n\n**W3** \"Diagnostic value\" 叙事说服力不足——8 domains 中 1 个 significant、J=13 不足 confirmatory、family-specific 不推广。\n\n**W4** Cross-family validation 标题 (\"Cross-Family Validation\") 对 J=4 single-seed 数据过强。\n\n**W5** 与 Han et al. EACL 2026 差异化不够深入（仅一句话区分 continuous vs binary）。\n\n**W6** -ing 分词短语结尾模式散见多处，属轻度 AI 写作痕迹。\n\n## Missing References\n1. Lord (1980) \"Applications of Item Response Theory\"\n2. Hambleton, Swaminathan & Rogers (1991) \"Fundamentals of IRT\"\n3. Liang et al. (2023) HELM\n4. Magar & Schwartz (2022) \"Data Contamination: From Memorization to Exploitation\"\n\n## 格式合规\n页数 ❌（约 8.5 页），其余全部 ✅。\n\n---\n\n请对以上每条 N1-N3 和 W1-W6 逐一给出 [AGREE] 或 [REBUT] 回应。对 Missing References 也请给出判断。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "5",
    "project": "contamcal-irt-calibration",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿原文\n\n请逐条回应 Reviewer 2 的每个 Must-Fix 和 Should-Fix 问题。对每条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Reviewer 2 评分\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5/5, **Excitement**: 2.5/5, **Reproducibility**: 4/5, **Confidence**: 4/5\n\n## Must-Fix 问题\n\n**N1** [critical] 页面超限：主要内容超出 8 页\n- Tables 2 和 3 float 到 page 9 顶部，Discussion and Conclusion 尾部文本延续到 page 9。主要内容约 8.5-8.6 页。ACL Long paper 限制 ≤ 8 页正文（Limitations/Ethics/References/Appendix 不计）。\n- 建议：将 Table 2（per-domain γ）移至 Appendix，压缩 §5.1 RRF ablation 段落，Table 3 考虑 inline 报告。\n\n**N2** [critical] 技术新颖性有限：2PL+γ 是 standard explanatory IRT/DIF 的领域应用\n- 论文自己承认 \"ContamCal's γ parameter is formally an instance of explanatory DIF\"。与 Han et al. EACL 2026 差异仅在 continuous vs binary exposure 和 domain-level stratification——这是 modeling detail 变体。\n- 建议：明确定位为 empirical investigation；与 Han et al. 做更细致对比。\n\n**N3** [critical] 叙事不一致：Framing 在 method paper 和 empirical investigation 之间摇摆\n- Title 副标题暗示 method contribution；Introduction ¶1-3 建立 calibration 是核心目标的期待；但 Results 发现 raw accuracy 最好。Contributions 1-3 分属不同类型（empirical finding / engineering trick / exploratory analysis），缺乏统一主线。\n- 建议：从第一段就以 empirical investigation 切入。将 ContamCal 定位为 investigative instrument 而非最终产品。\n\n## Should-Fix 问题\n\n**W1** Abstract 数字密度过高（~202 words, 8-9 个数值，每 ~22 词一个数字）。\n\n**W2** 实验范围过窄（SFT injection only, ≤3B），null finding 普适性存疑。\n\n**W3** \"Diagnostic value\" 叙事说服力不足——8 domains 中 1 个 significant、J=13 不足 confirmatory、family-specific 不推广。\n\n**W4** Cross-family validation 标题 (\"Cross-Family Validation\") 对 J=4 single-seed 数据过强。\n\n**W5** 与 Han et al. EACL 2026 差异化不够深入（仅一句话区分 continuous vs binary）。\n\n**W6** -ing 分词短语结尾模式散见多处，属轻度 AI 写作痕迹。\n\n## Missing References\n1. Lord (1980) \"Applications of Item Response Theory\"\n2. Hambleton, Swaminathan & Rogers (1991) \"Fundamentals of IRT\"\n3. Liang et al. (2023) HELM\n4. Magar & Schwartz (2022) \"Data Contamination: From Memorization to Exploitation\"\n\n## 格式合规\n页数 ❌（约 8.5 页），其余全部 ✅。\n\n---\n\n请对以上每条 N1-N3 和 W1-W6 逐一给出 [AGREE] 或 [REBUT] 回应。对 Missing References 也请给出判断。"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-18T01:40:48.126039+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1512
}
```

</details>

---


### Assistant

_source line 468 · 2026-05-18T01:40:52.689734+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 44

## Round 44

2 recorded events


### User

_source line 469 · 2026-05-18T01:40:55.356028+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交。

核心结论：**Overall 3.0 (Findings)**。

三个 critical issues：
1. **页面超限**——Tables 2/3 float 到 page 9，主要内容约 8.5 页
2. **技术新颖性有限**——2PL+γ 是 standard explanatory IRT/DIF 的领域应用，与 Han et al. EACL 2026 差异化不足
3. **叙事不一致**——Introduction 重度 motivate calibration，Results 发现 calibration 不必要，framing 在 method paper 和 empirical investigation 之间摇摆

主要优势：统计方法严谨、null finding 诚实报告、Min-K%++ directional reversal 有实用价值、identifiability boundary analysis 提供 actionable guidelines。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 470 · 2026-05-18T01:41:00.725959+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 471 · 2026-05-18T01:42:17.359954+00:00_

[Reviewer 1 审稿意见]:
## Round 5 交叉回应 — Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: 页面超限**

同意。我未做 PDF 编译验证，但从内容量判断（Results §4 包含 3 个 table + 3 个 figure + 密集文字），8.5 页的估算合理。ACL style 对正文 ≤8 页是硬限制，Tables 2/3 浮动到 page 9 即为 desk-reject 风险。R2 的压缩建议（Table 2 移入 Appendix、Table 3 inline 化）是可行方案。

补充：Table 4（domain γ）是论文 Contribution 3 的核心证据，如果移入 Appendix 会削弱这一贡献的可见性。建议优先压缩 §4.1 的 RRF ablation 段落（目前约 15 行详述 S1-only failure 的技术细节，可精简为 3-4 行 + pointer to Appendix）和 §4.2 的 Min-K%++ 描述。

---

**[AGREE] R2-N2: 技术新颖性有限**

同意。2PL+γ 确实是 explanatory IRT/DIF 的直接应用，continuous exposure 和 domain stratification 是 modeling 变体而非根本创新。论文自己在 Related Work §2 para 3 承认 "formally an instance of explanatory DIF"。与 Han et al. (2026) 的区别（continuous vs binary, domain-level stratification, counterfactual inference）是实现细节差异，不构成独立方法贡献。

不过我与 R2 对定位建议的看法略有不同：论文已经在 Conclusion 中将 ContamCal 定位为 "investigative instrument"（§5: "ContamCal's value lies in this decomposition"），问题是 Introduction 的 framing 没有与此一致（这正是 R2-N3 指出的叙事问题）。如果从头定位为 empirical investigation + methodology negative result，技术新颖性的要求会降低，评价标准转向 empirical contribution 的力度。

---

**[AGREE] R2-N3: 叙事不一致**

同意，且这与我在 R1-N4 中指出的标题过宽问题相关联。具体证据：

- Title "Does LLM Benchmark Contamination Need Calibration?" — 暗示通用 question paper
- Subtitle "An IRT Decomposition Study" — 暗示 empirical study
- Introduction §1 para 3: "No existing method bridges detection signals and a measurement-theoretic calibration framework" — 建立了 method gap 的叙事期待
- Introduction §1 para 4: "We develop ContamCal to investigate this question" — 定位为工具
- Results §4.1: "Raw accuracy achieves the lowest MAE" — 工具被自己的实验证伪
- Contributions list: 1 是 empirical null finding, 2 是 engineering observation, 3 是 exploratory analysis

这三类贡献确实缺乏统一主线。一个更一致的 framing 应该是：**"我们问 IRT 能否校准 contamination，答案是在当前条件下不需要，以下是为什么以及在什么条件下会需要"** — 以 question-driven empirical investigation 为主线，ContamCal 作为回答这个问题的工具而非贡献本身。

---

### Should-Fix 问题

**[AGREE] R2-W1: Abstract 数字密度过高**

同意。重新数 Abstract 中的数值/符号：0.6-0.7pp, τ=0.73, 300, τ=0.46, 2000, Δτ=0.27, γ=-0.57, 99.1%, d=-1.55, -1.98, AUC≥0.55, J≥50 — 共 12 个量化信息点。对于 ~202 words 的 abstract 来说确实过于密集，读起来像 results summary 而非 story。与 CLAUDE.md 中的论文写作规范"Abstract 不是 Results 的缩写，最多引用 2-3 个关键数字"形成对比。

---

**[AGREE] R2-W2: 实验范围过窄**

同意，与我的 R1-N4 一致。SFT injection at ≤3B 是高度限定的条件，null finding 的外部有效性依赖于这一 proxy 能代表真实 contamination，但论文缺乏证据支持这一假设。

---

**[AGREE] R2-W3: "Diagnostic value" 叙事说服力不足**

同意，与我的 R1-N2（多重比较）一致。8 domains 中 1 个 P(γ<0)=99.1% 未经多重比较校正，J=13 被论文自己的 simulation study 标为 exploratory（需 J≥50），family-specific 不推广。作为 Contribution 3 的支撑证据链不够强。

---

**[AGREE] R2-W4: Cross-family validation 标题过强**

同意，与我的 R1-W2 一致。§4.5 标题 "Cross-Family Validation" 暗示了 confirmatory validation，但 J=4 single-seed + Llama d100 MMLU excluded = 实际可用数据仅 3 个 Llama models。建议改为 "Cross-Family Exploratory Analysis" 或 "Preliminary Cross-Family Evidence"。

---

**[REBUT] R2-W5: 与 Han et al. (2026) 差异化不够深入**

部分不同意。Related Work §2 para 2 确实只有一句话区分（"Neither models contamination as a continuous covariate for score calibration"），这确实太简短。但我认为实际差异比 R2 描述的更大：

1. Han et al. 使用 psychometric DIF 检验 item parameters 是否因 contamination 改变（detection-oriented），而本文使用 explanatory DIF 进行 score calibration（correction-oriented）— 这是目标的根本不同
2. Han et al. 的 DIF 是 group-based（contaminated group vs clean group），本文是 continuous covariate — 这不仅是 modeling detail，而是允许 partial exposure 的语义区别
3. 本文的 counterfactual inference（设 $e_{ij}=0$ 取 posterior expectation）在 Han et al. 中没有对应操作

但 R2 的建议（做更细致对比）仍然合理：论文应该在 Related Work 中用 3-4 句话而非 1 句话来区分，并在 Method §2.1 中讨论为什么 continuous > binary 在 LLM contamination 场景下更合适（因为 web crawl exposure 是 graded 而非 all-or-nothing）。

---

**[AGREE] R2-W6: -ing 分词短语**

同意这是一个存在的问题，但影响极低。学术论文中 -ing phrases 只要不过度就不是显著问题。如果只是散见（而非系统性），属于可快速修复的 minor polish。

---

### Missing References 评估

1. **Lord (1980) "Applications of Item Response Theory"** — [AGREE] 应引用。论文大量使用 IRT 框架但仅引用了 Lalor et al. (2024) tutorial 和 De Boeck (2004) explanatory IRT。作为 IRT 的经典基础文献，Lord (1980) 应在 §2 Method 或 Related Work 中出现。

2. **Hambleton, Swaminathan & Rogers (1991) "Fundamentals of IRT"** — [AGREE] 同上理由。两本 IRT 经典教科书至少应引一本作为 framework foundation。

3. **Liang et al. (2023) HELM** — [AGREE] HELM 是大规模 LLM evaluation 的代表性工作，论文讨论 benchmark evaluation 但未引 HELM，是一个覆盖缺口。

4. **Magar & Schwartz (2022) "Data Contamination: From Memorization to Exploitation"** — [AGREE] 这是 contamination 影响的早期系统研究，Related Work §2 para 1 的 detection/mitigation 综述中应包含。

总结：4 条 missing reference 建议均合理，反映了论文在 (a) IRT 基础文献和 (b) contamination 早期文献上的引用不足。

---

### 总结

R2 的 6 条 Must-Fix/Should-Fix 中，我同意 5 条，部分反驳 1 条（W5 的严重程度）。R2 对叙事一致性（N3）和页面超限（N1）的识别是我未重点覆盖的角度，补充了我的 R1 review 中关于方法论假设和统计检验的侧重。两份 review 在核心判断上高度一致：论文框架有参考价值但证据强度受限，适合 Findings track（Overall 3.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 472 · 2026-05-18T01:42:22.534794+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 473 · 2026-05-18T01:42:25.160410+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 3 条 Must-Fix 和 6 条 Should-Fix 逐条给出了判断：同意 N1（页面超限）、N2（技术新颖性有限）、N3（叙事不一致）、W1-W4、W6，部分反驳 W5（Han et al. 差异化实际比 R2 描述的更大，但同意应在论文中展开）。4 条 Missing References 均���意。两份 review 核心判断一致：Overall 3.0 (Findings)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 474 · 2026-05-18T01:42:30.201885+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 47

## Round 47

8 recorded events


### User

_source line 475 · 2026-05-18T01:42:49.908834+00:00_

[Reviewer 2 审稿意见]:
## Round 5 交叉回应 — Reviewer 2 对 Reviewer 1 意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R1-N1: Oracle ablation 无法区分 genuine null 与 model misspecification**

R1 的论点在 γ 层面成立，但在 aggregate finding 层面不成立。核心区分：

- **0.6-0.7pp aggregate effect 是 model-independent observation**。Section 5.1 ¶3 明确写 "SFT-injected contamination shifts aggregate accuracy by only ~0.6pp on MMLU and ~0.7pp on ARC across dosage levels"——这是直接比较 d000 vs. d005/d025/d100 的 raw accuracy 差异，不依赖 IRT model 或 γ specification。即使 γ 完全 misspecified，raw accuracy shift 仍然是 0.6-0.7pp。
- **Misspecification concern 仅影响 γ diagnostic 结论**。如果 contamination 是 threshold-like 的，linear γ 会被 dilute toward zero，但这不改变 aggregate accuracy 差异的直接测量。

因此，R1 的建议"在 Abstract/Introduction 中明确写 under the additive linear specification"对 γ-related claims 是合理的，但不应限定 aggregate 0.6-0.7pp 这个 model-free 发现。建议分层限定：aggregate finding 保持原有表述，γ diagnostic finding（Contribution 3 的 Social Sciences 结论）加上 specification caveat。

不过，R1 有一个隐含的好观点：如果 contamination 在 item-level 有 non-linear/heterogeneous effects（some items 大幅 inflate, others 不变或 deflate），aggregate 0.6-0.7pp 可能掩盖了更大的 item-level distortions，而这些 distortions 在 ranking 层面可能产生影响。论文 Section 5.4 提到 opposing domain signs 正是这种 heterogeneity 的证据。论文应更明确讨论 aggregate negligibility 与 item-level heterogeneity 的关系。

---

**[AGREE] R1-N2: Social Sciences γ=-0.57 未经多重比较校正**

R1 的数学完全正确。8 个 domain 独立检验，Social Sciences P(γ<0)=99.1% 在 Bonferroni 校正 α=0.05/8=0.00625 下不通过（需 P≥99.375%）。

补充两点 nuance：
1. **Bayesian 框架下 multiple comparison 的处理方式有争议**。严格 Bayesian 立场认为 posterior probability 不需要频率主义校正（Gelman et al., 2012 已被论文引用）。但这要求使用 hierarchical model with partial pooling 来自然处理 multiplicity——论文用的是 independent per-domain fits，没有 shrinkage，因此需要某种形式的校正。
2. **论文已将该 finding 标为 "exploratory"**（Table 2 caption, Section 5.4 text, Contribution 3 使用 "requiring higher-powered replication"）。但 Abstract 和 Introduction 中的呈现强度与 "exploratory" 不匹配——Abstract 直接报告 "Social Sciences shows the strongest negative effect (γ=-0.57, posterior P(γ<0)=99.1%)" 没有任何 multiplicity caveat。

建议采纳 R1 的修改方向：(a) 在 Abstract 中删除 P(γ<0)=99.1% 或加注 "uncorrected for multiplicity"；(b) 在 Section 5.4 report Bonferroni-adjusted conclusion；(c) 或改用 hierarchical IRT（per-domain γ_k 从共同分布中采样），自然实现 shrinkage + multiplicity adjustment。选项 (c) 在方法论上最优。

---

**[AGREE] R1-N3: ARC PPP<0.05 下的结果呈现方式**

同意。Table 3（main text）将 MMLU 和 ARC 并列报告，PPP=0.003 的 caveat 仅在 caption 小字中提及。视觉上两者获得同等权重，但 ARC 的 IRT 结果在统计上不可靠。

我的审稿（Round 5 报告 N1）指出的页面超限问题与此相关：如果 ARC IRT 结果移至 Appendix，Table 3 可以瘦身为 MMLU-only，同时释放正文空间。这是一个两个问题可以同时解决的修改方向。

补充：Section 5.2 报告 "ARC-Challenge model fit is marginal across all tested configurations (PPP < 0.05 at J=8, 13, and 16)"，说明这不是 J 选择的问题，而是 2PL+γ 对 ARC 数据的结构性 misfit。论文应在 Discussion 中明确讨论为什么 ARC 不适合当前模型（可能原因：ARC items 的 difficulty distribution 更 homogeneous、item pool 更小 1,172 vs. 14,042）。

---

**[AGREE] R1-N4: SFT injection 生态效度限制核心 claim 适用范围**

同意，且与我的 Round 5 审稿 W2 一致。标题 "Does LLM Benchmark Contamination Need Calibration?" 暗示通用结论，但证据仅覆盖 SFT injection at ≤3B。

补充 R1 未提到的一个维度：**SFT injection 与 pretraining contamination 的差异不仅是 scale 问题，而是 mechanism 问题**。论文 Limitations ¶7 正确指出 "distributed exposure across many training steps rather than concentrated fine-tuning"。但更关键的是：pretraining contamination 发生在 representation learning 阶段，可能改变 model 的 internal representation（而非仅在 LoRA adapter 层）。这意味着 (1) detection signals 的 behavior 可能完全不同；(2) contamination effect 可能 embedded into θ rather than capturable by γ。论文 Section 5.5 的 θ asymmetry 发现其实已经暗示了这一点——cross-family 分析中 contamination 被 absorbed into θ rather than γ。

建议：标题至少加限定语，如 "Does SFT-Injected Benchmark Contamination Need Calibration?"。或保留问题式标题但在 Abstract 第一句就 scope 为 SFT injection。

---

### Should-Fix 问题

**[AGREE] R1-W1: J 值跨分析不一致**

同意。虽然 Appendix B (Table in appendix) 列出了 model set compositions，Section 4.1 也解释了原因（"domain-level runs preceded completion of the 3B retraining"），但核心问题是：**最有趣的 finding (domain γ) 使用了统计功效最低的配置 (J=13)**。论文在 Appendix C (prior sensitivity analysis) 对 Social Sciences 做了 J=16 的补充分析（Table in Appendix C），但主文 Table 2 仍报告 J=13 结果。应在主文中明确说明 J=13 vs. J=16 结果的一致性，而非将此信息埋在 Appendix。

---

**[AGREE] R1-W2: Cross-family "Validation" 标题误导**

完全同意。与我的 Round 5 审稿 W4 一致。J=4, single seed, d100 排除后 effective range 仅到 d025——这是 preliminary exploration 而非 validation。论文自己用 "exploratory" 描述（Section 4.2），但 Section 5.5 标题仍为 "Cross-Family Validation"，存在内部矛盾。

---

**[AGREE] R1-W3: RRF 的贡献是 exposure variance 而非 signal quality**

这是本轮交叉审稿中 R1 最独到的观察。

论文 Section 5.1 ¶2 明确报告：S1-only item selection 失败的原因是 "exposure variance compression: S1-only top-300 items concentrate in a narrow score band ([0.749, 0.867]), creating collinearity between γ·e_ij and difficulty parameters"。这是 variance 问题，不是 accuracy 问题。实际上 S1 的 AUC > 0.95（Figure 1），远高于 RRF 融合后的 average AUC。

论文最后总结 "RRF's value is therefore not only signal quality aggregation but exposure variance for IRT parameter separability"——这个措辞暗示 RRF 同时提供 quality 和 variance 两种贡献，但 ablation 证据仅支持 variance 贡献。没有实验证明 RRF 在 signal quality 维度优于 S1-only（S1 AUC > 0.95 vs. RRF composite AUC 未报告）。

建议：(1) 报告 RRF composite 的 overall AUC 与 S1-only 的对比；(2) 在方法/结论中精确表述 RRF 的贡献为 exposure variance diversification rather than signal quality improvement。

---

**[REBUT] R1-W4: Min-K%++ 方向反转可能是 SFT artifact**

R1 的 concern 合理，但论文已充分 qualify 了这一点。

Section 5.2 最后两句："We hypothesize that SFT injection at 0.5B disrupts the token-level surprisal landscape... This causal explanation is post-hoc; alternative explanations include position bias confound at 0.5B and near-full-rank LoRA adaptation disrupting the pre-trained loss landscape." 论文明确标注了 post-hoc 性质并列出了 alternative explanations。

不过我同意 Conclusion 的措辞需要调整。Conclusion 说 "Min-K%++ should not be trusted at the 0.5B scale" 这个 categorical claim 确实过强——这个结论应限定为 "under SFT injection"。我的 Round 5 审稿 M3 已指出同一问题。所以：REBUT R1 的 "因果解释不充分" 判断（论文已承认是 post-hoc），但 AGREE Conclusion 中的 claim 需加限定。

---

**[AGREE] R1-W5: CI coverage 不均匀**

同意。MMLU 50% CI covers 83%（over-coverage = uninformative intervals），ARC 50% CI covers 45%（under-coverage = overconfident）。这个不对称反映了 model fit 的 benchmark 依赖性。

补充：over-coverage 和 under-coverage 的根源可能不同。MMLU over-coverage 可能因为 posterior θ uncertainty 太大（J=16 不足以精确估计 θ）；ARC under-coverage 可能因为 2PL+γ 对 ARC 的结构性 misfit（PPP=0.003）。论文应分开讨论这两种 failure mode 的原因。

---

### 总结

| R1 Issue | 我的判断 | 核心理由 |
|----------|---------|---------|
| N1 | REBUT (partial) | 0.6-0.7pp 是 model-free observation，misspecification 仅影响 γ diagnostic |
| N2 | AGREE | 数学正确；建议 hierarchical IRT 或 Bonferroni 校正 |
| N3 | AGREE | ARC PPP=0.003 的结果不应与 MMLU 同等呈现 |
| N4 | AGREE | 标题/Abstract 需更明确 scope 为 SFT injection |
| W1 | AGREE | 最有趣的 finding 用最弱的数据 |
| W2 | AGREE | 标题与内容矛盾 |
| W3 | AGREE | R1 最独到的观察，ablation 仅支持 variance 贡献 |
| W4 | REBUT (partial) | 论文已 qualify，但 Conclusion claim 需限定 |
| W5 | AGREE | 应分开讨论 over/under-coverage 的不同根源 |

R1 与我（R2）在多个关键问题上 converge：scope 限制（N4/R2-W2）、cross-family 标题（W2/R2-W4）、narrative consistency（隐含在 N4 中/R2-N3）。R1 的 N2（multiple comparison）是一个我遗漏的重要统计问题。R1 的 W3（RRF variance vs. quality）是一个精准的技术洞察，我完全认同。

我对 N1 的 partial rebut 是实质性的：aggregate 0.6-0.7pp finding 的 validity 不取决于 γ specification，但论文需要更清楚地区分 model-free vs. model-dependent conclusions。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-18T01:43:36.712127+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-18T01:43:36.712714+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-18T01:48:47.030933+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?') but framing still inconsistent. Intro ¶1-3 heavily motivate calibration, Results show calibration unnecessary. Contributions 1-3 span empirical finding / engineering observation / exploratory analysis without unified main line. 'Why not just use raw accuracy?' paragraph in Conclusion reads as arguing against paper's own existence. Both AGREE: need full empirical investigation framing from ¶1, ContamCal as investigative instrument not product.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation; ContamCal as tool not contribution; consolidate Contributions to 2 items: (1) empirical null finding + identifiability, (2) diagnostic value + signal failure modes\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without qualification. Pretraining contamination (arXiv 2601.04301) shows significantly larger effects. All claims must be scoped to 'under SFT injection at ≤3B scale'. Both reviewers AGREE unanimously.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract. But title still asks generic question. R2 adds: SFT vs pretraining differs in mechanism not just scale — pretraining contamination embeds into representations (θ) not just LoRA adapter. §5.5 θ asymmetry already hints at this. Both AGREE title needs scoping or Abstract first sentence must scope.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims in Abstract/Intro/Conclusion to 'under SFT injection at ≤3B'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite and discuss pretraining contamination dose-response literature as contrast\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Either scope title ('Does SFT-Injected Benchmark Contamination Need Calibration?') or ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation (AUC=1.0, γ=-0.012 non-sig) has two interpretations: (a) genuine null effect (heterogeneity cancels), (b) model misspecification (linear γ cannot capture threshold/interaction effects). Paper adopts (a) without testing (b). Limitations ¶9 acknowledges threshold possibility but §5.1 oracle section ignores it. Both reviewers AGREE this is fundamental ambiguity.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations. R2 partial REBUT on R1-N1: aggregate 0.6-0.7pp is model-free observation (direct d000 vs d005/d025/d100 accuracy comparison), misspecification only affects γ diagnostic claims. Both AGREE: paper must distinguish model-free findings (aggregate accuracy shift) from model-dependent findings (γ significance/direction). γ-related claims need 'under additive linear specification' caveat.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i or γ×a_i interaction model as misspecification check\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If not testable, explicitly scope claim as 'under linear additive specification'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat to γ-related claims in Abstract/Intro/Conclusion; keep aggregate 0.6-0.7pp finding uncaveated as model-free\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Oracle ablation §5.4 now presents both interpretations with equal weight. Mean a_i comparison (Cohen's d=0.098, r=-0.013) rules out discrimination confound. Limitations ¶9 discusses threshold possibility.\"\n  resolution_round: null\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"8 independent domain tests, only Social Sciences significant at α=0.05. Bonferroni α=0.00625; CI upper bound -0.10 would likely include zero. BH correction also unlikely to survive 1/8 pattern. This is the sole evidence for 'diagnostic value' narrative. Both AGREE correction needed.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 reconfirms: Bonferroni threshold P(γ<0)≥99.375%, Social Sciences at 99.1% does not pass. R2 AGREE with nuance: (1) Bayesian posteriors don't strictly need frequentist correction per Gelman 2012, BUT independent per-domain fits without shrinkage do need correction; (2) Abstract reports P(γ<0)=99.1% without any multiplicity caveat. Both AGREE: report corrected result, or switch to hierarchical IRT for natural shrinkage.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results for domain-level γ\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"If non-significant after correction, reframe as 'suggestive pattern requiring higher-powered replication'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Either (a) add 'uncorrected for multiplicity' when reporting P(γ<0)=99.1% in Abstract/Results, or (b) implement hierarchical IRT with per-domain γ_k drawn from shared hyperprior for natural shrinkage. Option (b) preferred as it also addresses R2-W4 (independent fitting sacrifices common θ scale).\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Switched to Bayesian P(γ<0) framing with Gelman (2012) justification. Social Sciences P(γ<0)=99.1% reported. Prior sensitivity confirms robustness (97.95%-98.92% across N(0,0.5/1.0/2.0)). C3 reframed as 'exploratory domain-level diagnosis requiring J≥50 for confirmation'.\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations but results still in main table\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at J=8, 13, 16 per §5.4. Table 3 still reports ARC IRT results without PPP annotation. R2 nuance: ARC ~0.7pp from raw data is valid, but IRT-derived numbers are unreliable. Both AGREE Table 3 needs PPP annotation and ARC IRT results need caveat.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003 in caption, but ARC IRT results still in main table alongside MMLU giving visual parity. R1: move ARC IRT to Appendix or grey out. R2 AGREE: also helps solve page limit (R5-N1) by shrinking Table 3. Both AGREE 2PL+γ structural misfit for ARC (not just sample size issue) should be discussed in main text.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column in Table 3\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Discuss ARC misfit source (item pool heterogeneity vs model specification)\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix (keep ARC raw accuracy in main table); discuss structural misfit cause (smaller item pool 1172 vs 14042, difficulty distribution homogeneity) in main text\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality aggregation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical by R2. S2 reverses at 0.5B, S4 near-random below 1.5B. §5.2 admits RRF degrades to S1-only. No direct RRF vs S1-only ablation (τ, MAE, γ) at 1.5B/3B where S2 d≈+0.7. R1 partially rebuts absolute claim but agrees ablation is missing. Contribution 2 unsupported without this evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation now complete: S1-only causes MCMC non-convergence (MMLU R̂=1.53) due to exposure variance compression ([0.749,0.867]). This proves RRF necessary for IRT convergence. However R1 W3 insight (R2 calls 'most insightful observation'): ablation evidence supports RRF for exposure VARIANCE, not signal QUALITY. S1 AUC>0.95 exceeds RRF composite. Paper conflates these: 'not only signal quality aggregation but exposure variance' implies both supported, only latter is. Both AGREE: precise the contribution claim. Downgraded to warning since core ablation is done.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2 in D134 reframing\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation at 1.5B and 3B (τ, MAE, γ significance)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If RRF ≤ S1-only, downgrade Contribution 2 to 'item filtering improves IRT' without RRF-specific claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish 'RRF necessary for exposure variance diversification' from 'RRF provides superior signal quality'. Report RRF composite AUC vs S1-only AUC. Revise §5.1 summary sentence accordingly.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"RRF ablation complete. S1-only completely fails: MCMC non-convergence on MMLU (R̂=1.53, ESS=7), degenerate solution on ARC. RRF essential for exposure variance (compression to [0.749,0.867] under S1-only). §5.1 new paragraph documents ablation. C2 strengthened, not downgraded.\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically fails — reported only in Limitations\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"§5.1 only reports 50%. 80%/95% completely missing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"CI coverage now reported in Limitations: MMLU 83%/89%/100%, ARC 45%/65%/90%. ARC under-coverage corroborates PPP<0.05 misfit. Both AGREE this should be in main results, not just Limitations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results. R1: MMLU 95% CI covers 100% = completely uninformative. R2 AGREE, adds: over-coverage (MMLU) and under-coverage (ARC) have different root causes and should be discussed separately. MMLU over-coverage likely from posterior θ uncertainty at J=16; ARC under-coverage from structural misfit (PPP=0.003).\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage discussion to main results section\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss over-coverage and under-coverage root causes separately; acknowledge MMLU 95% CI = uninformative\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"CI coverage moved to §5.1 main results.\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses (13/16/24/28) and all below paper's own J≥50 threshold\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Contribution 4 combines simulation + empirical. Should split.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"J inconsistency from experimental timeline (domain runs before 3B retraining). All γ conclusions at J=13-16 are underpowered by paper's own standard. Both AGREE needs prominent caveat and ideally unified J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Model set table in Appendix B. But core problem: most interesting finding (domain γ) uses weakest configuration (J=13). Prior sensitivity in Appendix C uses J=16 for Social Sciences but main Table 2 still reports J=13. Both AGREE: either rerun domain analysis at J=16, or explicitly state J=13 vs J=16 consistency in main text.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J and model composition prominently in each table/figure\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16, or add main-text statement on J=13 vs J=16 consistency citing Appendix C\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Model set transparency table added to Appendix B (tab_model_sets) with 4 rows for J=16/13/16-28/13. Each table/figure caption now references J and configuration.\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 (300 RRF) vs 0.46 (2000 random) may reflect higher average a_i in RRF-selected items, not contamination signal value. Need discrimination-matched random subset comparison or report average a_i of RRF vs random sets.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently re-raised in R5. Resolution from R4 (mean a_i comparison, Cohen's d=0.098) appears in §5.1. Possibly resolved pending confirmation.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items; add discrimination-matched control\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Mean a_i comparison: RRF-selected mean=1.12, random mean=1.09, Cohen's d=0.098, r=-0.013. No discrimination confound. §5.1 documents this exclusion.\"\n  resolution_round: null\n\n- id: \"R1-C2\"\n  summary: \"Cross-family 'validation' title misleading for J=4 single-seed data\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"'Validated' too strong for single-seed N=3-4.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"§4.2 references 'Appendix E post-hoc power calculations' but Appendix E (sec:full_baselines) contains baseline tables, not power analysis. This is missing content, not just hard to find. Both strongly AGREE.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Phantom Appendix E reference removed. But §5.5 title still 'Cross-Family Validation' despite J=4 single seed + d100 MMLU excluded (effective Llama range only d000-d025). Both AGREE: rename to 'Cross-Family Exploratory Analysis' or 'Preliminary Cross-Family Evidence'. Llama d100 MMLU catastrophic collapse suggests cross-architecture SFT injection mechanism fundamentally differs from within-family.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Write and include actual Appendix E power analysis OR remove the reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 from 'Cross-Family Validation' to 'Preliminary Cross-Family Analysis' or similar\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Appendix E cross-reference removed from experimental_setup.tex. No phantom reference remains.\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50. Prior N(0,1) dominance?\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"γ~N(0,1) covers ±2 logit units. No prior sensitivity analysis. Need at least N(0,0.5) and N(0,2) alternatives. Also need e_ij distribution (mean, SD) to interpret γ effect size. Both AGREE.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently re-raised in R5. Prior sensitivity analysis now in Appendix C showing pooled γ is prior-dominated (2.6× shift), Social Sciences is data-dominated (1.2× shift). e_ij distribution reported. Possibly resolved.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2); report e_ij distribution\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Full prior sensitivity complete. Pooled: γ shifts 0.34→0.89 (2.6×, prior-dominated), all CI include 0. Social Sciences: γ -0.43→-0.51 (1.2× shift, data-dominated), all CI exclude 0, P(γ<0)≥97.95%. e_ij distribution: mean=0.041, median=0.016, max=0.879. Appendix prior_sensitivity section added.\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption at 0.5B but provides no direct evidence (e.g., perplexity distributions). Alternative explanations (position bias confound, near-full-rank LoRA catastrophic forgetting) not ruled out. R2 considers minor since empirical finding is well-documented. R1 wants either evidence or explicit 'mechanism TBD'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 W4: Min-K%++ reversal may be SFT artifact rather than inherent Min-K%++ flaw (0.5B position bias = SFT-induced catastrophic behavior). R2 partial REBUT: paper already qualifies as post-hoc with alternatives listed. Both AGREE: Conclusion claim 'Min-K%++ should not be trusted at the 0.5B scale' must be scoped to 'under SFT injection'.\"}\n  action_items:\n    - {round: 4, action: \"Either provide token-level perplexity comparison or reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion claim to 'Min-K%++ should not be trusted at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Limitations reframed causal explanation as 'post-hoc hypothesis' with alternative explanations listed.\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Five contributions too many — now consolidated to 3 but still lacks unified main line\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span null finding, item filtering, signal failure, identifiability, domain diagnosis. R2 suggests consolidate to 2-3. R1 agrees with reservation (null finding alone too thin for long paper). Suggest: (1) framework+null finding, (2) signal reliability boundaries (merge C3+C4), demote C5 to observation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions. R2 N3: still span different types (empirical finding / engineering observation / exploratory analysis) without unified main line. R1 AGREE. Both suggest further consolidation to 2 contributions.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Consider further consolidation to 2 contributions: (1) empirical null finding + identifiability analysis, (2) diagnostic value + signal failure modes\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Contributions consolidated to 3: C1(null finding + identifiability analysis), C2(signal-guided filtering + failure modes), C3(exploratory domain-level diagnosis).\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — now partially resolved but IRT classics still absent\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. (EACL Findings 2026) 'Quantifying Data Contamination in Psychometric Evaluations of LLMs' is most direct concurrent work — combines IRT + contamination. arXiv 2601.04301 provides pretraining dose-response data contradicting null finding scope. Chen et al. EMNLP 2025 survey. R1 cannot independently verify but agrees in principle they should be checked and cited.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R4 references added. New gaps: (1) IRT classics — Lord (1980), Hambleton et al. (1991) are standard references for papers using 2PL; (2) HELM (Liang et al. 2023) for LLM evaluation context; (3) Magar & Schwartz (2022) for early contamination analysis. R1 AGREE all 4. Also: Han et al. differentiation needs 3-4 sentences not 1 sentence (R1 partial REBUT R2-W5: actual differences larger than described but paper should expand).\"}\n  action_items:\n    - {round: 4, action: \"Verify and cite Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025 survey\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord (1980), Hambleton et al. (1991), Liang et al. (2023) HELM, Magar & Schwartz (2022). Expand Han et al. comparison to 3-4 sentences in Related Work.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"All 5 references verified and added: han2026quantifying, schaeffer2026causally, chen2025benchmarking, singh2024evaluation, gelman2012why.\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'. Per-domain model fit unverifiable. Especially critical for Social Sciences (sole significant domain). Both AGREE must report.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present in Table (0.096-0.570). Not re-raised in R5. Possibly resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values in Table 2\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"PPP values filled in Table 5 (domain γ table): range 0.096-0.570.\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers crowd out narrative. Both AGREE should trim to ~200 words with 2-3 key numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Abstract now ~202 words (within range) but still contains 8-9 specific numbers (~12 quantitative info points per R1 count). Reads like compressed Results not independent story. Both AGREE: keep 2-3 key numbers (aggregate effect, identifiability threshold), replace rest with qualitative descriptions.\"}\n  action_items:\n    - {round: 4, action: \"Trim Abstract to ≤220 words, reduce to 2-3 key numbers\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further reduce numeric density: keep ~0.6-0.7pp and J≥50 threshold, replace τ values/Cohen's d/γ values with qualitative statements\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Abstract trimmed to ~202 words.\"\n  resolution_round: null\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF applied to new domain\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT now cited. But Han et al. EACL 2026 (IRT+contamination) uncited — potentially closer concurrent work. Technical novelty remains limited: 2PL+γ is standard explanatory IRT/DIF. Value is empirical, not methodological.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R2 N2: paper self-acknowledges 'formally an instance of explanatory DIF'. Han et al. EACL 2026 now cited but differentiation is one sentence. R1 AGREE novelty limited. Both AGREE: must explicitly position as empirical contribution, not methodological innovation. Continuous vs binary exposure (paper's claimed differentiation from Han et al.) shown irrelevant by own oracle ablation.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. EACL 2026 as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state in Introduction that technical modeling is not the contribution; contribution is systematic empirical investigation of whether calibration is needed\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"PSN-IRT and Han et al. now cited. Paper positioned as empirical contribution, not methodological novelty.\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation + IRT classics\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"33 citations.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT, Kocyigit, Holland now cited. But new gaps: Han et al. EACL 2026, arXiv 2601.04301, Chen EMNLP 2025 survey. See R4-W4.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. R4 gaps filled. New gaps: Lord (1980), Hambleton (1991), HELM, Magar & Schwartz (2022). Han et al. comparison needs expansion. R1 partial REBUT R2-W5: actual differences are larger (goal-level: detection vs calibration; group-based vs continuous DIF; counterfactual inference) but paper must articulate them.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al., Chen et al., Singh et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord (1980), Hambleton (1991), HELM, Magar & Schwartz. Expand Han et al. comparison paragraph.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"All identified references now cited. 5 new bib entries added in Round 4.\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-N1\"\n  summary: \"Page limit exceeded — main content ~8.5 pages, ACL limit is 8 pages\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Tables 4 and 3 (Results section tables) float to page 9 top. Discussion/Conclusion text continues to page 9. Limitations begins at ~60% of page 9. Main content ~8.5 pages. ACL Long paper: ≤8 pages content, Limitations/Ethics/References/Appendix excluded. Desk-reject risk. Both AGREE. R1 suggests: compress §5.1 RRF ablation to 3-4 lines + Appendix pointer; R2 suggests: move Table 2 (domain γ) to Appendix, inline Table 3 numbers. Moving ARC IRT to Appendix (R3-N3 fix) also helps.\"}\n  action_items:\n    - {round: 5, action: \"Reduce main content to ≤8 pages. Priority cuts: (1) move ARC IRT from Table 3 to Appendix; (2) compress §5.1 RRF ablation paragraph; (3) consider moving Table 2 to Appendix or reducing Table 3 to inline format.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"Method §3.1 defines y_ijk with k = benchmark, but Eq.2 uses k = stratum/domain. Understandable in context but should be explicitly noted.\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes from benchmark to domain stratum\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-W2\"\n  summary: \"Ethics Statement too brief — no dual-use risk discussion\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Ethics Statement is 4 sentences covering data/model licensing only. No discussion of dual-use risks (e.g., detection signals being reverse-engineered to optimize contamination strategies, or framework being used to game leaderboards). Both flag as minor.\"}\n  action_items:\n    - {round: 5, action: \"Add 1-2 sentences on dual-use risk of contamination detection/calibration methods\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-W3\"\n  summary: \"B1b label unexplained in Table 3\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1\", note: \"Table 3 lists 'B1b: Remove & Rescore' and 'B5b: Emperor' but neither 'B1a' nor 'B5a' appear in the paper. The 'b' suffix is unexplained.\"}\n  action_items:\n    - {round: 5, action: \"Either explain B1a/B1b distinction or remove 'b' suffix\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues (unchanged from Round 4)\n- id: \"R2-N6\"\n  summary: \"Format non-compliance: Limitations after references + missing Ethics Statement\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Limitations is subsection under Discussion.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations still after bibliography. Ethics absent.\"}\n    - {round: 4, reviewers: \"\", note: \"R4 format check confirms Limitations before references, Ethics Statement present. Issue resolved.\"}\n  action_items:\n    - {round: 2, action: \"Move Limitations before references\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Add Ethics Statement\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Resolved. Limitations and Ethics both present before bibliography. Confirmed in R4.\"\n  resolution_round: 4\n\n- id: \"R1-C1\"\n  summary: \"Missing 1.5B/3B experimental data in Tables\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Table 1 only 0.5B.\"}\n    - {round: 3, reviewers: \"\", note: \"Subsumed by R2-W5 and R3-N5.\"}\n  action_items: []\n  resolution: \"Resolved. Table 4 now J=16 (8×1.5B + 8×3B) with all baselines.\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Triple impossibility over-generalized\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"DCR existence is counter-example.\"}\n    - {round: 3, reviewers: \"\", note: \"Triple impossibility removed from draft.\"}\n  action_items: []\n  resolution: \"Resolved — triple impossibility claim removed.\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Fisher Information simulation now has heatmap visualization\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Figure 2 with heatmap now present.\"}\n  action_items: []\n  resolution: \"Resolved — Figure 2 with heatmap now present.\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"Observational experiments over-interpret causal claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Paper restructured, observational experiments no longer present.\"}\n  action_items: []\n  resolution: \"Resolved — paper restructured.\"\n  resolution_round: 3\n\n- id: \"R1-W7\"\n  summary: \"Table 2 title misleading\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Table captions rewritten.\"}\n  action_items: []\n  resolution: \"Resolved — table captions updated.\"\n  resolution_round: 3\n\n- id: \"R3-N5\"\n  summary: \"Baseline configuration inconsistency — main table J vs appendix J\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Main Table J=13 vs appendix J=8.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now unified J=16 with 7 baselines. Model set table in Appendix B. Issue resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Table 3 unified at J=16 with all 7 baselines. Model sets documented.\"\n  resolution_round: 4\n\n- id: \"R2-W5\"\n  summary: \"Main table incomplete — only 3/7 baselines shown\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"7 baselines defined but only 3 in main table.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now contains B0/B1b/B3/B4/B5b/B6/ContamCal. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. All 7 baselines in Table 3.\"\n  resolution_round: 4\n\n- id: \"R2-W7\"\n  summary: \"GSM8K 11× overcorrection ratio — no decision rules\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"11× removed. Decision rules present in §6. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. 11× removed, decision rules added.\"\n  resolution_round: 4\n\n- id: \"R3-N8\"\n  summary: \"Table 5 ARC γ=-1.46 data provenance error\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"internal_reviewer\", note: \"ARC γ=-1.46 from N=8 (含 0.5B), not J=13.\"}\n    - {round: 4, reviewers: \"\", note: \"ARC row removed from domain γ table. All ARC γ CI claims removed from 6 locations (abstract, intro, results×2, conclusion, table). GSM8K row also removed (J=24 mismatch). Table now pure MMLU domain analysis.\"}\n  action_items:\n    - {round: 3, action: \"Remove ARC row from Table 5\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove all ARC γ claims from paper (6 locations)\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove GSM8K row (J=24 mismatch with J=13 caption)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Resolved. ARC and GSM8K rows removed from domain table. All ARC γ CI claims purged from 6 paper locations. Table 5 now pure MMLU domain analysis at J=13.\"\n  resolution_round: 4\n\n- id: \"R2-N3\"\n  summary: \"46% model exclusion rate — sensitivity analysis done\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Exclusion sensitivity analysis present in §5.1 (τ 0.46-0.60, no monotonic trend). Model sets documented in Appendix B. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Sensitivity analysis shows results not sensitive to exclusion rate.\"\n  resolution_round: 4\n\n- id: \"R1-W1\"\n  summary: \"Insufficient differentiation from DCR\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"DCR reimplemented as B6. MAE=0.108/0.314 shows systematic overcorrection. Clear differentiation achieved.\"}\n  action_items: []\n  resolution: \"Resolved. DCR clearly differentiated via reimplementation and direct comparison.\"\n  resolution_round: 4\n\n- id: \"R1-A3\"\n  summary: \"Eckerly (2017) citation needs verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Still cited. R4 reference audit: 9/43 not in OpenAlex (may be indexing delay for books/chapters). Eckerly is a Routledge book chapter — plausible but unverifiable online.\"}\n  action_items:\n    - {round: 1, action: \"WebSearch to verify Eckerly 2017\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Verified. Carol A. Eckerly, Handbook of Quantitative Methods for Detecting Cheating on Tests (Cizek & Wollack eds.), Routledge 2017, ISBN 978-1138821811. Author confirmed as former ETS Senior Psychometrician.\"\n  resolution_round: 5\n\n# Subsumed/tracked issues (unchanged)\n- id: \"R2-W4\"\n  summary: \"Independent per-domain IRT fitting sacrifices common θ scale\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Independent fitting produces incomparable θ scales.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"STEM γ=+0.50 identical.\"}\n    - {round: 4, reviewers: \"\", note: \"Not independently raised in R4. θ incomparability acknowledged in method. Lower priority given domain-level analysis is exploratory.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently raised in R5. Hierarchical IRT (suggested under R4-N1 for multiplicity) would also address this by placing domains on common scale.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Oracle Exposure ablation — interpretation now balanced\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Ground-truth injection labels never used as oracle.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Oracle done but interpretation one-sided.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Oracle ablation present (§5.1). But 'effect heterogeneity' interpretation adopted without equal weight to 'model misspecification' alternative. Subsumed by R3-W10 elevation to critical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Both interpretations now presented. R2 adds: aggregate 0.6-0.7pp is model-free, misspecification only affects γ claims. Tracked under R3-W10.\"}\n  action_items:\n    - {round: 4, action: \"Balance oracle interpretation with misspecification alternative\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"§5.4 oracle ablation now presents both interpretations with equal weight. Tracked under R3-W10.\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Narrative pivot from calibration to diagnostic\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Consider retitling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Subsumed by R2-N1 R4 update. Title changed but framing still methods-paper style.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Tracked under R2-N1. Title is question form but Introduction still builds calibration expectation.\"}\n  action_items:\n    - {round: 4, action: \"Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?')\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Title changed. Tracked under R2-N1.\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Limited technical novelty in IRT modeling\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N7. Novelty is empirical not methodological.\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R3-N7. Both reviewers confirm.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N7.\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"SFT vs real contamination gap\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 (elevated to critical in R4).\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R2-W6. Both reviewers re-confirm.\"}\n  action_items: []\n  resolution: \"Tracked under R2-W6.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"≤3B model scale limits practical applicability\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 ecological validity discussion.\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R2-W6.\"}\n  action_items:\n    - {round: 4, action: \"SFT ≤3B scoping added throughout paper\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Tracked under R2-W6. All claims scoped to SFT ≤3B.\"\n  resolution_round: null\n\n- id: \"R1-A1\"\n  summary: \"ARC PPP systematic misfit\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N3.\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R3-N3.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N3.\"\n  resolution_round: null\n\n- id: \"R1-A2\"\n  summary: \"ARC gamma direction wrong in method_notes.md\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Internal doc issue. Not paper-relevant.\"}\n  action_items: []\n  resolution: \"Internal documentation only, not paper-relevant.\"\n  resolution_round: null\n\n- id: \"R1-A4\"\n  summary: \"3B_d000 GSM8K anomaly needs explanation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Not raised in R4. Lower priority.\"}\n    - {round: 5, reviewers: \"\", note: \"Not raised in R5. Low priority.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?') but framing still inconsistent. Intro ¶1-3 heavily motivate calibration, Results show calibration unnecessary. Contributions 1-3 span empirical finding / engineering observation / exploratory analysis without unified main line. 'Why not just use raw accuracy?' paragraph in Conclusion reads as arguing against paper's own existence. Both AGREE: need full empirical investigation framing from ¶1, ContamCal as investigative instrument not product.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation; ContamCal as tool not contribution; consolidate Contributions to 2 items: (1) empirical null finding + identifiability, (2) diagnostic value + signal failure modes\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without qualification. Pretraining contamination (arXiv 2601.04301) shows significantly larger effects. All claims must be scoped to 'under SFT injection at ≤3B scale'. Both reviewers AGREE unanimously.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract. But title still asks generic question. R2 adds: SFT vs pretraining differs in mechanism not just scale — pretraining contamination embeds into representations (θ) not just LoRA adapter. §5.5 θ asymmetry already hints at this. Both AGREE title needs scoping or Abstract first sentence must scope.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims in Abstract/Intro/Conclusion to 'under SFT injection at ≤3B'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite and discuss pretraining contamination dose-response literature as contrast\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Either scope title ('Does SFT-Injected Benchmark Contamination Need Calibration?') or ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation (AUC=1.0, γ=-0.012 non-sig) has two interpretations: (a) genuine null effect (heterogeneity cancels), (b) model misspecification (linear γ cannot capture threshold/interaction effects). Paper adopts (a) without testing (b). Limitations ¶9 acknowledges threshold possibility but §5.1 oracle section ignores it. Both reviewers AGREE this is fundamental ambiguity.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations. R2 partial REBUT on R1-N1: aggregate 0.6-0.7pp is model-free observation (direct d000 vs d005/d025/d100 accuracy comparison), misspecification only affects γ diagnostic claims. Both AGREE: paper must distinguish model-free findings (aggregate accuracy shift) from model-dependent findings (γ significance/direction). γ-related claims need 'under additive linear specification' caveat.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i or γ×a_i interaction model as misspecification check\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If not testable, explicitly scope claim as 'under linear additive specification'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat to γ-related claims in Abstract/Intro/Conclusion; keep aggregate 0.6-0.7pp finding uncaveated as model-free\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Oracle ablation §5.4 now presents both interpretations with equal weight. Mean a_i comparison (Cohen's d=0.098, r=-0.013) rules out discrimination confound. Limitations ¶9 discusses threshold possibility.\"\n  resolution_round: null\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"8 independent domain tests, only Social Sciences significant at α=0.05. Bonferroni α=0.00625; CI upper bound -0.10 would likely include zero. BH correction also unlikely to survive 1/8 pattern. This is the sole evidence for 'diagnostic value' narrative. Both AGREE correction needed.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 reconfirms: Bonferroni threshold P(γ<0)≥99.375%, Social Sciences at 99.1% does not pass. R2 AGREE with nuance: (1) Bayesian posteriors don't strictly need frequentist correction per Gelman 2012, BUT independent per-domain fits without shrinkage do need correction; (2) Abstract reports P(γ<0)=99.1% without any multiplicity caveat. Both AGREE: report corrected result, or switch to hierarchical IRT for natural shrinkage.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results for domain-level γ\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"If non-significant after correction, reframe as 'suggestive pattern requiring higher-powered replication'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Either (a) add 'uncorrected for multiplicity' when reporting P(γ<0)=99.1% in Abstract/Results, or (b) implement hierarchical IRT with per-domain γ_k drawn from shared hyperprior for natural shrinkage. Option (b) preferred as it also addresses R2-W4 (independent fitting sacrifices common θ scale).\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Switched to Bayesian P(γ<0) framing with Gelman (2012) justification. Social Sciences P(γ<0)=99.1% reported. Prior sensitivity confirms robustness (97.95%-98.92% across N(0,0.5/1.0/2.0)). C3 reframed as 'exploratory domain-level diagnosis requiring J≥50 for confirmation'.\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations but results still in main table\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at J=8, 13, 16 per §5.4. Table 3 still reports ARC IRT results without PPP annotation. R2 nuance: ARC ~0.7pp from raw data is valid, but IRT-derived numbers are unreliable. Both AGREE Table 3 needs PPP annotation and ARC IRT results need caveat.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003 in caption, but ARC IRT results still in main table alongside MMLU giving visual parity. R1: move ARC IRT to Appendix or grey out. R2 AGREE: also helps solve page limit (R5-N1) by shrinking Table 3. Both AGREE 2PL+γ structural misfit for ARC (not just sample size issue) should be discussed in main text.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column in Table 3\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Discuss ARC misfit source (item pool heterogeneity vs model specification)\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix (keep ARC raw accuracy in main table); discuss structural misfit cause (smaller item pool 1172 vs 14042, difficulty distribution homogeneity) in main text\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality aggregation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical by R2. S2 reverses at 0.5B, S4 near-random below 1.5B. §5.2 admits RRF degrades to S1-only. No direct RRF vs S1-only ablation (τ, MAE, γ) at 1.5B/3B where S2 d≈+0.7. R1 partially rebuts absolute claim but agrees ablation is missing. Contribution 2 unsupported without this evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation now complete: S1-only causes MCMC non-convergence (MMLU R̂=1.53) due to exposure variance compression ([0.749,0.867]). This proves RRF necessary for IRT convergence. However R1 W3 insight (R2 calls 'most insightful observation'): ablation evidence supports RRF for exposure VARIANCE, not signal QUALITY. S1 AUC>0.95 exceeds RRF composite. Paper conflates these: 'not only signal quality aggregation but exposure variance' implies both supported, only latter is. Both AGREE: precise the contribution claim. Downgraded to warning since core ablation is done.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2 in D134 reframing\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation at 1.5B and 3B (τ, MAE, γ significance)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If RRF ≤ S1-only, downgrade Contribution 2 to 'item filtering improves IRT' without RRF-specific claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish 'RRF necessary for exposure variance diversification' from 'RRF provides superior signal quality'. Report RRF composite AUC vs S1-only AUC. Revise §5.1 summary sentence accordingly.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"RRF ablation complete. S1-only completely fails: MCMC non-convergence on MMLU (R̂=1.53, ESS=7), degenerate solution on ARC. RRF essential for exposure variance (compression to [0.749,0.867] under S1-only). §5.1 new paragraph documents ablation. C2 strengthened, not downgraded.\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically fails — reported only in Limitations\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"§5.1 only reports 50%. 80%/95% completely missing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"CI coverage now reported in Limitations: MMLU 83%/89%/100%, ARC 45%/65%/90%. ARC under-coverage corroborates PPP<0.05 misfit. Both AGREE this should be in main results, not just Limitations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results. R1: MMLU 95% CI covers 100% = completely uninformative. R2 AGREE, adds: over-coverage (MMLU) and under-coverage (ARC) have different root causes and should be discussed separately. MMLU over-coverage likely from posterior θ uncertainty at J=16; ARC under-coverage from structural misfit (PPP=0.003).\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage discussion to main results section\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss over-coverage and under-coverage root causes separately; acknowledge MMLU 95% CI = uninformative\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"CI coverage moved to §5.1 main results.\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses (13/16/24/28) and all below paper's own J≥50 threshold\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Contribution 4 combines simulation + empirical. Should split.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"J inconsistency from experimental timeline (domain runs before 3B retraining). All γ conclusions at J=13-16 are underpowered by paper's own standard. Both AGREE needs prominent caveat and ideally unified J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Model set table in Appendix B. But core problem: most interesting finding (domain γ) uses weakest configuration (J=13). Prior sensitivity in Appendix C uses J=16 for Social Sciences but main Table 2 still reports J=13. Both AGREE: either rerun domain analysis at J=16, or explicitly state J=13 vs J=16 consistency in main text.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J and model composition prominently in each table/figure\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16, or add main-text statement on J=13 vs J=16 consistency citing Appendix C\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Model set transparency table added to Appendix B (tab_model_sets) with 4 rows for J=16/13/16-28/13. Each table/figure caption now references J and configuration.\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 (300 RRF) vs 0.46 (2000 random) may reflect higher average a_i in RRF-selected items, not contamination signal value. Need discrimination-matched random subset comparison or report average a_i of RRF vs random sets.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently re-raised in R5. Resolution from R4 (mean a_i comparison, Cohen's d=0.098) appears in §5.1. Possibly resolved pending confirmation.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items; add discrimination-matched control\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Mean a_i comparison: RRF-selected mean=1.12, random mean=1.09, Cohen's d=0.098, r=-0.013. No discrimination confound. §5.1 documents this exclusion.\"\n  resolution_round: null\n\n- id: \"R1-C2\"\n  summary: \"Cross-family 'validation' title misleading for J=4 single-seed data\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"'Validated' too strong for single-seed N=3-4.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"§4.2 references 'Appendix E post-hoc power calculations' but Appendix E (sec:full_baselines) contains baseline tables, not power analysis. This is missing content, not just hard to find. Both strongly AGREE.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Phantom Appendix E reference removed. But §5.5 title still 'Cross-Family Validation' despite J=4 single seed + d100 MMLU excluded (effective Llama range only d000-d025). Both AGREE: rename to 'Cross-Family Exploratory Analysis' or 'Preliminary Cross-Family Evidence'. Llama d100 MMLU catastrophic collapse suggests cross-architecture SFT injection mechanism fundamentally differs from within-family.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Write and include actual Appendix E power analysis OR remove the reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 from 'Cross-Family Validation' to 'Preliminary Cross-Family Analysis' or similar\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Appendix E cross-reference removed from experimental_setup.tex. No phantom reference remains.\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50. Prior N(0,1) dominance?\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"γ~N(0,1) covers ±2 logit units. No prior sensitivity analysis. Need at least N(0,0.5) and N(0,2) alternatives. Also need e_ij distribution (mean, SD) to interpret γ effect size. Both AGREE.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently re-raised in R5. Prior sensitivity analysis now in Appendix C showing pooled γ is prior-dominated (2.6× shift), Social Sciences is data-dominated (1.2× shift). e_ij distribution reported. Possibly resolved.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2); report e_ij distribution\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Full prior sensitivity complete. Pooled: γ shifts 0.34→0.89 (2.6×, prior-dominated), all CI include 0. Social Sciences: γ -0.43→-0.51 (1.2× shift, data-dominated), all CI exclude 0, P(γ<0)≥97.95%. e_ij distribution: mean=0.041, median=0.016, max=0.879. Appendix prior_sensitivity section added.\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption at 0.5B but provides no direct evidence (e.g., perplexity distributions). Alternative explanations (position bias confound, near-full-rank LoRA catastrophic forgetting) not ruled out. R2 considers minor since empirical finding is well-documented. R1 wants either evidence or explicit 'mechanism TBD'.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 W4: Min-K%++ reversal may be SFT artifact rather than inherent Min-K%++ flaw (0.5B position bias = SFT-induced catastrophic behavior). R2 partial REBUT: paper already qualifies as post-hoc with alternatives listed. Both AGREE: Conclusion claim 'Min-K%++ should not be trusted at the 0.5B scale' must be scoped to 'under SFT injection'.\"}\n  action_items:\n    - {round: 4, action: \"Either provide token-level perplexity comparison or reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion claim to 'Min-K%++ should not be trusted at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Limitations reframed causal explanation as 'post-hoc hypothesis' with alternative explanations listed.\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Five contributions too many — now consolidated to 3 but still lacks unified main line\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span null finding, item filtering, signal failure, identifiability, domain diagnosis. R2 suggests consolidate to 2-3. R1 agrees with reservation (null finding alone too thin for long paper). Suggest: (1) framework+null finding, (2) signal reliability boundaries (merge C3+C4), demote C5 to observation.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions. R2 N3: still span different types (empirical finding / engineering observation / exploratory analysis) without unified main line. R1 AGREE. Both suggest further consolidation to 2 contributions.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Consider further consolidation to 2 contributions: (1) empirical null finding + identifiability analysis, (2) diagnostic value + signal failure modes\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Contributions consolidated to 3: C1(null finding + identifiability analysis), C2(signal-guided filtering + failure modes), C3(exploratory domain-level diagnosis).\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — now partially resolved but IRT classics still absent\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. (EACL Findings 2026) 'Quantifying Data Contamination in Psychometric Evaluations of LLMs' is most direct concurrent work — combines IRT + contamination. arXiv 2601.04301 provides pretraining dose-response data contradicting null finding scope. Chen et al. EMNLP 2025 survey. R1 cannot independently verify but agrees in principle they should be checked and cited.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R4 references added. New gaps: (1) IRT classics — Lord (1980), Hambleton et al. (1991) are standard references for papers using 2PL; (2) HELM (Liang et al. 2023) for LLM evaluation context; (3) Magar & Schwartz (2022) for early contamination analysis. R1 AGREE all 4. Also: Han et al. differentiation needs 3-4 sentences not 1 sentence (R1 partial REBUT R2-W5: actual differences larger than described but paper should expand).\"}\n  action_items:\n    - {round: 4, action: \"Verify and cite Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025 survey\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord (1980), Hambleton et al. (1991), Liang et al. (2023) HELM, Magar & Schwartz (2022). Expand Han et al. comparison to 3-4 sentences in Related Work.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"All 5 references verified and added: han2026quantifying, schaeffer2026causally, chen2025benchmarking, singh2024evaluation, gelman2012why.\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'. Per-domain model fit unverifiable. Especially critical for Social Sciences (sole significant domain). Both AGREE must report.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present in Table (0.096-0.570). Not re-raised in R5. Possibly resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values in Table 2\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"PPP values filled in Table 5 (domain γ table): range 0.096-0.570.\"\n  resolution_round: null\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers crowd out narrative. Both AGREE should trim to ~200 words with 2-3 key numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Abstract now ~202 words (within range) but still contains 8-9 specific numbers (~12 quantitative info points per R1 count). Reads like compressed Results not independent story. Both AGREE: keep 2-3 key numbers (aggregate effect, identifiability threshold), replace rest with qualitative descriptions.\"}\n  action_items:\n    - {round: 4, action: \"Trim Abstract to ≤220 words, reduce to 2-3 key numbers\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further reduce numeric density: keep ~0.6-0.7pp and J≥50 threshold, replace τ values/Cohen's d/γ values with qualitative statements\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"Abstract trimmed to ~202 words.\"\n  resolution_round: null\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF applied to new domain\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT now cited. But Han et al. EACL 2026 (IRT+contamination) uncited — potentially closer concurrent work. Technical novelty remains limited: 2PL+γ is standard explanatory IRT/DIF. Value is empirical, not methodological.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R2 N2: paper self-acknowledges 'formally an instance of explanatory DIF'. Han et al. EACL 2026 now cited but differentiation is one sentence. R1 AGREE novelty limited. Both AGREE: must explicitly position as empirical contribution, not methodological innovation. Continuous vs binary exposure (paper's claimed differentiation from Han et al.) shown irrelevant by own oracle ablation.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. EACL 2026 as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state in Introduction that technical modeling is not the contribution; contribution is systematic empirical investigation of whether calibration is needed\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"PSN-IRT and Han et al. now cited. Paper positioned as empirical contribution, not methodological novelty.\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation + IRT classics\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"33 citations.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"PSN-IRT, Kocyigit, Holland now cited. But new gaps: Han et al. EACL 2026, arXiv 2601.04301, Chen EMNLP 2025 survey. See R4-W4.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. R4 gaps filled. New gaps: Lord (1980), Hambleton (1991), HELM, Magar & Schwartz (2022). Han et al. comparison needs expansion. R1 partial REBUT R2-W5: actual differences are larger (goal-level: detection vs calibration; group-based vs continuous DIF; counterfactual inference) but paper must articulate them.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al., Chen et al., Singh et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord (1980), Hambleton (1991), HELM, Magar & Schwartz. Expand Han et al. comparison paragraph.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"All identified references now cited. 5 new bib entries added in Round 4.\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-N1\"\n  summary: \"Page limit exceeded — main content ~8.5 pages, ACL limit is 8 pages\"\n  category: format\n  severity: critical\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Tables 4 and 3 (Results section tables) float to page 9 top. Discussion/Conclusion text continues to page 9. Limitations begins at ~60% of page 9. Main content ~8.5 pages. ACL Long paper: ≤8 pages content, Limitations/Ethics/References/Appendix excluded. Desk-reject risk. Both AGREE. R1 suggests: compress §5.1 RRF ablation to 3-4 lines + Appendix pointer; R2 suggests: move Table 2 (domain γ) to Appendix, inline Table 3 numbers. Moving ARC IRT to Appendix (R3-N3 fix) also helps.\"}\n  action_items:\n    - {round: 5, action: \"Reduce main content to ≤8 pages. Priority cuts: (1) move ARC IRT from Table 3 to Appendix; (2) compress §5.1 RRF ablation paragraph; (3) consider moving Table 2 to Appendix or reducing Table 3 to inline format.\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"Method §3.1 defines y_ijk with k = benchmark, but Eq.2 uses k = stratum/domain. Understandable in context but should be explicitly noted.\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes from benchmark to domain stratum\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-W2\"\n  summary: \"Ethics Statement too brief — no dual-use risk discussion\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Ethics Statement is 4 sentences covering data/model licensing only. No discussion of dual-use risks (e.g., detection signals being reverse-engineered to optimize contamination strategies, or framework being used to game leaderboards). Both flag as minor.\"}\n  action_items:\n    - {round: 5, action: \"Add 1-2 sentences on dual-use risk of contamination detection/calibration methods\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# New issue from Round 5\n- id: \"R5-W3\"\n  summary: \"B1b label unexplained in Table 3\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - {round: 5, reviewers: \"R1\", note: \"Table 3 lists 'B1b: Remove & Rescore' and 'B5b: Emperor' but neither 'B1a' nor 'B5a' appear in the paper. The 'b' suffix is unexplained.\"}\n  action_items:\n    - {round: 5, action: \"Either explain B1a/B1b distinction or remove 'b' suffix\", assigned_to: \"paper_agent\", status: \"pending\"}\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues (unchanged from Round 4)\n- id: \"R2-N6\"\n  summary: \"Format non-compliance: Limitations after references + missing Ethics Statement\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Limitations is subsection under Discussion.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations still after bibliography. Ethics absent.\"}\n    - {round: 4, reviewers: \"\", note: \"R4 format check confirms Limitations before references, Ethics Statement present. Issue resolved.\"}\n  action_items:\n    - {round: 2, action: \"Move Limitations before references\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Add Ethics Statement\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Resolved. Limitations and Ethics both present before bibliography. Confirmed in R4.\"\n  resolution_round: 4\n\n- id: \"R1-C1\"\n  summary: \"Missing 1.5B/3B experimental data in Tables\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Table 1 only 0.5B.\"}\n    - {round: 3, reviewers: \"\", note: \"Subsumed by R2-W5 and R3-N5.\"}\n  action_items: []\n  resolution: \"Resolved. Table 4 now J=16 (8×1.5B + 8×3B) with all baselines.\"\n  resolution_round: 3\n\n- id: \"R1-C3\"\n  summary: \"Triple impossibility over-generalized\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"DCR existence is counter-example.\"}\n    - {round: 3, reviewers: \"\", note: \"Triple impossibility removed from draft.\"}\n  action_items: []\n  resolution: \"Resolved — triple impossibility claim removed.\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Fisher Information simulation now has heatmap visualization\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 3\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Figure 2 with heatmap now present.\"}\n  action_items: []\n  resolution: \"Resolved — Figure 2 with heatmap now present.\"\n  resolution_round: 3\n\n- id: \"R1-W5\"\n  summary: \"Observational experiments over-interpret causal claims\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Paper restructured, observational experiments no longer present.\"}\n  action_items: []\n  resolution: \"Resolved — paper restructured.\"\n  resolution_round: 3\n\n- id: \"R1-W7\"\n  summary: \"Table 2 title misleading\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 3, reviewers: \"\", note: \"Table captions rewritten.\"}\n  action_items: []\n  resolution: \"Resolved — table captions updated.\"\n  resolution_round: 3\n\n- id: \"R3-N5\"\n  summary: \"Baseline configuration inconsistency — main table J vs appendix J\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"R1,R2\", note: \"Main Table J=13 vs appendix J=8.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now unified J=16 with 7 baselines. Model set table in Appendix B. Issue resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Table 3 unified at J=16 with all 7 baselines. Model sets documented.\"\n  resolution_round: 4\n\n- id: \"R2-W5\"\n  summary: \"Main table incomplete — only 3/7 baselines shown\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"7 baselines defined but only 3 in main table.\"}\n    - {round: 4, reviewers: \"\", note: \"Table 3 now contains B0/B1b/B3/B4/B5b/B6/ContamCal. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. All 7 baselines in Table 3.\"\n  resolution_round: 4\n\n- id: \"R2-W7\"\n  summary: \"GSM8K 11× overcorrection ratio — no decision rules\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"11× removed. Decision rules present in §6. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. 11× removed, decision rules added.\"\n  resolution_round: 4\n\n- id: \"R3-N8\"\n  summary: \"Table 5 ARC γ=-1.46 data provenance error\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  mentions:\n    - {round: 3, reviewers: \"internal_reviewer\", note: \"ARC γ=-1.46 from N=8 (含 0.5B), not J=13.\"}\n    - {round: 4, reviewers: \"\", note: \"ARC row removed from domain γ table. All ARC γ CI claims removed from 6 locations (abstract, intro, results×2, conclusion, table). GSM8K row also removed (J=24 mismatch). Table now pure MMLU domain analysis.\"}\n  action_items:\n    - {round: 3, action: \"Remove ARC row from Table 5\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove all ARC γ claims from paper (6 locations)\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Remove GSM8K row (J=24 mismatch with J=13 caption)\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Resolved. ARC and GSM8K rows removed from domain table. All ARC γ CI claims purged from 6 paper locations. Table 5 now pure MMLU domain analysis at J=13.\"\n  resolution_round: 4\n\n- id: \"R2-N3\"\n  summary: \"46% model exclusion rate — sensitivity analysis done\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Exclusion sensitivity analysis present in §5.1 (τ 0.46-0.60, no monotonic trend). Model sets documented in Appendix B. Resolved.\"}\n  action_items: []\n  resolution: \"Resolved. Sensitivity analysis shows results not sensitive to exclusion rate.\"\n  resolution_round: 4\n\n- id: \"R1-W1\"\n  summary: \"Insufficient differentiation from DCR\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"DCR reimplemented as B6. MAE=0.108/0.314 shows systematic overcorrection. Clear differentiation achieved.\"}\n  action_items: []\n  resolution: \"Resolved. DCR clearly differentiated via reimplementation and direct comparison.\"\n  resolution_round: 4\n\n- id: \"R1-A3\"\n  summary: \"Eckerly (2017) citation needs verification\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 4\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Still cited. R4 reference audit: 9/43 not in OpenAlex (may be indexing delay for books/chapters). Eckerly is a Routledge book chapter — plausible but unverifiable online.\"}\n  action_items:\n    - {round: 1, action: \"WebSearch to verify Eckerly 2017\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Verified. Carol A. Eckerly, Handbook of Quantitative Methods for Detecting Cheating on Tests (Cizek & Wollack eds.), Routledge 2017, ISBN 978-1138821811. Author confirmed as former ETS Senior Psychometrician.\"\n  resolution_round: 5\n\n# Subsumed/tracked issues (unchanged)\n- id: \"R2-W4\"\n  summary: \"Independent per-domain IRT fitting sacrifices common θ scale\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 4\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Independent fitting produces incomparable θ scales.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"STEM γ=+0.50 identical.\"}\n    - {round: 4, reviewers: \"\", note: \"Not independently raised in R4. θ incomparability acknowledged in method. Lower priority given domain-level analysis is exploratory.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently raised in R5. Hierarchical IRT (suggested under R4-N1 for multiplicity) would also address this by placing domains on common scale.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W2\"\n  summary: \"Oracle Exposure ablation — interpretation now balanced\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Ground-truth injection labels never used as oracle.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Oracle done but interpretation one-sided.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Oracle ablation present (§5.1). But 'effect heterogeneity' interpretation adopted without equal weight to 'model misspecification' alternative. Subsumed by R3-W10 elevation to critical.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Both interpretations now presented. R2 adds: aggregate 0.6-0.7pp is model-free, misspecification only affects γ claims. Tracked under R3-W10.\"}\n  action_items:\n    - {round: 4, action: \"Balance oracle interpretation with misspecification alternative\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"§5.4 oracle ablation now presents both interpretations with equal weight. Tracked under R3-W10.\"\n  resolution_round: null\n\n- id: \"R1-W2\"\n  summary: \"Narrative pivot from calibration to diagnostic\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 1, reviewers: \"R2,R1\", note: \"Consider retitling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Subsumed by R2-N1 R4 update. Title changed but framing still methods-paper style.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Tracked under R2-N1. Title is question form but Introduction still builds calibration expectation.\"}\n  action_items:\n    - {round: 4, action: \"Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?')\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Title changed. Tracked under R2-N1.\"\n  resolution_round: null\n\n- id: \"R1-W3\"\n  summary: \"Limited technical novelty in IRT modeling\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N7. Novelty is empirical not methodological.\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R3-N7. Both reviewers confirm.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N7.\"\n  resolution_round: null\n\n- id: \"R1-W6\"\n  summary: \"SFT vs real contamination gap\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 (elevated to critical in R4).\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R2-W6. Both reviewers re-confirm.\"}\n  action_items: []\n  resolution: \"Tracked under R2-W6.\"\n  resolution_round: null\n\n- id: \"R2-W3\"\n  summary: \"≤3B model scale limits practical applicability\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R2-W6 ecological validity discussion.\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R2-W6.\"}\n  action_items:\n    - {round: 4, action: \"SFT ≤3B scoping added throughout paper\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"Tracked under R2-W6. All claims scoped to SFT ≤3B.\"\n  resolution_round: null\n\n- id: \"R1-A1\"\n  summary: \"ARC PPP systematic misfit\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Subsumed by R3-N3.\"}\n    - {round: 5, reviewers: \"\", note: \"Tracked under R3-N3.\"}\n  action_items: []\n  resolution: \"Tracked under R3-N3.\"\n  resolution_round: null\n\n- id: \"R1-A2\"\n  summary: \"ARC gamma direction wrong in method_notes.md\"\n  category: writing\n  severity: info\n  status: wont_fix\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Internal doc issue. Not paper-relevant.\"}\n  action_items: []\n  resolution: \"Internal documentation only, not paper-relevant.\"\n  resolution_round: null\n\n- id: \"R1-A4\"\n  summary: \"3B_d000 GSM8K anomaly needs explanation\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 1\n  last_seen_round: 1\n  mentions:\n    - {round: 4, reviewers: \"\", note: \"Not raised in R4. Lower priority.\"}\n    - {round: 5, reviewers: \"\", note: \"Not raised in R5. Low priority.\"}\n  action_items: []\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-18T01:48:47.182835+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 44781}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-18T01:51:41.194535+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "report": "# Round 5 Consolidated Review Report\n\n**论文**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (Findings track)\n**Deadline**: 2026-05-25\n**Reviewers**: R1（方法严谨性 + 实验有效性）, R2（新颖性 + 完整性 + 写作质量）\n**Cross-sharing**: 完成，所有关键问题已达成共识\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 用 Reciprocal Rank Fusion 融合多个 contamination detection signals 生成连续 exposure scores；Stage 2 将其嵌入 contamination-augmented 2PL IRT 模型（2PL+γ）进行校准。在 Qwen2.5 (0.5B-3B) 的 LoRA SFT injection 实验中得到核心 null finding：aggregate contamination effect 仅 ~0.6-0.7pp，raw accuracy 已是最优估计。论文将框架价值重新定位为 diagnostic（domain-level γ 异质性分析），附带 Min-K%++ 在 0.5B 的 directional reversal 发现和 γ recovery 的 identifiability boundary 分析（J≥50 at AUC≥0.55）。\n\n---\n\n## Strengths\n\n**S1. Null finding 的负责任报告 [R1, R2 共识]**\n在 publication bias 严重的领域中，坦诚报告 ContamCal 未能超越 raw accuracy 是值得肯定的。Table 3 系统性展示了所有 7 个 baseline 的比较，DCR 的 systematic overcorrection (MAE 0.108-0.314) 为社区提供了有价值的负面证据。\n\n**S2. 统计方法论超出 NLP 论文典型水平 [R1, R2 共识]**\nBayesian inference via NUTS + proper convergence diagnostics (split-R̂ < 1.01, bulk ESS > 400)、oracle ablation (ground-truth binary labels)、prior sensitivity analysis (区分 prior-dominated vs data-dominated conclusions)、simulation study for identifiability boundaries。\n\n**S3. Min-K%++ directional reversal 有实用价值 [R1, R2 共识]**\nCohen's d = -1.55 to -1.98 at 0.5B 是此前未报告的 failure mode。对 contamination detection 实践有直接指导意义（practitioners 不应在 small-scale SFT models 上使用 Min-K%++）。\n\n**S4. Identifiability boundary analysis 提供 actionable guidelines [R1, R2 共识]**\nJ≥50 at AUC≥0.55 的定量条件为未来 IRT-based LLM evaluation research 建立了操作标准，当前实践 (J=8-30) 远低于此阈值。\n\n**S5. RRF vs S1-only ablation 揭示了 IRT 应用的实践洞察 [R1]**\nS1-only item selection 导致 exposure variance compression ([0.749, 0.867]) 和 MCMC non-convergence (R̂=1.53, ESS=7)，证明了 multi-signal fusion 对 IRT parameter separability 的必要性。\n\n**S6. 写作质量整体良好 [R2]**\n无 em-dash，无显著 AI 写作痕迹。Calibration disambiguation paragraph 是好的预防性澄清。Limitations 覆盖 9 条，坦诚充分。\n\n---\n\n## Weaknesses — Must-Fix（影响接收决定）\n\n**W1. [critical] 页面超限 [R2 提出, R1 AGREE]**\nTables 2/3 (Results 核心内容) 浮动到 page 9 顶部，Discussion/Conclusion 尾部延续到 page 9，Limitations 约在 page 9 的 60% 才开始。主要内容约 8.5 页，超出 ACL Long paper ≤8 页正文限制。存在 desk-reject 风险。\n- 修改方向：(1) 移 ARC IRT 结果到 Appendix（同时解决 W3）; (2) 压缩 §5.1 RRF ablation 段落 (~15 行→3-4 行 + Appendix pointer); (3) 考虑 Table 2 (domain γ) 移入 Appendix 或 Table 3 inline 化。\n\n**W2. [critical] 叙事不一致：method paper vs empirical investigation [R2 提出, R1 AGREE]**\n- Introduction ¶1-3 重度 motivate \"post-hoc calibration is essential\"，建立 calibration 方法改进的期待\n- Results 发现 raw accuracy 最好，framework 的核心 pitch 被自己的实验推翻\n- Contributions 1-3 分属 empirical finding / engineering observation / exploratory analysis，缺乏统一主线\n- \"Why not just use raw accuracy?\" 段落在论证自己论文不必要\n- Subtitle \"An IRT Decomposition Study\" 与 method paper framing 矛盾\n- 修改方向：从 ¶1 即以 question-driven empirical investigation 切入；ContamCal 定位为 investigative instrument 而非最终产品；Contributions 精简为 2 条。\n\n**W3. [critical] ARC PPP=0.003 下结果与 MMLU 并列呈现 [R1 提出, R2 AGREE]**\nPPP=0.003 在所有 J 配置 (8/13/16) 下持续，表明 2PL+γ 对 ARC 的结构性 misfit。Table 3 中 ARC IRT 与 MMLU 并列给读者同等可靠的印象。Caption caveat 容易被忽略。\n- 修改方向：ARC IRT 移入 Appendix（保留 raw accuracy）；讨论 misfit 原因（item pool 更小 1172 vs 14042、difficulty distribution homogeneity）。\n\n**W4. [critical] SFT injection 生态效度限制核心 claim 适用范围 [R1 提出, R2 AGREE]**\n标题暗示通用结论，但证据仅覆盖 LoRA SFT injection at ≤3B。Pretraining contamination 机制根本不同（distributed exposure across millions of steps, representation-level embedding, no instruction formatting artifact）。Schaeffer et al. (2026) 显示 pretraining contamination 可能产生更大效应。R2 补充：pretraining contamination 可能 embed into θ rather than capturable by γ（§5.5 θ asymmetry 已暗示此点）。\n- 修改方向：标题加限定（\"Does SFT-Injected Benchmark Contamination Need Calibration?\"）或 Abstract 首句即 scope 为 SFT injection。\n\n**W5. [critical] Social Sciences γ=-0.57 未经多重比较校正 [R1 提出, R2 AGREE]**\n8 个 MMLU domain 独立检验，仅 Social Sciences 达 P(γ<0)=99.1%。Bonferroni 阈值 P≥99.375%，不通过。Abstract 直接报告此数字未标注 multiplicity。R2 nuance：独立 per-domain fits 无 shrinkage，Gelman 2012 的 Bayesian 免校正论证需要 hierarchical model。\n- 修改方向：(a) Abstract 中加 \"uncorrected for multiplicity\"；(b) 报告 Bonferroni-adjusted 结论；(c) 最优方案：改用 hierarchical IRT (per-domain γ_k from shared hyperprior)，自然实现 shrinkage + multiplicity adjustment。\n\n**W6. [critical] 技术新颖性有限 [R2 提出, R1 AGREE]**\n2PL+γ 是 standard explanatory IRT/DIF 的直接应用。论文自己承认 \"formally an instance of explanatory DIF\"。与 Han et al. EACL 2026 差异仅在 continuous vs binary exposure + domain stratification，是 modeling 变体而非 paradigm shift。论文的 oracle ablation 用 binary labels 也得到 non-significant γ，说明 continuous vs binary 区别在此设置下无实质影响。\n- 修改方向：明确定位为 empirical investigation，不 claim 方法创新。\n\n---\n\n## Weaknesses — Should-Fix（影响评分但不一票否决）\n\n**W7. [warning] Oracle ablation 的 model-free vs model-dependent 结论未区分 [R1 提出, R2 partial REBUT → 收敛]**\nR2 partial rebut 有实质贡献：aggregate 0.6-0.7pp 是 model-free observation（直接 d000 vs d005/d025/d100 accuracy 差异），不依赖 γ specification。但 γ diagnostic claims（Social Sciences P(γ<0)=99.1%, domain-level heterogeneity）依赖 additive linear specification。论文应在 Abstract/Results 中区分：model-free findings 保持原有表述，model-dependent findings 加 specification caveat。\n- 注：R2 补充：aggregate negligibility 可能掩盖 item-level distortions，§5.4 opposing domain signs 正是证据。\n\n**W8. [warning] Abstract 数字密度过高 [R2 提出, R1 AGREE]**\n~202 words 含 8-9 个具体数值（~12 quantitative info points），读起来像 Results 压缩版。应保留 2-3 个关键数字（aggregate effect, identifiability threshold），其余改为定性描述。\n\n**W9. [warning] J 值跨分析不一致 [R1 提出, R2 AGREE]**\nDomain-level analysis（最有趣的 finding）使用 J=13（统计功效最低的配置），而 pooled baselines 用 J=16。原因是实验时间线，但后续完整数据未用于重新验证 domain findings。Appendix C 中 J=16 prior sensitivity 确认 Social Sciences 方向，但主文 Table 2 仍报告 J=13。\n\n**W10. [warning] Cross-family \"Validation\" 标题误导 [R1 提出, R2 AGREE]**\n§5.5 标题 \"Cross-Family Validation\" vs 实际内容 J=4 single-seed + Llama d100 MMLU excluded。与论文自己的 \"exploratory\" 标注矛盾。Llama catastrophic format collapse 暗示 cross-architecture SFT injection 机制根本不同。\n\n**W11. [warning] RRF 的贡献是 exposure variance 而非 signal quality [R1 提出, R2 AGREE（\"R1 最独到的观察\"）]**\nAblation 证据仅支持 RRF 对 exposure variance diversification 的贡献。S1 AUC > 0.95 远超 RRF composite。§5.1 总结句 \"not only signal quality aggregation but exposure variance\" 暗示两者都有证据支持，但实际只有后者有实验验证。\n\n**W12. [warning] \"Diagnostic value\" 叙事说服力不足 [R2 提出, R1 AGREE]**\n8 domains 中 1 个 significant（uncorrected）、J=13 被论文自己标为 exploratory（需 J≥50）、family-specific 不跨架构推广。作为 Contribution 3 的支撑证据链不够强。\n\n**W13. [warning] Han et al. EACL 2026 差异化不足 [R2 提出, R1 partial REBUT → 收敛]**\nR1 nuance：实际差异比 R2 描述的更大（目标不同：detection vs calibration；continuous vs group-based DIF；counterfactual inference），但论文仅用一句话区分。应扩展为 3-4 句话，在 Method §2.1 讨论为什么 continuous exposure 在 LLM 场景下更合适。\n\n**W14. [warning] CI coverage 不对称且解释不足 [R1 提出, R2 AGREE]**\nMMLU 50% CI covers 83%（over-coverage = uninformative intervals），ARC 50% CI covers 45%（under-coverage = overconfident）。MMLU 95% CI covers 100% = 完全无信息。Over-coverage 和 under-coverage 根源不同，应分开讨论。\n\n**W15. [warning] Min-K%++ directional reversal 可能是 SFT artifact [R1 提出, R2 partial REBUT → 收敛]**\nR2 认为论文已 qualify（post-hoc hypothesis + alternative explanations），但两者都同意 Conclusion claim \"Min-K%++ should not be trusted at the 0.5B scale\" 应限定为 \"under SFT injection\"。\n\n**W16. [warning] Missing references: IRT classics + LLM evaluation [R2 提出, R1 AGREE 全部 4 条]**\n缺少 Lord (1980), Hambleton et al. (1991) 作为 IRT 基础文献；缺少 HELM (Liang et al. 2023) 作为 LLM evaluation 代表性工作；缺少 Magar & Schwartz (2022) 作为 contamination 早期文献。\n\n**W17. [info] -ing 分词短语散见 [R2 提出, R1 AGREE（影响极低）]**\nmethod.tex 中 \"adapting...\", \"avoiding...\", \"making it applicable...\" 等处，密度不高但存在。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下所有关键问题上达成一致（[AGREE]）：\n\n1. **Overall 3.0 (Findings)**：方法框架有参考价值，null finding 对社区有信息量，但证据强度和影响力不足以支撑主会议。\n2. **SFT 生态效度**：核心限制。标题/Abstract 需更明确 scope。\n3. **ARC PPP<0.05**：IRT 结果不应与 MMLU 并列呈现。\n4. **多重比较**：Social Sciences 在 Bonferroni 校正下不通过，Abstract 未标注。\n5. **页面超限**：~8.5 页，desk-reject 风险。\n6. **叙事不一致**：method paper vs empirical investigation framing 混淆。\n7. **技术新颖性**：2PL+γ 是 standard explanatory IRT/DIF 应用。\n8. **Cross-family 标题**：\"Validation\" 对 J=4 数据过强。\n9. **RRF variance vs quality**：ablation 仅支持 variance 贡献。\n10. **Abstract 数字密度**：需进一步精简。\n\n---\n\n## Reviewer Divergence\n\n所有分歧已在交叉回应中收敛为具体修改建议，无遗留矛盾：\n\n| 问题 | 分歧 | 收敛结论 |\n|------|------|---------|\n| Oracle/misspecification (R1-N1) | R2 partial REBUT: aggregate 0.6-0.7pp 是 model-free | 共识：区分 model-free findings 和 model-dependent findings，分层限定 |\n| Min-K++ causal (R1-W4) | R2 partial REBUT: 论文已 qualify | 共识：post-hoc 标注足够，但 Conclusion claim 需加 \"under SFT injection\" |\n| Han et al. (R2-W5) | R1 partial REBUT: 实际差异更大 | 共识：差异确实存在但论文应展开为 3-4 句话 |\n\n---\n\n## Questions for Authors\n\n1. **Domain γ at J=16**: 是否可以在 J=16 配置下重跑 domain-level γ 分析以确认 Social Sciences finding？\n2. **Non-linear γ specification**: 是否尝试过 threshold model (γ·𝟙[e>τ]) 或 interaction terms (γ×a_i) 来区分 genuine null 和 misspecification？\n3. **RRF composite AUC**: RRF 融合后的 overall AUC 与 S1-only AUC 的直接对比是什么？S1 + uniform noise 是否也能达到类似的 exposure variance？\n4. **Hierarchical IRT**: 是否考虑过 hierarchical model (per-domain γ_k from shared hyperprior) 来同时解决 multiplicity 和 independent fitting 问题？\n5. **Han et al. 实验对比**: Han et al. EACL 2026 在类似设置下的结论是什么？continuous vs binary exposure 的差异是否在可比条件下产生不同结果？\n6. **Code/data release**: Stan 代码、SFT 训练脚本和实验数据是否计划开源？\n\n---\n\n## Missing References\n\n| 参考文献 | 理由 | R1/R2 一致性 |\n|----------|------|-------------|\n| Lord (1980) \"Applications of IRT to Practical Testing Problems\" | IRT 奠基性教科书，使用 2PL 的论文应引 | 两者 AGREE |\n| Hambleton, Swaminathan & Rogers (1991) \"Fundamentals of IRT\" | IRT 标准参考 | 两者 AGREE |\n| Liang et al. (2023) HELM | LLM evaluation 代表性框架 | 两者 AGREE |\n| Magar & Schwartz (2022) \"Data Contamination: From Memorization to Exploitation\" | Contamination 早期系统研究 | 两者 AGREE |\n\n另需核实：holland_1993_dif (OpenAlex 返回 year=2009, author=Osterlind)、deboeck_2004_explanatory_irt (OpenAlex 返回 year=2005) 的元数据准确性。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中未找到 external_review.paperreview_ai.enabled 设置）。\n\n---\n\n## Overall Assessment\n\n**3.0 — Findings（可被 Findings 接收）**\n\n**置信度**: 4/5（两位 Reviewer 均有 IRT + LLM evaluation 领域背景，核心判断高度一致）\n\n**评分理由**:\n\n论文提出了一个合理的框架（将 detection signals 嵌入 IRT 进行 contamination calibration），实验设计在受控条件下严谨，null finding 的报告诚实透明。附带贡献（Min-K%++ reversal, identifiability boundaries）对社区有实用价值。\n\n但以下根本限制将论文定位于 Findings 而非主会议：\n\n1. **SFT ecological validity**: 核心 null finding 仅在 SFT injection ≤3B 下成立。Pretraining contamination 机制完全不同，可能产生更大效应。论文回答的是 \"SFT injection 需要校准吗？\" 而非标题所问的 \"LLM benchmark contamination 需要校准吗？\"\n\n2. **Technical novelty**: 2PL+γ 是 standard explanatory IRT/DIF，不是方法创新。与 Han et al. EACL 2026 的差异化不足。贡献在 empirical 层面，但 empirical 范围又被 SFT/≤3B 严格限定。\n\n3. **Evidence strength**: 三个贡献中，C1 (null finding) 受 SFT proxy 限制，C3 (domain diagnosis) 受 multiple comparison + J=13 underpowered 限制。C2 (signal failure modes) 是最 solid 的但属于 empirical observation。\n\n4. **Narrative**: 仍在 method paper 和 empirical investigation 之间摇摆。Introduction 建立 calibration 期待，Results 推翻之，造成读者期待落差。\n\n5. **Format**: 页面超限 (~8.5 页) 需立即修复。\n\n**与 Findings 接收标准的匹配度**:\n- ✅ 有用的实证知识（null finding 有信息量）\n- ✅ 方法论有参考价值（identifiability analysis, signal failure modes）\n- ✅ 统计规范高于领域平均\n- ❌ 影响力受限于 SFT/≤3B 条件\n- ❌ 不提供新方法或新 insight beyond \"calibration is unnecessary at small scale\"\n\n**修复后评分可能提升至 3.5 (Borderline Conference) 的条件**:\n(a) 页面超限修复 + 叙事统一为 empirical investigation；\n(b) 添加 hierarchical IRT 结果解决 multiplicity；\n(c) 增加 1-2 个 naturally contaminated model（如利用 GSM1K parallel test set）提升生态效度。\n其中 (a) 在 deadline 前可完成，(b)(c) 可能需要更多时间。\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- 数字密度过高（~12 quantitative info points in 202 words）。保留 aggregate effect + identifiability threshold，其余改为定性。\n- P(γ<0)=99.1% 需标注 \"uncorrected for multiplicity\" 或删除。\n- \"raw accuracy is already well-calibrated\" 是 model-free finding，可保持；γ-related claims 加 specification caveat。\n\n### Introduction\n- ¶1-3 过度 motivate calibration 方法的需求，与 Results 中 null finding 形成期待落差。\n- ¶3 \"No existing method bridges...\" 需考虑 Han et al. EACL 2026 是否已部分 bridge。\n- Contribution list 建议精简为 2 条，统一为 question-driven framing。\n\n### Related Work\n- 48 citations 量级合理，但缺少 IRT classics (Lord 1980, Hambleton 1991) 和 LLM evaluation framework (HELM)。\n- Han et al. 差异化仅 1 句话，需扩展为 3-4 句话讨论 goal-level 和 mechanism-level 差异。\n- Calibration disambiguation paragraph 是优秀的写法。\n\n### Method\n- 符号 k 在 §3.1 (benchmark index) 和 Eq.2 (domain/stratum index) 之间复用，需注明。\n- RRF 的 meta-circularity avoidance justification 写得好。\n- 2PL+γ additive structure 的 linear assumption 应在此处（而非仅 Limitations）讨论 potential misspecification。\n\n### Experimental Setup\n- SFT injection 设计严谨（controlled dosage, multiple seeds, quality-control filter）。\n- 0.5B 排除逻辑合理（position bias）。\n- Cross-family analysis 标题需从 \"Validation\" 改为 \"Exploratory Analysis\"。\n- B1b/B5b 的 \"b\" 后缀未解释。\n\n### Results\n- RRF ablation 段落可大幅压缩（核心 message 是 S1-only 导致 variance compression → MCMC failure）。\n- Table 3 ARC 列应移至 Appendix 或标注不可靠。\n- \"Diagnostic value of γ\" 段需明确区分 model-free vs model-dependent conclusions。\n\n### Discussion and Conclusion\n- \"Why not just use raw accuracy?\" 是好问题但 framing 不理想——应从 ¶1 开始就设置为 \"the answer may be no\"。\n- \"Min-K%++ should not be trusted at the 0.5B scale\" 需加 \"under SFT injection\"。\n- 可增加：在什么条件下 ContamCal 会优于 raw accuracy（larger models, pretraining contamination, better signals）。\n\n### Limitations\n- 9 条，覆盖面广，诚实。\n- \"Additive γ linearity\" 讨论应在 Method 中也出现，不仅在 Limitations。\n- CI coverage 的 over/under-coverage 根源应分开讨论（MMLU: posterior θ uncertainty; ARC: structural misfit）。\n\n### Ethics Statement\n- 过于简短（4 句）。应补充 dual-use risk 讨论。\n\n### Appendix\n- Prior sensitivity analysis 严谨。\n- Model set composition table 有价值。\n- 建议将 ARC IRT 详细结果、RRF ablation 技术细节移入此处以释放正文空间。\n\n---\n\n**Issue Tracker 状态**: Round 5 新增 4 个 issue (R5-N1 page limit, R5-W1 symbol overload, R5-W2 ethics brevity, R5-W3 B1b label)，更新 15 个已有 issue 的 last_seen_round 和 mentions。6 个 critical issue 仍为 in_progress (R2-N1 framing, R2-W6 SFT validity, R3-W10 γ misspecification, R4-N1 multiplicity, R3-N3 ARC PPP, R5-N1 page limit)。1 个新 critical issue (R5-N1 page limit) + R3-N7 novelty (warning but fundamental)。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "report": "# Round 5 Consolidated Review Report\n\n**论文**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**Venue**: EMNLP 2026 via ACL Rolling Review (Findings track)\n**Deadline**: 2026-05-25\n**Reviewers**: R1（方法严谨性 + 实验有效性）, R2（新颖性 + 完整性 + 写作质量）\n**Cross-sharing**: 完成，所有关键问题已达成共识\n\n---\n\n## Summary\n\n本文提出 ContamCal，一个两阶段框架：Stage 1 用 Reciprocal Rank Fusion 融合多个 contamination detection signals 生成连续 exposure scores；Stage 2 将其嵌入 contamination-augmented 2PL IRT 模型（2PL+γ）进行校准。在 Qwen2.5 (0.5B-3B) 的 LoRA SFT injection 实验中得到核心 null finding：aggregate contamination effect 仅 ~0.6-0.7pp，raw accuracy 已是最优估计。论文将框架价值重新定位为 diagnostic（domain-level γ 异质性分析），附带 Min-K%++ 在 0.5B 的 directional reversal 发现和 γ recovery 的 identifiability boundary 分析（J≥50 at AUC≥0.55）。\n\n---\n\n## Strengths\n\n**S1. Null finding 的负责任报告 [R1, R2 共识]**\n在 publication bias 严重的领域中，坦诚报告 ContamCal 未能超越 raw accuracy 是值得肯定的。Table 3 系统性展示了所有 7 个 baseline 的比较，DCR 的 systematic overcorrection (MAE 0.108-0.314) 为社区提供了有价值的负面证据。\n\n**S2. 统计方法论超出 NLP 论文典型水平 [R1, R2 共识]**\nBayesian inference via NUTS + proper convergence diagnostics (split-R̂ < 1.01, bulk ESS > 400)、oracle ablation (ground-truth binary labels)、prior sensitivity analysis (区分 prior-dominated vs data-dominated conclusions)、simulation study for identifiability boundaries。\n\n**S3. Min-K%++ directional reversal 有实用价值 [R1, R2 共识]**\nCohen's d = -1.55 to -1.98 at 0.5B 是此前未报告的 failure mode。对 contamination detection 实践有直接指导意义（practitioners 不应在 small-scale SFT models 上使用 Min-K%++）。\n\n**S4. Identifiability boundary analysis 提供 actionable guidelines [R1, R2 共识]**\nJ≥50 at AUC≥0.55 的定量条件为未来 IRT-based LLM evaluation research 建立了操作标准，当前实践 (J=8-30) 远低于此阈值。\n\n**S5. RRF vs S1-only ablation 揭示了 IRT 应用的实践洞察 [R1]**\nS1-only item selection 导致 exposure variance compression ([0.749, 0.867]) 和 MCMC non-convergence (R̂=1.53, ESS=7)，证明了 multi-signal fusion 对 IRT parameter separability 的必要性。\n\n**S6. 写作质量整体良好 [R2]**\n无 em-dash，无显著 AI 写作痕迹。Calibration disambiguation paragraph 是好的预防性澄清。Limitations 覆盖 9 条，坦诚充分。\n\n---\n\n## Weaknesses — Must-Fix（影响接收决定）\n\n**W1. [critical] 页面超限 [R2 提出, R1 AGREE]**\nTables 2/3 (Results 核心内容) 浮动到 page 9 顶部，Discussion/Conclusion 尾部延续到 page 9，Limitations 约在 page 9 的 60% 才开始。主要内容约 8.5 页，超出 ACL Long paper ≤8 页正文限制。存在 desk-reject 风险。\n- 修改方向：(1) 移 ARC IRT 结果到 Appendix（同时解决 W3）; (2) 压缩 §5.1 RRF ablation 段落 (~15 行→3-4 行 + Appendix pointer); (3) 考虑 Table 2 (domain γ) 移入 Appendix 或 Table 3 inline 化。\n\n**W2. [critical] 叙事不一致：method paper vs empirical investigation [R2 提出, R1 AGREE]**\n- Introduction ¶1-3 重度 motivate \"post-hoc calibration is essential\"，建立 calibration 方法改进的期待\n- Results 发现 raw accuracy 最好，framework 的核心 pitch 被自己的实验推翻\n- Contributions 1-3 分属 empirical finding / engineering observation / exploratory analysis，缺乏统一主线\n- \"Why not just use raw accuracy?\" 段落在论证自己论文不必要\n- Subtitle \"An IRT Decomposition Study\" 与 method paper framing 矛盾\n- 修改方向：从 ¶1 即以 question-driven empirical investigation 切入；ContamCal 定位为 investigative instrument 而非最终产品；Contributions 精简为 2 条。\n\n**W3. [critical] ARC PPP=0.003 下结果与 MMLU 并列呈现 [R1 提出, R2 AGREE]**\nPPP=0.003 在所有 J 配置 (8/13/16) 下持续，表明 2PL+γ 对 ARC 的结构性 misfit。Table 3 中 ARC IRT 与 MMLU 并列给读者同等可靠的印象。Caption caveat 容易被忽略。\n- 修改方向：ARC IRT 移入 Appendix（保留 raw accuracy）；讨论 misfit 原因（item pool 更小 1172 vs 14042、difficulty distribution homogeneity）。\n\n**W4. [critical] SFT injection 生态效度限制核心 claim 适用范围 [R1 提出, R2 AGREE]**\n标题暗示通用结论，但证据仅覆盖 LoRA SFT injection at ≤3B。Pretraining contamination 机制根本不同（distributed exposure across millions of steps, representation-level embedding, no instruction formatting artifact）。Schaeffer et al. (2026) 显示 pretraining contamination 可能产生更大效应。R2 补充：pretraining contamination 可能 embed into θ rather than capturable by γ（§5.5 θ asymmetry 已暗示此点）。\n- 修改方向：标题加限定（\"Does SFT-Injected Benchmark Contamination Need Calibration?\"）或 Abstract 首句即 scope 为 SFT injection。\n\n**W5. [critical] Social Sciences γ=-0.57 未经多重比较校正 [R1 提出, R2 AGREE]**\n8 个 MMLU domain 独立检验，仅 Social Sciences 达 P(γ<0)=99.1%。Bonferroni 阈值 P≥99.375%，不通过。Abstract 直接报告此数字未标注 multiplicity。R2 nuance：独立 per-domain fits 无 shrinkage，Gelman 2012 的 Bayesian 免校正论证需要 hierarchical model。\n- 修改方向：(a) Abstract 中加 \"uncorrected for multiplicity\"；(b) 报告 Bonferroni-adjusted 结论；(c) 最优方案：改用 hierarchical IRT (per-domain γ_k from shared hyperprior)，自然实现 shrinkage + multiplicity adjustment。\n\n**W6. [critical] 技术新颖性有限 [R2 提出, R1 AGREE]**\n2PL+γ 是 standard explanatory IRT/DIF 的直接应用。论文自己承认 \"formally an instance of explanatory DIF\"。与 Han et al. EACL 2026 差异仅在 continuous vs binary exposure + domain stratification，是 modeling 变体而非 paradigm shift。论文的 oracle ablation 用 binary labels 也得到 non-significant γ，说明 continuous vs binary 区别在此设置下无实质影响。\n- 修改方向：明确定位为 empirical investigation，不 claim 方法创新。\n\n---\n\n## Weaknesses — Should-Fix（影响评分但不一票否决）\n\n**W7. [warning] Oracle ablation 的 model-free vs model-dependent 结论未区分 [R1 提出, R2 partial REBUT → 收敛]**\nR2 partial rebut 有实质贡献：aggregate 0.6-0.7pp 是 model-free observation（直接 d000 vs d005/d025/d100 accuracy 差异），不依赖 γ specification。但 γ diagnostic claims（Social Sciences P(γ<0)=99.1%, domain-level heterogeneity）依赖 additive linear specification。论文应在 Abstract/Results 中区分：model-free findings 保持原有表述，model-dependent findings 加 specification caveat。\n- 注：R2 补充：aggregate negligibility 可能掩盖 item-level distortions，§5.4 opposing domain signs 正是证据。\n\n**W8. [warning] Abstract 数字密度过高 [R2 提出, R1 AGREE]**\n~202 words 含 8-9 个具体数值（~12 quantitative info points），读起来像 Results 压缩版。应保留 2-3 个关键数字（aggregate effect, identifiability threshold），其余改为定性描述。\n\n**W9. [warning] J 值跨分析不一致 [R1 提出, R2 AGREE]**\nDomain-level analysis（最有趣的 finding）使用 J=13（统计功效最低的配置），而 pooled baselines 用 J=16。原因是实验时间线，但后续完整数据未用于重新验证 domain findings。Appendix C 中 J=16 prior sensitivity 确认 Social Sciences 方向，但主文 Table 2 仍报告 J=13。\n\n**W10. [warning] Cross-family \"Validation\" 标题误导 [R1 提出, R2 AGREE]**\n§5.5 标题 \"Cross-Family Validation\" vs 实际内容 J=4 single-seed + Llama d100 MMLU excluded。与论文自己的 \"exploratory\" 标注矛盾。Llama catastrophic format collapse 暗示 cross-architecture SFT injection 机制根本不同。\n\n**W11. [warning] RRF 的贡献是 exposure variance 而非 signal quality [R1 提出, R2 AGREE（\"R1 最独到的观察\"）]**\nAblation 证据仅支持 RRF 对 exposure variance diversification 的贡献。S1 AUC > 0.95 远超 RRF composite。§5.1 总结句 \"not only signal quality aggregation but exposure variance\" 暗示两者都有证据支持，但实际只有后者有实验验证。\n\n**W12. [warning] \"Diagnostic value\" 叙事说服力不足 [R2 提出, R1 AGREE]**\n8 domains 中 1 个 significant（uncorrected）、J=13 被论文自己标为 exploratory（需 J≥50）、family-specific 不跨架构推广。作为 Contribution 3 的支撑证据链不够强。\n\n**W13. [warning] Han et al. EACL 2026 差异化不足 [R2 提出, R1 partial REBUT → 收敛]**\nR1 nuance：实际差异比 R2 描述的更大（目标不同：detection vs calibration；continuous vs group-based DIF；counterfactual inference），但论文仅用一句话区分。应扩展为 3-4 句话，在 Method §2.1 讨论为什么 continuous exposure 在 LLM 场景下更合适。\n\n**W14. [warning] CI coverage 不对称且解释不足 [R1 提出, R2 AGREE]**\nMMLU 50% CI covers 83%（over-coverage = uninformative intervals），ARC 50% CI covers 45%（under-coverage = overconfident）。MMLU 95% CI covers 100% = 完全无信息。Over-coverage 和 under-coverage 根源不同，应分开讨论。\n\n**W15. [warning] Min-K%++ directional reversal 可能是 SFT artifact [R1 提出, R2 partial REBUT → 收敛]**\nR2 认为论文已 qualify（post-hoc hypothesis + alternative explanations），但两者都同意 Conclusion claim \"Min-K%++ should not be trusted at the 0.5B scale\" 应限定为 \"under SFT injection\"。\n\n**W16. [warning] Missing references: IRT classics + LLM evaluation [R2 提出, R1 AGREE 全部 4 条]**\n缺少 Lord (1980), Hambleton et al. (1991) 作为 IRT 基础文献；缺少 HELM (Liang et al. 2023) 作为 LLM evaluation 代表性工作；缺少 Magar & Schwartz (2022) 作为 contamination 早期文献。\n\n**W17. [info] -ing 分词短语散见 [R2 提出, R1 AGREE（影响极低）]**\nmethod.tex 中 \"adapting...\", \"avoiding...\", \"making it applicable...\" 等处，密度不高但存在。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下所有关键问题上达成一致（[AGREE]）：\n\n1. **Overall 3.0 (Findings)**：方法框架有参考价值，null finding 对社区有信息量，但证据强度和影响力不足以支撑主会议。\n2. **SFT 生态效度**：核心限制。标题/Abstract 需更明确 scope。\n3. **ARC PPP<0.05**：IRT 结果不应与 MMLU 并列呈现。\n4. **多重比较**：Social Sciences 在 Bonferroni 校正下不通过，Abstract 未标注。\n5. **页面超限**：~8.5 页，desk-reject 风险。\n6. **叙事不一致**：method paper vs empirical investigation framing 混淆。\n7. **技术新颖性**：2PL+γ 是 standard explanatory IRT/DIF 应用。\n8. **Cross-family 标题**：\"Validation\" 对 J=4 数据过强。\n9. **RRF variance vs quality**：ablation 仅支持 variance 贡献。\n10. **Abstract 数字密度**：需进一步精简。\n\n---\n\n## Reviewer Divergence\n\n所有分歧已在交叉回应中收敛为具体修改建议，无遗留矛盾：\n\n| 问题 | 分歧 | 收敛结论 |\n|------|------|---------|\n| Oracle/misspecification (R1-N1) | R2 partial REBUT: aggregate 0.6-0.7pp 是 model-free | 共识：区分 model-free findings 和 model-dependent findings，分层限定 |\n| Min-K++ causal (R1-W4) | R2 partial REBUT: 论文已 qualify | 共识：post-hoc 标注足够，但 Conclusion claim 需加 \"under SFT injection\" |\n| Han et al. (R2-W5) | R1 partial REBUT: 实际差异更大 | 共识：差异确实存在但论文应展开为 3-4 句话 |\n\n---\n\n## Questions for Authors\n\n1. **Domain γ at J=16**: 是否可以在 J=16 配置下重跑 domain-level γ 分析以确认 Social Sciences finding？\n2. **Non-linear γ specification**: 是否尝试过 threshold model (γ·𝟙[e>τ]) 或 interaction terms (γ×a_i) 来区分 genuine null 和 misspecification？\n3. **RRF composite AUC**: RRF 融合后的 overall AUC 与 S1-only AUC 的直接对比是什么？S1 + uniform noise 是否也能达到类似的 exposure variance？\n4. **Hierarchical IRT**: 是否考虑过 hierarchical model (per-domain γ_k from shared hyperprior) 来同时解决 multiplicity 和 independent fitting 问题？\n5. **Han et al. 实验对比**: Han et al. EACL 2026 在类似设置下的结论是什么？continuous vs binary exposure 的差异是否在可比条件下产生不同结果？\n6. **Code/data release**: Stan 代码、SFT 训练脚本和实验数据是否计划开源？\n\n---\n\n## Missing References\n\n| 参考文献 | 理由 | R1/R2 一致性 |\n|----------|------|-------------|\n| Lord (1980) \"Applications of IRT to Practical Testing Problems\" | IRT 奠基性教科书，使用 2PL 的论文应引 | 两者 AGREE |\n| Hambleton, Swaminathan & Rogers (1991) \"Fundamentals of IRT\" | IRT 标准参考 | 两者 AGREE |\n| Liang et al. (2023) HELM | LLM evaluation 代表性框架 | 两者 AGREE |\n| Magar & Schwartz (2022) \"Data Contamination: From Memorization to Exploitation\" | Contamination 早期系统研究 | 两者 AGREE |\n\n另需核实：holland_1993_dif (OpenAlex 返回 year=2009, author=Osterlind)、deboeck_2004_explanatory_irt (OpenAlex 返回 year=2005) 的元数据准确性。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中未找到 external_review.paperreview_ai.enabled 设置）。\n\n---\n\n## Overall Assessment\n\n**3.0 — Findings（可被 Findings 接收）**\n\n**置信度**: 4/5（两位 Reviewer 均有 IRT + LLM evaluation 领域背景，核心判断高度一致）\n\n**评分理由**:\n\n论文提出了一个合理的框架（将 detection signals 嵌入 IRT 进行 contamination calibration），实验设计在受控条件下严谨，null finding 的报告诚实透明。附带贡献（Min-K%++ reversal, identifiability boundaries）对社区有实用价值。\n\n但以下根本限制将论文定位于 Findings 而非主会议：\n\n1. **SFT ecological validity**: 核心 null finding 仅在 SFT injection ≤3B 下成立。Pretraining contamination 机制完全不同，可能产生更大效应。论文回答的是 \"SFT injection 需要校准吗？\" 而非标题所问的 \"LLM benchmark contamination 需要校准吗？\"\n\n2. **Technical novelty**: 2PL+γ 是 standard explanatory IRT/DIF，不是方法创新。与 Han et al. EACL 2026 的差异化不足。贡献在 empirical 层面，但 empirical 范围又被 SFT/≤3B 严格限定。\n\n3. **Evidence strength**: 三个贡献中，C1 (null finding) 受 SFT proxy 限制，C3 (domain diagnosis) 受 multiple comparison + J=13 underpowered 限制。C2 (signal failure modes) 是最 solid 的但属于 empirical observation。\n\n4. **Narrative**: 仍在 method paper 和 empirical investigation 之间摇摆。Introduction 建立 calibration 期待，Results 推翻之，造成读者期待落差。\n\n5. **Format**: 页面超限 (~8.5 页) 需立即修复。\n\n**与 Findings 接收标准的匹配度**:\n- ✅ 有用的实证知识（null finding 有信息量）\n- ✅ 方法论有参考价值（identifiability analysis, signal failure modes）\n- ✅ 统计规范高于领域平均\n- ❌ 影响力受限于 SFT/≤3B 条件\n- ❌ 不提供新方法或新 insight beyond \"calibration is unnecessary at small scale\"\n\n**修复后评分可能提升至 3.5 (Borderline Conference) 的条件**:\n(a) 页面超限修复 + 叙事统一为 empirical investigation；\n(b) 添加 hierarchical IRT 结果解决 multiplicity；\n(c) 增加 1-2 个 naturally contaminated model（如利用 GSM1K parallel test set）提升生态效度。\n其中 (a) 在 deadline 前可完成，(b)(c) 可能需要更多时间。\n\n---\n\n## Detailed Comments by Section\n\n### Abstract\n- 数字密度过高（~12 quantitative info points in 202 words）。保留 aggregate effect + identifiability threshold，其余改为定性。\n- P(γ<0)=99.1% 需标注 \"uncorrected for multiplicity\" 或删除。\n- \"raw accuracy is already well-calibrated\" 是 model-free finding，可保持；γ-related claims 加 specification caveat。\n\n### Introduction\n- ¶1-3 过度 motivate calibration 方法的需求，与 Results 中 null finding 形成期待落差。\n- ¶3 \"No existing method bridges...\" 需考虑 Han et al. EACL 2026 是否已部分 bridge。\n- Contribution list 建议精简为 2 条，统一为 question-driven framing。\n\n### Related Work\n- 48 citations 量级合理，但缺少 IRT classics (Lord 1980, Hambleton 1991) 和 LLM evaluation framework (HELM)。\n- Han et al. 差异化仅 1 句话，需扩展为 3-4 句话讨论 goal-level 和 mechanism-level 差异。\n- Calibration disambiguation paragraph 是优秀的写法。\n\n### Method\n- 符号 k 在 §3.1 (benchmark index) 和 Eq.2 (domain/stratum index) 之间复用，需注明。\n- RRF 的 meta-circularity avoidance justification 写得好。\n- 2PL+γ additive structure 的 linear assumption 应在此处（而非仅 Limitations）讨论 potential misspecification。\n\n### Experimental Setup\n- SFT injection 设计严谨（controlled dosage, multiple seeds, quality-control filter）。\n- 0.5B 排除逻辑合理（position bias）。\n- Cross-family analysis 标题需从 \"Validation\" 改为 \"Exploratory Analysis\"。\n- B1b/B5b 的 \"b\" 后缀未解释。\n\n### Results\n- RRF ablation 段落可大幅压缩（核心 message 是 S1-only 导致 variance compression → MCMC failure）。\n- Table 3 ARC 列应移至 Appendix 或标注不可靠。\n- \"Diagnostic value of γ\" 段需明确区分 model-free vs model-dependent conclusions。\n\n### Discussion and Conclusion\n- \"Why not just use raw accuracy?\" 是好问题但 framing 不理想——应从 ¶1 开始就设置为 \"the answer may be no\"。\n- \"Min-K%++ should not be trusted at the 0.5B scale\" 需加 \"under SFT injection\"。\n- 可增加：在什么条件下 ContamCal 会优于 raw accuracy（larger models, pretraining contamination, better signals）。\n\n### Limitations\n- 9 条，覆盖面广，诚实。\n- \"Additive γ linearity\" 讨论应在 Method 中也出现，不仅在 Limitations。\n- CI coverage 的 over/under-coverage 根源应分开讨论（MMLU: posterior θ uncertainty; ARC: structural misfit）。\n\n### Ethics Statement\n- 过于简短（4 句）。应补充 dual-use risk 讨论。\n\n### Appendix\n- Prior sensitivity analysis 严谨。\n- Model set composition table 有价值。\n- 建议将 ARC IRT 详细结果、RRF ablation 技术细节移入此处以释放正文空间。\n\n---\n\n**Issue Tracker 状态**: Round 5 新增 4 个 issue (R5-N1 page limit, R5-W1 symbol overload, R5-W2 ethics brevity, R5-W3 B1b label)，更新 15 个已有 issue 的 last_seen_round 和 mentions。6 个 critical issue 仍为 in_progress (R2-N1 framing, R2-W6 SFT validity, R3-W10 γ misspecification, R4-N1 multiplicity, R3-N3 ARC PPP, R5-N1 page limit)。1 个新 critical issue (R5-N1 page limit) + R3-N7 novelty (warning but fundamental)。"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-18T01:51:46.808290+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5613
}
```

</details>

---


### Assistant

_source line 482 · 2026-05-18T01:51:54.253716+00:00_

**Round 5 审稿完成。**

**最终评分：3.0 — Findings**（两位 Reviewer 一致，交叉回应后全面收敛）

**核心结论**：

6 个 Must-Fix（critical）：
1. **页面超限** (~8.5 页，desk-reject 风险)
2. **叙事不一致** (method paper vs empirical investigation framing 混淆)
3. **ARC PPP=0.003** (不应与 MMLU 并列呈现)
4. **SFT 生态效度** (标题/Abstract 需 scope 为 SFT injection)
5. **多重比较** (Social Sciences P(γ<0)=99.1% Bonferroni 不通过)
6. **技术新颖性有限** (2PL+γ 是 standard explanatory IRT/DIF)

11 个 Should-Fix（warning），3 个 info 级。

**可提升至 3.5 (Borderline Conference) 的条件**：(a) 页面修复 + 叙事统一为 empirical investigation；(b) hierarchical IRT 解决 multiplicity；(c) naturally contaminated model 提升生态效度。其中 (a) 在 deadline 前可完成。

审稿报告和 Issue Tracker 均已提交/更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 48

## Round 48

2 recorded events


### User

_source line 483 · 2026-05-18T01:51:56.925852+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：R1 的 9 条意见中 AGREE 6 条，partial REBUT 2 条（N1 和 W4），完全 REBUT 0 条。

最重要的 convergence point：两位 reviewer 在 scope 限制（SFT-only title）、cross-family "validation" 误导、narrative consistency 上观点一致。R1 的 multiple comparison 校正（N2）是我遗漏的重要统计问题，我完全接受。我对 N1 的 partial rebut 有实质性理由：0.6-0.7pp 是 raw accuracy 差异的直接测量，不依赖 IRT model specification。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 484 · 2026-05-18T01:52:09.839984+00:00_

审稿报告已投递至 Research Director。

**Round 5 审稿结果摘要**：

**Overall: 3.0 (Findings)**，两位 Reviewer 一致。

**6 个 critical issues**（Must-Fix）：
1. **页面超限** (~8.5 页，desk-reject 风险)
2. **叙事不一致** (method paper vs empirical investigation framing 混淆)
3. **ARC PPP=0.003** (IRT 结果不应与 MMLU 并列)
4. **SFT 生态效度** (标题暗示通用结论但证据仅覆盖 SFT ≤3B)
5. **多重比较** (Social Sciences P(γ<0)=99.1% 在 Bonferroni 下不通过)
6. **技术新颖性有限** (2PL+γ 是 standard explanatory IRT/DIF)

**关键 convergence**：所有 critical issues 两位 Reviewer 均 AGREE。仅有 2 处 partial REBUT 已收敛为具体修改建议（区分 model-free vs model-dependent conclusions；Min-K%++ claim 加 SFT scope）。

**修复后可能提升至 3.5 的条件**：(a) 页面修复 + 叙事统一为 empirical investigation；(b) hierarchical IRT 解决 multiplicity；(c) 增加 naturally contaminated model 提升生态效度。其中 (a) 在 deadline 前可完成。

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 485 · 2026-05-18T01:54:45.701814+00:00_

[RESET REQUEST] Main Agent 达到硬限
  触发原因：idle 240min
  本轮累计 1 条消息 / 4h 1min

⚠️ 你自己的 context 状态：已 1 条消息 / 4h 1min

请回复：
  [RESET AGENT]     只重置 Main Agent，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Main Agent 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 486 · 2026-05-18T01:54:52.268774+00:00_

审稿报告已投递完毕，本轮圆桌审稿已收敛（两位 Reviewer 共识，Issue Tracker 已更新，报告已提交至 Research Director）。

[RESET BOTH]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 50

## Round 50

2 recorded events


### User

_source line 487 · 2026-05-18T01:56:04.872130+00:00_

[RESET REQUEST] Research Reviewer 达到硬限
  触发原因：运行时长 4h16m
  本轮累计 8 条消息 / 4h 16min

⚠️ 你自己的 context 状态：已 8 条消息 / 4h 16min

请回复：
  [RESET AGENT]     只重置 Research Reviewer，你继续
  [RESET BOTH]      顺便也重置你自己（推荐，如果本轮讨论已收敛）
  [DEFER Xm]        Xm 后再说
  [DENY <原因>]     不重置，让 Research Reviewer 继续带着上下文工作

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 488 · 2026-05-18T01:56:16.078926+00:00_

审稿报告已成功提交给 Research Director，本轮工作完成。

[RESET BOTH]

理由：Round 5 审稿圆桌已完成全部流程（独立审稿 → 交叉分享 → 收敛判断 → 报告投递 + Issue Tracker 更新）。两位 Reviewer 均给出 3.0 (Findings)，交叉回应中所有关键问题达成共识，报告已投递。本 session 无后续任务。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 51

## Round 51

70 recorded events


### User

_source line 489 · 2026-05-18T04:43:11.421282+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contamcal-irt-calibration
- 论文路径: projects/contamcal-irt-calibration/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-18T04:43:18.032984+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-18T04:43:18.084165+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-18T04:43:20.955699+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 493 · 2026-05-18T04:43:21.006420+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-18T04:43:25.174056+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-18T04:43:25.275364+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 496 · 2026-05-18T04:43:28.991127+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "7"
  }
}
```

</details>

---


### Tool result

_source line 497 · 2026-05-18T04:43:29.092045+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-18T04:43:32.558692+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-18T04:43:33.063870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-18T04:43:34.470002+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (279 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_006_mmlu_vanilla_2pl_fullitems | Full MMLU 14k items vanilla 2PL IRT to compute more robust Kendall tau ranking correlation (replacing 300 subsampled items version) | — | — | — |\n\n## 待处理\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\n- signals_05B_s123_batch（准备中）\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\n- exp_001_sft_15B_d025_s123（准备中）\n- exp_001_sft_3B_d000_v4（准备中）\n- exp_001_sft_3B_d000_s42（准备中）\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\n- exp_001_sft_d005_05B_r3: 0.5B d005 SFT retry #3 after OOM, superseded by later successful runs (v3 PID 239729)（准备中）\n- exp_001_eval_3B_d025_s123: 3B d025 seed=123 aligned eval for pooled IRT N
…[truncated 2657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1911
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-18T04:43:34.621143+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-18T04:43:34.722171+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	
12	\title{Does LLM Benchmark Contamination Need Calibration?\\An IRT Decomposition Study}
13	
14	\author{Anonymous}
15	
16	\begin{document}
17	\maketitle
18	
19	\begin{abstract}
20	\input{abstract}
21	\end{abstract}
22	
23	\input{introduction}
24	\input{related_work}
25	\input{method}
26	\input{experimental_setup}
27	\input{results}
28	\input{conclusion}
29	
30	\input{limitations}
31	\input{ethics}
32	
33	\bibliography{references}
34	
35	\input{appendix}
36	
37	\end{document}
38	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 503 · 2026-05-18T04:43:38.688710+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information about EMNLP 2026 call for papers submission guidelines, though the results pri
…[truncated 1165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 5624
}
```

</details>

---


### Tool call

_source line 504 · 2026-05-18T04:43:44.164680+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-18T04:43:45.370398+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines template page limit author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines template page limit author instructions"
  }
}
```

</details>

---


### Tool call

_source line 506 · 2026-05-18T04:43:45.822917+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 507 · 2026-05-18T04:43:49.743564+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on
…[truncated 1153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 5578
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-18T04:43:52.856289+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines template page limit author instructions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Submitting your paper for review - ACLPUB","url":"https://acl-org.github.io/ACLPUB/review-version.html"}]

Based on the search results, here's information about ACL Rolling Review 2026 submission guidelines:

## Submission Templates and Formatting

Submissions must adhere to the formatting in the submission templates, which is available as an Overleaf template. The template has a [review] setting that must be on for the submission. Additionally, ARR abandons the MS Word Template for conference submissions, with submissions based on the Word template desk-rejected starting fro
…[truncated 1166 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 7485
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-18T04:43:52.857130+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml\", \"content\": \"# Literature Map — contamcal-irt-calibration\\n# Generated: 2026-05-16\\n# Purpose: Related Work section foundation for ContamCal paper (EMNLP 2026)\\n\\npapers:\\n\\n  # ============================================================\\n  # Category: detection — Contamination Detection Methods\\n  # ============================================================\\n\\n  - id: \\\"zhang_2024_minkpp\\\"\\n    title: \\\"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"ICLR 2025\\\"\\n    year: 2024\\n    url: \\\"https://arxiv.org/abs/2404.02936\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"method-component\\\"\\n    relevance: \\\"Our S2 signal. Min-K%++ normalizes token probability with vocabulary statistics for membership inference. We discover its directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — a novel finding that challenges single-signal reliance.\\\"\\n    key_findings: \\\"Theoretically motivated detection via normalized token probabilities; outperforms Min-K% on WikiMIA and other benchmarks.\\\"\\n    our_advantage: \\\"ContamCal reveals Min-K++ is actively misleading (not just ineffective) at small scales — directional reversal is our headline empirical finding.\\\"\\n\\n  - id: \\\"shi_2023_minkprob\\\"\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"ICLR 2024\\\"\\n    year: 2023\\n    url: \\\"https://arxiv.org/abs/2310.16789\\\"\\n    category: \\\"detection\\\"\\n    role: \\\"foundation\\\"\\n    relevance: \\\"Original Min-K% Prob method and WikiMIA benchmark. Foundation for membership inference in LLMs. Min-K%++ (our S2) is a direct extension.\\\"\\n    key_findings: \\\
…[truncated 3811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7034
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-18T04:43:59.787787+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review May 2026 page limit long paper short paper formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review May 2026 page limit long paper short paper formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-18T04:44:00.743493+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-18T04:44:01.045169+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-18T04:44:01.095998+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-18T04:44:06.720638+00:00_

Web search results for query: "ACL Rolling Review May 2026 page limit long paper short paper formatting requirements"

Links: [{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

Based on the search results, here are the ACL Rolling Review (ARR) page limits and formatting requirements for long and short papers:

## Page Limits

Long papers must follow a page limit of 8 pages, and short papers must follow a page limit of 4 pages, not including limitations and ethical considerations.

## Formatting Requirements

### Content and Structure

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Review ve
…[truncated 947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6932
}
```

</details>

---


### Tool result

_source line 515 · 2026-05-18T04:44:06.721039+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 5625
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-18T04:44:11.843681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 517 · 2026-05-18T04:44:12.346068+00:00_

1	We investigate whether Item Response Theory (IRT) can separate genuine ability from contamination artifacts on Large Language Model (LLM) benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B--3B) and three benchmarks (MMLU, ARC-Challenge, GSM8K) as a testbed, we find that contamination shifts aggregate accuracy by only ${\sim}$0.6--0.7 percentage points, smaller than the estimation noise of any correction method; raw accuracy is already well-calibrated. We develop ContamCal, a two-stage pipeline that combines multi-signal item filtering with a contamination-augmented IRT model (2PL+$\gamma$). Signal-guided filtering substantially improves ability-dosage rank correlation over random subsets, while single-signal selection causes IRT convergence failure. Min-K\%++ exhibits strong directional reversal at the 0.5B scale. Domain-level analysis reveals heterogeneity: Social Sciences shows a negative $\gamma$ effect with high posterior confidence (uncorrected for multiplicity), a suggestive pattern that requires replication. Simulation studies establish that reliable $\gamma$ recovery requires $J \geq 50$, well above current practice. This structural gap between available ensemble sizes and statistical requirements limits contamination diagnosis via IRT.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 518 · 2026-05-18T04:44:12.346553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 519 · 2026-05-18T04:44:12.848627+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection, resource allocation, and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. The community has responded with twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, yet a fundamental question remains unanswered: what is the actual effect size of contamination on aggregate scores? Without this measurement, every mitigation decision is made in the dark. Quantifying the real effect of contamination on scores is therefore a prerequisite for any calibration decision.
4	
5	The literature implicitly assumes that the effect is large. Mitigation papers develop elaborate countermeasures; replacement benchmarks sacrifice comparability with established evaluations; correction methods like DCR \citep{xu2025dcr} apply aggressive adjustments. Yet no study has directly measured the aggregate effect size under controlled conditions with uncertainty quantification. The absence of this measurement leaves the field unable to distinguish settings where contamination genuinely distorts rankings from those where it is detectable but practically harmless.
6	
7	Detection methods such as Min-K\%++ \citep{zhang_2024_minkpp}, ConStat \citep{dekoninck2024constat}, and Kernel Divergence Signatures \citep{choi_2025_kds} can flag contaminated items but stop at binary classification. They do not quantify how much scores are inflated or produce adjusted scores with uncertainty estimates. IRT-based evaluation frameworks \citep{polo_2024_tinybenchmarks,habba_2025_growing_pains} apply psychometric ability estimation to improve 
…[truncated 3287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 520 · 2026-05-18T04:44:12.849002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 521 · 2026-05-18T04:44:13.301150+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination detection and mitigation.}
5	Membership inference for contamination detection builds on the foundations of training data extraction \citep{carlini_2021_extracting}, membership inference attacks \citep{shokri_2017_mia}, and early contamination analyses \citep{magar_2022_contamination}. Current approaches include Min-K\% \citep{shi_2023_minkprob} and Min-K\%++ \citep{zhang_2024_minkpp} (token-level surprisal), ConStat \citep{dekoninck2024constat} (accuracy gaps on paraphrased items), CDD/TED \citep{dong_2024_cdd} (completion-based probes), KDS \citep{choi_2025_kds} (kernel divergence), TS-Guessing \citep{deng_2024_tsguessing} (temporal splits), and Time Travel \citep{golchin_2024_time_travel} (guided generation probes). Concurrent with our work, \citet{tao2025detecting} propose an entropy collapse method for RL-trained models. \citet{kocyigit2025impact} show that post-training procedures (RLHF, DPO) degrade detection signal reliability; token-level methods become unreliable on instruction-tuned models. \citet{zhang_2024_gsm1k} construct GSM1K as a parallel test set to quantify GSM8K contamination: performance gaps between original and regenerated items serve as a natural experiment for contamination measurement. Recent surveys \citep{chen2025benchmarking,singh2024evaluation} systematically categorize these approaches. These methods flag contamination but do not produce adjusted scores. On the mitigation side, \citet{sun2025emperor} systematically evaluate twenty approaches and find that none reliably restores clean performance; inference-time decontamination \citep{yang2024inference} and decontamination via forgetting \citep{zhang2025forget} similarly show limited effectiveness. DCR \citep{xu2025dcr} estimates decontaminated scores via fuzzy inference but produces point estimates without uncertainty quantification or domain-level diagnosis. ContamCal consumes detection signals as inputs 
…[truncated 3302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 522 · 2026-05-18T04:44:13.301633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 523 · 2026-05-18T04:44:13.754200+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt}. We adapt these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Shared item pool.} A fixed item set is shared across all models and introduces residual correlations beyond scalar $\theta_j$ \citep{sanmartin_2009_irt}; we mitigate by fitting per-benchmark models.
14	\textit{Continuous exposure.} We replace binary leakage indicators with continuous scores $e_{ij} \in [0,1]$ derived from detection signals, as LLM contamination is graded rather than binary.
15	\textit{Counterfactual ability.} Training regime changes (SFT vs.\ RL) alter both representations and signal reliability; we recover clean ability via counterfactual inference (setting $e_{ij}=0$) rather than regime-specific parameters.
16	
17	\subsection{Stage 1: Multi-Signal Exposure Mapping}
18	
…[truncated 5870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 524 · 2026-05-18T04:44:13.754798+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 525 · 2026-05-18T04:44:14.207015+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed using Qwen2.5 \citep{qwen2024qwen25} at three scales (0.5B, 1.5B, 3B parameters). For each scale, we fine-tune with Low-Rank Adaptation \citep[LoRA;][]{hu2022lora} ($\alpha=32$, $r=16$, lr$=5\times10^{-5}$) on a general-purpose SFT corpus into which benchmark items are injected at four dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), and d100 (100\%). Injected items are formatted as instruction-response pairs and pass a quality-control filter that removes ambiguous or malformed entries.
8	
9	Each configuration is trained with two random seeds (s42, s123) for a total of 24 models across $3 \times 4 \times 2$ conditions. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.
10	
11	We exclude 0.5B models from MMLU and ARC IRT due to answer-position bias that correlates with dosage (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}). Three initial 3B checkpoints trained with inconsistent LoRA hyperparameters were retrained under the unified protocol ($\alpha=32$, lr$=5\times10^{-5}$; Appendix~\ref{sec:exclusion_details}). Our pooled calibration analysis (Table~\ref{tab:baselines}) uses $J=16$ respondents for MMLU/ARC (1.5B$\times$8 + 3B$\times$8) and $J=24$ for GSM8K (all scales retained). Domain-level $\gamma$ analysis (Table~\ref{tab:domain_gamma}, \S\ref{sec:domain_differential}) uses $J=13$ (1.5B$\times$8 + 3B$\times$5), as it preceded completion of the 3B retraining. The eight 1.5B d000 models serve as the clean reference anchor in both configurations.
12	
13	\subsection{Cross-Family Analysis}
14	\label{sec:cross_family}
15	
16	To test whether IRT calibration is robust to inclusion of new model families, we fine-tune Llama-3.2-3B \citep{grattafio
…[truncated 2412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 526 · 2026-05-18T04:44:14.207564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 527 · 2026-05-18T04:44:15.212073+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Calibration Quality}
5	\label{sec:calibration_results}
6	
7	\paragraph{Item filtering improves calibration.}
8	RRF-guided item filtering substantially improves IRT calibration quality over random item subsets. On a random 2000-item MMLU subset (same $J=13$ model set), vanilla 2PL achieves $\tau = 0.46$; on the 300-item RRF-selected subset, $\tau = 0.73$ ($\Delta\tau = 0.27$, controlled for model composition). Signal-guided filtering concentrates items where contamination effects are detectable, and enables sharper ability-dosage separation. Exclusion sensitivity analysis (removing 0--50\% of top-exposure items from random 2000-item subsets, $J=13$) yields $\tau$ ranging from 0.46 to 0.60 with no monotonic trend, and $\gamma$ remains non-significant at all exclusion rates. The $\tau$ improvement is not driven by item discrimination: mean $a_i$ does not differ between RRF-selected and random subsets (Cohen's $d = 0.098$, $p > 0.05$; $r_{\text{exposure}, a_i} = -0.013$).
9	
10	\paragraph{RRF vs.\ single-signal ablation.}
11	S1-only item selection causes IRT convergence failure ($\hat{R} = 1.53$, ESS$=$7) due to exposure variance compression: top-300 S1 items concentrate in a narrow score band, which creates collinearity between $\gamma \cdot e_{ij}$ and difficulty parameters. Multi-signal RRF fusion preserves broader exposure distributions necessary for $\gamma$ identifiability. Random 300-item subsets ($J=16$, 5 seeds) yield $\tau = 0.554 \pm 0.048$, which confirms that RRF's advantage ($\tau = 0.731$, $\Delta\tau = 0.177$) reflects informative item selection, not subset size.
12	
13	\paragraph{Aggregate contamination effects are negligible.}
14	Table~\ref{tab:baselines} compares calibration on 300 RRF-filtered items ($J=16$). Raw accuracy achieves the lowest MAE (MMLU 0.006) and outperforms all correction methods including vanilla 2PL and ContamCal. This occurs because SFT-injected contamination shifts aggreg
…[truncated 13418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 528 · 2026-05-18T04:44:15.212562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 529 · 2026-05-18T04:44:15.664601+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We investigated whether IRT can separate ability from contamination artifacts on LLM benchmarks. Three results emerge: (1)~under SFT injection at $\leq$3B, aggregate contamination effects are negligible (${\sim}$0.6--0.7pp), so raw accuracy is already well-calibrated and no correction method improves upon it; (2)~Min-K\%++ exhibits directional reversal at small scales; (3)~domain-level $\gamma$ is exploratory at $J=13$ and requires $J \geq 50$ for confirmation.
4	
5	\paragraph{Diagnostic value beyond aggregate calibration.}
6	Under SFT injection at $\leq$3B, raw accuracy is the best aggregate estimator because the contamination effect is near zero (${\sim}$0.6--0.7pp). The IRT framework's value lies in \textit{explaining why} rather than improving MAE: $\gamma$ quantifies that the effect is too small to distort rankings, provides a contamination existence diagnostic at domain granularity (Social Sciences posterior $P(\gamma<0) = 99.1\%$, robust to prior specification; Appendix~\ref{sec:prior_sensitivity}), and reveals heterogeneity invisible to aggregate scoring. The framework applies directly to settings with larger effects (e.g., pretraining-phase exposure) with no methodological changes. B6-DCR's systematic overcorrection (MAE 0.108) demonstrates the practical risk of correction methods that assume large effects without measurement-theoretic grounding.
7	
8	\paragraph{Circularity.}
9	Filtering items by exposure signal and then fitting IRT is not circular: $\tau$ measures $\theta$-dosage rank correlation, not $\gamma$ significance, and the oracle ablation confirms that even perfect binary labels do not produce a significant pooled $\gamma$.
10	
11	\paragraph{Implications and future work.}
12	Min-K\%++ should not be trusted at the 0.5B scale under SFT injection. The negligible aggregate effect under SFT injection does not preclude larger effects under pretraining contamination \citep{schaeffer2026caus
…[truncated 246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 530 · 2026-05-18T04:44:15.665033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 531 · 2026-05-18T04:44:16.117256+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify nine limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 3B parameters. Larger models (7B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Signal coverage.}
10	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\S\ref{sec:signal_failure}).
11	
12	\paragraph{Ensemble size and per-domain power.}
13	Reliable $\gamma$ recovery requires $J \geq 50$. Our domain-level analysis ($J = 13$) yields a strong directional signal (posterior $P(\gamma<0) > 99\%$) for only one of eight MMLU domains. Per-domain $\gamma$ diagnosis at current ensemble sizes is exploratory.
14	
15	\paragraph{Position bias.}
16	Qwen2.5-0.5B exhibits position bias correlated with dosage (A-option rate: 46\% at d000 to 98\% at d100); these models are excluded from MC IRT analyses, which reduces ensemble size.
17	
18	\paragraph{Credible interval coverage.}
19	CI coverage is benchmark-dependent (\S\ref{sec:calibration_results}), computed on 18 checkpoints for MMLU and 20 for ARC. The model does not provide uniformly calibrated uncertainty across benchmarks.
20	
21	\paragraph{Model misfit in non-STEM domains.}
22	A single linear $\gamma$ cannot capture non-monotone contamination effects within a domain. Richer specifications may be required.
23	
24	\paragraph{SFT ecological validity.}
25	We use LoRA-based SFT injection exclusively. Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures: distributed exposure across many training steps rather than concentrated fine-tuning. The position bias observed at 0.5B (A-option rate escalating from 46
…[truncated 1099 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 532 · 2026-05-18T04:44:16.118037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 533 · 2026-05-18T04:44:16.419416+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5 and Llama-3.2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	
5	We acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our finding that SFT injection at $\leq$3B produces negligible aggregate effects may itself reduce the incentive for such manipulation at small scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-18T04:44:16.419884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-18T04:44:16.470670+00:00_

1	\appendix
2	
3	\section{4PL Extension}
4	\label{sec:4pl_details}
5	
6	For MC-format benchmarks where guessing and ceiling effects are non-negligible, we extend to:
7	\begin{equation}
8	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\bigr),
9	\end{equation}
10	with $c_i \sim \text{Beta}(5,20)$ and $d_i \sim \text{Beta}(20,5)$. This requires $J \geq 16$ to avoid overparameterization; at $J=5$, 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068. Our domain-level analyses use 2PL+$\gamma$ at $J=13$; pooled calibration uses $J=16$.
11	
12	\section{Model Exclusion Details}
13	\label{sec:exclusion_details}
14	
15	Of the 16 models remaining after 0.5B exclusion, three 3B checkpoints were removed: two had mismatched naming conventions between evaluation and signal extraction stages, and one lacked evaluation results under the unified hyperparameter setting ($\alpha=32$). Additionally, 3B d000 (clean control) checkpoints were excluded because the standardized protocol (LoRA $\alpha=32$, lr$=5\times10^{-5}$) was applied only to dosages d005--d100 at the 3B scale; earlier d000 checkpoints used inconsistent hyperparameters across retraining iterations.
16	
17	\paragraph{Model sets across analyses.}
18	Table~\ref{tab:model_sets} summarizes model compositions. Model sets vary because domain-level runs preceded the 3B retraining (\S\ref{sec:injection}). Core findings ($\gamma$ non-significance, raw accuracy dominance) replicate across $J=13$ and $J=16$ configurations.
19	
20	\begin{table}[h]
21	\centering
22	\caption{Model set composition across analyses.}
23	\label{tab:model_sets}
24	\footnotesize
25	\begin{tabular}{lcll}
26	\toprule
27	Analysis & $J$ & Model Set & Section \\
28	\midrule
29	Pooled baselines & 16 & 8$\times$Qwen-1.5B + 8$\times$Qwen-3B & \S\ref{sec:calibration_results} \\
30	Domain $\gamma$ & 13 & 8$\times$Qwen-1.5B + 5$\times$Qwen-3B & \S\ref{sec:domain_differential} \\
31	Cross-family & 16--
…[truncated 9865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 536 · 2026-05-18T04:44:36.303737+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "paper_checklist.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-18T04:44:37.459100+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'contamcal-irt-calibration'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-18T04:44:37.459502+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-18T04:44:37.911632+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-18T04:44:37.962278+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-18T04:44:38.063183+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 542 · 2026-05-18T04:44:40.827078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool call

_source line 543 · 2026-05-18T04:44:40.927917+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 544 · 2026-05-18T04:44:40.979124+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{carlini_2021_extracting,
6	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
7	  title     = {Extracting Training Data from Large Language Models},
8	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
9	  year      = {2021},
10	  url       = {https://arxiv.org/abs/2012.07805}
11	}
12	
13	@inproceedings{choi_2025_kds,
14	  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},
15	  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},
16	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
17	  year      = {2025},
18	  url       = {https://arxiv.org/abs/2502.00678}
19	}
20	
21	@inproceedings{cormack_2009_rrf,
22	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
23	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
24	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
25	  pages     = {758--759},
26	  year      = {2009},
27	  publisher = {ACM},
28	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
29	}
30	
31	@book{deboeck_2004_explanatory_irt,
32	  author    = {De Boeck, Paul and Wilson, Mark},
33	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
34	  publisher = {Springer},
35	  year      = {2004},
36	  address   = {New York},
37	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
…[truncated 23627 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 545 · 2026-05-18T04:44:41.331282+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices"
3	  category: framing
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 2
7	  last_seen_round: 5
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
12	    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?') but framing still inconsistent. Intro ¶1-3 heavily motivate calibration, Results show calibration unnecessary. Contributions 1-3 span empirical finding / engineering observation / exploratory analysis without unified main line. 'Why not just use raw accuracy?' paragraph in Conclusion reads as arguing against paper's own existence. Both AGREE: need full empirical investigation framing from ¶1, ContamCal as investigative instrument not product."}
13	  action_items:
14	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
15	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
16	    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assigned_to: "paper_agent", status: "done"}
17	    - {round: 5, action: "Rewrite Introduction from ¶1 as question-driven empirical investigation; ContamCal as tool not contribution; consolida
…[truncated 27253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-18T04:45:06.779239+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-18T04:45:07.281902+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/decisions.yaml\", \"content\": \"_next_id: 139\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:26 UTC\\n  summary: MVP 用 simulation identifiability test 验证 4PL+γ IRT 核心假设，放弃 EMNLP 2026 May\\n    ARR\\n  rationale: 核心假设是 γ 与 θ 可分离——这在合成数据上可验证，无需 GPU。12 天内完成完整论文不现实，目标改为 AAAI 2027 / ICLR\\n    2027。MVP 通过后再配置 GPU 进入 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:29 UTC\\n  summary: 采纳 Reviewer 3 个 warning：扩展 simulation grid + 加 θ-exposure confounding +\\n    加 FPR/FNR 噪声模型\\n  rationale: Reviewer 指出原 MVP simulation 条件过于理想化。θ-exposure confounding 是 γ identifiability\\n    的核心威胁，必须在 MVP 阶段覆盖。参数 grid 扩展（18 conditions）和 FPR/FNR 噪声增量成本约 4-8h CPU，不影响时间线。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 10:57 UTC\\n  summary: Phase A PASS：4PL+γ 在 N_items=300 下成功分离 γ 和 θ；θ_RMSE 阈值从 0.2 放宽至 0.30\\n  rationale: 'Variant A (N_items=300, 4PL NUTS): γ_rel_bias=6.8%, θ_corr=0.943, 收敛完美。N_items=100\\n    的 borderline fail 确认为信息量不足（c/d 参数估计需要更多 items），非方法论缺陷。θ_RMSE 阈值从 0.2 放宽至 0.30，Reviewer\\n    论证理论最优 SE≈0.18-0.26，0.2 在 N=50 models 下不可达。ADVI 在 4PL 上彻底失败（bad local mode），MVP\\n    阶段放弃 ADVI，仅用 NUTS。2PL+γ 在 4PL 生成数据上严重 misspecified（γ=0.16），确认 4PL 的必要性。'\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: primary\\n    result: Phase A PASS (Variant A)\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 15:45 UTC\\n  summary: MVP 通过，进入 Research 阶段\\n  rationale: Phase A (identifiability) 和 P2 (confounding robustness) 两个 gate 全部 PASS。4PL+γ\\n    NUTS 在 N_items=300 条件下 γ 相对偏差 <8%，θ 相关性 >0.94，混淆分离后残差相关 0.058。ADVI 和 2PL 被排除。核心假设\\\"IRT\\n    模型可分离污染效应与真实能力\\\"在合成数据上得到验证。\\n  related_experiments:\\n  - exp_id: mvp_sim_4pl_gamma\\n    role: Phase A identifiability\\n    result: PASS at N_items=300\\n  - exp_id: mvp_sim_confounding\
…[truncated 1462 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-18T04:45:08.136094+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-18T04:45:08.188930+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 550 · 2026-05-18T04:45:13.727848+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 551 · 2026-05-18T04:45:13.778552+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 552 · 2026-05-18T04:45:16.992700+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent"
  }
}
```

</details>

---


### Tool result

_source line 553 · 2026-05-18T04:45:17.093804+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/review_director_c2ad40d8.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 554 · 2026-05-18T04:46:02.590030+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **标题**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **References**: `projects/contamcal-irt-calibration/docs/paper/references.bib`\n\n### Venue 要求（EMNLP 2026 via ARR May cycle）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper ≤8 pages content + unlimited references; Limitations section required (不计页数); Ethics statement optional (不计页数)\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **格式**: A4, 11pt\n- **评分标准**: 5=Award (~top 2.5%), 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **IRT 建模合理性**:\n   - 2PL+γ 模型的 additive linear γ 假设是否合理？oracle ablation 结论是否站得住脚？\n   - 独立 per-domain fitting vs hierarchical model 的选择是否有充分论证？\n   - Bayesian inference 设置（priors, convergence criteria, chain数）是否规范？\n   - PPP 作为 model fit 指标在不同 benchmark 上的表现差异（MMLU acceptable vs ARC marginal）是否有充分解释？\n\n2. **统计分析**:\n   - J=13/16 ensemble size 下的 γ 结论的 statistical power 是否充分？\n   - Social Sciences P(γ<0)=99.1% 的 multiplicity correction 处理是否妥当？\n   - Prior sensitivity analysis 的覆盖面和结论是否合理？\n   - CI coverage analysis（MMLU over-coverage, ARC under-coverage）的 root cause 分析\n\n3. **实验设计**:\n   - Controlled SFT injection 的 ecological validity（vs pretraining contamination）\n   - 0.5B exclusion 的合理性和影响\n   - Cross-family analysis（Llama J=4, single seed）的 power 和结论边界\n   - Model set inconsistency（J=13 vs J=16 across analyses）的影响\n   - RRF filtering（300 items from 14042）的 item selection bias\n\n4. **Identifiability analysis**:\n   - Simulation study 设计（20 conditions, 10 seeds, 200 runs）是否充分？\n   - J≥50 threshold 的实际可行性讨论\n   - Fisher information argument 的严谨性\n\n5. **Calibration claims**:\n   - \"Raw accuracy is already well-calibrated\" 的 claim scope（仅 SFT injection at ≤3B）\n   - MAE 比较中 raw accuracy 优于所有 correction methods 的解释力\n   - 0.6-0.7pp aggregate effect 作为 \"model-free observation\" 的定性\n\n请给出：Summary、Strengths（逐条）、Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）、Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### 论文信息\n- **标题**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **References**: `projects/contamcal-irt-calibration/docs/paper/references.bib`\n\n### Venue 要求（EMNLP 2026 via ARR May cycle）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper ≤8 pages content + unlimited references; Limitations section required (不计页数); Ethics statement optional (不计页数)\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **格式**: A4, 11pt\n- **评分标准**: 5=Award (~top 2.5%), 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **IRT 建模合理性**:\n   - 2PL+γ 模型的 additive linear γ 假设是否合理？oracle ablation 结论是否站得住脚？\n   - 独立 per-domain fitting vs hierarchical model 的选择是否有充分论证？\n   - Bayesian inference 设置（priors, convergence criteria, chain数）是否规范？\n   - PPP 作为 model fit 指标在不同 benchmark 上的表现差异（MMLU acceptable vs ARC marginal）是否有充分解释？\n\n2. **统计分析**:\n   - J=13/16 ensemble size 下的 γ 结论的 statistical power 是否充分？\n   - Social Sciences P(γ<0)=99.1% 的 multiplicity correction 处理是否妥当？\n   - Prior sensitivity analysis 的覆盖面和结论是否合理？\n   - CI coverage analysis（MMLU over-coverage, ARC under-coverage）的 root cause 分析\n\n3. **实验设计**:\n   - Controlled SFT injection 的 ecological validity（vs pretraining contamination）\n   - 0.5B exclusion 的合理性和影响\n   - Cross-family analysis（Llama J=4, single seed）的 power 和结论边界\n   - Model set inconsistency（J=13 vs J=16 across analyses）的影响\n   - RRF filtering（300 items from 14042）的 item selection bias\n\n4. **Identifiability analysis**:\n   - Simulation study 设计（20 conditions, 10 seeds, 200 runs）是否充分？\n   - J≥50 threshold 的实际可行性讨论\n   - Fisher information argument 的严谨性\n\n5. **Calibration claims**:\n   - \"Raw accuracy is already well-calibrated\" 的 claim scope（仅 SFT injection at ≤3B）\n   - MAE 比较中 raw accuracy 优于所有 correction methods 的解释力\n   - 0.6-0.7pp aggregate effect 作为 \"model-free observation\" 的定性\n\n请给出：Summary、Strengths（逐条）、Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）、Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 555 · 2026-05-18T04:46:22.130531+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19540
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-18T04:46:22.331783+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### 论文信息\n- **标题**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **References**: `projects/contamcal-irt-calibration/docs/paper/references.bib`\n\n### Venue 要求（EMNLP 2026 via ARR May cycle）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper ≤8 pages content + unlimited references; Limitations section required (不计页数); Ethics statement optional (不计页数)\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **格式**: A4, 11pt\n- **评分标准**: 5=Award (~top 2.5%), 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **新颖性 / Contribution positioning**:\n   - 2PL+γ 实质是标准 explanatory IRT/DIF 的 application — technical novelty 是否充分？\n   - 核心贡献是 empirical null finding（0.6-0.7pp）— 这对 EMNLP 2026 是否足够新颖？\n   - 与 Han et al. (EACL 2026) 的差异化是否充分？（binary DIF vs continuous RRF exposure）\n   - RRF fusion 的贡献（exposure variance vs signal quality）定位是否精确？\n\n2. **Framing 一致性**:\n   - Title（问题形式）→ Abstract → Introduction → Method → Results → Conclusion 是否主线统一？\n   - \"Question-driven empirical investigation\" framing 是否贯彻？是否残存 \"method paper\" 痕迹？\n   - Contributions list（2 items + 1 observation）是否与实验结果一一对应？\n   - \"Diagnostic value\" narrative（γ 的存在意义）是否有充分支撑？\n\n3. **Related Work 覆盖与 positioning**:\n   - 引用是否覆盖 direct competitors、baselines、benchmarks、theoretical foundations？\n   - IRT 经典文献（Lord 1980, Hambleton 1991）是否被适当引用？\n   - 近期 concurrent work 覆盖（Han et al. 2026, Schaeffer et al. 2026, Tao et al. 2025）\n   - ~52 references 是否足够？密度是否合适？\n\n4. **写作质量**:\n   - AI 写作痕迹检查：em-dash/en-dash 使用、-ing phrases、过度分段\n   - 术语一致性：k 索引重载（benchmark vs domain/stratum）\n   - Abstract 信息密度（word count, numeric density）\n   - 全文叙事节奏和段落长度\n\n5. **格式合规**:\n   - 页数是否 ≤8 pages（主体内容，不含 Limitations/Ethics/References/Appendix）\n   - Limitations section 是否存在且位置正确（Conclusion 之后、References 之前）\n   - 匿名化检查（无作者姓名、无自引暴露身份的表述）\n   - 图表 caption 自包含性、数值精度一致性\n\n请给出：Summary、Strengths（逐条）、Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）、Detailed Comments。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### 论文信息\n- **标题**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n- **论文路径**: `projects/contamcal-irt-calibration/docs/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experimental_setup.tex, results.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex）\n- **References**: `projects/contamcal-irt-calibration/docs/paper/references.bib`\n\n### Venue 要求（EMNLP 2026 via ARR May cycle）\n- **Deadline**: 2026-05-25\n- **页数限制**: Long paper ≤8 pages content + unlimited references; Limitations section required (不计页数); Ethics statement optional (不计页数)\n- **模板**: ACL template with `[review]` option\n- **匿名**: Double-blind\n- **格式**: A4, 11pt\n- **评分标准**: 5=Award (~top 2.5%), 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n请重点审查以下方面：\n\n1. **新颖性 / Contribution positioning**:\n   - 2PL+γ 实质是标准 explanatory IRT/DIF 的 application — technical novelty 是否充分？\n   - 核心贡献是 empirical null finding（0.6-0.7pp）— 这对 EMNLP 2026 是否足够新颖？\n   - 与 Han et al. (EACL 2026) 的差异化是否充分？（binary DIF vs continuous RRF exposure）\n   - RRF fusion 的贡献（exposure variance vs signal quality）定位是否精确？\n\n2. **Framing 一致性**:\n   - Title（问题形式）→ Abstract → Introduction → Method → Results → Conclusion 是否主线统一？\n   - \"Question-driven empirical investigation\" framing 是否贯彻？是否残存 \"method paper\" 痕迹？\n   - Contributions list（2 items + 1 observation）是否与实验结果一一对应？\n   - \"Diagnostic value\" narrative（γ 的存在意义）是否有充分支撑？\n\n3. **Related Work 覆盖与 positioning**:\n   - 引用是否覆盖 direct competitors、baselines、benchmarks、theoretical foundations？\n   - IRT 经典文献（Lord 1980, Hambleton 1991）是否被适当引用？\n   - 近期 concurrent work 覆盖（Han et al. 2026, Schaeffer et al. 2026, Tao et al. 2025）\n   - ~52 references 是否足够？密度是否合适？\n\n4. **写作质量**:\n   - AI 写作痕迹检查：em-dash/en-dash 使用、-ing phrases、过度分段\n   - 术语一致性：k 索引重载（benchmark vs domain/stratum）\n   - Abstract 信息密度（word count, numeric density）\n   - 全文叙事节奏和段落长度\n\n5. **格式合规**:\n   - 页数是否 ≤8 pages（主体内容，不含 Limitations/Ethics/References/Appendix）\n   - Limitations section 是否存在且位置正确（Conclusion 之后、References 之前）\n   - 匿名化检查（无作者姓名、无自引暴露身份的表述）\n   - 图表 caption 自包含性、数值精度一致性\n\n请给出：Summary、Strengths（逐条）、Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、Overall Assessment（含评分和置信度）、Detailed Comments。"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-18T04:46:23.794700+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1462
}
```

</details>

---


### Assistant

_source line 558 · 2026-05-18T04:46:33.485537+00:00_

Round 1 任务已分配给两名 Reviewer。

- **Reviewer 1**: 方法严谨性 + 实验设计（IRT 建模、统计分析、identifiability、实验控制）
- **Reviewer 2**: 新颖性 + 完整性 + 写作质量（contribution positioning、framing 一致性、Related Work、格式）

等待两位 Reviewer 返回初审意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 559 · 2026-05-18T04:52:05.660174+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 — Round 1 Review

**Paper**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## 总体评分
**Overall**: 3/5 (Findings)
**一句话总结**: 在严格控制条件下的诚实 null finding，实验设计和不确定性量化值得肯定，但技术新颖性有限且实验范围过窄（仅 SFT、≤3B），核心结论的可推广性不足以支撑主会议接收。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论正确（标准 IRT/DIF 应用），控制实验设计好，但 oracle ablation 暴露的模型规格问题未解决，k 索引重载造成符号混乱 |
| Excitement | 2.5/5 | Null finding 有信息量但范围太窄（SFT ≤3B），对 practitioner 最关心的 pretraining contamination 无法回答；diagnostic value 仅 1/8 domain 显著 |
| Reproducibility | 4/5 | 实验配置清晰（LoRA 超参、Stan/NUTS 推断、种子数），但 RRF 实现细节和 quality-control filter 的具体规则未充分说明 |
| Confidence | 4/5 | 对 IRT 和 LLM 评估均有了解 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 技术新颖性不足：2PL+γ 是标准 explanatory IRT/DIF 的直接应用
- 具体位置：Section 3.3 Eq.(2), Section 2 Related Work para 3
- 问题：论文在 Related Work (Section 2, para 3) 中已明确承认 γ 参数"is formally an instance of explanatory DIF (Holland 1993, Thissen 1993)"，并引用 De Boeck & Wilson (2004) 的 explanatory IRT 传统。论文声称的三项改编（continuous exposure、domain-level stratification、counterfactual inference via posterior expectation）分别是：(a) 将 binary group indicator 换成 continuous covariate——这在 DIF 文献中是标准做法（logistic regression DIF, Zumbo 1999 已被引用）；(b) 按 domain 分层拟合独立 IRT 模型——这是 subgroup analysis，不是方法创新；(c) 设 e_{ij}=0 计算后验期望——这是任何含 covariate 模型的标准 counterfactual inference。RRF fusion (Eq.1) 是信息检索中的标准技术 (Cormack et al., 2009)，应用于信号聚合虽合理但不构成方法贡献。总体来看，ContamCal 是现有工具的组合应用而非方法创新。
- 为什么影响接收：对于 EMNLP 主会议，需要 sufficient technical or empirical contribution。如果定位为 empirical study，则 null finding 的范围必须足够广才能有 community-level impact（见 N2）。
- 建议修改方向：(a) 更明确地将论文定位为 empirical study with a measurement framework，弱化 method novelty claim；(b) 在 Contribution 1 中突出 identifiability analysis（J≥50 threshold）作为独立贡献，因为这对整个 IRT-for-LLM 社区有实际指导价值，目前这部分埋在贡献描述的第二句。

**N2** [critical] Null finding 的范围过窄，削弱了标题所暗示的一般性结论
- 具体位置：Title, Abstract, Section 5.1 para 3, Section 6 para 1, Limitations para 1 & 7
- 问题：标题 "Does LLM Benchmark Contamination Need Calibration?" 隐含一个关于 benchmark contamination 的一般性问题，但实验仅覆盖 SFT injection at ≤3B (Qwen2.5 + exploratory Llama-3.2-3B)。论文自身在 Limitations (para 7, "SFT ecological validity") 和 Conclusion (para 3) 中承认 pretraining-stage leakage "may produce qualitatively different contamination signatures" 并引用 Schaeffer et al. (2026)。这意味着论文回答的实际问题是 "Does SFT-injected contamination at ≤3B need calibration?"，答案为 "no" 并不令人惊讶——SFT injection 是一种粗糙的模拟，在小模型上产生的效果本身就可能很弱。核心 0.6-0.7pp 的 null finding 对 practitioner 最关心的场景（pretraining contamination in 7B+ models）没有直接适用性。
- 为什么影响接收：如果 null finding 无法推广到 pretraining contamination，其 community impact 显著降低。审稿人 guideline (ARR H6) 提醒不应因 negative result 本身而拒稿，但 negative result 的价值取决于它排除了多大的假设空间——本文排除的空间较小。
- 建议修改方向：(a) 将标题和 abstract 中的 claim 显式限定为 SFT injection at ≤3B；(b) 增加至少一个 7B+ 模型的 pilot experiment（即使是 exploratory），以扩展 null finding 的可信范围；(c) 或者更深入地论证 SFT injection 作为 contamination proxy 的生态效度——当前 Limitations 中的讨论承认了问题但未提供任何支撑证据。

**N3** [critical] Oracle ablation 暴露根本性模型规格问题，论文未充分正视
- 具体位置：Section 5.1 para 5 ("Oracle ablation"), Limitations para 9 ("Additive γ linearity")
- 问题：即使使用 ground-truth binary labels (AUC=1.0)，pooled γ 仍然 non-significant（MMLU γ = -0.012, CI [-0.145, 0.119]）。论文提出两种解释：(a) 效应异质性（正负方向相互抵消）；(b) 线性 γ 误设（contamination 可能是 threshold-like behavior）。这两种解释的含义截然不同：如果是 (a)，domain-level 分析应该能捕捉到（但仅 1/8 显著）；如果是 (b)，整个 2PL+γ 框架的有效性受到质疑。论文将此作为 "confirms that filtering is not circular" 来讨论，但更核心的问题是：如果模型在 oracle 条件下都无法检测效应，那么用 imperfect RRF scores 的 ContamCal 在何种意义上是有用的？
- 为什么影响接收：这直接关系到论文核心框架的 validity。如果 2PL+γ 的 additive structure 本身不适合 capture contamination effects，那么 "γ provides diagnostic value" 的 claim 就缺乏基础。
- 建议修改方向：(a) 对两种解释进行 formal 区分（例如在 simulation 中测试 threshold model 下 linear γ 的 recovery behavior）；(b) 如果无法区分，需要在正文（而非仅在 Limitations 末段）明确 acknowledge 这是一个 open question，并相应弱化 diagnostic value 的 claim。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 与 Han et al. (EACL 2026) 的差异化不够充分
- 具体位置：Section 2 para 2, Introduction para 3
- 问题：论文列出三点差异（continuous vs binary indicators, calibration vs detection focus, controlled vs natural contamination），但：(a) continuous covariate DIF 是 DIF 文献的自然延伸，不是根本性区别；(b) "calibration" 在论文自身结果中被证明不如 raw accuracy——所以 calibration focus 作为差异化 claim 是 self-undermining 的；(c) controlled injection 是一个实验设计选择，不是方法差异。核心问题：如果 γ 不改善 calibration（Table 1 所示），那么 ContamCal 相对于 Han et al. 的 binary DIF 方法的实际优势在哪里？
- 建议：重新定位差异化：(a) 强调 identifiability analysis 和 simulation study（Han et al. 没有做这个）；(b) 强调 multi-signal fusion 的 variance preservation insight（对 IRT convergence 的必要性）。

**W2** [warning] Diagnostic value claim 证据不足
- 具体位置：Section 5.1 para 4, Section 5.4, Figure 3
- 问题："ContamCal's value lies in this decomposition" (Section 5.1 para 4) 的核心证据是 Social Sciences 的 γ = -0.57, P(γ<0) = 99.1%。但：(a) 这是 8 个 domain 中唯一的显著结果，且在 J=13 时 99.1% 未通过 Bonferroni 校正阈值 99.375%（论文在 Appendix Table 4 中报告 J=16 时 99.7% 才通过，但正文 Section 5.4 用的是 J=13 的 99.1%）；(b) 论文自身标注 "uncorrected for multiplicity" 且 "requires higher-powered replication"；(c) "negative direction is consistent with SFT injection on factual QA pairs disrupting contextual reasoning" 是 post-hoc 解释，无独立验证。如果主要证据需要 replication 才能确认，则 "diagnostic value" 目前只是一个 suggestive observation，不应作为核心贡献来呈现。
- 建议：将 diagnostic value 降级为 "suggestive finding" 而非 "value proposition"；或提供更强证据（如不同 seed 的 replicate、ablation on domain definition）。

**W3** [warning] Contribution 2 的定位与 framing 不一致
- 具体位置：Introduction, Contribution list item 2
- 问题：论文 framing 为 "question-driven empirical investigation"，但 Contribution 2 ("Signal-guided filtering and failure modes") 读起来像 method paper 的贡献。其中包含 RRF vs single-signal ablation、convergence failure diagnosis、Min-K%++ directional reversal——这些都是有价值的 empirical findings，但与 "Does contamination need calibration?" 的主线问题关系不够紧密。Min-K%++ reversal 尤其是一个独立的 finding，与 IRT calibration 没有逻辑依赖。
- 建议：(a) 将 Min-K%++ reversal 重新定位为 standalone finding，明确它对 detection pipeline 设计的 practical implication；(b) 将 "signal-guided filtering" 定位为 enabling condition for the main investigation，而非独立贡献。

**W4** [warning] k 索引重载造成符号混乱
- 具体位置：Section 3.1 (Eq. y_{ijk}, k = benchmark), Section 3.3 (Eq.2, k = stratum within benchmark)
- 问题：Section 3.1 定义 y_{ijk} 中 k 为 benchmark index，但 Section 3.3 (Eq.2) 中 k 变为 stratum/domain index，论文用括号注释 "here k indexes strata within a benchmark, not benchmarks themselves" 来处理。这在数学符号上是不规范的：同一论文中同一变量在相邻 section 改变含义，增加误读风险。
- 建议：为 stratum index 使用不同符号（如 d 或 s），保持 k 始终为 benchmark index。

**W5** [warning] J 值在不同分析间频繁切换，叙事连贯性受损
- 具体位置：Section 4.1 para 3, Section 5.1, Section 5.4, Appendix B Table 3
- 问题：论文使用 J=13（domain-level γ）、J=16（pooled baselines）、J=18/20/28（cross-family）、J=24（GSM8K）等多个 model set。虽然 Appendix B (Table 3) 做了汇总，但正文在 J 值之间频繁切换时缺乏足够的过渡说明。读者需要不断查表才能理解每个结论对应哪个 model set。特别是 Social Sciences 的 99.1% 结论在 J=13 下得出、在 J=16 下变为 99.7%，但正文 Section 5.4 第一段混合引用了两个 J 值的结果。
- 建议：在 Section 5 开头增加一段简要说明各分析使用的 model set 及其原因，减少读者的认知负担。

---

## 小问题（不影响接收）

- **M1**: Introduction line 17 使用 "Additionally" 开头——ARR guidelines 不会因此扣分，但建议替换为更自然的过渡。
- **M2**: Abstract 信息密度偏高，包含 ~170 words 但塞入了 6+ 个定量结论（0.6-0.7pp, Δτ=0.18/0.27, Cohen's d=-1.55/-1.98, J≥50, P(γ<0)=99.1%）。建议保留 2-3 个最关键的数字，其余移至正文。
- **M3**: Appendix Table 5 (Prior Sensitivity, J=16) 与正文 domain-level analysis (J=13) 使用不同 J 值但同为 Social Sciences 结果，容易混淆。Appendix 表头应更明确标注这是独立的 robustness check at J=16。
- **M4**: Section 3.2 中 S4 (Self-Critique) 定义为 "negative entropy of model self-evaluation distributions"，但仅引用 Kadavath et al. (2022) 作为 inspiration。Self-Critique 信号的具体计算方式（prompt 设计、evaluation distribution 如何构造）未给出足够细节以支持复现。
- **M5**: Appendix E (Table 6, ARC full baselines) 使用 J=8 且 S1-only exposure，与主分析 (J=16, RRF) 配置不同。这些结果的可比性有限，应在 caption 中更明确标注。
- **M6**: 格式检查——无法在未编译条件下精确确认页数是否 ≤8。正文内容（6 sections + 3 figures + 2 tables in-text）看起来接近上限，建议作者自查。匿名化无明显问题（author = Anonymous，未发现自引暴露）。Limitations section 位于 Conclusion 之后、References 之前，位置正确。

---

## Missing References（建议补充）

1. **Camilli & Shepard (1994)**, "Methods for Identifying Biased Test Items" — DIF 方法论的经典教材，与 Contribution 定位（explanatory DIF application）直接相关。
2. **Swaminathan & Rogers (1990)**, "Detecting Differential Item Functioning Using Logistic Regression Procedures" — logistic regression DIF with continuous covariates 的奠基文献，与本文 continuous exposure covariate 的 claim 直接对应。
3. **Roberts et al. (2025)** or similar work on IRT identifiability with small J — 论文在 simulation 中发现 J≥50 threshold，但缺少对 IRT 文献中 small-sample identifiability 问题的引用。

---

## 主要优势

- **S1**: 控制实验设计优秀。通过 SFT injection with controlled dosage levels (d000-d100)、two seeds、within-family design 系统隔离了 contamination 作为实验变量，这比自然 contamination 研究（无法确定 ground truth）更有说服力。
- **S2**: 诚实报告 null finding，不强行 overclaim。论文在发现 raw accuracy 优于所有校正方法后，没有试图隐藏或弱化这个结论，而是认真分析了 why。这种研究诚信在 contamination 文献中不常见。
- **S3**: Identifiability simulation study (Section 5.3, Figure 2) 对 IRT-for-LLM 社区有独立价值。J≥50 at AUC≥0.55 的 threshold 为未来研究设定了 practical minimum requirements，这是一个 actionable guideline。
- **S4**: Min-K%++ directional reversal (Section 5.2) 的文档化对 detection pipeline 设计者有直接实用价值。Cohen's d = -1.55 to -1.98 的效应量足以引起注意。
- **S5**: 写作质量整体良好。无 AI 写作痕迹（无 em-dash/en-dash、无 -ing trailing phrases、无 "leverage/utilize/delve" 等用词），术语使用精确，Limitations section 详尽（9 条，覆盖面广）。
- **S6**: Bayesian 推断方法正确（NUTS/Stan, 4 chains, Rhat < 1.01, ESS > 400, PPP diagnostics），prior sensitivity analysis 增加了结论的 robustness。

---

## Questions to Authors

1. Oracle ablation 中 pooled γ non-significant：如果您在 simulation 中对 threshold-like contamination effects 拟合 linear γ，recovery behavior 如何？这能区分 "heterogeneity" 和 "misspecification" 两种解释吗？
2. 为什么不在 domain-level 也做 oracle ablation？如果 domain-level oracle γ 仍然 non-significant，那么 "opposing directions cancel out in pooled analysis" 的解释就不成立。如果 domain-level oracle γ 显著，则支持了 diagnostic value claim。
3. SFT injection 中 quality-control filter (Section 4.1) 的具体规则是什么？"removes ambiguous or malformed entries" 的标准是什么？filter 移除的 item 比例是多少？
4. 如何看待 SFT injection 的生态效度？是否有证据表明 SFT contamination 和 pretraining contamination 在 IRT parameter space 中产生类似的 perturbation pattern？

---

## 总结

本文是一篇执行良好的 empirical study，在控制条件下系统测量了 benchmark contamination 的 aggregate effect size，并得出了一个 calibrated null finding。实验设计、Bayesian 推断和 limitation disclosure 都达到了高标准。主要问题在于：(1) 技术新颖性有限（标准 IRT/DIF 应用），(2) 实验范围过窄（SFT ≤3B），使得 null finding 的 generalizability 和 community impact 受限，(3) oracle ablation 暴露的模型规格问题未被充分解决。建议投 Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 560 · 2026-05-18T04:52:16.394161+00:00_

Reviewer 2 审稿意见已收到。核心评分：3/5 (Findings)，3 个 critical issues（技术新颖性不足、null finding 范围过窄、oracle ablation 暴露模型规格问题）。

等待 Reviewer 1 审稿意见返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 53

## Round 53

2 recorded events


### User

_source line 561 · 2026-05-18T04:52:18.992438+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：

- **Overall 3/5 (Findings)**，Soundness 3.5，Excitement 2.5
- **3 个 Must-Fix**：(1) 2PL+γ 是标准 explanatory IRT/DIF 的直接应用，技术新颖性不足；(2) SFT ≤3B 的 null finding 范围太窄，无法回答标题所暗示的一般性问题；(3) Oracle ablation 中即使 perfect labels 也得不到显著 γ，暴露根本性模型规格问题未解决
- **5 个 Should-Fix**：Han et al. 差异化不足、diagnostic value 证据单薄（1/8 domain 显著且未过 Bonferroni）、Contribution 2 与 question-driven framing 不一致、k 索引重载、J 值频繁切换影响可读性
- **主要优势**：控制实验设计优秀、诚实 null finding、identifiability simulation 有独立社区价值、Min-K%++ reversal 文档化有实用价值、写作整洁无 AI 痕迹

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 562 · 2026-05-18T04:52:27.615704+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 54

## Round 54

6 recorded events


### User

_source line 563 · 2026-05-18T04:53:13.107742+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿完成

**论文**: "Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study"
**审查侧重**: 方法严谨性 + 实验设计

---

## 总体评分

**Overall**: 3.0 / 5（Findings 水准）
**Confidence**: 4 / 5
**一句话总结**: 研究问题重要且 null result 有价值，但 SFT injection 的生态效度、线性 γ 潜在误设定、以及 J=13 下的 domain-level 推断与论文自身 J≥50 标准的矛盾，构成方法论层面的显著 gap。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3 / 5 | 核心方法合理但 oracle ablation 暴露的 γ 误设定未解决；domain-level 结论的统计 power 不足；CI coverage 问题削弱了 uncertainty quantification 的贡献声明 |
| Excitement | 3.5 / 5 | 研究问题及时、null result 有社区价值、identifiability analysis 是有用的方法论贡献；但 scope 限于 SFT ≤3B 显著降低了对实际 contamination 问题的回答力度 |

---

## 主要优势

1. **研究问题定义精准**：直接量化 contamination 的 aggregate effect size，填补了"检测多、度量少"的文献空白。Introduction 的叙事线（从 effect size 缺失到 measurement model 构建）逻辑清晰。

2. **诚实的 null result**：发现 raw accuracy 在 SFT injection ≤3B 条件下已经 well-calibrated（~0.6-0.7pp shift），没有过度包装成方法优越性，反而质疑了现有 correction 方法（DCR MAE=0.108 的 overcorrection 案例尤其有说服力）。

3. **Identifiability analysis 提供了可操作的 boundary**：simulation study 建立了 J≥50 at AUC≥0.55 的操作阈值（Figure 2），posterior CI width 与 J^{-0.48} 的经验收敛率验证了理论预期。这为后续 IRT-based contamination 研究提供了 design guideline。

4. **Min-K%++ directional reversal 的发现**：0.5B 尺度下 Cohen's d = -1.55 to -1.98 的方向反转（Section 5.2）是重要的实践警示，有独立的社区价值。

5. **RRF 的 meta-circularity 论证**：用 rank-based fusion 避开 learned aggregator 需要 contamination labels 的循环问题（Section 3.2），设计合理且论证充分。

6. **Limitations 章节异常详尽**：列出 9 项限制，体现了作者的自我批判能力。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **Ecological validity：SFT injection 的 null result 不能回答标题提出的问题**

- 具体位置：Title、Abstract、Section 4.1、Section 6 para 1
- 问题：标题问 "Does LLM Benchmark Contamination Need Calibration?"，但全部实验仅涵盖 LoRA-based SFT injection at ≤3B。Pretraining-phase contamination 是实际场景中最常见的形式，论文自身承认 "pretraining-phase contamination, which may produce larger effects"。SFT injection 在机制上与 pretraining leakage 有本质差异。
- 为什么影响接收：论文的核心 claim（"raw accuracy is already well-calibrated"）的 scope 被标题/abstract 的 framing 大幅放大。Scope-claim gap 是主要问题。
- 建议：修改标题限定 scope；Abstract/Introduction 中前移 scope limitation。

**N2** [critical] **Oracle ablation 暴露的 γ 误设定未获充分解决**

- 具体位置：Section 5.1 "Oracle ablation"、Limitations para 9
- 问题：即使 AUC=1.0，pooled γ 仍 non-significant（γ=-0.012）。论文给出 effect heterogeneity 和 misspecification 两个解释，但未测试 non-linear specifications 来区分 "no effect" vs "wrong model"。
- 为什么影响接收：如果 functional form 错误，null result 可能是模型不够灵敏的 artifact，核心 claim 的可信度依赖于此区分。
- 建议：测试至少一个 non-linear γ specification（如 threshold model）。

**N3** [critical] **J=13 domain-level 结论与 J≥50 identifiability 标准的自我矛盾**

- 具体位置：Section 5.3 (J≥50)、Section 5.4 (J=13 domain γ)、Abstract、Contribution list
- 问题：论文建立了 J≥50 标准后以 J=13 进行 domain analysis，并在 Abstract/Introduction 中将 Social Sciences P(γ<0)=99.1% 作为 key finding 展示。虽标注 "exploratory"，但实际呈现权重与 caution 不匹配。
- 为什么影响接收：内部自洽性问题——不能同时声称 J≥50 是必要条件并以 J=13 的结果为核心贡献。
- 建议：(a) 主文改用 J=16 结果；(b) 降低 domain γ 在 Abstract/Introduction 的权重。

---

## Should-Fix 问题

**W1** [warning] Multiplicity correction 处理不一致（引用 Gelman 2012 但未实施其推荐的 hierarchical model）
**W2** [warning] Cross-family analysis (Llama J=4, single seed) 的结论边界不明确
**W3** [warning] ARC PPP=0.003 结果仍出现在主文中
**W4** [warning] CI coverage 异常（MMLU over-coverage 83%, ARC under-coverage 45%）未获充分诊断
**W5** [warning] RRF filtering 的 item selection bias（300/14042, 仅报告 τ 未报告 MAE 的 random 对照）
**W6** [warning] "Model-free observation" 的 confound（SFT data composition 变化 vs contamination effect 未分离）

---

## Questions to Authors

Q1: 是否测试过 non-linear γ specifications？
Q2: SFT training 是否收敛？Training curves 未报告。
Q3: Hierarchical model 是否可在 camera-ready 前实现？
Q4: S1 不可用时（无 corpus access），RRF 退化为 S2+S4 的 applicability 讨论不足。
Q5: Within-family GSM8K 的 PPP 在哪里？

---

## Missing References

- Xu et al. (2024) "Benchmarking Benchmark Leakage in Large Language Models" (arXiv 2404.18824)
- Li et al. (2024) "Task Contamination: Language Models May Not Be Few-Shot Anymore" (AAAI 2024)

---

审稿完毕，请 Director 审阅。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 564 · 2026-05-18T04:53:50.134526+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1** [critical] 技术新颖性不足：2PL+γ 是标准 explanatory IRT/DIF 的直接应用\n- 论文在 Related Work (Section 2, para 3) 中已承认 γ 参数 \"is formally an instance of explanatory DIF\"\n- 三项声称的改编（continuous exposure、domain-level stratification、counterfactual inference）均为标准做法\n- RRF fusion (Eq.1) 是 IR 标准技术\n- 建议：更明确定位为 empirical study；突出 identifiability analysis 作为独立贡献\n\n**R2-N2** [critical] Null finding 范围过窄（SFT ≤3B），标题暗示一般性结论\n- 论文回答的实际问题是 \"Does SFT-injected contamination at ≤3B need calibration?\"\n- SFT 是粗糙模拟，小模型上效果本身可能很弱\n- 对 practitioner 最关心的 pretraining contamination 无直接适用性\n- 建议：标题限定 scope；增加 7B+ pilot；或深入论证 SFT 作为 contamination proxy 的生态效度\n\n**R2-N3** [critical] Oracle ablation 暴露根本性模型规格问题\n- AUC=1.0 时 pooled γ 仍 non-significant\n- 两种解释（heterogeneity vs misspecification）含义截然不同\n- 如果模型在 oracle 条件下都无法检测效应，ContamCal 在何种意义上有用？\n- 建议：在 simulation 中测试 threshold model 下 linear γ 的 recovery behavior\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1** Han et al. (EACL 2026) 差异化不充分——calibration focus 作为差异化 claim 是 self-undermining 的\n**R2-W2** Diagnostic value claim 证据单薄——仅 1/8 domain 显著，未过 Bonferroni\n**R2-W3** Contribution 2（signal filtering + Min-K%++ reversal）与 question-driven framing 不一致\n**R2-W4** k 索引重载（benchmark → stratum）造成符号混乱\n**R2-W5** J 值频繁切换（13/16/18/20/24/28），叙事连贯性受损\n\n### Reviewer 2 的 Minor 问题\n\n- M1: \"Additionally\" 过渡词\n- M2: Abstract 数字密度偏高（~6+ 定量结论）\n- M3: Appendix Table 5 vs 正文 J 值不一致\n- M4: S4 (Self-Critique) 计算细节不足\n- M5: Appendix E (ARC, J=8, S1-only) 可比性有限\n- M6: 页数接近上限需自查\n\n### Reviewer 2 的 Missing References\n1. Camilli & Shepard (1994) — DIF 方法论经典\n2. Swaminathan & Rogers (1990) — logistic regression DIF with continuous covariates\n3. Roberts et al. (2025) or similar — IRT identifiability with small J\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT]，附理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1** [critical] 技术新颖性不足：2PL+γ 是标准 explanatory IRT/DIF 的直接应用\n- 论文在 Related Work (Section 2, para 3) 中已承认 γ 参数 \"is formally an instance of explanatory DIF\"\n- 三项声称的改编（continuous exposure、domain-level stratification、counterfactual inference）均为标准做法\n- RRF fusion (Eq.1) 是 IR 标准技术\n- 建议：更明确定位为 empirical study；突出 identifiability analysis 作为独立贡献\n\n**R2-N2** [critical] Null finding 范围过窄（SFT ≤3B），标题暗示一般性结论\n- 论文回答的实际问题是 \"Does SFT-injected contamination at ≤3B need calibration?\"\n- SFT 是粗糙模拟，小模型上效果本身可能很弱\n- 对 practitioner 最关心的 pretraining contamination 无直接适用性\n- 建议：标题限定 scope；增加 7B+ pilot；或深入论证 SFT 作为 contamination proxy 的生态效度\n\n**R2-N3** [critical] Oracle ablation 暴露根本性模型规格问题\n- AUC=1.0 时 pooled γ 仍 non-significant\n- 两种解释（heterogeneity vs misspecification）含义截然不同\n- 如果模型在 oracle 条件下都无法检测效应，ContamCal 在何种意义上有用？\n- 建议：在 simulation 中测试 threshold model 下 linear γ 的 recovery behavior\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1** Han et al. (EACL 2026) 差异化不充分——calibration focus 作为差异化 claim 是 self-undermining 的\n**R2-W2** Diagnostic value claim 证据单薄——仅 1/8 domain 显著，未过 Bonferroni\n**R2-W3** Contribution 2（signal filtering + Min-K%++ reversal）与 question-driven framing 不一致\n**R2-W4** k 索引重载（benchmark → stratum）造成符号混乱\n**R2-W5** J 值频繁切换（13/16/18/20/24/28），叙事连贯性受损\n\n### Reviewer 2 的 Minor 问题\n\n- M1: \"Additionally\" 过渡词\n- M2: Abstract 数字密度偏高（~6+ 定量结论）\n- M3: Appendix Table 5 vs 正文 J 值不一致\n- M4: S4 (Self-Critique) 计算细节不足\n- M5: Appendix E (ARC, J=8, S1-only) 可比性有限\n- M6: 页数接近上限需自查\n\n### Reviewer 2 的 Missing References\n1. Camilli & Shepard (1994) — DIF 方法论经典\n2. Swaminathan & Rogers (1990) — logistic regression DIF with continuous covariates\n3. Roberts et al. (2025) or similar — IRT identifiability with small J\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT]，附理由。"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-18T04:53:59.707133+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9572
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-18T04:53:59.858133+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "contamcal-irt-calibration",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Ecological validity：SFT injection 的 null result 不能回答标题提出的问题\n- 全部实验仅涵盖 LoRA-based SFT injection at ≤3B\n- Pretraining-phase contamination 是实际场景中最常见的形式，机制上与 SFT 有本质差异\n- 核心 claim \"raw accuracy is already well-calibrated\" 的 scope 被标题/abstract 的 framing 大幅放大\n- 建议：修改标题限定 scope；前移 scope limitation\n\n**R1-N2** [critical] Oracle ablation 暴露的 γ 误设定未获充分解决\n- AUC=1.0 时 pooled γ 仍 non-significant（γ=-0.012）\n- 两个解释（heterogeneity / misspecification）未通过 non-linear specification 测试来区分\n- 如果 functional form 错误，null result 可能是模型不够灵敏的 artifact\n- 建议：测试至少一个 non-linear γ specification\n\n**R1-N3** [critical] J=13 domain-level 结论与 J≥50 identifiability 标准的自我矛盾\n- 论文建立 J≥50 标准后以 J=13 进行 domain analysis\n- Social Sciences P(γ<0)=99.1% 在 Abstract/Introduction 中作为 key finding 展示\n- 虽标注 \"exploratory\"，但实际呈现权重与 caution 不匹配\n- 建议：主文改用 J=16 结果；降低 domain γ 在 Abstract/Introduction 的权重\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** Multiplicity correction：引用 Gelman 2012 但未实施其推荐的 hierarchical model\n**R1-W2** Cross-family analysis (Llama J=4, single seed) 结论边界不明确\n**R1-W3** ARC PPP=0.003 结果仍出现在主文中\n**R1-W4** CI coverage 异常（MMLU over-coverage, ARC under-coverage）未充分诊断\n**R1-W5** RRF filtering item selection bias（300/14042, 仅报告 τ 未报告 MAE 的 random 对照）\n**R1-W6** \"Model-free observation\" 的 confound：SFT data composition 变化 vs contamination effect 未分离\n\n### Reviewer 1 的 Questions\n\nQ1: 是否测试过 non-linear γ specifications？\nQ2: SFT training curves 未报告——training 是否收敛？\nQ3: Hierarchical model 是否可在 camera-ready 前实现？\nQ4: S1 不可用时（无 corpus access），RRF 退化为 S2+S4 的 applicability 讨论不足\nQ5: Within-family GSM8K 的 PPP 在哪里？\n\n### Reviewer 1 的 Missing References\n1. Xu et al. (2024) \"Benchmarking Benchmark Leakage in Large Language Models\" (arXiv 2404.18824)\n2. Li et al. (2024) \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" (AAAI 2024)\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT]，附理由。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "contamcal-irt-calibration",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请对每个 Must-Fix 和 Should-Fix 逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1** [critical] Ecological validity：SFT injection 的 null result 不能回答标题提出的问题\n- 全部实验仅涵盖 LoRA-based SFT injection at ≤3B\n- Pretraining-phase contamination 是实际场景中最常见的形式，机制上与 SFT 有本质差异\n- 核心 claim \"raw accuracy is already well-calibrated\" 的 scope 被标题/abstract 的 framing 大幅放大\n- 建议：修改标题限定 scope；前移 scope limitation\n\n**R1-N2** [critical] Oracle ablation 暴露的 γ 误设定未获充分解决\n- AUC=1.0 时 pooled γ 仍 non-significant（γ=-0.012）\n- 两个解释（heterogeneity / misspecification）未通过 non-linear specification 测试来区分\n- 如果 functional form 错误，null result 可能是模型不够灵敏的 artifact\n- 建议：测试至少一个 non-linear γ specification\n\n**R1-N3** [critical] J=13 domain-level 结论与 J≥50 identifiability 标准的自我矛盾\n- 论文建立 J≥50 标准后以 J=13 进行 domain analysis\n- Social Sciences P(γ<0)=99.1% 在 Abstract/Introduction 中作为 key finding 展示\n- 虽标注 \"exploratory\"，但实际呈现权重与 caution 不匹配\n- 建议：主文改用 J=16 结果；降低 domain γ 在 Abstract/Introduction 的权重\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1** Multiplicity correction：引用 Gelman 2012 但未实施其推荐的 hierarchical model\n**R1-W2** Cross-family analysis (Llama J=4, single seed) 结论边界不明确\n**R1-W3** ARC PPP=0.003 结果仍出现在主文中\n**R1-W4** CI coverage 异常（MMLU over-coverage, ARC under-coverage）未充分诊断\n**R1-W5** RRF filtering item selection bias（300/14042, 仅报告 τ 未报告 MAE 的 random 对照）\n**R1-W6** \"Model-free observation\" 的 confound：SFT data composition 变化 vs contamination effect 未分离\n\n### Reviewer 1 的 Questions\n\nQ1: 是否测试过 non-linear γ specifications？\nQ2: SFT training curves 未报告——training 是否收敛？\nQ3: Hierarchical model 是否可在 camera-ready 前实现？\nQ4: S1 不可用时（无 corpus access），RRF 退化为 S2+S4 的 applicability 讨论不足\nQ5: Within-family GSM8K 的 PPP 在哪里？\n\n### Reviewer 1 的 Missing References\n1. Xu et al. (2024) \"Benchmarking Benchmark Leakage in Large Language Models\" (arXiv 2404.18824)\n2. Li et al. (2024) \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" (AAAI 2024)\n\n---\n\n请逐条给出 [AGREE] 或 [REBUT]，附理由。"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-18T04:54:01.326639+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1468
}
```

</details>

---


### Assistant

_source line 568 · 2026-05-18T04:54:05.702741+00:00_

交叉分享已发送，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 55

## Round 55

2 recorded events


### User

_source line 569 · 2026-05-18T04:54:08.284136+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **3.0/5 (Findings)**。三个 critical issues：(1) SFT injection 的生态效度不足以支撑标题暗示的 scope；(2) oracle ablation 暴露的 linear γ 误设定问题未解决，无法区分 "no effect" 和 "wrong model"；(3) J=13 domain-level 推断与论文自身建立的 J≥50 标准自相矛盾。六个 should-fix 问题涉及 multiplicity correction、cross-family power、ARC model misfit、CI coverage、RRF selection bias、以及 data composition confound。论文的优势在于问题定义精准、null result 诚实、identifiability analysis 有方法论价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 570 · 2026-05-18T04:54:13.842828+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 571 · 2026-05-18T04:56:28.767775+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 对 Reviewer 2 Round 1 意见的交叉回应

---

### Must-Fix 回应

**[AGREE] R2-N1: 技术新颖性不足**
同意。论文在 Section 2 para 3 已承认 γ "is formally an instance of explanatory DIF"。三项 adaptation（continuous exposure、domain stratification、counterfactual inference）均为 psychometrics/explanatory IRT 的标准做法。RRF 是 IR 成熟技术。建议重定位为 empirical measurement study + identifiability boundary analysis，后者（J≥50 threshold, Figure 2）是真正有独立方法论贡献的部分。

**[AGREE] R2-N2: Null finding 范围过窄**
完全同意，与我的 R1-N1 一致。补充两点：(1) LoRA SFT (α=32, r=16) 是 parameter-efficient lightweight fine-tuning，与 pretraining contamination 的 full-parameter optimization 在 representation-level 影响不可比；(2) ≤3B 模型 baseline accuracy 偏低（MMLU ~0.55-0.65），model capacity for memorization 可能不足以产生 aggregate effect，7B+ 模型可能有 qualitatively different 结果。

**[AGREE] R2-N3: Oracle ablation 暴露模型规格问题**
完全同意，与我的 R1-N2 一致。R2 建议在 simulation 中测试 threshold ground-truth 下 linear γ 的 recovery，比我的建议更精确。这个实验仅需修改 simulation code（现有 20 conditions × 10 seeds 框架），成本很低，但能明确区分 "no effect" vs "wrong model"。论文当前的叙事顺序（先列 heterogeneity 再 "alternatively" misspecification）可能误导读者。

---

### Should-Fix 回应

**[AGREE] R2-W1**: Han et al. 差异化中 "calibration focus" 在 null result 下 self-undermining。建议改为 controlled testbed + identifiability analysis + signal failure characterization 作为差异化维度。

**[AGREE] R2-W2**: Diagnostic value 证据单薄。1/8 domain 勉强显著（J=13 未过 Bonferroni, J=16 刚过），7/8 domains P(γ<0) 在 7.8%-44.1% 范围，不足以支撑 diagnostic capability 的 claim。

**[REBUT] R2-W3**: 部分不同意。Signal filtering 是 IRT pipeline 的 necessary condition（S1-only 导致 convergence failure, Section 5.1），不报告则读者无法理解 pipeline 为何需要 Stage 1。Min-K%++ reversal (d=-1.55 to -1.98) 有独立实用价值。但同意 Contribution list 的并列呈现权重过强，应调整 framing 为 "pipeline prerequisite + side finding"。

**[AGREE] R2-W4**: k 索引重载。与我的 R1-M1 一致。

**[AGREE] R2-W5**: J 值频繁切换（7 个不同 J 值）。与我对 model set inconsistency 的 concern 一致。核心问题是 J=13 vs J=16 交替出现，应统一使用 J=16。

---

### Minor 全部 [AGREE]

M1-M6 均合理。特别同意 M4（S4 Self-Critique 计算细节不足影响 reproducibility）和 M2（Abstract 数字密度过高）。

### Missing References 全部 [AGREE]

Camilli & Shepard (1994)、Swaminathan & Rogers (1990) 是 DIF 领域应引用的经典。

---

### 两位 Reviewer 的一致性总结

R1 和 R2 在以下核心问题上完全一致：
1. **Scope-claim gap**（SFT ≤3B vs 标题的一般性）— R1-N1 ≈ R2-N2
2. **Oracle ablation / γ misspecification** — R1-N2 ≈ R2-N3
3. **Domain-level 统计力不足** — R1-N3 ≈ R2-W2（R1 标为 Must-Fix, R2 标为 Should-Fix）
4. **J 值不一致** — R1 model set inconsistency ≈ R2-W5

唯一实质分歧：R2-W3（Contribution 2 与 framing 不一致），我部分 rebut——signal filtering 是 pipeline 必要组成，但同意 framing 需调整。

R2 额外提出的重要点（R1 未充分覆盖）：R2-N1 的技术新颖性不足，我完全同意且认为应列为 Must-Fix 级别。建议论文明确定位为 empirical study 而非 method paper。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 572 · 2026-05-18T04:56:35.427747+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 573 · 2026-05-18T04:56:37.975983+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：R2 的 3 个 Must-Fix 中全部 AGREE，5 个 Should-Fix 中 4 个 AGREE、1 个部分 REBUT（R2-W3: signal filtering 是 pipeline 必要前提，不完全偏离 framing），6 个 Minor 全部 AGREE，3 个 Missing References 全部 AGREE。

两位 Reviewer 的核心关切高度一致：scope-claim gap、oracle ablation misspecification、domain-level statistical power 不足。R2 额外提出的技术新颖性问题（R2-N1）是我 Round 1 未充分覆盖的有效观察。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 574 · 2026-05-18T04:56:43.332878+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 58

## Round 58

10 recorded events


### User

_source line 575 · 2026-05-18T04:56:52.765607+00:00_

[Reviewer 2 审稿意见]:

## Reviewer 2 交叉回应 — 逐条回应 Reviewer 1 Round 1

---

### Must-Fix 回应

**[AGREE] R1-N1: SFT injection 的 ecological validity / 标题 scope 过宽**

同意，且与我的 R2-N2 一致。补充两点：

(1) 论文 Conclusion para 3 写道 "The framework applies directly to settings with larger effects (e.g., pretraining-phase exposure) with no methodological changes"，这句话在没有任何 pretraining 实验支撑的情况下是一个 unsupported forward claim，加剧了 scope inflation 的问题。"applies directly" 是方法论层面的判断（IRT 数学形式不变），但实际问题是 pretraining contamination 是否产生 additive γ 结构可以捕捉的效应模式——这正是 R1 和我在 oracle ablation 问题（R1-N2 / R2-N3）中质疑的。

(2) 不过我想补充一个 nuance：R1 建议 "前移 scope limitation"，但论文 Abstract 第二句已经写了 "Using controlled SFT injection across Qwen2.5 (0.5B--3B)...as a testbed"，所以 Abstract 中 scope 标注是存在的。真正的问题是标题 "Does LLM Benchmark Contamination Need Calibration?" 没有限定语，读者从标题获得的期望与论文回答的问题不匹配。

---

**[AGREE] R1-N2: Oracle ablation 暴露 γ 误设定**

完全同意，与我的 R2-N3 相同的核心关切。我进一步强调：

论文 Section 5.1 para 5 将 oracle ablation 的主要功能定位为 "confirms that filtering is not circular"，但这回避了更根本的问题。Oracle ablation 的真正价值在于它是 model specification 的 stress test——如果 ground truth 都不能让模型检测到效应，那么模型本身的 functional form 就是可疑的。

R1 建议 "测试至少一个 non-linear γ specification"。我同意这是最有力的解决方案。具体建议：在 simulation study（Section 5.3）中增加一个条件：真实数据生成过程使用 threshold/step function contamination，拟合 linear γ，观察 bias pattern。如果 linear γ 在 threshold DGP 下系统性地 attenuate toward zero（如 Limitations para 9 所推测），这就区分了两种解释；如果 linear γ 仍能部分 recover，则误设定风险较低。这个 simulation 不需要额外实验数据，computational cost 很低。

---

**[AGREE with nuance] R1-N3: J=13 vs J≥50 的 "self-contradiction"**

同意核心关切，但 "self-contradiction" 的措辞稍强。

论文确实在多处标注了 "exploratory"（Abstract: "suggestive pattern that requires replication"；Section 5.4: "exploratory"；Conclusion: "requires J≥50 for confirmation"）。问题不是论文没有 caveat，而是 caveat 的呈现权重不匹配：

- Abstract 中 Social Sciences P(γ<0)=99.1% 与 J≥50 threshold 的信息权重相当，读者容易将 99.1% 视为一个 confirmatory finding
- Introduction Contribution list 末尾的 "Additionally" 段展示了这个结果，位置上虽降级但仍是 Introduction 的一部分
- Section 5.4 标题为 "Exploratory Domain Analysis" 是正确的信号，但 Figure 3 和 Table 4 的视觉权重（占据显著版面）与 "exploratory" 定位不一致

R1 建议 "主文改用 J=16 结果"——我同意这在技术上更合理（J=16 的 Social Sciences P(γ<0)=99.7% 通过了 Bonferroni 校正 99.375%，见 Appendix Table 4），同时也减少了 J=13 与 J≥50 标准之间的张力。但我认为更重要的修改是在 Abstract 中降低这个 finding 的权重：当前 Abstract 中 "Social Sciences shows a negative γ effect with high posterior confidence" 的表述对于一个 exploratory、uncorrected-for-multiplicity、J=13 的结果来说过于强势。

---

### Should-Fix 回应

**[AGREE] R1-W1: Gelman 2012 引用但未实施 hierarchical model**

同意。论文 Appendix D (Table 4) caption 引用 Gelman (2012) 说 "Results remain exploratory at these ensemble sizes"，Conclusion para 3 提到 "Hierarchical IRT with partial pooling...would provide shrinkage-based multiplicity adjustment" 作为 future work。但 Gelman (2012) 的核心建议正是用 hierarchical model 做 partial pooling 来替代 Bonferroni——论文知道正确做法但选择不做，这削弱了方法论的完整性。

不过我想指出一个 practical consideration：hierarchical IRT with partial pooling across 8 domains、J=13 models、heterogeneous item counts per domain，在 Stan 中的实现和收敛调试可能需要较大工作量。如果 reviewer consensus 认为这是 must-fix，需要给作者合理的工作量预期。在当前投稿周期（deadline 2026-05-25）内从头实现并调通可能不现实。我认为这更适合作为 strong suggestion for revision 而非 hard blocker。

---

**[REBUT] R1-W2: Cross-family analysis 结论边界不明确**

部分反驳。论文对 Llama cross-family analysis 的 caveat 相当充分：

- Section 4.2 明确写 "This analysis is **exploratory**: the single-seed design provides limited statistical power, and results should be interpreted accordingly"（粗体原文如此）
- Section 4.2 报告了 Llama d100/MMLU 的 catastrophic format collapse 并排除了该数据点
- Section 5.5 para 1 的结论限定为 "IRT ability estimation generalizes"（指 θ 估计的 robustness）而非 "ContamCal generalizes"
- Table 2 caption 明确标注了每个 benchmark 的 J 值

R1 的具体关切是什么需要更明确：如果是认为 "Calibrated MAE remains below 0.02" 这个结论被 over-generalized，我可以部分同意——这个数字在 J=18-28 的 mixed pool 下得出，但论文没有 report confidence interval for MAE 本身。但如果是认为 cross-family section 缺乏 caveat，我认为论文已经做到了。

---

**[AGREE with nuance] R1-W3: ARC PPP=0.003 在主文中**

同意关切方向，但论文的处理方式是可接受的。Section 5.1 para 3 提到 ARC 时立即标注 "IRT model fit is marginal (PPP=0.003)" 并将完整结果导向 Appendix F。这不是在隐藏问题。

但我同意 R1 的隐含观点：当一个模型的 PPP=0.003 时，从该模型得出的任何 IRT 参数估计（包括 γ、θ、a_i、b_i）都不可靠。当前正文中 "ARC exhibits the same pattern (raw MAE 0.007)" 的表述可能让读者误以为 ARC 结果与 MMLU 同等可信。建议在正文中更明确地说 ARC 的 IRT 结果因 model misfit 而不可 interpret，仅保留 raw accuracy 的报告。

---

**[AGREE] R1-W4: CI coverage 异常未充分诊断**

同意。MMLU over-coverage（50% CI 实际覆盖 83%）和 ARC under-coverage（50% CI 仅覆盖 45%）是两个不同的问题，但论文将它们归因为同一类现象（"benchmark-dependent"）而未深入分析。

MMLU 的 over-coverage 意味着 posterior uncertainty 过大——这可能源于 J=16 对于当前 prior specification 的 data-to-prior ratio 不足（与 Appendix C prior sensitivity 中 pooled γ 对 prior 敏感的发现一致）。ARC 的 under-coverage 则指向 model misfit（PPP=0.003），posterior predictive distribution 系统性地偏离了数据。这两个根因不同，需要分别诊断。论文将 CI coverage 列为 evaluation metric 之一（Section 4.3），但当 coverage 异常时未提供 actionable diagnosis，这削弱了 uncertainty quantification 作为卖点的可信度。

---

**[AGREE] R1-W5: RRF filtering 的 item selection bias / MAE random 对照缺失**

同意。论文报告了 random 300-item subsets 的 τ 对照（Section 5.1 para 2: τ = 0.554 ± 0.048 vs RRF τ = 0.731），但未报告 random subsets 的 MAE。这是一个遗漏：如果 random 300-item subsets 的 MAE 与 RRF-selected subsets 相当（都很低），则说明 MAE 改善来自 effect size 小而非 filtering；如果 random subsets MAE 更差，则 filtering 确实有校准价值。缺少这个对照使得 "filtering improves calibration" 的 claim 仅有 τ 一个指标支撑。

另外，300/14042（约 2%）的选择比例意味着 RRF-selected items 是 MMLU 中 contamination signal 最强的极端尾部。对这个 biased subset 的 IRT 拟合可能不代表 full benchmark 的行为。论文的 exclusion sensitivity analysis（Section 5.1 para 1, removing 0-50% top-exposure items from random 2000-item subsets）是相关的，但方向相反（从 random set 中排除 vs 从 full set 中选择），不能直接回答 selection bias 问题。

---

**[AGREE] R1-W6: "Model-free observation" 的 confound 问题**

同意这是一个有效的方法论关切。Section 5.1 para 3 将 0.6-0.7pp 称为 "a model-free observation: raw accuracy difference between d000 and d100"。但 Section 4.1 描述 SFT injection 时说 benchmark items are "injected" into a general-purpose SFT corpus，这意味着随着 dosage 增加（d005 → d100），benchmark items 要么 (a) 替代了部分 general SFT data，要么 (b) 增加了总训练数据量。论文未说明是哪种。

如果是 (a)（替代），则 d100 模型不仅获得了 benchmark items 的记忆，还损失了 general instruction-following 能力，0.6-0.7pp 是 contamination benefit 与 capability loss 的净效应，真实 contamination effect 可能更大。如果是 (b)（追加），则 d100 模型训练步数更多，0.6-0.7pp 可能部分来自额外训练而非 contamination。

这个 confound 实际上可能对论文有利也可能不利：如果 contamination benefit 被 capability loss 抵消（scenario a），那么 "raw accuracy is well-calibrated" 的结论仍然成立（net effect 仍然小），但 mechanism 不同。无论如何，将 0.6-0.7pp 简单归因为 contamination effect 是不精确的。

---

### Questions 回应

**Q1 (non-linear γ)**: 同意这是关键实验。与我的 R2-N3 建议一致。

**Q2 (SFT training curves)**: 同意应补充。训练收敛性对 controlled injection 实验的有效性至关重要——如果某些 dosage 配置未收敛，则该配置下的结果不可靠。

**Q3 (Hierarchical model feasibility)**: 同意建议方向。如上述 R1-W1 回应中所述，实际实现可能需要较多工作量，但至少应在 simulation study 中展示 hierarchical specification 对 domain-level γ 估计的影响。

**Q4 (S1 不可用时的降级讨论)**: 同意不足。Section 5.2 提到 S2+S4 在 0.5B 以下 near-random，但未讨论在 1.5B+ scale、S1 不可用时 S2+S4-only RRF 的表现如何。这对 closed-source model 场景的 applicability 很重要。

**Q5 (Within-family GSM8K PPP)**: 好问题。Cross-family PPP=0.83（Table 2），但 within-family GSM8K 的 PPP 似乎未在正文或附录中单独报告。考虑到 ARC 出现了 PPP=0.003 的 misfit 问题，GSM8K 的 model fit 需要显式确认。

---

### Missing References 回应

**Xu et al. (2024) "Benchmarking Benchmark Leakage"**: 同意应补充。这是一个系统性的 contamination benchmark，与本文的 controlled injection 方法互补。如果该论文有关于 aggregate effect size 的定量结论，将直接与本文的 null finding 形成对照。

**Li et al. (2024) "Task Contamination" (AAAI 2024)**: 部分同意。该论文关注 few-shot contamination 对 in-context learning 的影响，与本文的 SFT injection + IRT 框架不完全对应。但如果 Related Work 的 contamination detection 段要 claim 全面覆盖，这个方向（task-level contamination vs instance-level contamination）应该至少被提及。

---

### 总结

R1 的三个 Must-Fix 与我的审查高度一致（R1-N1≈R2-N2, R1-N2≈R2-N3, R1-N3 与 R2-W2/W5 部分重叠）。两位 Reviewer 独立收敛到相同的核心问题——scope limitation、oracle ablation、J≥50 与 J=13 的张力——增强了这些关切的可信度。Should-Fix 中我仅对 R1-W2（cross-family caveat）部分反驳，其余均同意。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-18T05:00:10.969550+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "review_issues.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "review_issues.yaml",
    "max_chars": "0"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-18T05:00:11.070512+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-18T05:00:16.922548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-18T05:00:17.174920+00:00_

1	- id: "R2-N1"
2	  summary: "Title/framing still promises decomposition+calibration but core finding is raw accuracy suffices"
3	  category: framing
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 2
7	  last_seen_round: 5
8	  mentions:
9	    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
10	    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
11	    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
12	    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?') but framing still inconsistent. Intro ¶1-3 heavily motivate calibration, Results show calibration unnecessary. Contributions 1-3 span empirical finding / engineering observation / exploratory analysis without unified main line. 'Why not just use raw accuracy?' paragraph in Conclusion reads as arguing against paper's own existence. Both AGREE: need full empirical investigation framing from ¶1, ContamCal as investigative instrument not product."}
13	  action_items:
14	    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
15	    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
16	    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assigned_to: "paper_agent", status: "done"}
17	    - {round: 5, action: "Rewrite Introduction from ¶1 as question-driven empirical investigation; ContamCal as tool not contribution; consolida
…[truncated 27253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-18T05:04:48.730067+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?') but framing still inconsistent. Intro ¶1-3 heavily motivate calibration, Results show calibration unnecessary. Contributions 1-3 span empirical finding / engineering observation / exploratory analysis without unified main line. 'Why not just use raw accuracy?' paragraph in Conclusion reads as arguing against paper's own existence. Both AGREE: need full empirical investigation framing from ¶1, ContamCal as investigative instrument not product.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes. R1-N1 and R2-N2 unanimously agree: 'Does LLM Benchmark Contamination Need Calibration?' implies general answer but experiments only SFT ≤3B. Abstract second sentence scopes but title does not. Conclusion 'applies directly to settings with larger effects' is unsupported forward claim. Both AGREE title must scope or be modified.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation; ContamCal as tool not contribution; consolidate Contributions to 2 items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim (e.g. add 'SFT-Injected' or similar); remove Conclusion 'applies directly' unsupported claim\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without qualification. Pretraining contamination (arXiv 2601.04301) shows significantly larger effects. All claims must be scoped to 'under SFT injection at ≤3B scale'. Both reviewers AGREE unanimously.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract. But title still asks generic question. R2 adds: SFT vs pretraining differs in mechanism not just scale — pretraining contamination embeds into representations (θ) not just LoRA adapter. §5.5 θ asymmetry already hints at this. Both AGREE title needs scoping or Abstract first sentence must scope.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1: LoRA SFT (α=32, r=16) is parameter-efficient lightweight fine-tuning, representation-level impact incomparable to pretraining contamination. ≤3B models baseline accuracy ~0.55-0.65 may lack memorization capacity. R2: Conclusion 'applies directly to settings with larger effects' is unsupported forward claim. Both AGREE scope limitation persists despite prior improvements.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims in Abstract/Intro/Conclusion to 'under SFT injection at ≤3B'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite and discuss pretraining contamination dose-response literature as contrast\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Remove/caveat Conclusion 'applies directly' claim; consider 7B+ pilot experiment to expand scope\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation (AUC=1.0, γ=-0.012 non-sig) has two interpretations: (a) genuine null effect (heterogeneity cancels), (b) model misspecification (linear γ cannot capture threshold/interaction effects). Paper adopts (a) without testing (b). Limitations ¶9 acknowledges threshold possibility but §5.1 oracle section ignores it. Both reviewers AGREE this is fundamental ambiguity.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations. R2 partial REBUT on R1-N1: aggregate 0.6-0.7pp is model-free observation (direct d000 vs d005/d025/d100 accuracy comparison), misspecification only affects γ diagnostic claims. Both AGREE: paper must distinguish model-free findings (aggregate accuracy shift) from model-dependent findings (γ significance/direction). γ-related claims need 'under additive linear specification' caveat.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both reviewers unanimously re-raise as critical. Oracle ablation framed as 'confirms filtering not circular' (§5.1 para 5) sidesteps the fundamental model specification question. R2 proposes concrete resolution: add threshold DGP condition to existing simulation framework (20 conditions × 10 seeds), fit linear γ, observe attenuation pattern. Low computational cost, high diagnostic value. Both AGREE this is required.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i or γ×a_i interaction model as misspecification check\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If not testable, explicitly scope claim as 'under linear additive specification'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat to γ-related claims; distinguish model-free vs model-dependent findings\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Run threshold DGP simulation: generate data with step-function contamination, fit linear γ, report attenuation pattern to distinguish 'no effect' from 'wrong model'\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction + underpowered J\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"8 independent domain tests, only Social Sciences significant at α=0.05. Bonferroni α=0.00625; CI upper bound -0.10 would likely include zero. BH correction also unlikely to survive 1/8 pattern. This is the sole evidence for 'diagnostic value' narrative. Both AGREE correction needed.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 reconfirms: Bonferroni threshold P(γ<0)≥99.375%, Social Sciences at 99.1% does not pass. R2 AGREE with nuance: (1) Bayesian posteriors don't strictly need frequentist correction per Gelman 2012, BUT independent per-domain fits without shrinkage do need correction; (2) Abstract reports P(γ<0)=99.1% without any multiplicity caveat. Both AGREE: report corrected result, or switch to hierarchical IRT for natural shrinkage.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-N3 elevates to critical (self-contradiction between J≥50 standard and J=13 domain analysis). R2 AGREE with nuance: 'self-contradiction' overstates but presentation weight mismatch is real. J=16 results (99.7%) cross Bonferroni but main text still uses J=13 (99.1%). Abstract presents 99.1% with high visual weight. Both AGREE: use J=16 in main text, reduce domain γ prominence in Abstract.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results for domain-level γ\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"If non-significant after correction, reframe as 'suggestive pattern requiring higher-powered replication'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' when reporting P(γ<0)=99.1% in Abstract/Results; C3 demoted to observation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results; reduce Social Sciences finding prominence in Abstract to secondary observation\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at J=8, 13, 16 per §5.4. Table 3 still reports ARC IRT results without PPP annotation. R2 nuance: ARC ~0.7pp from raw data is valid, but IRT-derived numbers are unreliable. Both AGREE Table 3 needs PPP annotation and ARC IRT results need caveat.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003 in caption, but ARC IRT results still in main table alongside MMLU giving visual parity. R1: move ARC IRT to Appendix or grey out. R2 AGREE: also helps solve page limit (R5-N1) by shrinking Table 3. Both AGREE 2PL+γ structural misfit for ARC (not just sample size issue) should be discussed in main text.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Improvement noted: ARC IRT moved to Appendix sec:arc_irt, Table 1 now MMLU-only. R1-W3 re-raises with nuance: §5.1 still mentions 'ARC exhibits the same pattern' which may mislead readers into treating ARC IRT results as equally reliable. R2 agrees: make explicit that ARC IRT parameters are uninterpretable due to misfit. Downgraded from critical to warning given appendix move.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column in Table 3\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Discuss ARC misfit source (item pool heterogeneity vs model specification)\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix; discuss structural misfit in main text\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Clarify in §5.1 that ARC IRT parameters are unreliable due to structural misfit; keep only raw accuracy for ARC in main text\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical by R2. S2 reverses at 0.5B, S4 near-random below 1.5B. §5.2 admits RRF degrades to S1-only. No direct RRF vs S1-only ablation (τ, MAE, γ) at 1.5B/3B where S2 d≈+0.7. R1 partially rebuts absolute claim but agrees ablation is missing. Contribution 2 unsupported without this evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation now complete: S1-only causes MCMC non-convergence (MMLU R̂=1.53) due to exposure variance compression ([0.749,0.867]). This proves RRF necessary for IRT convergence. However R1 W3 insight: ablation evidence supports RRF for exposure VARIANCE, not signal QUALITY. Paper conflates these. Both AGREE: precise the contribution claim. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-W5: Random 300-item subsets report τ=0.554±0.048 but no MAE comparison. If random MAE is similarly low, filtering value is limited to rank correlation. 300/14042 (2%) selection means extreme tail items only. R2 AGREE. Additionally, exclusion sensitivity analysis (§5.1) removes from random set (opposite direction to selection), not directly comparable.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2 in D134 reframing\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation at 1.5B and 3B (τ, MAE, γ significance)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If RRF ≤ S1-only, downgrade Contribution 2 to 'item filtering improves IRT' without RRF-specific claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish exposure variance contribution from signal quality; report RRF composite AUC vs S1-only AUC\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Report MAE for random 300-item subsets alongside τ to complete the comparison\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"§5.1 only reports 50%. 80%/95% completely missing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"CI coverage now reported in Limitations: MMLU 83%/89%/100%, ARC 45%/65%/90%. ARC under-coverage corroborates PPP<0.05 misfit. Both AGREE this should be in main results, not just Limitations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results. R1: MMLU 95% CI covers 100% = completely uninformative. R2 AGREE: over-coverage (MMLU) and under-coverage (ARC) have different root causes and should be discussed separately.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Improvement: CI coverage now in §5.1 with MMLU/ARC split. R1-W4 and R2 both agree root cause diagnosis still insufficient. MMLU over-coverage (50% CI=83%) = uninformatively wide posteriors (data-to-prior ratio too low at J=16, consistent with Appendix C prior sensitivity). ARC under-coverage (50% CI=45%) = structural misfit (PPP=0.003). Paper lumps as 'benchmark-dependent'. Both AGREE: separate diagnosis needed.\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage discussion to main results section\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss over-coverage and under-coverage root causes separately\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Provide explicit root-cause diagnosis: MMLU over-coverage from insufficient data-to-prior ratio; ARC under-coverage from structural misfit. Remove 'benchmark-dependent' umbrella framing.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses (13/16/18/20/24/28) — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Contribution 4 combines simulation + empirical. Should split.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"J inconsistency from experimental timeline (domain runs before 3B retraining). All γ conclusions at J=13-16 are underpowered by paper's own standard. Both AGREE needs prominent caveat and ideally unified J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Model set table in Appendix B. But core problem: most interesting finding (domain γ) uses weakest configuration (J=13). Prior sensitivity in Appendix C uses J=16 for Social Sciences but main Table 2 still reports J=13. Both AGREE: either rerun domain analysis at J=16, or explicitly state J=13 vs J=16 consistency in main text.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-N3 elevates to critical. J=16 data available (Appendix Table 4) but main text §5.4 still presents J=13. 7 different J values across sections without cohesive overview. R2-W5 AGREE: readers need constant table-checking. Both AGREE: (a) use J=16 in main text; (b) add model set overview paragraph at §5 start.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J and model composition prominently in each table/figure\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16 for cross-validation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16 domain results; add model set overview paragraph at §5 start\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 (300 RRF) vs 0.46 (2000 random) may reflect higher average a_i in RRF-selected items, not contamination signal value. Need discrimination-matched random subset comparison or report average a_i of RRF vs random sets.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently re-raised in R5. Resolution from R4 (mean a_i comparison, Cohen's d=0.098) appears in §5.1. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items; add discrimination-matched control\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Mean a_i comparison: RRF-selected mean=1.12, random mean=1.09, Cohen's d=0.098, r=-0.013. No discrimination confound. §5.1 documents this exclusion. Not re-raised in R5 or R6.\"\n  resolution_round: 5\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"'Validated' too strong for single-seed N=3-4.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"§4.2 references 'Appendix E post-hoc power calculations' but Appendix E contains baseline tables, not power analysis. Missing content. Both strongly AGREE.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Phantom reference removed. §5.5 title still 'Cross-Family Validation'. Both AGREE: rename.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-W2: conclusion boundaries still unclear. R2 partial REBUT: paper has adequate 'exploratory' labeling, catastrophic collapse documentation, and scoped conclusions. R2 notes MAE CI for cross-family pool not reported. Minor residual issue.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Write and include actual Appendix E power analysis OR remove the reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D138: §5.5 renamed. Adequate caveats present. Minor residual: MAE CI for cross-family pool not reported.\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50. Prior N(0,1) dominance?\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"γ~N(0,1) covers ±2 logit units. No prior sensitivity analysis. Need at least N(0,0.5) and N(0,2) alternatives. Also need e_ij distribution.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised in R5. Prior sensitivity now in Appendix C: pooled prior-dominated (2.6×), Social Sciences data-dominated (1.2×). Resolved.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2); report e_ij distribution\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Full prior sensitivity complete. Pooled: 2.6× prior-dominated. Social Sciences: 1.2× data-dominated, P(γ<0)≥97.95% across all priors. e_ij distribution reported. Not re-raised in R6.\"\n  resolution_round: 5\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption at 0.5B but provides no direct evidence. Alternative explanations not ruled out.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 W4: Min-K%++ reversal may be SFT artifact. R2 partial REBUT: paper already qualifies as post-hoc. Both AGREE: Conclusion claim must be scoped to 'under SFT injection'.\"}\n    - {round: 6, reviewers: \"\", note: \"Not independently re-raised in R6. Paper now scopes to 'at the 0.5B scale under SFT injection' in Conclusion, labels hypothesis as 'post-hoc'. Previous action items completed. Candidate for resolution pending Research Director confirmation.\"}\n  action_items:\n    - {round: 4, action: \"Either provide token-level perplexity comparison or reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion Min-K++ claim to 'at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D138: Conclusion scoped. Hypothesis labeled post-hoc. Alternative explanations listed in §5.2. Not re-raised in R6.\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span null finding, item filtering, signal failure, identifiability, domain diagnosis. R2 suggests consolidate to 2-3.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions. R2 N3: still span different types without unified main line. Both suggest further consolidation to 2 contributions.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Now 2 contributions + 1 observation. R2-W3: C2 (signal filtering + Min-K++ reversal) reads like method paper contribution, not empirical investigation finding. R1 partial REBUT: filtering is pipeline prerequisite (S1-only → convergence failure), Min-K++ reversal has standalone value. Both AGREE on compromise: reframe C2 as 'enabling analysis + standalone practical finding' rather than parallel contribution.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further consolidate to 2 contributions; demote C3 to observation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reframe C2 as 'enabling analysis for the investigation' + 'standalone practical finding (Min-K++ reversal)' rather than parallel contribution\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. (EACL Findings 2026) most direct concurrent work. arXiv 2601.04301 provides pretraining dose-response. Chen et al. EMNLP 2025 survey.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R4 references added. New gaps: Lord (1980), Hambleton (1991), HELM (Liang 2023), Magar & Schwartz (2022). Han et al. differentiation needs 3-4 sentences.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Lord, Hambleton, HELM, Magar now in bib. Han et al. differentiation expanded. New gaps identified: Camilli & Shepard (1994) DIF classic, Swaminathan & Rogers (1990) logistic regression DIF with continuous covariates, Xu et al. (2024) 'Benchmarking Benchmark Leakage', Li et al. (2024) 'Task Contamination' AAAI, Roberts et al. (2025) or similar on IRT small-J identifiability.\"}\n  action_items:\n    - {round: 4, action: \"Verify and cite Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025 survey\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord (1980), Hambleton (1991), HELM, Magar & Schwartz bib entries\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Expand Han et al. comparison to 3-4 sentences in Related Work/Introduction\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Add Camilli & Shepard (1994), Swaminathan & Rogers (1990), Xu et al. (2024), Li et al. (2024 AAAI) to bib and cite appropriately\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'. Per-domain model fit unverifiable.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present (0.096-0.570). Not re-raised in R5. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values in Table 2\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"PPP values filled in domain γ table: range 0.096-0.570. Table moved to Appendix in D138. Not re-raised in R6.\"\n  resolution_round: 5\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"~202 words but still 8-9 numbers. Both AGREE: keep 2-3 key numbers, replace rest with qualitative.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Trimmed to ~170 words but R2-M2 notes still 6+ numbers (0.6-0.7pp, Δτ values, Cohen's d, J≥50, P(γ<0)=99.1%). Both AGREE: keep only ~0.6-0.7pp and J≥50, replace others with qualitative descriptions.\"}\n  action_items:\n    - {round: 4, action: \"Trim Abstract to ≤220 words, reduce to 2-3 key numbers\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further reduce numeric density: keep ~0.6-0.7pp and J≥50, replace others with qualitative\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Final pass: retain only 0.6-0.7pp and J≥50 as numbers; Δτ, Cohen's d, P(γ<0) → qualitative\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Han et al. EACL 2026 uncited. Technical novelty remains limited.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Paper self-acknowledges 'formally an instance of explanatory DIF'. Both AGREE: must position as empirical contribution, not methodological.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R2-N1 elevates to critical. Paper repositioned as empirical investigation but C2 still reads as method contribution. Han et al. differentiation uses 'calibration focus' which is self-undermining under null result. R1 fully AGREE. Both: reposition differentiation around controlled testbed + identifiability analysis + signal failure characterization; elevate identifiability analysis (J≥50) as standalone contribution.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. EACL 2026 as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state in Introduction that contribution is systematic empirical investigation, not technical modeling\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reposition Han et al. differentiation: remove 'calibration focus' (self-undermining), emphasize controlled testbed + identifiability thresholds + signal failure modes. Elevate J≥50 identifiability as lead contribution item.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation needs rework\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"33 citations.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"New gaps: Han et al., arXiv 2601.04301, Chen EMNLP 2025.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. New gaps: Lord, Hambleton, HELM, Magar & Schwartz. Han et al. comparison needs expansion.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"~52 citations, major gaps filled. Han et al. expanded but R2-W1 notes differentiation is self-undermining ('calibration focus' fails under null result). R2 recommends Camilli & Shepard 1994, Swaminathan & Rogers 1990 for DIF foundation. R1 recommends Xu et al. 2024, Li et al. 2024 AAAI for contamination benchmark coverage.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al., Chen et al., Singh et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz bib entries + expand Han et al. comparison\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Rework Han et al. differentiation (remove 'calibration focus', emphasize testbed + identifiability); add Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Tables 4 and 3 float to page 9. Main content ~8.5 pages. ACL Long paper: ≤8 pages content. Desk-reject risk.\"}\n    - {round: 6, reviewers: \"R2\", note: \"R2-M6: Cannot confirm page count without compilation. Content (6 sections + 3 figures + 2 in-text tables) appears near limit. Domain γ table moved to appendix helps. Downgraded to warning — needs author verification.\"}\n  action_items:\n    - {round: 5, action: \"Move ARC IRT from Table 3 to Appendix; compress §5.1 RRF ablation; move Table 2 (domain γ) to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Compile and verify ≤8 pages main content; adjust if needed\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"Method §3.1 defines y_ijk with k = benchmark, but Eq.2 uses k = stratum/domain. Should be noted.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R2-W4: Parenthetical annotation added but insufficient. Same variable changing meaning between adjacent sections is non-standard notation. Both AGREE: use different symbol for strata (e.g. d or s).\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Replace k with different symbol (d or s) for strata index; keep k for benchmark\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — injection replaces or augments general SFT data unclear\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-W6: §4.1 does not specify whether benchmark items replace or augment general SFT corpus. If replacement (a), d100 loses general capability and 0.6-0.7pp is net of contamination benefit minus capability loss. If augmentation (b), d100 has more training steps. Either way, attributing 0.6-0.7pp purely to 'contamination effect' is imprecise. R2 AGREE: confound may favor or hurt the conclusion, but 'model-free observation' label is misleading.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol: replacement vs augmentation; discuss implications for the 0.6-0.7pp interpretation\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2\", note: \"R2-M4: §3.2 defines S4 as 'negative entropy of model self-evaluation distributions' citing Kadavath et al. 2022. Prompt design, evaluation distribution construction, and scoring mechanism not described. Insufficient for independent reproduction.\"}\n  action_items:\n    - {round: 6, action: \"Add S4 computation details: prompt template, evaluation distribution construction, scoring\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1\", note: \"R1-Q2: Training convergence is prerequisite for controlled injection validity. If some dosage configurations did not converge, results from those configurations are unreliable. No training curves or convergence metrics reported.\"}\n  action_items:\n    - {round: 6, action: \"Report SFT training curves or convergence verification (final loss, learning rate schedule completion) in Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-Q5: Cross-family GSM8K PPP=0.83 (Table 2) but within-family GSM8K PPP not in main text or appendix. Given ARC PPP=0.003 misfit, GSM8K model fit needs explicit confirmation.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP in results or appendix\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "issues_yaml": "- id: \"R2-N1\"\n  summary: \"Title/framing promises general answer but experiments only cover SFT ≤3B\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Title still 'ContamCal'. Abstract implies contamination-specific modeling.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Title changed to question form ('Does LLM Benchmark Contamination Need Calibration?') but framing still inconsistent. Intro ¶1-3 heavily motivate calibration, Results show calibration unnecessary. Contributions 1-3 span empirical finding / engineering observation / exploratory analysis without unified main line. 'Why not just use raw accuracy?' paragraph in Conclusion reads as arguing against paper's own existence. Both AGREE: need full empirical investigation framing from ¶1, ContamCal as investigative instrument not product.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Title question form improved but still over-scopes. R1-N1 and R2-N2 unanimously agree: 'Does LLM Benchmark Contamination Need Calibration?' implies general answer but experiments only SFT ≤3B. Abstract second sentence scopes but title does not. Conclusion 'applies directly to settings with larger effects' is unsupported forward claim. Both AGREE title must scope or be modified.\"}\n  action_items:\n    - {round: 2, action: \"Reframe paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 3, action: \"Change title, rewrite Abstract/Contributions\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Reframe as empirical investigation rather than method paper\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rewrite Introduction from ¶1 as question-driven empirical investigation; ContamCal as tool not contribution; consolidate Contributions to 2 items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Modify title to scope claim (e.g. add 'SFT-Injected' or similar); remove Conclusion 'applies directly' unsupported claim\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W6\"\n  summary: \"SFT injection ecological validity insufficient — null finding may be SFT artifact, not general property\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Intro motivates with pretraining but experiments only SFT.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Limitations one sentence only.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Abstract/Conclusion still say 'raw accuracy is already well-calibrated' without qualification. Pretraining contamination (arXiv 2601.04301) shows significantly larger effects. All claims must be scoped to 'under SFT injection at ≤3B scale'. Both reviewers AGREE unanimously.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Claims now scoped with 'Under SFT injection at ≤3B' in Abstract. But title still asks generic question. R2 adds: SFT vs pretraining differs in mechanism not just scale — pretraining contamination embeds into representations (θ) not just LoRA adapter. §5.5 θ asymmetry already hints at this. Both AGREE title needs scoping or Abstract first sentence must scope.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1: LoRA SFT (α=32, r=16) is parameter-efficient lightweight fine-tuning, representation-level impact incomparable to pretraining contamination. ≤3B models baseline accuracy ~0.55-0.65 may lack memorization capacity. R2: Conclusion 'applies directly to settings with larger effects' is unsupported forward claim. Both AGREE scope limitation persists despite prior improvements.\"}\n  action_items:\n    - {round: 3, action: \"Expand Limitations ecological validity discussion\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Scope all claims in Abstract/Intro/Conclusion to 'under SFT injection at ≤3B'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite and discuss pretraining contamination dose-response literature as contrast\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Ensure Abstract first sentence explicitly scopes to SFT injection\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Remove/caveat Conclusion 'applies directly' claim; consider 7B+ pilot experiment to expand scope\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-W10\"\n  summary: \"Additive linear γ assumption untested — oracle ablation cannot distinguish null effect from model misspecification\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Linear γ may average down to non-significant.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical. Oracle ablation (AUC=1.0, γ=-0.012 non-sig) has two interpretations: (a) genuine null effect (heterogeneity cancels), (b) model misspecification (linear γ cannot capture threshold/interaction effects). Paper adopts (a) without testing (b). Limitations ¶9 acknowledges threshold possibility but §5.1 oracle section ignores it. Both reviewers AGREE this is fundamental ambiguity.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"§5.1 oracle paragraph now presents both interpretations. R2 partial REBUT on R1-N1: aggregate 0.6-0.7pp is model-free observation (direct d000 vs d005/d025/d100 accuracy comparison), misspecification only affects γ diagnostic claims. Both AGREE: paper must distinguish model-free findings (aggregate accuracy shift) from model-dependent findings (γ significance/direction). γ-related claims need 'under additive linear specification' caveat.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Both reviewers unanimously re-raise as critical. Oracle ablation framed as 'confirms filtering not circular' (§5.1 para 5) sidesteps the fundamental model specification question. R2 proposes concrete resolution: add threshold DGP condition to existing simulation framework (20 conditions × 10 seeds), fit linear γ, observe attenuation pattern. Low computational cost, high diagnostic value. Both AGREE this is required.\"}\n  action_items:\n    - {round: 3, action: \"Discuss linearity assumption in Limitations\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Test item-level γ_i or γ×a_i interaction model as misspecification check\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If not testable, explicitly scope claim as 'under linear additive specification'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'under the additive linear specification' caveat to γ-related claims; distinguish model-free vs model-dependent findings\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Run threshold DGP simulation: generate data with step-function contamination, fit linear γ, report attenuation pattern to distinguish 'no effect' from 'wrong model'\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-N1\"\n  summary: \"Domain-level γ significance (Social Sciences 1/8) lacks multiple comparison correction + underpowered J\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"8 independent domain tests, only Social Sciences significant at α=0.05. Bonferroni α=0.00625; CI upper bound -0.10 would likely include zero. BH correction also unlikely to survive 1/8 pattern. This is the sole evidence for 'diagnostic value' narrative. Both AGREE correction needed.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 reconfirms: Bonferroni threshold P(γ<0)≥99.375%, Social Sciences at 99.1% does not pass. R2 AGREE with nuance: (1) Bayesian posteriors don't strictly need frequentist correction per Gelman 2012, BUT independent per-domain fits without shrinkage do need correction; (2) Abstract reports P(γ<0)=99.1% without any multiplicity caveat. Both AGREE: report corrected result, or switch to hierarchical IRT for natural shrinkage.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-N3 elevates to critical (self-contradiction between J≥50 standard and J=13 domain analysis). R2 AGREE with nuance: 'self-contradiction' overstates but presentation weight mismatch is real. J=16 results (99.7%) cross Bonferroni but main text still uses J=13 (99.1%). Abstract presents 99.1% with high visual weight. Both AGREE: use J=16 in main text, reduce domain γ prominence in Abstract.\"}\n  action_items:\n    - {round: 4, action: \"Report Bonferroni and BH corrected results for domain-level γ\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"If non-significant after correction, reframe as 'suggestive pattern requiring higher-powered replication'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add 'uncorrected for multiplicity' when reporting P(γ<0)=99.1% in Abstract/Results; C3 demoted to observation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text domain γ to J=16 results; reduce Social Sciences finding prominence in Abstract to secondary observation\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N3\"\n  summary: \"ARC PPP < 0.05 across all J configurations — IRT results unreliable\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R1\", note: \"Within-family J=13 ARC PPP=0.003 not reported.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"ARC PPP < 0.05 at J=8, 13, 16 per §5.4. Table 3 still reports ARC IRT results without PPP annotation. R2 nuance: ARC ~0.7pp from raw data is valid, but IRT-derived numbers are unreliable. Both AGREE Table 3 needs PPP annotation and ARC IRT results need caveat.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Table 3 now has PPP=0.003 in caption, but ARC IRT results still in main table alongside MMLU giving visual parity. R1: move ARC IRT to Appendix or grey out. R2 AGREE: also helps solve page limit (R5-N1) by shrinking Table 3. Both AGREE 2PL+γ structural misfit for ARC (not just sample size issue) should be discussed in main text.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Improvement noted: ARC IRT moved to Appendix sec:arc_irt, Table 1 now MMLU-only. R1-W3 re-raises with nuance: §5.1 still mentions 'ARC exhibits the same pattern' which may mislead readers into treating ARC IRT results as equally reliable. R2 agrees: make explicit that ARC IRT parameters are uninterpretable due to misfit. Downgraded from critical to warning given appendix move.\"}\n  action_items:\n    - {round: 3, action: \"Report ARC PPP=0.027 with caveat\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Add PPP annotation to ARC column in Table 3\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Discuss ARC misfit source (item pool heterogeneity vs model specification)\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Move ARC IRT results to Appendix; discuss structural misfit in main text\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Clarify in §5.1 that ARC IRT parameters are unreliable due to structural misfit; keep only raw accuracy for ARC in main text\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W1\"\n  summary: \"RRF multi-signal fusion — value is exposure variance, not signal quality; MAE random control missing\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"RRF = S1 only.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"C2 wording overclaims.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Elevated to critical by R2. S2 reverses at 0.5B, S4 near-random below 1.5B. §5.2 admits RRF degrades to S1-only. No direct RRF vs S1-only ablation (τ, MAE, γ) at 1.5B/3B where S2 d≈+0.7. R1 partially rebuts absolute claim but agrees ablation is missing. Contribution 2 unsupported without this evidence.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"RRF ablation now complete: S1-only causes MCMC non-convergence (MMLU R̂=1.53) due to exposure variance compression ([0.749,0.867]). This proves RRF necessary for IRT convergence. However R1 W3 insight: ablation evidence supports RRF for exposure VARIANCE, not signal QUALITY. Paper conflates these. Both AGREE: precise the contribution claim. Downgraded to warning.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-W5: Random 300-item subsets report τ=0.554±0.048 but no MAE comparison. If random MAE is similarly low, filtering value is limited to rank correlation. 300/14042 (2%) selection means extreme tail items only. R2 AGREE. Additionally, exclusion sensitivity analysis (§5.1) removes from random set (opposite direction to selection), not directly comparable.\"}\n  action_items:\n    - {round: 3, action: \"Reword C2 in D134 reframing\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Provide RRF vs S1-only ablation at 1.5B and 3B (τ, MAE, γ significance)\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"If RRF ≤ S1-only, downgrade Contribution 2 to 'item filtering improves IRT' without RRF-specific claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Distinguish exposure variance contribution from signal quality; report RRF composite AUC vs S1-only AUC\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Report MAE for random 300-item subsets alongside τ to complete the comparison\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N2\"\n  summary: \"CI coverage systematically abnormal — over-coverage and under-coverage have different root causes\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Need 80%/95% coverage + root cause diagnosis.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"§5.1 only reports 50%. 80%/95% completely missing.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"CI coverage now reported in Limitations: MMLU 83%/89%/100%, ARC 45%/65%/90%. ARC under-coverage corroborates PPP<0.05 misfit. Both AGREE this should be in main results, not just Limitations.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"CI coverage now in §5.1 main results. R1: MMLU 95% CI covers 100% = completely uninformative. R2 AGREE: over-coverage (MMLU) and under-coverage (ARC) have different root causes and should be discussed separately.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Improvement: CI coverage now in §5.1 with MMLU/ARC split. R1-W4 and R2 both agree root cause diagnosis still insufficient. MMLU over-coverage (50% CI=83%) = uninformatively wide posteriors (data-to-prior ratio too low at J=16, consistent with Appendix C prior sensitivity). ARC under-coverage (50% CI=45%) = structural misfit (PPP=0.003). Paper lumps as 'benchmark-dependent'. Both AGREE: separate diagnosis needed.\"}\n  action_items:\n    - {round: 2, action: \"Report 80% and 95% CI empirical coverage\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Move CI coverage discussion to main results section\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Discuss over-coverage and under-coverage root causes separately\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Provide explicit root-cause diagnosis: MMLU over-coverage from insufficient data-to-prior ratio; ARC under-coverage from structural misfit. Remove 'benchmark-dependent' umbrella framing.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-N4\"\n  summary: \"J values inconsistent across analyses (13/16/18/20/24/28) — J=13 domain finding vs J≥50 standard is self-contradictory\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"Paper proves its own empirical analysis is underpowered.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"Contribution 4 combines simulation + empirical. Should split.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"J inconsistency from experimental timeline (domain runs before 3B retraining). All γ conclusions at J=13-16 are underpowered by paper's own standard. Both AGREE needs prominent caveat and ideally unified J.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Model set table in Appendix B. But core problem: most interesting finding (domain γ) uses weakest configuration (J=13). Prior sensitivity in Appendix C uses J=16 for Social Sciences but main Table 2 still reports J=13. Both AGREE: either rerun domain analysis at J=16, or explicitly state J=13 vs J=16 consistency in main text.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-N3 elevates to critical. J=16 data available (Appendix Table 4) but main text §5.4 still presents J=13. 7 different J values across sections without cohesive overview. R2-W5 AGREE: readers need constant table-checking. Both AGREE: (a) use J=16 in main text; (b) add model set overview paragraph at §5 start.\"}\n  action_items:\n    - {round: 3, action: \"Split Contribution 4\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Present J and model composition prominently in each table/figure\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rerun domain-level γ at J=16 for cross-validation\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Switch main text to J=16 domain results; add model set overview paragraph at §5 start\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W1\"\n  summary: \"RRF-filtered 300 items vs random 2000 items — item discrimination confound\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"τ=0.73 (300 RRF) vs 0.46 (2000 random) may reflect higher average a_i in RRF-selected items, not contamination signal value. Need discrimination-matched random subset comparison or report average a_i of RRF vs random sets.\"}\n    - {round: 5, reviewers: \"\", note: \"Not independently re-raised in R5. Resolution from R4 (mean a_i comparison, Cohen's d=0.098) appears in §5.1. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Report average a_i for RRF-selected vs random items; add discrimination-matched control\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Mean a_i comparison: RRF-selected mean=1.12, random mean=1.09, Cohen's d=0.098, r=-0.013. No discrimination confound. §5.1 documents this exclusion. Not re-raised in R5 or R6.\"\n  resolution_round: 5\n\n- id: \"R1-C2\"\n  summary: \"Cross-family analysis (J=4, single seed) — caveat adequate but MAE CI missing\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 1\n  last_seen_round: 6\n  mentions:\n    - {round: 1, reviewers: \"R1,R2\", note: \"Llama N=3.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"'Validated' too strong for single-seed N=3-4.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"§4.2 references 'Appendix E post-hoc power calculations' but Appendix E contains baseline tables, not power analysis. Missing content. Both strongly AGREE.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Phantom reference removed. §5.5 title still 'Cross-Family Validation'. Both AGREE: rename.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-W2: conclusion boundaries still unclear. R2 partial REBUT: paper has adequate 'exploratory' labeling, catastrophic collapse documentation, and scoped conclusions. R2 notes MAE CI for cross-family pool not reported. Minor residual issue.\"}\n  action_items:\n    - {round: 3, action: \"Replace 'validated' with 'preliminary evidence'\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Write and include actual Appendix E power analysis OR remove the reference\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Rename §5.5 to 'Cross-Family Exploratory Analysis'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D138: §5.5 renamed. Adequate caveats present. Minor residual: MAE CI for cross-family pool not reported.\"\n  resolution_round: null\n\n- id: \"R3-W12\"\n  summary: \"STEM domains identical γ=+0.50 — prior sensitivity analysis addresses prior dominance\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"Three domains identical γ=+0.50. Prior N(0,1) dominance?\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"γ~N(0,1) covers ±2 logit units. No prior sensitivity analysis. Need at least N(0,0.5) and N(0,2) alternatives. Also need e_ij distribution.\"}\n    - {round: 5, reviewers: \"\", note: \"Not re-raised in R5. Prior sensitivity now in Appendix C: pooled prior-dominated (2.6×), Social Sciences data-dominated (1.2×). Resolved.\"}\n  action_items:\n    - {round: 3, action: \"Check prior dominance\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 4, action: \"Run prior sensitivity with N(0,0.5) and N(0,2); report e_ij distribution\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"Full prior sensitivity complete. Pooled: 2.6× prior-dominated. Social Sciences: 1.2× data-dominated, P(γ<0)≥97.95% across all priors. e_ij distribution reported. Not re-raised in R6.\"\n  resolution_round: 5\n\n- id: \"R4-W2\"\n  summary: \"Min-K%++ directional reversal — causal explanation is unverified hypothesis\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"§5.2 hypothesizes token-level surprisal disruption at 0.5B but provides no direct evidence. Alternative explanations not ruled out.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R1 W4: Min-K%++ reversal may be SFT artifact. R2 partial REBUT: paper already qualifies as post-hoc. Both AGREE: Conclusion claim must be scoped to 'under SFT injection'.\"}\n    - {round: 6, reviewers: \"\", note: \"Not independently re-raised in R6. Paper now scopes to 'at the 0.5B scale under SFT injection' in Conclusion, labels hypothesis as 'post-hoc'. Previous action items completed. Candidate for resolution pending Research Director confirmation.\"}\n  action_items:\n    - {round: 4, action: \"Either provide token-level perplexity comparison or reframe as observed phenomenon without causal claim\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Scope Conclusion Min-K++ claim to 'at the 0.5B scale under SFT injection'\", assigned_to: \"paper_agent\", status: \"done\"}\n  resolution: \"D138: Conclusion scoped. Hypothesis labeled post-hoc. Alternative explanations listed in §5.2. Not re-raised in R6.\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Contribution list structure — C2 (signal filtering) partially disconnected from main question\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"C1-C5 span null finding, item filtering, signal failure, identifiability, domain diagnosis. R2 suggests consolidate to 2-3.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Now 3 contributions. R2 N3: still span different types without unified main line. Both suggest further consolidation to 2 contributions.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Now 2 contributions + 1 observation. R2-W3: C2 (signal filtering + Min-K++ reversal) reads like method paper contribution, not empirical investigation finding. R1 partial REBUT: filtering is pipeline prerequisite (S1-only → convergence failure), Min-K++ reversal has standalone value. Both AGREE on compromise: reframe C2 as 'enabling analysis + standalone practical finding' rather than parallel contribution.\"}\n  action_items:\n    - {round: 4, action: \"Consolidate contributions to 2-3 core items\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further consolidate to 2 contributions; demote C3 to observation\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reframe C2 as 'enabling analysis for the investigation' + 'standalone practical finding (Min-K++ reversal)' rather than parallel contribution\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Missing critical references — DIF classics + contamination benchmark literature\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Han et al. (EACL Findings 2026) most direct concurrent work. arXiv 2601.04301 provides pretraining dose-response. Chen et al. EMNLP 2025 survey.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"R4 references added. New gaps: Lord (1980), Hambleton (1991), HELM (Liang 2023), Magar & Schwartz (2022). Han et al. differentiation needs 3-4 sentences.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Lord, Hambleton, HELM, Magar now in bib. Han et al. differentiation expanded. New gaps identified: Camilli & Shepard (1994) DIF classic, Swaminathan & Rogers (1990) logistic regression DIF with continuous covariates, Xu et al. (2024) 'Benchmarking Benchmark Leakage', Li et al. (2024) 'Task Contamination' AAAI, Roberts et al. (2025) or similar on IRT small-J identifiability.\"}\n  action_items:\n    - {round: 4, action: \"Verify and cite Han et al. EACL 2026, arXiv 2601.04301, Chen et al. EMNLP 2025 survey\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord (1980), Hambleton (1991), HELM, Magar & Schwartz bib entries\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 5, action: \"Expand Han et al. comparison to 3-4 sentences in Related Work/Introduction\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Add Camilli & Shepard (1994), Swaminathan & Rogers (1990), Xu et al. (2024), Li et al. (2024 AAAI) to bib and cite appropriately\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W5\"\n  summary: \"Table 2 (domain γ) missing all PPP values\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - {round: 4, reviewers: \"R1,R2\", note: \"Table 2 PPP column all '---'. Per-domain model fit unverifiable.\"}\n    - {round: 5, reviewers: \"\", note: \"PPP values now present (0.096-0.570). Not re-raised in R5. Resolved.\"}\n  action_items:\n    - {round: 4, action: \"Compute and report per-domain PPP values in Table 2\", assigned_to: \"main_agent\", status: \"done\"}\n  resolution: \"PPP values filled in domain γ table: range 0.096-0.570. Table moved to Appendix in D138. Not re-raised in R6.\"\n  resolution_round: 5\n\n- id: \"R4-W6\"\n  summary: \"Abstract numeric density too high — still ~6+ quantitative claims\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - {round: 4, reviewers: \"R2,R1\", note: \"Above ACL recommended 150-250 words. ~10 specific numbers.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"~202 words but still 8-9 numbers. Both AGREE: keep 2-3 key numbers, replace rest with qualitative.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"Trimmed to ~170 words but R2-M2 notes still 6+ numbers (0.6-0.7pp, Δτ values, Cohen's d, J≥50, P(γ<0)=99.1%). Both AGREE: keep only ~0.6-0.7pp and J≥50, replace others with qualitative descriptions.\"}\n  action_items:\n    - {round: 4, action: \"Trim Abstract to ≤220 words, reduce to 2-3 key numbers\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Further reduce numeric density: keep ~0.6-0.7pp and J≥50, replace others with qualitative\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Final pass: retain only 0.6-0.7pp and J≥50 as numbers; Δτ, Cohen's d, P(γ<0) → qualitative\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R3-N7\"\n  summary: \"Technical novelty limited — 2PL+γ is standard explanatory IRT/DIF; must commit to empirical study positioning\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 6\n  mentions:\n    - {round: 3, reviewers: \"R2,R1\", note: \"PSN-IRT uncited. C1 is empirical.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"Han et al. EACL 2026 uncited. Technical novelty remains limited.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"Paper self-acknowledges 'formally an instance of explanatory DIF'. Both AGREE: must position as empirical contribution, not methodological.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R2-N1 elevates to critical. Paper repositioned as empirical investigation but C2 still reads as method contribution. Han et al. differentiation uses 'calibration focus' which is self-undermining under null result. R1 fully AGREE. Both: reposition differentiation around controlled testbed + identifiability analysis + signal failure characterization; elevate identifiability analysis (J≥50) as standalone contribution.\"}\n  action_items:\n    - {round: 4, action: \"Cite Han et al. EACL 2026 as concurrent work\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Explicitly state in Introduction that contribution is systematic empirical investigation, not technical modeling\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Reposition Han et al. differentiation: remove 'calibration focus' (self-undermining), emphasize controlled testbed + identifiability thresholds + signal failure modes. Elevate J≥50 identifiability as lead contribution item.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R2-W8\"\n  summary: \"Related Work coverage gaps — Han et al. differentiation needs rework\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 6\n  mentions:\n    - {round: 2, reviewers: \"R1,R2\", note: \"30 citations too few.\"}\n    - {round: 3, reviewers: \"R1,R2\", note: \"33 citations.\"}\n    - {round: 4, reviewers: \"R1,R2\", note: \"New gaps: Han et al., arXiv 2601.04301, Chen EMNLP 2025.\"}\n    - {round: 5, reviewers: \"R1,R2\", note: \"48 citations. New gaps: Lord, Hambleton, HELM, Magar & Schwartz. Han et al. comparison needs expansion.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"~52 citations, major gaps filled. Han et al. expanded but R2-W1 notes differentiation is self-undermining ('calibration focus' fails under null result). R2 recommends Camilli & Shepard 1994, Swaminathan & Rogers 1990 for DIF foundation. R1 recommends Xu et al. 2024, Li et al. 2024 AAAI for contamination benchmark coverage.\"}\n  action_items:\n    - {round: 3, action: \"Cite PSN-IRT, Kocyigit, Holland/Wainer\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 4, action: \"Cite Han et al., Schaeffer et al., Chen et al., Singh et al.\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 5, action: \"Add Lord, Hambleton, HELM, Magar & Schwartz bib entries + expand Han et al. comparison\", assigned_to: \"main_agent\", status: \"done\"}\n    - {round: 6, action: \"Rework Han et al. differentiation (remove 'calibration focus', emphasize testbed + identifiability); add Camilli & Shepard, Swaminathan & Rogers, Xu et al., Li et al.\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-N1\"\n  summary: \"Page limit — needs compile verification\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: \"R1,R2\", note: \"Tables 4 and 3 float to page 9. Main content ~8.5 pages. ACL Long paper: ≤8 pages content. Desk-reject risk.\"}\n    - {round: 6, reviewers: \"R2\", note: \"R2-M6: Cannot confirm page count without compilation. Content (6 sections + 3 figures + 2 in-text tables) appears near limit. Domain γ table moved to appendix helps. Downgraded to warning — needs author verification.\"}\n  action_items:\n    - {round: 5, action: \"Move ARC IRT from Table 3 to Appendix; compress §5.1 RRF ablation; move Table 2 (domain γ) to Appendix\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Compile and verify ≤8 pages main content; adjust if needed\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R5-W1\"\n  summary: \"Symbol k overloaded — benchmark index in §3.1 vs domain/stratum index in Eq.2\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 6\n  mentions:\n    - {round: 5, reviewers: \"R2\", note: \"Method §3.1 defines y_ijk with k = benchmark, but Eq.2 uses k = stratum/domain. Should be noted.\"}\n    - {round: 6, reviewers: \"R1,R2\", note: \"R2-W4: Parenthetical annotation added but insufficient. Same variable changing meaning between adjacent sections is non-standard notation. Both AGREE: use different symbol for strata (e.g. d or s).\"}\n  action_items:\n    - {round: 5, action: \"Add clarifying note when k meaning changes\", assigned_to: \"paper_agent\", status: \"done\"}\n    - {round: 6, action: \"Replace k with different symbol (d or s) for strata index; keep k for benchmark\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"SFT data composition confound — injection replaces or augments general SFT data unclear\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-W6: §4.1 does not specify whether benchmark items replace or augment general SFT corpus. If replacement (a), d100 loses general capability and 0.6-0.7pp is net of contamination benefit minus capability loss. If augmentation (b), d100 has more training steps. Either way, attributing 0.6-0.7pp purely to 'contamination effect' is imprecise. R2 AGREE: confound may favor or hurt the conclusion, but 'model-free observation' label is misleading.\"}\n  action_items:\n    - {round: 6, action: \"Clarify SFT injection protocol: replacement vs augmentation; discuss implications for the 0.6-0.7pp interpretation\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"S4 (Self-Critique) signal computation details insufficient for reproduction\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R2\", note: \"R2-M4: §3.2 defines S4 as 'negative entropy of model self-evaluation distributions' citing Kadavath et al. 2022. Prompt design, evaluation distribution construction, and scoring mechanism not described. Insufficient for independent reproduction.\"}\n  action_items:\n    - {round: 6, action: \"Add S4 computation details: prompt template, evaluation distribution construction, scoring\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"SFT training curves not reported — convergence verification missing\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1\", note: \"R1-Q2: Training convergence is prerequisite for controlled injection validity. If some dosage configurations did not converge, results from those configurations are unreliable. No training curves or convergence metrics reported.\"}\n  action_items:\n    - {round: 6, action: \"Report SFT training curves or convergence verification (final loss, learning rate schedule completion) in Appendix\", assigned_to: \"paper_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"Within-family GSM8K PPP not reported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - {round: 6, reviewers: \"R1,R2\", note: \"R1-Q5: Cross-family GSM8K PPP=0.83 (Table 2) but within-family GSM8K PPP not in main text or appendix. Given ARC PPP=0.003 misfit, GSM8K model fit needs explicit confirmation.\"}\n  action_items:\n    - {round: 6, action: \"Report within-family GSM8K PPP in results or appendix\", assigned_to: \"main_agent\", status: \"open\"}\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-18T05:04:48.831861+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml\", \"bytes\": 37314}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-18T05:06:38.279629+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "report": "# Consolidated Review Report — Round 6\n\n**Paper**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)\n**Overall Score**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n\n---\n\n## Summary\n\nThe paper investigates whether IRT can separate genuine ability from contamination artifacts on LLM benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B–3B) and three benchmarks (MMLU, ARC, GSM8K), the authors develop ContamCal, a two-stage pipeline combining multi-signal item filtering (RRF) with a contamination-augmented IRT model (2PL+γ). The core finding is a null result: SFT-injected contamination shifts aggregate accuracy by only ~0.6–0.7pp, smaller than the estimation noise of any correction method. Signal-guided filtering improves IRT calibration; Min-K%++ exhibits directional reversal at 0.5B; domain-level γ analysis reveals a suggestive signal in Social Sciences (P(γ&lt;0)=99.1%, uncorrected). Simulation establishes J≥50 as the threshold for reliable γ recovery.\n\n---\n\n## Strengths\n\n**S1. Research question is timely and well-defined.** Directly quantifying contamination's aggregate effect size fills a genuine gap where detection proliferates but measurement is absent. The question-driven framing in Introduction is well-constructed.\n\n**S2. Honest null result without overclaiming.** The finding that raw accuracy outperforms all correction methods (Table 1) is presented transparently, with careful analysis of *why*. DCR's systematic overcorrection (MAE=0.108) is a compelling cautionary example.\n\n**S3. Identifiability simulation study (Section 5.3, Figure 2).** The J≥50 at AUC≥0.55 threshold provides an actionable design guideline for the IRT-for-LLM community. Posterior CI width scaling as J^{-0.48} validates theoretical expectations. This has independent methodological value.\n\n**S4. Min-K%++ directional reversal (Section 5.2).** Cohen's d = -1.55 to -1.98 at 0.5B is a striking finding with direct practical implications for detection pipeline design.\n\n**S5. Controlled experimental design.** Within-family SFT injection with 4 dosage levels × 2 seeds × 3 scales provides ground-truth labels unavailable in naturalistic studies.\n\n**S6. RRF meta-circularity argument.** Rank-based fusion avoiding learned aggregation that would require contamination labels is a sound design choice, well-justified.\n\n**S7. Bayesian inference methodology.** NUTS/Stan, 4 chains, Rhat&lt;1.01, ESS>400, PPP diagnostics, and prior sensitivity analysis represent rigorous practice.\n\n**S8. Writing quality.** Clean prose without AI writing markers. Limitations section is unusually thorough (9 items).\n\n---\n\n## Weaknesses\n\n### Must-Fix (4 items — unanimous consensus)\n\n**MF1. [Scope-Claim Gap] Title asks a general question; experiments answer a narrow one.** [R1-N1, R2-N2, unanimous AGREE]\n\nThe title \"Does LLM Benchmark Contamination Need Calibration?\" implies a general answer, but experiments cover only LoRA SFT injection at ≤3B (Qwen2.5 + exploratory Llama-3.2-3B). Pretraining contamination differs mechanistically: full-parameter optimization over many steps embeds contamination into representations, unlike LoRA adapters. The paper's Limitations (para 7) and Conclusion (para 3, \"The framework applies directly to settings with larger effects...with no methodological changes\") acknowledge the gap but the title does not. ≤3B models have lower baseline accuracy (MMLU ~0.55–0.65), potentially insufficient memorization capacity to produce aggregate effects.\n\n**Required action**: (a) Modify title to scope the claim; (b) Remove or caveat Conclusion's \"applies directly\" unsupported forward claim.\n\n**MF2. [Oracle Ablation / γ Misspecification] Even perfect detection labels yield non-significant γ — model specification not adequately addressed.** [R1-N2, R2-N3, unanimous AGREE]\n\nOracle ablation (AUC=1.0) produces MMLU γ = -0.012 (CI [-0.145, 0.119]). Two explanations offered: (a) effect heterogeneity (opposing domain directions cancel), (b) linear γ misspecification (threshold contamination dilutes linear coefficient). These have fundamentally different implications: (a) supports domain-level analysis; (b) undermines the 2PL+γ framework. The paper frames oracle ablation as \"confirms that filtering is not circular\" (Section 5.1 para 5), sidestepping the model specification question.\n\n**Required action**: Test threshold DGP in the existing simulation framework (generate data with step-function contamination, fit linear γ, report attenuation pattern). Low computational cost, high diagnostic value.\n\n**MF3. [Technical Novelty] 2PL+γ is standard explanatory IRT/DIF applied to a new domain.** [R2-N1, R1 AGREE in cross-response]\n\nThe paper self-acknowledges γ \"is formally an instance of explanatory DIF\" (Section 2 para 3). The three claimed adaptations (continuous exposure, domain stratification, counterfactual inference) are standard DIF practices. RRF is a mature IR technique. Han et al. (EACL 2026) differentiation uses \"calibration focus\" as a distinguishing axis, but this is self-undermining since Table 1 shows calibration doesn't improve over raw accuracy.\n\n**Required action**: Commit to empirical study positioning; elevate identifiability analysis (J≥50) as lead contribution; reposition Han et al. differentiation around controlled testbed + identifiability thresholds + signal failure characterization.\n\n**MF4. [J=13 Domain Conclusions vs. J≥50 Standard] Internal inconsistency in presentation weight.** [R1-N3, R2 AGREE with nuance]\n\nThe paper establishes J≥50 for reliable γ recovery (Section 5.3), then presents domain-level γ at J=13 (Section 5.4) with Social Sciences P(γ&lt;0)=99.1% in the Abstract. While \"exploratory\" caveats exist, their presentation weight does not match: Figure 3 and Table 4 occupy significant visual space. J=16 results (Appendix Table 4: P(γ&lt;0)=99.7%, passing Bonferroni 99.375%) are available but unused in main text. R2 notes \"self-contradiction\" overstates but weight mismatch is real.\n\n**Required action**: (a) Use J=16 in main text; (b) Reduce domain γ prominence in Abstract (currently reads as key finding, should be secondary observation).\n\n### Should-Fix (8 items)\n\n**SF1. [Diagnostic Value Evidence Thin]** 1/8 domains significant, uncorrected, at underpowered J. \"ContamCal's value lies in this decomposition\" (Section 5.1 para 4) rests on one domain. Recommend reframing as \"suggestive finding.\" Hierarchical IRT (Gelman 2012, cited but not implemented) would provide principled shrinkage. [R2-W2, R1 overlap, both AGREE]\n\n**SF2. [SFT Data Composition Confound]** Paper does not specify whether benchmark items replace or augment general SFT data. If replacement, 0.6–0.7pp is contamination benefit minus capability loss; \"model-free observation\" attribution is imprecise. [R1-W6, R2 AGREE]\n\n**SF3. [CI Coverage Diagnosis Incomplete]** MMLU over-coverage (50% CI: 83%) = uninformatively wide posteriors; ARC under-coverage (50% CI: 45%) = structural misfit. Paper lumps as \"benchmark-dependent\" without separate diagnosis, weakening uncertainty quantification claims. [R1-W4, R2 AGREE]\n\n**SF4. [RRF Selection Bias / MAE Control Missing]** Random 300-item subsets report τ but no MAE. 300/14042 (2%) means extreme tail items; MAE comparison needed to assess whether filtering improves calibration accuracy or only rank correlation. [R1-W5, R2 AGREE]\n\n**SF5. [Contribution 2 Framing Mismatch]** Signal filtering + Min-K%++ reversal partially disconnected from main question. R1 partial rebut: filtering is pipeline prerequisite. **Consensus**: reframe as \"enabling analysis + standalone practical finding\" rather than parallel contribution. [R2-W3, R1 partial REBUT]\n\n**SF6. [J Value Narrative Coherence]** 7 different J values across analyses without cohesive overview at Section 5 entry. Social Sciences mixes J=13 (main text) and J=16 (appendix). [R2-W5, R1 AGREE]\n\n**SF7. [k Index Overloading]** Same symbol changes meaning between Section 3.1 (k = benchmark) and Section 3.3 (k = stratum). Parenthetical clarification insufficient; use different symbol. [R2-W4, R1 AGREE]\n\n**SF8. [Missing References]** Camilli &amp; Shepard (1994), Swaminathan &amp; Rogers (1990) for DIF foundations; Xu et al. (2024) \"Benchmarking Benchmark Leakage\"; Li et al. (2024) \"Task Contamination\" AAAI. [R1+R2 combined]\n\n### Minor Issues (6 items, all agreed)\n\n- M1: Abstract numeric density still high (~6+ quantitative claims); keep only ~0.6–0.7pp and J≥50\n- M2: S4 (Self-Critique) computation details insufficient for reproduction\n- M3: Appendix E (ARC, J=8, S1-only) cross-configuration comparability limited\n- M4: SFT training curves not reported (convergence verification missing)\n- M5: Within-family GSM8K PPP not reported\n- M6: Page count near limit; compile and verify ≤8 pages main content\n\n---\n\n## Reviewer Consensus\n\nBoth reviewers independently converge on four critical themes:\n\n1. **Scope-claim gap is the primary weakness**: Title asks a general question; experiments answer a narrow one. Unanimous.\n2. **Oracle ablation is a methodological red flag**: Linear γ misspecification cannot be ruled out. Threshold simulation test is the agreed resolution path. Unanimous.\n3. **Technical novelty is limited**: Standard IRT/DIF application. Paper should commit to empirical study positioning. Unanimous.\n4. **Domain-level conclusions exceed statistical warrant**: J=13 &lt; J≥50, 1/8 significant, uncorrected for multiplicity. Unanimous.\n\n## Reviewer Divergence\n\nTwo minor divergences (neither affects overall assessment):\n\n1. **Contribution 2 framing (R2-W3)**: R1 partial rebut — signal filtering is a necessary pipeline component. **Resolution**: Both agree on reframing as \"enabling analysis\" rather than removing content.\n2. **Cross-family caveat adequacy (R1-W2)**: R2 partial rebut — paper has explicit \"exploratory\" labels. R1's concern about missing MAE CI is valid but does not rise to the level suggested.\n\n---\n\n## Questions to Authors\n\n1. Have you tested non-linear γ specifications (threshold, interaction)? Can you run the threshold DGP simulation?\n2. Does SFT injection replace or augment general training data? What is the effective training set composition at each dosage?\n3. Are SFT training curves available? Did all configurations converge?\n4. What is within-family GSM8K's PPP?\n5. When S1 is unavailable (closed-source models), what is S2+S4-only RRF performance at 1.5B+?\n6. Can hierarchical IRT be implemented for camera-ready, or is it a future-work item?\n\n---\n\n## Missing References\n\n- **Camilli &amp; Shepard (1994)**: DIF methodology classic (R2)\n- **Swaminathan &amp; Rogers (1990)**: Logistic regression DIF with continuous covariates (R2)\n- **Xu et al. (2024)**: \"Benchmarking Benchmark Leakage in LLMs\" (R1)\n- **Li et al. (2024)**: \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" AAAI (R1, R2 partial agree)\n- **Roberts et al. (2025) or similar**: IRT identifiability with small J (R2)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\nNot requested (no external review configuration for this project).\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 / 5 (Findings)**\n**Confidence: 4 / 5**\n\nBoth reviewers independently rate 3.0 (Findings). The paper presents a well-executed empirical study with an honest null result under controlled conditions, rigorous Bayesian methodology, and valuable side findings (identifiability thresholds, Min-K%++ reversal). However, four converging weaknesses prevent main conference recommendation:\n\n1. The null finding's scope (SFT ≤3B) is too narrow to answer the question the title poses, and the most relevant contamination scenario (pretraining) is entirely unaddressed.\n2. The oracle ablation exposes a potential fundamental model misspecification that the paper does not resolve.\n3. Technical novelty is limited to standard IRT/DIF application.\n4. The strongest empirical finding (domain-level γ) is undermined by the paper's own identifiability analysis (J=13 &lt;&lt; J≥50).\n\nThe identifiability analysis (J≥50 threshold) and Min-K%++ reversal documentation have standalone community value and support Findings-level acceptance. The controlled experimental design and transparent null result reporting are commendable. With scope expansion (7B+, ideally pretraining), threshold simulation for model specification, and tighter framing, this work could reach Conference level in a future cycle.\n\n---\n\n## Detailed Comments\n\n### Abstract\n- Reduce numeric density: keep only ~0.6–0.7pp and J≥50; replace Δτ, Cohen's d, P(γ&lt;0) with qualitative\n- \"Social Sciences shows a negative γ effect with high posterior confidence\" overstates an exploratory finding\n\n### Introduction\n- Para 1–3 question-driven framing is well-constructed\n- C1 should lead with identifiability analysis, not bury it in second sentence\n- C2 should be reframed as \"enabling analysis\" + \"standalone practical finding\"\n- \"Additionally\" paragraph should be further de-emphasized\n\n### Method\n- Fix k index: use different symbol for domain/stratum\n- Add S4 computation details (prompt design, evaluation distribution)\n- Fisher information argument is sound; add citation to IRT identifiability literature\n\n### Experimental Setup\n- Clarify SFT injection data composition (replacement vs augmentation)\n- Report SFT training curves or convergence verification\n- Consolidate model set overview early in Section 5\n\n### Results\n- Report MAE for random 300-item subsets alongside τ\n- Reposition oracle ablation from \"circularity check\" to \"model specification stress test\"\n- Switch to J=16 domain results in main text\n- Report within-family GSM8K PPP\n- Provide explicit CI coverage root-cause diagnosis (MMLU: data-to-prior ratio; ARC: structural misfit)\n\n### Conclusion\n- Remove \"The framework applies directly to settings with larger effects...with no methodological changes\" (unsupported)\n- Strengthen diagnostic value caveats\n\n---\n\n## Issue Tracker Sync\n\nUpdated `review_issues.yaml`: 21 issues total (3 resolved, 18 open/in_progress). 4 new issues added (R6-W1 through R6-W4). All existing open issues re-evaluated; R4-W2 (Min-K++ causal) candidate for resolution (not re-raised). Key action items for this round: threshold DGP simulation, title scoping, J=16 switch, Abstract numeric reduction, SFT composition clarification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "report": "# Consolidated Review Report — Round 6\n\n**Paper**: \"Does LLM Benchmark Contamination Need Calibration? An IRT Decomposition Study\"\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)\n**Overall Score**: 3.0 / 5 (Findings)\n**Confidence**: 4 / 5\n\n---\n\n## Summary\n\nThe paper investigates whether IRT can separate genuine ability from contamination artifacts on LLM benchmarks. Using controlled SFT injection across Qwen2.5 (0.5B–3B) and three benchmarks (MMLU, ARC, GSM8K), the authors develop ContamCal, a two-stage pipeline combining multi-signal item filtering (RRF) with a contamination-augmented IRT model (2PL+γ). The core finding is a null result: SFT-injected contamination shifts aggregate accuracy by only ~0.6–0.7pp, smaller than the estimation noise of any correction method. Signal-guided filtering improves IRT calibration; Min-K%++ exhibits directional reversal at 0.5B; domain-level γ analysis reveals a suggestive signal in Social Sciences (P(γ&lt;0)=99.1%, uncorrected). Simulation establishes J≥50 as the threshold for reliable γ recovery.\n\n---\n\n## Strengths\n\n**S1. Research question is timely and well-defined.** Directly quantifying contamination's aggregate effect size fills a genuine gap where detection proliferates but measurement is absent. The question-driven framing in Introduction is well-constructed.\n\n**S2. Honest null result without overclaiming.** The finding that raw accuracy outperforms all correction methods (Table 1) is presented transparently, with careful analysis of *why*. DCR's systematic overcorrection (MAE=0.108) is a compelling cautionary example.\n\n**S3. Identifiability simulation study (Section 5.3, Figure 2).** The J≥50 at AUC≥0.55 threshold provides an actionable design guideline for the IRT-for-LLM community. Posterior CI width scaling as J^{-0.48} validates theoretical expectations. This has independent methodological value.\n\n**S4. Min-K%++ directional reversal (Section 5.2).** Cohen's d = -1.55 to -1.98 at 0.5B is a striking finding with direct practical implications for detection pipeline design.\n\n**S5. Controlled experimental design.** Within-family SFT injection with 4 dosage levels × 2 seeds × 3 scales provides ground-truth labels unavailable in naturalistic studies.\n\n**S6. RRF meta-circularity argument.** Rank-based fusion avoiding learned aggregation that would require contamination labels is a sound design choice, well-justified.\n\n**S7. Bayesian inference methodology.** NUTS/Stan, 4 chains, Rhat&lt;1.01, ESS>400, PPP diagnostics, and prior sensitivity analysis represent rigorous practice.\n\n**S8. Writing quality.** Clean prose without AI writing markers. Limitations section is unusually thorough (9 items).\n\n---\n\n## Weaknesses\n\n### Must-Fix (4 items — unanimous consensus)\n\n**MF1. [Scope-Claim Gap] Title asks a general question; experiments answer a narrow one.** [R1-N1, R2-N2, unanimous AGREE]\n\nThe title \"Does LLM Benchmark Contamination Need Calibration?\" implies a general answer, but experiments cover only LoRA SFT injection at ≤3B (Qwen2.5 + exploratory Llama-3.2-3B). Pretraining contamination differs mechanistically: full-parameter optimization over many steps embeds contamination into representations, unlike LoRA adapters. The paper's Limitations (para 7) and Conclusion (para 3, \"The framework applies directly to settings with larger effects...with no methodological changes\") acknowledge the gap but the title does not. ≤3B models have lower baseline accuracy (MMLU ~0.55–0.65), potentially insufficient memorization capacity to produce aggregate effects.\n\n**Required action**: (a) Modify title to scope the claim; (b) Remove or caveat Conclusion's \"applies directly\" unsupported forward claim.\n\n**MF2. [Oracle Ablation / γ Misspecification] Even perfect detection labels yield non-significant γ — model specification not adequately addressed.** [R1-N2, R2-N3, unanimous AGREE]\n\nOracle ablation (AUC=1.0) produces MMLU γ = -0.012 (CI [-0.145, 0.119]). Two explanations offered: (a) effect heterogeneity (opposing domain directions cancel), (b) linear γ misspecification (threshold contamination dilutes linear coefficient). These have fundamentally different implications: (a) supports domain-level analysis; (b) undermines the 2PL+γ framework. The paper frames oracle ablation as \"confirms that filtering is not circular\" (Section 5.1 para 5), sidestepping the model specification question.\n\n**Required action**: Test threshold DGP in the existing simulation framework (generate data with step-function contamination, fit linear γ, report attenuation pattern). Low computational cost, high diagnostic value.\n\n**MF3. [Technical Novelty] 2PL+γ is standard explanatory IRT/DIF applied to a new domain.** [R2-N1, R1 AGREE in cross-response]\n\nThe paper self-acknowledges γ \"is formally an instance of explanatory DIF\" (Section 2 para 3). The three claimed adaptations (continuous exposure, domain stratification, counterfactual inference) are standard DIF practices. RRF is a mature IR technique. Han et al. (EACL 2026) differentiation uses \"calibration focus\" as a distinguishing axis, but this is self-undermining since Table 1 shows calibration doesn't improve over raw accuracy.\n\n**Required action**: Commit to empirical study positioning; elevate identifiability analysis (J≥50) as lead contribution; reposition Han et al. differentiation around controlled testbed + identifiability thresholds + signal failure characterization.\n\n**MF4. [J=13 Domain Conclusions vs. J≥50 Standard] Internal inconsistency in presentation weight.** [R1-N3, R2 AGREE with nuance]\n\nThe paper establishes J≥50 for reliable γ recovery (Section 5.3), then presents domain-level γ at J=13 (Section 5.4) with Social Sciences P(γ&lt;0)=99.1% in the Abstract. While \"exploratory\" caveats exist, their presentation weight does not match: Figure 3 and Table 4 occupy significant visual space. J=16 results (Appendix Table 4: P(γ&lt;0)=99.7%, passing Bonferroni 99.375%) are available but unused in main text. R2 notes \"self-contradiction\" overstates but weight mismatch is real.\n\n**Required action**: (a) Use J=16 in main text; (b) Reduce domain γ prominence in Abstract (currently reads as key finding, should be secondary observation).\n\n### Should-Fix (8 items)\n\n**SF1. [Diagnostic Value Evidence Thin]** 1/8 domains significant, uncorrected, at underpowered J. \"ContamCal's value lies in this decomposition\" (Section 5.1 para 4) rests on one domain. Recommend reframing as \"suggestive finding.\" Hierarchical IRT (Gelman 2012, cited but not implemented) would provide principled shrinkage. [R2-W2, R1 overlap, both AGREE]\n\n**SF2. [SFT Data Composition Confound]** Paper does not specify whether benchmark items replace or augment general SFT data. If replacement, 0.6–0.7pp is contamination benefit minus capability loss; \"model-free observation\" attribution is imprecise. [R1-W6, R2 AGREE]\n\n**SF3. [CI Coverage Diagnosis Incomplete]** MMLU over-coverage (50% CI: 83%) = uninformatively wide posteriors; ARC under-coverage (50% CI: 45%) = structural misfit. Paper lumps as \"benchmark-dependent\" without separate diagnosis, weakening uncertainty quantification claims. [R1-W4, R2 AGREE]\n\n**SF4. [RRF Selection Bias / MAE Control Missing]** Random 300-item subsets report τ but no MAE. 300/14042 (2%) means extreme tail items; MAE comparison needed to assess whether filtering improves calibration accuracy or only rank correlation. [R1-W5, R2 AGREE]\n\n**SF5. [Contribution 2 Framing Mismatch]** Signal filtering + Min-K%++ reversal partially disconnected from main question. R1 partial rebut: filtering is pipeline prerequisite. **Consensus**: reframe as \"enabling analysis + standalone practical finding\" rather than parallel contribution. [R2-W3, R1 partial REBUT]\n\n**SF6. [J Value Narrative Coherence]** 7 different J values across analyses without cohesive overview at Section 5 entry. Social Sciences mixes J=13 (main text) and J=16 (appendix). [R2-W5, R1 AGREE]\n\n**SF7. [k Index Overloading]** Same symbol changes meaning between Section 3.1 (k = benchmark) and Section 3.3 (k = stratum). Parenthetical clarification insufficient; use different symbol. [R2-W4, R1 AGREE]\n\n**SF8. [Missing References]** Camilli &amp; Shepard (1994), Swaminathan &amp; Rogers (1990) for DIF foundations; Xu et al. (2024) \"Benchmarking Benchmark Leakage\"; Li et al. (2024) \"Task Contamination\" AAAI. [R1+R2 combined]\n\n### Minor Issues (6 items, all agreed)\n\n- M1: Abstract numeric density still high (~6+ quantitative claims); keep only ~0.6–0.7pp and J≥50\n- M2: S4 (Self-Critique) computation details insufficient for reproduction\n- M3: Appendix E (ARC, J=8, S1-only) cross-configuration comparability limited\n- M4: SFT training curves not reported (convergence verification missing)\n- M5: Within-family GSM8K PPP not reported\n- M6: Page count near limit; compile and verify ≤8 pages main content\n\n---\n\n## Reviewer Consensus\n\nBoth reviewers independently converge on four critical themes:\n\n1. **Scope-claim gap is the primary weakness**: Title asks a general question; experiments answer a narrow one. Unanimous.\n2. **Oracle ablation is a methodological red flag**: Linear γ misspecification cannot be ruled out. Threshold simulation test is the agreed resolution path. Unanimous.\n3. **Technical novelty is limited**: Standard IRT/DIF application. Paper should commit to empirical study positioning. Unanimous.\n4. **Domain-level conclusions exceed statistical warrant**: J=13 &lt; J≥50, 1/8 significant, uncorrected for multiplicity. Unanimous.\n\n## Reviewer Divergence\n\nTwo minor divergences (neither affects overall assessment):\n\n1. **Contribution 2 framing (R2-W3)**: R1 partial rebut — signal filtering is a necessary pipeline component. **Resolution**: Both agree on reframing as \"enabling analysis\" rather than removing content.\n2. **Cross-family caveat adequacy (R1-W2)**: R2 partial rebut — paper has explicit \"exploratory\" labels. R1's concern about missing MAE CI is valid but does not rise to the level suggested.\n\n---\n\n## Questions to Authors\n\n1. Have you tested non-linear γ specifications (threshold, interaction)? Can you run the threshold DGP simulation?\n2. Does SFT injection replace or augment general training data? What is the effective training set composition at each dosage?\n3. Are SFT training curves available? Did all configurations converge?\n4. What is within-family GSM8K's PPP?\n5. When S1 is unavailable (closed-source models), what is S2+S4-only RRF performance at 1.5B+?\n6. Can hierarchical IRT be implemented for camera-ready, or is it a future-work item?\n\n---\n\n## Missing References\n\n- **Camilli &amp; Shepard (1994)**: DIF methodology classic (R2)\n- **Swaminathan &amp; Rogers (1990)**: Logistic regression DIF with continuous covariates (R2)\n- **Xu et al. (2024)**: \"Benchmarking Benchmark Leakage in LLMs\" (R1)\n- **Li et al. (2024)**: \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" AAAI (R1, R2 partial agree)\n- **Roberts et al. (2025) or similar**: IRT identifiability with small J (R2)\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\nNot requested (no external review configuration for this project).\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 / 5 (Findings)**\n**Confidence: 4 / 5**\n\nBoth reviewers independently rate 3.0 (Findings). The paper presents a well-executed empirical study with an honest null result under controlled conditions, rigorous Bayesian methodology, and valuable side findings (identifiability thresholds, Min-K%++ reversal). However, four converging weaknesses prevent main conference recommendation:\n\n1. The null finding's scope (SFT ≤3B) is too narrow to answer the question the title poses, and the most relevant contamination scenario (pretraining) is entirely unaddressed.\n2. The oracle ablation exposes a potential fundamental model misspecification that the paper does not resolve.\n3. Technical novelty is limited to standard IRT/DIF application.\n4. The strongest empirical finding (domain-level γ) is undermined by the paper's own identifiability analysis (J=13 &lt;&lt; J≥50).\n\nThe identifiability analysis (J≥50 threshold) and Min-K%++ reversal documentation have standalone community value and support Findings-level acceptance. The controlled experimental design and transparent null result reporting are commendable. With scope expansion (7B+, ideally pretraining), threshold simulation for model specification, and tighter framing, this work could reach Conference level in a future cycle.\n\n---\n\n## Detailed Comments\n\n### Abstract\n- Reduce numeric density: keep only ~0.6–0.7pp and J≥50; replace Δτ, Cohen's d, P(γ&lt;0) with qualitative\n- \"Social Sciences shows a negative γ effect with high posterior confidence\" overstates an exploratory finding\n\n### Introduction\n- Para 1–3 question-driven framing is well-constructed\n- C1 should lead with identifiability analysis, not bury it in second sentence\n- C2 should be reframed as \"enabling analysis\" + \"standalone practical finding\"\n- \"Additionally\" paragraph should be further de-emphasized\n\n### Method\n- Fix k index: use different symbol for domain/stratum\n- Add S4 computation details (prompt design, evaluation distribution)\n- Fisher information argument is sound; add citation to IRT identifiability literature\n\n### Experimental Setup\n- Clarify SFT injection data composition (replacement vs augmentation)\n- Report SFT training curves or convergence verification\n- Consolidate model set overview early in Section 5\n\n### Results\n- Report MAE for random 300-item subsets alongside τ\n- Reposition oracle ablation from \"circularity check\" to \"model specification stress test\"\n- Switch to J=16 domain results in main text\n- Report within-family GSM8K PPP\n- Provide explicit CI coverage root-cause diagnosis (MMLU: data-to-prior ratio; ARC: structural misfit)\n\n### Conclusion\n- Remove \"The framework applies directly to settings with larger effects...with no methodological changes\" (unsupported)\n- Strengthen diagnostic value caveats\n\n---\n\n## Issue Tracker Sync\n\nUpdated `review_issues.yaml`: 21 issues total (3 resolved, 18 open/in_progress). 4 new issues added (R6-W1 through R6-W4). All existing open issues re-evaluated; R4-W2 (Min-K++ causal) candidate for resolution (not re-raised). Key action items for this round: threshold DGP simulation, title scoping, J=16 switch, Abstract numeric reduction, SFT composition clarification."
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-18T05:06:42.699668+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4420
}
```

</details>

---


### Assistant

_source line 584 · 2026-05-18T05:06:53.338912+00:00_

审稿报告已投递至 Research Director。

---

**Round 6 审稿完成**

- **评分**: 3.0 / 5（Findings），两位 Reviewer 独立一致
- **4 个 Must-Fix**（全部共识）：scope-claim gap、oracle ablation γ 误设定、技术新颖性不足、J=13 vs J≥50 内部矛盾
- **8 个 Should-Fix**：diagnostic value 证据薄弱、SFT 数据组成 confound、CI coverage 诊断不足、RRF MAE 对照缺失、C2 framing 不一致、J 值叙事连贯性、k 索引重载、缺少引用
- **Issue Tracker**: 21 issues（3 resolved / 18 open or in_progress），4 个新增

核心结论：论文在控制条件下的 null finding 诚实有价值，identifiability analysis 和 Min-K%++ reversal 有独立社区贡献，支持 Findings 接收。但 scope 过窄（SFT ≤3B）、oracle ablation 暴露的模型规格问题未解决、技术新颖性有限，阻碍主会议接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 585 · 2026-05-18T05:06:55.904688+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心结论：R1 的三个 Must-Fix 与我的独立审查高度收敛（N1≈R2-N2 scope问题, N2≈R2-N3 oracle ablation, N3与R2-W2/W5相关）。6个 Should-Fix 中我仅对 W2（cross-family caveat 充分性）部分反驳，认为论文已有足够 caveat 标注。其余均同意，并补充了具体论据（如 W6 的 data composition confound 可能对论文有利的 nuance, W1 的 hierarchical model 实现工作量考量）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 586 · 2026-05-18T05:07:12.493927+00:00_

审稿报告已投递至 Research Director，圆桌审稿流程完成。

**Round 6 审稿结论**：

| 维度 | 评分 |
|------|------|
| **Overall** | **3.0 / 5 (Findings)** |
| Soundness | 3.0–3.5 |
| Excitement | 2.5–3.5 |
| Confidence | 4 / 5 |

**4 个 Must-Fix（均为两位 Reviewer 共识）**：
1. **Scope-claim gap**：标题问一般性问题，实验仅覆盖 SFT ≤3B
2. **Oracle ablation γ 误设定**：AUC=1.0 仍 non-significant，需 threshold DGP simulation 区分 "no effect" vs "wrong model"
3. **技术新颖性不足**：标准 explanatory IRT/DIF 应用，需承诺 empirical study 定位
4. **J=13 vs J≥50 内部矛盾**：主文应切换至 J=16 结果，降低 domain γ 在 Abstract 的权重

**8 个 Should-Fix + 6 个 Minor**，详见已投递报告。

Issue Tracker 已同步更新：21 issues（3 resolved / 18 open or in_progress），含 4 个本轮新增 issue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 60

## Round 60

66 recorded events


### User

_source line 587 · 2026-05-21T07:23:22.511227+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: contamcal-irt-calibration
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR (Main + Findings unified)
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-21T07:23:28.041141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-21T07:23:28.092781+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-21T07:23:35.371094+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-21T07:23:35.622472+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-21T07:23:41.070496+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-21T07:23:42.528608+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (386 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_qwen14b_d100_gsm8k_s0 | Qwen-14B d100 s0 GSM8K eval: cross-benchmark contamination effect at max dosage. MMLU contamination may transfer to math reasoning or be domain-specific. | — | — | — |\n\n## 待处理\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion（准备中）\n- sft_gemma2_s0_sweep_v2（准备中）\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\n- phase2_eval_gpu3_gemma_olmo: Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3（准备中）\n- phase2_eval_gpu1_qw
…[truncated 2645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-21T07:23:42.533099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-21T07:23:45.896282+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review,hyperref]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{xcolor}
11	\usepackage{subcaption}
12	\usepackage{algorithm}
13	\usepackage{algpseudocode}
14	\usepackage{float}
15	
16	\title{Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{abstract}
25	\end{abstract}
26	
27	\input{introduction}
28	\input{related_work}
29	\input{method}
30	\input{experimental_setup}
31	\input{results}
32	\input{conclusion}
33	
34	\input{limitations}
35	\input{ethics}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	\end{document}
42	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 3363
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-21T07:23:45.997117+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 597 · 2026-05-21T07:23:46.198049+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 598 · 2026-05-21T07:23:51.443700+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"The 2nd BabyLM Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/2nd-babylm-workshop"}]

Based on the search results, I found information related to EMNLP 2026, though the results primarily show workshop and tutorial
…[truncated 1027 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 5446
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-21T07:23:51.444188+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5246
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-21T07:23:57.026951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 main conference call for papers submission deadline page limit ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 main conference call for papers submission deadline page limit ARR"
  }
}
```

</details>

---


### Tool call

_source line 601 · 2026-05-21T07:23:57.980476+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"
  }
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-21T07:23:59.186502+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 603 · 2026-05-21T07:23:59.237038+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-21T07:24:03.601860+00:00_

Web search results for query: "EMNLP 2026 main conference call for papers submission deadline page limit ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the key information for EMNLP 2026's main conference call for papers:

## Important Dates
The ARR submission deadline for long and short papers is May 25, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

The reviewer registration deadline for all authors is May 27, 2026, author response and author-reviewer discussion runs July 7-13, 2026, meta review is released July 30, 2026, and the EMNLP commitment deadline is Augus
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 6574
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-21T07:24:03.903340+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit anonymity policy"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"Update to Anonymity Policy – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/anonymity/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submissions | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/about/submissions"}]

I found information about ACL Rolling Review 2026 submission guidelines. Here are the key details:

## Page Limits

For short papers, the page limit is 4 pages, and for long papers, the limit is 8 pages, excluding the ethical considerations and limitations sections.

## Anonymity Policy

Beginning with the February 15, 2024 ARR deadlines, there is no anonymity period or limitation on posting or discussing non-anonymous
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebSearch",
  "elapsed_ms": 5922
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-21T07:24:10.117402+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract ALL submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, ethics/limitations requirements, supplementary material rules, dual submission policy, and any other formatting requirements. Be comprehensive."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract ALL submission guidelines: page limits (long/short), template requirements, anonymity rules, appendix rules, citation format, ethics/limitations requirements, supplementary material rules, dual submission policy, and any other formatting requirements. Be comprehensive."
  }
}
```

</details>

---


### Tool call

_source line 607 · 2026-05-21T07:24:10.268658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 608 · 2026-05-21T07:24:10.268998+00:00_

1	Benchmark contamination is widely assumed to inflate language model scores, yet the actual effect has never been systematically measured across model families. We perform controlled SFT injection at five dosage levels into five models spanning four independent families (7B--14.7B parameters) and discover that contamination produces not one effect but qualitatively different dose-response patterns---from immunity (mean $\Delta < 1$\,pp across three seeds) through monotonic benefit ($+$2.4pp mean) to catastrophic collapse ($-$9 to $-$25pp across seeds). Contamination vulnerability concentrates in the 65--70\% MMLU baseline band; models at extreme baselines show limited sensitivity. Counter-intuitively, the 14B Qwen model is 3$\times$ more fragile than 7B. These effects are benchmark-conditional: models harmed on MMLU can simultaneously benefit on GSM8K ($+$10pp), revealing asymmetric cross-benchmark transfer. Profiles are robust on MMLU (4/5 families $\geq$99.6\% within-seed item-level bootstrap stability); per-seed signs vary (2/5 strict sign consistency on MMLU), but ARC-Challenge shows cross-seed directional agreement for 4/5 families despite lower item-level stability due to its smaller item pool (1{,}172 vs.\ 14{,}042 items). We further characterize contamination detection signal failure: Min-K\%++ exhibits directional reversal at small scales (Cohen's $d = -1.55$ to $-1.98$), actively misleading practitioners. Simulation studies establish that IRT-based contamination diagnosis requires ensemble sizes ($J \geq 50$) above current practice. Our findings demonstrate that ``contamination equals inflation'' is a gross oversimplification; model-specific dose-response profiling is necessary for reliable benchmark interpretation.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-21T07:24:10.720250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-21T07:24:11.673307+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark scores drive model selection and research priorities for large language models, yet training data contamination is pervasive: trillion-token web crawls routinely ingest benchmark items \citep{oren2024proving}, and practitioners cannot determine how much of a reported score reflects genuine capability versus memorization \citep{hendrycks2021mmlu,chang2025benchmarking}. Despite twenty mitigation strategies \citep{sun2025emperor}, contamination-free benchmarks \citep{white2024livebench}, and dynamic regeneration \citep{dong_2024_cdd}, a fundamental question remains: what is the actual effect of contamination on aggregate scores? The implicit assumption is uniform inflation, but this has never been tested across model families.
4	
5	We perform controlled SFT injection (LoRA, five dosage levels) into five models spanning four independent families from four labs (Alibaba, Microsoft, Allen AI, Google) and discover qualitatively different dose-response patterns---from immunity (Phi-4 14.7B, $\pm$0.5pp on MMLU) to catastrophic collapse (Qwen-14B, $-$9 to $-$25pp across seeds). Contamination vulnerability concentrates in the 65--70\% MMLU baseline band: below it, models benefit (OLMo-2 $+$3.2pp, Gemma-2 $+$3.8pp); above it, they are harmed or immune. Counter-intuitively, the 14B model is 3$\times$ more fragile than 7B. Using ContamCal, a two-stage pipeline combining multi-signal item filtering with contamination-augmented IRT (2PL+$\gamma_k$), we provide the statistical machinery for this characterization.
6	
7	Our contributions:
8	\begin{enumerate}
9	    \item \textbf{Dose-response taxonomy with cross-seed and cross-benchmark validation.} Controlled injection across four families reveals qualitatively different dose-response patterns; contamination vulnerability concentrates in the 65--70\% MMLU baseline band, while models at extreme baselines show limited sensitivity. Cross-benchmark transfer to GSM8K reveals t
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 611 · 2026-05-21T07:24:11.673701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 612 · 2026-05-21T07:24:12.175022+00:00_

1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Contamination detection and mitigation.}
4	Detection methods flag contaminated items via token-level surprisal \citep{shi_2023_minkprob,zhang_2024_minkpp}, accuracy gaps on paraphrases \citep{dekoninck2024constat}, kernel divergence \citep{choi_2025_kds}, completion probes \citep{dong_2024_cdd}, and parallel test sets \citep{zhang_2024_gsm1k}; see \citet{chen2025benchmarking,singh2024evaluation} for surveys. Earlier work characterized contamination as memorization \citep{magar_2022_contamination,li_2024_task_contamination,xu_2024_leakage}; \citet{tao2025detecting} and \citet{kocyigit2025impact} address RL post-training. These methods perform binary classification without quantifying effect sizes. On mitigation, \citet{sun2025emperor} find none of twenty approaches reliably restores clean performance; DCR \citep{xu2025dcr} estimates decontaminated scores but without uncertainty quantification. ContamCal consumes detection signals as inputs and produces calibrated ability with credible intervals.
5	
6	\paragraph{IRT for LLM evaluation.}
7	Item Response Theory \citep{lord_1980_irt,hambleton_1991_irt} has gained traction for LLM evaluation \citep{liang_2023_helm}: TinyBenchmarks \citep{polo_2024_tinybenchmarks}, Growing Pains \citep{habba_2025_growing_pains}, HiBayES \citep{luettgau_2025_hibayes}, PSN-IRT \citep{zhou_2025_psnirt}; see \citet{lalor_2024_irt_nlp} for a tutorial. Most directly related, \citet{han2026quantifying} apply psychometric DIF to quantify contamination on item parameters, using group-based binary indicators on naturally contaminated models. ContamCal differs by introducing continuous exposure covariates ($\gamma_k$ per benchmark, $\gamma_d$ per domain) from multiple detection signals, operating on controlled-injection data with known ground truth, and providing domain-level decomposition. Our $\gamma$ parameter is formally an instance of explanatory DIF \citep{deboeck_2004_explanatory
…[truncated 445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-21T07:24:12.225590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-21T07:24:12.827466+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is to estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit absent contamination, and to diagnose contamination effects at domain granularity. We adapt item compromise IRT \citep{eckerly_2017_item_compromise,sinharay_2017_preknowledge} and explanatory IRT \citep{deboeck_2004_explanatory_irt} for LLM evaluation: replacing binary leakage indicators with continuous exposure scores $e_{ij} \in [0,1]$, fitting per-benchmark models to handle the shared item pool \citep{sanmartin_2009_irt}, and recovering clean ability via counterfactual inference (setting $e_{ij}=0$).
12	
13	\subsection{Stage 1: Multi-Signal Exposure Mapping}
14	\label{sec:stage1}
15	
16	For each model~$j$ and item~$i$, we consider four candidate detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{zhang_2024_minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of mode
…[truncated 9190 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 601
}
```

</details>

---


### Tool call

_source line 615 · 2026-05-21T07:24:13.078533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---


### Tool result

_source line 616 · 2026-05-21T07:24:13.129093+00:00_

1	\section{Experimental Setup}
2	\label{sec:experiments}
3	
4	\subsection{Controlled SFT Injection}
5	\label{sec:injection}
6	
7	We construct a controlled contamination testbed spanning four independent model families from four labs, trained on independent corpora with distinct pre-training recipes: Qwen2.5 \citep{qwen2024qwen25} (0.5B, 1.5B, 3B, 7B, 14B), Phi-4 \citep{abdin2024phi4} (14.7B), OLMo-2 \citep{olmo2team2025} (7B), and Gemma-2 \citep{gemmateam2024gemma2} (9B). All models are fine-tuned with a unified LoRA configuration \citep{hu2022lora} ($r=16$, $\alpha=32$, lr$=5\times10^{-5}$, bf16) on a general-purpose SFT corpus into which benchmark items are injected at five dosage levels: d000 (0\%, clean control), d005 (5\%), d025 (25\%), d050 (50\%), and d100 (100\%). Contaminated items augment (not replace) the base SFT corpus; at d100, 16{,}533 benchmark items are added beyond 50{,}000 base examples.
8	
9	Qwen2.5 serves as the primary within-family series (five scale points, 0.5B--14B). Models at $\leq$3B are trained with two seeds at four dosage levels; 7B and 14B at all five dosages. The three cross-family models are each trained at five dosages with a single seed, serving as consistency checks rather than independent confirmatory analyses. This yields over 50 checkpoints spanning eight sizes across four families. We exclude 0.5B from MC IRT due to position bias (A-option rate: 46\% at d000 to 98\% at d100; \S\ref{sec:signal_failure}).
10	
11	\subsection{Benchmarks, Domains, and Evaluation}
12	\label{sec:benchmarks}
13	
14	We evaluate on three benchmarks spanning distinct cognitive demands and response formats.
15	
16	\textbf{MMLU} \citep{hendrycks2021mmlu} (5-shot): 14,042 multiple-choice items across 57 subjects, grouped into 8 cognitive domains (Math, Science, CS \& Engineering, Medical, Humanities, Social Sciences, Business \& Law, Other). This stratification reveals within-benchmark heterogeneity that aggregate scoring obscures (\S\ref{sec:results}).
17
…[truncated 1364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-21T07:24:13.279983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/results.tex"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-21T07:24:13.330712+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Cross-family results (\S\ref{sec:taxonomy}) use seed$=$42 data across five models from four independent families. Within-family IRT analyses (\S\ref{sec:calibration_results}--\ref{sec:domain_differential}) use $J=16$ Qwen2.5 models (8$\times$1.5B + 8$\times$3B); domain-level contamination estimates $\gamma_d$ (\S\ref{sec:domain_differential}) are reported at $J=16$ in the text and $J=13$ in Figure~\ref{fig:domain_gamma}.
5	
6	\subsection{Dose-Response Patterns}
7	\label{sec:taxonomy}
8	
9	\begin{table}[t]
10	\centering
11	\caption{Observed dose-response patterns under controlled SFT injection (seed$=$42, MMLU). $\Delta$acc: d000$\to$d100 change (95\% CI from item-level paired bootstrap, $B=10{,}000$). Stab.: bootstrap classification stability. Classifications are robust to threshold hyperparameter choice (180/180 model--seed--combination pairs across 30 $(\tau,\sigma)$ combinations; Appendix~\ref{sec:classification_sensitivity}).}
12	\label{tab:taxonomy}
13	\footnotesize
14	\begin{tabular}{llccccc}
15	\toprule
16	Pattern & Model & Baseline & $\Delta$acc & 95\% CI & Peak & Stab. \\
17	\midrule
18	Immune & Phi-4 14.7B & 76.4\% & $\pm$0.5pp & [$-$0.60, $+$0.26] & negl. & 100\% \\
19	Collapse & Qwen-14B & 69.4\% & $-$9.4 to $-$12.7pp & [$-$12.74, $-$9.0] & --- & 100\% \\
20	V-recovery & Qwen-7B & 66.1\% & $-$1.8pp & [$-$2.36, $-$1.22] & $-$3.1\textsuperscript{d025} & 99.6\% \\
21	Benefit & Gemma-2 9B & 61.9\% & $+$3.8pp & [$+$3.18, $+$4.33] & mono. & 76.6\% \\
22	Benefit & OLMo-2 7B & 53.8\% & $+$3.2pp\textsuperscript{$\dagger$} & [$+$2.73, $+$3.71] & sat.\textsuperscript{d050} & 100\% \\
23	\bottomrule
24	\multicolumn{7}{l}{\scriptsize $^{\dagger}$Seed-sensitive: s42 $+$3.2pp, s123 $-$0.6pp, s0 $+$1.4pp; cross-seed CI crosses zero. See \S\ref{sec:cross_seed}.}
25	\end{tabular}
26	\end{table}
27	
28	Applying Algorithm~\ref{alg:profile-classification} to seed$=$42 accuracy trajectories yields qualitatively different dose-res
…[truncated 15641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 619 · 2026-05-21T07:24:13.632222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 620 · 2026-05-21T07:24:14.586217+00:00_

1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	We systematically profiled how SFT-injected contamination affects benchmark scores across model families and scales. Three findings emerge.
4	
5	\paragraph{Diverse patterns, not uniform inflation.}
6	Controlled injection reveals qualitatively different dose-response patterns, not uniform inflation: vulnerability concentrates in the 65--70\% MMLU baseline band. Critically, difference-in-differences analysis provides causal evidence that these effects arise from global capability modulation rather than item-specific memorization---no model shows significant treated/untreated divergence (\S\ref{sec:memorization_test})---challenging the theoretical basis of overlap-based detection methods. Direction is consistent across benchmarks (3/5 on ARC; Gemma-2 benefits on MMLU but shows no significant ARC effect); shape varies with benchmark properties (Appendix~\ref{sec:arc_cross_benchmark}). Cross-seed analysis (\S\ref{sec:cross_seed}) shows direction is reproducible but magnitude is seed-sensitive; conflicting findings in the literature may partly reflect unreported seed variance.
7	
8	\paragraph{Why bigger $\neq$ more robust.}
9	Qwen-14B ($-$9 to $-$25pp across seeds, mean $-$15.7pp) is 3$\times$ more fragile than Qwen-7B ($-$1.8pp at d100, trough $-$3.1pp at d025): SFT injection disrupts more specialized representations that smaller models have not yet developed. Organizations fine-tuning frontier models on mixed-quality data face greater capability degradation risk.
10	
11	\paragraph{Diagnostic value beyond aggregate calibration.}
12	Domain analysis reveals heterogeneity masked by aggregate scores (Social Sciences $P(\gamma_d\!<\!0) = 99.7\%$). The IRT framework captures both family-level patterns and domain-level decomposition. Pretraining contamination may produce qualitatively different effects \citep{schaeffer2026causally}; scaling to 70B+ is a natural next step.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-21T07:24:14.636992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-21T07:24:14.988252+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	We identify ten limitations that bound the scope of our conclusions.
5	
6	\paragraph{Scale ceiling.}
7	All experiments use models at or below 14.7B parameters. Larger models (70B+) may exhibit qualitatively different contamination dynamics where SFT injection is absorbed without producing measurable signal divergence.
8	
9	\paragraph{Seed sensitivity.}
10	Cross-seed analysis (\S\ref{sec:cross_seed}) confirms that effect \emph{direction} is reproducible across three seeds, but magnitude and dose-response shape exhibit seed-dependent variability. OLMo-2's cross-seed CI crosses zero, rendering its benefit classification borderline. Practitioners should report multi-seed CIs rather than single-seed point estimates.
11	
12	\paragraph{SFT ecological validity.}
13	We use LoRA-based SFT injection exclusively in AUGMENT mode (contaminated items appended to, not replacing, base SFT data). Pretraining-stage leakage, which occurs during large-scale web crawl ingestion, may produce qualitatively different contamination signatures. The position bias at 0.5B (A-option rate escalating from 46\% to 98\% with dosage) is likely SFT-specific. Generalization to pretraining contamination requires further validation.
14	
15	\paragraph{ARC-Challenge bootstrap stability.}
16	ARC-Challenge contains only 1{,}172 items (vs.\ 14{,}042 for MMLU), resulting in substantially lower bootstrap profile stability: OLMo-2 53.3\%, Gemma-2 62.7\% (vs.\ $\geq$76.6\% on MMLU). Gemma-2's ARC $\Delta$acc 95\% CI crosses zero, and Qwen-14B exhibits a different pattern (V-recovery) on ARC than on MMLU (Collapse). Cross-benchmark consistency claims should be interpreted as directional agreement, not pattern-level replication.
17	
18	\paragraph{Signal coverage.}
19	S1 (embedding similarity) requires training corpus access, unavailable for closed-source models. For API-only models, only S2 and S4 are applicable, and both show poor discrimination below 1.5B (\
…[truncated 3201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 623 · 2026-05-21T07:24:15.038813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 624 · 2026-05-21T07:24:15.189515+00:00_

1	\section*{Ethics Statement}
2	
3	All experiments use publicly available, open-weight language models (Qwen2.5, Phi-4, OLMo-2, and Gemma-2) under their respective licenses. Contamination injection is performed via standard supervised fine-tuning on existing public benchmark items; no new data collection involving human subjects is conducted. All evaluation benchmarks (MMLU, ARC-Challenge, GSM8K) are publicly released datasets. This work does not involve private user data, personally identifiable information, or human annotation.
4	
5	We acknowledge a dual-use risk: the contamination injection protocol we describe could be used to deliberately inflate benchmark scores. We mitigate this by focusing on detection and measurement rather than injection optimization, and by releasing detection signals rather than injection recipes. Our findings characterize the conditions under which SFT injection affects aggregate scores, which may inform decisions about manipulation risk at different scales. The measurement framework is intended to improve evaluation transparency, not to enable gaming.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-21T07:24:15.240229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 626 · 2026-05-21T07:24:15.291155+00:00_

1	\appendix
2	
3	\section{ARC-Challenge Cross-Benchmark Analysis}
4	\label{sec:arc_cross_benchmark}
5	
6	ARC-Challenge (25-shot, 1{,}172 items) patterns under s42 are directionally consistent with MMLU for four of five models: OLMo-2 benefits ($+$3.9pp), Qwen-7B ($-$2.9pp) and Qwen-14B ($-$3.4pp) are harmed, Phi-4 remains immune ($+$0.6pp). Gemma-2 achieves $n\!=\!3$ on ARC: s42 exhibits a 16pp oscillation artifact (endpoint $-$1.20pp), s0 shows harm ($-$1.97pp), and s123 shows benefit ($+$2.73pp). The $n\!=\!3$ ARC mean is $-$0.15pp (SD$=$2.41pp; BCa 95\% CI [$-$1.97, $+$1.42]), with cross-seed direction inconsistent ($-$/$-$/$+$). This contrasts with MMLU, where all three seeds show benefit (mean $+$2.38pp, CI [$+$1.49, $+$3.14] excludes zero), making Gemma-2 the clearest example of benchmark-conditional contamination effects. Bootstrap stability is substantially lower than MMLU (OLMo-2: 53.3\%, Gemma-2: 62.7\%) due to the smaller item pool (1{,}172 vs.\ 14{,}042).
7	
8	\paragraph{Cross-seed ARC consistency.}
9	Phi-4 is the strongest anchor with $n\!=\!3$ on both benchmarks: ARC mean $\Delta = +0.66$pp (SD$=$0.18pp; s0 $+$0.51, s42 $+$0.60, s123 $+$0.86; BCa 95\% CI [$+$0.51, $+$0.77]), MMLU mean $\Delta = +0.73$pp---cross-benchmark agreement within 0.07pp. While statistically detectable on ARC (CI excludes zero, unlike MMLU CI [$-$0.17, $+$1.39]), the effect ($+$0.66pp) is too small to meaningfully inflate benchmark scores, consistent with the Immune classification. Qwen-7B achieves $n\!=\!3$ on ARC: mean $\Delta = -2.42$pp (SD$=$0.51pp; s0 $-$1.88, s42 $-$2.90, s123 $-$2.47; BCa 95\% CI [$-$2.90, $-$2.08]), confirming persistent harm. The d005 V-dip severity is seed-dependent ($-$1.8pp vs.\ $-$4.7pp). Qwen-14B achieves $n\!=\!3$ on both benchmarks: MMLU mean $\Delta = -15.7$pp (BCa CI [$-$24.99, $-$10.49]; s0 most extreme at $-$25.0pp due to position bias amplification); ARC mean $\Delta = -5.03$pp (BCa CI [$-$9.38, $-$2.76]). Both CIs exclude zero, confirming C
…[truncated 23683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-21T07:24:16.344479+00:00_

# EMNLP 2026 Submission Guidelines

## Page Limits
- **Long papers:** 8 pages of content
- **Short papers:** 4 pages of content
- **Final versions:** +1 additional page allowed (9 pages for long, 5 pages for short) to address reviewer feedback

## Templates & Formatting
Authors must "follow all of the ARR submission requirements," with specific guidance available via the ACL Rolling Review platform.

## Anonymity Rules
The review process maintains double-blind evaluation. "Reviewers will not see authors, nor will authors see reviewers" and ARR review visibility remains restricted. However, authors may opt to make their anonymized submissions publicly visible. "Following the ACL and ARR policies, there is no anonymity period requirement."

## Authorship & Modifications
During commitment to EMNLP, author list modifications (additions/deletions) are prohibited, though author order changes remain permissible.

## Ethics & Limitations
Submissions must comply with:
- ACL's Publication Ethics Policy
- ARR's Ethics Policy including the responsible NLP research checklist
- ACL's Disclosure Policy for coordinated vulnerability disclosure

Papers must include limitations sections per ARR standards.

## Supplementary Materials
"Optional Supplementary Materials (appendices, software and data)" are allowed per ARR guidelines.

## Dual Submission Policy
"Dual submissions are not allowed!" Papers submitted to ARR's May 2026 cycle must explicitly declare EMNLP 2026 commitment intent at submission; this choice is binding. Papers from earlier ARR cycles may still commit to EMNLP.

## Citation & Writing Assistance
Standard citation practices apply. AI writing assistance is permitted per ACL 2023 policy.

## Resubmission & Withdrawal
Full policies available through ARR's CFP documentation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "WebFetch",
  "elapsed_ms": 6227
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-21T07:24:23.777108+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-21T07:24:25.235588+00:00_

{"result":"# 项目 contamcal-irt-calibration 概况\n\n## 实验状态 (386 个)\n\n- **exp_001_sft_d100_05B**: DONE (success) — \n- **exp_001_sft_0pct**: DONE (success) — \n- **exp_001_sft_0pct_3B_s123**: DONE (success) — \n- **exp_001_eval_15B_d000_s42**: DONE (failed) — \n- **exp_001_sft_d005_05B_v2**: DONE (failed) — \n- **exp_001_sft_d005_05B**: DONE (killed) — \n- **exp_001_sft_100pct_05B**: DONE (failed) — \n- **exp_001_sft_0pct_3B**: DONE (success) — \n- **exp_001_sft_injection**: DONE (success) — \n- **exp_001_sft_0pct_15B_s123**: DONE (success) — \n- **exp_001_sft_0pct_05B_s123**: DONE (success) — \n- **exp_001_sft_0pct_15B**: DONE (success) — \n- **exp_001_sft_0pct_05B**: DONE (success) — \n- **mvp_sim_confounding**: DONE (success) — \n- **mvp_sim_4pl_gamma**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-21\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| eval_qwen14b_d100_gsm8k_s0 | Qwen-14B d100 s0 GSM8K eval: cross-benchmark contamination effect at max dosage. MMLU contamination may transfer to math reasoning or be domain-specific. | — | — | — |\n\n## 待处理\n- eval_gemma2_mmlu_s0: Gemma-2 s0 MMLU 5-shot eval for d000-d050 (partial); d100 pending retrain completion（排队等待 GPU）\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\n- eval_gemma2_arc_s0: Gemma-2 s0 ARC 25-shot eval for d000-d050 (partial); d100 pending retrain completion（准备中）\n- sft_gemma2_s0_sweep_v2（准备中）\n- gsm8k_phi4_s42_westd: GSM8K eval for Phi-4 s42: test if Immune archetype (±0.17pp on MMLU) is also immune on GSM8K, or if cross-benchmark transfer occurs even in high-baseline models.（准备中）\n- phase2_eval_gpu3_gemma_olmo: Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3（准备中）\n- phase2_eval_gpu1_qw
…[truncated 2645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-21T07:24:25.235970+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-21T07:24:25.687280+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-21T07:24:26.339230+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "figures/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "figures/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-21T07:24:26.640461+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-21T07:24:27.192487+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-21T07:24:28.146311+00:00_

- id: "R2-N1"
  summary: "Title/framing promises general answer but experiments only cover SFT ≤3B"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 6
  mentions:
    - {round: 2, reviewers: "R1,R2", note: "Table 2: vanilla 2PL MAE ≤ ContamCal on all benchmarks. Title/Abstract promise contamination-aware calibration but experiments show standard IRT suffices."}
    - {round: 3, reviewers: "R1,R2", note: "Title still 'ContamCal'. Abstract implies contamination-specific modeling."}
    - {round: 4, reviewers: "R1,R2", note: "Title 'Decomposing Contamination from Calibration' promises decomposition but core result is nothing to decompose (~0.6-0.7pp). 'Diagnostic value' pivot introduced too late (§1 ¶4). R1 and R2 both AGREE this is narrative mismatch. Suggest empirical investigation framing."}
    - {round: 5, reviewers: "R1,R2", note: "Title changed to question form but framing still inconsistent."}
    - {round: 6, reviewers: "R1,R2", note: "Title question form improved but still over-scopes."}
  action_items:
    - {round: 2, action: "Reframe paper", assigned_to: "paper_agent", status: "done"}
    - {round: 3, action: "Change title, rewrite Abstract/Contributions", assigned_to: "paper_agent", status: "done"}
    - {round: 4, action: "Reframe as empirical investigation rather than method paper", assigned_to: "paper_agent", status: "done"}
    - {round: 5, action: "Rewrite Introduction from ¶1 as question-driven empirical investigation", assigned_to: "paper_agent", status: "done"}
    - {round: 6, action: "Modify title to scope claim", assigned_to: "paper_agent", status: "done"}
  resolution: "D149+ rewrite: Title changed to 'Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families'. Paper repositioned as systematic empirical investigation of dose-response across 5 models (7B-14.7B) from 4 families. No over-scoping."
  resolution_round: 7

- id: "R2-W6"
  summary: "SFT injection eco
…[truncated 23585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-21T07:24:28.146860+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-21T07:24:28.248463+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-21T07:24:34.922395+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | head -80 || echo \"NO_CONFIG\"",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/ -name \"*.yaml\" -o -name \"*.yml\" | head -10 && echo \"---\" && cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/config.yaml 2>/dev/null | head -80 || echo \"NO_CONFIG\"",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-21T07:24:35.674732+00:00_

find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/agent/’: No such file or directory
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-21T07:24:35.725280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-21T07:24:35.776001+00:00_

1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	% --- Restored entries (required by reviewer) ---
6	
7	@book{camilli_1994_dif,
8	  author    = {Camilli, Gregory and Shepard, Lorrie A.},
9	  title     = {Methods for Identifying Biased Test Items},
10	  series    = {Measurement Methods for the Social Sciences},
11	  publisher = {Sage Publications},
12	  year      = {1994},
13	  address   = {Thousand Oaks, CA},
14	  isbn      = {978-0-8039-4416-9}
15	}
16	
17	@article{swaminathan_1990_dif,
18	  author  = {Swaminathan, Hariharan and Rogers, H. Jane},
19	  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},
20	  journal = {Journal of Educational Measurement},
21	  volume  = {27},
22	  number  = {4},
23	  pages   = {361--370},
24	  year    = {1990},
25	  doi     = {10.1111/j.1745-3984.1990.tb00754.x}
26	}
27	
28	@book{holland_1993_dif,
29	  author    = {Holland, Paul W. and Wainer, Howard},
30	  title     = {Differential Item Functioning},
31	  publisher = {Lawrence Erlbaum Associates},
32	  year      = {1993},
33	  address   = {Hillsdale, NJ}
34	}
35	
36	@article{xu_2024_leakage,
37	  author        = {Xu, Ruijie and Wang, Zengzhi and Fan, Run-Ze and Liu, Pengfei},
38	  title         = {Benchmarking Benchmark Leakage in Large Language Models},
39	  journal       = {arXiv preprint},
40	  year          = {2024},
41	  eprint        = {2404.18824},
42	  archiveprefix = {arXiv},
43	  url           = {https://arxiv.org/abs/2404.18824}
44	}
45	
46	@inproceedings{li_2024_task_contamination,
47	  author    = {Li, Changmao and Flanigan, Jeffrey},
48	  title     = {Task Contamination: Language Models May Not Be Few-Shot Anymore},
49	  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},
50	  volume    = {38},
51	  number    = {16},
52	  pages     = {18471--18480},
53	  
…[truncated 7992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-21T07:24:40.439558+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/ -maxdepth 2 -name \"config.yaml\" 2>/dev/null | head -5",
  "description": "Find config files for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5 && echo \"---\" && find /home/ubuntu/.agent-ml-research-idea_gen_0509_13/ -maxdepth 2 -name \"config.yaml\" 2>/dev/null | head -5",
    "description": "Find config files for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-21T07:24:40.540510+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-21T07:25:24.931238+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:dispatch_visual_check,director_post_to_reviewer",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:dispatch_visual_check,director_post_to_reviewer",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-21T07:25:25.031996+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-21T07:25:29.654714+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "review_chat_id": "oc_da6d629d7f92da47a5e85cb7e296ae13"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-21T07:25:43.576500+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 13921
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-21T07:25:43.627166+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计声明可靠性**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- Long paper 正文 ≤ 8 页（Limitations + Ethics 不计入；References 无限）\n- ACL 模板，double-blind 匿名\n- Limitations 章节必须存在（缺失 desk-reject）\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **方法论严谨性**:\n   - 2PL+γ IRT 模型的数学正确性和假设合理性\n   - RRF multi-signal fusion 的统计性质\n   - Dose-response profile classification algorithm 的合理性和鲁棒性\n   - Bayesian inference 设置（priors, convergence diagnostics, PPP）是否恰当\n   - 可识别性分析（identifiability simulation）是否充分\n\n2. **实验设计**:\n   - 控制变量注入方案（SFT injection with LoRA）的生态效度\n   - 模型/家族选择的代表性和覆盖度\n   - Cross-seed 和 cross-benchmark 验证的充分性\n   - DiD 分析的因果推断有效性\n   - Baselines 是否全面公平\n\n3. **统计声明可靠性**:\n   - 所有 CI、p-value、PPP 是否正确报告\n   - 多重比较校正是否恰当\n   - 效应量（Cohen's d, pp 差异）是否合理解读\n   - Cross-seed stability 声明是否与 n=3 样本量匹配\n   - Ensemble size J 对各分析的影响是否充分讨论\n\n4. **可复现性**:\n   - 实验细节是否足以复现\n   - 超参数选择是否有依据\n   - 代码/数据可用性声明\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出你的审稿意见。对每个 Weakness 标注严重程度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计声明可靠性**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- Long paper 正文 ≤ 8 页（Limitations + Ethics 不计入；References 无限）\n- ACL 模板，double-blind 匿名\n- Limitations 章节必须存在（缺失 desk-reject）\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **方法论严谨性**:\n   - 2PL+γ IRT 模型的数学正确性和假设合理性\n   - RRF multi-signal fusion 的统计性质\n   - Dose-response profile classification algorithm 的合理性和鲁棒性\n   - Bayesian inference 设置（priors, convergence diagnostics, PPP）是否恰当\n   - 可识别性分析（identifiability simulation）是否充分\n\n2. **实验设计**:\n   - 控制变量注入方案（SFT injection with LoRA）的生态效度\n   - 模型/家族选择的代表性和覆盖度\n   - Cross-seed 和 cross-benchmark 验证的充分性\n   - DiD 分析的因果推断有效性\n   - Baselines 是否全面公平\n\n3. **统计声明可靠性**:\n   - 所有 CI、p-value、PPP 是否正确报告\n   - 多重比较校正是否恰当\n   - 效应量（Cohen's d, pp 差异）是否合理解读\n   - Cross-seed stability 声明是否与 n=3 样本量匹配\n   - Ensemble size J 对各分析的影响是否充分讨论\n\n4. **可复现性**:\n   - 实验细节是否足以复现\n   - 超参数选择是否有依据\n   - 代码/数据可用性声明\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出你的审稿意见。对每个 Weakness 标注严重程度。"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-21T07:25:53.661655+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10034
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-21T07:25:53.762665+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责 **新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- Long paper 正文 ≤ 8 页（Limitations + Ethics 不计入；References 无限）\n- ACL 模板，double-blind 匿名\n- Limitations 章节必须存在（缺失 desk-reject）\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **新颖性与贡献**:\n   - 核心发现（dose-response taxonomy, global modulation, signal failure）的新颖性\n   - 与现有工作的差异化程度（特别是 Han et al. 2026 的 DIF 方法）\n   - 贡献是否匹配 EMNLP 主会议水平（vs. Findings）\n   - \"contamination ≠ inflation\" 这一 claim 的证据强度\n   - 各贡献的独立价值和整体协同\n\n2. **Related Work 完整性**:\n   - 是否覆盖所有重要相关工作（contamination detection, IRT for LLMs, DIF literature）\n   - 与 concurrent work 的区分是否准确公允\n   - 是否有遗漏的关键参考文献\n   - Related Work 的组织结构是否清晰\n\n3. **写作质量**:\n   - 论文叙事是否连贯（problem → method → findings → implications）\n   - Abstract 是否准确概括论文贡献\n   - Introduction 的动机是否令人信服\n   - 术语使用是否一致\n   - 图表质量和信息密度\n   - 论文长度是否合适\n\n4. **格式合规**:\n   - 是否符合 ACL 模板格式\n   - 匿名性是否完全（无 de-anonymizing 信息）\n   - Limitations 章节是否充分\n   - Ethics statement 是否恰当\n   - 引用格式是否正确\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出你的审稿意见。对每个 Weakness 标注严重程度。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责 **新颖性 + Related Work 完整性 + 写作质量 + 格式合规**。\n\n## Venue 信息\n- **EMNLP 2026** via ACL Rolling Review (ARR May cycle)\n- Deadline: 2026-05-25\n- Long paper 正文 ≤ 8 页（Limitations + Ethics 不计入；References 无限）\n- ACL 模板，double-blind 匿名\n- Limitations 章节必须存在（缺失 desk-reject）\n\n## 论文路径\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/main.tex`\n\n## 你的审查侧重\n\n请重点评估以下维度：\n\n1. **新颖性与贡献**:\n   - 核心发现（dose-response taxonomy, global modulation, signal failure）的新颖性\n   - 与现有工作的差异化程度（特别是 Han et al. 2026 的 DIF 方法）\n   - 贡献是否匹配 EMNLP 主会议水平（vs. Findings）\n   - \"contamination ≠ inflation\" 这一 claim 的证据强度\n   - 各贡献的独立价值和整体协同\n\n2. **Related Work 完整性**:\n   - 是否覆盖所有重要相关工作（contamination detection, IRT for LLMs, DIF literature）\n   - 与 concurrent work 的区分是否准确公允\n   - 是否有遗漏的关键参考文献\n   - Related Work 的组织结构是否清晰\n\n3. **写作质量**:\n   - 论文叙事是否连贯（problem → method → findings → implications）\n   - Abstract 是否准确概括论文贡献\n   - Introduction 的动机是否令人信服\n   - 术语使用是否一致\n   - 图表质量和信息密度\n   - 论文长度是否合适\n\n4. **格式合规**:\n   - 是否符合 ACL 模板格式\n   - 匿名性是否完全（无 de-anonymizing 信息）\n   - Limitations 章节是否充分\n   - Ethics statement 是否恰当\n   - 引用格式是否正确\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 结构输出你的审稿意见。对每个 Weakness 标注严重程度。"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-21T07:25:55.372500+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1609
}
```

</details>

---


### Assistant

_source line 652 · 2026-05-21T07:26:02.941619+00:00_

Round 1 已启动：

- ✅ 视觉审查 Agent 已派发（fire-and-forget，不阻塞）
- ✅ Reviewer 1（方法严谨性 + 实验设计）已分配
- ✅ Reviewer 2（新颖性 + 写作质量）已分配

等待两位 Reviewer 返回独立审稿意见，收齐后进入 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 653 · 2026-05-21T07:31:16.354416+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿意见：方法严谨性 + 实验设计 + 统计声明可靠性

**论文标题**: Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families

---

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 将 benchmark contamination 建模为 psychometric dose-response 问题的思路新颖且有价值，但核心实验在统计功效边界上运行（n=3 seeds, J=13–16 models），多个关键 claim 的证据强度不足以支撑其表述力度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 方法论框架扎实（explanatory IRT + RRF fusion），但经验验证在 identifiability 边界运行；DiD 无显著性可能是 power 不足而非真阴性；多处 claim 强于证据 |
| Excitement | 3.5/5 | 将 contamination 视为连续剂量效应并建立 dose-response taxonomy 是真正的 conceptual novelty；若统计问题得到解决，有潜力影响社区对 benchmark contamination 的思考方式 |
| Reproducibility | 3/5 | 模型和 benchmark 公开，方法描述详细，但无代码/数据发布承诺（Ethics Statement 仅说 "publicly available" 数据集）；IRT 模型的 Stan 实现细节分散在正文和 appendix 中 |
| Confidence | 4/5 | 对 IRT 建模、Bayesian inference、实验设计有较强专业背景；对个别 contamination detection signal 的内部机制了解较浅 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Cross-seed stability 声明与 n=3 样本量严重不匹配

- 具体位置：Section 5.3, Table 3
- 问题：论文以 n=3 random seeds 为基础声称 dose-response pattern 的 "cross-seed stability"（例如 "strict sign consistency requires all seeds to share the same sign of Δacc(d0)"）。但 n=3 下任何方差估计的置信区间都极宽——即使 3/3 seeds 同方向，bootstrap 置信水平也仅 ~87.5%（远低于惯例 95%）。Table 3 报告了 per-seed Δacc 范围（如 Qwen-7B: "−1.38 to +1.19"），但未提供 seed 间变异性的正式统计检验或置信区间。论文的 taxonomy-level consistency criteria（"2/5 families agree" for strict sign consistency）本身就是在小样本上二次聚合，统计可靠性存疑。
- 为什么影响接收：dose-response taxonomy 是论文的核心贡献（Contribution 1），如果分类在更多 seeds 下不稳定，整个框架的实用价值成问题。
- 建议修改方向：(1) 增加到至少 n=5–10 seeds（对于 0.5B–3B 模型，LoRA SFT 成本可控）；(2) 报告 bootstrap CI 覆盖 seed 变异性；(3) 降低 claim 力度，明确标注 "preliminary taxonomy under limited replication"。

**N2** [critical] IRT 模型 identifiability 在经验 ensemble size (J=13–16) 下刚好处于边界

- 具体位置：Section 3.3 (Identifiability), Appendix D, Appendix P
- 问题：Appendix D 的 simulation 显示 AUC recovery 在 J≥16 时达到 >0.85，95% CI coverage 在 J=13–16 时为 nominal（~0.93）。但经验分析中，排除后实际 J=16（Section 5, Appendix G: 16 out of 16 models retained after exclusion for seed=42, but other seeds may differ）。这意味着论文的统计推断恰好运行在 simulation 验证的下界。更关键的是：
  - Appendix P 的 DGP simulation 显示 CI coverage 在 J 增大时反而下降（Table 11: J=500 时 coverage 仅 0.68–1.00），论文解释为 "the intervals become overcondident as J increases because the model converges to a biased point estimate"。这暗示 2PL+γ 模型存在系统性偏差，在大 J 下会过度自信。
  - 论文的 identifiability simulation 使用的是 uniform exposure（Appendix D），但实际 RRF exposure 分布是 right-skewed 的（Section 3.2 提到 "most model-item pairs receiving near-zero exposure"）。在高度偏斜的 exposure 分布下，γ 的 identifiability 可能更差。
- 为什么影响接收：如果 IRT 参数估计不可靠，下游的 dose-response classification 和 calibration 结论都会受影响。
- 建议修改方向：(1) 在 simulation 中使用与实际 RRF exposure 分布匹配的 skewed exposure 而非 uniform；(2) 明确报告每个 seed 下实际 J 和 exclusion 情况；(3) 讨论 CI coverage 随 J 下降的理论原因及其对当前结论的影响。

**N3** [critical] DiD 分析的 null result 可能是 statistical power 不足而非真阴性

- 具体位置：Section 5.4, Table 4, Figure 2
- 问题：论文声称 "All DiD non-significant: contamination operates via global capability modulation"（Contribution 2）。但 DiD 检验的 power 取决于：(1) per-item 效应量——如果 contamination 同时提升全局能力并有微小 item-specific 效应，DiD 可能检测不到后者；(2) n=3 seeds 提供的 within-cell 变异性极有限；(3) treated vs. untreated item 的划分阈值（d025）可能不够灵敏。Table 4 显示 DID 值范围从 −0.8 到 +0.6pp，这些效应量在 n=3 下的 power 是多少？论文未做 power analysis。
- 此外，Figure 2 的 symmetry 声明（"confirm symmetry (gap < 0.4pp)"）依赖于视觉判断而非正式检验。
- 为什么影响接收：将 "no significant effect" 等同于 "no effect" 是经典的 absence-of-evidence ≠ evidence-of-absence 错误。如果论文要做因果声明（"causal evidence"），必须证明 power 足够。
- 建议修改方向：(1) 做 post-hoc power analysis 报告最小可检测效应量（MDES）；(2) 将结论从 "contamination operates via global modulation" 弱化为 "we find no evidence of item-specific memorization at the current power level"；(3) 讨论如果存在例如 0.5pp 的 item-specific 效应，当前设计是否能检测到。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] RRF fusion 缺乏 calibration 验证

- 具体位置：Section 3.2, Eq. (1)
- 问题：RRF 来自信息检索（Cormack et al., 2009），其 rank-based fusion 假设各 signal 的 rank ordering 有意义且可比较。但论文未验证：(1) RRF score v_ij 的数值大小是否反映真实 contamination 程度（而非仅是排名结果）；(2) 4 个 signal 中任何一个翻转排序时 fusion 的鲁棒性；(3) signal 间相关性——如果 S1-S4 高度相关，RRF 相当于对同一信息加权平均，并不比单一 signal 好。Table 5 显示 RRF-guided selection 比 random 好（MAE 0.006 vs 较高值），但这仅间接验证了 RRF 选择了 "好的" items，而非 v_ij 本身是 calibrated contamination measure。
- 建议：(1) 报告 4 个 signal 间的 rank correlation；(2) 做 leave-one-signal-out 消融验证 RRF 的 complementarity；(3) 对 v_ij 做 calibration plot（predicted vs. actual contamination）——在 controlled injection 设定下这是可行的。

**W2** [warning] SFT injection 的 ecological validity 未充分量化

- 具体位置：Section 4.1, Limitations (page 9)
- 问题：真实的 benchmark leakage 发生在 pretraining 阶段（trillion-token web crawl），而本文用 post-training LoRA SFT 注入。论文在 Limitations 中承认这一点（"pretraining-stage leakage...may produce qualitatively different contamination signatures"），但正文的 contribution 表述（"we perform controlled SFT injection...and discover qualitatively different dose-response patterns"）和标题（"Profiling Contamination Dose-Response"）暗示更广泛的适用性。
- SFT injection 在 AUGMENT mode（将 contaminated items appended to, not replacing, base SFT data）下进行——这进一步偏离真实场景，因为实际的 web crawl 泄露不会在 fine-tuning 数据中以这种方式出现。
- 建议：(1) 在 abstract/intro 中明确限定为 "post-training contamination"；(2) 设计一个小规模的 pretraining injection 实验（即使只用 0.5B 模型）以验证 dose-response pattern 是否 transfer；(3) 讨论 AUGMENT vs REPLACE mode 的影响。

**W3** [warning] Baseline 比较中 ContamCal 的优势不够显著

- 具体位置：Section 5.5, Table 5, Tables 12-13 (Appendix R)
- 问题：Table 5 中 ContamCal (4PL+γ) 在 MMLU 上 MAE=0.035，而 B4-LinearRegression MAE=0.071——improvement 约 50%。但在 ARC 上 ContamCal MAE=0.035 vs B4 MAE=0.056（更小的差距），在 GSM8K 上（Table 13）ContamCal MAE=0.020 vs B4 MAE=0.003（B4 反而更好！）。B6-DCR 在 Table 5 中无 MAE 值（marked as "—"），论文仅说 "B6-DCR systematically overcorrects"，未定量比较。
- 在 full baseline comparison (Table 12, ARC, pooled 0.5B+1.5B), ContamCal MAE=0.035 vs B0-Raw 0.059, B3-Vanilla4PL 0.071, B4-LinearRegression 0.056。改善存在但不大，且在 GSM8K 上反而不如最简单的 B4。
- 建议：(1) 在所有 benchmark 上统一报告所有 baseline 的 MAE，不要选择性报告；(2) 明确讨论 ContamCal 在 GSM8K 上不如 B4 的原因；(3) 考虑用 paired bootstrap test 检验 MAE 差异是否显著。

**W4** [warning] Bayesian 和 frequentist 术语混用

- 具体位置：多处，例如 Section 5.1 ("significant"), Section 5.2 ("statistically significant at p < 0.05"), Section 5.4 ("non-significant")
- 问题：论文使用 Bayesian MCMC 推断（NUTS in Stan），posterior credible intervals 在语义上不同于 frequentist confidence intervals。但正文中多次使用 "significant" "p-value" 等 frequentist 术语：
  - Section 5.1 提到 "CI excludes zero" 作为 significance 判据——这是 Bayesian credible interval 的解读，与 p-value 不同
  - Table 1 注释中出现 "p < 0.0005"——这里的 p 是 PPP (posterior predictive p-value)？还是 frequentist p？未说明
  - Section 5.4 的 DiD 检验似乎使用的是 frequentist t-test（"p > .05; ns"），而 IRT 参数本身是 Bayesian 估计
  - Section 5.2 提到 "not statistically significant at p < 0.05"——同样未说明 p 的来源
- 建议：(1) 统一统计框架，明确标注每个检验是 Bayesian 还是 frequentist；(2) 对 Bayesian CI，使用 "credible interval" 而非 "confidence interval"；(3) 对 PPP，明确标注。

---

## 小问题（不影响接收）

- **M1**: Algorithm 1 的 threshold τ 在正文中说是 "explicit and adaptive"（Section 3.4），但 τ 的具体取值（0.5, 0.75, 1.0, 1.25, 1.5, 2.0 pp）在 Appendix K Table 9 中给出。正文应提供 default τ 值或至少指向 appendix。
- **M2**: Section 3.2 将 |S| = 3 作为 "our primary pipeline"（排除 S2 和 S4 因为某些模型不支持），但 Table 5 的 calibration 分析使用的是 "300 RRF-filtered items"——是用 3 signal 还是 4 signal 的 RRF？不清楚。
- **M3**: Appendix G 的 model exclusion criteria（"mismatched naming conventions between evaluation and signal extraction stages"）过于模糊，无法复现。
- **M4**: Figure 1 被引用为 dose-response pattern 的可视化，但图中仅展示了一个 benchmark (MMLU) 的一个 seed (seed=42) 的结果。应在 caption 中说明这是代表性示例。
- **M5**: Eq. (2) 定义了 decontamination accuracy Acc_j^*，但未解释 "posterior expectation under zero exposure" 在实践中如何计算——是将 v_ij 设为 0 后重新计算 posterior mean of θ_j，还是直接将 γ_i · v_ij 从 logit 中减去？这两种做法在非线性模型中结果不同。
- **M6**: 引用格式：部分 bib 条目年份与 OpenAlex 不匹配（如 holland_1993_dif 标注 1993 但 API 返回 2009，lord_1980_irt 标注 1980 但 API 返回 2012——可能是再版）。建议核查。

---

## Questions to Authors

**Q1**: Appendix P 显示 CI coverage 随 J 增大而下降（Table 11），论文解释为 "model converges to a biased point estimate"。能否详细解释这个 bias 的来源？这是否意味着 2PL+γ 模型在大样本下是 misspecified 的？如果是，为什么在小 J 下 coverage 反而好——是因为 prior 在 dominating？

**Q2**: RRF exposure score v_ij 的分布是 right-skewed 的（大部分 items 接近 zero）。在 IRT 模型中，γ_i 的估计主要依赖有非零 v_ij 的 items。但如果绝大多数 items 的 v_ij ≈ 0，γ_i 实际上由少数高 exposure items 驱动。这是否引入了 leverage effect？有没有做 influential observation 诊断？

**Q3**: Table 2 的 cross-benchmark transfer 结论基于 d100 exposure。在 lower dosage 下（d005, d025）transfer pattern 是否一致？

**Q4**: 论文排除了 0.5B 模型因 position bias（"A-option rate: 46% at d000 to 98% at d100"）。这个现象本身非常有趣——SFT contamination 是否将 0.5B 模型 "trained" 为总选 A？这是否暗示 small models 的 dose-response 可能完全不同于 medium/large models？论文是否考虑过将 position bias correction 后的 0.5B 结果作为补充分析？

---

## Missing References

- **Recht et al. (2019)** "Do ImageNet Classifiers Generalize to ImageNet?" — 关于 benchmark overfitting 的经典工作，与 contamination 主题高度相关。
- **Yang et al. (2023)** "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples" — 直接相关的 contamination 通过 rephrasing 减轻的工作。
- **Bakhtin et al. (2024)** 或其他关于 pretraining data deduplication 对 contamination 影响的工作——论文讨论了 post-training contamination 但未引用 pretraining decontamination 的方法论工作。

---

## 主要优势

1. **概念新颖性**：将 benchmark contamination 建模为连续剂量-效应关系并用 psychometric 框架分析是真正的新视角。Dose-response taxonomy（Immune/Collapse/V-Recovery/Benefit）提供了比二分法（contaminated/clean）更丰富的分析维度。
2. **实验设计的 controlled injection 方法论**：用 LoRA SFT 在已知 ground truth 下注入 contamination，使得可以对 detection 方法进行有控制的评估——这在现有文献中较少见。
3. **Appendix 的 thoroughness**：18 个 appendix sections 覆盖了 identifiability simulation、DGP robustness、sensitivity analysis、convergence diagnostics 等——表明作者对方法论细节的认真态度。
4. **多 baseline 比较**：7 个 baseline 方法（包括 raw accuracy、remove-and-rescore、vanilla IRT、linear regression、Emperor、DCR）提供了较全面的参照。
5. **Within-family domain analysis**（Section 5.7）揭示了 STEM 与 Social Sciences 在 contamination 敏感性上的差异，这是一个有实际价值的发现。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 654 · 2026-05-21T07:31:30.168631+00:00_

Reviewer 1 审稿意见已收到。评分 3.5（Borderline Conference），3 个 critical must-fix + 4 个 warning should-fix。

核心关切：(1) n=3 seeds 下 cross-seed stability 声明过强，(2) IRT identifiability 在经验 J=13-16 边界运行，(3) DiD null result 缺 power analysis。

等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 62

## Round 62

2 recorded events


### User

_source line 655 · 2026-05-21T07:31:33.404949+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。核心创新——用 IRT dose-response 框架分析 contamination——有价值，但三个 critical 问题需要解决：(1) n=3 seeds 不足以支撑 cross-seed stability 声明；(2) IRT identifiability 恰好在经验 ensemble size 的边界上，且 simulation 用的 uniform exposure 与实际 skewed 分布不匹配；(3) DiD null result 缺乏 power analysis，不能等同于 "no item-specific effect"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 656 · 2026-05-21T07:31:42.544608+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 完成后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_da6d629d7f92da47a5e85cb7e296ae13:director"
}
```

</details>

---


## Round 63

## Round 63

6 recorded events
