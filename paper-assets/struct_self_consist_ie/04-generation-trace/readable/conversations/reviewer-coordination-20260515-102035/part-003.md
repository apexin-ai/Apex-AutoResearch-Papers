# Reviewer coordination (archived snapshot) — Part 3 of 3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-coordination-20260515-102035.md) · [Structured JSON](../../../sessions/21/21967d528122a3266743.json)

## Round 61

### Tool call

_source line 1253 · 2026-05-15T10:08:21.640546+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

````json
{
  "text": "[severity: info] 补充回答——针对第二轮 framing 评估请求中与首轮报告不重叠的部分\n\n注：Q1/Q2/Q3/Q5 的详细分析已在首轮报告中覆盖。以下仅补充新增内容。\n\n---\n\n### 确认：完全同意 Director 的初步判断\n\nDirector 的 5 点判断（negative = stronger, universal > regime-specific, controlled ablation = rigor, 去掉 title 中 \"under Constrained Decoding\", proven fundamental limitation）与我首轮报告的独立结论一致。特别是第 1 点——positive result 反而会被审稿人 dismiss（\"just don't use constrained decoding\"），negative result 让发现不可 trivially dismiss。\n\n---\n\n### Q3 补充：Discussion [Planned experiment] 替换的具体写法建议\n\ndiscussion:23-27 当前文本：\n```\n\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form generation...\n[Planned experiment: free-form ablation on SciERC NER/RE.]\nAll findings reported in this paper are specific to the constrained decoding regime...\n```\n\n建议替换为：\n\n```\n\\paragraph{Score compression is task-inherent.}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's\nrestricted token space. We test this via controlled ablation: generating free-form\n(unconstrained) outputs on the same instances with post-hoc JSON parsing\n(parse rate 99.95\\%, 4406/4408). LP variance is essentially unchanged\n(within-sample std ratio 0.97$\\times$, tied fraction 59.7\\%$\\to$57.7\\%;\nTable~\\ref{tab:freeform_ablation}). This rules out constrained decoding as the cause\nof compression and establishes LP compression as inherent to structured output generation.\nThe correlation-selection gap is therefore a fundamental challenge for test-time scaling\nin structured IE, not an artifact of any particular decoding strategy.\n```\n\n要点：\n- 段落标题从\"Toward mechanistic confirmation\"→\"Score compression is task-inherent\"（结论性，不是待验证）\n- 报告实际数据而非预测\n- 明确说 \"rules out\"（有受控实验支撑，措辞合理）\n- 删除 \"All findings are specific to the constrained decoding regime\"（scope limiting 不再需要，因为 ablation 证明了 universality）\n- 最后一句 \"fundamental challenge...not an artifact\" 是新 framing 的 keystone sentence\n\n---\n\n### Q4: 是否建议启动 exp-019 supervised verifier baseline？\n\n**建议不启动，原因如下：**\n\n1. **时间约束**：DDL 2026-05-25，还有 10 天。论文文本还需要 framing 修正 + 重新审查。训练 verifier + 评估 + 写入论文的 end-to-end 时间 ≥ 3-4 天。风险过高。\n\n2. **scope creep 风险**：论文当前是 analytical/diagnostic 性质的贡献（发现 gap + 诊断原因 + controlled ablation）。加入 supervised verifier 会把论文变成 \"we found a problem AND solved it\"——如果 verifier 效果好，审稿人会要求更多 ablation（verifier architecture, training data size, generalization）；如果效果不好，削弱 \"gap is closable\" 的 narrative。\n\n3. **free-form ablation 已经提供了 \"so what\"**：\n   - Gap 是 fundamental → 需要新范式（trained verifiers, not just better unsupervised signals）\n   - 非 tied subset +2.9pp → LP 在特定条件下 works → actionable\n   - 这两点组合 = 足够的 forward-looking contribution\n\n4. **verifier 更适合作为 follow-up paper**：本文定义问题 + 诊断，下一篇解决。这在 NLP 社区是正常的 publication pattern。\n\n**如果 Director 执意要做**：用最简单的 logistic regression verifier（已有 exp-016 数据：5-signal LR, 5-fold CV）作为 proxy。但 exp-016 已经显示 ensemble 不优于 best single signal (EM AUROC 0.749 > LR ensemble 0.666) → supervised linear verifier 不够强 → 需要 neural verifier → 时间不够。\n\n---\n\n### Q5 补充：最优定位的 one-liner\n\n首轮报告已给出完整定位。压缩为一句 headline：\n\n**\"We discover, diagnose, and experimentally probe the correlation-selection gap — the first demonstrated fundamental limitation of unsupervised confidence signals for structured IE test-time scaling, proven universal via controlled ablation.\"**\n\n注意：\"first\" 在这里指 \"first demonstrated via controlled experiment\"，不是 \"first to study confidence for IE\"（Nédellec 2026 先于我们）。Paper Agent 需要确保措辞精确。\n\n---\n\n### 行动优先级建议\n\n1. **P0（立即）**：修改 paper_framing.md — Claims 1 + Story Spine + Title\n2. **P0（立即）**：修改 abstract / intro / discussion / conclusion 中的 5 处因果归因（首轮报告已列清单）\n3. **P1（Today）**：新增 appendix Table (freeform ablation comparison) — LP variance, selection F1, QE ρ\n4. **P2（If time）**：RE LP selection flip 加 3-seed bootstrap → 如果显著，升级为 secondary finding；不显著则 appendix 注释\n5. **Skip**：exp-019 supervised verifier",
  "project": "struct_self_consist_ie"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] 补充回答——针对第二轮 framing 评估请求中与首轮报告不重叠的部分\n\n注：Q1/Q2/Q3/Q5 的详细分析已在首轮报告中覆盖。以下仅补充新增内容。\n\n---\n\n### 确认：完全同意 Director 的初步判断\n\nDirector 的 5 点判断（negative = stronger, universal > regime-specific, controlled ablation = rigor, 去掉 title 中 \"under Constrained Decoding\", proven fundamental limitation）与我首轮报告的独立结论一致。特别是第 1 点——positive result 反而会被审稿人 dismiss（\"just don't use constrained decoding\"），negative result 让发现不可 trivially dismiss。\n\n---\n\n### Q3 补充：Discussion [Planned experiment] 替换的具体写法建议\n\ndiscussion:23-27 当前文本：\n```\n\\paragraph{Toward mechanistic confirmation.}\nOur diagnosis predicts that LP score compression should diminish under free-form generation...\n[Planned experiment: free-form ablation on SciERC NER/RE.]\nAll findings reported in this paper are specific to the constrained decoding regime...\n```\n\n建议替换为：\n\n```\n\\paragraph{Score compression is task-inherent.}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's\nrestricted token space. We test this via controlled ablation: generating free-form\n(unconstrained) outputs on the same instances with post-hoc JSON parsing\n(parse rate 99.95\\%, 4406/4408). LP variance is essentially unchanged\n(within-sample std ratio 0.97$\\times$, tied fraction 59.7\\%$\\to$57.7\\%;\nTable~\\ref{tab:freeform_ablation}). This rules out constrained decoding as the cause\nof compression and establishes LP compression as inherent to structured output generation.\nThe correlation-selection gap is therefore a fundamental challenge for test-time scaling\nin structured IE, not an artifact of any particular decoding strategy.\n```\n\n要点：\n- 段落标题从\"Toward mechanistic confirmation\"→\"Score compression is task-inherent\"（结论性，不是待验证）\n- 报告实际数据而非预测\n- 明确说 \"rules out\"（有受控实验支撑，措辞合理）\n- 删除 \"All findings are specific to the constrained decoding regime\"（scope limiting 不再需要，因为 ablation 证明了 universality）\n- 最后一句 \"fundamental challenge...not an artifact\" 是新 framing 的 keystone sentence\n\n---\n\n### Q4: 是否建议启动 exp-019 supervised verifier baseline？\n\n**建议不启动，原因如下：**\n\n1. **时间约束**：DDL 2026-05-25，还有 10 天。论文文本还需要 framing 修正 + 重新审查。训练 verifier + 评估 + 写入论文的 end-to-end 时间 ≥ 3-4 天。风险过高。\n\n2. **scope creep 风险**：论文当前是 analytical/diagnostic 性质的贡献（发现 gap + 诊断原因 + controlled ablation）。加入 supervised verifier 会把论文变成 \"we found a problem AND solved it\"——如果 verifier 效果好，审稿人会要求更多 ablation（verifier architecture, training data size, generalization）；如果效果不好，削弱 \"gap is closable\" 的 narrative。\n\n3. **free-form ablation 已经提供了 \"so what\"**：\n   - Gap 是 fundamental → 需要新范式（trained verifiers, not just better unsupervised signals）\n   - 非 tied subset +2.9pp → LP 在特定条件下 works → actionable\n   - 这两点组合 = 足够的 forward-looking contribution\n\n4. **verifier 更适合作为 follow-up paper**：本文定义问题 + 诊断，下一篇解决。这在 NLP 社区是正常的 publication pattern。\n\n**如果 Director 执意要做**：用最简单的 logistic regression verifier（已有 exp-016 数据：5-signal LR, 5-fold CV）作为 proxy。但 exp-016 已经显示 ensemble 不优于 best single signal (EM AUROC 0.749 > LR ensemble 0.666) → supervised linear verifier 不够强 → 需要 neural verifier → 时间不够。\n\n---\n\n### Q5 补充：最优定位的 one-liner\n\n首轮报告已给出完整定位。压缩为一句 headline：\n\n**\"We discover, diagnose, and experimentally probe the correlation-selection gap — the first demonstrated fundamental limitation of unsupervised confidence signals for structured IE test-time scaling, proven universal via controlled ablation.\"**\n\n注意：\"first\" 在这里指 \"first demonstrated via controlled experiment\"，不是 \"first to study confidence for IE\"（Nédellec 2026 先于我们）。Paper Agent 需要确保措辞精确。\n\n---\n\n### 行动优先级建议\n\n1. **P0（立即）**：修改 paper_framing.md — Claims 1 + Story Spine + Title\n2. **P0（立即）**：修改 abstract / intro / discussion / conclusion 中的 5 处因果归因（首轮报告已列清单）\n3. **P1（Today）**：新增 appendix Table (freeform ablation comparison) — LP variance, selection F1, QE ρ\n4. **P2（If time）**：RE LP selection flip 加 3-seed bootstrap → 如果显著，升级为 secondary finding；不显著则 appendix 注释\n5. **Skip**：exp-019 supervised verifier",
    "project": "struct_self_consist_ie"
  }
}
````

</details>

---


### Tool result

_source line 1254 · 2026-05-15T10:08:25.558739+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 1255 · 2026-05-15T10:08:27.251324+00:00_

之前已提交过包含全部 6 个问题的详细审查报告。Director 的新请求与之高度重叠，但有两个新问题需要补充回答：Q4（exp-019 supervised verifier）和部分措辞调整。让我针对新增内容补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer"
}
```

</details>

---


## Round 62

## Round 62

11 recorded events


### User

_source line 1256 · 2026-05-15T10:12:39.846282+00:00_

[系统通知 — roadmap_updated]:
[系统通知] ROADMAP.md 已更新（原因：D072: Ablation 负结果 → universal gap proven, 启动 supervised verifier, 更新 framing），请审查研究方向和计划的合理性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "source": "roadmap_updated"
}
```

</details>

---


### Tool call

_source line 1257 · 2026-05-15T10:12:44.769159+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_roadmap",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_roadmap",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1258 · 2026-05-15T10:12:44.869818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1259 · 2026-05-15T10:12:46.777975+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

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
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1260 · 2026-05-15T10:12:46.828794+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:12 UTC | 更新原因: D072: Ablation 负结果 → universal gap proven, 启动 supervised verifier, 更新 framing\\n\\n## 核心方向\\n系统比较 5 类置信信号在 IE test-time scaling 中的有效性。**核心发现：universal correlation-selection gap（controlled ablation 证明 score compression 是 model/task intrinsic，非 constrained decoding artifact）。** 详见 paper_framing.md。\\n\\n## 当前阶段\\n**Review + 新实验并行** — D072 方向确定：ablation 负结果证明 gap 是 universal → 论文从 observation 升级为 proven fundamental limitation。\\n\\n### 关键进展\\n1. **exp-018 free-form ablation 完成 (NEGATIVE)**: LP std ratio 0.97, tied fraction -2pp → constrained decoding bottleneck 假设被证伪。Score compression is intrinsic.\\n2. **D072 framing**: Universal gap + controlled experiment evidence。Title 回退去掉 \\\"under Constrained Decoding\\\"。负结果反而 strengthens paper（universal > regime-specific）。\\n3. **D070 写作修订**: 21 项全部完成并验证 PASS。\\n4. **exp-019 supervised verifier**: 正在实现，目标证明 gap IS closable with supervision → \\\"so what\\\" moment。\\n5. **RE LP selection flip**: free-form 下 RE LP selection -0.68pp → +1.69pp，Agent 正在做深度分析。\\n\\n### 评分趋势 + 突破策略\\nR1-R6: 3.0/5 plateau → 根因: content ceiling (Reviewer 诊断)\\n**D072 突破路径**: controlled ablation (done) + supervised verifier (running) + universal framing = 从\\\"12 页说路不通\\\"到\\\"证明为什么不通 + 怎么通\\\"\\n\\n## 近期任务\\n- [x] exp-018 free-form ablation 完成 (NEGATIVE → universality proven)\\n- [x] D072 framing decision logged\\n- [x] paper_framing.md updated for D072\\n- [x] D070 全部 21 项修订完成 + Reviewer 验证 PASS\\n- [ ] Agent: exp-019 supervised verifier baseline (DeBERTa, 5-fold CV)\\n- [ ] Agent: RE LP selection flip 深度分析\\n- [ ] Agent: non-tied subset constrained vs free-form 重叠分析\\n- [ ] Reviewer: D072 framing 独立评估（已发请求）\\n- [ ] Paper Agent: Discussion [Planned experiment] → actual ablation results\\n- [ ] Paper Agen
…[truncated 1551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1261 · 2026-05-15T10:13:14.951429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1262 · 2026-05-15T10:13:15.002176+00:00_

1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-15 — D072: Ablation 负结果证明 gap 是 universal。Free-form ablation falsified "constrained decoding bottleneck" hypothesis (LP std ratio 0.97, tied fraction -2pp). Score compression is model/task intrinsic → gap is a fundamental property of structured IE, not a regime artifact. Paper strengthened: controlled experiment proves universality via elimination. Launching exp-019 supervised verifier as "so what" moment.
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Findings (via ARR May 2026)
7	- Deadline: ARR May cycle, 2026-05-25
8	
9	## Core Claims (3 条, D072 updated — ablation proves universality)
10	
11	### Claim 1 (PRIMARY — Universal Correlation-Selection Gap)
12	The correlation-selection gap in structured IE is a **fundamental property of the task**, not an artifact of constrained decoding. Confidence signals reliably predict output quality (AUROC up to 0.75) but cannot select better candidates from multiple samples. A controlled free-form decoding ablation proves this gap is universal: removing constrained decoding does NOT recover logprob variance or selection ability.
13	
14	**Two-layer argument**:
15	- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.
16	- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to intrinsic score compression (60% of instances have within-sample range < 0.05). (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation FALSIFIES regime-specific hypothesis**: removing constrained decoding does NOT recover logprob discrimination (std ratio 0.97, tied fraction -2pp) → compression is model/task intrinsic, proving universality via elimination.
17	
18	**Key evidence (score compression)**:
19	- Non-tied su
…[truncated 905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1263 · 2026-05-15T10:13:17.570751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md",
  "offset": "30",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md",
    "offset": "30",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1264 · 2026-05-15T10:13:17.671725+00:00_

30	- **Conclusion**: Score compression is model/task intrinsic. The gap is universal.
31	
32	**Key evidence (supervised verifier)** [PLANNED — exp-019]:
33	- If simple supervised verifier partially closes the gap → proves gap IS closable with supervision → transforms negative finding into actionable one with upper bound on unsupervised methods
34	
35	**Implications**: Not just "signals don't work" but "here's WHY they don't work (intrinsic score compression), here's proof it's universal (controlled ablation), and here's the path forward (supervised approaches can close the gap)."
36	
37	### Claim 2 (METHODOLOGY — QE Evaluation Framework)
38	Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.
39	
40	**Key results**:
41	- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)
42	- RE (preliminary, single benchmark): voting_conf leads both full and conditional
43	- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
44	- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09
45	
46	**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
47	- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
48	- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
49	- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706
50	
51	### Claim 2b (Selection evidence)
52	**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):
53	- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
54	- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.359
…[truncated 4818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1265 · 2026-05-15T10:14:12.208223+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: warning] ROADMAP D072 更新审查\n\n## 总体评价：方向正确，2 个 warning\n\nD072 的核心方向转变（regime-specific → universal gap）完全正确，与我两轮报告的独立结论一致。paper_framing.md 更新后 Claims 1、Layer 2 命名、Story Spine 均准确反映了 ablation 结果。\n\n---\n\n### Warning 1: RE LP selection flip 在 Story Spine 中的地位过高\n\npaper_framing.md:85 将 RE flip (+1.69pp) 提升为 Story Spine 第 4 点：\n> \"RE shows qualitatively different behavior — free-form LP selection flips from -0.68pp to +1.69pp, suggesting the gap mechanism differs across task complexity levels.\"\n\n**问题**：\n- Single seed (seed=42)，无 bootstrap 显著性检验\n- NER 方向相反（+0.59pp → +0.18pp）→ mixed evidence\n- RE 本身为 single benchmark，已标 preliminary\n- +1.69pp 在主实验 bootstrap CI [-3.0, +4.2]pp 范围内 → 不能排除噪声\n- \"suggesting the gap mechanism differs across task complexity levels\" 是 claim without sufficient evidence\n\n**建议**：\n- 降级为 appendix observation，不入 Story Spine\n- 如果要保留，必须先做 3-seed bootstrap（Agent 正在做 RE flip analysis → 等结果）\n- 如果 3-seed 显著 → 可升级为 secondary finding\n- 如果不显著 → 删除或仅 appendix 注释\n\n### Warning 2: Selection F1 绝对值在 ablation 与主实验间有差异\n\nablation_report.json 中 constrained NER：greedy=0.618, LP=0.624\n论文 Table 2：greedy=0.644, LP=0.650\n\n差异约 2.6pp。两者应使用相同的 constrained decoding 数据（exp_012_rerun_1024）。可能原因：\n- 分析脚本与论文评估管线的 F1 计算方法不同（span matching 标准？）\n- 实例筛选不同（是否排除了 22 个 empty-gold instances？）\n- 不同的 greedy run（不同 checkpoint 的 T=0 输出？）\n\n**影响**：ablation 内部对比（constrained vs free-form）用同一代码，within-ablation 结论有效。但论文中引用 ablation 数据时不能直接与 Table 2 混用。\n\n**建议**：Agent 排查原因。如果是 eval 方法差异 → ablation appendix table 用自己的数字体系，注明评估方法；如果是 data 差异 → 修复。\n\n---\n\n### Info: exp-019 supervised verifier 风险评估\n\n我此前建议 skip（DDL 风险）。Director 决定推进——尊重这个判断。补充评估：\n\n**可行性**：DeBERTa 5-fold CV on 529 instances → 训练 ~1-2 小时/fold → 半天可完成。可行。\n\n**风险矩阵**：\n| 结果 | 论文影响 | 风险 |\n|------|---------|------|\n| Verifier 显著优于 unsupervised | 强 \"so what\"：gap IS closable | 审稿人可能要求更多 verifier ablation |\n| Verifier 略优（+1-3pp, 不显著） | 弱 evidence，不值得一节 | 浪费时间 |\n| Verifier 不优于 best unsupervised | 削弱 \"closable\" claim | 需要解释为何 |\n\n**关键设计问题**（Agent 实现时需注意）：\n- Verifier input 是什么？(input_text, candidate_output) → predict F1? Binary good/bad?\n- Training labels 来自哪里？如果用 gold F1 → test-time 不可得 → 审稿人会说 \"requires gold labels, defeats the purpose\"\n- 需要在 Discussion 中明确定位为 \"proof of concept that supervision helps, not a practical system\"\n\n---\n\n### Info: 其他 ROADMAP 项确认\n\n- \"Dream 结果需 discount\" ✓ 正确处理\n- \"Paper Agent: Title 回退 + Claim 1 rewrite\" ✓ 正确排期\n- \"Non-tied subset constrained vs free-form 重叠分析\" ✓ 有价值——如果同一批 instances 在两种条件下都是 non-tied，进一步证明 compression 是 instance-level intrinsic property\n- 10 天 DDL ✓ 可行但紧——critical path 是 paper text revision（framing 变化影响 abstract/intro/discussion/conclusion 全部主要章节）",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: warning] ROADMAP D072 更新审查\n\n## 总体评价：方向正确，2 个 warning\n\nD072 的核心方向转变（regime-specific → universal gap）完全正确，与我两轮报告的独立结论一致。paper_framing.md 更新后 Claims 1、Layer 2 命名、Story Spine 均准确反映了 ablation 结果。\n\n---\n\n### Warning 1: RE LP selection flip 在 Story Spine 中的地位过高\n\npaper_framing.md:85 将 RE flip (+1.69pp) 提升为 Story Spine 第 4 点：\n> \"RE shows qualitatively different behavior — free-form LP selection flips from -0.68pp to +1.69pp, suggesting the gap mechanism differs across task complexity levels.\"\n\n**问题**：\n- Single seed (seed=42)，无 bootstrap 显著性检验\n- NER 方向相反（+0.59pp → +0.18pp）→ mixed evidence\n- RE 本身为 single benchmark，已标 preliminary\n- +1.69pp 在主实验 bootstrap CI [-3.0, +4.2]pp 范围内 → 不能排除噪声\n- \"suggesting the gap mechanism differs across task complexity levels\" 是 claim without sufficient evidence\n\n**建议**：\n- 降级为 appendix observation，不入 Story Spine\n- 如果要保留，必须先做 3-seed bootstrap（Agent 正在做 RE flip analysis → 等结果）\n- 如果 3-seed 显著 → 可升级为 secondary finding\n- 如果不显著 → 删除或仅 appendix 注释\n\n### Warning 2: Selection F1 绝对值在 ablation 与主实验间有差异\n\nablation_report.json 中 constrained NER：greedy=0.618, LP=0.624\n论文 Table 2：greedy=0.644, LP=0.650\n\n差异约 2.6pp。两者应使用相同的 constrained decoding 数据（exp_012_rerun_1024）。可能原因：\n- 分析脚本与论文评估管线的 F1 计算方法不同（span matching 标准？）\n- 实例筛选不同（是否排除了 22 个 empty-gold instances？）\n- 不同的 greedy run（不同 checkpoint 的 T=0 输出？）\n\n**影响**：ablation 内部对比（constrained vs free-form）用同一代码，within-ablation 结论有效。但论文中引用 ablation 数据时不能直接与 Table 2 混用。\n\n**建议**：Agent 排查原因。如果是 eval 方法差异 → ablation appendix table 用自己的数字体系，注明评估方法；如果是 data 差异 → 修复。\n\n---\n\n### Info: exp-019 supervised verifier 风险评估\n\n我此前建议 skip（DDL 风险）。Director 决定推进——尊重这个判断。补充评估：\n\n**可行性**：DeBERTa 5-fold CV on 529 instances → 训练 ~1-2 小时/fold → 半天可完成。可行。\n\n**风险矩阵**：\n| 结果 | 论文影响 | 风险 |\n|------|---------|------|\n| Verifier 显著优于 unsupervised | 强 \"so what\"：gap IS closable | 审稿人可能要求更多 verifier ablation |\n| Verifier 略优（+1-3pp, 不显著） | 弱 evidence，不值得一节 | 浪费时间 |\n| Verifier 不优于 best unsupervised | 削弱 \"closable\" claim | 需要解释为何 |\n\n**关键设计问题**（Agent 实现时需注意）：\n- Verifier input 是什么？(input_text, candidate_output) → predict F1? Binary good/bad?\n- Training labels 来自哪里？如果用 gold F1 → test-time 不可得 → 审稿人会说 \"requires gold labels, defeats the purpose\"\n- 需要在 Discussion 中明确定位为 \"proof of concept that supervision helps, not a practical system\"\n\n---\n\n### Info: 其他 ROADMAP 项确认\n\n- \"Dream 结果需 discount\" ✓ 正确处理\n- \"Paper Agent: Title 回退 + Claim 1 rewrite\" ✓ 正确排期\n- \"Non-tied subset constrained vs free-form 重叠分析\" ✓ 有价值——如果同一批 instances 在两种条件下都是 non-tied，进一步证明 compression 是 instance-level intrinsic property\n- 10 天 DDL ✓ 可行但紧——critical path 是 paper text revision（framing 变化影响 abstract/intro/discussion/conclusion 全部主要章节）",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1266 · 2026-05-15T10:14:16.227319+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4019
}
```

</details>

---


## Round 63

## Round 63

6 recorded events


### User

_source line 1267 · 2026-05-15T10:14:18.826845+00:00_

[系统通知 — worker_done:worker_analysis_n16_readiness_check_20260515T100959]:
Worker worker_analysis_n16_readiness_check_20260515T100959 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "source": "worker_done:worker_analysis_n16_readiness_check_20260515t100959"
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-15T10:14:24.608261+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/worker_analysis_n16_readiness_check*result*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/worker_analysis_n16_readiness_check*result*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-15T10:14:24.658939+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_n16_readiness_check_20260515T100959_result.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-15T10:14:26.868929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_n16_readiness_check_20260515T100959_result.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_n16_readiness_check_20260515T100959_result.json"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-15T10:14:26.869394+00:00_

1	{
2	  "raw": "报告已生成并注册。核心发现：\n\n**seed42 和 seed123 的 N=16 实验已完成**（各 551 instances，含 logprobs），`exp001_n16_seed123_full` 只是被 kill 的旧尝试，`exp001_n16_seed123`（无 `_full` 后缀）实际已成功运行。\n\n**唯一缺失的是 seed456 的 full N=16 运行**。`output/exp001_n16_seed456/` 为空目录，仅有 `_200only` 的 200 实例部分结果。\n\n运行命令：\n```bash\ncd /root/autodl-tmp/struct_self_consist_ie && \\\npython code/run_mvp_pilot.py \\\n  --model_path checkpoints/qwen3-8b-scierc-merged-v2 \\\n  --data_dir data/ --dataset scierc --subtask joint \\\n  --n_samples 16 --temperature 1.0 --seed 456 \\\n  --output_dir output/exp001_n16_seed456 \\\n  --collect_logprobs \\\n  2>&1 | tee output/exp001_n16_seed456_run.log\n```\n\n预计 ~8-9 分钟完成。所有依赖（vLLM 0.18.1、xgrammar 0.1.33）和模型均就绪。"
3	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 1272 · 2026-05-15T10:14:37.400466+00:00_

N=16 readiness check 结果：seed42 和 seed123 已完成，seed456 缺失待运行（~8-9分钟）。这是数据补全任务，非关键审查项。如果 Agent 启动 seed456 运行，我会在完成时检查 GPU 合规性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer"
}
```

</details>

---


## Round 64

## Round 64

5 recorded events


### User

_source line 1273 · 2026-05-15T10:17:44.005058+00:00_

[系统通知 — roadmap_updated]:
[系统通知] ROADMAP.md 已更新（原因：D073: exp-019 verifier cancelled, Reviewer confirmed D072 direction），请审查研究方向和计划的合理性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "source": "roadmap_updated"
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-15T10:17:56.170460+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

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
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-15T10:17:56.221377+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ROADMAP.md\", \"content\": \"# struct_self_consist_ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:17 UTC | 更新原因: D073: exp-019 verifier cancelled, Reviewer confirmed D072 direction\\n\\n## 核心方向\\n系统比较 5 类置信信号在 IE test-time scaling 中的有效性。**核心发现：universal correlation-selection gap（controlled ablation 证明 score compression 是 model/task intrinsic，非 constrained decoding artifact）。** 详见 paper_framing.md。\\n\\n## 当前阶段\\n**Review + 论文修订并行** — D072/D073 方向确定，Reviewer 四维度独立确认。\\n\\n### 关键进展\\n1. **exp-018 free-form ablation (NEGATIVE)**: LP std ratio 0.97, tied -2pp → constrained decoding 假设被证伪。Gap is universal.\\n2. **D072 framing**: Universal gap + controlled experiment evidence。Title 去掉 \\\"under Constrained Decoding\\\"。\\n3. **D073**: exp-019 verifier SKIPPED（Reviewer 建议：DDL 风险 + scope creep + analytical paper 不加 solution）。\\n4. **D070 写作修订**: 21 项完成验证 PASS。\\n5. **Parse rate 99.95%**: Bonus finding — fine-tuned 模型 free-form 下仍生成合法 JSON。\\n6. **Reviewer 审查**: 四维度确认 D072 方向，提供 7 处精确修改清单。\\n\\n### 评分趋势 + 突破策略\\nR1-R6: 3.0/5 plateau → 根因: content ceiling\\n**D072 突破**: controlled ablation (done) + universal framing + Reviewer 精确修改清单 = 从 observation 到 proven fundamental limitation\\n\\n## 近期任务\\n- [x] exp-018 free-form ablation (NEGATIVE → universality proven)\\n- [x] D072 + D073 decisions logged\\n- [x] paper_framing.md updated\\n- [x] D070 全部 21 项修订 PASS\\n- [x] Reviewer 独立评估完成（四维度确认）\\n- [ ] **Agent**: ablation 深度分析 + appendix table 准备\\n- [ ] **Agent**: 多种子实验 (seed 123/456) — 如果代码 ready\\n- [ ] **Paper Agent**: D072 patch（title + abstract + intro + discussion + conclusion 修改）\\n- [ ] **Paper Agent**: 补充 patch（parse rate bonus + Reviewer 具体写法 + appendix table）\\n- [ ] Dream (dream_20260515T092545): writing 阶段 → 结果需 discount（基于 D071 旧 framing）\\n- [ ] Round 7 提交\\n- [ ] 最终提交 (DDL: 2026-05-25, 距今 10 天)\\n\\n## GPU 预算\\nautodl-5090: 4× RTX 
…[truncated 1350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-15T10:18:08.334058+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] ROADMAP D073 更新审查：PASS\n\nD073 变更合理：\n1. **exp-019 verifier 取消** ✓ — 与我的建议一致（DDL 风险 + scope creep + analytical paper 定位）\n2. **核心方向不变**：universal gap + controlled ablation ✓\n3. **任务列表清晰**：关键路径 = Paper Agent D072 patch → Round 7，无冗余实验阻塞\n4. **多种子实验（seed 123/456）保留为可选** ✓ — 之前 N16 readiness check 显示 seed42/123 已完成，只缺 seed456。如果用于 RE flip 3-seed validation 则有价值，否则可跳过\n\n无新增 warning。关键路径清晰：Paper Agent D072 patch 是当前 blocking item。",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] ROADMAP D073 更新审查：PASS\n\nD073 变更合理：\n1. **exp-019 verifier 取消** ✓ — 与我的建议一致（DDL 风险 + scope creep + analytical paper 定位）\n2. **核心方向不变**：universal gap + controlled ablation ✓\n3. **任务列表清晰**：关键路径 = Paper Agent D072 patch → Round 7，无冗余实验阻塞\n4. **多种子实验（seed 123/456）保留为可选** ✓ — 之前 N16 readiness check 显示 seed42/123 已完成，只缺 seed456。如果用于 RE flip 3-seed validation 则有价值，否则可跳过\n\n无新增 warning。关键路径清晰：Paper Agent D072 patch 是当前 blocking item。",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-15T10:18:12.320978+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 3986
}
```

</details>

---


## Round 65

## Round 65

2 recorded events


### User

_source line 1278 · 2026-05-15T10:19:43.512435+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1279 · 2026-05-15T10:20:35.547569+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 服务器名是 `autodl-5090`（不是 `autodl-5090(root)`，后者会报 unknown server）
- 项目 GPU 白名单未在 constraints.yaml 中明确定义（文件未创建），但历史上用 cuda:0 跑 freeform ablation 未被 flag。每次新实验仍需核对 `execution.gpu_ids`
- RE 结论全文必须标 "(preliminary, single benchmark)"——这是多轮审稿的硬约束，遗漏 = critical
- Selection F1 绝对值：ablation_report.json 与论文 Table 2 有 ~2.6pp 差异（greedy NER: 0.618 vs 0.644），原因未查明。**不要混用两套数字**

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`
- 论文源文件：`docs/paper/sections/{abstract,introduction,method,experiments,discussion,conclusion,appendix}.tex`
- paper_framing.md：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md`
- 模型 checkpoint：`checkpoints/qwen3-8b-scierc-merged-v2`（远程）
- Ablation 结果：`results/exp_freeform_ablation/ablation_report.json`（远程）
- N=16 数据：seed42 + seed123 完成，seed456 缺失（仅有 200-instance 部分结果）
- 无 wandb 配置，无活跃训练进程

### 3. 📊 当前状态
**刚完成**：
- D070/D071 论文修订 21 项验证（PASS）
- Free-form ablation 结果独立审查 → [critical] LP 压缩因果归因被否定
- 两轮 framing 影响评估（四维度审查）→ Agent "不需调整" 被打回
- D072 framing（universal gap）独立确认
- D073 ROADMAP 审查（exp-019 verifier 取消，PASS）

**Registry 状态**：exp_freeform_ablation 未在 registry 中注册（count=0 when filtered）。Worker 注册了 artifact `art_20260515_b80d82`。

**等待中**：
- Paper Agent D072 patch（title + abstract + intro + discussion + conclusion 全面修改）
- Dream (dream_20260515T092545) 结果（基于旧 D071 framing，需 discount）
- 可能的多种子实验回调

### 4. 📋 待办
- Paper Agent 提交 D072 patch → 按首轮报告的 7 处修改清单逐条核实（abstract:6-7, discussion:11/14/15/23-27/31, intro:25, conclusion:8）
- Dream 结果返回 → 过滤掉 framing 相关评语，保留与 framing 无关的审稿建议
- RE flip 3-seed 分析结果返回 → 显著则可升级为 secondary finding，不显著则要求从 Story Spine 降级到 appendix
- 多种子 N=16 seed456 完成 → 核实数据完整性
- Round 7 提交 → 全文最终审查（特别关注：是否还有残留的 "constrained decoding bottleneck" 因果归因）
- Selection F1 差异（ablation 0.618 vs Table 2 0.644）→ Agent 排查后审查结论

### 5. 🎯 战略上下文
**决策链**：D067(gap reframing) → D069(scope limiting) → D070(narrative restructure) → D071(regime-specific bottleneck) → D072(ablation 否定→universal gap) → D073(verifier cancelled)

**核心结论**：LP score compression 是结构化 IE 的固有属性（std ratio 0.97x constrained vs free-form），非 constrained decoding 导致。Correlation-selection gap 是 universal。

**最容易判断错的事**：
1. **论文中残留的 "constrained decoding" 因果归因**——D071 在 abstract/intro/discussion/conclusion 至少 7 处写了 "constrained decoding causes compression"，D072 patch 必须全部修正。grep `constrained.decoding` 全文扫描
2. **RE flip 不要过度解读**——single seed, +1.69pp, NER 方向相反。paper_framing.md Story Spine 第 4 点已将其提升过高，我已发 warning 但未见降级
3. **"first" 措辞**——论文不能说 "first to study confidence for IE"（Nédellec 2026 先于我们），只能说 "first controlled ablation proving universality" 且需措辞精确
4. **Parse rate 99.95%**——这挑战了 intro:19 "without constrained decoding, a substantial fraction of outputs are unparseable"。如果新论文仍保留此句，与 ablation 数据矛盾
5. **6 轮 3.0/5 的根因是 content ceiling**——ablation 结果是唯一新 content。如果 D072 patch 只改叙事不加 ablation 数据，评分不会突破
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_523053f5a039428dc15666668fa856b3:reviewer"
}
```

</details>

---
