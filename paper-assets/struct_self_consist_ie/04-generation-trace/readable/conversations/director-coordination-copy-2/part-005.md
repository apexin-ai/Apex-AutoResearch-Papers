# Director coordination — Part 5 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 97

### Tool call

_source line 1275 · 2026-05-16T06:39:43.219327+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性/贡献框架 + 相关工作完整性 + 写作/格式合规\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子文件）\n- **目标 venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **格式**: ACL template (review mode), 8 页正文 + unlimited references, double-blind, 需含 Limitations section\n\n### 你的审查重点\n\n1. **新颖性与贡献**\n   - \"Correlation-selection gap\" 概念是否是 genuine empirical finding 还是 instance-level 信号的 definitional consequence\n   - 与 Yao et al. (2026) 的增量贡献是否足够清晰（structural matching, QE/selection separation, difficulty gradient）\n   - 三个 contributions 的表述是否准确区分了 by-construction 和 empirical\n   - 论文定位：纯诊断 (diagnostic) paper vs 提供解决方案，对 EMNLP 是否足够\n\n2. **相关工作**\n   - Self-consistency 文献覆盖是否完整（wang2023, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty 等）\n   - MBR decoding 文献是否完整（Eikema, Freitag, Deguchi centroid MBR 等）\n   - Uncertainty/calibration 文献（semantic uncertainty, P(True), conformal prediction）\n   - 是否有重要缺失引用（检查 Mejer & Crammer 2011, Xie et al. 2024 self-evaluation, Bertoldi et al. 等）\n   - Bib entries 是否全部在正文引用（无 orphan entries）\n   - 引用年份是否准确（oh2025latentsc 应为 2026?）\n\n3. **写作质量**\n   - Abstract 信息密度是否合理（是否过于 compressed）\n   - 论文 narrative flow：problem → method → finding → implication 是否清晰\n   - †RE 标注系统是否一致使用\n   - \"preliminary\" 出现次数是否过多\n   - Discussion 中 LP hypothesis 编号（\"three mechanisms\" vs 实际 4 个 (a)(b)(c)(d)）\n   - Table/Figure 自含性（caption 是否足够理解）\n   - Greedy/Single baseline 命名是否全文一致\n\n4. **格式合规**\n   - 页数是否在 8 页正文内（不含 references, limitations, ethics）\n   - ACL template 使用是否正确（review mode）\n   - 匿名性是否满足 double-blind（无 self-citation 暴露身份）\n   - Limitations section 是否存在且有实质内容\n   - Ethics statement 是否存在\n\n请按以下结构输出你的审稿报告：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者回答的)\n- **Missing References**\n- **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重**：新颖性/贡献框架 + 相关工作完整性 + 写作/格式合规\n\n### 论文信息\n- **标题**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n- **路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子文件）\n- **目标 venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **格式**: ACL template (review mode), 8 页正文 + unlimited references, double-blind, 需含 Limitations section\n\n### 你的审查重点\n\n1. **新颖性与贡献**\n   - \"Correlation-selection gap\" 概念是否是 genuine empirical finding 还是 instance-level 信号的 definitional consequence\n   - 与 Yao et al. (2026) 的增量贡献是否足够清晰（structural matching, QE/selection separation, difficulty gradient）\n   - 三个 contributions 的表述是否准确区分了 by-construction 和 empirical\n   - 论文定位：纯诊断 (diagnostic) paper vs 提供解决方案，对 EMNLP 是否足够\n\n2. **相关工作**\n   - Self-consistency 文献覆盖是否完整（wang2023, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty 等）\n   - MBR decoding 文献是否完整（Eikema, Freitag, Deguchi centroid MBR 等）\n   - Uncertainty/calibration 文献（semantic uncertainty, P(True), conformal prediction）\n   - 是否有重要缺失引用（检查 Mejer & Crammer 2011, Xie et al. 2024 self-evaluation, Bertoldi et al. 等）\n   - Bib entries 是否全部在正文引用（无 orphan entries）\n   - 引用年份是否准确（oh2025latentsc 应为 2026?）\n\n3. **写作质量**\n   - Abstract 信息密度是否合理（是否过于 compressed）\n   - 论文 narrative flow：problem → method → finding → implication 是否清晰\n   - †RE 标注系统是否一致使用\n   - \"preliminary\" 出现次数是否过多\n   - Discussion 中 LP hypothesis 编号（\"three mechanisms\" vs 实际 4 个 (a)(b)(c)(d)）\n   - Table/Figure 自含性（caption 是否足够理解）\n   - Greedy/Single baseline 命名是否全文一致\n\n4. **格式合规**\n   - 页数是否在 8 页正文内（不含 references, limitations, ethics）\n   - ACL template 使用是否正确（review mode）\n   - 匿名性是否满足 double-blind（无 self-citation 暴露身份）\n   - Limitations section 是否存在且有实质内容\n   - Ethics statement 是否存在\n\n请按以下结构输出你的审稿报告：\n- **Summary** (2-3 句)\n- **Strengths** (逐条)\n- **Weaknesses** (逐条，标注 Must-Fix / Should-Fix / Minor)\n- **Questions** (需要作者回答的)\n- **Missing References**\n- **Overall Assessment** (strong reject / weak reject / borderline / weak accept / strong accept + 置信度 1-5)"
  }
}
```

</details>

---


### Tool result

_source line 1276 · 2026-05-16T06:39:44.783275+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1563
}
```

</details>

---


### Tool call

_source line 1277 · 2026-05-16T06:39:52.125519+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1278 · 2026-05-16T06:39:52.176240+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1279 · 2026-05-16T06:40:06.085226+00:00_

Round 1 审稿已启动：

- **Reviewer 1**（方法严谨性 + 实验设计 + 统计分析）— 已分配
- **Reviewer 2**（新颖性/贡献框架 + 相关工作 + 写作格式）— 已分配
- **外部审稿**：未配置，跳过

等待两位 Reviewer 返回初审报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 98

## Round 98

2 recorded events


### User

_source line 1280 · 2026-05-16T06:45:21.633322+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 Round 1 审稿报告完成

**Paper**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition

### 总体评分
- **Soundness**: 3.5/5
- **Excitement**: 3.5/5
- **Reproducibility**: 4/5
- **Overall**: 3.5/5 (Borderline Findings/Conference)
- **Confidence**: 4/5

### 核心判断
研究问题新颖（QE vs selection 解耦），统计实践扎实（bootstrap CIs, TOST with external anchors, effect sizes），但有两个关键问题需要解决。

### Must-Fix (2项)
**N1**: Selection gap 的 effective test bed 仅限 SciERC（CoNLL 是 ceiling-effect control，WNUT collapse）。标题和 abstract 暗示 NER 普遍现象，但实证仅来自一个科学领域数据集（n=529）。建议：增加中等难度数据集或收窄 claim scope。

**N2**: Framing 过度强调 "4/5 signals assign identical scores"（by-construction trivial），模糊了核心 empirical finding（MBR conversion 产生 per-sample rankings 后仍然失败，因为 utility 在 across-instances 而非 within-instance 维度与 F1 相关）。当前叙事使读者误以为 gap 对 instance-level signals 是显而易见的定义问题。

### Should-Fix (5项)
W1: ρ=0.45 称 "moderate-to-strong" 但此值来自 ceiling-effect 数据集 CoNLL；SciERC 上最佳仅 ρ=0.379
W2: N≤16 不足以支撑 scaling claim，需 N=32+ 验证
W3: 缺少 greedy decoding baseline——部署决策的核心对照
W4: 3 seeds 下 Kendall W=1.000 统计信息量不足
W5: Soft Jaccard 命名不准确（分母用 max 非 union）

### 主要优势
- Entity-token LP 消融深层诊断（排除 format-token dilution，指向 intrinsic model overconfidence）
- Free-form ablation 4-seed RE reversal（+1.84±0.12 pp）
- 统计实践（TOST 循环论证识别与外部锚定、bootstrap CIs、Bonferroni 讨论）
- Honest negative-result reporting with appropriate caveats

### 5 个作者需回答的问题
Q1: 是否尝试过 soft selection / weighted fusion 而非 hard argmax MBR?
Q2: Oracle headroom 依赖 gold annotations，部署时如何估计？
Q3: Entity-token LP variance 在 CoNLL vs SciERC 的巨大差异是否与 entity type diversity 有关？
Q4: RE LP reversal 的 constrained baseline 仅 single-seed，reversal magnitude 相对 seed variance 是否显著？
Q5: 4B 模型 QE 优于 8B 的 counterintuitive finding 需要更多讨论——是否因 output diversity 更大？

完整审稿报告已在 Reviewer 1 session 中生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1281 · 2026-05-16T06:45:27.723369+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 99

## Round 99

2 recorded events


### User

_source line 1282 · 2026-05-16T06:45:30.401969+00:00_

[Reviewer 1 审稿结果]:
Round 1 审稿报告已完成并提交给 Review Director。

核心结论：**Overall 3.5/5（Borderline Findings/Conference）**。研究问题有价值，统计实践优秀，但两个 Must-Fix 问题需要解决：(1) selection gap 的有效验证仅限 SciERC 一个数据集，generalizability 不足；(2) framing 过度强调 instance-level signals 的 by-construction limitation，掩盖了 MBR failure 这一更有价值的 empirical finding。5 项 Should-Fix 中最重要的是缺少 greedy decoding baseline 和 N>16 的验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1283 · 2026-05-16T06:45:36.961444+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 100

## Round 100

6 recorded events


### User

_source line 1284 · 2026-05-16T06:45:38.469616+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)
**审查侧重**: 新颖性/贡献框架 + 相关工作完整性 + 写作/格式合规

---

## 总体评分
**Overall**: 3/5 (Findings)
**一句话总结**: 实验设计扎实、统计方法严谨的诊断性论文，但核心发现部分来自信号设计的定义性后果而非纯粹的经验发现，且缺乏有效解决方案，新颖性对 main conference 不足。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验覆盖全面（3 NER + 1 RE、2 模型族、温度/规模/N 消融），统计检验严格，但核心 claim 的 framing 混淆了 by-construction 与 empirical |
| Excitement | 2/5 | LP 压缩现象及 MBR 跨/内实例相关性分析有价值，但整体为增量扩展（vs Yao et al. 2026），且无可行解决方案 |
| Reproducibility | 4/5 | 训练配置完整，数据集公开，承诺代码释出 |
| Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、LLM-based IE 和 uncertainty estimation 文献 |

---

## Strengths

**S1.** QE 与 selection 的解耦是有价值的方法论贡献——Prior work 仅报告相关性未验证 selection 可行性。

**S2.** 统计方法论在 NLP empirical papers 中属上乘：bootstrap CI、TOST with 内外 margin、multi-seed Kendall's W、Fisher combined p-values。

**S3.** LP 压缩诊断链层次分明：全序列→entity-token（4× variance 但 selection 更差）→free-form（std ratio 0.97）→verbalized conf（更压缩）→non-tied subset（+2.9pp, p=0.004），系统排除多种假说，最终指向模型对 entity tokens 的过度自信。

**S4.** Appendix 质量高：FK independence test、LOO-SJ 等价证明、OOD schema transfer、SJ normalizer robustness。

**S5.** †RE hedging 诚实且一致，thinking-token confound 有三部分定量分析。

---

## Must-Fix 问题

**N1** [critical] Instance-level 信号的 "gap" 是设计的定义性后果，而非经验发现

- 位置：Section 3.1, Contribution 1 (Intro), Abstract lines 4-5
- 5 个信号中 4 个（SJ, VC, FK, EM）by construction 对同一 instance 所有 candidate 赋相同分数。MBR 转换是额外方法步骤而非 "gap" 本身。但 Abstract（"none improves"）、Intro Contribution 1 和 Conclusion 将 definitional failure 与 empirical failure（LP 压缩）混为同一现象。
- 影响接收：核心 claim novelty 定性。如果 gap 的 4/5 成分是 by-construction，novelty 主要集中在 LP 压缩和 MBR 跨/内不对称——有价值但范围更窄。
- 建议：Contribution 1 中明确区分 (a) MBR fails because utility correlates across but not within instances（empirical）和 (b) LP too compressed（empirical），移除将 instance-level signals "无法 select" 包装为 surprising 的 framing。

**N2** [critical] Contribution framing 相对 Yao et al. (2026) 夸大增量贡献

- 位置：Introduction line 8, Related Work §2 ¶2
- SJ vs EM 改进在 SciERC 仅 Δρ=+0.065（borderline, Table 8: "would not survive Bonferroni"），CoNLL 上 EM 反领先。QE/selection separation 受 N1 削弱。Difficulty gradient 是自然的 multi-dataset 延伸。
- 建议：重心放在 MBR 失败机制和 LP 压缩诊断上，structural matching 不应作为 universal improvement 呈现。

---

## Should-Fix 问题

**W1** [warning] 纯诊断无 remedy 削弱 contribution
- Entity-token LP 失败（-2.0pp），verbalized conf 失败（-2.45pp），non-tied LP 依赖 post-hoc ε。Limitations 承认 "LP×VC combinations remain unexplored"——这恰是最自然的 remedy。
- 建议：至少尝试一个 lightweight pilot（LP×VC、calibration-based rescoring）。

**W2** [warning] RE 覆盖过广但证据过弱
- RE 出现在 Abstract、所有主表、Discussion，但仅 SciERC 单 benchmark、40% zero-F1、多数单 seed。†RE 标记 >15 处，hedging noise 大。Free-form RE reversal 是最有趣发现但被埋在 appendix。
- 建议：全做（加 TACRED）或全移至 Appendix，当前策略两头不讨好。

**W3** [warning] Abstract 信息过度压缩
- 9 句覆盖 5 signals、MBR mechanics、LP 0.041 nats、free-form ablation、RE reversal。MBR conversion 机制和具体数字不适合 abstract。

---

## 小问题

- M1: `mejer2011confidence` key 年份 2011 但 entry 为 2010（EMNLP 2010）
- M2: `feng2025optimal` first author mismatch（Feng vs Austin，可能 first/last 倒置）
- M3: `hobelsberger2025`, `lightman2024`, `venktesh2025`, `zhang2025conformal` 在 OpenAlex 未匹配——建议核实
- M4: Table 2 caption "Fisher p" 与 Appendix "Fisher combined p" 术语不一致
- M5: Discussion §5 LP hypotheses (a)-(d) 并列结构不一致（"and" 重复使用）

---

## Questions

1. Non-tied LP subset 的 +2.9pp 在部署时需要 ground-truth 来选 ε。是否有 oracle-free proxy 可预测 LP 在哪些 instances 有 discriminative power？
2. SJ-utility 与 F1 的 within-instance ρ 具体是多少？接近 0 还是类似 LP 的 0.248？
3. LP×VC combination 是否有初步数据？

---

## Missing References

引用覆盖完整。50 entries, 0 orphan, 0 missing bib。Director 清单上所有关键引用均已覆盖（wang2023, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty, Eikema/Freitag/Deguchi MBR, Kuhn semantic uncertainty, Kadavath P(True), Mejer & Crammer, Xie self-evaluation, Zhang conformal）。

---

## 格式合规

- ✅ `\usepackage[review]{acl}` review mode
- ✅ `\author{Anonymous}` double-blind
- ✅ Limitations section 有实质内容（13 lines, 覆盖 RE/scale/verifier/N/free-form/thinking-token/temperature/verbalized/combinations/ε/entity-token LP）
- ✅ Ethics statement 存在
- ⚠️ 页数需编译确认（内容丰富，可能紧凑）

---

**Verdict**: Borderline — weak accept for Findings, not main conference。如果 (a) 重新 frame contributions 区分 by-construction/empirical, (b) 收窄 RE 覆盖, (c) 至少尝试一个 lightweight remedy, 论文将更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1285 · 2026-05-16T06:46:06.078674+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 完整审稿报告\n\n**Overall**: 3/5 (Findings track, not main conference)\n\n**Strengths**:\n- S1: QE 与 selection 的解耦是有价值的方法论贡献\n- S2: 统计方法论在 NLP empirical papers 中属上乘\n- S3: LP 压缩诊断链层次分明（全序列→entity-token→free-form→verbalized→non-tied subset）\n- S4: Appendix 质量高（FK independence, LOO-SJ, OOD, SJ normalizer）\n- S5: †RE hedging 诚实一致\n\n**Must-Fix**:\n- N1 [critical]: Instance-level 信号的 \"gap\" 是设计的定义性后果而非经验发现。4/5 信号 by construction 对同一 instance 赋相同分数。MBR 转换是额外方法步骤。Abstract/Intro/Conclusion 将 definitional failure 与 empirical failure（LP 压缩）混为同一现象。建议 Contribution 1 明确区分 (a) MBR across-vs-within asymmetry（empirical）和 (b) LP compression（empirical）。\n\n- N2 [critical]: Contribution framing 相对 Yao et al. (2026) 夸大增量贡献。SJ vs EM 改进仅 Δρ=+0.065（borderline, \"would not survive Bonferroni\"），CoNLL 上 EM 反领先。Difficulty gradient 是自然 multi-dataset 延伸。建议重心放在 MBR 失败机制和 LP 压缩诊断。\n\n**Should-Fix**:\n- W1: 纯诊断无 remedy（entity-token LP 失败, verbalized conf 失败, non-tied LP 依赖 post-hoc ε）。至少尝试一个 lightweight pilot（LP×VC, calibration-based rescoring）。\n- W2: RE 覆盖过广但证据过弱。†RE >15 处，hedging noise 大。Free-form RE reversal 是最有趣发现但被埋在 appendix。建议全做或全移 Appendix。\n- W3: Abstract 信息过度压缩（9 句覆盖 5 signals + MBR + LP 0.041 nats + free-form + RE reversal）。\n\n**Minor**:\n- M1: mejer2011confidence key 年份错误（实际 EMNLP 2010）\n- M2: feng2025optimal first author mismatch\n- M3: hobelsberger2025, lightman2024, venktesh2025, zhang2025conformal 在 OpenAlex 未匹配\n- M4: Table 2 caption \"Fisher p\" vs Appendix \"Fisher combined p\" 术语不一致\n- M5: Discussion LP hypotheses (a)-(d) \"and\" 重复\n\n**Questions**:\n1. Non-tied LP subset +2.9pp 部署时需 ground-truth 选 ε，是否有 oracle-free proxy？\n2. SJ-utility 与 F1 的 within-instance ρ 具体多少？\n3. LP×VC combination 是否有初步数据？\n\n**Missing References**: 无（50 entries, 0 orphan, 0 missing）\n\n**��式**: ✅ ACL review mode, ✅ anonymous, ✅ Limitations, ✅ Ethics, ⚠️ 页数需编译确认\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 完整审稿报告\n\n**Overall**: 3/5 (Findings track, not main conference)\n\n**Strengths**:\n- S1: QE 与 selection 的解耦是有价值的方法论贡献\n- S2: 统计方法论在 NLP empirical papers 中属上乘\n- S3: LP 压缩诊断链层次分明（全序列→entity-token→free-form→verbalized→non-tied subset）\n- S4: Appendix 质量高（FK independence, LOO-SJ, OOD, SJ normalizer）\n- S5: †RE hedging 诚实一致\n\n**Must-Fix**:\n- N1 [critical]: Instance-level 信号的 \"gap\" 是设计的定义性后果而非经验发现。4/5 信号 by construction 对同一 instance 赋相同分数。MBR 转换是额外方法步骤。Abstract/Intro/Conclusion 将 definitional failure 与 empirical failure（LP 压缩）混为同一现象。建议 Contribution 1 明确区分 (a) MBR across-vs-within asymmetry（empirical）和 (b) LP compression（empirical）。\n\n- N2 [critical]: Contribution framing 相对 Yao et al. (2026) 夸大增量贡献。SJ vs EM 改进仅 Δρ=+0.065（borderline, \"would not survive Bonferroni\"），CoNLL 上 EM 反领先。Difficulty gradient 是自然 multi-dataset 延伸。建议重心放在 MBR 失败机制和 LP 压缩诊断。\n\n**Should-Fix**:\n- W1: 纯诊断无 remedy（entity-token LP 失败, verbalized conf 失败, non-tied LP 依赖 post-hoc ε）。至少尝试一个 lightweight pilot（LP×VC, calibration-based rescoring）。\n- W2: RE 覆盖过广但证据过弱。†RE >15 处，hedging noise 大。Free-form RE reversal 是最有趣发现但被埋在 appendix。建议全做或全移 Appendix。\n- W3: Abstract 信息过度压缩（9 句覆盖 5 signals + MBR + LP 0.041 nats + free-form + RE reversal）。\n\n**Minor**:\n- M1: mejer2011confidence key 年份错误（实际 EMNLP 2010）\n- M2: feng2025optimal first author mismatch\n- M3: hobelsberger2025, lightman2024, venktesh2025, zhang2025conformal 在 OpenAlex 未匹配\n- M4: Table 2 caption \"Fisher p\" vs Appendix \"Fisher combined p\" 术语不一致\n- M5: Discussion LP hypotheses (a)-(d) \"and\" 重复\n\n**Questions**:\n1. Non-tied LP subset +2.9pp 部署时需 ground-truth 选 ε，是否有 oracle-free proxy？\n2. SJ-utility 与 F1 的 within-instance ρ 具体多少？\n3. LP×VC combination 是否有初步数据？\n\n**Missing References**: 无（50 entries, 0 orphan, 0 missing）\n\n**��式**: ✅ ACL review mode, ✅ anonymous, ✅ Limitations, ✅ Ethics, ⚠️ 页数需编译确认\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix、Minor 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 1286 · 2026-05-16T06:46:18.798791+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 12720
}
```

</details>

---


### Tool call

_source line 1287 · 2026-05-16T06:46:18.850798+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 完整审稿报告\n\n**Overall**: 3.5/5 (Borderline Findings/Conference)\n**Confidence**: 4/5\n\n**核心判断**: 研究问题新颖（QE vs selection 解耦），统计实践扎实，但两个关键问题需要解决。\n\n**Must-Fix**:\n- N1: Selection gap 的 effective test bed 仅限 SciERC（CoNLL 是 ceiling-effect control，WNUT collapse）。标题和 abstract 暗示 NER 普遍现��，但实证仅来自���个科学领域数据集（n=529）。建议增加中等难度数据集或收窄 claim scope。\n\n- N2: Framing 过度强调 \"4/5 signals assign identical scores\"（by-construction trivial），模糊了核�� empirical finding（MBR conversion 产生 per-sample rankings 后仍然失败，因为 utility 在 across-instances 而非 within-instance 维度与 F1 相关）。当前叙事使读者误以��� gap 对 instance-level signals 是显而易见的定义问题。\n\n**Should-Fix**:\n- W1: ρ=0.45 称 \"moderate-to-strong\" 但此值来自 ceiling-effect 数据集 CoNLL；SciERC 上最佳仅 ρ=0.379。\n- W2: N≤16 不足以支撑 scaling claim，需 N=32+ 验证。\n- W3: 缺少 greedy decoding baseline——部署决策的核心对照。\n- W4: 3 seeds 下 Kendall W=1.000 统计信息量不足。\n- W5: Soft Jaccard 命名不准确（分母用 max 非 union）。\n\n**主要优势**:\n- Entity-token LP 消融深层诊断\n- Free-form ablation 4-seed RE reversal\n- 统计实践（TOST 循环论证识别与外部锚��）\n- Honest negative-result reporting\n\n**Questions**:\n- Q1: 是否尝试过 soft selection / weighted fusion 而非 hard argmax MBR?\n- Q2: Oracle headroom 依赖 gold annotations，部��时如何估计？\n- Q3: Entity-token LP variance 在 CoNLL vs SciERC 的巨大差异是否与 entity type diversity 有关？\n- Q4: RE LP reversal 的 constrained baseline 仅 single-seed，reversal magnitude 相对 seed variance 是否显著？\n- Q5: 4B QE 优于 8B 的 counterintuitive finding 是否因 output diversity 更大？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix 和 Questions。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每一条使用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 完整审稿报告\n\n**Overall**: 3.5/5 (Borderline Findings/Conference)\n**Confidence**: 4/5\n\n**核心判断**: 研究问题新颖（QE vs selection 解耦），统计实践扎实，但两个关键问题需要解决。\n\n**Must-Fix**:\n- N1: Selection gap 的 effective test bed 仅限 SciERC（CoNLL 是 ceiling-effect control，WNUT collapse）。标题和 abstract 暗示 NER 普遍现��，但实证仅来自���个科学领域数据集（n=529）。建议增加中等难度数据集或收窄 claim scope。\n\n- N2: Framing 过度强调 \"4/5 signals assign identical scores\"（by-construction trivial），模糊了核�� empirical finding（MBR conversion 产生 per-sample rankings 后仍然失败，因为 utility 在 across-instances 而非 within-instance 维度与 F1 相关）。当前叙事使读者误以��� gap 对 instance-level signals 是显而易见的定义问题。\n\n**Should-Fix**:\n- W1: ρ=0.45 称 \"moderate-to-strong\" 但此值来自 ceiling-effect 数据集 CoNLL；SciERC 上最佳仅 ρ=0.379。\n- W2: N≤16 不足以支撑 scaling claim，需 N=32+ 验证。\n- W3: 缺少 greedy decoding baseline——部署决策的核心对照。\n- W4: 3 seeds 下 Kendall W=1.000 统计信息量不足。\n- W5: Soft Jaccard 命名不准确（分母用 max 非 union）。\n\n**主要优势**:\n- Entity-token LP 消融深层诊断\n- Free-form ablation 4-seed RE reversal\n- 统计实践（TOST 循环论证识别与外部锚��）\n- Honest negative-result reporting\n\n**Questions**:\n- Q1: 是否尝试过 soft selection / weighted fusion 而非 hard argmax MBR?\n- Q2: Oracle headroom 依赖 gold annotations，部��时如何估计？\n- Q3: Entity-token LP variance 在 CoNLL vs SciERC 的巨大差异是否与 entity type diversity 有关？\n- Q4: RE LP reversal 的 constrained baseline 仅 single-seed，reversal magnitude 相对 seed variance 是否显著？\n- Q5: 4B QE 优于 8B 的 counterintuitive finding 是否因 output diversity 更大？\n\n---\n\n请逐条回应上述所有 Must-Fix、Should-Fix 和 Questions。"
  }
}
```

</details>

---


### Tool result

_source line 1288 · 2026-05-16T06:46:20.311352+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1460
}
```

</details>

---


### Assistant

_source line 1289 · 2026-05-16T06:46:23.165535+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条��应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1290 · 2026-05-16T06:46:25.765453+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Overall 3/5 (Findings level)**，主要问题是：

1. **N1 [critical]**: "Correlation-selection gap" 对 4/5 instance-level 信号是设计的定义性后果（by construction 无法区分 candidates），不应与 LP 压缩的经验发现混为同一现象
2. **N2 [critical]**: 相对 Yao et al. (2026) 的增量贡献被 framing 夸大——SJ vs EM 改进仅 borderline significant
3. **W1–W3**: 纯诊断无 remedy、RE 覆盖策略不统一、Abstract 过度压缩

优势方面：统计方法论严谨（bootstrap CI, TOST, multi-seed stability）、LP 压缩诊断链层次分明、Appendix 质量高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1291 · 2026-05-16T06:46:30.632390+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 102

## Round 102

2 recorded events


### User

_source line 1292 · 2026-05-16T06:48:06.347901+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 Reviewer 2 完成

### 同意的条目
- **R2-N1** (definitional vs empirical): 完全同意，与我的 R1-N2 一致
- **R2-W2** (RE 覆盖过广): 同意，建议全移 appendix
- **R2-W3** (Abstract 过度压缩): 同意
- **R2-M1–M5**: 全部同意
- **R2-Q1–Q3**: 全部同意是有价值的问题，特别是 Q2（SJ-utility within-instance ρ 缺失）是支撑核心 claim 的关键数据空白

### 有分歧的条目
- **R2-N2** (贡献 incremental): 部分同意。SJ vs EM (Δρ=+0.065, borderline) 和 difficulty gradient 确实不强，但 QE-selection separation 和 LP compression diagnostic chain（全序列→entity-token→free-form→verbalized→non-tied，涉及 5 层消融）是超越 Yao et al. 的 non-trivial 贡献。R2 的修改建议方向正确（重心转向 MBR failure + LP diagnostics），但不应将整体贡献判为仅 incremental。

- **R2-W1** (无 remedy): 同意 LP×VC 缺席遗憾，但诊断性论文不必须包含 remedy（ARR H13: "additional experiments could be performed" 非自动 weakness）。

### Overall 分歧
R2: 3/5 (Findings) vs R1: 3.5/5 (Borderline)
分歧核心：R2 对 SJ contribution 和 difficulty gradient 的批评合理，但 LP compression diagnostic chain 和 entity-token ablation 的独立价值被低估。修正 framing（N1/N2）后论文贡献更清晰。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1293 · 2026-05-16T06:48:11.357043+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1294 · 2026-05-16T06:48:13.959285+00:00_

[Reviewer 1 审稿结果]:
交叉回应已完成并提交。核心结论：与 R2 在 N1（definitional vs empirical framing）、W2–W3、所有 Minor 和 Questions 上一致；在 N2（overall contribution）和 W1（remedy necessity）上有程度分歧——我认为 LP diagnostic chain 的独立价值使论文高于 pure Findings level。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1295 · 2026-05-16T06:48:18.769914+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 104

## Round 104

10 recorded events


### User

_source line 1296 · 2026-05-16T06:48:53.165002+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

---

### Must-Fix

**[AGREE] R1-N1: Selection gap effective test bed 仅限 SciERC**

同意实质性问题。CoNLL 是 ceiling-effect control（论文自认, Section 4.3 line 92），WNUT collapse（Table 5），selection 分析实际仅 SciERC n=529。LLaMA SciERC 复制（Table 6: 相同 pattern）增加了模型维度的信心，4B ablation 也一致（Section 4.4），但仍限于单一科学领域。Title 和 Abstract "three NER benchmarks" 超出 effective test bed 支撑。增加中等难度数据集的建议合理。

**[AGREE] R1-N2: Framing 过度强调 by-construction trivial 部分**

强烈同意，这与我的 N1 一致。R1 的表述更精准：核心 empirical finding 是 MBR conversion 产生 per-sample rankings 后仍失败（across vs within instance 相关性不对称，Discussion ¶2, Appendix K），而非 "instance-level signals can't select"（trivial）。Section 4.3 line 85 的叙述容易让读者误读为 definitional 问题。

---

### Should-Fix

**[AGREE] R1-W1: ρ=0.45 的 headline number 来自 ceiling 数据集**

Table 1 ρ=0.451 来自 CoNLL Qwen EM，SciERC 最佳仅 VC ρ=0.379。应使用 primary test bed 数值。

**[REBUT] R1-W2: N≤16 不足以支撑 scaling claim**

论文的 scaling claim 是 diminishing returns（"N=8 captures most benefit", Appendix D），不是 large-N asymptotic。Selection gap 是 signal-level 问题（LP 压缩、MBR within-instance 失败）而非 sample-size 问题：N=16 CoNLL VC 仅 capture 10% oracle headroom（Appendix D line 261）。不过同意 QE 的 N-scaling claim 可从 N=32 数据点获益。

**[AGREE] R1-W3: 缺少 greedy decoding baseline**

合理遗漏。"Single" = one T=1.0 draw（非 argmax）。Greedy 是部署中最自然的 no-cost baseline，无论结果如何都对叙事有价值。

**[AGREE] R1-W4: 3 seeds Kendall W=1.000 统计信息量不足**

论文自己承认（Appendix J line 890: "statistical power with n=3 is limited"）。不应被 overclaimed。

**[REBUT] R1-W5: Soft Jaccard 命名不准确**

论文在 Eq 4 footnote 明确说明 max vs union 差异，Appendix C Table 4 验证 |Δρ|<0.01。Naming 不完全精确但完全透明，不影响结论。是 terminology preference 而非实质问题。

---

### Questions

**Q1 (soft selection/fusion)**: 合理建议。VC selection 已做某种 soft fusion（majority vote entity union），但 LP-weighted 多 sample fusion 未测试，值得探索。

**Q2 (oracle headroom deployment)**: 诊断性论文的固有局限。核心 argument 不依赖 headroom 绝对值——signal ≈ single-sample 已说明信号无效。

**Q3 (entity-token LP variance 差异)**: 合理假设。CoNLL 4 types 高频清晰 → near-deterministic；SciERC 6 types 稀有多样 → 更多 variation。论文未直接分析，值得补充。

**[REBUT] Q4 (RE reversal single-seed)**: Appendix I 报告 4-seed 完整数据：+1.69/+1.76/+2.00/+1.91pp（σ=0.12pp），远小于 reversal magnitude（~2.5pp swing）。Reversal 是 robust 的。

**Q5 (4B > 8B 因 diversity)**: 最合理解释。较小模型相同温度产生更多样 outputs，给 consistency signals 更大 dynamic range。Table 7 仅有 8B 数据，缺 4B 对比。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1297 · 2026-05-16T06:49:30.044613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "630",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "630",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1298 · 2026-05-16T06:49:30.145736+00:00_

630	    status: in_progress
631	  resolution: ""
632	  resolution_round: null
633	
634	# ===== CARRIED FORWARD (status unchanged) =====
635	- id: R9-W2
636	  summary: "orphan bib entries 未在正文引用"
637	  category: writing
638	  severity: warning
639	  status: open
640	  first_raised_round: 9
641	  last_seen_round: 12
642	  mentions:
643	  - round: 9
644	    reviewers: [1, 2]
645	    note: "24 个 orphan entries"
646	  - round: 12
647	    reviewers: [2]
648	    note: "R2 引用完整性检查: 47 entries, 0 orphan. 可能已修复, 待 Research Director 确认."
649	  action_items:
650	  - round: 9
651	    action: "引用相关 entries 或删除不相关的"
652	    assigned_to: Paper Agent
653	    status: in_progress
654	  resolution: ""
655	  resolution_round: null
656	
657	- id: R9-M4
658	  summary: "rho rounding 不精确"
659	  category: writing
660	  severity: info
661	  status: open
662	  first_raised_round: 9
663	  last_seen_round: 9
664	  mentions:
665	  - round: 9
666	    reviewers: [1, 2]
667	    note: "统一小数位数"
668	  - round: 12
669	    reviewers: []
670	    note: "R12 未被独立提及, 可能已修复"
671	  action_items:
672	  - round: 9
673	    action: "统一小数位数"
674	    assigned_to: Paper Agent
675	    status: open
676	  resolution: ""
677	  resolution_round: null
678	
679	- id: R9-M5
680	  summary: "Selection table NER/RE 统计标准不一致"
681	  category: writing
682	  severity: info
683	  status: in_progress
684	  first_raised_round: 9
685	  last_seen_round: 12
686	  mentions:
687	  - round: 11
688	    reviewers: [1]
689	    note: "NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p"
690	  - round: 12
691	    reviewers: [1, 2]
692	    note: "与 R11-M1 合并处理"
693	  action_items:
694	  - round: 9
695	    action: "统一统计报告标准"
696	    assigned_to: Paper Agent
697	    status: in_progress
698	  resolution: ""
699	  resolution_round: null
700	
701	- id: R9-M6
702	  summary: "Bib name order issues"
703	  category: writing
704	  severity: info
705	  status: open
706	  first_raised_round: 9
707	  last_seen_round: 9
708	  action_items:
709	  - round: 9
710	    
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1299 · 2026-05-16T06:49:45.206751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "729",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "729",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1300 · 2026-05-16T06:49:45.257372+00:00_

729	    note: "R12: R1-Q5 提出应更突出呈现 RE reversal. R2 rebut: 单 benchmark + 40% zero-F1, 谨慎处理适当, 但可定位为 promising direction. 共识: 不作为 positive result 突出, 但应更积极讨论."
730	  action_items:
731	  - round: 12
732	    action: "Discussion 将 RE free-form reversal 定位为 promising direction 而非纯 caveat"
733	    assigned_to: Paper Agent
734	    status: in_progress
735	  resolution: ""
736	  resolution_round: null
737	
738	- id: R11-W8
739	  summary: "Thinking token CoNLL control 论证薄弱"
740	  category: experiment
741	  severity: info
742	  status: in_progress
743	  first_raised_round: 11
744	  last_seen_round: 11
745	  mentions:
746	  - round: 11
747	    reviewers: [1, 2]
748	    note: "CoNLL 高 tied fraction 更可能因 task easiness. 其他两个论证较强, 整体充分"
749	  - round: 12
750	    reviewers: []
751	    note: "R12 未被独立提及"
752	  action_items:
753	  - round: 11
754	    action: "弱化 CoNLL control 论证或补充 task easiness 混淆说明"
755	    assigned_to: Paper Agent
756	    status: in_progress
757	  resolution: ""
758	  resolution_round: null
759	
760	- id: R11-M2
761	  summary: "Figure 1 caption 对 LP per-sample signal 不适用"
762	  category: writing
763	  severity: info
764	  status: in_progress
765	  first_raised_round: 11
766	  last_seen_round: 11
767	  mentions:
768	  - round: 11
769	    reviewers: [1, 2]
770	    note: "共识"
771	  - round: 12
772	    reviewers: []
773	    note: "R12 未被独立提及"
774	  action_items:
775	  - round: 11
776	    action: "修改 Figure 1 caption"
777	    assigned_to: Paper Agent
778	    status: in_progress

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1301 · 2026-05-16T06:53:22.730114+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (updated Round 13) =====\n- id: R0-C3\n  summary: \"RE 结论仅基于 SciERC 单数据集, selection gap effective test bed 仅 SciERC\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 13\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529). CoNLL 是 ceiling-effect control (论文自认), WNUT collapse. 标题/Abstract 'three NER benchmarks' 超出 effective test bed 支撑. R2 补充: LLaMA SciERC 复制和 4B ablation 增加模型维度信心, 但仍限于单一科学领域.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 12\n    action: \"Title→NER (D106). TACRED 不可行 (D105 结构不兼容).\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集. 避免 'three NER benchmarks' 暗示三个数据集都验证了 selection gap.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological, instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 核心 empirical finding 是 MBR conversion 产生 per-sample rankings 后仍失败 (across vs within instance 相关性不对称). '4/5 signals assign identical scores' 是 by-construction trivial, 不应作为 surprising finding 呈现. Section 4.3 line 85 叙述容易让读者误读. R1: 叙事使读者误以为 gap 对 instance-level signals 是显而易见的. R2: Abstract 'none improves', Intro Contribution 1, Conclusion 将 definitional failure 与 empirical failure 混为同一. 已持续 11 轮, 仍是最核心 framing 问题.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重���: 删除 'by construction', MBR failure→empirical, Appendix L→主文 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"Contribution 1 明确区分: (a) MBR across-vs-within asymmetry (empirical) + (b) LP compression (empirical). 移除将 instance-level 'cannot select' 包装为 surprising 的 framing.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 12\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, ε降为辅助\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文已使用 pooled within-instance ρ=0.248 和 CDF 特征作为主叙事. 可能已改善.\"\n  action_items:\n  - round: 12\n    action: \"Abstract '60% tied'→continuous, ε降为辅助 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R2 再次标为 Must-Fix (SJ vs EM Δρ=+0.065 borderline, difficulty gradient 是自然延伸). R1 部分同意但辩护 LP diagnostic chain (全序列→entity-token→free-form→verbalized→non-tied, 5层消融) 和 QE-selection separation 是超越 Yao 的 non-trivial 贡献. 共识: structural matching 不应作为 universal improvement 呈现, 重心应转向 MBR failure mechanism + LP diagnostics.\"\n  action_items:\n  - round: 12\n    action: \"Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"重心转向 MBR failure + LP diagnostics 作为核心贡献, structural matching 降级为 methodological choice\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识. 3B-8B 本质是同一 capability tier.\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文 Conclusion 已限定 'in the small-model regime (3B-8B)'. 可能已改善.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.000 p≈0.05 仅 borderline significant\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 两位再次同意. Appendix 承认 power limited 但正文未体现. R2 引用 Appendix J line 890 自我承认.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp 暗示组合策略可能有效\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"聚焦到 entity-token-only LP, 共识至少应尝试\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: Entity-token LP 已在 Discussion 报告 (4× variance 但 selection -2.0pp, CoNLL near-zero). 实验已执行且结果纳入论文. R2-W1 仍建议 LP×VC combination, 但 entity-token LP 本身已完成.\"\n  action_items:\n  - round: 12\n    action: \"Entity-token LP re-inference + 分析\"\n    assigned_to: Main Agent\n    status: done\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"11+ 次 preliminary, 建议首次说明后用 dagger 标记\"\n  - round: 12\n    reviewers: []\n    note: \"论文已改用 †RE 标记体系\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被提及. 论文使用 †RE 标记一致.\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 次数, 用 dagger 替代\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"论文已统一使用 †RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 token averaging, schema-enforced tokens, vocabulary 缩小等 hypotheses\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Discussion 已列出 (a)(b)(c)(d) 四个 hypotheses, 但标注 'three mechanisms' 编号错误\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未独立提及编号问题. R2-M5 提到 (a)-(d) 并列结构不一致 ('and' 重复). 编号错误可能未修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four' mechanisms\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax\"\n  - round: 12\n    reviewers: []\n    note: \"Table 2 已改为 'Single‡' 标注 T=1.0 draw\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R1-W3 明确提出缺少 greedy (argmax) decoding baseline——部署决策的核心对照. R2 同意. 'Single' = T=1.0 draw, 不等于 greedy. Greedy 是部署中最自然的 no-cost baseline.\"\n  action_items:\n  - round: 11\n    action: \"全文统一为 single-sample baseline\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"增加 greedy (T=0, argmax) decoding baseline 实验结果\"\n    assigned_to: Main Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"需解释原因\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. Table 2 footnote 已解释 'RE serves as exploratory extension on single benchmark'. 可能已充分.\"\n  action_items:\n  - round: 12\n    action: \"在正文或 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes 2022, CSP, Beyond Confidence\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"新增: Deguchi 2024, Mejer & Crammer 2011, Xie 2024\"\n  - round: 13\n    reviewers: [2]\n    note: \"R13 R2 引用完整性检查: 50 entries, 0 orphan, 0 missing bib. 所有关键引用均已覆盖 (wang2023, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty, Eikema/Freitag/Deguchi MBR, Kuhn semantic uncertainty, Kadavath P(True), Mejer & Crammer, Xie self-evaluation, Zhang conformal).\"\n  action_items:\n  - round: 12\n    action: \"补充: Deguchi et al. (2024), Mejer & Crammer (2011), Xie et al. (2024)\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出, 但应更积极讨论\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文 Abstract 和 Discussion 已包含 RE reversal 描述.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. Figure 1 caption 当前版本已含 LP 说明.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ISSUES FROM ROUND 12 (updated R13) =====\n- id: R12-N1\n  summary: \"ρ=0.45 描述为 strong quality estimation, 实际最佳 primary dataset 仅 ρ=0.379\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: Should-Fix, 改措辞为 moderate-to-strong 或加限定语\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 R1-W1 再次提出: ρ=0.45 headline 来自 ceiling-effect 数据集 CoNLL (EM ρ=0.451); primary test bed SciERC 上最佳仅 VC ρ=0.379. R2 同意. 论文 Abstract 已改用 'moderate-to-strong' 但仍以 ρ=0.45 作为 headline number.\"\n  action_items:\n  - round: 12\n    action: \"将 'strong quality estimation' 改为 'moderate-to-strong'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"Abstract/Intro headline number 改用 primary dataset (SciERC) 数值, 或明确标注 ρ=0.45 来自 ceiling-effect dataset\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: Entity-token LP 已测试但失败 (-2.0pp). R2 仍标为 Should-Fix, 建议 LP×VC 或 calibration-based rescoring. R1 同意 LP×VC 缺席遗憾, 但辩护诊断性论文不必须包含 remedy (ARR H13). 部分分歧: R1 认为不是 blocking, R2 认为影响 excitement.\"\n  action_items:\n  - round: 12\n    action: \"增加至少一个 pilot remedy 实验\"\n    assigned_to: Main Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Section 3.3 vs Table A13 n 值不一致\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 可能已修正或 reviewer 未注意.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"两位独立标记\"\n  - round: 13\n    reviewers: [2]\n    note: \"R13 R2-M5 提到 (a)-(d) 并列结构不一致. 编号错误可能未修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Eq.4 用 max(|g_i|,|g_j|) 而非 |A∪B|\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R1-W5 再次提���. R2 rebut: Eq 4 footnote 已明确说明, Appendix Table 4 验证 |Δρ|<0.01, 完全透明. 共识降级: terminology preference, 非实质问题.\"\n  action_items:\n  - round: 12\n    action: \"改名为 Soft Overlap Score 或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [2]\n    note: \"OpenAlex 匹配 2026 版本\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及\"\n  action_items:\n  - round: 12\n    action: \"核实并更新 bib year\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 13) =====\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在所有主表+Abstract 但仅 SciERC 单 benchmark + 40% zero-F1\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2-W2: RE 出现在 Abstract、所有主表、Discussion, 但 †RE >15 处 hedging noise 大. Free-form RE reversal 是最有趣发现但被埋 appendix. R1 同意全移 appendix. 共识: 全做 (加 TACRED) 或全移 Appendix, 当前策略两头不讨好.\"\n  action_items:\n  - round: 13\n    action: \"决策: RE 全移 Appendix (作为 exploratory extension), 或增加第二个 RE benchmark. 当前混合呈现策略削弱论文.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 (9句覆盖全部机制和数字)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2-W3: 9 句覆盖 5 signals、MBR mechanics、LP 0.041 nats、free-form ablation、RE reversal. MBR conversion 机制和具体数字不适合 abstract. R1 同意.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract: 移除 MBR mechanical 细节和具体数字 (0.041 nats), 保留 problem-finding-significance 结构\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M1\n  summary: \"Bib 年份/作者问题: mejer2011→2010, feng2025 author mismatch, 多条未匹配 OpenAlex\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"M1: mejer2011confidence 实际是 EMNLP 2010. M2: feng2025optimal first author mismatch. M3: hobelsberger2025, lightman2024, venktesh2025, zhang2025conformal 未匹配 OpenAlex.\"\n  action_items:\n  - round: 13\n    action: \"核实并修正: mejer key→2010, feng2025 author order, 验证 4 条 unmatched entries\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"术语应统一\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"24 个 orphan entries\"\n  - round: 12\n    reviewers: [2]\n    note: \"47 entries, 0 orphan. 可能已修复.\"\n  - round: 13\n    reviewers: [2]\n    note: \"R13 R2 引用完整性检查: 50 entries, 0 orphan. 已修复.\"\n  action_items:\n  - round: 9\n    action: \"引用相关 entries 或删除不相关的\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"统一小数位数\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文当前统一使用 3 位小数.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"与 R11-M1 合并处理\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. Table 2 footnote 已解释.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n\n# ===== RECURRING ISSUES (updated Round 13) =====\n- id: R0-C3\n  summary: \"RE 结论仅基于 SciERC 单数据集, selection gap effective test bed 仅 SciERC\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 13\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529). CoNLL 是 ceiling-effect control (论文自认), WNUT collapse. 标题/Abstract 'three NER benchmarks' 超出 effective test bed 支撑. R2 补充: LLaMA SciERC 复制和 4B ablation 增加模型维度信心, 但仍限于单一科学领域.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 12\n    action: \"Title→NER (D106). TACRED 不可行 (D105 结构不兼容).\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集. 避免 'three NER benchmarks' 暗示三个数据集都验证了 selection gap.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological, instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 核心 empirical finding 是 MBR conversion 产生 per-sample rankings 后仍失败 (across vs within instance 相关性不对称). '4/5 signals assign identical scores' 是 by-construction trivial, 不应作为 surprising finding 呈现. Section 4.3 line 85 叙述容易让读者误读. R1: 叙事使读者误以为 gap 对 instance-level signals 是显而易见的. R2: Abstract 'none improves', Intro Contribution 1, Conclusion 将 definitional failure 与 empirical failure 混为同一. 已持续 11 轮, 仍是最核心 framing 问题.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重���: 删除 'by construction', MBR failure→empirical, Appendix L→主文 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"Contribution 1 明确区分: (a) MBR across-vs-within asymmetry (empirical) + (b) LP compression (empirical). 移除将 instance-level 'cannot select' 包装为 surprising 的 framing.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 12\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, ε降为辅助\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文已使用 pooled within-instance ρ=0.248 和 CDF 特征作为主叙事. 可能已改善.\"\n  action_items:\n  - round: 12\n    action: \"Abstract '60% tied'→continuous, ε降为辅助 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R2 再次标为 Must-Fix (SJ vs EM Δρ=+0.065 borderline, difficulty gradient 是自然延伸). R1 部分同意但辩护 LP diagnostic chain (全序列→entity-token→free-form→verbalized→non-tied, 5层消融) 和 QE-selection separation 是超越 Yao 的 non-trivial 贡献. 共识: structural matching 不应作为 universal improvement 呈现, 重心应转向 MBR failure mechanism + LP diagnostics.\"\n  action_items:\n  - round: 12\n    action: \"Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"重心转向 MBR failure + LP diagnostics 作为核心贡献, structural matching 降级为 methodological choice\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识. 3B-8B 本质是同一 capability tier.\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文 Conclusion 已限定 'in the small-model regime (3B-8B)'. 可能已改善.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.000 p≈0.05 仅 borderline significant\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 两位再次同意. Appendix 承认 power limited 但正文未体现. R2 引用 Appendix J line 890 自我承认.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP non-tied subset +2.9pp 暗示组合策略可能有效\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"聚焦到 entity-token-only LP, 共识至少应尝试\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: Entity-token LP 已在 Discussion 报告 (4× variance 但 selection -2.0pp, CoNLL near-zero). 实验已执行且结果纳入论文. R2-W1 仍建议 LP×VC combination, 但 entity-token LP 本身已完成.\"\n  action_items:\n  - round: 12\n    action: \"Entity-token LP re-inference + 分析\"\n    assigned_to: Main Agent\n    status: done\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"11+ 次 preliminary, 建议首次说明后用 dagger 标记\"\n  - round: 12\n    reviewers: []\n    note: \"论文已改用 †RE 标记体系\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被提及. 论文使用 †RE 标记一致.\"\n  action_items:\n  - round: 11\n    action: \"减少 preliminary 次数, 用 dagger 替代\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"论文已统一使用 †RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 token averaging, schema-enforced tokens, vocabulary 缩小等 hypotheses\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Discussion 已列出 (a)(b)(c)(d) 四个 hypotheses, 但标注 'three mechanisms' 编号错误\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未独立提及编号问题. R2-M5 提到 (a)-(d) 并列结构不一致 ('and' 重复). 编号错误可能未修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four' mechanisms\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax\"\n  - round: 12\n    reviewers: []\n    note: \"Table 2 已改为 'Single‡' 标注 T=1.0 draw\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R1-W3 明确提出缺少 greedy (argmax) decoding baseline——部署决策的核心对照. R2 同意. 'Single' = T=1.0 draw, 不等于 greedy. Greedy 是部署中最自然的 no-cost baseline.\"\n  action_items:\n  - round: 11\n    action: \"全文统一为 single-sample baseline\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"增加 greedy (T=0, argmax) decoding baseline 实验结果\"\n    assigned_to: Main Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"需解释原因\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. Table 2 footnote 已解释 'RE serves as exploratory extension on single benchmark'. 可能已充分.\"\n  action_items:\n  - round: 12\n    action: \"在正文或 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Fernandes 2022, CSP, Beyond Confidence\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"新增: Deguchi 2024, Mejer & Crammer 2011, Xie 2024\"\n  - round: 13\n    reviewers: [2]\n    note: \"R13 R2 引用完整性检查: 50 entries, 0 orphan, 0 missing bib. 所有关键引用均已覆盖 (wang2023, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty, Eikema/Freitag/Deguchi MBR, Kuhn semantic uncertainty, Kadavath P(True), Mejer & Crammer, Xie self-evaluation, Zhang conformal).\"\n  action_items:\n  - round: 12\n    action: \"补充: Deguchi et al. (2024), Mejer & Crammer (2011), Xie et al. (2024)\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出, 但应更积极讨论\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文 Abstract 和 Discussion 已包含 RE reversal 描述.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. Figure 1 caption 当前版本已含 LP 说明.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ISSUES FROM ROUND 12 (updated R13) =====\n- id: R12-N1\n  summary: \"ρ=0.45 描述为 strong quality estimation, 实际最佳 primary dataset 仅 ρ=0.379\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: Should-Fix, 改措辞为 moderate-to-strong 或加限定语\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 R1-W1 再次提出: ρ=0.45 headline 来自 ceiling-effect 数据集 CoNLL (EM ρ=0.451); primary test bed SciERC 上最佳仅 VC ρ=0.379. R2 同意. 论文 Abstract 已改用 'moderate-to-strong' 但仍以 ρ=0.45 作为 headline number.\"\n  action_items:\n  - round: 12\n    action: \"将 'strong quality estimation' 改为 'moderate-to-strong'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"Abstract/Intro headline number 改用 primary dataset (SciERC) 数值, 或明确标注 ρ=0.45 来自 ceiling-effect dataset\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: Entity-token LP 已测试但失败 (-2.0pp). R2 仍标为 Should-Fix, 建议 LP×VC 或 calibration-based rescoring. R1 同意 LP×VC 缺席遗憾, 但辩护诊断性论文不必须包含 remedy (ARR H13). 部分分歧: R1 认为不是 blocking, R2 认为影响 excitement.\"\n  action_items:\n  - round: 12\n    action: \"增加至少一个 pilot remedy 实验\"\n    assigned_to: Main Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Section 3.3 vs Table A13 n 值不一致\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 可能已修正或 reviewer 未注意.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"两位独立标记\"\n  - round: 13\n    reviewers: [2]\n    note: \"R13 R2-M5 提到 (a)-(d) 并列结构不一致. 编号错误可能未修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Eq.4 用 max(|g_i|,|g_j|) 而非 |A∪B|\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R1-W5 再次提���. R2 rebut: Eq 4 footnote 已明确说明, Appendix Table 4 验证 |Δρ|<0.01, 完全透明. 共识降级: terminology preference, 非实质问题.\"\n  action_items:\n  - round: 12\n    action: \"改名为 Soft Overlap Score 或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [2]\n    note: \"OpenAlex 匹配 2026 版本\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及\"\n  action_items:\n  - round: 12\n    action: \"核实并更新 bib year\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 13) =====\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在所有主表+Abstract 但仅 SciERC 单 benchmark + 40% zero-F1\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2-W2: RE 出现在 Abstract、所有主表、Discussion, 但 †RE >15 处 hedging noise 大. Free-form RE reversal 是最有趣发现但被埋 appendix. R1 同意全移 appendix. 共识: 全做 (加 TACRED) 或全移 Appendix, 当前策略两头不讨好.\"\n  action_items:\n  - round: 13\n    action: \"决策: RE 全移 Appendix (作为 exploratory extension), 或增加第二个 RE benchmark. 当前混合呈现策略削弱论文.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 (9句覆盖全部机制和数字)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R2-W3: 9 句覆盖 5 signals、MBR mechanics、LP 0.041 nats、free-form ablation、RE reversal. MBR conversion 机制和具体数字不适合 abstract. R1 同意.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract: 移除 MBR mechanical 细节和具体数字 (0.041 nats), 保留 problem-finding-significance 结构\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M1\n  summary: \"Bib 年份/作者问题: mejer2011→2010, feng2025 author mismatch, 多条未匹配 OpenAlex\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"M1: mejer2011confidence 实际是 EMNLP 2010. M2: feng2025optimal first author mismatch. M3: hobelsberger2025, lightman2024, venktesh2025, zhang2025conformal 未匹配 OpenAlex.\"\n  action_items:\n  - round: 13\n    action: \"核实并修正: mejer key→2010, feng2025 author order, 验证 4 条 unmatched entries\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"术语应统一\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"24 个 orphan entries\"\n  - round: 12\n    reviewers: [2]\n    note: \"47 entries, 0 orphan. 可能已修复.\"\n  - round: 13\n    reviewers: [2]\n    note: \"R13 R2 引用完整性检查: 50 entries, 0 orphan. 已修复.\"\n  action_items:\n  - round: 9\n    action: \"引用相关 entries 或删除不相关的\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"统一小数位数\"\n  - round: 12\n    reviewers: []\n    note: \"R12 未被独立提及\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文当前统一使用 3 位小数.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"NER 2-seed mean+sigma + Fisher p, RE 单 seed 无 p\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"与 R11-M1 合并处理\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. Table 2 footnote 已解释.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1302 · 2026-05-16T06:53:22.831533+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 25742}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1303 · 2026-05-16T06:55:11.629930+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# Round 13 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)\n**Reviewers**: 2 人 (R1: 方法/实验/统计; R2: 新颖性/相关工作/写作)\n**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛\n\n---\n\n## Summary\n\n论文研究 LLM-based NER 中 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 quality estimation 和 best-of-N selection 两个维度的表现差异。核心发现是 \"correlation-selection gap\"：signals 达到 moderate QE（Spearman ρ 至 0.45）但无法改善 sample selection。诊断链深入分析了 LP 压缩机制（entity-token ablation、free-form ablation、verbalized confidence）。实验覆盖 3 个 NER + 1 个 RE 数据集、2 个模型族、4B/8B scale。\n\n---\n\n## Strengths\n\n1. **QE/selection 解耦的方法论价值** [共识]：Prior work 仅报告 consistency-accuracy 相关性（Yao et al. 2026），本文首次系统验证 QE 不等价于 selection，并定量化 oracle headroom（13-18pp）与实际 selection gain（≈0pp）的落差。\n\n2. **统计方法论严谨** [共识]：Bootstrap CI with Bonferroni、TOST equivalence testing with 内外锚定（识别并解决了 oracle-headroom circularity）、Fisher combined p、multi-seed Kendall's W。在 NLP empirical papers 中属上乘。\n\n3. **LP 压缩诊断链层次分明** [共识]：全序列 LP → entity-token LP（4× variance 但 -2.0pp selection）→ free-form decoding（std ratio 0.97）→ verbalized confidence（更压缩）→ non-tied subset（+2.9pp, p=0.004）。5 层消融系统排除假说，最终指向 entity-token intrinsic overconfidence。\n\n4. **Free-form ablation RE reversal** [共识]：4-seed 一致���（+1.84±0.12pp），是真正的 empirical finding，揭示 constrained decoding 对 RE LP selection 的抑制效应。\n\n5. **诚实的 negative-result reporting** [共识]：†RE hedging 一致、thinking-token confound 三部分定量排除、Appendix 质量高（FK independence test、LOO-SJ 等价证明、OOD transfer、SJ normalizer robustness）。\n\n---\n\n## Weaknesses\n\n### Must-Fix (2 项，强共识)\n\n**MF1** [R3-W2, 持续 11 轮] Contribution framing 混淆 by-construction 与 empirical finding\n\n4/5 信号 by construction 对同一 instance 赋相同 QE 分数——这不是 surprising empirical finding 而是信号设计的定义性后果。MBR/consensus-proximity 将这些转换为 per-sample rankings 后仍然失败（因 utility 在 across-instances 维度与 F1 相关但 within-instance 不相关）——**这才是核心 empirical finding**，但被 \"4/5 signals can't select\" 的 trivial framing 掩盖。\n\n- 当前 Abstract line 4-5, Intro Contribution 1, Section 4.3 line 85 均将 definitional + empirical 混为同一\"gap\"\n- R1: \"叙事使读者误以为 gap 对 instance-level signals 是显而易见的定义问题\"\n- R2: \"如果 gap 的 4/5 成分是 by-construction, novelty 主要集中在 LP 压缩和 MBR across/within 不对称\"\n\n**建议**：Contribution 1 重组为纯 empirical：(a) MBR consensus-proximity produces per-sample rankings but fails because utility correlates across but not within instances; (b) LP—the only natively per-sample signal—is too compressed (median 0.041 nats) with entity-token overconfidence as root cause。将 \"instance-level signals assign identical scores\" 降为 Section 3.1 的 methodological premise 而非 finding。\n\n**MF2** [R0-C3, 持续 14 轮] Selection gap 的 effective test bed 仅限 SciERC (n=529)\n\n- CoNLL: 论文自认 ceiling-effect control（single-sample F1=0.91, oracle headroom ~4pp）\n- WNUT-17: signals collapse（52% zero-F1）\n- 标题/Abstract \"three NER benchmarks\" 和 \"Named Entity Recognition\" 超出 effective support\n- LLaMA SciERC + 4B ablation 增加模型维度信心，但仍限于 scientific domain\n- TACRED 已证不可行（D105 结构不兼容）\n\n**建议**：(a) 收窄 claim 措辞——明确 selection gap 在 \"medium-difficulty regimes\" 验证，CoNLL/WNUT 验证 boundary conditions 而非 gap 本身；或 (b) 增加一个中等难度��用领域数据集（如 OntoNotes subset、Few-NERD）。\n\n---\n\n### Should-Fix (5 项)\n\n**SF1** [R12-N1] ρ=0.45 headline number 来自 ceiling-effect dataset [共识]\n- Abstract/Intro 用 \"ρ up to 0.45\" 但此值来自 CoNLL EM（ceiling dataset）\n- Primary test bed SciERC 最佳仅 VC ρ=0.379\n- **建议**：headline 改用 primary dataset 数值，或标注来源\n\n**SF2** [R12-W1] 纯诊断无有效 remedy [部分共识]\n- Entity-token LP 失败（-2.0pp）、verbalized conf 失败（-2.45pp）\n- LP×VC combination / calibration-based rescoring 未测试\n- R1: 诊断性论文不必须含 remedy (ARR H13)；R2: 限制 excitement\n- **建议**：至少尝试一个 lightweight pilot（即使 negative 也有信息量）\n\n**SF3** [R13-W1] RE 覆盖策略不统一 [共识]\n- RE 出现在 Abstract、所有主表、Discussion，但仅 SciERC 单 benchmark + 40% zero-F1\n- †RE 标记 >15 处，hedging noise 大\n- Free-form RE reversal 是最有趣发现但被埋 appendix\n- **建议**：全移 Appendix（作为 exploratory extension）或增加第二个 RE benchmark\n\n**SF4** [R11-W7/R13] 缺少 greedy (argmax) decoding baseline [共识]\n- \"Single\" = T=1.0 draw ≠ greedy decoding\n- Greedy 是部署中最自然的 no-cost baseline\n- 无论结果��何都对叙事有价值（如 greedy > all signals → gap 更 striking）\n\n**SF5** [R11-W1] 与 Yao et al. (2026) 的增量贡献 framing [部分共识]\n- SJ vs EM 改进仅 Δρ=+0.065（borderline, \"would not survive Bonferroni\"）\n- Difficulty gradient 是自然的 multi-dataset 延伸\n- R1 辩护：LP diagnostic chain 和 QE-selection separation 是 non-trivial\n- **建议**：重心转向 MBR failure mechanism + LP diagnostics，structural matching 降为 methodological choice\n\n---\n\n### Minor (6 项)\n\n| ID | Issue | 共识 |\n|----|-------|------|\n| R11-W3 | 3 seeds Kendall W=1.000 统计信息量不足，正文应弱化 ranking stability claim | 共识 |\n| R13-W2 | Abstract 过度压缩（9句覆盖全部机制+数字），建议精简 | 共识 |\n| R12-M1 | Discussion LP hypotheses \"three mechanisms\" → 实际 (a)(b)(c)(d) 四个 | 共识 |\n| R13-M1 | Bib issues: mejer2011→2010, feng2025 author mismatch, 4 条 OpenAlex unmatched | R2 |\n| R13-M2 | Table 2 \"Fisher p\" vs Appendix \"Fisher combined p\" 术语不一致 | R2 |\n| R12-M2 | Soft Jaccard 命名（max 分母）：transparent footnote + robustness table，非实质问题 | 降级为 preference |\n\n---\n\n## Reviewer Consensus\n\n**[AGREE]** 两位在以下关键问题上完全一致：\n- MF1: by-construction/empirical framing 混淆（最核心问题，持续 11 轮）\n- MF2: effective test bed 仅 SciERC\n- SF1: ρ=0.45 headline 来源\n- SF4: 缺少 greedy baseline\n- 统计方法论是论文优势\n- LP diagnostic chain 是核心贡献\n\n## Reviewer Divergence\n\n**[程度分歧]**（方向一致，仅严重性不同）：\n- **Overall score**: R1 3.5/5 (Borderline Conference) vs R2 3/5 (Findings)。分歧源于 LP diagnostic chain 的独立贡献权重——R1 认为 5 层消融超越 incremental，R2 认为缺乏 remedy 限制 excitement。\n- **SF2 (remedy)**: R1 认为诊断论文不必���含 remedy；R2 认为影响 acceptance level。\n- **SF5 (Yao incremental)**: R1 部分辩护 LP chain；R2 认为整体偏 incremental。\n\n**[已解决分歧]**：\n- R1-W2 (N≤16 scaling): R2 rebut 合理——论文 claim 是 diminishing returns �� asymptotic。不纳入 final recommendations。\n- R1-W5 (SJ naming): R2 rebut 合理——footnote + robustness table 已 transparent。降为 preference。\n- Q4 (RE reversal significance): R2 提供 4-seed evidence (σ=0.12pp)，reversal robust。已解决。\n\n---\n\n## Questions (需作者澄清)\n\n1. MBR within-instance utility-F1 correlation 具体多少？（如 SJ-utility 的 within-instance ρ）——这是支撑 MF1 reframe 的关键数据空白。\n2. LP×VC combination 或 LP z-score normalization 是否有任何初步数据？\n3. Non-tied LP subset (+2.9pp) 部署时无 ground-truth 选 ε，是否有 oracle-free proxy 可预测哪些 instances LP 有 discriminative power？\n4. Entity-token LP variance CoNLL (median 2×10⁻¹⁰) vs SciERC (4×) 的巨大差异是否与 entity type diversity (4 vs 6 types) 和 model certainty level 有关？\n5. 4B QE 优于 8B 是否因 output diversity 更大？缺 Table 8 对应的 4B diversity 数据。\n\n---\n\n## Missing References\n\nR2 引用���整性检查：50 entries, 0 orphan, 0 missing bib。所有关键引用已覆盖。\n\nMinor bib issues（R13-M1）需核实但不影响引用完整性。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n状态：not_requested。项目未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (weak accept for Findings track, not strong enough for Main Conference)**\n\n**置信度**: 4/5\n\n**理由**：\n- 研究问题有价值（QE ≠ selection 的系统验证），LP 压缩诊断链深入且多层\n- 统计方法论在同类论文中属上乘\n- 但：(1) 核心 framing 将 definitional 与 empirical 混淆已持续 11 轮未根本解决；(2) effective test bed 仅 SciERC 一个中等难度数据集；(3) 纯诊断无 remedy 限制 impact\n- 修正 MF1+MF2 后定位为 Findings paper 合理；Main Conference 需要额外贡献（remedy pilot 或第二个 medium-difficulty dataset）\n\n**R1**: 3.5/5 — Borderline Conference，认为 LP diagnostic chain 足够支撑\n**R2**: 3/5 — Findings level，认为缺乏 remedy + incremental over Yao\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息过度压缩（SF3），ρ=0.45 headline 来自 ceiling dataset（SF1），MBR mechanical 细节不适合 abstract level。\n\n**Introduction**: Contribution 1 需重组（MF1）。与 Yao et al. 的差异描述可接受但应更精确（SF5）。\n\n**Method (§3)**: 信号定义严谨，instance-level vs per-sample 区分清晰。SJ footnote 透明。Evaluation framework 合理（gold-empty exclusion justified）。\n\n**Experiments (§4)**: Table 1 QE 结果 solid。Table 2 selection 结果��核心 evidence 但需 greedy baseline（SF4）。Scale ablation 限定合理（\"within 3B-8B\"）。\n\n**Discussion (§5)**: LP hypotheses 编号错误（minor）。Entity-token ablation 是强贡献���Free-form RE reversal 值得更 prominent treatment。\"Likely requires learned per-sample scoring\" 结论合理。\n\n**Limitations**: 全面覆盖 13 项，诚实透明。\n\n**Appendix**: 质量高，FK independence/OOD/TOST external anchors/N-scaling 均有独立价值。",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# Round 13 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\n**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)\n**Reviewers**: 2 人 (R1: 方法/实验/统计; R2: 新颖性/相关工作/写作)\n**轮次**: Round 1 独立审稿 + 交叉回应，1 轮收敛\n\n---\n\n## Summary\n\n论文研究 LLM-based NER 中 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 quality estimation 和 best-of-N selection 两个维度的表现差异。核心发现是 \"correlation-selection gap\"：signals 达到 moderate QE（Spearman ρ 至 0.45）但无法改善 sample selection。诊断链深入分析了 LP 压缩机制（entity-token ablation、free-form ablation、verbalized confidence）。实验覆盖 3 个 NER + 1 个 RE 数据集、2 个模型族、4B/8B scale。\n\n---\n\n## Strengths\n\n1. **QE/selection 解耦的方法论价值** [共识]：Prior work 仅报告 consistency-accuracy 相关性（Yao et al. 2026），本文首次系统验证 QE 不等价于 selection，并定量化 oracle headroom（13-18pp）与实际 selection gain（≈0pp）的落差。\n\n2. **统计方法论严谨** [共识]：Bootstrap CI with Bonferroni、TOST equivalence testing with 内外锚定（识别并解决了 oracle-headroom circularity）、Fisher combined p、multi-seed Kendall's W。在 NLP empirical papers 中属上乘。\n\n3. **LP 压缩诊断链层次分明** [共识]：全序列 LP → entity-token LP（4× variance 但 -2.0pp selection）→ free-form decoding（std ratio 0.97）→ verbalized confidence（更压缩）→ non-tied subset（+2.9pp, p=0.004）。5 层消融系统排除假说，最终指向 entity-token intrinsic overconfidence。\n\n4. **Free-form ablation RE reversal** [共识]：4-seed 一致���（+1.84±0.12pp），是真正的 empirical finding，揭示 constrained decoding 对 RE LP selection 的抑制效应。\n\n5. **诚实的 negative-result reporting** [共识]：†RE hedging 一致、thinking-token confound 三部分定量排除、Appendix 质量高（FK independence test、LOO-SJ 等价证明、OOD transfer、SJ normalizer robustness）。\n\n---\n\n## Weaknesses\n\n### Must-Fix (2 项，强共识)\n\n**MF1** [R3-W2, 持续 11 轮] Contribution framing 混淆 by-construction 与 empirical finding\n\n4/5 信号 by construction 对同一 instance 赋相同 QE 分数——这不是 surprising empirical finding 而是信号设计的定义性后果。MBR/consensus-proximity 将这些转换为 per-sample rankings 后仍然失败（因 utility 在 across-instances 维度与 F1 相关但 within-instance 不相关）——**这才是核心 empirical finding**，但被 \"4/5 signals can't select\" 的 trivial framing 掩盖。\n\n- 当前 Abstract line 4-5, Intro Contribution 1, Section 4.3 line 85 均将 definitional + empirical 混为同一\"gap\"\n- R1: \"叙事使读者误以为 gap 对 instance-level signals 是显而易见的定义问题\"\n- R2: \"如果 gap 的 4/5 成分是 by-construction, novelty 主要集中在 LP 压缩和 MBR across/within 不对称\"\n\n**建议**：Contribution 1 重组为纯 empirical：(a) MBR consensus-proximity produces per-sample rankings but fails because utility correlates across but not within instances; (b) LP—the only natively per-sample signal—is too compressed (median 0.041 nats) with entity-token overconfidence as root cause。将 \"instance-level signals assign identical scores\" 降为 Section 3.1 的 methodological premise 而非 finding。\n\n**MF2** [R0-C3, 持续 14 轮] Selection gap 的 effective test bed 仅限 SciERC (n=529)\n\n- CoNLL: 论文自认 ceiling-effect control（single-sample F1=0.91, oracle headroom ~4pp）\n- WNUT-17: signals collapse（52% zero-F1）\n- 标题/Abstract \"three NER benchmarks\" 和 \"Named Entity Recognition\" 超出 effective support\n- LLaMA SciERC + 4B ablation 增加模型维度信心，但仍限于 scientific domain\n- TACRED 已证不可行（D105 结构不兼容）\n\n**建议**：(a) 收窄 claim 措辞——明确 selection gap 在 \"medium-difficulty regimes\" 验证，CoNLL/WNUT 验证 boundary conditions 而非 gap 本身；或 (b) 增加一个中等难度��用领域数据集（如 OntoNotes subset、Few-NERD）。\n\n---\n\n### Should-Fix (5 项)\n\n**SF1** [R12-N1] ρ=0.45 headline number 来自 ceiling-effect dataset [共识]\n- Abstract/Intro 用 \"ρ up to 0.45\" 但此值来自 CoNLL EM（ceiling dataset）\n- Primary test bed SciERC 最佳仅 VC ρ=0.379\n- **建议**：headline 改用 primary dataset 数值，或标注来源\n\n**SF2** [R12-W1] 纯诊断无有效 remedy [部分共识]\n- Entity-token LP 失败（-2.0pp）、verbalized conf 失败（-2.45pp）\n- LP×VC combination / calibration-based rescoring 未测试\n- R1: 诊断性论文不必须含 remedy (ARR H13)；R2: 限制 excitement\n- **建议**：至少尝试一个 lightweight pilot（即使 negative 也有信息量）\n\n**SF3** [R13-W1] RE 覆盖策略不统一 [共识]\n- RE 出现在 Abstract、所有主表、Discussion，但仅 SciERC 单 benchmark + 40% zero-F1\n- †RE 标记 >15 处，hedging noise 大\n- Free-form RE reversal 是最有趣发现但被埋 appendix\n- **建议**：全移 Appendix（作为 exploratory extension）或增加第二个 RE benchmark\n\n**SF4** [R11-W7/R13] 缺少 greedy (argmax) decoding baseline [共识]\n- \"Single\" = T=1.0 draw ≠ greedy decoding\n- Greedy 是部署中最自然的 no-cost baseline\n- 无论结果��何都对叙事有价值（如 greedy > all signals → gap 更 striking）\n\n**SF5** [R11-W1] 与 Yao et al. (2026) 的增量贡献 framing [部分共识]\n- SJ vs EM 改进仅 Δρ=+0.065（borderline, \"would not survive Bonferroni\"）\n- Difficulty gradient 是自然的 multi-dataset 延伸\n- R1 辩护：LP diagnostic chain 和 QE-selection separation 是 non-trivial\n- **建议**：重心转向 MBR failure mechanism + LP diagnostics，structural matching 降为 methodological choice\n\n---\n\n### Minor (6 项)\n\n| ID | Issue | 共识 |\n|----|-------|------|\n| R11-W3 | 3 seeds Kendall W=1.000 统计信息量不足，正文应弱化 ranking stability claim | 共识 |\n| R13-W2 | Abstract 过度压缩（9句覆盖全部机制+数字），建议精简 | 共识 |\n| R12-M1 | Discussion LP hypotheses \"three mechanisms\" → 实际 (a)(b)(c)(d) 四个 | 共识 |\n| R13-M1 | Bib issues: mejer2011→2010, feng2025 author mismatch, 4 条 OpenAlex unmatched | R2 |\n| R13-M2 | Table 2 \"Fisher p\" vs Appendix \"Fisher combined p\" 术语不一致 | R2 |\n| R12-M2 | Soft Jaccard 命名（max 分母）：transparent footnote + robustness table，非实质问题 | 降级为 preference |\n\n---\n\n## Reviewer Consensus\n\n**[AGREE]** 两位在以下关键问题上完全一致：\n- MF1: by-construction/empirical framing 混淆（最核心问题，持续 11 轮）\n- MF2: effective test bed 仅 SciERC\n- SF1: ρ=0.45 headline 来源\n- SF4: 缺少 greedy baseline\n- 统计方法论是论文优势\n- LP diagnostic chain 是核心贡献\n\n## Reviewer Divergence\n\n**[程度分歧]**（方向一致，仅严重性不同）：\n- **Overall score**: R1 3.5/5 (Borderline Conference) vs R2 3/5 (Findings)。分歧源于 LP diagnostic chain 的独立贡献权重——R1 认为 5 层消融超越 incremental，R2 认为缺乏 remedy 限制 excitement。\n- **SF2 (remedy)**: R1 认为诊断论文不必���含 remedy；R2 认为影响 acceptance level。\n- **SF5 (Yao incremental)**: R1 部分辩护 LP chain；R2 认为整体偏 incremental。\n\n**[已解决分歧]**：\n- R1-W2 (N≤16 scaling): R2 rebut 合理——论文 claim 是 diminishing returns �� asymptotic。不纳入 final recommendations。\n- R1-W5 (SJ naming): R2 rebut 合理——footnote + robustness table 已 transparent。降为 preference。\n- Q4 (RE reversal significance): R2 提供 4-seed evidence (σ=0.12pp)，reversal robust。已解决。\n\n---\n\n## Questions (需作者澄清)\n\n1. MBR within-instance utility-F1 correlation 具体多少？（如 SJ-utility 的 within-instance ρ）——这是支撑 MF1 reframe 的关键数据空白。\n2. LP×VC combination 或 LP z-score normalization 是否有任何初步数据？\n3. Non-tied LP subset (+2.9pp) 部署时无 ground-truth 选 ε，是否有 oracle-free proxy 可预测哪些 instances LP 有 discriminative power？\n4. Entity-token LP variance CoNLL (median 2×10⁻¹⁰) vs SciERC (4×) 的巨大差异是否与 entity type diversity (4 vs 6 types) 和 model certainty level 有关？\n5. 4B QE 优于 8B 是否因 output diversity 更大？缺 Table 8 对应的 4B diversity 数据。\n\n---\n\n## Missing References\n\nR2 引用���整性检查：50 entries, 0 orphan, 0 missing bib。所有关键引用已覆盖。\n\nMinor bib issues（R13-M1）需核实但不影响引用完整性。\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n状态：not_requested。项目未配置外部审稿。\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (weak accept for Findings track, not strong enough for Main Conference)**\n\n**置信度**: 4/5\n\n**理由**：\n- 研究问题有价值（QE ≠ selection 的系统验证），LP 压缩诊断链深入且多层\n- 统计方法论在同类论文中属上乘\n- 但：(1) 核心 framing 将 definitional 与 empirical 混淆已持续 11 轮未根本解决；(2) effective test bed 仅 SciERC 一个中等难度数据集；(3) 纯诊断无 remedy 限制 impact\n- 修正 MF1+MF2 后定位为 Findings paper 合理；Main Conference 需要额外贡献（remedy pilot 或第二个 medium-difficulty dataset）\n\n**R1**: 3.5/5 — Borderline Conference，认为 LP diagnostic chain 足够支撑\n**R2**: 3/5 — Findings level，认为缺乏 remedy + incremental over Yao\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息过度压缩（SF3），ρ=0.45 headline 来自 ceiling dataset（SF1），MBR mechanical 细节不适合 abstract level。\n\n**Introduction**: Contribution 1 需重组（MF1）。与 Yao et al. 的差异描述可接受但应更精确（SF5）。\n\n**Method (§3)**: 信号定义严谨，instance-level vs per-sample 区分清晰。SJ footnote 透明。Evaluation framework 合理（gold-empty exclusion justified）。\n\n**Experiments (§4)**: Table 1 QE 结果 solid。Table 2 selection 结果��核心 evidence 但需 greedy baseline（SF4）。Scale ablation 限定合理（\"within 3B-8B\"）。\n\n**Discussion (§5)**: LP hypotheses 编号错误（minor）。Entity-token ablation 是强贡献���Free-form RE reversal 值得更 prominent treatment。\"Likely requires learned per-sample scoring\" 结论合理。\n\n**Limitations**: 全面覆盖 13 项，诚实透明。\n\n**Appendix**: 质量高，FK independence/OOD/TOST external anchors/N-scaling 均有独立价值。",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 1304 · 2026-05-16T06:55:15.748967+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4119
}
```

</details>

---


### Assistant

_source line 1305 · 2026-05-16T06:55:22.667333+00:00_

---

**Round 13 审稿完成。**

汇总：
- **Overall: Borderline**（R1: 3.5/5, R2: 3/5）
- **2 项 Must-Fix**：(1) by-construction vs empirical framing 混淆（持续 11 轮）；(2) effective test bed 仅 SciERC
- **5 项 Should-Fix**：ρ headline 来源、无 remedy、RE 策略不统一、缺 greedy baseline、Yao incremental
- **6 项 Minor**

报告已投递 Research Director。Issue tracker 已同步更新（3 项 resolved、新增 4 项、recurring issues 追加 R13 记录）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1306 · 2026-05-16T06:55:25.318900+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

汇总：对 R1 的 10 条意见中，我 **AGREE** 了 6 条（N1, N2, W1, W3, W4, Q3），**REBUT** 了 3 条（W2 scaling claim 范围有限但合理, W5 naming 透明无实质影响, Q4 RE reversal 有 4-seed 支撑），对 Q5 给出了一致性分析。两位 Reviewer 在核心问题上高度一致：framing 混淆 by-construction vs empirical（R1-N2 ≈ R2-N1）、effective test bed 过窄（R1-N1）、贡献增量有限（R2-N2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1307 · 2026-05-16T06:55:35.342969+00:00_

Round 13 审稿已完成。报告已提交给 Research Director。

**最终结论：Borderline（Findings track weak accept，Main Conference 不足）**

核心问题：
1. **MF1**：Contribution framing 混淆 by-construction（4/5 信号定义上无法区分 candidates）与 empirical finding（MBR within-instance failure + LP compression）——持续 11 轮未根本解决
2. **MF2**：Selection gap effective test bed 仅 SciERC (n=529)——持续 14 轮

修正路径：重组 Contribution 1 为纯 empirical + 收窄 claim scope 或增加中等难度数据集 → Findings track 可接受。Main Conference 还需 remedy pilot 或额外 dataset。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 106

## Round 106

68 recorded events


### User

_source line 1308 · 2026-05-16T07:37:28.918496+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1309 · 2026-05-16T07:37:34.901249+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1310 · 2026-05-16T07:37:34.952171+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1311 · 2026-05-16T07:37:39.203932+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1312 · 2026-05-16T07:37:39.204343+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1313 · 2026-05-16T07:37:39.405290+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1314 · 2026-05-16T07:37:39.455867+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1315 · 2026-05-16T07:37:45.638836+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1316 · 2026-05-16T07:37:47.045933+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (111 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_vc_lp_cascade_selection** (killed): VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\n- **exp_tacred_re_benchmark** (killed): TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\n- **exp_entity_token_lp** (negative): Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\n  [exp_entity_token_lp_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/data/results.json) | [exp_entity_token_lp_report](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report/report.md)\n\n## 趋势\n成功 61 / 负向 24 / 失败 4 / 共 111\n\n## 下一步\
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1407
}
```

</details>

---


### Tool call

_source line 1317 · 2026-05-16T07:37:47.196755+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1318 · 2026-05-16T07:37:47.999948+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1319 · 2026-05-16T07:37:48.000469+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-16T07:37:48.453011+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-16T07:37:55.133451+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Call for Papers: NLP for Science Workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/nlp-science"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"[Call for participation] Present your Findings of EMNLP paper at the NLP4MusA (NLP for Music and Audio) workshop | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-participation-present-your-findings-emnlp-paper-nlp4musa-nlp-music-and-audio-workshop"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"}]

I found information about EMNLP 2026, but the search results primarily contain details about tutorial proposals and workshop calls rather than
…[truncated 2983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7132
}
```

</details>

---


### Tool result

_source line 1322 · 2026-05-16T07:37:55.133819+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6680
}
```

</details>

---


### Tool call

_source line 1323 · 2026-05-16T07:38:00.828922+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline call for papers main conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline call for papers main conference"
  }
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-16T07:38:01.633171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1325 · 2026-05-16T07:38:02.086262+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-16T07:38:02.689182+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-16T07:38:07.057370+00:00_

Web search results for query: "EMNLP 2026 submission deadline call for papers main conference"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's the information about EMNLP 2026 s
…[truncated 1198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6228
}
```

</details>

---


### Tool result

_source line 1328 · 2026-05-16T07:38:14.036736+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit formatting requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"}]

Based on the search results, here are the EMNLP 2026 author guidelines regarding page limits and formatting requirements:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. For the Industry Track specifically, industry track papers cannot exceed 6 pages in length (excluding ethical considerations and references).

## What Doesn't Count Toward Page Limits

References and limitations sections do not count toward the page limit, nor do the following optional sections: acknowledgements (only in the final vers
…[truncated 777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 12403
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-16T07:38:14.037606+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 110\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 10899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 11951
}
```

</details>

---


### Tool result

_source line 1330 · 2026-05-16T07:38:14.088584+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 11399
}
```

</details>

---


### Tool call

_source line 1331 · 2026-05-16T07:38:24.633806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1332 · 2026-05-16T07:38:25.351651+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals on a primary medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) boundary conditions, at two model scales (4B and 8B).
4	All signals achieve moderate-to-strong quality estimation ($\rho{=}0.38$ on the primary test bed, up to 0.45 on a ceiling-effect control), yet none improves best-of-$N$ selection over cost-free greedy decoding---the \textit{correlation-selection gap}.
5	Consensus-proximity (MBR) selection achieves positive within-instance utility--F1 correlation (median $\rho{=}0.52$) but fails due to pervasive instance degeneracy (21--58\% of instances yield identical outputs); log-probability---the only per-sample signal---is too compressed within instances to discriminate.
6	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm that compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
7	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 717
}
```

</details>

---


### Tool call

_source line 1333 · 2026-05-16T07:38:25.502663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1334 · 2026-05-16T07:38:25.553409+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement; we extend their work by separating quality estimation from best-of-$N$ selection, diagnosing two failure mechanisms (instance degeneracy and LP compression) through a multi-ablation chain across a three-dataset difficulty gradient.
9	
10	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency signals achieve moderate-to-strong quality estimation ($\rho{=}0.38$ on the primary test bed, up to 0.45 on a ceiling-effect control) but fail to improve selection over cost-free greedy decoding ($T{=}0$) despite substantial oracle headroom.
11	The gap has two causes: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{LP compression}---log-probability, the only per
…[truncated 2446 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1335 · 2026-05-16T07:38:25.604152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1336 · 2026-05-16T07:38:25.604591+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 2968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1337 · 2026-05-16T07:38:26.056633+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1338 · 2026-05-16T07:38:26.961438+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, seed${=}42$, single-seed; 3-seed stability in Table~\ref{tab:multiseed}). Best in \textbf{bold}. RE results in Appendix~\ref{app:re_extension}. $N{=}16$ in Table~\ref{tab:robustness}.}
27	\la
…[truncated 7238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 1339 · 2026-05-16T07:38:27.012185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1340 · 2026-05-16T07:38:27.464318+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
12	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence estimation for structured prediction via CRF marginals and confidence-weighted models; our signals are model-agnostic.
13	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided}.
14	
15	\paragraph{Uncertainty estimation and calibration.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncertainty quantification \cite{xia2025survey}, and calibr
…[truncated 1476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1341 · 2026-05-16T07:38:27.464687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1342 · 2026-05-16T07:38:27.916817+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Four of five signals are instance-level aggregates; consensus-proximity (MBR) converts these to per-sample rankings (Table~\ref{tab:selection}), instantiating MBR decoding \cite{eikema2022sampling} with signal-specific utility functions.
11	Within-instance analysis reveals that MBR utility does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on non-degenerate instances MBR closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
12	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
13	These degenerate instances dominate the aggregate, diluting genuine gains to near-zero.
14	Despite MBR's success in machine translation \cite{freitag2022high}, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit (Appendix~\ref{app:mbr_discussion}).
15	Meanwhile, deterministic greedy decoding ($T{=}0$)---requiring no sampling cost---achieves F1${=}0.663$ on SciERC, surpassing all $N{=}8$ selection strategies (best: LP at 0.647; Table~\ref{tab:selection})
…[truncated 5898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1343 · 2026-05-16T07:38:27.917345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1344 · 2026-05-16T07:38:28.419728+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate-to-strong quality estimation ($\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform cost-free greedy decoding.
4	The gap stems from two mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).
5	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
6	The gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).
7	Whether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1345 · 2026-05-16T07:38:28.420105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1346 · 2026-05-16T07:38:29.323890+00:00_

1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	We evaluate signals individually; whether signal combinations (e.g., LP $\times$ consistency) or learned weightings could close the selection gap is unexplored.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection despite increasing with
…[truncated 145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1347 · 2026-05-16T07:38:29.374500+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1348 · 2026-05-16T07:38:29.876833+00:00_

File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1349 · 2026-05-16T07:38:30.429222+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1350 · 2026-05-16T07:38:30.480102+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## ρ 一致性审计 (2026-05-15) — 关键管道 bug\\n- **根因**：旧管道 `compute_metrics.py` 包含 gold-empty 实例 + FK 对全空 sample 返回 0（应为 1.0）\\n- CoNLL 697/3453 (20%) gold-empty 实例导致 FK ρ 膨胀 0.48→0.81，SJ ρ 压低 0.48→0.18，排名反转\\n- **统一标准**：排除 gold-empty 实例。CoNLL n=2756，SciERC n=551（或 n=529 排除空 gold NER）\\n- 论文所有 ρ 值必须来自 gold-filtered 管道（`rho_audit.py
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1351 · 2026-05-16T07:38:30.581684+00:00_

called mcp__agent-ml-research__read_local_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_local_file</summary>

```json
{
  "file": "projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "tool_args": {
    "file": "projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1352 · 2026-05-16T07:38:30.582036+00:00_

&lt;tool_use_error>Error: No such tool available: mcp__agent-ml-research__read_local_file&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_local_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1353 · 2026-05-16T07:38:35.729463+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1354 · 2026-05-16T07:38:36.282618+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 13708 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-16T07:38:36.684724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-16T07:38:36.735429+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{eikema2022
…[truncated 3208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1357 · 2026-05-16T07:38:37.639461+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_framing.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1358 · 2026-05-16T07:38:37.890939+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-15 — D098: 4B scale ablation 2×2 矩阵完成。4B ≈ 8B（多数 correlation 4B 反而更高），gap 与 model capacity 无关，task difficulty 是信号退化主驱动。Scale ablation 证明 universality across scales。R14 RESOLVED。\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (3 条, D072 updated — ablation proves universality)\\n\\n### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)\\nThe correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.\\n\\n**Two-layer argument**:\\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.\\n\\n**Key evidence (score compression)**:\\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ:
…[truncated 1371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-16T07:38:38.292974+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1360 · 2026-05-16T07:38:38.544307+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-16T07:38:38.695293+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1362 · 2026-05-16T07:38:38.746000+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-16T07:38:42.511708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-16T07:38:42.914077+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====
3	- id: R0-C1
4	  summary: "模型规模单一（仅 8B）"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  resolution: "Round 2 Reviewer 确认措辞修正到位"
11	  resolution_round: 2
12	- id: R0-C2
13	  summary: "相关工作显著遗漏"
14	  category: framing
15	  severity: warning
16	  status: resolved
17	  first_raised_round: 0
18	  last_seen_round: 1
19	  resolution: "Round 2 确认 49 条 bib 全部 cited"
20	  resolution_round: 2
21	- id: R0-C4
22	  summary: "SJ 方法新颖性有限"
23	  category: method
24	  severity: warning
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 1
28	  resolution: "Round 2 确认三点差异化清晰"
29	  resolution_round: 2
30	- id: R0-C5
31	  summary: "全文零图表"
32	  category: writing
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 0
37	  resolution: "论文已包含 6 个 figures"
38	  resolution_round: 1
39	- id: R0-C6
40	  summary: "成本分析 negligible 误导"
41	  category: method
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 0
46	  resolution: "Round 1+ 未再提及"
47	  resolution_round: 1
48	- id: R0-W1
49	  summary: "未探索 signal combination"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 0
55	  resolution: "Round 1+ 未再提及"
56	  resolution_round: 1
57	- id: R0-W4
58	  summary: "统计检验不系统"
59	  category: experiment
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 0
63	  last_seen_round: 1
64	  resolution: "Round 2 Reviewer 评价 bootstrap 达到高标准"
65	  resolution_round: 2
66	- id: R3-W4
67	  summary: "FK independence 假设未验证"
68	  category: experiment
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 3
72	  last_seen_round: 8
73	  resolution: "Appendix instance-level permutation test (n=529-2756, p<0.001) 验证"
74	  resolution_round: 9
75	- id: R3-W5
76	  summary: "Cross-model
…[truncated 27454 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1365 · 2026-05-16T07:38:43.366537+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1366 · 2026-05-16T07:38:43.869009+00:00_

200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
…[truncated 15424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1367 · 2026-05-16T07:38:44.321615+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-16T07:38:44.775098+00:00_

&lt;persisted-output>
Output too large (33.9KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/2b04ff1e-ddc7-4775-969e-ac644dbd7276/tool-results/toolu_017fvuxKbQtw9dBdFN4NjKBw.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md:163:外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md:166:项目未配置 paperreview.ai 外部审稿（external_review.paperreview_ai.enabled 未启用）。外部审稿：未请求。
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md:156:外部审稿：未配置（项目未启用 `external_review.paperreview_ai.enabled`）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/fe
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1369 · 2026-05-16T07:38:44.825854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1370 · 2026-05-16T07:38:44.926897+00:00_

100	  year = {2022},
101	  url = {https://arxiv.org/abs/2207.05221}
102	}
103	
104	@inproceedings{kang2025selfcertainty,
105	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
106	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
107	  booktitle = {NeurIPS 2025},
108	  year = {2025},
109	  url = {https://arxiv.org/abs/2502.18581}
110	}
111	
112	@inproceedings{kim2026reasc,
113	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
114	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
115	  booktitle = {ACL 2026},
116	  year = {2026},
117	  url = {https://arxiv.org/abs/2601.02970}
118	}
119	
120	@article{li2025llms,
121	  title = {LLMs Can Generate a Better Answer by Aggregating Their Own Responses},
122	  author = {Li, Zichong and Feng, Xinyu and Cai, Yuheng and Zhang, Zixuan and Liu, Tianyi and Liang, Chen and Chen, Weizhu and Wang, Haoyu and Zhao, Tuo},
123	  journal = {arXiv preprint arXiv:2503.04104},
124	  year = {2025},
125	  url = {https://arxiv.org/abs/2503.04104}
126	}
127	
128	@inproceedings{kuhn2023semantic,
129	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
130	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
131	  booktitle = {ICLR 2023},
132	  year = {2023},
133	  url = {https://arxiv.org/abs/2302.09664}
134	}
135	
136	@inproceedings{malinin2021uncertainty,
137	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
138	  author = {Malinin, Andrey and Gales, Mark},
139	  booktitle = {International Conference on Learning Representations},
140	  year = {2021},
141	  url = {https://openreview.net/forum?id=jN5y-zb5Q7m}
142	}
143	
144	@inproceedings{li2023codeie,
145	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
146	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang 
…[truncated 7483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1371 · 2026-05-16T07:40:11.688478+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 (long paper)，参考文献/limitations/ethics/appendix 不计\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (作者已匿名)\n- **附录**: 允许，不参与页数限制但可被审稿人参考\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n（references: `docs/paper/references.bib`）\n\n### 论文概要\n标题: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n研究 LLM-based NER 中 5 种置信信号的质量估计与样本选择能力。核心发现：信号可估计质量（ρ=0.38）但无法选出优于 greedy decoding 的样本——\"correlation-selection gap\"。诊断两种失败机制：instance degeneracy 和 LP compression。\n\n### 重点审查方向\n\n1. **方法定义与数学正确性**：\n   - 5 种信号（SJ, VC, FK, EM, LP）的定义是否严谨？公式是否正确？\n   - SJ 分母用 max(|g_i|,|g_j|) 而非 union——命名为 \"Soft Jaccard\" 是否恰当？\n   - Instance-level vs per-sample 信号的区分是否清晰？\n\n2. **实验设计**：\n   - 数据集选择（SciERC/CoNLL/WNUT-17 三梯度）是否合理？\n   - Selection gap 的有效测试台是否仅限 SciERC（CoNLL ceiling-effect, WNUT collapse）？如此，三数据集验证的 claim 是否过强？\n   - N=8/16 样本量是否充分？\n   - Greedy baseline (T=0) 的加入是否恰当？Single sample (T=1.0 draw) vs Greedy (argmax) 的区别是否充分说明？\n\n3. **统计分析**：\n   - 3-seed stability（σ≤0.026）的统计效力如何？n=3 下 Kendall W 有多大信息量？\n   - Bootstrap CI、Fisher combined p、TOST equivalence testing 的使用是否恰当？\n   - Gold-empty instance filtering 在 QE 和 Selection 之间是否一致？（Section 3.3 写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453）\n   - ε=0.05 threshold 用于 LP tied/non-tied 分层——是否有 prior justification？Sensitivity analysis 是否充分？\n\n4. **消融实验链**：\n   - Free-form decoding ablation（std ratio 0.97）→ 排除 constrained decoding\n   - Entity-token LP（4× variance but -2.0pp selection）→ 排除 format-token dilution\n   - Verbalized confidence → 排除 LP-specific\n   - 这条诊断链的逻辑是否严密？每一步排除是否成立？\n\n5. **Claim-Evidence 对齐**：\n   - \"correlation-selection gap\" 的操作性定义在哪？是否清晰？\n   - 4/5 signals 是 instance-level → 不能 select 是 by construction。这算 finding 还是 trivial observation？MBR conversion 后仍失败才是 empirical finding——论文区分清楚了吗？\n   - Scale ablation (4B vs 8B) 能否支撑 \"task difficulty drives the gap\" 的结论？\n\n请以 EMNLP 顶级审稿人标准评估。输出格式：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的关键相关工作）\n- Overall Assessment（评分 + 置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n### 你的审查侧重：方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 (long paper)，参考文献/limitations/ethics/appendix 不计\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (作者已匿名)\n- **附录**: 允许，不参与页数限制但可被审稿人参考\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n（references: `docs/paper/references.bib`）\n\n### 论文概要\n标题: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n研究 LLM-based NER 中 5 种置信信号的质量估计与样本选择能力。核心发现：信号可估计质量（ρ=0.38）但无法选出优于 greedy decoding 的样本——\"correlation-selection gap\"。诊断两种失败机制：instance degeneracy 和 LP compression。\n\n### 重点审查方向\n\n1. **方法定义与数学正确性**：\n   - 5 种信号（SJ, VC, FK, EM, LP）的定义是否严谨？公式是否正确？\n   - SJ 分母用 max(|g_i|,|g_j|) 而非 union——命名为 \"Soft Jaccard\" 是否恰当？\n   - Instance-level vs per-sample 信号的区分是否清晰？\n\n2. **实验设计**：\n   - 数据集选择（SciERC/CoNLL/WNUT-17 三梯度）是否合理？\n   - Selection gap 的有效测试台是否仅限 SciERC（CoNLL ceiling-effect, WNUT collapse）？如此，三数据集验证的 claim 是否过强？\n   - N=8/16 样本量是否充分？\n   - Greedy baseline (T=0) 的加入是否恰当？Single sample (T=1.0 draw) vs Greedy (argmax) 的区别是否充分说明？\n\n3. **统计分析**：\n   - 3-seed stability（σ≤0.026）的统计效力如何？n=3 下 Kendall W 有多大信息量？\n   - Bootstrap CI、Fisher combined p、TOST equivalence testing 的使用是否恰当？\n   - Gold-empty instance filtering 在 QE 和 Selection 之间是否一致？（Section 3.3 写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453）\n   - ε=0.05 threshold 用于 LP tied/non-tied 分层——是否有 prior justification？Sensitivity analysis 是否充分？\n\n4. **消融实验链**：\n   - Free-form decoding ablation（std ratio 0.97）→ 排除 constrained decoding\n   - Entity-token LP（4× variance but -2.0pp selection）→ 排除 format-token dilution\n   - Verbalized confidence → 排除 LP-specific\n   - 这条诊断链的逻辑是否严密？每一步排除是否成立？\n\n5. **Claim-Evidence 对齐**：\n   - \"correlation-selection gap\" 的操作性定义在哪？是否清晰？\n   - 4/5 signals 是 instance-level → 不能 select 是 by construction。这算 finding 还是 trivial observation？MBR conversion 后仍失败才是 empirical finding——论文区分清楚了吗？\n   - Scale ablation (4B vs 8B) 能否支撑 \"task difficulty drives the gap\" 的结论？\n\n请以 EMNLP 顶级审稿人标准评估。输出格式：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的关键相关工作）\n- Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 1372 · 2026-05-16T07:40:39.712155+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28023
}
```

</details>

---


### Tool call

_source line 1373 · 2026-05-16T07:40:39.863287+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性/增量贡献 + 相关工作完整性 + 写作/格式\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 (long paper)，参考文献/limitations/ethics/appendix 不计\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (作者已匿名)\n- **附录**: 允许，不参与页数限制但可被审稿人参考\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n（references: `docs/paper/references.bib`, 50 entries）\n\n### 论文概要\n标题: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n在 LLM-based NER 中评估 5 种置信信号（SJ, VC, FK, EM, LP）的质量估计与样本选择。核心发现 \"correlation-selection gap\"：信号可估计输出质量但无法选出更好样本。两种失败机制：instance degeneracy (21-58%) 和 LP compression (0.041 nats)。\n\n### 重点审查方向\n\n1. **新颖性与增量贡献**：\n   - 与 Yao et al. (2026) 的差异（同样研究 consistency-accuracy correlation for LLM-based IE）——本文贡献的增量是否够 EMNLP main conference？\n   - \"Correlation-selection gap\" 是否是 genuine contribution 还是已知现象的新标签？MBR decoding 社区（Eikema, Freitag）已知 MBR 在 structured output 上退化——本文增加了什么？\n   - 4/5 signals instance-level → cannot select by construction 这一观察的学术价值？\n   - Entity-token LP 实验是 positive pilot remedy 还是 negative result？其贡献如何定位？\n   - 整体定位：这是 diagnostic/empirical study（强调发现）还是 methodology paper（强调方法）？framing 是否一致？\n\n2. **相关工作完整性**（需用 web_search 验证）：\n   - Self-consistency 扩展到 structured output：是否遗漏 2025-2026 的关键工作？\n   - Confidence estimation for IE：除了 Culotta (2004)、Mejer & Crammer (2010)，是否有更近的工作？\n   - MBR for structured prediction：Eikema et al. (2025) 已引用，还有其他吗？\n   - Test-time compute scaling for IE：是否有遗漏？\n   - 引用数量（50）对 EMNLP 是否足够？\n\n3. **引用完整性审核**：\n   - 检查 references.bib 中的条目：年份是否正确？作者是否匹配？\n   - 特别关注：mejer2010confidence（bib 中 key 是否标注了正确年份？）、feng2025optimal（作者顺序）、oh2026latentsc（年份 2025 vs 2026？）\n   - 是否有 orphan bib entries（bib 中有但正文未引用）？\n   - 是否有 missing citations（正文提及但 bib 中无）？\n\n4. **写作质量**：\n   - Abstract 是否过度压缩？（9 句覆盖 5 signals + MBR mechanics + LP compression + free-form ablation）\n   - RE 的呈现策略：出现在 Abstract、主表、Discussion，但同时有大量 †RE 标记。是应该全在 Appendix 还是全在主文？\n   - Contribution list 是否清晰区分 definitional observation 和 empirical finding？\n   - \"moderate-to-strong\" quality estimation 的措辞——ρ=0.38 在 primary dataset (SciERC)，ρ=0.45 来自 ceiling-effect control (CoNLL)——headline 数字选择是否误导？\n   - Discussion 中 LP compression hypotheses 是标注 \"three\" 还是 \"four\" mechanisms？(a)(b)(c)(d) 四个。\n   - Limitations section 覆盖是否全面？\n\n5. **格式合规**：\n   - 正文是否在 8 页限制内？（需检查 compiled 长度，不含 references/limitations/appendix）\n   - ACL style 是否正确使用？\n   - 表格/图表编号是否连续？Caption 是否清晰？\n   - 匿名合规：是否有 de-anonymization 风险？（代码释放承诺用 [anonymized URL]）\n\n请以 EMNLP 最严格审稿人标准评估。输出格式：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的关键相关工作，需搜索验证）\n- Overall Assessment（评分 + 置信度）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n### 你的审查侧重：新颖性/增量贡献 + 相关工作完整性 + 写作/格式\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 (long paper)，参考文献/limitations/ethics/appendix 不计\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind (作者已匿名)\n- **附录**: 允许，不参与页数限制但可被审稿人参考\n\n### 论文路径\n`projects/struct_self_consist_ie/docs/paper/main.tex`\n（sections 在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex）\n（references: `docs/paper/references.bib`, 50 entries）\n\n### 论文概要\n标题: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n在 LLM-based NER 中评估 5 种置信信号（SJ, VC, FK, EM, LP）的质量估计与样本选择。核心发现 \"correlation-selection gap\"：信号可估计输出质量但无法选出更好样本。两种失败机制：instance degeneracy (21-58%) 和 LP compression (0.041 nats)。\n\n### 重点审查方向\n\n1. **新颖性与增量贡献**：\n   - 与 Yao et al. (2026) 的差异（同样研究 consistency-accuracy correlation for LLM-based IE）——本文贡献的增量是否够 EMNLP main conference？\n   - \"Correlation-selection gap\" 是否是 genuine contribution 还是已知现象的新标签？MBR decoding 社区（Eikema, Freitag）已知 MBR 在 structured output 上退化——本文增加了什么？\n   - 4/5 signals instance-level → cannot select by construction 这一观察的学术价值？\n   - Entity-token LP 实验是 positive pilot remedy 还是 negative result？其贡献如何定位？\n   - 整体定位：这是 diagnostic/empirical study（强调发现）还是 methodology paper（强调方法）？framing 是否一致？\n\n2. **相关工作完整性**（需用 web_search 验证）：\n   - Self-consistency 扩展到 structured output：是否遗漏 2025-2026 的关键工作？\n   - Confidence estimation for IE：除了 Culotta (2004)、Mejer & Crammer (2010)，是否有更近的工作？\n   - MBR for structured prediction：Eikema et al. (2025) 已引用，还有其他吗？\n   - Test-time compute scaling for IE：是否有遗漏？\n   - 引用数量（50）对 EMNLP 是否足够？\n\n3. **引用完整性审核**：\n   - 检查 references.bib 中的条目：年份是否正确？作者是否匹配？\n   - 特别关注：mejer2010confidence（bib 中 key 是否标注了正确年份？）、feng2025optimal（作者顺序）、oh2026latentsc（年份 2025 vs 2026？）\n   - 是否有 orphan bib entries（bib 中有但正文未引用）？\n   - 是否有 missing citations（正文提及但 bib 中无）？\n\n4. **写作质量**：\n   - Abstract 是否过度压缩？（9 句覆盖 5 signals + MBR mechanics + LP compression + free-form ablation）\n   - RE 的呈现策略：出现在 Abstract、主表、Discussion，但同时有大量 †RE 标记。是应该全在 Appendix 还是全在主文？\n   - Contribution list 是否清晰区分 definitional observation 和 empirical finding？\n   - \"moderate-to-strong\" quality estimation 的措辞——ρ=0.38 在 primary dataset (SciERC)，ρ=0.45 来自 ceiling-effect control (CoNLL)——headline 数字选择是否误导？\n   - Discussion 中 LP compression hypotheses 是标注 \"three\" 还是 \"four\" mechanisms？(a)(b)(c)(d) 四个。\n   - Limitations section 覆盖是否全面？\n\n5. **格式合规**：\n   - 正文是否在 8 页限制内？（需检查 compiled 长度，不含 references/limitations/appendix）\n   - ACL style 是否正确使用？\n   - 表格/图表编号是否连续？Caption 是否清晰？\n   - 匿名合规：是否有 de-anonymization 风险？（代码释放承诺用 [anonymized URL]）\n\n请以 EMNLP 最严格审稿人标准评估。输出格式：\n- Summary（2-3 句）\n- Strengths（逐条）\n- Weaknesses（逐条，分 Must-Fix / Should-Fix / Minor）\n- Questions（需要作者回答的问题）\n- Missing References（遗漏的关键相关工作，需搜索验证）\n- Overall Assessment（评分 + 置信度）"
  }
}
```

</details>

---


### Tool result

_source line 1374 · 2026-05-16T07:40:41.327316+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1464
}
```

</details>

---


### Assistant

_source line 1375 · 2026-05-16T07:40:49.413358+00:00_

**Round 1 已启动。** 两位 Reviewer 已收到任务，正在独立初审：

- **Reviewer 1** — 方法严谨性 / 实验设计 / 统计分析
- **Reviewer 2** — 新颖性 / 相关工作 / 写作格式

等待两位 Reviewer 返回初审报告后进入交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1376 · 2026-05-16T07:44:15.779051+00:00_

[Reviewer 1 审稿意见]:
## Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)

### Summary

本文评估 LLM-based NER 中 5 种置信信号在质量估计（QE）和 best-of-N 选择两个任务上的表现，核心发现是"correlation-selection gap"：信号能预测哪些 instance 做得好（ρ=0.38），却不能选出比 greedy decoding 更好的样本。论文诊断两种失败机制——instance degeneracy 和 LP compression——并通过 free-form decoding、entity-token LP 等消融验证 compression 是内在属性。实验覆盖三数据集难度梯度、两个模型族、两种规模。

### Strengths

**S1.** 概念贡献清晰且有实际意义。QE/selection 的解耦是这篇论文的核心洞察，且直接指向实践者容易犯的错误（用高 ρ 信号做选择）。这个区分在 IE 领域尚未被明确指出。

**S2.** 诊断链逻辑严密。Free-form decoding (std ratio 0.97) → entity-token LP (4× variance 但 -2.0pp selection) → verbalized confidence (更压缩)，每一步排除一个假设，且每步都有量化证据。RE free-form 的反向效果（+1.8pp）被恰当标注为 regime-dependent。

**S3.** 统计实践远超 NLP 论文平均水平。Bootstrap CI、TOST equivalence testing（含外部锚定 δ）、Fisher combined p、多种 ε sensitivity sweep、multi-seed Kendall's W——方法论上非常负责。

**S4.** 三数据集难度梯度设计合理。CoNLL (ceiling-effect control) 和 WNUT-17 (signal-collapse boundary) 明确标注为边界条件而非主要验证集，避免了过度 claim。

**S5.** 消融实验覆盖面广。Thinking token 影响分析（三角论证）、SJ normalizer robustness（Δρ<0.01）、LOO-SJ equivalence proof、FK independence permutation test——预见并回应了大多数潜在质疑。

### Weaknesses

#### Must-Fix（影响接收决定）

**N1** [critical] Instance-level 信号"无法选择"在很大程度上是 by construction，论文区分不够sharp

- 具体位置：Section 3.1 (最后一句), Section 4.3 (第一段)
- 问题：4/5 信号是 instance-level aggregates，给同一 input 的所有 N 个候选分配相同分数——它们在字面意义上不具备选择能力。论文用 MBR/consensus-proximity 将其转化为 per-sample ranking，但 MBR 转换后仍然失败才是 empirical finding。当前叙述中，contribution #1 ("the correlation-selection gap") 把 instance-level 信号的 by-construction 限制和 LP 的 empirical 失败混在一起计算，夸大了"5个信号全部失败"的 surprise factor。
- 为什么影响接收：如果 reviewer/reader 认为 4/5 的"发现"是 trivial observation (对 instance-level 信号无法选择而感到不惊讶)，那么核心 contribution 实质上缩减为"LP 选择失败 + 诊断"——仍有价值但需要更诚实的 framing。
- 建议：在 Introduction/Method 中更清晰地将 gap 分为两层：(a) structural limitation (instance-level → needs conversion) 和 (b) empirical failure (MBR conversion has positive within-instance ρ=0.52 but fails due to degeneracy; LP is per-sample but too compressed)。当前 Section 5 (Discussion) 确实做了这个区分，但 abstract 和 introduction 中的 framing 过于 monolithic。

**N2** [critical] Selection gap 的有效验证集实质上仅 SciERC 一个数据集

- 具体位置：Section 4.3, Table 3 (selection), Table 6 (cross_selection)
- 问题：CoNLL oracle headroom 仅 4pp（论文正确标注为 ceiling-effect control）；WNUT-17 信号全部 collapse（capability boundary）。真正验证 selection gap 的只有 SciERC。Table 6 中 LLaMA/SciERC 的 LP 0.652 vs single 0.646 确实 replicate 了 gap，但这仍然是同一数据集的不同模型。论文 claim "The pattern holds across CoNLL and WNUT-17 (Table 6)" (Section 4.3, line 90)，但 CoNLL 上 holding 的原因是 ceiling effect（无 headroom 可选），并非信号失败——这是 qualitatively 不同的原因。
- 为什么影响接收：一篇诊断性论文的 claim 泛化性依赖于在足够多的 non-trivial settings 中复现。单数据集（SciERC）+ 单模型家族（Qwen/LLaMA 都是 8B decoder-only）的 selection 实验难以支撑 "the gap" 作为 general phenomenon 的 framing。
- 建议：(1) 明确将 CoNLL/WNUT 定位为 boundary-condition analysis 而非 replication（当前部分语言已如此但不一致）；(2) 增加一个 medium-difficulty 数据集（如 ACE05 或 Few-NERD subset）以验证 gap 在 SciERC 之外成立；(3) 或者软化 claim 为 "demonstrated on medium-difficulty NER" 而非隐含的 general phenomenon。

#### Should-Fix（影响评分但不一票否决）

**W1** [warning] Scale ablation (4B vs 8B) 支撑 "task difficulty drives the gap" 结论的证据力不足

- 具体位置：Section 4.4, Table 4
- 问题：仅 2 个规模点（4B, 8B），属同一模型家族（Qwen3），scale 范围极窄。结论 "task difficulty is a stronger predictor of the gap than model scale" 基于 4B 在 SciERC 上 QE 提升但 selection 仍失败——但 4B 可能产生更多 diversity（更多 degenerate 或更少？），论文未报告 4B 的 degeneracy 统计。缺少 4B 的 instance degeneracy 数据使得无法判断：是 task difficulty 驱动 gap，还是 4B 恰好有相似的 degeneracy pattern？
- 建议：报告 4B 的 degeneracy 统计（constant F1 fraction, oracle headroom）；承认 2-point scale ablation 的限制性更强。

**W2** [warning] Fisher combined p 仅基于 2 seeds 的统计合理性

- 具体位置：Table 3 (selection), Section 4.3
- 问题：Table 3 报告 "2-seed mean±σ, Fisher combined p vs. single-sample"。Fisher's method 组合 2 个独立 p-value 的统计效力极低——2-seed Fisher 本质上就是一个 χ²(4) 检验，对于检测 13pp oracle headroom 中的 0.2pp effect size 几乎没有检测力。这不是错误（Fisher's method technically works with k=2），但给人一种统计严谨性的表象而实际上 power 极低。
- 建议：(1) 报告 power analysis（在给定 effect size 下 2-seed Fisher 的检测力）；(2) 或直接使用 bootstrap CI 作为主要统计推断依据（论文 appendix 已有），将 Fisher p 降级为辅助证据。

**W3** [warning] Kendall's W 在 n=3 seeds 下的信息量问题

- 具体位置：Table 9 (ranking-stability), Appendix F
- 问题：Kendall's W=1.000 with 3 raters ranking 5 signals = complete agreement，但 n=3 下即使 W=1.0 也不显著（临界值约 0.88 at α=0.05 for k=3, m=5）。论文注释 "though statistical power with n=3 is limited" 是诚实的，但仍在 abstract/introduction 中使用 "σ≤0.026" 暗示高稳定性。
- 建议：明确 3-seed 的主要功能是 sanity check（排除 catastrophic seed sensitivity），而非统计推断依据。避免将其作为 robustness 证据的第一行引用。

**W4** [warning] Greedy baseline (T=0) 与 T=1.0 sampling 的比较公平性

- 具体位置：Section 4.3, Table 3
- 问题：Greedy (T=0) F1=0.663 > best selection LP 0.647。但 greedy 是 deterministic argmax（token-level 最优局部选择），而 T=1.0 sampling 引入了 substantial noise。如果目的是展示 selection 无法回收 sampling noise 的代价，这是合理的。但论文使用 "surpassing all N=8 selection strategies" 的修辞暗示 greedy 是 selection 的公平 competitor。实际上，greedy 和 sampling+selection 解决的是不同问题（deterministic quality vs. exploration+selection）。
- 为什么重要：这使得 "gap" 的 practical implication 变得模糊——如果 conclusion 是 "just use greedy"，那么整个 sampling+QE+selection pipeline 的研究价值需要重新 frame。
- 建议：更明确地讨论 greedy 不是 selection 的 baseline 而是 "practical cost-free alternative"——当前脚注已有暗示但主文不够清晰。将 "single-sample" 作为选择的正式 baseline（Table 3 结构已对），减少对 greedy 的修辞强调。

**W5** [warning] ε=0.05 threshold 虽有 sensitivity analysis，但 "非 tied 子集 +2.9pp (p=0.004)" 的 multiple testing 问题

- 具体位置：Section 5, Appendix G (Table 8)
- 问题：Table 8 展示 ε sweep 从 0.01 到 0.20，selection gain 单调递增——这表明 ε=0.05 并非 "natural split point" 而是连续谱上的一个 arbitrary cutoff。论文在 Section 4.3 脚注中说 "survives Bonferroni correction over 5 comparisons"，但 Bonferroni over 5 signals 不等于 correction over 7 ε values × 5 signals。Limitations 节承认 "post-hoc exploratory choice" 但主文仍突出 p=0.004。
- 建议：将 non-tied subset 结果明确定位为 "exploratory/descriptive"（当前 Limitations 已接近这个 framing，但 Discussion §5 段落 2 将其作为 "confirming compression as the bottleneck" 的主要证据——这超出了 exploratory framing 允许的 claim 强度）。

#### Minor（不影响接收）

**M1.** SJ 命名：分母用 max(|g_i|,|g_j|) 而非 |A∪B|——虽然 footnote 已说明，且 Table 5 证明 Δρ<0.01，但 "Soft Jaccard" 这个名称可能误导熟悉 Jaccard index 的读者。建议考虑 "penalized set overlap" 或在首次使用时加注 "a variant penalizing cardinality mismatch"。

**M2.** Section 4.1 报告 SciERC Qwen seed=42 单 seed 结果，而 Table 7 (multi-seed) 显示 VC mean=0.386±0.019。主表值 0.379 是 seed=42 的值——这本身没问题，但 reader 可能困惑为什么主表不用 3-seed mean。建议统一或在表格脚注中更明确说明。

**M3.** "Correlation-selection gap" 的操作性定义出现在 Section 4.3 第一句——但 abstract 和 introduction 已经大量使用这个术语。建议在 Introduction 首次使用时给出 one-sentence 操作性定义。

**M4.** Table 3 selection F1 = 0.647 (LP) 但 Discussion 中 non-tied subset 的 F1 明显更高——这种 subsetting 分析在主表 vs appendix 之间的呈现稍有断裂，可增加一句在 Table 3 caption 中的 forward pointer。

### Questions for Authors

**Q1.** 4B 模型的 instance degeneracy fraction 是多少？如果 4B 产生更多 diversity（degeneracy 更低），但 selection 仍然失败，这会更强力地支持 "task difficulty drives the gap"。反之，如果 degeneracy 也更低但 selection 仍失败，那可能暗示 compression 也是 scale-independent。

**Q2.** 为什么 selection 实验用 2-seed 而非 3-seed（QE 用了 3-seed）？这是计算资源限制还是有方法论原因？

**Q3.** MBR utility correlation (within-instance SJ ρ=0.524 median) 如何计算？对于 21% 的 degenerate instances（F1 identical across all N），ρ 是 undefined——这些 instances 被排除还是赋值 0？

**Q4.** RE free-form decoding 的 selection reversal (+1.8pp) 是否暗示：对于 RE，constrained decoding 本身就是 gap 的原因？如果是，这是否削弱了 "compression is intrinsic" 的 NER 结论（因为它暗示 decoding regime 可以改变 gap 存在与否）？

**Q5.** Table 3 中 Random baseline 0.610 明显低于 Single 0.645——这 0.035pp 差距来源是什么？如果 random 从 N=8 中随机选一个，期望值应等于 mean(per-sample F1)，而 single 是 one draw from the same distribution。两者应该有相同的期望值（都是 E[F1] under T=1.0）——除非 "Single" 实际上使用了与 sampling 不同的 seed/batch？请澄清。

### Missing References

1. **Pasad et al. (2023/2024)** "Minimum Bayes Risk Decoding for Sequence-to-Sequence Models": 直接相关的 MBR decoding for structured outputs 工作，比 Eikema & Aziz 2022 更新且覆盖 seq2seq。
2. **Bertsch et al. (2023)** "It's MBR All the Way Down": 讨论 MBR utility 选择对 selection quality 的影响，与本文 consensus-proximity 策略直接相关。
3. **Xu et al. (2024/2025)** 关于 NER 中 self-consistency 或 sample-and-select 的工作（如有）——当前 related work 未覆盖 NER-specific test-time compute scaling。
4. **Lin & Chen (2023)** "LLM-Eval" or similar works on per-sample scoring for structured outputs as an alternative to consistency-based methods.

### Overall Assessment

**Soundness: 3.5/5** — 方法论上基本严谨，统计实践优秀，但 N1（by-construction limitation 混入 empirical finding）和 N2（单数据集验证）构成 soundness 隐患。消融链逻辑成立，但 claim 强度偶尔超出证据力。

**Excitement: 3.5/5** — QE/selection 解耦 + 诊断链是有价值的贡献，但本质上是 negative result paper（"signals don't work for selection"），impact 依赖于 community 是否在意这个问题。对于做 test-time compute scaling for IE 的研究者有直接参考价值。

**Overall: 3.0 (Borderline: could be accepted to main conference or Findings)** — 贡献真实且实验扎实，但两个核心问题——(1) 核心 finding 部分是 by-construction 的 tautology，(2) selection gap 的非 trivial 验证仅限一个数据集——使其离 clear accept 有距离。如果作者在 rebuttal 中 (a) 重新 frame contribution 使 trivial/non-trivial 部分清晰分离，(b) 补充 4B degeneracy 数据或第二个 medium-difficulty 数据集验证，则可上调至 3.5。

**Confidence: 4/5** — 我熟悉 MBR decoding、self-consistency、NER evaluation、以及 LLM uncertainty estimation 文献。对统计方法（TOST、bootstrap CI）有直接实践经验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1377 · 2026-05-16T07:44:21.945493+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 108

## Round 108

2 recorded events


### User

_source line 1378 · 2026-05-16T07:44:24.509370+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：论文实验扎实、统计实践优秀，但有两个影响接收的问题——(1) 4/5 信号无法选择是 by construction 的结构限制（非 empirical finding），论文 framing 混淆了 trivial 和 non-trivial 部分；(2) selection gap 的有效验证实质上仅限 SciERC 一个数据集。Overall 评分 3.0 (borderline)，可通过 rebuttal 上调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1379 · 2026-05-16T07:44:32.684439+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 完成独立审稿后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 109

## Round 109

6 recorded events


### User

_source line 1380 · 2026-05-16T07:49:24.221372+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

### 论文信息
Title: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
Venue: EMNLP 2026 Main Conference (via ARR May 2026 cycle)

---

## 总体评分
**Overall**: 2.5/5（介于 Findings 和需要 substantial revisions 之间）
**一句话总结**: 实验设计扎实、消融全面，但核心发现（correlation-selection gap）的新颖性有限——它在很大程度上是 MBR 社区已知现象在 IE 场景下的重新标签化，且缺少直接相关的关键文献。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨：3-dataset difficulty gradient、multi-seed stability、free-form ablation (4 seeds)、bootstrap CIs、TOST equivalence testing 等统计工具使用规范。Thinking token confound 的三重论证令人信服。主要扣分：ε=0.05 阈值为 post-hoc 探索性选择。 |
| Excitement | 2/5 | 核心发现（"good QE ≠ good selection"）在 MBR 和 uncertainty 社区有先例；论文将其命名为 correlation-selection gap 并给出 IE 场景的两种机制解释，但未提出有效 remedy。3B-8B scale 限制了对当前主流大模型的指导意义。 |
| Overall | 2.5/5 | 扎实的经验性诊断研究，但增量贡献可能不足以达到 EMNLP main conference 的门槛。更适合 Findings。 |
| Reproducibility | 4/5 | Training config、prompt template、constrained decoding 细节均已公开；代码承诺释放。 |
| Confidence | 4/5 | 审稿人在 uncertainty estimation、MBR decoding、IE 评估方面有较充分背景。 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 与 Yao et al. (2026) 的增量贡献不够清晰
- Section 1 line 8、Section 2 line 10
- 论文声称 Yao et al. "leaving open" 三个问题，但 gap 表述过于笼统。需精确界定：Yao et al. 使用 hard-prompting（非 fine-tuned），instance degeneracy 在其设置中可能不存在——这是否正好是 gap 的来源？
- 建议：明确 Yao et al. 不涉及 fine-tuned models、不区分 QE 与 selection、无 MBR 分析。将差异表格化。

**N2** [critical] "Correlation-selection gap" 与 MBR 社区已知结论的关系未充分讨论
- Section 1 Contribution #1、Section 5 Discussion
- Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。"Good metric correlation ≠ good selection" 在 QE for MT 领域也有先例。论文的贡献应定位为"在 IE 场景下给出两种具体失败机制"，而非发现全新现象。
- 建议：将 Contribution #1 从 "identifying the gap" 改为 "diagnosing two specific failure mechanisms that explain the gap in IE"。

**N3** [critical] 缺少两篇直接相关的重要文献
1. **Schall & de Melo (RANLP 2025)** "The Hidden Cost of Structure" — 直接研究 constrained decoding 如何影响 LP distribution，与 LP compression hypotheses (b)(c) 高度相关
2. **Yun et al. (Findings EMNLP 2025)** "The Price of Format: Diversity Collapse in LLMs" — format templates 导致的 diversity collapse，与 instance degeneracy 直接相关

---

## Should-Fix 问题

**W1** "Moderate-to-strong" QE 措辞有误导性 — ρ=0.38 属 medium effect，ρ=0.45 来自受 inflation 影响的 ceiling-effect control
**W2** 论文定位模糊（diagnostic vs. methodology），应明确定位为 diagnostic study
**W3** 4/5 signals instance-level → cannot select 是 definitional tautology，非 empirical finding
**W4** 3B-8B scale 限制实践指导意义，标题/abstract 未充分限定
**W5** Discussion 中 LP compression hypotheses 列举格式有误，且 (b) 与 (d) 区分不够清晰

---

## 小问题
- Abstract 缺引用
- "Cost-free greedy decoding" 措辞不精确
- WNUT-17 结果不在主文 Table 中
- bhattacharyya2026beyond 引用关联不清楚

---

## 主要优势
- 三数据集难度梯度设计精巧
- 统计方法（Bootstrap CI、TOST with external anchors、Kendall's W）远超同类论文
- 消融链完整连贯
- Instance degeneracy 量化分析有信息量
- 透明度高（主动提出 confounds）

---

## Questions for Authors
1. Yao et al. (2026) hard-prompted LLMs 的 instance degeneracy 比例？degeneracy 是 fine-tuning artifact 还是 task 固有属性？
2. 是否考虑过 LP × VC product 等简单 signal combination？
3. Entity-token LP CoNLL 上 variance ≈ 0 是否说明 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？
4. Greedy (T=0) > all N=8 selection — 是否 temperature sampling 的 noise > selection 能 recover 的 signal？

---

## Missing References
1. Schall & de Melo (RANLP 2025) "The Hidden Cost of Structure"
2. Yun et al. (Findings EMNLP 2025) "The Price of Format: Diversity Collapse in LLMs"
3. Park et al. (NeurIPS 2024) "Grammar-Aligned Decoding"

---

## 引用完整性
- 0 orphan, 0 missing, 42/50 verified
- xie2024selfevaluation 第一作者可能需确认（OpenAlex 匹配 Ren 而非 Xie）
- mejer2010confidence ✓, feng2025optimal ✓, oh2026latentsc (AAAI 2026, 年份正确) ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1381 · 2026-05-16T07:49:48.255675+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳，并提供证据\n\n---\n\n## Reviewer 2 审稿意见原文\n\n### Overall: 2.5/5（介于 Findings 和需要 substantial revisions 之间）\n\n核心判断: 实验设计扎实、消融全面，但核心发现（correlation-selection gap）的新颖性有限——它在很大程度上是 MBR 社区已知现象在 IE 场景下的重新标签化，且缺少直接相关的关键文献。\n\n### Must-Fix 问题\n\n**N1** [critical] 与 Yao et al. (2026) 的增量贡献不够清晰\n- Section 1 line 8、Section 2 line 10\n- 论文声称 Yao et al. \"leaving open\" 三个问题，但 gap 表述过于笼统。需精确界定：Yao et al. 使用 hard-prompting（非 fine-tuned），instance degeneracy 在其设置中可能不存在——这是否正好是 gap 的来源？\n- 建议：明确 Yao et al. 不涉及 fine-tuned models、不区分 QE 与 selection、无 MBR 分析。将差异表格化。\n\n**N2** [critical] \"Correlation-selection gap\" 与 MBR 社区已知结论的关系未充分讨论\n- Section 1 Contribution #1、Section 5 Discussion\n- Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。\"Good metric correlation ≠ good selection\" 在 QE for MT 领域也有先例。论文的贡献应定位为\"在 IE 场景下给出两种具体失败机制\"，而非发现全新现象。\n- 建议：将 Contribution #1 从 \"identifying the gap\" 改为 \"diagnosing two specific failure mechanisms that explain the gap in IE\"。\n\n**N3** [critical] 缺少两篇直接相关的重要文献\n1. Schall & de Melo (RANLP 2025) \"The Hidden Cost of Structure\" — 直接研究 constrained decoding 如何影响 LP distribution，与 LP compression hypotheses (b)(c) 高度相关\n2. Yun et al. (Findings EMNLP 2025) \"The Price of Format: Diversity Collapse in LLMs\" — format templates 导致的 diversity collapse，与 instance degeneracy 直接相关\n\n### Should-Fix 问题\n\n**W1** \"Moderate-to-strong\" QE 措辞有误导性 — ρ=0.38 属 medium effect，ρ=0.45 来自受 inflation 影响的 ceiling-effect control\n\n**W2** 论文定位模糊（diagnostic vs. methodology），应明确定位为 diagnostic study\n\n**W3** 4/5 signals instance-level → cannot select 是 definitional tautology，非 empirical finding\n\n**W4** 3B-8B scale 限制实践指导意义，标题/abstract 未充分限定\n\n**W5** Discussion 中 LP compression hypotheses 列举格式有误，且 (b) 与 (d) 区分不够清晰\n\n### Minor 问题\n- Abstract 缺引用\n- \"Cost-free greedy decoding\" 措辞不精确\n- WNUT-17 结果不在主文 Table 中\n- bhattacharyya2026beyond 引用关联不清楚\n\n### Missing References\n1. Schall & de Melo (RANLP 2025) \"The Hidden Cost of Structure\"\n2. Yun et al. (Findings EMNLP 2025) \"The Price of Format: Diversity Collapse in LLMs\"\n3. Park et al. (NeurIPS 2024) \"Grammar-Aligned Decoding\"\n\n### Questions for Authors\n1. Yao et al. (2026) hard-prompted LLMs 的 instance degeneracy 比例？degeneracy 是 fine-tuning artifact 还是 task 固有属性？\n2. 是否考虑过 LP × VC product 等简单 signal combination？\n3. Entity-token LP CoNLL 上 variance ≈ 0 是否说明 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？\n4. Greedy (T=0) > all N=8 selection — 是否 temperature sampling 的 noise > selection 能 recover 的 signal？\n\n---\n\n请对以上每个 Must-Fix (N1/N2/N3)、Should-Fix (W1-W5)、Missing References 逐条回应 [AGREE] 或 [REBUT]。对 Questions 部分如有补充观点也请说明。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳，并提供证据\n\n---\n\n## Reviewer 2 审稿意见原文\n\n### Overall: 2.5/5（介于 Findings 和需要 substantial revisions 之间）\n\n核心判断: 实验设计扎实、消融全面，但核心发现（correlation-selection gap）的新颖性有限——它在很大程度上是 MBR 社区已知现象在 IE 场景下的重新标签化，且缺少直接相关的关键文献。\n\n### Must-Fix 问题\n\n**N1** [critical] 与 Yao et al. (2026) 的增量贡献不够清晰\n- Section 1 line 8、Section 2 line 10\n- 论文声称 Yao et al. \"leaving open\" 三个问题，但 gap 表述过于笼统。需精确界定：Yao et al. 使用 hard-prompting（非 fine-tuned），instance degeneracy 在其设置中可能不存在——这是否正好是 gap 的来源？\n- 建议：明确 Yao et al. 不涉及 fine-tuned models、不区分 QE 与 selection、无 MBR 分析。将差异表格化。\n\n**N2** [critical] \"Correlation-selection gap\" 与 MBR 社区已知结论的关系未充分讨论\n- Section 1 Contribution #1、Section 5 Discussion\n- Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。\"Good metric correlation ≠ good selection\" 在 QE for MT 领域也有先例。论文的贡献应定位为\"在 IE 场景下给出两种具体失败机制\"，而非发现全新现象。\n- 建议：将 Contribution #1 从 \"identifying the gap\" 改为 \"diagnosing two specific failure mechanisms that explain the gap in IE\"。\n\n**N3** [critical] 缺少两篇直接相关的重要文献\n1. Schall & de Melo (RANLP 2025) \"The Hidden Cost of Structure\" — 直接研究 constrained decoding 如何影响 LP distribution，与 LP compression hypotheses (b)(c) 高度相关\n2. Yun et al. (Findings EMNLP 2025) \"The Price of Format: Diversity Collapse in LLMs\" — format templates 导致的 diversity collapse，与 instance degeneracy 直接相关\n\n### Should-Fix 问题\n\n**W1** \"Moderate-to-strong\" QE 措辞有误导性 — ρ=0.38 属 medium effect，ρ=0.45 来自受 inflation 影响的 ceiling-effect control\n\n**W2** 论文定位模糊（diagnostic vs. methodology），应明确定位为 diagnostic study\n\n**W3** 4/5 signals instance-level → cannot select 是 definitional tautology，非 empirical finding\n\n**W4** 3B-8B scale 限制实践指导意义，标题/abstract 未充分限定\n\n**W5** Discussion 中 LP compression hypotheses 列举格式有误，且 (b) 与 (d) 区分不够清晰\n\n### Minor 问题\n- Abstract 缺引用\n- \"Cost-free greedy decoding\" 措辞不精确\n- WNUT-17 结果不在主文 Table 中\n- bhattacharyya2026beyond 引用关联不清楚\n\n### Missing References\n1. Schall & de Melo (RANLP 2025) \"The Hidden Cost of Structure\"\n2. Yun et al. (Findings EMNLP 2025) \"The Price of Format: Diversity Collapse in LLMs\"\n3. Park et al. (NeurIPS 2024) \"Grammar-Aligned Decoding\"\n\n### Questions for Authors\n1. Yao et al. (2026) hard-prompted LLMs 的 instance degeneracy 比例？degeneracy 是 fine-tuning artifact 还是 task 固有属性？\n2. 是否考虑过 LP × VC product 等简单 signal combination？\n3. Entity-token LP CoNLL 上 variance ≈ 0 是否说明 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？\n4. Greedy (T=0) > all N=8 selection — 是否 temperature sampling 的 noise > selection 能 recover 的 signal？\n\n---\n\n请对以上每个 Must-Fix (N1/N2/N3)、Should-Fix (W1-W5)、Missing References 逐条回应 [AGREE] 或 [REBUT]。对 Questions 部分如有补充观点也请说明。"
  }
}
```

</details>

---


### Tool result

_source line 1382 · 2026-05-16T07:50:18.528586+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30272
}
```

</details>

---


### Tool call

_source line 1383 · 2026-05-16T07:50:18.580316+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳，并提供证据\n\n---\n\n## Reviewer 1 审稿意见原文\n\n### Overall: 3.0 (Borderline: could be accepted to main conference or Findings)\n\n核心判断: 贡献真实且实验扎实，但两个核心问题——(1) 核心 finding 部分是 by-construction 的 tautology，(2) selection gap 的非 trivial 验证仅限一个数据集——使其离 clear accept 有距离。\n\n### Must-Fix\n\n**N1** [critical] Instance-level 信号\"无法选择\"在很大程度上是 by construction，论文区分不够 sharp\n- 4/5 信号是 instance-level aggregates，给同一 input 的所有 N 个候选分配相同分数——它们在字面意义上不具备选择能力。论文用 MBR/consensus-proximity 将其转化为 per-sample ranking，但 MBR 转换后仍然失败才是 empirical finding。当前叙述中，contribution #1 把 instance-level 信号的 by-construction 限制和 LP 的 empirical 失败混在一起计算，夸大了\"5个信号全部失败\"的 surprise factor。\n- 建议：在 Introduction/Method 中更清晰地将 gap 分为两层：(a) structural limitation 和 (b) empirical failure。\n\n**N2** [critical] Selection gap 的有效验证集实质上仅 SciERC 一个数据集\n- CoNLL oracle headroom 仅 4pp（ceiling-effect control）；WNUT-17 信号全部 collapse。真正验证 selection gap 的只有 SciERC。\"The pattern holds across CoNLL and WNUT-17\" 中 CoNLL 上 holding 的原因是 ceiling effect（无 headroom 可选），并非信号失败——这是 qualitatively 不同的原因。\n- 建议：增加一个 medium-difficulty 数据集或软化 claim。\n\n### Should-Fix\n\n**W1** Scale ablation (4B vs 8B) 支撑 \"task difficulty drives the gap\" 结论的证据力不足\n- 仅 2 个规模点，scale 范围极窄。缺少 4B 的 instance degeneracy 数据。\n\n**W2** Fisher combined p 仅基于 2 seeds 的统计合理性\n- 2-seed Fisher 本质上是 χ²(4)，对检测 0.2pp effect size 几乎没有检测力。给人统计严谨性的表象但 power 极低。\n\n**W3** Kendall's W 在 n=3 seeds 下的信息量问题\n- W=1.000 with 3 raters ranking 5 signals，n=3 下即使 W=1.0 也不显著。\n\n**W4** Greedy baseline (T=0) 与 T=1.0 sampling 的比较公平性\n- Greedy 是 deterministic argmax，T=1.0 sampling 引入 substantial noise。两者解决的是不同问题。\"surpassing all N=8 selection strategies\" 的修辞暗示 greedy 是 selection 的公平 competitor。\n- 建议：将 greedy 定位为 \"practical cost-free alternative\" 而非 selection baseline。\n\n**W5** ε=0.05 threshold — \"非 tied 子集 +2.9pp (p=0.004)\" 的 multiple testing 问题\n- ε sweep 从 0.01 到 0.20 selection gain 单调递增——ε=0.05 并非 natural split point。Bonferroni over 5 signals ≠ correction over 7 ε values × 5 signals。\n\n### Minor\n**M1.** SJ 命名（max 分母 vs union）可能误导\n**M2.** 主表 seed=42 单 seed vs multi-seed mean 的选择不够一致\n**M3.** Correlation-selection gap 操作性定义出现太晚\n**M4.** Table 3 → non-tied subset 之间缺少 forward pointer\n\n### Questions\nQ1. 4B instance degeneracy fraction?\nQ2. 为什么 selection 用 2-seed 而非 3-seed?\nQ3. MBR within-instance ρ 对 degenerate instances 如何处理?\nQ4. RE free-form reversal 是否削弱 \"compression is intrinsic\" 结论?\nQ5. Random (0.610) vs Single (0.645) 差距来源?\n\n### Missing References\n1. Pasad et al. (2023/2024) \"MBR Decoding for Seq2Seq\"\n2. Bertsch et al. (2023) \"It's MBR All the Way Down\"\n3. Xu et al. (2024/2025) NER-specific test-time compute scaling\n4. Lin & Chen (2023) LLM-Eval per-sample scoring\n\n---\n\n请对以上每个 Must-Fix (N1/N2)、Should-Fix (W1-W5)、Minor (M1-M4)、Missing References 逐条回应 [AGREE] 或 [REBUT]。对 Questions 部分如有补充观点也请说明。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** 反驳，并提供证据\n\n---\n\n## Reviewer 1 审稿意见原文\n\n### Overall: 3.0 (Borderline: could be accepted to main conference or Findings)\n\n核心判断: 贡献真实且实验扎实，但两个核心问题——(1) 核心 finding 部分是 by-construction 的 tautology，(2) selection gap 的非 trivial 验证仅限一个数据集——使其离 clear accept 有距离。\n\n### Must-Fix\n\n**N1** [critical] Instance-level 信号\"无法选择\"在很大程度上是 by construction，论文区分不够 sharp\n- 4/5 信号是 instance-level aggregates，给同一 input 的所有 N 个候选分配相同分数——它们在字面意义上不具备选择能力。论文用 MBR/consensus-proximity 将其转化为 per-sample ranking，但 MBR 转换后仍然失败才是 empirical finding。当前叙述中，contribution #1 把 instance-level 信号的 by-construction 限制和 LP 的 empirical 失败混在一起计算，夸大了\"5个信号全部失败\"的 surprise factor。\n- 建议：在 Introduction/Method 中更清晰地将 gap 分为两层：(a) structural limitation 和 (b) empirical failure。\n\n**N2** [critical] Selection gap 的有效验证集实质上仅 SciERC 一个数据集\n- CoNLL oracle headroom 仅 4pp（ceiling-effect control）；WNUT-17 信号全部 collapse。真正验证 selection gap 的只有 SciERC。\"The pattern holds across CoNLL and WNUT-17\" 中 CoNLL 上 holding 的原因是 ceiling effect（无 headroom 可选），并非信号失败——这是 qualitatively 不同的原因。\n- 建议：增加一个 medium-difficulty 数据集或软化 claim。\n\n### Should-Fix\n\n**W1** Scale ablation (4B vs 8B) 支撑 \"task difficulty drives the gap\" 结论的证据力不足\n- 仅 2 个规模点，scale 范围极窄。缺少 4B 的 instance degeneracy 数据。\n\n**W2** Fisher combined p 仅基于 2 seeds 的统计合理性\n- 2-seed Fisher 本质上是 χ²(4)，对检测 0.2pp effect size 几乎没有检测力。给人统计严谨性的表象但 power 极低。\n\n**W3** Kendall's W 在 n=3 seeds 下的信息量问题\n- W=1.000 with 3 raters ranking 5 signals，n=3 下即使 W=1.0 也不显著。\n\n**W4** Greedy baseline (T=0) 与 T=1.0 sampling 的比较公平性\n- Greedy 是 deterministic argmax，T=1.0 sampling 引入 substantial noise。两者解决的是不同问题。\"surpassing all N=8 selection strategies\" 的修辞暗示 greedy 是 selection 的公平 competitor。\n- 建议：将 greedy 定位为 \"practical cost-free alternative\" 而非 selection baseline。\n\n**W5** ε=0.05 threshold — \"非 tied 子集 +2.9pp (p=0.004)\" 的 multiple testing 问题\n- ε sweep 从 0.01 到 0.20 selection gain 单调递增——ε=0.05 并非 natural split point。Bonferroni over 5 signals ≠ correction over 7 ε values × 5 signals。\n\n### Minor\n**M1.** SJ 命名（max 分母 vs union）可能误导\n**M2.** 主表 seed=42 单 seed vs multi-seed mean 的选择不够一致\n**M3.** Correlation-selection gap 操作性定义出现太晚\n**M4.** Table 3 → non-tied subset 之间缺少 forward pointer\n\n### Questions\nQ1. 4B instance degeneracy fraction?\nQ2. 为什么 selection 用 2-seed 而非 3-seed?\nQ3. MBR within-instance ρ 对 degenerate instances 如何处理?\nQ4. RE free-form reversal 是否削弱 \"compression is intrinsic\" 结论?\nQ5. Random (0.610) vs Single (0.645) 差距来源?\n\n### Missing References\n1. Pasad et al. (2023/2024) \"MBR Decoding for Seq2Seq\"\n2. Bertsch et al. (2023) \"It's MBR All the Way Down\"\n3. Xu et al. (2024/2025) NER-specific test-time compute scaling\n4. Lin & Chen (2023) LLM-Eval per-sample scoring\n\n---\n\n请对以上每个 Must-Fix (N1/N2)、Should-Fix (W1-W5)、Minor (M1-M4)、Missing References 逐条回应 [AGREE] 或 [REBUT]。对 Questions 部分如有补充观点也请说明。"
  }
}
```

</details>

---


### Tool result

_source line 1384 · 2026-05-16T07:50:20.041842+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1461
}
```

</details>

---


### Assistant

_source line 1385 · 2026-05-16T07:50:25.207436+00:00_

交叉分享已分发给两位 Reviewer。等待逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1386 · 2026-05-16T07:50:27.823685+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论摘要**：

- **Overall 2.5/5**，建议 Findings 而非 Main Conference
- **3 个 Must-Fix**：(1) 与 Yao et al. 的增量不清晰；(2) correlation-selection gap 被 oversold，应定位为 mechanism diagnosis 而非全新发现；(3) 缺少 Schall & de Melo (RANLP 2025) 和 Yun et al. (EMNLP Findings 2025) 两篇直接相关文献
- **5 个 Should-Fix**：moderate-to-strong 措辞误导、定位模糊、4/5 signals 是 tautology、scale 限制、LP hypotheses 格式/区分问题
- **主要优势**：实验设计精巧（3-dataset difficulty gradient）、统计方法远超同类、消融链完整、instance degeneracy 分析有价值
- **引用完整性**：50 条 bib 全部被引用且无遗漏，mejer2010confidence/feng2025optimal/oh2026latentsc 均确认正确

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1387 · 2026-05-16T07:50:32.482634+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 111

## Round 111

2 recorded events


### User

_source line 1388 · 2026-05-16T07:52:04.716216+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: 与 Yao et al. (2026) 的增量贡献界定**

同意需要更清晰的差异化。Section 1 line 8 仅用一句话概括 ("leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient")，但未说明 Yao et al. 使用 hard-prompting 这一关键方法论差异。如果 instance degeneracy (Table 5: 21-58% constant F1) 是 fine-tuning 的产物而非 task 固有属性，那么本文最核心的 failure mechanism 可能不存在于 Yao et al. 的设置中——这恰好构成最强的差异化论点，但论文未抓住。建议作者在 Related Work 中增加一个明确对比段落，将 fine-tuning → low diversity → degeneracy 作为关键区分点。

**[REBUT] R2-N2: "Gap" 是 MBR 社区已知现象的重新标签化**

部分反驳。R2 的论点是 "good metric correlation ≠ good selection" 在 QE for MT 已有先例，且 Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。但有两个关键区别：

1. **失败机制的 specificity**：MBR 文献讨论的是 utility function mismatch（utility 不 align with human quality），而本文诊断的是 instance degeneracy（utility 在 instance 内 positively correlates with F1，median ρ=0.524 on SciERC [Table 5]，但 21% instances 没有任何 headroom 可选）。这不是 utility degradation，而是 headroom elimination——一个 qualitatively 不同的机制。

2. **Structural difference of IE outputs**：MT 中 MBR 失败因为 utility functions (BLEU, COMET) 不 capture quality；本文中 SJ utility DOES capture quality (within-instance ρ=0.524)，但 degeneracy 使其 moot。Section 5 (Discussion) 第二段明确写道："Despite MBR's success in machine translation, all variants fail here because degeneracy eliminates the headroom that positive within-instance correlation would otherwise exploit"——这 IS 新贡献，不是重新标签化。

但我同意 R2 关于 **framing** 的建议：将 Contribution #1 从 "identifying the gap" 调整为 "diagnosing two specific failure mechanisms unique to fine-tuned IE models" 会使 novelty claim 更准确。当前 abstract 和 introduction 的 framing 确实过于强调 "discovery" 而非 "diagnosis"。

**[AGREE with reservation] R2-N3: 缺少两篇关键文献**

关于 relevance 我同意：
- Schall & de Melo ("The Hidden Cost of Structure") 如果确实研究 constrained decoding 对 LP distribution 的影响，则与 hypotheses (b)(c) 直接相关——尽管本文的 free-form ablation (Appendix §10, Panel A: std ratio 0.97) 已经 empirically 排除了 (b)(c) 对 NER 的解释力，引用此文可强化 "我们知道这个 hypothesis，并实证排除了它" 的论证。
- Yun et al. ("The Price of Format") 与 instance degeneracy 话题相关，但需注意：本文的 degeneracy 指 fine-tuned models 产生 identical entity sets（output-level），不同于 format-induced diversity collapse（token-level diversity）。Table 8 (diversity) 显示 SciERC 有 43% unique outputs——degeneracy 不是 universal collapse，而是 instance-specific 的 high-confidence convergence。

**Reservation**：我无法验证这两篇文献是否真实存在（建议 Director 使用 verify_references 确认）。如果存在，应当引用但不改变论文结论。

---

### Should-Fix 问题

**[AGREE] R2-W1: "Moderate-to-strong" 措辞**

ρ=0.38 按 Cohen (1988) 标准属 medium effect (0.3-0.5 range)。论文在 abstract 中写 "moderate-to-strong quality estimation (ρ=0.38 on the primary test bed, up to 0.45 on a ceiling-effect control)"——但 0.45 来自 CoNLL，而论文自身承认 CoNLL 的 ρ 因 zero/non-zero boundary 而被 inflate +0.03-0.05 (Section 3.3 footnote)。"Moderate" 或 "moderate quality estimation" 是更准确的描述。

**[AGREE] R2-W2: 论文定位模糊**

同意。论文同时尝试 (a) 提供实践指导 (Section 5 "Practical recommendations") 和 (b) 诊断失败机制——但 (a) 的 actionable takeaway 很薄弱（"use VC for QE, trained verifiers for selection"）。明确定位为 diagnostic/analytical study 会使期望对齐，也减少 reviewer 对 "so what?" 的追问。

**[AGREE] R2-W3: Instance-level 信号无法选择是 definitional tautology**

强烈同意——这与我的 N1 完全一致。Section 3.1 最后一句确实说明了这一区分，但 abstract/introduction 将 "5 signals all fail at selection" 作为统一 narrative 呈现时，模糊了 trivial (instance-level by construction) 与 non-trivial (MBR conversion fails due to degeneracy; LP fails due to compression) 之间的界限。

**[PARTIALLY AGREE] R2-W4: 3B-8B scale 限制**

同意标题/abstract 未充分限定 scale 范围。但 Limitations 节 (line 2: "whether the gap holds for 70B+ models or closed-source APIs is untested") 和 Conclusion (line 7: "Whether these mechanisms persist at 70B+ scales is an open question") 已有明确限定。问题在于 abstract 中使用 "at two model scales (4B and 8B)" 但未说明这是 narrow range。建议在 abstract 中添加 "in the small-model regime (3B-8B)" 的限定词。

**[PARTIALLY AGREE] R2-W5: Hypotheses (b) 与 (d) 区分不清**

区分确实存在但需要仔细阅读才能理解：
- (b) = constrained decoding **强制产生** schema tokens（因此这些 tokens 必然存在）
- (d) = model **赋予** schema tokens 极高 LP（即使不强制，模型也会产生它们——free-form parse rate 99.95% 证实这一点）

逻辑链是：free-form ablation (std ratio 0.97) 排除 (b)+(c) → 但 format tokens 仍然存在 (parse rate 99.95%) → 所以 (d) 仍可能成立 → entity-token LP ablation 直接测试 (d) → (d) 也不够解释（entity-token variance 在 CoNLL 上 collapse）。

这个推理链是 sound 的，但 Section 5 的呈现确实可以更清晰——特别是 (b) 和 (d) 的关键区别（constraint-imposed vs. model-learned）可以用一句话显式说明。

---

### Missing References

**[CONDITIONAL AGREE]** 三篇 references 的 topic relevance 我认同：
1. Schall & de Melo — constrained decoding ↔ LP distribution 直接相关于 hypothesis (b)(c)
2. Yun et al. — format ↔ diversity 相关于 instance degeneracy 讨论
3. Park et al. "Grammar-Aligned Decoding" — 与 constrained decoding (Willard & Merrill 2023, 本文引用) 属同一 line

但我对 1 和 2 的真实性持保留态度。如果确认存在，应当引用；但即使引用，不改变论文的 empirical findings（free-form ablation 已经排除了 constrained decoding 作为 NER compression 的主因）。

---

### Questions 补充观点

**R2-Q1 (degeneracy: fine-tuning artifact vs task-intrinsic?)**: 极好的问题。与我的 Q1 互补。如果 Yao et al. 的 hard-prompted setting 也有 high degeneracy，则 degeneracy 是 task-intrinsic（NER 答案空间有限）；如果仅 fine-tuned models 有，则是 fine-tuning 导致的 overconfidence。这直接影响论文的 practical relevance：如果是 fine-tuning artifact，那么 alternative training regimes (e.g., diversity-promoting objectives) 可能是比 trained verifiers 更自然的解决方案。

**R2-Q2 (signal combination)**: Limitations 节 (line 10) 承认 "whether signal combinations (e.g., LP × consistency) or learned weightings could close the selection gap is unexplored"。这是合理的 scope limitation，但如果 LP×VC 的简单实验只需几行代码就能做，不做显得遗憾。

**R2-Q4 (temperature noise > selection signal)**: 与我的 W4 高度相关。Greedy (T=0) F1=0.663 > best LP selection 0.647 暗示 T=1.0 的 sampling noise 本身就超过了 selection 能 recover 的信号。但论文应区分两种 use case：(a) 如果你只要一个输出，greedy wins——那为什么 sample？(b) 如果你需要 diverse outputs（for downstream reranking, ensembling），那 selection 的 failure 是 concerning。当前论文隐含假设 (b) 的 setting 但用 (a) 的 greedy baseline 来强化 negative result。

---

### 总结：与 R2 的共识和分歧

**共识领域**（高一致性）：
- Instance-level signals 无法选择是 partly tautological (R2-W3 = 我的 N1)
- Scale 范围需要更明确限定 (R2-W4 ≈ 我的 W1)
- "Moderate-to-strong" 用词需降级 (R2-W1)
- 论文定位应明确为 diagnostic study (R2-W2)
- 与 Yao et al. 的差异化需加强 (R2-N1)

**分歧领域**：
- R2 认为 gap 是 MBR 已知现象的重新标签化 → 我认为 instance degeneracy 是 qualitatively new mechanism（within-instance utility correlation IS positive; failure is from headroom elimination, not utility mismatch）
- R2 给 Overall 2.5 (substantial revisions needed) → 我给 3.0 (borderline)。分歧来源：我认为消融链和统计实践的质量本身有足够 contribution value，即使 framing 需调整；R2 对 novelty 要求更高。

**我的评分是否需要调整**：读完 R2 意见后，我维持 Overall 3.0 不变。R2 的 N2 有道理但我不完全同意其"重新标签化"判断；其他问题大部分与我的发现重合或互补。如果作者能 address N1 (framing) 和 N2 (positioning vs MBR literature) 的 rebuttal，3.0→3.5 是可能的。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1389 · 2026-05-16T07:52:13.698383+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 对 Reviewer 1 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1390 · 2026-05-16T07:52:16.306652+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。主要结论：

- 与 R2 在 5 个点上达成共识（instance-level tautology、scale 限定、QE 措辞、定位、Yao et al. 差异化）
- 在核心分歧点（N2: gap 是否为 MBR 已知现象的重标签化）提出反驳——instance degeneracy 是 qualitatively 不同于 utility mismatch 的失败机制，within-instance ρ=0.524 证明 utility 本身是好的，问题在于 headroom 被消除
- 维持 Overall 3.0 评分不变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1391 · 2026-05-16T07:52:20.821765+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 113

## Round 113

12 recorded events


### User

_source line 1392 · 2026-05-16T07:53:41.846769+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

### Must-Fix
[AGREE] R1-N1: Instance-level 信号 by construction 无法选择，论文叙述混淆 definitional limitation 与 empirical failure。与我的 W3 完全一致。Contribution #1 应重新表述为 mechanism diagnosis。

[AGREE] R1-N2: Selection gap 有效验证仅限 SciERC。CoNLL 无 headroom (4pp)，WNUT-17 信号 collapse。部分 defense：SciERC 上有 4 个独立 model-config 复现（Qwen-8B, LLaMA-8B, Qwen-4B, LLaMA N=16），但确实是单一 difficulty regime。

### Should-Fix
[AGREE] R1-W1: Scale ablation 仅 2 点 (4B/8B)，4B 缺 degeneracy 数据。

[REBUT] R1-W2: Fisher 2-seed 确实 underpowered，但论文核心论证依赖 effect size (d=0.038)、bootstrap CI [-3.0, +4.2]pp、TOST equivalence，非 Fisher p。建议弱化 Fisher combined p 权重，但结论不变。

[AGREE] R1-W3: Kendall's W (n=3) 信息量有限，论文自己也承认 (App. line 399)。

[REBUT] R1-W4: Greedy vs T=1.0 比较从 practitioner 视角有价值（"8× cost 能否胜过零成本 greedy？"），但修辞 "surpassing all selection strategies" 需调整为 "practical cost-free alternative"。

[AGREE] R1-W5: ε=0.05 无 natural breakpoint，CDF smooth，Bonferroni 未覆盖 ε 维度。

### Minor
[AGREE] M1-M4 全部同意。

### Missing References
[REBUT] R1 所提 4 篇中 Pasad et al. 和 Bertsch et al. 是 MBR-for-MT，论文已有 6 篇 MBR 引用，非 critical miss。Xu et al. 和 Lin & Chen 未找到具体论文。

补充：我认为 Schall & de Melo (RANLP 2025) "The Hidden Cost of Structure" 和 Yun et al. (EMNLP Findings 2025) "The Price of Format" 是更严重的遗漏。

### Questions 补充
- Q3: degenerate instances 的 within-instance ρ 应为 undefined (F1 方差=0)，Discussion 中 median ρ=0.524 应排除了这些实例但未明确说明
- Q4: "Intrinsic" claim 应限定为 NER-specific，RE free-form reversal 确实构成反例
- Q5: Random (0.610) vs Single (0.645) 差距 3.5pp 需作者澄清定义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1393 · 2026-05-16T07:55:05.614009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schall de Melo \"The Hidden Cost of Structure\" RANLP 2025 constrained decoding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schall de Melo \"The Hidden Cost of Structure\" RANLP 2025 constrained decoding"
  }
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-16T07:55:06.669947+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yun \"The Price of Format\" \"Diversity Collapse\" EMNLP Findings 2025 LLMs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yun \"The Price of Format\" \"Diversity Collapse\" EMNLP Findings 2025 LLMs"
  }
}
```

</details>

---


### Tool call

_source line 1395 · 2026-05-16T07:55:06.670552+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Park \"Grammar-Aligned Decoding\" NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Park \"Grammar-Aligned Decoding\" NeurIPS 2024"
  }
}
```

</details>

---


### Tool result

_source line 1396 · 2026-05-16T07:55:10.234970+00:00_

Web search results for query: "Schall de Melo "The Hidden Cost of Structure" RANLP 2025 constrained decoding"

Links: [{"title":"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance - ACL Anthology","url":"https://aclanthology.org/2025.ranlp-1.124/"},{"title":"The Hidden Cost of Structure: How Constrained Decoding ...","url":"https://acl-bg.org/proceedings/2025/RANLP%202025/pdf/2025.ranlp-1.124.pdf"},{"title":"How Constrained Decoding Affects Language Model ...","url":"https://aclanthology.org/2025.ranlp-1.124.pdf"},{"title":"RANLP 2025 Programme","url":"https://ranlp.org/ranlp2025/wp-content/uploads/2025/10/Full_RANLP_2025_Programme.pdf"},{"title":"Accepted papers","url":"https://ranlp.org/ranlp2025/index.php/accepted-papers/"},{"title":"RANLP 2025 Natural Language Processing in the ...","url":"https://aclanthology.org/2025.ranlp-1.0.pdf"},{"title":"Appendix","url":"https://arxiv.org/html/2603.03305"}]

I found the paper! Here's what I retrieved:

"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" is a paper by Maximilian Schall and Gerard de Melo, published in the Proceedings of the 15th International Conference on Recent Advances in Natural Language Processing (RANLP 2025) in Varna, Bulgaria.

The paper examines how Large Language Models excel at generating fluent text, but real-world applications increasingly demand structured outputs like JSON that can be programmatically processed. The authors investigate the interaction between task performance and format compliance through comprehensive experiments across 11 models and multiple benchmarks.

A key finding is that the paper uncovers a fundamental divergence between base and instruction-tuned models under structural constraints.

The paper has been published and is available through the ACL Anthology at https://aclanthology.org/2025.ranlp-1.124/


REMINDER: You MUST include the sources above in your response to the user using markdown
…[truncated 12 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 4620
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-16T07:55:12.895793+00:00_

Web search results for query: "Yun "The Price of Format" "Diversity Collapse" EMNLP Findings 2025 LLMs"

Links: [{"title":"The Price of Format: Diversity Collapse in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.836/"},{"title":"The Price of Format: Diversity Collapse in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397426577_The_Price_of_Format_Diversity_Collapse_in_LLMs"},{"title":"[2505.18949] The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/abs/2505.18949"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://aclanthology.org/2025.findings-emnlp.836.pdf"},{"title":"The Price of Format: Diversity Collapse in LLMs","url":"https://arxiv.org/html/2505.18949v1"},{"title":"Chenyang An - ACL Anthology","url":"https://aclanthology.org/people/chenyang-an/unverified/"},{"title":"The Price of Format: Diversity Collapse in LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/price-format-diversity-collapse-llms"},{"title":"Longfei Yun - ACL Anthology","url":"https://aclanthology.org/people/longfei-yun/"},{"title":"[Literature Review] The Price of Format: Diversity Collapse in LLMs","url":"https://www.themoonlight.io/en/review/the-price-of-format-diversity-collapse-in-llms"}]

I found the paper you're looking for. Here's the information:

"The Price of Format: Diversity Collapse in LLMs" is authored by Longfei Yun, Chenyang An, Zilong Wang, Letian Peng, and Jingbo Shang, published in Findings of the Association for Computational Linguistics: EMNLP 2025, pages 15454–15468.

**Key Findings:**

The paper identifies a critical limitation of structured formatting in LLMs: it induces a phenomenon called diversity collapse, where the model generates semantically similar outputs for open-ended inputs, undermining creativity and variability.

The analysis shows that format consistency between fine-tuning and inference is crucial for structure-sensitive tasks (e.g.
…[truncated 574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6225
}
```

</details>

---


### Tool result

_source line 1398 · 2026-05-16T07:55:14.050954+00:00_

Web search results for query: "Park "Grammar-Aligned Decoding" NeurIPS 2024"

Links: [{"title":"Grammar-Aligned Decoding Kanghee Park1∗ Jiayu Wang1∗ Taylor Berg-Kirkpatrick2","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/2bdc2267c3d7d01523e2e17ac0a754f3-Paper-Conference.pdf"},{"title":"Grammar-Aligned Decoding","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://neurips.cc/virtual/2024/poster/96599"},{"title":"[2405.21047] Grammar-Aligned Decoding","url":"https://arxiv.org/abs/2405.21047"},{"title":"Grammar-Aligned Decoding","url":"https://papers.nips.cc/paper_files/paper/2024/hash/2bdc2267c3d7d01523e2e17ac0a754f3-Abstract-Conference.html"},{"title":"Grammar-Aligned Decoding | OpenReview","url":"https://openreview.net/forum?id=5G7ve8E1Lu"},{"title":"NeurIPS Poster Grammar-Aligned Decoding","url":"https://nips.cc/virtual/2024/poster/96599"},{"title":"Grammar-Aligned Decoding","url":"https://arxiv.org/html/2405.21047v3"},{"title":"[Quick Review] Grammar-Aligned Decoding","url":"https://liner.com/review/grammaraligned-decoding"},{"title":"Grammar-aligned decoding | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3738690"}]

Based on the search results, I found comprehensive information about the "Grammar-Aligned Decoding" paper by Park and colleagues at NeurIPS 2024.

## Overview

The paper is authored by Kanghee Park, Jiayu Wang, Taylor Berg-Kirkpatrick, Nadia Polikarpova, and Loris D'Antoni, and was presented at NeurIPS 2024 Main Conference Track.

## Problem Statement

Large Language Models (LLMs) struggle with reliably generating highly structured outputs, such as program code, mathematical formulas, or well-formed markup. Constrained decoding approaches mitigate this problem by greedily restricting what tokens an LLM ca
…[truncated 1210 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7380
}
```

</details>

---


### Tool call

_source line 1399 · 2026-05-16T07:59:40.321170+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 †RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n\n# ===== RECURRING ISSUES (updated Round 14) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 14\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control (4pp headroom), WNUT collapse. 'The pattern holds across CoNLL and WNUT-17' 的 CoNLL holding 原因是无 headroom 而非信号失败——qualitatively 不同. LLaMA SciERC 4 configs 复现增加信心, 但仍限于单一 difficulty regime.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Section 4.3 'pattern holds across CoNLL and WNUT-17' 需区分 ceiling-effect holding 与 signal-failure holding. 建议增加 medium-difficulty 数据集或进一步软化 generalization claim.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 14\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 仍是最核心 framing 问题.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识 (R1-N1 = R2-W3): Contribution #1 将 instance-level by-construction limitation 和 LP empirical failure 混为统一叙事, 夸大了 '5个信号全部失败' 的 surprise factor. Section 3.1 末句有区分但 Abstract/Intro 仍 monolithic. 需清晰两层: (a) structural limitation (instance-level → needs conversion, 非 surprising), (b) empirical failure (MBR conversion 产生 per-sample rankings 后仍失败 + LP compression). 已持续 12 轮.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: 删除 by construction, MBR failure→empirical\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"Contribution 1 明确区分 MBR asymmetry (empirical) + LP compression (empirical)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Abstract 和 Introduction 中 '5 signals all fail' 的统一叙事需拆分为: (a) instance-level 信号需 MBR 转换 (acknowledged design property), (b) MBR 转换后仍失败 despite positive within-instance ρ=0.524 (empirical), (c) LP per-sample 但 compressed (empirical). 当前 Section 5 有此区分, 需向前传递至 Abstract/Intro.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 14\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, ε降为辅助\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 R1-W5 + R2 AGREE: ε sweep 0.01-0.20 gain 单调递增, 0.05 非 natural split point. Bonferroni over 5 signals ≠ correction over 7ε×5 signals. Discussion 将 non-tied +2.9pp 用作 'confirming compression as bottleneck' 的主要证据, 超出 exploratory framing 允许的 claim 强度.\"\n  action_items:\n  - round: 12\n    action: \"Abstract '60% tied'→continuous, ε降为辅助 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Discussion 第二段 non-tied subset 结果应明确定位为 exploratory/descriptive. 当前 'confirming compression as the bottleneck' phrasing 过强.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R2 标为 Must-Fix. R1 部分同意.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识 (R2-N1 + R1 AGREE): Yao et al. 使用 hard-prompting 非 fine-tuned, instance degeneracy 可能不存在于其设置中. 这恰好是最强差异化论点但论文未抓住. Related Work 需增加对比段落: fine-tuning → low diversity → degeneracy 作为关键区分. Section 1 line 8 的 'leaving open' 表述过于笼统.\"\n  action_items:\n  - round: 12\n    action: \"Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"重心转向 MBR failure + LP diagnostics 作为核心贡献\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Related Work 增加明确对比段落: (1) Yao et al. = hard-prompted, 本文 = fine-tuned; (2) instance degeneracy 可能是 fine-tuning 产物而非 task 固有; (3) QE/selection 解耦是独立于 Yao et al. 的贡献.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识.\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文 Conclusion 已限定.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: R2-W4 + R1 PARTIALLY AGREE. Conclusion 和 Limitations 已限定, 但 Abstract 中 'at two model scales (4B and 8B)' 未说明是 narrow range. 建议 abstract 添加 'in the small-model regime'.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 14\n    action: \"Abstract 中 'at two model scales (4B and 8B)' 添加 'in the small-model regime (3B-8B)' 限定.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.000 p≈0.05 仅 borderline significant\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 两位再次同意.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 R1-W3 + R2 AGREE: n=3 W=1.0 在 α=0.05 不显著. 3-seed 的功能是 sanity check (排除 catastrophic seed sensitivity) 而非统计推断依据. 不应在 abstract 中作为 robustness evidence 首行引用.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"明确 3-seed 功能定位为 sanity check, 避免作为 robustness 证据的第一引用.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation — (b)/(d) 区分\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 hypotheses\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Discussion 已列出 (a)(b)(c)(d), 编号错误 three→four\"\n  - round: 13\n    reviewers: [2]\n    note: \"(a)-(d) 并列结构不一致\"\n  - round: 14\n    reviewers: [1]\n    note: \"R14 R1 PARTIALLY AGREE R2-W5: (b)=constrained decoding 强制 schema tokens vs (d)=model 自主赋予高 LP. 区分 sound 但需一句话显式说明 'constraint-imposed vs model-learned'. 当前论文写 'four mechanisms', 编号已修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four' mechanisms\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 14\n    action: \"(b) 和 (d) 之间添加一句显式说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax\"\n  - round: 12\n    reviewers: []\n    note: \"Table 2 已改为 'Single‡' 标注\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"缺少 greedy (argmax) baseline\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Greedy T=0 F1=0.663 已加入 Table 2. 但修辞问题转移至 R14-W2.\"\n  action_items:\n  - round: 13\n    action: \"增加 greedy (T=0, argmax) decoding baseline\"\n    assigned_to: Main Agent\n    status: done\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed, RE 单 seed\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"需解释原因\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. Figure 1 caption 当前版本已含 LP 说明.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出\"\n  - round: 14\n    reviewers: [1]\n    note: \"R14 R1 交叉回应补充: 'intrinsic' claim 应限定为 NER-specific, RE free-form reversal 构成反例.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ISSUES FROM ROUND 12 (updated R14) =====\n- id: R12-N1\n  summary: \"ρ=0.45 headline 来自 ceiling-effect dataset, primary dataset 仅 ρ=0.379\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"改措辞为 moderate-to-strong 或加限定语\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"论文 Abstract 已改用 'moderate-to-strong' 但仍以 ρ=0.45 作为 headline.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识 (R2-W1 + R1 AGREE): ρ=0.38 按 Cohen (1988) 属 medium effect. 'moderate-to-strong' 中的 'strong' 来自 CoNLL ρ=0.45, 而 CoNLL 的 ρ 因 zero/non-zero boundary inflate +0.03-0.05. 建议用 'moderate' 或明确标注 ρ=0.45 来源.\"\n  action_items:\n  - round: 12\n    action: \"'strong quality estimation' 改为 'moderate-to-strong'\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 14\n    action: \"Abstract/Intro headline: 'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset, 应改为 'moderate (ρ=0.38 on primary, up to 0.45 on ceiling-effect control)' 或直接用 'moderate'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"Entity-token LP 已测试但失败. R2 仍建议 LP×VC combination.\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. Entity-token LP 作为 negative pilot remedy 已纳入. LP×VC 仍未测试.\"\n  action_items:\n  - round: 12\n    action: \"增加至少一个 pilot remedy 实验\"\n    assigned_to: Main Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Section 3.3 vs Table A13 n 值不一致\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. Section 3.3 当前写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453 统一适用于 QE 和 selection.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"两位独立标记\"\n  - round: 13\n    reviewers: [2]\n    note: \"(a)-(d) 并列结构不一致\"\n  - round: 14\n    reviewers: [1]\n    note: \"论文当前写 'four (non-mutually-exclusive) mechanisms'. 编号已修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four'\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Eq.4 用 max(|g_i|,|g_j|) 而非 |A∪B|\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"共识降级: terminology preference, 非实质问题.\"\n  - round: 14\n    reviewers: [1]\n    note: \"R14 R1-M1: 仍建议考虑 'penalized set overlap' 或首次使用时加注. Footnote 已有说明, Appendix Table 5 证明 Δρ<0.01.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [2]\n    note: \"OpenAlex 匹配 2026 版本\"\n  - round: 14\n    reviewers: [2]\n    note: \"R14 R2 确认: oh2026latentsc, AAAI 2026, 年份正确.\"\n  action_items:\n  - round: 12\n    action: \"核实并更新 bib year\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n\n# ===== ISSUES FROM ROUND 13 (updated R14) =====\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"全做 (加 TACRED) 或全移 Appendix\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. RE 已移至 Appendix 作为 exploratory extension (Appendix E). 标题聚焦 NER. Abstract 仅提及 'exploratory extension to relation extraction'. 主表为 NER-only.\"\n  action_items:\n  - round: 13\n    action: \"RE 全移 Appendix 作为 exploratory extension\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 (9句覆盖全部机制和数字)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"精简 Abstract: 移除 MBR mechanical 细节\"\n  - round: 14\n    reviewers: [2]\n    note: \"R14 R2 minor: Abstract 仍覆盖 MBR conversion、LP 0.041 nats、free-form、entity-token. 但未被 Must-Fix 提及, 可能改善程度可接受.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"mejer2011→2010, feng2025 author mismatch\"\n  - round: 14\n    reviewers: [2]\n    note: \"R14 R2 引用审核: mejer2010confidence ✓, feng2025optimal ✓, oh2026latentsc ✓. 42/50 verified.\"\n  action_items:\n  - round: 13\n    action: \"核实并修正 bib entries\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"术语应统一\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"统一小数位数\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. 论文当前统一使用 3 位小数.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 14) =====\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系未充分讨论, 贡献定位需从 discovery 转为 diagnosis\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N2 提出 gap 是 MBR 已知现象的重标签化. R1 REBUT: instance degeneracy (within-instance ρ=0.524 但 21% 无 headroom) 是 qualitatively 不同于 utility mismatch 的新机制. 但 R1 同意 framing 应从 'identifying the gap' 转为 'diagnosing two specific failure mechanisms unique to fine-tuned IE models'. 部分分歧但实质共识: 贡献定位需调整.\"\n  action_items:\n  - round: 14\n    action: \"Contribution #1 从 'identifying the correlation-selection gap' 改为 'diagnosing two specific failure mechanisms (instance degeneracy + LP compression) that explain why QE does not translate to selection in fine-tuned IE models'. Related Work 需讨论 Eikema et al. (2025) 的 MBR utility degradation 与本文 degeneracy mechanism 的 qualitative 区别.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N3 提出, R1 CONDITIONAL AGREE (已验证存在). (1) Schall & de Melo 'The Hidden Cost of Structure' (RANLP 2025, ACL Anthology) 直接研究 constrained decoding 对 LP distribution 的影响, 与 hypothesis (b)(c) 相关. (2) Yun et al. 'The Price of Format: Diversity Collapse' (Findings EMNLP 2025, ACL Anthology) format template → diversity collapse, 与 instance degeneracy 相关但不同 (output-level vs token-level). (3) Park et al. 'Grammar-Aligned Decoding' (NeurIPS 2024) constrained decoding 同线.\"\n  action_items:\n  - round: 14\n    action: \"引用 Schall & de Melo (RANLP 2025), Yun et al. (EMNLP Findings 2025), 考虑 Park et al. (NeurIPS 2024). Schall 可强化 'we know hypothesis (b)(c) and empirically rule them out'. Yun 可讨论 format-induced diversity 与 fine-tuning degeneracy 的区别.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) 统计效力极低, 应降级为辅助证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W2 提出. R2 REBUT (结论不依赖 Fisher, 核心依据是 d=0.038 + bootstrap CI + TOST). 实质共识: Fisher p 呈现权重应降低.\"\n  action_items:\n  - round: 14\n    action: \"Table 2 将 Fisher combined p 降级为辅助, 主文依赖 bootstrap CI 和 effect size 作为主要推断依据.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W4 提出. R2 REBUT 认为从 practitioner 视角有价值, 但同意 'surpassing all N=8 selection strategies' 修辞需调整. 实质共识: greedy 应定位为 'practical cost-free alternative' 而非 selection baseline. 需区分两种 use case: (a) 单输出→greedy wins, (b) 需要 diverse outputs→selection failure is concerning.\"\n  action_items:\n  - round: 14\n    action: \"Section 4.3 和 Discussion 将 greedy 从 'surpassing all selection strategies' 修辞改为 'practical cost-free alternative'. 明确讨论 sampling 的价值在 QE 而非 selection.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation 缺少 instance degeneracy 统计\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W1 提出, R2 AGREE. 4B 的 constant F1 fraction 和 oracle headroom 未报告, 无法判断 gap 是 task difficulty 还是 degeneracy pattern 驱动.\"\n  action_items:\n  - round: 14\n    action: \"报告 4B 的 degeneracy 统计 (constant F1 fraction, oracle headroom) 或承认 2-point scale ablation 限制.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-Q5: 两者期望值应相同 (E[F1] under T=1.0), 除非 'Single' 使用了不同 seed/batch. 需作者澄清.\"\n  action_items:\n  - round: 14\n    action: \"澄清 Random vs Single baseline 的定义差异和 3.5pp 差距来源.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-M2: Table 1 VC=0.379 (seed=42) vs Table 7 VC mean=0.386±0.019. 虽然正确但可能造成混淆.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 或 footnote 中更明确说明为何使用单 seed 而非 3-seed mean.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-M3: 建议 Introduction 首次使用时给出 one-sentence 操作性定义.\"\n  action_items:\n  - round: 14\n    action: \"Introduction 首次使用 'correlation-selection gap' 时添加 one-sentence 操作性定义.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 †RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n\n# ===== RECURRING ISSUES (updated Round 14) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 14\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control (4pp headroom), WNUT collapse. 'The pattern holds across CoNLL and WNUT-17' 的 CoNLL holding 原因是无 headroom 而非信号失败——qualitatively 不同. LLaMA SciERC 4 configs 复现增加信心, 但仍限于单一 difficulty regime.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Section 4.3 'pattern holds across CoNLL and WNUT-17' 需区分 ceiling-effect holding 与 signal-failure holding. 建议增加 medium-difficulty 数据集或进一步软化 generalization claim.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 14\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 仍是最核心 framing 问题.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识 (R1-N1 = R2-W3): Contribution #1 将 instance-level by-construction limitation 和 LP empirical failure 混为统一叙事, 夸大了 '5个信号全部失败' 的 surprise factor. Section 3.1 末句有区分但 Abstract/Intro 仍 monolithic. 需清晰两层: (a) structural limitation (instance-level → needs conversion, 非 surprising), (b) empirical failure (MBR conversion 产生 per-sample rankings 后仍失败 + LP compression). 已持续 12 轮.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: 删除 by construction, MBR failure→empirical\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"Contribution 1 明确区分 MBR asymmetry (empirical) + LP compression (empirical)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Abstract 和 Introduction 中 '5 signals all fail' 的统一叙事需拆分为: (a) instance-level 信号需 MBR 转换 (acknowledged design property), (b) MBR 转换后仍失败 despite positive within-instance ρ=0.524 (empirical), (c) LP per-sample 但 compressed (empirical). 当前 Section 5 有此区分, 需向前传递至 Abstract/Intro.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 14\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, ε降为辅助\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 R1-W5 + R2 AGREE: ε sweep 0.01-0.20 gain 单调递增, 0.05 非 natural split point. Bonferroni over 5 signals ≠ correction over 7ε×5 signals. Discussion 将 non-tied +2.9pp 用作 'confirming compression as bottleneck' 的主要证据, 超出 exploratory framing 允许的 claim 强度.\"\n  action_items:\n  - round: 12\n    action: \"Abstract '60% tied'→continuous, ε降为辅助 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Discussion 第二段 non-tied subset 结果应明确定位为 exploratory/descriptive. 当前 'confirming compression as the bottleneck' phrasing 过强.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13: R2 标为 Must-Fix. R1 部分同意.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识 (R2-N1 + R1 AGREE): Yao et al. 使用 hard-prompting 非 fine-tuned, instance degeneracy 可能不存在于其设置中. 这恰好是最强差异化论点但论文未抓住. Related Work 需增加对比段落: fine-tuning → low diversity → degeneracy 作为关键区分. Section 1 line 8 的 'leaving open' 表述过于笼统.\"\n  action_items:\n  - round: 12\n    action: \"Camera-ready 级: 添加 1-2 句对 Yao et al. 的量化对比\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 13\n    action: \"重心转向 MBR failure + LP diagnostics 作为核心贡献\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"Related Work 增加明确对比段落: (1) Yao et al. = hard-prompted, 本文 = fine-tuned; (2) instance degeneracy 可能是 fine-tuning 产物而非 task 固有; (3) QE/selection 解耦是独立于 Yao et al. 的贡献.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识.\"\n  - round: 13\n    reviewers: []\n    note: \"R13 未被独立提及. 论文 Conclusion 已限定.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: R2-W4 + R1 PARTIALLY AGREE. Conclusion 和 Limitations 已限定, 但 Abstract 中 'at two model scales (4B and 8B)' 未说明是 narrow range. 建议 abstract 添加 'in the small-model regime'.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 14\n    action: \"Abstract 中 'at two model scales (4B and 8B)' 添加 'in the small-model regime (3B-8B)' 限定.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.000 p≈0.05 仅 borderline significant\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 两位再次同意.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 R1-W3 + R2 AGREE: n=3 W=1.0 在 α=0.05 不显著. 3-seed 的功能是 sanity check (排除 catastrophic seed sensitivity) 而非统计推断依据. 不应在 abstract 中作为 robustness evidence 首行引用.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 14\n    action: \"明确 3-seed 功能定位为 sanity check, 避免作为 robustness 证据的第一引用.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation — (b)/(d) 区分\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 hypotheses\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Discussion 已列出 (a)(b)(c)(d), 编号错误 three→four\"\n  - round: 13\n    reviewers: [2]\n    note: \"(a)-(d) 并列结构不一致\"\n  - round: 14\n    reviewers: [1]\n    note: \"R14 R1 PARTIALLY AGREE R2-W5: (b)=constrained decoding 强制 schema tokens vs (d)=model 自主赋予高 LP. 区分 sound 但需一句话显式说明 'constraint-imposed vs model-learned'. 当前论文写 'four mechanisms', 编号已修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four' mechanisms\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 14\n    action: \"(b) 和 (d) 之间添加一句显式说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"T=1.0 sample 不等于 argmax\"\n  - round: 12\n    reviewers: []\n    note: \"Table 2 已改为 'Single‡' 标注\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"缺少 greedy (argmax) baseline\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Greedy T=0 F1=0.663 已加入 Table 2. 但修辞问题转移至 R14-W2.\"\n  action_items:\n  - round: 13\n    action: \"增加 greedy (T=0, argmax) decoding baseline\"\n    assigned_to: Main Agent\n    status: done\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"CoNLL 高 tied fraction 更可能因 task easiness\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1]\n    note: \"Table 3 NER 2-seed, RE 单 seed\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"需解释原因\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"共识\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. Figure 1 caption 当前版本已含 LP 说明.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"LP 分布 intrinsic (std ratio 0.97), 但 RE selection outcome 反转机制未解释\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出\"\n  - round: 14\n    reviewers: [1]\n    note: \"R14 R1 交叉回应补充: 'intrinsic' claim 应限定为 NER-specific, RE free-form reversal 构成反例.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== ISSUES FROM ROUND 12 (updated R14) =====\n- id: R12-N1\n  summary: \"ρ=0.45 headline 来自 ceiling-effect dataset, primary dataset 仅 ρ=0.379\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"改措辞为 moderate-to-strong 或加限定语\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"论文 Abstract 已改用 'moderate-to-strong' 但仍以 ρ=0.45 作为 headline.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识 (R2-W1 + R1 AGREE): ρ=0.38 按 Cohen (1988) 属 medium effect. 'moderate-to-strong' 中的 'strong' 来自 CoNLL ρ=0.45, 而 CoNLL 的 ρ 因 zero/non-zero boundary inflate +0.03-0.05. 建议用 'moderate' 或明确标注 ρ=0.45 来源.\"\n  action_items:\n  - round: 12\n    action: \"'strong quality estimation' 改为 'moderate-to-strong'\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 14\n    action: \"Abstract/Intro headline: 'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset, 应改为 'moderate (ρ=0.38 on primary, up to 0.45 on ceiling-effect control)' 或直接用 'moderate'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"Entity-token LP 已测试但失败. R2 仍建议 LP×VC combination.\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. Entity-token LP 作为 negative pilot remedy 已纳入. LP×VC 仍未测试.\"\n  action_items:\n  - round: 12\n    action: \"增加至少一个 pilot remedy 实验\"\n    assigned_to: Main Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Section 3.3 vs Table A13 n 值不一致\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. Section 3.3 当前写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453 统一适用于 QE 和 selection.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"两位独立标记\"\n  - round: 13\n    reviewers: [2]\n    note: \"(a)-(d) 并列结构不一致\"\n  - round: 14\n    reviewers: [1]\n    note: \"论文当前写 'four (non-mutually-exclusive) mechanisms'. 编号已修正.\"\n  action_items:\n  - round: 12\n    action: \"修正 'three' → 'four'\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"Eq.4 用 max(|g_i|,|g_j|) 而非 |A∪B|\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"共识降级: terminology preference, 非实质问题.\"\n  - round: 14\n    reviewers: [1]\n    note: \"R14 R1-M1: 仍建议考虑 'penalized set overlap' 或首次使用时加注. Footnote 已有说明, Appendix Table 5 证明 Δρ<0.01.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers: [2]\n    note: \"OpenAlex 匹配 2026 版本\"\n  - round: 14\n    reviewers: [2]\n    note: \"R14 R2 确认: oh2026latentsc, AAAI 2026, 年份正确.\"\n  action_items:\n  - round: 12\n    action: \"核实并更新 bib year\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n\n# ===== ISSUES FROM ROUND 13 (updated R14) =====\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"全做 (加 TACRED) 或全移 Appendix\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. RE 已移至 Appendix 作为 exploratory extension (Appendix E). 标题聚焦 NER. Abstract 仅提及 'exploratory extension to relation extraction'. 主表为 NER-only.\"\n  action_items:\n  - round: 13\n    action: \"RE 全移 Appendix 作为 exploratory extension\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 (9句覆盖全部机制和数字)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"精简 Abstract: 移除 MBR mechanical 细节\"\n  - round: 14\n    reviewers: [2]\n    note: \"R14 R2 minor: Abstract 仍覆盖 MBR conversion、LP 0.041 nats、free-form、entity-token. 但未被 Must-Fix 提及, 可能改善程度可接受.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"mejer2011→2010, feng2025 author mismatch\"\n  - round: 14\n    reviewers: [2]\n    note: \"R14 R2 引用审核: mejer2010confidence ✓, feng2025optimal ✓, oh2026latentsc ✓. 42/50 verified.\"\n  action_items:\n  - round: 13\n    action: \"核实并修正 bib entries\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 13\n    reviewers: [2]\n    note: \"术语应统一\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 9\n    reviewers: [1, 2]\n    note: \"统一小数位数\"\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. 论文当前统一使用 3 位小数.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 14\n    reviewers: []\n    note: \"R14 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 14) =====\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系未充分讨论, 贡献定位需从 discovery 转为 diagnosis\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N2 提出 gap 是 MBR 已知现象的重标签化. R1 REBUT: instance degeneracy (within-instance ρ=0.524 但 21% 无 headroom) 是 qualitatively 不同于 utility mismatch 的新机制. 但 R1 同意 framing 应从 'identifying the gap' 转为 'diagnosing two specific failure mechanisms unique to fine-tuned IE models'. 部分分歧但实质共识: 贡献定位需调整.\"\n  action_items:\n  - round: 14\n    action: \"Contribution #1 从 'identifying the correlation-selection gap' 改为 'diagnosing two specific failure mechanisms (instance degeneracy + LP compression) that explain why QE does not translate to selection in fine-tuned IE models'. Related Work 需讨论 Eikema et al. (2025) 的 MBR utility degradation 与本文 degeneracy mechanism 的 qualitative 区别.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R2-N3 提出, R1 CONDITIONAL AGREE (已验证存在). (1) Schall & de Melo 'The Hidden Cost of Structure' (RANLP 2025, ACL Anthology) 直接研究 constrained decoding 对 LP distribution 的影响, 与 hypothesis (b)(c) 相关. (2) Yun et al. 'The Price of Format: Diversity Collapse' (Findings EMNLP 2025, ACL Anthology) format template → diversity collapse, 与 instance degeneracy 相关但不同 (output-level vs token-level). (3) Park et al. 'Grammar-Aligned Decoding' (NeurIPS 2024) constrained decoding 同线.\"\n  action_items:\n  - round: 14\n    action: \"引用 Schall & de Melo (RANLP 2025), Yun et al. (EMNLP Findings 2025), 考虑 Park et al. (NeurIPS 2024). Schall 可强化 'we know hypothesis (b)(c) and empirically rule them out'. Yun 可讨论 format-induced diversity 与 fine-tuning degeneracy 的区别.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) 统计效力极低, 应降级为辅助证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W2 提出. R2 REBUT (结论不依赖 Fisher, 核心依据是 d=0.038 + bootstrap CI + TOST). 实质共识: Fisher p 呈现权重应降低.\"\n  action_items:\n  - round: 14\n    action: \"Table 2 将 Fisher combined p 降级为辅助, 主文依赖 bootstrap CI 和 effect size 作为主要推断依据.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W4 提出. R2 REBUT 认为从 practitioner 视角有价值, 但同意 'surpassing all N=8 selection strategies' 修辞需调整. 实质共识: greedy 应定位为 'practical cost-free alternative' 而非 selection baseline. 需区分两种 use case: (a) 单输出→greedy wins, (b) 需要 diverse outputs→selection failure is concerning.\"\n  action_items:\n  - round: 14\n    action: \"Section 4.3 和 Discussion 将 greedy 从 'surpassing all selection strategies' 修辞改为 'practical cost-free alternative'. 明确讨论 sampling 的价值在 QE 而非 selection.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation 缺少 instance degeneracy 统计\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R1-W1 提出, R2 AGREE. 4B 的 constant F1 fraction 和 oracle headroom 未报告, 无法判断 gap 是 task difficulty 还是 degeneracy pattern 驱动.\"\n  action_items:\n  - round: 14\n    action: \"报告 4B 的 degeneracy 统计 (constant F1 fraction, oracle headroom) 或承认 2-point scale ablation 限制.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-Q5: 两者期望值应相同 (E[F1] under T=1.0), 除非 'Single' 使用了不同 seed/batch. 需作者澄清.\"\n  action_items:\n  - round: 14\n    action: \"澄清 Random vs Single baseline 的定义差异和 3.5pp 差距来源.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-M2: Table 1 VC=0.379 (seed=42) vs Table 7 VC mean=0.386±0.019. 虽然正确但可能造成混淆.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 或 footnote 中更明确说明为何使用单 seed 而非 3-seed mean.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-M3: 建议 Introduction 首次使用时给出 one-sentence 操作性定义.\"\n  action_items:\n  - round: 14\n    action: \"Introduction 首次使用 'correlation-selection gap' 时添加 one-sentence 操作性定义.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1400 · 2026-05-16T07:59:40.474599+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 31321}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 153
}
```

</details>

---


### Tool call

_source line 1401 · 2026-05-16T08:02:12.894773+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 14\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+相关工作+写作格式）\n**审稿轮次**: Round 1 独立初审 → 交叉分享 (完整原文转发 + 逐条 AGREE/REBUT) → 收敛判断：**1 轮收敛**\n\n---\n\n## Summary\n\n本文评估 LLM-based NER 中 5 种置信信号（SJ, VC, FK, EM, LP）在质量估计和 best-of-N 选择上的表现。核心发现 \"correlation-selection gap\"：信号能预测哪些 instance 做得好（ρ=0.38 on SciERC），但无法选出比 greedy decoding 更好的样本。论文诊断两种失败机制——instance degeneracy（21-58% instances 产生相同 F1）和 LP compression（median within-instance range 0.041 nats），并通过 free-form decoding、entity-token LP isolation、verbalized confidence 三步消融链验证 compression 是 model/task 内在属性。实验覆盖三数据集难度梯度、两个模型族（Qwen3, LLaMA-3.1）、两种规模（4B, 8B）。\n\n---\n\n## Strengths\n\n**S1. 概念贡献有实践价值** [R1-S1, R2 同意]\nQE/selection 解耦是本文核心洞察。实践者可能误以为高 ρ 信号能做 best-of-N 选择——本文明确指出这一 fallacy。在 IE 领域尚未被清晰阐述。\n\n**S2. 诊断消融链逻辑严密** [R1-S2, R2 同意]\nFree-form decoding (std ratio 0.97, 4 seeds) → entity-token LP (4× variance 但 -2.0pp selection) → verbalized confidence (更压缩) → 每步排除一个 hypothesis 并有量化证据。RE free-form 反向效果恰当标注为 regime-dependent。\n\n**S3. 统计实践远超 NLP 论文平均水平** [R1-S3, R2-Soundness 4/5]\nBootstrap CI (B=10,000)、TOST equivalence testing（含 3 组外部锚定 δ）、Fisher combined p、ε sensitivity sweep、multi-seed Kendall's W、FK independence permutation test。方法论上非常负责。\n\n**S4. 三数据集难度梯度设计精巧** [R1-S4, R2 同意]\nSciERC (medium, 65% F1) + CoNLL (ceiling-effect, 91%) + WNUT-17 (collapse, 52% zero-F1)，各自角色明确标注。避免了将 boundary conditions 过度 claim 为 validation。\n\n**S5. Instance degeneracy 量化分析有信息量** [R1-S5, R2 同意]\nTable 5 的 degeneracy 统计（constant F1/constant utility/oracle gap closed/within-instance ρ）是本文最有价值的实证贡献之一。MBR 社区讨论 utility degradation，但 \"utility IS good (ρ=0.524) yet headroom IS eliminated\" 是更精确的诊断。\n\n**S6. 透明度高** [R1-S5, R2-Reproducibility 4/5]\n主动提出 confounds（thinking token 三重论证、SJ normalizer robustness、LOO-SJ equivalence、ε sensitivity、external TOST anchors），代码承诺释放。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [CONSENSUS] Contribution #1 framing 混淆 definitional tautology 与 empirical failure**\n- R1-N1 提出，R2-W3 独立提出，交叉分享强共识\n- 4/5 信号是 instance-level aggregates → 给所有候选分配相同 QE 分数 → 不能直接选择。这是 by construction 的属性，非 empirical finding。论文用 MBR/consensus-proximity 转化为 per-sample ranking 后仍失败才是 empirical finding（within-instance ρ=0.524 但 21% instances 无 headroom）。LP 的 compression 也是独立的 empirical failure。\n- 当前 Abstract/Introduction 将 \"5 signals all fail at selection\" 作为统一 narrative，夸大了 surprise factor。Section 5 (Discussion) 有两层区分但未向前传递至 Abstract/Introduction。\n- **此问题已持续 12 轮（R3-W2 → R14），是最核心 framing 障碍。**\n- 行动：Abstract/Intro 明确拆分三层——(a) instance-level 信号需 MBR 转换 (acknowledged design property, not surprising), (b) MBR 转换后仍失败 despite positive within-instance ρ (empirical), (c) LP per-sample 但 compressed (empirical)。\n\n**MF2. [CONSENSUS] Selection gap 有效验证仅限 SciERC 单数据集**\n- R1-N2 提出，R2 AGREE\n- CoNLL oracle headroom 仅 4pp（论文正确标注为 ceiling-effect control），WNUT-17 信号 collapse（capability boundary）。真正验证 selection gap 的 non-trivial setting 仅 SciERC。Table 6 中 LLaMA/SciERC 在同一数据集上用不同模型 replicate 了 gap，增加了模型维度信心，但仍限于单一 difficulty regime。\n- Section 4.3 \"The pattern holds across CoNLL and WNUT-17\" 中 CoNLL 的 \"holding\" 原因是无 headroom（ceiling effect），非信号失败——qualitatively 不同的原因。\n- 行动：增加 medium-difficulty 数据集（如 Few-NERD subset）或进一步软化 generalization claim。Section 4.3 需区分 ceiling-effect holding 与 signal-failure holding。\n\n**MF3. [CONSENSUS] 与 Yao et al. (2026) 增量贡献界定不清**\n- R2-N1 提出，R1 AGREE\n- Section 1 line 8 用一句话概括差异（\"leaving open\" 三个问题），但未说明 Yao et al. 使用 hard-prompting 而非 fine-tuned models 这一关键方法论差异。如果 instance degeneracy 是 fine-tuning 产物（高 confidence convergence），则本文最核心的 failure mechanism 不存在于 Yao et al. 的设置中——这恰好构成最强差异化论点，但论文未利用。\n- 行动：Related Work 增加对比段落，将 fine-tuning → low diversity → degeneracy 作为与 Yao et al. 的关键区分。\n\n**MF4. [PARTIAL DIVERGENCE → CONSENSUS ON ACTION] Gap 与 MBR 社区已知结论的定位**\n- R2-N2 提出（gap 是 MBR 已知现象的重标签化），R1 REBUT（instance degeneracy ≠ utility mismatch：MBR 文献讨论 utility function 不 align with quality，本文中 SJ utility DOES correlate with F1 within instances (ρ=0.524)，失败来自 headroom elimination）\n- 分歧点：R2 认为 novelty 有限（2.5/5），R1 认为 degeneracy 是 qualitatively 新机制（3.0/5）\n- **实质共识**：Contribution #1 应从 \"identifying the gap\" 调整为 \"diagnosing two specific failure mechanisms (instance degeneracy + LP compression) that explain why QE does not translate to selection in fine-tuned IE models\"。需在 Related Work 中明确讨论与 Eikema et al. (2025) MBR utility degradation 的区别。\n\n**MF5. [CONSENSUS] 缺少两篇直接相关文献**\n- R2-N3 提出，R1 CONDITIONAL AGREE，Review Director 已验证存在\n- (1) **Schall & de Melo (RANLP 2025)** \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\" — 直接研究 constrained decoding 对 LP distribution 的影响，与 hypothesis (b)(c) 高度相关。本文 free-form ablation 已 empirically 排除 (b)(c) 对 NER 的解释力，引用可强化 \"we know this hypothesis and rule it out\"。[ACL Anthology 已确认]\n- (2) **Yun et al. (Findings EMNLP 2025)** \"The Price of Format: Diversity Collapse in LLMs\" — format templates → diversity collapse，与 instance degeneracy 话题相关但不同（output-level degeneracy vs token-level diversity）。[ACL Anthology 已确认]\n- (3) **Park et al. (NeurIPS 2024)** \"Grammar-Aligned Decoding\" — constrained decoding 同线，与 Willard & Louf (2023) 互补。[NeurIPS proceedings 已确认]\n\n---\n\n### Should-Fix（影响评分但不阻塞接收）\n\n**SF1. [CONSENSUS] \"Moderate-to-strong\" QE 措辞有误导性**\n- R2-W1 提出，R1 AGREE\n- ρ=0.38 (SciERC) 按 Cohen (1988) 属 medium effect。ρ=0.45 来自 CoNLL ceiling-effect control，且该数据集的 ρ 因 zero/non-zero boundary inflate +0.03-0.05 (Section 3.3 footnote)。建议 Abstract 改用 \"moderate\" 或明确标注 ρ=0.45 来源。\n\n**SF2. [CONSENSUS] 论文定位应明确为 diagnostic study**\n- R2-W2 提出，R1 AGREE\n- 论文同时尝试 practical guidance (Section 5 \"Practical recommendations\") 和 mechanism diagnosis，但 actionable takeaway 薄弱（\"use VC for QE, trained verifiers for selection\"）。明确定位为 diagnostic/analytical study 会使期望对齐。\n\n**SF3. [CONSENSUS] Scale ablation (4B vs 8B) 证据力不足 + 缺少 4B degeneracy 数据**\n- R1-W1 提出，R2-W4 同意\n- 仅 2 个规模点（同一模型家族 Qwen3），scale 范围极窄（同属 small-model regime）。4B 的 constant F1 fraction、oracle headroom 未报告，无法判断 gap 是 task difficulty 还是 degeneracy pattern 驱动。Abstract \"at two model scales (4B and 8B)\" 未限定为 narrow range。\n\n**SF4. [CONSENSUS] ε=0.05 threshold non-tied subset 结果定位过强**\n- R1-W5 提出，R2 AGREE\n- ε sweep 0.01-0.20 gain 单调递增，0.05 非 natural split point。Discussion 将 non-tied subset +2.9pp (p=0.004) 用作 \"confirming compression as the bottleneck\" 的主要证据，超出 exploratory framing 允许的 claim 强度。Limitations 承认 \"post-hoc exploratory choice\" 但 Discussion 未体现。Bonferroni over 5 signals ≠ correction over 7ε × 5 signals。\n\n**SF5. [CONSENSUS] Greedy (T=0) 修辞需调整**\n- R1-W4 提出，R2 部分 REBUT（practitioner 视角有价值但修辞需改）\n- \"Surpassing all N=8 selection strategies\" 暗示 greedy 是 selection 的公平 competitor。实际上 greedy 和 sampling+selection 解决不同问题。建议定位为 \"practical cost-free alternative\"。需区分：(a) 只要单输出 → greedy wins, (b) 需要 diverse outputs + QE → sampling 仍有价值。\n\n**SF6. [CONSENSUS] Fisher combined p (2-seed) 呈现权重过高**\n- R1-W2 提出，R2 REBUT（核心论证依赖 d=0.038 + bootstrap CI + TOST，非 Fisher）\n- 实质共识：Fisher p 呈现权重应降低，bootstrap CI 和 effect size 作为主要推断依据。\n\n**SF7. [CONSENSUS] Kendall's W (n=3) 应定位为 sanity check**\n- R1-W3 提出，R2 AGREE\n- n=3 下 W=1.0 在 α=0.05 不显著。3-seed 功能是排除 catastrophic seed sensitivity，非统计推断依据。不应在 abstract 中作为 robustness evidence 首行引用。\n\n---\n\n### Minor（不影响接收）\n\n**M1.** [R1-M1, R2 同意] SJ 命名：分母用 max(|g_i|,|g_j|) 而非 union。Footnote 已说明且 Appendix Table 5 证明 Δρ<0.01，但名称可能误导。建议首次使用时加注。\n\n**M2.** [R1-M2] 主表 seed=42 单 seed vs multi-seed mean 选择不一致（Table 1 VC=0.379 vs Table 7 mean=0.386±0.019）。Caption 应更明确说明。\n\n**M3.** [R1-M3] Correlation-selection gap 操作性定义出现在 Section 4.3，但 Abstract/Introduction 已大量使用。建议 Introduction 首次使用时给出 one-sentence 定义。\n\n**M4.** [R1-M4] Table 2 → Discussion non-tied subset 之间缺少 forward pointer。\n\n**M5.** [R1-Q5] Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清。两者期望值应相同（E[F1] under T=1.0），除非定义不同。需澄清。\n\n**M6.** [R2-W5, R1 PARTIALLY AGREE] LP compression hypotheses (b) 与 (d) 区分不够显式。(b)=constrained decoding 强制 schema tokens vs (d)=model 自主赋予高 LP。建议一句话明确 \"constraint-imposed vs model-learned\" 区别。\n\n**M7.** [R2] \"Cost-free greedy decoding\" 措辞不精确（greedy 仍需 forward pass）。\n\n---\n\n## Reviewer Consensus\n\n**强共识（两位独立提出或一方提出另一方 AGREE，无 REBUT）：**\n- [AGREE] MF1: Framing tautology（R3-W2 延续至 R14，最核心问题）\n- [AGREE] MF2: 单数据集 selection 验证\n- [AGREE] MF3: Yao et al. 差异化\n- [AGREE] MF5: 缺失文献（已验证）\n- [AGREE] SF1-SF7: 全部 should-fix 项\n- [AGREE] M1-M7: 全部 minor 项\n\n## Reviewer Divergence\n\n**MF4: Gap 与 MBR 社区已知结论的关系**\n- R2 立场：gap 在很大程度上是 MBR 社区已知现象（\"good metric correlation ≠ good selection\"）在 IE 场景下的重新标签化。Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。论文贡献应定位为 mechanism diagnosis 而非全新发现。\n- R1 立场：Instance degeneracy 是 qualitatively 不同于 utility mismatch 的新机制。MBR 文献中的失败是 utility function 不 align with human quality；本文中 SJ utility DOES capture quality (within-instance ρ=0.524)，但 degeneracy 消除了 headroom。这不是重标签化。\n- 评估：两方论点均有道理。R1 的反驳更精确（MBR utility degradation ≠ headroom elimination），但 R2 关于 framing 调整的建议（\"diagnosing\" 而非 \"identifying\"）被 R1 接受。**行动方向明确：reframe contribution 定位。**\n\n---\n\n## Questions for Authors（需回答以支撑接收）\n\n**Q1.** [R1-Q1, R2-Q1] Instance degeneracy 是 fine-tuning artifact 还是 task 固有属性？如果 hard-prompted models（如 Yao et al. 设置）也有 high degeneracy，则结论不同。这直接影响 remedy 方向（diversity-promoting training vs. trained verifiers）。\n\n**Q2.** [R1-Q2] Selection 实验为何用 2-seed 而非 3-seed（QE 用了 3-seed）？\n\n**Q3.** [R1-Q3] MBR within-instance ρ=0.524 对 degenerate instances（F1 方差=0）如何处理？excluded or assigned 0？\n\n**Q4.** [R1-Q4, R2-Q4] RE free-form reversal (+1.8pp) 是否限定 \"compression is intrinsic\" 为 NER-specific？\n\n**Q5.** [R1-Q5] Random (0.610) vs Single (0.645) 3.5pp 差距来源？\n\n**Q6.** [R2-Q2] LP × VC 等简单 signal combination 是否测试过？如果仅需几行代码且未做，需解释 scope limitation 的合理性。\n\n**Q7.** [R2-Q3] Entity-token LP CoNLL 上 variance ≈ 0 — 是否暗示 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？\n\n---\n\n## Missing References\n\n**已验证存在（Must-Add）：**\n1. Schall & de Melo (RANLP 2025) \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\" — constrained decoding ↔ LP distribution [ACL Anthology: 2025.ranlp-1.124]\n2. Yun et al. (Findings EMNLP 2025) \"The Price of Format: Diversity Collapse in LLMs\" — format → diversity collapse [ACL Anthology: 2025.findings-emnlp.836]\n3. Park et al. (NeurIPS 2024) \"Grammar-Aligned Decoding\" — constrained decoding [NeurIPS 2024 proceedings]\n\n**R1 建议（非 critical，论文已有 6 篇 MBR 引用）：**\n4. Pasad et al. — MBR for seq2seq（MBR-for-MT 线，非必须）\n5. Bertsch et al. \"It's MBR All the Way Down\"（MBR-for-MT 线，非必须）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**评分：Borderline (2.75/5)**\n- R1: 3.0/5 (Borderline), Confidence 4/5\n- R2: 2.5/5 (Between Findings and substantial revisions), Confidence 4/5\n\n**评分理由：**\n\n论文实验设计扎实、统计实践优秀、消融链完整——这些方法论品质本身值得认可。Instance degeneracy 的量化分析和 LP compression 诊断链是有价值的实证贡献。\n\n但存在两个核心障碍：\n\n1. **Framing 问题（MF1, 持续 12 轮）**：论文最核心的概念贡献——correlation-selection gap——部分是 definitional tautology（4/5 信号 by construction 不能选择），部分是 empirical finding（MBR 转换失败 + LP compression）。这一区分在 Discussion 中存在但未传递至 Abstract/Introduction。当前 framing 夸大了 surprise factor，使得 informed reviewer 在第一印象上就会质疑 novelty。\n\n2. **Novelty 定位（MF4）**：\"Good QE ≠ good selection\" 在 MBR 社区有先例；本文的增量贡献在于 IE-specific failure mechanisms。如果 reframe 为 \"diagnosing two specific failure mechanisms\" 而非 \"identifying a new gap\"，贡献会更准确也更有说服力。\n\n**建议：**\n- 如果能在 rebuttal 中 (a) reframe contribution 区分 trivial/non-trivial, (b) 补充 4B degeneracy 数据, (c) 添加缺失文献, 论文适合 **EMNLP 2026 Findings**。\n- 对于 Main Conference，单数据集 selection 验证（MF2）和 novelty 定位（MF4）是较大障碍，需额外数据或更强的理论贡献。\n\n**置信度：4/5** — 两位 Reviewer 在 uncertainty estimation、MBR decoding、IE evaluation、统计方法方面均有充分背景。\n\n---\n\n## Issue Tracker 更新摘要\n\n**本轮新增 issues：** 7（R14-N1/N2/W1/W2/W3/M1/M2/M3）\n**本轮确认解决：** 4（R11-W7 greedy baseline, R12-M1 four mechanisms, R12-M3 oh2026 year, R13-W1 RE appendix, R13-M1 bib entries）\n**持续 open/in_progress：** R0-C3, R3-W2, R7-C2, R11-W1, R11-W2, R11-W3, R11-W6, R12-N1, R12-W1, R12-W2 等\n**最长未解决 issue：** R3-W2 (tautology framing, Round 3 → Round 14, 持续 12 轮)",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 14\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+相关工作+写作格式）\n**审稿轮次**: Round 1 独立初审 → 交叉分享 (完整原文转发 + 逐条 AGREE/REBUT) → 收敛判断：**1 轮收敛**\n\n---\n\n## Summary\n\n本文评估 LLM-based NER 中 5 种置信信号（SJ, VC, FK, EM, LP）在质量估计和 best-of-N 选择上的表现。核心发现 \"correlation-selection gap\"：信号能预测哪些 instance 做得好（ρ=0.38 on SciERC），但无法选出比 greedy decoding 更好的样本。论文诊断两种失败机制——instance degeneracy（21-58% instances 产生相同 F1）和 LP compression（median within-instance range 0.041 nats），并通过 free-form decoding、entity-token LP isolation、verbalized confidence 三步消融链验证 compression 是 model/task 内在属性。实验覆盖三数据集难度梯度、两个模型族（Qwen3, LLaMA-3.1）、两种规模（4B, 8B）。\n\n---\n\n## Strengths\n\n**S1. 概念贡献有实践价值** [R1-S1, R2 同意]\nQE/selection 解耦是本文核心洞察。实践者可能误以为高 ρ 信号能做 best-of-N 选择——本文明确指出这一 fallacy。在 IE 领域尚未被清晰阐述。\n\n**S2. 诊断消融链逻辑严密** [R1-S2, R2 同意]\nFree-form decoding (std ratio 0.97, 4 seeds) → entity-token LP (4× variance 但 -2.0pp selection) → verbalized confidence (更压缩) → 每步排除一个 hypothesis 并有量化证据。RE free-form 反向效果恰当标注为 regime-dependent。\n\n**S3. 统计实践远超 NLP 论文平均水平** [R1-S3, R2-Soundness 4/5]\nBootstrap CI (B=10,000)、TOST equivalence testing（含 3 组外部锚定 δ）、Fisher combined p、ε sensitivity sweep、multi-seed Kendall's W、FK independence permutation test。方法论上非常负责。\n\n**S4. 三数据集难度梯度设计精巧** [R1-S4, R2 同意]\nSciERC (medium, 65% F1) + CoNLL (ceiling-effect, 91%) + WNUT-17 (collapse, 52% zero-F1)，各自角色明确标注。避免了将 boundary conditions 过度 claim 为 validation。\n\n**S5. Instance degeneracy 量化分析有信息量** [R1-S5, R2 同意]\nTable 5 的 degeneracy 统计（constant F1/constant utility/oracle gap closed/within-instance ρ）是本文最有价值的实证贡献之一。MBR 社区讨论 utility degradation，但 \"utility IS good (ρ=0.524) yet headroom IS eliminated\" 是更精确的诊断。\n\n**S6. 透明度高** [R1-S5, R2-Reproducibility 4/5]\n主动提出 confounds（thinking token 三重论证、SJ normalizer robustness、LOO-SJ equivalence、ε sensitivity、external TOST anchors），代码承诺释放。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [CONSENSUS] Contribution #1 framing 混淆 definitional tautology 与 empirical failure**\n- R1-N1 提出，R2-W3 独立提出，交叉分享强共识\n- 4/5 信号是 instance-level aggregates → 给所有候选分配相同 QE 分数 → 不能直接选择。这是 by construction 的属性，非 empirical finding。论文用 MBR/consensus-proximity 转化为 per-sample ranking 后仍失败才是 empirical finding（within-instance ρ=0.524 但 21% instances 无 headroom）。LP 的 compression 也是独立的 empirical failure。\n- 当前 Abstract/Introduction 将 \"5 signals all fail at selection\" 作为统一 narrative，夸大了 surprise factor。Section 5 (Discussion) 有两层区分但未向前传递至 Abstract/Introduction。\n- **此问题已持续 12 轮（R3-W2 → R14），是最核心 framing 障碍。**\n- 行动：Abstract/Intro 明确拆分三层——(a) instance-level 信号需 MBR 转换 (acknowledged design property, not surprising), (b) MBR 转换后仍失败 despite positive within-instance ρ (empirical), (c) LP per-sample 但 compressed (empirical)。\n\n**MF2. [CONSENSUS] Selection gap 有效验证仅限 SciERC 单数据集**\n- R1-N2 提出，R2 AGREE\n- CoNLL oracle headroom 仅 4pp（论文正确标注为 ceiling-effect control），WNUT-17 信号 collapse（capability boundary）。真正验证 selection gap 的 non-trivial setting 仅 SciERC。Table 6 中 LLaMA/SciERC 在同一数据集上用不同模型 replicate 了 gap，增加了模型维度信心，但仍限于单一 difficulty regime。\n- Section 4.3 \"The pattern holds across CoNLL and WNUT-17\" 中 CoNLL 的 \"holding\" 原因是无 headroom（ceiling effect），非信号失败——qualitatively 不同的原因。\n- 行动：增加 medium-difficulty 数据集（如 Few-NERD subset）或进一步软化 generalization claim。Section 4.3 需区分 ceiling-effect holding 与 signal-failure holding。\n\n**MF3. [CONSENSUS] 与 Yao et al. (2026) 增量贡献界定不清**\n- R2-N1 提出，R1 AGREE\n- Section 1 line 8 用一句话概括差异（\"leaving open\" 三个问题），但未说明 Yao et al. 使用 hard-prompting 而非 fine-tuned models 这一关键方法论差异。如果 instance degeneracy 是 fine-tuning 产物（高 confidence convergence），则本文最核心的 failure mechanism 不存在于 Yao et al. 的设置中——这恰好构成最强差异化论点，但论文未利用。\n- 行动：Related Work 增加对比段落，将 fine-tuning → low diversity → degeneracy 作为与 Yao et al. 的关键区分。\n\n**MF4. [PARTIAL DIVERGENCE → CONSENSUS ON ACTION] Gap 与 MBR 社区已知结论的定位**\n- R2-N2 提出（gap 是 MBR 已知现象的重标签化），R1 REBUT（instance degeneracy ≠ utility mismatch：MBR 文献讨论 utility function 不 align with quality，本文中 SJ utility DOES correlate with F1 within instances (ρ=0.524)，失败来自 headroom elimination）\n- 分歧点：R2 认为 novelty 有限（2.5/5），R1 认为 degeneracy 是 qualitatively 新机制（3.0/5）\n- **实质共识**：Contribution #1 应从 \"identifying the gap\" 调整为 \"diagnosing two specific failure mechanisms (instance degeneracy + LP compression) that explain why QE does not translate to selection in fine-tuned IE models\"。需在 Related Work 中明确讨论与 Eikema et al. (2025) MBR utility degradation 的区别。\n\n**MF5. [CONSENSUS] 缺少两篇直接相关文献**\n- R2-N3 提出，R1 CONDITIONAL AGREE，Review Director 已验证存在\n- (1) **Schall & de Melo (RANLP 2025)** \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\" — 直接研究 constrained decoding 对 LP distribution 的影响，与 hypothesis (b)(c) 高度相关。本文 free-form ablation 已 empirically 排除 (b)(c) 对 NER 的解释力，引用可强化 \"we know this hypothesis and rule it out\"。[ACL Anthology 已确认]\n- (2) **Yun et al. (Findings EMNLP 2025)** \"The Price of Format: Diversity Collapse in LLMs\" — format templates → diversity collapse，与 instance degeneracy 话题相关但不同（output-level degeneracy vs token-level diversity）。[ACL Anthology 已确认]\n- (3) **Park et al. (NeurIPS 2024)** \"Grammar-Aligned Decoding\" — constrained decoding 同线，与 Willard & Louf (2023) 互补。[NeurIPS proceedings 已确认]\n\n---\n\n### Should-Fix（影响评分但不阻塞接收）\n\n**SF1. [CONSENSUS] \"Moderate-to-strong\" QE 措辞有误导性**\n- R2-W1 提出，R1 AGREE\n- ρ=0.38 (SciERC) 按 Cohen (1988) 属 medium effect。ρ=0.45 来自 CoNLL ceiling-effect control，且该数据集的 ρ 因 zero/non-zero boundary inflate +0.03-0.05 (Section 3.3 footnote)。建议 Abstract 改用 \"moderate\" 或明确标注 ρ=0.45 来源。\n\n**SF2. [CONSENSUS] 论文定位应明确为 diagnostic study**\n- R2-W2 提出，R1 AGREE\n- 论文同时尝试 practical guidance (Section 5 \"Practical recommendations\") 和 mechanism diagnosis，但 actionable takeaway 薄弱（\"use VC for QE, trained verifiers for selection\"）。明确定位为 diagnostic/analytical study 会使期望对齐。\n\n**SF3. [CONSENSUS] Scale ablation (4B vs 8B) 证据力不足 + 缺少 4B degeneracy 数据**\n- R1-W1 提出，R2-W4 同意\n- 仅 2 个规模点（同一模型家族 Qwen3），scale 范围极窄（同属 small-model regime）。4B 的 constant F1 fraction、oracle headroom 未报告，无法判断 gap 是 task difficulty 还是 degeneracy pattern 驱动。Abstract \"at two model scales (4B and 8B)\" 未限定为 narrow range。\n\n**SF4. [CONSENSUS] ε=0.05 threshold non-tied subset 结果定位过强**\n- R1-W5 提出，R2 AGREE\n- ε sweep 0.01-0.20 gain 单调递增，0.05 非 natural split point。Discussion 将 non-tied subset +2.9pp (p=0.004) 用作 \"confirming compression as the bottleneck\" 的主要证据，超出 exploratory framing 允许的 claim 强度。Limitations 承认 \"post-hoc exploratory choice\" 但 Discussion 未体现。Bonferroni over 5 signals ≠ correction over 7ε × 5 signals。\n\n**SF5. [CONSENSUS] Greedy (T=0) 修辞需调整**\n- R1-W4 提出，R2 部分 REBUT（practitioner 视角有价值但修辞需改）\n- \"Surpassing all N=8 selection strategies\" 暗示 greedy 是 selection 的公平 competitor。实际上 greedy 和 sampling+selection 解决不同问题。建议定位为 \"practical cost-free alternative\"。需区分：(a) 只要单输出 → greedy wins, (b) 需要 diverse outputs + QE → sampling 仍有价值。\n\n**SF6. [CONSENSUS] Fisher combined p (2-seed) 呈现权重过高**\n- R1-W2 提出，R2 REBUT（核心论证依赖 d=0.038 + bootstrap CI + TOST，非 Fisher）\n- 实质共识：Fisher p 呈现权重应降低，bootstrap CI 和 effect size 作为主要推断依据。\n\n**SF7. [CONSENSUS] Kendall's W (n=3) 应定位为 sanity check**\n- R1-W3 提出，R2 AGREE\n- n=3 下 W=1.0 在 α=0.05 不显著。3-seed 功能是排除 catastrophic seed sensitivity，非统计推断依据。不应在 abstract 中作为 robustness evidence 首行引用。\n\n---\n\n### Minor（不影响接收）\n\n**M1.** [R1-M1, R2 同意] SJ 命名：分母用 max(|g_i|,|g_j|) 而非 union。Footnote 已说明且 Appendix Table 5 证明 Δρ<0.01，但名称可能误导。建议首次使用时加注。\n\n**M2.** [R1-M2] 主表 seed=42 单 seed vs multi-seed mean 选择不一致（Table 1 VC=0.379 vs Table 7 mean=0.386±0.019）。Caption 应更明确说明。\n\n**M3.** [R1-M3] Correlation-selection gap 操作性定义出现在 Section 4.3，但 Abstract/Introduction 已大量使用。建议 Introduction 首次使用时给出 one-sentence 定义。\n\n**M4.** [R1-M4] Table 2 → Discussion non-tied subset 之间缺少 forward pointer。\n\n**M5.** [R1-Q5] Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清。两者期望值应相同（E[F1] under T=1.0），除非定义不同。需澄清。\n\n**M6.** [R2-W5, R1 PARTIALLY AGREE] LP compression hypotheses (b) 与 (d) 区分不够显式。(b)=constrained decoding 强制 schema tokens vs (d)=model 自主赋予高 LP。建议一句话明确 \"constraint-imposed vs model-learned\" 区别。\n\n**M7.** [R2] \"Cost-free greedy decoding\" 措辞不精确（greedy 仍需 forward pass）。\n\n---\n\n## Reviewer Consensus\n\n**强共识（两位独立提出或一方提出另一方 AGREE，无 REBUT）：**\n- [AGREE] MF1: Framing tautology（R3-W2 延续至 R14，最核心问题）\n- [AGREE] MF2: 单数据集 selection 验证\n- [AGREE] MF3: Yao et al. 差异化\n- [AGREE] MF5: 缺失文献（已验证）\n- [AGREE] SF1-SF7: 全部 should-fix 项\n- [AGREE] M1-M7: 全部 minor 项\n\n## Reviewer Divergence\n\n**MF4: Gap 与 MBR 社区已知结论的关系**\n- R2 立场：gap 在很大程度上是 MBR 社区已知现象（\"good metric correlation ≠ good selection\"）在 IE 场景下的重新标签化。Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。论文贡献应定位为 mechanism diagnosis 而非全新发现。\n- R1 立场：Instance degeneracy 是 qualitatively 不同于 utility mismatch 的新机制。MBR 文献中的失败是 utility function 不 align with human quality；本文中 SJ utility DOES capture quality (within-instance ρ=0.524)，但 degeneracy 消除了 headroom。这不是重标签化。\n- 评估：两方论点均有道理。R1 的反驳更精确（MBR utility degradation ≠ headroom elimination），但 R2 关于 framing 调整的建议（\"diagnosing\" 而非 \"identifying\"）被 R1 接受。**行动方向明确：reframe contribution 定位。**\n\n---\n\n## Questions for Authors（需回答以支撑接收）\n\n**Q1.** [R1-Q1, R2-Q1] Instance degeneracy 是 fine-tuning artifact 还是 task 固有属性？如果 hard-prompted models（如 Yao et al. 设置）也有 high degeneracy，则结论不同。这直接影响 remedy 方向（diversity-promoting training vs. trained verifiers）。\n\n**Q2.** [R1-Q2] Selection 实验为何用 2-seed 而非 3-seed（QE 用了 3-seed）？\n\n**Q3.** [R1-Q3] MBR within-instance ρ=0.524 对 degenerate instances（F1 方差=0）如何处理？excluded or assigned 0？\n\n**Q4.** [R1-Q4, R2-Q4] RE free-form reversal (+1.8pp) 是否限定 \"compression is intrinsic\" 为 NER-specific？\n\n**Q5.** [R1-Q5] Random (0.610) vs Single (0.645) 3.5pp 差距来源？\n\n**Q6.** [R2-Q2] LP × VC 等简单 signal combination 是否测试过？如果仅需几行代码且未做，需解释 scope limitation 的合理性。\n\n**Q7.** [R2-Q3] Entity-token LP CoNLL 上 variance ≈ 0 — 是否暗示 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？\n\n---\n\n## Missing References\n\n**已验证存在（Must-Add）：**\n1. Schall & de Melo (RANLP 2025) \"The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance\" — constrained decoding ↔ LP distribution [ACL Anthology: 2025.ranlp-1.124]\n2. Yun et al. (Findings EMNLP 2025) \"The Price of Format: Diversity Collapse in LLMs\" — format → diversity collapse [ACL Anthology: 2025.findings-emnlp.836]\n3. Park et al. (NeurIPS 2024) \"Grammar-Aligned Decoding\" — constrained decoding [NeurIPS 2024 proceedings]\n\n**R1 建议（非 critical，论文已有 6 篇 MBR 引用）：**\n4. Pasad et al. — MBR for seq2seq（MBR-for-MT 线，非必须）\n5. Bertsch et al. \"It's MBR All the Way Down\"（MBR-for-MT 线，非必须）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。\n\n---\n\n## Overall Assessment\n\n**评分：Borderline (2.75/5)**\n- R1: 3.0/5 (Borderline), Confidence 4/5\n- R2: 2.5/5 (Between Findings and substantial revisions), Confidence 4/5\n\n**评分理由：**\n\n论文实验设计扎实、统计实践优秀、消融链完整——这些方法论品质本身值得认可。Instance degeneracy 的量化分析和 LP compression 诊断链是有价值的实证贡献。\n\n但存在两个核心障碍：\n\n1. **Framing 问题（MF1, 持续 12 轮）**：论文最核心的概念贡献——correlation-selection gap——部分是 definitional tautology（4/5 信号 by construction 不能选择），部分是 empirical finding（MBR 转换失败 + LP compression）。这一区分在 Discussion 中存在但未传递至 Abstract/Introduction。当前 framing 夸大了 surprise factor，使得 informed reviewer 在第一印象上就会质疑 novelty。\n\n2. **Novelty 定位（MF4）**：\"Good QE ≠ good selection\" 在 MBR 社区有先例；本文的增量贡献在于 IE-specific failure mechanisms。如果 reframe 为 \"diagnosing two specific failure mechanisms\" 而非 \"identifying a new gap\"，贡献会更准确也更有说服力。\n\n**建议：**\n- 如果能在 rebuttal 中 (a) reframe contribution 区分 trivial/non-trivial, (b) 补充 4B degeneracy 数据, (c) 添加缺失文献, 论文适合 **EMNLP 2026 Findings**。\n- 对于 Main Conference，单数据集 selection 验证（MF2）和 novelty 定位（MF4）是较大障碍，需额外数据或更强的理论贡献。\n\n**置信度：4/5** — 两位 Reviewer 在 uncertainty estimation、MBR decoding、IE evaluation、统计方法方面均有充分背景。\n\n---\n\n## Issue Tracker 更新摘要\n\n**本轮新增 issues：** 7（R14-N1/N2/W1/W2/W3/M1/M2/M3）\n**本轮确认解决：** 4（R11-W7 greedy baseline, R12-M1 four mechanisms, R12-M3 oh2026 year, R13-W1 RE appendix, R13-M1 bib entries）\n**持续 open/in_progress：** R0-C3, R3-W2, R7-C2, R11-W1, R11-W2, R11-W3, R11-W6, R12-N1, R12-W1, R12-W2 等\n**最长未解决 issue：** R3-W2 (tautology framing, Round 3 → Round 14, 持续 12 轮)",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 1402 · 2026-05-16T08:02:17.111659+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4216
}
```

</details>

---


### Assistant

_source line 1403 · 2026-05-16T08:02:25.995267+00:00_

**Round 14 审稿完成。**

报告已投递至 Research Director。核心结论：

**Overall: Borderline (2.75/5)** — R1 给 3.0，R2 给 2.5。

**5 个 Must-Fix（强共识）：**
1. Contribution framing 混淆 tautology 与 empirical failure（持续 12 轮的核心问题）
2. Selection gap 有效验证仅限 SciERC 单数据集
3. 与 Yao et al. (2026) 增量贡献界定不清
4. Gap 贡献定位需从 "discovery" 转为 "mechanism diagnosis"（R1/R2 有分歧但行动方向一致）
5. 缺少 3 篇已验证存在的直接相关文献

**7 个 Should-Fix**（QE 措辞、论文定位、scale 限定、ε threshold、greedy 修辞、Fisher p 降级、Kendall W 定位）

**建议**：reframe 后适合 EMNLP 2026 Findings；Main Conference 需额外数据集或更强理论贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1404 · 2026-05-16T08:02:28.626841+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

总结：
- **Must-Fix N1/N2**: 两条均同意。N1 与我的 W3 完全一致（by-construction tautology），N2 关于单数据集验证我补充了 SciERC 上有 4 个 model-config 复现的 partial defense。
- **Should-Fix**: 同意 W1/W3/W5，部分反驳 W2（Fisher p 虽 underpowered 但非核心论证）和 W4（greedy 比较有 practical value 但修辞需调整）。
- **Missing References**: 反驳 R1 的 4 篇（MT-focused MBR 或未找到），认为我提出的 Schall & de Melo 和 Yun et al. 是更关键的遗漏。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1405 · 2026-05-16T08:02:41.693697+00:00_

审稿报告已投递至 Research Director。

**Round 14 审稿完成总结：**

- **评分**：Borderline (2.75/5)，R1 给 3.0，R2 给 2.5
- **5 个 Must-Fix**：(1) Framing 混淆 tautology/empirical failure（持续 12 轮未解决）；(2) Selection gap 仅 SciERC 单数据集验证；(3) 与 Yao et al. 增量贡献不清；(4) 需从 "discovering gap" 重定位为 "diagnosing IE-specific mechanisms"；(5) 缺 3 篇已验证文献
- **7 个 Should-Fix**：QE 措辞、diagnostic 定位、scale 限定、ε threshold、greedy 修辞、Fisher p 降级、Kendall's W 定位
- **建议**：reframe + 补数据后适合 Findings；Main Conference 需额外数据集或更强理论贡献
- **Issue Tracker**：已更新，新增 7 条，确认解决 4 条，最长未解决 issue R3-W2 持续 12 轮

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 115

## Round 115

62 recorded events


### User

_source line 1406 · 2026-05-16T08:31:45.238852+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026 Main Conference
- 投稿类别: ARR May 2026 cycle
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1407 · 2026-05-16T08:31:51.613775+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1408 · 2026-05-16T08:31:51.665542+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1409 · 2026-05-16T08:31:57.740457+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1410 · 2026-05-16T08:31:57.841366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1411 · 2026-05-16T08:32:01.706654+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1412 · 2026-05-16T08:32:02.977214+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (111 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_vc_lp_cascade_selection** (killed): VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\n- **exp_tacred_re_benchmark** (killed): TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\n- **exp_entity_token_lp** (negative): Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\n  [exp_entity_token_lp_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/data/results.json) | [exp_entity_token_lp_report](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_entity_token_lp/report/report.md)\n\n## 趋势\n成功 61 / 负向 24 / 失败 4 / 共 111\n\n## 下一步\
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1270
}
```

</details>

---


### Tool call

_source line 1413 · 2026-05-16T08:32:02.977594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1414 · 2026-05-16T08:32:03.329177+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ The Correlation-Selection Gap in LLM-Based Named Entity Recognition}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1415 · 2026-05-16T08:32:03.329550+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1416 · 2026-05-16T08:32:03.379959+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1417 · 2026-05-16T08:32:09.052776+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1418 · 2026-05-16T08:32:09.504873+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---on a medium-difficulty benchmark (SciERC) with ceiling-effect (CoNLL) and signal-collapse (WNUT-17) controls, within a narrow model-scale range (4B--8B).
4	All signals achieve moderate quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control), yet best-of-$N$ selection fails to outperform greedy decoding ($T{=}0$)---the \textit{correlation-selection gap}.
5	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 21--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation (median $\rho{=}0.52$); and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats, with entity-token isolation revealing intrinsic overconfidence rather than format-token dilution.
6	A five-layer ablation chain (free-form decoding, entity-token LP, verbalized confidence, non-tied subset, signal combinations) confirms these mechanisms are intrinsic to capable fine-tuned models, not artifacts of constrained decoding.
7	Signal rankings shift with task difficulty and collapse at the capability boundary; closing the gap likely requires learned per-sample scoring.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1419 · 2026-05-16T08:32:09.505258+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1420 · 2026-05-16T08:32:09.957168+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing two failure mechanisms---instance degeneracy and LP compression---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	We define the \textbf{correlation-selection gap} as the disparity between a signal's rank correlation with F1 ($\rho$) and its ability to select the best output from $N$ candidates (Figure~\ref{fig:overview}): on SciERC, signals achieve moderate quality estimation ($\rho{=}0.38$, up to 0.45 on a ceiling-effect control) yet selection fails to improve over greedy decoding
…[truncated 3024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1421 · 2026-05-16T08:32:10.007811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1422 · 2026-05-16T08:32:10.459883+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all target discrete answers.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy scales with model capability: CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero (\S\ref{sec:discussion}).
13	This creates an inherent tension between model quality and selection utility that we expect to intensify as models improve.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization but does not address structured extraction.
15	\citet{culotta2004confidence} and \citet{mejer2010confidence} pioneer confidence es
…[truncated 2303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1423 · 2026-05-16T08:32:10.460308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1424 · 2026-05-16T08:32:10.912321+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 3040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1425 · 2026-05-16T08:32:10.912833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1426 · 2026-05-16T08:32:11.816628+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
15	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed count for primary results reflects computational budget.}
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
…[truncated 7949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1427 · 2026-05-16T08:32:11.816997+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1428 · 2026-05-16T08:32:12.319339+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	VC leads on medium-difficulty NER ($\rho{=}0.379$, SciERC); EM leads easy NER and binary discrimination (AUROC${=}0.816$, CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse. RE signal rankings are reported in Appendix~\ref{app:re_extension}.
6	
7	\paragraph{Why the gap exists.}
8	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
9	
10	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
11	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
12	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
13	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; SciERC (66\%) shows 21\%; WNUT-17 (48\%) shows near-zero---the tension between model quality and selection utility is inherent.
14	Scale ablation confirms this tension: Qwen3-8B shows 21\% instance degeneracy on SciERC vs.\ 10.4\% for the weaker Qwen3-4B, despite comparable within-instance utility correlation ($\rho{=}0.52$ vs.\ $0.55$; Table~\ref{tab:degeneracy}).
15	Despite MBR's success in machine translation \cite{freitag2022high}, all 
…[truncated 7276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1429 · 2026-05-16T08:32:12.319864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1430 · 2026-05-16T08:32:12.822105+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER, revealing the \textit{correlation-selection gap}: moderate quality estimation ($\rho{=}0.38$ on medium-difficulty NER, up to 0.45 on a ceiling-effect control) coexists with selection that fails to outperform greedy decoding ($T{=}0$).
4	The gap stems from two mechanisms: instance degeneracy (21--58\% of instances produce identical F1 across all $N$ samples, scaling with model capability and eliminating selection headroom despite positive within-instance utility correlation) and LP compression (the only per-sample signal has median within-instance range of 0.041 nats).
5	Diagnostic ablations---free-form decoding, entity-token LP isolation---confirm compression is intrinsic rather than an artifact of constrained decoding or format-token dilution.
6	The gap is demonstrated in the medium-difficulty regime where models achieve moderate but imperfect accuracy; signal rankings shift with difficulty and collapse at the capability boundary in the small-model regime (3B--8B).
7	Whether these mechanisms persist at 70B+ scales is an open question; trained verifiers and an exploratory extension to relation extraction (Appendix~\ref{app:re_extension}) are promising directions.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1431 · 2026-05-16T08:32:12.822481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1432 · 2026-05-16T08:32:13.325111+00:00_

1	Our evaluation covers three NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.4$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selectio
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1433 · 2026-05-16T08:32:13.375927+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1434 · 2026-05-16T08:32:14.279760+00:00_

File content (26138 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1435 · 2026-05-16T08:32:14.280279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-16T08:32:14.581846+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-16T08:32:22.367816+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 submission guidelines author instructions"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here are the key submission guidelines and author instructions for ACL Rolling Review (ARR) for May 2026:

## Author Requirements

All submitting authors have to sign up as reviewers (deadline: 48h after the submission deadline). The deadline for completing the registration form is January 7th 2026 EoD AoE (for the January cycle), and
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8087
}
```

</details>

---


### Tool result

_source line 1438 · 2026-05-16T08:32:22.368222+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7786
}
```

</details>

---


### Tool call

_source line 1439 · 2026-05-16T08:32:28.391468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit"
  }
}
```

</details>

---


### Tool call

_source line 1440 · 2026-05-16T08:32:29.195003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 page limit long paper short paper formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 page limit long paper short paper formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1441 · 2026-05-16T08:32:30.701502+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1442 · 2026-05-16T08:32:30.701877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1443 · 2026-05-16T08:32:32.540410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1444 · 2026-05-16T08:32:33.042872+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $
…[truncated 13706 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-16T08:32:33.344538+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"}]

Based on the search results, here is the information about EMNLP 2026 call for papers:

## Submission Deadline
The EMNLP 2026 paper submission deadline is 2026-05-25 23:59:59 (UTC-12).

## Page Limits
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Additional Requirements
The mandatory Limitations section is required, placed after the conclusion.

The official EMNLP 2026 Call for Main Conference Papers can be found a
…[truncated 181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 4953
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-16T08:32:33.344894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-16T08:32:33.395652+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{brown2024monkeys,
4	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
5	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
6	  journal = {arXiv preprint arXiv:2407.21787},
7	  year = {2024},
8	  url = {https://arxiv.org/abs/2407.21787}
9	}
10	
11	@inproceedings{chen2024usc,
12	  title = {Universal Self-Consistency for Large Language Model Generation},
13	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
14	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2311.17311}
17	}
18	
19	@article{cobbe2021verifiers,
20	  title = {Training Verifiers to Solve Math Word Problems},
21	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
22	  journal = {arXiv preprint arXiv:2110.14168},
23	  year = {2021},
24	  url = {https://arxiv.org/abs/2110.14168}
25	}
26	
27	@inproceedings{culotta2004confidence,
28	  title = {Confidence Estimation for Information Extraction},
29	  author = {Culotta, Aron and McCallum, Andrew},
30	  booktitle = {HLT-NAACL 2004},
31	  year = {2004},
32	  url = {https://aclanthology.org/N04-4028/}
33	}
34	
35	@inproceedings{derczynski2017wnut,
36	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
37	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
38	  booktitle = {W-NUT Workshop at EMNLP 2017},
39	  year = {2017},
40	  url = {https://aclanthology.org/W17-4418/}
41	}
42	
43	@inproceedings{eikema2022
…[truncated 3208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1448 · 2026-05-16T08:32:36.509525+00:00_

Web search results for query: "ACL Rolling Review 2026 page limit long paper short paper formatting requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"}]

Based on the search results, here are the ACL Rolling Review 2026 page limit and formatting requirements:

## Page Limits

Long papers may have up to eight (8) pages of content plus unlimited pages for references. The search results do not specify a distinct short paper page limit specifically for ACL Rolling Review 2026, though general ACL conferences typically have different limits for short papers.

## Formatting Requirements

Paper submissions must use the official ACL style templates, which are available as an Overleaf template 
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7314
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-16T08:32:42.987883+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 1450 · 2026-05-16T08:32:42.988286+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-16T08:32:44.394275+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 112\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool result

_source line 1452 · 2026-05-16T08:32:44.394769+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1406
}
```

</details>

---


### Tool call

_source line 1453 · 2026-05-16T08:32:44.846826+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "200",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "200",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1454 · 2026-05-16T08:32:45.149399+00:00_

200	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
201	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
202	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
203	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
204	
205	\paragraph{WNUT-17 full signal analysis.}
206	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
207	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
208	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
209	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
210	
211	\begin{table}[t]
212	\centering
213	\small
214	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
215	\label{tab:wnut}
216	\begin{tabular}{lccccc}
…[truncated 21563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1455 · 2026-05-16T08:32:45.200106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1456 · 2026-05-16T08:32:45.653419+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-9, abbreviated) =====
3	- id: R0-C1
4	  summary: "模型规模单一（仅 8B）"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  resolution: "Round 2 Reviewer 确认措辞修正到位"
11	  resolution_round: 2
12	- id: R0-C2
13	  summary: "相关工作显著遗漏"
14	  category: framing
15	  severity: warning
16	  status: resolved
17	  first_raised_round: 0
18	  last_seen_round: 1
19	  resolution: "Round 2 确认 49 条 bib 全部 cited"
20	  resolution_round: 2
21	- id: R0-C4
22	  summary: "SJ 方法新颖性有限"
23	  category: method
24	  severity: warning
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 1
28	  resolution: "Round 2 确认三点差异化清晰"
29	  resolution_round: 2
30	- id: R0-C5
31	  summary: "全文零图表"
32	  category: writing
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 0
37	  resolution: "论文已包含 6 个 figures"
38	  resolution_round: 1
39	- id: R0-C6
40	  summary: "成本分析 negligible 误导"
41	  category: method
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 0
46	  resolution: "Round 1+ 未再提及"
47	  resolution_round: 1
48	- id: R0-W1
49	  summary: "未探索 signal combination"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 0
55	  resolution: "Round 1+ 未再提及"
56	  resolution_round: 1
57	- id: R0-W4
58	  summary: "统计检验不系统"
59	  category: experiment
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 0
63	  last_seen_round: 1
64	  resolution: "Round 2 Reviewer 评价 bootstrap 达到高标准"
65	  resolution_round: 2
66	- id: R3-W4
67	  summary: "FK independence 假设未验证"
68	  category: experiment
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 3
72	  last_seen_round: 8
73	  resolution: "Appendix instance-level permutation test (n=529-2756, p<0.001) 验证"
74	  resolution_round: 9
75	- id: R3-W5
76	  summary: "Cross-model
…[truncated 34185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-16T08:33:01.847529+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-16T08:33:02.299825+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- run_mvp_pilot.py 支持 --collect_logprobs, --num_test (默认已改为 9999)\\n\\n## 数据修正链 (D054-D060) 关键教训\\n- exp_012 是唯一使用 max_tokens=512 的实验，导致 voting_conf ρ 虚高 (0.502→0.379)\\n- SJ/FK 对 max_tokens 参数鲁棒（Δ<0.004），但 voting_conf 极度敏感\\n- 修正后 AUROC 排名反转：EM (0.749) > SJ (0.692) > Voting (0.684)\\n- Selection claim 由 bootstrap 确认为 null result（p=0.39），不能写 \\\"significantly outperforms\\\"\\n- 论文数据必须来自 _rerun_1024 或本身就用 1024 的实验\\n\\n## D066 LLaMA fresh rerun (2026-05-15)\\n- D066 决策：LLaMA 3-seed 全部使用 fresh rerun 数据（seed42_r1024 + seed123 + seed456_r1024）\\n- exp_018_llama_scierc_seed456（旧 exp_007 复制品）已标记 SUPERSEDED\\n- LLaMA NER SJ ρ 修正：旧 0.362±0.004 → 新 0.325±0.021（σ 增大 5× 是真实 seed 变异，seed123 拉高均值）\\n- **分析脚本与 report.json 的 EM/VC 值存在系统性差异**（如 seed42 VC: 脚本 0.373 vs report.json 0.405）。Reviewer 要求论文统一使用分析脚本输出（与 Qwen 同一套）。不要从 registry metrics（来自 report.json）直接引用 EM/VC 到论文。\\n- NER 信号排名 6/6 完全稳定：VC > SJ > EM > FK > LP\\n- Core claim \\\"structural > logprob\\\" NER 全部成立 (12/12)；RE 仅 VC 稳定胜 LP\\n\\n## ρ 一致性审计 (2026-05-15) — 关键管道 bug\\n- **根因**：旧管道 `compute_metrics.py` 包含 gold-empty 实例 + FK 对全空 sample 返回 0（应为 1.0）\\n- CoNLL 697/3453 (20%) gold-empty 实例导致 FK ρ 膨胀 0.48→0.81，SJ ρ 压低 0.48→0.18，排名反转\\n- **统一标准**：排除 gold-empty 实例。CoNLL n=2756，SciERC n=551（或 n=529 排除空 gold NER）\\n- 论文所有 ρ 值必须来自 gold-filtered 管道（`rho_audit.py
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-16T08:33:03.307760+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 1460 · 2026-05-16T08:33:03.860275+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1461 · 2026-05-16T08:33:04.212144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1462 · 2026-05-16T08:33:04.313435+00:00_

500	At this cutpoint, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\varepsilon$, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
501	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
502	This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\%$ (vs.\ seed${=}42$: $0.041$ nats, $60.3\%$).
503	Seed~456 uses a different subtask flag (joint vs.\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\ 8.20 nats; Mann--Whitney $p{=}0.55$), confirming that the subtask change does not affect compression.
504	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
509	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
510	\label{fig:lp_range_cdf}
511	\end{figure}
512	
513	\begin{table}[t]
514	\centering
515	\small
516	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
517	\label{tab:logprob_ties}
518	\begin{tabular}{lc}
519	\toprule
520	$\varepsilon$ threshold & Tied instances (\%) \\
521	\midrule
522	0.01 & 1.1\% \\
523	0.05 & 60.3\% \\
524	0.1  & ${\sim}$84\% \\
525	0.5  & ${\sim}$99\% \\
526	\bottomrule
527	\end{tabular}
528	\end{table}
529	
530	\paragraph{Non-tied subset.}
531	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significa
…[truncated 17579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1463 · 2026-05-16T08:34:31.781594+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n- **文件**: `projects/struct_self_consist_ie/docs/paper/main.tex`（及 `sections/` 下各子文件）\n- **目标 Venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n\n### Venue 要求\n- Long paper: 8 页正文 + unlimited references + Appendix 不计入页数\n- 模板: ACL style（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须（≤1 页，不计入页数）\n- Ethics statement 推荐\n\n### 论文概要\n论文研究 LLM-based NER 中自一致性信号的质量估计与样本选择能力。在 SciERC（主要）、CoNLL-2003（ceiling-effect control）、WNUT-17（signal-collapse boundary）上评估 5 个置信度信号（4 个 instance-level + 1 个 per-sample LP），使用 Qwen3-8B、LLaMA-3.1-8B（+ 4B ablation）。核心发现是 \"correlation-selection gap\"：信号有中等 QE 能力（ρ 达 0.38）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。\n\n### 你需要重点审查的方面\n\n1. **实验设计合理性**\n   - 数据集选择（SciERC/CoNLL/WNUT-17 三级难度梯度）是否充分？Selection gap 的有效测试仅在 SciERC (n=529) 上有意义——CoNLL 是 ceiling control，WNUT 是 collapse boundary——单数据集支撑核心 claim 是否足够？\n   - 模型规模范围（4B-8B）是否足以支撑结论？\n   - N=8 primary / N=16 scaling 的选择是否合理？\n\n2. **统计分析严谨性**\n   - 2-seed Fisher combined p 的统计效力是否充足？\n   - 3-seed Kendall W=1.0 的统计意义（n=3 时 p≈0.05 仅 borderline）\n   - ε=0.05 tied/non-tied 切分的 post-hoc 性质是否充分说明？non-tied subset +2.9pp (p=0.004) 在 Bonferroni over 多少个比较下是否 survive？\n   - TOST 等价性检验的 equivalence margins 选择和解释\n   - Bootstrap CI 的使用和解释是否恰当？\n\n3. **方法论**\n   - 5 个信号中 4 个是 instance-level（by construction 无法区分 per-sample），只有 LP 是 per-sample——这个 \"gap\" 在多大程度上是定义上的 tautology vs 经验发现？\n   - Consensus-proximity (MBR) 将 instance-level 转为 per-sample ranking 后仍然失败——这与 MBR 文献中已知的 failure modes 关系如何？\n   - Instance degeneracy 和 LP compression 的诊断是否充分支撑 \"intrinsic\" 结论？\n   - Free-form ablation (std ratio 0.97) 足以排除 constrained decoding 作为原因吗？\n   - Entity-token LP isolation 的实验设计和结论解读\n\n4. **4B scale ablation**\n   - Table 6 报告了 degeneracy 统计（8B 21% vs 4B 10.4%），数据是否完整？\n   - 2-point scale ablation 的解释力\n\n5. **可重复性**\n   - 训练配置、推理设置、评估协议是否描述充分？\n   - Thinking token confound 的 3-part analysis 是否令人信服？\n\n请按 EMNLP 最严格标准审稿，输出完整审稿报告，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n- **文件**: `projects/struct_self_consist_ie/docs/paper/main.tex`（及 `sections/` 下各子文件）\n- **目标 Venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n\n### Venue 要求\n- Long paper: 8 页正文 + unlimited references + Appendix 不计入页数\n- 模板: ACL style（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须（≤1 页，不计入页数）\n- Ethics statement 推荐\n\n### 论文概要\n论文研究 LLM-based NER 中自一致性信号的质量估计与样本选择能力。在 SciERC（主要）、CoNLL-2003（ceiling-effect control）、WNUT-17（signal-collapse boundary）上评估 5 个置信度信号（4 个 instance-level + 1 个 per-sample LP），使用 Qwen3-8B、LLaMA-3.1-8B（+ 4B ablation）。核心发现是 \"correlation-selection gap\"：信号有中等 QE 能力（ρ 达 0.38）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。\n\n### 你需要重点审查的方面\n\n1. **实验设计合理性**\n   - 数据集选择（SciERC/CoNLL/WNUT-17 三级难度梯度）是否充分？Selection gap 的有效测试仅在 SciERC (n=529) 上有意义——CoNLL 是 ceiling control，WNUT 是 collapse boundary——单数据集支撑核心 claim 是否足够？\n   - 模型规模范围（4B-8B）是否足以支撑结论？\n   - N=8 primary / N=16 scaling 的选择是否合理？\n\n2. **统计分析严谨性**\n   - 2-seed Fisher combined p 的统计效力是否充足？\n   - 3-seed Kendall W=1.0 的统计意义（n=3 时 p≈0.05 仅 borderline）\n   - ε=0.05 tied/non-tied 切分的 post-hoc 性质是否充分说明？non-tied subset +2.9pp (p=0.004) 在 Bonferroni over 多少个比较下是否 survive？\n   - TOST 等价性检验的 equivalence margins 选择和解释\n   - Bootstrap CI 的使用和解释是否恰当？\n\n3. **方法论**\n   - 5 个信号中 4 个是 instance-level（by construction 无法区分 per-sample），只有 LP 是 per-sample——这个 \"gap\" 在多大程度上是定义上的 tautology vs 经验发现？\n   - Consensus-proximity (MBR) 将 instance-level 转为 per-sample ranking 后仍然失败——这与 MBR 文献中已知的 failure modes 关系如何？\n   - Instance degeneracy 和 LP compression 的诊断是否充分支撑 \"intrinsic\" 结论？\n   - Free-form ablation (std ratio 0.97) 足以排除 constrained decoding 作为原因吗？\n   - Entity-token LP isolation 的实验设计和结论解读\n\n4. **4B scale ablation**\n   - Table 6 报告了 degeneracy 统计（8B 21% vs 4B 10.4%），数据是否完整？\n   - 2-point scale ablation 的解释力\n\n5. **可重复性**\n   - 训练配置、推理设置、评估协议是否描述充分？\n   - Thinking token confound 的 3-part analysis 是否令人信服？\n\n请按 EMNLP 最严格标准审稿，输出完整审稿报告，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 1464 · 2026-05-16T08:35:02.295397+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 30513
}
```

</details>

---


### Tool call

_source line 1465 · 2026-05-16T08:35:02.396347+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + Related Work + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n- **文件**: `projects/struct_self_consist_ie/docs/paper/main.tex`（及 `sections/` 下各子文件）\n- **目标 Venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n\n### Venue 要求\n- Long paper: 8 页正文 + unlimited references + Appendix 不计入页数\n- 模板: ACL style（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须（≤1 页，不计入页数）\n- Ethics statement 推荐\n\n### 论文概要\n论文评估 5 个置信度信号在 LLM-based NER 中的质量估计与样本选择能力。核心发现是 \"correlation-selection gap\"：信号有中等 QE 能力（ρ 达 0.38）但选择失败，greedy decoding 超过所有选择策略。诊断两个机制：instance degeneracy 和 LP compression。测试床：SciERC（primary）、CoNLL-2003（ceiling control）、WNUT-17（collapse boundary）。模型：Qwen3-8B、LLaMA-3.1-8B、Qwen3-4B。\n\n### 你需要重点审查的方面\n\n1. **新颖性与贡献评估**\n   - \"Correlation-selection gap\" 作为核心概念，与 MBR 社区已知的 selection failure 关系如何？是真正的新发现还是已知现象的重标签化（re-labeling）？\n   - 与 Yao et al. (2026) 的增量贡献是否清晰？他们也研究 consistency-accuracy correlations for LLM-based IE，区别在于 hard-prompting vs fine-tuned models 以及 QE vs selection 的解耦。这些区别是否足以构成独立贡献？\n   - Instance degeneracy 作为 failure mechanism 的新颖性——这是否只是说\"好模型产出更一致\"（trivial observation）还是有更深的洞察？\n   - 贡献列表的 framing：Contribution #1 是否将 by-construction limitation（instance-level 信号）和 empirical failure（MBR + LP compression）混为一体？\n\n2. **Related Work 覆盖度**\n   - 检查以下文献是否被引用和充分讨论：\n     - Schall & de Melo \"The Hidden Cost of Structure\" (RANLP 2025) — constrained decoding 对 LP 的影响\n     - Yun et al. \"The Price of Format: Diversity Collapse\" (EMNLP Findings 2025) — format 导致 diversity collapse\n     - Park et al. \"Grammar-Aligned Decoding\" (NeurIPS 2024) — constrained decoding\n     - Eikema et al. (2025) structured MBR utility degradation\n   - 对 Yao et al. (2026) 的 positioning 是否充分？论文是否清晰说明了 fine-tuned models 中 instance degeneracy 可能是 fine-tuning 产物而非 task 固有特性？\n   - 其他可能遗漏的重要相关工作\n\n3. **写作质量**\n   - Abstract 信息密度：当前 abstract 覆盖了 5 个信号、3 个数据集、degeneracy 百分比、LP 0.041 nats、5 层 ablation chain、signal rankings shift——是否过于密集？\n   - 术语一致性：\"Soft Jaccard\" 的命名（分母是 max 不是 union）是否有误导性？\n   - \"Correlation-selection gap\" 的操作性定义首次出现在 Section 4.3 还是 Introduction？\n   - Greedy (T=0) vs sampling+selection 的修辞：\"surpassing all N=8 selection strategies\" 是否过强？应定位为 practical cost-free alternative 还是 selection baseline？\n   - ρ=0.45 headline 出现在 abstract 但来自 ceiling-effect dataset CoNLL，primary dataset SciERC 仅 ρ=0.379——按 Cohen (1988) 这是 medium effect，\"moderate-to-strong\" 中的 \"strong\" 是否有误导性？\n   - Table 2 中 Random (0.610) vs Single (0.645) 差距 3.5pp 的来源是否解释清楚？两者期望值在 T=1.0 下应相同？\n   - Fisher combined p 的呈现权重是否过高？\n\n4. **格式合规**\n   - 正文是否在 8 页以内（含 figures/tables）？\n   - 参考文献格式是否符合 ACL style？\n   - 匿名性检查：是否有泄露身份的内容（URL、致谢、self-citation 暴露等）？\n   - Limitations section 位置和长度\n   - Ethics statement 位置\n\n5. **引用真实性抽查**\n   - 抽查 5-10 条引用：bib entry 的 author、year、venue 是否准确？\n   - 是否有 orphan bib entries（在 .bib 中但未在正文引用）？\n\n请按 EMNLP 最严格标准审稿，输出完整审稿报告，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + Related Work + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n- **文件**: `projects/struct_self_consist_ie/docs/paper/main.tex`（及 `sections/` 下各子文件）\n- **目标 Venue**: EMNLP 2026 Main Conference（ARR May 2026 cycle）\n- **截止日期**: 2026-05-25\n\n### Venue 要求\n- Long paper: 8 页正文 + unlimited references + Appendix 不计入页数\n- 模板: ACL style（`\\usepackage[review]{acl}`）\n- Double-blind 匿名审稿\n- Limitations section 必须（≤1 页，不计入页数）\n- Ethics statement 推荐\n\n### 论文概要\n论文评估 5 个置信度信号在 LLM-based NER 中的质量估计与样本选择能力。核心发现是 \"correlation-selection gap\"：信号有中等 QE 能力（ρ 达 0.38）但选择失败，greedy decoding 超过所有选择策略。诊断两个机制：instance degeneracy 和 LP compression。测试床：SciERC（primary）、CoNLL-2003（ceiling control）、WNUT-17（collapse boundary）。模型：Qwen3-8B、LLaMA-3.1-8B、Qwen3-4B。\n\n### 你需要重点审查的方面\n\n1. **新颖性与贡献评估**\n   - \"Correlation-selection gap\" 作为核心概念，与 MBR 社区已知的 selection failure 关系如何？是真正的新发现还是已知现象的重标签化（re-labeling）？\n   - 与 Yao et al. (2026) 的增量贡献是否清晰？他们也研究 consistency-accuracy correlations for LLM-based IE，区别在于 hard-prompting vs fine-tuned models 以及 QE vs selection 的解耦。这些区别是否足以构成独立贡献？\n   - Instance degeneracy 作为 failure mechanism 的新颖性——这是否只是说\"好模型产出更一致\"（trivial observation）还是有更深的洞察？\n   - 贡献列表的 framing：Contribution #1 是否将 by-construction limitation（instance-level 信号）和 empirical failure（MBR + LP compression）混为一体？\n\n2. **Related Work 覆盖度**\n   - 检查以下文献是否被引用和充分讨论：\n     - Schall & de Melo \"The Hidden Cost of Structure\" (RANLP 2025) — constrained decoding 对 LP 的影响\n     - Yun et al. \"The Price of Format: Diversity Collapse\" (EMNLP Findings 2025) — format 导致 diversity collapse\n     - Park et al. \"Grammar-Aligned Decoding\" (NeurIPS 2024) — constrained decoding\n     - Eikema et al. (2025) structured MBR utility degradation\n   - 对 Yao et al. (2026) 的 positioning 是否充分？论文是否清晰说明了 fine-tuned models 中 instance degeneracy 可能是 fine-tuning 产物而非 task 固有特性？\n   - 其他可能遗漏的重要相关工作\n\n3. **写作质量**\n   - Abstract 信息密度：当前 abstract 覆盖了 5 个信号、3 个数据集、degeneracy 百分比、LP 0.041 nats、5 层 ablation chain、signal rankings shift——是否过于密集？\n   - 术语一致性：\"Soft Jaccard\" 的命名（分母是 max 不是 union）是否有误导性？\n   - \"Correlation-selection gap\" 的操作性定义首次出现在 Section 4.3 还是 Introduction？\n   - Greedy (T=0) vs sampling+selection 的修辞：\"surpassing all N=8 selection strategies\" 是否过强？应定位为 practical cost-free alternative 还是 selection baseline？\n   - ρ=0.45 headline 出现在 abstract 但来自 ceiling-effect dataset CoNLL，primary dataset SciERC 仅 ρ=0.379——按 Cohen (1988) 这是 medium effect，\"moderate-to-strong\" 中的 \"strong\" 是否有误导性？\n   - Table 2 中 Random (0.610) vs Single (0.645) 差距 3.5pp 的来源是否解释清楚？两者期望值在 T=1.0 下应相同？\n   - Fisher combined p 的呈现权重是否过高？\n\n4. **格式合规**\n   - 正文是否在 8 页以内（含 figures/tables）？\n   - 参考文献格式是否符合 ACL style？\n   - 匿名性检查：是否有泄露身份的内容（URL、致谢、self-citation 暴露等）？\n   - Limitations section 位置和长度\n   - Ethics statement 位置\n\n5. **引用真实性抽查**\n   - 抽查 5-10 条引用：bib entry 的 author、year、venue 是否准确？\n   - 是否有 orphan bib entries（在 .bib 中但未在正文引用）？\n\n请按 EMNLP 最严格标准审稿，输出完整审稿报告，包括 Summary、Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions for Authors、Missing References、Overall Score（strong reject / weak reject / borderline / weak accept / strong accept）+ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 1466 · 2026-05-16T08:35:03.878119+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1481
}
```

</details>

---


### Assistant

_source line 1467 · 2026-05-16T08:35:12.715326+00:00_

Round 1 已启动，两名 Reviewer 任务已分配：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| R1 | 方法严谨性 + 实验设计 + 统计分析 | 已派发 |
| R2 | 新颖性 + Related Work + 写作质量 + 格式合规 | 已派发 |

等待两位 Reviewer 提交独立审稿报告，收到后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1468 · 2026-05-16T08:40:34.318557+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿报告

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
**审查侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## 总体评分

**Overall**: 3.0 / 5 (Findings acceptance)
**一句话总结**: 论文提出了一个有价值的概念区分（quality estimation vs. sample selection），诊断了两个失败机制，但核心 claim 在实质上仅由单数据集（SciERC, n=529）支撑，且统计分析存在若干需要修正的问题。

---

## 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 核心 claim 的实验支撑依赖单一有效数据集；统计检验的多重比较校正不完整；instance-level 信号的 selection failure 部分是定义上的必然而非经验发现 |
| Excitement | 3.5 / 5 | Correlation-selection gap 是有用的概念贡献；instance degeneracy 作为机制解释有洞察力；但结论偏向 negative result（"现有信号都不行"），缺少前进路径的具体验证 |
| Reproducibility | 4.0 / 5 | 训练配置详尽（Table 9），prompt template、constrained decoding 细节完整；代码承诺开源；但 2-seed 主实验的 variance estimation 偏弱 |
| Confidence | 4 / 5 | 熟悉 MBR decoding、self-consistency、NER 评估方法论和统计检验 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 核心 claim 的有效测试仅由单数据集支撑
- 具体位置：Section 4 (Experiments), Table 2, §4.3
- 问题：论文声称发现 "correlation-selection gap"——信号有 QE 能力但 selection 失败。但实际有效测试 selection gap 的仅 SciERC (n=529)：
  - CoNLL 被明确标记为 "ceiling-effect control"（single-sample F1≈0.91, oracle headroom 仅 4 pp）——作者自己在 Table 5 和 §D 中承认 "selection analysis on these configurations is uninformative"
  - WNUT-17 被标记为 "signal-collapse boundary"（52% zero F1）——信号本身崩溃，无法测试 selection
  - 因此论文的核心发现——greedy 超过所有 N=8 策略——实质上仅在 SciERC 上被验证
- 为什么影响接收：一个旨在揭示 "LLM-based NER" 普遍现象的论文，核心 claim 由单一 domain-specific 数据集（科学文本, 6 entity types, n=529）支撑，泛化性不足。SciERC 的 medium-difficulty 特性（~65% F1）恰好处于 degeneracy 和 collapse 之间的窄带——这可能是一个 sweet-spot artifact 而非普遍现象。
- 建议修改方向：(1) 增加至少一个额外的 medium-difficulty 数据集（如 OntoNotes 5.0 NER 的子集、ACE 2005、或 Few-NERD）在相似 F1 range (50-70%) 验证 selection gap；或 (2) 将 claim 明确限定为 "on a medium-difficulty scientific NER benchmark"，相应调整 title 和 abstract 的泛化程度。

**N2** [critical] 4/5 信号的 selection failure 部分是定义上的必然，非纯经验发现
- 具体位置：Section 3.1 (Problem Formulation), §4.3, Table 2
- 问题：SJ、VC、FK、EM 均为 instance-level 信号——by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 "selection" 实际测试的是 consensus-proximity（MBR），不是原始信号的 selection 能力。这与 LP（唯一 per-sample 信号）的 selection failure 有本质区别：
  - Instance-level 信号不能 select → 这是信号设计的数学必然
  - LP 不能 select → 这是经验发现（compression）
  - 论文将两者混为 "5 个信号都失败"，夸大了发现的规模
- Abstract、Introduction 的 contribution list、和 Conclusion 均写 "five confidence signals" 统一处理，但真正的 empirical surprise 只在 LP。
- 为什么影响接收：Framing 误导了读者对贡献规模的判断。如果准确表述为 "instance-level 信号无法 select（by design），LP 因 compression 也无法 select"，那么贡献集中在 LP compression 的诊断上——这仍有价值，但论文需要重新调整 framing。
- 建议修改方向：在 abstract 和 introduction 中明确区分两类 failure（definitional vs. empirical），将 MBR/consensus-proximity failure 与 LP compression 分别讨论。当前 §3.1 第一段已有初步区分，但后续行文未贯彻。

**N3** [critical] 2-seed Fisher combined p 的统计效力严重不足
- 具体位置：Table 2 ("2-seed mean±σ, Fisher combined p vs. single-sample"), §4.3
- 问题：Selection 的核心结论——"no signal significantly outperforms single-sample (all p>0.05)"——基于仅 2 个 random seed 的 Fisher combined p-value。
  - 2 个独立 sign test 的 Fisher combination 对小效应的检测力极低。LP 的 Δ=+0.2 pp (p=0.29)，但 bootstrap 95% CI 为 [-3.0, +4.2] pp——这个 CI 宽度为 7.2 pp，远超 oracle headroom 的 40%。如此宽的 CI 下，无法区分 "无效果" 和 "有小到中等效果但检测不到"。
  - Cohen's d=0.038（§F, TOST 段落）本身说明效应很小，但 CI 的宽度意味着即使真实效应为 +3 pp（实际有意义），2-seed 设计也可能给出 p>0.05。
  - 3-seed 实验（Table 8）报告 σ≤0.026 for ρ，但这是 QE metric 的 seed 稳定性，不是 selection F1 的 seed 稳定性——论文没有报告 selection F1 的 3-seed variance。
- 为什么影响接收："所有信号的 selection 与 single-sample 无显著差异" 是论文最核心的 negative result。如果这个结论建立在 underpowered test 上，读者无法判断这是 true null 还是 Type II error。
- 建议修改方向：(1) 将 selection 实验扩展到至少 3-seed（最好 5-seed），报告 selection F1 的 seed 间 σ 和 CI；(2) 进行 post-hoc power analysis，明确在当前样本量和 seed 数下能检测到的最小效应大小；(3) 报告 equivalence 的 power，而非仅 p-value。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Non-tied LP subset +2.9 pp (p=0.004) 的 Bonferroni 校正不完整
- 具体位置：§4.3 footnote 4, §F (Appendix), Table in §F (ε sweep)
- 问题：Footnote 4 称 "+2.9 pp, p=0.004 survives Bonferroni correction over 5 comparisons"（α_adj=0.01）。但 Bonferroni 的 5 comparisons 仅计入 5 个信号，未计入 ε 的 post-hoc 选择。Appendix Table (ε sweep) 测试了 7 个 ε 值（0.01 到 0.20），每个给出不同的 subset 和 p-value。如果校正为 7 ε × 5 signals = 35 comparisons，α_adj=0.0014，p=0.004 不再 survive。
- 论文在 Limitations 中坦诚 ε=0.05 是 post-hoc，但 main text footnote 的 "survives Bonferroni" 表述给读者留下了 robust finding 的印象。
- 建议：(1) 在 footnote 4 中明确 Bonferroni 仅覆盖 signal 维度，不含 ε 选择的自由度；(2) 用 permutation test 或 bootstrap 而非 Bonferroni 来评估 subset analysis 的稳健性；或 (3) 更保守地称其为 "exploratory finding" 而非 "survives correction"。

**W2** [warning] Kendall's W=1.0 (3 seeds) 的呈现方式
- 具体位置：§4.4 "Signal rankings are stable across seeds (Kendall's W=1.0 at N=8; Table 11)"
- 问题：Main text 呈现 W=1.0 without caveat。虽然 m=3 raters, n=5 items 下 W=1.0 的 p 值确实显著（χ²=12, df=4, p≈0.017），但问题不是显著性而是 precision：仅 3 个 seed 时，即使一个 seed 产生微小的 ranking 变化（如 VC 和 SJ 互换），W 就会明显下降。Appendix 已承认 "statistical power with n=3 is limited"，但 main text 的呈现过于自信。
- 建议：Main text 加注 "(though 3 seeds provide limited precision for the W estimate)" 或类似 caveat。

**W3** [warning] 模型规模范围（3B-8B）限制了 "intrinsic" 结论的强度
- 具体位置：Conclusion ("confirm these mechanisms are intrinsic to capable fine-tuned models"), §5 Discussion
- 问题：论文在 3B-8B 范围内观察到 instance degeneracy 随 capability 增加（8B 21% vs 4B 10.4%），并推断这是 "intrinsic" 的。但 3B-8B 全是小模型；在 70B+ 规模下，模型可能产生更多样的样本（因更好的 calibration），也可能更 degenerate。两个方向都合理，但论文无法区分。
- "Intrinsic to capable fine-tuned models" 的 claim 基于一个仅有两点（4B 和 8B）的线性外推，且 direction 取决于 capability 的 operationalization。
- Limitations 中虽提及 "whether the gap holds for 70B+ models is untested"，但 Conclusion 的 "intrinsic" 用语暗示了更强的普遍性。
- 建议：将 "intrinsic" 限定为 "intrinsic within the 3B-8B fine-tuned regime we tested"；或提供理论论证为什么 degeneracy 必然随 capability 单调递增。

**W4** [warning] Free-form ablation 对 NER 的 std ratio 0.97 不足以排除 constrained decoding
- 具体位置：§5 "Ablation: free-form decoding", Appendix §K (Table 6)
- 问题：NER 的 free-form std ratio 为 0.97（几乎不变），论文据此声称 "ruling out constrained decoding as the cause of NER compression"。但：
  - 同一 ablation 在 RE 上显示 LP selection 方向完全逆转（constrained -0.9 pp → free-form +1.8 pp），说明 constrained decoding 对 structured extraction 有实质影响
  - NER 和 RE 的不同表现可能反映 NER 的 format template 更简单（entity list vs. relation triples），而非 constrained decoding 无关
  - std ratio 0.97 的 effect size 很小，但 free-form QE 提升了 VC ρ（0.379→0.409），说明 constraint 确实有影响，只是在 selection 维度不明显
- 建议：弱化 "ruling out" 的措辞为 "constrained decoding has minimal effect on NER LP variance but substantial effect on RE"；讨论 NER/RE 差异的可能原因。

**W5** [warning] TOST 等价性结论是 configuration-dependent，main text 未充分反映
- 具体位置：§4.3, Appendix §F (External equivalence margins)
- 问题：Main text 称 "TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration"（§4.3）。但 Appendix §F 更明确地指出：
  - LLaMA-CoNLL: 所有 δ 下均 pass（robust）
  - Qwen-CoNLL: 所有 external δ 下均 fail（selection 实际 degrades 0.9-1.5 pp）
  - SciERC NER: 仅 SJ 在最宽 δ_SEM=1.33 pp 下 pass
  - 这意味着 "equivalence" 仅在一个 configuration 下是 robust 的；其他 configurations 显示信号 actively harms selection
- 建议：Main text 应更平衡地呈现——不仅是 "signals don't help"，某些 configurations 下信号 actively hurts。

---

## 小问题（不影响接收）

- **Title 与 scope 不匹配**：Title 说 "Named Entity Recognition" 但 abstract 和正文多处讨论 RE（虽然标记为 exploratory）。建议 title 明确为 NER 或在 title 中删除 "Named Entity Recognition" 改为 "Information Extraction"（但这需要更强的 RE 支撑）。
- **Greedy (T=0) 与 single-sample 的区分**：Table 2 中 Greedy=0.663 vs Single=0.645，差异 +1.8 pp，但未报告显著性检验。如果 greedy 本身 vs single-sample 不显著，那 "greedy surpasses all selection strategies" 的实际意义减弱——它也不显著优于 single-sample。
- **Table 4 (Degeneracy) 中 CoNLL 用 N=16 而 SciERC 用 N=8**：不同 N 下 degeneracy 比例不可直接比较（更多 samples 更可能产生不同输出）。
- **§5 Discussion 中 "signal combinations" 段落**：LP×VC 的三种组合策略描述简短，但 oracle tiebreaker 的 +7.9 pp 是重要 calibration point，值得更突出。
- **Appendix §G FK split-half reliability**: SciERC r=0.395 较低，暗示 FK 在 harder tasks 上不够稳定，但 main text 仍将 FK 与其他信号并列讨论。

---

## 主要优势

1. **概念贡献清晰且有价值**：将 quality estimation 与 sample selection 解耦是一个重要的方法论区分，解释了为什么看似有效的 confidence signal 在实际 selection 中失败。Figure 1 的 overview 图设计精良，一张图传达了核心发现。

2. **诊断分析深入**：五层 ablation chain（free-form、entity-token LP、verbalized confidence、non-tied subset、signal combination）系统性地排除了替代解释。特别是 verbalized confidence（Appendix §R）的加入——它展示了更高的 ρ 但更差的 selection——强化了 correlation-selection gap 的概念。

3. **Instance degeneracy 作为机制解释具有洞察力**：将 selection failure 归因于 "模型越好，选择空间越小" 的内在矛盾，这是一个非平凡的发现。Within-instance SJ-F1 ρ=0.52（正相关）vs. 整体 selection failure 的对比清晰展示了这一矛盾。

4. **实验透明度高**：对 post-hoc 分析（ε=0.05）、thinking token confound、训练 mismatch 等潜在问题的主动披露达到了很高的标准。Limitations section 诚实且详尽。

5. **Related work positioning 准确**：与 MBR 文献（Eikema et al., 2022, 2025）、self-consistency（Wang et al., 2023）、Yao et al. (2026) 的区分明确——特别是指出本文的 failure mode 不同于 MBR 的 utility misalignment（§2, §5）。

6. **三数据集难度梯度设计**：虽然有效 selection 测试仅在 SciERC 上（N1），但三级梯度（ceiling/medium/collapse）本身是良好的实验设计思路，为 signal behavior 随 difficulty 变化提供了有用的 calibration。

---

## Questions for Authors

1. **关于 N1（单数据集）**：是否有在其他 medium-difficulty NER 数据集（如 OntoNotes 子集或 ACE 2005）上的初步结果？如果没有，能否论证 SciERC 的哪些特性使其结论可能泛化（或不泛化）？

2. **关于 N2（definitional vs. empirical）**：论文是否考虑过仅围绕 LP compression 作为 central finding，将 instance-level 信号的 selection failure 作为 "expected baseline"？这样的 framing 是否会更准确地反映贡献？

3. **关于 greedy vs. selection 的实际含义**：如果一个 practitioner 已知可以用 greedy (T=0)，那 quality estimation（知道哪些 input 可靠）的 practical value 是什么？是否有 downstream use case（如 selective prediction、active learning）where QE signals have clear value despite selection failure？

4. **Instance degeneracy 的实际检测**：在推理时，degeneracy 可以被检测到（所有 N 个输出相同）。是否考虑过一个简单的 hybrid 策略：degenerate instances 用 greedy，non-degenerate instances 用 MBR selection？这相比 pure greedy 的 expected gain 是多少？

5. **Entity-token LP worsening selection despite 4× variance**：§5 讨论了 entity-token LP 在 SciERC 上 variance 增大但 selection 更差。作者能否提供 within-instance entity-token LP 与 F1 的 correlation（类比 pooled ρ=0.248 for full LP）？如果 entity-token LP 的 within-instance ρ 更低，则说明增加的 variance 是 noise 而非 signal。

---

## Missing References

1. **Yixin Liu et al. (2024)**, "Litcoder: Estimating task difficulty for code generation" — 关于 per-sample difficulty estimation 的 test-time compute 工作，与本文的 QE/selection 区分相关。
2. **Shuofei Qiao et al. (2023)**, "Making language models better tool learners with execution feedback" — 关于 structured output 的 verification 机制，与 trained verifiers 的讨论相关。
3. **Daniel Deutsch et al. (2022)**, "Training and meta-evaluating machine translation evaluation metrics at the paragraph level" — MBR with structural metrics 在更复杂 output 上的表现，与 SJ-based MBR 的讨论直接相关。

---

## Overall Assessment 详细说明

**推荐**: 3.0 — Findings acceptance

论文提出了一个有价值的概念（correlation-selection gap），诊断了两个有洞察力的失败机制（instance degeneracy + LP compression），实验设计在结构上是合理的（三级难度梯度、多模型、ablation chain）。

但三个 critical 问题削弱了结论的可信度：(1) 核心 claim 实质上由单数据集支撑；(2) 5-signal framing 夸大了经验发现的规模（4/5 的 failure 是 definitional）；(3) selection 的核心 negative result 基于 underpowered 2-seed test，无法区分 true null 和 Type II error。

如果作者能解决 N1（增加数据集或限定 claim scope）、N2（重新 frame 贡献）、N3（增加 seed 数或 power analysis），我会将评分提升到 3.5-4.0（borderline accept to accept）。当前版本更适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1469 · 2026-05-16T08:40:46.162424+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后启动交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 117

## Round 117

2 recorded events


### User

_source line 1470 · 2026-05-16T08:40:48.765790+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断：Overall 3.0/5 (Findings acceptance)**

三个 critical 问题：
1. 核心 claim（correlation-selection gap）实质上仅由 SciERC (n=529) 一个数据集支撑——CoNLL 是 ceiling control，WNUT-17 是 collapse boundary，都无法有效测试 selection gap
2. 5 个信号中 4 个是 instance-level（by construction 无法 select），将 definitional limitation 与 LP compression 的 empirical finding 混为 "5 signals all fail" 夸大了发现规模
3. Selection 的核心 negative result 基于 2-seed Fisher combined p，bootstrap CI 宽达 7.2 pp，无法区分 true null 和 Type II error

五个 should-fix：non-tied subset 的 Bonferroni 不完整、Kendall's W=1.0 呈现过于自信、3B-8B scale range 不足以支撑 "intrinsic" claim、free-form ablation 的 "ruling out" 措辞过强、TOST 等价性结论的 configuration-dependency 未充分呈现。

论文的主要优势在于概念贡献清晰（QE vs. selection 解耦）、诊断分析深入（五层 ablation chain）、实验透明度高（主动披露 post-hoc 分析和 confounds）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1471 · 2026-05-16T08:40:55.518406+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 完成审稿后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 118

## Round 118

6 recorded events


### User

_source line 1472 · 2026-05-16T08:43:16.819626+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
**审查侧重**: 新颖性 + Related Work + 写作质量 + 格式合规

---

## 总体评分

**Overall**: 3/5 (Findings)
**一句话总结**: 论文提出的 correlation-selection gap 在结构化 IE 中得到充分实证支持，但核心发现的新颖性与 MBR 社区已有知识的增量边界不够清晰，实验限于 3B-8B 小模型且关键数据点（Table 2 Random vs Single 差距）缺乏解释。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计全面（difficulty gradient, multi-seed, ablation chain），统计方法恰当；但 Table 2 Random vs Single 3.5pp 差距未解释 |
| Excitement | 2.5/5 | 核心发现（fine-tuned models produce degenerate outputs → selection fails）直觉上可预期；与 Yao et al. (2026) 增量贡献清晰但不令人兴奋；negative result 有价值但 impact 有限 |
| Overall | 3/5 | 扎实的 empirical analysis paper，适合 Findings track |
| Confidence | 4/5 | 熟悉 MBR decoding、uncertainty estimation、LLM-based IE |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Contribution #1 framing 混淆 by-construction limitation 与 empirical finding
- 位置：Introduction, Contribution #1
- 4/5 信号是 instance-level aggregates，BY DESIGN 对所有 N 个 candidate 赋相同 QE 分。这不是需要 "diagnose" 的失败，而是信号设计的固有属性。论文通过 MBR 将它们转换为 per-sample ranking，但当前 framing 让读者误以为作者发现了 4 个信号为什么无法做 selection——这近乎 tautological。
- 建议：拆分为 (a) MBR conversion fails due to instance degeneracy 和 (b) LP fails due to compression，明确前者的 architectural limitation。

**N2** [critical] Instance degeneracy 新颖性边界未充分建立
- 位置：Section 2 (lines 10-13), Section 5 (lines 8-14)
- "Better fine-tuned models → more consistent outputs → less selection headroom" 在直觉上可预期。论文未区分此发现与 (1) Yun et al. (2025) 的 format-induced diversity collapse, (2) fine-tuning overfitting 的边界。核心 claim "intrinsic to capable fine-tuned models" 未排除 fine-tuning recipe 的 artifact（LoRA rank=32, 5 epochs, dropout=0）。
- 建议：讨论 fine-tuning hyperparameters 对 degeneracy 的潜在影响；将 Yun et al. 的 diversity collapse 作为 related mechanism 讨论；考虑 LoRA rank ablation。

**N3** [critical] Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp 缺乏解释
- 位置：Table 2
- 在 T=1.0 下，Random (uniform from N) 和 Single (one T=1.0 draw) 的期望 F1 应相同。3.5pp 系统性差距（across 529 instances × 2 seeds, ~2.7σ）不太可能是随机波动。如果计算方式不同需明确说明，因为这影响所有 selection methods 的 baseline 解读。

---

## Should-Fix 问题

**W1** [warning] Abstract 信息密度过高
- Abstract 在 ~150 词中塞入 5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation、signal ranking shift。核心信息被数字淹没。此外 ρ=0.45 来自 ceiling-effect control CoNLL，primary SciERC 仅 ρ=0.379。

**W2** [warning] "Soft Jaccard" 命名误导
- 分母用 max(|g_i|,|g_j|) 非 union。NLP 社区中 "Jaccard" 有固定含义（union 分母）。虽然实验不受 normalizer 选择影响（Table 5, Δρ<0.01），但命名造成 reproducibility confusion。

**W3** [warning] 与 Yao et al. (2026) positioning 遗漏关键讨论
- 未讨论 hard-prompted models 中是否存在类似 output concentration。如果 hard-prompted models 不存在 degeneracy → degeneracy 是 fine-tuning artifact，非 task-intrinsic。

**W4** [warning] Yun et al. (2025) 引用讨论不充分
- Yun et al. 的 diversity collapse 与 instance degeneracy 直接相关，但仅作为 "inference efficiency" 附注引用。Free-form ablation 未检验 constant-F1 fraction 是否改变。

**W5** [warning] "surpassing all N=8 selection strategies" 修辞过强
- Greedy 和 selection 回答不同问题、成本不同。应 frame 为 "selection adds no benefit" 而非 "greedy surpasses selection"。Greedy vs Single-sample 差距 (1.8pp) 未经 significance test。

**W6** [warning] 2-seed Fisher combined p 统计效力不足
- 主实验仅 2 seeds，Fisher combined p 信息量有限。Negative result 论文需要更强的 power analysis 排除 false negative。

---

## 小问题
- VC QE signal (Eq 6, continuous) vs VC selection (freq>N/2, discrete) 的关系应在正文说清楚
- SciERC checkpoint 未用 load_best_model_at_end，是否影响 degeneracy
- Introduction 和 Section 4.3 对 "correlation-selection gap" 重复定义
- Thinking token confound 的核心结论可提到 main text footnote

---

## 引用核查
- 53 bib entries, 0 orphan, 0 missing
- 44 verified, 4 not found (recent arXiv, OpenAlex lag), 5 mismatch (name encoding)
- 结论：引用真实可靠

## 格式合规
- ✓ ACL review template, ✓ anonymous, ✓ Limitations, ✓ Ethics, ✓ 引用格式
- 正文页数需编译确认

## 遗漏参考文献
- Director 指定的 4 篇均已引用（schall2025hidden, yun2025price, park2024grammar, eikema2025structured）
- 可能遗漏：Gao et al. (2023) scaling laws for reward model overoptimization

## 主要优势
1. 实验设计 thoroughly controlled（difficulty gradient, multi-model, multi-seed）
2. QE vs selection 解耦框架有方法论价值
3. Negative result 诚实处理，统计证据充分
4. Appendix 质量极高（16+ sections）
5. Within-instance analysis 是最佳部分（non-degenerate instances MBR closes 23-41% gap）

## Questions for Authors
1. Table 2 Random vs Single 精确计算公式及 3.5pp 差距来源？
2. Instance degeneracy 是否与 fine-tuning recipe 相关？
3. Free-form ablation 下 constant-F1 fraction 是否改变？
4. Greedy vs Single 1.8pp 差距是否经过 significance test？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1473 · 2026-05-16T08:44:08.528338+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分：3.0 / 5 (Findings acceptance)\n\n**Must-Fix:**\n\n**N1** [critical] 核心 claim 的有效测试仅由单数据集支撑\n- Selection gap 有效测试仅 SciERC (n=529)。CoNLL 是 ceiling control (4pp headroom)，WNUT-17 是 collapse boundary (52% zero F1)。论文核心发现——greedy 超过所有 N=8 策略——实质上仅在 SciERC 上被验证。\n- SciERC 的 medium-difficulty 特性 (~65% F1) 可能是 sweet-spot artifact 而非普遍现象。\n- 建议增加 medium-difficulty 数据集或限定 claim scope。\n\n**N2** [critical] 4/5 信号的 selection failure 部分是定义上的必然，非纯经验发现\n- SJ、VC、FK、EM 是 instance-level，by construction 对同一 input 所有 N 个候选给相同分数。Table 2 中这些信号的 \"selection\" 实际测试的是 consensus-proximity (MBR)。\n- 论文将 definitional limitation 与 LP compression 的 empirical finding 混为 \"5 个信号都失败\"，夸大了发现规模。\n- Abstract/Intro/Conclusion 均统一处理 \"five confidence signals\"，但真正的 empirical surprise 只在 LP。\n\n**N3** [critical] 2-seed Fisher combined p 的统计效力严重不足\n- Selection 核心 negative result 基于 2 个 seed 的 Fisher combined p。Bootstrap CI [-3.0, +4.2] pp 宽 7.2 pp，远超 oracle headroom 40%。\n- Cohen's d=0.038 说明效应小，但 CI 宽度意味着即使真实效应 +3 pp 也检测不到。\n- 3-seed 实验报告的是 QE 的 seed 稳定性，非 selection F1 的 seed variance。\n- 建议扩展到至少 3-5 seed + power analysis。\n\n**Should-Fix:**\n\n**W1** Non-tied LP subset +2.9pp (p=0.004) 的 Bonferroni 仅覆盖 5 signals，未计入 7 个 ε 值的 post-hoc 选择（7ε×5=35 comparisons, α_adj=0.0014, p=0.004 不再 survive）。\n\n**W2** Kendall's W=1.0 (3 seeds) 在 main text 呈现过于自信，缺少 precision caveat。\n\n**W3** 3B-8B 不足以支撑 \"intrinsic to capable fine-tuned models\" 的 claim。70B+ 可能更 degenerate 也可能产生更多样样本。两个数据点的线性外推不充分。\n\n**W4** Free-form ablation std ratio 0.97 不足以 \"rule out\" constrained decoding——同一 ablation 在 RE 上显示 LP selection 方向完全逆转 (+1.8pp)。\n\n**W5** TOST 等价性结论是 configuration-dependent（LLaMA-CoNLL robust pass，Qwen-CoNLL 所有 external δ 下 fail，SciERC 仅 SJ 在最宽 δ 下 pass），main text 未充分反映。\n\n**主要优势（R1 认为）：**\n1. 概念贡献清晰（QE vs selection 解耦）\n2. 五层 ablation chain 深入\n3. Instance degeneracy 作为机制解释有洞察力\n4. 实验透明度高\n5. Related work positioning 准确\n6. 三数据集难度梯度设计好\n\n**R1 Questions:**\n1. 是否有其他 medium-difficulty NER 数据集上的初步结果？\n2. 是否考虑过仅围绕 LP compression 作为 central finding？\n3. QE 的 practical value（downstream use case）？\n4. Hybrid 策略（degenerate→greedy, non-degenerate→MBR）的 expected gain？\n5. Entity-token LP 的 within-instance ρ 是否更低（增加的 variance 是 noise 还是 signal）？\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Questions 逐条给出 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分：3.0 / 5 (Findings acceptance)\n\n**Must-Fix:**\n\n**N1** [critical] 核心 claim 的有效测试仅由单数据集支撑\n- Selection gap 有效测试仅 SciERC (n=529)。CoNLL 是 ceiling control (4pp headroom)，WNUT-17 是 collapse boundary (52% zero F1)。论文核心发现——greedy 超过所有 N=8 策略——实质上仅在 SciERC 上被验证。\n- SciERC 的 medium-difficulty 特性 (~65% F1) 可能是 sweet-spot artifact 而非普遍现象。\n- 建议增加 medium-difficulty 数据集或限定 claim scope。\n\n**N2** [critical] 4/5 信号的 selection failure 部分是定义上的必然，非纯经验发现\n- SJ、VC、FK、EM 是 instance-level，by construction 对同一 input 所有 N 个候选给相同分数。Table 2 中这些信号的 \"selection\" 实际测试的是 consensus-proximity (MBR)。\n- 论文将 definitional limitation 与 LP compression 的 empirical finding 混为 \"5 个信号都失败\"，夸大了发现规模。\n- Abstract/Intro/Conclusion 均统一处理 \"five confidence signals\"，但真正的 empirical surprise 只在 LP。\n\n**N3** [critical] 2-seed Fisher combined p 的统计效力严重不足\n- Selection 核心 negative result 基于 2 个 seed 的 Fisher combined p。Bootstrap CI [-3.0, +4.2] pp 宽 7.2 pp，远超 oracle headroom 40%。\n- Cohen's d=0.038 说明效应小，但 CI 宽度意味着即使真实效应 +3 pp 也检测不到。\n- 3-seed 实验报告的是 QE 的 seed 稳定性，非 selection F1 的 seed variance。\n- 建议扩展到至少 3-5 seed + power analysis。\n\n**Should-Fix:**\n\n**W1** Non-tied LP subset +2.9pp (p=0.004) 的 Bonferroni 仅覆盖 5 signals，未计入 7 个 ε 值的 post-hoc 选择（7ε×5=35 comparisons, α_adj=0.0014, p=0.004 不再 survive）。\n\n**W2** Kendall's W=1.0 (3 seeds) 在 main text 呈现过于自信，缺少 precision caveat。\n\n**W3** 3B-8B 不足以支撑 \"intrinsic to capable fine-tuned models\" 的 claim。70B+ 可能更 degenerate 也可能产生更多样样本。两个数据点的线性外推不充分。\n\n**W4** Free-form ablation std ratio 0.97 不足以 \"rule out\" constrained decoding——同一 ablation 在 RE 上显示 LP selection 方向完全逆转 (+1.8pp)。\n\n**W5** TOST 等价性结论是 configuration-dependent（LLaMA-CoNLL robust pass，Qwen-CoNLL 所有 external δ 下 fail，SciERC 仅 SJ 在最宽 δ 下 pass），main text 未充分反映。\n\n**主要优势（R1 认为）：**\n1. 概念贡献清晰（QE vs selection 解耦）\n2. 五层 ablation chain 深入\n3. Instance degeneracy 作为机制解释有洞察力\n4. 实验透明度高\n5. Related work positioning 准确\n6. 三数据集难度梯度设计好\n\n**R1 Questions:**\n1. 是否有其他 medium-difficulty NER 数据集上的初步结果？\n2. 是否考虑过仅围绕 LP compression 作为 central finding？\n3. QE 的 practical value（downstream use case）？\n4. Hybrid 策略（degenerate→greedy, non-degenerate→MBR）的 expected gain？\n5. Entity-token LP 的 within-instance ρ 是否更低（增加的 variance 是 noise 还是 signal）？\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5) 和 Questions 逐条给出 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1474 · 2026-05-16T08:44:28.825644+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20297
}
```

</details>

---


### Tool call

_source line 1475 · 2026-05-16T08:44:29.227072+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分：3/5 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] Contribution #1 framing 混淆 by-construction limitation 与 empirical finding\n- 4/5 信号是 instance-level aggregates，BY DESIGN 对所有 N 个 candidate 赋相同 QE 分。这不是需要 \"diagnose\" 的失败，而是信号设计的固有属性。论文通过 MBR 转换为 per-sample ranking，但 framing 让读者误以为作者发现了 4 个信号为何无法 select。\n- 建议：拆分为 (a) MBR conversion fails due to instance degeneracy 和 (b) LP fails due to compression。\n\n**N2** [critical] Instance degeneracy 新颖性边界未充分建立\n- \"Better fine-tuned models → more consistent outputs → less selection headroom\" 直觉上可预期。\n- 未区分与 Yun et al. (2025) format-induced diversity collapse 和 fine-tuning overfitting 的边界。\n- \"Intrinsic to capable fine-tuned models\" 未排除 fine-tuning recipe artifact（LoRA rank=32, 5 epochs, dropout=0）。\n- 建议：讨论 fine-tuning hyperparameters 对 degeneracy 的潜在影响；考虑 LoRA rank ablation。\n\n**N3** [critical] Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp 缺乏解释\n- 在 T=1.0 下，Random (uniform from N) 和 Single (one T=1.0 draw) 的期望 F1 应相同。3.5pp 系统性差距 (across 529 instances × 2 seeds, ~2.7σ) 不太可能是随机波动。如果计算方式不同需明确说明，因为这影响所有 selection methods 的 baseline 解读。\n\n**Should-Fix:**\n\n**W1** Abstract 信息密度过高。ρ=0.45 来自 ceiling-effect control CoNLL，primary SciERC 仅 ρ=0.379。\n\n**W2** \"Soft Jaccard\" 命名误导。分母用 max(|g_i|,|g_j|) 非 union，NLP 社区中 \"Jaccard\" 有固定含义。\n\n**W3** 与 Yao et al. (2026) positioning 遗漏关键讨论——未讨论 hard-prompted models 是否存在类似 output concentration。如果不存在 → degeneracy 是 fine-tuning artifact 非 task-intrinsic。\n\n**W4** Yun et al. (2025) 引用讨论不充分——diversity collapse 与 instance degeneracy 直接相关但仅作附注引用。\n\n**W5** \"surpassing all N=8 selection strategies\" 修辞过强。Greedy vs Single 1.8pp 未经 significance test。\n\n**W6** 2-seed Fisher combined p 统计效力不足。Negative result 需更强 power analysis。\n\n**小问题：**\n- VC QE (continuous) vs VC selection (freq>N/2, discrete) 关系应说清\n- SciERC checkpoint 未用 load_best_model_at_end 是否影响 degeneracy\n- Introduction 和 Section 4.3 对 gap 重复定义\n\n**R2 主要优势认定：**\n1. 实验设计 thoroughly controlled\n2. QE vs selection 解耦框架有方法论价值\n3. Negative result 诚实处理\n4. Appendix 质量极高\n5. Within-instance analysis 是最佳部分（non-degenerate MBR closes 23-41% gap）\n\n**R2 Questions:**\n1. Table 2 Random vs Single 精确计算公式及 3.5pp 差距来源？\n2. Instance degeneracy 是否与 fine-tuning recipe 相关？\n3. Free-form ablation 下 constant-F1 fraction 是否改变？\n4. Greedy vs Single 1.8pp 差距是否经过 significance test？\n\n**R2 Missing References:**\n- Gao et al. (2023) scaling laws for reward model overoptimization\n\n**R2 引用核查：** 53 entries, 0 orphan, 0 missing, 44 verified。\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions 逐条给出 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Must-Fix、Should-Fix 和主要观点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分：3/5 (Findings)\n\n**Must-Fix:**\n\n**N1** [critical] Contribution #1 framing 混淆 by-construction limitation 与 empirical finding\n- 4/5 信号是 instance-level aggregates，BY DESIGN 对所有 N 个 candidate 赋相同 QE 分。这不是需要 \"diagnose\" 的失败，而是信号设计的固有属性。论文通过 MBR 转换为 per-sample ranking，但 framing 让读者误以为作者发现了 4 个信号为何无法 select。\n- 建议：拆分为 (a) MBR conversion fails due to instance degeneracy 和 (b) LP fails due to compression。\n\n**N2** [critical] Instance degeneracy 新颖性边界未充分建立\n- \"Better fine-tuned models → more consistent outputs → less selection headroom\" 直觉上可预期。\n- 未区分与 Yun et al. (2025) format-induced diversity collapse 和 fine-tuning overfitting 的边界。\n- \"Intrinsic to capable fine-tuned models\" 未排除 fine-tuning recipe artifact（LoRA rank=32, 5 epochs, dropout=0）。\n- 建议：讨论 fine-tuning hyperparameters 对 degeneracy 的潜在影响；考虑 LoRA rank ablation。\n\n**N3** [critical] Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp 缺乏解释\n- 在 T=1.0 下，Random (uniform from N) 和 Single (one T=1.0 draw) 的期望 F1 应相同。3.5pp 系统性差距 (across 529 instances × 2 seeds, ~2.7σ) 不太可能是随机波动。如果计算方式不同需明确说明，因为这影响所有 selection methods 的 baseline 解读。\n\n**Should-Fix:**\n\n**W1** Abstract 信息密度过高。ρ=0.45 来自 ceiling-effect control CoNLL，primary SciERC 仅 ρ=0.379。\n\n**W2** \"Soft Jaccard\" 命名误导。分母用 max(|g_i|,|g_j|) 非 union，NLP 社区中 \"Jaccard\" 有固定含义。\n\n**W3** 与 Yao et al. (2026) positioning 遗漏关键讨论——未讨论 hard-prompted models 是否存在类似 output concentration。如果不存在 → degeneracy 是 fine-tuning artifact 非 task-intrinsic。\n\n**W4** Yun et al. (2025) 引用讨论不充分——diversity collapse 与 instance degeneracy 直接相关但仅作附注引用。\n\n**W5** \"surpassing all N=8 selection strategies\" 修辞过强。Greedy vs Single 1.8pp 未经 significance test。\n\n**W6** 2-seed Fisher combined p 统计效力不足。Negative result 需更强 power analysis。\n\n**小问题：**\n- VC QE (continuous) vs VC selection (freq>N/2, discrete) 关系应说清\n- SciERC checkpoint 未用 load_best_model_at_end 是否影响 degeneracy\n- Introduction 和 Section 4.3 对 gap 重复定义\n\n**R2 主要优势认定：**\n1. 实验设计 thoroughly controlled\n2. QE vs selection 解耦框架有方法论价值\n3. Negative result 诚实处理\n4. Appendix 质量极高\n5. Within-instance analysis 是最佳部分（non-degenerate MBR closes 23-41% gap）\n\n**R2 Questions:**\n1. Table 2 Random vs Single 精确计算公式及 3.5pp 差距来源？\n2. Instance degeneracy 是否与 fine-tuning recipe 相关？\n3. Free-form ablation 下 constant-F1 fraction 是否改变？\n4. Greedy vs Single 1.8pp 差距是否经过 significance test？\n\n**R2 Missing References:**\n- Gao et al. (2023) scaling laws for reward model overoptimization\n\n**R2 引用核查：** 53 entries, 0 orphan, 0 missing, 44 verified。\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions 逐条给出 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1476 · 2026-05-16T08:44:30.685298+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1458
}
```

</details>

---


### Assistant

_source line 1477 · 2026-05-16T08:44:34.085709+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1478 · 2026-05-16T08:44:36.697407+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

总结：论文在实验设计和统计方法上非常扎实（Soundness 4/5），但在新颖性上有明显短板（Excitement 2.5/5）。三个 Must-Fix 问题：(1) Contribution #1 混淆了信号设计的固有限制与实证发现；(2) instance degeneracy 的新颖性未充分与已知现象区分，且未排除 fine-tuning recipe artifact；(3) Table 2 Random vs Single 3.5pp 差距无解释。六个 Should-Fix 涵盖 abstract 密度、命名、positioning、修辞、统计效力。引用和格式基本合规。Overall 评分 3/5（Findings track）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1479 · 2026-05-16T08:44:40.658546+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1480 · 2026-05-16T08:46:27.561198+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix

**[AGREE] R1-N1: 核心 claim 仅由 SciERC 单数据集有效支撑**
同意。CoNLL 4pp headroom 和 WNUT-17 52% zero-F1 使两者均无法有效测试 selection gap。核心 finding 仅在 SciERC n=529 上验证。LLaMA/SciERC (Table 6) 提供了独立 model family 的复现，但总体 claim scope 应限定为 "medium-difficulty fine-tuned NER"。

**[AGREE] R1-N2: 4/5 信号的 selection failure 部分是 definitional**
强烈同意，与我的 R2-N1 一致。Instance-level 信号 by construction 无法区分 candidates，真正的 empirical surprise 仅在 LP compression 和 MBR 被 degeneracy 消除两点。"Five signals all fail" 的统一包装夸大了 empirical contribution。

**[REBUT] R1-N3: 2-seed Fisher combined p 统计效力严重不足**
部分同意方向，但不同意 critical 定级。理由：(1) Cohen's d=0.038 意味着即使完美 powered test 也会确认 null effect——effect size 近零才是核心证据，不是 p-value；(2) 多重证据链（TOST at δ=2pp, 4 cross-configurations 复现, greedy 0.663 > best 0.647）超越单一 p-value；(3) R1 说 "真实效应+3pp也检测不到" 但 across 529 instances per-instance variance 是 dominant source，2-seed 限制的是 seed-level variance。建议降级为 should-fix + power analysis。

---

### Should-Fix

**[AGREE] R1-W1**: Non-tied LP Bonferroni 仅覆盖 5 signals 未计入 7ε。Full correction (35 comparisons, α_adj=0.0014) 下 p=0.004 不再 survive。Main text footnote 选择性报告 correction scope。

**[AGREE] R1-W2**: Kendall's W=1.0 with n=3 seeds 信息量有限，main text 缺 caveat。

**[AGREE] R1-W3**: 与我的 R2-N2 一致。3B-8B 两个数据点不支持 "intrinsic" claim。

**[REBUT] R1-W4**: RE 与 NER output structure 不同，cross-task 类比不成立。NER 证据（std ratio 0.97, tied fraction 仅降 2pp）在 NER 范围内充分。但同意 "rule out" 措辞过强，建议改为 "provides evidence against"。

**[AGREE] R1-W5**: TOST configuration-dependence 在 main text 反映不足。Qwen-CoNLL 所有 external δ 下 fail 意味着 selection actively harmful——比 "no benefit" 更强的结论被埋在 appendix。

---

### R1 Questions

Q1 (其他 medium-difficulty 数据集): [AGREE] ACE2005 / OntoNotes medium-difficulty subset 是自然选择。
Q2 (仅聚焦 LP compression): [REBUT] QE vs selection 解耦框架是最有价值贡献，不应放弃。问题在于 framing。
Q3 (QE practical value): [AGREE] 缺乏 downstream use case 讨论（selective prediction, active learning）。
Q4 (Hybrid strategy): [AGREE] Table 3 已有数据支撑计算 hybrid expected gain，计算成本几乎为零。
Q5 (Entity-token LP ρ): [REBUT] Section 5 (lines 63-66) 已回答：4× variance increase 但 selection 更差(-2.0pp)，增加的是 noise 非 signal。

---

### 与 R1 的共识和分歧

**共识**: N1 (single-dataset), N2 (definitional limitation), W2 (W caveat), W3 (scale claim), W5 (TOST nuance)
**分歧**: N3 (我认为应降为 should-fix), W4 (NER-specific evidence 在 NER 范围内充分)
**R1 发现但我未独立发现**: W1 (Bonferroni scope for ε selection) — 有价值补充

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1481 · 2026-05-16T08:46:31.599326+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 121

## Round 121

2 recorded events


### User

_source line 1482 · 2026-05-16T08:46:35.543762+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

两位 Reviewer 的主要共识集中在三点：(1) 核心 claim 仅由 SciERC 单数据集有效支撑；(2) 4/5 信号的 selection failure 部分是 definitional 而非 empirical surprise；(3) 模型规模范围 (3B-8B) 不足以支撑 "intrinsic" claim。主要分歧在统计效力问题的严重性定级（R1 认为 critical，我认为 should-fix）和 free-form ablation 的 cross-task 推断有效性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1483 · 2026-05-16T08:46:40.746647+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 122

## Round 122

10 recorded events


### User

_source line 1484 · 2026-05-16T08:47:39.805404+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2

---

### Must-Fix

**[AGREE] R2-N1: Contribution #1 framing 混淆 by-construction limitation 与 empirical finding**

完全同意，这与我的 R1-N2 指向同一问题。§3.1 第一段明确写了 "4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates"，但 abstract ("five confidence signals... yet best-of-N selection fails") 和 Contribution list ("Two failure mechanisms") 的 framing 将两类本质不同的 failure 混为一谈。R2 提出的拆分方案合理：(a) MBR conversion fails due to instance degeneracy; (b) LP fails due to compression。这能更准确地传达贡献的规模和性质。

补充我的发现：Table 2 中 instance-level 信号的 selection F1 (SJ 0.646, FK 0.646, EM 0.637, VC 0.623) 实际测试的是 consensus-proximity (MBR) 的有效性，不是原始信号的 selection 能力。将 MBR failure 归因于 "信号失败" 是 attribution error。

---

**[PARTIALLY AGREE] R2-N2: Instance degeneracy 新颖性边界**

R2 的两个子论点需要分别评判：

(a) "Better fine-tuned models → more consistent outputs → less headroom 可预期"——部分同意。直觉上 "更好的模型更一致" 确实可预期。但论文的具体贡献不止于此：within-instance SJ-F1 ρ=0.52（Table 4, §5）表明 MBR utility IS aligned with quality（正相关），问题不在 utility misalignment 而在 headroom vanishing。这与 Eikema et al. (2025) 报告的 MBR failure mode 不同（他们归因于 bag-of-unit utility mismatch）。这一区分不是 trivial。Non-degenerate instances 上 MBR closes 23-41% of oracle gap（Table 4）——这证明了 MBR 在有 headroom 时是 work 的。将 failure 精确定位到 headroom 而非 utility 是有价值的诊断。

(b) **"未排除 fine-tuning recipe artifact"——完全同意，这是我未充分强调的问题。** 论文用 LoRA rank=32, dropout=0, 5 epochs（Table 9），且 SciERC 训练未使用 load_best_model_at_end（仅 CoNLL/WNUT 用了）。这意味着 SciERC checkpoint 可能 over-trained，导致 output diversity 人为降低。Degeneracy 21% (8B) vs 10.4% (4B) 的差异可能部分反映了 larger model overfitting faster with same epochs，而非 capability 的 intrinsic property。
- **缺少的 ablation**: LoRA rank ablation（rank 8 vs 16 vs 32）或 epoch ablation（3 vs 5 epochs）能有效区分 fine-tuning artifact 和 intrinsic property。
- **与 Yao et al. (2026) 的关键对比**（也是 R2-W3 的问题）：如果 hard-prompted models 不表现出 degeneracy，则 degeneracy 是 fine-tuning artifact。论文 §2 提到 Yao et al. 但未讨论这一关键区分。

结论：within-instance analysis 的诊断有新颖性，但 "intrinsic to capable fine-tuned models" 的 claim 需要更强支撑。

---

**[AGREE] R2-N3: Table 2 Random (0.610) vs Single (0.645) 差距 3.5pp**

这是我审稿中遗漏的重要问题。在 T=1.0 下：
- Single = one T=1.0 draw → 一个随机 sample 的 F1，averaged across instances
- Random = uniform random from N=8 → 一个随机 sample 的 F1，averaged across instances

两者的期望应相同：E[Random] = E[Single] = (1/N) Σ E[F1(y_i)]。

3.5pp 的系统性差距 (across 529 instances, 2 seeds, ±0.003 variance) 不太可能是随机波动。可能的解释：
1. **计算方式不同**：Single 可能是 N 个 sample 的 mean F1（即期望值），而 Random 是单次 random draw 的 F1。但如果如此，多次 random draw 的均值应收敛到 Single。
2. **样本选择偏差**：如果 Random 使用的 random generator 与 seed 产生了系统性的低质量选择。
3. **F1 计算的 aggregation 差异**：如果 Single 是 macro-averaged 而 Random 使用了不同的 aggregation。

无论原因如何，这个差距影响所有 selection method 的 baseline interpretation——如果 Random 系统性偏低，那 selection methods 相对 Random 的 +3-4pp 实际上可能只是恢复到了 expectation，而非真正的 selection gain。这需要作者明确解释计算方式。

---

### Should-Fix

**[PARTIALLY AGREE] R2-W1: Abstract 信息密度**

Abstract 实际写的是 "ρ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control"——两个数字都明确标注了来源。准确但有 framing 问题：将 ceiling-effect control（CoNLL）的 ρ=0.45 放入 abstract 给读者留下了比 primary result (0.38) 更乐观的印象。由于 CoNLL 的 ρ inflate 部分源于 zero/non-zero boundary effect（§4.2 footnote 5, Appendix §B 均提及），在 abstract 中使用这个数字需要 caveat。

建议：abstract 仅报告 primary test bed 的 ρ=0.38，或用 "ρ=0.38 (primary)" 不提 CoNLL 数字。

---

**[REBUT] R2-W2: "Soft Jaccard" 命名**

R2 认为分母用 max(|g_i|,|g_j|) 而非 union 使 "Jaccard" 名称误导。但：
1. 论文 Eq. 4 的 footnote 已明确说明 "The denominator uses max(|g_i|, |g_j|) per type group rather than |A∪B|"
2. Appendix Table 10 (§D) 验证了 max vs union normalizer 在所有 6 个 model-dataset 组合上 |Δρ|<0.01——结论不受影响
3. "Soft Jaccard" 在 image segmentation 文献中已有使用先例（Iglovikov et al., 2018 等），"Soft" 前缀本身暗示了对标准 Jaccard 的修改
4. 真正的 novelty 在 token-level IoU matching + Hungarian algorithm 的组合，不在分母选择

命名可以更精确（如 "modified Jaccard" 或 "max-normalized overlap"），但这不构成 should-fix 级别的问题——数学定义完整且 robustness 已验证。

---

**[AGREE] R2-W3: 与 Yao et al. (2026) 未讨论 hard-prompted models 的 degeneracy**

完全同意。§2 写了 "Yao et al. (2026) examine consistency–accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models"。但关键问题是：hard-prompted models 是否也表现出 instance degeneracy？
- 如果是 → degeneracy 是 structured extraction 的 task-intrinsic property
- 如果否 → degeneracy 是 fine-tuning artifact（与 R2-N2(b) 呼应）

这个对比对论文的核心 claim ("intrinsic to capable fine-tuned models") 有直接影响。论文 §2 和 §5 都没有讨论这一区分。建议作者在 revision 中至少定性讨论 Yao et al. 的 output diversity 情况，最好补充一个 hard-prompted baseline 的 degeneracy 统计。

---

**[PARTIALLY AGREE] R2-W4: Yun et al. (2025) 讨论不充分**

R2 指出 Yun et al. (2025) 的 diversity collapse 与 instance degeneracy 直接相关。论文 §2 引用了 Schall et al. (2025, "hidden costs of constrained generation for log-probability estimation") 和 Yun et al. (2025, "inference efficiency")，但后者的 diversity collapse finding 与本文的 instance degeneracy 确实高度相关。

不过，论文的 free-form ablation (Appendix §K, Table 6) 已经 address 了 constrained decoding 是否导致 compression 的问题（NER std ratio=0.97），间接 address 了 Yun et al. 的 concern。问题是这个 connection 没有被显式讨论。建议在 §2 或 §5 中增加 1-2 句话，显式连接 Yun et al. 的 diversity collapse 与本文的 degeneracy，并指向 free-form ablation 作为回应。

---

**[AGREE] R2-W5: "surpassing all N=8 selection strategies" 修辞过强**

同意。§4.3 和 Contribution #3 写 "Greedy (T=0, F1=0.663) surpasses all N=8 selection strategies (best: 0.647)"，但 Greedy vs Single (0.663 vs 0.645, +1.8pp) 未经 significance test。如果 Greedy vs Single 不显著，那实际结论应是 "Greedy ≈ Single > all selection strategies"，这改变了 practical implication——不是 greedy 特别好，而是 selection 特别差（甚至不如 random single draw）。

---

**[AGREE] R2-W6: 2-seed Fisher combined p 统计效力不足**

与我的 R1-N3 完全一致。补充：论文虽然在 Table 8 报告了 3-seed QE stability (σ≤0.026)，但这是 Spearman ρ 的 seed 稳定性，不是 selection F1 的。Selection F1 的 seed 间 variance 可能更大（因为 selection 依赖 per-instance ranking 而非 aggregate correlation），但论文没有报告这个数字。

---

### 小问题

**[AGREE]** VC QE (continuous, Eq. 5) vs VC selection (freq > N/2, discrete, footnote 1)：论文 footnote 1 已做区分，但 Table 2 中两种 VC 使用不同定义却共享同一行标签 "VC"，容易混淆。建议在 table caption 中明确。

**[AGREE]** SciERC checkpoint 未用 load_best_model_at_end（Table 9）：这可能导致 SciERC model over-trained，人为增加 degeneracy。这与 R2-N2 的 fine-tuning recipe concern 一致。

**[AGREE]** Introduction 和 §4.3 重复定义 gap：轻微冗余，可合并。

---

### R2 Questions 回应

**Q1 (Random vs Single 计算)**: [AGREE] 需要作者回答。如上述 R2-N3 分析。

**Q2 (Fine-tuning recipe 与 degeneracy)**: [AGREE] 这是 R2-N2(b) 的核心问题。LoRA rank、epoch、dropout 都可能影响 output diversity。论文需要至少 acknowledge 这个 confound，最好提供 ablation evidence。

**Q3 (Free-form 下 constant-F1 fraction)**: [AGREE] 这是诊断 free-form ablation 的关键补充数据。如果 free-form decoding 下 degeneracy 显著降低，则 constrained decoding（而非 model capability）是 degeneracy 的部分原因。Appendix §K Table 6 Panel A 报告了 LP distribution 变化但没有报告 constant-F1 fraction 的变化——这个遗漏值得补充。

**Q4 (Greedy vs Single significance)**: [AGREE] 与 R2-W5 一致。

---

### R2 Missing References

**[PARTIALLY AGREE]** Gao et al. (2023) scaling laws for reward model overoptimization：与论文的直接相关性有限（NER selection ≠ RLHF reward hacking），但 "best-of-N 随 N 增加可能 over-optimize on proxy signal" 的概念框架与本文的 "selection fails despite more samples" 有概念联系。建议仅在 §5 discussion 中作为 broader context 提及，非 core citation。

---

### 与我 R1 审稿的交叉对照

| 问题 | R1 | R2 | 一致性 |
|------|-----|-----|--------|
| Framing conflation (definitional vs empirical) | N2 (critical) | N1 (critical) | **完全一致** |
| 2-seed power | N3 (critical) | W6 (should-fix) | 一致，我评级更高 |
| 单数据集支撑 | N1 (critical) | 未提及 | R2 未覆盖 |
| Random vs Single 3.5pp | 未发现 | N3 (critical) | **R2 发现了我遗漏的问题** |
| Degeneracy novelty/recipe artifact | W3 (scale range) | N2 (critical) | 相关但角度不同 |
| Greedy rhetoric | Minor | W5 (should-fix) | 一致 |
| Yao et al. (2026) positioning | 未涉及 | W3 (should-fix) | **R2 发现了我遗漏的问题** |

**总结**：R2 和我在核心问题（framing conflation, statistical power）上高度一致。R2 补充了两个我遗漏的重要问题（Random vs Single 差距, fine-tuning recipe artifact）。我补充了 R2 未覆盖的单数据集泛化问题。两份审稿结合后，论文需要 address 的核心问题集中在：(1) framing 重构, (2) 统计 power 加强, (3) 泛化性验证或 claim 限定, (4) Random vs Single 解释, (5) fine-tuning recipe ablation or acknowledgment。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1485 · 2026-05-16T08:48:37.096045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1486 · 2026-05-16T08:48:37.146711+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1487 · 2026-05-16T08:48:40.059342+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "max_chars": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "max_chars": "500"
  }
}
```

</details>

---


### Tool result

_source line 1488 · 2026-05-16T08:48:40.109956+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# Memory — struct_self_consist_ie\\n\\n## 服务器环境\\n- autodl-5090: 4× RTX 5090 32GB, Python 3.12, vLLM 0.18.1, LLaMA Factory 0.9.4, tmux 3.2a\\n- gpu-5090-4x-2: 4× RTX 5090 32GB, PyTorch 2.10.0+cu128, vLLM 0.18.1\\n- conda: /root/miniconda3/\\n- 环境初始化: `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\\n- 项目路径: /root/autodl-tmp/struct_self_consist_ie/\\n- 基座模型: /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/\\n- ft_002_v2 merged: checkpoints/qwen3-8b-scierc-merged-v2/\\n- \\n\\n... [截断: 省略 3369 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 3869, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1489 · 2026-05-16T08:56:22.946328+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 †RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n\n# ===== RECURRING ISSUES (updated Round 15) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 15\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: R1-N1 (critical) + R2 AGREE. 核心 finding (greedy > all N=8) 实质仅 SciERC 验证. SciERC medium-difficulty (~65% F1) 可能是 sweet-spot artifact. LLaMA/SciERC 提供 cross-model 复现但仍限于同一 domain.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"增加至少一个 medium-difficulty NER 数据集 (OntoNotes subset, ACE 2005, Few-NERD) 或将所有 claim 显式限定为 medium-difficulty scientific NER.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 15\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 仍是最核心 framing 问题.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: Contribution #1 混合 instance-level limitation 和 LP failure.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识 (R1-N2 + R2-N1): '5 signals all fail' 的统一叙事仍然混淆 definitional limitation (instance-level by construction) 和 empirical finding (MBR degeneracy + LP compression). §3.1 有区分但 Abstract/Intro/Conclusion 未贯彻. 已持续 13 轮, 是最长期未解决的核心问题.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: 删除 by construction, MBR failure→empirical\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract/Intro 拆分三层: (a) instance-level → MBR conversion needed (acknowledged design property), (b) MBR 转换后仍失败 despite ρ=0.52 within-instance (empirical finding), (c) LP per-sample but compressed (empirical finding). Contribution #1 必须反映此区分.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 15\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, ε降为辅助\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: ε sweep gain 单调递增, Bonferroni over 5 signals ≠ correction over 7ε×5.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-W1 + R2 AGREE. Footnote 4 'survives Bonferroni over 5 comparisons' 未计入 7ε post-hoc 选择. 35 comparisons (7ε×5) 下 α_adj=0.0014, p=0.004 不再 survive.\"\n  action_items:\n  - round: 12\n    action: \"Abstract '60% tied'→continuous, ε降为辅助 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Footnote 4 修正 Bonferroni scope 或改为 'exploratory finding'. 当前 'survives correction' 给读者 robust finding 错觉.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: fine-tuning → degeneracy 是关键区分但论文未抓住.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-W3 + R1 AGREE. 关键未回答问题: hard-prompted models 是否存在 instance degeneracy? 如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic. 这是最强差异化论点但仍未被显式讨论.\"\n  action_items:\n  - round: 14\n    action: \"Related Work 增加明确对比段落.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Related Work 或 Discussion 增加显式讨论: (1) Yao et al. = hard-prompted, 本文 = fine-tuned; (2) hard-prompted 是否有 degeneracy 是区分 task-intrinsic vs fine-tuning artifact 的关键; (3) 如无 hard-prompted degeneracy data, 显式承认此 open question.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Abstract 'at two model scales' 未说明 narrow range.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-W3 + R2 AGREE. 3B-8B 两个数据点不足以支撑 'intrinsic to capable fine-tuned models'. 70B+ 行为未知. Conclusion 已限定但 Discussion 'intrinsic' 用语仍暗示更强普遍性.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 15\n    action: \"Discussion 'intrinsic to capable fine-tuned models' 改为 'intrinsic within the 3B-8B fine-tuned regime we tested'. 全文搜索 'intrinsic' 确认无 over-generalization.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.0 p≈0.05 仅 borderline significant\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: 3-seed 功能是 sanity check 非统计推断依据.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-W2 + R2 AGREE. m=3 raters, n=5 items 下单个 ranking swap 即导致 W 大幅下降. Main text 呈现 W=1.0 过于自信, 需 precision caveat.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Main text 'Kendall's W=1.0' 后加 '(though 3 seeds provide limited precision)' 或类似 caveat.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation — (b)/(d) 区分\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 hypotheses\"\n  - round: 14\n    reviewers: [1]\n    note: \"constraint-imposed vs model-learned 区分 sound.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. 论文已有 (a)-(d) 四个 hypotheses, constraint-imposed vs model-learned 区分明确.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加一句显式说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出\"\n  - round: 14\n    reviewers: [1]\n    note: \"'intrinsic' claim 应限定为 NER-specific.\"\n  - round: 15\n    reviewers: [1]\n    note: \"R15 R1-W4 partial: RE reversal 削弱 NER 'ruling out' claim. 共识改 'ruling out' → 'provides evidence against'.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"'ruling out constrained decoding' 改为 'provides evidence against constrained decoding as the primary cause for NER'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"ρ=0.45 headline 来自 ceiling-effect dataset, primary dataset 仅 ρ=0.379\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"改措辞为 moderate-to-strong 或加限定语\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"ρ=0.38 按 Cohen (1988) 属 medium effect.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-W1 + R1 PARTIALLY AGREE. Abstract 'ρ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control' — CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05). 建议 abstract 仅报告 primary ρ=0.38.\"\n  action_items:\n  - round: 14\n    action: \"'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract 改为仅报告 primary ρ=0.38, 或 'moderate (ρ=0.38 on primary, up to 0.45 on ceiling-effect control)' 避免 strong 暗示.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 14\n    reviewers: []\n    note: \"Entity-token LP + LP×VC 已测试, 全部 negative.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. Entity-token LP (4× variance, -2.0pp), LP×VC 三种策略 (best +0.1pp, NS), verbalized confidence (weakest) 全部 negative. Oracle tiebreaker +7.9pp 证明 per-sample signal 存在但 unextractable. 论文已尽力但 no successful remedy.\"\n  action_items:\n  - round: 14\n    action: \"LP×VC combination 整合入 Discussion.\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. Section 3.3 当前写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453 统一 QE 和 selection.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"共识降级: terminology preference, 非实质问题.\"\n  - round: 14\n    reviewers: [1]\n    note: \"Footnote 已有说明, Appendix Δρ<0.01.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: R2-W2 再次提出. R1 REBUT (footnote + Appendix Table 5 Δρ<0.01 + image segmentation precedent). 非共识问题.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 (9句覆盖全部机制和数字)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"精简 Abstract: 移除 MBR mechanical 细节\"\n  - round: 14\n    reviewers: [2]\n    note: \"Abstract 仍覆盖过多技术细节.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: R2-W1 再次提及. Abstract 塞入 5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation. 核心信息被数字淹没.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系未充分讨论, 贡献定位需从 discovery 转为 diagnosis\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"贡献定位需从 'identifying gap' 转为 'diagnosing failure mechanisms'.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 与 R3-W2 同一根源. Contribution 定位仍需调整. R2 额外指出 instance degeneracy 直觉上 'better model → more consistent → less headroom' 可预期, 但 R1 反驳 within-instance ρ=0.52 证明 MBR aligned (非 utility mismatch) 是 non-trivial 区分.\"\n  action_items:\n  - round: 14\n    action: \"Contribution #1 从 'identifying' 改为 'diagnosing two specific failure mechanisms'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Contribution 需突出 within-instance analysis 的 novelty: MBR utility IS aligned (ρ=0.52), failure 来自 headroom vanishing 而非 utility mismatch (区别于 Eikema et al. 2025).\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) 统计效力极低, 应降级为辅助证据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Fisher p 呈现权重应降低.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-N3 (critical) + R2-W6 (should-fix). 方向共识: 2-seed Fisher p 统计效力不足. Severity 分歧: R2 argues d=0.038 + TOST + cross-config 复现是更强证据链, p-value 非核心. 共识: 需 (1) 报告 selection F1 seed variance, (2) 依赖 effect size 和 multiple convergent lines 而非 p>0.05, (3) 考虑 power analysis.\"\n  action_items:\n  - round: 14\n    action: \"Table 2 将 Fisher combined p 降级为辅助.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"主文从 'all p>0.05' 叙事转向 'd=0.038 with multiple convergent lines (TOST, cross-config, greedy comparison)'. 补报 selection F1 3-seed σ.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"greedy 应定位为 practical cost-free alternative.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-W5 + R1 AGREE. 'surpassing all N=8 selection strategies' 仍过强. Greedy vs Single 1.8pp 未 significance-tested. 如不显著, 结论应为 'Greedy ≈ Single > all selection'.\"\n  action_items:\n  - round: 14\n    action: \"'surpassing' 改为 'practical cost-free alternative'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"测试 Greedy vs Single 显著性. 修辞改为 'selection adds no benefit over greedy or single-sample'. 明确 sampling 价值在 QE 而非 selection.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation 缺少 instance degeneracy 统计\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"4B constant F1 fraction 和 oracle headroom 未报告.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Table 6 已包含 4B data (constant F1 10.4%, constant utility 7.0%, within-inst ρ 0.550, oracle gap closed 25.2%). 数据问题已解决. 但新 concern: 8B/4B degeneracy 差异可能反映 fine-tuning recipe artifact (same epochs, larger model overfits faster) 而非 capability. 见 R15-N1.\"\n  action_items:\n  - round: 14\n    action: \"报告 4B 的 degeneracy 统计.\"\n    assigned_to: \"Main Agent (data) + Paper Agent (writing)\"\n    status: done\n  - round: 15\n    action: \"解释 8B vs 4B degeneracy 差异是 capability-driven 还是 recipe artifact. 见 R15-N1.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-Q5: 两者期望值应相同.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-N3 (critical) + R1 AGREE. E[Random] = E[Single] under T=1.0. 3.5pp 差距 (~2.7σ) 是系统性的, 不太可能是随机波动. 可能原因: 计算方式不同 (Random=single draw vs Single=mean over N), aggregation 差异, 或 seed 偏差. 影响所有 selection baseline 解读. 从 R14 的 info 级别升级为 critical.\"\n  action_items:\n  - round: 14\n    action: \"澄清 Random vs Single baseline 的定义差异和 3.5pp 差距来源.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"明确 Random 和 Single 的精确计算公式. 如果定义不同 (如 Random=instance-level random draw, Single=per-seed mean) 则需显式说明并讨论对 baseline 解读的影响.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. Introduction 首次使用时有 Figure 1 caption 定义.\"\n  action_items:\n  - round: 14\n    action: \"Introduction 首次使用时添加 one-sentence 操作性定义.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. 论文统一 3 位小数.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 15) =====\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2-N2(b) + R1 PARTIALLY AGREE. LoRA rank=32, dropout=0, 5 epochs (Table 9). SciERC 未用 load_best_model_at_end. 8B 可能因同样 epoch 数 overfit 更快导致 degeneracy 更高 (21% vs 4B 10.4%). 缺少 LoRA rank / epoch ablation 来区分 recipe artifact 和 capability-intrinsic property.\"\n  action_items:\n  - round: 15\n    action: \"在 Discussion/Limitations 显式承认 fine-tuning recipe confound. 理想情况下提供 LoRA rank 或 epoch ablation; 至少承认 degeneracy 差异可能部分源于 training recipe 而非 capability.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W5 + R2 AGREE. LLaMA-CoNLL: robust pass. Qwen-CoNLL: all external δ FAIL (selection degrades 0.9-1.5pp). SciERC: only SJ at widest δ. 'Selection actively harmful' 比 'no benefit' 更强, 但被埋在 Appendix.\"\n  action_items:\n  - round: 15\n    action: \"Main text Section 4.3 需更平衡呈现 TOST 结果: 某些配置下信号 actively harm selection, 非仅 'no benefit'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 †RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n\n# ===== RECURRING ISSUES (updated Round 15) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 15\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: R1-N1 (critical) + R2 AGREE. 核心 finding (greedy > all N=8) 实质仅 SciERC 验证. SciERC medium-difficulty (~65% F1) 可能是 sweet-spot artifact. LLaMA/SciERC 提供 cross-model 复现但仍限于同一 domain.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"增加至少一个 medium-difficulty NER 数据集 (OntoNotes subset, ACE 2005, Few-NERD) 或将所有 claim 显式限定为 medium-difficulty scientific NER.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 15\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 仍是最核心 framing 问题.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: Contribution #1 混合 instance-level limitation 和 LP failure.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识 (R1-N2 + R2-N1): '5 signals all fail' 的统一叙事仍然混淆 definitional limitation (instance-level by construction) 和 empirical finding (MBR degeneracy + LP compression). §3.1 有区分但 Abstract/Intro/Conclusion 未贯彻. 已持续 13 轮, 是最长期未解决的核心问题.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: 删除 by construction, MBR failure→empirical\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract/Intro 拆分三层: (a) instance-level → MBR conversion needed (acknowledged design property), (b) MBR 转换后仍失败 despite ρ=0.52 within-instance (empirical finding), (c) LP per-sample but compressed (empirical finding). Contribution #1 必须反映此区分.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + 核心叙事受 threshold 选择影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 15\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, ε降为辅助\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: ε sweep gain 单调递增, Bonferroni over 5 signals ≠ correction over 7ε×5.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-W1 + R2 AGREE. Footnote 4 'survives Bonferroni over 5 comparisons' 未计入 7ε post-hoc 选择. 35 comparisons (7ε×5) 下 α_adj=0.0014, p=0.004 不再 survive.\"\n  action_items:\n  - round: 12\n    action: \"Abstract '60% tied'→continuous, ε降为辅助 (D106)\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Footnote 4 修正 Bonferroni scope 或改为 'exploratory finding'. 当前 'survives correction' 给读者 robust finding 错觉.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: fine-tuning → degeneracy 是关键区分但论文未抓住.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-W3 + R1 AGREE. 关键未回答问题: hard-prompted models 是否存在 instance degeneracy? 如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic. 这是最强差异化论点但仍未被显式讨论.\"\n  action_items:\n  - round: 14\n    action: \"Related Work 增加明确对比段落.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Related Work 或 Discussion 增加显式讨论: (1) Yao et al. = hard-prompted, 本文 = fine-tuned; (2) hard-prompted 是否有 degeneracy 是区分 task-intrinsic vs fine-tuning artifact 的关键; (3) 如无 hard-prompted degeneracy data, 显式承认此 open question.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Abstract 'at two model scales' 未说明 narrow range.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-W3 + R2 AGREE. 3B-8B 两个数据点不足以支撑 'intrinsic to capable fine-tuned models'. 70B+ 行为未知. Conclusion 已限定但 Discussion 'intrinsic' 用语仍暗示更强普遍性.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 15\n    action: \"Discussion 'intrinsic to capable fine-tuned models' 改为 'intrinsic within the 3B-8B fine-tuned regime we tested'. 全文搜索 'intrinsic' 确认无 over-generalization.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.0 p≈0.05 仅 borderline significant\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: 3-seed 功能是 sanity check 非统计推断依据.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-W2 + R2 AGREE. m=3 raters, n=5 items 下单个 ranking swap 即导致 W 大幅下降. Main text 呈现 W=1.0 过于自信, 需 precision caveat.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Main text 'Kendall's W=1.0' 后加 '(though 3 seeds provide limited precision)' 或类似 caveat.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation — (b)/(d) 区分\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 hypotheses\"\n  - round: 14\n    reviewers: [1]\n    note: \"constraint-imposed vs model-learned 区分 sound.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. 论文已有 (a)-(d) 四个 hypotheses, constraint-imposed vs model-learned 区分明确.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加一句显式说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出\"\n  - round: 14\n    reviewers: [1]\n    note: \"'intrinsic' claim 应限定为 NER-specific.\"\n  - round: 15\n    reviewers: [1]\n    note: \"R15 R1-W4 partial: RE reversal 削弱 NER 'ruling out' claim. 共识改 'ruling out' → 'provides evidence against'.\"\n  action_items:\n  - round: 12\n    action: \"Discussion 将 RE free-form reversal 定位为 promising direction\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"'ruling out constrained decoding' 改为 'provides evidence against constrained decoding as the primary cause for NER'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"ρ=0.45 headline 来自 ceiling-effect dataset, primary dataset 仅 ρ=0.379\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"改措辞为 moderate-to-strong 或加限定语\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"ρ=0.38 按 Cohen (1988) 属 medium effect.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-W1 + R1 PARTIALLY AGREE. Abstract 'ρ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control' — CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05). 建议 abstract 仅报告 primary ρ=0.38.\"\n  action_items:\n  - round: 14\n    action: \"'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract 改为仅报告 primary ρ=0.38, 或 'moderate (ρ=0.38 on primary, up to 0.45 on ceiling-effect control)' 避免 strong 暗示.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 14\n    reviewers: []\n    note: \"Entity-token LP + LP×VC 已测试, 全部 negative.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. Entity-token LP (4× variance, -2.0pp), LP×VC 三种策略 (best +0.1pp, NS), verbalized confidence (weakest) 全部 negative. Oracle tiebreaker +7.9pp 证明 per-sample signal 存在但 unextractable. 论文已尽力但 no successful remedy.\"\n  action_items:\n  - round: 14\n    action: \"LP×VC combination 整合入 Discussion.\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 12\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. Section 3.3 当前写 n=529 on SciERC from 551, n=2756 on CoNLL from 3453 统一 QE 和 selection.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"共识降级: terminology preference, 非实质问题.\"\n  - round: 14\n    reviewers: [1]\n    note: \"Footnote 已有说明, Appendix Δρ<0.01.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: R2-W2 再次提出. R1 REBUT (footnote + Appendix Table 5 Δρ<0.01 + image segmentation precedent). 非共识问题.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 (9句覆盖全部机制和数字)\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"精简 Abstract: 移除 MBR mechanical 细节\"\n  - round: 14\n    reviewers: [2]\n    note: \"Abstract 仍覆盖过多技术细节.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: R2-W1 再次提及. Abstract 塞入 5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation. 核心信息被数字淹没.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系未充分讨论, 贡献定位需从 discovery 转为 diagnosis\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"贡献定位需从 'identifying gap' 转为 'diagnosing failure mechanisms'.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 与 R3-W2 同一根源. Contribution 定位仍需调整. R2 额外指出 instance degeneracy 直觉上 'better model → more consistent → less headroom' 可预期, 但 R1 反驳 within-instance ρ=0.52 证明 MBR aligned (非 utility mismatch) 是 non-trivial 区分.\"\n  action_items:\n  - round: 14\n    action: \"Contribution #1 从 'identifying' 改为 'diagnosing two specific failure mechanisms'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Contribution 需突出 within-instance analysis 的 novelty: MBR utility IS aligned (ρ=0.52), failure 来自 headroom vanishing 而非 utility mismatch (区别于 Eikema et al. 2025).\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) 统计效力极低, 应降级为辅助证据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Fisher p 呈现权重应降低.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R1-N3 (critical) + R2-W6 (should-fix). 方向共识: 2-seed Fisher p 统计效力不足. Severity 分歧: R2 argues d=0.038 + TOST + cross-config 复现是更强证据链, p-value 非核心. 共识: 需 (1) 报告 selection F1 seed variance, (2) 依赖 effect size 和 multiple convergent lines 而非 p>0.05, (3) 考虑 power analysis.\"\n  action_items:\n  - round: 14\n    action: \"Table 2 将 Fisher combined p 降级为辅助.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"主文从 'all p>0.05' 叙事转向 'd=0.038 with multiple convergent lines (TOST, cross-config, greedy comparison)'. 补报 selection F1 3-seed σ.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"greedy 应定位为 practical cost-free alternative.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-W5 + R1 AGREE. 'surpassing all N=8 selection strategies' 仍过强. Greedy vs Single 1.8pp 未 significance-tested. 如不显著, 结论应为 'Greedy ≈ Single > all selection'.\"\n  action_items:\n  - round: 14\n    action: \"'surpassing' 改为 'practical cost-free alternative'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"测试 Greedy vs Single 显著性. 修辞改为 'selection adds no benefit over greedy or single-sample'. 明确 sampling 价值在 QE 而非 selection.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation 缺少 instance degeneracy 统计\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"4B constant F1 fraction 和 oracle headroom 未报告.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Table 6 已包含 4B data (constant F1 10.4%, constant utility 7.0%, within-inst ρ 0.550, oracle gap closed 25.2%). 数据问题已解决. 但新 concern: 8B/4B degeneracy 差异可能反映 fine-tuning recipe artifact (same epochs, larger model overfits faster) 而非 capability. 见 R15-N1.\"\n  action_items:\n  - round: 14\n    action: \"报告 4B 的 degeneracy 统计.\"\n    assigned_to: \"Main Agent (data) + Paper Agent (writing)\"\n    status: done\n  - round: 15\n    action: \"解释 8B vs 4B degeneracy 差异是 capability-driven 还是 recipe artifact. 见 R15-N1.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-Q5: 两者期望值应相同.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: R2-N3 (critical) + R1 AGREE. E[Random] = E[Single] under T=1.0. 3.5pp 差距 (~2.7σ) 是系统性的, 不太可能是随机波动. 可能原因: 计算方式不同 (Random=single draw vs Single=mean over N), aggregation 差异, 或 seed 偏差. 影响所有 selection baseline 解读. 从 R14 的 info 级别升级为 critical.\"\n  action_items:\n  - round: 14\n    action: \"澄清 Random vs Single baseline 的定义差异和 3.5pp 差距来源.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"明确 Random 和 Single 的精确计算公式. 如果定义不同 (如 Random=instance-level random draw, Single=per-seed mean) 则需显式说明并讨论对 baseline 解读的影响.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. Introduction 首次使用时有 Figure 1 caption 定义.\"\n  action_items:\n  - round: 14\n    action: \"Introduction 首次使用时添加 one-sentence 操作性定义.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. 论文统一 3 位小数.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 15) =====\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R2-N2(b) + R1 PARTIALLY AGREE. LoRA rank=32, dropout=0, 5 epochs (Table 9). SciERC 未用 load_best_model_at_end. 8B 可能因同样 epoch 数 overfit 更快导致 degeneracy 更高 (21% vs 4B 10.4%). 缺少 LoRA rank / epoch ablation 来区分 recipe artifact 和 capability-intrinsic property.\"\n  action_items:\n  - round: 15\n    action: \"在 Discussion/Limitations 显式承认 fine-tuning recipe confound. 理想情况下提供 LoRA rank 或 epoch ablation; 至少承认 degeneracy 差异可能部分源于 training recipe 而非 capability.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R1-W5 + R2 AGREE. LLaMA-CoNLL: robust pass. Qwen-CoNLL: all external δ FAIL (selection degrades 0.9-1.5pp). SciERC: only SJ at widest δ. 'Selection actively harmful' 比 'no benefit' 更强, 但被埋在 Appendix.\"\n  action_items:\n  - round: 15\n    action: \"Main text Section 4.3 需更平衡呈现 TOST 结果: 某些配置下信号 actively harm selection, 非仅 'no benefit'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1490 · 2026-05-16T08:56:23.102453+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 30728}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 156
}
```

</details>

---


### Tool call

_source line 1491 · 2026-05-16T08:58:54.595505+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 15 审稿报告 — Consolidated Review\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计; R2: 新颖性+Related Work+写作+格式）\n**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）\n\n---\n\n## Summary\n\n论文研究 LLM-based NER 中 5 个置信度信号（4 个 instance-level 一致性信号 + 1 个 per-sample LP）的质量估计与样本选择能力，在 SciERC（primary, ~65% F1）、CoNLL-2003（ceiling control, ~91% F1）、WNUT-17（collapse boundary, 48% F1）上评估，使用 Qwen3-8B、LLaMA-3.1-8B 及 4B ablation。核心发现是 \"correlation-selection gap\"：信号有中等 QE 能力（ρ=0.38 on SciERC）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。\n\n---\n\n## Strengths\n\n**S1. QE vs selection 解耦框架有方法论价值** [Both]\n将 quality estimation（哪些 input 可靠？）与 sample selection（哪个 output 最好？）解耦是重要的方法论贡献。Figure 1 一张图传达核心发现，设计精良。\n\n**S2. 诊断分析系统性强** [Both]\n五层 ablation chain（free-form decoding、entity-token LP、verbalized confidence、non-tied subset、signal combination）逐层排除替代解释。Verbalized confidence baseline（更高 ρ 但更差 selection）特别有力地验证了 gap 概念。\n\n**S3. Within-instance analysis 是最强贡献** [Both]\nMBR utility 在 non-degenerate instances 上与 F1 正相关（median ρ=0.52），且 MBR 在这些 instances 上 closes 23-41% of oracle gap——证明 MBR 在有 headroom 时 work。Failure 来自 headroom vanishing 而非 utility misalignment，这与 Eikema et al. (2025) 报告的 MBR failure mode 有 qualitative 区别。\n\n**S4. 实验透明度高** [R1]\n对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。\n\n**S5. Appendix 质量极高** [R2]\n16+ appendix sections 提供了 FK independence test、SJ normalizer robustness、ε sensitivity sweep、calibration analysis、diversity quantification、free-form ablation 等全面补充分析。\n\n**S6. 三数据集难度梯度设计** [Both]\n虽然 selection 有效测试仅在 SciERC 上（见 MF1），ceiling/medium/collapse 梯度本身是良好的实验设计，为信号行为随难度变化提供了有用的 calibration。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [强共识] Framing conflation: \"5 signals all fail\" 混淆 definitional limitation 与 empirical finding**\n- R1-N2 (critical) + R2-N1 (critical)；交叉验证：R1 AGREE R2-N1，R2 AGREE R1-N2\n- 4/5 信号（SJ、VC、FK、EM）是 instance-level，by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 \"selection\" 实际测试的是 consensus-proximity (MBR)。将 MBR failure 归因于 \"信号失败\" 是 attribution error。\n- Abstract (\"five confidence signals... yet best-of-N selection fails\")、Contribution #1 和 Conclusion 将两类本质不同的 failure 混为一谈。§3.1 第一段已有区分 (\"This distinction is consequential for selection\") 但未向 Abstract/Intro/Conclusion 传递。\n- **真正的 empirical findings 是**: (a) MBR 转换产生 per-sample ranking 后仍失败（despite within-instance ρ=0.52），因 instance degeneracy 消除 headroom; (b) LP 因 compression 失败（median range 0.041 nats）。\n- **Required action**: Abstract/Intro 拆分三层叙事——(a) instance-level 需 MBR 转换（acknowledged design property），(b) MBR 转换后仍失败 despite positive within-instance correlation（empirical），(c) LP per-sample but compressed（empirical）。\n- **历史**: 此问题自 Round 3 (R3-W2) 首次提出，持续 13 轮未完全解决。\n\n**MF2. [强共识] 核心 claim 实质上仅由 SciERC (n=529) 单数据集支撑**\n- R1-N1 (critical)；R2 交叉 AGREE\n- CoNLL 是论文自己的 \"ceiling-effect control\"（oracle headroom 仅 4pp，论文在 Appendix §D 承认 \"selection analysis on these configurations is uninformative\"）。WNUT-17 是 \"signal-collapse boundary\"（52% zero F1）。因此核心 finding——greedy > all N=8 selection——仅在 SciERC 上验证。\n- SciERC 的 medium-difficulty regime (~65% F1) 可能是 sweet-spot artifact 而非普遍现象。LLaMA/SciERC 提供 cross-model 复现但仍限于同一 domain（科学文本，6 entity types）。\n- **Required action**: (1) 增加至少一个 medium-difficulty NER 数据集（OntoNotes subset、ACE 2005、Few-NERD）在 50-70% F1 range 验证; 或 (2) 将所有 claim 显式限定为 \"medium-difficulty scientific NER\" 并相应调整 title/abstract 泛化程度。\n- **历史**: 自 Round 0 (R0-C3) 首次提出，持续 15 轮。\n\n**MF3. [强共识] Table 2 Random (0.610) vs Single (0.645): 3.5pp 差距未解释**\n- R2-N3 (critical)；R1 交叉 AGREE\n- 在 T=1.0 下，Random（从 N=8 均匀选取）和 Single（一次 T=1.0 采样）的期望 F1 应相同：E[Random] = E[Single] = (1/N)ΣE[F1(yi)]。3.5pp 系统性差距（across n=529 instances, 2 seeds, ±0.003 variance, ~2.7σ）不太可能是随机波动。\n- 此差距影响所有 selection method 的 baseline 解读。若 Random 系统性偏低，则 selection methods 相对 Random 的 +3-4pp 可能仅是恢复期望，而非真正的 selection gain。\n- **Required action**: 明确 Random 和 Single 的精确计算方式。若定义不同（如 Random=instance-level random draw, Single=per-seed mean），需显式说明并讨论对 baseline 解读的影响。\n- **历史**: Round 14 (R14-M1) 作为 info 提出，本轮升级为 critical。\n\n**MF4. [方向共识, Severity 分歧] 2-seed Fisher combined p 统计效力不足**\n- R1-N3 (critical) + R2-W6 (should-fix)；R2 交叉 REBUT on severity（同意方向）\n- 核心 negative conclusion \"no signal significantly outperforms single-sample (all p>0.05)\" 基于 2-seed Fisher combined p。Bootstrap 95% CI [-3.0, +4.2]pp（宽 7.2pp），远超 oracle headroom 40%。\n- **R2 反驳 severity**: Cohen's d=0.038 接近零是更可靠的证据；TOST equivalence、4 cross-configurations 复现、greedy comparison 构成多重证据链，超越单一 p-value。\n- **共识 action**: (1) 报告 selection F1 的 3-seed variance（当前仅报告 QE 的 seed stability）；(2) 主文从 \"all p>0.05\" 叙事转向 \"d=0.038 with multiple convergent lines\"；(3) 考虑 power analysis。\n\n### Should-Fix（影响评分）\n\n**SF1. [共识] Instance degeneracy: fine-tuning recipe artifact 未排除**\n- R2-N2(b) + R1 交叉 PARTIALLY AGREE\n- LoRA rank=32, dropout=0, 5 epochs（Table 9），SciERC 未用 load_best_model_at_end。8B vs 4B degeneracy 差异（21% vs 10.4%）可能反映 larger model with same epochs overfits faster，而非 capability-intrinsic property。\n- **Action**: 在 Discussion/Limitations 显式承认 fine-tuning recipe confound；理想情况提供 LoRA rank 或 epoch ablation。\n\n**SF2. [共识] 与 Yao et al. (2026) positioning: 缺少 hard-prompted degeneracy 讨论**\n- R2-W3 + R1 交叉 AGREE\n- 关键未回答问题：hard-prompted models 是否存在 instance degeneracy？如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic。这是论文最强差异化论点但未被显式讨论。\n- **Action**: Related Work 或 Discussion 增加显式对比。\n\n**SF3. [共识] \"Surpassing all N=8 selection strategies\" 修辞过强**\n- R2-W5 + R1 交叉 AGREE\n- Greedy (T=0, 0.663) vs Single (T=1.0, 0.645) +1.8pp 未经 significance test。如不显著，结论应为 \"Greedy ≈ Single > all selection strategies\"——failure 是 selection 不如 random single draw，非 greedy 特别好。\n- **Action**: 测试 Greedy vs Single 显著性；修辞改为 \"selection adds no benefit\"。\n\n**SF4. [共识] Non-tied LP subset Bonferroni correction scope 不完整**\n- R1-W1 + R2 交叉 AGREE\n- Footnote 4 称 \"+2.9pp, p=0.004 survives Bonferroni over 5 comparisons\"，但未计入 7 个 ε 值的 post-hoc 选择。Full correction: 7ε × 5 signals = 35 comparisons, α_adj=0.0014, p=0.004 不再 survive。\n- **Action**: 修正 Bonferroni scope 或改为 \"exploratory finding\"。\n\n**SF5. [共识] Kendall's W=1.0 (3 seeds) 呈现缺乏 precision caveat**\n- R1-W2 + R2 交叉 AGREE\n- m=3, n=5 下单个 ranking swap 即导致 W 大幅下降。Main text 需加 precision caveat。\n\n**SF6. [共识] Scale range (3B-8B) 不足以支撑 \"intrinsic\" claim**\n- R1-W3 + R2 交叉 AGREE\n- 两个数据点不支持 \"intrinsic to capable fine-tuned models\" 的外推。\n- **Action**: 限定为 \"within the 3B-8B fine-tuned regime\"。\n\n**SF7. [共识] TOST 等价性 configuration-dependent, main text 未充分呈现**\n- R1-W5 + R2 交叉 AGREE\n- Qwen-CoNLL: 所有 external δ 下 FAIL（selection degrades 0.9-1.5pp）——信号 actively harmful。此结论比 \"no benefit\" 更强，但被埋在 Appendix。\n- **Action**: Section 4.3 更平衡呈现 TOST 结果。\n\n**SF8. [部分共识] Abstract ρ=0.45 headline 来自 ceiling-effect dataset**\n- R2-W1 + R1 交叉 PARTIALLY AGREE\n- CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05)。Primary SciERC ρ=0.38 按 Cohen (1988) 属 medium effect。\n- **Action**: Abstract 仅报告 primary ρ=0.38，或明确标注 0.45 来源。\n\n### Minor Issues\n\nM1. Free-form ablation \"ruling out\" 改为 \"provides evidence against\"（共识）\nM2. VC QE (continuous, Eq.5) vs VC selection (freq>N/2, discrete) 在 Table 2 中共享标签 \"VC\"，需在 caption 澄清\nM3. Greedy vs Single 1.8pp 需 significance test\nM4. SciERC checkpoint 未用 load_best_model_at_end，可能增加 degeneracy，需 acknowledge\nM5. \"Soft Jaccard\" 命名（R2 提出，R1 rebut——非共识问题，但可考虑首次使用时加注）\nM6. Yun et al. (2025) diversity collapse 与 degeneracy 的联系需显式讨论（1-2 句）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Framing 必须重构**：区分 definitional (instance-level) 和 empirical (MBR + LP) failure modes\n2. **核心 claim scope** 必须限定或跨数据集验证\n3. **Random vs Single 差距**必须解释\n4. **\"Intrinsic\" claim** 需限定到已测试 regime\n5. **Greedy 修辞**应重新定位\n6. **Yao et al. 对比**需补充 hard-prompted degeneracy 讨论\n7. **Non-tied LP Bonferroni** correction scope 需修正\n8. 两位 Reviewer 独立评分均为 **3.0/5 (Findings-level)**\n\n## Reviewer Divergence [REBUT]\n\n1. **2-seed Fisher p severity**: R1 评 critical，R2 评 should-fix。R2 认为 d=0.038 + 多重证据链比单一 p-value 更可靠。两位同意方向（power 不足），分歧仅在是否 blocks acceptance。\n2. **Free-form ablation cross-task inference**: R1 认为 RE reversal (+1.8pp) 削弱 NER \"ruling out\" claim；R2 认为 NER/RE output structure 不同，NER-specific evidence (std ratio 0.97) 在 NER 范围内充分。**共识: 弱化措辞为 \"provides evidence against\"。**\n3. **\"Soft Jaccard\" 命名**: R2 认为误导；R1 rebut（footnote + Appendix Δρ<0.01 + 先例）。非共识问题。\n\n---\n\n## Questions for Authors\n\nQ1. [Both] Table 2 Random (0.610) vs Single (0.645): 精确计算公式？3.5pp 系统性差距来源？\nQ2. [Both] Instance degeneracy 是否对 fine-tuning recipe 敏感（LoRA rank、epochs、dropout、load_best_model_at_end）？\nQ3. [R1] 是否有其他 medium-difficulty NER 数据集上的初步结果？\nQ4. [R2, R1 AGREE] Free-form decoding 下 constant-F1 fraction 是否改变？\nQ5. [R1] Hybrid 策略（degenerate→greedy, non-degenerate→MBR）的 expected gain？\nQ6. [R1] Entity-token LP 的 within-instance ρ（F1）是多少？增加的 variance 是 noise 还是 signal？\nQ7. [R2, R1 AGREE] Greedy (T=0) vs Single (T=1.0) 是否经过 significance test？\n\n---\n\n## Missing References\n\n1. Gao et al. (2023) \"Scaling laws for reward model overoptimization\" — best-of-N proxy signal limitation 的概念联系（R2 提出，R1 PARTIALLY AGREE: 相关性有限，可在 Discussion 提及）\n2. Deutsch et al. (2022) \"Training and meta-evaluating machine translation evaluation metrics at the paragraph level\" — MBR with structural metrics（R1 提出）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Overall Assessment\n\n**Score: borderline**\n**Confidence: 4/5**\n**推荐 Track: Findings**\n\n两位 Reviewer 独立评分均为 3.0/5。论文提出了有价值的概念贡献（QE vs selection 解耦）并提供了深入的诊断分析。Within-instance analysis（MBR utility aligned but headroom vanishing）是最强贡献，与 Eikema et al. (2025) 的 MBR utility mismatch 有 qualitative 区别。\n\n但四个 Must-Fix 问题限制了当前版本的可接受性：\n1. **Framing inflation**: \"5 signals all fail\" 将 definitional limitation 包装为 empirical discovery（持续 13 轮未完全解决）\n2. **Single-dataset support**: 核心 claim 仅在 SciERC (n=529) 上有效验证（持续 15 轮）\n3. **Unexplained baseline**: Random vs Single 3.5pp 差距影响 baseline 解读\n4. **Statistical power**: 2-seed Fisher p 不足以支撑核心 negative result\n\n**Findings track 路径**: 解决 MF1（framing 重构）、MF3（Random vs Single 解释）、SF1-SF8 中的写作修正即可满足 Findings track 要求。\n\n**Main conference 路径**: 在 Findings 路径基础上，还需 MF2（增加数据集或进一步限定 scope）和 MF4（statistical power 加强）。\n\n---\n\n## Detailed Comments (Section-by-Section)\n\n### Abstract\n- 信息密度仍高——5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation 均出现\n- ρ=0.45 来自 ceiling-effect control，可能给 \"moderate-to-strong\" 错觉\n- \"Five confidence signals\" 统一叙事需拆分\n- \"Within a narrow model-scale range (4B-8B)\" 良好限定\n\n### Introduction (§1)\n- Contribution #1 混合 definitional 和 empirical failure——需重构\n- Figure 1 + operationalization 有效\n- 已正确识别 instance-level vs per-sample 区分但未贯彻到 contribution list\n\n### Related Work (§2)\n- 覆盖全面（self-consistency, MBR, uncertainty, calibration）\n- Schall et al., Yun et al., Park et al., Eikema et al. 均已引用\n- 缺少: Yao et al. hard-prompted vs fine-tuned degeneracy 对比\n- 缺少: Yun et al. diversity collapse 与 instance degeneracy 的显式联系\n\n### Method (§3)\n- 信号定义数学严谨，evaluation framework 清晰\n- §3.1 有关键区分但需向前传递\n\n### Experiments (§4)\n- Table 1 QE 结果呈现清晰\n- Table 2 Selection 结果是核心但 Random vs Single 差距需解释\n- §4.3 \"all p>0.05\" 叙事应转向 effect size\n- Table 4 Degeneracy: 含 4B data，within-instance analysis 是最强部分\n\n### Discussion (§5)\n- Instance degeneracy mechanism 论证充分（MBR + within-instance ρ）\n- LP compression 诊断系统（四个 hypotheses, constraint-imposed vs model-learned）\n- \"Intrinsic\" 用语需 scope 限定\n- Signal combinations: LP×VC 三策略 + oracle tiebreaker +7.9pp 是重要 calibration\n\n### Conclusion (§6)\n- 准确总结但继承 framing 问题\n- 70B+ open question 恰当\n\n### Limitations\n- 全面诚实\n- 应增加 fine-tuning recipe confound acknowledgment\n\n### Ethics Statement\n- 对论文 scope 而言充分\n\n### 格式合规\n- ACL review template ✓, Anonymous ✓, Limitations ✓, Ethics ✓\n- 引用: 53 entries, 0 orphan, 44 verified（R2 审核）\n- 正文页数需编译确认",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 15 审稿报告 — Consolidated Review\n\n**论文**: \"Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition\"\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计; R2: 新颖性+Related Work+写作+格式）\n**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）\n\n---\n\n## Summary\n\n论文研究 LLM-based NER 中 5 个置信度信号（4 个 instance-level 一致性信号 + 1 个 per-sample LP）的质量估计与样本选择能力，在 SciERC（primary, ~65% F1）、CoNLL-2003（ceiling control, ~91% F1）、WNUT-17（collapse boundary, 48% F1）上评估，使用 Qwen3-8B、LLaMA-3.1-8B 及 4B ablation。核心发现是 \"correlation-selection gap\"：信号有中等 QE 能力（ρ=0.38 on SciERC）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。\n\n---\n\n## Strengths\n\n**S1. QE vs selection 解耦框架有方法论价值** [Both]\n将 quality estimation（哪些 input 可靠？）与 sample selection（哪个 output 最好？）解耦是重要的方法论贡献。Figure 1 一张图传达核心发现，设计精良。\n\n**S2. 诊断分析系统性强** [Both]\n五层 ablation chain（free-form decoding、entity-token LP、verbalized confidence、non-tied subset、signal combination）逐层排除替代解释。Verbalized confidence baseline（更高 ρ 但更差 selection）特别有力地验证了 gap 概念。\n\n**S3. Within-instance analysis 是最强贡献** [Both]\nMBR utility 在 non-degenerate instances 上与 F1 正相关（median ρ=0.52），且 MBR 在这些 instances 上 closes 23-41% of oracle gap——证明 MBR 在有 headroom 时 work。Failure 来自 headroom vanishing 而非 utility misalignment，这与 Eikema et al. (2025) 报告的 MBR failure mode 有 qualitative 区别。\n\n**S4. 实验透明度高** [R1]\n对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。\n\n**S5. Appendix 质量极高** [R2]\n16+ appendix sections 提供了 FK independence test、SJ normalizer robustness、ε sensitivity sweep、calibration analysis、diversity quantification、free-form ablation 等全面补充分析。\n\n**S6. 三数据集难度梯度设计** [Both]\n虽然 selection 有效测试仅在 SciERC 上（见 MF1），ceiling/medium/collapse 梯度本身是良好的实验设计，为信号行为随难度变化提供了有用的 calibration。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [强共识] Framing conflation: \"5 signals all fail\" 混淆 definitional limitation 与 empirical finding**\n- R1-N2 (critical) + R2-N1 (critical)；交叉验证：R1 AGREE R2-N1，R2 AGREE R1-N2\n- 4/5 信号（SJ、VC、FK、EM）是 instance-level，by construction 对同一 input 的所有 N 个候选给出相同分数。Table 2 中这些信号的 \"selection\" 实际测试的是 consensus-proximity (MBR)。将 MBR failure 归因于 \"信号失败\" 是 attribution error。\n- Abstract (\"five confidence signals... yet best-of-N selection fails\")、Contribution #1 和 Conclusion 将两类本质不同的 failure 混为一谈。§3.1 第一段已有区分 (\"This distinction is consequential for selection\") 但未向 Abstract/Intro/Conclusion 传递。\n- **真正的 empirical findings 是**: (a) MBR 转换产生 per-sample ranking 后仍失败（despite within-instance ρ=0.52），因 instance degeneracy 消除 headroom; (b) LP 因 compression 失败（median range 0.041 nats）。\n- **Required action**: Abstract/Intro 拆分三层叙事——(a) instance-level 需 MBR 转换（acknowledged design property），(b) MBR 转换后仍失败 despite positive within-instance correlation（empirical），(c) LP per-sample but compressed（empirical）。\n- **历史**: 此问题自 Round 3 (R3-W2) 首次提出，持续 13 轮未完全解决。\n\n**MF2. [强共识] 核心 claim 实质上仅由 SciERC (n=529) 单数据集支撑**\n- R1-N1 (critical)；R2 交叉 AGREE\n- CoNLL 是论文自己的 \"ceiling-effect control\"（oracle headroom 仅 4pp，论文在 Appendix §D 承认 \"selection analysis on these configurations is uninformative\"）。WNUT-17 是 \"signal-collapse boundary\"（52% zero F1）。因此核心 finding——greedy > all N=8 selection——仅在 SciERC 上验证。\n- SciERC 的 medium-difficulty regime (~65% F1) 可能是 sweet-spot artifact 而非普遍现象。LLaMA/SciERC 提供 cross-model 复现但仍限于同一 domain（科学文本，6 entity types）。\n- **Required action**: (1) 增加至少一个 medium-difficulty NER 数据集（OntoNotes subset、ACE 2005、Few-NERD）在 50-70% F1 range 验证; 或 (2) 将所有 claim 显式限定为 \"medium-difficulty scientific NER\" 并相应调整 title/abstract 泛化程度。\n- **历史**: 自 Round 0 (R0-C3) 首次提出，持续 15 轮。\n\n**MF3. [强共识] Table 2 Random (0.610) vs Single (0.645): 3.5pp 差距未解释**\n- R2-N3 (critical)；R1 交叉 AGREE\n- 在 T=1.0 下，Random（从 N=8 均匀选取）和 Single（一次 T=1.0 采样）的期望 F1 应相同：E[Random] = E[Single] = (1/N)ΣE[F1(yi)]。3.5pp 系统性差距（across n=529 instances, 2 seeds, ±0.003 variance, ~2.7σ）不太可能是随机波动。\n- 此差距影响所有 selection method 的 baseline 解读。若 Random 系统性偏低，则 selection methods 相对 Random 的 +3-4pp 可能仅是恢复期望，而非真正的 selection gain。\n- **Required action**: 明确 Random 和 Single 的精确计算方式。若定义不同（如 Random=instance-level random draw, Single=per-seed mean），需显式说明并讨论对 baseline 解读的影响。\n- **历史**: Round 14 (R14-M1) 作为 info 提出，本轮升级为 critical。\n\n**MF4. [方向共识, Severity 分歧] 2-seed Fisher combined p 统计效力不足**\n- R1-N3 (critical) + R2-W6 (should-fix)；R2 交叉 REBUT on severity（同意方向）\n- 核心 negative conclusion \"no signal significantly outperforms single-sample (all p>0.05)\" 基于 2-seed Fisher combined p。Bootstrap 95% CI [-3.0, +4.2]pp（宽 7.2pp），远超 oracle headroom 40%。\n- **R2 反驳 severity**: Cohen's d=0.038 接近零是更可靠的证据；TOST equivalence、4 cross-configurations 复现、greedy comparison 构成多重证据链，超越单一 p-value。\n- **共识 action**: (1) 报告 selection F1 的 3-seed variance（当前仅报告 QE 的 seed stability）；(2) 主文从 \"all p>0.05\" 叙事转向 \"d=0.038 with multiple convergent lines\"；(3) 考虑 power analysis。\n\n### Should-Fix（影响评分）\n\n**SF1. [共识] Instance degeneracy: fine-tuning recipe artifact 未排除**\n- R2-N2(b) + R1 交叉 PARTIALLY AGREE\n- LoRA rank=32, dropout=0, 5 epochs（Table 9），SciERC 未用 load_best_model_at_end。8B vs 4B degeneracy 差异（21% vs 10.4%）可能反映 larger model with same epochs overfits faster，而非 capability-intrinsic property。\n- **Action**: 在 Discussion/Limitations 显式承认 fine-tuning recipe confound；理想情况提供 LoRA rank 或 epoch ablation。\n\n**SF2. [共识] 与 Yao et al. (2026) positioning: 缺少 hard-prompted degeneracy 讨论**\n- R2-W3 + R1 交叉 AGREE\n- 关键未回答问题：hard-prompted models 是否存在 instance degeneracy？如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic。这是论文最强差异化论点但未被显式讨论。\n- **Action**: Related Work 或 Discussion 增加显式对比。\n\n**SF3. [共识] \"Surpassing all N=8 selection strategies\" 修辞过强**\n- R2-W5 + R1 交叉 AGREE\n- Greedy (T=0, 0.663) vs Single (T=1.0, 0.645) +1.8pp 未经 significance test。如不显著，结论应为 \"Greedy ≈ Single > all selection strategies\"——failure 是 selection 不如 random single draw，非 greedy 特别好。\n- **Action**: 测试 Greedy vs Single 显著性；修辞改为 \"selection adds no benefit\"。\n\n**SF4. [共识] Non-tied LP subset Bonferroni correction scope 不完整**\n- R1-W1 + R2 交叉 AGREE\n- Footnote 4 称 \"+2.9pp, p=0.004 survives Bonferroni over 5 comparisons\"，但未计入 7 个 ε 值的 post-hoc 选择。Full correction: 7ε × 5 signals = 35 comparisons, α_adj=0.0014, p=0.004 不再 survive。\n- **Action**: 修正 Bonferroni scope 或改为 \"exploratory finding\"。\n\n**SF5. [共识] Kendall's W=1.0 (3 seeds) 呈现缺乏 precision caveat**\n- R1-W2 + R2 交叉 AGREE\n- m=3, n=5 下单个 ranking swap 即导致 W 大幅下降。Main text 需加 precision caveat。\n\n**SF6. [共识] Scale range (3B-8B) 不足以支撑 \"intrinsic\" claim**\n- R1-W3 + R2 交叉 AGREE\n- 两个数据点不支持 \"intrinsic to capable fine-tuned models\" 的外推。\n- **Action**: 限定为 \"within the 3B-8B fine-tuned regime\"。\n\n**SF7. [共识] TOST 等价性 configuration-dependent, main text 未充分呈现**\n- R1-W5 + R2 交叉 AGREE\n- Qwen-CoNLL: 所有 external δ 下 FAIL（selection degrades 0.9-1.5pp）——信号 actively harmful。此结论比 \"no benefit\" 更强，但被埋在 Appendix。\n- **Action**: Section 4.3 更平衡呈现 TOST 结果。\n\n**SF8. [部分共识] Abstract ρ=0.45 headline 来自 ceiling-effect dataset**\n- R2-W1 + R1 交叉 PARTIALLY AGREE\n- CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05)。Primary SciERC ρ=0.38 按 Cohen (1988) 属 medium effect。\n- **Action**: Abstract 仅报告 primary ρ=0.38，或明确标注 0.45 来源。\n\n### Minor Issues\n\nM1. Free-form ablation \"ruling out\" 改为 \"provides evidence against\"（共识）\nM2. VC QE (continuous, Eq.5) vs VC selection (freq>N/2, discrete) 在 Table 2 中共享标签 \"VC\"，需在 caption 澄清\nM3. Greedy vs Single 1.8pp 需 significance test\nM4. SciERC checkpoint 未用 load_best_model_at_end，可能增加 degeneracy，需 acknowledge\nM5. \"Soft Jaccard\" 命名（R2 提出，R1 rebut——非共识问题，但可考虑首次使用时加注）\nM6. Yun et al. (2025) diversity collapse 与 degeneracy 的联系需显式讨论（1-2 句）\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Framing 必须重构**：区分 definitional (instance-level) 和 empirical (MBR + LP) failure modes\n2. **核心 claim scope** 必须限定或跨数据集验证\n3. **Random vs Single 差距**必须解释\n4. **\"Intrinsic\" claim** 需限定到已测试 regime\n5. **Greedy 修辞**应重新定位\n6. **Yao et al. 对比**需补充 hard-prompted degeneracy 讨论\n7. **Non-tied LP Bonferroni** correction scope 需修正\n8. 两位 Reviewer 独立评分均为 **3.0/5 (Findings-level)**\n\n## Reviewer Divergence [REBUT]\n\n1. **2-seed Fisher p severity**: R1 评 critical，R2 评 should-fix。R2 认为 d=0.038 + 多重证据链比单一 p-value 更可靠。两位同意方向（power 不足），分歧仅在是否 blocks acceptance。\n2. **Free-form ablation cross-task inference**: R1 认为 RE reversal (+1.8pp) 削弱 NER \"ruling out\" claim；R2 认为 NER/RE output structure 不同，NER-specific evidence (std ratio 0.97) 在 NER 范围内充分。**共识: 弱化措辞为 \"provides evidence against\"。**\n3. **\"Soft Jaccard\" 命名**: R2 认为误导；R1 rebut（footnote + Appendix Δρ<0.01 + 先例）。非共识问题。\n\n---\n\n## Questions for Authors\n\nQ1. [Both] Table 2 Random (0.610) vs Single (0.645): 精确计算公式？3.5pp 系统性差距来源？\nQ2. [Both] Instance degeneracy 是否对 fine-tuning recipe 敏感（LoRA rank、epochs、dropout、load_best_model_at_end）？\nQ3. [R1] 是否有其他 medium-difficulty NER 数据集上的初步结果？\nQ4. [R2, R1 AGREE] Free-form decoding 下 constant-F1 fraction 是否改变？\nQ5. [R1] Hybrid 策略（degenerate→greedy, non-degenerate→MBR）的 expected gain？\nQ6. [R1] Entity-token LP 的 within-instance ρ（F1）是多少？增加的 variance 是 noise 还是 signal？\nQ7. [R2, R1 AGREE] Greedy (T=0) vs Single (T=1.0) 是否经过 significance test？\n\n---\n\n## Missing References\n\n1. Gao et al. (2023) \"Scaling laws for reward model overoptimization\" — best-of-N proxy signal limitation 的概念联系（R2 提出，R1 PARTIALLY AGREE: 相关性有限，可在 Discussion 提及）\n2. Deutsch et al. (2022) \"Training and meta-evaluating machine translation evaluation metrics at the paragraph level\" — MBR with structural metrics（R1 提出）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Overall Assessment\n\n**Score: borderline**\n**Confidence: 4/5**\n**推荐 Track: Findings**\n\n两位 Reviewer 独立评分均为 3.0/5。论文提出了有价值的概念贡献（QE vs selection 解耦）并提供了深入的诊断分析。Within-instance analysis（MBR utility aligned but headroom vanishing）是最强贡献，与 Eikema et al. (2025) 的 MBR utility mismatch 有 qualitative 区别。\n\n但四个 Must-Fix 问题限制了当前版本的可接受性：\n1. **Framing inflation**: \"5 signals all fail\" 将 definitional limitation 包装为 empirical discovery（持续 13 轮未完全解决）\n2. **Single-dataset support**: 核心 claim 仅在 SciERC (n=529) 上有效验证（持续 15 轮）\n3. **Unexplained baseline**: Random vs Single 3.5pp 差距影响 baseline 解读\n4. **Statistical power**: 2-seed Fisher p 不足以支撑核心 negative result\n\n**Findings track 路径**: 解决 MF1（framing 重构）、MF3（Random vs Single 解释）、SF1-SF8 中的写作修正即可满足 Findings track 要求。\n\n**Main conference 路径**: 在 Findings 路径基础上，还需 MF2（增加数据集或进一步限定 scope）和 MF4（statistical power 加强）。\n\n---\n\n## Detailed Comments (Section-by-Section)\n\n### Abstract\n- 信息密度仍高——5 信号、3 数据集、degeneracy%、LP nats、5-layer ablation 均出现\n- ρ=0.45 来自 ceiling-effect control，可能给 \"moderate-to-strong\" 错觉\n- \"Five confidence signals\" 统一叙事需拆分\n- \"Within a narrow model-scale range (4B-8B)\" 良好限定\n\n### Introduction (§1)\n- Contribution #1 混合 definitional 和 empirical failure——需重构\n- Figure 1 + operationalization 有效\n- 已正确识别 instance-level vs per-sample 区分但未贯彻到 contribution list\n\n### Related Work (§2)\n- 覆盖全面（self-consistency, MBR, uncertainty, calibration）\n- Schall et al., Yun et al., Park et al., Eikema et al. 均已引用\n- 缺少: Yao et al. hard-prompted vs fine-tuned degeneracy 对比\n- 缺少: Yun et al. diversity collapse 与 instance degeneracy 的显式联系\n\n### Method (§3)\n- 信号定义数学严谨，evaluation framework 清晰\n- §3.1 有关键区分但需向前传递\n\n### Experiments (§4)\n- Table 1 QE 结果呈现清晰\n- Table 2 Selection 结果是核心但 Random vs Single 差距需解释\n- §4.3 \"all p>0.05\" 叙事应转向 effect size\n- Table 4 Degeneracy: 含 4B data，within-instance analysis 是最强部分\n\n### Discussion (§5)\n- Instance degeneracy mechanism 论证充分（MBR + within-instance ρ）\n- LP compression 诊断系统（四个 hypotheses, constraint-imposed vs model-learned）\n- \"Intrinsic\" 用语需 scope 限定\n- Signal combinations: LP×VC 三策略 + oracle tiebreaker +7.9pp 是重要 calibration\n\n### Conclusion (§6)\n- 准确总结但继承 framing 问题\n- 70B+ open question 恰当\n\n### Limitations\n- 全面诚实\n- 应增加 fine-tuning recipe confound acknowledgment\n\n### Ethics Statement\n- 对论文 scope 而言充分\n\n### 格式合规\n- ACL review template ✓, Anonymous ✓, Limitations ✓, Ethics ✓\n- 引用: 53 entries, 0 orphan, 44 verified（R2 审核）\n- 正文页数需编译确认",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 1492 · 2026-05-16T08:58:58.915542+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4320
}
```

</details>

---


### Assistant

_source line 1493 · 2026-05-16T08:59:11.865013+00:00_

审稿完成。

**Round 15 审稿报告已投递至 Research Director。**

核心结论：

- **Overall: borderline (3.0/5)，推荐 Findings track**
- 两位 Reviewer 独立评分一致，交叉回应后关键问题全部达成共识（1 轮收敛）

**4 个 Must-Fix**:
1. Framing conflation — "5 signals all fail" 混淆 definitional limitation 与 empirical finding（持续 13 轮未解决）
2. 核心 claim 仅 SciERC (n=529) 单数据集支撑（持续 15 轮）
3. Table 2 Random vs Single 3.5pp 差距未解释（本轮从 info 升级为 critical）
4. 2-seed Fisher combined p 统计效力不足（severity 分歧: R1 critical / R2 should-fix）

**8 个 Should-Fix**: fine-tuning recipe artifact、Yao et al. positioning、greedy 修辞、Bonferroni scope、Kendall's W caveat、scale range "intrinsic" claim、TOST configuration-dependence、abstract ρ=0.45 headline

Issue tracker 已同步更新至 Round 15（含 1 个新 issue R15-N1、1 个 resolved R14-N2、多项 in-progress 状态更新）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1494 · 2026-05-16T08:59:14.509540+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。

逐条回应了 R2 的所有 Must-Fix (N1-N3)、Should-Fix (W1-W6)、小问题和 Questions：
- **N1 (framing conflation)**: AGREE，与我的 R1-N2 一致
- **N2 (degeneracy novelty)**: PARTIALLY AGREE — within-instance analysis 有新颖性，但 fine-tuning recipe artifact 未排除是有效批评
- **N3 (Random vs Single 3.5pp)**: AGREE，我遗漏的重要问题，期望值应相同但差距系统性存在
- **W2 (Soft Jaccard naming)**: REBUT — 公式已明确，Appendix Table 10 验证了 normalizer robustness
- 其余 W1/W3-W6 和小问题基本 AGREE

两份审稿的交叉对照表总结了共识和互补发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1495 · 2026-05-16T08:59:31.838230+00:00_

审稿报告已投递至 Research Director。

**Round 15 审稿完成，汇报如下：**

---

**评分**: borderline (3.0/5)，两位 Reviewer 独立评分一致，推荐 **Findings track**。

**4 个 Must-Fix（强共识）**：
1. **Framing conflation**（持续 13 轮）："5 signals all fail" 将 instance-level by-construction limitation 与 LP compression empirical finding 混为一谈，需拆分三层叙事
2. **单数据集支撑**（持续 15 轮）：核心 claim 仅在 SciERC (n=529) 上有效验证
3. **Random vs Single 3.5pp 差距未解释**：E[Random]=E[Single] 但存在系统性偏差，影响 baseline 解读
4. **2-seed 统计效力不足**：核心 negative result 应依赖 effect size (d=0.038) + 多重证据链，而非 p>0.05

**8 个 Should-Fix**：fine-tuning recipe artifact 未排除、Yao et al. hard-prompted degeneracy 未讨论、greedy 修辞过强、Bonferroni scope 不完整、Kendall's W caveat 缺失、"intrinsic" claim 需限定、TOST configuration-dependence 未充分呈现、Abstract ρ=0.45 headline 来源。

**最强贡献**：within-instance analysis（MBR utility aligned ρ=0.52 但 headroom vanishing，区别于 Eikema et al. 2025 的 utility mismatch）。

Issue tracker 已同步更新至 Round 15。报告已投递 Research Director，审稿阶段结束。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 124

## Round 124

56 recorded events


### User

_source line 1496 · 2026-05-17T06:12:35.038510+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1497 · 2026-05-17T06:12:41.353459+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1498 · 2026-05-17T06:12:41.354373+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1499 · 2026-05-17T06:12:45.520318+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1500 · 2026-05-17T06:12:45.570981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1501 · 2026-05-17T06:12:49.484828+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1502 · 2026-05-17T06:12:50.589391+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (120 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_027_fewnerd_n16** (success): LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\n- **exp_016_rerun_1024_bootstrap** (negative): 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant. ← 基于 exp_016_rerun_1024\n  [fig_selection_gap_1024](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf)\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \"score compression is general\" claim. If effective → important positive finding requiring narrative adjustment. ← 基于 exp_012_rerun_1024\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\n\n## 趋势\n成功 70 / 负向 24 / 失败 4 / 共 120\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 1503 · 2026-05-17T06:12:50.589878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1504 · 2026-05-17T06:12:50.640447+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Fail to Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, Qwen3-4B, LLaMA-3.1-8B).
41	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	Code and data will be released upon acceptance at [anonymized URL].
45	
46	\bibliography{references}
47	
48	\appendix
49	\input{sections/appendix}
50	
51	\end{document}
52	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1505 · 2026-05-17T06:12:56.831029+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_local_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1506 · 2026-05-17T06:12:56.881640+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1507 · 2026-05-17T06:13:00.645744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-17T06:13:01.047649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-17T06:13:01.462173+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and the primary test bed; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to structural selection---the \textit{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{=}0$) despite 12--14~pp oracle headroom.
6	We diagnose two mechanisms: (a)~\textit{instance degeneracy}---fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom; and (b)~\textit{log-probability compression}---median within-instance range of 0.041 nats.
7	LP selection effectiveness is inversely predicted by degeneracy: at 10\% degeneracy (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
8	Structural signals fail uniformly regardless of degeneracy, confirming the gap is persistent for consensus-based methods.
9	Closing the structural gap likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 414
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-17T06:13:01.462447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-17T06:13:01.512850+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---majority voting over multiple samples---yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
8	\citet{yao2026consistency} examine consistency--accuracy correlations for LLM-based IE using exact-match agreement under hard-prompting; we extend their work to fine-tuned models, separating quality estimation from best-of-$N$ selection and diagnosing why the former succeeds while the latter fails---within the dominant deployment paradigm for production NER.
9	
10	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
11	These signals achieve reliable quality estimation ($\rho$ up to 0.42 on the primary test bed and Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap}: structural best-of-$N$ selection matches or degrades greedy decoding ($T{
…[truncated 3201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1512 · 2026-05-17T06:13:09.291332+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the web search results, here's the information about EMNLP 2026 call for papers:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## Important Dates

Key dates include:
- Reviewer registration deadline for all authors: May 27, 2026
- Author response and author-reviewer discussion: July 7-13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 20
…[truncated 1207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8645
}
```

</details>

---


### Tool call

_source line 1513 · 2026-05-17T06:13:15.765244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"
  }
}
```

</details>

---


### Tool call

_source line 1514 · 2026-05-17T06:13:16.267334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1515 · 2026-05-17T06:13:16.619061+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
6	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
7	This distinction is consequential for selection: in our study, 4 of 5 signals are instance-level aggregates that assign identical QE scores to all $N$ candidates. Consensus-proximity (MBR) converts these to per-sample rankings (\S\ref{sec:selection_gap}), but these rankings do not improve selection; only natively per-sample signals can, in principle, exploit oracle headroom.
8	
9	\subsection{Confidence Signals}\label{sec:signals}
10	
11	Four are \textit{consistency signals}: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]); log-probability [LP] is the sole \textit{model-internal}, per-sample signal.
12	
13	\paragraph{Log-probability (model-internal, per-sample).}
14	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
15	\begin{equation}\label{eq:logprob}
16	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
17	\end{equation}
18	
19	\paragraph{Exact match voting (surface, instance-level).}
20	The proportion of samples producing the most common output:
21	\begin{equation}\label{eq:em}
22	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
23	\end{equation}
24	
25	\paragraph{Fleiss' $\kappa$ (surface, instance-level).}
26	We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary pres
…[truncated 3479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 1516 · 2026-05-17T06:13:16.669651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1517 · 2026-05-17T06:13:16.720589+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 52\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures.
16	Qwen3-8B's SciERC checkpoint has a minor train--test mismatch (empty thinking tokens); a quantitative analysis rules out this confound (Appendix~\ref{app:thinking_token}).
17	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ with 3 seeds verifies scaling and ranking stability ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}); gains beyond $N{=}8$ are sublinear (Appendix~\ref{app:n_scaling}).}
18	Inference uses vLLM with constrained decoding \cite{willard2023guided}.\footnote{Quality estimation uses a single primary seed (seed${=}42$); selection uses 2-seed averages for variance estimation. Three-seed experiments ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}) confirm ranking stability; the reduced seed c
…[truncated 16434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1518 · 2026-05-17T06:13:31.382667+00:00_

Web search results for query: "ACL Rolling Review 2026 submission format page limit long paper short paper guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here is the information about ACL Rolling Review 2026 submission format, page limits, and guidelines:

## Paper Types and Page Limits

ACL Rolling Review invites the submission of long and short papers on substantial, original, and unpublished research in all aspects of Computational Linguistics and Natural Language Processing.

**Long Papers:** Review versions of long pap
…[truncated 1246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 15617
}
```

</details>

---


### Tool call

_source line 1519 · 2026-05-17T06:13:36.249386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1520 · 2026-05-17T06:13:37.153254+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	For quality estimation, all signals achieve positive $\rho$ across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL).
5	Rankings hold across model families and a 4B ablation (Table~\ref{tab:scale_ablation}); at the capability boundary (WNUT-17), all signals collapse.
6	For selection, LP is the only signal achieving significant gains, and only at low degeneracy: $+1.36$~pp on Few-NERD (10\% degeneracy, $p{<}0.001$), $+0.42$~pp on SciERC (21\%, $p{=}0.091$), failure on CoNLL (58\%).
7	Structural signals uniformly degrade selection regardless of dataset.
8	RE signal rankings are reported in Appendix~\ref{app:re_extension}.
9	
10	\paragraph{Why the gap exists.}
11	We identify two mechanisms: \textit{instance degeneracy} (affecting consensus-proximity selection) and \textit{LP compression} (affecting per-sample selection).
12	
13	Within-instance analysis (restricted to non-degenerate instances where F1 varies across samples) reveals that MBR utility \cite{eikema2022sampling} does correlate positively with F1 (SJ median within-instance $\rho{=}0.524$ on SciERC, $0.994$ on CoNLL), and on these instances consensus-proximity selection closes 23\% (SciERC) to 41\% (CoNLL) of the oracle gap.
14	However, fine-tuned models exhibit pervasive \textit{instance degeneracy}: 21\% of SciERC instances (58\% on CoNLL) produce identical F1 across all $N$ samples, offering zero selection headroom; an additional 13\% (49\% on CoNLL) yield constant utility scores, preventing MBR ranking entirely (Table~\ref{tab:degeneracy}).
15	Instance degeneracy is not an artifact of our setup but a consequence of model capability: the better the model, the less room for selection to add value.
16	CoNLL (91\% single-sample F1) exhibits 58\% degeneracy; Few-NERD (75\%) shows 10\%; SciERC (66\%) shows 21\%; WNUT-17 (${\approx}$42\%, macro) shows near-zer
…[truncated 14593 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1521 · 2026-05-17T06:13:37.304207+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1522 · 2026-05-17T06:13:37.354893+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} study consistency--accuracy correlations for LLM-based NER/RE under hard-prompting, leaving open whether structural matching improves on surface agreement, whether quality estimation translates to selection, and whether findings generalize across a difficulty gradient---the three questions we address.
11	Our experiments use fine-tuned models---the dominant deployment paradigm for production NER---where instance degeneracy is most pronounced.
12	Degeneracy varies across datasets: CoNLL (91\% single-sample F1) exhibits 58\%; SciERC (66\%) shows 21\%; Few-NERD (75\%) shows 10\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
13	Few-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.
14	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/sum
…[truncated 4262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1523 · 2026-05-17T06:13:37.355312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1524 · 2026-05-17T06:13:37.405765+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.42 on Few-NERD and SciERC; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to structural selection: despite 12--14~pp oracle headroom, no structural signal significantly outperforms greedy decoding on any dataset.
6	The gap stems from two jointly operating mechanisms: instance degeneracy (10--58\% of instances produce identical F1 across all $N$ samples) and LP compression (median within-instance range of 0.041 nats).
7	Instance degeneracy monotonically predicts LP selection effectiveness across three datasets: at 10\% degeneracy (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals (logistic regression, MLP, random forest) cannot close the oracle gap, confirming the bottleneck is in the structural feature space.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the structural gap requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline at low degeneracy.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1525 · 2026-05-17T06:13:43.479704+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1526 · 2026-05-17T06:13:43.480058+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B--8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested---larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression---entity-token-only LP (excluding format/schema tokens)---which fails to improve selection
…[truncated 206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1527 · 2026-05-17T06:13:43.832291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1528 · 2026-05-17T06:13:43.933290+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality---including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & 
…[truncated 9116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1529 · 2026-05-17T06:13:58.441418+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "literature_map.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1530 · 2026-05-17T06:14:00.097763+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: 
…[truncated 3614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1656
}
```

</details>

---


### Tool call

_source line 1531 · 2026-05-17T06:14:00.248816+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 1532 · 2026-05-17T06:14:00.249215+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1533 · 2026-05-17T06:14:05.691345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1534 · 2026-05-17T06:14:06.495603+00:00_

&lt;persisted-output>
Output too large (33.7KB). Full output saved to: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt

Preview (first 2KB):
issues:
# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====
- id: R0-C1
  summary: "模型规模单一（仅 8B）"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 Reviewer 确认措辞修正到位"
  resolution_round: 2
- id: R0-C2
  summary: "相关工作显著遗漏"
  category: framing
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 确认 49 条 bib 全部 cited"
  resolution_round: 2
- id: R0-C4
  summary: "SJ 方法新颖性有限"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 确认三点差异化清晰"
  resolution_round: 2
- id: R0-C5
  summary: "全文零图表"
  category: writing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "论文已包含 6 个 figures"
  resolution_round: 1
- id: R0-C6
  summary: "成本分析 negligible 误导"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "Round 1+ 未再提及"
  resolution_round: 1
- id: R0-W1
  summary: "未探索 signal combination"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: "Round 1+ 未再提及"
  resolution_round: 1
- id: R0-W4
  summary: "统计检验不系统"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 1
  resolution: "Round 2 Reviewer 评价 bootstrap 达到高标准"
  resolution_round: 2
- id: R3-W4
  summary: "FK independence 假设未验证"
  category: experiment
  severity: warning
  status: resolved
  first_raised_round: 3
  last_seen_round: 8
  resolution: "Appendix instance-level pe
…[truncated 333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 804
}
```

</details>

---


### Tool call

_source line 1535 · 2026-05-17T06:14:06.495979+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/config.yaml 2>/dev/null | grep -A 10 \"external_review\" || echo \"NO_EXTERNAL_REVIEW_CONFIG\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1536 · 2026-05-17T06:14:06.546402+00:00_

NO_EXTERNAL_REVIEW_CONFIG

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1537 · 2026-05-17T06:14:10.861262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
  "limit": "200",
  "offset": "70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
    "limit": "200",
    "offset": "70"
  }
}
```

</details>

---


### Tool result

_source line 1538 · 2026-05-17T06:14:10.911938+00:00_

70	  status: resolved
71	  first_raised_round: 3
72	  last_seen_round: 8
73	  resolution: "Appendix instance-level permutation test (n=529-2756, p<0.001) 验证"
74	  resolution_round: 9
75	- id: R3-W5
76	  summary: "Cross-model scope 过宽"
77	  category: framing
78	  severity: warning
79	  status: resolved
80	  first_raised_round: 3
81	  last_seen_round: 5
82	  resolution: "标题改为当前版本，scope 限定"
83	  resolution_round: 9
84	- id: R4-W3
85	  summary: "Abstract 信息密度过高"
86	  category: writing
87	  severity: warning
88	  status: resolved
89	  first_raised_round: 4
90	  last_seen_round: 8
91	  resolution: "Abstract 压缩为 problem-finding-significance 结构"
92	  resolution_round: 9
93	- id: R5-N1
94	  summary: "贡献框架偏 incremental"
95	  category: framing
96	  severity: warning
97	  status: resolved
98	  first_raised_round: 5
99	  last_seen_round: 5
100	  resolution: "贡献重新框架化为 finding-led"
101	  resolution_round: 9
102	- id: R7-W1
103	  summary: "LP temperature 依赖未说明"
104	  category: experiment
105	  severity: warning
106	  status: resolved
107	  first_raised_round: 7
108	  last_seen_round: 7
109	  resolution: "Appendix 排除 LP + Limitations 扩展说明"
110	  resolution_round: 9
111	- id: R7-W3
112	  summary: "Eikema Related Work 覆盖不足"
113	  category: writing
114	  severity: warning
115	  status: resolved
116	  first_raised_round: 7
117	  last_seen_round: 7
118	  resolution: "Related Work 增加 Eikema 讨论"
119	  resolution_round: 9
120	- id: R8-N1
121	  summary: "页数超限"
122	  category: writing
123	  severity: warning
124	  status: resolved
125	  first_raised_round: 8
126	  last_seen_round: 8
127	  resolution: "主文在限制内"
128	  resolution_round: 9
129	- id: R8-W2
130	  summary: "Thinking token 对 LP 影响未分析"
131	  category: experiment
132	  severity: warning
133	  status: resolved
134	  first_raised_round: 8
135	  last_seen_round: 8
136	  resolution: "Appendix 3-part quantitative analysis 已补充"
137	  resolution_round: 9
138	- id: R8-W3
139	  summary: "SJ normalizer 选择敏感性"
140	  category: method
141	  severity
…[truncated 3811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1539 · 2026-05-17T06:14:15.127813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
  "limit": "300",
  "offset": "265"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
    "limit": "300",
    "offset": "265"
  }
}
```

</details>

---


### Tool result

_source line 1540 · 2026-05-17T06:14:15.128353+00:00_

265	  summary: "缺少 greedy decoding baseline"
266	  category: experiment
267	  severity: warning
268	  status: resolved
269	  first_raised_round: 11
270	  last_seen_round: 14
271	  resolution: "Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2."
272	  resolution_round: 14
273	- id: R12-M1
274	  summary: "Discussion LP hypotheses 标注 three mechanisms 但实际列出四个"
275	  category: writing
276	  severity: info
277	  status: resolved
278	  first_raised_round: 12
279	  last_seen_round: 14
280	  resolution: "论文已修正为 'four (non-mutually-exclusive) mechanisms'"
281	  resolution_round: 14
282	- id: R12-M3
283	  summary: "oh2025latentsc bib year 应更新为 2026"
284	  category: writing
285	  severity: info
286	  status: resolved
287	  first_raised_round: 12
288	  last_seen_round: 14
289	  resolution: "R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)"
290	  resolution_round: 14
291	- id: R13-W1
292	  summary: "RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark"
293	  category: experiment
294	  severity: warning
295	  status: resolved
296	  first_raised_round: 13
297	  last_seen_round: 14
298	  resolution: "RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER."
299	  resolution_round: 14
300	- id: R13-M1
301	  summary: "Bib 年份/作者问题"
302	  category: writing
303	  severity: info
304	  status: resolved
305	  first_raised_round: 13
306	  last_seen_round: 14
307	  resolution: "R14 审核确认主要 bib entries 正确"
308	  resolution_round: 14
309	- id: R14-N2
310	  summary: "缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)"
311	  category: writing
312	  severity: warning
313	  status: resolved
314	  first_raised_round: 14
315	  last_seen_round: 15
316	  resolution: "R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work."
317	  resolution_round: 15
318	
319	# ===== RECURRING ISSUES (updated Round 15) =====
320	- id: R0-C3
321	  summary: "Selection gap effective test bed 仅 SciERC 单数据集"
322	  category: experiment
323	  severity: critical
324	  status: in_progress
32
…[truncated 8676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1541 · 2026-05-17T06:14:22.853613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
  "limit": "300",
  "offset": "560"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
    "limit": "300",
    "offset": "560"
  }
}
```

</details>

---


### Tool result

_source line 1542 · 2026-05-17T06:14:22.854090+00:00_

560	    note: "constraint-imposed vs model-learned 区分 sound."
561	  - round: 15
562	    reviewers: []
563	    note: "R15 未被独立提及. 论文已有 (a)-(d) 四个 hypotheses, constraint-imposed vs model-learned 区分明确."
564	  action_items:
565	  - round: 14
566	    action: "(b) 和 (d) 之间添加一句显式说明 constraint-imposed vs model-learned 的区别."
567	    assigned_to: Paper Agent
568	    status: in_progress
569	  resolution: ""
570	  resolution_round: null
571	
572	- id: R11-W8
573	  summary: "Thinking token CoNLL control 论证薄弱"
574	  category: experiment
575	  severity: info
576	  status: in_progress
577	  first_raised_round: 11
578	  last_seen_round: 11
579	  mentions:
580	  - round: 15
581	    reviewers: []
582	    note: "R15 未被独立提及."
583	  action_items:
584	  - round: 11
585	    action: "弱化 CoNLL control 论证或补充 task easiness 混淆说明"
586	    assigned_to: Paper Agent
587	    status: in_progress
588	  resolution: ""
589	  resolution_round: null
590	
591	- id: R11-M1
592	  summary: "Selection table NER 2-seed vs RE single seed 未说明原因"
593	  category: writing
594	  severity: warning
595	  status: in_progress
596	  first_raised_round: 11
597	  last_seen_round: 12
598	  mentions:
599	  - round: 15
600	    reviewers: []
601	    note: "R15 未被独立提及. RE 已移至 Appendix."
602	  action_items:
603	  - round: 12
604	    action: "在 footnote 解释 NER/RE seed 数量不对称原因"
605	    assigned_to: Paper Agent
606	    status: in_progress
607	  resolution: ""
608	  resolution_round: null
609	
610	- id: R11-M2
611	  summary: "Figure 1 caption 对 LP per-sample signal 不适用"
612	  category: writing
613	  severity: info
614	  status: in_progress
615	  first_raised_round: 11
616	  last_seen_round: 11
617	  mentions:
618	  - round: 15
619	    reviewers: []
620	    note: "R15 未被独立提及."
621	  action_items:
622	  - round: 11
623	    action: "修改 Figure 1 caption"
624	    assigned_to: Paper Agent
625	    status: in_progress
626	  resolution: ""
627	  resolution_round: null
628	
629	- id: R11-N3
630	  summary: "Abstract LP compression intrinsic 措辞被
…[truncated 7975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1543 · 2026-05-17T06:14:31.700371+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
  "limit": "200",
  "offset": "850"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
    "limit": "200",
    "offset": "850"
  }
}
```

</details>

---


### Tool result

_source line 1544 · 2026-05-17T06:14:31.801300+00:00_

850	  resolution_round: null
851	
852	- id: R14-W2
853	  summary: "Greedy (T=0) vs sampling+selection 比较修辞过强"
854	  category: writing
855	  severity: warning
856	  status: in_progress
857	  first_raised_round: 14
858	  last_seen_round: 15
859	  mentions:
860	  - round: 14
861	    reviewers: [1, 2]
862	    note: "greedy 应定位为 practical cost-free alternative."
863	  - round: 15
864	    reviewers: [1, 2]
865	    note: "R15: R2-W5 + R1 AGREE. 'surpassing all N=8 selection strategies' 仍过强. Greedy vs Single 1.8pp 未 significance-tested. 如不显著, 结论应为 'Greedy ≈ Single > all selection'."
866	  action_items:
867	  - round: 14
868	    action: "'surpassing' 改为 'practical cost-free alternative'."
869	    assigned_to: Paper Agent
870	    status: in_progress
871	  - round: 15
872	    action: "测试 Greedy vs Single 显著性. 修辞改为 'selection adds no benefit over greedy or single-sample'. 明确 sampling 价值在 QE 而非 selection."
873	    assigned_to: Paper Agent
874	    status: in_progress
875	  resolution: ""
876	  resolution_round: null
877	
878	- id: R14-W3
879	  summary: "4B scale ablation 缺少 instance degeneracy 统计"
880	  category: experiment
881	  severity: warning
882	  status: in_progress
883	  first_raised_round: 14
884	  last_seen_round: 15
885	  mentions:
886	  - round: 14
887	    reviewers: [1, 2]
888	    note: "4B constant F1 fraction 和 oracle headroom 未报告."
889	  - round: 15
890	    reviewers: [1, 2]
891	    note: "R15: Table 6 已包含 4B data (constant F1 10.4%, constant utility 7.0%, within-inst ρ 0.550, oracle gap closed 25.2%). 数据问题已解决. 但新 concern: 8B/4B degeneracy 差异可能反映 fine-tuning recipe artifact (same epochs, larger model overfits faster) 而非 capability. 见 R15-N1."
892	  action_items:
893	  - round: 14
894	    action: "报告 4B 的 degeneracy 统计."
895	    assigned_to: "Main Agent (data) + Paper Agent (writing)"
896	    status: done
897	  - round: 15
898	    action: "解释 8B vs 4B degeneracy 差异是 capability-driven 还是 recipe artifact. 见 R15-N1."
899	    assigned_to: Paper Agent
900	    status: in
…[truncated 4705 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1545 · 2026-05-17T06:14:35.866244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
  "limit": "100",
  "offset": "1045"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-director-0161122b/e846db28-54f4-424c-9d4a-edbb033c7d37/tool-results/b2wro9v68.txt",
    "limit": "100",
    "offset": "1045"
  }
}
```

</details>

---


### Tool result

_source line 1546 · 2026-05-17T06:14:35.866606+00:00_

1045	
1046	- id: R15-W1
1047	  summary: "TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful"
1048	  category: experiment
1049	  severity: warning
1050	  status: open
1051	  first_raised_round: 15
1052	  last_seen_round: 15
1053	  mentions:
1054	  - round: 15
1055	    reviewers: [1, 2]
1056	    note: "R1-W5 + R2 AGREE. LLaMA-CoNLL: robust pass. Qwen-CoNLL: all external δ FAIL (selection degrades 0.9-1.5pp). SciERC: only SJ at widest δ. 'Selection actively harmful' 比 'no benefit' 更强, 但被埋在 Appendix."
1057	  action_items:
1058	  - round: 15
1059	    action: "Main text Section 4.3 需更平衡呈现 TOST 结果: 某些配置下信号 actively harm selection, 非仅 'no benefit'."
1060	    assigned_to: Paper Agent
1061	    status: open
1062	  resolution: ""
1063	  resolution_round: null

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1547 · 2026-05-17T06:15:29.748014+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "16",
  "text": "## Round 16 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 正文 ≤8 页, double-blind, Limitations section 必须\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n\n### 你的审查侧重\n\n1. **统计方法论**:\n   - Table 2 selection results 使用 2-seed paired sign test, Fisher combined p. 评估统计效力是否足够支撑结论\n   - Bonferroni correction scope: footnote 4 声称 \"survives Bonferroni over 5 comparisons\" 但 ε threshold 是 post-hoc 选择（7ε×5=35 comparisons）\n   - Random baseline (0.610) vs Single/Greedy (0.645) 的 3.5pp 差距是否合理（E[Random] 理论上应 = E[Single] under same T）\n   - Kendall's W=1.0 with only 3 seeds — precision caveat 是否充分\n\n2. **实验设计**:\n   - Instance degeneracy 8B(21%) vs 4B(10.4%) 差异: capability-driven 还是 fine-tuning recipe artifact (same epochs, larger model overfits faster)?\n   - LoRA rank ablation (rank=8 vs 32): degeneracy 7%→21%, 但 selection 仍失败. 是否足以区分 degeneracy 和 LP compression 的独立贡献?\n   - Gold-empty instance filtering: QE 和 Selection 用 n=529 from 551, n=2756 from 3453. 一致性是否 OK?\n\n3. **核心 claim 的证据链**:\n   - \"Correlation-selection gap\": 13pp oracle headroom 下所有信号 ≈ greedy. 证据链是否完整?\n   - Degeneracy-gating pattern (58%→fail, 21%→+0.42pp, 10%→+1.36pp): 仅 3 个数据点的 monotonic pattern, 是否过度解读?\n   - TOST 等价性: configuration-dependent (LLaMA-CoNLL pass, Qwen-CoNLL fail). 主文是否平衡呈现?\n\n4. **再现性**:\n   - Qwen3-8B SciERC checkpoint 有 empty thinking tokens. Appendix 3-part analysis 是否充分排除 confound?\n   - vLLM + constrained decoding pipeline 的细节是否足够再现?\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，格式: Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (score + confidence)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "16",
    "text": "## Round 16 审稿任务 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 正文 ≤8 页, double-blind, Limitations section 必须\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n\n### 你的审查侧重\n\n1. **统计方法论**:\n   - Table 2 selection results 使用 2-seed paired sign test, Fisher combined p. 评估统计效力是否足够支撑结论\n   - Bonferroni correction scope: footnote 4 声称 \"survives Bonferroni over 5 comparisons\" 但 ε threshold 是 post-hoc 选择（7ε×5=35 comparisons）\n   - Random baseline (0.610) vs Single/Greedy (0.645) 的 3.5pp 差距是否合理（E[Random] 理论上应 = E[Single] under same T）\n   - Kendall's W=1.0 with only 3 seeds — precision caveat 是否充分\n\n2. **实验设计**:\n   - Instance degeneracy 8B(21%) vs 4B(10.4%) 差异: capability-driven 还是 fine-tuning recipe artifact (same epochs, larger model overfits faster)?\n   - LoRA rank ablation (rank=8 vs 32): degeneracy 7%→21%, 但 selection 仍失败. 是否足以区分 degeneracy 和 LP compression 的独立贡献?\n   - Gold-empty instance filtering: QE 和 Selection 用 n=529 from 551, n=2756 from 3453. 一致性是否 OK?\n\n3. **核心 claim 的证据链**:\n   - \"Correlation-selection gap\": 13pp oracle headroom 下所有信号 ≈ greedy. 证据链是否完整?\n   - Degeneracy-gating pattern (58%→fail, 21%→+0.42pp, 10%→+1.36pp): 仅 3 个数据点的 monotonic pattern, 是否过度解读?\n   - TOST 等价性: configuration-dependent (LLaMA-CoNLL pass, Qwen-CoNLL fail). 主文是否平衡呈现?\n\n4. **再现性**:\n   - Qwen3-8B SciERC checkpoint 有 empty thinking tokens. Appendix 3-part analysis 是否充分排除 confound?\n   - vLLM + constrained decoding pipeline 的细节是否足够再现?\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，格式: Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (score + confidence)."
  }
}
```

</details>

---


### Tool result

_source line 1548 · 2026-05-17T06:15:48.825116+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19077
}
```

</details>

---


### Tool call

_source line 1549 · 2026-05-17T06:15:48.976020+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "16",
  "text": "## Round 16 审稿任务 — Reviewer 2（新颖性 + 贡献定位 + 相关工作 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 正文 ≤8 页, double-blind, Limitations section 必须\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n\n### 你的审查侧重\n\n1. **新颖性与贡献定位**:\n   - 核心 finding \"correlation-selection gap\" 的新颖性评估: 与 MBR 社区已知结论 (Eikema et al. 2025, Deguchi et al. 2024) 的关系\n   - Contribution 列表是否清晰区分 definitional limitation (instance-level signals by construction 无法 rank candidates) vs empirical finding (MBR with ρ=0.52 仍失败因为 degeneracy)\n   - 与 Yao et al. (2026) 的增量: 本文 = fine-tuned models + selection analysis + degeneracy diagnosis. 差异化是否充分?\n   - \"Strong Predictors, Weak Selectors\" 标题暗示的叙事是否有 tautological 成分?\n\n2. **相关工作覆盖**:\n   - 检查是否有重要遗漏（特别是 2025-2026 年 NER + self-consistency + MBR + uncertainty estimation 方向）\n   - 引用密度是否达到 EMNLP 标准（当前 ~55 papers）\n   - Related Work 的 positioning 是否准确（不是 survey，而是定位自身）\n\n3. **写作质量**:\n   - Abstract 信息密度评估: 9 句覆盖 5 信号、3 数据集、degeneracy%、LP nats 等. 是否过载?\n   - Introduction 叙事线: problem → insight → method → evidence 是否连贯?\n   - 术语一致性: \"correlation-selection gap\" 操作性定义的位置和清晰度\n   - AI 写作痕迹检查: em-dash, -ing phrases, 过度分段, 用词黑名单\n   - Soft Jaccard 命名准确性（分母 max 非 union）\n\n4. **完整性**:\n   - 论文 scope 是否与证据匹配（NER-focused 但有 RE exploratory extension）\n   - scale range (3B-8B) claims 是否适当限定\n   - ρ=0.42 headline 是否从最有利的 dataset 而非 primary test bed 报告\n   - Few-NERD LP +1.36pp 作为 positive finding 的呈现是否平衡（也是 N=8, single model）\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，格式: Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (score + confidence)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "16",
    "text": "## Round 16 审稿任务 — Reviewer 2（新颖性 + 贡献定位 + 相关工作 + 写作质量）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 正文 ≤8 页, double-blind, Limitations section 必须\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n\n### 你的审查侧重\n\n1. **新颖性与贡献定位**:\n   - 核心 finding \"correlation-selection gap\" 的新颖性评估: 与 MBR 社区已知结论 (Eikema et al. 2025, Deguchi et al. 2024) 的关系\n   - Contribution 列表是否清晰区分 definitional limitation (instance-level signals by construction 无法 rank candidates) vs empirical finding (MBR with ρ=0.52 仍失败因为 degeneracy)\n   - 与 Yao et al. (2026) 的增量: 本文 = fine-tuned models + selection analysis + degeneracy diagnosis. 差异化是否充分?\n   - \"Strong Predictors, Weak Selectors\" 标题暗示的叙事是否有 tautological 成分?\n\n2. **相关工作覆盖**:\n   - 检查是否有重要遗漏（特别是 2025-2026 年 NER + self-consistency + MBR + uncertainty estimation 方向）\n   - 引用密度是否达到 EMNLP 标准（当前 ~55 papers）\n   - Related Work 的 positioning 是否准确（不是 survey，而是定位自身）\n\n3. **写作质量**:\n   - Abstract 信息密度评估: 9 句覆盖 5 信号、3 数据集、degeneracy%、LP nats 等. 是否过载?\n   - Introduction 叙事线: problem → insight → method → evidence 是否连贯?\n   - 术语一致性: \"correlation-selection gap\" 操作性定义的位置和清晰度\n   - AI 写作痕迹检查: em-dash, -ing phrases, 过度分段, 用词黑名单\n   - Soft Jaccard 命名准确性（分母 max 非 union）\n\n4. **完整性**:\n   - 论文 scope 是否与证据匹配（NER-focused 但有 RE exploratory extension）\n   - scale range (3B-8B) claims 是否适当限定\n   - ρ=0.42 headline 是否从最有利的 dataset 而非 primary test bed 报告\n   - Few-NERD LP +1.36pp 作为 positive finding 的呈现是否平衡（也是 N=8, single model）\n\n请按 ACL/ARR 审稿标准输出完整审稿报告，格式: Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment (score + confidence)."
  }
}
```

</details>

---


### Tool result

_source line 1550 · 2026-05-17T06:15:50.383742+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1407
}
```

</details>

---


### Assistant

_source line 1551 · 2026-05-17T06:16:00.517601+00:00_

Round 16 审稿任务已分配:
- **Reviewer 1** → 方法严谨性 + 实验设计 + 统计方法论
- **Reviewer 2** → 新颖性 + 贡献定位 + 相关工作 + 写作质量

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 125

## Round 125

34 recorded events


### User

_source line 1552 · 2026-05-17T06:19:37.336698+00:00_

[Reviewer 1 审稿意见]:
## Round 16 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）

**论文**: "Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction"
**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)

---

## Summary

This paper evaluates five confidence signals (four instance-level, one per-sample) for quality estimation and sample selection in LLM-based NER. It demonstrates that while all signals achieve reliable quality estimation (ρ up to 0.42, AUROC up to 0.82), none translates QE into effective best-of-N selection—the "correlation-selection gap." Two mechanisms are identified: instance degeneracy (10–58% identical outputs) and LP compression (median range 0.041 nats). The degeneracy-gating pattern across three datasets shows LP selection effectiveness is inversely related to degeneracy rate. The paper is thorough, well-structured, and makes a genuine negative-result contribution with extensive ablations.

---

## 总体评分

**Overall**: 3.5/5 (borderline Findings/Conference)
**一句话总结**: 实证工作扎实、消融全面，但核心 degeneracy-gating claim 的统计支撑仅有 3 个数据点，且多处统计方法论存在可改进空间，制约了结论的普适性。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计系统、ablation 充分，但统计效力不足（2-seed sign test）、核心 monotonic claim 仅 3 数据点、Bonferroni scope 存在争议 |
| Excitement | 3/5 | 负面结果有价值且相关性强，但缺少 actionable positive contribution（如 verifier baseline 或 task-specific LP variant） |
| Reproducibility | 4/5 | 训练配置详尽、constrained decoding pipeline 有描述，但 vLLM 版本/XGrammar 具体配置缺失 |
| Confidence | 4/5 | 仔细阅读，熟悉 MBR decoding 和 NER 评估方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 2-seed paired sign test 的统计效力严重不足

- 具体位置：Section 4.3 (Table 2), footnote 4, §4.1 footnote ("Quality estimation uses a single primary seed (seed=42); selection uses 2-seed averages for variance estimation")
- 问题：Selection 的核心结论"no signal significantly outperforms greedy"基于 2-seed paired sign test。Sign test 是最保守的非参数检验（仅使用方向信息，丢弃幅度信息），在 2-seed 设定下几乎无法检测到真实效应。如果 LP 真的有 +0.2pp 的效应，sign test 在 n=529、2 seeds 下的 power 极低。这意味着 p=0.29 可能是 under-powered null 而非 true null。论文用 3-seed 实验声称 σ≤0.026 证明 stability，但这仍然不够：3 个 seeds 不足以可靠估计 σ，更不足以构建有效的假设检验。
- 为什么影响接收：核心负面结论（"selection fails"）的统计基础不牢靠。审稿人无法区分"效应不存在"和"检验无力检测到效应"。
- 建议修改方向：(1) 使用 paired bootstrap test（B=10,000）替代 sign test，利用幅度信息；(2) 增加 seed 数至 5+ 或报告 power analysis；(3) 明确区分 "no evidence of effect" 与 "evidence of no effect"——TOST 部分尝试做了但仅限附录且结论 configuration-dependent。

**N2** [critical] Degeneracy-gating 的 monotonic pattern 仅基于 3 个数据点

- 具体位置：Table 4 (§4.4), Abstract line 7, Conclusion line 7, Figure 3
- 问题：核心 claim "instance degeneracy monotonically predicts LP selection effectiveness" 来自 CoNLL(58%→fail), SciERC(21%→+0.42pp), Few-NERD(10%→+1.36pp) 三个数据点。3 点的 monotonic trend 在统计上不具有意义——任意 3 个不同值必然可以排出 monotonic order。论文自己报告 Spearman ρ=−0.57, p=0.066 (n=11，含 per-type 数据点, Figure 3 caption)，即未达到 α=0.05 显著水平。
- 为什么影响接收：这是论文最突出的 claim（出现在 title 暗示、abstract、intro contribution list、conclusion），但统计证据不支持将其从 observational pattern 提升为 "predictive mechanism"。
- 建议修改方向：(1) 将语言从 "monotonically predicts" 降级为 "is consistent with a monotonic relationship, though the limited number of dataset-level data points (n=3) precludes statistical confirmation"；(2) 补充 per-type 分析的正式统计（已有 per-type data），计算 cross-dataset + per-type 的 mixed-effects model；(3) 或承认这是 exploratory observation 而非 confirmed mechanism。

**N3** [critical] Bonferroni correction scope 与 post-hoc ε 选择的交互

- 具体位置：§4.3 footnote 4 ("survives Bonferroni over 5 comparisons"), §Discussion Non-tied subset analysis, Appendix Table 8 (ε sweep)
- 问题：论文声称 non-tied LP subset 的 +2.9pp (p=0.004) "survives Bonferroni correction over 5 comparisons" (p_adj=0.020)。但 Bonferroni scope 仅覆盖 5 signal comparisons，未纳入 ε threshold 的 post-hoc 选择。Table 8 (Appendix) 明确展示了 7 个 ε 值的 sweep (0.01–0.20)，且 ε=0.05 被选择恰恰因为它 "yields the strongest statistical separation"。如果将 7 个 ε × 5 signals = 35 comparisons 纳入 Bonferroni，p_adj = 0.004 × 35 = 0.14，不再显著。
- 为什么影响接收：这是论文唯一的正面统计显著结果（"LP does carry per-sample discriminative information"），如果 multiple comparison correction 范围不当，核心 evidence chain 断裂。
- 建议修改方向：(1) 明确承认 ε=0.05 是 post-hoc 选择，Bonferroni 范围存在争议；(2) 使用 pre-registered split（如 median split）或 permutation-based FDR 控制；(3) Limitations 中已提到 "post-hoc exploratory choice" 但主文 footnote 4 的 framing 仍暗示这是 confirmed finding——两处需要保持一致。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Random baseline (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距缺乏理论解释

- 具体位置：Table 2 (§4.3)
- 问题：如果 Random 是从同一温度 T=1.0 的 N 个 samples 中随机选一个，而 Single 是同一分布的单次采样，理论上 E[Random] = E[Single] = E[sample under T=1.0]。但 Table 2 显示 Random=0.610, Greedy(T=0)=0.645。Greedy 是不同分布（argmax decoding），差异合理。但 "Random" 的含义需要澄清：如果 Random 是从 N=8 candidates 中 uniform 选取的 expected F1，它应该等于 single-sample mean F1 under T=1.0。Table 4 (Few-NERD) 中 Greedy=0.748 而 SciERC Greedy=0.614（full-set），暗示 Table 2 的 Greedy=0.645 是 gold-filtered subset 的 T=0 结果。那 Random=0.610 是 gold-filtered subset 的 sample mean under T=1？如果是，0.610 vs 0.645 反映的是 T=1 vs T=0 的 quality gap，而非 selection 能力。论文未明确标注 Random 的定义。
- 建议：明确说明 Random baseline 的语义——是 T=1 single sample mean 还是其他构造；讨论 Greedy(T=0) 与 Sample mean(T=1) 的差异是否意味着 T=1 本身降低了 quality。

**W2** [warning] Kendall's W=1.0 with only 3 seeds 的 precision caveat 不充分

- 具体位置：§4.5 ("Signal rankings are stable across seeds (Kendall's W=1.0 at N=8; Table 11)")，Appendix Table 11
- 问题：Kendall's W with m=3 raters (seeds) ranking k=5 items (signals) 的 sampling distribution 是非常 discrete 的。W=1.0 只说明 3 个 seeds 恰好产生了相同 ranking，但置信区间极宽。论文在 Appendix (line 899) 有 caveat ("statistical power with n=3 is limited")，但主文 §4.5 直接引用 W=1.0 作为 robustness 证据，无 qualification。
- 建议：主文中加入 caveat，如 "though the small number of seeds (3) limits the precision of this estimate"。

**W3** [warning] Instance degeneracy 8B(21%) vs 4B(10.4%): capability vs fine-tuning recipe confound

- 具体位置：§4.5, Table 5 (Discussion), §4.5 "Instance degeneracy also scales with model capability"
- 问题：论文声称 "instance degeneracy scales with model capability" (8B: 21%, 4B: 10.4%)。但两个模型使用相同 training recipe（5 epochs, rank=32）。更大模型在相同 epochs 下可能 overfit 更快（更多参数 per data point），导致更强的 output convergence——这是 training dynamics artifact 而非 fundamental capability-driven 现象。如果 4B 训练更多 epochs 使其达到相似 F1，degeneracy 可能追平。论文的 LoRA-rank ablation (rank=8 降低 degeneracy 到 7%) 实际上 支持 "fine-tuning recipe" 解释而非 "capability" 解释。
- 建议：(1) 讨论 effective parameter count / data ratio 的 confound；(2) 弱化 "scales with model capability" 的 causal 语言为 "correlates with model scale under matched training"；(3) 考虑 early-stopping ablation 作为 disentanglement。

**W4** [warning] TOST 等价性结论的 configuration-dependent 呈现不平衡

- 具体位置：§4.3 (line 109), Appendix §TOST (External equivalence margins)
- 问题：主文 §4.3 说 "TOST equivalence holds under all external anchors for LLaMA-CoNLL but varies by configuration"——但 varies 的方向是 Qwen-CoNLL **所有** signal 都 fail equivalence（降级 0.9–1.5pp），这意味着 signals 可能 actively harm selection。附录详细报告了这一点，但主文的措辞 "varies by configuration" 过于轻描淡写。一个 reviewer 可能认为这削弱了 "no harm" 的 claim。
- 建议：主文中更清晰地呈现——某些配置下 signal selection 显著 worse than greedy（Qwen-CoNLL），这不仅仅是 "equivalence fails" 而是 "active degradation"。

**W5** [warning] Gold-empty instance filtering 在 QE 和 Selection 之间的不一致

- 具体位置：§3.3 ("Both quality estimation and selection exclude instances with no gold annotations: n=529 on SciERC (from 551), n=2,756 on CoNLL (from 3,453)")，但 Table 4 中 SciERC 使用 n=551
- 问题：Table 4 (Few-NERD comparison) 中 SciERC 使用 "full test set (n=551) for protocol consistency" 而非 gold-filtered n=529，且 Greedy=0.614 而非 Table 2 的 0.645。脚注解释了差异但这引入了 apple-to-orange comparison。Table 2 (gold-filtered) 的 LP Δ=+0.2pp 与 Table 4 的 LP Δ=+0.42pp 不一致——读者需要仔细追踪哪个表用哪个 n。
- 建议：统一报告协议，或在 Table 4 中同时报告 gold-filtered 数字以便 direct comparison。

---

## 小问题（不影响接收）

- §4.1: "3-seed stability σ≤0.026" — σ 是 sample std 还是 population std? Table 10 caption 说 "population standard deviation over 3 seeds" 但 3 个 seeds 的 pop std 和 sample std 差别显著。
- Table 2: EM 的 p 值为 "---" 而非数字。如果 EM < greedy，应报告方向。
- Appendix Table 12 (ranking stability): Kendall's W=0.822 for RE at N=8 暗示 RE rankings 不如 NER stable，但主文未提及这一差异。
- §Discussion "Hypotheses for LP compression" 列出 (b)(c)(a)(d) 而非 (a)(b)(c)(d)——排序似乎有意但未解释。
- Figure 3 caption 中 Spearman ρ=−0.57, p=0.066, n=11: 这个 n=11 的构成（3 datasets + 8 per-type points）混合了不同粒度的数据点，可能违反 independence 假设。

---

## 主要优势

1. **系统性强**: 5 signals × 4 datasets × 2+ models × multiple N/T/seed configurations，覆盖面在同类论文中属于上乘。
2. **负面结果的诊断深度**: 不仅报告 "什么不 work"，还系统诊断 why（degeneracy + LP compression），并通过 LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination 等 4 重诊断排除 alternative explanations。
3. **Transparency**: 诚实报告 TOST 结论的 configuration-dependence，ε 的 post-hoc 性质（在 Limitations 中），多处主动报告 caveats。
4. **Few-NERD 对照实验**: 通过引入低 degeneracy 数据集验证 LP selection 在有利条件下确实 work，增强了 degeneracy 作为解释变量的可信度。
5. **写作质量**: 论文结构清晰，叙事线条连贯（QE works → selection fails → why → when does it work），符合 empirical analysis paper 的最佳范式。

---

## Questions for Authors

1. 2-seed sign test 的 power analysis: 在 effect size d=0.038 (Cohen's d, 来自附录 TOST 部分) 下，sign test with n=529 的 power 是多少？是否考虑过 Wilcoxon signed-rank test 以利用幅度信息？
2. ε=0.05 threshold 的选择：如果 pre-register median LP range (0.041) 作为 split point，non-tied subset 的 selection gain 是否仍然显著？
3. Degeneracy 的 operationalization: "constant F1" 定义是否过于严格？如果用 F1 range < 0.01 (或其他 soft threshold)，degeneracy rate 会如何变化，monotonic pattern 是否 robust？
4. Few-NERD 训练只用了 3 epochs (vs 其他 datasets 的 5 epochs)——这是否本身影响 degeneracy rate？如果 Few-NERD 也训练 5 epochs，degeneracy 是否会升高？

---

## Missing References

- Freitag et al. (2023) "Results of WMT23 Metrics Shared Task" — MBR 在 MT 中的最新成果
- Li et al. (2024) "Confidence Estimation for LLM-Based Dialogue State Tracking" — 结构化输出的 confidence estimation
- Xu et al. (2024) "Rejection Improves Reliability" — selective prediction 与 NER 的交叉
- 缺少 NER 评估方法论综述引用（如 Ratinov & Roth 2009 已引但 Derczynski et al. 2016 "Broad Twitter Corpus" 评估方法未引）

---

## Overall Assessment

**Score: 3.5/5** (between Findings and Conference)

这是一篇扎实的 empirical analysis 论文，对 "self-consistency 是否能 scale 到结构化 IE" 这一实践相关问题给出了有价值的负面结果。诊断深度（4 重 ablation chain）和实验覆盖面是论文的明显优势。

主要弱点在统计方法论层面：(1) 核心否定结论基于 under-powered 2-seed sign test；(2) 唯一正面结果（non-tied LP）的 multiple comparison correction 范围有争议；(3) 最突出的 claim（degeneracy-gating monotonic pattern）仅 3 个宏观数据点，且 formal test 未达显著。这些问题不影响数据的真实性，但影响 claim 的强度和表述。

如果作者能 (a) 加强统计基础（more seeds 或 bootstrap tests），(b) 适当弱化 monotonic claim 的语言，(c) 平衡呈现 TOST 在不同 configurations 下的 divergent 结论，论文可以达到 Conference 水平。当前状态适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1553 · 2026-05-17T06:20:01.514791+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1554 · 2026-05-17T06:20:01.515208+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1555 · 2026-05-17T06:20:02.219522+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1556 · 2026-05-17T06:20:02.270484+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1557 · 2026-05-17T06:20:05.713438+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1558 · 2026-05-17T06:20:06.566978+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (120 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_027_fewnerd_n16** (success): LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\n- **exp_016_rerun_1024_bootstrap** (negative): 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant. ← 基于 exp_016_rerun_1024\n  [fig_selection_gap_1024](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf)\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \"score compression is general\" claim. If effective → important positive finding requiring narrative adjustment. ← 基于 exp_012_rerun_1024\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\n\n## 趋势\n成功 70 / 负向 24 / 失败 4 / 共 120\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1559 · 2026-05-17T06:20:06.768149+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1560 · 2026-05-17T06:20:06.818752+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1561 · 2026-05-17T06:20:09.930704+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1562 · 2026-05-17T06:20:09.931162+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1563 · 2026-05-17T06:20:10.433262+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1564 · 2026-05-17T06:20:10.483822+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1565 · 2026-05-17T06:20:14.298440+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1566 · 2026-05-17T06:20:14.750527+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_0.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7_consistency.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_9.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1567 · 2026-05-17T06:20:14.801196+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 1568 · 2026-05-17T06:20:14.851807+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1569 · 2026-05-17T06:20:18.917082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_15.md",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1570 · 2026-05-17T06:20:18.917539+00:00_

1	---
2	round: 15
3	overall_score: borderline
4	timestamp: 2026-05-16T08:58:54.626080+00:00
5	reviewer_ids: [1, 2]
6	cross_response_reviewer_ids: [1, 2]
7	force_resubmit: False
8	---
9	
10	# Round 15 审稿报告 — Consolidated Review
11	
12	**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
13	**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026)
14	**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计; R2: 新颖性+Related Work+写作+格式）
15	**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）
16	
17	---
18	
19	## Summary
20	
21	论文研究 LLM-based NER 中 5 个置信度信号（4 个 instance-level 一致性信号 + 1 个 per-sample LP）的质量估计与样本选择能力，在 SciERC（primary, ~65% F1）、CoNLL-2003（ceiling control, ~91% F1）、WNUT-17（collapse boundary, 48% F1）上评估，使用 Qwen3-8B、LLaMA-3.1-8B 及 4B ablation。核心发现是 "correlation-selection gap"：信号有中等 QE 能力（ρ=0.38 on SciERC）但选择失败，greedy decoding (T=0) 超过所有 N=8 选择策略。诊断两个机制：instance degeneracy（21-58% 实例产生相同 F1）和 LP compression（中位数 within-instance range 0.041 nats）。
22	
23	---
24	
25	## Strengths
26	
27	**S1. QE vs selection 解耦框架有方法论价值** [Both]
28	将 quality estimation（哪些 input 可靠？）与 sample selection（哪个 output 最好？）解耦是重要的方法论贡献。Figure 1 一张图传达核心发现，设计精良。
29	
30	**S2. 诊断分析系统性强** [Both]
31	五层 ablation chain（free-form decoding、entity-token LP、verbalized confidence、non-tied subset、signal combination）逐层排除替代解释。Verbalized confidence baseline（更高 ρ 但更差 selection）特别有力地验证了 gap 概念。
32	
33	**S3. Within-instance analysis 是最强贡献** [Both]
34	MBR utility 在 non-degenerate instances 上与 F1 正相关（median ρ=0.52），且 MBR 在这些 instances 上 closes 23-41% of oracle gap——证明 MBR 在有 headroom 时 work。Failure 来自 headroom vanishing 而非 utility misalignment，这与 Eikema et al. (2025) 报告的 MBR failure mode 有 qualitative 区别。
35	
36	**S4. 实验透明度高** [R1]
37	对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。
38	
39	**S5. Appendix 质量极高** [R2]
40	16+ appendix sections 提供了 FK independence test、SJ normalizer robustness、ε sensitivity 
…[truncated 3379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1571 · 2026-05-17T06:20:19.218824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1572 · 2026-05-17T06:20:19.269471+00:00_

1	issues:
2	# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====
3	- id: R0-C1
4	  summary: "模型规模单一（仅 8B）"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 1
10	  resolution: "Round 2 Reviewer 确认措辞修正到位"
11	  resolution_round: 2
12	- id: R0-C2
13	  summary: "相关工作显著遗漏"
14	  category: framing
15	  severity: warning
16	  status: resolved
17	  first_raised_round: 0
18	  last_seen_round: 1
19	  resolution: "Round 2 确认 49 条 bib 全部 cited"
20	  resolution_round: 2
21	- id: R0-C4
22	  summary: "SJ 方法新颖性有限"
23	  category: method
24	  severity: warning
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 1
28	  resolution: "Round 2 确认三点差异化清晰"
29	  resolution_round: 2
30	- id: R0-C5
31	  summary: "全文零图表"
32	  category: writing
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 0
37	  resolution: "论文已包含 6 个 figures"
38	  resolution_round: 1
39	- id: R0-C6
40	  summary: "成本分析 negligible 误导"
41	  category: method
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 0
46	  resolution: "Round 1+ 未再提及"
47	  resolution_round: 1
48	- id: R0-W1
49	  summary: "未探索 signal combination"
50	  category: experiment
51	  severity: warning
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 0
55	  resolution: "Round 1+ 未再提及"
56	  resolution_round: 1
57	- id: R0-W4
58	  summary: "统计检验不系统"
59	  category: experiment
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 0
63	  last_seen_round: 1
64	  resolution: "Round 2 Reviewer 评价 bootstrap 达到高标准"
65	  resolution_round: 2
66	- id: R3-W4
67	  summary: "FK independence 假设未验证"
68	  category: experiment
69	  severity: warning
70	  status: resolved
71	  first_raised_round: 3
72	  last_seen_round: 8
73	  resolution: "Appendix instance-level permutation test (n=529-2756, p<0.001) 验证"
74	  resolution_round: 9
75	- id: R3-W5
76	  summary: "Cross-mode
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1573 · 2026-05-17T06:20:23.785599+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "100",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1574 · 2026-05-17T06:20:23.886773+00:00_

100	  resolution: "贡献重新框架化为 finding-led"
101	  resolution_round: 9
102	- id: R7-W1
103	  summary: "LP temperature 依赖未说明"
104	  category: experiment
105	  severity: warning
106	  status: resolved
107	  first_raised_round: 7
108	  last_seen_round: 7
109	  resolution: "Appendix 排除 LP + Limitations 扩展说明"
110	  resolution_round: 9
111	- id: R7-W3
112	  summary: "Eikema Related Work 覆盖不足"
113	  category: writing
114	  severity: warning
115	  status: resolved
116	  first_raised_round: 7
117	  last_seen_round: 7
118	  resolution: "Related Work 增加 Eikema 讨论"
119	  resolution_round: 9
120	- id: R8-N1
121	  summary: "页数超限"
122	  category: writing
123	  severity: warning
124	  status: resolved
125	  first_raised_round: 8
126	  last_seen_round: 8
127	  resolution: "主文在限制内"
128	  resolution_round: 9
129	- id: R8-W2
130	  summary: "Thinking token 对 LP 影响未分析"
131	  category: experiment
132	  severity: warning
133	  status: resolved
134	  first_raised_round: 8
135	  last_seen_round: 8
136	  resolution: "Appendix 3-part quantitative analysis 已补充"
137	  resolution_round: 9
138	- id: R8-W3
139	  summary: "SJ normalizer 选择敏感性"
140	  category: method
141	  severity: warning
142	  status: resolved
143	  first_raised_round: 8
144	  last_seen_round: 8
145	  resolution: "Appendix table delta-rho<0.005 证明不敏感"
146	  resolution_round: 9
147	- id: R9-W1
148	  summary: "缺少其他 per-sample signal baseline"
149	  category: experiment
150	  severity: warning
151	  status: resolved
152	  first_raised_round: 9
153	  last_seen_round: 9
154	  resolution: "Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)"
155	  resolution_round: 9
156	- id: R9-W3
157	  summary: "TOST 等价性结论 configuration-dependent 未整合进正文"
158	  category: experiment
159	  severity: warning
160	  status: resolved
161	  first_raised_round: 9
162	  last_seen_round: 9
163	  resolution: "Section 4.2 已含 config-dependent note"
164	  resolution_round: 9
165	- id: R9-W4
166	  summary: "VC majority-voting selection 失败机制未分析"
167	  category: met
…[truncated 2339 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1575 · 2026-05-17T06:20:27.209950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "248",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "248",
    "limit": "200"
  }
}
```

</details>

---
