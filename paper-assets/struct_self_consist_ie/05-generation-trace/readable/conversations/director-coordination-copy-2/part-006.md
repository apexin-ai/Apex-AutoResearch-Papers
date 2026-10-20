# Director coordination — Part 6 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 125

### Tool result

_source line 1576 · 2026-05-17T06:20:27.261533+00:00_

248	  category: experiment
249	  severity: warning
250	  status: resolved
251	  first_raised_round: 11
252	  last_seen_round: 13
253	  resolution: "Entity-token LP 实验已完成并纳入 Discussion (4× variance, selection -2.0pp, CoNLL collapse)"
254	  resolution_round: 13
255	- id: R11-W5
256	  summary: "Preliminary 标注过于频繁"
257	  category: writing
258	  severity: warning
259	  status: resolved
260	  first_raised_round: 11
261	  last_seen_round: 12
262	  resolution: "论文已统一使用 †RE 标记系统替代反复 preliminary"
263	  resolution_round: 13
264	- id: R11-W7
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
310	  summary: "缺少两篇直接相关文
…[truncated 5123 chars]

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

_source line 1577 · 2026-05-17T06:20:30.373274+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "445",
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
    "offset": "445",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1578 · 2026-05-17T06:20:30.474166+00:00_

445	    action: "Footnote 4 修正 Bonferroni scope 或改为 'exploratory finding'. 当前 'survives correction' 给读者 robust finding 错觉."
446	    assigned_to: Paper Agent
447	    status: in_progress
448	  resolution: ""
449	  resolution_round: null
450	
451	- id: R11-W1
452	  summary: "与 Yao et al. (2026) 增量贡献定义不够清晰"
453	  category: framing
454	  severity: warning
455	  status: in_progress
456	  first_raised_round: 11
457	  last_seen_round: 15
458	  mentions:
459	  - round: 11
460	    reviewers: [1, 2]
461	    note: "R2 提出, R1 反驳 selection analysis 有独立价值"
462	  - round: 12
463	    reviewers: [1, 2]
464	    note: "共识: 现有差异描述可接受, camera-ready 级 refinement"
465	  - round: 14
466	    reviewers: [1, 2]
467	    note: "R14 强共识: fine-tuning → degeneracy 是关键区分但论文未抓住."
468	  - round: 15
469	    reviewers: [1, 2]
470	    note: "R15: R2-W3 + R1 AGREE. 关键未回答问题: hard-prompted models 是否存在 instance degeneracy? 如果否→degeneracy 是 fine-tuning artifact 非 task-intrinsic. 这是最强差异化论点但仍未被显式讨论."
471	  action_items:
472	  - round: 14
473	    action: "Related Work 增加明确对比段落."
474	    assigned_to: Paper Agent
475	    status: in_progress
476	  - round: 15
477	    action: "Related Work 或 Discussion 增加显式讨论: (1) Yao et al. = hard-prompted, 本文 = fine-tuned; (2) hard-prompted 是否有 degeneracy 是区分 task-intrinsic vs fine-tuning artifact 的关键; (3) 如无 hard-prompted degeneracy data, 显式承认此 open question."
478	    assigned_to: Paper Agent
479	    status: in_progress
480	  resolution: ""
481	  resolution_round: null
482	
483	- id: R11-W2
484	  summary: "Scale range (3B-8B) 不足以支撑普适性结论"
485	  category: framing
486	  severity: warning
487	  status: in_progress
488	  first_raised_round: 11
489	  last_seen_round: 15
490	  mentions:
491	  - round: 11
492	    reviewers: [1, 2]
493	    note: "需确认所有 scale claims 限定范围"
494	  - round: 12
495	    reviewers: [1, 2]
496	    note: "R12 两位再次强共识."
497	  - round: 14
498	    reviewers: [1, 2]
499	    note: "Abstract 'at two model scales' 未说明 narrow range."
500	  - round: 15
501	    reviewers: [1
…[truncated 4447 chars]

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

_source line 1579 · 2026-05-17T06:20:35.592691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "644",
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
    "offset": "644",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1580 · 2026-05-17T06:20:35.693663+00:00_

644	    reviewers: [1]
645	    note: "R15 R1-W4 partial: RE reversal 削弱 NER 'ruling out' claim. 共识改 'ruling out' → 'provides evidence against'."
646	  action_items:
647	  - round: 12
648	    action: "Discussion 将 RE free-form reversal 定位为 promising direction"
649	    assigned_to: Paper Agent
650	    status: in_progress
651	  - round: 15
652	    action: "'ruling out constrained decoding' 改为 'provides evidence against constrained decoding as the primary cause for NER'."
653	    assigned_to: Paper Agent
654	    status: in_progress
655	  resolution: ""
656	  resolution_round: null
657	
658	- id: R12-N1
659	  summary: "ρ=0.45 headline 来自 ceiling-effect dataset, primary dataset 仅 ρ=0.379"
660	  category: framing
661	  severity: warning
662	  status: in_progress
663	  first_raised_round: 12
664	  last_seen_round: 15
665	  mentions:
666	  - round: 12
667	    reviewers: [1, 2]
668	    note: "改措辞为 moderate-to-strong 或加限定语"
669	  - round: 14
670	    reviewers: [1, 2]
671	    note: "ρ=0.38 按 Cohen (1988) 属 medium effect."
672	  - round: 15
673	    reviewers: [1, 2]
674	    note: "R15: R2-W1 + R1 PARTIALLY AGREE. Abstract 'ρ up to 0.38 on the primary test bed, 0.45 on a ceiling-effect control' — CoNLL ρ=0.45 受 zero/non-zero boundary inflate (+0.03-0.05). 建议 abstract 仅报告 primary ρ=0.38."
675	  action_items:
676	  - round: 14
677	    action: "'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset."
678	    assigned_to: Paper Agent
679	    status: in_progress
680	  - round: 15
681	    action: "Abstract 改为仅报告 primary ρ=0.38, 或 'moderate (ρ=0.38 on primary, up to 0.45 on ceiling-effect control)' 避免 strong 暗示."
682	    assigned_to: Paper Agent
683	    status: in_progress
684	  resolution: ""
685	  resolution_round: null
686	
687	- id: R12-W1
688	  summary: "纯诊断无 remedy 尝试, 限制论文 impact"
689	  category: experiment
690	  severity: warning
691	  status: in_progress
692	  first_raised_round: 12
693	  last_seen_round: 15
694	  mentions:
695	  - round: 12
696	    reviewers: [1, 2]
697	
…[truncated 5073 chars]

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

_source line 1581 · 2026-05-17T06:20:40.310313+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "843",
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
    "offset": "843",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1582 · 2026-05-17T06:20:40.411266+00:00_

843	    assigned_to: Paper Agent
844	    status: in_progress
845	  - round: 15
846	    action: "主文从 'all p>0.05' 叙事转向 'd=0.038 with multiple convergent lines (TOST, cross-config, greedy comparison)'. 补报 selection F1 3-seed σ."
847	    assigned_to: Paper Agent
848	    status: in_progress
849	  resolution: ""
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
892	  action_items
…[truncated 4798 chars]

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

_source line 1583 · 2026-05-17T06:20:43.220048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "1042",
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
    "offset": "1042",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1584 · 2026-05-17T06:20:43.271355+00:00_

1042	    status: open
1043	  resolution: ""
1044	  resolution_round: null
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
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 1585 · 2026-05-17T06:21:28.976297+00:00_

收到 Reviewer 1 (Round 16) 审稿报告。

**R1 关键发现概要**：
- 评分 3.5/5 (borderline Findings/Conference)
- 3 个 Critical：(N1) 2-seed sign test 效力不足, (N2) degeneracy-gating monotonic claim 仅 3 数据点且 p=0.066 未达显著, (N3) Bonferroni scope 未纳入 ε post-hoc 选择 (35 comparisons 下 p_adj=0.14)
- 5 个 Should-Fix：Random baseline 未定义, Kendall W precision caveat, 8B/4B degeneracy confound, TOST 呈现不平衡, gold-filtering 不一致

**与历史 issue 的映射**：
| R16 Finding | 对应历史 Issue | 变化 |
|---|---|---|
| N1 (sign test) | R14-W1 | 升级为 critical，更具体指出 sign test 而非 Fisher combined p |
| N2 (3-point monotonic) | **新** — Few-NERD 加入后产生的新 claim 被挑战 |
| N3 (Bonferroni scope) | R7-C2 | 更精确量化：7ε×5=35 comparisons |
| W1 (Random gap) | R14-M1 | 持续存在 |
| W3 (recipe confound) | R15-N1 | 持续存在，LoRA-rank ablation 被反向引用 |
| W4 (TOST) | R15-W1 | 持续存在 |

**当前状态**：等待 Reviewer 2 报告。收到后将执行交叉分享 (Step 2)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 126

## Round 126

6 recorded events


### User

_source line 1586 · 2026-05-17T06:21:30.076856+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

核心发现：论文实证工作扎实（5 signals × 4 datasets × 多 ablation），但有三个关键统计方法论问题需要 must-fix：(1) 2-seed sign test 效力不足以支撑 "selection fails" 的否定结论；(2) degeneracy-gating monotonic pattern 仅 3 个宏观数据点，formal test p=0.066 未达显著；(3) non-tied LP subset 的 Bonferroni scope 未覆盖 post-hoc ε 选择（7ε×5=35 comparisons 下不再显著）。整体评分 3.5/5，当前状态适合 Findings，加强统计基础后可达 Conference。

---

[Reviewer 2 审稿意见]:
## Round 16 审稿报告 — Reviewer 2（新颖性 + 贡献定位 + 相关工作 + 写作质量）

---

## Summary

本文研究 self-consistency 信号在 LLM-based NER 中的质量估计（QE）与样本选择（selection）效果。作者评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 4 个 NER benchmark 上的表现，发现：信号可有效预测实例级质量（ρ up to ~0.42），但无法有效选择 best-of-N 候选（"correlation-selection gap"）。文章诊断出两个机制：instance degeneracy 和 LP compression，并展示 degeneracy 单调预测 LP selection 有效性。

论文实验设计系统、分析细致，诊断链（LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination）令人印象深刻。但新颖性存在结构性问题：核心 "gap" 部分是定义性质的（instance-level signals by construction 无法区分候选），且与 MBR 社区已知限制有重叠。

---

## Strengths

**S1. 系统性实验设计。** 4 个 benchmark 形成 difficulty gradient（ceiling → medium → low-resource → signal-collapse），每个数据集有明确角色定位。2 个模型族 + 4B scale ablation 提供跨架构证据。

**S2. 诊断深度出色。** 从 "gap exists" 到 "why it exists" 的诊断链是本文最强部分：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 constrained decoding → entity-token LP 排除 format dilution → supervised combination 确认 feature space bottleneck。这比纯粹的 empirical survey 多了一层因果推断。

**S3. Negative result 的科学��值。** 对 NER practitioners 有实际意义：不要在 fine-tuned 高性能模型上指望 self-consistency 做 selection；QE 用于 selective prediction / error flagging 是可行的落地方向。

**S4. 统计严谨性。** Bootstrap CI、paired sign tests、TOST equivalence testing、Bonferroni correction 均适当使用。Non-tied subset 分析的 post-hoc 性质在 limitations 中有坦诚说明。

**S5. Few-NERD 对比实验设计巧妙。** 利用 degeneracy 差异形成跨 dataset 自然实验（58% → 21% → 10%），展示 monotonic 关系，超越了单 dataset 的局部结论。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] Correlation-selection gap 的新颖性存在 tautological 成分

- 具体位置：Section 3.1, Section 4.3, Abstract
- 问题：论文的核心 contribution "correlation-selection gap" 对 structural signals（4/5）存在定义性质的成分。Section 3.1 明确写道："4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates." 既然 instance-level signals BY CONSTRUCTION 对同一 input 的所有候选给出相同分数，它们当然无法做 selection。将其转化为 MBR/consensus-proximity 选择（选最接近集体平均的候选）后依然失败，才是真正的 empirical finding。但论文 framing 将两者混为一谈——标题 "Strong Predictors, Weak Selectors" 暗示这是一个意外的发现，而实际上 structural signals 的 "weakness" 部分来自定义而非实验。
- 为什么影响接收：审稿人会质疑核心贡献中有多少是 trivially true vs genuinely surprising。如果去掉定义性部分，真正的 empirical finding 变窄为：(a) MBR with SJ utility (median within-instance ρ=0.52) 仍然失败 because of degeneracy; (b) LP fails due to compression。这两点是有价值的，但需要更精确的 framing。
- 建议：明确在 Introduction 中区分 "definitional limitation"（instance-level signals cannot rank candidates）和 "empirical finding"（even MBR conversion with positive utility correlation fails due to degeneracy; LP fails due to compression）。重写 contribution 2 的措辞，将 emphasis 放在 degeneracy 和 compression 的诊断上而非 "gap" 本身。

**N2** [critical] ρ=0.42 headline claim 存在数值不一致

- 具体位置：Abstract line 3, Introduction line 11, Figure 1 caption, Discussion line 113, Related Work line 26, vs. Contribution 1 (Introduction line 29)
- 问题：Abstract 说 "ρ up to 0.42 on Few-NERD and the primary test bed"；Figure 1 caption 说 "ρ up to 0.45 on CoNLL, 0.42 on primary test bed"；Related Work 说 "signals with ρ up to 0.45 on CoNLL (0.42 on the primary test bed)"。但 Table 1 清楚显�� SciERC（primary test bed）最高 ρ = VC 0.379。ρ=0.42 来自 Few-NERD LP（0.421）。然而 Contribution 1 正确地写 "VC ρ=0.38 on the primary test bed"。论文内部存在矛盾：同一数据的同一描述在不同位置给出不同数值（0.38 vs 0.42）。
- 为什么影响接收：数值不一致损害论文可信度。Figure 1 caption 明确将 0.42 归因于 "primary test bed"，但该数值并非来自 SciERC (N=8)。这在 reviewer 看来要么是 cherry-picking 要么是粗心。
- 建议：统一所有 headline 数值。若 primary test bed = SciERC，则 ρ 上界应报告为 0.38（N=8）或明确标注 N=16 时的数值。若要报告 0.42，必须明确归因于 Few-NERD。

**N3** [critical] 与 MBR 社区已知结论的增量不够清晰

- 具体位置：Section 2 (Related Work), Section 5 (Discussion)
- 问题：MBR 社区早已知道 MBR 不是万能的。Eikema et al. (2025) "Structure-Conditional MBR" 明确讨论 MBR utilities degrade on structured outputs due to bag-of-unit mismatches。论文承认 "our diagnosis is complementary" (Related Work line 24) 但没有充分量化增量。本文的核心发现——positive within-instance utility correlation (ρ=0.52) 不导致 selection gains because of degeneracy——与 Eikema et al. (2025) 的 "utility misalignment vs output concentration" 区分是互补的，但这个互补关系需要更明确地 articulate。
- 建议：在 Related Work 中增加一个明确的 differentiation paragraph，用 1-2 句话精确说明：Eikema et al. 认为问题在 utility design，本文证明即使 utility IS aligned（ρ=0.52），degeneracy 也会 eliminate headroom。这才是真正的 incremental contribution over MBR literature。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Few-NERD LP +1.36pp 作为 positive finding 的呈现不够平衡

- 具体位置：Abstract line 7, Section 4.4, Table 5
- 问题：+1.36pp 是论文中唯一统计显著的正向 selection 结果，但来自：(a) 单一模型 Qwen3-8B，(b) N=8，(c) 非 primary test bed。论文确实在 limitations 中提到了 scale 限制，但 abstract 将其与主 finding 并列呈现（"at 10% degeneracy, LP achieves +1.36pp"），给人的印象是这是一个 robust finding。实际上只有 1 个 model × 1 个 N × 1 个 dataset 的证据。
- 建议：在 Abstract 或 Introduction 中加限定语（如 "on the single low-degeneracy dataset tested"），或增加 LLaMA Few-NERD 验证。

**W2** [warning] Soft Jaccard 命名有误导性

- 具体位置：Section 3.2 Eq.4, footnote
- 问题：论文自己在脚注中承认分母用 max(|g_i|,|g_j|) 而非 union。标准 Jaccard = |A∩B|/|A∪B|；本文度量更接近 Dice/Sørensen 变体或 Overlap coefficient。命名为 "Soft Jaccard" 会误导读者对其数学性质的预期。虽然 Table 8 证明 max vs union 对结果影响极小（Δρ<0.01），但命名本身不准确。
- 建议：改名为 "Soft Overlap" 或在首次出现时明确说明 "we term this Soft Jaccard following [X], though the denominator differs from standard Jaccard"。

**W3** [warning] 与 Yao et al. (2026) 的差异化尚不充分

- 具体位置：Section 2 (Related Work lines 10-13), Introduction line 8
- 问题：论文正确指出 Yao et al. 用 hard-prompting、本文用 fine-tuned models。但更本质的差异——(1) separation of QE from selection, (2) degeneracy diagnosis, (3) difficulty gradient design——在 Related Work 中以 "the three questions we address" 一笔带过。Yao et al. 已经 demonstrate consistency-accuracy correlations for NER/RE；本文的核心增量不仅是 fine-tuned models，更是 "why QE ≠ selection"。这个叙事在 positioning 中不够突出。
- 建议：用一个更直接的对比句，如 "Yao et al. demonstrate that consistency correlates with accuracy; we show that this correlation is necessary but not sufficient for sample selection, and diagnose why."

**W4** [warning] Abstract 信息过载

- 具体位置：Abstract (9 sentences)
- 问题：9 句话中包含：5 signals, 3 signal families, 4 benchmarks, 2 mechanisms (degeneracy + compression), ρ=0.42, AUROC=0.82, 3 个 degeneracy 百分比 (10%/21%/58%), 3 个 selection gains (+1.36/+0.42/fail), p-values, LP nats (0.041), 4B-8B models。这远超审稿人在 30 秒内能吸收的信息密度。Abstract 读起来像 Results 的压缩版而非 story 的提炼。
- 建议：减少具体数字到 3-4 个最关键的（如仅保留 "ρ up to 0.4+, 13pp oracle headroom, 0 net selection gain"），将 degeneracy gradient 简化为一句话的 pattern description 而非 3 个 data points。

**W5** [warning] "correlation-selection gap" 操作性定义位置太晚

- 具体位置：Section 4.3 line 76 (first formal definition)
- 问题：术语从 Abstract 开始使用（"quality estimation does not translate to structural selection---the correlation-selection gap"），但正式操作性定义直到 Section 4.3 第一行才出现（"We define the correlation-selection gap as the disparity between a signal's instance-level rank correlation with F1 and its ability to select the best output from N candidates."）。Introduction 和 Abstract 中的使用依赖读者从上下文推断含义。
- 建议：在 Introduction 首次使用该术语时（line 12）插入一句 operational definition，或至少在括号中给出精确含义。

**W6** [warning] Scale claims 措辞需更保守

- 具体位置：Title ("Fail to Scale"), Conclusion, Limitations
- 问题：标题声称信号 "fail to scale" structured IE，但实验仅覆盖 4B-8B（3 models）。"Scale" 在 LLM 语境中通常暗示 model scale（7B → 70B → 400B+），而本文仅测试 4B 和 8B。Limitations 正确承认 70B+ 未测试，但标题的 "fail to scale" 语义更广，可能被误读为跨 model scale 的 general claim。
- 建议：考虑将标题中 "Scale" 改为更精确的措辞（如 "Fail for Structured Information Extraction" 或 "Fail in Structured Selection"），或在 Introduction 中 upfront 限定 scale range。

### Minor Issues（不影响接收）

**M1.** LaTeX em-dash (---) 使用频率：正文 sections 共 ~40 处（不含 appendix），密度偏高但大多是合理的 parenthetical。Introduction line 33 的嵌套 em-dash 结构 ("We trace this to two mechanisms---instance degeneracy...---and confirm via a diagnostic chain...") 是最长的一处，建议拆分为独立句子。

**M2.** "-ing" 分词短语：Discussion line 96 "yet tends to select the most typical rather than the best output---consistent with MBR's known mode-seeking bias" — "consistent with" 分词悬挂不严重但可改为独立从句。整体 -ing 使用不泛滥。

**M3.** 术语 "instance degeneracy" 虽有 clear definition (all N samples produce identical F1)，但 "degeneracy" 在物理学/数学中有不同含义。读者可能需要一瞬间适应。可考虑 "output convergence" 或 "sample collapse" 作为替代。

**M4.** Table 5 (fewnerd) 中 SciERC greedy = 0.614 vs Table 3 greedy = 0.645，footnote 解释了是 full-set vs gold-filtered 的差异，但同一数据集两张表格不同数值仍然容易造成混淆。

**M5.** Ethics Statement 提到 "Code and data will be released upon acceptance at [anonymized URL]" — 这是 camera-ready 信息，review 版应确认不包含 de-anonymizing 信息。

---

## Questions for Authors

Q1. Figure 1 caption 声称 "ρ up to 0.42 on primary test bed"，但 Table 1 显示 SciERC（declared primary test bed）最高 ρ = VC 0.379。这个 0.42 具体来自哪个 configuration？是否混淆了 Few-NERD 的数值？

Q2. 如果 instance degeneracy 是 fine-tuning 带来的副产物（且随 model capability 增加而加重），那 70B+ 模型的 degeneracy 是否会更严重？这是否意味着本文的 negative conclusion 在更大模型上只会更强？还是存在 non-monotonic 的可能？

Q3. 您观察到 LoRA rank=8 时 degeneracy 从 21% 降至 7%，但 LP selection 仍然失败。这是否暗示 LP compression 比 degeneracy 更 fundamental？为什么 Discussion 中仍将 degeneracy 作为 primary 诊断而非 LP compression？

Q4. Few-NERD 的 low degeneracy (10%) despite high performance (75% F1) 被归因于 "dataset-specific factors (number of entity types, semantic overlap)"。这是一个重要的 confound：如果 degeneracy 主要由 dataset 特性决定而非 model capability，那 degeneracy-LP 的 monotonic relationship 可能是 spurious correlation（confounded by dataset difficulty/characteristics）。仅 3 个 data points 无法排除这一 confound。

---

## Missing References

1. **Wan et al. (2023)** "GPT-RE: In-context Learning for Relation Triple Extraction using Large Language Models" — direct competitor in LLM-based RE
2. **Xu et al. (2024)** "Large Language Models for Generative Information Extraction: A Survey" — comprehensive survey of generative IE that would strengthen Related Work coverage
3. **Li et al. (2024)** "LLM-NER: Named Entity Recognition with Large Language Models" 或类似 2024-2025 generative NER survey work
4. **Amini et al. (2024) / Shi et al. (2024)** — NER uncertainty estimation with ensemble methods
5. **Bertsch et al. (2024)** "In-Context Learning with Long-Context Models: An In-Depth Exploration" — relevant for understanding why hard-prompting vs fine-tuning produces different behaviors

当前 58 个引用对 EMNLP 长文偏少（typical: 50-70），覆盖面合理但 2025-2026 generative NER/IE survey 和 token-level uncertainty 方向可补充���

---

## Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验本身严谨，但 "gap" 的 framing 将定义性限制与实验发现混合，核心数值 (ρ=0.42) 有报告不一致 |
| Excitement | 3.0/5 | Negative result 有价值但增量受限——MBR 社区已知 MBR 非万能；fine-tuned NER 的 degeneracy 诊断是新的但 scope 窄 |
| Overall | 3.0/5 | Findings-level paper. 实验质量高但新颖性需要更精确的 framing 来 justify main conference |
| Confidence | 4/5 | 熟悉 NER、self-consistency、MBR decoding 和 uncertainty estimation 领域 |

**一句话总结：** 实验设计和诊断链出色，但核心 "correlation-selection gap" 的新颖性被定义性成分稀释，headline 数值有内部不一致，建议修正 framing 后投 Findings。

**Recommendation: 3.0 — Findings acceptance**（需修正 N1-N3 后方可接收；当前 framing 下 main conference excitement 不足）

---

[Reviewer 2 审稿结果]:
审稿报告已提交。

核心发现：
- **N1 (critical)**: "correlation-selection gap" 对 structural signals 有 tautological 成分（instance-level signals by construction 无法区分候选），需要更精确区分定义性限制 vs 实验发现
- **N2 (critical)**: ρ=0.42 headline 在论文内部不一致——Figure 1 caption 和多处声称此值来自 "primary test bed"(SciERC)，但 Table 1 显示 SciERC 最高仅 0.379
- **N3 (critical)**: 与 MBR 社区已知结论（Eikema et al. 2025）的增量需要更明确 articulate

整体评分 3.0/5，建议 Findings-level 接收，需修正 framing 和数值一致性问题。

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

_source line 1587 · 2026-05-17T06:22:39.355332+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "16",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 16 审稿报告。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** — 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** — 反驳，并提供证据\n\n特别关注：\n- R1 的统计方法论批评（sign test power, monotonic claim, Bonferroni scope）与你的 framing/novelty 批评是否一致\n- 你是否认同 R1 的 3.5/5 评分，还是认为更高/更低\n\n---\n\n## Reviewer 1 完整审稿原文：\n\n## Round 16 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## Summary\n\nThis paper evaluates five confidence signals (four instance-level, one per-sample) for quality estimation and sample selection in LLM-based NER. It demonstrates that while all signals achieve reliable quality estimation (ρ up to 0.42, AUROC up to 0.82), none translates QE into effective best-of-N selection—the \"correlation-selection gap.\" Two mechanisms are identified: instance degeneracy (10–58% identical outputs) and LP compression (median range 0.041 nats). The degeneracy-gating pattern across three datasets shows LP selection effectiveness is inversely related to degeneracy rate. The paper is thorough, well-structured, and makes a genuine negative-result contribution with extensive ablations.\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5 (borderline Findings/Conference)\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] 2-seed paired sign test 的统计效力严重不足\n\n- 具体位置：Section 4.3 (Table 2), footnote 4, §4.1 footnote\n- 问题：Selection 的核心结论\"no signal significantly outperforms greedy\"基于 2-seed paired sign test。Sign test 是最保守的非参数检验（仅使用方向信息，丢弃幅度信息），在 2-seed 设定下几乎无法检测到真实效应。如果 LP 真的有 +0.2pp 的效应，sign test 在 n=529、2 seeds 下的 power 极低。这意味着 p=0.29 可能是 under-powered null 而非 true null。\n- 为什么影响接收：核心负面结论（\"selection fails\"）的统计基础不牢靠。审稿人无法区分\"效应不存在\"和\"检验无力检测到效应\"。\n- 建议修改方向：(1) 使用 paired bootstrap test（B=10,000）替代 sign test；(2) 增加 seed 数至 5+ 或报告 power analysis；(3) 明确区分 \"no evidence of effect\" 与 \"evidence of no effect\"。\n\n**N2** [critical] Degeneracy-gating 的 monotonic pattern 仅基于 3 个数据点\n\n- 具体位置：Table 4 (§4.4), Abstract line 7, Conclusion line 7, Figure 3\n- 问题：核心 claim \"instance degeneracy monotonically predicts LP selection effectiveness\" 来自 CoNLL(58%→fail), SciERC(21%→+0.42pp), Few-NERD(10%→+1.36pp) 三个数据点。3 点的 monotonic trend 在统计上不具有意义——任意 3 个不同值必然可以排出 monotonic order。论文自己报告 Spearman ρ=−0.57, p=0.066 (n=11, Figure 3 caption)，即未达到 α=0.05 显著水平。\n- 建议修改方向：(1) 将语言从 \"monotonically predicts\" 降级为 \"is consistent with a monotonic relationship\"；(2) 补充 per-type 分析的正式统计；(3) 承认这是 exploratory observation 而非 confirmed mechanism。\n\n**N3** [critical] Bonferroni correction scope 与 post-hoc ε 选择的交互\n\n- 具体位置：§4.3 footnote 4, Appendix Table 8 (ε sweep)\n- 问题：论文声称 non-tied LP subset 的 +2.9pp (p=0.004) \"survives Bonferroni correction over 5 comparisons\" (p_adj=0.020)。但 Bonferroni scope 仅覆盖 5 signal comparisons，未纳入 ε threshold 的 post-hoc 选择。Table 8 展示了 7 个 ε 值的 sweep (0.01–0.20)，且 ε=0.05 被选择恰恰因为它 \"yields the strongest statistical separation\"。如果将 7 个 ε × 5 signals = 35 comparisons 纳入 Bonferroni，p_adj = 0.004 × 35 = 0.14，不再显著。\n- 建议修改方向：(1) 明确承认 ε=0.05 是 post-hoc 选择；(2) 使用 pre-registered split 或 permutation-based FDR 控制；(3) 主文 footnote 4 和 Limitations 保持一致。\n\n---\n\n## Should-Fix 问题\n\n**W1** Random baseline (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距缺乏理论解释\n\n**W2** Kendall's W=1.0 with only 3 seeds 的 precision caveat 不充分\n\n**W3** Instance degeneracy 8B(21%) vs 4B(10.4%): capability vs fine-tuning recipe confound\n\n**W4** TOST 等价性结论的 configuration-dependent 呈现不平衡\n\n**W5** Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n---\n\n## 小问题\n\n- §4.1: \"3-seed stability σ≤0.026\" — σ 是 sample std 还是 population std?\n- Table 2: EM 的 p 值为 \"---\" 而非数字\n- Appendix Table 12: Kendall's W=0.822 for RE at N=8 暗示 RE rankings 不如 NER stable\n- §Discussion \"Hypotheses for LP compression\" 排序 (b)(c)(a)(d) 似有意但未解释\n- Figure 3 caption: n=11 混合不同粒度数据点，可能违反 independence 假设\n\n---\n\n## Questions for Authors\n\n1. 2-seed sign test 的 power analysis: 在 effect size d=0.038 下，sign test with n=529 的 power 是多少？\n2. ε=0.05 threshold：如果 pre-register median LP range (0.041) 作为 split point，non-tied subset 的 selection gain 是否仍然显著？\n3. Degeneracy 的 operationalization: 如果用 F1 range < 0.01 (soft threshold)，monotonic pattern 是否 robust？\n4. Few-NERD 训练只用了 3 epochs (vs 其他 datasets 的 5 epochs)——这是否影响 degeneracy rate？\n\n---\n\n## Missing References\n\n- Freitag et al. (2023) \"Results of WMT23 Metrics Shared Task\"\n- Li et al. (2024) \"Confidence Estimation for LLM-Based Dialogue State Tracking\"\n- Xu et al. (2024) \"Rejection Improves Reliability\"\n- Derczynski et al. (2016) \"Broad Twitter Corpus\"\n\n---\n\n## Overall Assessment\n\n**Score: 3.5/5** (between Findings and Conference)\n实证工作扎实、消融全面，但核心 degeneracy-gating claim 的统计支撑仅有 3 个数据点，且多处统计方法论存在可改进空间。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 16 审稿报告。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** — 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** — 反驳，并提供证据\n\n特别关注：\n- R1 的统计方法论批评（sign test power, monotonic claim, Bonferroni scope）与你的 framing/novelty 批评是否一致\n- 你是否认同 R1 的 3.5/5 评分，还是认为更高/更低\n\n---\n\n## Reviewer 1 完整审稿原文：\n\n## Round 16 审稿报告 — Reviewer 1（方法严谨性 + 实验设计 + 统计方法论）\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)\n\n---\n\n## Summary\n\nThis paper evaluates five confidence signals (four instance-level, one per-sample) for quality estimation and sample selection in LLM-based NER. It demonstrates that while all signals achieve reliable quality estimation (ρ up to 0.42, AUROC up to 0.82), none translates QE into effective best-of-N selection—the \"correlation-selection gap.\" Two mechanisms are identified: instance degeneracy (10–58% identical outputs) and LP compression (median range 0.041 nats). The degeneracy-gating pattern across three datasets shows LP selection effectiveness is inversely related to degeneracy rate. The paper is thorough, well-structured, and makes a genuine negative-result contribution with extensive ablations.\n\n---\n\n## 总体评分\n\n**Overall**: 3.5/5 (borderline Findings/Conference)\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] 2-seed paired sign test 的统计效力严重不足\n\n- 具体位置：Section 4.3 (Table 2), footnote 4, §4.1 footnote\n- 问题：Selection 的核心结论\"no signal significantly outperforms greedy\"基于 2-seed paired sign test。Sign test 是最保守的非参数检验（仅使用方向信息，丢弃幅度信息），在 2-seed 设定下几乎无法检测到真实效应。如果 LP 真的有 +0.2pp 的效应，sign test 在 n=529、2 seeds 下的 power 极低。这意味着 p=0.29 可能是 under-powered null 而非 true null。\n- 为什么影响接收：核心负面结论（\"selection fails\"）的统计基础不牢靠。审稿人无法区分\"效应不存在\"和\"检验无力检测到效应\"。\n- 建议修改方向：(1) 使用 paired bootstrap test（B=10,000）替代 sign test；(2) 增加 seed 数至 5+ 或报告 power analysis；(3) 明确区分 \"no evidence of effect\" 与 \"evidence of no effect\"。\n\n**N2** [critical] Degeneracy-gating 的 monotonic pattern 仅基于 3 个数据点\n\n- 具体位置：Table 4 (§4.4), Abstract line 7, Conclusion line 7, Figure 3\n- 问题：核心 claim \"instance degeneracy monotonically predicts LP selection effectiveness\" 来自 CoNLL(58%→fail), SciERC(21%→+0.42pp), Few-NERD(10%→+1.36pp) 三个数据点。3 点的 monotonic trend 在统计上不具有意义——任意 3 个不同值必然可以排出 monotonic order。论文自己报告 Spearman ρ=−0.57, p=0.066 (n=11, Figure 3 caption)，即未达到 α=0.05 显著水平。\n- 建议修改方向：(1) 将语言从 \"monotonically predicts\" 降级为 \"is consistent with a monotonic relationship\"；(2) 补充 per-type 分析的正式统计；(3) 承认这是 exploratory observation 而非 confirmed mechanism。\n\n**N3** [critical] Bonferroni correction scope 与 post-hoc ε 选择的交互\n\n- 具体位置：§4.3 footnote 4, Appendix Table 8 (ε sweep)\n- 问题：论文声称 non-tied LP subset 的 +2.9pp (p=0.004) \"survives Bonferroni correction over 5 comparisons\" (p_adj=0.020)。但 Bonferroni scope 仅覆盖 5 signal comparisons，未纳入 ε threshold 的 post-hoc 选择。Table 8 展示了 7 个 ε 值的 sweep (0.01–0.20)，且 ε=0.05 被选择恰恰因为它 \"yields the strongest statistical separation\"。如果将 7 个 ε × 5 signals = 35 comparisons 纳入 Bonferroni，p_adj = 0.004 × 35 = 0.14，不再显著。\n- 建议修改方向：(1) 明确承认 ε=0.05 是 post-hoc 选择；(2) 使用 pre-registered split 或 permutation-based FDR 控制；(3) 主文 footnote 4 和 Limitations 保持一致。\n\n---\n\n## Should-Fix 问题\n\n**W1** Random baseline (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距缺乏理论解释\n\n**W2** Kendall's W=1.0 with only 3 seeds 的 precision caveat 不充分\n\n**W3** Instance degeneracy 8B(21%) vs 4B(10.4%): capability vs fine-tuning recipe confound\n\n**W4** TOST 等价性结论的 configuration-dependent 呈现不平衡\n\n**W5** Gold-empty instance filtering 在 QE 和 Selection 之间的不一致\n\n---\n\n## 小问题\n\n- §4.1: \"3-seed stability σ≤0.026\" — σ 是 sample std 还是 population std?\n- Table 2: EM 的 p 值为 \"---\" 而非数字\n- Appendix Table 12: Kendall's W=0.822 for RE at N=8 暗示 RE rankings 不如 NER stable\n- §Discussion \"Hypotheses for LP compression\" 排序 (b)(c)(a)(d) 似有意但未解释\n- Figure 3 caption: n=11 混合不同粒度数据点，可能违反 independence 假设\n\n---\n\n## Questions for Authors\n\n1. 2-seed sign test 的 power analysis: 在 effect size d=0.038 下，sign test with n=529 的 power 是多少？\n2. ε=0.05 threshold：如果 pre-register median LP range (0.041) 作为 split point，non-tied subset 的 selection gain 是否仍然显著？\n3. Degeneracy 的 operationalization: 如果用 F1 range < 0.01 (soft threshold)，monotonic pattern 是否 robust？\n4. Few-NERD 训练只用了 3 epochs (vs 其他 datasets 的 5 epochs)——这是否影响 degeneracy rate？\n\n---\n\n## Missing References\n\n- Freitag et al. (2023) \"Results of WMT23 Metrics Shared Task\"\n- Li et al. (2024) \"Confidence Estimation for LLM-Based Dialogue State Tracking\"\n- Xu et al. (2024) \"Rejection Improves Reliability\"\n- Derczynski et al. (2016) \"Broad Twitter Corpus\"\n\n---\n\n## Overall Assessment\n\n**Score: 3.5/5** (between Findings and Conference)\n实证工作扎实、消融全面，但核心 degeneracy-gating claim 的统计支撑仅有 3 个数据点，且多处统计方法论存在可改进空间。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
```

</details>

---


### Tool result

_source line 1588 · 2026-05-17T06:23:24.871866+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 45516
}
```

</details>

---


### Tool call

_source line 1589 · 2026-05-17T06:23:25.273596+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "16",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 16 审稿��告。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** — 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** — 反驳，并提供证据\n\n特别关注：\n- R2 对 tautological framing (N1) 的批评与你的 N2 (monotonic pattern) 是否有 tension\n- R2 发现的 ρ=0.42 数值不一致 (N2) 你是否验证\n- 你对 R2 的 3.0/5 评分是否同意（你给了 3.5）\n\n---\n\n## Reviewer 2 完整审稿原文：\n\n## Round 16 审稿报告 — Reviewer 2（新颖性 + 贡献定位 + 相关工作 + 写作质量）\n\n---\n\n## Summary\n\n本文研究 self-consistency 信号在 LLM-based NER 中的质量估计（QE）与样本选择（selection）效果。作者评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 4 个 NER benchmark 上的表现，发现：信号可有效预测实例级质量（ρ up to ~0.42），但无法有效选择 best-of-N 候选（\"correlation-selection gap\"）。文章诊断出两个机制：instance degeneracy 和 LP compression，并展示 degeneracy 单调预测 LP selection 有效性。\n\n论文实验设计系统、分析细致，诊断链（LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination）令人印象深刻。但新颖性存在结构性问题：核心 \"gap\" 部分是定义性质的（instance-level signals by construction 无法区分候选），且与 MBR 社区已知限制有重叠。\n\n---\n\n## Strengths\n\n**S1.** 4 个 benchmark 形成 difficulty gradient，每个有明确角色定位。2 个模型族 + 4B scale ablation 提供跨架构证据。\n**S2.** 诊断深度出色：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 → entity-token LP 排除 → supervised combination 确认 feature space bottleneck。\n**S3.** Negative result 对 NER practitioners 有实际意义。\n**S4.** 统计方法使用适当。Non-tied subset 分析的 post-hoc 性质在 limitations 中有坦诚说明。\n**S5.** Few-NERD 对比实验利用 degeneracy 差异形成跨 dataset 自然实验。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] Correlation-selection gap 的新颖性存在 tautological 成分\n\n- Section 3.1 明确写道：\"4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates.\" 既然 instance-level signals BY CONSTRUCTION 对同一 input 的所有候选给出相同分数，它们当然无法做 selection。将其转化为 MBR/consensus-proximity 选择后依然失败，才是真正的 empirical finding。但论文 framing 将两者混为一谈——标题暗示这是一个意外发现。\n- 建议：明确在 Introduction 中区分 \"definitional limitation\" 和 \"empirical finding\"（MBR with positive utility correlation fails due to degeneracy; LP fails due to compression）。\n\n**N2** [critical] ρ=0.42 headline claim 存在数值不一致\n\n- Abstract 说 \"ρ up to 0.42 on Few-NERD and the primary test bed\"；Figure 1 caption 说 \"ρ up to 0.45 on CoNLL, 0.42 on primary test bed\"。但 Table 1 显示 SciERC（primary test bed）最高 ρ = VC 0.379。ρ=0.42 来自 Few-NERD LP (0.421)。Contribution 1 正确写 \"VC ρ=0.38 on the primary test bed\"。内部矛盾损害可信度。\n- 建议：统一所有 headline 数值。若 primary = SciERC，上界应为 0.38（N=8）。\n\n**N3** [critical] 与 MBR 社区已知结论的增量不够清晰\n\n- Eikema et al. (2025) 已讨论 MBR utilities degrade on structured outputs。本文核心增量——positive within-instance utility correlation (ρ=0.52) 不导致 selection gains because of degeneracy——需要更明确 articulate。即：Eikema 认为问题在 utility design，本文证明即使 utility IS aligned (ρ=0.52)，degeneracy 也会 eliminate headroom。\n- 建议：Related Work 增加一个 differentiation paragraph。\n\n---\n\n## Should-Fix 问题\n\n**W1** Few-NERD LP +1.36pp 作为 positive finding 仅有 1 model × 1 N × 1 dataset 的证据。\n\n**W2** Soft Jaccard 命名有误导性（分母 max 而非 union）。\n\n**W3** 与 Yao et al. (2026) 的差异化不充分——核心增量不仅是 fine-tuned models，更是 \"why QE ≠ selection\"。\n\n**W4** Abstract 信息过载（9 句话塞入过多技术细节和数字）。\n\n**W5** \"correlation-selection gap\" 操作性定义位置太晚（Section 4.3 才出现）。\n\n**W6** Scale claims 措辞——标题 \"Fail to Scale\" 暗示 model scale，但仅测试 4B-8B。\n\n---\n\n## Minor Issues\n\n- M1: em-dash 使用 ~40 处，Introduction line 33 嵌套 em-dash 需拆分\n- M2: Discussion line 96 -ing 分词可改为独立从句\n- M3: \"instance degeneracy\" 术语可能与物理学/数学含义混淆\n- M4: Table 5 vs Table 3 SciERC greedy 数值不同（full-set vs gold-filtered）\n- M5: Ethics Statement 含 camera-ready 信息\n\n---\n\n## Questions for Authors\n\nQ1. Figure 1 caption \"ρ up to 0.42 on primary test bed\" 具体来自哪个 configuration？与 Table 1 SciERC max ρ=0.379 矛盾。\nQ2. 70B+ 模型 degeneracy 是否更严重？non-monotonic 可能？\nQ3. LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败——是否暗示 LP compression 比 degeneracy 更 fundamental？\nQ4. Few-NERD low degeneracy (10%) 可能由 dataset 特性（entity types, semantic overlap）而非 model capability 决定，3 个 data points 无法排除 confound。\n\n---\n\n## Missing References\n\n1. Wan et al. (2023) \"GPT-RE\"\n2. Xu et al. (2024) \"Large Language Models for Generative Information Extraction: A Survey\"\n3. Li et al. (2024) \"LLM-NER\" 或类似 generative NER survey\n4. Amini et al. (2024) / Shi et al. (2024) — NER uncertainty estimation with ensemble methods\n5. Bertsch et al. (2024) \"In-Context Learning with Long-Context Models\"\n\n---\n\n## Overall Assessment\n\n**Score: 3.0/5** (Findings-level)\n实验设计和诊断链出色，但核心 \"correlation-selection gap\" 的新颖性被定义性成分稀释，headline 数值有内部不一致。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 16 审稿��告。请逐条回应其 Must-Fix 和 Should-Fix 问题：\n- **[AGREE]** — 同意，并说明理由（cite 具体 Section/Table/Figure）\n- **[REBUT]** — 反驳，并提供证据\n\n特别关注：\n- R2 对 tautological framing (N1) 的批评与你的 N2 (monotonic pattern) 是否有 tension\n- R2 发现的 ρ=0.42 数值不一致 (N2) 你是否验证\n- 你对 R2 的 3.0/5 评分是否同意（你给了 3.5）\n\n---\n\n## Reviewer 2 完整审稿原文：\n\n## Round 16 审稿报告 — Reviewer 2（新颖性 + 贡献定位 + 相关工作 + 写作质量）\n\n---\n\n## Summary\n\n本文研究 self-consistency 信号在 LLM-based NER 中的质量估计（QE）与样本选择（selection）效果。作者评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 4 个 NER benchmark 上的表现，发现：信号可有效预测实例级质量（ρ up to ~0.42），但无法有效选择 best-of-N 候选（\"correlation-selection gap\"）。文章诊断出两个机制：instance degeneracy 和 LP compression，并展示 degeneracy 单调预测 LP selection 有效性。\n\n论文实验设计系统、分析细致，诊断链（LoRA-rank ablation、free-form decoding、entity-token LP、supervised combination）令人印象深刻。但新颖性存在结构性问题：核心 \"gap\" 部分是定义性质的（instance-level signals by construction 无法区分候选），且与 MBR 社区已知限制有重叠。\n\n---\n\n## Strengths\n\n**S1.** 4 个 benchmark 形成 difficulty gradient，每个有明确角色定位。2 个模型族 + 4B scale ablation 提供跨架构证据。\n**S2.** 诊断深度出色：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 → entity-token LP 排除 → supervised combination 确认 feature space bottleneck。\n**S3.** Negative result 对 NER practitioners 有实际意义。\n**S4.** 统计方法使用适当。Non-tied subset 分析的 post-hoc 性质在 limitations 中有坦诚说明。\n**S5.** Few-NERD 对比实验利用 degeneracy 差异形成跨 dataset 自然实验。\n\n---\n\n## Must-Fix 问题\n\n**N1** [critical] Correlation-selection gap 的新颖性存在 tautological 成分\n\n- Section 3.1 明确写道：\"4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates.\" 既然 instance-level signals BY CONSTRUCTION 对同一 input 的所有候选给出相同分数，它们当然无法做 selection。将其转化为 MBR/consensus-proximity 选择后依然失败，才是真正的 empirical finding。但论文 framing 将两者混为一谈——标题暗示这是一个意外发现。\n- 建议：明确在 Introduction 中区分 \"definitional limitation\" 和 \"empirical finding\"（MBR with positive utility correlation fails due to degeneracy; LP fails due to compression）。\n\n**N2** [critical] ρ=0.42 headline claim 存在数值不一致\n\n- Abstract 说 \"ρ up to 0.42 on Few-NERD and the primary test bed\"；Figure 1 caption 说 \"ρ up to 0.45 on CoNLL, 0.42 on primary test bed\"。但 Table 1 显示 SciERC（primary test bed）最高 ρ = VC 0.379。ρ=0.42 来自 Few-NERD LP (0.421)。Contribution 1 正确写 \"VC ρ=0.38 on the primary test bed\"。内部矛盾损害可信度。\n- 建议：统一所有 headline 数值。若 primary = SciERC，上界应为 0.38（N=8）。\n\n**N3** [critical] 与 MBR 社区已知结论的增量不够清晰\n\n- Eikema et al. (2025) 已讨论 MBR utilities degrade on structured outputs。本文核心增量——positive within-instance utility correlation (ρ=0.52) 不导致 selection gains because of degeneracy——需要更明确 articulate。即：Eikema 认为问题在 utility design，本文证明即使 utility IS aligned (ρ=0.52)，degeneracy 也会 eliminate headroom。\n- 建议：Related Work 增加一个 differentiation paragraph。\n\n---\n\n## Should-Fix 问题\n\n**W1** Few-NERD LP +1.36pp 作为 positive finding 仅有 1 model × 1 N × 1 dataset 的证据。\n\n**W2** Soft Jaccard 命名有误导性（分母 max 而非 union）。\n\n**W3** 与 Yao et al. (2026) 的差异化不充分——核心增量不仅是 fine-tuned models，更是 \"why QE ≠ selection\"。\n\n**W4** Abstract 信息过载（9 句话塞入过多技术细节和数字）。\n\n**W5** \"correlation-selection gap\" 操作性定义位置太晚（Section 4.3 才出现）。\n\n**W6** Scale claims 措辞——标题 \"Fail to Scale\" 暗示 model scale，但仅测试 4B-8B。\n\n---\n\n## Minor Issues\n\n- M1: em-dash 使用 ~40 处，Introduction line 33 嵌套 em-dash 需拆分\n- M2: Discussion line 96 -ing 分词可改为独立从句\n- M3: \"instance degeneracy\" 术语可能与物理学/数学含义混淆\n- M4: Table 5 vs Table 3 SciERC greedy 数值不同（full-set vs gold-filtered）\n- M5: Ethics Statement 含 camera-ready 信息\n\n---\n\n## Questions for Authors\n\nQ1. Figure 1 caption \"ρ up to 0.42 on primary test bed\" 具体来自哪个 configuration？与 Table 1 SciERC max ρ=0.379 矛盾。\nQ2. 70B+ 模型 degeneracy 是否更严重？non-monotonic 可能？\nQ3. LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败——是否暗示 LP compression 比 degeneracy 更 fundamental？\nQ4. Few-NERD low degeneracy (10%) 可能由 dataset 特性（entity types, semantic overlap）而非 model capability 决定，3 个 data points 无法排除 confound。\n\n---\n\n## Missing References\n\n1. Wan et al. (2023) \"GPT-RE\"\n2. Xu et al. (2024) \"Large Language Models for Generative Information Extraction: A Survey\"\n3. Li et al. (2024) \"LLM-NER\" 或类似 generative NER survey\n4. Amini et al. (2024) / Shi et al. (2024) — NER uncertainty estimation with ensemble methods\n5. Bertsch et al. (2024) \"In-Context Learning with Long-Context Models\"\n\n---\n\n## Overall Assessment\n\n**Score: 3.0/5** (Findings-level)\n实验设计和诊断链出色，但核心 \"correlation-selection gap\" 的新颖性被定义性成分稀释，headline 数值有内部不一致。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
```

</details>

---


### Tool result

_source line 1590 · 2026-05-17T06:23:26.683708+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1410
}
```

</details>

---


### Assistant

_source line 1591 · 2026-05-17T06:23:38.784554+00:00_

交叉分享任务已分配。等待两位 Reviewer 完成逐条回应后进入收敛判断。

**当前 Round 16 进度：**
- Step 1 ✓ — R1 (3.5/5) + R2 (3.0/5) 独立初审完成
- Step 2 → 交叉分享已发出，等待回应
- Step 3 — 收敛判断（待交叉回应到达）
- Step 4 — 汇总报告

**初步观察（两位 Reviewer 共识方向）：**
1. **Framing tautology** — R1-N2 + R2-N1 一致：instance-level signals 的 selection failure 部分是定义性的
2. **统计效力** — R1-N1 (2-seed sign test) 是 R1 独有的强关注点，R2 仅作 should-fix
3. **数值不一致** — R2-N2 (ρ=0.42 vs 0.379) 是新发现，R1 未直接提及
4. **Degeneracy 3 data points** — R1-N2 + R2-Q4 方向一致
5. **Bonferroni scope** — R1-N3，R2 的 S4 反而 praise 统计方法——可能有 tension

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 127

## Round 127

2 recorded events


### User

_source line 1592 · 2026-05-17T06:28:10.976951+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 逐条回应 Reviewer 2 审稿意见

---

### Must-Fix 问题

**[AGREE] R2-N1: Correlation-selection gap 的 tautological 成分**

同意 R2 的核心判断。我验证了 Section 3.1 原文明确写道："4 of 5 signals are instance-level aggregates that assign identical QE scores to all N candidates"，Introduction 也重复了这一表述。既然论文自己承认 4/5 信号 by construction 无法区分候选，那么这些信号"无法做 selection"确实是定义性结论而非经验发现。

但我要补充一个 nuance：论文的真正 empirical contribution 是两部分——(a) 将 instance-level signals 转化为 MBR/consensus-proximity 选择后仍然失败（因 degeneracy），(b) LP 作为唯一 per-sample signal 也失败（因 compression）。问题在于论文 framing 把这两个不同层次的发现混在一起，用同一个 "gap" 标签包装，造成新颖性被稀释的印象。

**与我的 N2（monotonic pattern）的关系**：没有 tension。R2 指出 instance-level gap 是定义性的，我指出 degeneracy→LP failure 的关系是描述性的（缺乏机制解释）。两者从不同角度指向同一问题：论文需要更精确地界定哪些是 definitional, 哪些是 empirical, 哪些是 mechanistic contribution。建议作者在修改时明确分层。

---

**[AGREE] R2-N2: ρ=0.42 headline claim 数值不一致**

完全同意，且我已独立验证。具体发现：

- Abstract: "ρ up to 0.42 on Few-NERD and the primary test bed" — 措辞暗示两个 dataset 都达到 0.42
- Figure 1 caption: "ρ up to 0.45 on CoNLL, 0.42 on primary test bed" — 直接声称 primary test bed 达到 0.42
- Table 1 实际数据: SciERC（primary test bed）最高 ρ = VC 0.379
- Few-NERD: LP ρ = 0.421（Section 4.3 inline）— 这才是 0.42 的来源
- Contribution 1: "VC ρ=0.38 on the primary test bed" — 这个是正确的

结论：0.42 只能归属于 Few-NERD LP，不能归属于 SciERC。Figure 1 caption 的 "0.42 on primary test bed" 与 Table 1 矛盾（差 0.04），Abstract 的合并表述进一步放大了混淆。这是一个实质性的数值一致性问题，不是四舍五入误差。Contribution 1 的 "ρ=0.38" 反而是正确的，说明作者在不同位置使用了不同数据源却未统一校验。

这个问题在我的 Round 16 审稿中没有独立发现，感谢 R2 的细致核查。

---

**[AGREE with nuance] R2-N3: 与 MBR 社区已知结论的增量不清晰**

同意需要更明确的 differentiation。R2 准确指出了本文的真正增量：Eikema et al. (2025) 认为问题在 utility design，本文证明即使 utility IS aligned (within-instance ρ=0.52)，degeneracy 也会 eliminate headroom。这个 distinction 确实是本文的核心贡献之一，但目前在 Related Work 中不够突出。

补充：本文场景（NER structured output）与 MBR 文献的典型场景（MT/summarization）有本质差异——NER 的离散标签空间导致更极端的 degeneracy。这个 structural argument 也应该在 positioning 中被强调。

---

### Should-Fix 问题

**[AGREE] R2-W1: Few-NERD LP +1.36pp 证据单薄**

同意。仅 1 model × 1 N × 1 dataset 的 positive finding 不足以支撑将其作为"LP can work when degeneracy is low"的通用结论。需要至少说明是 suggestive evidence 而非 demonstrated result。

**[AGREE] R2-W2: Soft Jaccard 命名误导**

同意。分母用 max 而非 union 确实不是标准 Jaccard 定义。建议改名或加注释说明。

**[AGREE] R2-W3: 与 Yao et al. (2026) 差异化不足**

同意。核心增量不仅是 fine-tuned models，更是"为什么 QE correlates but selection fails"的诊断，这在当前 Related Work 中没有被充分对比。

**[AGREE] R2-W4: Abstract 信息过载**

同意。Abstract 试图在 ~9 句中塞入过多技术细节（5 signals、4 benchmarks、degeneracy、LP compression、LoRA-rank ablation），导致核心 narrative 被稀释。

**[AGREE] R2-W5: "Correlation-selection gap" 操作性定义位置太晚**

同意，这与我的 Round 16 意见一致。核心概念在 Section 4.3 才正式定义，但 Abstract 和 Introduction 已经大量使用。建议在 Section 3 或 Introduction 末尾给出 operational definition。

**[REBUT] R2-W6: Scale claims 措辞**

部分反驳。标题 "Fail to Scale" 在论文语境中不仅指 model scale，也指 sample count（N=4→16）和 signal sophistication（从单一到组合）。虽然 4B-8B 确实不覆盖大模型，但论文 Section 4.2 明确标注了 ablation 范围，且 title 的 "scale" 更多是指 "scaling up effort does not help"（增加 N、增加信号复杂度）。不过我承认这个双关可能误导读者，建议作者在 Abstract 中加一句澄清 "scale" 的具体含义。

---

### 关于评分差异（R2: 3.0 vs R1: 3.5）

R2 给 3.0 的核心理由是 tautological framing 稀释新颖性。我理解这个逻辑，但仍维持 3.5，理由如下：

1. **诊断链的完整性仍有独立价值**：即使 instance-level gap 是定义性的，从 degeneracy 量化 → LoRA-rank 解耦 → LP compression 诊断 → supervised combination 确认 feature bottleneck 的完整链条，在 NER 领域是 novel 的实证工作
2. **Negative result 的实践意义**：对 NER practitioners 来说，知道"不要在 high-degeneracy 场景投入 selection effort"是 actionable insight
3. **数值不一致（N2）是可修复问题**：这影响 presentation 而非 scientific contribution

但如果作者无法在修改中清晰分层 definitional vs empirical contribution（N1），我会考虑下调至 3.0。

---

### 对 R2 Questions for Authors 的补充

**Q3 (LP compression vs degeneracy)**：这是一个非常好的问题，与我的 N2 直接相关。LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败——这暗示 LP compression 可能是独立于 degeneracy 的 bottleneck。论文目前将两者用 monotonic relationship 联系，但 Q3 指向的可能性（LP compression 是 more fundamental）应该在 Discussion 中被讨论。

**Q4 (Few-NERD confound)**：同意。3 个 data points (datasets) 无法排除 dataset-specific confounds。Few-NERD 的低 degeneracy 可能由 entity type 多样性或 semantic distinctiveness 驱动，而非 model capability 的反映。

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

_source line 1593 · 2026-05-17T06:28:18.389623+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 128

## Round 128

2 recorded events


### User

_source line 1594 · 2026-05-17T06:28:20.965240+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **N1 (tautological framing)**：同意，但补充了 empirical contribution 的分层（MBR conversion 失败 + LP compression）与我的 N2 互补而非冲突
- **N2 (ρ=0.42 不一致)**：完全同意并独立验证——Figure 1 caption 和 Abstract 声称 primary test bed 达到 0.42，但 Table 1 实际最大值为 0.379
- **N3 (MBR 增量)**：同意需要更明确的 differentiation paragraph
- **W1-W5**：全部同意
- **W6 (scale claims)**：部分反驳——"scale" 在论文中指 N/信号复杂度，不仅指 model scale
- **评分差异**：维持 3.5（vs R2 的 3.0），因诊断链完整性和实践意义仍有独立价值，但若 N1 修改不到位会下调

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

_source line 1595 · 2026-05-17T06:28:31.199311+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 129

## Round 129

8 recorded events


### User

_source line 1596 · 2026-05-17T06:34:28.588672+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 针对 Reviewer 1 Round 16 审稿报告

---

## Must-Fix 问题逐条回应

### [AGREE] R1-N1: 2-seed paired sign test 的统计效力不足

同意这是一个实质性方法论问题，但需补充两点 nuance：

**同意理由：** Sign test 仅使用方向信息，丢弃效应幅度，是最保守的非参数检验。在 effect size 仅为 +0.2pp 的情况下（Table 3, LP 0.647 vs Greedy 0.645），sign test 的 power 确实极低。论文无法区分 "true null" 和 "under-powered null"，这对核心负面结论构成威胁。

**补充观察：**
1. 论文在 §5 (Effect of sample count) 中报告了 N=32 时的 bootstrap significance testing (B=10,000)，得到 LP +0.95pp, p=0.031——这恰恰表明 sign test 确实 under-powered，因为用更强力的检验和更大 N 后效应变显著了。这实际上 *反驳了* 论文自身的 "selection fails" 叙事。
2. Few-NERD 结果 (+1.36pp, p<0.001, Table 4) 使用了 paired bootstrap 而非 sign test，说明作者已知 sign test 的局限但未统一方法。

**结论：** R1 的批评方向正确。但我认为影响程度比 R1 判断的稍轻——论文的核心故事不是 "LP 完全无效"，而是 "LP 在高 degeneracy 下无效、低 degeneracy 下有效"，后者用了更强的统计方法。问题在于 SciERC 上的 null result 表述过于绝对（§4.3 "no signal significantly outperforms greedy"），应改为 "effect is small and not reliably detected with current sample size"。

---

### [AGREE] R1-N2: Degeneracy-gating monotonic pattern 仅基于 3 个数据点

同意这是论文最薄弱的 claim 之一，但论文自身提供了部分缓解证据。

**同意理由：** 3 个数据点的 monotonic trend 在统计上无意义——任意 3 个不同值必然排出 monotonic order（概率=1/3 仅 3! 种排列中有 2 种 monotonic）。Figure 2 caption 自报 Spearman ρ=−0.57, p=0.066 (n=11)，未达 α=0.05。论文在 Abstract ("instance degeneracy monotonically predicts LP selection effectiveness") 和 Conclusion 中使用的 "monotonically predicts" 语言确实过强。

**部分缓解证据（论文自身提供但未充分强调）：**
- Figure 2 包含 n=11 数据点（3 dataset-level + 8 entity-type-level within Few-NERD），7/8 Few-NERD entity types 在 degeneracy <20% 时显示正 LP gains (§4.4)
- Per-entity-type 分析显示 Spearman ρ(degen, headroom)=−0.881, p=0.004 (§5, Appendix X)
- LoRA-rank ablation 从另一角度支持因果方向（rank↓ → degeneracy↓ → headroom↑）

**结论：** 我同意 R1 的建议——应将 "monotonically predicts" 降级为 "is consistent with a monotonic relationship" 或 "degeneracy is inversely associated with LP selection effectiveness"。但我认为 per-entity-type 分析（n=8, ρ=−0.881, p=0.004）比 R1 给予的信用更多，它不仅是 3 个点，而是在 controlled within-dataset setting 下的 8 个点。论文的问题是 **混合了不同粒度的证据** 而非 **完全没有证据**。

---

### [PARTIALLY REBUT] R1-N3: Bonferroni scope 与 post-hoc ε 选择

R1 的数学正确，但对论文的实际 claim 结构判断过严。

**R1 论点：** 7 ε × 5 signals = 35 comparisons → p_adj = 0.004 × 35 = 0.14，不再显著。

**反驳理由：**

1. **论文 Limitations 已明确承认 ε=0.05 是 post-hoc 选择：** §Limitations 原文："The ε=0.05 threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across ε ∈ [0, 0.2] (Appendix F), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy." 论文已将此定位为 diagnostic/exploratory，而非主 claim。

2. **ε 值之间高度相关（嵌套子集）：** ε=0.05 的子集完全包含于 ε=0.04 的子集之内。Bonferroni 假设独立比较，对嵌套比较过于保守。更合适的校正是 permutation-based FDR 或 step-down procedure。

3. **ε=0.05 有 a priori 动机：** 论文报告 median LP range = 0.041 nats (Table 18)。选择 ε≈median 作为 split point 有统计先验理由（中位数分割），不是纯粹 data-dredging。

4. **Non-tied subset 结果不是论文核心 claim：** 论文核心是负面结论（selection fails on full set）。Non-tied subset 分析的作用是 *诊断压缩机制*（"LP does carry per-sample discriminative information; compression is the bottleneck"），不是提出一个新的选择策略。

**部分同意：** Footnote 4 的表述确实过于自信——"survives Bonferroni correction over 5 comparisons" 应明确注明 "conditional on the pre-selected ε=0.05 threshold"。R1 关于 transparency 的要求合理。

**结论：** 这是一个 Should-Fix 而非 Must-Fix。论文已在 Limitations 中承认了这一点，且 non-tied analysis 定位为 diagnostic 而非 prescriptive。但 footnote 4 需要更诚实的措辞。

---

## Should-Fix 问题逐条回应

### [AGREE] R1-W1: Random (0.610) vs Greedy (0.645) 的 3.5pp 差距

同意这值得解释。Greedy (T=0) 是 argmax decoding，应该系统性优于 T=1.0 下的随机抽样均值。3.5pp 差距暗示 temperature sampling 引入了非 trivial 的质量下降。论文应简要说明这是 temperature-quality tradeoff 的预期表现，并讨论这是否影响 oracle headroom 的解释（oracle 也来自 T=1.0 samples）。

### [AGREE] R1-W2: Kendall's W=1.0 with 3 seeds 的 precision caveat

同意。5 signals 在 3 seeds 下 W=1.0 意味着所有 3 seeds 给出相同排序。但 5 items 仅有 120 种排列，3 observations 下 W=1.0 的 p 值已知偏大（exact p 约 0.028）。这是有意义的但不如论文暗示的那样 definitive。应注明 "stability within the tested range of 3 seeds"。

### [REBUT] R1-W3: 8B vs 4B degeneracy 的 capability vs fine-tuning confound

不完全同意。论文已通过 **LoRA-rank ablation (§4.5)** 直接控制了这个 confound：同一 8B 模型，rank=32 → 21% degeneracy，rank=8 → 7% degeneracy。这证明 fine-tuning capacity（而非 base model capability）drives degeneracy。Table 5 的 8B vs 4B 对比是 observational，但 rank ablation 是 interventional——论文已经做了 R1 要求的控制实验。

### [AGREE] R1-W4: TOST 等价性结论的 configuration-dependent 呈现

同意。Table 15 (Appendix F) 显示 TOST 结果在 NER 和 RE 之间差异很大：NER 上 4/5 signals 在 ε=3pp 通过等价，但 RE 上 EM 和 VC 在 ε=5pp 仍不通过。论文正文倾向于强调 NER 的等价性结论，而 RE 的 systematic underperformance 在附录中被淡化。呈现应更平衡。

### [AGREE] R1-W5: Gold-empty instance filtering 不一致

同意。Table 4 对 SciERC 使用 full set (n=551, greedy=0.614)，而 Table 3 使用 gold-filtered (n=529, greedy=0.645)。Footnote 8 虽有说明，但这种 protocol 不一致会让审稿人困惑。应统一为一种 protocol 或在表格 caption 中更明确标注。

---

## 关于 R1 的 3.5/5 评分

**我认为 3.5/5 是合理的，但我倾向于 3.0/5。** 理由：

1. **R1 的统计批评我大部分同意**——特别是 N1（sign test power）和 N2（3-point monotonicity），这两个问题直接削弱论文最有 novelty 的 claim（degeneracy-gating mechanism）。

2. **从我的 framing/novelty 角度补充：** 论文的核心 "correlation-selection gap" 在概念上是 *partially expected*——instance-level signals 无法区分同一 input 的不同 outputs，这在 §3.1 定义时就已蕴含。论文将一个设计层面可预见的限制包装为 empirical discovery，novelty premium 有限。真正有趣的是 LP（per-sample signal）也 largely fails 的诊断，但这部分 claim 恰好是统计支撑最弱的。

3. **Positive aspects（与 R1 一致）：** 实验覆盖度高（4 datasets, 2 model families, 4B ablation, LoRA-rank ablation, free-form ablation, entity-token LP ablation, supervised verifier baseline），消融链完整，negative result 本身有价值。

4. **如果 N1-N3 全部修复：** 论文可以升至 3.5-4.0/5——前提是将 "monotonically predicts" 改为探索性观察，sign test 替换为 paired bootstrap，non-tied subset 分析的 framing 调整为 diagnostic。

**我的独立评分：3.0-3.5/5（Findings track，borderline Conference）。** 与 R1 的 3.5 相比略低，主要因为 novelty concern：gap 的存在对熟悉 MBR/self-consistency 文献的审稿人而言不够 surprising。

---

## 与我的审查侧重的一致性分析

R1 的统计方法论批评与我的 framing/novelty 批评 **互相加强**：

- R1 指出 degeneracy-gating 的统计支撑不足 → 我指出这恰恰是论文最有 novelty 的 claim，如果它 statistically 站不住，论文就回退为 "instance-level signals 做不了 selection"（a priori 可预见）+ "LP 也基本做不了"（有趣但 under-supported）
- R1 的 N3（Bonferroni scope）→ 这削弱了 "compression is the bottleneck" 这条诊断链的最后一环（non-tied subset 证据），但我认为这个影响比 R1 判断的小（论文已正确定位为 exploratory）

两位 reviewer 的批评汇合点：**论文最有价值的贡献（degeneracy as predictive mechanism）恰好是统计上最脆弱的。** 修复路径清晰（更多 datasets、bootstrap testing、language softening），但 revision 需要实质性补充实验（至少 2-3 个额外 datasets 来支撑 monotonic claim）。

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

_source line 1597 · 2026-05-17T06:34:58.875293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "1043",
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
    "offset": "1043",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1598 · 2026-05-17T06:34:58.926003+00:00_

1043	  resolution: ""
1044	  resolution_round: null
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
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1599 · 2026-05-17T06:39:55.987216+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4x variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 dagger-RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n\n# ===== RECURRING ISSUES (updated Round 16) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 16\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 核心 finding 实质仅 SciERC 验证.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已加入 Few-NERD (10% degen, LP +1.36pp). 但 R2-W1 指出 Few-NERD positive finding 仅 1 model x 1 N x 1 dataset. 数据集覆盖有改善但仍不充分. R1 的 monotonic claim 问题 (3 dataset-level points) 本质上是同一问题的统计表达.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"增加至少一个 medium-difficulty NER 数据集或将 claim 限定为 medium-difficulty scientific NER.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Few-NERD 已加入但 positive finding 需 cross-model 验证 (LLaMA Few-NERD). 或承认 monotonic pattern 为 exploratory observation.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 16\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 仍是最核心 framing 问题.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: Contribution #1 混合 instance-level limitation 和 LP failure.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: '5 signals all fail' 仍然混淆 definitional limitation 和 empirical finding.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R2-N1 + R1 AGREE): 标题 'Strong Predictors, Weak Selectors' 暗示意外发现, 但 4/5 signals 的 weakness 部分是 by construction. 真正 empirical: (a) MBR with positive ρ=0.52 仍失败 (degeneracy), (b) LP per-sample but compressed. 论文需分三层: definitional → MBR empirical → LP empirical. 此问题自 Round 3 持续 14 轮未解决.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: 删除 by construction, MBR failure→empirical\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract/Intro 拆分三层叙事.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Title 的 'Weak Selectors' 需 nuance: 区分 definitionally weak (instance-level) 和 empirically weak (MBR despite aligned utility + LP despite per-sample). Contribution 2 重写: emphasis 放在 degeneracy/compression 诊断而非 gap 本身.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + Bonferroni scope 争议\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 16\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, epsilon降为辅助\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: epsilon sweep gain 单调递增, Bonferroni over 5 signals != correction over 7epsilon x 5.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Footnote 4 'survives Bonferroni over 5 comparisons' 未计入 7epsilon post-hoc 选择.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 分歧: R1-N3 (critical) vs R2 PARTIALLY REBUT (should-fix). R2 理由: (1) Limitations 已承认 post-hoc; (2) epsilon 值嵌套 (非独立), Bonferroni 过保守; (3) median LP range=0.041 提供 a priori 动机; (4) non-tied analysis 定位为 diagnostic 非 prescriptive. 共识: footnote 4 措辞需修正, 但 severity 有分歧.\"\n  action_items:\n  - round: 12\n    action: \"Abstract 'tied'→continuous, epsilon降为辅助\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Footnote 4 修正 Bonferroni scope 或改为 exploratory finding.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Footnote 4 改为 'survives Bonferroni over 5 signal comparisons, conditional on the pre-selected epsilon=0.05 threshold (see Limitations for discussion of post-hoc nature)'. 不可声称 unconditional significance.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: fine-tuning→degeneracy 是关键区分但论文未抓住.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 关键未回答: hard-prompted models 是否存在 instance degeneracy?\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W3 + R1 AGREE): 核心增量不仅是 fine-tuned vs hard-prompted, 更是 'why QE != selection' 的诊断. 建议对比句: 'Yao et al. demonstrate correlation; we show correlation is necessary but not sufficient, and diagnose why.'\"\n  action_items:\n  - round: 14\n    action: \"Related Work 增加明确对比段落.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Related Work 加入直接对比: 'Yao et al. demonstrate consistency correlates with accuracy; we show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression).'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Abstract 'at two model scales' 未说明 narrow range.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Discussion 'intrinsic' 用语仍暗示更强普遍性.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W6 + R1 PARTIAL REBUT): R2 认为标题 'Fail to Scale' 暗示 model scale; R1 反驳 'scale' 在论文中指 N/信号复杂度. 共识: 'scale' 含义需在 Abstract 中澄清.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 15\n    action: \"Discussion 'intrinsic to capable fine-tuned models' 改为 'within the 3B-8B fine-tuned regime we tested'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Abstract 或 Introduction 中澄清 'scale' 的含义 (指 scaling up N, signal sophistication, and model size within 4B-8B), 避免被误读为跨 model scale 的 general claim.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.0 p~0.05 仅 borderline significant\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: 3-seed 功能是 sanity check 非统计推断依据.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 主文呈现 W=1.0 过于自信, 需 precision caveat.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W2 + R2 AGREE): m=3 raters, k=5 items, exact p~0.028. 有意义但不如论文暗示的 definitive. 主文需加 caveat.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"主文 'Kendall W=1.0' 后加 '(though statistical precision is limited with 3 seeds; exact p approx 0.028)' 或类似 qualification.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 hypotheses\"\n  - round: 14\n    reviewers: [1]\n    note: \"constraint-imposed vs model-learned 区分 sound.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. 论文已有 (a)-(d) 四个 hypotheses. R2 交叉中 Q3 指出 LoRA rank=8 降低 degeneracy 但 LP 仍失败, 暗示 LP compression 可能比 degeneracy 更 fundamental.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出\"\n  - round: 14\n    reviewers: [1]\n    note: \"'intrinsic' claim 应限定为 NER-specific.\"\n  - round: 15\n    reviewers: [1]\n    note: \"R15: RE reversal 削弱 NER 'ruling out' claim.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 15\n    action: \"'ruling out constrained decoding' 改为 'provides evidence against constrained decoding as the primary cause for NER'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"rho headline 来自 ceiling-effect dataset / 数值不一致\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"改措辞为 moderate-to-strong 或加限定语\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"rho=0.38 按 Cohen (1988) 属 medium effect.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Abstract 仅报告 primary rho=0.38.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R2-N2 + R1 AGREE, 独立验证): 论文内部数值矛盾严重. Abstract/Figure 1 caption 声称 'rho up to 0.42 on primary test bed', 但 Table 1 SciERC 最高 rho = VC 0.379. rho=0.42 实际来自 Few-NERD LP (0.421). Contribution 1 正确写 0.38. 这不是四舍五入误差 (差 0.04), 是不同位置引用了不同数据源. 从 R15 的 warning 升级为 critical (影响可信度).\"\n  action_items:\n  - round: 14\n    action: \"'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract 改为仅报告 primary rho=0.38.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"全文统一 headline rho: SciERC (primary) max = 0.38 (VC, N=8); Few-NERD LP = 0.42. Figure 1 caption 修正 (当前错误地将 0.42 归因于 primary test bed). Abstract 改为 'rho up to 0.38 on the primary test bed (0.42 on Few-NERD)'. 禁止混淆归属.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 14\n    reviewers: []\n    note: \"Entity-token LP + LP x VC 已测试, 全部 negative.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. 多种 remedy 已测试并全部 negative (entity-token LP, LP x VC, supervised combination, verbalized confidence). 论文已尽合理努力.\"\n  action_items:\n  - round: 14\n    action: \"LP x VC combination 整合入 Discussion.\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W5 + R2 AGREE): Table 4 SciERC 使用 full set (n=551, greedy=0.614), Table 2 使用 gold-filtered (n=529, greedy=0.645). Footnote 解释差异但仍造成 apple-to-orange comparison. LP delta 从 +0.2pp (Table 2) 到 +0.42pp (Table 4) 不一致.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"统一 protocol: Table 4 中同时报告 gold-filtered 数字以便 direct comparison, 或将所有表格统一为同一 n.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"共识降级: terminology preference, 非实质问题.\"\n  - round: 14\n    reviewers: [1]\n    note: \"Footnote 已有说明, Appendix delta-rho<0.01.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: R2-W2 再次提出. R1 REBUT.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W2 + R1 AGREE): 分母用 max 而非 union 不是标准 Jaccard. 建议改名为 'Soft Overlap' 或首次出现时加注释.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 / 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"精简 Abstract: 移除 MBR mechanical 细节\"\n  - round: 14\n    reviewers: [2]\n    note: \"Abstract 仍覆盖过多技术细节.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: Abstract 塞入过多数字.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W4 + R1 AGREE): 9 句话含 5 signals, 4 benchmarks, 2 mechanisms, rho/AUROC/degeneracy%/LP nats/p-values. 远超审稿人 30 秒吸收能力. 核心 narrative 被数字淹没.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Abstract 数字压缩到 3-4 个最关键的 (如 rho~0.4, 13pp oracle headroom, 0 net selection gain). Degeneracy gradient 简化为一句 pattern description 而非列出 3 个百分比.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系: 贡献定位需从 discovery 转为 diagnosis\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"贡献定位需从 'identifying gap' 转为 'diagnosing failure mechanisms'.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 与 R3-W2 同一根源.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R2-N3 + R1 AGREE): Eikema et al. (2025) 认为问题在 utility design. 本文证明即使 utility IS aligned (within-instance rho=0.52), degeneracy 也 eliminate headroom. 这是真正的 incremental contribution, 但 Related Work 对此区分不够明确. R1 补充: NER 离散标签空间导致更极端 degeneracy, 这个 structural argument 也应强调.\"\n  action_items:\n  - round: 14\n    action: \"Contribution #1 从 'identifying' 改为 'diagnosing two specific failure mechanisms'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Contribution 需突出 within-instance analysis novelty.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Related Work 增加 differentiation paragraph: 'Eikema et al. argue the problem lies in utility design; we demonstrate that even when utility IS well-aligned (within-instance rho=0.52), output degeneracy eliminates the headroom MBR needs.' 同时强调 NER 离散标签空间导致比 MT/summarization 更极端的 degeneracy.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) / sign test 统计效力极低\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Fisher p 呈现权重应降低.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 方向共识, severity 分歧.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R1-N1 + R2 AGREE): Sign test 仅用方向信息, effect size +0.2pp 下 power 极低. R2 补充: (1) N=32 bootstrap (p=0.031) 反驳了论文自身的 'selection fails' 叙事; (2) Few-NERD 用了 paired bootstrap 而 SciERC 用 sign test, 方法不统一. 共识: SciERC null result 不应表述为 'no signal significantly outperforms greedy', 应改为 'effect is small and not reliably detected'. 升级为 critical (核心否定结论的统计基础).\"\n  action_items:\n  - round: 14\n    action: \"Table 2 将 Fisher combined p 降级为辅助.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"主文从 'all p>0.05' 叙事转向 effect size + convergent evidence lines.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"(1) 统一统计方法: SciERC 也用 paired bootstrap (B=10000) 替代 sign test; (2) 主文改为 'the observed LP advantage (+0.2pp) is small (d=0.038) and not reliably detected'; (3) 与 N=32 bootstrap p=0.031 整合叙事 (LP 在更大 N 下可能 work); (4) 报告 power analysis 或明确声明 'absence of evidence is not evidence of absence'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"greedy 应定位为 practical cost-free alternative.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 'surpassing all N=8 selection strategies' 仍过强.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. 但 R1-W1 (Random vs Greedy 3.5pp) 间接相关: 如果差距是 temperature-quality tradeoff, greedy 'surpassing' 只反映 T=0 vs T=1 差异.\"\n  action_items:\n  - round: 14\n    action: \"'surpassing' 改为 'practical cost-free alternative'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"测试 Greedy vs Single 显著性. 修辞改为 'selection adds no benefit over greedy or single-sample'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation: 8B vs 4B degeneracy 差异的解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"4B constant F1 fraction 和 oracle headroom 未报告.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Table 6 已包含 4B data. 新 concern: 8B/4B 差异可能是 recipe artifact.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 分歧: R1-W3 (capability vs recipe confound) vs R2 REBUT. R2 理由: LoRA-rank ablation (rank=32→21%, rank=8→7%) 是 interventional evidence, 已证明 fine-tuning capacity (非 base capability) drives degeneracy. 8B vs 4B 是 observational, rank ablation 是 interventional—论文已做了控制实验. R1 的 concern 被部分 addressed.\"\n  action_items:\n  - round: 14\n    action: \"报告 4B 的 degeneracy 统计.\"\n    assigned_to: \"Main Agent (data) + Paper Agent (writing)\"\n    status: done\n  - round: 15\n    action: \"解释 8B vs 4B degeneracy 差异.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Discussion 明确说明: LoRA-rank ablation (interventional) 证明 fine-tuning capacity drives degeneracy; 8B vs 4B 对比 (observational) 与此一致但非独立证据. 弱化 'scales with model capability' → 'correlates with model scale under matched training recipe; LoRA-rank ablation confirms fine-tuning capacity as the driver'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-Q5: 两者期望值应相同.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 从 info 升级为 critical. E[Random]=E[Single] under T=1.0.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W1 + R2 AGREE): 3.5pp 差距是系统性的. R2 补充: 如果是 temperature-quality tradeoff, 论文应简要说明并讨论是否影响 oracle headroom 解释 (oracle 也来自 T=1 samples). 如果 Random 和 Single 计算方式不同 (如 aggregation 差异), 需显式说明.\"\n  action_items:\n  - round: 14\n    action: \"澄清 Random vs Single baseline 的定义差异和 3.5pp 差距来源.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"明确 Random 和 Single 的精确计算公式: (1) Random = 从 N candidates 中 uniform draw 的单次 F1, averaged over instances? (2) Single = 单次 T=1 generation 的 F1, averaged over instances? 如果两者定义相同, 3.5pp 差距暗示 seed-specific 分布偏差, 需报告 per-seed breakdown.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W5 + R1 AGREE): 操作性定义直到 Section 4.3 才出现, 但术语从 Abstract 开始使用. 需在 Introduction 首次使用时给出 one-sentence operational definition.\"\n  action_items:\n  - round: 14\n    action: \"Introduction 首次使用时添加 one-sentence 操作性定义.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Introduction line 12 首次使用 'correlation-selection gap' 时插入操作性定义, 如 '(the disparity between a signal ranking instances reliably and its ability to select the best output within a single instance)'. 不需要正式公式, 但含义必须在首次出现时明确.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW/UPDATED ISSUES (Round 15→16) =====\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 8B 可能因同样 epoch 数 overfit 更快.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 分歧: R1-W3 维持 concern; R2 REBUT 指出 LoRA-rank ablation 已做 interventional control. 共识: 8B vs 4B observational evidence 弱于 LoRA-rank interventional evidence; 论文应调整权重.\"\n  action_items:\n  - round: 15\n    action: \"Discussion/Limitations 显式承认 fine-tuning recipe confound.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"LoRA-rank ablation 作为 primary evidence (interventional), 8B vs 4B 作为 supporting (observational). 弱化 '8B vs 4B proves capability scaling' 到 '8B vs 4B is consistent with rank ablation findings'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Qwen-CoNLL selection degrades 0.9-1.5pp.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W4 + R2 AGREE): 论文正文倾向于强调 NER equivalence, 而 systematic underperformance 被淡化. 呈现应更平衡.\"\n  action_items:\n  - round: 15\n    action: \"Main text 更平衡呈现 TOST 结果.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Section 4.3 增加一句: 'In some configurations (Qwen-CoNLL), signal-based selection actively degrades performance (0.9-1.5pp below greedy), suggesting selection can be harmful rather than merely ineffective.'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N1\n  summary: \"Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点, 统计不显著 (p=0.066)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R1-N2 + R2 AGREE): 3 个 dataset-level 数据点的 monotonic trend 无统计意义 (任意 3 个不同值有 1/3 概率 monotonic). Figure 3 Spearman rho=-0.57, p=0.066, n=11 未达 alpha=0.05. R2 补充: per-entity-type (n=8, rho=-0.881, p=0.004) 在 controlled within-dataset setting 下更有力, 但混合粒度分析 (3 dataset + 8 entity-type) 可能违反 independence. 共识: 'monotonically predicts' 语言过强, 应降级为 exploratory observation.\"\n  action_items:\n  - round: 16\n    action: \"(1) Abstract/Conclusion 中 'instance degeneracy monotonically predicts LP selection effectiveness' 改为 'instance degeneracy is inversely associated with LP selection effectiveness'; (2) 区分 dataset-level evidence (n=3, exploratory) 和 entity-type-level evidence (n=8, p=0.004, more rigorous); (3) 讨论 mixed-granularity independence 假设; (4) 如要保留 'predictive' claim, 需要更多 dataset-level 数据点.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N2\n  summary: \"rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾 (已并入 R12-N1 升级)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-N2 + R1 独立验证 AGREE): Figure 1 caption 'rho up to 0.42 on primary test bed' 与 Table 1 SciERC max=0.379 直接矛盾. 0.42 来自 Few-NERD LP. 这是数值归属错误, 非四舍五入.\"\n  action_items:\n  - round: 16\n    action: \"见 R12-N1 的 Round 16 action item (全文统一 headline rho 归属).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4x variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 dagger-RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n\n# ===== RECURRING ISSUES (updated Round 16) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 16\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 核心 finding 实质仅 SciERC 验证.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已加入 Few-NERD (10% degen, LP +1.36pp). 但 R2-W1 指出 Few-NERD positive finding 仅 1 model x 1 N x 1 dataset. 数据集覆盖有改善但仍不充分. R1 的 monotonic claim 问题 (3 dataset-level points) 本质上是同一问题的统计表达.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"增加至少一个 medium-difficulty NER 数据集或将 claim 限定为 medium-difficulty scientific NER.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Few-NERD 已加入但 positive finding 需 cross-model 验证 (LLaMA Few-NERD). 或承认 monotonic pattern 为 exploratory observation.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 16\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: Contribution list 重组为纯 empirical\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: 仍是最核心 framing 问题.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: Contribution #1 混合 instance-level limitation 和 LP failure.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: '5 signals all fail' 仍然混淆 definitional limitation 和 empirical finding.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R2-N1 + R1 AGREE): 标题 'Strong Predictors, Weak Selectors' 暗示意外发现, 但 4/5 signals 的 weakness 部分是 by construction. 真正 empirical: (a) MBR with positive ρ=0.52 仍失败 (degeneracy), (b) LP per-sample but compressed. 论文需分三层: definitional → MBR empirical → LP empirical. 此问题自 Round 3 持续 14 轮未解决.\"\n  action_items:\n  - round: 12\n    action: \"Contribution list 重组: 删除 by construction, MBR failure→empirical\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract/Intro 拆分三层叙事.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Title 的 'Weak Selectors' 需 nuance: 区分 definitionally weak (instance-level) 和 empirically weak (MBR despite aligned utility + LP despite per-sample). Contribution 2 重写: emphasis 放在 degeneracy/compression 诊断而非 gap 本身.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + Bonferroni scope 争议\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 16\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 9\n    reviewers: [1]\n    note: \"仅作 question 提出\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"circularity 存在, 影响辅助分析\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: 主文用 continuous characterization, epsilon降为辅助\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: epsilon sweep gain 单调递增, Bonferroni over 5 signals != correction over 7epsilon x 5.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Footnote 4 'survives Bonferroni over 5 comparisons' 未计入 7epsilon post-hoc 选择.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 分歧: R1-N3 (critical) vs R2 PARTIALLY REBUT (should-fix). R2 理由: (1) Limitations 已承认 post-hoc; (2) epsilon 值嵌套 (非独立), Bonferroni 过保守; (3) median LP range=0.041 提供 a priori 动机; (4) non-tied analysis 定位为 diagnostic 非 prescriptive. 共识: footnote 4 措辞需修正, 但 severity 有分歧.\"\n  action_items:\n  - round: 12\n    action: \"Abstract 'tied'→continuous, epsilon降为辅助\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Footnote 4 修正 Bonferroni scope 或改为 exploratory finding.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Footnote 4 改为 'survives Bonferroni over 5 signal comparisons, conditional on the pre-selected epsilon=0.05 threshold (see Limitations for discussion of post-hoc nature)'. 不可声称 unconditional significance.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 提出, R1 反驳 selection analysis 有独立价值\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 现有差异描述可接受, camera-ready 级 refinement\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: fine-tuning→degeneracy 是关键区分但论文未抓住.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 关键未回答: hard-prompted models 是否存在 instance degeneracy?\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W3 + R1 AGREE): 核心增量不仅是 fine-tuned vs hard-prompted, 更是 'why QE != selection' 的诊断. 建议对比句: 'Yao et al. demonstrate correlation; we show correlation is necessary but not sufficient, and diagnose why.'\"\n  action_items:\n  - round: 14\n    action: \"Related Work 增加明确对比段落.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Related Work 加入直接对比: 'Yao et al. demonstrate consistency correlates with accuracy; we show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression).'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"需确认所有 scale claims 限定范围\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 两位再次强共识.\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Abstract 'at two model scales' 未说明 narrow range.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Discussion 'intrinsic' 用语仍暗示更强普遍性.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W6 + R1 PARTIAL REBUT): R2 认为标题 'Fail to Scale' 暗示 model scale; R1 反驳 'scale' 在论文中指 N/信号复杂度. 共识: 'scale' 含义需在 Abstract 中澄清.\"\n  action_items:\n  - round: 12\n    action: \"在 Conclusion/Discussion 明确限定为 small-model regime\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 15\n    action: \"Discussion 'intrinsic to capable fine-tuned models' 改为 'within the 3B-8B fine-tuned regime we tested'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Abstract 或 Introduction 中澄清 'scale' 的含义 (指 scaling up N, signal sophistication, and model size within 4B-8B), 避免被误读为跨 model scale 的 general claim.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"Kendall W=1.000 with n=3 不具信息量\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 共识: n=3 时 W=1.0 p~0.05 仅 borderline significant\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14: 3-seed 功能是 sanity check 非统计推断依据.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 主文呈现 W=1.0 过于自信, 需 precision caveat.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W2 + R2 AGREE): m=3 raters, k=5 items, exact p~0.028. 有意义但不如论文暗示的 definitive. 主文需加 caveat.\"\n  action_items:\n  - round: 12\n    action: \"正文降低 ranking stability 表述强度\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"主文 'Kendall W=1.0' 后加 '(though statistical precision is limited with 3 seeds; exact p approx 0.028)' 或类似 qualification.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 16\n  mentions:\n  - round: 11\n    reviewers: [1, 2]\n    note: \"应讨论 hypotheses\"\n  - round: 14\n    reviewers: [1]\n    note: \"constraint-imposed vs model-learned 区分 sound.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. 论文已有 (a)-(d) 四个 hypotheses. R2 交叉中 Q3 指出 LoRA rank=8 降低 degeneracy 但 LP 仍失败, 暗示 LP compression 可能比 degeneracy 更 fundamental.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"共识: 不作为 positive result 突出\"\n  - round: 14\n    reviewers: [1]\n    note: \"'intrinsic' claim 应限定为 NER-specific.\"\n  - round: 15\n    reviewers: [1]\n    note: \"R15: RE reversal 削弱 NER 'ruling out' claim.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 15\n    action: \"'ruling out constrained decoding' 改为 'provides evidence against constrained decoding as the primary cause for NER'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"rho headline 来自 ceiling-effect dataset / 数值不一致\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"改措辞为 moderate-to-strong 或加限定语\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"rho=0.38 按 Cohen (1988) 属 medium effect.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Abstract 仅报告 primary rho=0.38.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R2-N2 + R1 AGREE, 独立验证): 论文内部数值矛盾严重. Abstract/Figure 1 caption 声称 'rho up to 0.42 on primary test bed', 但 Table 1 SciERC 最高 rho = VC 0.379. rho=0.42 实际来自 Few-NERD LP (0.421). Contribution 1 正确写 0.38. 这不是四舍五入误差 (差 0.04), 是不同位置引用了不同数据源. 从 R15 的 warning 升级为 critical (影响可信度).\"\n  action_items:\n  - round: 14\n    action: \"'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Abstract 改为仅报告 primary rho=0.38.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"全文统一 headline rho: SciERC (primary) max = 0.38 (VC, N=8); Few-NERD LP = 0.42. Figure 1 caption 修正 (当前错误地将 0.42 归因于 primary test bed). Abstract 改为 'rho up to 0.38 on the primary test bed (0.42 on Few-NERD)'. 禁止混淆归属.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 12\n    reviewers: [1, 2]\n    note: \"至少一个 pilot remedy 会显著增强\"\n  - round: 14\n    reviewers: []\n    note: \"Entity-token LP + LP x VC 已测试, 全部 negative.\"\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. 多种 remedy 已测试并全部 negative (entity-token LP, LP x VC, supervised combination, verbalized confidence). 论文已尽合理努力.\"\n  action_items:\n  - round: 14\n    action: \"LP x VC combination 整合入 Discussion.\"\n    assigned_to: Paper Agent\n    status: done\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W5 + R2 AGREE): Table 4 SciERC 使用 full set (n=551, greedy=0.614), Table 2 使用 gold-filtered (n=529, greedy=0.645). Footnote 解释差异但仍造成 apple-to-orange comparison. LP delta 从 +0.2pp (Table 2) 到 +0.42pp (Table 4) 不一致.\"\n  action_items:\n  - round: 12\n    action: \"确认 n 值并统一说明 filtering 策略\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"统一 protocol: Table 4 中同时报告 gold-filtered 数字以便 direct comparison, 或将所有表格统一为同一 n.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 16\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"共识降级: terminology preference, 非实质问题.\"\n  - round: 14\n    reviewers: [1]\n    note: \"Footnote 已有说明, Appendix delta-rho<0.01.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: R2-W2 再次提出. R1 REBUT.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W2 + R1 AGREE): 分母用 max 而非 union 不是标准 Jaccard. 建议改名为 'Soft Overlap' 或首次出现时加注释.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 / 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 16\n  mentions:\n  - round: 13\n    reviewers: [1, 2]\n    note: \"精简 Abstract: 移除 MBR mechanical 细节\"\n  - round: 14\n    reviewers: [2]\n    note: \"Abstract 仍覆盖过多技术细节.\"\n  - round: 15\n    reviewers: [2]\n    note: \"R15: Abstract 塞入过多数字.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W4 + R1 AGREE): 9 句话含 5 signals, 4 benchmarks, 2 mechanisms, rho/AUROC/degeneracy%/LP nats/p-values. 远超审稿人 30 秒吸收能力. 核心 narrative 被数字淹没.\"\n  action_items:\n  - round: 13\n    action: \"精简 Abstract\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Abstract 数字压缩到 3-4 个最关键的 (如 rho~0.4, 13pp oracle headroom, 0 net selection gain). Degeneracy gradient 简化为一句 pattern description 而非列出 3 个百分比.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系: 贡献定位需从 discovery 转为 diagnosis\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"贡献定位需从 'identifying gap' 转为 'diagnosing failure mechanisms'.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 与 R3-W2 同一根源.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R2-N3 + R1 AGREE): Eikema et al. (2025) 认为问题在 utility design. 本文证明即使 utility IS aligned (within-instance rho=0.52), degeneracy 也 eliminate headroom. 这是真正的 incremental contribution, 但 Related Work 对此区分不够明确. R1 补充: NER 离散标签空间导致更极端 degeneracy, 这个 structural argument 也应强调.\"\n  action_items:\n  - round: 14\n    action: \"Contribution #1 从 'identifying' 改为 'diagnosing two specific failure mechanisms'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"Contribution 需突出 within-instance analysis novelty.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Related Work 增加 differentiation paragraph: 'Eikema et al. argue the problem lies in utility design; we demonstrate that even when utility IS well-aligned (within-instance rho=0.52), output degeneracy eliminates the headroom MBR needs.' 同时强调 NER 离散标签空间导致比 MT/summarization 更极端的 degeneracy.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) / sign test 统计效力极低\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"Fisher p 呈现权重应降低.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 方向共识, severity 分歧.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R1-N1 + R2 AGREE): Sign test 仅用方向信息, effect size +0.2pp 下 power 极低. R2 补充: (1) N=32 bootstrap (p=0.031) 反驳了论文自身的 'selection fails' 叙事; (2) Few-NERD 用了 paired bootstrap 而 SciERC 用 sign test, 方法不统一. 共识: SciERC null result 不应表述为 'no signal significantly outperforms greedy', 应改为 'effect is small and not reliably detected'. 升级为 critical (核心否定结论的统计基础).\"\n  action_items:\n  - round: 14\n    action: \"Table 2 将 Fisher combined p 降级为辅助.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"主文从 'all p>0.05' 叙事转向 effect size + convergent evidence lines.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"(1) 统一统计方法: SciERC 也用 paired bootstrap (B=10000) 替代 sign test; (2) 主文改为 'the observed LP advantage (+0.2pp) is small (d=0.038) and not reliably detected'; (3) 与 N=32 bootstrap p=0.031 整合叙事 (LP 在更大 N 下可能 work); (4) 报告 power analysis 或明确声明 'absence of evidence is not evidence of absence'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"greedy 应定位为 practical cost-free alternative.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 'surpassing all N=8 selection strategies' 仍过强.\"\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. 但 R1-W1 (Random vs Greedy 3.5pp) 间接相关: 如果差距是 temperature-quality tradeoff, greedy 'surpassing' 只反映 T=0 vs T=1 差异.\"\n  action_items:\n  - round: 14\n    action: \"'surpassing' 改为 'practical cost-free alternative'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 15\n    action: \"测试 Greedy vs Single 显著性. 修辞改为 'selection adds no benefit over greedy or single-sample'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation: 8B vs 4B degeneracy 差异的解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1, 2]\n    note: \"4B constant F1 fraction 和 oracle headroom 未报告.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Table 6 已包含 4B data. 新 concern: 8B/4B 差异可能是 recipe artifact.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 分歧: R1-W3 (capability vs recipe confound) vs R2 REBUT. R2 理由: LoRA-rank ablation (rank=32→21%, rank=8→7%) 是 interventional evidence, 已证明 fine-tuning capacity (非 base capability) drives degeneracy. 8B vs 4B 是 observational, rank ablation 是 interventional—论文已做了控制实验. R1 的 concern 被部分 addressed.\"\n  action_items:\n  - round: 14\n    action: \"报告 4B 的 degeneracy 统计.\"\n    assigned_to: \"Main Agent (data) + Paper Agent (writing)\"\n    status: done\n  - round: 15\n    action: \"解释 8B vs 4B degeneracy 差异.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Discussion 明确说明: LoRA-rank ablation (interventional) 证明 fine-tuning capacity drives degeneracy; 8B vs 4B 对比 (observational) 与此一致但非独立证据. 弱化 'scales with model capability' → 'correlates with model scale under matched training recipe; LoRA-rank ablation confirms fine-tuning capacity as the driver'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 14\n    reviewers: [1]\n    note: \"R1-Q5: 两者期望值应相同.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 从 info 升级为 critical. E[Random]=E[Single] under T=1.0.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W1 + R2 AGREE): 3.5pp 差距是系统性的. R2 补充: 如果是 temperature-quality tradeoff, 论文应简要说明并讨论是否影响 oracle headroom 解释 (oracle 也来自 T=1 samples). 如果 Random 和 Single 计算方式不同 (如 aggregation 差异), 需显式说明.\"\n  action_items:\n  - round: 14\n    action: \"澄清 Random vs Single baseline 的定义差异和 3.5pp 差距来源.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"明确 Random 和 Single 的精确计算公式: (1) Random = 从 N candidates 中 uniform draw 的单次 F1, averaged over instances? (2) Single = 单次 T=1 generation 的 F1, averaged over instances? 如果两者定义相同, 3.5pp 差距暗示 seed-specific 分布偏差, 需报告 per-seed breakdown.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: []\n    note: \"R15 未被独立提及.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-W5 + R1 AGREE): 操作性定义直到 Section 4.3 才出现, 但术语从 Abstract 开始使用. 需在 Introduction 首次使用时给出 one-sentence operational definition.\"\n  action_items:\n  - round: 14\n    action: \"Introduction 首次使用时添加 one-sentence 操作性定义.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Introduction line 12 首次使用 'correlation-selection gap' 时插入操作性定义, 如 '(the disparity between a signal ranking instances reliably and its ability to select the best output within a single instance)'. 不需要正式公式, 但含义必须在首次出现时明确.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n# ===== CARRIED FORWARD (status unchanged) =====\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW/UPDATED ISSUES (Round 15→16) =====\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: 8B 可能因同样 epoch 数 overfit 更快.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 分歧: R1-W3 维持 concern; R2 REBUT 指出 LoRA-rank ablation 已做 interventional control. 共识: 8B vs 4B observational evidence 弱于 LoRA-rank interventional evidence; 论文应调整权重.\"\n  action_items:\n  - round: 15\n    action: \"Discussion/Limitations 显式承认 fine-tuning recipe confound.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"LoRA-rank ablation 作为 primary evidence (interventional), 8B vs 4B 作为 supporting (observational). 弱化 '8B vs 4B proves capability scaling' 到 '8B vs 4B is consistent with rank ablation findings'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 16\n  mentions:\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15: Qwen-CoNLL selection degrades 0.9-1.5pp.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R1-W4 + R2 AGREE): 论文正文倾向于强调 NER equivalence, 而 systematic underperformance 被淡化. 呈现应更平衡.\"\n  action_items:\n  - round: 15\n    action: \"Main text 更平衡呈现 TOST 结果.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 16\n    action: \"Section 4.3 增加一句: 'In some configurations (Qwen-CoNLL), signal-based selection actively degrades performance (0.9-1.5pp below greedy), suggesting selection can be harmful rather than merely ineffective.'\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N1\n  summary: \"Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点, 统计不显著 (p=0.066)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识 (R1-N2 + R2 AGREE): 3 个 dataset-level 数据点的 monotonic trend 无统计意义 (任意 3 个不同值有 1/3 概率 monotonic). Figure 3 Spearman rho=-0.57, p=0.066, n=11 未达 alpha=0.05. R2 补充: per-entity-type (n=8, rho=-0.881, p=0.004) 在 controlled within-dataset setting 下更有力, 但混合粒度分析 (3 dataset + 8 entity-type) 可能违反 independence. 共识: 'monotonically predicts' 语言过强, 应降级为 exploratory observation.\"\n  action_items:\n  - round: 16\n    action: \"(1) Abstract/Conclusion 中 'instance degeneracy monotonically predicts LP selection effectiveness' 改为 'instance degeneracy is inversely associated with LP selection effectiveness'; (2) 区分 dataset-level evidence (n=3, exploratory) 和 entity-type-level evidence (n=8, p=0.004, more rigorous); (3) 讨论 mixed-granularity independence 假设; (4) 如要保留 'predictive' claim, 需要更多 dataset-level 数据点.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N2\n  summary: \"rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾 (已并入 R12-N1 升级)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 16\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 (R2-N2 + R1 独立验证 AGREE): Figure 1 caption 'rho up to 0.42 on primary test bed' 与 Table 1 SciERC max=0.379 直接矛盾. 0.42 来自 Few-NERD LP. 这是数值归属错误, 非四舍五入.\"\n  action_items:\n  - round: 16\n    action: \"见 R12-N1 的 Round 16 action item (全文统一 headline rho 归属).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1600 · 2026-05-17T06:39:56.089986+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 37398}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1601 · 2026-05-17T06:42:06.987038+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 16 审稿报告 — Consolidated Review\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计方法论; R2: 新颖性+贡献定位+相关工作+写作质量）\n**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）\n\n---\n\n## Summary\n\n论文评估 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 LLM-based NER 中的质量估计与样本选择能力，在 4 个 benchmark 上（SciERC primary, CoNLL ceiling, Few-NERD low-degeneracy, WNUT collapse）使用 Qwen3-8B/LLaMA-3.1-8B/4B ablation。核心发现：信号可有效预测实例级质量（ρ up to 0.38-0.42），但无法有效选择 best-of-N 候选。诊断两个机制：instance degeneracy（10-58%）和 LP compression（median range 0.041 nats）。论文系统性强、诊断链完整、统计透明度高，但存在 framing 混淆、数值不一致和统计效力不足的关键问题。\n\n---\n\n## Strengths\n\n**S1. 系统性实验设计** [Both AGREE]\n4 个 benchmark 形成 difficulty gradient，2 模型族 + 4B scale ablation + LoRA-rank ablation 提供多层证据。覆盖面在同类论文中属上乘。\n\n**S2. 诊断链深度** [Both AGREE, 最强贡献]\n从\"gap exists\"到\"why it exists\"的五层 ablation：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 constrained decoding → entity-token LP 排除 format dilution → supervised combination 确认 feature space bottleneck。Within-instance analysis（non-degenerate ρ=0.52, MBR closes 23-41% oracle gap）证明 failure 来自 headroom vanishing 而非 utility misalignment。\n\n**S3. Negative result 实践意义** [Both AGREE]\n对 NER practitioners actionable：不要在 fine-tuned 高性能模型上指望 self-consistency 做 selection；QE 用于 selective prediction/error flagging 是可行方向。\n\n**S4. 统计透明度** [Both AGREE]\n对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。\n\n**S5. Few-NERD 对照实验** [Both AGREE]\n利用 degeneracy 差异（58%→21%→10%）形成跨 dataset 自然实验，LP selection 在低 degeneracy 下有效（+1.36pp, p<0.001），增强了 degeneracy 作为解释变量的可信度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [强共识] Framing 混淆 definitional limitation 与 empirical finding**\n- R2-N1 (critical) + R1 AGREE\n- 4/5 信号（SJ, VC, FK, EM）是 instance-level，by construction 对同一 input 所有候选给出相同分数。标题\"Strong Predictors, Weak Selectors\"暗示这是意外发现，但 instance-level signals 的\"weakness\"部分来自定义而非实验。\n- 真正的 empirical findings：(a) MBR conversion with positive within-instance ρ=0.52 仍失败（因 degeneracy），(b) LP per-sample but compressed。论文需明确分三层：definitional → MBR empirical → LP empirical。\n- **历史**：自 Round 3 (R3-W2) 首次提出，持续 14 轮未完全解决。\n\n**MF2. [强共识] ρ=0.42 headline 数值在论文内部矛盾**\n- R2-N2 (critical) + R1 独立验证 AGREE\n- Abstract/Figure 1 caption 声称\"ρ up to 0.42 on primary test bed\"，但 Table 1 SciERC（declared primary）最高 ρ = VC 0.379。ρ=0.42 实际来自 Few-NERD LP (0.421)。Contribution 1 正确写\"ρ=0.38\"。差 0.04，非四舍五入误差。\n- 影响论文可信度——审稿人会视为 cherry-picking 或粗心。\n\n**MF3. [强共识] 2-seed sign test 统计效力不足以支撑核心否定结论**\n- R1-N1 (critical) + R2 AGREE\n- \"no signal significantly outperforms greedy\"基于 2-seed paired sign test，effect size 仅 +0.2pp 下 power 极低。R2 补充：N=32 时 paired bootstrap 得 LP +0.95pp, p=0.031，实际上反驳了论文自身的\"selection fails\"叙事。Few-NERD 用 paired bootstrap 但 SciERC 用 sign test，方法不统一。\n- 共识修改：从\"no signal significantly outperforms\"改为\"effect is small and not reliably detected with current sample size\"；统一使用 paired bootstrap。\n\n**MF4. [强共识] Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点，统计不显著**\n- R1-N2 (critical) + R2 AGREE\n- 任意 3 个不同值必然可排出 monotonic order。Figure 3 Spearman ρ=−0.57, p=0.066 (n=11) 未达 α=0.05。\n- R2 补充缓解证据：per-entity-type 分析 (n=8, ρ=−0.881, p=0.004) 在 controlled within-dataset setting 更有力。但混合粒度（3 dataset + 8 entity-type）可能违反 independence。\n- 共识：\"monotonically predicts\"降级为\"is inversely associated with\"或\"is consistent with a monotonic relationship\"。\n\n**MF5. [强共识] 与 MBR 社区已知结论的增量需更清晰 articulate**\n- R2-N3 (critical) + R1 AGREE\n- Eikema et al. (2025) 已讨论 MBR utilities degrade on structured outputs。本文真正增量：即使 utility IS aligned (ρ=0.52)，degeneracy 也 eliminate headroom——这与 Eikema 的\"utility misalignment\"解释形成 complementary diagnosis。\n- R1 补充：NER 离散标签空间导致比 MT/summarization 更极端的 degeneracy，这个 structural argument 也应强调。\n- Related Work 需明确 differentiation paragraph。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [强共识] Random (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距未解释**\n- R1-W1 + R2 AGREE\n- E[Random]=E[Single] under T=1.0 应相同。3.5pp 系统性差距需澄清精确计算方式和 temperature-quality tradeoff 的影响。\n\n**SF2. [强共识] Abstract 信息过载**\n- R2-W4 + R1 AGREE\n- 9 句话塞入 5 signals、4 benchmarks、degeneracy%、LP nats、p-values 等，远超审稿人 30 秒吸收能力。数字压缩到 3-4 个最关键的。\n\n**SF3. [强共识] Kendall's W=1.0 with 3 seeds 需 precision caveat**\n- R1-W2 + R2 AGREE\n- m=3, k=5，exact p≈0.028，有意义但不如论文暗示的 definitive。\n\n**SF4. [强共识] Gold-empty instance filtering protocol 不一致**\n- R1-W5 + R2 AGREE\n- Table 4 SciERC (n=551, greedy=0.614) vs Table 2 (n=529, greedy=0.645)。LP Δ 从 +0.2pp 到 +0.42pp。需统一 protocol 或同时报告两版本。\n\n**SF5. [强共识] TOST configuration-dependent 呈现不平衡**\n- R1-W4 + R2 AGREE\n- Qwen-CoNLL 下 selection actively degrades (0.9-1.5pp)，这比\"no benefit\"更强的结论被淡化在 Appendix。\n\n**SF6. [强共识] \"Correlation-selection gap\" 操作性定义位置太晚**\n- R2-W5 + R1 AGREE\n- 术语从 Abstract 使用，Section 4.3 才正式定义。Introduction 首次使用时需给出 one-sentence operational definition。\n\n**SF7. [强共识] 与 Yao et al. (2026) 差异化不足**\n- R2-W3 + R1 AGREE\n- 核心增量不仅是 fine-tuned vs hard-prompted，更是\"why QE ≠ selection\"的诊断。需更直接的对比句。\n\n**SF8. [强共识] Soft Jaccard 命名误导**\n- R2-W2 + R1 AGREE\n- 分母用 max 而非 union，不是标准 Jaccard。改名或加注释。\n\n**SF9. [强共识] Scale claims 措辞需澄清**\n- R2-W6 + R1 PARTIAL REBUT\n- 标题\"Fail to Scale\"暗示 model scale，实测仅 4B-8B。R1 反驳：论文中\"scale\"指 N/信号复杂度。共识：Abstract 中需澄清\"scale\"具体含义。\n\n### Reviewer Divergence（分歧）\n\n**D1. Bonferroni scope（R1-N3）: R1 判 critical, R2 降为 should-fix**\n- R1：7ε × 5 signals = 35 comparisons → p_adj=0.14，不再显著。\n- R2 反驳：(1) Limitations 已承认 post-hoc；(2) ε 值嵌套（非独立），Bonferroni 过保守；(3) median LP range=0.041 提供 a priori 动机；(4) non-tied analysis 定位为 diagnostic 非 prescriptive。\n- 共识：Footnote 4 措辞需修正（\"conditional on pre-selected ε\"），但是否为 must-fix 有分歧。\n- **Director 判定：Should-Fix**。R2 的论证成立——嵌套比较下 Bonferroni 过保守，且论文已在 Limitations 中正确 acknowledge。但 footnote 4 必须修正措辞。\n\n**D2. 8B vs 4B degeneracy: capability vs recipe confound（R1-W3 vs R2 REBUT）**\n- R1：same training recipe, 更大模型可能 overfit 更快。\n- R2：LoRA-rank ablation 是 interventional evidence（同一 8B 模型 rank 32→21%, rank 8→7%），已控制此 confound。\n- **Director 判定：R2 的反驳有力**。LoRA-rank ablation 作为 interventional evidence 比 observational 8B/4B 对比更强。但论文应明确区分两者的证据权重。\n\n---\n\n## Questions for Authors\n\n1. **ρ=0.42 归属**：Figure 1 caption \"ρ up to 0.42 on primary test bed\" 具体来自哪个 configuration？Table 1 SciERC max = 0.379，与此矛盾。\n2. **Sign test power**：在 effect size d=0.038、n=529 下，sign test 的 power 是多少？为什么 SciERC 用 sign test 但 Few-NERD 用 paired bootstrap？\n3. **LP compression vs degeneracy hierarchy**：LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败。这是否暗示 LP compression 是独立于 degeneracy 的 more fundamental bottleneck？为何 Discussion 仍将 degeneracy 作为 primary diagnosis？\n4. **Few-NERD degeneracy confound**：低 degeneracy (10%) 可能由 dataset 特性（entity types 多样性、semantic overlap）而非 model capability 决定。仅 3 个 dataset-level data points 无法排除此 confound。如增加 entity-type-level 的 formal test，结论是否 robust？\n5. **Random vs Single 定义**：两者的精确计算方式是什么？E[Random]=E[Single] under T=1.0，3.5pp 系统性差距来源何在？\n6. **70B+ extrapolation**：如果 degeneracy 随 fine-tuning capacity 增加，70B+ 模型是否更严重？还是存在 non-monotonic 可能？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同建议补充：**\n- Xu et al. (2024) — Rejection/selective prediction 与 NER 交叉\n- Li et al. (2024) — LLM confidence estimation for structured outputs\n\n**R1 建议：**\n- Freitag et al. (2023) \"Results of WMT23 Metrics Shared Task\" — MBR 最新成果\n- Derczynski et al. (2016) — NER 评估方法论\n\n**R2 建议：**\n- Wan et al. (2023) \"GPT-RE\" — LLM-based RE direct competitor\n- Xu et al. (2024) \"Large Language Models for Generative Information Extraction: A Survey\"\n- Bertsch et al. (2024) \"In-Context Learning with Long-Context Models\"\n\n当前 58 个引用偏少（EMNLP 长文 typical 50-70），2025-2026 generative NER/IE survey 方向可补充。\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：未请求。**\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | — | 4.0 |\n| Overall | 3.5 | 3.0 | **3.25 (borderline Findings/Conference)** |\n\n**Overall Score: 3.25/5 — Borderline (Findings track, conditionally upgradeable to Conference)**\n\n**共识判断：** 实验设计和诊断链是论文的明显优势，negative result 对 NER 社区有实践价值。但论文存在四个关键瓶颈：\n\n1. **Framing（14 轮未解决）**：definitional vs empirical contribution 仍混淆\n2. **数值一致性**：ρ=0.42 归属错误直接损害可信度\n3. **统计基础**：核心否定结论依赖 under-powered sign test；核心 mechanistic claim（monotonic gating）统计不显著\n4. **Novelty positioning**：与 MBR 文献的增量未清晰 articulate\n\n**修复路径：**\n- 如果 MF1-MF5 全部修复（framing 分层 + 数值统一 + bootstrap 替代 sign test + monotonic 降级 + MBR differentiation），论文可升至 3.5-4.0（Conference track）\n- 如果仅修复 MF2（数值一致性）和 MF3/MF4（统计表述弱化），论文适合 Findings track\n- 如果 MF1（framing）在 16 轮后仍不能解决，论文将难以获得正面推荐\n\n**Recommendation: Findings acceptance with major revisions required for Conference consideration.**\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息过载（SF2）+ 数值矛盾（MF2）+ \"scale\"含义不明（SF9）。需大幅精简数字，统一 ρ 归属，澄清 scale 含义。\n\n**Introduction**: Gap 的 tautological framing 是最严重问题（MF1）。操作性定义缺失（SF6）。Contribution list 需分层。\n\n**Section 3 (Method)**: §3.1 有 instance-level/per-sample 区分但未向 Abstract/Intro 传递。Soft Jaccard 命名（SF8）。\n\n**Section 4 (Results)**: Sign test power 不足（MF3）。Table 2 与 Table 4 的 protocol 不一致（SF4）。Footnote 4 Bonferroni scope 措辞（D1）。Monotonic claim 过强（MF4）。\n\n**Section 5 (Discussion)**: Degeneracy 作为 primary diagnosis 的合理性（Q3）。与 Eikema et al. 的区分不足（MF5）。8B vs 4B 证据权重需调整（D2）。\n\n**Related Work**: 与 Yao et al. 差异化不足（SF7）。MBR differentiation paragraph 缺失（MF5）。\n\n**Limitations**: 已承认多个关键 caveats（ε post-hoc, seed 数量, scale range），质量高。但部分 caveats 与主文表述不一致（如 footnote 4 vs Limitations on ε）。\n\n**Appendix**: 质量极高。16+ sections 提供全面补充分析。但 appendix 质量不能弥补主文 framing 和统计问题。",
  "project": "struct_self_consist_ie",
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
    "report": "# Round 16 审稿报告 — Consolidated Review\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026)\n**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验+统计方法论; R2: 新颖性+贡献定位+相关工作+写作质量）\n**圆桌流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断（1 轮收敛）\n\n---\n\n## Summary\n\n论文评估 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 LLM-based NER 中的质量估计与样本选择能力，在 4 个 benchmark 上（SciERC primary, CoNLL ceiling, Few-NERD low-degeneracy, WNUT collapse）使用 Qwen3-8B/LLaMA-3.1-8B/4B ablation。核心发现：信号可有效预测实例级质量（ρ up to 0.38-0.42），但无法有效选择 best-of-N 候选。诊断两个机制：instance degeneracy（10-58%）和 LP compression（median range 0.041 nats）。论文系统性强、诊断链完整、统计透明度高，但存在 framing 混淆、数值不一致和统计效力不足的关键问题。\n\n---\n\n## Strengths\n\n**S1. 系统性实验设计** [Both AGREE]\n4 个 benchmark 形成 difficulty gradient，2 模型族 + 4B scale ablation + LoRA-rank ablation 提供多层证据。覆盖面在同类论文中属上乘。\n\n**S2. 诊断链深度** [Both AGREE, 最强贡献]\n从\"gap exists\"到\"why it exists\"的五层 ablation：instance degeneracy 量化 → LoRA-rank 解耦 → free-form decoding 排除 constrained decoding → entity-token LP 排除 format dilution → supervised combination 确认 feature space bottleneck。Within-instance analysis（non-degenerate ρ=0.52, MBR closes 23-41% oracle gap）证明 failure 来自 headroom vanishing 而非 utility misalignment。\n\n**S3. Negative result 实践意义** [Both AGREE]\n对 NER practitioners actionable：不要在 fine-tuned 高性能模型上指望 self-consistency 做 selection；QE 用于 selective prediction/error flagging 是可行方向。\n\n**S4. 统计透明度** [Both AGREE]\n对 post-hoc 分析（ε=0.05）、thinking token confound、gold-filtering 方法论、configuration-dependent TOST 结果的主动披露达到高标准。Limitations 诚实详尽。\n\n**S5. Few-NERD 对照实验** [Both AGREE]\n利用 degeneracy 差异（58%→21%→10%）形成跨 dataset 自然实验，LP selection 在低 degeneracy 下有效（+1.36pp, p<0.001），增强了 degeneracy 作为解释变量的可信度。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF1. [强共识] Framing 混淆 definitional limitation 与 empirical finding**\n- R2-N1 (critical) + R1 AGREE\n- 4/5 信号（SJ, VC, FK, EM）是 instance-level，by construction 对同一 input 所有候选给出相同分数。标题\"Strong Predictors, Weak Selectors\"暗示这是意外发现，但 instance-level signals 的\"weakness\"部分来自定义而非实验。\n- 真正的 empirical findings：(a) MBR conversion with positive within-instance ρ=0.52 仍失败（因 degeneracy），(b) LP per-sample but compressed。论文需明确分三层：definitional → MBR empirical → LP empirical。\n- **历史**：自 Round 3 (R3-W2) 首次提出，持续 14 轮未完全解决。\n\n**MF2. [强共识] ρ=0.42 headline 数值在论文内部矛盾**\n- R2-N2 (critical) + R1 独立验证 AGREE\n- Abstract/Figure 1 caption 声称\"ρ up to 0.42 on primary test bed\"，但 Table 1 SciERC（declared primary）最高 ρ = VC 0.379。ρ=0.42 实际来自 Few-NERD LP (0.421)。Contribution 1 正确写\"ρ=0.38\"。差 0.04，非四舍五入误差。\n- 影响论文可信度——审稿人会视为 cherry-picking 或粗心。\n\n**MF3. [强共识] 2-seed sign test 统计效力不足以支撑核心否定结论**\n- R1-N1 (critical) + R2 AGREE\n- \"no signal significantly outperforms greedy\"基于 2-seed paired sign test，effect size 仅 +0.2pp 下 power 极低。R2 补充：N=32 时 paired bootstrap 得 LP +0.95pp, p=0.031，实际上反驳了论文自身的\"selection fails\"叙事。Few-NERD 用 paired bootstrap 但 SciERC 用 sign test，方法不统一。\n- 共识修改：从\"no signal significantly outperforms\"改为\"effect is small and not reliably detected with current sample size\"；统一使用 paired bootstrap。\n\n**MF4. [强共识] Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点，统计不显著**\n- R1-N2 (critical) + R2 AGREE\n- 任意 3 个不同值必然可排出 monotonic order。Figure 3 Spearman ρ=−0.57, p=0.066 (n=11) 未达 α=0.05。\n- R2 补充缓解证据：per-entity-type 分析 (n=8, ρ=−0.881, p=0.004) 在 controlled within-dataset setting 更有力。但混合粒度（3 dataset + 8 entity-type）可能违反 independence。\n- 共识：\"monotonically predicts\"降级为\"is inversely associated with\"或\"is consistent with a monotonic relationship\"。\n\n**MF5. [强共识] 与 MBR 社区已知结论的增量需更清晰 articulate**\n- R2-N3 (critical) + R1 AGREE\n- Eikema et al. (2025) 已讨论 MBR utilities degrade on structured outputs。本文真正增量：即使 utility IS aligned (ρ=0.52)，degeneracy 也 eliminate headroom——这与 Eikema 的\"utility misalignment\"解释形成 complementary diagnosis。\n- R1 补充：NER 离散标签空间导致比 MT/summarization 更极端的 degeneracy，这个 structural argument 也应强调。\n- Related Work 需明确 differentiation paragraph。\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. [强共识] Random (0.610) vs Greedy/Single (0.645) 的 3.5pp 差距未解释**\n- R1-W1 + R2 AGREE\n- E[Random]=E[Single] under T=1.0 应相同。3.5pp 系统性差距需澄清精确计算方式和 temperature-quality tradeoff 的影响。\n\n**SF2. [强共识] Abstract 信息过载**\n- R2-W4 + R1 AGREE\n- 9 句话塞入 5 signals、4 benchmarks、degeneracy%、LP nats、p-values 等，远超审稿人 30 秒吸收能力。数字压缩到 3-4 个最关键的。\n\n**SF3. [强共识] Kendall's W=1.0 with 3 seeds 需 precision caveat**\n- R1-W2 + R2 AGREE\n- m=3, k=5，exact p≈0.028，有意义但不如论文暗示的 definitive。\n\n**SF4. [强共识] Gold-empty instance filtering protocol 不一致**\n- R1-W5 + R2 AGREE\n- Table 4 SciERC (n=551, greedy=0.614) vs Table 2 (n=529, greedy=0.645)。LP Δ 从 +0.2pp 到 +0.42pp。需统一 protocol 或同时报告两版本。\n\n**SF5. [强共识] TOST configuration-dependent 呈现不平衡**\n- R1-W4 + R2 AGREE\n- Qwen-CoNLL 下 selection actively degrades (0.9-1.5pp)，这比\"no benefit\"更强的结论被淡化在 Appendix。\n\n**SF6. [强共识] \"Correlation-selection gap\" 操作性定义位置太晚**\n- R2-W5 + R1 AGREE\n- 术语从 Abstract 使用，Section 4.3 才正式定义。Introduction 首次使用时需给出 one-sentence operational definition。\n\n**SF7. [强共识] 与 Yao et al. (2026) 差异化不足**\n- R2-W3 + R1 AGREE\n- 核心增量不仅是 fine-tuned vs hard-prompted，更是\"why QE ≠ selection\"的诊断。需更直接的对比句。\n\n**SF8. [强共识] Soft Jaccard 命名误导**\n- R2-W2 + R1 AGREE\n- 分母用 max 而非 union，不是标准 Jaccard。改名或加注释。\n\n**SF9. [强共识] Scale claims 措辞需澄清**\n- R2-W6 + R1 PARTIAL REBUT\n- 标题\"Fail to Scale\"暗示 model scale，实测仅 4B-8B。R1 反驳：论文中\"scale\"指 N/信号复杂度。共识：Abstract 中需澄清\"scale\"具体含义。\n\n### Reviewer Divergence（分歧）\n\n**D1. Bonferroni scope（R1-N3）: R1 判 critical, R2 降为 should-fix**\n- R1：7ε × 5 signals = 35 comparisons → p_adj=0.14，不再显著。\n- R2 反驳：(1) Limitations 已承认 post-hoc；(2) ε 值嵌套（非独立），Bonferroni 过保守；(3) median LP range=0.041 提供 a priori 动机；(4) non-tied analysis 定位为 diagnostic 非 prescriptive。\n- 共识：Footnote 4 措辞需修正（\"conditional on pre-selected ε\"），但是否为 must-fix 有分歧。\n- **Director 判定：Should-Fix**。R2 的论证成立——嵌套比较下 Bonferroni 过保守，且论文已在 Limitations 中正确 acknowledge。但 footnote 4 必须修正措辞。\n\n**D2. 8B vs 4B degeneracy: capability vs recipe confound（R1-W3 vs R2 REBUT）**\n- R1：same training recipe, 更大模型可能 overfit 更快。\n- R2：LoRA-rank ablation 是 interventional evidence（同一 8B 模型 rank 32→21%, rank 8→7%），已控制此 confound。\n- **Director 判定：R2 的反驳有力**。LoRA-rank ablation 作为 interventional evidence 比 observational 8B/4B 对比更强。但论文应明确区分两者的证据权重。\n\n---\n\n## Questions for Authors\n\n1. **ρ=0.42 归属**：Figure 1 caption \"ρ up to 0.42 on primary test bed\" 具体来自哪个 configuration？Table 1 SciERC max = 0.379，与此矛盾。\n2. **Sign test power**：在 effect size d=0.038、n=529 下，sign test 的 power 是多少？为什么 SciERC 用 sign test 但 Few-NERD 用 paired bootstrap？\n3. **LP compression vs degeneracy hierarchy**：LoRA rank=8 降低 degeneracy 到 7% 但 LP selection 仍失败。这是否暗示 LP compression 是独立于 degeneracy 的 more fundamental bottleneck？为何 Discussion 仍将 degeneracy 作为 primary diagnosis？\n4. **Few-NERD degeneracy confound**：低 degeneracy (10%) 可能由 dataset 特性（entity types 多样性、semantic overlap）而非 model capability 决定。仅 3 个 dataset-level data points 无法排除此 confound。如增加 entity-type-level 的 formal test，结论是否 robust？\n5. **Random vs Single 定义**：两者的精确计算方式是什么？E[Random]=E[Single] under T=1.0，3.5pp 系统性差距来源何在？\n6. **70B+ extrapolation**：如果 degeneracy 随 fine-tuning capacity 增加，70B+ 模型是否更严重？还是存在 non-monotonic 可能？\n\n---\n\n## Missing References\n\n**两位 Reviewer 共同建议补充：**\n- Xu et al. (2024) — Rejection/selective prediction 与 NER 交叉\n- Li et al. (2024) — LLM confidence estimation for structured outputs\n\n**R1 建议：**\n- Freitag et al. (2023) \"Results of WMT23 Metrics Shared Task\" — MBR 最新成果\n- Derczynski et al. (2016) — NER 评估方法论\n\n**R2 建议：**\n- Wan et al. (2023) \"GPT-RE\" — LLM-based RE direct competitor\n- Xu et al. (2024) \"Large Language Models for Generative Information Extraction: A Survey\"\n- Bertsch et al. (2024) \"In-Context Learning with Long-Context Models\"\n\n当前 58 个引用偏少（EMNLP 长文 typical 50-70），2025-2026 generative NER/IE survey 方向可补充。\n\n---\n\n## External Review\n\n**外部审稿（Stanford Agentic Reviewer）：未请求。**\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | — | 4.0 |\n| Overall | 3.5 | 3.0 | **3.25 (borderline Findings/Conference)** |\n\n**Overall Score: 3.25/5 — Borderline (Findings track, conditionally upgradeable to Conference)**\n\n**共识判断：** 实验设计和诊断链是论文的明显优势，negative result 对 NER 社区有实践价值。但论文存在四个关键瓶颈：\n\n1. **Framing（14 轮未解决）**：definitional vs empirical contribution 仍混淆\n2. **数值一致性**：ρ=0.42 归属错误直接损害可信度\n3. **统计基础**：核心否定结论依赖 under-powered sign test；核心 mechanistic claim（monotonic gating）统计不显著\n4. **Novelty positioning**：与 MBR 文献的增量未清晰 articulate\n\n**修复路径：**\n- 如果 MF1-MF5 全部修复（framing 分层 + 数值统一 + bootstrap 替代 sign test + monotonic 降级 + MBR differentiation），论文可升至 3.5-4.0（Conference track）\n- 如果仅修复 MF2（数值一致性）和 MF3/MF4（统计表述弱化），论文适合 Findings track\n- 如果 MF1（framing）在 16 轮后仍不能解决，论文将难以获得正面推荐\n\n**Recommendation: Findings acceptance with major revisions required for Conference consideration.**\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 信息过载（SF2）+ 数值矛盾（MF2）+ \"scale\"含义不明（SF9）。需大幅精简数字，统一 ρ 归属，澄清 scale 含义。\n\n**Introduction**: Gap 的 tautological framing 是最严重问题（MF1）。操作性定义缺失（SF6）。Contribution list 需分层。\n\n**Section 3 (Method)**: §3.1 有 instance-level/per-sample 区分但未向 Abstract/Intro 传递。Soft Jaccard 命名（SF8）。\n\n**Section 4 (Results)**: Sign test power 不足（MF3）。Table 2 与 Table 4 的 protocol 不一致（SF4）。Footnote 4 Bonferroni scope 措辞（D1）。Monotonic claim 过强（MF4）。\n\n**Section 5 (Discussion)**: Degeneracy 作为 primary diagnosis 的合理性（Q3）。与 Eikema et al. 的区分不足（MF5）。8B vs 4B 证据权重需调整（D2）。\n\n**Related Work**: 与 Yao et al. 差异化不足（SF7）。MBR differentiation paragraph 缺失（MF5）。\n\n**Limitations**: 已承认多个关键 caveats（ε post-hoc, seed 数量, scale range），质量高。但部分 caveats 与主文表述不一致（如 footnote 4 vs Limitations on ε）。\n\n**Appendix**: 质量极高。16+ sections 提供全面补充分析。但 appendix 质量不能弥补主文 framing 和统计问题。",
    "project": "struct_self_consist_ie",
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

_source line 1602 · 2026-05-17T06:42:10.900997+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3913
}
```

</details>

---


### Assistant

_source line 1603 · 2026-05-17T06:42:17.623117+00:00_

Round 16 审稿完成。

**汇总结果：**
- 评分：3.25/5（borderline Findings/Conference）
- 5 个 Must-Fix：framing 混淆（14 轮未解决）、ρ=0.42 数值矛盾、sign test 效力不足、monotonic claim 统计不显著、MBR 增量定位不清
- 9 个 Should-Fix + 2 个分歧点
- 1 轮交叉分享后收敛
- 修复路径清晰：framing 分层 + 数值统一 + bootstrap + monotonic 降级 + MBR differentiation 可升至 Conference track

报告已投递 Research Director，Issue Tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 130

## Round 130

2 recorded events


### User

_source line 1604 · 2026-05-17T06:42:20.258667+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **N1 (sign test power)**: AGREE — 但影响比 R1 判断的稍轻，因为论文核心故事是 degeneracy-gated 而非 universal null
- **N2 (3-point monotonicity)**: AGREE — 语言过强，但 per-entity-type 分析 (n=8, ρ=−0.881, p=0.004) 提供了 R1 未充分考虑的额外证据
- **N3 (Bonferroni scope)**: PARTIALLY REBUT — 数学正确但过严；论文已在 Limitations 定位为 exploratory，且 ε 值高度嵌套使 Bonferroni 过于保守
- **W1-W5**: 大部分 AGREE，W3 REBUT（LoRA-rank ablation 已控制该 confound）
- **评分**: 同意 R1 的 3.5 附近，我倾向略低 (3.0-3.5)，因 novelty concern——gap 对熟悉 MBR 文献的人 partially expected

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

_source line 1605 · 2026-05-17T06:42:30.643115+00:00_

Round 16 审稿完成。报告已投递至 Research Director。

**最终评分：3.25/5（borderline Findings/Conference）**

核心问题汇总：
- **MF1**：Framing 混淆 definitional vs empirical（14 轮未解决）
- **MF2**：ρ=0.42 数值归属错误（Figure 1/Abstract 与 Table 1 矛盾）
- **MF3**：2-seed sign test 效力不足支撑核心否定结论
- **MF4**：Monotonic claim 仅 3 dataset-level 点，p=0.066 未显著
- **MF5**：与 MBR 社区已知结论的增量未清晰 articulate

修复路径明确：全部修复可升至 Conference track；仅修复数值和统计表述适合 Findings。Issue tracker 已同步更新（含 2 个新 issue + 13 个 recurring issue 的 Round 16 记录）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 131

## Round 131

66 recorded events


### User

_source line 1606 · 2026-05-17T07:04:29.419938+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
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

_source line 1607 · 2026-05-17T07:04:34.852950+00:00_

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

_source line 1608 · 2026-05-17T07:04:34.853679+00:00_

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

_source line 1609 · 2026-05-17T07:04:39.570737+00:00_

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

_source line 1610 · 2026-05-17T07:04:39.571095+00:00_



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

_source line 1611 · 2026-05-17T07:04:46.145513+00:00_

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


### Tool call

_source line 1612 · 2026-05-17T07:04:46.397763+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "literature_map.yaml",
  "max_chars": "12000"
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
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 1613 · 2026-05-17T07:04:46.598954+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (120 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-17\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_027_fewnerd_n16** (success): LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\n- **exp_016_rerun_1024_bootstrap** (negative): 3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant. ← 基于 exp_016_rerun_1024\n  [fig_selection_gap_1024](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_016_rerun_1024_bootstrap/chart/fig_selection_gap_1024.pdf)\n- **exp_verbalized_confidence** (negative): Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \"score compression is general\" claim. If effective → important positive finding requiring narrative adjustment. ← 基于 exp_012_rerun_1024\n  [verbalized_confidence_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_verbalized_confidence/data/verbalized_confidence_summary.txt)\n\n## 趋势\n成功 70 / 负向 24 / 失败 4 / 共 120\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5
…[truncated 1164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 453
}
```

</details>

---


### Tool result

_source line 1614 · 2026-05-17T07:04:46.599673+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-14T21:00:00.000Z'\\n  total_papers: 55\\ncategories: []\\npapers:\\n  wang2023selfconsistency:\\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\\n    authors:\\n    - Xuezhi Wang\\n    - Jason Wei\\n    - Dale Schuurmans\\n    - Quoc Le\\n    - Ed Chi\\n    - Sharan Narang\\n    - Aakanksha Chowdhery\\n    - Denny Zhou\\n    year: 2023\\n    venue: ICLR 2023\\n    url: https://arxiv.org/abs/2203.11171\\n    doi: ''\\n    bibtex_key: wang2023selfconsistency\\n    category: self_consistency_reasoning\\n    role: foundation\\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\\n      from closed-form answers to structured IE outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  taubenfeld2025cisc:\\n    title: Confidence Improves Self-Consistency in LLMs\\n    authors:\\n    - Amir Taubenfeld\\n    - Tom Sheffer\\n    - Eran Ofek\\n    - Amir Feder\\n    - Ariel Goldstein\\n    - Zorik Gekhman\\n    - Gal Yona\\n    year: 2025\\n    venue: ACL Findings 2025\\n    url: https://arxiv.org/abs/2502.06233\\n    doi: 10.18653/v1/2025.findings-acl.1030\\n    bibtex_key: taubenfeld2025cisc\\n    category: self_consistency_reasoning\\n    role: direct-competitor\\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\\n      same \\\"strong predictor, weak selector\\\" gap but for structured outputs.'\\n    abstract: ''\\n    semantic_scholar_id: ''\\n    verified: true\\n    added_by: paper-research:cluster1\\n    added_at: '2026-05-14T15:47:22.188Z'\\n  kang2025selfcertainty:\\n    title: 
…[truncated 10992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 1615 · 2026-05-17T07:04:54.981319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1616 · 2026-05-17T07:04:55.483526+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 1617 · 2026-05-17T07:04:55.935457+00:00_

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

_source line 1618 · 2026-05-17T07:04:55.935767+00:00_



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

_source line 1619 · 2026-05-17T07:04:56.638323+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1620 · 2026-05-17T07:04:56.688970+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

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

_source line 1621 · 2026-05-17T07:05:01.916329+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
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
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1622 · 2026-05-17T07:05:01.967093+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/str
…[truncated 3679 chars]

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

_source line 1623 · 2026-05-17T07:05:02.369094+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool result

_source line 1624 · 2026-05-17T07:05:17.153153+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on my search results, here's the key information about EMNLP 2026 submission guidelines and author instructions:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpub
…[truncated 1965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 14784
}
```

</details>

---


### Tool call

_source line 1625 · 2026-05-17T07:05:23.577909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1626 · 2026-05-17T07:05:24.481714+00:00_

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
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1627 · 2026-05-17T07:05:24.983933+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May 2026 submission format page limit template anonymity requirements",
  "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
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
    "query": "EMNLP 2026 ARR May 2026 submission format page limit template anonymity requirements",
    "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 1628 · 2026-05-17T07:05:25.486181+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
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
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1629 · 2026-05-17T07:05:25.536781+00:00_



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


### Tool result

_source line 1630 · 2026-05-17T07:05:32.683985+00:00_

Web search results for query: "EMNLP 2026 ARR May 2026 submission format page limit template anonymity requirements"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here is the information for EMNLP 2026 ARR May 2026 submission requirements:

## Submission Format and Requirements

Both long and short paper submissions should follow all of the ARR submission requirements, including ACL's Publication Ethics Policy, and ARR's Ethics Policy including the responsible NLP research checklist.

Papers must not include authors' names and affiliations, and self-references that reveal the author
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7700
}
```

</details>

---


### Tool call

_source line 1631 · 2026-05-17T07:05:37.653780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL rolling review 2026 long paper short paper page limit format requirements",
  "allowed_domains": "['aclrollingreview.org']"
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
    "query": "ACL rolling review 2026 long paper short paper page limit format requirements",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1632 · 2026-05-17T07:05:44.175258+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'pending', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '向 Reviewer 分配审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'in_progress', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'pending', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'pending', 'activeForm': '检查外部审稿配置'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'pending', 'activeForm': '向 Reviewer 分配审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
  }
}
```

</details>

---


### Tool call

_source line 1633 · 2026-05-17T07:05:45.081583+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
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
    "file": "memory.md",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool result

_source line 1634 · 2026-05-17T07:05:45.633716+00:00_

Web search results for query: "ACL rolling review 2026 long paper short paper page limit format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Discontinuation of the MS Word Template – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/discontinuation-word-template"}]

I found information about ACL Rolling Review 2026, but I need to search for more specific details about page limi
…[truncated 3005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7979
}
```

</details>

---


### Tool result

_source line 1635 · 2026-05-17T07:05:45.634075+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 1458
}
```

</details>

---


### Tool result

_source line 1636 · 2026-05-17T07:05:45.634421+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"content\": \"# 项目记忆\\n\\n## 文献调研：一致性 ≠ 正确性（2026-05-16）\\n\\n### 调研背景\\nFew-NERD（8类粗粒度NER）上，结构一致性信号（SJ/FK/EM/VC）的 global ρ 为负或近零，selection delta 全为负。根因：模型存在 systematic bias（类型语义重叠 → 8 samples 一致但全错），暴露 self-consistency 的根本假设缺陷。\\n\\n### 最相关论文（5篇）\\n\\n#### 1. Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\\n- **Authors**: Adam Byerly, Daniel Khashabi\\n- **Year/Venue**: 2024, TACL (arXiv: 2411.01101)\\n- **关系**: **最强验证**。正式证明当 errors correlated 时，self-consistency 放大而非纠正错误\\n- **Key insight**: 长上下文任务中，positional bias 导致所有 samples 产生相关错误，违反 self-consistency 的核心假设（error independence）。Self-consistency 不仅无效，反而 actively degrades performance。实验覆盖 GPT-4o、LLaMA-3.3-70B、Qwen-2.5-72B\\n- **与我们的平行关系**: 他们的 \\\"positional bias → correlated errors\\\" 对应我们的 \\\"type semantic overlap → systematic misclassification\\\"。机制不同但失败模式完全相同\\n\\n#### 2. Consistency–Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction\\n- **Venue**: PMC (PMC12888769), 2025\\n- **关系**: **IE 领域直接验证**\\n- **Key insight**: 在 EPOP 语料（植物健康数据，实体+关系抽取）上测试 GPT/DeepSeek/Qwen/Kimi 四个模型，发现 high consistency does NOT strongly correlate with high accuracy。相关性是 model-dependent 且随 task complexity 变化。在 relational IE 中，consistency alone 不应被用作 prediction quality 的 proxy\\n- **与我们的关系**: 直接在 IE 任务上验证了我们在 NER 上的发现——一致性不等于正确性\\n\\n#### 3. Beyond Majority Voting: SCOPE (Subgroup-specific Confidence-weighted Pseudo-label Estimation)\\n- **Year/Venue**: 2024, arXiv: 2512.15146\\n- **关系**: **提出解决方案**\\n- **Key insight**: Majority voting 的问题：(1) 所有 votes 权重相同，忽略 confidence；(2) binary voting 无法捕获 fine-grained signals；(3) confirmation bias——模型强化自身错误。SCOPE 用 step-wise confidence 加权替代简单 frequency count，并通过 dynamic subgroup partitioning 平衡 quality 与 diversity\\n- **可借鉴**: confidence weighting + subgroup partitioning 思路可用于我们的
…[truncated 3363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 1637 · 2026-05-17T07:05:56.523443+00:00_

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

_source line 1638 · 2026-05-17T07:05:57.025598+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals---four instance-level (structural and surface agreement) and one per-sample (log-probability, LP)---for quality estimation and sample selection on four NER benchmarks spanning a difficulty gradient, using 4B--8B models.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction.
5	However, quality estimation does not translate to sample selection---the \textit{correlation-selection gap}: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
6	The gap has a three-layer structure: four instance-level signals cannot rank candidates within an instance by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\% identical outputs) eliminates headroom; and LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats).
7	LP selection is inversely associated with degeneracy: at 10\% (Few-NERD), $+1.36$~pp ($p{<}0.001$); at 58\% (CoNLL), LP fails.
8	In the low-degeneracy regime, LP scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
9	Closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	

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

_source line 1639 · 2026-05-17T07:05:57.025951+00:00_

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

_source line 1640 · 2026-05-17T07:05:59.183918+00:00_

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
11	These signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
12	Yet quality estimation does not translate to structural selection---the \textbf{correlation-selection gap} (the disparity between a signal's ability to rank instances reliably 
…[truncated 3753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 2157
}
```

</details>

---


### Tool call

_source line 1641 · 2026-05-17T07:05:59.234567+00:00_

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

_source line 1642 · 2026-05-17T07:05:59.235227+00:00_

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
…[truncated 3512 chars]

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

_source line 1643 · 2026-05-17T07:05:59.235636+00:00_

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

_source line 1644 · 2026-05-17T07:05:59.386681+00:00_

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
…[truncated 18253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1645 · 2026-05-17T07:05:59.437298+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_framing.md",
  "max_chars": "8000"
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
    "max_chars": "8000"
  }
}
```

</details>

---


### Tool result

_source line 1646 · 2026-05-17T07:05:59.488042+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md\", \"content\": \"# Paper Framing — struct_self_consist_ie\\n\\n> Updated 2026-05-16 — D120: exp-021 Few-NERD confirms degeneracy-gating: LP selection is regime-dependent (works at 10% degen, fails at 21%+), structural signals universally fail. 4 datasets complete. D116: Dream full review → DUAL CONTRIBUTION reframe. exp-023: LoRA rank=8 degen 7.2% vs 21% but selection still fails → multi-causal. R² on n=3 qualitative only.\\n\\n## Target Venue\\n- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)\\n- Deadline: ARR May cycle, 2026-05-25\\n\\n## Core Claims (D116 updated — DUAL CONTRIBUTION: QE positive + selection diagnostic)\\n\\n### Claim 1 (PRIMARY — Dual Contribution: QE Framework + Selection Diagnostic)\\n**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.\\n**Diagnostic contribution (B)**: Selection effectiveness is regime-dependent, governed by a degeneracy-gating mechanism:\\n- **LP selection**: degeneracy-gated — works in low-degeneracy regimes (Few-NERD 10% degen → +1.36pp, p<0.05), marginally effective at moderate degeneracy (SciERC 21% → +0.42pp, p=0.091), fails at high degeneracy (CoNLL 58% → no improvement). Monotonic gradient across 4 datasets.\\n- **Structural signals (SJ/FK/EM/VC)**: universally fail at selection regardless of degeneracy level. Even at 10% degeneracy (Few-NERD), all structural signals underperform greedy.\\n- **Multi-causal diagnosis**: (1) instance degeneracy eliminates headroom for 4/5 signals; (2) LP compression limits remaining signal; (3) reducing degeneracy (LoRA rank=8: 7.2% vs 21%) increases oracle headroom but structural signals STILL cannot exploit it → degeneracy is the gate for LP, but structural signals face a deeper de
…[truncated 6463 chars]

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

_source line 1647 · 2026-05-17T07:06:06.067824+00:00_

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

_source line 1648 · 2026-05-17T07:06:07.071951+00:00_

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
…[truncated 14803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1649 · 2026-05-17T07:06:07.222954+00:00_

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

_source line 1650 · 2026-05-17T07:06:07.574646+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text through LLM comparison \cite{chen2024usc}, sub-claim decomposition \cite{thirukovalluru2024atomic}, or hallucination detection \cite{manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement signals that assume equivalence can be determined via exact match or semantic similarity.
6	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
7	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap.
8	
9	\paragraph{Consistency for structured IE.}
10	\citet{yao2026consistency} demonstrate that consistency correlates with accuracy for LLM-based NER/RE under hard-prompting.
11	We show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression) that explain why correlation does not translate to selection gains.
12	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, where instance degeneracy is most pronounced.
13	Degeneracy varies across datasets: CoNLL (91\% single-sample F1) exhibits 58\%; SciERC (66\%) shows 21\%; Few-NERD (75\%) shows 10\%; WNUT-17 (${\approx}$42\%, macro) shows near-zero (\S\ref{sec:discussion}).
14	Few-NERD's low degeneracy despite high performance reveals that dataset-specific factors modulate degeneracy beyond model capability alone.
15	CoCoA \cite{vashurin2025cocoa} fuses confidence with consisten
…[truncated 4518 chars]

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

_source line 1651 · 2026-05-17T07:06:07.574998+00:00_

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

_source line 1652 · 2026-05-17T07:06:08.077120+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (10--58\%) collapses the candidate pool; and LP, the sole per-sample signal, is compressed to near-ineffectiveness (median range 0.041 nats).
6	LP selection effectiveness is inversely associated with instance degeneracy: at 10\% (Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 21\% (SciERC), $+0.42$~pp ($p{=}0.091$); at 58\% (CoNLL), LP fails.
7	In the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap, confirming the bottleneck is in the feature space.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline when degeneracy is low.
11	

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

_source line 1653 · 2026-05-17T07:06:08.228154+00:00_

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

_source line 1654 · 2026-05-17T07:06:08.379257+00:00_

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
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1655 · 2026-05-17T07:06:08.379704+00:00_

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

_source line 1656 · 2026-05-17T07:06:08.630775+00:00_

File content (30903 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1657 · 2026-05-17T07:06:19.184313+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "glob": "*.yaml",
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
    "glob": "*.yaml",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 1658 · 2026-05-17T07:06:19.485907+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1659 · 2026-05-17T07:06:19.636880+00:00_

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


### Tool result

_source line 1660 · 2026-05-17T07:06:19.737801+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 123\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1661 · 2026-05-17T07:06:26.210301+00:00_

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

_source line 1662 · 2026-05-17T07:06:26.260844+00:00_

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

_source line 1663 · 2026-05-17T07:06:26.261309+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
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
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1664 · 2026-05-17T07:06:26.311918+00:00_

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
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/data_integrity_audit_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_11.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_13.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_
…[truncated 122 chars]

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

_source line 1665 · 2026-05-17T07:07:00.942362+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'in_progress', 'activeForm': '向 Reviewer 分配审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer', 'status': 'in_progress', 'activeForm': '向 Reviewer 分配审稿任务'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'pending', 'activeForm': '交叉分享审稿意见'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 1666 · 2026-05-17T07:07:00.942893+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1667 · 2026-05-17T07:07:31.178058+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex\n- Appendix: `docs/paper/sections/appendix.tex`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法论严谨性**\n   - 5 个 confidence signal 的定义是否数学上严密？有无遗漏或错误？\n   - \"instance-level vs per-sample\" 的区分是否清晰且正确？\n   - MBR / consensus-proximity selection 的形式化是否完整？\n   - Soft Jaccard 的分母选择 (max 而非 union) 是否合理？论文声称差异 <0.01 但未给出证据\n\n2. **实验设计与统计分析**\n   - 4 个 NER benchmark 的选择是否合理？是否存在 cherry-picking？\n   - seed 数量（primary 1 seed, selection 2 seeds）是否足够？3-seed stability claim 是否可靠？\n   - bootstrap / sign test / TOST 等统计检验的使用是否恰当？\n   - p 值报告是否一致？多重比较校正是否充分？\n   - 论文声称 \"correlation-selection gap\" 时的统计基础是否牢固？\n   - degeneracy 与 LP selection 的 n=3 datasets 梯度关系是否过度解读？\n   - LoRA rank=8 ablation: 7.2% vs 21% degeneracy 但 selection 仍失败——这是否足以支撑 \"necessary but not sufficient\" 的 claim？\n\n3. **Claim 与 Evidence 对应**\n   - 每个 Contribution 是否有充分的实验支撑？\n   - 负面结果的解读是否过度？（e.g., \"fails\" vs \"not statistically significant\"）\n   - Oracle headroom 的计算方式是否合理？\n   - 自由格式解码 ablation 的结论（\"compression is model-intrinsic\"）是否过强？\n\n4. **实验可复现性**\n   - 训练细节是否充分（LoRA 参数、学习率、batch size、epoch、data split）？\n   - 推理设置是否完整（vLLM 版本、constrained decoding 细节）？\n   - 评估 protocol 是否清晰（gold-filtered vs full-set 的切换）？\n\n请按以下格式输出审稿报告：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n## Questions (需要作者澄清)\n## Missing References\n## Detailed Comments (逐节)\n## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)\n## Confidence (1-5)\n```",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验设计**\n\n### Venue 信息\n- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex\n- Appendix: `docs/paper/sections/appendix.tex`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **方法论严谨性**\n   - 5 个 confidence signal 的定义是否数学上严密？有无遗漏或错误？\n   - \"instance-level vs per-sample\" 的区分是否清晰且正确？\n   - MBR / consensus-proximity selection 的形式化是否完整？\n   - Soft Jaccard 的分母选择 (max 而非 union) 是否合理？论文声称差异 <0.01 但未给出证据\n\n2. **实验设计与统计分析**\n   - 4 个 NER benchmark 的选择是否合理？是否存在 cherry-picking？\n   - seed 数量（primary 1 seed, selection 2 seeds）是否足够？3-seed stability claim 是否可靠？\n   - bootstrap / sign test / TOST 等统计检验的使用是否恰当？\n   - p 值报告是否一致？多重比较校正是否充分？\n   - 论文声称 \"correlation-selection gap\" 时的统计基础是否牢固？\n   - degeneracy 与 LP selection 的 n=3 datasets 梯度关系是否过度解读？\n   - LoRA rank=8 ablation: 7.2% vs 21% degeneracy 但 selection 仍失败——这是否足以支撑 \"necessary but not sufficient\" 的 claim？\n\n3. **Claim 与 Evidence 对应**\n   - 每个 Contribution 是否有充分的实验支撑？\n   - 负面结果的解读是否过度？（e.g., \"fails\" vs \"not statistically significant\"）\n   - Oracle headroom 的计算方式是否合理？\n   - 自由格式解码 ablation 的结论（\"compression is model-intrinsic\"）是否过强？\n\n4. **实验可复现性**\n   - 训练细节是否充分（LoRA 参数、学习率、batch size、epoch、data split）？\n   - 推理设置是否完整（vLLM 版本、constrained decoding 细节）？\n   - 评估 protocol 是否清晰（gold-filtered vs full-set 的切换）？\n\n请按以下格式输出审稿报告：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n## Questions (需要作者澄清)\n## Missing References\n## Detailed Comments (逐节)\n## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)\n## Confidence (1-5)\n```",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
````

</details>

---


### Tool result

_source line 1668 · 2026-05-17T07:07:57.441678+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26263
}
```

</details>

---


### Tool call

_source line 1669 · 2026-05-17T07:07:58.244975+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex\n- Appendix: `docs/paper/sections/appendix.tex`\n- References: `docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献评估**\n   - \"correlation-selection gap\" 概念是否真正 novel？是否只是重新包装了已知现象（e.g., MBR 在某些任务上失败）？\n   - 与 Nédellec & Xia (2026) 的 consistency-accuracy correlation 工作相比，增量贡献有多大？\n   - \"instance degeneracy\" 是否只是 fine-tuned model 的 trivial 属性（更好的模型输出更一致）？\n   - 论文的核心 insight 是否足以支撑 EMNLP 主会议长文？还是更适合 Findings/Workshop？\n   - \"quality estimation succeeds but selection fails\" 的 framing 是否有足够的实际意义？\n\n2. **Related Work 完整性**\n   - 自检以下 citation 是否被引用或讨论：\n     - MBR decoding 在 NLP 中的成功/失败案例（MT vs 其他任务）\n     - Self-consistency 失败模式的分析（e.g., Byerly & Khashabi 2024 on correlated errors）\n     - LLM-based NER 的最新进展（UniNER, GoLLIE, CodeIE 等）\n     - Structured prediction uncertainty estimation（CRF-based, sequence labeling calibration）\n     - Diversity collapse in fine-tuned models\n   - 引用数量是否达到 EMNLP 主会议水平？（通常 40-60 篇）\n   - 是否有 hallucinated citations？请逐一检查关键引用的真实性\n\n3. **写作质量 — AI 写作痕迹检查（硬规则）**\n   - 全文搜索 em-dash (—) 和解释性 en-dash (–)：每处标记\n   - 搜索 \"-ing,\" 结尾的分词短语\n   - 搜索过度使用的过渡词（Furthermore/Moreover/Additionally 连续出现）\n   - 搜索 AI 用词黑名单：delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift/novel（过度使用）\n   - 段落是否过度分段（每 2-3 句换段）？\n   - 专有名词首次出现是否有定义？\n   - Abstract 中的缩写是否在 Abstract 内定义？\n\n4. **格式合规**\n   - 页数是否在 8 页以内（正文）？\n   - 匿名化是否彻底？（检查 \\author, 文中有无 self-citation 泄露身份）\n   - 图表 caption 是否 self-contained？\n   - 表格格式：小数精度是否统一？最优加粗？\n   - 图中字体是否 ≥7pt？\n\n5. **叙事结构与 Framing**\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线？\n   - Introduction 的 5 段结构是否完整？\n   - 论文是\"故事驱动\"还是\"实验报告\"风格？\n   - Contribution list 中的每一条是否在前文有铺垫且有后续实验支撑？\n\n请按以下格式输出审稿报告：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n## Questions (需要作者澄清)\n## Missing References\n## Detailed Comments (逐节)\n## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)\n## Confidence (1-5)\n```",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性 + 写作质量**\n\n### Venue 信息\n- 目标: EMNLP 2026 Main Conference (via ARR May 2026 cycle)\n- 截止日期: 2026-05-25\n- 页数限制: 长文 8 页正文（Limitations/Ethics/References/Appendix 不计入）\n- 模板: ACL style (`\\usepackage[review]{acl}`)\n- 匿名规则: double-blind\n\n### 论文路径\n- 主文件: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各章节在 `docs/paper/sections/` 下: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex\n- Appendix: `docs/paper/sections/appendix.tex`\n- References: `docs/paper/references.bib`\n\n### 你的审查重点\n\n请从以下维度严格评审：\n\n1. **新颖性与贡献评估**\n   - \"correlation-selection gap\" 概念是否真正 novel？是否只是重新包装了已知现象（e.g., MBR 在某些任务上失败）？\n   - 与 Nédellec & Xia (2026) 的 consistency-accuracy correlation 工作相比，增量贡献有多大？\n   - \"instance degeneracy\" 是否只是 fine-tuned model 的 trivial 属性（更好的模型输出更一致）？\n   - 论文的核心 insight 是否足以支撑 EMNLP 主会议长文？还是更适合 Findings/Workshop？\n   - \"quality estimation succeeds but selection fails\" 的 framing 是否有足够的实际意义？\n\n2. **Related Work 完整性**\n   - 自检以下 citation 是否被引用或讨论：\n     - MBR decoding 在 NLP 中的成功/失败案例（MT vs 其他任务）\n     - Self-consistency 失败模式的分析（e.g., Byerly & Khashabi 2024 on correlated errors）\n     - LLM-based NER 的最新进展（UniNER, GoLLIE, CodeIE 等）\n     - Structured prediction uncertainty estimation（CRF-based, sequence labeling calibration）\n     - Diversity collapse in fine-tuned models\n   - 引用数量是否达到 EMNLP 主会议水平？（通常 40-60 篇）\n   - 是否有 hallucinated citations？请逐一检查关键引用的真实性\n\n3. **写作质量 — AI 写作痕迹检查（硬规则）**\n   - 全文搜索 em-dash (—) 和解释性 en-dash (–)：每处标记\n   - 搜索 \"-ing,\" 结尾的分词短语\n   - 搜索过度使用的过渡词（Furthermore/Moreover/Additionally 连续出现）\n   - 搜索 AI 用词黑名单：delve/leverage/utilize/facilitate/myriad/plethora/paradigm shift/novel（过度使用）\n   - 段落是否过度分段（每 2-3 句换段）？\n   - 专有名词首次出现是否有定义？\n   - Abstract 中的缩写是否在 Abstract 内定义？\n\n4. **格式合规**\n   - 页数是否在 8 页以内（正文）？\n   - 匿名化是否彻底？（检查 \\author, 文中有无 self-citation 泄露身份）\n   - 图表 caption 是否 self-contained？\n   - 表格格式：小数精度是否统一？最优加粗？\n   - 图中字体是否 ≥7pt？\n\n5. **叙事结构与 Framing**\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 是否形成连贯主线？\n   - Introduction 的 5 段结构是否完整？\n   - 论文是\"故事驱动\"还是\"实验报告\"风格？\n   - Contribution list 中的每一条是否在前文有铺垫且有后续实验支撑？\n\n请按以下格式输出审稿报告：\n```\n## Summary (2-3 句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Must-Fix] / [Should-Fix] / [Minor])\n## Questions (需要作者澄清)\n## Missing References\n## Detailed Comments (逐节)\n## Overall Score (strong reject / weak reject / borderline / weak accept / strong accept)\n## Confidence (1-5)\n```",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
````

</details>

---


### Tool result

_source line 1670 · 2026-05-17T07:07:59.711310+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1466
}
```

</details>

---


### Assistant

_source line 1671 · 2026-05-17T07:08:04.178652+00:00_

Round 1 任务已分配给两位 Reviewer。等待审稿结果返回。

- **Reviewer 1**（方法严谨性 + 实验设计）：已触发
- **Reviewer 2**（新颖性 + 完整性 + 写作质量）：已触发

收到两位 Reviewer 的报告后，将执行 Step 2 交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 132

## Round 132

2 recorded events


### User

_source line 1672 · 2026-05-17T07:12:19.338544+00:00_

[Reviewer 1 审稿意见]:

# Round 1 Review — Reviewer 1 (方法严谨性 + 实验设计)

**Paper**: "Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction"

---

## Summary (2-3 句)

本文系统评估了 5 种 confidence signals 在 LLM-based NER 中的 quality estimation 和 sample selection 能力，发现 QE 成功但 selection 失败（correlation-selection gap），并通过 instance degeneracy 和 LP compression 两个机制给出诊断。实验设计严谨度高于平均水准（多数据集、多模型、多 seed、bootstrap/TOST 统计检验），但部分核心 claim 的因果推断证据不足，跨数据集梯度 n=3 支撑的泛化结论需要审慎对待。

---

## Strengths

1. **问题定义清晰且有贡献** (Section 1, 3.3): "correlation-selection gap" 的概念化有价值——将 QE 和 selection 明确解耦，指出一个被 prior work 忽略的 confound。instance-level vs per-sample 的形式化区分（Section 3.1）简洁且数��上正确。

2. **实验设计的系统性** (Section 4): 4 个 NER benchmark 构成 difficulty gradient（WNUT-17 collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个数据集的角色清晰。两个模型族（Qwen3-8B, LLaMA-3.1-8B）加 4B/3B ablation 排除模型特异性。

3. **统计方法论上佳** (Section 4.3, Appendix): Bootstrap CI（B=10,000）、paired sign test、TOST 等效性检验、Bonferroni 校正、Kendall's W 排名稳定性、Fisher 合并 p 值——统计工具选择恰当，且在负面结果中使用 TOST 避免了"absence of evidence = evidence of absence"的谬误。

4. **三层诊断结构有说服力** (Section 4.3): (a) instance-level 信号 by construction 不能排名候选 → (b) MBR with aligned utility 因 degeneracy 失败 → (c) LP 有 per-sample 信息但被 compression 限制。逻辑递进清晰。

5. **负面结果的审慎表达**: 论文多处使用"inversely associated with"而非"causes"，使用"necessary but not sufficient"限定 claim，Limitations 节详尽列举未覆盖条件。

6. **Appendix 丰富且组织有序**: 涵盖 FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等，大多数潜在反驳都有对应的 ablation 或 control。

---

## Weaknesses

### [Must-Fix] W1: 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)

- **位置**: Section 4.4 (Table 4), Section 5 "Regime boundaries", Figure 3
- **问题**: 论文的核心 claim 之一是 "LP selection effectiveness is inversely associated with degeneracy rate across datasets"，但这一梯度仅基于 n=3 数据集（CoNLL 58% → SciERC 21% → Few-NERD 10%）。任何三个数据点的单调排列概率为 1/3!= 1/6，即使在随机条件下也有 16.7% 的概率出现单调趋势。
- **补充**: 论文试图用 entity-type-level analysis（n=8, ρ=-0.881, p=0.004）加强论证，但 entity type 之间共享同一模型、同一 checkpoint、同一 inference pipeline，违反独立性假设。不同 entity type 的 degeneracy 差异可能源自 type frequency、schema complexity 等混淆变量，而非 degeneracy 本身直接导致 LP selection 差异。
- **Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测**，统计上有问题：cross-dataset aggregates 和 per-entity-type points 的方差结构完全不同，不应直接 pool。
- **为什么影响接收**: 如果 degeneracy 梯度的因果解释不成立，Contribution 3 的基础动摇。
- **建议**: (a) 增加至少 2-3 个数据集的实验（如 OntoNotes、ACE05）扩大 n；(b) 用 Few-NERD 内 entity-type analysis 时，控制 type frequency 和 entity boundary difficulty 等混淆变量；(c) 不要 pool 不同粒度的观测到同一 correlation。

### [Must-Fix] W2: "Necessary but not sufficient" claim 的 LoRA-rank ablation 存在混淆变量

- **位置**: Section 4.5 "LoRA-rank ablation" (line: "Low degeneracy is thus a necessary but not sufficient condition for selection")
- **问题**: LoRA rank=8 ablation 降低了 degeneracy (21% → 7.2%) 且增加了 oracle headroom (13.3 → 16.0 pp)，但 LP selection 仍失败。论文据此声称 degeneracy 是 "necessary but not sufficient"。但 LoRA rank=8 同时降低了模型能力（greedy F1: 0.645 → 0.640），改变了学到的 representation space。LP compression 在 rank=8 下可能因模型能力下降而加剧，而非因为 degeneracy 本身不充分。
- **矛盾**: Few-NERD 在 10% degeneracy 下 LP selection 成功 (+1.36 pp)，而 rank=8 SciERC 在 7.2% degeneracy 下仍失败。如果 degeneracy 是唯一 gating factor，Few-NERD 的成功和 rank=8 SciERC 的失败之间的差异需要更好的解释。论文在 Section 4.4 简要提到 "LP signal quality (ρ) provides an additional prerequisite"，但这实质上是在说 degeneracy + LP quality 联���决定 selection，而非 degeneracy alone is necessary。
- **为什么影响接收**: "Necessary but not sufficient" 是一个精确的逻辑声明；当前实验设计无法将 degeneracy 从 LP compression 中独立隔离。
- **建议**: (a) 明确指出 LoRA rank ablation 同时改变了多个变量（degeneracy、model quality、LP compression degree），不能做 clean causal attribution；(b) 将 claim 弱化为 "low degeneracy co-occurs with LP selection success, but rank-8 ablation shows it is not alone sufficient"；(c) 最好提供 rank=8 下的 LP compression 统计（median LP range、tied fraction），以量化 compression 在两种 rank 下的变化。

### [Should-Fix] W3: 负面结果的统计功效 (power) 未报告

- **位置**: Section 4.3 (Table 3, "LP achieves only 0.647, Δ=+0.2 pp, d=0.038, p=0.29")
- **问题**: 论文的中心论点是负面结果（selection 不显著优于 greedy）。对于负面结果，需要报告 power analysis：在当前样本量 (n=529) 和 seed 数量 (2) 下，检测 1 pp 效应（一个实际有意义的改进）的统计功效是多少？如果 power 很低（如 <50%），则 p=0.29 无法区分 "真的没效果" 和 "效果存在但检测不到"。
- **TOST 部分缓解了这个问题** (Appendix D)，但 TOST 使用的 δ=2pp (internal anchor) 是否过宽？externally anchored δ=1.0pp 下，SciERC 未通过 TOST。
- **为什么影响评分**: 虽然 TOST 是好的补充，但主文没有明确讨论 power，可能误导读者认为 "p>0.05" 等同于 "确认无效果"。
- **建议**: 在 main text 或 appendix 中加入 post-hoc power analysis，报告当前设计检测 Δ=1pp 的 power；或者明确指出 Few-NERD (n=32,565) 的结果 (LP +1.36 pp, p<0.001) 才是 definitive evidence，SciERC 的 non-significance 可能受限于 power。

### [Should-Fix] W4: "Compression is model-intrinsic" 的结论与 RE 结果矛盾

- **位置**: Section 5 "Ablation: free-form decoding" + Appendix H (Table 8)
- **问题**: 论文 NER free-form ablation 发现 LP 分布几乎不变 (std ratio 0.97)，据此声称 "compression is model-intrinsic rather than constraint-imposed"。但 RE 的 free-form decoding 显著恢复了 LP selection (+2.35 pp, p=0.025)，直接证明 constraints DO compress LP for RE。
- **论文在 Section 5 最后简要提到这一分歧**，但 Abstract 和 Introduction 中 "compression is model-intrinsic" 的 framing 没有 qualification。读者如果只看主文可能误以为这是普适结论。
- **为什么影响评分**: 论文的诊断框架混淆了 task-specific behavior 和 universal mechanism。
- **建议**: (a) 将主文 claim 限定为 "for NER, compression is model-intrinsic; for RE, constraint-imposed mechanisms contribute significantly"；(b) 在 Abstract 或 Introduction 的 diagnostic chain 描述中加入 task qualifier。

### [Should-Fix] W5: Primary seed (seed=42) 的代表性与 selection 实验的 2-seed 限制

- **位置**: Section 4.1 footnote 4 ("Quality estimation uses a single primary seed; selection uses 2-seed averages")
- **问题**: QE 主结果仅 1 seed，selection 仅 2 seeds。虽然 Table 6 的 3-seed stability test 显示 σ≤0.026 for ρ rankings，但 selection F1 的 seed variance 未被同样充分量化。Table 3 报告的 selection F1 σ（如 LP: ±0.005）基于仅 2 seeds 的极差，这不是可靠的 variance estimate。
- **Few-NERD 是 1-seed result** (Table 4)，尽管 n=32,565 提供了足够 statistical power，但 systematic bias（如训练 seed 影响 degeneracy rate）仍可能存在。
- **建议**: 至少为 Few-NERD 的核心 selection 结果 (LP +1.36 pp) 添加 2-3 seed replication；或者在 Limitations 中更明确指出 selection 结果的 seed coverage 比 QE 更有限。

### [Should-Fix] W6: Few-NERD 训练配置差异未充分讨论

- **位置**: Appendix L ("3 epochs" for Few-NERD vs. 5 epochs for SciERC/CoNLL)
- **问题**: Few-NERD 仅训练 3 epochs（vs. 其他数据集的 5 epochs），这可能直接导致 lower degeneracy（更少训练 → 更弱模型 → 更多 diversity）。如果 Few-NERD 的低 degeneracy 部分源自 under-training 而非数据集固有特性，则 degeneracy-selection 关系的因果方向被混淆。
- **论文在 Discussion 中提到** "dataset-specific factors (number of entity types, semantic overlap) also modulate the rate"，但没有排除 training epoch 差异这一 confound。
- **建议**: 在 appendix 中添加 epoch sensitivity 分析（如 Few-NERD 5 epoch 的 degeneracy rate），或明确讨论为何使用 3 epochs（early stopping? 收敛?）。

### [Minor] W7: Soft Jaccard 分母选择的 claim 缺乏完整表达

- **位置**: Section 3.2, Equation 4, footnote
- **问题**: 论文声称 max vs union normalizer 差异 Δρ<0.01，并在 Appendix (Table 5) 给出了 6 个 model-dataset combinations 的证据。这实际上是充分的。但 footnote 的表述 "nearly identical rankings (Δρ<0.01; Table X)" 暗示这是所有条件下的 bound，而表中最大差异是 0.009——距 0.01 仅一个量级，更准确的表述是 "|Δρ| ��� 0.009"。
- **建议**: 微调措辞精度即可。

### [Minor] W8: Table 3 与 Table 4 的 greedy F1 不一致可能困惑读者

- **位置**: Table 3 (SciERC greedy=0.645), Table 4 (SciERC greedy=0.614)
- **问题**: 两表使用不同 evaluation protocol (gold-filtered n=529 vs. full-set n=551)，导致同一模型的 greedy F1 差 3.1 pp。虽然 Table 4 有脚注解释，但读者在主文中连续看到两个不同的 baseline 数字时容易困惑。
- **建议**: 统一 evaluation protocol，或在 Table 4 同时报告 gold-filtered 数字。

---

## Questions (需要作者澄清)

**Q1**: Section 4.5 LoRA rank=8 ablation 中，LP 的 median within-instance range 是多少？如果 rank=8 下 LP range 显著小于 rank=32 下的 0.041 nats，则 selection failure 可归因于更严重的 compression 而非 degeneracy 本身不充分���

**Q2**: Few-NERD 训练为何仅 3 epochs？是否有 early stopping 或 validation loss plateau 的证据？5 epochs 下的 degeneracy rate 是多少？

**Q3**: Table 3 的 sign test 使用的是 instance-level 配对（对每个 instance 比较 LP-selected F1 vs greedy F1），还是 corpus-level 比较？如果是 instance-level，n=529 × 2 seeds = 1058 paired observations 应该有更强的 power。

**Q4**: Within-instance SJ-F1 ρ=0.52 (Section 5) 报告为 median；distribution 如何？有多少比例的 non-degenerate instances 有 ρ<0？如果大量 instances 的 within-instance correlation 为负或接近零，则 "well-aligned utility" 的 claim 需要 qualify。

**Q5**: Entity-type-level degeneracy-LP gain 分析（Appendix, ρ=-0.881, p=0.004, n=8）中，是否考虑过 entity type frequency 或 average entity count per sentence 作为 confound？高频类型可能同时有 higher degeneracy 和 lower selection gain，但因果机制可能是 frequency → model confidence → degeneracy + LP compression，而非 degeneracy → LP failure。

---

## Missing References

1. **Best-of-N with process reward models**: Lightman et al. (2024) "Let's Verify Step by Step" 在 math reasoning 中展示了 verifier-based BoN 的 scaling law——与本文"需要 learned verifier"的结论直接相关，已引用但可更深入对比。
2. **Self-consistency for structured prediction beyond NER**: Yoran et al. (2023) "Answering Questions by Meta-Reasoning over Multiple Chains of Thought" 和 Li et al. (2023) "Making Language Models Better Reasoners with Step-Aware Verifier" 在 structured reasoning 中有类似 gap 的发现。
3. **Diversity in fine-tuned models**: Zhang et al. (2024) "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters" (DeepMind) 讨论了 fine-tuned model 的 diversity collapse 与 test-time compute 的关系——直接相关。
4. **MBR for structured prediction**: Eikema et al. (2025) "Structured MBR" 已引用但可更详细讨论为何 IE 的 bag-of-unit mismatch 比 MT 更严重。

---

## Detailed Comments (逐节)

### Abstract
- 信息密度高，四个必答问题都有覆盖。
- "correlation-selection gap" 概念在 Abstract 中引入但未定义（主文 Section 4.3 才定义），建议用一句简短释义。
- 数字选择合理（ρ, AUROC, pp gains, p values）。

### Introduction
- 叙事线清晰：从 self-consistency 的成功切入 NER 的结构性挑战。
- Contribution 3 "Degeneracy as a regime boundary" 的 claim 在 Introduction 中比实际证据更强（写作是 "inversely associated" 但 structure 暗示因果）。

### Method (Section 3)
- 形式化清晰。5 个 signal 的数学定义完整且正确。
- Fleiss' κ 的 adaptation 有 independence concern（已在 Appendix B 用 permutation test 验证，充分）。
- MBR/consensus-proximity 的等价性证明 (Appendix C, LOO-SJ) 是好的补充。

### Experiments (Section 4)
- 数据集选择合理且角色分工清晰。
- 训练细节 (Appendix E, Table 7) 充分：LoRA config、optimizer、batch size、epoch 均报告。
- vLLM + XGrammar constrained decoding 描述清楚；但 vLLM 版本号未报告（影响 reproducibility）。

### Discussion (Section 5)
- 这一节承载了大量 ablation 和 diagnostic 结果，密度极高。
- Entity-token LP ablation 的 negative result 是好的：排除了 format-token dilution 作为 primary cause。
- Signal combination 失败（logistic regression、MLP、RF）有力支撑了 "feature space bottleneck" 的结论。
- "Practical considerations" 段落实用价值高（N=8 suffices for QE, cost-benefit for selection is unfavorable）。

### Limitations
- 全面且诚实（scale limitation、seed coverage、untested verifier、ε post-hoc choice）。
- 建议补充: power analysis limitation、Few-NERD epoch confound。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 主要 claims 有充分支撑（QE works, selection fails），但核心因果诊断（degeneracy gates LP selection）的证据基础偏薄（cross-dataset n=3, entity-type confounds, LoRA ablation 混淆变量）。统计方法使用恰当。 |
| Excitement | 3.5/5 | "Correlation-selection gap" 是 useful conceptual contribution，对 test-time compute scaling 社区有 immediate practical value（告诉 practitioner 何时 BoN 不工作）。但核心发现是 negative result + diagnostic，novelty 在于 framing 而非 new method。 |
| Reproducibility | 4/5 | 训练 config 完整 (Table 7)，prompt template 提供，constrained decoding 细节清楚。缺 vLLM 版本号，缺部分配置的 exact random seeds for selection experiments。Code release upon acceptance 声明。 |

---

## Overall Score

**Borderline Accept (3.5/5)**

论文的实验工作量大、统计处理严谨、negative results 的报告方式远超平均水平。"Correlation-selection gap" 的概念化和三层诊断对社区有价值。主要扣分来自：(1) 核心因果 claim（degeneracy as regime boundary）的证据基础偏弱（n=3 datasets, confounded ablation）；(2) "model-intrinsic compression" claim 与 RE 结果矛盾但主文未充分 qualify。如果作者能在 rebuttal 中：(a) 提供 LoRA rank=8 下的 LP compression statistics，(b) 澄清 Few-NERD epoch confound，(c) 弱化/qualify 因果语言，我倾向接收。

---

## Confidence

**4/5** — 我对方法论和统计分析的评估有信心；对 NER/IE 领域的 related work coverage 有较好把握，但未验证所有 appendix 中的数值计算。


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

_source line 1673 · 2026-05-17T07:12:26.544457+00:00_

Reviewer 1 的审稿意见已收到。等待 Reviewer 2 的审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1674 · 2026-05-17T07:12:29.643618+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

总结：我给出 **Borderline Accept (3.5/5)** 的评分。论文实验量大、统计严谨、negative results 的处理方式优秀，"correlation-selection gap" 概念有价值。主要问题集中在：

1. **[Must-Fix]** 跨数据集 degeneracy 梯度仅 n=3，因果推断证据不足
2. **[Must-Fix]** LoRA rank=8 ablation 的 "necessary but not sufficient" claim 存在未隔离的混淆变量
3. **[Should-Fix]** 负面结果缺少 power analysis
4. **[Should-Fix]** "compression is model-intrinsic" 与 RE free-form results 矛盾但主文未 qualify
5. **[Should-Fix]** Few-NERD 训练 epoch 差异可能 confound degeneracy 比较
6. **[Should-Fix]** Selection 实验 seed coverage 有限（1-2 seeds）

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

_source line 1675 · 2026-05-17T07:12:34.953387+00:00_

Reviewer 1 审稿报告已收到。等待 Reviewer 2 完成初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 134

## Round 134

8 recorded events


### User

_source line 1676 · 2026-05-17T07:13:42.126290+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

**论文**: "Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**审查侧重**: 新颖性 + 完整性 + 写作质量

---

## Summary (2-3 句)

本文系统评估了五种置信度信号在 LLM-based NER 中的质量估计（QE）和样本选择表现，发现 QE 成功但 selection 失败，并将失败归因于 instance degeneracy 和 LP compression。这是一篇以诊断为核心的 negative result 论文，分析扎实但实际贡献偏向观察和归因，缺乏可操作的方法提出。

---

## Strengths (逐条)

**S1. 问题 framing 清晰且有价值。** "Correlation-selection gap" 概念将两个通常被混淆的任务（QE vs. selection）明确分离，对该领域后续研究有 conceptual guidance 意义。

**S2. 实验设计全面且系统。** 四个数据集构成 difficulty gradient（WNUT-17 → SciERC → Few-NERD → CoNLL），两个 model families + 4B ablation，$N$ 和 $T$ 的系统变化，三层诊断链（construction → degeneracy → compression），ablation 覆盖 LoRA rank、free-form decoding、entity-token LP、supervised verifier。

**S3. 统计严谨性高。** 使用 paired sign tests、bootstrap CIs、Bonferroni correction、TOST equivalence testing。明确区分 "absence of evidence" 和 "evidence of absence"。多 seed 实验确认 ranking stability。

**S4. Negative result 的论证逻辑完整。** 三层结构（by construction → degeneracy → compression）层层递进，supervised verifier baseline 确认 bottleneck 在 feature space 而非 aggregation，使负面结果具有诊断价值。

**S5. Related work 覆盖面广。** 59 篇引用，覆盖 self-consistency、MBR decoding、uncertainty estimation、best-of-N、diversity collapse 等多个相关方向。与 Yao et al. (2026) 的区分清楚。

---

## Weaknesses (逐条)

### Must-Fix 问题

**W1** [Must-Fix] **核心概念 "correlation-selection gap" 的新颖性有限**

- 具体位置：Section 1 (Introduction), Section 4.2
- 问题：该 "gap" 本质上是一个已知的 observation 的 repackaging：instance-level signals 无法区分同一 input 的不同 outputs 是其定义的直接推论（论文自己称 "by construction"）；MBR 在 structured outputs 上失败已有文献指出 (Eikema et al., 2025)；fine-tuned models 的 diversity collapse 是 Kirk et al. (2024) 和 Yun et al. (2025) 的已知现象。
- 论文的核心 insight 可以简化为：(1) instance-level signals 不能做 per-sample ranking（trivial by definition），(2) fine-tuned models 输出太一致（known），(3) LP 被 format tokens 压缩（specific but minor）。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。
- 为什么影响接收：如果核心 framing 被认为是重新包装已知观察，论文的 contribution bar 不够 main conference。
- 建议修改方向：需要更清楚地 articulate 为什么诊断本身（而非解决方案）值得作为独立 contribution，或增加可操作的方法（如基于诊断设计的 targeted remedy）。

**W2** [Must-Fix] **"Instance degeneracy" 作为概念贡献的独立性不足**

- 具体位置：Section 5 (Discussion), Table 5
- 问题：论文将 instance degeneracy 描述为 gap 的核心原因，但同时承认 "the better the model, the less room for selection to add value"（Section 5, line 15）。这使得 degeneracy 不是一个 "failure mechanism" 而是 model success 的 natural consequence。CoNLL 58% degeneracy 对应 91% F1——模型已经很好了，当然输出一致。Few-NERD 10% degeneracy 对应 75% F1——不是 degeneracy "low" 而是模型在该任务上 underfit。
- 为什么影响接收：如果 degeneracy 是 model capability 的 trivial correlate，那 "degeneracy gates LP selection" 本质上等价于 "LP selection only works when the model is bad enough to produce diverse wrong answers"，这降低了发现的意义。
- 建议修改方向：需要用 Few-NERD 的反例（75% F1 但仅 10% degeneracy）更有力地论证 degeneracy 不完全是 capability 的 proxy，进一步分析什么 dataset/task properties 独立于 capability 影响 degeneracy。

**W3** [Must-Fix] **缺乏任何可操作的 positive contribution**

- 具体位置：Section 6 (Conclusion), Section 5 (Discussion, "Pilot remedy")
- 问题：论文的全部 takeaway 是 "closing the gap requires trained verifiers"（最后一句话 cite Cobbe et al., 2021），但：(a) 不训练 verifier，(b) 不提出新 signal，(c) entity-token LP 作为唯一 remedy 被证明失败。一篇纯诊断性论文在 EMNLP main conference 需要极强的 insight novelty 来补偿缺乏 actionable method 的问题。
- 为什么影响接收：ARR 的 excitement 评分要求 "I would mention this paper to others"——一篇结论为 "现有方法都不行，需要 future work" 的论文很难达到这个 bar。
- 建议修改方向：(1) 增加一个 lightweight trained verifier baseline 来验证诊断的 actionability，或 (2) 将论文定位为 Findings 而非 main conference。

### Should-Fix 问题

**W4** [Should-Fix] **LaTeX em-dash (`---`) 过度使用，存在 AI 写作风格痕迹**

- 具体位置：全文，共 90 处（正文约 35 处，Appendix 55 处）
- 问题：Abstract 2 处、Introduction 7 处、Experiments 9 处、Discussion 14 处。平均每段出现 1-2 个解释性 em-dash。例如：
  - "Self-consistency---majority voting over multiple samples---yields..."（Introduction L3）
  - "quality estimation does not translate to sample selection---the correlation-selection gap"（Abstract L5）
  - "fine-tuned models produce identical outputs for 10--58\% of instances, eliminating selection headroom despite positive within-instance utility--F1 correlation"（Introduction L13）
- 这是 AI 生成文本的典型标志，经验丰富的审稿人会注意到。正文部分至少应减少到 10 处以内。
- 建议：用逗号、括号或拆分为两句替代大部分 em-dash。

**W5** [Should-Fix] **Abstract 和 Introduction 过度堆砌数字，报告风格重于故事风格**

- 具体位置：Abstract（10 行中包含约 15 个具体数字）、Introduction（contribution list）
- 问题：Abstract 第 4 行 "$\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82"；第 6 行 "$\rho{=}0.52$... 10--58\%... median range 0.041 nats"。读者在 30 秒内无法消化这些数字。Introduction 的 contribution list 同样堆砌了大量具体 $\rho$ 和 pp 值。
- 故事线（Why does SC fail for NER?）是有吸引力的，但被数字淹没了。
- 建议：Abstract 中保留 2-3 个最关键的数字，其余用定性描述。Introduction contribution 中减少内嵌统计。

**W6** [Should-Fix] **与 Yao et al. (2026) 的增量贡献需更明确的差异化**

- 具体位置：Section 2 (Related Work, "Consistency for structured IE" paragraph)
- 问题：论文承认 Yao et al. (2026) 已证明 consistency-accuracy correlation 存在。本文的 claimed extension 是 (1) fine-tuned models, (2) QE/selection 分离, (3) failure diagnosis。但 (1) 是实验设置变化而非方法贡献，(3) 的核心发现（degeneracy + compression）如 W1-W2 所述是较 predictable 的。
- 建议：增加一个直接的 Table 或 Figure 对比 Yao et al. 的 setting/findings 与本文的差异。

**W7** [Should-Fix] **Missing reference: Byerly & Khashabi (2024) "Self-Consistency Falls Short"**

- 这是关于 self-consistency 失败模式的直接相关工作（arXiv:2411.01101），讨论了 correlated errors 导致 SC 失败的机制。本文的 "instance degeneracy" 与他们的 "correlated errors from architectural biases" 是相关的失败模式——应该引用并讨论区别。

**W8** [Should-Fix] **Discussion section 过长，部分内容适合移入 Appendix**

- 具体位置：Section 5，约占 2+ 页
- 问题："Hypotheses for LP compression"（4 个假设的列举）、"Signal combinations"（3 种策略均失败的报告）、"Effect of sample count" 和 "Effect of sampling temperature" 都是 robustness/ablation 内容，更适合 Appendix。Discussion 应聚焦 high-level implications。
- 影响：可能导致正文超 8 页（需确认编译后页数）。

### Minor 问题

**M1** [Minor] Appendix L235 使用 "leverage"（AI 用词黑名单）："Structural signals leverage $\binom{N}{2}$ pairwise comparisons"。

**M2** [Minor] Abstract 中 "LP" 首次出现时虽有括号解释 "(log-probability, LP)" 但 "NER" 和 "MBR" 未在 Abstract 内定义。

**M3** [Minor] Table 3 (selection) 中 EM 和 VC 没有 $p$ 值，仅标 "---"，但 caption 说 "$p$ vs. greedy baseline from paired sign tests"——应解释为何省略。

**M4** [Minor] Figure 2 caption 中 "dashed line at ~15%" 使用了 "~" 而非精确值——如果是 threshold claim 应提供更严格的定义。

**M5** [Minor] `---` 在 LaTeX 中生成 em-dash 但 `--` 生成 en-dash。文中 "4B--8B" 和 "10--58\%" 使用 `--` 是正确的数字范围标记，无需修改。但正文中大量 `---` 作为解释性 dash 应修改。

---

## Questions (需要作者澄清)

**Q1.** Few-NERD 的低 degeneracy (10%) 和高 F1 (75%) 看似矛盾——是否因为 Few-NERD 有 8 个 entity types（vs. CoNLL 的 4 个）导致 output space 更大？如果是，这说明 degeneracy 主要是 output space size 的函数而非 model capability 的函数，这会影响整体叙事。

**Q2.** LoRA rank=8 实验中 degeneracy 降到 7% 但 selection 仍然失败——这是否说明 degeneracy 实际上不是 "gating factor"？论文说 "necessary but not sufficient"，但如果 necessary condition met 后仍然失败，那 degeneracy 的解释力被高估了。

**Q3.** 论文只在 4B-8B 范围测试——70B+ 模型是否会展现不同的 degeneracy 行为？如果更大模型 degeneracy 更高（符合 "better model → more degenerate" 逻辑），那整个 research direction（用 confidence signals 做 selection for structured IE）是否根本无望？

**Q4.** Supervised verifier baseline 只使用了 5 个现有 signal 作为 features——如果加入 token-level features（如 entity-token LP 的分布统计）是否能 close gap？这个 baseline 的 feature space 可能太受限。

---

## Missing References

1. **Byerly & Khashabi (2024)** "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems" (arXiv:2411.01101) — 关于 SC 中 correlated errors 的失败模式分析
2. **Sequence labeling calibration** — 未见 CRF-based calibration 的经典工作如 Lafferty et al. (2001) 或近年 neural CRF calibration 论文
3. **Diversity-promoting decoding** — Vijayakumar et al. (2016) "Diverse Beam Search" 等多样性解码方法作为 degeneracy 的潜在缓解手段应被讨论

---

## Detailed Comments (逐节)

**Abstract**: 信息过密，15+ 个数字在 10 行内。"four instance-level... and one per-sample" 的分类是有效的叙事元素，但后续数字堆砌削弱了可读性。

**Introduction**: 结构完整（背景 → 问题 → 已有不足 → 本文 → 贡献），符合 5 段要求。但 contribution list 中 (2) 和 (3) 有重叠——degeneracy 既是 gap 的原因（contribution 2）又是 regime boundary（contribution 3）。

**Related Work**: 组织良好，四个 paragraph 主题清晰。与 Yao et al. (2026) 的定位合理但可更具体。

**Method**: 公式化清晰，SJ 的定义（Eq. 4）和 instance-level vs. per-sample 的区分是有价值的 methodological contribution。

**Experiments**: 系统性强，Table 1-4 信息密度高。Few-NERD 的 cross-dataset contrast 是最有说服力的部分。

**Discussion**: 内容丰富但过长。"Why the gap exists" paragraph 是核心，后续 ablations 重复论证可压缩。

**Conclusion**: 过于简短（10 行），未讨论 broader implications。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计严谨，统计方法正确，ablations 充分。唯一扣分点：degeneracy 作为 causal mechanism 的论证有循环性（W2）。 |
| Excitement | 2.5/5 | 问题有趣但结论是 negative result + "需要 future work"。缺乏可操作的 positive contribution（W3）。对领域的 guidance 价值有限——告诉人们"别用 unsupervised signals 做 selection"但不提供替代方案。 |
| Reproducibility | 4/5 | 模型、数据集均公开，超参数详细，承诺 code release。Qwen3-8B thinking token confound 有透明披露。 |
| Overall Assessment | 3/5 (Findings) | 分析质量高但 contribution bar 不够 main conference。适合 Findings。 |

---

## Overall Score

**Borderline reject (leaning Findings)**

这是一篇 well-executed 的实证分析论文，统计严谨性和实验覆盖度都很高。但作为 EMNLP 主会议长文，核心贡献（"诊断为什么 SC 在 NER 上不行"）的 novelty 和 actionability 不足：
- "correlation-selection gap" 的两个主要原因分别是 definitional (instance-level signals can't rank by construction) 和 known (fine-tuned models collapse diversity)
- LP compression 是 specific 且 interesting 的发现，但实际意义有限（即使在 non-tied subset 上 LP 也只 +2.9 pp）
- 没有 positive method contribution

如果补充 (1) 一个 lightweight trained verifier 证明诊断的 actionability，或 (2) 更深入分析 degeneracy 的 non-trivial determinants（beyond model capability），可以升至 weak accept。

## Confidence
**4/5** — 我仔细阅读了全文包括 appendix 的关键部分，对 MBR decoding 和 uncertainty estimation 文献有较好了解。对 Few-NERD 数据集的具体 entity type 分布不够熟悉。

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

_source line 1677 · 2026-05-17T07:13:55.323754+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'in_progress', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 1678 · 2026-05-17T07:13:55.324303+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1679 · 2026-05-17T07:14:34.439423+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall Score**: Borderline reject (leaning Findings), 3/5\n**Confidence**: 4/5\n\n**Strengths**:\nS1. 问题 framing 清晰且有价值\nS2. 实验设计全面且系统\nS3. 统计严谨性高\nS4. Negative result 的论证逻辑完整\nS5. Related work 覆盖面广（59 篇引用）\n\n**Weaknesses**:\n\n**W1 [Must-Fix]** 核心概念 \"correlation-selection gap\" 的新颖性有限。本质上是已知 observation 的 repackaging：(1) instance-level signals 不能做 per-sample ranking 是 trivial by definition；(2) fine-tuned models 的 diversity collapse 是已知现象 (Kirk et al., 2024)；(3) LP compression 是 specific but minor。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。\n\n**W2 [Must-Fix]** \"Instance degeneracy\" 作为概念贡献的独立性不足。degeneracy 不是 \"failure mechanism\" 而是 model success 的 natural consequence。CoNLL 58% degeneracy = 91% F1（模型很好当然一致）；Few-NERD 10% = 75% F1（模型 underfit）。\"degeneracy gates LP selection\" 本质等价于 \"LP selection only works when the model is bad enough to produce diverse wrong answers\"。\n\n**W3 [Must-Fix]** 缺乏任何可操作的 positive contribution。全部 takeaway 是 \"需要 trained verifiers\"，但不训练 verifier、不提出新 signal、唯一 remedy (entity-token LP) 失败。纯诊断性论文需要极强 insight novelty 来补偿。\n\n**W4 [Should-Fix]** em-dash 过度使用（约 90 处），AI 写作风格痕迹。\n\n**W5 [Should-Fix]** Abstract 和 Introduction 过度堆砌数字（Abstract 10 行含 15+ 个数字），报告风格重于故事风格。\n\n**W6 [Should-Fix]** 与 Yao et al. (2026) 的增量贡献需更明确差异化。\n\n**W7 [Should-Fix]** Missing reference: Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"。\n\n**W8 [Should-Fix]** Discussion section 过长（2+ 页），部分内容适合移入 Appendix。\n\n**M1-M5**: \"leverage\" 用词、Abstract 缩写未定义 (NER/MBR)、Table 3 EM/VC 无 p 值未解释、Figure 2 \"~15%\" 不精确、em-dash vs en-dash 区分。\n\n**Questions**:\nQ1. Few-NERD 低 degeneracy (10%) 和高 F1 (75%) 是否因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 的函数。\nQ2. LoRA rank=8 degeneracy 7% 但 selection 失败——degeneracy 是否不是 \"gating factor\"？\nQ3. 70B+ 模型是否 degeneracy 更高？如果是，整个 research direction 是否无望？\nQ4. Supervised verifier 只用 5 个 signal 做 features，加入 token-level features 能否 close gap？\n\n**Missing References**: Byerly & Khashabi (2024)、CRF-based calibration (Lafferty et al.)、Diverse Beam Search (Vijayakumar et al., 2016)\n\n**官方维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 4/5\n\n---\n\n请对 W1-W8、M1-M5、Q1-Q4 逐条回应。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 完整审稿意见\n\n**Overall Score**: Borderline reject (leaning Findings), 3/5\n**Confidence**: 4/5\n\n**Strengths**:\nS1. 问题 framing 清晰且有价值\nS2. 实验设计全面且系统\nS3. 统计严谨性高\nS4. Negative result 的论证逻辑完整\nS5. Related work 覆盖面广（59 篇引用）\n\n**Weaknesses**:\n\n**W1 [Must-Fix]** 核心概念 \"correlation-selection gap\" 的新颖性有限。本质上是已知 observation 的 repackaging：(1) instance-level signals 不能做 per-sample ranking 是 trivial by definition；(2) fine-tuned models 的 diversity collapse 是已知现象 (Kirk et al., 2024)；(3) LP compression 是 specific but minor。三者组合的诊断价值有余，但是否构成 EMNLP 主会议长文的贡献量存疑。\n\n**W2 [Must-Fix]** \"Instance degeneracy\" 作为概念贡献的独立性不足。degeneracy 不是 \"failure mechanism\" 而是 model success 的 natural consequence。CoNLL 58% degeneracy = 91% F1（模型很好当然一致）；Few-NERD 10% = 75% F1（模型 underfit）。\"degeneracy gates LP selection\" 本质等价于 \"LP selection only works when the model is bad enough to produce diverse wrong answers\"。\n\n**W3 [Must-Fix]** 缺乏任何可操作的 positive contribution。全部 takeaway 是 \"需要 trained verifiers\"，但不训练 verifier、不提出新 signal、唯一 remedy (entity-token LP) 失败。纯诊断性论文需要极强 insight novelty 来补偿。\n\n**W4 [Should-Fix]** em-dash 过度使用（约 90 处），AI 写作风格痕迹。\n\n**W5 [Should-Fix]** Abstract 和 Introduction 过度堆砌数字（Abstract 10 行含 15+ 个数字），报告风格重于故事风格。\n\n**W6 [Should-Fix]** 与 Yao et al. (2026) 的增量贡献需更明确差异化。\n\n**W7 [Should-Fix]** Missing reference: Byerly & Khashabi (2024) \"Self-Consistency Falls Short\"。\n\n**W8 [Should-Fix]** Discussion section 过长（2+ 页），部分内容适合移入 Appendix。\n\n**M1-M5**: \"leverage\" 用词、Abstract 缩写未定义 (NER/MBR)、Table 3 EM/VC 无 p 值未解释、Figure 2 \"~15%\" 不精确、em-dash vs en-dash 区分。\n\n**Questions**:\nQ1. Few-NERD 低 degeneracy (10%) 和高 F1 (75%) 是否因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 的函数。\nQ2. LoRA rank=8 degeneracy 7% 但 selection 失败——degeneracy 是否不是 \"gating factor\"？\nQ3. 70B+ 模型是否 degeneracy 更高？如果是，整个 research direction 是否无望？\nQ4. Supervised verifier 只用 5 个 signal 做 features，加入 token-level features 能否 close gap？\n\n**Missing References**: Byerly & Khashabi (2024)、CRF-based calibration (Lafferty et al.)、Diverse Beam Search (Vijayakumar et al., 2016)\n\n**官方维度打分**: Soundness 4/5, Excitement 2.5/5, Reproducibility 4/5\n\n---\n\n请对 W1-W8、M1-M5、Q1-Q4 逐条回应。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
```

</details>

---


### Tool result

_source line 1680 · 2026-05-17T07:15:02.957471+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 28518
}
```

</details>

---


### Tool call

_source line 1681 · 2026-05-17T07:15:03.610679+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall Score**: Borderline Accept (3.5/5)\n**Confidence**: 4/5\n\n**Strengths**:\nS1. 问题定义清晰且有贡献——\"correlation-selection gap\" 概念化有价值\nS2. 实验设计的系统性——4 NER benchmarks 构成 difficulty gradient\nS3. 统计方法论上佳——Bootstrap CI、paired sign test、TOST、Bonferroni、Kendall's W\nS4. 三层诊断结构有说服力——construction → degeneracy → compression\nS5. 负面结果的审慎表达——\"inversely associated with\" 而非 \"causes\"\nS6. Appendix 丰富且组织有序\n\n**Weaknesses**:\n\n**W1 [Must-Fix]** 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)。三个数据点单调排列概率 1/6。Entity-type-level analysis (n=8, ρ=-0.881, p=0.004) 存在独立性违反。Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测，统计上有问题。建议增加 2-3 个数据集。\n\n**W2 [Must-Fix]** LoRA rank=8 ablation 的 \"necessary but not sufficient\" claim 存在混淆变量。Rank=8 同时降低了 model capability (greedy F1: 0.645→0.640)、改变了 representation space。LP compression 可能因 model capability 下降而加剧。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% degeneracy → LP fails 的矛盾未充分解释。\n\n**W3 [Should-Fix]** 负面结果缺少 power analysis。n=529、2 seeds 下检测 1pp 效应的 power 未报告。TOST 的 internal anchor δ=2pp 可能过宽。\n\n**W4 [Should-Fix]** \"Compression is model-intrinsic\" 与 RE free-form results 矛盾。RE free-form decoding 恢复了 LP selection (+2.35pp, p=0.025)，但 Abstract/Introduction 中未 qualify。\n\n**W5 [Should-Fix]** Selection 实验 seed coverage 有限（QE 1 seed, selection 2 seeds）。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。\n\n**W6 [Should-Fix]** Few-NERD 训练仅 3 epochs (vs 其他 5 epochs) 可能 confound degeneracy 比较。Under-training → lower degeneracy → 无法区分 dataset effect 和 training effect。\n\n**W7 [Minor]** SJ normalizer claim \"Δρ<0.01\" 措辞精度可改进（实际最大差异 0.009）。\n\n**W8 [Minor]** Table 3 vs Table 4 的 greedy F1 不一致（gold-filtered vs full-set）可能困惑读者。\n\n**Questions**:\nQ1. LoRA rank=8 下 LP 的 median within-instance range 是多少？compression 是否更严重？\nQ2. Few-NERD 训练为何仅 3 epochs？5 epochs 下 degeneracy 是多少？\nQ3. Table 3 sign test 是 instance-level 配对还是 corpus-level？\nQ4. Within-instance SJ-F1 ρ=0.52 的 distribution？多少比例 non-degenerate instances 有 ρ<0？\nQ5. Entity-type-level 分析是否控制了 entity type frequency / average entity count 作为 confound？\n\n**Missing References**: Lightman et al. (2024)、Yoran et al. (2023)、Zhang et al. (2024) DeepMind test-time compute、Eikema et al. (2025) structured MBR\n\n**官方维度打分**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n---\n\n请对 W1-W8、Q1-Q5 逐条回应。",
  "project": "struct_self_consist_ie",
  "chat_id": "oc_3897c2857f11615119e277e820eae311",
  "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
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
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应：对每个 Weakness 和 Question 标注 **[AGREE]**（同意并说明理由）或 **[REBUT]**（反驳并提供具体证据，cite 论文中的 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 完整审稿意见\n\n**Overall Score**: Borderline Accept (3.5/5)\n**Confidence**: 4/5\n\n**Strengths**:\nS1. 问题定义清晰且有贡献——\"correlation-selection gap\" 概念化有价值\nS2. 实验设计的系统性——4 NER benchmarks 构成 difficulty gradient\nS3. 统计方法论上佳——Bootstrap CI、paired sign test、TOST、Bonferroni、Kendall's W\nS4. 三层诊断结构有说服力——construction → degeneracy → compression\nS5. 负面结果的审慎表达——\"inversely associated with\" 而非 \"causes\"\nS6. Appendix 丰富且组织有序\n\n**Weaknesses**:\n\n**W1 [Must-Fix]** 跨数据集 degeneracy 梯度的因果推断基础薄弱 (n=3)。三个数据点单调排列概率 1/6。Entity-type-level analysis (n=8, ρ=-0.881, p=0.004) 存在独立性违反。Figure 3 的 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合了两个粒度的观测，统计上有问题。建议增加 2-3 个数据集。\n\n**W2 [Must-Fix]** LoRA rank=8 ablation 的 \"necessary but not sufficient\" claim 存在混淆变量。Rank=8 同时降低了 model capability (greedy F1: 0.645→0.640)、改变了 representation space。LP compression 可能因 model capability 下降而加剧。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% degeneracy → LP fails 的矛盾未充分解释。\n\n**W3 [Should-Fix]** 负面结果缺少 power analysis。n=529、2 seeds 下检测 1pp 效应的 power 未报告。TOST 的 internal anchor δ=2pp 可能过宽。\n\n**W4 [Should-Fix]** \"Compression is model-intrinsic\" 与 RE free-form results 矛盾。RE free-form decoding 恢复了 LP selection (+2.35pp, p=0.025)，但 Abstract/Introduction 中未 qualify。\n\n**W5 [Should-Fix]** Selection 实验 seed coverage 有限（QE 1 seed, selection 2 seeds）。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。\n\n**W6 [Should-Fix]** Few-NERD 训练仅 3 epochs (vs 其他 5 epochs) 可能 confound degeneracy 比较。Under-training → lower degeneracy → 无法区分 dataset effect 和 training effect。\n\n**W7 [Minor]** SJ normalizer claim \"Δρ<0.01\" 措辞精度可改进（实际最大差异 0.009）。\n\n**W8 [Minor]** Table 3 vs Table 4 的 greedy F1 不一致（gold-filtered vs full-set）可能困惑读者。\n\n**Questions**:\nQ1. LoRA rank=8 下 LP 的 median within-instance range 是多少？compression 是否更严重？\nQ2. Few-NERD 训练为何仅 3 epochs？5 epochs 下 degeneracy 是多少？\nQ3. Table 3 sign test 是 instance-level 配对还是 corpus-level？\nQ4. Within-instance SJ-F1 ρ=0.52 的 distribution？多少比例 non-degenerate instances 有 ρ<0？\nQ5. Entity-type-level 分析是否控制了 entity type frequency / average entity count 作为 confound？\n\n**Missing References**: Lightman et al. (2024)、Yoran et al. (2023)、Zhang et al. (2024) DeepMind test-time compute、Eikema et al. (2025) structured MBR\n\n**官方维度打分**: Soundness 3.5/5, Excitement 3.5/5, Reproducibility 4/5\n\n---\n\n请对 W1-W8、Q1-Q5 逐条回应。",
    "project": "struct_self_consist_ie",
    "chat_id": "oc_3897c2857f11615119e277e820eae311",
    "director_session_key": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
  }
}
```

</details>

---


### Tool result

_source line 1682 · 2026-05-17T07:15:05.017934+00:00_

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

_source line 1683 · 2026-05-17T07:15:22.292669+00:00_

交叉分享已发送给两位 Reviewer。等待他们的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 135

## Round 135

2 recorded events


### User

_source line 1684 · 2026-05-17T07:15:24.997323+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：**Borderline reject，建议 Findings**。

主要问题：
1. "Correlation-selection gap" 概念新颖性有限——两个主因分别是 definitional（instance-level signals 不能 rank）和 known（fine-tuned models collapse diversity）
2. "Instance degeneracy" 本质上是 model capability 的 trivial correlate，Few-NERD 反例的解释力不够充分
3. 全篇无 positive method contribution，纯诊断性论文对 excitement 分数不利

写作质量方面：无 Unicode em/en-dash，但 LaTeX `---` 有 90 处（正文约 35 处），是 AI 写作的典型标志。Abstract 数字堆砌过度。引用 59 篇数量达标且均通过真实性验证，但缺 Byerly & Khashabi (2024) 等相关负面结果文献。

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

_source line 1685 · 2026-05-17T07:15:29.499510+00:00_

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


## Round 136

## Round 136

2 recorded events


### User

_source line 1686 · 2026-05-17T07:16:49.477237+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 — 对 Reviewer 2 审稿意见逐条回应

---

## Weaknesses 回应

**[REBUT] R2-W1: "Correlation-selection gap" 新颖性有限**

R2 称三层诊断是已知 observation 的 repackaging。我部分不同意：

(1) "Instance-level signals 不能做 per-sample ranking 是 trivial by definition" — 表面上 trivial，但 prior work（Yao et al. 2026; Vashurin et al. 2025 CoCoA; Taubenfeld et al. 2025 CISC）直接用 consistency signals 做 selection，说明社区并未普遍认识到这一区分。论文 Section 1 第二段明确指出 "Prior work on confidence estimation for LLM-based IE has conflated quality estimation with sample selection"。如果是 trivial，这些 prior work 不应该存在。

(2) "Diversity collapse 是已知现象" — Kirk et al. (2024) 讨论的是 RLHF 下的 diversity collapse 作为 alignment tax；本文的 instance degeneracy 是 supervised fine-tuning 下的量化现象，且关键贡献不在于发现 degeneracy 存在，而在于量化其与 selection headroom 的具体关系（Table 5: 21% constant F1 + 13% constant utility = 34% instances 完全没有 selection room）。

(3) 但我同意 R2 关于 "是否构成 EMNLP 主会议长文贡献量" 的质疑。纯诊断性 negative result 论文需要很强的 insight density。论文在 diagnostic depth 上做到了，但缺乏 constructive output 确实限制了贡献的完整性。

**结论**: 不同意 "repackaging" 的定性，但同意 contribution 量对 main conference 偏弱，可能更适合 Findings。

---

**[REBUT] R2-W2: Degeneracy = model success 的 natural consequence**

R2 的逻辑是：CoNLL 58% degeneracy ← 91% F1（好模型），Few-NERD 10% ← 75% F1（弱模型），因此 degeneracy 仅反映 model quality。

但论文有两个直接反驳：

(a) **Few-NERD 75% F1 + 10% degeneracy vs. SciERC 66% F1 + 21% degeneracy** (Table 4, Section 5): Few-NERD 性能更高但 degeneracy 更低。如果 degeneracy 纯粹是 model quality 的函数，这一反转不应出现。论文在 Section 5 明确讨论："Few-NERD's low degeneracy despite high performance suggests that dataset-specific factors (number of entity types, semantic overlap) also modulate the rate。"

(b) **4B vs 8B on SciERC** (Table 5): 8B degeneracy 21% vs 4B degeneracy 10.4%，但 within-instance utility correlation 可比 (ρ=0.52 vs 0.55)。这证明 degeneracy 不仅是 accuracy 的 proxy——更高能力的模型在相同任务上产生更多 degeneracy，即使 within-instance 的 quality 分布仍有结构。

R2 的简化 ("LP selection only works when the model is bad enough") 与 Few-NERD 数据矛盾：Few-NERD 是 75% F1（不差），LP 仍然 work (+1.36 pp)。

**但我同意** R2 的 deeper point：论文需要更清楚地 disentangle degeneracy 的多个 driver（model quality, output space size, schema complexity, training epochs），而非将其作为一个 monolithic "mechanism"。这与我在 W1 中提出的 concern 一致。

---

**[AGREE] R2-W3: 缺乏可操作的 positive contribution**

同意。论文唯一的 constructive suggestion 是 "需要 trained verifiers"（Section 5 最后段, Conclusion 最后句），但自己没有实现。Entity-token LP remedy 失败（Section 5 entity-token LP ablation），supervised verifier baseline 也失败 (Section 4.5)。LP + VC 组合全部失败 (Section 5 "Signal combinations")。

对于 EMNLP main conference，我认为至少需要以下之一来补偿：
- 一个 working (哪怕 partial) verifier baseline 展示 oracle gap 可以被 partially closed
- 或者一个 clear actionable framework 告诉 practitioner exactly when to use BoN（例如基于 degeneracy rate 的 decision rule）

论文在 practical considerations 段落有一些 guidance，但不够 concrete to be actionable。

不过我注意到：Few-NERD 的 LP selection 成功 (+1.36 pp, p<0.001) 本身就是 positive result，只是论文将其 framing 为 diagnostic evidence 而非 practical method。如果 reframe 为 "LP selection works in the low-degeneracy regime, and we characterize when that regime occurs"，practical value 会更明显。

---

**[AGREE] R2-W4: em-dash 过度使用**

同意这是一个 presentation quality 问题。我没有专门计数，但通读全文时确实注意到频繁的 em-dash 使用（特别是在 Discussion section）。按照 ACL 写作规范和审稿人期望，减少 em-dash 使用是低成本高收益的修改。

---

**[AGREE] R2-W5: Abstract 和 Introduction 数字堆��**

同意。我重新检查 Abstract：在约 180 words 中有 "ρ up to 0.38", "0.42", "AUROC up to 0.82", "~13 pp", "ρ=0.52", "10-58%", "0.041 nats", "+1.36 pp", "p<0.001", "58%", "+0.42 pp", "$N=8$ to 16", "p=0.003" — 密度过高。这是 experimental report 风格而非 story-driven 叙事。每个数字单独看是 justified，但整体上牺牲了可读性。

---

**[REBUT] R2-W6: 与 Yao et al. (2026) 差异化不足**

论文在 Section 1 第二段（Introduction）和 Section 2 "Consistency for structured IE" 段落中明确列出差异：(1) Yao et al. 使用 hard-prompting，本文使用 fine-tuned models（degeneracy 更严重）；(2) Yao et al. 仅报告 correlation，未区分 QE vs selection；(3) 本文诊断了两个具体 failure mechanisms。

差异化实际上是充分的——Table 4 的 Few-NERD 结果和 Section 4.5 的 LoRA ablation 都是 Yao et al. 不覆盖的实验。但 Introduction 中差异化的叙述方式可以更 upfront（目前在第二段中间，容易被跳过）。

---

**[REBUT] R2-W7: Missing reference Byerly & Khashabi (2024) "Self-Consistency Falls Short"**

我无法确认这篇论文存在。在我的知识范围内，没有 Byerly & Khashabi (2024) 以这个确切标题发表的论文。如果 R2 能提供确切 venue 或 arXiv ID，我可以重新评估。建议作者在 rebuttal 中 verify 这一引用的存在性。

---

**[AGREE] R2-W8: Discussion 过长**

同意。Discussion (Section 5) 承载了：(1) practical implications, (2) why the gap exists (degeneracy + LP compression analysis), (3) non-tied subset analysis, (4) N-scaling effect, (5) temperature effect, (6) verbalized confidence, (7) signal combinations, (8) LP compression hypotheses, (9) free-form ablation, (10) entity-token LP, (11) pilot remedy, (12) practical considerations, (13) regime boundaries, (14) methodological implications. 这是 14 个 distinct sub-topics 在一个 section 中。

建议：将 (3) non-tied subset, (4) N-scaling, (5) temperature, (6) verbalized confidence, (7) signal combinations 移入 Appendix，仅在 Discussion 保留引用。这可释放 ~1 page 空间用于 constructive contribution。

---

## Minor Issues 回应

**[AGREE] R2-M1**: "leverage" 用词问题——Minor，容易修复。

**[REBUT] R2-M2**: Abstract 中 NER 需定义——NER (Named Entity Recognition) 是 NLP 社区的标准缩写，ARR 审稿人不需要定义。MBR 可能确实需要定义或避免在 Abstract 中使��（Abstract 中首次出现 "MBR / consensus-proximity selection" 在 line 6，未展开）。

**[AGREE] R2-M3**: Table 3 EM/VC 无 p 值——同意需要解释。查看 Table 3，EM (0.637) 和 VC (0.623) 明显低于 greedy (0.645)，因此方向为负，paired test 不会给 "improvement" p 值。但论文应标注 "—" 并注释 "below greedy, test not applicable"。

**[AGREE] R2-M4**: Figure 3 "~15%" 的定义——确实不精确。Dashed line 位置应有 explicit justification（如来自 ROC 分析或 breakpoint detection），而非视觉近似。

**[REBUT] R2-M5**: em-dash vs en-dash 区分——这是排版规范问题，不影响科学内容。论文使用 LaTeX `---` (em-dash) 用于解释性插入。按 ACL style guide，em-dash 本身不违规，只是频率过高（同意 W4）。

---

## Questions 回应

**[AGREE] R2-Q1: Output space size 驱动 degeneracy**

这是一个重要的 alternative explanation。Few-NERD 8 types vs CoNLL 4 types 意味着可能的 entity set configurations 指数级更多，自然降低 exact match degeneracy。论文在 Section 5 提到 "number of entity types" 作为 modulating factor，但未做 controlled analysis。

这与我在 W1 中的 concern 一致：degeneracy 可能主要是 output space size 的函数，而非独立的 "mechanism"。如果在 CoNLL 上增加 entity types（如 fine-grained NER），degeneracy 可能也会下降——那么 "degeneracy gates selection" 本质上就是 "output space diversity gates selection"，这个 framing 更准确但也更 trivial。

---

**[AGREE] R2-Q2: LoRA rank=8 证据对 degeneracy-as-gating-factor 的挑战**

完全同意。这与我在 W2 中的分析一致：rank=8 下 degeneracy 7.2% 但 LP selection 仍失败，直接挑战了 "degeneracy is the gating factor" 的 framing。论文的 "necessary but not sufficient" 回应在逻辑上成立，但实验设计上混淆了 degeneracy 下降和模型能力下降这两个变量。

---

**[REBUT] R2-Q3: 70B+ 模型是否使 research direction 无望**

不同意 "无望" 的暗示。两个理由：

(a) 70B+ 模型可能有更强的 LP signal quality（representation space 更丰富），即使 degeneracy 更高。LP compression 可能在 larger models 中有不同 pattern——论文未测试不代表方向无望。

(b) 更重要的是，论文的 QE contribution 不受 degeneracy 影响——即使 70B 模型 degeneracy 更高，QE signals 仍然有用（selective prediction, error flagging）。只是 selection 方向可能确实在 highly capable models 上受限。

论文在 Limitations 中诚实承认这一未知："Whether the gap holds for 70B+ models is untested—larger models may produce more diverse samples." 这是合理的 scope limitation 而非 fatal flaw。

---

**[AGREE] R2-Q4: Supervised verifier 仅用 5 scalar features**

同意这是 verifier experiment 的主要局限。5 个 scalar features（all are instance-level aggregates except LP）本身就 encode 不了 per-sample discriminative information——这几乎是 set up to fail。

如果加入 token-level features（如 per-entity log-prob, attention entropy, hidden state uncertainty），verifier 可能表现完全不同。Section 4.5 的 supervised verifier 结论 ("bottleneck lies in the feature space") 实际上只能说 "bottleneck lies in THESE specific 5 features"，不能泛化为 "no feature combination can close the gap"。

但我也注意到��论文 frame 这个实验的目的是 "test whether the information bottleneck lies in the aggregation method or the features themselves"——在这个 narrow claim 下，实验设计是合理的（固定 features，变 aggregation method）。只是 broader conclusion 需要 qualify。

---

## 总结性评价

R2 的核心 concern（novelty/contribution 量不足 for main conference）是合理的，但部分 technical criticisms（W2 的 degeneracy = model success 简化）在论文数据面前不完全成立。我认为论文的贡献介于 Main Conference 和 Findings 之间：

- **支撑 Main Conference 的因素**: 实验系统性、统计严谨性、三层诊断的清晰度、Few-NERD positive result
- **支撑 Findings 的因素**: 缺乏 constructive contribution (W3)、核心因果 claim 证据偏薄 (与我的 W1-W2 一致)、novelty 主要在 framing 而非 new method

我维持 **Borderline Accept (3.5/5)** 的评分，但认为 R2 的 **Borderline Reject (3/5)** 也在合���范围内。关键分歧在于 "purely diagnostic paper with strong execution" 是否 sufficient for main conference。


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

_source line 1687 · 2026-05-17T07:16:54.581478+00:00_

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


## Round 137

## Round 137

2 recorded events


### User

_source line 1688 · 2026-05-17T07:16:57.171236+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。核心判断：R2 的 novelty/contribution 量质疑合理（特别是 W3 缺乏 constructive output），但部分 technical criticisms（W2 将 degeneracy 简化为 model success proxy）与论文中 Few-NERD 和 4B/8B 对比的数据矛盾。我维持 Borderline Accept (3.5/5)，认为两位 reviewer 的主要分歧在于 "purely diagnostic paper with strong execution" 是否满足 main conference 门槛。

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

_source line 1689 · 2026-05-17T07:17:04.694499+00:00_

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


## Round 138

## Round 138

30 recorded events


### User

_source line 1690 · 2026-05-17T07:18:18.763301+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: 跨数据集 degeneracy 梯度因果推断基础薄弱 (n=3)**

同意。三个数据集的单调排列概率确实是 1/6（单方向 1/3），统计上不具说服力。Entity-type-level analysis (n=8, ρ=-0.881, p=0.004) 虽更有力，但论文自己在 Section 4.3 (line 166) 也承认 "the pooled Spearman correlation (ρ=−0.57, p=0.066, n=11) treats dataset-level and entity-type-level points as independent"。混合两个粒度的观测确实有统计问题——entity types within Few-NERD 共享训练pipeline、模型权重、和 constrained decoding schema，不满足独立性假设。

补充发现：LoRA rank ablation 提供了部分 converging evidence（rank=32 → 21% degen, rank=8 → 7.2%），但方向一致≠因果确认。建议至少增加 1-2 个 dataset（如 OntoNotes、ACE05）来加强跨数据集证据。

**[AGREE] R1-W2: LoRA rank=8 ablation 混淆变量**

同意且认为这是论文的关键逻辑缺陷之一。核心矛盾：
- Few-NERD: 10% degeneracy, F1≈75%, LP ρ=0.421 → LP selection works (+1.36pp)
- SciERC rank=8: 7.2% degeneracy, F1≈64%, LP ρ 未报告 → LP selection fails

论文的 "necessary but not sufficient" claim 试图化解这个矛盾，但未提供关键数据：rank=8 下 LP 的 within-instance range 和 LP-F1 correlation。如果 rank=8 同时劣化了 LP 信号质量（因为 lower-rank 模型的 representation 更粗糙），则无法分离 degeneracy effect 和 capability effect。R1 的 Q1 直击要害——如果 rank=8 的 LP compression 更严重，那 "degeneracy is necessary" 的 claim 就缺少 crucial evidence。

**[AGREE] R1-W3: 负面结果缺少 power analysis**

部分同意。对 SciERC 主要结果 (n=529, 2 seeds)，检测 1pp 效应的 statistical power 确实未报告。论文提到 "absence of evidence should not be equated with evidence of absence"（Section 4.2, line 115）——这句话本身就暗示 power 可能不足。

不过，论文用 TOST equivalence testing (Appendix Table 8) 部分缓解了这个问题：在 external anchor δ=1.0pp 下部分配置 pass equivalence。Few-NERD (n=32,565) 的高 power 正面结果也从另一端提供了边界条件。

建议：补充一个简单的 power calculation（假设 σ≈0.15, paired test, n=529, 2 seeds 对 1pp effect 的 power 大约是 50-60%），让读者理解 SciERC 负面结果的可信度。

**[AGREE] R1-W4: "Compression is model-intrinsic" 与 RE free-form 结果矛盾**

同意这是一个 presentation 问题。证据：
- Section 5, line 92-93: NER free-form decoding "yields nearly identical LP distributions (std ratio 0.97)"
- Section 5, line 93-94: RE free-form "+2.35pp (95% CI [+0.24, +4.50], p=0.025)"

论文确实在 Discussion 中做了 NER vs RE 的区分，但 Abstract (line 6) 说 "LP carries genuine per-sample information but is compressed to near-ineffectiveness (median range 0.041 nats)" 未加 "for NER" 限定。Introduction 的 contribution 2(c) 同样未 qualify。这使得 paper-level claim 过强。

**[REBUT] R1-W5: Few-NERD 核心结果 seed coverage 有限**

部分反驳。R1 担心 "Few-NERD LP +1.36pp 是 1-seed result" 意味着可靠性不足，但这里需区分两种统计推断：
1. **Seed replication**（across seeds）：确实只有 1 seed
2. **Instance-level inference**（within seed）：n=32,565 instances, paired bootstrap, p<0.001, 95% CI [+1.18, +1.53]

With n=32,565 paired observations, the within-seed statistical test has极高的 power。Bootstrap CI 排除零且较窄 (0.35pp wide)。Seed replication 测试的是 training run stochasticity，而非 selection signal 的 statistical reliability。

然而，我承认如果 training seed 偶然产生了低 degeneracy 的 checkpoint，结论的可泛化性确实受影响。鉴于主实验 multi-seed stability (σ≤0.026, Table 7)，合理推断 Few-NERD 结果也是 seed-robust 的，但严格来说这是假设而非验证��

**[AGREE] R1-W6: Few-NERD 3 epochs vs 其他 5 epochs 的 confound**

强烈同意，且我认为这是此前我和 R1 都未充分强调的重要问题。

关键证据：
- 主文 Section 4.1, line 15: "fine-tuned with LoRA (rank=32, α=64) for **5 epochs**" —— 暗示所有数据集统一设置
- Appendix Section Few-NERD Full Results (line 1087): "Qwen3-8B, LoRA rank=32, **3 epochs**, N=8, T=1.0"

这存在两个问题：
1. **主文 disclosure 不充分**：正文说 5 epochs 但 Few-NERD 实际用了 3 epochs，读者必须读到 Appendix 才能发现差异。
2. **Confound 严重**：Under-training (3 vs 5 epochs) 直接降低模型 convergence → 降低 output consistency → 降低 degeneracy。因此 Few-NERD 的低 degeneracy (10%) 可能部分源于训练不足而非 dataset intrinsic property。这严重削弱了 "degeneracy is dataset-specific" 和 "degeneracy gates LP selection" 的 cross-dataset comparison。

如果 5-epoch Few-NERD degeneracy 显著高于 10%，论文的整个 degeneracy-gating narrative 需要重新评估。

**[AGREE] R1-W7: SJ normalizer "Δρ<0.01" 措辞**

同意。Appendix Table 6 显示最大 Δρ=0.009，说 "<0.01" 技术上正确但应更精确写为 "≤0.009" 或 "max |Δρ|=0.009"。Minor。

**[REBUT] R1-W8: Table 3 vs Table 4 greedy F1 不一致**

部分反驳。论文在 Table 4 的 footnote（Section 4.3, line 143）明确解释："SciERC greedy (0.614) and headroom (13.8pp) differ from Table 3 (gold-filtered n=529, greedy=0.645) due to full-set evaluation; the ranking and significance are unchanged."

Footnote 存在且解释清楚，但同意它容易被忽略。建议在 Table 4 caption 中直接注明 "full-set evaluation (cf. gold-filtered in Table 3)" 而非仅在 footnote 说明。

---

### Questions 回应

**Q1. LoRA rank=8 LP median within-instance range?**

[AGREE 这是关键缺失数据] 论文未报告。Section 4.5 (line 203-208) 报告了 rank=8 的 degeneracy (7.2%) 和 selection F1，但完全没有 LP distribution 的数据。这使得 "LP compression persists regardless of LoRA rank" 的 claim 是 unsupported assertion。

**Q2. Few-NERD 3 epochs 原因？5 epochs degeneracy？**

[AGREE 这是关键 confound] 3 epochs 在 Appendix line 1087 确认。原因未说明（可能是 dataset 规模大导致 5 epochs 过于 costly？Few-NERD 有 37,648 instances vs SciERC 551）。5-epoch degeneracy 未报告，但这是验证 degeneracy-gating claim 的 crucial control。

**Q3. Table 3 sign test 是 instance-level 配对还是 corpus-level？**

[可回答] Section 4.2, line 114 说 "2-seed sign tests"，结合 footnote "Multi-seed NER experiments confirm seed variation is small"。据此推断是 instance-level paired sign test：对每个 instance 比较 LP-selected sample 的 F1 vs greedy F1，统计 win/loss/tie counts。n=529 是 instance 数而非 corpus count。

**Q4. Within-instance SJ-F1 ρ=0.52 的分布？**

[AGREE 未报告] Section 5 只给了 median (0.524 SciERC, 0.994 CoNLL)。分布形状、负 ρ 的比例、以及 non-degenerate subset 的 size 均未 characterize。考虑到 median 0.524 暗示至少一半 instances 的 ρ≤0.524，且可能有相当比例 ρ<0 的 instances，这些信息对理解 MBR 的 failure mode 很重要。

**Q5. Entity-type-level analysis 是否控制了 frequency/average entity count？**

[AGREE 未控制] Appendix Table (per-type analysis) 只按 degeneracy sort。Entity type frequency（多少 instances 包含该 type）和 average entity count per instance 都可能 confound：high-frequency types 有更多 training data → lower degeneracy，而非 type semantics 本身的 effect。Partial correlation 控制 frequency 后 ρ 可能衰减。

---

### Missing References 回应

**Lightman et al. (2024) "Let's Verify Step by Step"**: 已在 Related Work (Section 2, line 35) 被引用 `\cite{lightman2024verify}`。R1 可能遗漏。

**Yoran et al. (2023)**: 如果指的是 self-consistency 相关工作，未被引用。应核实具体论文。

**Zhang et al. (2024) DeepMind test-time compute**: 未被引用。如果指 "Scaling LLM Test-Time Compute" 系列，Snell et al. (2025) 已覆盖 ICLR 版本。DeepMind 的具体论文需核实。

**Eikema et al. (2025) structured MBR**: 已在 Section 2 (line 25) 被引用 `\citet{eikema2025structured}`。R1 可能遗漏。

---

### 综合评价

R1 的审稿质量很高，特别是 W1、W2、W6 三个 weakness 直击方法论薄弱环节。我与 R1 的主要共识：
1. Degeneracy-gating narrative 的统计基础不够坚实（n=3 + confounded Few-NERD training）
2. LoRA ablation 的 causal claim 有混淆变量
3. 论文是高质量的 negative result 但 contribution bar 对 main conference 可能不够

我与 R1 的主要分歧：
- R1 给 Excitement 3.5/5，我给 2.5/5。我认为纯诊断 + 无 actionable method 使得论文更适合 Findings。
- R1 对 seed coverage 的担忧（W5）我认为对 Few-NERD 不太成立（n=32,565 的 within-seed power 极高）。

**建议 Final Score**: Borderline (3/5, leaning Findings)。若能修复 W6 (Few-NERD epoch confound) 并补充 W2 (rank=8 LP compression data)，可升至 3.5。

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

_source line 1691 · 2026-05-17T07:18:44.319219+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'in_progress', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'pending', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 1692 · 2026-05-17T07:18:44.369851+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1693 · 2026-05-17T07:19:00.831303+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "review_issues.yaml",
  "max_chars": "12000"
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
    "file": "review_issues.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---


### Tool result

_source line 1694 · 2026-05-17T07:19:00.882019+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'review_issues.yaml'\", \"metadata\": {}}"}

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

_source line 1695 · 2026-05-17T07:19:05.158464+00:00_

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

_source line 1696 · 2026-05-17T07:19:05.259205+00:00_

No matching deferred tools found

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

_source line 1697 · 2026-05-17T07:19:08.723835+00:00_

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

_source line 1698 · 2026-05-17T07:19:08.975237+00:00_

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
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1699 · 2026-05-17T07:19:14.544322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1700 · 2026-05-17T07:19:14.695786+00:00_

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
…[truncated 4010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1701 · 2026-05-17T07:19:19.034402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "299",
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
    "offset": "299",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1702 · 2026-05-17T07:19:19.085320+00:00_

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
319	# ===== RECURRING ISSUES (updated Round 16) =====
320	- id: R0-C3
321	  summary: "Selection gap effective test bed 仅 SciERC 单数据集"
322	  category: experiment
323	  severity: critical
324	  status: in_progress
325	  first_raised_round: 0
326	  last_seen_round: 16
327	  mentions:
328	  - round: 0
329	    reviewers: [1, 2]
330	    note: "需跨数据集验证或降级措辞"
331	  - round: 4
332	    reviewers: [1, 2]
333	    note: "claim 降级到位"
334	  - round: 9
335	    reviewers: [1, 2]
336	    note: "Conclusion hedge 到位"
337	  - round: 11
338	    reviewers: [1, 2]
339	    note: "R11 fresh review 再次提出"
340	  - round: 12
341	    reviewers: [1, 2]
342	    note: "R12 强共识: 标题限定 NER 或增 RE dataset"
343	  - round: 13
344	    reviewers: [1, 2]
345	    note: "R13 强共识: Selection gap effective test bed 仅 SciERC (n=529)."
346	  - round: 14
347	    reviewers: [1, 2]
348	    note: "R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse."
349	  - round: 15
350	    reviewers: [1, 2]
351	    note: "R15 强共识: 核心 finding 实质仅 SciERC 验证."
352	  - round: 16
353	    reviewers: [1, 2]
354	    note: "R16: 论文已加入 Few-NERD (10% degen, LP +1.36pp). 但 R2-W1 指出 Few-NERD positive finding 仅 1 model x 1 N x 1 dataset. 数据集覆盖有改善但仍不充分. R1 的 monotonic claim 问题 (3 dataset-level points) 本质上是同一问题的统计表达."
355	  action_items:
356	  - round: 11
357	    action: "标题或 abstract 首句显式限定 RE scope"
358	    assigned_to: Pap
…[truncated 5587 chars]

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

_source line 1703 · 2026-05-17T07:19:25.057992+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "498",
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
    "offset": "498",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1704 · 2026-05-17T07:19:25.058459+00:00_

498	    assigned_to: Paper Agent
499	    status: in_progress
500	  - round: 16
501	    action: "Related Work 加入直接对比: 'Yao et al. demonstrate consistency correlates with accuracy; we show this correlation is necessary but not sufficient for sample selection, and diagnose two specific failure mechanisms (degeneracy, compression).'"
502	    assigned_to: Paper Agent
503	    status: in_progress
504	  resolution: ""
505	  resolution_round: null
506	
507	- id: R11-W2
508	  summary: "Scale range (3B-8B) 不足以支撑普适性结论"
509	  category: framing
510	  severity: warning
511	  status: in_progress
512	  first_raised_round: 11
513	  last_seen_round: 16
514	  mentions:
515	  - round: 11
516	    reviewers: [1, 2]
517	    note: "需确认所有 scale claims 限定范围"
518	  - round: 12
519	    reviewers: [1, 2]
520	    note: "R12 两位再次强共识."
521	  - round: 14
522	    reviewers: [1, 2]
523	    note: "Abstract 'at two model scales' 未说明 narrow range."
524	  - round: 15
525	    reviewers: [1, 2]
526	    note: "R15: Discussion 'intrinsic' 用语仍暗示更强普遍性."
527	  - round: 16
528	    reviewers: [1, 2]
529	    note: "R16 (R2-W6 + R1 PARTIAL REBUT): R2 认为标题 'Fail to Scale' 暗示 model scale; R1 反驳 'scale' 在论文中指 N/信号复杂度. 共识: 'scale' 含义需在 Abstract 中澄清."
530	  action_items:
531	  - round: 12
532	    action: "在 Conclusion/Discussion 明确限定为 small-model regime"
533	    assigned_to: Paper Agent
534	    status: done
535	  - round: 15
536	    action: "Discussion 'intrinsic to capable fine-tuned models' 改为 'within the 3B-8B fine-tuned regime we tested'."
537	    assigned_to: Paper Agent
538	    status: in_progress
539	  - round: 16
540	    action: "Abstract 或 Introduction 中澄清 'scale' 的含义 (指 scaling up N, signal sophistication, and model size within 4B-8B), 避免被误读为跨 model scale 的 general claim."
541	    assigned_to: Paper Agent
542	    status: in_progress
543	  resolution: ""
544	  resolution_round: null
545	
546	- id: R11-W3
547	  summary: "3 seeds 统计效力不足 (Kendall W)"
548	  category: experiment
549	  severity: warning
550	  status: 
…[truncated 4456 chars]

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

_source line 1705 · 2026-05-17T07:19:29.825321+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "697",
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
    "offset": "697",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1706 · 2026-05-17T07:19:29.876074+00:00_

697	  severity: critical
698	  status: in_progress
699	  first_raised_round: 12
700	  last_seen_round: 16
701	  mentions:
702	  - round: 12
703	    reviewers: [1, 2]
704	    note: "改措辞为 moderate-to-strong 或加限定语"
705	  - round: 14
706	    reviewers: [1, 2]
707	    note: "rho=0.38 按 Cohen (1988) 属 medium effect."
708	  - round: 15
709	    reviewers: [1, 2]
710	    note: "R15: Abstract 仅报告 primary rho=0.38."
711	  - round: 16
712	    reviewers: [1, 2]
713	    note: "R16 强共识 (R2-N2 + R1 AGREE, 独立验证): 论文内部数值矛盾严重. Abstract/Figure 1 caption 声称 'rho up to 0.42 on primary test bed', 但 Table 1 SciERC 最高 rho = VC 0.379. rho=0.42 实际来自 Few-NERD LP (0.421). Contribution 1 正确写 0.38. 这不是四舍五入误差 (差 0.04), 是不同位置引用了不同数据源. 从 R15 的 warning 升级为 critical (影响可信度)."
714	  action_items:
715	  - round: 14
716	    action: "'moderate-to-strong' 中 'strong' 部分仅基于 ceiling-effect dataset."
717	    assigned_to: Paper Agent
718	    status: in_progress
719	  - round: 15
720	    action: "Abstract 改为仅报告 primary rho=0.38."
721	    assigned_to: Paper Agent
722	    status: in_progress
723	  - round: 16
724	    action: "全文统一 headline rho: SciERC (primary) max = 0.38 (VC, N=8); Few-NERD LP = 0.42. Figure 1 caption 修正 (当前错误地将 0.42 归因于 primary test bed). Abstract 改为 'rho up to 0.38 on the primary test bed (0.42 on Few-NERD)'. 禁止混淆归属."
725	    assigned_to: Paper Agent
726	    status: in_progress
727	  resolution: ""
728	  resolution_round: null
729	
730	- id: R12-W1
731	  summary: "纯诊断无 remedy 尝试, 限制论文 impact"
732	  category: experiment
733	  severity: warning
734	  status: in_progress
735	  first_raised_round: 12
736	  last_seen_round: 16
737	  mentions:
738	  - round: 12
739	    reviewers: [1, 2]
740	    note: "至少一个 pilot remedy 会显著增强"
741	  - round: 14
742	    reviewers: []
743	    note: "Entity-token LP + LP x VC 已测试, 全部 negative."
744	  - round: 15
745	    reviewers: []
746	    note: "R15 未被独立提及."
747	  - round: 16
748	    reviewers: []
749	    note: "R16 未被独立提及. 多种 remedy 已测试并全部 negative (entity-token LP, 
…[truncated 5222 chars]

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

_source line 1707 · 2026-05-17T07:19:35.348986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "895",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
    "offset": "895",
    "limit": "300"
  }
}
```

</details>

---


### Tool result

_source line 1708 · 2026-05-17T07:19:35.349590+00:00_

895	
896	- id: R14-W1
897	  summary: "Fisher combined p (2-seed) / sign test 统计效力极低"
898	  category: experiment
899	  severity: critical
900	  status: in_progress
901	  first_raised_round: 14
902	  last_seen_round: 16
903	  mentions:
904	  - round: 14
905	    reviewers: [1, 2]
906	    note: "Fisher p 呈现权重应降低."
907	  - round: 15
908	    reviewers: [1, 2]
909	    note: "R15: 方向共识, severity 分歧."
910	  - round: 16
911	    reviewers: [1, 2]
912	    note: "R16 强共识 (R1-N1 + R2 AGREE): Sign test 仅用方向信息, effect size +0.2pp 下 power 极低. R2 补充: (1) N=32 bootstrap (p=0.031) 反驳了论文自身的 'selection fails' 叙事; (2) Few-NERD 用了 paired bootstrap 而 SciERC 用 sign test, 方法不统一. 共识: SciERC null result 不应表述为 'no signal significantly outperforms greedy', 应改为 'effect is small and not reliably detected'. 升级为 critical (核心否定结论的统计基础)."
913	  action_items:
914	  - round: 14
915	    action: "Table 2 将 Fisher combined p 降级为辅助."
916	    assigned_to: Paper Agent
917	    status: in_progress
918	  - round: 15
919	    action: "主文从 'all p>0.05' 叙事转向 effect size + convergent evidence lines."
920	    assigned_to: Paper Agent
921	    status: in_progress
922	  - round: 16
923	    action: "(1) 统一统计方法: SciERC 也用 paired bootstrap (B=10000) 替代 sign test; (2) 主文改为 'the observed LP advantage (+0.2pp) is small (d=0.038) and not reliably detected'; (3) 与 N=32 bootstrap p=0.031 整合叙事 (LP 在更大 N 下可能 work); (4) 报告 power analysis 或明确声明 'absence of evidence is not evidence of absence'."
924	    assigned_to: Paper Agent
925	    status: in_progress
926	  resolution: ""
927	  resolution_round: null
928	
929	- id: R14-W2
930	  summary: "Greedy (T=0) vs sampling+selection 比较修辞过强"
931	  category: writing
932	  severity: warning
933	  status: in_progress
934	  first_raised_round: 14
935	  last_seen_round: 16
936	  mentions:
937	  - round: 14
938	    reviewers: [1, 2]
939	    note: "greedy 应定位为 practical cost-free alternative."
940	  - round: 15
941	    reviewers: [1, 2]
942	    note: "R15: 'surpassing all N=8 selection strategies' 仍过
…[truncated 9880 chars]

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

_source line 1709 · 2026-05-17T07:19:40.367874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml",
  "offset": "1194",
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
    "offset": "1194",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1710 · 2026-05-17T07:19:40.368363+00:00_

1194	
1195	- id: R16-N2
1196	  summary: "rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾 (已并入 R12-N1 升级)"
1197	  category: writing
1198	  severity: critical
1199	  status: open
1200	  first_raised_round: 16
1201	  last_seen_round: 16
1202	  mentions:
1203	  - round: 16
1204	    reviewers: [1, 2]
1205	    note: "R16 (R2-N2 + R1 独立验证 AGREE): Figure 1 caption 'rho up to 0.42 on primary test bed' 与 Table 1 SciERC max=0.379 直接矛盾. 0.42 来自 Few-NERD LP. 这是数值归属错误, 非四舍五入."
1206	  action_items:
1207	  - round: 16
1208	    action: "见 R12-N1 的 Round 16 action item (全文统一 headline rho 归属)."
1209	    assigned_to: Paper Agent
1210	    status: open
1211	  resolution: ""
1212	  resolution_round: null

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

_source line 1711 · 2026-05-17T07:20:17.775630+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'in_progress', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 1712 · 2026-05-17T07:20:17.826432+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1713 · 2026-05-17T07:24:41.609978+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4x variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 dagger-RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n\n# ===== RECURRING ISSUES (updated Round 17) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 17\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 核心 finding 实质仅 SciERC 验证.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已加入 Few-NERD. 但 positive finding 仅 1 model x 1 N x 1 dataset.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: Few-NERD 加入后 dataset 覆盖改善, 但 cross-dataset degeneracy gradient 仍仅 n=3. R1 建议增加 OntoNotes/ACE05. R2 建议 Few-NERD cross-model 验证. 核心问题: degeneracy-gating pattern 的统计基础薄弱.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 17\n    action: \"增加 1-2 个 NER 数据集 (OntoNotes, ACE05) 扩大 degeneracy gradient 的 n; 或将 cross-dataset gradient 明确标注为 exploratory observation (n=3 不足以做因果推断).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 17\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识: 标题暗示意外发现但 4/5 signals weakness 部分 by construction.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2 重申 novelty 有限 (W1). R1 部分反驳: prior work 确实 conflated QE/selection, 概念分离有价值. 但两位都同意纯诊断性贡献对 main conference 门槛偏弱. R1 建议 reframe LP positive result (Few-NERD) 为 actionable finding.\"\n  action_items:\n  - round: 17\n    action: \"三层叙事明确分离: (1) definitional limitation (noted, not discovered); (2) MBR empirical failure despite aligned utility (novel diagnosis); (3) LP compression (novel finding). 标题 'Weak Selectors' 加 nuance.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + Bonferroni scope 争议\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 17\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Footnote 4 措辞需修正.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"Footnote 4 改为 'survives Bonferroni over 5 signal comparisons, conditional on pre-selected epsilon=0.05'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"核心增量是 'why QE != selection' 的诊断.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W6 再次提出差异化不足. R1 反驳: 差异化充分但叙述位置不够 upfront. 共识: Introduction 中应更显著地定位差异.\"\n  action_items:\n  - round: 17\n    action: \"Introduction 第二段将 Yao et al. 差异化提前并加粗关键区分点: (1) fine-tuned models (degeneracy 更严重), (2) QE/selection 分离, (3) failure mechanism diagnosis.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"'scale' 含义需澄清.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-Q3 提出 70B+ 模型可能 degeneracy 更高, 整个方向可能无望. R1 反驳: 70B LP quality 可能不同, QE 不受影响. 共识: Limitations 需更明确讨论 scale 外推的不确定性.\"\n  action_items:\n  - round: 16\n    action: \"Abstract/Introduction 澄清 'scale' 含义.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"m=3, exact p~0.028.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"主文加 caveat: 'though statistical precision is limited with m=3 raters'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"论文已有 (a)-(d) 四个 hypotheses.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W4 + R2 AGREE): RE free-form +2.35pp (p=0.025) 直接证明 constraints DO compress LP for RE. Abstract/Introduction 中 'compressed to near-ineffectiveness' 未限定为 NER-specific. 需加 task qualifier.\"\n  action_items:\n  - round: 17\n    action: \"Abstract line 6 和 Introduction contribution 2(c) 中 'compressed to near-ineffectiveness' 加 'for NER' 限定. Discussion 已有 NER/RE 区分但需更显著.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"rho headline 来自 ceiling-effect dataset / 数值不一致\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Abstract/Figure 1 caption rho=0.42 归因错误.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. R16 action 仍 open.\"\n  action_items:\n  - round: 16\n    action: \"全文统一 headline rho 归属. Figure 1 caption 修正.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"多种 remedy 已测试并全部 negative.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W3 + R1 AGREE): 纯诊断性论文缺乏 positive contribution 是核心 excitement 问题. 已测试 entity-token LP, LP x VC, supervised combination, verbalized confidence, 全部 negative. R1 建议 reframe Few-NERD LP positive result 为 actionable finding (LP works when degeneracy <15%). R2 建议增加 lightweight trained verifier.\"\n  action_items:\n  - round: 17\n    action: \"(1) Reframe Few-NERD LP +1.36pp 为 practical positive finding, 不仅是诊断证据; (2) 提供 degeneracy-based decision rule (practitioners should check degeneracy rate before investing in BoN); (3) 如果时间允许, train lightweight verifier 在 SciERC 上验证 oracle gap 可否被 partially closed.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Table 4 SciERC full set vs Table 2 gold-filtered.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W8 + R2 partial rebut): Footnote 解释存在但容易被忽略. 建议 Table 4 同时报告 gold-filtered 数字或在 caption 中更显著标注.\"\n  action_items:\n  - round: 17\n    action: \"Table 4 caption 中显式标注 'full-set evaluation (cf. gold-filtered in Table 3)' 而非仅在 footnote.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"建议改名为 'Soft Overlap' 或加注释.\"\n  - round: 17\n    reviewers: [1]\n    note: \"R17 (R1-W7): footnote 表述 'Δρ<0.01' 应改为 '|Δρ|≤0.009'. Minor.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 / 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"9 句话含过多技术细节.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W5 + R1 AGREE): Abstract 约 180 words 含 15+ 数字 (ρ, AUROC, pp, nats, p, N, degeneracy%). 远超审稿人 30 秒吸收能力. 实验报告风格而非 story-driven.\"\n  action_items:\n  - round: 17\n    action: \"Abstract 数字压缩到 4-5 个最关键的. 移除 specific ρ/AUROC 数字, 用 'moderate-to-strong correlations' 替代. 保留 key claims: 13pp oracle headroom, 0 net selection gain, degeneracy pattern.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Eikema argues utility design; 本文证明 utility IS aligned but degeneracy eliminates headroom.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. R16 action 仍 open.\"\n  action_items:\n  - round: 16\n    action: \"Related Work 增加 differentiation paragraph vs Eikema.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) / sign test 统计效力极低\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"SciERC null result 应改为 'effect small and not reliably detected'.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W3 + R2 AGREE): 负面结果缺少 power analysis. n=529, 2 seeds 检测 1pp 效应的 power 约 50-60%. p=0.29 无法区分 '真无效果' 和 '检测不到'. 建议加 post-hoc power analysis 或更明确指出 Few-NERD (n=32,565) 才是 definitive evidence.\"\n  action_items:\n  - round: 17\n    action: \"(1) 加 post-hoc power analysis: 在 n=529, σ~0.15 下检测 1pp 效应的 power; (2) 主文改为 'the observed LP advantage is small and not reliably detected at N=8'; (3) 明确指出 Few-NERD 是 definitive evidence, SciERC 受限于 power.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"greedy 'surpassing' 只反映 T=0 vs T=1 差异.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 15\n    action: \"修辞改为 'selection adds no benefit over greedy'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation: 8B vs 4B degeneracy 差异的解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"LoRA-rank ablation 是 interventional evidence.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 16\n    action: \"LoRA-rank as primary (interventional), 8B vs 4B as supporting (observational).\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"3.5pp 差距是系统性的. 定义差异需说明.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. 论文 Section 4.3 line 110 已有解释: 'the difference between deterministic decoding (T=0) and uniformly sampling one of N stochastic candidates (T=1.0); greedy is not drawn from the candidate pool.' 此解释清楚了 Random 是从 N 个 T=1 sample 中随机选, Greedy 是 T=0.\"\n  action_items:\n  - round: 16\n    action: \"明确 Random 和 Greedy 的精确定义差异.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Introduction 首次使用时需给出 one-sentence 定义.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-M4 → R1 comment on Abstract): 'correlation-selection gap' 在 Abstract 引入但未定义. 建议 Abstract 或 Introduction 首次使用时加一句简短释义.\"\n  action_items:\n  - round: 17\n    action: \"Introduction 首次使用 'correlation-selection gap' 时加 '(the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance)' 或类似释义.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 维持; R2 REBUT (LoRA-rank 已做 interventional control).\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W6 + R2 strongly AGREE): Few-NERD 训练 3 epochs vs 其他 5 epochs 是关键 confound. 主文说 '5 epochs' 暗示统一, Appendix 才披露 3 epochs. Under-training 直接降低 degeneracy. 如果 5-epoch Few-NERD degeneracy 显著高于 10%, 整个 degeneracy-gating narrative 需重新评估.\"\n  action_items:\n  - round: 17\n    action: \"(1) 主文 Section 4.1 明确披露 Few-NERD 为 3 epochs (非仅 Appendix); (2) 解释为何使用 3 epochs (dataset 规模/early stopping?); (3) 如可能, 补充 5-epoch Few-NERD degeneracy 数据; (4) 承认 epoch difference 作为 confound 并讨论其对 cross-dataset comparison 的影响.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"呈现应更平衡.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 16\n    action: \"Section 4.3 增加 harmful selection 讨论.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N1\n  summary: \"Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点, 统计不显著 (p=0.066)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"3 个 dataset-level 数据点无统计意义.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识 (R1-W1 + R2 AGREE): 核心问题不变. Figure 3 pooled correlation 混合两个粒度的观测, 统计上有问题. Entity-type-level (n=8, ρ=-0.881, p=0.004) 更有力但存在 independence 问题 (共享 model/pipeline). 建议: (1) 不 pool 不同粒度; (2) 控制 entity type frequency; (3) cross-dataset claim 降级为 exploratory.\"\n  action_items:\n  - round: 17\n    action: \"(1) Figure 3 不 pool 两个粒度, 分别报告 dataset-level (n=3, exploratory) 和 entity-type-level (n=8, p=0.004); (2) 控制 entity type frequency/entity count 作为 confound; (3) 主文 'monotonically predicts' 改为 'inversely associated with' (已部分完成但需全文统一).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N2\n  summary: \"rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Figure 1 caption 'rho up to 0.42 on primary test bed' 与 Table 1 SciERC max=0.379 矛盾.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. R16 action 仍 open.\"\n  action_items:\n  - round: 16\n    action: \"全文统一 headline rho 归属.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 17) =====\n- id: R17-W1\n  summary: \"LoRA rank=8 下 LP compression 统计数据缺失, 无法支撑 'necessary but not sufficient' claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识 (R1-W2/Q1 + R2 AGREE): LoRA rank=8 ablation 降低 degeneracy (21%→7.2%) 且增加 headroom (13.3→16.0pp), 但 LP selection 仍失败. 论文据此声称 'necessary but not sufficient'. 但未报告 rank=8 下 LP 的 median within-instance range 和 tied fraction. 如果 rank=8 下 LP compression 更严重 (因模型能力下降), 则 selection failure 可归因于 compression 加剧而非 degeneracy 本身不充分. 此外, rank=8 同时改变了 model capability (greedy F1: 0.645→0.640), 无法做 clean causal attribution.\"\n  action_items:\n  - round: 17\n    action: \"(1) 报告 LoRA rank=8 下 LP 的 median within-instance range, tied fraction, 和 pooled within-instance ρ(LP,F1); (2) 将 claim 弱化为 'low degeneracy co-occurs with LP selection success, but rank-8 ablation shows it is not alone sufficient — though the ablation also reduces model capacity, preventing clean causal attribution'; (3) 明确承认 LoRA ablation 同时改变了多个变量.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: \"Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露, 可能 confound degeneracy 比较\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识 (R1-W6 + R2 strongly AGREE): 主文 Section 4.1 说 '5 epochs' 暗示统一设置, 但 Appendix 显示 Few-NERD 仅 3 epochs. Under-training 直接降低 model convergence → 降低 degeneracy. Few-NERD 的低 degeneracy (10%) 可能部分源自训练不足而非 dataset intrinsic property. 这严重削弱 'degeneracy is dataset-specific' 和跨数据集 degeneracy-gating 的因果论证.\"\n  action_items:\n  - round: 17\n    action: \"(1) 主文 Section 4.1 明确披露 Few-NERD 为 3 epochs 及原因; (2) 补充 5-epoch Few-NERD 的 degeneracy rate 和 LP selection 数据; (3) 如果 5-epoch degeneracy 显著升高, 讨论对 degeneracy-gating narrative 的影响.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: \"em-dash (---) 使用约 90 处, AI 写作风格痕迹显著\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W4 + R1 AGREE): 正文约 35 处, Appendix 约 55 处. Abstract 2 处, Introduction 7 处, Discussion 14 处. 每段 1-2 个解释性 em-dash. 审稿人最敏感的 AI 写作标志. 建议减少到正文 10 处以内.\"\n  action_items:\n  - round: 17\n    action: \"grep '---' 全文, 将大部分解释性 em-dash 替换为逗号、括号或拆句. 正文目标 ≤10 处, 保留仅限于无法替代的场景.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W4\n  summary: \"Discussion section 过长 (2+ 页, 14 个 sub-topics), 部分内容应移入 Appendix\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W8 + R1 AGREE): Discussion 承载 14 个 sub-topics. 建议移入 Appendix: non-tied subset analysis, N-scaling effect, temperature effect, verbalized confidence, signal combinations. 可释放 ~1 page 用于 positive contribution 或更清晰的 framing.\"\n  action_items:\n  - round: 17\n    action: \"将 Discussion 中的 N-scaling, temperature, verbalized confidence, signal combinations 移入 Appendix, 仅在 Discussion 保留引用. Discussion 聚焦: (1) why the gap exists, (2) regime boundaries, (3) practical implications, (4) methodological implications.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: \"Supervised verifier baseline 使用 5 个 scalar features 过于受限, 结论过度泛化\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-Q4 + R1 AGREE): 5 个 features 中 4 个是 instance-level aggregates, 本质上 encode 不了 per-sample discriminative information. 'bottleneck lies in the feature space' 仅适用于 THESE 5 features, 不能泛化为 'no feature combination can close the gap'. 加入 token-level features 可能完全改变结论.\"\n  action_items:\n  - round: 17\n    action: \"Section 4.5 supervised verifier 结论限定为 'the bottleneck lies in these five specific features rather than the aggregation model'. 不可声称 no features can close the gap.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M1\n  summary: \"Abstract 中 MBR 缩写未展开\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"R17 (R2-M2): Abstract 中 MBR 首次出现未展开 (Minimum Bayes Risk). NER 是标准缩写无需展开, 但 MBR 应展开.\"\n  action_items:\n  - round: 17\n    action: \"Abstract 中 MBR 首次出现时展开为 'minimum Bayes risk (MBR)'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: \"Table 3 中 EM 和 VC 的 p 值标为 '---' 但未解释原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"R17 (R2-M3): EM (0.637) 和 VC (0.623) 低于 greedy (0.645), 方向为负. 应标注 'below greedy' 或注释说明.\"\n  action_items:\n  - round: 17\n    action: \"Table 3 caption 或 footnote 解释为何 EM/VC 无 p 值 (方向为负, 不测试 improvement).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M3\n  summary: \"Figure 3 '~15%' degeneracy threshold 缺乏精确定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"R17 (R2-M4): dashed line 位置应有 explicit justification (如 breakpoint detection), 而非视觉近似.\"\n  action_items:\n  - round: 17\n    action: \"Figure 3 caption 或正文说明 15% 的来源 (如 visual breakpoint 或 formal threshold analysis). 或改为 'approximately 15%' 并承认是 exploratory.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-14, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4x variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 dagger-RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n\n# ===== RECURRING ISSUES (updated Round 17) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 17\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 核心 finding 实质仅 SciERC 验证.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已加入 Few-NERD. 但 positive finding 仅 1 model x 1 N x 1 dataset.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: Few-NERD 加入后 dataset 覆盖改善, 但 cross-dataset degeneracy gradient 仍仅 n=3. R1 建议增加 OntoNotes/ACE05. R2 建议 Few-NERD cross-model 验证. 核心问题: degeneracy-gating pattern 的统计基础薄弱.\"\n  action_items:\n  - round: 11\n    action: \"标题或 abstract 首句显式限定 RE scope\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 12\n    action: \"Title→NER (D106).\"\n    assigned_to: Paper Agent\n    status: done\n  - round: 13\n    action: \"收窄 claim scope 或增加中等难度数据集.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  - round: 17\n    action: \"增加 1-2 个 NER 数据集 (OntoNotes, ACE05) 扩大 degeneracy gradient 的 n; 或将 cross-dataset gradient 明确标注为 exploratory observation (n=3 不足以做因果推断).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 17\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识: 标题暗示意外发现但 4/5 signals weakness 部分 by construction.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2 重申 novelty 有限 (W1). R1 部分反驳: prior work 确实 conflated QE/selection, 概念分离有价值. 但两位都同意纯诊断性贡献对 main conference 门槛偏弱. R1 建议 reframe LP positive result (Few-NERD) 为 actionable finding.\"\n  action_items:\n  - round: 17\n    action: \"三层叙事明确分离: (1) definitional limitation (noted, not discovered); (2) MBR empirical failure despite aligned utility (novel diagnosis); (3) LP compression (novel finding). 标题 'Weak Selectors' 加 nuance.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + Bonferroni scope 争议\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 17\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Footnote 4 措辞需修正.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"Footnote 4 改为 'survives Bonferroni over 5 signal comparisons, conditional on pre-selected epsilon=0.05'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"核心增量是 'why QE != selection' 的诊断.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-W6 再次提出差异化不足. R1 反驳: 差异化充分但叙述位置不够 upfront. 共识: Introduction 中应更显著地定位差异.\"\n  action_items:\n  - round: 17\n    action: \"Introduction 第二段将 Yao et al. 差异化提前并加粗关键区分点: (1) fine-tuned models (degeneracy 更严重), (2) QE/selection 分离, (3) failure mechanism diagnosis.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"'scale' 含义需澄清.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: R2-Q3 提出 70B+ 模型可能 degeneracy 更高, 整个方向可能无望. R1 反驳: 70B LP quality 可能不同, QE 不受影响. 共识: Limitations 需更明确讨论 scale 外推的不确定性.\"\n  action_items:\n  - round: 16\n    action: \"Abstract/Introduction 澄清 'scale' 含义.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"m=3, exact p~0.028.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"主文加 caveat: 'though statistical precision is limited with m=3 raters'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"论文已有 (a)-(d) 四个 hypotheses.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"R16 未被独立提及.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W4 + R2 AGREE): RE free-form +2.35pp (p=0.025) 直接证明 constraints DO compress LP for RE. Abstract/Introduction 中 'compressed to near-ineffectiveness' 未限定为 NER-specific. 需加 task qualifier.\"\n  action_items:\n  - round: 17\n    action: \"Abstract line 6 和 Introduction contribution 2(c) 中 'compressed to near-ineffectiveness' 加 'for NER' 限定. Discussion 已有 NER/RE 区分但需更显著.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-N1\n  summary: \"rho headline 来自 ceiling-effect dataset / 数值不一致\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Abstract/Figure 1 caption rho=0.42 归因错误.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. R16 action 仍 open.\"\n  action_items:\n  - round: 16\n    action: \"全文统一 headline rho 归属. Figure 1 caption 修正.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"多种 remedy 已测试并全部 negative.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W3 + R1 AGREE): 纯诊断性论文缺乏 positive contribution 是核心 excitement 问题. 已测试 entity-token LP, LP x VC, supervised combination, verbalized confidence, 全部 negative. R1 建议 reframe Few-NERD LP positive result 为 actionable finding (LP works when degeneracy <15%). R2 建议增加 lightweight trained verifier.\"\n  action_items:\n  - round: 17\n    action: \"(1) Reframe Few-NERD LP +1.36pp 为 practical positive finding, 不仅是诊断证据; (2) 提供 degeneracy-based decision rule (practitioners should check degeneracy rate before investing in BoN); (3) 如果时间允许, train lightweight verifier 在 SciERC 上验证 oracle gap 可否被 partially closed.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Table 4 SciERC full set vs Table 2 gold-filtered.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W8 + R2 partial rebut): Footnote 解释存在但容易被忽略. 建议 Table 4 同时报告 gold-filtered 数字或在 caption 中更显著标注.\"\n  action_items:\n  - round: 17\n    action: \"Table 4 caption 中显式标注 'full-set evaluation (cf. gold-filtered in Table 3)' 而非仅在 footnote.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"建议改名为 'Soft Overlap' 或加注释.\"\n  - round: 17\n    reviewers: [1]\n    note: \"R17 (R1-W7): footnote 表述 'Δρ<0.01' 应改为 '|Δρ|≤0.009'. Minor.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 / 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"9 句话含过多技术细节.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W5 + R1 AGREE): Abstract 约 180 words 含 15+ 数字 (ρ, AUROC, pp, nats, p, N, degeneracy%). 远超审稿人 30 秒吸收能力. 实验报告风格而非 story-driven.\"\n  action_items:\n  - round: 17\n    action: \"Abstract 数字压缩到 4-5 个最关键的. 移除 specific ρ/AUROC 数字, 用 'moderate-to-strong correlations' 替代. 保留 key claims: 13pp oracle headroom, 0 net selection gain, degeneracy pattern.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Eikema argues utility design; 本文证明 utility IS aligned but degeneracy eliminates headroom.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. R16 action 仍 open.\"\n  action_items:\n  - round: 16\n    action: \"Related Work 增加 differentiation paragraph vs Eikema.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) / sign test 统计效力极低\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"SciERC null result 应改为 'effect small and not reliably detected'.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W3 + R2 AGREE): 负面结果缺少 power analysis. n=529, 2 seeds 检测 1pp 效应的 power 约 50-60%. p=0.29 无法区分 '真无效果' 和 '检测不到'. 建议加 post-hoc power analysis 或更明确指出 Few-NERD (n=32,565) 才是 definitive evidence.\"\n  action_items:\n  - round: 17\n    action: \"(1) 加 post-hoc power analysis: 在 n=529, σ~0.15 下检测 1pp 效应的 power; (2) 主文改为 'the observed LP advantage is small and not reliably detected at N=8'; (3) 明确指出 Few-NERD 是 definitive evidence, SciERC 受限于 power.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"greedy 'surpassing' 只反映 T=0 vs T=1 差异.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 15\n    action: \"修辞改为 'selection adds no benefit over greedy'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation: 8B vs 4B degeneracy 差异的解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"LoRA-rank ablation 是 interventional evidence.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 16\n    action: \"LoRA-rank as primary (interventional), 8B vs 4B as supporting (observational).\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"3.5pp 差距是系统性的. 定义差异需说明.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. 论文 Section 4.3 line 110 已有解释: 'the difference between deterministic decoding (T=0) and uniformly sampling one of N stochastic candidates (T=1.0); greedy is not drawn from the candidate pool.' 此解释清楚了 Random 是从 N 个 T=1 sample 中随机选, Greedy 是 T=0.\"\n  action_items:\n  - round: 16\n    action: \"明确 Random 和 Greedy 的精确定义差异.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Introduction 首次使用时需给出 one-sentence 定义.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-M4 → R1 comment on Abstract): 'correlation-selection gap' 在 Abstract 引入但未定义. 建议 Abstract 或 Introduction 首次使用时加一句简短释义.\"\n  action_items:\n  - round: 17\n    action: \"Introduction 首次使用 'correlation-selection gap' 时加 '(the disparity between a signal's ability to rank instances reliably and its failure to select the best output within a single instance)' 或类似释义.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 维持; R2 REBUT (LoRA-rank 已做 interventional control).\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R1-W6 + R2 strongly AGREE): Few-NERD 训练 3 epochs vs 其他 5 epochs 是关键 confound. 主文说 '5 epochs' 暗示统一, Appendix 才披露 3 epochs. Under-training 直接降低 degeneracy. 如果 5-epoch Few-NERD degeneracy 显著高于 10%, 整个 degeneracy-gating narrative 需重新评估.\"\n  action_items:\n  - round: 17\n    action: \"(1) 主文 Section 4.1 明确披露 Few-NERD 为 3 epochs (非仅 Appendix); (2) 解释为何使用 3 epochs (dataset 规模/early stopping?); (3) 如可能, 补充 5-epoch Few-NERD degeneracy 数据; (4) 承认 epoch difference 作为 confound 并讨论其对 cross-dataset comparison 的影响.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"呈现应更平衡.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  action_items:\n  - round: 16\n    action: \"Section 4.3 增加 harmful selection 讨论.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N1\n  summary: \"Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点, 统计不显著 (p=0.066)\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"3 个 dataset-level 数据点无统计意义.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识 (R1-W1 + R2 AGREE): 核心问题不变. Figure 3 pooled correlation 混合两个粒度的观测, 统计上有问题. Entity-type-level (n=8, ρ=-0.881, p=0.004) 更有力但存在 independence 问题 (共享 model/pipeline). 建议: (1) 不 pool 不同粒度; (2) 控制 entity type frequency; (3) cross-dataset claim 降级为 exploratory.\"\n  action_items:\n  - round: 17\n    action: \"(1) Figure 3 不 pool 两个粒度, 分别报告 dataset-level (n=3, exploratory) 和 entity-type-level (n=8, p=0.004); (2) 控制 entity type frequency/entity count 作为 confound; (3) 主文 'monotonically predicts' 改为 'inversely associated with' (已部分完成但需全文统一).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N2\n  summary: \"rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Figure 1 caption 'rho up to 0.42 on primary test bed' 与 Table 1 SciERC max=0.379 矛盾.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及. R16 action 仍 open.\"\n  action_items:\n  - round: 16\n    action: \"全文统一 headline rho 归属.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 17) =====\n- id: R17-W1\n  summary: \"LoRA rank=8 下 LP compression 统计数据缺失, 无法支撑 'necessary but not sufficient' claim\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识 (R1-W2/Q1 + R2 AGREE): LoRA rank=8 ablation 降低 degeneracy (21%→7.2%) 且增加 headroom (13.3→16.0pp), 但 LP selection 仍失败. 论文据此声称 'necessary but not sufficient'. 但未报告 rank=8 下 LP 的 median within-instance range 和 tied fraction. 如果 rank=8 下 LP compression 更严重 (因模型能力下降), 则 selection failure 可归因于 compression 加剧而非 degeneracy 本身不充分. 此外, rank=8 同时改变了 model capability (greedy F1: 0.645→0.640), 无法做 clean causal attribution.\"\n  action_items:\n  - round: 17\n    action: \"(1) 报告 LoRA rank=8 下 LP 的 median within-instance range, tied fraction, 和 pooled within-instance ρ(LP,F1); (2) 将 claim 弱化为 'low degeneracy co-occurs with LP selection success, but rank-8 ablation shows it is not alone sufficient — though the ablation also reduces model capacity, preventing clean causal attribution'; (3) 明确承认 LoRA ablation 同时改变了多个变量.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: \"Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露, 可能 confound degeneracy 比较\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识 (R1-W6 + R2 strongly AGREE): 主文 Section 4.1 说 '5 epochs' 暗示统一设置, 但 Appendix 显示 Few-NERD 仅 3 epochs. Under-training 直接降低 model convergence → 降低 degeneracy. Few-NERD 的低 degeneracy (10%) 可能部分源自训练不足而非 dataset intrinsic property. 这严重削弱 'degeneracy is dataset-specific' 和跨数据集 degeneracy-gating 的因果论证.\"\n  action_items:\n  - round: 17\n    action: \"(1) 主文 Section 4.1 明确披露 Few-NERD 为 3 epochs 及原因; (2) 补充 5-epoch Few-NERD 的 degeneracy rate 和 LP selection 数据; (3) 如果 5-epoch degeneracy 显著升高, 讨论对 degeneracy-gating narrative 的影响.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W3\n  summary: \"em-dash (---) 使用约 90 处, AI 写作风格痕迹显著\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W4 + R1 AGREE): 正文约 35 处, Appendix 约 55 处. Abstract 2 处, Introduction 7 处, Discussion 14 处. 每段 1-2 个解释性 em-dash. 审稿人最敏感的 AI 写作标志. 建议减少到正文 10 处以内.\"\n  action_items:\n  - round: 17\n    action: \"grep '---' 全文, 将大部分解释性 em-dash 替换为逗号、括号或拆句. 正文目标 ≤10 处, 保留仅限于无法替代的场景.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W4\n  summary: \"Discussion section 过长 (2+ 页, 14 个 sub-topics), 部分内容应移入 Appendix\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-W8 + R1 AGREE): Discussion 承载 14 个 sub-topics. 建议移入 Appendix: non-tied subset analysis, N-scaling effect, temperature effect, verbalized confidence, signal combinations. 可释放 ~1 page 用于 positive contribution 或更清晰的 framing.\"\n  action_items:\n  - round: 17\n    action: \"将 Discussion 中的 N-scaling, temperature, verbalized confidence, signal combinations 移入 Appendix, 仅在 Discussion 保留引用. Discussion 聚焦: (1) why the gap exists, (2) regime boundaries, (3) practical implications, (4) methodological implications.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: \"Supervised verifier baseline 使用 5 个 scalar features 过于受限, 结论过度泛化\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 (R2-Q4 + R1 AGREE): 5 个 features 中 4 个是 instance-level aggregates, 本质上 encode 不了 per-sample discriminative information. 'bottleneck lies in the feature space' 仅适用于 THESE 5 features, 不能泛化为 'no feature combination can close the gap'. 加入 token-level features 可能完全改变结论.\"\n  action_items:\n  - round: 17\n    action: \"Section 4.5 supervised verifier 结论限定为 'the bottleneck lies in these five specific features rather than the aggregation model'. 不可声称 no features can close the gap.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M1\n  summary: \"Abstract 中 MBR 缩写未展开\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"R17 (R2-M2): Abstract 中 MBR 首次出现未展开 (Minimum Bayes Risk). NER 是标准缩写无需展开, 但 MBR 应展开.\"\n  action_items:\n  - round: 17\n    action: \"Abstract 中 MBR 首次出现时展开为 'minimum Bayes risk (MBR)'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: \"Table 3 中 EM 和 VC 的 p 值标为 '---' 但未解释原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"R17 (R2-M3): EM (0.637) 和 VC (0.623) 低于 greedy (0.645), 方向为负. 应标注 'below greedy' 或注释说明.\"\n  action_items:\n  - round: 17\n    action: \"Table 3 caption 或 footnote 解释为何 EM/VC 无 p 值 (方向为负, 不测试 improvement).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M3\n  summary: \"Figure 3 '~15%' degeneracy threshold 缺乏精确定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"R17 (R2-M4): dashed line 位置应有 explicit justification (如 breakpoint detection), 而非视觉近似.\"\n  action_items:\n  - round: 17\n    action: \"Figure 3 caption 或正文说明 15% 的来源 (如 visual breakpoint 或 formal threshold analysis). 或改为 'approximately 15%' 并承认是 exploratory.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1714 · 2026-05-17T07:24:41.712450+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 34367}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 1715 · 2026-05-17T07:27:12.744576+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 17 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量)\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断 → 汇总\n\n---\n\n## Summary\n\n本文系统评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 LLM-based NER 中的质量估计（QE）和 best-of-N 样本选择表现。核心发现是 \"correlation-selection gap\"：QE 成功（ρ up to 0.38 on SciERC, 0.42 on Few-NERD; AUROC up to 0.82）但 selection 失败，归因于三层机制——instance-level signals by construction 不能排名候选、instance degeneracy (10-58%) 消除 MBR headroom、LP compression (median range 0.041 nats) 限制 per-sample 信号。LP selection 在低 degeneracy regime (Few-NERD, 10%) 显著有效 (+1.36pp, p<0.001)，在高 degeneracy regime 失败。实验覆盖 4 个 NER benchmark、2 个 model families (Qwen3-8B, LLaMA-3.1-8B)、4B ablation，统计方法严谨（bootstrap CI, TOST, Bonferroni）。\n\n---\n\n## Strengths\n\n1. **问题定义有价值**: \"Correlation-selection gap\" 将 QE 和 selection 明确解耦，指出 prior work 长期混淆的两个任务。Instance-level vs per-sample 的形式化区分简洁且数学正确。[R1 S1, R2 S1 — AGREE]\n\n2. **实验设计系统**: 4 个 NER benchmark 构成 difficulty gradient（WNUT collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），角色清晰。两个 model families + 4B/3B ablation + LoRA-rank ablation 排除多种 confound。[R1 S2, R2 S2 — AGREE]\n\n3. **统计严谨性远超平均**: Bootstrap CI (B=10,000)、paired sign tests、TOST equivalence testing、Bonferroni correction、Kendall's W ranking stability。负面结果使用 TOST 避免 \"absence of evidence = evidence of absence\" 谬误。明确区分 effect size 和 statistical significance。[R1 S3, R2 S3 — AGREE]\n\n4. **三层诊断逻辑递进**: (a) by construction → (b) degeneracy → (c) compression。Supervised verifier baseline 确认 bottleneck 在 feature space（而非 aggregation），free-form ablation 和 entity-token LP 排除替代假说。[R1 S4, R2 S4 — AGREE]\n\n5. **负面结果表达审慎**: 使用 \"inversely associated with\" 而非 \"causes\"，\"necessary but not sufficient\" 限定 claim，Limitations 详尽。[R1 S5]\n\n6. **Appendix 丰富**: FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等覆盖大多数潜在反驳。[R1 S6]\n\n7. **引用覆盖充分**: 59 篇引用，覆盖 self-consistency、MBR decoding、uncertainty estimation、best-of-N、diversity collapse 等方向。与 Yao et al. (2026) 的区分清楚。[R2 S5]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**W1. Degeneracy-gating 跨数据集因果证据薄弱 (n=3)**\n[R1-W1, R2-Q1 — 强共识]\n核心 claim \"LP selection effectiveness is inversely associated with degeneracy\" 仅基于 3 个 dataset-level 数据点（CoNLL 58% → SciERC 21% → Few-NERD 10%），单调排列概率 1/6。Figure 3 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合两个粒度的观测（3 dataset-level + 8 entity-type-level），违反独立性假设。Entity-type-level evidence (n=8, ρ=-0.881, p=0.004) 更有力但共享训练 pipeline。建议：(a) 增加 1-2 个数据集；(b) 不 pool 不同粒度；(c) 控制 entity type frequency 作为 confound。\n\n**W2. LoRA rank=8 ablation 的 \"necessary but not sufficient\" claim 缺乏关键数据**\n[R1-W2/Q1, R2-Q2 — 强共识]\nRank=8 降低 degeneracy (21%→7.2%) 但 LP selection 仍失败，论文据此声称 degeneracy \"necessary but not sufficient\"。但未报告 rank=8 下 LP 的 median within-instance range 和 tied fraction。如果 rank=8 下 LP compression 更严重（因模型能力下降），则 selection failure 可归因于 compression 加剧而非 degeneracy 不充分。同时 rank=8 降低了 greedy F1 (0.645→0.640)，无法做 clean causal attribution。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% → LP fails 的矛盾需更好解释。\n\n**W3. Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露**\n[R1-W6, R2 strongly AGREE — 强共识]\n主文 Section 4.1 说 \"5 epochs\" 暗示统一设置，Appendix 才披露 Few-NERD 仅 3 epochs。Under-training 直接降低 model convergence → 降低 degeneracy。Few-NERD 的低 degeneracy (10%) 可能部分源自训练不足而非 dataset intrinsic property。这严重削弱 \"degeneracy is dataset-specific\" 和跨数据集 degeneracy-gating 的因果论证。需：(a) 主文披露差异；(b) 解释原因；(c) 补充 5-epoch degeneracy 数据。\n\n**W4. 缺乏可操作的 positive contribution**\n[R2-W3, R1 AGREE — 强共识]\n论文全部 takeaway 是 \"closing the gap requires trained verifiers\"，但不训练 verifier、不提出新 signal。已测试的 remedy 全部失败（entity-token LP, LP×VC, supervised combination, verbalized confidence）。纯诊断性 negative result 论文需要极强 insight novelty 或可操作性来补偿。Few-NERD LP +1.36pp 是 positive result，但被 framing 为诊断证据而非实用方法。建议：(a) reframe LP 在低 degeneracy regime 的成功为 actionable finding；(b) 提供 degeneracy-based decision rule。\n\n### Should-Fix\n\n**W5. 负面结果缺少 power analysis**\n[R1-W3, R2 AGREE]\nSciERC (n=529, 2 seeds) 检测 1pp 效应的 power 约 50-60%。p=0.29 无法区分 \"真无效果\" 和 \"检测不到\"。Few-NERD (n=32,565) 才是 definitive evidence。建议加 post-hoc power analysis 或明确指出 Few-NERD 是 definitive。\n\n**W6. \"Compression is model-intrinsic\" 与 RE free-form 结果矛盾但主文未 qualify**\n[R1-W4, R2 AGREE]\nNER free-form ablation std ratio 0.97 → \"model-intrinsic\"。但 RE free-form +2.35pp (p=0.025) 直接证明 constraints DO compress LP for RE。Abstract/Introduction 中 \"compressed to near-ineffectiveness\" 未限定为 NER-specific。\n\n**W7. em-dash (---) 过度使用（约 90 处），AI 写作风格痕迹**\n[R2-W4, R1 AGREE]\n正文约 35 处，Appendix 约 55 处。平均每段 1-2 个解释性 em-dash。审稿人最敏感的 AI 写作标志。建议正文减至 ≤10 处。\n\n**W8. Abstract 和 Introduction 过度堆砌数字**\n[R2-W5, R1 AGREE]\nAbstract 约 180 words 含 15+ 个具体数字。实验报告风格而非 story-driven。建议保留 3-4 个最关键数字，其余用定性描述。\n\n**W9. Discussion section 过长 (2+ 页, 14 个 sub-topics)**\n[R2-W8, R1 AGREE]\nN-scaling, temperature, verbalized confidence, signal combinations 等 ablation 内容适合移入 Appendix。可释放 ~1 page 用于改善 framing 或增加 constructive contribution。\n\n**W10. Supervised verifier baseline feature space 过于受限**\n[R2-Q4, R1 AGREE]\n5 个 features 中 4 个是 instance-level aggregates，encode 不了 per-sample discriminative information。\"Bottleneck lies in the feature space\" 仅适用于这 5 个 features，不能泛化。\n\n**W11. 与 Yao et al. (2026) 差异化叙述位置不够显著**\n[R2-W6, R1 partial REBUT]\n差异化内容存在但在 Introduction 中不够 upfront。R1 认为差异充分，R2 认为应更显著。共识：Introduction 应更前置差异化。\n\n**W12. Selection 实验 seed coverage 有限**\n[R1-W5, R2 partial REBUT]\nQE 仅 1 seed，selection 仅 2 seeds。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。R2 反驳：n=32,565 的 within-seed power 极高。共识：training seed stochasticity 的影响虽合理推断为小（multi-seed stability σ≤0.026），但严格来说未被验证。\n\n### Minor\n\n**M1.** Abstract 中 MBR 缩写未展开 [R2-M2]\n**M2.** Table 3 EM/VC 无 p 值未解释（方向为负）[R2-M3]\n**M3.** Figure 3 \"~15%\" degeneracy threshold 缺乏精确定义 [R2-M4]\n**M4.** SJ normalizer claim \"Δρ<0.01\" 应改为 \"|Δρ|≤0.009\" [R1-W7]\n**M5.** Table 3 vs Table 4 greedy F1 不一致（gold-filtered vs full-set），footnote 存在但容易被忽略 [R1-W8]\n**M6.** \"leverage\" 用词 (Appendix L235) [R2-M1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **实验执行质量高**: 统计方法、ablation 覆盖、负面结果处理均远超平均。[R1 3.5 + R2 4 Soundness]\n2. **Degeneracy-gating 因果证据不足**: n=3 datasets, pooled granularity, Few-NERD epoch confound, LoRA rank=8 混淆变量。\n3. **缺乏 positive contribution**: 诊断有深度但无可操作方法。多种 remedy 已测试（全 negative），这有价值但降低了 excitement。\n4. **写作可改进**: em-dash 过多、数字堆砌、Discussion 过长。\n5. **Reproducibility 高**: 模型/数据集公开，超参数详细，承诺 code release。\n\n## Reviewer Divergence [分歧记录]\n\n1. **Overall score**: R1 = Borderline Accept (3.5/5), R2 = Borderline Reject (3.0/5, leaning Findings)\n2. **Excitement**: R1 = 3.5, R2 = 2.5\n3. **分歧本质**: 纯诊断性论文（strong execution + negative result + diagnostic value）是否满足 EMNLP main conference 门槛。R1 认为 \"correlation-selection gap\" 概念化 + 三层诊断的系统性 + Few-NERD positive result 足以构成 borderline accept；R2 认为核心发现的 novelty（partially definitional + partially known phenomena）和 actionability 不够 main conference，更适合 Findings。\n4. **Degeneracy as trivial correlate**: R2 初始 claim degeneracy = model success 的 trivial correlate；R1 用 Few-NERD (75% F1, 10% degen) 和 4B/8B 对比反驳，证明 degeneracy 不完全是 capability proxy。R2 在交叉中部分接受但维持 deeper point：论文需 disentangle degeneracy 的多个 driver。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1.** LoRA rank=8 下 LP 的 median within-instance range、tied fraction、pooled within-instance ρ(LP,F1) 是多少？[R1-Q1, R2 AGREE — 关键缺失数据]\n\n**Q2.** Few-NERD 训练为何仅 3 epochs？5 epochs 下的 degeneracy rate 和 LP selection 效果是多少？[R1-Q2, R2 AGREE — 关键 confound]\n\n**Q3.** Within-instance SJ-F1 ρ=0.52 的 distribution 如何？多少比例的 non-degenerate instances 有 ρ<0？[R1-Q4, R2 partial concern]\n\n**Q4.** Entity-type-level degeneracy-LP gain 分析是否控制了 entity type frequency 或 average entity count per sentence 作为 confound？[R1-Q5, R2 AGREE]\n\n**Q5.** Supervised verifier 加入 token-level features（如 per-entity LP 分布统计）能否 close gap？[R2-Q4, R1 AGREE]\n\n**Q6.** Few-NERD 低 degeneracy 是否主要因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 函数。[R2-Q1]\n\n---\n\n## Missing References\n\n1. **Byerly & Khashabi (2024)** \"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\" — SC 中 correlated errors 导致失败的分析 [R2-W7; R1 质疑此引用是否存在，需作者核实]\n2. **Diverse Beam Search** (Vijayakumar et al., 2016) — diversity-promoting decoding 作为 degeneracy 的潜在缓解 [R2]\n3. **CRF-based calibration 经典工作** — structured prediction uncertainty estimation [R2]\n4. **Zhang et al. (2024) DeepMind test-time compute scaling** — fine-tuned model diversity collapse 与 test-time compute 关系 [R1; R2 指出 Snell et al. 2025 已覆盖 ICLR 版本]\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n**Confidence: 4/5**\n\n这是一篇实验工作量大、统计处理严谨、ablation 覆盖度高的论文。\"Correlation-selection gap\" 概念对社区有 guidance 价值，三层诊断结构清晰，Few-NERD 的 positive result 证明 LP selection 在低 degeneracy regime 可行。\n\n但论文面临以下核心问题：\n1. **因果证据薄弱**：degeneracy-gating 的跨数据集证据仅 n=3 且 Few-NERD 存在 epoch confound，LoRA ablation 有混淆变量\n2. **Novelty/actionability 不足**：三层诊断中第一层 (instance-level limitation) 是 definitional，第二层 (degeneracy) 与已知 diversity collapse 有重叠，第三层 (LP compression) 是 specific but limited impact。缺乏可操作的 positive method contribution\n3. **写作问题**：em-dash 过多 (~90)、Abstract 数字堆砌、Discussion 过长\n\n**投稿建议**: 介于 Main Conference 和 Findings 之间。如果能在 rebuttal/revision 中：(a) 补充 LoRA rank=8 LP compression 数据，(b) 澄清 Few-NERD epoch confound（最好补 5-epoch 数据），(c) reframe LP 在低 degeneracy regime 的成功为 actionable finding 并提供 decision rule，(d) 大幅减少 em-dash 和 Abstract 数字，可升至 weak accept。否则建议 Findings。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 信息密度过高，15+ 数字在 ~180 words 中\n- \"Correlation-selection gap\" 首次出现时需一句释义\n- \"Compressed to near-ineffectiveness\" 未限定 NER-specific\n- MBR 缩写未展开\n\n### Introduction\n- 叙事线清晰（self-consistency success → NER structural challenge → gap → diagnosis）\n- Contribution 2 和 3 有重叠（degeneracy 既是 gap 原因又是 regime boundary）\n- 与 Yao et al. 的差异化位置不够 upfront\n- Contribution list 中 by-construction limitation 应标注为 conceptual note 而非 empirical finding\n\n### Method (Section 3)\n- 形式化清晰正确，5 个 signal 定义完整\n- FK adaptation 有 independence test 支撑（Appendix）\n- SJ 分母用 max 非标准 Jaccard，footnote 有说明但 naming 可改进\n\n### Experiments (Section 4)\n- 数据集选择合理且角色分工清晰\n- 训练细节充分（Table 7），但 Few-NERD 3 epochs 需在主文披露\n- vLLM 版本号未报告\n- Table 3 vs Table 4 evaluation protocol 差异需更显著标注\n\n### Discussion (Section 5)\n- 内容丰富但过长，14 个 sub-topics 可压缩\n- \"Why the gap exists\" 是核心，degeneracy + LP compression 分析有力\n- Entity-token LP ablation (negative result) 有价值\n- Signal combination + supervised verifier 确认 feature space bottleneck\n- Practical considerations 实用（N=8 suffices for QE）\n\n### Conclusion\n- 过于简短（10 行），未讨论 broader implications\n- 建议增加 practical guidance summary\n\n### Limitations\n- 全面且诚实\n- 建议补充：power analysis limitation、Few-NERD epoch confound\n\n---\n\n## 官方维度打分（ACL ARR Review Form 综合）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5/5 | 3/5 | 3.25/5 |\n\n---\n\n## Issue Tracker 更新摘要 (Round 17)\n\n**新增 issues**: 6 个\n- R17-W1 [critical]: LoRA rank=8 LP compression 数据缺失\n- R17-W2 [critical]: Few-NERD 3 epochs confound 未在主文披露\n- R17-W3 [warning]: em-dash 过度使用 (~90 处)\n- R17-W4 [warning]: Discussion 过长\n- R17-W5 [warning]: Supervised verifier 结论过度泛化\n- R17-M1/M2/M3 [info]: 缩写、p 值、threshold 精度\n\n**跨轮次 recurring issues 仍 open**: R0-C3, R3-W2, R12-N1, R13-W2, R14-W1, R16-N1 等\n**跨轮次已解决 issues**: 34 个（Rounds 0-15）",
  "project": "struct_self_consist_ie",
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
    "report": "# Round 17 审稿报告\n\n**论文**: \"Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\"\n**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**截止日期**: 2026-05-25\n**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量)\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断 → 汇总\n\n---\n\n## Summary\n\n本文系统评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 LLM-based NER 中的质量估计（QE）和 best-of-N 样本选择表现。核心发现是 \"correlation-selection gap\"：QE 成功（ρ up to 0.38 on SciERC, 0.42 on Few-NERD; AUROC up to 0.82）但 selection 失败，归因于三层机制——instance-level signals by construction 不能排名候选、instance degeneracy (10-58%) 消除 MBR headroom、LP compression (median range 0.041 nats) 限制 per-sample 信号。LP selection 在低 degeneracy regime (Few-NERD, 10%) 显著有效 (+1.36pp, p<0.001)，在高 degeneracy regime 失败。实验覆盖 4 个 NER benchmark、2 个 model families (Qwen3-8B, LLaMA-3.1-8B)、4B ablation，统计方法严谨（bootstrap CI, TOST, Bonferroni）。\n\n---\n\n## Strengths\n\n1. **问题定义有价值**: \"Correlation-selection gap\" 将 QE 和 selection 明确解耦，指出 prior work 长期混淆的两个任务。Instance-level vs per-sample 的形式化区分简洁且数学正确。[R1 S1, R2 S1 — AGREE]\n\n2. **实验设计系统**: 4 个 NER benchmark 构成 difficulty gradient（WNUT collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），角色清晰。两个 model families + 4B/3B ablation + LoRA-rank ablation 排除多种 confound。[R1 S2, R2 S2 — AGREE]\n\n3. **统计严谨性远超平均**: Bootstrap CI (B=10,000)、paired sign tests、TOST equivalence testing、Bonferroni correction、Kendall's W ranking stability。负面结果使用 TOST 避免 \"absence of evidence = evidence of absence\" 谬误。明确区分 effect size 和 statistical significance。[R1 S3, R2 S3 — AGREE]\n\n4. **三层诊断逻辑递进**: (a) by construction → (b) degeneracy → (c) compression。Supervised verifier baseline 确认 bottleneck 在 feature space（而非 aggregation），free-form ablation 和 entity-token LP 排除替代假说。[R1 S4, R2 S4 — AGREE]\n\n5. **负面结果表达审慎**: 使用 \"inversely associated with\" 而非 \"causes\"，\"necessary but not sufficient\" 限定 claim，Limitations 详尽。[R1 S5]\n\n6. **Appendix 丰富**: FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等覆盖大多数潜在反驳。[R1 S6]\n\n7. **引用覆盖充分**: 59 篇引用，覆盖 self-consistency、MBR decoding、uncertainty estimation、best-of-N、diversity collapse 等方向。与 Yao et al. (2026) 的区分清楚。[R2 S5]\n\n---\n\n## Weaknesses\n\n### Critical (Must-Fix)\n\n**W1. Degeneracy-gating 跨数据集因果证据薄弱 (n=3)**\n[R1-W1, R2-Q1 — 强共识]\n核心 claim \"LP selection effectiveness is inversely associated with degeneracy\" 仅基于 3 个 dataset-level 数据点（CoNLL 58% → SciERC 21% → Few-NERD 10%），单调排列概率 1/6。Figure 3 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合两个粒度的观测（3 dataset-level + 8 entity-type-level），违反独立性假设。Entity-type-level evidence (n=8, ρ=-0.881, p=0.004) 更有力但共享训练 pipeline。建议：(a) 增加 1-2 个数据集；(b) 不 pool 不同粒度；(c) 控制 entity type frequency 作为 confound。\n\n**W2. LoRA rank=8 ablation 的 \"necessary but not sufficient\" claim 缺乏关键数据**\n[R1-W2/Q1, R2-Q2 — 强共识]\nRank=8 降低 degeneracy (21%→7.2%) 但 LP selection 仍失败，论文据此声称 degeneracy \"necessary but not sufficient\"。但未报告 rank=8 下 LP 的 median within-instance range 和 tied fraction。如果 rank=8 下 LP compression 更严重（因模型能力下降），则 selection failure 可归因于 compression 加剧而非 degeneracy 不充分。同时 rank=8 降低了 greedy F1 (0.645→0.640)，无法做 clean causal attribution。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% → LP fails 的矛盾需更好解释。\n\n**W3. Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露**\n[R1-W6, R2 strongly AGREE — 强共识]\n主文 Section 4.1 说 \"5 epochs\" 暗示统一设置，Appendix 才披露 Few-NERD 仅 3 epochs。Under-training 直接降低 model convergence → 降低 degeneracy。Few-NERD 的低 degeneracy (10%) 可能部分源自训练不足而非 dataset intrinsic property。这严重削弱 \"degeneracy is dataset-specific\" 和跨数据集 degeneracy-gating 的因果论证。需：(a) 主文披露差异；(b) 解释原因；(c) 补充 5-epoch degeneracy 数据。\n\n**W4. 缺乏可操作的 positive contribution**\n[R2-W3, R1 AGREE — 强共识]\n论文全部 takeaway 是 \"closing the gap requires trained verifiers\"，但不训练 verifier、不提出新 signal。已测试的 remedy 全部失败（entity-token LP, LP×VC, supervised combination, verbalized confidence）。纯诊断性 negative result 论文需要极强 insight novelty 或可操作性来补偿。Few-NERD LP +1.36pp 是 positive result，但被 framing 为诊断证据而非实用方法。建议：(a) reframe LP 在低 degeneracy regime 的成功为 actionable finding；(b) 提供 degeneracy-based decision rule。\n\n### Should-Fix\n\n**W5. 负面结果缺少 power analysis**\n[R1-W3, R2 AGREE]\nSciERC (n=529, 2 seeds) 检测 1pp 效应的 power 约 50-60%。p=0.29 无法区分 \"真无效果\" 和 \"检测不到\"。Few-NERD (n=32,565) 才是 definitive evidence。建议加 post-hoc power analysis 或明确指出 Few-NERD 是 definitive。\n\n**W6. \"Compression is model-intrinsic\" 与 RE free-form 结果矛盾但主文未 qualify**\n[R1-W4, R2 AGREE]\nNER free-form ablation std ratio 0.97 → \"model-intrinsic\"。但 RE free-form +2.35pp (p=0.025) 直接证明 constraints DO compress LP for RE。Abstract/Introduction 中 \"compressed to near-ineffectiveness\" 未限定为 NER-specific。\n\n**W7. em-dash (---) 过度使用（约 90 处），AI 写作风格痕迹**\n[R2-W4, R1 AGREE]\n正文约 35 处，Appendix 约 55 处。平均每段 1-2 个解释性 em-dash。审稿人最敏感的 AI 写作标志。建议正文减至 ≤10 处。\n\n**W8. Abstract 和 Introduction 过度堆砌数字**\n[R2-W5, R1 AGREE]\nAbstract 约 180 words 含 15+ 个具体数字。实验报告风格而非 story-driven。建议保留 3-4 个最关键数字，其余用定性描述。\n\n**W9. Discussion section 过长 (2+ 页, 14 个 sub-topics)**\n[R2-W8, R1 AGREE]\nN-scaling, temperature, verbalized confidence, signal combinations 等 ablation 内容适合移入 Appendix。可释放 ~1 page 用于改善 framing 或增加 constructive contribution。\n\n**W10. Supervised verifier baseline feature space 过于受限**\n[R2-Q4, R1 AGREE]\n5 个 features 中 4 个是 instance-level aggregates，encode 不了 per-sample discriminative information。\"Bottleneck lies in the feature space\" 仅适用于这 5 个 features，不能泛化。\n\n**W11. 与 Yao et al. (2026) 差异化叙述位置不够显著**\n[R2-W6, R1 partial REBUT]\n差异化内容存在但在 Introduction 中不够 upfront。R1 认为差异充分，R2 认为应更显著。共识：Introduction 应更前置差异化。\n\n**W12. Selection 实验 seed coverage 有限**\n[R1-W5, R2 partial REBUT]\nQE 仅 1 seed，selection 仅 2 seeds。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。R2 反驳：n=32,565 的 within-seed power 极高。共识：training seed stochasticity 的影响虽合理推断为小（multi-seed stability σ≤0.026），但严格来说未被验证。\n\n### Minor\n\n**M1.** Abstract 中 MBR 缩写未展开 [R2-M2]\n**M2.** Table 3 EM/VC 无 p 值未解释（方向为负）[R2-M3]\n**M3.** Figure 3 \"~15%\" degeneracy threshold 缺乏精确定义 [R2-M4]\n**M4.** SJ normalizer claim \"Δρ<0.01\" 应改为 \"|Δρ|≤0.009\" [R1-W7]\n**M5.** Table 3 vs Table 4 greedy F1 不一致（gold-filtered vs full-set），footnote 存在但容易被忽略 [R1-W8]\n**M6.** \"leverage\" 用词 (Appendix L235) [R2-M1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **实验执行质量高**: 统计方法、ablation 覆盖、负面结果处理均远超平均。[R1 3.5 + R2 4 Soundness]\n2. **Degeneracy-gating 因果证据不足**: n=3 datasets, pooled granularity, Few-NERD epoch confound, LoRA rank=8 混淆变量。\n3. **缺乏 positive contribution**: 诊断有深度但无可操作方法。多种 remedy 已测试（全 negative），这有价值但降低了 excitement。\n4. **写作可改进**: em-dash 过多、数字堆砌、Discussion 过长。\n5. **Reproducibility 高**: 模型/数据集公开，超参数详细，承诺 code release。\n\n## Reviewer Divergence [分歧记录]\n\n1. **Overall score**: R1 = Borderline Accept (3.5/5), R2 = Borderline Reject (3.0/5, leaning Findings)\n2. **Excitement**: R1 = 3.5, R2 = 2.5\n3. **分歧本质**: 纯诊断性论文（strong execution + negative result + diagnostic value）是否满足 EMNLP main conference 门槛。R1 认为 \"correlation-selection gap\" 概念化 + 三层诊断的系统性 + Few-NERD positive result 足以构成 borderline accept；R2 认为核心发现的 novelty（partially definitional + partially known phenomena）和 actionability 不够 main conference，更适合 Findings。\n4. **Degeneracy as trivial correlate**: R2 初始 claim degeneracy = model success 的 trivial correlate；R1 用 Few-NERD (75% F1, 10% degen) 和 4B/8B 对比反驳，证明 degeneracy 不完全是 capability proxy。R2 在交叉中部分接受但维持 deeper point：论文需 disentangle degeneracy 的多个 driver。\n\n---\n\n## Questions (需要作者澄清)\n\n**Q1.** LoRA rank=8 下 LP 的 median within-instance range、tied fraction、pooled within-instance ρ(LP,F1) 是多少？[R1-Q1, R2 AGREE — 关键缺失数据]\n\n**Q2.** Few-NERD 训练为何仅 3 epochs？5 epochs 下的 degeneracy rate 和 LP selection 效果是多少？[R1-Q2, R2 AGREE — 关键 confound]\n\n**Q3.** Within-instance SJ-F1 ρ=0.52 的 distribution 如何？多少比例的 non-degenerate instances 有 ρ<0？[R1-Q4, R2 partial concern]\n\n**Q4.** Entity-type-level degeneracy-LP gain 分析是否控制了 entity type frequency 或 average entity count per sentence 作为 confound？[R1-Q5, R2 AGREE]\n\n**Q5.** Supervised verifier 加入 token-level features（如 per-entity LP 分布统计）能否 close gap？[R2-Q4, R1 AGREE]\n\n**Q6.** Few-NERD 低 degeneracy 是否主要因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 函数。[R2-Q1]\n\n---\n\n## Missing References\n\n1. **Byerly & Khashabi (2024)** \"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\" — SC 中 correlated errors 导致失败的分析 [R2-W7; R1 质疑此引用是否存在，需作者核实]\n2. **Diverse Beam Search** (Vijayakumar et al., 2016) — diversity-promoting decoding 作为 degeneracy 的潜在缓解 [R2]\n3. **CRF-based calibration 经典工作** — structured prediction uncertainty estimation [R2]\n4. **Zhang et al. (2024) DeepMind test-time compute scaling** — fine-tuned model diversity collapse 与 test-time compute 关系 [R1; R2 指出 Snell et al. 2025 已覆盖 ICLR 版本]\n\n---\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n**Confidence: 4/5**\n\n这是一篇实验工作量大、统计处理严谨、ablation 覆盖度高的论文。\"Correlation-selection gap\" 概念对社区有 guidance 价值，三层诊断结构清晰，Few-NERD 的 positive result 证明 LP selection 在低 degeneracy regime 可行。\n\n但论文面临以下核心问题：\n1. **因果证据薄弱**：degeneracy-gating 的跨数据集证据仅 n=3 且 Few-NERD 存在 epoch confound，LoRA ablation 有混淆变量\n2. **Novelty/actionability 不足**：三层诊断中第一层 (instance-level limitation) 是 definitional，第二层 (degeneracy) 与已知 diversity collapse 有重叠，第三层 (LP compression) 是 specific but limited impact。缺乏可操作的 positive method contribution\n3. **写作问题**：em-dash 过多 (~90)、Abstract 数字堆砌、Discussion 过长\n\n**投稿建议**: 介于 Main Conference 和 Findings 之间。如果能在 rebuttal/revision 中：(a) 补充 LoRA rank=8 LP compression 数据，(b) 澄清 Few-NERD epoch confound（最好补 5-epoch 数据），(c) reframe LP 在低 degeneracy regime 的成功为 actionable finding 并提供 decision rule，(d) 大幅减少 em-dash 和 Abstract 数字，可升至 weak accept。否则建议 Findings。\n\n---\n\n## Detailed Comments (逐节)\n\n### Abstract\n- 信息密度过高，15+ 数字在 ~180 words 中\n- \"Correlation-selection gap\" 首次出现时需一句释义\n- \"Compressed to near-ineffectiveness\" 未限定 NER-specific\n- MBR 缩写未展开\n\n### Introduction\n- 叙事线清晰（self-consistency success → NER structural challenge → gap → diagnosis）\n- Contribution 2 和 3 有重叠（degeneracy 既是 gap 原因又是 regime boundary）\n- 与 Yao et al. 的差异化位置不够 upfront\n- Contribution list 中 by-construction limitation 应标注为 conceptual note 而非 empirical finding\n\n### Method (Section 3)\n- 形式化清晰正确，5 个 signal 定义完整\n- FK adaptation 有 independence test 支撑（Appendix）\n- SJ 分母用 max 非标准 Jaccard，footnote 有说明但 naming 可改进\n\n### Experiments (Section 4)\n- 数据集选择合理且角色分工清晰\n- 训练细节充分（Table 7），但 Few-NERD 3 epochs 需在主文披露\n- vLLM 版本号未报告\n- Table 3 vs Table 4 evaluation protocol 差异需更显著标注\n\n### Discussion (Section 5)\n- 内容丰富但过长，14 个 sub-topics 可压缩\n- \"Why the gap exists\" 是核心，degeneracy + LP compression 分析有力\n- Entity-token LP ablation (negative result) 有价值\n- Signal combination + supervised verifier 确认 feature space bottleneck\n- Practical considerations 实用（N=8 suffices for QE）\n\n### Conclusion\n- 过于简短（10 行），未讨论 broader implications\n- 建议增加 practical guidance summary\n\n### Limitations\n- 全面且诚实\n- 建议补充：power analysis limitation、Few-NERD epoch confound\n\n---\n\n## 官方维度打分（ACL ARR Review Form 综合）\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 4/5 | 3.75/5 |\n| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |\n| Reproducibility | 4/5 | 4/5 | 4/5 |\n| Overall | 3.5/5 | 3/5 | 3.25/5 |\n\n---\n\n## Issue Tracker 更新摘要 (Round 17)\n\n**新增 issues**: 6 个\n- R17-W1 [critical]: LoRA rank=8 LP compression 数据缺失\n- R17-W2 [critical]: Few-NERD 3 epochs confound 未在主文披露\n- R17-W3 [warning]: em-dash 过度使用 (~90 处)\n- R17-W4 [warning]: Discussion 过长\n- R17-W5 [warning]: Supervised verifier 结论过度泛化\n- R17-M1/M2/M3 [info]: 缩写、p 值、threshold 精度\n\n**跨轮次 recurring issues 仍 open**: R0-C3, R3-W2, R12-N1, R13-W2, R14-W1, R16-N1 等\n**跨轮次已解决 issues**: 34 个（Rounds 0-15）",
    "project": "struct_self_consist_ie",
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

_source line 1716 · 2026-05-17T07:27:16.722386+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3977
}
```

</details>

---


### Tool call

_source line 1717 · 2026-05-17T07:27:35.481169+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '检查论文资料完整性和 EMNLP 2026 投稿要求'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 人数和侧重点'}, {'content': 'Step 0.6: 外部审稿线检查', 'status': 'completed', 'activeForm': '检查外部审稿配置（未配置，跳过）'}, {'content': 'Step 1: Round 1 独立审稿 — 收集结果', 'status': 'completed', 'activeForm': '收集 Reviewer 1 和 Reviewer 2 审稿结果'}, {'content': 'Step 2: 交叉分享 — Reviewer 互评', 'status': 'completed', 'activeForm': '交叉分享审稿意见并收集回应'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断审稿共识是否收敛'}, {'content': 'Step 4: 汇总报告并投递', 'status': 'completed', 'activeForm': '汇总审稿报告并投递给 Research Director'}]"
  }
}
```

</details>

---


### Tool result

_source line 1718 · 2026-05-17T07:27:35.531763+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1719 · 2026-05-17T07:27:46.291151+00:00_

Round 17 审稿完成。

**审稿结果摘要**：

- **Overall Score: Borderline (3.25/5)**，介于 Main Conference 和 Findings 之间
- **R1**: Borderline Accept (3.5/5) — 高执行质量 + 诊断价值
- **R2**: Borderline Reject (3.0/5) — novelty/actionability 不足

**4 个 Critical Must-Fix**：
1. Degeneracy-gating 跨数据集因果证据薄弱 (n=3)
2. LoRA rank=8 LP compression 数据缺失，无法支撑 "necessary but not sufficient"
3. Few-NERD 3 epochs confound 未在主文披露
4. 缺乏可操作的 positive contribution

**核心分歧**：纯诊断性高执行质量论文是否满足 EMNLP 主会议门槛（R1 认为 borderline yes，R2 认为 no）。

审稿报告和 Issue Tracker 已投递给 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1720 · 2026-05-17T07:27:48.821965+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：我与 R1 在方法论问题上高度共识（degeneracy 因果推断薄弱、LoRA ablation 混淆变量、Few-NERD 3 epochs confound），但在 excitement 评分上我更保守（2.5 vs R1 的 3.5）——因为论文缺乏任何 positive method contribution。

Few-NERD 3 epochs 的发现（Appendix line 1087 vs 主文声称的 uniform 5 epochs）是一个重要的 disclosure 问题，可能削弱整个 degeneracy-gating narrative 的跨数据集对比基础。

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

_source line 1721 · 2026-05-17T07:28:01.256399+00:00_

审稿流程已全部完成。

**Round 17 审稿总结：**

- **综合评分**: Borderline (3.25/5)
- **R1**: Borderline Accept (3.5/5) / **R2**: Borderline Reject (3.0/5, leaning Findings)
- 审稿报告已投递给 Research Director，Issue Tracker 已同步更新

**关键共识问题（4 个 critical + 8 个 should-fix + 6 个 minor）：**
1. Degeneracy-gating 跨数据集因果证据薄弱 (n=3)
2. LoRA rank=8 下 LP compression 数据缺失，"necessary but not sufficient" claim 无法验证
3. Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露，confound degeneracy 比较
4. 缺乏可操作的 positive contribution

**核心分歧（未解决）：** 纯诊断性论文（strong execution + negative result）是否满足 EMNLP main conference 门槛。R1 认为 borderline 足够，R2 认为更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 140

## Round 140

74 recorded events


### User

_source line 1722 · 2026-05-18T01:26:37.668517+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference Long Paper
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

_source line 1723 · 2026-05-18T01:26:46.045722+00:00_

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

_source line 1724 · 2026-05-18T01:26:46.096770+00:00_

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

_source line 1725 · 2026-05-18T01:26:50.965646+00:00_

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

_source line 1726 · 2026-05-18T01:26:50.966154+00:00_



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

_source line 1727 · 2026-05-18T01:26:54.931817+00:00_

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

_source line 1728 · 2026-05-18T01:26:55.735220+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (128 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_029a** (failed): Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific. ← 基于 ft_002_v2\n  [server_diagnostic_exp029](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_029a/report/server_diagnostic_1a84e4.md)\n- **exp_029b** (failed): Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets. ← 基于 ft_002_v2\n- **exp_028_fewnerd_5epoch** (negative): Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\n\n## 趋势\n成功 74 / 负向 26 / 失败 6 / 共 128\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\n\n## 告警\n- ft_002: 已被终止 — unknown\n- mvp_pilot_002: 训练失败 — unknown\n- exp_007_ner_llama: 已被终止 — unknown\n- exp001_seed123: 已被终止 — unknown\n- exp001_seed456: 已被终止 — unknown\n- 
…[truncated 1005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1729 · 2026-05-18T01:26:55.785961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1730 · 2026-05-18T01:26:55.786425+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 1731 · 2026-05-18T01:27:00.806307+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
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
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1732 · 2026-05-18T01:27:00.907263+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_g
…[truncated 650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1733 · 2026-05-18T01:27:05.025144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1734 · 2026-05-18T01:27:05.075846+00:00_

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

_source line 1735 · 2026-05-18T01:27:11.048639+00:00_

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

_source line 1736 · 2026-05-18T01:27:11.902221+00:00_

1	\begin{abstract}
2	Self-consistency yields large gains on discrete-answer tasks, but named entity recognition (NER) produces \textit{sets} of entities with partial overlap, where no majority vote analog exists.
3	We evaluate five confidence signals (four instance-level, one per-sample log-probability [LP]) for quality estimation and sample selection on four NER benchmarks using 4B\textendash 8B models.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38), supporting selective prediction.
5	Quality estimation does not translate to selection, however: despite ${\sim}$13~pp oracle headroom, no signal consistently outperforms greedy decoding.
6	The gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection fails because instance degeneracy (14\textendash 47\% identical outputs) eliminates headroom; and LP requires two jointly necessary conditions: low instance degeneracy, and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
7	When both conditions are met, LP achieves significant gains ($+1.36$~pp at 14\% degeneracy, $p{<}0.001$); when either is violated, selection fails.
8	Degeneracy is the dominant bottleneck, controllable via temperature and training budget; in the low-degeneracy regime, LP scales with sample count ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
9	Closing the gap for structural signals likely requires learned per-sample scoring.
10	\end{abstract}
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 1737 · 2026-05-18T01:27:11.952819+00:00_

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

_source line 1738 · 2026-05-18T01:27:12.405468+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency (majority voting over multiple samples) yields large gains on discrete-answer reasoning \citep{wang2023selfconsistency}, and test-time compute scaling has emerged as a complementary axis to model scaling \cite{snell2025scaling, brown2024monkeys}.
4	But named entity recognition (NER) poses a structurally different challenge: the output is a \textit{set} of entities, two samples may extract overlapping but non-identical sets, and there is no obvious majority to vote on.
5	
6	Prior work on confidence estimation for LLM-based IE has conflated \textit{quality estimation} (which inputs does the model handle reliably?) with \textit{sample selection} (which of $N$ outputs is best?).
7	Existing self-consistency methods \cite{wang2023selfconsistency, chen2024usc, taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence, an assumption that breaks for entity sets with partial overlap.
8	Unlike \citet{yao2026consistency}, who demonstrate that self-consistency correlates with task accuracy, we investigate \textit{why} this correlation fails to yield selection improvements, diagnosing degeneracy and compression as the two blocking mechanisms.
9	Our experiments use fine-tuned models, the dominant deployment paradigm for production NER, and separate quality estimation from best-of-$N$ selection.
10	
11	A methodological premise structures our analysis: four of five signals (SJ, VC, FK, EM) are instance-level aggregates that by design assign identical scores to all $N$ candidates for a given input; only log-probability (LP) is natively per-sample.
12	These signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82; Figure~\ref{fig:overview}), supporting selective prediction and error flagging.
13	Yet quality estimation does not translate to structural selection, a disparity we term the \textbf{correlation-selection gap} (
…[truncated 3530 chars]

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

_source line 1739 · 2026-05-18T01:27:12.405866+00:00_

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

_source line 1740 · 2026-05-18T01:27:12.908357+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency \cite{wang2023selfconsistency} improves reasoning via majority voting; extensions handle free-form text \cite{chen2024usc, thirukovalluru2024atomic, manakul2023selfcheckgpt}.
5	Test-time scaling studies \cite{snell2025scaling, brown2024monkeys} and reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty, kim2026reasc, wang2025rankedvoting, oh2026latentsc} all rely on answer-level agreement; \citet{feng2025optimal} and \citet{wang2025make} adapt to difficulty-aware settings; \citet{li2025llms} propose generative self-aggregation for IE but focus on fusion rather than selection.
6	We extend self-consistency to set-valued structured outputs and identify the correlation-selection gap.
7	
8	\paragraph{Consistency for structured IE.}
9	\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we show correlation is necessary but not sufficient, diagnosing degeneracy and compression as blocking mechanisms.
10	Our experiments use fine-tuned models, where degeneracy is most pronounced and is modulated by task structure and training convergence (Appendix~\ref{app:epoch_confound}).
11	CoCoA \cite{vashurin2025cocoa} fuses confidence with consistency for QA/summarization; our supervised verifier baseline (\S\ref{sec:robustness_main}) suggests combination strategy is not the bottleneck.
12	Earlier work on confidence for structured prediction \cite{culotta2004confidence, mejer2010confidence, fomicheva2020unsupervised} establishes the paradigm we extend to set-valued outputs.
13	Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie, li2023codeie, wadhwa2023revisiting} and constrained decoding \cite{willard2023guided, park2024grammar, schall2025hidden, yun2025price}.
14	
15	\paragraph{Uncertainty estimation and MBR decoding.}
16	Surveys cover confidence estimation \cite{geng2024confidence}, uncer
…[truncated 1575 chars]

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

_source line 1741 · 2026-05-18T01:27:12.908757+00:00_

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

_source line 1742 · 2026-05-18T01:27:13.360686+00:00_

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
…[truncated 2976 chars]

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

_source line 1743 · 2026-05-18T01:27:13.361107+00:00_

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

_source line 1744 · 2026-05-18T01:27:13.813379+00:00_

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
…[truncated 11384 chars]

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

_source line 1745 · 2026-05-18T01:27:13.813763+00:00_

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

_source line 1746 · 2026-05-18T01:27:14.316385+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Implications for practitioners.}
4	All signals achieve positive quality estimation across non-collapsed datasets (LP $\rho{=}0.42$ on Few-NERD, VC $\rho{=}0.38$ on SciERC, EM AUROC${=}0.82$ on CoNLL), with rankings stable across model families and a 4B ablation (Table~\ref{tab:scale_ablation}).
5	For selection, LP achieves significant gains only when both conditions are met ($+1.36$~pp on Few-NERD, $p{<}0.001$; Table~\ref{tab:fewnerd}); structural signals uniformly degrade selection.
6	RE signal rankings are in Appendix~\ref{app:re_extension}.
7	
8	\paragraph{Why the gap exists.}
9	Two mechanisms block selection: \textit{instance degeneracy} (consensus-proximity) and \textit{weak LP-quality alignment} (per-sample).
10	Within non-degenerate instances, MBR utility \cite{eikema2022sampling} correlates positively with F1 (SJ median $\rho{=}0.524$) and closes 23--41\% of the oracle gap, but 17.8\% (SciERC) to 47.4\% (CoNLL) of instances produce identical F1 across all samples, eliminating headroom entirely (Table~\ref{tab:degeneracy}).
11	Degeneracy is determined by the interplay of task structure, model architecture, and training convergence (Appendix~\ref{app:epoch_confound}); cross-model evidence (LLaMA 89.2\% vs.\ Qwen 47.4\% on CoNLL; Table~\ref{tab:cross_selection}) reinforces the pattern.
12	LP is severely compressed (median range 0.041 nats; Table~\ref{tab:logprob_ties}), with pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$.
13	
14	\paragraph{Non-tied subset and $N$-scaling.}
15	Where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), within-instance $\rho$ rises to 0.39 and LP selection yields $+2.9$~pp ($p{=}0.004$, survives Bonferroni; Table~\ref{tab:nontied_main}).
16	LP scales with $N$ in the low-degeneracy regime ($+0.52$~pp from $N{=}8$ to 16 on Few-NERD, $p{=}0.003$; \S\ref{sec:fewnerd}); on SciERC, even $N{=}32$ captures less than 5\% of headroom (Table~\ref{tab:n_scaling_
…[truncated 3549 chars]

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

_source line 1747 · 2026-05-18T01:27:14.316783+00:00_

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

_source line 1748 · 2026-05-18T01:27:15.320879+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We evaluate five confidence signals for quality estimation and sample selection in LLM-based NER across four benchmarks spanning a difficulty gradient.
4	All signals achieve reliable quality estimation ($\rho$ up to 0.38 on the primary test bed, 0.42 on Few-NERD; AUROC up to 0.82), supporting selective prediction and error flagging.
5	However, quality estimation does not translate to sample selection, and the gap has a three-layer structure: four instance-level signals cannot rank candidates by construction; MBR selection with well-aligned utility ($\rho{=}0.52$) fails because instance degeneracy (14\textendash 47\%) collapses the candidate pool; and LP, the sole per-sample signal, requires two jointly necessary conditions: low degeneracy and adequate LP-quality alignment ($\rho \gtrsim 0.3$).
6	LP selection succeeds when both conditions are met: at 13.8\% degeneracy with strong alignment ($\rho{\approx}0.5$; Few-NERD), LP achieves $+1.36$~pp ($p{<}0.001$); at 17.8\% with weak alignment ($\rho{\approx}0.24$; SciERC), $+0.42$~pp ($p{=}0.091$); at 47.4\% (CoNLL), LP fails.
7	In the low-degeneracy regime, LP selection scales with sample budget ($+0.52$~pp from $N{=}8$ to 16, paired $p{=}0.003$).
8	Structural signals fail uniformly regardless of degeneracy, and supervised combination of all five signals cannot close the oracle gap; the bottleneck lies in the signal space accessible to unsupervised aggregation, not in the combination method.
9	Whether these patterns persist at 70B+ scales remains open.
10	Closing the gap for structural signals requires content-aware verifiers that examine output semantics \cite{cobbe2021verifiers}; LP provides a lightweight baseline when both degeneracy and alignment conditions are met.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 1749 · 2026-05-18T01:27:15.372075+00:00_

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

_source line 1750 · 2026-05-18T01:27:15.472943+00:00_

1	Our evaluation covers four NER datasets; an exploratory RE extension on SciERC is reported in Appendix~\ref{app:re_extension} but generalization to other RE benchmarks remains unvalidated.
2	We cover 4B\textendash 8B scale; whether the gap holds for 70B+ models or closed-source APIs is untested. Larger models may produce more diverse samples.
3	We do not train a verifier, leaving unknown how much oracle headroom a supervised approach could recover.
4	
5	We evaluate at $N{=}8$ (primary) and $N{=}16$; behavior at larger sample sizes is unknown (Appendix~\ref{app:n_scaling}).
6	The free-form ablation covers SciERC NER and CoNLL NER with one model; RE free-form results are in Appendix~\ref{app:re_extension}.
7	Qwen3-8B's SciERC checkpoint used empty \texttt{&lt;think>&lt;/think>} blocks; a three-part analysis rules out this confound (Appendix~\ref{app:thinking_token}).
8	LP compression worsens on easy datasets at lower temperature (CoNLL tied fractions reach 95.8\% at $T{=}0.7$); whether reduced temperature translates to selection gains remains untested.
9	We tested verbalized confidence \cite{tian2023calibration} as a second per-sample signal; it exhibits severe overconfidence (mean 8.58/10 on SciERC, 9.24/10 on CoNLL) and yields the weakest QE and selection among all signals (Appendix~\ref{app:verbalized_confidence}).
10	Ad-hoc LP${\times}$VC combinations yield at most $+0.2$~pp over greedy (not significant; \S\ref{sec:discussion}); whether \textit{learned} combinations could close the gap remains open.
11	The $\varepsilon{=}0.05$ threshold used for tied/non-tied LP stratification is a post-hoc exploratory choice; while selection F1 is stable across $\varepsilon \in [0, 0.2]$ (Appendix~\ref{app:epsilon_robustness}), the specific subset gains should be interpreted as characterizing the compression phenomenon rather than as a tuned selection strategy.
12	We tested one remedy for LP compression (entity-token-only LP, excluding format/schema tokens) which fails to improve sel
…[truncated 672 chars]

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

_source line 1751 · 2026-05-18T01:27:15.523725+00:00_

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

_source line 1752 · 2026-05-18T01:27:15.775247+00:00_

File content (34318 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1753 · 2026-05-18T01:27:24.068012+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,request_external_review,mcp__agent-ml-research__request_external_review",
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
    "query": "select:WebSearch,request_external_review,mcp__agent-ml-research__request_external_review",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 1754 · 2026-05-18T01:27:24.118620+00:00_



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

_source line 1755 · 2026-05-18T01:27:29.352835+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
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
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 1756 · 2026-05-18T01:27:30.407471+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
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
    "file": "decisions.yaml",
    "max_chars": "5000"
  }
}
```

</details>

---


### Tool call

_source line 1757 · 2026-05-18T01:27:31.714002+00:00_

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

_source line 1758 · 2026-05-18T01:27:40.648269+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"}]

Based on the search results, here are the key submission guidelines and author instructions for EMNLP 2026:

## Submission Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Submission Process

Papers are submitted through the ACL Rolling Review (ARR) system. Authors submit articles to ARR, where submissions receive reviews and meta-reviews from ARR reviewers and action editors; Authors commit their rev
…[truncated 2426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 11295
}
```

</details>

---


### Tool result

_source line 1759 · 2026-05-18T01:27:40.649007+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 130\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 3529 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 10241
}
```

</details>

---


### Tool result

_source line 1760 · 2026-05-18T01:27:40.699642+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 8985
}
```

</details>

---


### Tool call

_source line 1761 · 2026-05-18T01:27:50.238700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR submission format page limit template anonymous review guidelines",
  "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
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
    "query": "EMNLP 2026 ARR submission format page limit template anonymous review guidelines",
    "allowed_domains": "['2026.emnlp.org', 'aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 1762 · 2026-05-18T01:27:50.439877+00:00_

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

_source line 1763 · 2026-05-18T01:27:50.490529+00:00_

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


### Tool result

_source line 1764 · 2026-05-18T01:27:56.614929+00:00_

Web search results for query: "EMNLP 2026 ARR submission format page limit template anonymous review guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"ACL Policies for Review and Citation - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policies_for_Review_and_Citation"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's the information about EMNLP 2026 ARR submission requirements:

## Page Limits

Short papers have a 4-page limit and long papers have an 8-page limit, excluding ethical considerations and limitations.

## Anonymity and Review Guidelines

The reviewing process will be double-blind, with reviewers not seeing authors, nor will authors see reviewers. Howev
…[truncated 994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6376
}
```

</details>

---


### Tool call

_source line 1765 · 2026-05-18T01:28:00.680856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines submission format LaTeX template page limit",
  "allowed_domains": "['aclrollingreview.org']"
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
    "query": "ACL Rolling Review 2026 author guidelines submission format LaTeX template page limit",
    "allowed_domains": "['aclrollingreview.org']"
  }
}
```

</details>

---


### Tool call

_source line 1766 · 2026-05-18T01:28:01.283812+00:00_

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

_source line 1767 · 2026-05-18T01:28:01.686526+00:00_

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
15	  severity: critical
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
76	  summary: "Cross-mod
…[truncated 37150 chars]

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


### Tool result

_source line 1768 · 2026-05-18T01:28:07.208640+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines submission format LaTeX template page limit"

Links: [{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on my search results, here is information about ACL Rolling Review 2026 author guidelines for submission format, LaTeX tem
…[truncated 1222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6527
}
```

</details>

---


### Tool call

_source line 1769 · 2026-05-18T01:28:23.338819+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
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
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1770 · 2026-05-18T01:28:24.744837+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

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


### Tool call

_source line 1771 · 2026-05-18T01:28:24.896017+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1772 · 2026-05-18T01:28:24.947551+00:00_

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
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
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
47	\quad FK & $
…[truncated 4982 chars]

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

_source line 1773 · 2026-05-18T01:28:35.771146+00:00_

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

_source line 1774 · 2026-05-18T01:28:35.821843+00:00_

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

_source line 1775 · 2026-05-18T01:28:42.346026+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
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
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
  }
}
```

</details>

---


### Tool result

_source line 1776 · 2026-05-18T01:28:42.396748+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.&lt;/tool_use_error>

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

_source line 1777 · 2026-05-18T01:28:47.369325+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/project_config*",
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
    "pattern": "**/project_config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 1778 · 2026-05-18T01:28:47.420073+00:00_

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

_source line 1779 · 2026-05-18T01:28:52.057222+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "files_with_matches"
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
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 1780 · 2026-05-18T01:28:52.309112+00:00_

Found 14 files
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_group_oc_3897c2857f11615119e277e820eae311_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T113255/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_14.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_10.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_523053f5a039428dc15666668fa856b3_20260515T183358_453446.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T152516_433719.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260515T102033_395761.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1781 · 2026-05-18T01:28:57.025311+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review.*enabled|paperreview_ai.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "glob": "CLAUDE.md"
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
    "pattern": "external_review.*enabled|paperreview_ai.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "glob": "CLAUDE.md"
  }
}
```

</details>

---


### Tool result

_source line 1782 · 2026-05-18T01:28:57.076435+00:00_

CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1783 · 2026-05-18T01:29:03.353242+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/AGENTS.md",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/AGENTS.md",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1784 · 2026-05-18T01:29:03.403851+00:00_

1	## 当前项目
2	当前绑定项目：**struct_self_consist_ie**
3	
4	## 按需查阅
5	- 项目配置：`load_project_config("struct_self_consist_ie")` 或 `load_project_config("struct_self_consist_ie", section="execution")`
6	- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）
7	- 路线图：`read_roadmap()` 读取研究方向和短期任务
8	- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/`（写文件后用 `register_artifact` 注册）
9	
10	## Worker 操作规范
11	
12	### paper-writing-norms
13	
14	# 论文写作风格规范
15	
16	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
17	
18	---
19	
20	## 一、总体写作哲学
21	
22	### 1.1 故事驱动，不是数据堆砌
23	
24	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
25	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
26	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
27	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
28	
29	### 1.2 主线统一性
30	
31	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
32	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
33	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
34	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
35	
36	### 1.3 专有名词必须有定义
37	
38	- 首次出现的专有名词/缩写必须给出完整定义和解释
39	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
40	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
41	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
42	
43	### 1.4 写作前必读同类优秀论文
44	
45	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
46	- 重点学：
47	  - Abstract 怎么用最少篇幅讲完故事
48	  - Introduction 怎么从大问题切入到具体贡献
49	  - Related Work 怎么 positioning 自己（不是 survey）
50	  - Table/Figure 怎么压缩信息密度

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

_source line 1785 · 2026-05-18T01:29:20.447723+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
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
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 1786 · 2026-05-18T01:29:20.498367+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_lp_range_cdf.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_degeneracy_lp_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

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

_source line 1787 · 2026-05-18T01:29:30.078881+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status",
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
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1788 · 2026-05-18T01:29:30.129440+00:00_



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

_source line 1789 · 2026-05-18T01:29:35.305276+00:00_

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

_source line 1790 · 2026-05-18T01:29:35.355816+00:00_

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


### Tool call

_source line 1791 · 2026-05-18T01:30:13.364292+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 18 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, `[review]` 选项, 8 页正文 + unlimited references + appendix\n- **匿名规则**: Double-blind\n- **附录**: 允许，参与审稿\n\n### 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `docs/paper/sections/` 下\n- PDF: `docs/paper/main.pdf`\n\n### 审查重点\n\n请重点审查以下方面:\n\n1. **统计分析严谨性**:\n   - SciERC 负面结果 (n=529, 2 seeds) 的统计效力是否充分？p=0.29 能否区分\"真无效果\"和\"检测不到\"？\n   - Cross-dataset degeneracy gradient 仅 3 个 dataset-level 数据点，因果推断是否合理？\n   - Entity-type-level correlation (n=8, ρ=-0.881, p=0.004) 的 independence 假设是否成立（共享 model/pipeline）？\n   - Fisher combined p (2-seed) / sign test 效力问题\n   - Bonferroni 校正 scope 是否恰当？\n\n2. **实验设计 confound 控制**:\n   - Few-NERD 训练 3 epochs vs 其他数据集 5 epochs：这个训练差异是否 confound 了 degeneracy 的跨数据集比较？\n   - LoRA rank=8 ablation 同时改变了 model capacity 和 degeneracy，能否做 clean causal attribution？\n   - Supervised verifier baseline 使用 5 个 scalar features (4 个 instance-level) 是否过于受限？\n\n3. **方法定义清晰度**:\n   - \"Instance degeneracy\" 的操作性定义是否精确一致？\n   - LP compression 的 mechanistic explanation 是否充分？\n   - ε=0.05 threshold 的 justification\n\n4. **数值一致性**:\n   - Abstract/Figure 1 中 ρ=0.42 vs Table 1 max=0.379 的矛盾\n   - Table 4 (full-set) vs Table 2 (gold-filtered) 的 evaluation protocol 差异是否清楚标注？\n   - Random (0.610) vs Greedy (0.645) 差距来源\n\n### 历史 open issues (供参考)\n以下问题在上轮(R17)仍为 open/in_progress，请在审查中确认其当前状态:\n- R0-C3: Selection gap 仅 SciERC 单数据集 (critical)\n- R16-N1: Degeneracy-gating monotonic claim 仅 3 数据点 (critical)\n- R17-W1: LoRA rank=8 LP compression 数据缺失 (critical)\n- R17-W2: Few-NERD 3 epochs confound (critical)\n- R14-W1: Fisher combined p 统计效力 (critical)\n- R14-M1: Random vs Single 差距来源 (critical)\n\n请按 ARR reviewer form 格式输出: Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment (score + confidence)",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "18"
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
    "text": "## Round 18 审稿任务 — Reviewer 1\n\n**你的侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, `[review]` 选项, 8 页正文 + unlimited references + appendix\n- **匿名规则**: Double-blind\n- **附录**: 允许，参与审稿\n\n### 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `docs/paper/sections/` 下\n- PDF: `docs/paper/main.pdf`\n\n### 审查重点\n\n请重点审查以下方面:\n\n1. **统计分析严谨性**:\n   - SciERC 负面结果 (n=529, 2 seeds) 的统计效力是否充分？p=0.29 能否区分\"真无效果\"和\"检测不到\"？\n   - Cross-dataset degeneracy gradient 仅 3 个 dataset-level 数据点，因果推断是否合理？\n   - Entity-type-level correlation (n=8, ρ=-0.881, p=0.004) 的 independence 假设是否成立（共享 model/pipeline）？\n   - Fisher combined p (2-seed) / sign test 效力问题\n   - Bonferroni 校正 scope 是否恰当？\n\n2. **实验设计 confound 控制**:\n   - Few-NERD 训练 3 epochs vs 其他数据集 5 epochs：这个训练差异是否 confound 了 degeneracy 的跨数据集比较？\n   - LoRA rank=8 ablation 同时改变了 model capacity 和 degeneracy，能否做 clean causal attribution？\n   - Supervised verifier baseline 使用 5 个 scalar features (4 个 instance-level) 是否过于受限？\n\n3. **方法定义清晰度**:\n   - \"Instance degeneracy\" 的操作性定义是否精确一致？\n   - LP compression 的 mechanistic explanation 是否充分？\n   - ε=0.05 threshold 的 justification\n\n4. **数值一致性**:\n   - Abstract/Figure 1 中 ρ=0.42 vs Table 1 max=0.379 的矛盾\n   - Table 4 (full-set) vs Table 2 (gold-filtered) 的 evaluation protocol 差异是否清楚标注？\n   - Random (0.610) vs Greedy (0.645) 差距来源\n\n### 历史 open issues (供参考)\n以下问题在上轮(R17)仍为 open/in_progress，请在审查中确认其当前状态:\n- R0-C3: Selection gap 仅 SciERC 单数据集 (critical)\n- R16-N1: Degeneracy-gating monotonic claim 仅 3 数据点 (critical)\n- R17-W1: LoRA rank=8 LP compression 数据缺失 (critical)\n- R17-W2: Few-NERD 3 epochs confound (critical)\n- R14-W1: Fisher combined p 统计效力 (critical)\n- R14-M1: Random vs Single 差距来源 (critical)\n\n请按 ARR reviewer form 格式输出: Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment (score + confidence)",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "18"
  }
}
```

</details>

---


### Tool result

_source line 1792 · 2026-05-18T01:30:34.630463+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 21266
}
```

</details>

---


### Tool call

_source line 1793 · 2026-05-18T01:30:34.782396+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 18 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 写作质量 + 完整性\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, `[review]` 选项, 8 页正文 + unlimited references + appendix\n- **匿名规则**: Double-blind\n- **附录**: 允许，参与审稿\n\n### 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `docs/paper/sections/` 下\n- PDF: `docs/paper/main.pdf`\n\n### 审查重点\n\n请重点审查以下方面:\n\n1. **新颖性与贡献评估**:\n   - 与 Yao et al. (2026) 的增量贡献是否足够清晰？差异化是否 upfront？\n   - \"Correlation-selection gap\" 概念中，4/5 signals 是 instance-level (selection 失败 by construction) 部分是否 tautological？\n   - 纯诊断性论文缺乏 positive contribution/remedy，是否足以达到 EMNLP main conference 门槛？\n   - Few-NERD LP positive result (+1.36pp) 是否被充分 frame 为 actionable finding？\n\n2. **写作质量与叙事**:\n   - Abstract 是否过度压缩/信息过载？(上轮反馈: 180 words 含 15+ 数字，实验报告风格)\n   - Introduction 叙事线是否连贯？problem → insight → method → validation 结构是否清晰？\n   - \"correlation-selection gap\" 术语首次使用时是否有操作性定义？\n   - Discussion section 长度是否合理？(上轮反馈: 2+ 页，14 sub-topics 过多)\n   - AI 写作痕迹: em-dash 使用频率、-ing phrases、过度分段\n\n3. **格式合规**:\n   - 页数是否在 8 页限制内？\n   - ACL 模板选项是否正确 (`[review]`)？\n   - 匿名化是否完整？\n   - 引用格式是否正确？\n   - Limitations / Ethics Statement 是否完整？\n   - Appendix 是否在 bibliography 之后？\n\n4. **Related Work 定位**:\n   - 引用是否充分覆盖: self-consistency, MBR decoding, confidence estimation, structured IE？\n   - 与 MBR 社区已知结论 (Eikema et al.) 的差异化是否清楚？\n   - 是否存在重要遗漏文献？\n\n### 历史 open issues (供参考)\n以下问题在上轮(R17)仍为 open/in_progress，请在审查中确认其当前状态:\n- R3-W2: Gap 概念部分 tautological (critical)\n- R11-W1: 与 Yao et al. 增量贡献定义不够清晰 (warning)\n- R13-W2: Abstract 信息过度压缩 (warning)\n- R12-W1: 纯诊断无 remedy 尝试 (warning)\n- R17-W3: em-dash 使用约 90 处 (warning)\n- R17-W4: Discussion 过长 (warning)\n- R12-N1: rho headline 归因错误 (critical)\n- R16-N2: rho=0.42 数值矛盾 (critical)\n- R14-M3: correlation-selection gap 操作性定义位置 (warning)\n- R11-N3: LP compression intrinsic 措辞被 RE free-form 削弱 (warning)\n\n请按 ARR reviewer form 格式输出: Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment (score + confidence)",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "18"
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
    "text": "## Round 18 审稿任务 — Reviewer 2\n\n**你的侧重**: 新颖性 + 写作质量 + 完整性\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (via ACL Rolling Review May 2026 cycle)\n- **截止日期**: 2026-05-25\n- **格式**: ACL LaTeX 模板, `[review]` 选项, 8 页正文 + unlimited references + appendix\n- **匿名规则**: Double-blind\n- **附录**: 允许，参与审稿\n\n### 论文路径\n- LaTeX 源码: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n- 各 section 在 `docs/paper/sections/` 下\n- PDF: `docs/paper/main.pdf`\n\n### 审查重点\n\n请重点审查以下方面:\n\n1. **新颖性与贡献评估**:\n   - 与 Yao et al. (2026) 的增量贡献是否足够清晰？差异化是否 upfront？\n   - \"Correlation-selection gap\" 概念中，4/5 signals 是 instance-level (selection 失败 by construction) 部分是否 tautological？\n   - 纯诊断性论文缺乏 positive contribution/remedy，是否足以达到 EMNLP main conference 门槛？\n   - Few-NERD LP positive result (+1.36pp) 是否被充分 frame 为 actionable finding？\n\n2. **写作质量与叙事**:\n   - Abstract 是否过度压缩/信息过载？(上轮反馈: 180 words 含 15+ 数字，实验报告风格)\n   - Introduction 叙事线是否连贯？problem → insight → method → validation 结构是否清晰？\n   - \"correlation-selection gap\" 术语首次使用时是否有操作性定义？\n   - Discussion section 长度是否合理？(上轮反馈: 2+ 页，14 sub-topics 过多)\n   - AI 写作痕迹: em-dash 使用频率、-ing phrases、过度分段\n\n3. **格式合规**:\n   - 页数是否在 8 页限制内？\n   - ACL 模板选项是否正确 (`[review]`)？\n   - 匿名化是否完整？\n   - 引用格式是否正确？\n   - Limitations / Ethics Statement 是否完整？\n   - Appendix 是否在 bibliography 之后？\n\n4. **Related Work 定位**:\n   - 引用是否充分覆盖: self-consistency, MBR decoding, confidence estimation, structured IE？\n   - 与 MBR 社区已知结论 (Eikema et al.) 的差异化是否清楚？\n   - 是否存在重要遗漏文献？\n\n### 历史 open issues (供参考)\n以下问题在上轮(R17)仍为 open/in_progress，请在审查中确认其当前状态:\n- R3-W2: Gap 概念部分 tautological (critical)\n- R11-W1: 与 Yao et al. 增量贡献定义不够清晰 (warning)\n- R13-W2: Abstract 信息过度压缩 (warning)\n- R12-W1: 纯诊断无 remedy 尝试 (warning)\n- R17-W3: em-dash 使用约 90 处 (warning)\n- R17-W4: Discussion 过长 (warning)\n- R12-N1: rho headline 归因错误 (critical)\n- R16-N2: rho=0.42 数值矛盾 (critical)\n- R14-M3: correlation-selection gap 操作性定义位置 (warning)\n- R11-N3: LP compression intrinsic 措辞被 RE free-form 削弱 (warning)\n\n请按 ARR reviewer form 格式输出: Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment (score + confidence)",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "18"
  }
}
```

</details>

---


### Tool result

_source line 1794 · 2026-05-18T01:30:36.590071+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1807
}
```

</details>

---


### Assistant

_source line 1795 · 2026-05-18T01:30:42.207214+00:00_

Round 18 审稿任务已分配：
- Reviewer 1（方法/统计）和 Reviewer 2（新颖性/写作）已启动独立审稿
- 等待两位 Reviewer 返回初审意见后进入交叉分享环节

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 141

## Round 141

2 recorded events


### User

_source line 1796 · 2026-05-18T01:35:20.288077+00:00_

[Reviewer 1 审稿意见]:
## Round 18 Review — Reviewer 1 (方法严谨性 + 实验设计 + 统计分析)

### Summary

This paper investigates why self-consistency signals that reliably estimate instance-level quality (QE) for LLM-based NER fail to improve best-of-N sample selection. Five confidence signals are evaluated across four NER benchmarks using 4B-8B models. The paper identifies a "correlation-selection gap" with a three-layer diagnosis: instance-level signals cannot rank candidates by construction; MBR selection fails due to instance degeneracy; and LP (the sole per-sample signal) requires both low degeneracy and adequate alignment. LP succeeds on Few-NERD (+1.36pp, p<0.001) but fails on SciERC (p=0.29) and CoNLL.

---

### Strengths

1. **Well-structured diagnostic framework.** The three-layer decomposition (instance-level limitation → degeneracy → alignment) is clean and helps the reader understand why selection fails at each level. The paper does a good job separating QE from selection as conceptually distinct tasks (Section 2.1, Section 3.3).

2. **Comprehensive ablation coverage.** The paper systematically manipulates temperature (App. §T_ablation), N-scaling (App. §n_scaling_selection), LoRA rank (§5.4), model scale (Table 5), free-form decoding (App. §freeform_ablation), and training epochs (App. §epoch_confound). This breadth strengthens confidence in the robustness of the primary negative findings.

3. **Honest reporting of negative results.** The paper does not overstate LP's utility; it clearly delineates where LP succeeds (Few-NERD, low degeneracy + high alignment) and where it fails, with appropriate statistical caveats.

4. **Strong Few-NERD validation.** The n=32,565 evaluation provides >99% power and yields a tight CI [+1.18, +1.53] for the LP selection gain, making the positive finding on this dataset convincing (Table 3, Appendix §fewnerd).

5. **Entity-type-level granularity.** Table in Appendix §per_type_lp provides per-type decomposition that adds mechanistic insight beyond dataset-level summaries.

---

### Weaknesses

**W1 [Major]** Statistical power of the primary SciERC selection test is insufficient to distinguish "true null" from "underpowered."

- Section 3.3 reports LP +0.2pp (p=0.29) on SciERC (n=529, 2 seeds). The footnote acknowledges ~55% post-hoc power for a 1pp effect. At this power level, P(fail to reject | true effect of 1pp) ≈ 0.45. The paper cannot claim that selection "fails" on SciERC; it can only claim "not detected."
- The paper partially hedges but the framing throughout treats the SciERC negative as established fact rather than inconclusive, inflating the "two necessary conditions" narrative.
- The N-scaling table (App. §n_scaling_selection) shows +0.42pp at N=8 growing to +0.91pp at N=32, suggesting LP may have a real but small effect on SciERC that the 2-seed test cannot detect.
- **Impact**: The three-way gradient (47% → fail, 18% → weak, 14% → success) relies on the middle point being genuinely "weak/null" rather than merely underpowered.
- **Suggestion**: Report minimum detectable effect at 80% power for each configuration. If SciERC at n=529 can only detect ≥2pp, state this explicitly and reframe accordingly.

**W2 [Major]** Cross-dataset degeneracy gradient: causal inference from 3 observational data points is overfit.

- Section 3.4 and Contribution 3 claim "the cross-dataset gradient establishes degeneracy as one condition." Three data points (CoNLL, SciERC, Few-NERD) cannot "establish" anything—any three ordered numbers are trivially monotonic. The datasets differ on ≥5 dimensions simultaneously: degeneracy, LP alignment, task difficulty, schema complexity, training epochs (3 vs 5), and training data size.
- The per-entity-type analysis (n=8, ρ=-0.881) partially addresses this but has its own issues (W3).
- **Impact**: The "monotonic" claim in Figure 2 and Section 3.4 overstates what the evidence supports.
- **Suggestion**: Reframe as "consistent with" rather than "establishes"; explicitly list confounded variables; present the gradient as descriptive evidence corroborated by controlled ablations (LoRA, temperature).

**W3 [Major]** Per-entity-type correlation (n=8, ρ=-0.881, p=0.004): non-independence inflates significance.

- The 8 entity types from a single model on Few-NERD share: (a) same trained weights, (b) same tokenizer/decoding, (c) same temperature, (d) often shared entity mentions across types within the same sentences. The Spearman test assumes independent observations; effective df likely <6.
- **Impact**: The p=0.004 may overstate significance by 5-10x. If true p is ~0.02-0.04, it still suggests a trend but wouldn't survive correction over ~20 comparisons.
- **Suggestion**: Report a permutation test shuffling type labels, or acknowledge non-independence and interpret as suggestive.

**W4 [Major]** Few-NERD 3-epoch training confound: control is incomplete.

- Appendix §epoch_confound shows 5-epoch Few-NERD triples degeneracy (11.1% → 31.3%) and halves LP gains (+1.37pp → +0.62pp). This demonstrates favorable conditions are partly training-induced.
- The 5-epoch model has higher greedy F1 (0.777 vs 0.748), introducing a performance-regime confound. A matched-degeneracy comparison (e.g., SciERC at T=1.2 where degeneracy=12.5% vs Few-NERD at 13.8%) would better isolate alignment as the differentiator.
- **Impact**: Practitioners using standard 5-epoch training would face higher degeneracy; the paper's demonstration of LP success may not generalize to typical training configurations.
- **Suggestion**: Foreground that the 3-epoch model reflects validation-loss early stopping; add the matched-degeneracy cross-dataset comparison.

**W5 [Moderate]** LoRA rank=8 ablation conflates capacity and degeneracy.

- Section 5.4: rank=8 simultaneously reduces capacity and changes training dynamics. The lower alignment (ρ≈0.24) could stem from insufficient capacity rather than evidence for a separate "alignment" condition.
- The temperature ablation (T=1.2: degeneracy 12.5%, ρ=0.225; Table §t_degeneracy) provides cleaner evidence on the same full-rank model and should be foregrounded as the primary argument.
- **Suggestion**: Acknowledge the capacity confound; emphasize temperature as the cleaner manipulation.

**W6 [Moderate]** Supervised verifier baseline tests only recycled features.

- Section 5.4: LR/MLP/RF trained on 5 scalar features that are the same insufficient signals. Concluding "the bottleneck lies in what the signals encode, not how they are aggregated" is valid only for this feature set.
- A verifier with hidden states, attention patterns, or raw text would have fundamentally different capacity.
- **Suggestion**: Scope the conclusion explicitly to "supervised combination of the 5 unsupervised signals" rather than implying supervised approaches in general cannot help.

**W7 [Minor]** Instance degeneracy definition is operationally ambiguous.

- Introduction says "fine-tuned models produce identical outputs for 14–47% of instances" but Table §diversity shows only 11% identical outputs on SciERC. The operational definition is "constant F1 across all N samples" (different outputs can yield same F1). The prose conflates these in Section 1.
- **Suggestion**: Clarify at first use that degeneracy means constant-F1, not output identity.

---

### Questions

1. SciERC within-instance ρ(LP, F1)=0.248 vs Few-NERD ρ≈0.5: Is this alignment difference explained by entity ambiguity, schema complexity, or training? Have you examined per-type alignment on SciERC?

2. Table §per_type_lp_scierc shows within-SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79), contradicting the cross-dataset and within-Few-NERD patterns. How do you reconcile this?

3. Random (0.610) vs Greedy (0.645): Is this gap entirely from T=1.0 sampling quality degradation? What is average sample F1 at T=1.0?

4. With 2-3 seeds, Fisher combined p has very limited sensitivity. What prevents running 5+ seeds?

---

### Missing References

- MBR for code generation (Shi et al. 2022) would strengthen the structured-output connection
- Eisenstein et al. (2023, reward model ensembles) relevant to signal limitation discussion
- Perez et al. (2022, sycophancy) as related diversity-collapse mechanism

---

### Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | Core claims supported but statistical power issues (W1) and non-independence (W3) weaken quantitative conclusions |
| Excitement | 3.5/5 | Negative result genuinely useful; diagnosis framework insightful; but practical implication ("use greedy or train verifier") somewhat expected |
| Reproducibility | 4.0/5 | Training configs, hyperparameters, prompts, statistical tests well-documented |
| Reviewer Confidence | 4/5 | Familiar with MBR, confidence estimation, NER evaluation; checked statistical claims in detail |

**Overall: 3.0/5** (Findings-level; needs revisions on statistical framing)

**一句话总结**: 诊断框架有洞察力，但统计论证关键环节（SciERC 检验力不足、3 数据点因果推断、非独立性假设）削弱了核心 claim 的可信度，需要 reframe 才能达到 main conference 水准。

---

### 历史 Open Issues 状态更新

| Issue | 状态 | 当前论文证据 |
|-------|------|-------------|
| R0-C3: Selection gap 仅 SciERC | **Partially resolved** | 现有 4 个数据集均展示 gap（结构信号全部失败），但 LP 正面结果仅 Few-NERD |
| R16-N1: Monotonic claim 仅 3 数据点 | **Still open** | 仍为 3 dataset-level 点；entity-type 分析有非独立性问题 (W3) |
| R17-W1: LoRA rank=8 LP compression 数据 | **Resolved** | LP range 0.057 vs 0.041 nats 已报告 (§5.4) |
| R17-W2: Few-NERD 3 epochs confound | **Partially resolved** | 5-epoch control provided (App. §epoch_confound) 但引入新 confound (W4) |
| R14-W1: Fisher combined p 统计效力 | **Still open** | 仍为 2 seeds; paper 承认但未增加 |
| R14-M1: Random vs Single 差距来源 | **Resolved** | Random 从 T=1.0 samples 中均匀选取，低于 T=0 greedy 是预期行为；已通过 oracle analysis 解释 |

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

_source line 1797 · 2026-05-18T01:35:32.610368+00:00_

Reviewer 1 审稿已收到。

**R1 核心发现摘要**:
- Overall: 3.0/5 (Findings-level, needs revisions)
- 4 个 Major weaknesses: 统计效力不足(W1)、3数据点因果推断(W2)、非独立性假设(W3)、Few-NERD epoch confound(W4)
- 2 个 Moderate: LoRA capacity confound(W5)、supervised verifier scope(W6)
- 1 个 Minor: degeneracy 定义歧义(W7)
- 历史 issues: R16-N1 和 R14-W1 仍 open

等待 Reviewer 2 审稿完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1798 · 2026-05-18T01:35:35.366109+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心发现：论文诊断框架清晰且有洞察力（Overall 3.0/5, Findings-level），但有 4 个 Major weakness：
1. SciERC 选择测试统计效力不足（~55% power），无法区分"真无效"与"检测不到"
2. 跨数据集 degeneracy gradient 仅 3 个观测点，因果推断过强
3. Per-entity-type 相关性（n=8）违反独立性假设，p 值可能被高估 5-10x
4. Few-NERD 3-epoch 训练 confound 控制不完整，favorable conditions 部分来自训练配置

历史 open issues 中 R17-W1 和 R14-M1 已解决，R16-N1 和 R14-W1 仍 open。

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

_source line 1799 · 2026-05-18T01:35:43.481516+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 143

## Round 143

6 recorded events


### User

_source line 1800 · 2026-05-18T01:37:11.820660+00:00_

[Reviewer 2 审稿意见]:
## Round 18 审稿报告 — Reviewer 2（新颖性 + 写作质量 + 完整性）

---

## Paper Summary

本文研究 LLM-based NER 中五种 confidence signals（4 个 instance-level：SJ, VC, FK, EM；1 个 per-sample：LP）用于质量估计（QE）和样本选择（selection）的表现。核心发现是 QE 和 selection 之间存在"correlation-selection gap"：所有信号都能可靠估计实例质量（ρ 最高 0.42，AUROC 最高 0.82），但无法将此优势转化为 best-of-N 选择增益。论文诊断出三层失败机制，并识别 LP 选择成功的两个必要条件（低 degeneracy + 充足 alignment）。

---

## Summary of Strengths

**S1. QE 与 selection 的系统性分离是重要的方法论贡献。** 现有文献混淆这两个任务；本文通过严格定义和分离实验，揭示了二者之间的 disconnect。这对 test-time compute scaling 社区有实际价值。

**S2. 实验设计严谨且全面。** 四个 NER 数据集构成清晰的 difficulty gradient（WNUT-17 → SciERC → Few-NERD → CoNLL），两个模型族，4B ablation，温度/N/LoRA-rank 多维度消融。统计检验（bootstrap CI, TOST, Bonferroni, Fisher combined p）远超同类工作的严谨程度。Few-NERD（n=32,565）提供了高统计功效的验证。

**S3. Two-condition 分析框架有洞察力。** 跨数据集梯度（47% → 17.8% → 13.8% degeneracy 对应 fail → +0.42pp → +1.36pp）加上 LoRA-rank ablation（degeneracy 降至 7.2% 但 ρ≈0.24 导致仍然失败）优雅地解耦了两个必要条件。per-entity-type 分析（ρ=−0.881, p=0.004）提供了细粒度统计支撑。

**S4. Appendix 质量极高。** 20+ 节 appendix 系统性地覆盖了 robustness、calibration、TOST、multi-seed stability、free-form ablation、epoch confound 等。每个潜在 confound 都有专门控制实验。

**S5. 写作质量相较前轮有显著提升。** Em-dash 问题已完全修复（零处解释性 dash）；Discussion 从 14 个子话题压缩至 7 个；"correlation-selection gap" 在 Introduction 首次使用时有括号操作性定义。

---

## Summary of Weaknesses

**W1 [warning] 纯诊断性论文缺乏 positive contribution/remedy。**
- 具体位置：Conclusion（Section 7）、Discussion practical guidelines
- 问题：论文的核心结论是"现有信号不 work"，唯一的正面发现（Few-NERD LP +1.36pp）效果modest。论文建议"closing the gap requires content-aware verifiers"但未尝试实现。supervised verifier baseline（Section 5.5, LR/MLP/RF）全部失败，但这些是极简 baseline，不代表 learned verifier 不可行。
- 为什么影响评分：对于 EMNLP main conference，审稿人通常期望论文在诊断问题之外提供至少一个可行的改进方向。当前论文的 actionable takeaway 有限："if degeneracy < 15% and alignment > 0.3, use LP"这一 guideline 实用但门槛较高。
- 建议：至少训练一个简单但非 trivial 的 learned verifier（如基于 entity embedding 的 scorer），或对 few-shot prompted verifier 做初步实验，以展示 oracle gap 是否可部分回收。即使回收 5-10% 也能大幅增强论文的贡献叙事。
- 历史状态：延续 R12-W1，仍 OPEN。

**W2 [warning] "Three-layer" gap 结构中 Layer 1 是 definitional，接近 tautological。**
- 具体位置：Abstract line 6, Section 5.3 paragraph 1, Conclusion line 5
- 问题：Layer 1 说"four instance-level signals cannot rank candidates by construction"。这是信号定义的直接推论，不是实验发现。真正的实验贡献在 Layer 2（MBR fails due to degeneracy）和 Layer 3（LP requires two conditions）。将 definitional observation 包装为 three-layer structure 的第一层，在叙事上夸大了分析的深度。
- 建议：将 Layer 1 重新 frame 为 methodological premise（已在 Introduction line 11 有类似表述），让 "gap" 的核心叙事集中在 Layer 2-3 的实证发现上。或者，将 MBR conversion 失败的实证证据（而非定义性陈述）作为 Layer 1 的内容。
- 历史状态：延续 R3-W2，PARTIALLY ADDRESSED（已明确标注 "by construction" 但仍作为 layer 1 呈现）。

**W3 [warning] Abstract 信息密度仍然过高。**
- 具体位置：Abstract（9 sentences, ~170 words）
- 问题：包含 ρ up to 0.38, ~13 pp, 14-47%, +1.36 pp, p<0.001, ρ ≳ 0.3, +0.52 pp, p=0.003 等至少 8 个定量值。虽然叙事线完整（problem → QE works → selection fails → diagnosis → positive case → future direction），但数字密度使得 30 秒快速阅读时难以提取核心 message。
- 建议：将 three-layer 细节和 N-scaling 数字（+0.52pp）移出 Abstract，只保留核心 claim 所需的 2-3 个关键数字。最后一句"Closing the gap for structural signals likely requires learned per-sample scoring"可以更具体。
- 历史状态：延续 R13-W2，PARTIALLY IMPROVED（叙事完整但密度仍高）。

**W4 [warning] 模型规模覆盖有限（4B-8B），结论外推受限。**
- 具体位置：Limitations lines 1-2, Introduction line 25
- 问题：所有实验限于 4B-8B 模型。Degeneracy 是核心 bottleneck，但更大模型（70B+）或 API 模型可能产生更多样的输出，从根本上改变 degeneracy regime。论文承认这一局限（"behavior at 70B+ scales remains an open question"），但这意味着核心结论可能仅适用于中小规模 fine-tuned 模型。
- 影响：审稿人可能质疑：如果 70B 模型天然低 degeneracy，那论文的大部分分析是否仅反映了小模型的特性而非结构化 IE 的固有困难？

---

## Questions for Authors

**Q1.** Table 3 (cross-dataset comparison) 中 SciERC greedy=0.614 与 Table 2 greedy=0.645 的差异由 footnote 解释为 "full-set vs gold-filtered evaluation"。但这意味着同一数据集在同一论文中使用了两种不同的 evaluation protocol，这容易造成混淆。能否统一 protocol 或更显著地标注？

**Q2.** Supervised verifier baseline（Section 5.5）使用 3-fold CV 在 SciERC 上训练，数据量极小（~350 training instances）。这个 baseline 是否公平地代表了 learned verifier 的潜力？如果在 Few-NERD（32K instances）上训练是否结果不同？

**Q3.** Few-NERD 使用 3 epochs 而其他数据集使用 5 epochs（Appendix P），epoch confound analysis 显示 5-epoch 模型 degeneracy 从 11% 升至 31%。如何排除 Few-NERD 的 LP success 不完全是 training schedule 的 artifact？

**Q4.** Entity-token LP（Discussion line 22）方差增大 4× 但选择反而更差。这与"LP compression is the bottleneck"的叙事矛盾——如果更高方差不帮助，bottleneck 是否真的是 compression？

---

## Missing References

引用覆盖基本充分。57 个 unique citations 覆盖了 self-consistency、MBR decoding、confidence estimation、structured IE 的主要文献。

可能遗漏的方向：
- **Structured prediction diversity**: Vijayakumar et al. (2018) "Diverse Beam Search" 和相关 diverse decoding 工作，与 degeneracy 问题直接相关
- **Set-valued prediction theory**: Vovk et al. conformal prediction for set-valued outputs，与 set-valued NER output 有理论联系
- **NER-specific confidence**: Shen et al. / Li et al. 在 NER uncertainty 方面的近期工作

4 个 orphan bib entries（bhattacharyya2026beyond, malinin2021uncertainty, ren2023selfevaluation, zhang2025conformal）建议清理。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| ACL 模板 + `[review]` | ✅ | `\usepackage[review]{acl}` |
| 正文 ≤ 8 页 | ✅ | 第 8 页含 Limitations + Ethics，References 从第 8 页底开始 |
| 匿名化 | ✅ | `\author{Anonymous}`，代码 URL 为 `[anonymized URL]` |
| 行号 | ✅ | review 模式自动启用 |
| Limitations | ✅ | 详尽，15 行，覆盖 scale/dataset/verifier/N/seeds |
| Ethics Statement | ✅ | 存在但较简短（5 行） |
| Appendix 在 bibliography 后 | ✅ | main.tex 结构正确 |
| 引用格式 | ✅ | `\cite` / `\citet` / `\citep` 使用正确 |
| AI 写作痕迹 | ✅ | em-dash 已清零；-ing phrases 在正常范围；无过度分段 |

---

## 历史 Open Issues 状态更新

| Issue | 状态 | 说明 |
|-------|------|------|
| R3-W2: Gap 概念 tautological | PARTIALLY FIXED | Layer 1 标注了 "by construction" 但仍作为 three-layer 的一部分 |
| R11-W1: vs Yao et al. 增量 | IMPROVED | Introduction line 8 明确差异化定位 |
| R13-W2: Abstract 过密 | PARTIALLY IMPROVED | 叙事线完整但数字仍多 |
| R12-W1: 纯诊断无 remedy | OPEN | 未尝试 learned verifier |
| R17-W3: em-dash ~90 处 | RESOLVED | 零处解释性 dash |
| R17-W4: Discussion 过长 | IMPROVED | 7 个子话题，结构清晰 |
| R12-N1: ρ headline 归因 | RESOLVED | Abstract/Introduction 数值与表格一致 |
| R16-N2: ρ=0.42 矛盾 | RESOLVED | 0.38=SciERC VC, 0.42=Few-NERD LP，不同 dataset 无矛盾 |
| R14-M3: gap 操作性定义 | RESOLVED | Introduction line 13 括号内定义 |
| R11-N3: LP intrinsic 措辞 | ADDRESSED | Discussion 正确区分 NER/RE；free-form ablation 确认 NER 压缩非 constraint-imposed |

---

## 小问题（不影响接收）

1. Table 3 footnote 解释 SciERC greedy 0.614 vs 0.645 差异，但 footnote 编号被 `\protect\footnotemark` 分开两个 footnote（lines 100-113），阅读体验不佳。
2. Figure 2 caption 中 "dashed line at ~15%" 用 `\protect\footnotemark` 引用 footnote，但 footnote 说明仅引用了 Person/Art 两个 entity type 的边界，统计支撑有限（n=2）。
3. Appendix Section "Calibration Baseline" (P) 在 calibration analysis (B) 之后相隔很远，建议合并或交叉引用更明确。
4. 4 个 orphan bib entries 未被引用，建议清理。

---

## 主要优势总结

1. **方法论清晰**：QE vs selection 的系统性分离填补了文献空白
2. **统计严谨性突出**：bootstrap CI, TOST, Bonferroni, Fisher combined p, permutation tests
3. **Two-condition 框架**：degeneracy + alignment 的解耦分析优雅且有说服力
4. **写作质量显著提升**：em-dash 清零，Discussion 压缩，术语定义到位
5. **Appendix 质量极高**：20+ 节系统性覆盖所有潜在 confounds

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法严谨，统计检验全面；但 three-layer gap 的 Layer 1 是 definitional 而非 empirical |
| Excitement | 2.5/5 | 诊断性洞察有价值（QE≠selection），但缺乏正面贡献/remedy；LP +1.36pp 效果 modest |
| Reproducibility | 4/5 | 训练配置完整（Appendix E），prompt template 公开，统计检验细节充分，代码承诺 release |
| Datasets | 3/5 | 使用公开 benchmark，无新数据集贡献 |
| Software | 2/5 | 代码尚未 release（"upon acceptance"） |
| Confidence | 4/5 | 仔细阅读了全文 + 完整 appendix；NER/QE/MBR 相关领域有足够评审能力 |

## Overall Assessment

**Overall: 3.0/5 (Findings)**

**一句话总结**：这是一篇方法论严谨、统计充分的诊断性论文，成功揭示了 QE 与 selection 之间的 disconnect 及其两个必要条件，但纯诊断性质（无 remedy 尝试）和 Layer 1 的 tautological 成分使其更适合 Findings 而非 Main Conference。

论文在写作和技术执行层面质量高，特别是 em-dash 问题的完全修复和 Discussion 的压缩值得肯定。如果作者能（a）训练一个简单 learned verifier 展示 oracle gap 的部分可回收性，以及（b）将 three-layer 叙事重构为 two-layer empirical analysis + methodological premise，论文将显著增强对 Main Conference 的竞争力。

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

_source line 1801 · 2026-05-18T01:37:42.423433+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 18 交叉分享 — Reviewer 1 请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Strengths\nS1. QE 与 selection 的系统性分离是重要的方法论贡献。\nS2. 实验设计严谨且全面。四个 NER 数据集构成 difficulty gradient，bootstrap CI, TOST, Bonferroni, Fisher combined p。\nS3. Two-condition 分析框架有洞察力。\nS4. Appendix 质量极高。20+ 节覆盖所有 confounds。\nS5. 写作质量显著提升。em-dash 清零，Discussion 压缩，术语定义到位。\n\n### Weaknesses\n\n**W1 [warning] 纯诊断性论文缺乏 positive contribution/remedy。**\n- 核心结论是\"现有信号不 work\"，唯一正面发现（Few-NERD LP +1.36pp）效果 modest。建议\"closing the gap requires content-aware verifiers\"但未实现。supervised verifier baseline（LR/MLP/RF）全部失败但是极简 baseline。\n- 对于 EMNLP main conference，审稿人期望诊断之外提供至少一个可行改进方向。\n- 建议：训练一个简单但非 trivial 的 learned verifier 展示 oracle gap 部分可回收性。\n\n**W2 [warning] \"Three-layer\" gap 结构中 Layer 1 是 definitional，接近 tautological。**\n- Layer 1 \"four instance-level signals cannot rank candidates by construction\" 是定义推论非实验发现。真正贡献在 Layer 2-3。将 definitional observation 包装为 three-layer 第一层夸大了分析深度。\n- 建议：Layer 1 重新 frame 为 methodological premise，核心叙事集中在 Layer 2-3 实证发现。\n\n**W3 [warning] Abstract 信息密度仍然过高。**\n- 9 sentences, ~170 words，含至少 8 个定量值（ρ, AUROC, pp, nats, p, N, degeneracy%）。30 秒快速阅读难以提取核心 message。\n- 建议：只保留核心 claim 所需的 2-3 个关键数字。\n\n**W4 [warning] 模型规模覆盖有限（4B-8B），结论外推受限。**\n- 70B+ 或 API 模型可能产生更多样输出，从根本上改变 degeneracy regime。核心结论可能仅适用于中小规模 fine-tuned 模型。\n\n### Questions\n\nQ1. Table 3 vs Table 2 evaluation protocol 差异容易混淆。\nQ2. Supervised verifier 在 SciERC ~350 training instances 上训练，是否公平？Few-NERD 上训练是否结果不同？\nQ3. Few-NERD 3 epochs: 如何排除 LP success 不完全是 training schedule artifact？\nQ4. Entity-token LP 方差增大 4× 但选择更差。与\"LP compression is bottleneck\"叙事矛盾？\n\n### Missing References\n- Diverse Beam Search (Vijayakumar et al. 2018)\n- Conformal prediction for set-valued outputs (Vovk et al.)\n- NER-specific confidence (Shen et al. / Li et al.)\n- 4 个 orphan bib entries\n\n### Overall: 3.0/5 (Findings)\n\n---\n\n请逐条回应 W1-W4 和 Q1-Q4。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "18"
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
    "text": "## Round 18 交叉分享 — Reviewer 1 请回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 2 完整审稿意见\n\n### Strengths\nS1. QE 与 selection 的系统性分离是重要的方法论贡献。\nS2. 实验设计严谨且全面。四个 NER 数据集构成 difficulty gradient，bootstrap CI, TOST, Bonferroni, Fisher combined p。\nS3. Two-condition 分析框架有洞察力。\nS4. Appendix 质量极高。20+ 节覆盖所有 confounds。\nS5. 写作质量显著提升。em-dash 清零，Discussion 压缩，术语定义到位。\n\n### Weaknesses\n\n**W1 [warning] 纯诊断性论文缺乏 positive contribution/remedy。**\n- 核心结论是\"现有信号不 work\"，唯一正面发现（Few-NERD LP +1.36pp）效果 modest。建议\"closing the gap requires content-aware verifiers\"但未实现。supervised verifier baseline（LR/MLP/RF）全部失败但是极简 baseline。\n- 对于 EMNLP main conference，审稿人期望诊断之外提供至少一个可行改进方向。\n- 建议：训练一个简单但非 trivial 的 learned verifier 展示 oracle gap 部分可回收性。\n\n**W2 [warning] \"Three-layer\" gap 结构中 Layer 1 是 definitional，接近 tautological。**\n- Layer 1 \"four instance-level signals cannot rank candidates by construction\" 是定义推论非实验发现。真正贡献在 Layer 2-3。将 definitional observation 包装为 three-layer 第一层夸大了分析深度。\n- 建议：Layer 1 重新 frame 为 methodological premise，核心叙事集中在 Layer 2-3 实证发现。\n\n**W3 [warning] Abstract 信息密度仍然过高。**\n- 9 sentences, ~170 words，含至少 8 个定量值（ρ, AUROC, pp, nats, p, N, degeneracy%）。30 秒快速阅读难以提取核心 message。\n- 建议：只保留核心 claim 所需的 2-3 个关键数字。\n\n**W4 [warning] 模型规模覆盖有限（4B-8B），结论外推受限。**\n- 70B+ 或 API 模型可能产生更多样输出，从根本上改变 degeneracy regime。核心结论可能仅适用于中小规模 fine-tuned 模型。\n\n### Questions\n\nQ1. Table 3 vs Table 2 evaluation protocol 差异容易混淆。\nQ2. Supervised verifier 在 SciERC ~350 training instances 上训练，是否公平？Few-NERD 上训练是否结果不同？\nQ3. Few-NERD 3 epochs: 如何排除 LP success 不完全是 training schedule artifact？\nQ4. Entity-token LP 方差增大 4× 但选择更差。与\"LP compression is bottleneck\"叙事矛盾？\n\n### Missing References\n- Diverse Beam Search (Vijayakumar et al. 2018)\n- Conformal prediction for set-valued outputs (Vovk et al.)\n- NER-specific confidence (Shen et al. / Li et al.)\n- 4 个 orphan bib entries\n\n### Overall: 3.0/5 (Findings)\n\n---\n\n请逐条回应 W1-W4 和 Q1-Q4。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "18"
  }
}
```

</details>

---


### Tool result

_source line 1802 · 2026-05-18T01:38:16.849319+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 34425
}
```

</details>

---


### Tool call

_source line 1803 · 2026-05-18T01:38:17.050473+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 18 交叉分享 — Reviewer 2 请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n## Reviewer 1 完整审稿意见\n\n### Strengths\nS1. Well-structured diagnostic framework. Three-layer decomposition clean and instructive.\nS2. Comprehensive ablation coverage. Temperature, N-scaling, LoRA rank, model scale, free-form, epochs.\nS3. Honest reporting of negative results.\nS4. Strong Few-NERD validation (n=32,565, >99% power, CI [+1.18, +1.53]).\nS5. Entity-type-level granularity in Appendix.\n\n### Weaknesses\n\n**W1 [Major] SciERC selection test 统计效力不足。**\n- LP +0.2pp (p=0.29) on SciERC (n=529, 2 seeds). ~55% post-hoc power for 1pp effect. 无法区分\"真无效果\"和\"检测不到\"。\n- 论文 framing 将 SciERC 负面结果作为 established fact 而非 inconclusive。\n- N-scaling 表 (App.) 显示 +0.42pp at N=8 → +0.91pp at N=32，暗示 LP 可能有小但真实的效应。\n- 三路梯度 (47% → fail, 18% → weak, 14% → success) 依赖中间点是 genuinely \"weak/null\" 而非 underpowered。\n- 建议：报告 minimum detectable effect at 80% power。\n\n**W2 [Major] Cross-dataset degeneracy gradient: 3 观测点因果推断 overfit。**\n- 3 数据点不能 \"establish\" 任何因果关系（任何 3 有序数字都 trivially monotonic）。数据集在 ≥5 维度同时不同（degeneracy, alignment, difficulty, schema, epochs, data size）。\n- 建议：Reframe \"consistent with\" 而非 \"establishes\"；列出 confounded variables；用 controlled ablations 辅助。\n\n**W3 [Major] Per-entity-type correlation (n=8, ρ=-0.881, p=0.004): 非独立性膨胀显著性。**\n- 8 entity types 共享 model, tokenizer, temperature, 且 entities often co-occur in same sentences. Independent obs assumption violated; effective df < 6.\n- p=0.004 可能被高估 5-10x. 建议 permutation test 或承认 non-independence.\n\n**W4 [Major] Few-NERD 3-epoch training confound 控制不完整。**\n- 5-epoch triples degeneracy (11.1% → 31.3%) and halves LP gains (+1.37pp → +0.62pp). Favorable conditions partly training-induced.\n- 5-epoch model 有更高 greedy F1 (0.777 vs 0.748)，引入 performance-regime confound.\n- 建议：Foreground 3-epoch = early stopping；加 matched-degeneracy cross-dataset comparison.\n\n**W5 [Moderate] LoRA rank=8 ablation conflates capacity and degeneracy。**\n- rank=8 同时降低 capacity 和改变 training dynamics。Lower alignment (ρ≈0.24) 可能源自 insufficient capacity。\n- 温度 ablation (T=1.2) 提供更 clean 的证据。建议 foreground T=1.2。\n\n**W6 [Moderate] Supervised verifier baseline 仅 recycled features。**\n- 5 scalar features 中 4 个 instance-level. \"Bottleneck lies in what signals encode\" 仅对此 feature set 成立。\n- 建议：Scope conclusion to \"these 5 features\" 而非 general supervised approaches.\n\n**W7 [Minor] Instance degeneracy 定义操作性模糊。**\n- Prose says \"identical outputs\" 但实际操作定义是 \"constant F1 across all N samples\"（不同输出可产生相同 F1）。\n- 建议：首次使用时澄清。\n\n### Questions\n\nQ1. SciERC within-instance ρ(LP, F1)=0.248 vs Few-NERD ρ≈0.5 差异原因？有无 SciERC per-type alignment？\nQ2. SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79) 与 cross-dataset/within-Few-NERD 矛盾如何解释？\nQ3. Random (0.610) vs Greedy (0.645) gap 是否完全来自 T=1.0 质量下降？\nQ4. 为何不跑 5+ seeds？\n\n### Missing References\n- Shi et al. 2022 (MBR for code generation)\n- Eisenstein et al. 2023 (reward model ensembles)\n- Perez et al. 2022 (sycophancy, diversity collapse)\n\n### Overall: 3.0/5 (Findings-level; needs revisions on statistical framing)\n\n---\n\n请逐条回应 W1-W7 和 Q1-Q4。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "18"
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
    "text": "## Round 18 交叉分享 — Reviewer 2 请回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应其 Weaknesses 和 Questions：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n## Reviewer 1 完整审稿意见\n\n### Strengths\nS1. Well-structured diagnostic framework. Three-layer decomposition clean and instructive.\nS2. Comprehensive ablation coverage. Temperature, N-scaling, LoRA rank, model scale, free-form, epochs.\nS3. Honest reporting of negative results.\nS4. Strong Few-NERD validation (n=32,565, >99% power, CI [+1.18, +1.53]).\nS5. Entity-type-level granularity in Appendix.\n\n### Weaknesses\n\n**W1 [Major] SciERC selection test 统计效力不足。**\n- LP +0.2pp (p=0.29) on SciERC (n=529, 2 seeds). ~55% post-hoc power for 1pp effect. 无法区分\"真无效果\"和\"检测不到\"。\n- 论文 framing 将 SciERC 负面结果作为 established fact 而非 inconclusive。\n- N-scaling 表 (App.) 显示 +0.42pp at N=8 → +0.91pp at N=32，暗示 LP 可能有小但真实的效应。\n- 三路梯度 (47% → fail, 18% → weak, 14% → success) 依赖中间点是 genuinely \"weak/null\" 而非 underpowered。\n- 建议：报告 minimum detectable effect at 80% power。\n\n**W2 [Major] Cross-dataset degeneracy gradient: 3 观测点因果推断 overfit。**\n- 3 数据点不能 \"establish\" 任何因果关系（任何 3 有序数字都 trivially monotonic）。数据集在 ≥5 维度同时不同（degeneracy, alignment, difficulty, schema, epochs, data size）。\n- 建议：Reframe \"consistent with\" 而非 \"establishes\"；列出 confounded variables；用 controlled ablations 辅助。\n\n**W3 [Major] Per-entity-type correlation (n=8, ρ=-0.881, p=0.004): 非独立性膨胀显著性。**\n- 8 entity types 共享 model, tokenizer, temperature, 且 entities often co-occur in same sentences. Independent obs assumption violated; effective df < 6.\n- p=0.004 可能被高估 5-10x. 建议 permutation test 或承认 non-independence.\n\n**W4 [Major] Few-NERD 3-epoch training confound 控制不完整。**\n- 5-epoch triples degeneracy (11.1% → 31.3%) and halves LP gains (+1.37pp → +0.62pp). Favorable conditions partly training-induced.\n- 5-epoch model 有更高 greedy F1 (0.777 vs 0.748)，引入 performance-regime confound.\n- 建议：Foreground 3-epoch = early stopping；加 matched-degeneracy cross-dataset comparison.\n\n**W5 [Moderate] LoRA rank=8 ablation conflates capacity and degeneracy。**\n- rank=8 同时降低 capacity 和改变 training dynamics。Lower alignment (ρ≈0.24) 可能源自 insufficient capacity。\n- 温度 ablation (T=1.2) 提供更 clean 的证据。建议 foreground T=1.2。\n\n**W6 [Moderate] Supervised verifier baseline 仅 recycled features。**\n- 5 scalar features 中 4 个 instance-level. \"Bottleneck lies in what signals encode\" 仅对此 feature set 成立。\n- 建议：Scope conclusion to \"these 5 features\" 而非 general supervised approaches.\n\n**W7 [Minor] Instance degeneracy 定义操作性模糊。**\n- Prose says \"identical outputs\" 但实际操作定义是 \"constant F1 across all N samples\"（不同输出可产生相同 F1）。\n- 建议：首次使用时澄清。\n\n### Questions\n\nQ1. SciERC within-instance ρ(LP, F1)=0.248 vs Few-NERD ρ≈0.5 差异原因？有无 SciERC per-type alignment？\nQ2. SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79) 与 cross-dataset/within-Few-NERD 矛盾如何解释？\nQ3. Random (0.610) vs Greedy (0.645) gap 是否完全来自 T=1.0 质量下降？\nQ4. 为何不跑 5+ seeds？\n\n### Missing References\n- Shi et al. 2022 (MBR for code generation)\n- Eisenstein et al. 2023 (reward model ensembles)\n- Perez et al. 2022 (sycophancy, diversity collapse)\n\n### Overall: 3.0/5 (Findings-level; needs revisions on statistical framing)\n\n---\n\n请逐条回应 W1-W7 和 Q1-Q4。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "18"
  }
}
```

</details>

---


### Tool result

_source line 1804 · 2026-05-18T01:38:18.662340+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1611
}
```

</details>

---


### Assistant

_source line 1805 · 2026-05-18T01:38:23.666254+00:00_

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


## Round 144

## Round 144

2 recorded events


### User

_source line 1806 · 2026-05-18T01:38:26.426797+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断：Overall 3.0/5（Findings level）。**

主要评估：
- **格式完全合规**：8 页正文，`[review]` 模板，匿名化完整，em-dash 问题已清零
- **历史 issues**：10 个中 6 个 RESOLVED，2 个 IMPROVED，2 个仍 OPEN（纯诊断无 remedy、Layer 1 tautological）
- **核心 weakness**：纯诊断性论文缺乏 positive contribution（W1）和 three-layer gap 中 Layer 1 是 definitional（W2）是限制论文达到 Main Conference 门槛的主要因素
- **核心 strength**：QE vs selection 的系统性分离、two-condition 框架的解耦分析、统计检验的严谨性远超同类工作

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

_source line 1807 · 2026-05-18T01:38:32.404486+00:00_

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


## Round 145

## Round 145

2 recorded events


### User

_source line 1808 · 2026-05-18T01:39:43.190814+00:00_

[Reviewer 1 审稿意见]:
## Round 18 交叉回应 — Reviewer 1 回应 Reviewer 2

### Weaknesses 回应

**[AGREE] R2-W1: 纯诊断性论文缺乏 positive contribution/remedy**
同意这是最大 venue-fit 风险。唯一 positive finding (Few-NERD LP +1.36pp) 效果 modest，supervised verifier baseline 使用同样 5 个信号属于 straw-man。但 R2 建议训练 non-trivial verifier 存在 scope creep 风险。论文的实际贡献在于 practical guidelines (§6) 和 negative-result methodology；对 Findings track 足够，对 main 需要更强 positive signal。

**[AGREE] R2-W2: Layer 1 是 definitional/tautological**
同意。"Instance-level signals cannot rank by construction" 是数学事实非实验发现。Introduction 已称其为 "methodological premise" (§1 line 11)，但 Abstract/Contributions 仍包装为 three-layer 第一层。建议 Contribution 2 改写为 "Two empirical mechanisms (degeneracy, alignment) that block the sole per-sample signal"。注意 Layer 1 有叙事功能（解释为何需要区分 signal types），问题在于与实证发现并列计数。

**[REBUT] R2-W3: Abstract 信息密度过高**
部分不同意。诊断性论文中具体数值 IS the contribution——reviewer 需要从 Abstract 判断 QE 强度 (ρ=0.38)、gap 大小 (13pp headroom)、LP 成功条件 (+1.36pp, p<0.001)、失败条件 (14-47% degeneracy)。但同意中间机制数字 (median ρ=0.52, +0.52pp N-scaling) 可移入正文。建议保留 4-5 核心数字、移除 3-4 个。

**[AGREE] R2-W4: 模型规模覆盖有限（4B-8B）**
完全同意。我的补充：Table §degeneracy 显示 8B degeneracy (17.8%) > 4B (10.4%)，更大模型 degeneracy 更高。如果趋势延续到 70B+，degeneracy 问题可能更严重而非更轻。但 70B+ 的 LP alignment 可能突破 ρ≈0.3 门槛——无实验数据无法判断方向。

---

### Questions 回应

**[REBUT] R2-Q1: Table 3 vs Table 2 protocol 混淆**
论文已有标注：Table 3 脚注解释 full-set vs gold-filtered 差异，§2.3 解释 filtering rationale。差异是 deliberate design choice（Table 2: controlled selection comparison; Table 3: cross-dataset degeneracy comparison）。同意可在 Table 3 caption 加粗 "(full-set evaluation)" 提高可见性。

**[AGREE] R2-Q2: Supervised verifier 在 SciERC ~350 instances 训练是否公平？**
合理质疑。SciERC 3-fold CV 数据量对 LR/RF 充分但非 verifier 公平测试。Few-NERD 上未训练 verifier。论文应在 SciERC N=32 (19.2pp headroom) 上补充或解释为何 data size 非 bottleneck。

**[REBUT] R2-Q3: Few-NERD LP success 是否 training schedule artifact？**
App. §epoch_confound 直接回答：5-epoch model 仍有 LP +0.62pp（正向但减半）。证明 LP success 非 3-epoch artifact——在 5 epochs 仍存在，仅因 degeneracy 增加 (11.1%→31.3%) 而减弱。3-epoch 对应 validation-loss 最优 checkpoint (step 32,000)，是标准 early stopping 产物。但如我 W4 所述：5-epoch 同时改变 greedy F1，引入 performance-regime confound，matched-degeneracy 比较缺失。

**[REBUT] R2-Q4: Entity-token LP 方差 4× 但选择更差，与 compression-is-bottleneck 矛盾？**
不矛盾。论文 claim 不是 "variance 越高 selection 越好"，而是 "compression 限制 exploitation"。§6 line 22 解释：entity-token LP 的高方差来自 fewer-token averaging noise 和 position-dependent variation，是 noise 非 signal。Full-sequence ρ(LP,F1)=0.248 已是最优 aggregation。这反而强化了 "bottleneck in what signals encode" 结论——即使放大到 entity tokens 也无法突破表征层面的 near-determinism。

---

### 与 R2 的分歧总结

R2 更关注 **framing/venue-fit** (positive contribution, abstract density, three-layer packaging)；我更关注 **statistical rigor** (power, independence, confounds)。两组问题互补：
1. 统计 claim 需降级 (我的 W1-W3)
2. 叙事结构需调整 (R2 的 W2)
3. Venue-fit 需考虑 (R2 的 W1)

共同结论：当前版本适合 **Findings** (3.0/5)，若解决统计 framing + 补充一个 non-trivial positive result 可冲 main conference。

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

_source line 1809 · 2026-05-18T01:39:59.007304+00:00_

Reviewer 1 交叉回应已收到。核心共识：两位 Reviewer 均评 3.0/5 (Findings level)，Layer 1 tautological 和纯诊断无 remedy 达成一致。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 146

## Round 146

2 recorded events


### User

_source line 1810 · 2026-05-18T01:40:01.748923+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Review Director。

总结：对 R2 的 4 个 Weaknesses 同意 3 个（W1 venue-fit、W2 tautological layer、W4 scale），对 W3 (abstract density) 部分反驳。Questions 中 Q2 同意（verifier fairness），Q1/Q3/Q4 反驳并引用论文内证据。核心分歧：R2 侧重 framing/venue-fit，我侧重 statistical rigor，两组问题互补。

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

_source line 1811 · 2026-05-18T01:40:07.898446+00:00_

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


## Round 147

## Round 147

8 recorded events


### User

_source line 1812 · 2026-05-18T01:40:45.092400+00:00_

[Reviewer 2 审稿意见]:
## Round 18 交叉回应 — Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Weaknesses 回应

**[AGREE] R1-W1: SciERC 统计效力不足**

同意这是一个重要的统计 framing 问题。论文脚注（Section 5.3 footnote）承认 "post-hoc power: ~55% at n=529 for 1 pp effect"，但主文本仍以 "no signal consistently outperforms greedy" 作为核心结论的支柱之一，将 underpowered null result 等同于 established negative。

关键证据支持 R1 的担忧：
- N-scaling 表（Appendix Table 14, `tab:n_scaling_selection`）显示 SciERC LP 选择增益随 N 单调递增：+0.42pp (N=8) → +0.63pp (N=16) → +0.91pp (N=32)，bootstrap p=0.091 at N=32。这更像是一个 small but real effect 被 underpowered design 未能检测到，而非真正的零效应。
- 论文正确地将 Few-NERD（n=32,565, >99% power）作为 "definitive test"，但 Abstract 和 Introduction 的 framing 并未反映这一优先级——读者首先读到的是 SciERC 的 "fail" 而非 Few-NERD 的 success。

补充 R1 的建议：除了报告 minimum detectable effect at 80% power，还应在 Abstract/Introduction 中调整 framing 优先级，先呈现 Few-NERD 的 positive result 作为主要发现，再将 SciERC 定位为 "insufficient power to detect effects below ~1.5pp"。

**[AGREE] R1-W2: Cross-dataset gradient 3 点因果推断过强**

完全同意 "establishes" 一词对 n=3 观测过强。三个有序数字 trivially 形成 monotonic pattern，且数据集在 degeneracy、alignment、difficulty、schema、epoch、data size 等 ≥5 个维度同时不同。

但补充一点 R1 可能低估的证据：论文不仅依赖 cross-dataset 3 点，还有：
1. Per-entity-type within Few-NERD（n=8 types, ρ=−0.881）——虽然 R1-W3 正确质疑了 p 值，但 pattern 本身是 informative 的
2. LoRA-rank ablation（同一数据集内 degeneracy 7.2% but ρ≈0.24 → fail）
3. Temperature ablation（T=1.2: degeneracy 12.5%, ρ=0.225 → fail; Table `tab:t_degeneracy`）

这些 within-dataset controlled ablations 比 cross-dataset 比较更有说服力。建议作者 reframe 为 "the cross-dataset gradient is consistent with, and supplemented by, controlled within-dataset ablations that isolate each condition independently"。

**[AGREE] R1-W3: Per-entity-type ρ 非独立性膨胀显著性**

同意这是一个 underappreciated 的统计问题。8 个 entity types 共享同一模型、tokenizer、temperature 设定，且同一句子内常包含多个 entity type（SciERC per-type 分析中 entity count 和 relation count 的 ρ=0.769，Appendix Section 4 paragraph "Capability stratification"），因此 types 之间的 F1 scores 不独立。

具体影响估计：
- 若 effective df 降至 4-5（合理估计），p 值可能从 0.004 膨胀至 0.02-0.04
- 即使如此，仍可能在 α=0.05 水平显著，但不再 survive Bonferroni correction
- Appendix Table `tab:per_type_lp` 中的 pattern（7/8 types positive, 唯一 negative type = highest degeneracy）在描述性层面仍 compelling

建议作者做 cluster-robust permutation test（以 entity type 为 cluster），或明确将 p=0.004 标注为 "assuming independence; non-independence may inflate significance by up to an order of magnitude"。

**[REBUT] R1-W4: Few-NERD 3-epoch confound**

部分不同意 R1 将此视为 Major weakness。论文的 epoch confound analysis（Appendix Table `tab:epoch_confound`）实际上是一个 well-designed controlled ablation：

1. **Early stopping 是标准实践**：3-epoch 模型在 validation loss 最佳点（step 32,000 ≈ epoch 3.9）停止。这不是刻意选择低 degeneracy 条件，而是遵循标准训练流程。论文明确说："Standard early stopping practice thus naturally selects the low-degeneracy regime where LP selection is most effective"（Appendix `app:epoch_confound`）。

2. **5-epoch ablation 是控制实验**：结果显示 degeneracy 从 11% → 31%，LP gains 从 +1.37 → +0.62pp。这正好证明了 degeneracy-gating mechanism——不是 confound，而是论文核心 thesis 的额外证据。

3. **Within-instance alignment 稳定**：mean ρ 从 0.524 → 0.407，变化相对有限，supporting "alignment is task-determined not training-determined" 的论点。

但 R1 关于 "performance-regime confound"（5-epoch greedy F1 更高）的观察值得回应。更高 baseline F1 确实压缩了 headroom 的绝对量，但 5-epoch 模型的 degeneracy 变化（11% → 31%）远大于 greedy F1 变化（0.748 → 0.777），degeneracy 仍是主导因素。

R1 建议的 matched-degeneracy cross-dataset comparison 不现实：无法独立控制 degeneracy 而保持其他变量不变。温度是最接近的 lever，但温度同时改变 sample quality。

**[AGREE] R1-W5: LoRA rank=8 ablation conflates capacity and degeneracy**

同意温度 ablation 提供更 clean 的证据。LoRA rank=8 同时降低 model capacity（可能导致更差的 representation quality），改变 training dynamics（更少的可训练参数导致不同的 loss landscape），以及降低 degeneracy。因此 ρ≈0.24 可能反映 insufficient capacity 而非 inherently weak alignment。

论文实际上已有更 clean 的证据：
- T=1.2 ablation（Table `tab:t_degeneracy`）：degeneracy 降至 12.5%（接近 Few-NERD 的 13.8%），但 within-instance ρ(LP, F1)=0.225，仍远低于 Few-NERD 的 ~0.5
- 这在相同模型、相同数据集上仅改变温度，cleanly 分离了 degeneracy 和 alignment

Discussion Section 6 paragraph "Regime boundaries" 确实提到了温度 ablation，但 foreground 不够。建议作者将 T=1.2 ablation 提升为 Section 5.5 "Robustness" 中的 primary evidence，LoRA-rank 降级为 supplementary。

**[AGREE] R1-W6: Supervised verifier baseline 仅 recycled features**

完全同意，与我自己的 W1（纯诊断无 remedy）一致。5 个 scalar features 中 4 个是 instance-level，唯一的 per-sample feature（LP）本身就是被分析的对象。使用 LR/MLP/RF 在这些 features 上训练只能证明 "these specific features combined still don't work"，无法证明 "supervised approaches in general can't close the gap"。

论文的结论 "the bottleneck lies in what the signals encode, not how they are aggregated"（Section 5.5）对这组 features 成立，但不应推广到 general supervised verifiers。有潜力但未被测试的 feature sources 包括：
- Model hidden states / attention patterns
- Entity-level embeddings
- Prompted self-evaluation（verbalized confidence 已测试但效果差）
- Cross-sample feature interactions（已部分测试：pairwise interaction features, AUROC 0.632 vs 0.639）

建议 scope conclusion 为 "the bottleneck lies in what these five unsupervised signals encode"。

**[AGREE] R1-W7: Instance degeneracy 定义操作性模糊**

这是一个我在自己审稿中遗漏的有效观察。

具体矛盾：
- Abstract line 6："instance degeneracy (14–47% **identical outputs**)"
- Table `tab:fewnerd` footnote："Instance degeneracy: fraction of gold-filtered instances where all N samples produce **identical instance-level F1**"
- Table `tab:degeneracy` caption："Constant F1: all N samples receive **identical instance-level F1**"
- Table `tab:diversity`："Identical = fraction of instances with **all N outputs identical**"

"Identical outputs" 和 "identical F1" 是不同的操作：两个不同的 entity set 可以产生相同的 F1（例如，错误不同但数量相同）。Table `tab:diversity` 的 "Identical" (Qwen/SciERC: 11%) 和 Table `tab:degeneracy` 的 "Constant F1" (SciERC 8B: 17.8%) 数值不同，证实这两个定义产生不同的集合。

Abstract 使用 "identical outputs" 但操作上使用 "identical F1" 会误导读者。建议首次使用时明确："instance degeneracy (the fraction of instances where all N samples receive identical F1 scores, including cases where outputs differ but produce equivalent evaluation outcomes)"。

---

### Questions 回应

**Q1. SciERC vs Few-NERD alignment 差异原因**

好问题。论文将 alignment 归因于 "task structure"（Discussion paragraph "Regime boundaries"），但未进一步分析。SciERC 有 6 个 entity types 且 schema 较复杂（scientific terms, methods, tasks 等边界模糊），而 Few-NERD INTRA coarse 有 8 个 well-separated entity types（Person, Location, Organization 等）。一个可能的解释是：entity boundary 越 clear-cut，LP 越能区分 correct vs incorrect extractions。

Appendix Table `tab:per_type_lp_scierc` 提供了 SciERC per-type selection data，但**没有**报告 per-type within-instance ρ(LP, F1)——只有 degeneracy 和 LP Δ。这是一个遗漏：如果能报告 SciERC per-type alignment ρ，可以直接检验 R1 的假设。

**Q2. SciERC per-type ρ(degeneracy, LP Δ)=0.14 的矛盾**

Table `tab:per_type_lp_scierc` 显示 SciERC 内 per-type ρ=0.14 (p=0.79)，与 cross-dataset 和 within-Few-NERD 的 strong negative correlation 矛盾。论文承认这一矛盾："additional type-specific factors likely modulate selection at this granularity"。

我的解读：SciERC 只有 6 个 entity types（vs Few-NERD 的 8 个），degeneracy range 更窄（6.2%-20.0% vs 6.0%-19.8%），且 SciERC types 之间的 boundary clarity 差异更大（例如 OtherScientificTerm 是 catch-all category）。在窄范围内检测 monotonic relationship 需要更高 signal-to-noise ratio。但这个解释论文未给出，确实是一个未被充分讨论的 inconsistency。

**Q3. Random (0.610) vs Greedy (0.645) gap**

基本来自 T=1.0 sampling quality 下降。Temperature ablation（Appendix Table `tab:t_ablation`）显示 sample F1 从 0.636 (T=0.5) 降至 0.612 (T=1.0)。Random selection 在 N=8 samples 中均匀采样，其期望 F1 ≈ mean sample F1 ≈ 0.612，接近观察到的 0.610。Greedy (T=0, argmax) 不受 temperature quality 下降影响。所以 gap 确实主要来自 T=1.0 的 quality degradation。

**Q4. 为何不跑 5+ seeds**

论文 Limitations section line 13 承认 "2 training seeds; training seed stochasticity is not exhaustively quantified"。计算成本是合理原因（4 datasets × 3 models × N=8-16 samples × 多 seed），但 Few-NERD 的 n=32,565 提供了充分的 within-seed statistical power。更多 seeds 主要帮助量化 training stochasticity（不同 LoRA 初始化的影响），这对于 Few-NERD positive result 的可靠性比较重要。建议至少在 Few-NERD 上跑 3-5 个 training seeds 作为 camera-ready 的 robustness check。

---

### Missing References 回应

R1 建议的三篇 references：
- **Shi et al. 2022 (MBR for code generation)**：与 MBR 在非 MT 领域的应用相关，建议添加到 Related Work "MBR decoding" 段落
- **Eisenstein et al. 2023 (reward model ensembles)**：与 learned verifier 讨论相关，可补充到 "Best-of-N with learned verifiers" 段落
- **Perez et al. 2022 (sycophancy/diversity collapse)**：与 RLHF diversity collapse 相关，论文已引用 kirk2024understanding (diversity collapse in RLHF)，Perez 是另一个角度但覆盖类似问题

建议至少添加前两篇。

---

### 总体评价

R1 的审稿在统计方法论层面非常精准。W1（power）、W2（n=3 因果）、W3（非独立性）构成一组相互关联的统计 framing concerns，如果全部 addressed，论文的 claims 需要 significant softening——从 "establishes" 到 "consistent with"，从 "fail" 到 "insufficient evidence for gains at this sample size"。

W4（epoch confound）我认为 R1 评估偏严——论文已有 controlled ablation，且 early stopping 是标准实践。W5-W7 的建议具体且可操作。

R1 的 Overall 3.0 与我的评估一致。核心分歧在于 W4 的严重程度，但总体上 R1 的审稿质量很高。

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

_source line 1813 · 2026-05-18T01:41:09.154636+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
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

_source line 1814 · 2026-05-18T01:41:09.205291+00:00_



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

_source line 1815 · 2026-05-18T01:46:16.490918+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-18, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4x variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 dagger-RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n- id: R17-W1\n  summary: \"LoRA rank=8 下 LP compression 统计数据缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"R18 确认 LP range 0.057 vs 0.041 nats 已报告 (Section 5.4)\"\n  resolution_round: 18\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"R18 确认: Random 从 T=1.0 samples 均匀选取, Greedy 是 T=0 argmax. 差异来自 T=1.0 quality degradation. 已在正文解释.\"\n  resolution_round: 18\n- id: R16-N2\n  summary: \"rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"R18-R2 确认: ρ=0.38 是 SciERC VC, ρ=0.42 是 Few-NERD LP, 不同 dataset 无矛盾. Figure 1 caption 已正确归属.\"\n  resolution_round: 18\n- id: R12-N1\n  summary: \"rho headline 来自 ceiling-effect dataset / 数值不一致\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"R18-R2 确认 headline rho 归属正确: 0.38=SciERC primary, 0.42=Few-NERD.\"\n  resolution_round: 18\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"R18-R2 确认 Introduction line 13 括号内定义到位.\"\n  resolution_round: 18\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 18\n  resolution: \"R18-R2 确认 Discussion 正确区分 NER/RE; free-form ablation confirms NER compression non-constraint-imposed.\"\n  resolution_round: 18\n- id: R17-W3\n  summary: \"em-dash (---) 使用约 90 处, AI 写作风格痕迹显著\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"R18-R2 格式合规检查确认: 零处解释性 em-dash, AI 写作痕迹已清零.\"\n  resolution_round: 18\n\n# ===== RECURRING ISSUES (updated Round 18) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 18\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 核心 finding 实质仅 SciERC 验证.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已加入 Few-NERD. 但 positive finding 仅 1 model x 1 N x 1 dataset.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: Few-NERD 加入后 dataset 覆盖改善, 但 cross-dataset degeneracy gradient 仍仅 n=3.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: R1 'Partially resolved' — 4 datasets 均展示 structural signal failure, 但 LP positive result 仅 Few-NERD. Cross-dataset gradient 仍 n=3. R2 确认覆盖改善.\"\n  action_items:\n  - round: 17\n    action: \"增加 1-2 个 NER 数据集扩大 degeneracy gradient 的 n; 或将 cross-dataset gradient 明确标注为 exploratory.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 18\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识: 标题暗示意外发现但 4/5 signals weakness 部分 by construction.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 纯诊断性贡献对 main conference 门槛偏弱.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识: Layer 1 ('cannot rank by construction') 是定义推论非实验发现. Introduction 已称 'methodological premise' 但 Abstract/Contributions 仍包装为 three-layer 第一层. 问题在于与实证发现并列计数夸大分析深度. 建议 Contribution 2 改为 'Two empirical mechanisms (degeneracy, alignment) that block the sole per-sample signal'.\"\n  action_items:\n  - round: 18\n    action: \"将 three-layer 重构为: (1) methodological premise (not counted as contribution); (2) two empirical mechanisms. Abstract/Contribution 列表中不再将 'by construction' 作为独立发现列出.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N1\n  summary: \"Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点, 统计不显著\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"3 个 dataset-level 数据点无统计意义.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: Figure 3 pooled correlation 混合两个粒度, entity-type-level n=8 有 independence 问题.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识: (R1-W2 + R1-W3) n=3 不能 'establish' 因果; 任何 3 有序数字 trivially monotonic; datasets differ on ≥5 confounded dimensions. Entity-type ρ=-0.881 (p=0.004) 有 non-independence (shared model/tokenizer/temp), effective df<6, p 可能高估 5-10x. 建议: (1) 'consistent with' 非 'establishes'; (2) permutation test 或承认 non-independence; (3) controlled ablations (T, LoRA) 作为 primary 证据.\"\n  action_items:\n  - round: 18\n    action: \"(1) 'establishes' → 'is consistent with' / 'inversely associated with'; (2) entity-type p=0.004 加 caveat 'assuming independence; non-independence may inflate by up to 10x'; (3) foreground T-ablation 和 LoRA-rank as controlled within-dataset evidence, cross-dataset as supporting observation.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) / sign test 统计效力极低\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"SciERC null result 应改为 'effect small and not reliably detected'.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 负面结果缺少 power analysis. n=529, 2 seeds 检测 1pp 效应的 power 约 50-60%.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W1 + R2 AGREE): SciERC p=0.29 无法区分 'no effect' vs 'underpowered'. N-scaling 表显示 +0.42→+0.63→+0.91pp (N=8→16→32) suggesting small real effect. 三路梯度中间点 (18%→weak) 依赖此 null 是 genuine. Few-NERD (n=32,565) 才是 definitive. 建议: 报告 MDE at 80% power; 调整 framing 优先级 (Few-NERD first).\"\n  action_items:\n  - round: 18\n    action: \"(1) 报告 SciERC minimum detectable effect at 80% power (likely ~1.5-2pp); (2) 改 'fails' → 'insufficient evidence for gains below ~1.5pp at this sample size'; (3) Abstract/Introduction 先呈现 Few-NERD positive 再呈现 SciERC inconclusive.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"多种 remedy 已测试并全部 negative.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 纯诊断性论文缺乏 positive contribution. 已测试 entity-token LP, LP x VC, supervised combination, verbalized confidence, 全部 negative.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R2-W1 + R1 AGREE): 纯诊断+negative result 对 EMNLP main conference 门槛不足. Supervised verifier baseline 是 straw-man (5 scalar features). Practical guidelines (degeneracy check) 有价值但 modest. 需至少一个 non-trivial positive contribution. 但 R1 也注意到 scope creep 风险.\"\n  action_items:\n  - round: 18\n    action: \"(1) Reframe Few-NERD LP +1.36pp 为 primary practical finding (not just diagnostic evidence); (2) 提供明确 practitioners' decision rule; (3) 考虑训练简单 learned verifier (如 entity embedding scorer) 展示 oracle gap 部分可回收性 — 即使 5-10% 也大幅增强贡献叙事.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: \"Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露, 可能 confound degeneracy 比较\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: 主文说 '5 epochs' 暗示统一, Appendix 才披露 3 epochs.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: R1-W4 视为 Major (5-epoch control incomplete, performance-regime confound). R2 部分反驳: 3-epoch = validation-loss early stopping 是标准实践; 5-epoch ablation IS the controlled experiment showing degeneracy mechanism; +0.62pp at 5 epochs 证明 LP success 非 3-epoch artifact. 分歧在严重程度而非方向. 共识: 主文需明确 Few-NERD=3epochs 及原因, 但 severity 从 critical 降至 warning.\"\n  action_items:\n  - round: 18\n    action: \"(1) Section 4.1 明确: 'Few-NERD uses early stopping at epoch 3 (validation-loss optimum) while other datasets train for 5 epochs'; (2) Foreground that LP success persists at 5 epochs (+0.62pp) though attenuated; (3) 承认 training schedule modulates but does not create the LP selection phenomenon.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 维持; R2 REBUT (LoRA-rank 已做 interventional control).\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: Few-NERD 3 vs 5 epochs confound.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: Merged with R17-W2. R2 argues early stopping is standard practice, degeneracy IS training-modulated (论文 thesis 之一). R1 accepts 5-epoch control exists but wants matched-degeneracy comparison.\"\n  action_items:\n  - round: 18\n    action: \"Discussion 增加: degeneracy is jointly determined by task structure AND training convergence; practitioners have partial control via epoch/temperature.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 / 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"9 句话含过多技术细节.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: ~180 words 含 15+ 数字, 实验报告风格.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: R2-W3 仍提出 (~170 words, 8+ quantitative values). R1 部分反驳: 诊断性论文中数值 IS the contribution, 但同意中间机制数字 (median ρ=0.52, +0.52pp N-scaling) 可移除. 共识: 保留 4-5 核心数字, 移除 3-4 个.\"\n  action_items:\n  - round: 18\n    action: \"Abstract 保留: ~13pp headroom, +1.36pp (p<0.001), 14-47% degeneracy, ρ≈0.3 threshold. 移除: median ρ=0.52, +0.52pp N-scaling, 具体 AUROC 值.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"核心增量是 'why QE != selection' 的诊断.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 差异化不足, 叙述位置不够 upfront.\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18-R2: 'IMPROVED' — Introduction line 8 明确差异化定位.\"\n  action_items:\n  - round: 17\n    action: \"Introduction 第二段将 Yao et al. 差异化提前.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"'scale' 含义需澄清.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 70B+ 可能 degeneracy 更高, 整个方向可能无望.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 (R2-W4 + R1 AGREE): 4B-8B 覆盖有限. R1 补充: 8B degeneracy > 4B, 趋势可能延续到 70B+. 但 70B LP alignment 可能不同. 共识: Limitations 需更明确讨论.\"\n  action_items:\n  - round: 18\n    action: \"Limitations 增加: 'Larger models may exhibit higher degeneracy (consistent with 8B>4B trend) but potentially different LP alignment; the net effect on selection remains open.'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"m=3, exact p~0.028.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"主文加 caveat: 'though statistical precision is limited with m=3 raters'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + Bonferroni scope 争议\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 17\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Footnote 4 措辞需修正.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"Footnote 4 改为 'survives Bonferroni over 5 signal comparisons, conditional on pre-selected epsilon=0.05'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"论文已有 (a)-(d) 四个 hypotheses.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Table 4 SciERC full set vs Table 2 gold-filtered.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"Footnote 解释存在但容易被忽略.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 (R2-Q1 + R1 rebut): Protocol difference is deliberate (Table 2: controlled selection; Table 3: cross-dataset degeneracy). R1 同意可在 Table 3 caption 加粗 '(full-set evaluation)' 提高可见性.\"\n  action_items:\n  - round: 18\n    action: \"Table 3 caption 加粗 '(full-set evaluation; cf. gold-filtered protocol in Table 2)' 替代仅 footnote 说明.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"建议改名为 'Soft Overlap' 或加注释.\"\n  - round: 17\n    reviewers: [1]\n    note: \"R17: footnote 表述需微调.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Eikema argues utility design; 本文证明 utility IS aligned but degeneracy eliminates headroom.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 论文 Related Work 已有 Eikema 讨论.\"\n  action_items:\n  - round: 16\n    action: \"Related Work 增加 differentiation paragraph vs Eikema.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"greedy 'surpassing' 只反映 T=0 vs T=1 差异.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 15\n    action: \"修辞改为 'selection adds no benefit over greedy'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation: 8B vs 4B degeneracy 差异的解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"LoRA-rank ablation 是 interventional evidence.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 (R1-W5 + R2 AGREE): LoRA-rank simultaneously changes capacity + degeneracy, cannot cleanly attribute. Temperature ablation (T=1.2) is cleaner. 建议 T=1.2 作为 primary evidence, LoRA-rank 作为 supplementary.\"\n  action_items:\n  - round: 18\n    action: \"Section 5.4/Discussion: foreground T=1.2 ablation as primary within-dataset evidence for alignment condition; LoRA-rank as supplementary (acknowledge capacity confound).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"呈现应更平衡.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 16\n    action: \"Section 4.3 增加 harmful selection 讨论.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W4\n  summary: \"Discussion section 过长, 部分内容应移入 Appendix\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 14 个 sub-topics.\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18-R2: 'IMPROVED' — 现已压缩至 7 个子话题, 结构清晰.\"\n  action_items:\n  - round: 17\n    action: \"Discussion 移入 Appendix: N-scaling, temperature, verbalized confidence, signal combinations.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: \"Supervised verifier baseline 使用 5 个 scalar features 过于受限, 结论过度泛化\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 5 features 中 4 个 instance-level, 不能泛化.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W6 + R2 AGREE): 'Bottleneck lies in what signals encode' 仅对这 5 个 features 成立. Hidden states / attention / entity embeddings 有完全不同的 capacity. Scope conclusion to 'these five unsupervised signals'.\"\n  action_items:\n  - round: 18\n    action: \"Section 5.4 结论改为: 'the bottleneck lies in what these five unsupervised signals encode, not how they are aggregated; whether content-aware features (hidden states, entity embeddings) can close the gap remains open.'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M1\n  summary: \"Abstract 中 MBR 缩写未展开\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 当前 Abstract 未使用 MBR 缩写 (改为 full term). 待确认.\"\n  action_items:\n  - round: 17\n    action: \"确认 Abstract 中 MBR 是否仍存在; 如有则展开.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: \"Table 3 中 EM 和 VC 的 p 值标为 '---' 但未解释原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 17\n    action: \"Table 3 caption 或 footnote 解释 EM/VC 无 p 值原因.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M3\n  summary: \"Figure 3 '~15%' degeneracy threshold 缺乏精确定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"Dashed line 位置应有 explicit justification.\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18-R2 小问题 #2: footnote 仅引用 Person/Art 两个 type 边界 (n=2), 统计支撑有限.\"\n  action_items:\n  - round: 18\n    action: \"Figure caption 说明 15% 来源: empirical boundary between Person (13.4%, +1.25pp) and Art (19.8%, -0.17pp); acknowledge exploratory.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 18) =====\n- id: R18-N1\n  summary: \"Instance degeneracy 定义操作性模糊: prose 说 'identical outputs' 但实际操作是 'identical F1'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W7 + R2 AGREE): Abstract 'identical outputs' vs Table footnote 'identical instance-level F1' 是不同操作 (两个不同 entity set 可产生相同 F1). Table diversity: Identical outputs=11% vs Table degeneracy: Constant F1=17.8% 证实两定义产生不同集合. 误导读者.\"\n  action_items:\n  - round: 18\n    action: \"首次使用时明确: 'instance degeneracy (the fraction of instances where all N samples receive identical F1 scores, regardless of output identity)'. Abstract 不再使用 'identical outputs'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-N2\n  summary: \"LoRA rank=8 ablation 同时改变 capacity 和 degeneracy, 无法做 clean causal attribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W5 + R2 AGREE): rank=8 同时降低 capacity (greedy F1 0.645→0.640) 和改变 training dynamics. ρ≈0.24 可能是 insufficient capacity 而非证据 for separate 'alignment' condition. T=1.2 ablation (same model, same dataset, only changes temperature) 提供更 clean 的证据 (degeneracy 12.5%, ρ=0.225). 建议 T=1.2 作为 primary.\"\n  action_items:\n  - round: 18\n    action: \"Section 5.4: (1) 承认 LoRA-rank ablation 的 capacity confound; (2) foreground T=1.2 as primary evidence for alignment condition; (3) LoRA-rank as supplementary (同时改变多个变量).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-N3\n  summary: \"4 个 orphan bib entries 未被引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [2]\n    note: \"R2 格式检查发现: bhattacharyya2026beyond, malinin2021uncertainty, ren2023selfevaluation, zhang2025conformal 未在正文/appendix 引用.\"\n  action_items:\n  - round: 18\n    action: \"清理或引用这 4 个 orphan bib entries.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-N4\n  summary: \"缺失引用: Diverse Beam Search (Vijayakumar 2018) 与 degeneracy 直接相关\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1 建议 Shi et al. 2022 (MBR for code), Eisenstein et al. 2023 (reward ensembles). R2 建议 Vijayakumar et al. 2018 (Diverse Beam Search), conformal prediction for set-valued outputs. 至少前两类应添加.\"\n  action_items:\n  - round: 18\n    action: \"Related Work 补充: (1) MBR 在 non-MT structured outputs 的应用; (2) diverse decoding 与 degeneracy 的关系.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
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
    "issues_yaml": "issues:\n# ===== RESOLVED ISSUES (Rounds 0-18, abbreviated) =====\n- id: R0-C1\n  summary: \"模型规模单一（仅 8B）\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 确认措辞修正到位\"\n  resolution_round: 2\n- id: R0-C2\n  summary: \"相关工作显著遗漏\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认 49 条 bib 全部 cited\"\n  resolution_round: 2\n- id: R0-C4\n  summary: \"SJ 方法新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 确认三点差异化清晰\"\n  resolution_round: 2\n- id: R0-C5\n  summary: \"全文零图表\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"论文已包含 6 个 figures\"\n  resolution_round: 1\n- id: R0-C6\n  summary: \"成本分析 negligible 误导\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W1\n  summary: \"未探索 signal combination\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"Round 1+ 未再提及\"\n  resolution_round: 1\n- id: R0-W4\n  summary: \"统计检验不系统\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 1\n  resolution: \"Round 2 Reviewer 评价 bootstrap 达到高标准\"\n  resolution_round: 2\n- id: R3-W4\n  summary: \"FK independence 假设未验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 8\n  resolution: \"Appendix instance-level permutation test (n=529-2756, p<0.001) 验证\"\n  resolution_round: 9\n- id: R3-W5\n  summary: \"Cross-model scope 过宽\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"标题改为当前版本，scope 限定\"\n  resolution_round: 9\n- id: R4-W3\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  resolution: \"Abstract 压缩为 problem-finding-significance 结构\"\n  resolution_round: 9\n- id: R5-N1\n  summary: \"贡献框架偏 incremental\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  resolution: \"贡献重新框架化为 finding-led\"\n  resolution_round: 9\n- id: R7-W1\n  summary: \"LP temperature 依赖未说明\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Appendix 排除 LP + Limitations 扩展说明\"\n  resolution_round: 9\n- id: R7-W3\n  summary: \"Eikema Related Work 覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 7\n  resolution: \"Related Work 增加 Eikema 讨论\"\n  resolution_round: 9\n- id: R8-N1\n  summary: \"页数超限\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"主文在限制内\"\n  resolution_round: 9\n- id: R8-W2\n  summary: \"Thinking token 对 LP 影响未分析\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix 3-part quantitative analysis 已补充\"\n  resolution_round: 9\n- id: R8-W3\n  summary: \"SJ normalizer 选择敏感性\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  resolution: \"Appendix table delta-rho<0.005 证明不敏感\"\n  resolution_round: 9\n- id: R9-W1\n  summary: \"缺少其他 per-sample signal baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Limitations 承认 + verbalized confidence 实验已补充 (Appendix K)\"\n  resolution_round: 9\n- id: R9-W3\n  summary: \"TOST 等价性结论 configuration-dependent 未整合进正文\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 已含 config-dependent note\"\n  resolution_round: 9\n- id: R9-W4\n  summary: \"VC majority-voting selection 失败机制未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Discussion 已补 MBR mode-seeking bias 分析\"\n  resolution_round: 9\n- id: R9-W5\n  summary: \"多重比较校正不完整\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 footnote 说明校正策略\"\n  resolution_round: 9\n- id: R9-W6\n  summary: \"Table 1 主表单种子未标注\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 1 caption 加 cross-ref\"\n  resolution_round: 9\n- id: R9-W7\n  summary: \"Scale ablation not-model-capacity 结论过强\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"弱化为 within the 4B-8B range\"\n  resolution_round: 9\n- id: R9-M1\n  summary: \"Table 2 Greedy 术语歧义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Table 2 caption 标注 T=1.0 sample\"\n  resolution_round: 9\n- id: R9-M2\n  summary: \"FK 负依赖数值无推导\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"引用 Appendix permutation test\"\n  resolution_round: 9\n- id: R9-M3\n  summary: \"correlation-selection gap 术语无操作性定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"Section 4.2 给出操作性定义\"\n  resolution_round: 9\n- id: R9-W2\n  summary: \"orphan bib entries 未在正文引用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 13\n  resolution: \"R13 确认 50 entries, 0 orphan\"\n  resolution_round: 13\n- id: R11-M3\n  summary: \"缺失引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"所有缺失引用已补充. R13 确认 50 entries, 0 orphan, 0 missing.\"\n  resolution_round: 13\n- id: R11-W4\n  summary: \"缺少信号组合实验 / entity-token-only LP 未测试\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 13\n  resolution: \"Entity-token LP 实验已完成并纳入 Discussion (4x variance, selection -2.0pp, CoNLL collapse)\"\n  resolution_round: 13\n- id: R11-W5\n  summary: \"Preliminary 标注过于频繁\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 12\n  resolution: \"论文已统一使用 dagger-RE 标记系统替代反复 preliminary\"\n  resolution_round: 13\n- id: R11-W7\n  summary: \"缺少 greedy decoding baseline\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  resolution: \"Greedy (T=0) F1=0.663 已加入 Table 2. 修辞问题见 R14-W2.\"\n  resolution_round: 14\n- id: R12-M1\n  summary: \"Discussion LP hypotheses 标注 three mechanisms 但实际列出四个\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"论文已修正为 'four (non-mutually-exclusive) mechanisms'\"\n  resolution_round: 14\n- id: R12-M3\n  summary: \"oh2025latentsc bib year 应更新为 2026\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  resolution: \"R14 确认 bib key oh2026latentsc 年份正确 (AAAI 2026)\"\n  resolution_round: 14\n- id: R13-W1\n  summary: \"RE 覆盖策略不统一: 出现在主表+Abstract 但仅单 benchmark\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"RE 已移至 Appendix E 作为 exploratory extension. 标题/Abstract/主表均聚焦 NER.\"\n  resolution_round: 14\n- id: R13-M1\n  summary: \"Bib 年份/作者问题\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  resolution: \"R14 审核确认主要 bib entries 正确\"\n  resolution_round: 14\n- id: R14-N2\n  summary: \"缺少两篇直接相关文献: Schall & de Melo (RANLP 2025) + Yun et al. (EMNLP Findings 2025)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 15\n  resolution: \"R15 确认 schall2025hidden, yun2025price, park2024grammar 均已引用于 Related Work.\"\n  resolution_round: 15\n- id: R17-W1\n  summary: \"LoRA rank=8 下 LP compression 统计数据缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"R18 确认 LP range 0.057 vs 0.041 nats 已报告 (Section 5.4)\"\n  resolution_round: 18\n- id: R14-M1\n  summary: \"Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"R18 确认: Random 从 T=1.0 samples 均匀选取, Greedy 是 T=0 argmax. 差异来自 T=1.0 quality degradation. 已在正文解释.\"\n  resolution_round: 18\n- id: R16-N2\n  summary: \"rho=0.42 在 Abstract/Figure 1 与 Table 1 之间数值矛盾\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 18\n  resolution: \"R18-R2 确认: ρ=0.38 是 SciERC VC, ρ=0.42 是 Few-NERD LP, 不同 dataset 无矛盾. Figure 1 caption 已正确归属.\"\n  resolution_round: 18\n- id: R12-N1\n  summary: \"rho headline 来自 ceiling-effect dataset / 数值不一致\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 18\n  resolution: \"R18-R2 确认 headline rho 归属正确: 0.38=SciERC primary, 0.42=Few-NERD.\"\n  resolution_round: 18\n- id: R14-M3\n  summary: \"Correlation-selection gap 操作性定义出现在 Section 4.3, 但 Abstract/Intro 已大量使用\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 14\n  last_seen_round: 18\n  resolution: \"R18-R2 确认 Introduction line 13 括号内定义到位.\"\n  resolution_round: 18\n- id: R11-N3\n  summary: \"Abstract LP compression intrinsic 措辞被 RE free-form reversal 削弱\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 18\n  resolution: \"R18-R2 确认 Discussion 正确区分 NER/RE; free-form ablation confirms NER compression non-constraint-imposed.\"\n  resolution_round: 18\n- id: R17-W3\n  summary: \"em-dash (---) 使用约 90 处, AI 写作风格痕迹显著\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: \"R18-R2 格式合规检查确认: 零处解释性 em-dash, AI 写作痕迹已清零.\"\n  resolution_round: 18\n\n# ===== RECURRING ISSUES (updated Round 18) =====\n- id: R0-C3\n  summary: \"Selection gap effective test bed 仅 SciERC 单数据集\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 0\n  last_seen_round: 18\n  mentions:\n  - round: 0\n    reviewers: [1, 2]\n    note: \"需跨数据集验证或降级措辞\"\n  - round: 4\n    reviewers: [1, 2]\n    note: \"claim 降级到位\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Conclusion hedge 到位\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R11 fresh review 再次提出\"\n  - round: 12\n    reviewers: [1, 2]\n    note: \"R12 强共识: 标题限定 NER 或增 RE dataset\"\n  - round: 13\n    reviewers: [1, 2]\n    note: \"R13 强共识: Selection gap effective test bed 仅 SciERC (n=529).\"\n  - round: 14\n    reviewers: [1, 2]\n    note: \"R14 强共识: CoNLL 是 ceiling-effect control, WNUT collapse.\"\n  - round: 15\n    reviewers: [1, 2]\n    note: \"R15 强共识: 核心 finding 实质仅 SciERC 验证.\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16: 论文已加入 Few-NERD. 但 positive finding 仅 1 model x 1 N x 1 dataset.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: Few-NERD 加入后 dataset 覆盖改善, 但 cross-dataset degeneracy gradient 仍仅 n=3.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: R1 'Partially resolved' — 4 datasets 均展示 structural signal failure, 但 LP positive result 仅 Few-NERD. Cross-dataset gradient 仍 n=3. R2 确认覆盖改善.\"\n  action_items:\n  - round: 17\n    action: \"增加 1-2 个 NER 数据集扩大 degeneracy gradient 的 n; 或将 cross-dataset gradient 明确标注为 exploratory.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R3-W2\n  summary: \"Gap 概念部分 tautological: instance-level 信号 selection 失败是定义必然; MBR empirical failure 被掩盖\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 18\n  mentions:\n  - round: 3\n    reviewers: [1, 2]\n    note: \"需分离两层论证\"\n  - round: 9\n    reviewers: [1, 2]\n    note: \"Abstract/Intro reframe 完成\"\n  - round: 11\n    reviewers: [1, 2]\n    note: \"R2 认为 Contribution 1 仍含 definitional 成分\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R16 强共识: 标题暗示意外发现但 4/5 signals weakness 部分 by construction.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 纯诊断性贡献对 main conference 门槛偏弱.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识: Layer 1 ('cannot rank by construction') 是定义推论非实验发现. Introduction 已称 'methodological premise' 但 Abstract/Contributions 仍包装为 three-layer 第一层. 问题在于与实证发现并列计数夸大分析深度. 建议 Contribution 2 改为 'Two empirical mechanisms (degeneracy, alignment) that block the sole per-sample signal'.\"\n  action_items:\n  - round: 18\n    action: \"将 three-layer 重构为: (1) methodological premise (not counted as contribution); (2) two empirical mechanisms. Abstract/Contribution 列表中不再将 'by construction' 作为独立发现列出.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R16-N1\n  summary: \"Degeneracy-gating monotonic claim 仅 3 dataset-level 数据点, 统计不显著\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 16\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"3 个 dataset-level 数据点无统计意义.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: Figure 3 pooled correlation 混合两个粒度, entity-type-level n=8 有 independence 问题.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识: (R1-W2 + R1-W3) n=3 不能 'establish' 因果; 任何 3 有序数字 trivially monotonic; datasets differ on ≥5 confounded dimensions. Entity-type ρ=-0.881 (p=0.004) 有 non-independence (shared model/tokenizer/temp), effective df<6, p 可能高估 5-10x. 建议: (1) 'consistent with' 非 'establishes'; (2) permutation test 或承认 non-independence; (3) controlled ablations (T, LoRA) 作为 primary 证据.\"\n  action_items:\n  - round: 18\n    action: \"(1) 'establishes' → 'is consistent with' / 'inversely associated with'; (2) entity-type p=0.004 加 caveat 'assuming independence; non-independence may inflate by up to 10x'; (3) foreground T-ablation 和 LoRA-rank as controlled within-dataset evidence, cross-dataset as supporting observation.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W1\n  summary: \"Fisher combined p (2-seed) / sign test 统计效力极低\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"SciERC null result 应改为 'effect small and not reliably detected'.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 负面结果缺少 power analysis. n=529, 2 seeds 检测 1pp 效应的 power 约 50-60%.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W1 + R2 AGREE): SciERC p=0.29 无法区分 'no effect' vs 'underpowered'. N-scaling 表显示 +0.42→+0.63→+0.91pp (N=8→16→32) suggesting small real effect. 三路梯度中间点 (18%→weak) 依赖此 null 是 genuine. Few-NERD (n=32,565) 才是 definitive. 建议: 报告 MDE at 80% power; 调整 framing 优先级 (Few-NERD first).\"\n  action_items:\n  - round: 18\n    action: \"(1) 报告 SciERC minimum detectable effect at 80% power (likely ~1.5-2pp); (2) 改 'fails' → 'insufficient evidence for gains below ~1.5pp at this sample size'; (3) Abstract/Introduction 先呈现 Few-NERD positive 再呈现 SciERC inconclusive.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W1\n  summary: \"纯诊断无 remedy 尝试, 限制论文 impact\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"多种 remedy 已测试并全部 negative.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 纯诊断性论文缺乏 positive contribution. 已测试 entity-token LP, LP x VC, supervised combination, verbalized confidence, 全部 negative.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R2-W1 + R1 AGREE): 纯诊断+negative result 对 EMNLP main conference 门槛不足. Supervised verifier baseline 是 straw-man (5 scalar features). Practical guidelines (degeneracy check) 有价值但 modest. 需至少一个 non-trivial positive contribution. 但 R1 也注意到 scope creep 风险.\"\n  action_items:\n  - round: 18\n    action: \"(1) Reframe Few-NERD LP +1.36pp 为 primary practical finding (not just diagnostic evidence); (2) 提供明确 practitioners' decision rule; (3) 考虑训练简单 learned verifier (如 entity embedding scorer) 展示 oracle gap 部分可回收性 — 即使 5-10% 也大幅增强贡献叙事.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W2\n  summary: \"Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露, 可能 confound degeneracy 比较\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17 强共识: 主文说 '5 epochs' 暗示统一, Appendix 才披露 3 epochs.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: R1-W4 视为 Major (5-epoch control incomplete, performance-regime confound). R2 部分反驳: 3-epoch = validation-loss early stopping 是标准实践; 5-epoch ablation IS the controlled experiment showing degeneracy mechanism; +0.62pp at 5 epochs 证明 LP success 非 3-epoch artifact. 分歧在严重程度而非方向. 共识: 主文需明确 Few-NERD=3epochs 及原因, 但 severity 从 critical 降至 warning.\"\n  action_items:\n  - round: 18\n    action: \"(1) Section 4.1 明确: 'Few-NERD uses early stopping at epoch 3 (validation-loss optimum) while other datasets train for 5 epochs'; (2) Foreground that LP success persists at 5 epochs (+0.62pp) though attenuated; (3) 承认 training schedule modulates but does not create the LP selection phenomenon.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-N1\n  summary: \"Instance degeneracy 可能是 fine-tuning recipe artifact 而非 capability-intrinsic\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"R1 维持; R2 REBUT (LoRA-rank 已做 interventional control).\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: Few-NERD 3 vs 5 epochs confound.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: Merged with R17-W2. R2 argues early stopping is standard practice, degeneracy IS training-modulated (论文 thesis 之一). R1 accepts 5-epoch control exists but wants matched-degeneracy comparison.\"\n  action_items:\n  - round: 18\n    action: \"Discussion 增加: degeneracy is jointly determined by task structure AND training convergence; practitioners have partial control via epoch/temperature.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-W2\n  summary: \"Abstract 信息过度压缩 / 过载\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"9 句话含过多技术细节.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: ~180 words 含 15+ 数字, 实验报告风格.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18: R2-W3 仍提出 (~170 words, 8+ quantitative values). R1 部分反驳: 诊断性论文中数值 IS the contribution, 但同意中间机制数字 (median ρ=0.52, +0.52pp N-scaling) 可移除. 共识: 保留 4-5 核心数字, 移除 3-4 个.\"\n  action_items:\n  - round: 18\n    action: \"Abstract 保留: ~13pp headroom, +1.36pp (p<0.001), 14-47% degeneracy, ρ≈0.3 threshold. 移除: median ρ=0.52, +0.52pp N-scaling, 具体 AUROC 值.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W1\n  summary: \"与 Yao et al. (2026) 增量贡献定义不够清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"核心增量是 'why QE != selection' 的诊断.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 差异化不足, 叙述位置不够 upfront.\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18-R2: 'IMPROVED' — Introduction line 8 明确差异化定位.\"\n  action_items:\n  - round: 17\n    action: \"Introduction 第二段将 Yao et al. 差异化提前.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W2\n  summary: \"Scale range (3B-8B) 不足以支撑普适性结论\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"'scale' 含义需澄清.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 70B+ 可能 degeneracy 更高, 整个方向可能无望.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 (R2-W4 + R1 AGREE): 4B-8B 覆盖有限. R1 补充: 8B degeneracy > 4B, 趋势可能延续到 70B+. 但 70B LP alignment 可能不同. 共识: Limitations 需更明确讨论.\"\n  action_items:\n  - round: 18\n    action: \"Limitations 增加: 'Larger models may exhibit higher degeneracy (consistent with 8B>4B trend) but potentially different LP alignment; the net effect on selection remains open.'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W3\n  summary: \"3 seeds 统计效力不足 (Kendall W)\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"m=3, exact p~0.028.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"主文加 caveat: 'though statistical precision is limited with m=3 raters'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R7-C2\n  summary: \"epsilon=0.05 threshold 依赖性 + Bonferroni scope 争议\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 17\n  mentions:\n  - round: 7\n    reviewers: [1, 2]\n    note: \"threshold 无 prior justification\"\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Footnote 4 措辞需修正.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 保持 R16 action.\"\n  action_items:\n  - round: 16\n    action: \"Footnote 4 改为 'survives Bonferroni over 5 signal comparisons, conditional on pre-selected epsilon=0.05'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W6\n  summary: \"LP compression 缺乏 mechanistic explanation\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"论文已有 (a)-(d) 四个 hypotheses.\"\n  - round: 17\n    reviewers: []\n    note: \"R17 未被独立提及.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"(b) 和 (d) 之间添加说明 constraint-imposed vs model-learned 的区别.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-W8\n  summary: \"Thinking token CoNLL control 论证薄弱\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"弱化 CoNLL control 论证或补充 task easiness 混淆说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M1\n  summary: \"Selection table NER 2-seed vs RE single seed 未说明原因\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 12\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 12\n    action: \"在 footnote 解释 NER/RE seed 数量不对称原因\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R11-M2\n  summary: \"Figure 1 caption 对 LP per-sample signal 不适用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 11\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 11\n    action: \"修改 Figure 1 caption\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-W2\n  summary: \"Gold-empty instance filtering 在 QE 和 Selection 之间不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Table 4 SciERC full set vs Table 2 gold-filtered.\"\n  - round: 17\n    reviewers: [1, 2]\n    note: \"Footnote 解释存在但容易被忽略.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 (R2-Q1 + R1 rebut): Protocol difference is deliberate (Table 2: controlled selection; Table 3: cross-dataset degeneracy). R1 同意可在 Table 3 caption 加粗 '(full-set evaluation)' 提高可见性.\"\n  action_items:\n  - round: 18\n    action: \"Table 3 caption 加粗 '(full-set evaluation; cf. gold-filtered protocol in Table 2)' 替代仅 footnote 说明.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R12-M2\n  summary: \"Soft Jaccard 命名不准确 (分母是 max 不是 union)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"建议改名为 'Soft Overlap' 或加注释.\"\n  - round: 17\n    reviewers: [1]\n    note: \"R17: footnote 表述需微调.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 12\n    action: \"改名或首次出现时明确说明\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R13-M2\n  summary: \"Table 2 caption 'Fisher p' vs Appendix 'Fisher combined p' 术语不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 13\n    action: \"统一 Fisher p 术语\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-N1\n  summary: \"Correlation-selection gap 与 MBR 社区已知结论的关系\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"Eikema argues utility design; 本文证明 utility IS aligned but degeneracy eliminates headroom.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 论文 Related Work 已有 Eikema 讨论.\"\n  action_items:\n  - round: 16\n    action: \"Related Work 增加 differentiation paragraph vs Eikema.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W2\n  summary: \"Greedy (T=0) vs sampling+selection 比较修辞过强\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: []\n    note: \"greedy 'surpassing' 只反映 T=0 vs T=1 差异.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 15\n    action: \"修辞改为 'selection adds no benefit over greedy'.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-W3\n  summary: \"4B scale ablation: 8B vs 4B degeneracy 差异的解释\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 18\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"LoRA-rank ablation 是 interventional evidence.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 (R1-W5 + R2 AGREE): LoRA-rank simultaneously changes capacity + degeneracy, cannot cleanly attribute. Temperature ablation (T=1.2) is cleaner. 建议 T=1.2 作为 primary evidence, LoRA-rank 作为 supplementary.\"\n  action_items:\n  - round: 18\n    action: \"Section 5.4/Discussion: foreground T=1.2 ablation as primary within-dataset evidence for alignment condition; LoRA-rank as supplementary (acknowledge capacity confound).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R14-M2\n  summary: \"主表 seed=42 单 seed vs multi-seed mean 选择不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 14\n    action: \"Table 1 caption 中更明确说明为何使用单 seed.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R15-W1\n  summary: \"TOST 等价性结论 configuration-dependent, 某些配置下 selection actively harmful\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 15\n  last_seen_round: 17\n  mentions:\n  - round: 16\n    reviewers: [1, 2]\n    note: \"呈现应更平衡.\"\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 16\n    action: \"Section 4.3 增加 harmful selection 讨论.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W4\n  summary: \"Discussion section 过长, 部分内容应移入 Appendix\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 14 个 sub-topics.\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18-R2: 'IMPROVED' — 现已压缩至 7 个子话题, 结构清晰.\"\n  action_items:\n  - round: 17\n    action: \"Discussion 移入 Appendix: N-scaling, temperature, verbalized confidence, signal combinations.\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-W5\n  summary: \"Supervised verifier baseline 使用 5 个 scalar features 过于受限, 结论过度泛化\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [1, 2]\n    note: \"R17: 5 features 中 4 个 instance-level, 不能泛化.\"\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W6 + R2 AGREE): 'Bottleneck lies in what signals encode' 仅对这 5 个 features 成立. Hidden states / attention / entity embeddings 有完全不同的 capacity. Scope conclusion to 'these five unsupervised signals'.\"\n  action_items:\n  - round: 18\n    action: \"Section 5.4 结论改为: 'the bottleneck lies in what these five unsupervised signals encode, not how they are aggregated; whether content-aware features (hidden states, entity embeddings) can close the gap remains open.'\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M1\n  summary: \"Abstract 中 MBR 缩写未展开\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. 当前 Abstract 未使用 MBR 缩写 (改为 full term). 待确认.\"\n  action_items:\n  - round: 17\n    action: \"确认 Abstract 中 MBR 是否仍存在; 如有则展开.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M2\n  summary: \"Table 3 中 EM 和 VC 的 p 值标为 '---' 但未解释原因\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 17\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 17\n    action: \"Table 3 caption 或 footnote 解释 EM/VC 无 p 值原因.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R17-M3\n  summary: \"Figure 3 '~15%' degeneracy threshold 缺乏精确定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 17\n  last_seen_round: 18\n  mentions:\n  - round: 17\n    reviewers: [2]\n    note: \"Dashed line 位置应有 explicit justification.\"\n  - round: 18\n    reviewers: [2]\n    note: \"R18-R2 小问题 #2: footnote 仅引用 Person/Art 两个 type 边界 (n=2), 统计支撑有限.\"\n  action_items:\n  - round: 18\n    action: \"Figure caption 说明 15% 来源: empirical boundary between Person (13.4%, +1.25pp) and Art (19.8%, -0.17pp); acknowledge exploratory.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M4\n  summary: \"rho rounding 不精确\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一小数位数\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M5\n  summary: \"Selection table NER/RE 统计标准不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 12\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及. RE 已移至 Appendix.\"\n  action_items:\n  - round: 9\n    action: \"统一统计报告标准\"\n    assigned_to: Paper Agent\n    status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R9-M6\n  summary: \"Bib name order issues\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n  - round: 18\n    reviewers: []\n    note: \"R18 未被独立提及.\"\n  action_items:\n  - round: 9\n    action: \"统一 bib 作者姓名格式\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== NEW ISSUES (Round 18) =====\n- id: R18-N1\n  summary: \"Instance degeneracy 定义操作性模糊: prose 说 'identical outputs' 但实际操作是 'identical F1'\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W7 + R2 AGREE): Abstract 'identical outputs' vs Table footnote 'identical instance-level F1' 是不同操作 (两个不同 entity set 可产生相同 F1). Table diversity: Identical outputs=11% vs Table degeneracy: Constant F1=17.8% 证实两定义产生不同集合. 误导读者.\"\n  action_items:\n  - round: 18\n    action: \"首次使用时明确: 'instance degeneracy (the fraction of instances where all N samples receive identical F1 scores, regardless of output identity)'. Abstract 不再使用 'identical outputs'.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-N2\n  summary: \"LoRA rank=8 ablation 同时改变 capacity 和 degeneracy, 无法做 clean causal attribution\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R18 强共识 (R1-W5 + R2 AGREE): rank=8 同时降低 capacity (greedy F1 0.645→0.640) 和改变 training dynamics. ρ≈0.24 可能是 insufficient capacity 而非证据 for separate 'alignment' condition. T=1.2 ablation (same model, same dataset, only changes temperature) 提供更 clean 的证据 (degeneracy 12.5%, ρ=0.225). 建议 T=1.2 作为 primary.\"\n  action_items:\n  - round: 18\n    action: \"Section 5.4: (1) 承认 LoRA-rank ablation 的 capacity confound; (2) foreground T=1.2 as primary evidence for alignment condition; (3) LoRA-rank as supplementary (同时改变多个变量).\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-N3\n  summary: \"4 个 orphan bib entries 未被引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [2]\n    note: \"R2 格式检查发现: bhattacharyya2026beyond, malinin2021uncertainty, ren2023selfevaluation, zhang2025conformal 未在正文/appendix 引用.\"\n  action_items:\n  - round: 18\n    action: \"清理或引用这 4 个 orphan bib entries.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R18-N4\n  summary: \"缺失引用: Diverse Beam Search (Vijayakumar 2018) 与 degeneracy 直接相关\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 18\n  last_seen_round: 18\n  mentions:\n  - round: 18\n    reviewers: [1, 2]\n    note: \"R1 建议 Shi et al. 2022 (MBR for code), Eisenstein et al. 2023 (reward ensembles). R2 建议 Vijayakumar et al. 2018 (Diverse Beam Search), conformal prediction for set-valued outputs. 至少前两类应添加.\"\n  action_items:\n  - round: 18\n    action: \"Related Work 补充: (1) MBR 在 non-MT structured outputs 的应用; (2) diverse decoding 与 degeneracy 的关系.\"\n    assigned_to: Paper Agent\n    status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1816 · 2026-05-18T01:46:16.592405+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 35440}, \"error\": \"\"}"}

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

_source line 1817 · 2026-05-18T01:47:52.269561+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 18 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**目标**: EMNLP 2026 Main Conference Long Paper (ARR May 2026)\n**截止**: 2026-05-25\n**Reviewers**: 2 人 (R1: 方法严谨性/统计分析; R2: 新颖性/写作/完整性)\n\n---\n\n## Summary\n\n本文研究五种 confidence signals 在 LLM-based NER 中的质量估计（QE）与样本选择（selection）表现。核心发现：所有信号都能可靠估计实例质量（ρ 最高 0.42, AUROC 0.82），但无法将 QE 优势转化为 best-of-N 选择增益（13pp oracle headroom 未被利用）。论文诊断出三层失败机制，识别 LP 选择成功的两个必要条件（低 degeneracy + 充足 alignment），在 Few-NERD 上验证正面发现（+1.36pp, p<0.001）。\n\n---\n\n## Strengths\n\n1. **QE 与 selection 的系统性分离**。填补文献中混淆这两个任务的空白，对 test-time compute scaling 社区有方法论价值。[强共识]\n\n2. **实验设计全面且统计严谨**。四数据集 difficulty gradient，两模型族，4B ablation，温度/N/LoRA-rank/epoch 多维消融。Bootstrap CI, TOST, Bonferroni, Fisher combined p, permutation tests 远超同类工作。[强共识]\n\n3. **Two-condition 分析框架优雅**。Degeneracy + alignment 的解耦分析有洞察力，Few-NERD (n=32,565) 提供高统计功效验证（>99% power, CI [+1.18, +1.53]）。[强共识]\n\n4. **诚实报告负面结果**。不过度宣传 LP 效用，清晰界定成功/失败条件。[强共识]\n\n5. **写作质量显著提升**。Em-dash 清零，Discussion 从 14 个子话题压缩至 7 个，术语定义到位，格式完全合规。[强共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix (blocking for Main Conference)\n\n**W1 [Critical] SciERC selection test 统计效力不足，negative result 被 over-stated。** [强共识: R1-W1 + R2 AGREE]\n- n=529, 2 seeds, ~55% power for 1pp effect. p=0.29 无法区分 \"no effect\" vs \"underpowered\"\n- N-scaling (+0.42→+0.91pp at N=8→32) suggests small but real effect\n- 三路梯度中间点（18%→weak）依赖此 null 为 genuine\n- **Action**: 报告 MDE at 80% power; reframe \"fails\"→\"insufficient evidence below ~1.5pp\"; Abstract/Intro 先呈现 Few-NERD positive\n\n**W2 [Critical] Cross-dataset degeneracy gradient: n=3 因果推断过强 + entity-type non-independence。** [强共识: R1-W2/W3 + R2 AGREE]\n- 3 dataset-level 数据点 trivially monotonic; datasets confounded on ≥5 dimensions\n- Entity-type ρ=-0.881 (p=0.004) 违反 independence (shared model/tokenizer/temp); effective df<6; p 可能高估 5-10x\n- **Action**: \"establishes\"→\"is consistent with\"; entity-type p 加 non-independence caveat; foreground T-ablation as controlled evidence; cross-dataset 降级为 exploratory\n\n**W3 [Critical] Three-layer gap 中 Layer 1 是 definitional, 接近 tautological。** [强共识: R1 AGREE + R2-W2]\n- \"Instance-level signals cannot rank by construction\" 是定义推论非实验发现\n- 与 empirical Layers 2-3 并列计数夸大分析深度\n- **Action**: Reframe as methodological premise; Contributions 改为 two empirical mechanisms\n\n**W4 [Critical] 纯诊断性论文缺乏 positive contribution，venue-fit 风险。** [强共识: R2-W1 + R1 AGREE]\n- 核心结论 = \"现有信号不 work\"; supervised verifier baseline (5 scalar features) 是 straw-man\n- LP +1.36pp modest; actionable takeaway 有限\n- **Action**: Reframe Few-NERD LP as primary practical finding; 提供 practitioners' decision rule; 考虑 lightweight learned verifier\n\n### Should-Fix (important for acceptance)\n\n**W5 [Warning] Few-NERD 3-epoch training confound。** [分歧: R1 Major, R2 部分反驳]\n- 3 epochs = early stopping (标准实践); 5-epoch control shows LP still works (+0.62pp)\n- 但主文未披露 3-epoch fact; performance-regime confound (greedy F1 0.748 vs 0.777)\n- **Action**: Section 4.1 明确披露; foreground 5-epoch still positive\n\n**W6 [Warning] LoRA rank=8 ablation conflates capacity and degeneracy。** [强共识: R1-W5 + R2 AGREE]\n- rank=8 同时改变 model capacity; lower ρ≈0.24 可能 = insufficient capacity\n- T=1.2 ablation 更 clean (same model, degeneracy 12.5%, ρ=0.225)\n- **Action**: T=1.2 为 primary evidence; LoRA-rank 承认 capacity confound\n\n**W7 [Warning] Supervised verifier 结论过度泛化。** [强共识: R1-W6 + R2 AGREE]\n- \"Bottleneck lies in what signals encode\" 仅对 5 个 features 成立\n- Hidden states / entity embeddings 有完全不同 capacity\n- **Action**: Scope to \"these five unsupervised signals\"\n\n**W8 [Warning] Abstract 信息密度仍过高。** [部分分歧: R2-W3, R1 部分反驳]\n- ~170 words, 8+ 定量值; R1 认为部分数值 IS contribution\n- 共识: 保留 4-5 核心数字, 移除中间机制数字\n\n**W9 [Warning] 模型规模 4B-8B 覆盖有限。** [共识: R2-W4 + R1 AGREE]\n- 8B degeneracy > 4B, 70B+ 可能更严重; LP alignment 方向不确定\n- **Action**: Limitations 增加 scale extrapolation discussion\n\n**W10 [Warning] Instance degeneracy 定义操作性模糊。** [强共识: R1-W7 + R2 AGREE]\n- Prose \"identical outputs\" vs operation \"identical F1\"; Table diversity (11%) ≠ Table degeneracy (17.8%)\n- **Action**: 首次使用时明确 \"identical F1\" 非 \"identical outputs\"\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. Overall 3.0/5 (Findings-level) — 两位 Reviewer 独立达成相同评分\n2. 纯诊断性质 + straw-man verifier 限制了 Main Conference 竞争力\n3. 统计 claims 需系统性 softening (establishes→consistent with; fails→insufficient evidence)\n4. QE/selection 分离的方法论贡献 + Few-NERD 验证是真实有价值的\n5. 写作质量和实验设计执行层面达到高标准\n6. LoRA-rank confound: T=1.2 应为 primary evidence\n\n## Reviewer Divergence [REBUT]\n\n1. **Abstract 数字密度** (轻微): R2 认为过多 (8+ 数字); R1 认为诊断论文需要数值但同意中间机制数字可移除. 共识: 减至 4-5 个.\n2. **Few-NERD epoch confound severity** (中度): R1 视为 Major (performance-regime confound, matched-degeneracy 比较缺失); R2 视为 well-designed control showing the mechanism works (LP still +0.62pp at 5 epochs). 共识: 需主文披露, 但 severity ≤ warning.\n\n---\n\n## Questions for Authors\n\n1. SciERC within-instance ρ(LP,F1)=0.248 vs Few-NERD ρ≈0.5 差异是否由 entity boundary clarity 解释？有无 SciERC per-type alignment 数据？\n2. SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79) 与 cross-dataset 和 within-Few-NERD 的 strong negative correlation 如何 reconcile？\n3. Supervised verifier 在 Few-NERD (32K instances) 上训练是否结果不同？\n4. Entity-token LP 方差 4× 但选择更差: if higher variance doesn't help, is compression truly the bottleneck, or is it representation-level determinism?\n\n---\n\n## Missing References\n\n- Vijayakumar et al. (2018) \"Diverse Beam Search\" — 直接关联 degeneracy/diversity\n- Shi et al. (2022) MBR for code generation — structured output MBR\n- Eisenstein et al. (2023) reward model ensembles — signal limitation\n- 4 个 orphan bib entries 需清理: bhattacharyya2026beyond, malinin2021uncertainty, ren2023selfevaluation, zhang2025conformal\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**Overall: 3.0/5 — Findings-level (weak reject for Main Conference)**\n\n**置信度**: 4/5 (高)\n\n**一句话**: 方法论严谨的诊断性论文，成功揭示 QE/selection disconnect，但纯诊断性质（无 remedy）、统计 claims 过强（n=3 因果、underpowered null = \"fail\"、non-independence）、以及 Layer 1 tautological 限制其达到 Main Conference 门槛。适合 Findings track。\n\n**升级路径** (非建议，仅记录 Reviewer 共识):\n- 统计 claims 系统性 softening\n- Reframe three-layer → methodological premise + two empirical mechanisms\n- 补充至少一个 non-trivial positive contribution (learned verifier 或 LP practitioners' rule 的正式化)\n- Few-NERD LP +1.36pp reframe 为 primary finding 而非仅诊断证据\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 保留 4-5 核心数字 (headroom, +1.36pp, degeneracy range, ρ threshold)\n- 移除: ρ up to 0.38, +0.52pp N-scaling, MBR utility ρ=0.52\n- \"identical outputs\" → \"identical F1 scores\"\n\n### Introduction\n- Contribution 2 \"three-layer\" → methodological premise + two empirical layers\n- \"establishes\" → \"is consistent with\"\n- 先 Few-NERD positive, 再 SciERC inconclusive\n\n### Method\n- Instance degeneracy 操作性定义首次出现时明确\n\n### Experiments\n- Section 4.1: 明确 Few-NERD = 3 epochs (early stopping)\n- Table 3 caption 加粗 \"(full-set evaluation)\"\n- Table 2 EM/VC 无 p 值原因说明\n\n### Discussion\n- T=1.2 ablation 作为 alignment condition 的 primary evidence\n- LoRA-rank: 承认 capacity confound\n- Supervised verifier: scope to \"these five features\"\n- Figure 2: 15% threshold 来源说明\n\n### Limitations\n- Scale extrapolation: 70B+ degeneracy 可能更高但 alignment 未知\n- SciERC MDE at 80% power\n\n### References\n- 清理 4 个 orphan entries\n- 补充 diverse decoding / structured MBR 文献",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "weak reject",
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
    "report": "# Round 18 审稿报告 — struct_self_consist_ie\n\n**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction\n**目标**: EMNLP 2026 Main Conference Long Paper (ARR May 2026)\n**截止**: 2026-05-25\n**Reviewers**: 2 人 (R1: 方法严谨性/统计分析; R2: 新颖性/写作/完整性)\n\n---\n\n## Summary\n\n本文研究五种 confidence signals 在 LLM-based NER 中的质量估计（QE）与样本选择（selection）表现。核心发现：所有信号都能可靠估计实例质量（ρ 最高 0.42, AUROC 0.82），但无法将 QE 优势转化为 best-of-N 选择增益（13pp oracle headroom 未被利用）。论文诊断出三层失败机制，识别 LP 选择成功的两个必要条件（低 degeneracy + 充足 alignment），在 Few-NERD 上验证正面发现（+1.36pp, p<0.001）。\n\n---\n\n## Strengths\n\n1. **QE 与 selection 的系统性分离**。填补文献中混淆这两个任务的空白，对 test-time compute scaling 社区有方法论价值。[强共识]\n\n2. **实验设计全面且统计严谨**。四数据集 difficulty gradient，两模型族，4B ablation，温度/N/LoRA-rank/epoch 多维消融。Bootstrap CI, TOST, Bonferroni, Fisher combined p, permutation tests 远超同类工作。[强共识]\n\n3. **Two-condition 分析框架优雅**。Degeneracy + alignment 的解耦分析有洞察力，Few-NERD (n=32,565) 提供高统计功效验证（>99% power, CI [+1.18, +1.53]）。[强共识]\n\n4. **诚实报告负面结果**。不过度宣传 LP 效用，清晰界定成功/失败条件。[强共识]\n\n5. **写作质量显著提升**。Em-dash 清零，Discussion 从 14 个子话题压缩至 7 个，术语定义到位，格式完全合规。[强共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix (blocking for Main Conference)\n\n**W1 [Critical] SciERC selection test 统计效力不足，negative result 被 over-stated。** [强共识: R1-W1 + R2 AGREE]\n- n=529, 2 seeds, ~55% power for 1pp effect. p=0.29 无法区分 \"no effect\" vs \"underpowered\"\n- N-scaling (+0.42→+0.91pp at N=8→32) suggests small but real effect\n- 三路梯度中间点（18%→weak）依赖此 null 为 genuine\n- **Action**: 报告 MDE at 80% power; reframe \"fails\"→\"insufficient evidence below ~1.5pp\"; Abstract/Intro 先呈现 Few-NERD positive\n\n**W2 [Critical] Cross-dataset degeneracy gradient: n=3 因果推断过强 + entity-type non-independence。** [强共识: R1-W2/W3 + R2 AGREE]\n- 3 dataset-level 数据点 trivially monotonic; datasets confounded on ≥5 dimensions\n- Entity-type ρ=-0.881 (p=0.004) 违反 independence (shared model/tokenizer/temp); effective df<6; p 可能高估 5-10x\n- **Action**: \"establishes\"→\"is consistent with\"; entity-type p 加 non-independence caveat; foreground T-ablation as controlled evidence; cross-dataset 降级为 exploratory\n\n**W3 [Critical] Three-layer gap 中 Layer 1 是 definitional, 接近 tautological。** [强共识: R1 AGREE + R2-W2]\n- \"Instance-level signals cannot rank by construction\" 是定义推论非实验发现\n- 与 empirical Layers 2-3 并列计数夸大分析深度\n- **Action**: Reframe as methodological premise; Contributions 改为 two empirical mechanisms\n\n**W4 [Critical] 纯诊断性论文缺乏 positive contribution，venue-fit 风险。** [强共识: R2-W1 + R1 AGREE]\n- 核心结论 = \"现有信号不 work\"; supervised verifier baseline (5 scalar features) 是 straw-man\n- LP +1.36pp modest; actionable takeaway 有限\n- **Action**: Reframe Few-NERD LP as primary practical finding; 提供 practitioners' decision rule; 考虑 lightweight learned verifier\n\n### Should-Fix (important for acceptance)\n\n**W5 [Warning] Few-NERD 3-epoch training confound。** [分歧: R1 Major, R2 部分反驳]\n- 3 epochs = early stopping (标准实践); 5-epoch control shows LP still works (+0.62pp)\n- 但主文未披露 3-epoch fact; performance-regime confound (greedy F1 0.748 vs 0.777)\n- **Action**: Section 4.1 明确披露; foreground 5-epoch still positive\n\n**W6 [Warning] LoRA rank=8 ablation conflates capacity and degeneracy。** [强共识: R1-W5 + R2 AGREE]\n- rank=8 同时改变 model capacity; lower ρ≈0.24 可能 = insufficient capacity\n- T=1.2 ablation 更 clean (same model, degeneracy 12.5%, ρ=0.225)\n- **Action**: T=1.2 为 primary evidence; LoRA-rank 承认 capacity confound\n\n**W7 [Warning] Supervised verifier 结论过度泛化。** [强共识: R1-W6 + R2 AGREE]\n- \"Bottleneck lies in what signals encode\" 仅对 5 个 features 成立\n- Hidden states / entity embeddings 有完全不同 capacity\n- **Action**: Scope to \"these five unsupervised signals\"\n\n**W8 [Warning] Abstract 信息密度仍过高。** [部分分歧: R2-W3, R1 部分反驳]\n- ~170 words, 8+ 定量值; R1 认为部分数值 IS contribution\n- 共识: 保留 4-5 核心数字, 移除中间机制数字\n\n**W9 [Warning] 模型规模 4B-8B 覆盖有限。** [共识: R2-W4 + R1 AGREE]\n- 8B degeneracy > 4B, 70B+ 可能更严重; LP alignment 方向不确定\n- **Action**: Limitations 增加 scale extrapolation discussion\n\n**W10 [Warning] Instance degeneracy 定义操作性模糊。** [强共识: R1-W7 + R2 AGREE]\n- Prose \"identical outputs\" vs operation \"identical F1\"; Table diversity (11%) ≠ Table degeneracy (17.8%)\n- **Action**: 首次使用时明确 \"identical F1\" 非 \"identical outputs\"\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. Overall 3.0/5 (Findings-level) — 两位 Reviewer 独立达成相同评分\n2. 纯诊断性质 + straw-man verifier 限制了 Main Conference 竞争力\n3. 统计 claims 需系统性 softening (establishes→consistent with; fails→insufficient evidence)\n4. QE/selection 分离的方法论贡献 + Few-NERD 验证是真实有价值的\n5. 写作质量和实验设计执行层面达到高标准\n6. LoRA-rank confound: T=1.2 应为 primary evidence\n\n## Reviewer Divergence [REBUT]\n\n1. **Abstract 数字密度** (轻微): R2 认为过多 (8+ 数字); R1 认为诊断论文需要数值但同意中间机制数字可移除. 共识: 减至 4-5 个.\n2. **Few-NERD epoch confound severity** (中度): R1 视为 Major (performance-regime confound, matched-degeneracy 比较缺失); R2 视为 well-designed control showing the mechanism works (LP still +0.62pp at 5 epochs). 共识: 需主文披露, 但 severity ≤ warning.\n\n---\n\n## Questions for Authors\n\n1. SciERC within-instance ρ(LP,F1)=0.248 vs Few-NERD ρ≈0.5 差异是否由 entity boundary clarity 解释？有无 SciERC per-type alignment 数据？\n2. SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79) 与 cross-dataset 和 within-Few-NERD 的 strong negative correlation 如何 reconcile？\n3. Supervised verifier 在 Few-NERD (32K instances) 上训练是否结果不同？\n4. Entity-token LP 方差 4× 但选择更差: if higher variance doesn't help, is compression truly the bottleneck, or is it representation-level determinism?\n\n---\n\n## Missing References\n\n- Vijayakumar et al. (2018) \"Diverse Beam Search\" — 直接关联 degeneracy/diversity\n- Shi et al. (2022) MBR for code generation — structured output MBR\n- Eisenstein et al. (2023) reward model ensembles — signal limitation\n- 4 个 orphan bib entries 需清理: bhattacharyya2026beyond, malinin2021uncertainty, ren2023selfevaluation, zhang2025conformal\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置外部审稿）。\n\n---\n\n## Overall Assessment\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.0 | 3.5 | 3.25 |\n| Excitement | 3.5 | 2.5 | 3.0 |\n| Reproducibility | 4.0 | 4.0 | 4.0 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**Overall: 3.0/5 — Findings-level (weak reject for Main Conference)**\n\n**置信度**: 4/5 (高)\n\n**一句话**: 方法论严谨的诊断性论文，成功揭示 QE/selection disconnect，但纯诊断性质（无 remedy）、统计 claims 过强（n=3 因果、underpowered null = \"fail\"、non-independence）、以及 Layer 1 tautological 限制其达到 Main Conference 门槛。适合 Findings track。\n\n**升级路径** (非建议，仅记录 Reviewer 共识):\n- 统计 claims 系统性 softening\n- Reframe three-layer → methodological premise + two empirical mechanisms\n- 补充至少一个 non-trivial positive contribution (learned verifier 或 LP practitioners' rule 的正式化)\n- Few-NERD LP +1.36pp reframe 为 primary finding 而非仅诊断证据\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 保留 4-5 核心数字 (headroom, +1.36pp, degeneracy range, ρ threshold)\n- 移除: ρ up to 0.38, +0.52pp N-scaling, MBR utility ρ=0.52\n- \"identical outputs\" → \"identical F1 scores\"\n\n### Introduction\n- Contribution 2 \"three-layer\" → methodological premise + two empirical layers\n- \"establishes\" → \"is consistent with\"\n- 先 Few-NERD positive, 再 SciERC inconclusive\n\n### Method\n- Instance degeneracy 操作性定义首次出现时明确\n\n### Experiments\n- Section 4.1: 明确 Few-NERD = 3 epochs (early stopping)\n- Table 3 caption 加粗 \"(full-set evaluation)\"\n- Table 2 EM/VC 无 p 值原因说明\n\n### Discussion\n- T=1.2 ablation 作为 alignment condition 的 primary evidence\n- LoRA-rank: 承认 capacity confound\n- Supervised verifier: scope to \"these five features\"\n- Figure 2: 15% threshold 来源说明\n\n### Limitations\n- Scale extrapolation: 70B+ degeneracy 可能更高但 alignment 未知\n- SciERC MDE at 80% power\n\n### References\n- 清理 4 个 orphan entries\n- 补充 diverse decoding / structured MBR 文献",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "weak reject",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 1818 · 2026-05-18T01:47:56.382252+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4112
}
```

</details>

---


### Assistant

_source line 1819 · 2026-05-18T01:48:06.926878+00:00_

---

**Round 18 圆桌审稿完成。**

报告已投递至 Research Director。

**核心结论**: Overall 3.0/5 (weak reject for Main Conference, Findings-level)。两位 Reviewer 独立达成一致评分。

**4 个 Must-Fix 问题**:
1. SciERC negative result 被 over-stated（统计效力仅 ~55%）
2. Cross-dataset gradient 因果推断过强（n=3 + non-independence）
3. Three-layer gap 的 Layer 1 是 definitional 非 empirical
4. 纯诊断性质缺乏 positive contribution

**升级路径**: 统计 claims softening + reframe three-layer → two empirical mechanisms + 补充 non-trivial positive contribution + Few-NERD LP reframe 为 primary finding。

Issue Tracker 已同步更新（7 个 resolved, 新增 4 个 issues, 现存 28 个 open/in_progress）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 148

## Round 148

2 recorded events


### User

_source line 1820 · 2026-05-18T01:48:09.710536+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

**逐条结论摘要：**

| Issue | 判定 | 核心理由 |
|-------|------|----------|
| W1 Power | AGREE | SciERC n=529 确实 underpowered；N-scaling 趋势暗示 small real effect |
| W2 n=3 gradient | AGREE | 语言过强，但 within-dataset ablations 提供补充证据 |
| W3 Non-independence | AGREE | Effective df < 6，p=0.004 可能膨胀 5-10x |
| W4 Epoch confound | REBUT | Early stopping 是标准实践；5-epoch 是控制实验而非 confound |
| W5 LoRA conflation | AGREE | T=1.2 ablation 是更 clean 的证据 |
| W6 Verifier features | AGREE | 结论应限定为 "these 5 features" |
| W7 Degeneracy 定义 | AGREE | Abstract "identical outputs" vs 操作定义 "identical F1" 有实质差异 |

R1 的统计方法论批评整体准确且 well-calibrated，唯一过严的是 W4。两位 Reviewer 对 Overall 3.0 (Findings) 一致。

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

_source line 1821 · 2026-05-18T01:48:22.258559+00:00_

**Round 18 圆桌审稿完成。**

审稿报告已投递给 Research Director。

**最终结论**: Overall 3.0/5 (Findings-level, weak reject for Main Conference)

**关键共识**:
- 4 个 Must-Fix issues: 统计效力 over-statement、n=3 因果过强、Layer 1 tautological、缺乏 positive contribution
- 6 个 Should-Fix issues: epoch confound 披露、LoRA capacity confound、verifier 结论 scope、Abstract 密度、scale 覆盖、degeneracy 定义
- 本轮新解决 7 个历史 issues (R17-W1, R14-M1, R16-N2, R12-N1, R14-M3, R11-N3, R17-W3)
- 格式完全合规，写作质量达到高标准

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 149

## Round 149

62 recorded events


### User

_source line 1822 · 2026-05-18T05:51:42.453937+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference Long Paper
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

_source line 1823 · 2026-05-18T05:51:47.680771+00:00_

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

_source line 1824 · 2026-05-18T05:51:47.781947+00:00_

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
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1825 · 2026-05-18T05:51:52.247523+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
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
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1826 · 2026-05-18T05:51:52.298101+00:00_



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

_source line 1827 · 2026-05-18T05:51:56.261984+00:00_

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

_source line 1828 · 2026-05-18T05:51:57.517296+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (128 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-18\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **exp_029b** (success): Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets. ← 基于 ft_002_v2\n- **exp_029a** (success): Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific. ← 基于 ft_002_v2\n  [server_diagnostic_exp029](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_029a/report/server_diagnostic_1a84e4.md) | [exp_029a_analysis_results](/api/workspace-files/projects/struct_self_consist_ie/artifacts/exp_029a/data/exp_029a_analysis_summary.txt)\n- **exp_028_fewnerd_5epoch** (negative): Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\n\n## 趋势\n成功 76 / 负向 26 / 失败 4 / 共 128\ngreedy_f1: 0.6491 ↓（近 3 次 success）\nheadroom_pp: 8.4 ↑（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nautodl-5090:
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1255
}
```

</details>

---


### Tool call

_source line 1829 · 2026-05-18T05:51:57.969262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
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
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1830 · 2026-05-18T05:51:58.421284+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.

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

_source line 1831 · 2026-05-18T05:51:58.421608+00:00_

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

_source line 1832 · 2026-05-18T05:51:58.472025+00:00_



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

_source line 1833 · 2026-05-18T05:52:05.554015+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/main.tex",
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
    "pattern": "**/paper/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1834 · 2026-05-18T05:52:05.805524+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

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

_source line 1835 · 2026-05-18T05:52:05.805871+00:00_

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


### Tool result

_source line 1836 · 2026-05-18T05:52:13.083850+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's the information about EMNLP 2026 submission deadlines and author guidelines:

## Key Submission Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors by May 27, 2026. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

Additional important dates include:
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: Augus
…[truncated 885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7277
}
```

</details>

---
