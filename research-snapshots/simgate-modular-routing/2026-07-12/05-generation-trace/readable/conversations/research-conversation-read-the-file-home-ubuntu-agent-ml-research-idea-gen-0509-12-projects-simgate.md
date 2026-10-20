# Research conversation: Read the file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac2440b250dcb7b95.jsonl`
- **Structured JSON:** [`6c5f6ff9bf4dc4e5f792.json`](../../sessions/6c/6c5f6ff9bf4dc4e5f792.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-19T20:28:10.264Z_

Read the file /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_21.md and summarize: (1) the Must-Fix items, (2) the Should-Fix items, (3) any items that specifically requested NEW experiments (not just analysis/writing). Also look for any patterns about what reviewers found most problematic. Report the content concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c4d4f0db-2852-40ad-afac-040fa0e315f4",
  "agentId": "ac2440b250dcb7b95",
  "type": "user",
  "uuid": "7ae78104-8bc5-43f6-aab2-7bd806b92b12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T20:28:11.819Z_

I'll read the review report and summarize the key items for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae78104-8bc5-43f6-aab2-7bd806b92b12",
  "isSidechain": true,
  "agentId": "ac2440b250dcb7b95",
  "requestId": "req_011CbCZLYfJ31yacvxTv1iNF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5957bd4a-64cd-42f8-a01c-4cecacd3f401",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UNHctaP6sHXbBsnnhQ7cZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18776,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18776,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T20:28:11.934Z_

<details open><summary>🔧 Tool call — Read · `toolu_017Uz9tRASqaGyZGVsHfxb9s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_21.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5957bd4a-64cd-42f8-a01c-4cecacd3f401",
  "isSidechain": true,
  "agentId": "ac2440b250dcb7b95",
  "requestId": "req_011CbCZLYfJ31yacvxTv1iNF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbf3a856-e3d5-410f-b051-243f429fdf25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UNHctaP6sHXbBsnnhQ7cZF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18776,
      "cache_read_input_tokens": 0,
      "output_tokens": 109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 109,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18776,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T20:28:11.949Z_

<details><summary>↩ Tool result · `toolu_017Uz9tRASqaGyZGVsHfxb9s`</summary>

```text
1	---
2	round: 21
3	review_mode: fresh
4	overall_score: 3.0-3.5 (Findings to Borderline Conference)
5	timestamp: 2026-05-19T16:02:24.093419+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: True
9	---
10	
11	# 审稿报告（修订版）：Death Avoidance as the Dominant Routing Signal
12	
13	**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
14	**Venue**: EMNLP 2026 (Long Paper via ARR)
15	**Deadline**: 2026-05-25
16	**Round**: 19 (fresh review)
17	**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）
18	**修订原因**: 交叉回应后 Excitement 收敛（R1 3.5→3.0, R2 2.5→3.0）、新增关键共识点
19	
20	---
21	
22	## Summary
23	
24	本文提出 episode-level counterfactual diagnostic framework，将 modular LLM agent 的 routing signal 分解为 death-avoidance 和 non-death 两个成分。在 ScienceWorld（11 task types, 245 episodes, Qwen2.5-7B-Instruct）上，78.9% 的 non-tie routing labels 源于 death asymmetry：internal strategy 因幻觉触发 catastrophic death（−100 penalty），而 deterministic strategy 存活。DAF 在 P=100 下达 90.4%。Cross-model replication（Llama-3.1-8B）、four intervention axes（retry, Reflexion, 72B scaling, action filtering）、cross-environment probes（MATH, ALFWorld）进一步支持诊断。Router 训练（Qwen3 LoRA, 0.6B-4B）step-level 接近 chance，episode-level 仅 4B 有边际改善。
25	
26	---
27	
28	## Strengths
29	
30	**S1. 问题定义精准且有价值。** [R1-S1, R2 交叉后同意] 现有 routing 文献关注"怎么 route"（Toolformer, ART, Chameleon, CogRouter, When2Tool），本文追问"routing 到底在 route 什么信号"——这是一个被忽视的诊断性问题。R2 在交叉回应中承认此贡献有独立价值，将 Excitement 从 2.5 上调至 3.0。
31	
32	**S2. Pure-strategy counterfactual 设计干净。** [R1-S2, R2-S4, 强共识] 控制相同 random seed + initial conditions，episode-level labeling function（Algorithm 1）death-aware 且 penalty-independent。
33	
34	**S3. 统计分析超同类水准。** [R1-S4, R2-S1, 强共识] Episode-level bootstrap（B=10,000）、wild cluster bootstrap、per-task CIs、8-seed robustness、Cohen's d=3.02。R1 Reproducibility 4.5/5，R2 4/5。
35	
36	**S4. Robustness checks 全面。** [强共识] Leave-one-task-out DAF（75.9%-78.9%）、penalty sensitivity（Appendix K）、cross-model replication、anti-cherry-picking analysis（18/19 excluded types 也 death-dominated, ΔDR=+38.2pp）、SCI=0.2147。
37	
38	**S5. Negative results 诚实呈现。** [R2-S2, 强共识] Router step-level ≈ chance、data augmentation 无效——对社区有价值，呈现坦诚。
39	
40	**S6. Cross-model validation。** [R2-S5, 共识] Llama-3.1-8B 复制（11 tasks, N=220）direction consistency 10/10，death dominance 跨模型稳定。
41	
42	---
43	
44	## Weaknesses
45	
46	### Must-Fix（影响接收决定）
47	
48	**MF1 [Critical, 强共识] DAF headline framing 误导。**
49	- R1-N1 首提，R2 完全同意。Abstract 和 §3.1 以 "DAF = 90.4%" 为 headline，掩盖其 penalty-dependent 本质。DAF = δP/(δP + Δ_nd) 随 P 单调递增是数学后果，在 Δ_nd ≈ +2.84 且 P=100 时 DAF 接近 1 是代数必然。78.9% label fraction 才是 penalty-independent 的 robust finding。
50	- R2 在交叉回应中补充："如果 DAF 是 P 的单调函数且论文没有实际做不同 P 值实验（仅数学推导），那 DAF 的经验价值有限。"
51	- **Action**: Abstract 以 78.9% 为 primary metric；§3.1 段落重组，DAF 降为 derived quantity；增加 DAF 在 Δ_nd<0 边界行为讨论。
52	
53	**MF2 [Critical, 部分共识] 核心发现 novelty 不足——"obvious in hindsight"。**
54	- R2-W1 首提（Critical），R1 部分 REBUT。
55	- **R1 的辩护**：(1) 78.9% label fraction 是 penalty-independent 的，不能从 P=100 setup 直接推出；(2) 同期 routing 文献（When2Tool, Tool-Use-Tax, RouteLLM 等）全部聚焦 capability matching，无一讨论 catastrophic failure 作为 routing signal——如果 death dominance 真的 obvious，为什么无人验证？
56	- **R2 的回应**：承认问题定义有独立价值（Excitement 2.5→3.0），但维持 "一个好问题配一个可预见的答案，对 Findings 够，对 main conference 不够"。
57	- **交叉后状态**：R1 Excitement 3.5→3.0，R2 2.5→3.0，**Excitement 收敛至 3.0/5**。分歧从 1.0 gap 缩小为 0，但 Overall 仍有 0.5 差距（R1: 3.5, R2: 3.0），因为 R1 认为 Soundness+Reproducibility 的高分足以补偿 Excitement。
58	- **Director 裁决**: 维持 Critical。问题定义的贡献部分缓解了 triviality concern，但 EMNLP reviewer panel 中 excitement deficit 是常见 rejection reason。当前 non-triviality 论证（§5）力度不足。
59	- **Action**: 三角度强化：(1) routing 文献 prior assumptions 与实证的反差；(2) intervention resistance 的 non-predictability；(3) cross-model δ stability 作为结构性发现。
60	
61	**MF3 [Critical, 强共识] Framing 内在张力——framework vs finding 定位不清。**
62	- R2-W2 首提，R1 在交叉回应中完全同意（"论文在 diagnostic framework 和 empirical finding 之间摇摆"）。R1 补充了关键观察："如果选择 framework-centric 路线，novelty 质疑（R2-W1）就会被大幅缓解。"
63	- **Action**: 选择一个主线贯穿标题/Abstract/Contributions/Conclusion。推荐 framework-centric——既缓解 novelty concern，又对 single-environment scope 更 tolerant。
64	
65	**MF4 [Critical, 强共识] Cluster bootstrap K=11 低于公认阈值。**
66	- R1-N2 首提（Critical），R2 在交叉回应中完全同意并补充了额外论据：(1) p=0.002 仅比最小可报告值 (1/2048 ≈ 0.0005) 大 4 倍；(2) `find-non-living-thing` (zero death) 作为 outlier 可能影响 effect size。
67	- **缓解因素**（R2 同时指出）：多种互补 robustness evidence（8-seed, per-task CIs, exact permutation）共同构成比单一 cluster bootstrap 更强的证据链。两位 reviewer 均认为 "critical-but-partially-mitigated"。
68	- **Action**: 正文以 non-clustered bootstrap 为主推断；cluster bootstrap 定位为 conservative sensitivity check；增加 K=11 vs K≥40 的显式讨论。
69	
70	**MF5 [Critical, 强共识] Episode→step label projection 噪声——router diagnostic 价值严重受损。**
71	- R1-N3 首提（Critical），R2 在交叉回应中称其为 "比论文的解释更有说服力的替代假说"。
72	- **核心分歧转变**: 论文解读 = "step-level signal 本质上不存在"；R1 替代假说 = "signal 可能存在但被 ~88% noise/uninformative label 淹没"。两位 reviewer 均倾向 R1 解释。
73	- R2 进一步指出 R1-W2（pure-strategy 外部效度）和 R1-N3 形成 tension：如果 label noise 是 router 失败原因（N3），则 step-level routing 可能 feasible，那 pure-strategy 对比高估 death asymmetry（W2）就更严重。
74	- **Action**: §3.6 明确区分两种解释；测试 death-proximal labeling baseline（如只用 death event 附近 steps 训练）；或明确声明 router failure 是 label sparsity 而非 fundamental non-learnability。
75	
76	### Should-Fix（影响评分但不一票否决）
77	
78	**SF1 [Warning, 强共识] Cross-environment probes 定位过强。**
79	- R1-W1 和 R2-W3 一致。MATH = unfalsifiable null result，ALFWorld = 不同机制。Abstract "cross-domain probes" 措辞需弱化为 "boundary probes/consistency checks"。
80	
81	**SF2 [Warning, 共识] 缺少 penalty magnitude 的实际实验验证。**
82	- R2-W6 首提，R1 在交叉回应中完全同意。Appendix K 的 DAF vs P 是数学推导而非实验。R1 补充：Table 13 显示 P ≤ 25 时 correlation 不显著——"death dominance 是 ScienceWorld 特定 penalty regime 下的现象"。
83	
84	**SF3 [Warning, 共识] Pure-strategy 设计的外部效度。**
85	- R1-W2 首提，R2 同意并补充了与 R1-N3 的 tension 关系。
86	
87	**SF4 [Warning, 强共识] Conclusion 过于简短（2 句话）。**
88	
89	**SF5 [Warning, 强共识] Safe RL Related Work 不够深入。**
90	- 缺 CMDP (Altman 1999) 和 risk-sensitive RL 与 death avoidance 的理论映射。
91	
92	**SF6 [Warning, R2 首提, R1 部分 REBUT] Abstract 数字过密。**
93	- R1 认为 "每个数字都有明确指代，empirical 论文需要具体数字"。R2 维持 concern。
94	- **Director 裁决**: 如采用 framework-centric framing，Abstract 可自然减少数字密度（R1 观点）。列为 Should-Fix。
95	
96	**SF7 [Warning, 强共识] "Modality" 术语歧义。**
97	
98	**SF8 [Warning, R1 首提] Reflexion dose-response N=5 统计功效不足。**
99	
100	**SF9 [Warning, 交叉后新增共识] Routing 的 practical value 本身存疑。**
101	- R1-Q4 首提，R2 在交叉回应中称之为 "devastating observation"。3.7% internal-preferred base rate + 96.3% oracle 选择 always-deterministic → always-deterministic 在实际部署中已接近最优。62% tie rate（R2-M1）进一步支持——大多数 episodes routing 选择无差异。
102	- **Action**: §5 Discussion 直接面对这个 implication：不仅 "routing signal 被 death avoidance 主导"，更进一步 "routing 在当前 setup 下几乎不必要"——这本身是一个有价值的诊断性结论。
103	
104	### Minor
105	
106	**m1 [Info, 共识]** 62% tie rate 含义需在正文讨论。
107	
108	**m2 [Info, R1]** Figure 2 caption 报告 Spearman's ρ。
109	
110	**m3 [Info, 强共识]** `webb-2023` 年份需确认（2014 WP vs 2023 journal）。
111	
112	**m4 [Info, R1]** Appendix R 阈值选择缺理论依据。
113	
114	**m5 [Info, R2]** AI assistants disclosure 建议更具体。
115	
116	**m6 [Info, 共识]** Missing references: Altman (1999) CMDP, Mihatsch & Neuneier (2002), Natarajan et al. (2013) noisy label learning。
117	
118	**m7 [Info, R1]** Table 1 weighting scheme（episode-weighted vs task-weighted）需明确。
119	
120	---
121	
122	## Questions（需要作者澄清）
123	
124	**Q1.** [R1-Q1, R2-W6] DAF 公式假设 Δ_nd 不随 P 变化——是否在 P≠100 的 ScienceWorld 变体上做过实际验证？Appendix K 是数学推导还是实际实验？
125	
126	**Q2.** [R1-Q2, R2-Q4, 强共识] 105 internal deaths 全来自 `focus on [object]` 误用——death avoidance 是否等价于 single-action bug avoidance？Grounding ablation 降至 29%，residual gap ≥12pp。如果修复该 pattern，death dominance 是否消失？
127	
128	**Q3.** [R2-Q2, SF9] 62% tie rate + 3.7% internal-preferred base rate → routing 在大多数情况下无差异，always-deterministic 接近最优。论文如何看待这一 observation 对 routing 价值的影响？
129	
130	**Q4.** [R1-N3, 强共识] Router near-chance accuracy 是因为 death signal 本质上不是 step-level 的，还是因为 episode-level labels 投射到 steps 时 ~88% noise/uninformative rate？是否考虑过 death-proximal labeling（只用 death event 附近 steps 训练）？
131	
132	**Q5.** [R1-Q5] Llama cross-model replication 的完整 DAF 是多少？"intact" 太模糊，需要具体数字。
133	
134	**Q6.** [R2-Q3] SCI=0.2147 但 top-3 task types 占 39.8% total death-rate differential——death dominance 是 task-type specific 还是 environment-wide？
135	
136	---
137	
138	## Missing References
139	
140	- **Altman, E. (1999). Constrained Markov Decision Processes.** Death avoidance 作为 implicit constraint 的理论对应。[R2, R1 同意]
141	- **Mihatsch & Neuneier (2002). Risk-sensitive RL.** 与 catastrophic failure avoidance 直接相关。[R2, R1 同意]
142	- **Natarajan et al. (2013). Learning with Noisy Labels.** 为 ~88% uninformative label rate 下的 router near-chance accuracy 提供理论 grounding。[R1, R2 同意]
143	
144	---
145	
146	## External Review (Stanford Agentic Reviewer)
147	
148	**状态**: 已跳过（用户选择不提交）。
149	
150	---
151	
152	## Visual Layout Check（非评分项）
153	
154	**状态**: 超时（elapsed 727s）。无排版审查结果。
155	
156	**基于 PDF 阅读的基本格式确认**:
157	- ✅ 正文 8 页（§1-§6 在 p1-p8），符合 ≤8 页要求
158	- ✅ Limitations（p8-9），具体且坦诚
159	- ✅ Ethics Statement（p9）
160	- ✅ Double-blind: "Anonymous ACL submission"
161	- ✅ ACL 模板 + [review] option
162	- ✅ Figures/Tables 位置合理
163	- ⚠️ webb-2023 年份需确认
164	
165	---
166	
167	## Reviewer Consensus（交叉回应后最终状态）
168	
169	### 完全收敛
170	| 议题 | R1 | R2 | 状态 |
171	|------|----|----|------|
172	| DAF headline framing (MF1) | Critical | Critical | ✅ 强共识 |
173	| K=11 cluster bootstrap (MF4) | Critical | Agrees (critical-but-mitigated) | ✅ 共识 |
174	| Episode→step noise (MF5) | Critical | Agrees ("更有说服力") | ✅ 强共识 |
175	| Framing tension (MF3) | Agrees | Critical | ✅ 强共识 |
176	| Cross-env overclaimed (SF1) | Should-Fix | Critical→Should-Fix | ✅ 共识 |
177	| Routing practical value (SF9) | Q4 ("devastating") | Agrees | ✅ 强共识（交叉后新增） |
178	| **Excitement** | **3.5→3.0** | **2.5→3.0** | **✅ 收敛至 3.0** |
179	| Soundness | 3.5 | 3.5 | ✅ 一致 |
180	| Reproducibility | 4.5 | 4 | ✅ 基本一致 |
181	
182	### 残余分歧
183	| 议题 | R1 | R2 | 差异 |
184	|------|----|----|------|
185	| **Overall Score** | **3.5** (Borderline Conference) | **3.0** (Findings) | **0.5 gap** |
186	| Abstract density (SF6) | REBUT | Should-Fix | 主观分歧 |
187	
188	**0.5 分残余差距根源**: R1 认为 Soundness 3.5 + Reproducibility 4.5 的高分足以在 Excitement 3.0 下支撑 Borderline Conference；R2 认为 Excitement 3.0 的 novelty ceiling 决定了 Findings 更合适。两者均为合理的 reviewer perspective。
189	
190	---
191	
192	## Overall Assessment
193	
194	**Overall Score: 3.0–3.5（Findings 至 Borderline Conference）**
195	
196	**维度汇总（交叉回应后最终值）**:
197	| 维度 | R1 (调整后) | R2 (调整后) | 综合 |
198	|------|------------|------------|------|
199	| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
200	| Excitement | **3.0/5** | **3.0/5** | **3.0/5** |
201	| Reproducibility | 4.5/5 | 4/5 | **4.25/5** |
202	| Clarity | — | 3/5 | **3/5** |
203	
204	**综合评估**:
205	
206	论文问了一个重要且被忽视的诊断性问题，给出了清晰的回答，counterfactual 设计干净，统计分析超过同类水准，robustness checks 全面，negative results 诚实呈现。
207	
208	核心问题：
209	1. **DAF framing 误导**（MF1）——低成本修复
210	2. **Novelty 受限但非 trivial**（MF2）——Excitement 收敛至 3.0，问题定义有价值但答案可预见性限制了 ceiling
211	3. **Framing 不统一**（MF3）——需选择 framework-centric 或 finding-centric 主线
212	4. **K=11 统计推断**（MF4）——通过 non-clustered bootstrap 为主推断来缓解
213	5. **Router diagnostic 受 label noise 污染**（MF5）——需区分 label noise vs fundamental non-learnability
214	6. **Routing 的 practical value 本身存疑**（SF9, 交叉后新增强共识）——3.7% internal-preferred + 62% ties → always-deterministic 几乎最优
215	
216	**Revision 路径**:
217	- **提升至 Conference (3.5-4.0) 的条件**: (1) 选择 framework-centric framing（同时缓解 MF2 和 MF3）；(2) K=11 辩护充分（MF4，低难度）；(3) DAF framing 修正（MF1，低难度）；(4) death-proximal labeling baseline 或 clear attribution（MF5）；(5) §5 直面 routing practical value 问题（SF9）
218	- **如果 MF2 (novelty) 和 SF9 (routing value) 无法有效回应，更可能落在 Findings (3.0)**
219	
220	---
221	
222	## Detailed Comments
223	
224	### Title & Abstract
225	- 标题聚焦 finding 但 Contribution 1 是 framework——需统一（MF3）
226	- Abstract 以 78.9% 为 primary，DAF 降为补充（MF1）
227	- 如采用 framework-centric framing，数字密度可自然降低（SF6）
228	
229	### §1 Introduction
230	- 问题定义清晰，逻辑链通畅
231	- Contributions 列表需重组以匹配选定的 framing 主线
232	
233	### §2 Method
234	- 写作最清晰的部分
235	- Algorithm 1 设计合理
236	- §2.4 Scope of episode-level analysis 段需更强调 episode→step gap implications
237	- DAF 需更 upfront 承认是 derived quantity
238	
239	### §3 Experiments
240	- §3.1 核心实证清晰，但段落结构需修正（78.9% 先于 DAF）
241	- §3.2 Cross-model 缺 Llama DAF 具体数字
242	- §3.3 Agent improvement 有价值；72B DAF=92.4% 说明 scaling 不消除 death dominance
243	- §3.4 Cross-env 过于浅显，需重定位为 boundary probes
244	- §3.5 Oracle degeneracy (96.3% always-det) 和 3.7% internal-preferred 需更突出讨论
245	- §3.6 Router 应明确框架为 negative result；区分 label noise vs signal non-learnability
246	
247	### §4 Related Work
248	- Tool Use / Adaptive Routing 覆盖充分
249	- **Safe RL 需扩展**——补 CMDP, risk-sensitive RL 理论连接
250	
251	### §5 Discussion
252	- "Non-triviality" 论证力度不足（MF2 核心）
253	- "Anatomy of catastrophic failure"——105 deaths 全来自 `focus on`，implications 需更深讨论
254	- **需新增**: routing practical value 的直接讨论（SF9）
255	- **需新增**: pure-strategy vs mixed-strategy gap 估计（SF3）
256	
257	### §6 Conclusion
258	- 严重不足——2 句话，需扩展至 ~0.5 页
259	
260	### Limitations
261	- 覆盖面 adequate，但缺 "P=100 specific" 限制的明确讨论
262	
263	### 格式合规
264	- ✅ 正文 8 页 | ✅ Limitations | ✅ Ethics | ✅ Double-blind | ✅ ACL template
265	- ⚠️ webb-2023 年份 | ⚠️ modality 术语
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cbf3a856-e3d5-410f-b051-243f429fdf25",
  "isSidechain": true,
  "promptId": "c4d4f0db-2852-40ad-afac-040fa0e315f4",
  "agentId": "ac2440b250dcb7b95",
  "type": "user",
  "uuid": "efa02b77-9827-450f-b3c0-f29e7850d915",
  "sourceToolAssistantUUID": "cbf3a856-e3d5-410f-b051-243f429fdf25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-19T20:28:29.305Z_

## Summary of Review Round 21

### Must-Fix Items

1. **MF1: DAF Headline Framing (Critical)** – The 90.4% DAF metric is mathematically dependent on penalty P=100 and is actually an algebraic consequence, not a robust empirical finding. The paper misleadingly presents this as the primary result. Action: Use 78.9% label fraction (penalty-independent) as the primary metric; demote DAF to a derived quantity; discuss edge behavior when Δ_nd<0.

2. **MF2: Limited Novelty (Critical)** – The core finding feels "obvious in hindsight." While the problem definition has value, the finding itself is predictable given the setup. Excitement converged to 3.0/5 after cross-review. Action: Strengthen three angles: (1) contrast prior assumptions in routing literature against empirical results, (2) emphasize why intervention resistance isn't predictable, (3) highlight cross-model δ stability as structural evidence.

3. **MF3: Framing Ambiguity (Critical)** – The paper oscillates between "diagnostic framework" and "empirical finding" positioning. Reviewers note this tension weakens both. Action: Choose one main framing line (framework-centric recommended) and maintain it through title, abstract, contributions, and conclusion.

4. **MF4: Cluster Bootstrap Underpowered (Critical)** – K=11 is below accepted thresholds; p=0.002 is only 4× larger than the minimum reportable value. Partially mitigated by multiple robustness checks. Action: Lead with non-clustered bootstrap; position cluster bootstrap as conservative sensitivity check; add explicit K=11 vs K≥40 discussion.

5. **MF5: Episode→Step Label Projection Noise (Critical)** – The ~88% uninformative label rate when projecting episode-level labels to steps severely damages the router diagnostic value. Two competing interpretations: either signal doesn't exist at step-level, or it's drowned in noise. Action: Clearly separate these interpretations; test death-proximal labeling baseline; or explicitly state failure is label sparsity, not fundamental non-learnability.

### Should-Fix Items

1. **SF1: Cross-environment Probes Overclaimed** – MATH is unfalsifiable; ALFWorld uses different mechanisms. Downgrade language from "cross-domain probes" to "boundary probes/consistency checks."

2. **SF2: Missing Empirical Penalty Verification** – Appendix K shows DAF vs P is math, not experiments. Table 13 reveals correlation is insignificant at P≤25—death dominance is ScienceWorld penalty-regime–specific.

3. **SF3: Pure-Strategy External Validity** – The counterfactual design has limited generalizability to mixed-strategy real-world routing.

4. **SF4: Conclusion Too Brief** – Only 2 sentences; needs expansion to ~0.5 page.

5. **SF5: Safe RL Related Work Shallow** – Missing CMDP (Altman 1999) and risk-sensitive RL theoretical mappings.

6. **SF6: Abstract Overly Dense** – Too many numbers; framework-centric framing would naturally reduce density.

7. **SF9 (New Consensus from Cross-Review): Routing Practical Value Questionable** – 3.7% internal-preference base rate + 96.3% oracle chooses always-deterministic + 62% tie rate = routing is nearly unnecessary. Action: §5 should directly address this—paper's insight isn't just "death avoidance dominates" but "routing is barely needed under these conditions."

### Items Requesting NEW Experiments

- **Death-proximal labeling baseline** (MF5) – Train router only on steps proximal to death events to test whether signal exists but is buried in noise.
- **Empirical penalty verification** (SF2) – Run actual experiments at P≠100 to verify Δ_nd independence claim; Appendix K is purely mathematical.

### Key Patterns Reviewers Found Most Problematic

1. **Misleading headline metrics** – The paper leads with a penalty-dependent statistic (DAF at P=100) instead of the robust one (78.9% label fraction).

2. **Novelty ceiling** – Problem definition is solid and underexplored, but the answer is predictable given the framing. Excitement capped at 3.0/5 even after cross-review convergence.

3. **Framing incoherence** – Oscillating between framework-centric and finding-centric positioning weakens both claims. Unified framing could rescue novelty score.

4. **Statistical inference fragility** – K=11 cluster bootstrap is weak; multiple robustness checks partially compensate but don't fully resolve concerns.

5. **Router failure attribution ambiguity** – Unclear whether step-level signal is fundamentally absent or just buried under ~88% label noise—this distinction matters for generalizability claims.

6. **Routing's irrelevance** – The most damaging insight (new in cross-review consensus): the empirical setup shows routing is nearly optional anyway (always-deterministic is oracle-near optimal), which raises questions about the practical importance of the diagnostic itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efa02b77-9827-450f-b3c0-f29e7850d915",
  "isSidechain": true,
  "agentId": "ac2440b250dcb7b95",
  "requestId": "req_011CbCZLfnfSks4oxjB6DB4E",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "86e44169-6f25-4dba-a60e-886db0044b91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV4rj4JDx6uXoFHVs9rTjN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8169,
      "cache_read_input_tokens": 18776,
      "output_tokens": 1224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8169
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1224,
          "cache_read_input_tokens": 18776,
          "cache_creation_input_tokens": 8169,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8169,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
